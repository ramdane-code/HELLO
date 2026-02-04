import wooldridge as woo
import pandas as pd
import statsmodels.formula.api as smf
import numpy as np
import linearmodels as plm


# Script 13.1 : Example-13-2.py (Modèle Pooled cross sections (sections transversales groupées)) 	
cps78_85 = woo.dataWoo('cps78_85')

# OLS results including interaction terms:
reg = smf.ols(formula='lwage ~ y85*(educ+female) + exper +'
							  'I((exper** 2)/100) + union',
						data=cps78_85)
results = reg.fit()

# print regression table:
table = pd.DataFrame({'b': round(results.params, 4),
					'se': round(results.bse, 4),
					't': round(results.tvalues, 4),
					'pval': round(results.pvalues, 4)})
print(f'table: \n{table}\n')



# Script 13.2: Example-13-3-1.py (Procédure Différence des Différences et Estimateur DiD)

kielmc = woo.dataWoo('kielmc')

# separate regressions for 1978 and 1981:
y78 = (kielmc['year'] == 1978)
reg78 = smf.ols(formula='rprice ~ nearinc', data=kielmc, subset=y78)
results78 = reg78.fit()
y81 = (kielmc['year'] == 1981)
reg81 = smf.ols(formula='rprice ~ nearinc', data=kielmc, subset=y81)
results81 = reg81.fit()

# joint regression including an interaction term:
reg_joint = smf.ols(formula='rprice ~ nearinc * C(year)', data=kielmc)
results_joint = reg_joint.fit()

# print regression tables:
table_78 = pd.DataFrame({'b': round(results78.params, 4),
						'se': round(results78.bse, 4),
						't': round(results78.tvalues, 4),
						'pval': round(results78.pvalues, 4)})
print(f'table_78: \n{table_78}\n')

table_81 = pd.DataFrame({'b': round(results81.params, 4),
						'se': round(results81.bse, 4),
						't': round(results81.tvalues, 4),
						'pval': round(results81.pvalues, 4)})
print(f'table_81: \n{table_81}\n')

table_joint = pd.DataFrame({'b': round(results_joint.params, 4),
							'se': round(results_joint.bse, 4),
							't': round(results_joint.tvalues, 4),
							'pval': round(results_joint.pvalues, 4)})
print(f'table_joint: \n{table_joint}\n')



# Script 13.3 : Example-13-3-2.py ((évaluer l'effet de l'implantation d'incinérateur sur les prix des maisons))

kielmc = woo.dataWoo('kielmc')

# difference in difference (DiD):
reg_did = smf.ols(formula='np.log(rprice) ~ nearinc* C(year)', data=kielmc)
results_did = reg_did.fit()

# print regression table:
table_did = pd.DataFrame({'b': round(results_did.params, 4),
						'se': round(results_did.bse, 4),
						't': round(results_did.tvalues, 4),
						'pval': round(results_did.pvalues, 4)})
print(f'table_did: \n{table_did}\n')

# DiD with control variables:
reg_didC = smf.ols(formula='np.log(rprice) ~ nearinc* C(year) + age +'
											'I(age ** 2) + np.log(intst) + np.log(land) +'
											'np.log(area) + rooms + baths',
									data=kielmc)
results_didC = reg_didC.fit()

# print regression table:
table_didC = pd.DataFrame({'b': round(results_didC.params, 4),
						'se': round(results_didC.bse, 4),
						't': round(results_didC.tvalues, 4),
						'pval': round(results_didC.pvalues, 4)})
print(f'table_didC: \n{table_didC}\n')



# Script 13.4: Example-FD.py (1ère différence pour neutraliser effets non observés)

crime2 = woo.dataWoo('crime2')

# create time variable dummy by converting a Boolean variable to an integer:
crime2['t'] = (crime2['year'] == 87).astype(int) # False=0, True=1

# create an index in this balanced data set by combining two arrays:
id_tmp = np.linspace(1, 46, num=46)
crime2['id'] = np.sort(np.concatenate([id_tmp, id_tmp]))

# manually calculate first differences per entity for crmrte and unem:
crime2['crmrte_diff1'] = \
	crime2.sort_values(['id', 'year']).groupby('id')['crmrte'].diff()
crime2['unem_diff1'] = \
	crime2.sort_values(['id', 'year']).groupby('id')['unem'].diff()
var_selection = ['id', 't', 'crimes', 'unem', 'crmrte_diff1', 'unem_diff1']
print(f'crime2[var_selection].head(): \n{crime2[var_selection].head()}\n')

# estimate FD model with statmodels on differenced data:
reg_sm = smf.ols(formula='crmrte_diff1 ~ unem_diff1', data=crime2)
results_sm = reg_sm.fit()

# print results:
table_sm = pd.DataFrame({'b': round(results_sm.params, 4),
						'se': round(results_sm.bse, 4),
						't': round(results_sm.tvalues, 4),
						'pval': round(results_sm.pvalues, 4)})
print(f'table_sm: \n{table_sm}\n')

# estimate FD model with linearmodels:
crime2 = crime2.set_index(['id', 'year'])
reg_plm = plm.FirstDifferenceOLS.from_formula(formula='crmrte ~ t + unem',
data=crime2)
results_plm = reg_plm.fit()

# print results:
table_plm = pd.DataFrame({'b': round(results_plm.params, 4),
						'se': round(results_plm.std_errors, 4),
						't': round(results_plm.tstats, 4),
						'pval': round(results_plm.pvalues, 4)})
print(f'table_plm: \n{table_plm}\n')



### Script 13.5: Example-13-9.py (modèle en 1ère différence avec Linearmodels)

crime4 = woo.dataWoo('crime4')
crime4 = crime4.set_index(['county', 'year'], drop=False)

# estimate FD model:
reg = plm.FirstDifferenceOLS.from_formula(
	formula='np.log(crmrte) ~ year + d83 + d84 + d85 + d86 + d87 +'
						     'lprbarr + lprbconv + lprbpris + lavgsen + lpolpc',
	data=crime4)
results = reg.fit()
print(f'results: \n{results}\n')

