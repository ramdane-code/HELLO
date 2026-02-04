import wooldridge as woo
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np
import scipy.stats as stats


# Script 11.1: Example-11-4.py (Modèles AR pour prédire rendt des actions à partir de leur passé)
nyse = woo.dataWoo('nyse')
nyse['ret'] = nyse['return']

# add all lags up to order 3:
nyse['ret_lag1'] = nyse['ret'].shift(1)
nyse['ret_lag2'] = nyse['ret'].shift(2)
nyse['ret_lag3'] = nyse['ret'].shift(3)

# linear regression of model with lags:
reg1 = smf.ols(formula='ret ~ ret_lag1', data=nyse)
reg2 = smf.ols(formula='ret ~ ret_lag1 + ret_lag2', data=nyse)
reg3 = smf.ols(formula='ret ~ ret_lag1 + ret_lag2 + ret_lag3', data=nyse)
results1 = reg1.fit()
results2 = reg2.fit()
results3 = reg3.fit()

# print regression tables:
table1 = pd.DataFrame({'b': round(results1.params, 4),
			          'se': round(results1.bse, 4),
					  't': round(results1.tvalues, 4),
					  'pval': round(results1.pvalues, 4)})
print(f'table1: \n{table1}\n')
table2 = pd.DataFrame({'b': round(results2.params, 4),
					 'se': round(results2.bse, 4),
					 't': round(results2.tvalues, 4),
					 'pval': round(results2.pvalues, 4)})
print(f'table2: \n{table2}\n')
table3 = pd.DataFrame({'b': round(results3.params, 4),
					  'se': round(results3.bse, 4),
					  't': round(results3.tvalues, 4),
					  'pval': round(results3.pvalues, 4)})
print(f'table3: \n{table3}\n')


### Script 11.2: Example-EffMkts.py(import cours boursier Apple et calcul du rendement journalier)
# download data for 'AAPL' (= Apple) and define start and end: ==Assigner ticker au cours actions Apple et définir la période==
																															 # d'intérêt : 31/12/2007 au 31/12/2016 
tickers = ['AAPL']
start_date = '2007-12-31'
end_date = '2016-12-31'

# use pandas_datareader for the import:  # ==importer les données Apple pour la période choisie==
AAPL_data = yf.download('AAPL', start=start_date, end=end_date)

# drop ticker symbol from column name: ==enlever le niveau AAPL de l'index (level=1) pour simplifier la col==
AAPL_data.columns = AAPL_data.columns.droplevel(level=1) # retire le niv.1 de l'index des col du df: 
                                                                        # simplifier le multiindex:  ne garder que 'Close', 'Open'...)
# Afficher les têtes des colonnes du DataFrame AAPL_data:
print(f'AAPL_data.columns: \n{AAPL_data.columns}\n')  #


# calculate return as the log difference: ==calcule rendt  log journalier de l'action Apple c différence des log== 
                                                                # du prix de clôture ajusté d'un jour sur l'autre (Close).
AAPL_data['ret'] = np.log(AAPL_data['Close']).diff()   # Appliquer diff au log de la col 'Close'

# time series plot of adjusted closing prices:
plt.plot('ret', data=AAPL_data, color='black', linestyle='-') # ==créer graphique 'ret' à partir des données AAPl_data['ret']==
plt.ylabel('Apple Log Returns')
plt.xlabel('time')
plt.savefig('PyGraphs/Example-EffMkts.pdf')

# linear regression of models with lags: # 
AAPL_data['ret_lag1'] = AAPL_data['ret'].shift(1) # ==créer la variable 'ret_lag1'==
AAPL_data['ret_lag2'] = AAPL_data['ret'].shift(2)
AAPL_data['ret_lag3'] = AAPL_data['ret'].shift(3)
reg1 = smf.ols(formula='ret ~ ret_lag1', data=AAPL_data)
reg2 = smf.ols(formula='ret ~ ret_lag1 + ret_lag2', data=AAPL_data) #==régression 'ret' sur son lag1 et son lag2==
reg3 = smf.ols(formula='ret ~ ret_lag1 + ret_lag2 + ret_lag3', data=AAPL_data)
results1 = reg1.fit()
results2 = reg2.fit()
results3 = reg3.fit()

# print regression tables: # ==afficher l'output dans table1, table2, table3==
table1 = pd.DataFrame({'b': round(results1.params, 4),
					 'se': round(results1.bse, 4),
					 't': round(results1.tvalues, 4),
					 'pval': round(results1.pvalues, 4)})
print(f'table1: \n{table1}\n')
table2 = pd.DataFrame({'b': round(results2.params, 4),
					  'se': round(results2.bse, 4),
					  't': round(results2.tvalues, 4),
					  'pval': round(results2.pvalues, 4)})
print(f'table2: \n{table2}\n')
table3 = pd.DataFrame({'b': round(results3.params, 4),
					  'se': round(results3.bse, 4),
					  't': round(results3.tvalues, 4),
					  'pval': round(results3.pvalues, 4)})
print(f'table3: \n{table3}\n')


## Script 11.3 : Simulate-RandomWalk.py(simulation d'une marche aléatoire sans dérive)

# set the random seed:
np.random.seed(1234567)

# initialize plot:
x_range = np.linspace(0, 50, num=51)
plt.ylim([-18, 18])
plt.xlim([0, 50])

# loop over draws:
for r in range(0, 30):
      # i.i.d. standard normal shock:
      e = stats.norm.rvs(0, 1, size=51)
      # set first entry to 0 (gives y_0 = 0):
      e[0] = 0
      # random walk as cumulative sum of shocks:
      y = np.cumsum(e)
      # add line to graph:
      plt.plot(x_range, y, color='lightgrey', linestyle='-')
plt.axhline(linewidth=2, linestyle='--', color='black')
plt.ylabel('y')
plt.xlabel('time')
plt.savefig('PyGraphs/Simulate-RandomWalk.pdf')


### Script 11.4 : Simulate-RandomWalkDrift.py(simulation d'une marche aléatoire avec dérive)

# set the random seed:
np.random.seed(1234567)

# initialize plot:
x_range = np.linspace(0, 50, num=51)
plt.ylim([0, 100])
plt.xlim([0, 50])

# loop over draws:
for r in range(0, 30):
     # i.i.d. standard normal shock:
     e = stats.norm.rvs(0, 1, size=51)
     # set first entry to 0 (gives y_0 = 0):
     e[0] = 0
     # random walk as cumulative sum of shocks plus drift:
     y = np.cumsum(e) + 2 * x_range
     # add line to graph:
     plt.plot(x_range, y, color='lightgrey', linestyle='-')
plt.plot(x_range, 2 * x_range, linewidth=2, linestyle='--', color='black')
plt.ylabel('y')
plt.xlabel('time')
plt.savefig('PyGraphs/Simulate-RandomWalkDrift.pdf')

### Script 11.5 : Simulate-RandomWalkDrift-Diff.py : simuler une marche aléatoire avec dérive en différences

# set the random seed:
np.random.seed(1234567)

# initialize plot:
x_range = np.linspace(1, 50, num=50)
plt.ylim([-1, 5])
plt.xlim([0, 50])

# loop over draws:
for r in range(0, 30):
	# i.i.d. standard normal shock and cumulative sum of shocks:
	e = stats.norm.rvs(0, 1, size=51)
	e[0] = 0
	y = np.cumsum(2 + e)
	# first difference:
	Dy = y[1:51] - y[0:50]
	# add line to graph:
	plt.plot(x_range, Dy, color='lightgrey', linestyle='-')
plt.axhline(y=2, linewidth=2, linestyle='--', color='black')
plt.ylabel('y')
plt.xlabel('time')
plt.savefig('PyGraphs/Simulate-RandomWalkDrift-Diff.pdf')

### Script 11.6: Example-11-6.py

fertil3 = woo.dataWoo('fertil3')
T = len(fertil3)

# define time series (years only) beginning in 1913:
fertil3.index = pd.date_range(start='1913', periods=T, freq='Y').year

# compute first differences:
fertil3['gfr_diff1'] = fertil3['gfr'].diff()
fertil3['pe_diff1'] = fertil3['pe'].diff()
print(f'fertil3.head(): \n{fertil3.head()}\n')

# linear regression of model with first differences:
reg1 = smf.ols(formula='gfr_diff1 ~ pe_diff1', data=fertil3)
results1 = reg1.fit()

# print regression table:
table1 = pd.DataFrame({'b': round(results1.params, 4),
					 'se': round(results1.bse, 4),
					 't': round(results1.tvalues, 4),
					 'pval': round(results1.pvalues, 4)})
print(f'table1: \n{table1}\n')

# linear regression of model with lagged differences:
fertil3['pe_diff1_lag1'] = fertil3['pe_diff1'].shift(1)
fertil3['pe_diff1_lag2'] = fertil3['pe_diff1'].shift(2)
reg2 = smf.ols(formula='gfr_diff1 ~ pe_diff1 + pe_diff1_lag1 + pe_diff1_lag2',
							data=fertil3)
results2 = reg2.fit()

# print regression table:
table2 = pd.DataFrame({'b': round(results2.params, 4),
					  'se': round(results2.bse, 4),
					  't': round(results2.tvalues, 4),
					  'pval': round(results2.pvalues, 4)})
print(f'table2: \n{table2}\n')