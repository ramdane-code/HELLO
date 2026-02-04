import statsmodels.formula.api as smf
import statsmodels.api as sm
import wooldridge as woo
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Script 18.1: Example-18-1.py (estimation de modèles à retards distribués sur données de séries temporelles économiques)
hseinv = woo.dataWoo('hseinv')
print(hseinv.columns) # ['year','inv','pop','price','linv','lpop','lprice','t','invpc', 'linvpc','lprice_1','linvpc_1','gprice','ginvpc']

# add lags and detrend:
hseinv['linvpc_det'] = sm.tsa.tsatools.detrend(hseinv['linvpc'])
hseinv['gprice_lag1'] = hseinv['gprice'].shift(1)
hseinv['linvpc_det_lag1'] = hseinv['linvpc_det'].shift(1)

# Koyck geometric d.l.:
reg_koyck = smf.ols(formula='linvpc_det ~ gprice + linvpc_det_lag1', data=hseinv)
results_koyck = reg_koyck.fit()

# print regression table:
table_koyck = pd.DataFrame({'b': round(results_koyck.params, 4),
                            'se': round(results_koyck.bse, 4),
                            't': round(results_koyck.tvalues, 4),
                            'pval': round(results_koyck.pvalues, 4)})
print(f'table_koyck: \n{table_koyck}\n')

# rational d.l.: formulation complète
reg_rational = smf.ols(formula='linvpc_det ~ gprice + linvpc_det_lag1 +'
								'gprice_lag1',
						data=hseinv)
results_rational = reg_rational.fit()

# print regression table:
table_rational = pd.DataFrame({'b': round(results_rational.params, 4),
                            'se': round(results_rational.bse, 4),
                            't': round(results_rational.tvalues, 4),
                            'pval': round(results_rational.pvalues, 4)})
print(f'table_rational: \n{table_rational}\n')

# LRP:
lrp_koyck = results_koyck.params['gprice'] / (
				1 - results_koyck.params['linvpc_det_lag1'])
print(f'lrp_koyck: {lrp_koyck}\n')

lrp_rational = (results_rational.params['gprice'] +
							results_rational.params['gprice_lag1']) / (
									1 - results_rational.params['linvpc_det_lag1'])
print(f'lrp_rational: {lrp_rational}\n')



#Script 18.2: Example-18-4.py (test de racine unitaire ADF sur une ST)

inven = woo.dataWoo('inven')
inven['lgdp'] = np.log(inven['gdp'])

# automated ADF:
res_ADF_aut = sm.tsa.stattools.adfuller(inven['lgdp'], maxlag=1, autolag=None,
													regression='ct', regresults=True)
ADF_stat_aut = res_ADF_aut[0]
ADF_pval_aut = res_ADF_aut[1]
table = pd.DataFrame({'names': res_ADF_aut[3].resols.model.exog_names,
                        'b': np.round(res_ADF_aut[3].resols.params, 4),
                        'se': np.round(res_ADF_aut[3].resols.bse, 4),
                        't': np.round(res_ADF_aut[3].resols.tvalues, 4),
                        'pval': np.round(res_ADF_aut[3].resols.pvalues, 4)})
print(f'table: \n{table}\n')
print(f'ADF_stat_aut: {ADF_stat_aut}\n')
print(f'ADF_pval_aut: {ADF_pval_aut}\n')


# Script 18.3 : Simulate-Spurious-Regression-1.py régression fallacieuse (spurious regression) en ST)	
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import scipy.stats as stats

# set the random seed:
np.random.seed(123456)

# i.i.d. N(0,1) innovations:
n = 51
e = stats.norm.rvs(0, 1, size=n)
e[0] = 0
a = stats.norm.rvs(0, 1, size=n)
a[0] = 0

# independent random walks:
x = np.cumsum(a)
y = np.cumsum(e)
sim_data = pd.DataFrame({'y': y, 'x': x})

# regression:
reg = smf.ols(formula='y ~ x', data=sim_data)
results = reg.fit()

# print regression table:
table = pd.DataFrame({'b': round(results.params, 4),
                    'se': round(results.bse, 4),
                    't': round(results.tvalues, 4),
                    'pval': round(results.pvalues, 4)})
print(f'table: \n{table}\n')

# graph:
plt.plot(x, color='black', marker='', linestyle='-', label='x')
plt.plot(y, color='black', marker='', linestyle='--', label='y')
plt.ylabel('x,y')
plt.legend()
plt.savefig('PyGraphs/Simulate-Spurious-Regression-1.pdf')


# Script 18.4 : Simulate-Spurious-Regression-2.py( simuler et quantifier régression fallacieuse en ST.)	

# set the random seed:
np.random.seed(123456)
pvals = np.empty(10000)

# repeat r times:
for i in range(10000):
	# i.i.d. N(0,1) innovations:
	n = 51
	e = stats.norm.rvs(0, 1, size=n)
	e[0] = 0
	a = stats.norm.rvs(0, 1, size=n)
	a[0] = 0
	# independent random walks:
	x = np.cumsum(a)
	y = np.cumsum(e)
	sim_data = pd.DataFrame({'y': y, 'x': x})
	# regression:
	reg = smf.ols(formula='y ~ x', data=sim_data)
	results = reg.fit()
	pvals[i] = results.pvalues['x']
	# how often is p<=5%:
	count_pval_smaller = np.count_nonzero(pvals <= 0.05) # counts True elements
	print(f'count_pval_smaller: {count_pval_smaller}\n')
	# how often is p>5%:
	count_pval_greater = np.count_nonzero(pvals > 0.05)
	print(f'count_pval_greater: {count_pval_greater}\n')



	
# Script 18.5.	Prévisions en st


phillips = woo.dataWoo('phillips')

# define yearly time series beginning in 1948:
date_range = pd.date_range(start='1948', periods=len(phillips), freq='Y')
phillips.index = date_range.year

# estimate models:
yt96 = (phillips['year'] <= 1996)
reg_1 = smf.ols(formula='unem ~ unem_1', data=phillips, subset=yt96)
results_1 = reg_1.fit()
reg_2 = smf.ols(formula='unem ~ unem_1 + inf_1', data=phillips, subset=yt96)
results_2 = reg_2.fit()

# predictions for 1997-2003 including 95% forecast intervals:
yf97 = (phillips['year'] > 1996)
pred_1 = results_1.get_prediction(phillips[yf97])
pred_1_FI = pred_1.summary_frame(
	   alpha=0.05)[['mean', 'obs_ci_lower', 'obs_ci_upper']]
pred_1_FI.index = date_range.year[yf97]
print(f'pred_1_FI: \n{pred_1_FI}\n')
pred_2 = results_2.get_prediction(phillips[yf97])
pred_2_FI = pred_2.summary_frame(
	  alpha=0.05)[['mean', 'obs_ci_lower', 'obs_ci_upper']]
pred_2_FI.index = date_range.year[yf97]
print(f'pred_2_FI: \n{pred_2_FI}\n')

# forecast errors:
e1 = phillips[yf97]['unem'] - pred_1_FI['mean']
e2 = phillips[yf97]['unem'] - pred_2_FI['mean']

# RMSE and MAE:
rmse1 = np.sqrt(np.mean(e1 ** 2))
print(f'rmse1: {rmse1}\n')
rmse2 = np.sqrt(np.mean(e2 ** 2))
print(f'rmse2: {rmse2}\n')
mae1 = np.mean(abs(e1))
print(f'mae1: {mae1}\n')
mae2 = np.mean(abs(e2))
print(f'mae2: {mae2}\n')

# graph:
plt.plot(phillips[yf97]['unem'], color='black', marker='', label='unem')
plt.plot(pred_1_FI['mean'], color='black',
			marker='', linestyle='--', label='forecast without inflation')
plt.plot(pred_2_FI['mean'], color='black',
			marker='', linestyle='-.', label='forecast with inflation')
plt.ylabel('unemployment')
plt.xlabel('time')
plt.legend()
plt.savefig('PyGraphs/Example-18-8.pdf') 