import scipy.stats as stats
import numpy as np
import statsmodels.formula.api as smf
import wooldridge as woo
import pandas as pd
import matplotlib.pyplot as plt

### Script 6.1: Data-Scaling.py (changer dans la régression l'échelle de la variable dépendante et des variables indép)

bwght = woo.dataWoo('bwght')

# regress and report coefficients:Regression with weight in ounces:
reg = smf.ols(formula='bwght ~ cigs + faminc', data=bwght)
results = reg.fit()

# weight in pounds, manual way: créer une nouvelle variable bwght_lbs qui sera utilisée dans la régression.
bwght['bwght_lbs'] = bwght['bwght'] / 16  # poids en livres = poids en onces / 16
reg_lbs = smf.ols(formula='bwght_lbs ~ cigs + faminc', data=bwght)
results_lbs = reg_lbs.fit()

# weight in pounds, direct way: # effectuer la transformation de la variable
reg_lbs2 = smf.ols(formula='I(bwght/16) ~ cigs + faminc', data=bwght) # noter le I() pour indiquer que la transformation est faite dans la formule.
results_lbs2 = reg_lbs2.fit()

# packs of cigarettes: # transformer cigs en paquets de cigarettes (20 cigarettes par paquet)
reg_packs = smf.ols(formula='bwght ~ I(cigs/20) + faminc', data=bwght)
results_packs = reg_packs.fit()

# compare results:
table = pd.DataFrame({'b': round(results.params, 4),
                                      'b_lbs': round(results_lbs.params, 4),
                                      'b_lbs2': round(results_lbs2.params, 4),
                                      'b_packs': round(results_packs.params, 4)})
print(f'table: \n{table}\n')


# Script 6.2: Example-6-1.py (Standardisation des variables : variation du prix de l'immobilier en écart types (scaled))

# define a function for the standardization:
def scale(x):
	x_mean = np.mean(x)
	x_var = np.var(x, ddof=1)
	x_scaled = (x - x_mean) / np.sqrt(x_var)
	return x_scaled

# standardize and estimate:
hprice2 = woo.dataWoo('hprice2')
hprice2['price_sc'] = scale(hprice2['price'])
hprice2['nox_sc'] = scale(hprice2['nox'])
hprice2['crime_sc'] = scale(hprice2['crime'])
hprice2['rooms_sc'] = scale(hprice2['rooms'])
hprice2['dist_sc'] = scale(hprice2['dist'])
hprice2['stratio_sc'] = scale(hprice2['stratio'])
reg = smf.ols(
formula='price_sc ~ 0 + nox_sc + crime_sc + rooms_sc + dist_sc + stratio_sc',
		data=hprice2)
results = reg.fit()

# print regression table:
table = pd.DataFrame({'b': round(results.params, 4),
					'se': round(results.bse, 4),
					't': round(results.tvalues, 4),
					'pval': round(results.pvalues, 4)})
print(f'table: \n{table}\n')


# Script 6.3: Formula-Logarithm.py (modèle partiellement log)

hprice2 = woo.dataWoo('hprice2')

reg = smf.ols(formula='np.log(price) ~ np.log(nox) + rooms', data=hprice2)
results = reg.fit()

# print regression table:
table = pd.DataFrame({'b': round(results.params, 4),
					'se': round(results.bse, 4),
					't': round(results.tvalues, 4),
					'pval': round(results.pvalues, 4)})
print(f'table: \n{table}\n')


# Script 6.4: Example-6-2.py (utiliser spécifications log et puissance(quadratique))
import wooldridge as woo
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

hprice2 = woo.dataWoo('hprice2')

reg = smf.ols(
	formula='np.log(price) ~ np.log(nox)+np.log(dist)+rooms+I(rooms** 2)+stratio',
	data=hprice2)
results = reg.fit()

# print regression table:
table = pd.DataFrame({'b': round(results.params, 4),
					'se': round(results.bse, 4),
					't': round(results.tvalues, 4),
					'pval': round(results.pvalues, 4)})
print(f'table: \n{table}\n')


# Script 6.5: Example-6-2-Ftest.py (test F de pertinence d'une var au carré)
import wooldridge as woo
import numpy as np
import statsmodels.formula.api as smf

hprice2 = woo.dataWoo('hprice2')
n = hprice2.shape[0]

reg = smf.ols(
	formula='np.log(price) ~ np.log(nox)+np.log(dist)+rooms+I(rooms ** 2)+stratio',
	data=hprice2)
results = reg.fit()

# implemented F test for rooms:
hypotheses = ['rooms = 0', 'I(rooms ** 2) = 0']
ftest = results.f_test(hypotheses)
fstat = float(ftest.statistic) 
fpval = ftest.pvalue

print(f'fstat: {fstat}\n')
print(f'fpval: {fpval}\n')


### Script 6.6: Example-6-3.py  (utilisation d'une intéraction, de termes quadratiques et d'une variable standardisée)

attend = woo.dataWoo('attend')
n = attend.shape[0]

reg = smf.ols(formula='stndfnl ~ atndrte * priGPA + ACT + I(priGPA ** 2) + I(ACT ** 2)',data=attend)
results = reg.fit()

# print regression table:
table = pd.DataFrame({'b': round(results.params, 4),
					'se': round(results.bse, 4),
					't': round(results.tvalues, 4),
					'pval': round(results.pvalues, 4)})
print(f'table: \n{table}\n')

# estimate for partial effect at priGPA=2.59:
b = results.params
partial_effect = b['atndrte'] + 2.59 * b['atndrte:priGPA']
print(f'partial_effect: {partial_effect}\n')

# F test for partial effect at priGPA=2.59:
hypotheses = 'atndrte + 2.59 * atndrte:priGPA = 0'
ftest = results.f_test(hypotheses)
fstat = float(ftest.statistic)
fpval = ftest.pvalue

print(f'fstat: {fstat}\n')
print(f'fpval: {fpval}\n')


# Script 6.7: Predictions.py (utiliser la méthode predict de statsmodels pour estimer la valeur de y compte tenu de celles de xi)

gpa2 = woo.dataWoo('gpa2')

reg = smf.ols(formula='colgpa ~ sat + hsperc + hsize + I(hsize ** 2)', data=gpa2)
results = reg.fit()

# print regression table:
table = pd.DataFrame({'b': round(results.params, 4),
					'se': round(results.bse, 4),
					't': round(results.tvalues, 4),
					'pval': round(results.pvalues, 4)})
print(f'table: \n{table}\n')

# generate data set containing the regressor values for predictions:
cvalues1 = pd.DataFrame({'sat': [1200], 'hsperc': [30],
						'hsize': [5]}, index=['newPerson1'])
print(f'cvalues1: \n{cvalues1}\n')

# point estimate of prediction (cvalues1):
colgpa_pred1 = results.predict(cvalues1)
print(f'colgpa_pred1: \n{colgpa_pred1}\n')

# define three sets of regressor variables:
cvalues2 = pd.DataFrame({'sat': [1200, 900, 1400, ],
						'hsperc': [30, 20, 5], 'hsize': [5, 3, 1]},
						index=['newPerson1', 'newPerson2', 'newPerson3'])
print(f'cvalues2: \n{cvalues2}\n')

# point estimate of prediction (cvalues2):
colgpa_pred2 = results.predict(cvalues2)
print(f'colgpa_pred2: \n{colgpa_pred2}\n')


# Script 6.8: Example-6-5.py  (prédiction de la valeur de y (étant donnés les xi) avec un IC)

gpa2 = woo.dataWoo('gpa2')

reg = smf.ols(formula='colgpa ~ sat + hsperc + hsize + I(hsize ** 2)', data=gpa2)
results = reg.fit()

# define three sets of regressor variables:
cvalues2 = pd.DataFrame({'sat': [1200, 900, 1400, ],
						'hsperc': [30, 20, 5], 'hsize': [5, 3, 1]},
						index=['newPerson1', 'newPerson2', 'newPerson3'])

# point estimates and 95% confidence and prediction intervals:
colgpa_PICI_95 = results.get_prediction(cvalues2).summary_frame(alpha=0.05)
print(f'colgpa_PICI_95: \n{colgpa_PICI_95}\n')

# point estimates and 99% confidence and prediction intervals:
colgpa_PICI_99 = results.get_prediction(cvalues2).summary_frame(alpha=0.01)
print(f'colgpa_PICI_99: \n{colgpa_PICI_99}\n')


### Script 6.9: Effects-Manual.py (estimation, IC et graphiques)

hprice2 = woo.dataWoo('hprice2')

# repeating the regression from Example 6.2:
reg = smf.ols(
	formula='np.log(price) ~ np.log(nox)+np.log(dist)+rooms+I(rooms** 2)+stratio',
	data=hprice2)
results = reg.fit()

# predictions with rooms = 4-8, all others at the sample mean:
nox_mean = np.mean(hprice2['nox'])
dist_mean = np.mean(hprice2['dist'])
stratio_mean = np.mean(hprice2['stratio'])
X = pd.DataFrame({'rooms': np.linspace(4, 8, num=5),
				'nox': nox_mean,
				'dist': dist_mean,
				'stratio': stratio_mean})
print(f'X: \n{X}\n')

# calculate 95% confidence interval:
lpr_PICI = results.get_prediction(X).summary_frame(alpha=0.05)
lpr_CI = lpr_PICI[['mean', 'mean_ci_lower', 'mean_ci_upper']]
print(f'lpr_CI: \n{lpr_CI}\n')

# plot:
plt.plot(X['rooms'], lpr_CI['mean'], color='black', linestyle='-', label='')
plt.plot(X['rooms'], lpr_CI['mean_ci_upper'], color='lightgrey', linestyle='--', label='upper CI')
plt.plot(X['rooms'], lpr_CI['mean_ci_lower'], color='darkgrey', linestyle='--', label='lower CI')
plt.ylabel('lprice')
plt.xlabel('rooms')
plt.legend()
plt.savefig('PyGraphs/Effects-Manual.pdf')