import wooldridge as woo
import pandas as pd
import linearmodels as plm
import statsmodels.formula.api as smf

# Script 14.1 : Example-14-2.py(estimateur à effets fixes de rendt Educ dans le tps)
wagepan = woo.dataWoo('wagepan')
wagepan = wagepan.set_index(['nr', 'year'], drop=False)

# FE model estimation:
reg = plm.PanelOLS.from_formula(
	formula='lwage ~ married + union + C(year)* educ + EntityEffects',
	data=wagepan, drop_absorbed=True)
results = reg.fit()

# print regression table:
table = pd.DataFrame({'b': round(results.params, 4),
					'se': round(results.std_errors, 4),
					't': round(results.tstats, 4),
					'pval': round(results.pvalues, 4)})
print(f'table: \n{table}\n')



# Script 14.2 : Example-14-4-1.py (explore structure du panel : affiche nbre d'obs, d'ans, d'individus, détecte var constantes)

wagepan = woo.dataWoo('wagepan')

# print relevant dimensions for panel:
N = wagepan.shape[0]
T = wagepan['year'].drop_duplicates().shape[0]
n = wagepan['nr'].drop_duplicates().shape[0]
print(f'N: {N}\n')
print(f'T: {T}\n')
print(f'n: {n}\n')

# check non-varying variables
# (I) across time and within individuals by calculating individual
# specific variances for each variable:
isv_nr = (wagepan.groupby('nr').var() == 0) # True, if variance is zero

# choose variables where all grouped variances are zero:
noVar_nr = isv_nr.all(axis=0) # which cols are completely True
print(f'isv_nr.columns[noVar_nr]: \n{isv_nr.columns[noVar_nr]}\n')

# (II) across individuals within one point in time for each variable:
isv_t = (wagepan.groupby('year').var() == 0)
noVar_t = isv_t.all(axis=0)
print(f'isv_t.columns[noVar_t]: \n{isv_t.columns[noVar_t]}\n')



# Script 14.3: Example-14-4-2.py (compare 3 modèles: OLS poolé, effets aléatoires (RE) et effets fixes (FE).)

wagepan = woo.dataWoo('wagepan')

# estimate different models:
wagepan = wagepan.set_index(['nr', 'year'], drop=False)
reg_ols = plm.PooledOLS.from_formula(
	formula='lwage ~ educ + black + hisp + exper + I(exper** 2) +'
						'married + union + C(year)', data=wagepan)
results_ols = reg_ols.fit()

reg_re = plm.RandomEffects.from_formula(
	formula='lwage ~ educ + black + hisp + exper + I(exper** 2) +'
						'married + union + C(year)', data=wagepan)
results_re = reg_re.fit()

reg_fe = plm.PanelOLS.from_formula(
	formula='lwage ~ I(exper** 2) + married + union +'
						'C(year) + EntityEffects', data=wagepan)
results_fe = reg_fe.fit()

# print results:
theta_hat = results_re.theta.iloc[0, 0]
print(f'theta_hat: {theta_hat}\n')

table_ols = pd.DataFrame({'b': round(results_ols.params, 4),
						'se': round(results_ols.std_errors, 4),
						't': round(results_ols.tstats, 4),
						'pval': round(results_ols.pvalues, 4)})
print(f'table_ols: \n{table_ols}\n')

table_re = pd.DataFrame({'b': round(results_re.params, 4),
						'se': round(results_re.std_errors, 4),
						't': round(results_re.tstats, 4),
						'pval': round(results_re.pvalues, 4)})
print(f'table_re: \n{table_re}\n')

table_fe = pd.DataFrame({'b': round(results_fe.params, 4),
						'se': round(results_fe.std_errors, 4),
						't': round(results_fe.tstats, 4),
						'pval': round(results_fe.pvalues, 4)})
print(f'table_fe: \n{table_fe}\n')


# Script 14.5: Example-Dummy-CRE-1.py (3 estimation des paramètres FE: reg_we, reg_dum, reg_cre)

wagepan = woo.dataWoo('wagepan')
wagepan['t'] = wagepan['year']
wagepan['entity'] = wagepan['nr']
wagepan = wagepan.set_index(['nr'])

# include group specific means:
wagepan['married_b'] = wagepan.groupby('nr').mean()['married']
wagepan['union_b'] = wagepan.groupby('nr').mean()['union']
wagepan = wagepan.set_index(['year'], append=True)

# estimate FE parameters in 3 different ways:
reg_we = plm.PanelOLS.from_formula(
        formula='lwage ~ married + union + C(t)* educ + EntityEffects',
       drop_absorbed=True, data=wagepan)
results_we = reg_we.fit()

reg_dum = smf.ols(
	formula='lwage ~ married + union + C(t)*educ + C(entity)',
	data=wagepan)
results_dum = reg_dum.fit()

reg_cre = plm.RandomEffects.from_formula(
	formula='lwage ~ married + union + C(t)*educ + married_b + union_b',
	data=wagepan)
results_cre = reg_cre.fit()

#compare to RE estimates:
reg_re = plm.RandomEffects.from_formula(
	formula='lwage ~ married + union + C(t)*educ',
	data=wagepan)
results_re = reg_re.fit()

var_selection = ['married', 'union', 'C(t)[T.1982]:educ']

#print results:
table = pd.DataFrame({'b_we': round(results_we.params[var_selection], 4),
					'b_dum': round(results_dum.params[var_selection], 4),
					'b_cre': round(results_cre.params[var_selection], 4),
					'b_re': round(results_re.params[var_selection], 4)})
print(f'table: \n{table}\n')

###Script 14.6 : Example-CRE-test-RE.py(test validité modèle à effets aléat (RE) à l'aide du modèle à effets aléatoires corrélés (CRE, méthode de Mundlak)) 	

wagepan = woo.dataWoo('wagepan')
wagepan['t'] = wagepan['year']
wagepan['entity'] = wagepan['nr']
wagepan = wagepan.set_index(['nr'])

# include group specific means:
wagepan['married_b'] = wagepan.groupby('nr').mean()['married']
wagepan['union_b'] = wagepan.groupby('nr').mean()['union']
wagepan = wagepan.set_index(['year'], append=True)

# estimate CRE:
reg_cre = plm.RandomEffects.from_formula(
	formula='lwage ~ married + union + C(t)*educ + married_b + union_b',
	data=wagepan)
results_cre = reg_cre.fit()

# RE test as an Wald test on the CRE specific coefficients:
wtest = results_cre.wald_test(formula='married_b = union_b = 0')
print(f'wtest: \n{wtest}\n')

# Script 14.7: Example-CRE-2.py (Modèle CRE pour voir impact de plusieurs var sur lwage)

import linearmodels as plm
wagepan = woo.dataWoo('wagepan')
wagepan['t'] = wagepan['year']
wagepan['entity'] = wagepan['nr']
wagepan = wagepan.set_index(['nr'])

# include group specific means:
wagepan['married_b'] = wagepan.groupby('nr').mean()['married']
wagepan['union_b'] = wagepan.groupby('nr').mean()['union']
wagepan = wagepan.set_index(['year'], append=True)

# estimate CRE paramters:
reg = plm.RandomEffects.from_formula(
	formula='lwage ~ married + union + educ +'
					'black + hisp + married_b + union_b',
	data=wagepan)
results = reg.fit()

# print regression table:
table = pd.DataFrame({'b': round(results.params, 4),
					'se': round(results.std_errors, 4),
					't': round(results.tstats, 4),
					'pval': round(results.pvalues, 4)})
print(f'table: \n{table}\n')

# Script 14.8 : Example-13-9-ClSE.py(modèle en différence 1ère sur données de panel)	

crime4 = woo.dataWoo('crime4')
crime4 = crime4.set_index(['county', 'year'], drop=False)

# estimate FD model:
reg = plm.FirstDifferenceOLS.from_formula(
		formula='np.log(crmrte) ~ year + d83 + d84 + d85 + d86 + d87 +'
							'lprbarr + lprbconv + lprbpris + lavgsen + lpolpc',
		data=crime4)

# regression with standard SE:
results_default = reg.fit()

# regression with "clustered" SE:
results_cluster = reg.fit(cov_type='clustered', cluster_entity=True,
												debiased=False)

# regression with "clustered" SE (small-sample correction):
results_css = reg.fit(cov_type='clustered', cluster_entity=True)

# print results:
table = pd.DataFrame({'b': round(results_default.params, 4),
					'se_default': round(results_default.std_errors, 4),
					'se_cluster': round(results_cluster.std_errors, 4),
					'se_css': round(results_css.std_errors, 4)})
print(f'table: \n{table}\n')