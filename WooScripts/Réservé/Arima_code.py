import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from statsmodels.tsa.seasonal import STL
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

from pmdarima import auto_arima

# -------------------------------------------------------------------
# 1. CHARGEMENT DE LA SERIE PIB
# -------------------------------------------------------------------
file_path = r"C:\Users\ramda\Desktop\CorrélogPIB_Alg\PibpHab.xlsx"
df = pd.read_excel(file_path)
series = df['PibpHab'].astype(float)

# -------------------------------------------------------------------
# 2. DECOMPOSITION STL
# -------------------------------------------------------------------
if len(series.dropna()) >= 24:
    try:
        stl = STL(series, period=12)
        res = stl.fit()

        res.trend.plot(figsize=(12,3), title="Tendance (Trend)")
        plt.show()

        res.seasonal.plot(figsize=(12,3), title="Saisonnalité (Seasonal)")
        plt.show()

        res.resid.plot(figsize=(12,3), title="Résidus (Residual)")
        plt.show()
    except Exception as e:
        print(f"STL échoué: {e}")
else:
    print("STL skipped: série trop courte (<24 observations).")

# -------------------------------------------------------------------
# 3. GRAPHIQUES : SERIE, ROLLING MEAN, ROLLING VAR, ACF, PACF
# -------------------------------------------------------------------

plt.figure(figsize=(12, 4))
plt.plot(series)
plt.title("Série PIB")
plt.show()

plt.figure(figsize=(12, 4))
plt.plot(series.rolling(12).mean())
plt.title("Moyenne glissante (12)")
plt.show()

plt.figure(figsize=(12, 4))
plt.plot(series.rolling(12).var())
plt.title("Variance glissante (12)")
plt.show()

# Limiter lags à 50% de la taille de la série
clean = series.dropna()
max_lags_acf = min(40, max(1, len(clean) // 2 - 1))

plot_acf(clean, lags=max_lags_acf)
plt.show()

plot_pacf(clean, lags=max_lags_acf)
plt.show()

# -------------------------------------------------------------------
# 4. FONCTIONS ADF
# -------------------------------------------------------------------
def run_adf(series, regression_type):
    result = adfuller(series.dropna(), regression=regression_type, autolag='AIC')
    return {
        "regression": regression_type,
        "p_value": result[1],
        "adf_stat": result[0],
        "crit": result[4]
    }

def test_adf_all(series):
    return [run_adf(series, m) for m in ["ct", "c", "n"]]

def classify(results):
    for r in results:
        if r["p_value"] <= 0.05:
            if r["regression"] == "ct": return "TS", r
            if r["regression"] == "c":  return "DS", r
            if r["regression"] == "n": return "Stationnaire", r
    return "Non stationnaire", None

def make_stationary(series):
    d = 0
    cur = series.copy()

    status, res = classify(test_adf_all(cur))

    while status == "Non stationnaire":
        cur = cur.diff().dropna()
        d += 1
        status, res = classify(test_adf_all(cur))

    return cur, d, status, res

# -------------------------------------------------------------------
# 5. STATIONNARISATION
# -------------------------------------------------------------------
stationary_series, d, status, test = make_stationary(series)

print("\n------------------------------")
print("Différenciations nécessaires :", d)
print("Type de série :", status)
print("Modèle retenu :", test["regression"])
print("ADF stat :", test["adf_stat"])
print("p-value :", test["p_value"])
print("------------------------------")

plt.plot(stationary_series)
plt.title("Série stationnaire")
plt.show()

# Limiter lags à 50% de la taille de la série stationnaire
clean_stat = stationary_series.dropna()
max_lags_stat = min(40, max(1, len(clean_stat) // 2 - 1))

plot_acf(clean_stat, lags=max_lags_stat)
plt.show()

plot_pacf(clean_stat, lags=max_lags_stat)
plt.show()

# -------------------------------------------------------------------
# 6. SELECTION AUTOMATIQUE (p,d,q) et (P,D,Q)
# -------------------------------------------------------------------
print("\nRecherche automatique du modèle ARIMA...")

try:
    model = auto_arima(
        series.dropna(),
        seasonal=True,
        m=12,               # période saisonnière (adapter si nécessaire)
        stepwise=True,
        trace=True,
        information_criterion='aic'
    )

    print("\n------------------------------")
    print("MEILLEUR MODELE ARIMA / SARIMA")
    print(model.summary())
    print("------------------------------")
except Exception as e:
    print(f"auto_arima a échoué: {e}")
    print("Vérifiez que la série est assez longue et n'a pas trop de NaN.")
