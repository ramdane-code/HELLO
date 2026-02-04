import pandas as pd
import numpy as np
import statsmodels.api as sm
from linearmodels.iv import IV2SLS


# --- Chargement ou création des données ---
# Exemple : df = pd.read_csv("tes_données.csv")
# df doit contenir les colonnes : CONS, I, W, P, WP, K, X, G, TAX
try:
	df = pd.read_excel(r"C:\Users\ramda\Desktop\C8EX3.XLS")
except Exception:
	# fallback: create empty DataFrame with expected columns to avoid hard crash
	print("Impossible de lire l'Excel. Vérifiez le chemin ou fournissez un CSV. Création d'un DataFrame vide pour développer.")
	df = pd.DataFrame(columns=["CONS", "I", "W", "P", "WP", "K", "X", "G", "TAX"]) 


# Génération d'une variable de tendance
df["TREND"] = np.arange(len(df)) + 1919

# Somme W + WP
if set(["W", "WP"]).issubset(df.columns):
	df["WT"] = df["W"] + df["WP"]

# --- Régressions OLS (équivalentes à EQUATION ... LS) ---
# EQA: CONS = C + P + P(-1) + W + WP
if "P" in df.columns:
	df["P_lag"] = df["P"].shift(1)
if "X" in df.columns:
	df["X_lag"] = df["X"].shift(1)

# Supprimer les premières lignes contenant des NaN issues des lags
df = df.dropna().reset_index(drop=True)

if not df.empty:
	EQA = sm.OLS(df["CONS"], sm.add_constant(df[["P", "P_lag", "W", "WP"]], has_constant='add')).fit()
	EQB = sm.OLS(df["I"], sm.add_constant(df[["P", "P_lag", "K"]])).fit()
	EQC = sm.OLS(df["W"], sm.add_constant(df[["X", "X_lag", "TREND"]])).fit()

	print(EQA.summary())
	print(EQB.summary())
	print(EQC.summary())

	# --- Prévisions (FORCST) ---
	df["WA"] = EQA.predict(sm.add_constant(df[["P", "P_lag", "W", "WP"]]))
	df["PA"] = EQB.predict(sm.add_constant(df[["P", "P_lag", "K"]]))
	df["XA"] = EQC.predict(sm.add_constant(df[["X", "X_lag", "TREND"]]))

	# --- Autres équations (après prévision) ---
	EQ4 = sm.OLS(df["CONS"], sm.add_constant(df[["PA", "P_lag", "WT"]])).fit()
	EQ5 = sm.OLS(df["I"], sm.add_constant(df[["PA", "P_lag", "K"]])).fit()
	EQ6 = sm.OLS(df["W"], sm.add_constant(df[["XA", "X_lag", "TREND"]])).fit()

	print(EQ4.summary())
	print(EQ5.summary())
	print(EQ6.summary())

	# --- Estimation par TSLS (équivalentes à EQUATION ... TSLS) ---
	# Instruments : P_lag, K, X_lag, WP, TREND, G, TAX
	try:
		eq1 = IV2SLS.from_formula(
			"CONS ~ 1 + P_lag + P + WT + [P ~ P_lag + K + X_lag + WP + TREND + G + TAX]",
			data=df,
		).fit()
		eq2 = IV2SLS.from_formula(
			"I ~ 1 + P_lag + K + P + [P ~ P_lag + K + X_lag + WP + TREND + G + TAX]",
			data=df,
		).fit()
		eq3 = IV2SLS.from_formula(
			"W ~ 1 + X_lag + TREND + X + [W ~ P_lag + K + X_lag + WP + TREND + G + TAX]",
			data=df,
		).fit()

		print(eq1.summary())
		print(eq2.summary())
		print(eq3.summary())
	except Exception as e:
		print("Erreur lors de l'estimation IV/TSLS :", e)
else:
	print("DataFrame vide après dropna : rien à estimer. Vérifiez le chargement des données.")