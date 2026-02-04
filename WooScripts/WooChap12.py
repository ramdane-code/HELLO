import wooldridge as woo
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import numpy as np
import patsy as pt
import yfinance as yf

# Script 12.1 : Example-12-2-Static.py(Vérifier présence d'autocorrélation résidus dans  régression courbe de Phillips statique)
phillips = woo.dataWoo('phillips')
T = len(phillips)

# define yearly time series beginning in 1948:
date_range = pd.date_range(start='1948', periods=T, freq='YE')
phillips.index = date_range.year

# estimation of static Phillips curve:
yt96 = (phillips['year'] <= 1996)
reg_s = smf.ols(formula='Q("inf") ~ unem', data=phillips, subset=yt96)
results_s = reg_s.fit()

# residuals and AR(1) test:
phillips['resid_s'] = results_s.resid
phillips['resid_s_lag1'] = phillips['resid_s'].shift(1)
reg = smf.ols(formula='resid_s ~ resid_s_lag1', data=phillips, subset=yt96)
results = reg.fit()

# print regression table:
table = pd.DataFrame({'b': round(results.params, 4),
					'se': round(results.bse, 4),
					't': round(results.tvalues, 4),
					'pval': round(results.pvalues, 4)})
print(f'table: \n{table}\n')



# Script 12.2 : Example-12-2-ExpAug.py (courbe de Phillips espérée augmentée (expected-augmented Phillips curve)) 	

phillips = woo.dataWoo('phillips')
T = len(phillips)

# define yearly time series beginning in 1948:
date_range = pd.date_range(start='1948', periods=T, freq='YE')
phillips.index = date_range.year

# estimation of expectations-augmented Phillips curve:
yt96 = (phillips['year'] <= 1996)
phillips['inf_diff1'] = phillips['inf'].diff()
reg_ea = smf.ols(formula='inf_diff1 ~ unem', data=phillips, subset=yt96)
results_ea = reg_ea.fit()
phillips['resid_ea'] = results_ea.resid
phillips['resid_ea_lag1'] = phillips['resid_ea'].shift(1)
reg = smf.ols(formula='resid_ea ~ resid_ea_lag1', data=phillips, subset=yt96)
results = reg.fit()

# print regression table:
table = pd.DataFrame({'b': round(results.params, 4),
					'se': round(results.bse, 4),
					't': round(results.tvalues, 4),
					'pval': round(results.pvalues, 4)})
print(f'table: \n{table}\n')

# Script 12.2 : Example-12-2-ExpAug.py**: courbe de Phillips espérée augmentée (expected-augmented Phillips curve)	

phillips = woo.dataWoo('phillips')
T = len(phillips)

# define yearly time series beginning in 1948:
date_range = pd.date_range(start='1948', periods=T, freq='YE')
phillips.index = date_range.year

# estimation of expectations-augmented Phillips curve:
yt96 = (phillips['year'] <= 1996)
phillips['inf_diff1'] = phillips['inf'].diff()
reg_ea = smf.ols(formula='inf_diff1 ~ unem', data=phillips, subset=yt96)
results_ea = reg_ea.fit()
phillips['resid_ea'] = results_ea.resid
phillips['resid_ea_lag1'] = phillips['resid_ea'].shift(1)
reg = smf.ols(formula='resid_ea ~ resid_ea_lag1', data=phillips, subset=yt96)
results = reg.fit()

# print regression table:
table = pd.DataFrame({'b': round(results.params, 4),
					'se': round(results.bse, 4),
					't': round(results.tvalues, 4),
					'pval': round(results.pvalues, 4)})
print(f'table: \n{table}\n')



# Script 12.3: Example-12-4.py(estimer importations de chlorure de baryum et terter la corrélation en série AR(3))

barium = woo.dataWoo('barium')
T = len(barium)

# monthly time series starting Feb. 1978:
barium.index = pd.date_range(start='1978-02', periods=T, freq='M')
reg = smf.ols(formula='np.log(chnimp) ~ np.log(chempi) + np.log(gas) +'
										'np.log(rtwex) + befile6 + affile6 + afdec6',
						data=barium)
results = reg.fit()

# automatic test:
bg_result = sm.stats.diagnostic.acorr_breusch_godfrey(results, nlags=3)
fstat_auto = bg_result[2]
fpval_auto = bg_result[3]
print(f'fstat_auto: {fstat_auto}\n')
print(f'fpval_auto: {fpval_auto}\n')

# pedestrian test:
barium['resid'] = results.resid
barium['resid_lag1'] = barium['resid'].shift(1)
barium['resid_lag2'] = barium['resid'].shift(2)
barium['resid_lag3'] = barium['resid'].shift(3)

reg_manual = smf.ols(formula='resid ~ resid_lag1 + resid_lag2 + resid_lag3 +'
							'np.log(chempi) + np.log(gas) + np.log(rtwex) +'
							'befile6 + affile6 + afdec6', data=barium)
results_manual = reg_manual.fit()

hypotheses = ['resid_lag1 = 0', 'resid_lag2 = 0', 'resid_lag3 = 0']
ftest_manual = results_manual.f_test(hypotheses)
fstat_manual = float(ftest_manual.statistic)
fpval_manual = ftest_manual.pvalue
print(f'fstat_manual: {fstat_manual}\n')
print(f'fpval_manual: {fpval_manual}\n')


# Script 12.3: Example-12-4.py(estimer importations de chlorure de baryum et terter la corrélation en série AR(3))

import statsmodels.formula.api as smf

barium = woo.dataWoo('barium')
T = len(barium)

# monthly time series starting Feb. 1978:
barium.index = pd.date_range(start='1978-02', periods=T, freq='M') # on crée un index de date avant de faire la régression
reg = smf.ols(formula='np.log(chnimp) ~ np.log(chempi) + np.log(gas) +'
										'np.log(rtwex) + befile6 + affile6 + afdec6',
						data=barium)
results = reg.fit()

# automatic test:
bg_result = sm.stats.diagnostic.acorr_breusch_godfrey(results, nlags=3)
fstat_auto = bg_result[2] # le diag a retourné un tuple, on extrait le fstat bg_result[2] 
fpval_auto = bg_result[3] # le diag a retourné un tuple, on extrait le pval bg_result[3]
print(f'fstat_auto: {fstat_auto}\n')
print(f'fpval_auto: {fpval_auto}\n')

# pedestrian test:
barium['resid'] = results.resid
barium['resid_lag1'] = barium['resid'].shift(1) # créer variables décalées pour les résidus 
barium['resid_lag2'] = barium['resid'].shift(2)
barium['resid_lag3'] = barium['resid'].shift(3)

reg_manual = smf.ols(formula='resid ~ resid_lag1 + resid_lag2 + resid_lag3 +'
									'np.log(chempi) + np.log(gas) + np.log(rtwex) +'
									'befile6 + affile6 + afdec6', data=barium)
results_manual = reg_manual.fit()

hypotheses = ['resid_lag1 = 0', 'resid_lag2 = 0', 'resid_lag3 = 0']
ftest_manual = results_manual.f_test(hypotheses)
fstat_manual = float(ftest_manual.statistic)
fpval_manual = ftest_manual.pvalue
print(f'fstat_manual: {fstat_manual}\n')
print(f'fpval_manual: {fpval_manual}\n')


# Script 12.4 : Example-DWtest.py (analyse sur la courbe de Phillips et test DW)	

phillips = woo.dataWoo('phillips')
T = len(phillips)

# define yearly time series beginning in 1948:
date_range = pd.date_range(start='1948', periods=T, freq='Y')
phillips.index = date_range.year

# estimation of both Phillips curve models:
yt96 = (phillips['year'] <= 1996)
phillips['inf_diff1'] = phillips['inf'].diff()
reg_s = smf.ols(formula='Q("inf") ~ unem', data=phillips, subset=yt96)
reg_ea = smf.ols(formula='inf_diff1 ~ unem', data=phillips, subset=yt96)
results_s = reg_s.fit()
results_ea = reg_ea.fit()

# DW tests:
DW_s = sm.stats.stattools.durbin_watson(results_s.resid)
DW_ea = sm.stats.stattools.durbin_watson(results_ea.resid)
print(f'DW_s: {DW_s}\n')
print(f'DW_ea: {DW_ea}\n')

# Script 12.5: Example-12-5.py ((estimation OLS puis GLSAR(feasable General Least Square-FGLS)))

barium = woo.dataWoo('barium')
T = len(barium)

# monthly time series starting Feb. 1978:
barium.index = pd.date_range(start='1978-02', periods=T, freq='ME')

# perform the Cochrane-Orcutt estimation (iterative procedure):
y, X = pt.dmatrices('np.log(chnimp) ~ np.log(chempi) + np.log(gas) +'
					'np.log(rtwex) + befile6 + affile6 + afdec6',
					data=barium, return_type='dataframe')
reg = sm.GLSAR(y, X)
CORC_results = reg.iterative_fit(maxiter=100)
table = pd.DataFrame({'b_CORC': CORC_results.params,
					'se_CORC': CORC_results.bse})
print(f'reg.rho: {reg.rho}\n')



# Script 12.6 : Example-12-1.py(estimer taux d'emploi puis utilisation de différentes formules variance-covariance pour calculer coef de rég et erreurs types)  	

prminwge = woo.dataWoo('prminwge')
T = len(prminwge) 
prminwge.index = pd.date_range(start='1950', periods=T, freq='YE').year

# Ajouter la variable 'time' pour la tendance
prminwge['time'] = prminwge['year'] - 1949

# OLS regression:
reg = smf.ols(formula='np.log(prepop) ~ np.log(mincov) + np.log(prgnp) + np.log(usgnp) + time', data=prminwge)

# results with regular SE:
results_regu = reg.fit()

# print regression table:
table_regu = pd.DataFrame({'b': round(results_regu.params, 4),
                        'se': round(results_regu.bse, 4),
                        't': round(results_regu.tvalues, 4),
                        'pval': round(results_regu.pvalues, 4)})
print(f'table_regu: \n{table_regu}\n')

# results with HAC SE:
results_hac = reg.fit(cov_type='HAC', cov_kwds={'maxlags': 2})

# print regression table:
table_hac = pd.DataFrame({'b': round(results_hac.params, 4),
                        'se': round(results_hac.bse, 4),
                        't': round(results_hac.tvalues, 4),
                        'pval': round(results_hac.pvalues, 4)})
print(f'table_hac: \n{table_hac}\n')


# Script 12.7: Example-12-9.py (modèle ARCH pour rendement des actions)

nyse = woo.dataWoo('nyse')
nyse['ret'] = nyse['return']
nyse['ret_lag1'] = nyse['ret'].shift(1)

# linear regression of model:
reg = smf.ols(formula='ret ~ ret_lag1', data=nyse)
results = reg.fit()

# squared residuals:
nyse['resid_sq'] = results.resid ** 2
nyse['resid_sq_lag1'] = nyse['resid_sq'].shift(1)

# Retirer les lignes avec NaN pour la régression ARCH
nyse_arch = nyse.dropna(subset=['resid_sq', 'resid_sq_lag1'])

# model for squared residuals:
ARCHreg = smf.ols(formula='resid_sq ~ resid_sq_lag1', data=nyse_arch)
results_ARCH = ARCHreg.fit()

# print regression table:
table = pd.DataFrame({
    'b': round(results_ARCH.params, 4),
    'se': round(results_ARCH.bse, 4),
    't': round(results_ARCH.tvalues, 4),
    'pval': round(results_ARCH.pvalues, 4)
})
print(f'table: \n{table}\n')

# Script 12.8: Example-ARCH.py (estimer un modèle ARCH sur les résidus des rendements log de Apple (ne fonctionne pas)) 
# (ne fonctionne pas car yfinance ne supporte pas les données de 2007-2016?)

# Configuration des dates
start_date = '2007-12-31'
end_date = '2016-12-31'

# Téléchargement des données
try:
    AAPL_data = yf.download('AAPL', start=start_date, end=end_date, progress=False)
    
    if AAPL_data.empty:
        raise ValueError("Aucune donnée téléchargée - vérifiez les dates ou la connexion internet")
        
    # Calcul des rendements
    price_col = 'Adj Close' if 'Adj Close' in AAPL_data.columns else 'Close'
    AAPL_data = yf.download('AAPL', start=start_date, end=end_date, progress=False)
    AAPL_data = AAPL_data[price_col].diff()
    AAPL_data['ret_lag1'] = AAPL_data['ret'].shift(1)
    
    # Nettoyage des données pour AR(1)
    AAPL_clean = AAPL_data.dropna(subset=['ret', 'ret_lag1']).copy()
    
    if len(AAPL_clean) < 2:
        raise ValueError("Pas assez d'observations après nettoyage")
    
    # Régression AR(1)
    ar_model = smf.ols(formula='ret ~ ret_lag1', data=AAPL_clean)
    ar_results = ar_model.fit()
    
    # Calcul des résidus au carré pour ARCH
    AAPL_clean['resid_sq'] = ar_results.resid ** 2
    AAPL_clean['resid_sq_lag1'] = AAPL_clean['resid_sq'].shift(1)
    
    # Nettoyage pour modèle ARCH
    AAPL_arch = AAPL_clean.dropna(subset=['resid_sq', 'resid_sq_lag1']).copy()
    
    if len(AAPL_arch) < 2:
        raise ValueError("Pas assez d'observations pour le modèle ARCH")
    
    # Régression ARCH(1)
    arch_model = smf.ols(formula='resid_sq ~ resid_sq_lag1', data=AAPL_arch)
    arch_results = arch_model.fit()
    
    # Affichage des résultats
    results_table = pd.DataFrame({
        'Coefficient': arch_results.params,
        'Std Error': arch_results.bse,
        't-value': arch_results.tvalues,
        'p-value': arch_results.pvalues
    }).round(4)
    
    print("Résultats du modèle ARCH(1):")
    print(results_table)
    
except Exception as e:
    print(f"Une erreur s'est produite: {str(e)}")
    if 'AAPL_data' in locals():
        print(f"Nombre d'observations téléchargées: {len(AAPL_data)}")
        