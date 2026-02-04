import wooldridge as woo
import numpy as np
import pandas as pd
import linearmodels.iv as iv
import statsmodels.formula.api as smf
import scipy.stats as stats

# Script 15.1: Example-15-1.py (variables instrumentales pour estimer rendt de l'éduc des femmes)
mroz = woo.dataWoo('mroz')

# restrict to non-missing wage observations:
mroz = mroz.dropna(subset=['lwage'])

cov_yz = np.cov(mroz['lwage'], mroz['fatheduc'])[1, 0]
cov_xy = np.cov(mroz['educ'], mroz['lwage'])[1, 0]
cov_xz = np.cov(mroz['educ'], mroz['fatheduc'])[1, 0]
var_x = np.var(mroz['educ'], ddof=1)
x_bar = np.mean(mroz['educ'])
y_bar = np.mean(mroz['lwage'])

# OLS slope parameter manually:
b_ols_man = cov_xy / var_x
print(f'b_ols_man: {b_ols_man}\n')

# IV slope parameter manually:
b_iv_man = cov_yz / cov_xz
print(f'b_iv_man: {b_iv_man}\n')

# OLS automatically:
reg_ols = smf.ols(formula='np.log(wage) ~ educ', data=mroz)
results_ols = reg_ols.fit()

# print regression table:
table_ols = pd.DataFrame({'b': round(results_ols.params, 4),
                        'se': round(results_ols.bse, 4),
                        't': round(results_ols.tvalues, 4),
                        'pval': round(results_ols.pvalues, 4)})
print(f'table_ols: \n{table_ols}\n')

# IV automatically:
reg_iv = iv.IV2SLS.from_formula(formula='np.log(wage) ~ 1 + [educ ~ fatheduc]',
																data=mroz)
results_iv = reg_iv.fit(cov_type='unadjusted', debiased=True)

# print regression table:
table_iv = pd.DataFrame({'b': round(results_iv.params, 4),
                        'se': round(results_iv.std_errors, 4),
                        't': round(results_iv.tstats, 4),
                        'pval': round(results_iv.pvalues, 4)})
print(f'table_iv: \n{table_iv}\n')


### Script 15.2: Example-15-4.py (dummy variables comme variable instrumentale)

card = woo.dataWoo('card')

# checking for relevance with reduced form:
reg_redf = smf.ols(
	formula='educ ~ nearc4 + exper + I(exper** 2) + black + smsa +'
	'south + smsa66 + reg662 + reg663 + reg664 + reg665 + reg666 +'
	'reg667 + reg668 + reg669', data=card)
results_redf = reg_redf.fit()

# print regression table:
table_redf = pd.DataFrame({'b': round(results_redf.params, 4),
                        'se': round(results_redf.bse, 4),
                        't': round(results_redf.tvalues, 4),
                        'pval': round(results_redf.pvalues, 4)})
print(f'table_redf: \n{table_redf}\n')

# OLS:
reg_ols = smf.ols(
	formula='np.log(wage) ~ educ + exper + I(exper** 2) + black + smsa +'
	'south + smsa66 + reg662 + reg663 + reg664 + reg665 +'
	'reg666 + reg667 + reg668 + reg669', data=card)
results_ols = reg_ols.fit()

# print regression table:
table_ols = pd.DataFrame({'b': round(results_ols.params, 4),
                        'se': round(results_ols.bse, 4),
                        't': round(results_ols.tvalues, 4),
                        'pval': round(results_ols.pvalues, 4)})
print(f'table_ols: \n{table_ols}\n')

# IV automatically:
reg_iv = iv.IV2SLS.from_formula(
	formula='np.log(wage)~ 1 + exper + I(exper** 2) + black + smsa + '
				'south + smsa66 + reg662 + reg663 + reg664 + reg665 +'
				'reg666 + reg667 + reg668 + reg669 + [educ ~ nearc4]',
	data=card)
results_iv = reg_iv.fit(cov_type='unadjusted', debiased=True)

# print regression table:
table_iv = pd.DataFrame({'b': round(results_iv.params, 4),
                        'se': round(results_iv.std_errors, 4),
                        't': round(results_iv.tstats, 4),
                        'pval': round(results_iv.pvalues, 4)})
print(f'table_iv: \n{table_iv}\n')


# Script 15.3 : Example-15-5.py (estimation 2SLS en 2 étapes et automatiquement par IV2SLS)                                                                                                          

mroz = woo.dataWoo('mroz')

# restrict to non-missing wage observations:
mroz = mroz.dropna(subset=['lwage'])

# 1st stage (reduced form):
reg_redf = smf.ols(formula='educ ~ exper + I(exper** 2) + motheduc + fatheduc',
									data=mroz)
results_redf = reg_redf.fit()
mroz['educ_fitted'] = results_redf.fittedvalues

# print regression table:
table_redf = pd.DataFrame({'b': round(results_redf.params, 4),
                        'se': round(results_redf.bse, 4),
                        't': round(results_redf.tvalues, 4),
                        'pval': round(results_redf.pvalues, 4)})
print(f'table_redf: \n{table_redf}\n')

# 2nd stage:
reg_secstg = smf.ols(formula='np.log(wage) ~ educ_fitted + exper + I(exper** 2)',
										     data=mroz)
results_secstg = reg_secstg.fit()

# print regression table:
table_secstg = pd.DataFrame({'b': round(results_secstg.params, 4),
                            'se': round(results_secstg.bse, 4),
                            't': round(results_secstg.tvalues, 4),
                            'pval': round(results_secstg.pvalues, 4)})
print(f'table_secstg: \n{table_secstg}\n')

# IV automatically:
reg_iv = iv.IV2SLS.from_formula(
	formula='np.log(wage) ~ 1 + exper + I(exper** 2) +'
						'[educ ~ motheduc + fatheduc]',
	data=mroz)
results_iv = reg_iv.fit(cov_type='unadjusted', debiased=True)

# print regression table:
table_iv = pd.DataFrame({'b': round(results_iv.params, 4),
                        'se': round(results_iv.std_errors, 4),
                        't': round(results_iv.tstats, 4),
                        'pval': round(results_iv.pvalues, 4)})
print(f'table_iv: \n{table_iv}\n')

# Script 15.4 : Example-15-7.py (estimation rendt de l'éducation des femmes mariées par l'approche de la fonction de contrôle)                                                                                                         

mroz = woo.dataWoo('mroz')

# restrict to non-missing wage observations:
mroz = mroz.dropna(subset=['lwage'])

# 1st stage (reduced form):
reg_redf = smf.ols(formula='educ ~ exper + I(exper** 2) + motheduc + fatheduc',
									data=mroz)
results_redf = reg_redf.fit()
mroz['resid'] = results_redf.resid

# 2nd stage:
reg_secstg = smf.ols(formula='np.log(wage)~ resid + educ + exper + I(exper** 2)',
										data=mroz)
results_secstg = reg_secstg.fit()

# print regression table:
table_secstg = pd.DataFrame({'b': round(results_secstg.params, 4),
                            'se': round(results_secstg.bse, 4),
                            't': round(results_secstg.tvalues, 4),
                            'pval': round(results_secstg.pvalues, 4)})
print(f'table_secstg: \n{table_secstg}\n')



# Script 15.5 : Example-15-8.py (estimation IV2SLS et tests : R2, t-stat, khi2)                                                                                                          

mroz = woo.dataWoo('mroz')

# restrict to non-missing wage observations:
mroz = mroz.dropna(subset=['lwage'])

# IV regression:
reg_iv = iv.IV2SLS.from_formula(formula='np.log(wage) ~ 1 + exper + I(exper** 2) +'
														'[educ ~ motheduc + fatheduc]', data=mroz)
results_iv = reg_iv.fit(cov_type='unadjusted', debiased=True)

# print regression table:
table_iv = pd.DataFrame({'b': round(results_iv.params, 4),
                        'se': round(results_iv.std_errors, 4),
                        't': round(results_iv.tstats, 4),
                        'pval': round(results_iv.pvalues, 4)})
print(f'table_iv: \n{table_iv}\n')

# auxiliary regression:
mroz['resid_iv'] = results_iv.resids
reg_aux = smf.ols(formula='resid_iv ~ exper + I(exper** 2) + motheduc + fatheduc',
									data=mroz)
results_aux = reg_aux.fit()

# calculations for test:
r2 = results_aux.rsquared
n = results_aux.nobs
teststat = n * r2
pval = 1 - stats.chi2.cdf(teststat, 1)

print(f'r2: {r2}\n')
print(f'n: {n}\n')
print(f'teststat: {teststat}\n')
print(f'pval: {pval}\n')



# Script 15.6 : Example-15-10.py(régression IV sur différences 1ère pour évaluer effet d'une subvention )
import wooldridge as woo
import numpy as np
import pandas as pd
import linearmodels.iv as iv

# Charger les données
jtrain = woo.dataWoo('jtrain')

# Sélectionner uniquement les années 1987 et 1988
jtrain_87_88 = jtrain[jtrain['year'].isin([1987, 1988])].copy()
jtrain_87_88 = jtrain_87_88.set_index(['fcode', 'year'])

# Calculer les différences premières pour chaque entreprise
jtrain_87_88 = jtrain_87_88.sort_index()
jtrain_87_88['lscrap_diff1'] = jtrain_87_88.groupby('fcode')['lscrap'].diff()
jtrain_87_88['hrsemp_diff1'] = jtrain_87_88.groupby('fcode')['hrsemp'].diff()
jtrain_87_88['grant_diff1'] = jtrain_87_88.groupby('fcode')['grant'].diff()

# Retirer les lignes avec NaN (première année de chaque groupe)
jtrain_87_88_clean = jtrain_87_88.dropna(subset=['lscrap_diff1', 'hrsemp_diff1', 'grant_diff1'])

# Régression IV sur les différences premières
reg_iv = iv.IV2SLS.from_formula(
    formula='lscrap_diff1 ~ 1 + [hrsemp_diff1 ~ grant_diff1]',
    data=jtrain_87_88_clean
)
results_iv = reg_iv.fit(cov_type='unadjusted', debiased=True)

# Affichage des résultats
table_iv = pd.DataFrame({
    'b': round(results_iv.params, 4),
    'se': round(results_iv.std_errors, 4),
    't': round(results_iv.tstats, 4),
    'pval': round(results_iv.pvalues, 4)
})
print(f'table_iv: \n{table_iv}\n')