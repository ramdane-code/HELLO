import argparse
import sys
import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from statsmodels.tsa.seasonal import STL
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

try:
    from pmdarima import auto_arima
except Exception:
    auto_arima = None


def run_adf(series, regression_type):
    """Run ADF and return dict with key results."""
    res = adfuller(series.dropna(), regression=regression_type, autolag='AIC')
    return {
        "regression": regression_type,
        "p_value": res[1],
        "adf_stat": res[0],
        "crit": res[4]
    }


def test_adf_all(series):
    return [run_adf(series, m) for m in ["ct", "c", "nc"]]


def classify(results):
    """
    Interpret ADF results simply:
    - If any test has p_value <= 0.05 => reject unit root => stationary
    - Otherwise => non-stationary
    Return (label, best_result)
    """
    # Prefer the test with lowest p-value
    best = min(results, key=lambda x: x["p_value"]) if results else None
    if best is None:
        return "Inconnu", None
    if best["p_value"] <= 0.05:
        # stationary; indicate the regression type that yielded stationarity
        label_map = {"ct": "Stationnaire (avec tendance)", "c": "Stationnaire (avec constante)", "nc": "Stationnaire (sans constante)"}
        return label_map.get(best["regression"], "Stationnaire"), best
    return "Non stationnaire", best


def make_stationary(series, max_d=5):
    """Iteratively difference until ADF indicates stationarity or max_d reached."""
    d = 0
    cur = series.copy()
    status, res = classify(test_adf_all(cur))
    while status == "Non stationnaire" and d < max_d:
        cur = cur.diff().dropna()
        d += 1
        status, res = classify(test_adf_all(cur))
    return cur, d, status, res


def safe_read_excel(path, sheet_name=0):
    try:
        return pd.read_excel(path, sheet_name=sheet_name)
    except Exception as e:
        raise IOError(f"Impossible de lire le fichier Excel '{path}': {e}")


def plot_series_and_decomposition(series, title_prefix="Série"):
    plt.figure(figsize=(12, 4))
    plt.plot(series)
    plt.title(f"{title_prefix}")
    plt.show()

    # STL decomposition if long enough
    if len(series.dropna()) >= 24:
        try:
            stl = STL(series.dropna(), period=12)
            res = stl.fit()
            res.trend.plot(figsize=(12, 3), title=f"{title_prefix} - Tendance (Trend)")
            plt.show()
            res.seasonal.plot(figsize=(12, 3), title=f"{title_prefix} - Saisonnalité (Seasonal)")
            plt.show()
            res.resid.plot(figsize=(12, 3), title=f"{title_prefix} - Résidus (Residual)")
            plt.show()
        except Exception as e:
            print(f"STL skipped (trop court ou erreur): {e}")
    else:
        print("STL skipped: série trop courte (<24 observations).")


def main():
    parser = argparse.ArgumentParser(description="Tracer série, ADF, ACF et PACF pour une colonne Excel/CSV.")
    parser.add_argument("--file", required=False, default=r"C:\\Users\\ramda\\Desktop\\CorrélogPIB_Alg\\PibpHab.xlsx",
                        help="Chemin vers le fichier Excel ou CSV (par défaut le fichier PibpHab.xlsx sur le Desktop).")
    parser.add_argument("--excel", action="store_true", help="Forcer la lecture Excel (pd.read_excel). Si absent, lit par extension .csv/.xlsx.")
    parser.add_argument("--sheet", default=0, help="Nom ou index de la feuille Excel (défaut 0)")
    parser.add_argument("--col", required=False, help="Nom de la colonne contenant la série (ex: 'Pib')")
    parser.add_argument("--lags", type=int, default=40, help="Nombre de lags pour ACF/PACF")
    args = parser.parse_args()

    path = args.file
    if not os.path.exists(path):
        print(f"Le fichier spécifié n'existe pas: {path}")
        sys.exit(1)

    # Lecture
    if args.excel or path.lower().endswith(('.xls', '.xlsx')):
        df = safe_read_excel(path, sheet_name=args.sheet)
    else:
        try:
            df = pd.read_csv(path)
        except Exception as e:
            raise IOError(f"Impossible de lire le fichier CSV '{path}': {e}")

    # Si colonne non fournie, afficher les colonnes et sortir
    if not args.col:
        print("Colonnes disponibles dans le fichier:")
        print(list(df.columns))
        print("Relancez avec --col NOM_COLONNE pour sélectionner la série.")
        sys.exit(0)

    if args.col not in df.columns:
        print(f"Colonne '{args.col}' non trouvée. Colonnes disponibles: {list(df.columns)}")
        sys.exit(1)

    # Extraire la série numérique
    try:
        series = pd.to_numeric(df[args.col], errors='coerce')
    except Exception as e:
        print(f"Erreur lors de la conversion de la colonne '{args.col}' en numérique: {e}")
        sys.exit(1)

    if series.dropna().empty:
        print("La série sélectionnée est vide après suppression des NaN. Impossible d'analyser.")
        sys.exit(1)

    # 1. Afficher infos de base
    print("\n--- Informations de base ---")
    print(f"Observations totales: {len(series)} | Observations non-null: {series.dropna().shape[0]}")

    # 2. Décomposition et graphiques
    plot_series_and_decomposition(series.dropna(), title_prefix=f"Série '{args.col}'")

    # 3. Moyenne/variance glissante
    plt.figure(figsize=(12, 4))
    plt.plot(series)
    plt.title("Série")
    plt.show()

    plt.figure(figsize=(12, 4))
    plt.plot(series.rolling(12).mean())
    plt.title("Moyenne glissante (12)")
    plt.show()

    plt.figure(figsize=(12, 4))
    plt.plot(series.rolling(12).var())
    plt.title("Variance glissante (12)")
    plt.show()

    # 4. ADF tests
    print("\n--- Tests ADF ---")
    results = test_adf_all(series)
    for r in results:
        print(f"reg={r['regression']}: adf={r['adf_stat']:.4f}, p={r['p_value']:.4f}")

    # Determiner d (nombre de différenciations nécessaires)
    stationary_series, d, status, test = make_stationary(series)
    print("\n------------------------------")
    print(f"Différenciations nécessaires : {d}")
    print(f"Type de série : {status}")
    if test:
        print(f"Meilleur test: regression={test['regression']}, adf={test['adf_stat']:.4f}, p={test['p_value']:.4f}")
    print("------------------------------")

    # 5. ACF / PACF sur la série stationnaire
    # Limiter lags à 50% de la taille de la série (contrainte PACF)
    clean_series = stationary_series.dropna()
    max_lags = min(args.lags, max(1, len(clean_series) // 2 - 1))
    
    plot_acf(clean_series, lags=max_lags)
    plt.show()

    # plot_pacf: préciser method pour éviter warnings/erreurs sur certaines versions
    try:
        plot_pacf(clean_series, lags=max_lags, method='ywm')
    except Exception:
        plot_pacf(clean_series, lags=max_lags)
    plt.show()

    # 6. auto_arima (optionnel)
    if auto_arima is None:
        print("pmdarima non installé: auto_arima ignoré. Pour l'installer: pip install pmdarima")
    else:
        try:
            print("\nRecherche automatique du modèle ARIMA (auto_arima)...")
            model = auto_arima(series.dropna(), seasonal=True, m=12, stepwise=True, trace=True, information_criterion='aic')
            print("\n------------------------------")
            print("MEILLEUR MODELE ARIMA / SARIMA")
            print(model.summary())
            print("------------------------------")
        except Exception as e:
            print(f"auto_arima a échoué: {e}")


if __name__ == '__main__':
    main()
