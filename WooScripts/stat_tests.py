#!/usr/bin/env python3
# stat_tests.py
"""
Mini-bibliothèque de tests statistiques (t & F) avec CLI et export tables (CSV/HTML/LaTeX).
Usage (exemples):
  python stat_tests.py ttest --mode one-sample --data 2.3,2.5,2.1 --mu0 2.0 --alternative two-sided
  python stat_tests.py ttest --mode two-sample --data1 5.1,4.9,5.0 --data2 4.7,4.9,4.8 --equal_var False
  python stat_tests.py ftest --mode variances --data1 2.1,2.3,2.5 --data2 1.9,2.0,1.8
  python stat_tests.py ftest --mode regression --X "1,2;2,3;3,4" --y "2.1,2.9,3.8"
  python stat_tests.py table --dist t --max_df 30 --alphas 0.10,0.05,0.01 --output latex
"""

from typing import Sequence, Tuple, Optional, List, Dict
import argparse
import sys
import numpy as np
import pandas as pd
import scipy.stats as st
import textwrap
import io

# Optional import for nicer regression summary (not strictly required)
try:
    import statsmodels.api as sm  # used only if available for regression summary
    STATS_MODELS_AVAILABLE = True
except Exception:
    STATS_MODELS_AVAILABLE = False

# -------------------------
# Utility functions
# -------------------------
def parse_numeric_list(s: str) -> List[float]:
    """Parse string like '1,2,3' into [1.0, 2.0, 3.0]."""
    if s is None or s.strip() == "":
        return []
    parts = [p.strip() for p in s.split(',') if p.strip() != ""]
    return [float(p) for p in parts]

def warn(msg: str):
    print(f"WARNING: {msg}", file=sys.stderr)

def interpret_p(p_value: float, alpha: float = 0.05) -> str:
    """Return a short interpretation message for p-value given alpha."""
    if np.isnan(p_value):
        return "p-value indéterminée"
    if p_value < alpha:
        return f"p = {p_value:.4g} < {alpha} ⇒ rejet de H0 au seuil {alpha}"
    else:
        return f"p = {p_value:.4g} ≥ {alpha} ⇒ ne pas rejeter H0 au seuil {alpha}"

# -------------------------
# t-tests
# -------------------------
def t_test_one_sample(data: Sequence[float], mu0: float = 0.0, alternative: str = "two-sided") -> Dict:
    """
    One-sample t-test.
    alternative: 'two-sided', 'greater' (mean > mu0), 'less' (mean < mu0)
    Returns dict with t_stat, df, p_value (one- or two-sided accordingly), mean, sd, n
    """
    data = np.asarray(data, dtype=float)
    n = data.size
    if n < 2:
        raise ValueError("Au moins 2 observations requises pour un t-test (n >= 2).")
    mean = data.mean()
    sd = data.std(ddof=1)
    if sd == 0:
        warn("Écarts-types nuls (variance 0) — le test t n'est pas applicable.")
        t_stat = np.nan
        p = np.nan
    else:
        se = sd / np.sqrt(n)
        t_stat = (mean - mu0) / se
        df = n - 1
        if alternative == "two-sided":
            p = 2.0 * st.t.sf(abs(t_stat), df)
        elif alternative == "greater":
            p = st.t.sf(t_stat, df)
        elif alternative == "less":
            p = st.t.cdf(t_stat, df)
        else:
            raise ValueError("alternative doit être 'two-sided', 'greater' ou 'less'")
    return {'test': 'one-sample t', 'alternative': alternative, 't_stat': t_stat,
            'df': n-1, 'p_value': p, 'mean': mean, 'sd': sd, 'n': n}

def t_test_two_sample(x: Sequence[float], y: Sequence[float], equal_var: bool = True,
                      alternative: str = "two-sided") -> Dict:
    """
    Two-sample t-test (independent samples).
    equal_var=True -> pooled Student t-test; False -> Welch's t-test.
    alternative: 'two-sided', 'greater' (mean_x > mean_y), 'less'
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    nx, ny = x.size, y.size
    if nx < 2 or ny < 2:
        raise ValueError("Chaque échantillon doit avoir au moins 2 observations.")
    mx, my = x.mean(), y.mean()
    sx2, sy2 = x.var(ddof=1), y.var(ddof=1)
    if sx2 == 0 and sy2 == 0:
        warn("Les deux échantillons ont variance nulle.")
        t_stat = np.nan; df = np.nan; p = np.nan
    else:
        if equal_var:
            pooled_var = ((nx - 1)*sx2 + (ny - 1)*sy2) / (nx + ny - 2)
            se = np.sqrt(pooled_var * (1.0/nx + 1.0/ny))
            t_stat = (mx - my) / se
            df = nx + ny - 2
        else:
            se = np.sqrt(sx2/nx + sy2/ny)
            t_stat = (mx - my) / se
            # Welch-Satterthwaite approximation
            num = (sx2/nx + sy2/ny)**2
            den = ((sx2/nx)**2) / (nx - 1) + ((sy2/ny)**2) / (ny - 1)
            df = num / den
        if alternative == "two-sided":
            p = 2.0 * st.t.sf(abs(t_stat), df)
        elif alternative == "greater":
            p = st.t.sf(t_stat, df)
        elif alternative == "less":
            p = st.t.cdf(t_stat, df)
        else:
            raise ValueError("alternative doit être 'two-sided', 'greater' ou 'less'")
    return {'test': 'two-sample t', 'alternative': alternative, 'equal_var': equal_var,
            't_stat': t_stat, 'df': df, 'p_value': p,
            'mx': mx, 'my': my, 'sx2': sx2, 'sy2': sy2, 'nx': nx, 'ny': ny}

def t_test_paired(x: Sequence[float], y: Sequence[float], alternative: str = "two-sided") -> Dict:
    """
    Paired t-test: perform t-test on differences x - y.
    alternative: 'two-sided', 'greater' (mean_diff > 0), 'less'
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if x.size != y.size:
        raise ValueError("Pour le t apparié, x et y doivent avoir même taille.")
    diff = x - y
    return t_test_one_sample(diff, mu0=0.0, alternative=alternative)

# -------------------------
# F-tests
# -------------------------
def f_test_variances(x: Sequence[float], y: Sequence[float], alternative: str = "two-sided") -> Dict:
    """
    Classical F-test for equality of variances.
    By convention F = sx2 / sy2 (df1 = nx-1, df2 = ny-1).
    alternative: 'two-sided', 'greater' (var_x > var_y), 'less'
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    nx, ny = x.size, y.size
    if nx < 2 or ny < 2:
        raise ValueError("Chaque échantillon doit avoir au moins 2 observations.")
    sx2 = x.var(ddof=1)
    sy2 = y.var(ddof=1)
    df1, df2 = nx - 1, ny - 1
    if sy2 == 0:
        warn("Variance du second échantillon = 0 -> F infini ou indéterminé.")
    F = sx2 / sy2 if sy2 != 0 else np.inf
    if alternative == 'greater':
        p = st.f.sf(F, df1, df2)
    elif alternative == 'less':
        p = st.f.cdf(F, df1, df2)
    elif alternative == 'two-sided':
        # two-sided approximate: double the smaller tail
        if F >= 1:
            p = 2.0 * st.f.sf(F, df1, df2)
        else:
            p = 2.0 * st.f.cdf(F, df1, df2)
        p = min(p, 1.0)
    else:
        raise ValueError("alternative doit être 'two-sided','greater' ou 'less'")
    return {'test': 'F variances', 'alternative': alternative, 'F': F,
            'df1': df1, 'df2': df2, 'p_value': p, 'sx2': sx2, 'sy2': sy2,
            'nx': nx, 'ny': ny}

def regression_f_test(X: np.ndarray, y: np.ndarray) -> Dict:
    """
    Global F-test for OLS regression:
      H0: all slope coefficients (excluding intercept) = 0
    X: matrix (n x k) WITHOUT intercept column. The function will add an intercept.
    Returns F_stat, df_model(k), df_resid(n-k-1), p_value, R2, beta_hat
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    n = y.size
    if X.ndim == 1:
        X = X.reshape(-1, 1)
    k = X.shape[1]
    if n <= k:
        raise ValueError("Nombre d'observations trop petit pour estimer le modèle (n > k requise).")
    Xc = np.column_stack([np.ones(n), X])
    # OLS via normal equations
    beta_hat, *_ = np.linalg.lstsq(Xc, y, rcond=None)
    y_hat = Xc.dot(beta_hat)
    resid = y - y_hat
    ssr = ((y_hat - y.mean())**2).sum()
    sse = (resid**2).sum()
    sst = ((y - y.mean())**2).sum()
    R2 = ssr / sst if sst != 0 else 0.0
    df_model = k
    df_resid = n - k - 1
    if df_resid <= 0:
        raise ValueError("Degrés de liberté résiduels <= 0.")
    if (1.0 - R2) == 0:
        F_stat = np.inf
    else:
        F_stat = (R2 / df_model) / ((1.0 - R2) / df_resid)
    p_value = st.f.sf(F_stat, df_model, df_resid)
    return {'test': 'F regression', 'F_stat': F_stat, 'df_model': df_model,
            'df_resid': df_resid, 'p_value': p_value, 'R2': R2, 'beta_hat': beta_hat,
            'n': n, 'k': k}

# -------------------------
# Critical value tables
# -------------------------
def t_critical_table(df_list: Sequence[int], alphas_two_sided: Sequence[float]) -> pd.DataFrame:
    rows = []
    for df in df_list:
        row = {'df': int(df)}
        for a in alphas_two_sided:
            row[f'alpha={a} (two-sided)'] = st.t.ppf(1.0 - a/2.0, df)
        rows.append(row)
    return pd.DataFrame(rows)

def f_critical_table(df1_list: Sequence[int], df2_list: Sequence[int], alphas: Sequence[float]) -> pd.DataFrame:
    rows = []
    for df1 in df1_list:
        for df2 in df2_list:
            row = {'df1': int(df1), 'df2': int(df2)}
            for a in alphas:
                row[f'alpha={a}'] = st.f.ppf(1.0 - a, df1, df2)
            rows.append(row)
    return pd.DataFrame(rows)

# -------------------------
# Export helpers
# -------------------------
def export_dataframe(df: pd.DataFrame, output_format: str = "csv") -> str:
    """
    Return the content string in requested format. Supported: 'csv', 'html', 'latex'.
    """
    output_format = output_format.lower()
    buf = io.StringIO()
    if output_format == "csv":
        df.to_csv(buf, index=False)
        return buf.getvalue()
    elif output_format == "html":
        return df.to_html(index=False, border=0)
    elif output_format in ("latex", "tex"):
        try:
            return df.to_latex(index=False, float_format="%.6g")
        except Exception:
            # fallback: simple LaTeX tabular
            return df.to_string(index=False)
    else:
        raise ValueError("Format de sortie non supporté (csv|html|latex).")

# -------------------------
# CLI
# -------------------------
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="stat_tests.py — tests t & F + génération de tables critiques (CSV/HTML/LaTeX).",
        formatter_class=argparse.RawTextHelpFormatter
    )
    sub = p.add_subparsers(dest='command', required=True, help="Commande principale")

    # ttest command
    p_t = sub.add_parser('ttest', help="Executer un test t (one-sample, two-sample, paired).")
    p_t.add_argument('--mode', choices=['one-sample','two-sample','paired'], required=True,
                     help="Mode de t-test.")
    p_t.add_argument('--data', type=str, default=None,
                     help="Données pour one-sample ou pour paired (format: 'x1,x2,...').")
    p_t.add_argument('--data1', type=str, default=None, help="Premier échantillon (two-sample).")
    p_t.add_argument('--data2', type=str, default=None, help="Second échantillon (two-sample).")
    p_t.add_argument('--mu0', type=float, default=0.0, help="Valeur hypothèse nulle pour one-sample.")
    p_t.add_argument('--equal_var', action='store_true', help="Pour two-sample: utiliser Student pooled (default: Welch).")
    p_t.add_argument('--alternative', choices=['two-sided','greater','less'], default='two-sided',
                     help="Type d'alternative. 'greater' means mean > mu0 or mean_x > mean_y.")
    p_t.add_argument('--alpha', type=float, default=0.05, help="Niveau pour interprétation (default 0.05).")
    p_t.add_argument('--output', choices=['text','csv','html','latex'], default='text',
                     help="Format de sortie pour résultats/tab. 'text' affiche à l'écran.")

    # ftest command
    p_f = sub.add_parser('ftest', help="Executer un test F.")
    p_f.add_argument('--mode', choices=['variances','regression'], required=True,
                     help="variances: comparer deux variances; regression: F global d'une OLS.")
    p_f.add_argument('--data1', type=str, default=None, help="Premier échantillon (variances).")
    p_f.add_argument('--data2', type=str, default=None, help="Second échantillon (variances).")
    p_f.add_argument('--X', type=str, default=None, help="Matrice X pour regression; lignes séparées par ';', colonnes par ','.")
    p_f.add_argument('--y', type=str, default=None, help="Vecteur y pour regression (format 'v1,v2,...').")
    p_f.add_argument('--alternative', choices=['two-sided','greater','less'], default='two-sided',
                     help="Pour variances: 'greater' means var_x > var_y.")
    p_f.add_argument('--alpha', type=float, default=0.05, help="Niveau pour interprétation.")
    p_f.add_argument('--output', choices=['text','csv','html','latex'], default='text',
                     help="Format de sortie pour résultats/tab. 'text' affiche à l'écran.")

    # table command
    p_tab = sub.add_parser('table', help="Générer tables critiques t ou F.")
    p_tab.add_argument('--dist', choices=['t','f'], required=True, help="Distribution: t ou f.")
    p_tab.add_argument('--max_df', type=int, default=30, help="max df pour t (1..max_df).")
    p_tab.add_argument('--df1_list', type=str, default="1,2,3,5,10", help="Liste df1 pour F (csv).")
    p_tab.add_argument('--df2_list', type=str, default="5,10,20,50", help="Liste df2 pour F (csv).")
    p_tab.add_argument('--alphas', type=str, default="0.10,0.05,0.01", help="Niveaux alpha (csv).")
    p_tab.add_argument('--output', choices=['csv','html','latex','text'], default='text', help="Format de sortie.")

    return p

def cli_main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == 'ttest':
        if args.mode == 'one-sample':
            data = parse_numeric_list(args.data)
            if len(data) == 0:
                parser.error("--data est requis pour one-sample")
            res = t_test_one_sample(data, mu0=args.mu0, alternative=args.alternative)
            if args.output == 'text':
                print("One-sample t-test")
                print(f"n = {res['n']}, mean = {res['mean']:.6g}, sd = {res['sd']:.6g}")
                print(f"t = {res['t_stat']:.6g}, df = {res['df']}")
                print(interpret_p(res['p_value'], args.alpha))
            else:
                df = pd.DataFrame([res])
                content = export_dataframe(df, args.output)
                print(content)

        elif args.mode == 'two-sample':
            x = parse_numeric_list(args.data1)
            y = parse_numeric_list(args.data2)
            if len(x) == 0 or len(y) == 0:
                parser.error("--data1 et --data2 requis pour two-sample")
            eq = args.equal_var
            res = t_test_two_sample(x, y, equal_var=eq, alternative=args.alternative)
            if args.output == 'text':
                print("Two-sample t-test (independent samples)")
                print(f"n1 = {res['nx']}, mean1 = {res['mx']:.6g}, var1 = {res['sx2']:.6g}")
                print(f"n2 = {res['ny']}, mean2 = {res['my']:.6g}, var2 = {res['sy2']:.6g}")
                print(f"method = {'Student pooled' if eq else 'Welch'}")
                print(f"t = {res['t_stat']:.6g}, df = {res['df']:.4g}")
                print(interpret_p(res['p_value'], args.alpha))
            else:
                df = pd.DataFrame([res])
                print(export_dataframe(df, args.output))

        elif args.mode == 'paired':
            x = parse_numeric_list(args.data)
            y = parse_numeric_list(args.data2) if args.data2 else []
            if len(x) == 0 or len(y) == 0:
                parser.error("--data et --data2 requis pour paired")
            res = t_test_paired(x, y, alternative=args.alternative)
            if args.output == 'text':
                print("Paired t-test")
                print(f"n = {res['n']}, mean diff = {res['mean']:.6g}, sd diff = {res['sd']:.6g}")
                print(f"t = {res['t_stat']:.6g}, df = {res['df']}")
                print(interpret_p(res['p_value'], args.alpha))
            else:
                print(export_dataframe(pd.DataFrame([res]), args.output))

    elif args.command == 'ftest':
        if args.mode == 'variances':
            x = parse_numeric_list(args.data1)
            y = parse_numeric_list(args.data2)
            if len(x) == 0 or len(y) == 0:
                parser.error("--data1 et --data2 requis pour variances")
            res = f_test_variances(x, y, alternative=args.alternative)
            if args.output == 'text':
                print("F-test de comparaison de variances")
                print(f"n1 = {res['nx']}, var1 = {res['sx2']:.6g}")
                print(f"n2 = {res['ny']}, var2 = {res['sy2']:.6g}")
                print(f"F = {res['F']:.6g}, df1 = {res['df1']}, df2 = {res['df2']}")
                print(interpret_p(res['p_value'], args.alpha))
            else:
                print(export_dataframe(pd.DataFrame([res]), args.output))

        elif args.mode == 'regression':
            if args.X is None or args.y is None:
                parser.error("--X et --y requis pour regression")
            # parse X: "a,b;c,d;..." -> rows separated by ';', cols by ','
            rows = [r.strip() for r in args.X.split(';') if r.strip() != ""]
            X_list = [parse_numeric_list(r) for r in rows]
            X = np.array(X_list)
            y = np.array(parse_numeric_list(args.y))
            if X.shape[0] != y.size:
                parser.error("Nombre de lignes de X doit être égal à la longueur de y.")
            res = regression_f_test(X, y)
            if args.output == 'text':
                print("Regression OLS — F test global")
                print(f"n = {res['n']}, k = {res['k']}")
                print(f"R2 = {res['R2']:.6g}")
                print(f"F = {res['F_stat']:.6g}, df_model = {res['df_model']}, df_resid = {res['df_resid']}")
                print(interpret_p(res['p_value'], args.alpha))
                if STATS_MODELS_AVAILABLE:
                    # optional detailed summary using statsmodels
                    Xc = np.column_stack([np.ones(res['n']), X])
                    model = sm.OLS(y, Xc).fit()
                    print("\n--- Résumé OLS (statsmodels) ---")
                    print(model.summary())
            else:
                print(export_dataframe(pd.DataFrame([res]), args.output))

    elif args.command == 'table':
        alphas = [float(a) for a in args.alphas.split(',') if a.strip() != ""]
        if args.dist == 't':
            max_df = int(args.max_df)
            df_list = list(range(1, max_df+1))
            df = t_critical_table(df_list, alphas)
            if args.output == 'text':
                print(df.to_string(index=False))
            else:
                print(export_dataframe(df, args.output))
        elif args.dist == 'f':
            df1_list = [int(i) for i in args.df1_list.split(',') if i.strip() != ""]
            df2_list = [int(i) for i in args.df2_list.split(',') if i.strip() != ""]
            df = f_critical_table(df1_list, df2_list, alphas)
            if args.output == 'text':
                print(df.to_string(index=False))
            else:
                print(export_dataframe(df, args.output))
    else:
        parser.error("Commande inconnue.")

# -------------------------
# Module-level precautions / doc example
# -------------------------
MODULE_PRECAUTIONS = textwrap.dedent("""
Precautions d'utilisation (incluses dans le module) :
- Hypothèse de normalité : t et F supposent populations normales. Pour petits échantillons (n < ~30),
  vérifier normalité (ex : Shapiro-Wilk) avant d'interpréter strictement.
- Indépendance : les observations doivent être indépendantes (sauf pour t apparié).
- Homogénéité des variances : Student pooled t-test suppose variances égales ; préférez Welch si doute.
- Sensibilité du test F : très sensible aux écarts de normalité.
- Pour la régression : validité du F dépend de la bonne spécification du modèle OLS (résidus indépendants, homoscedastiques, normalement distribués).
- Toujours rapporter tailles d'effet et intervalles de confiance en sus des p-values.
""")

# -------------------------
# If used as a script
# -------------------------
if __name__ == "__main__":
    # print short header + precautions
    print("stat_tests.py — mini-bibliothèque de tests t et F (CLI + exports).")
    print(MODULE_PRECAUTIONS)
    cli_main()
