import wooldridge as woo
import pandas as pd
import statsmodels.formula.api as smf
import numpy as np
import statsmodels.api as sm

### Script 7.1: Example-7-1.py (variable explicative fictive - dummy variable)
wage1 = woo.dataWoo('wage1')

reg = smf.ols(formula='wage ~ female + educ + exper + tenure', data=wage1)
results = reg.fit()

# print regression table:
table = pd.DataFrame({'b': round(results.params, 4),
					'se': round(results.bse, 4),
					't': round(results.tvalues, 4),
					'pval': round(results.pvalues, 4)})
print(f'table: \n{table}\n')


### Script 7.2: Example-7-6.py (implémenter terme d'intéraction avec variable dummy)

wage1 = woo.dataWoo('wage1')

reg = smf.ols(formula='np.log(wage) ~ married * female + educ + exper +'
                                      'I(exper ** 2) + tenure + I(tenure ** 2)', data=wage1)
results = reg.fit()

# print regression table:
table = pd.DataFrame({'b': round(results.params, 4),
					'se': round(results.bse, 4),
					't': round(results.tvalues, 4),
					'pval': round(results.pvalues, 4)})
print(f'table: \n{table}\n')


# Script 7.3: Example-7-1-Boolean.py (var bool (True, False) à la place des dummies (1,0))

wage1 = woo.dataWoo('wage1')

# regression with boolean variable:
wage1['isfemale'] = (wage1['female'] == 1)
reg = smf.ols(formula='wage ~ isfemale + educ + exper + tenure', data=wage1)
results = reg.fit()

# print regression table:
table = pd.DataFrame({'b': round(results.params, 4),
											'se': round(results.bse, 4),
											't': round(results.tvalues, 4),
											'pval': round(results.pvalues, 4)})
print(f'table: \n{table}\n')


# Script 7.4: Regr-Categorical.py (utiliser les variables categoricals. rem: absence fichier CPS1985)

CPS1985 = pd.read_csv('C:\\Users\\ramda\\.vscode\\MonProjet\\hello\\MesData\\datasets\\CPS1985.csv')
# rename variable to make outputs more compact:
CPS1985['oc'] = CPS1985['occupation']

# table of categories and frequencies for two categorical variables:
freq_gender = pd.crosstab(CPS1985['gender'], columns='count')
print(f'freq_gender: \n{freq_gender}\n')

freq_occupation = pd.crosstab(CPS1985['oc'], columns='count')
print(f'freq_occupation: \n{freq_occupation}\n')

# directly using categorical variables in regression formula:
reg = smf.ols(formula='np.log(wage) ~ education +'
												'experience + C(gender) + C(oc)', data=CPS1985)
results = reg.fit()
# print regression table:
table = pd.DataFrame({'b': round(results.params, 4),
											'se': round(results.bse, 4),
											't': round(results.tvalues, 4),
											'pval': round(results.pvalues, 4)})
print(f'table: \n{table}\n')

# rerun regression with different reference category:
reg_newref = smf.ols(formula='np.log(wage) ~ education + experience + '
										'C(gender, Treatment("male")) + '
										'C(oc, Treatment("technical"))', data=CPS1985)
results_newref = reg_newref.fit()
# print results:
table_newref = pd.DataFrame({'b': round(results_newref.params, 4),
							'se': round(results_newref.bse, 4),
							't': round(results_newref.tvalues, 4),
							'pval': round(results_newref.pvalues, 4)})
print(f'table_newref: \n{table_newref}\n')


### Script 7.5: Regr-Categorical-Anova.py (Tableau Anova-analyse of variance- de statsmodels, donne test F...:pb : fichier CPS 1985 introuvable)


CPS1985 = pd.read_csv('C:\\Users\\ramda\\.vscode\\MonProjet\\hello\\MesData\\datasets\\CPS1985.csv')

# run regression:
reg = smf.ols(
	formula='np.log(wage) ~ education + experience + gender + occupation',
	data=CPS1985)
results = reg.fit()
# print regression table:
table_reg = pd.DataFrame({'b': round(results.params, 4),
						'se': round(results.bse, 4),
						't': round(results.tvalues, 4),
						'pval': round(results.pvalues, 4)})
print(f'table_reg: \n{table_reg}\n')

# ANOVA table:
table_anova = sm.stats.anova_lm(results, typ=2)
print(f'table_anova: \n{table_anova}\n')


# Script 7.6 : Example-7-8.py(estimer ST.. divisée en périodes (plages) avec Categoricals)

lawsch85 = woo.dataWoo('lawsch85')

# define cut points for the rank:
cutpts = [0, 10, 25, 40, 60, 100, 175]

# create categorical variable containing ranges for the rank:
lawsch85['rc'] = pd.cut(lawsch85['rank'], bins=cutpts,
										labels=['(0,10]', '(10,25]', '(25,40]',
												'(40,60]', '(60,100]', '(100,175]'])

# display frequencies:
freq = pd.crosstab(lawsch85['rc'], columns='count')
print(f'freq: \n{freq}\n')

# run regression:
reg = smf.ols(formula='np.log(salary) ~ C(rc, Treatment("(100,175]")) +'
										'LSAT + GPA + np.log(libvol) + np.log(cost)',
						data=lawsch85)
results = reg.fit()

# print regression table:
table_reg = pd.DataFrame({'b': round(results.params, 4),
						'se': round(results.bse, 4),
						't': round(results.tvalues, 4),
						'pval': round(results.pvalues, 4)})
print(f'table_reg: \n{table_reg}\n')

# ANOVA table:
table_anova = sm.stats.anova_lm(results, typ=2)
print(f'table_anova: \n{table_anova}\n')


# Script 7.7 : Dummy-Interact.py (OLS sur subset d'échantillon, interaction dummy, F test)	

gpa3 = woo.dataWoo('gpa3')

# filtrer uniquement les données de printemps (spring == 1)
gpa3_spring = gpa3[gpa3['spring'] == 1]

# model with full interactions with female dummy (only for spring data):
reg = smf.ols(formula='cumgpa ~ female * (sat + hsperc + tothrs)',
              data=gpa3_spring)
results = reg.fit()

# print regression table:
table = pd.DataFrame({'b': round(results.params, 4),
                    'se': round(results.bse, 4),
                    't': round(results.tvalues, 4),
                    'pval': round(results.pvalues, 4)})
print(f'table: \n{table}\n')

# F-Test for H0 (the interaction coefficients of 'female' are zero):
hypotheses = ['female = 0', 'female:sat = 0',
             'female:hsperc = 0', 'female:tothrs = 0']
ftest = results.f_test(hypotheses)
fstat = float(ftest.statistic)
fpval = ftest.pvalue 

print(f'fstat: {fstat}\n')
print(f'fpval: {fpval}\n')


# Script 7.8:Dummy-Interact-Separate.py (OLS séparée par sexe (hommes/femmes))
import wooldridge as woo
import pandas as pd
import statsmodels.formula.api as smf

gpa3 = woo.dataWoo('gpa3')

# estimate model for males (& spring data):
reg_m = smf.ols(formula='cumgpa ~ sat + hsperc + tothrs',
								data=gpa3,
								subset=(gpa3['spring'] == 1) & (gpa3['female'] == 0)) # les obs 'female' de la col spring == 0 sont les hommes</font>
results_m = reg_m.fit()

# print regression table:
table_m = pd.DataFrame({'b': round(results_m.params, 4),
                        'se': round(results_m.bse, 4),
                        't': round(results_m.tvalues, 4),
                        'pval': round(results_m.pvalues, 4)})
print(f'table_m: \n{table_m}\n')

# estimate model for females (& spring data):
reg_f = smf.ols(formula='cumgpa ~ sat + hsperc + tothrs',
							data=gpa3,
							subset=(gpa3['spring'] == 1) & (gpa3['female'] == 1)) # les obs 'female' de la col spring == 1 sont les femmes</font>
results_f = reg_f.fit()

# print regression table:
table_f = pd.DataFrame({'b': round(results_f.params, 4),
                        'se': round(results_f.bse, 4),
                        't': round(results_f.tvalues, 4),
                        'pval': round(results_f.pvalues, 4)})
print(f'table_f: \n{table_f}\n')