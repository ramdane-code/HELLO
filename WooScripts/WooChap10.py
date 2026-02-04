import wooldridge as woo
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import pandas_datareader as pdr
import yfinance as yf

# Script 10.1: Example-10-2.py (ST : expliquer taux d'intérêt par taux d'inflation et déficit budgétaire)

intdef = woo.dataWoo('intdef') # intdef : DataSet contenant les col taux d'intérêt i3, taux d'inflation inf, déficit budgtaire def

# linear regression of static model (==Q function avoids conflicts with keywords==):
reg = smf.ols(formula='i3 ~ Q("inf") + Q("def")', data=intdef)
results = reg.fit()

# print regression table:
table = pd.DataFrame({'b': round(results.params, 4),
					'se': round(results.bse, 4),
					't': round(results.tvalues, 4),
					'pval': round(results.pvalues, 4)})
print(f'table: \n{table}\n')



# Script 10.2: Example-Barium.py(date_range de Pandas pour générer index pour ST équidistantes)
barium = woo.dataWoo('barium')
T = len(barium) 

# monthly time series starting Feb. 1978:
barium.index = pd.date_range(start='1978-02', periods=T, freq='M')
print(f'barium["chnimp"].head(): \n{barium["chnimp"].head()}\n') # import de Chine 

# plot chnimp (default: index on the x-axis): 
plt.plot('chnimp', data=barium, color='black', linestyle='-')
plt.ylabel('chnimp')
plt.xlabel('time')



# Script 10.3 : Example-StockData.py( utiliser pandas_datareader pour importer des données de BD extérieures)
import wooldridge as woo
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

# Utilisation de yfinance à la place de DataReader (plus fiable pour Yahoo)
import yfinance as yf

# Paramètres de téléchargement
tickers = ['F']
start_date = '2014-01-01'
end_date = '2015-12-31'

print("Téléchargement via yfinance...")
F_data = yf.download(tickers, start=start_date, end=end_date)

if F_data is None or F_data.empty:
	raise RuntimeError("Aucune donnée récupérée pour les tickers fournis via yfinance.")

# Afficher un aperçu des données importées
print('F_data.head():')
print(F_data.head())
print('\nF_data.tail():')
print(F_data.tail())

# <font color="#c0504d">time series plot of adjusted closing prices:</font>
plt.plot('Close', data=F_data, color='black', linestyle='-')
plt.ylabel('Ford Close Price')
plt.xlabel('time')
plt.savefig('PyGraphs/Example-StockData.pdf')


# Script 10.4: Example-10-4.py(Modèle de Décalage distribué (DLM) : reg du tx gl de fécondité sur pe+pe_lag1+pe_lag2+ww2+pill)
fertil3 = woo.dataWoo('fertil3')
T = len(fertil3)  # longueur de la période de référence

# define yearly time series beginning in 1913: série temporelle annuelle de longueur T et débutant en 1913 
fertil3.index = pd.date_range(start='1913', periods=T, freq='Y').year

# add all lags of 'pe' up to order 2:  # pe : personal exemption
fertil3['pe_lag1'] = fertil3['pe'].shift(1) # crée nouvelle col. pe_lag1 où chq valeur = valeur pe(-1). Rem : la ligne 0 est Nan
fertil3['pe_lag2'] = fertil3['pe'].shift(2) # crée nouvelle col. pe_lag2 = valeur pe (-2). Rem : ligne 0 et 1 sont Nan. 

# linear regression of model with lags: 
reg = smf.ols(formula='gfr ~ pe + pe_lag1 + pe_lag2 + ww2 + pill', data=fertil3) # var dummy pour 2eme GM et pill : prise pillute
results = reg.fit()

# print regression table:
table = pd.DataFrame({'b': round(results.params, 4),
					'se': round(results.bse, 4),
					't': round(results.tvalues, 4),
					'pval': round(results.pvalues, 4)})
print(f'table: \n{table}\n')



# Script 10.5: Example-10-4.py :Propension à LT (LRP) mesure l'effet cumulatif de la variable pe sur gfr
fertil3 = woo.dataWoo('fertil3')
T = len(fertil3)

# define yearly time series beginning in 1913:
fertil3.index = pd.date_range(start='1913', periods=T, freq='YE').year

# add all lags of 'pe' up to order 2: # crée col pe(-1) et pe(-2)
fertil3['pe_lag1'] = fertil3['pe'].shift(1)
fertil3['pe_lag2'] = fertil3['pe'].shift(2)

# linear regression of model with lags:
reg = smf.ols(formula='gfr ~ pe + pe_lag1 + pe_lag2 + ww2 + pill', data=fertil3)
results = reg.fit()

# F test (H0: all pe coefficients are=0): test de significativité globale des personal exemptions
hypotheses1 = ['pe = 0', 'pe_lag1 = 0', 'pe_lag2 = 0']
ftest1 = results.f_test(hypotheses1)
fstat1 = float(ftest1.statistic)  # convert to float for better readability
fpval1 = ftest1.pvalue

print(f'fstat1: {fstat1}\n')
print(f'fpval1: {fpval1}\n')

# calculating the LRP:
b = results.params
b_pe_tot = b['pe'] + b['pe_lag1'] + b['pe_lag2']
print(f'b_pe_tot: {b_pe_tot}\n')

# F test (H0: LRP=0):
hypotheses2 = ['pe + pe_lag1 + pe_lag2 = 0']
ftest2 = results.f_test(hypotheses2)
fstat2 = float(ftest2.statistic)  # convert to float for better readability
fpval2 = ftest2.pvalue

print(f'fstat2: {fstat2}\n')
print(f'fpval2: {fpval2}\n')



# Script 10.6: Example-10-7.py (régression avec et sans tendance linéaire Nb)

hseinv = woo.dataWoo('hseinv')  # charger 'hseinv'

# Calculer les logarithmes à l'avance pour éviter l'erreur patsy/np
import numpy as np
hseinv['log_invpc'] = np.log(hseinv['invpc'])
hseinv['log_price'] = np.log(hseinv['price'])

#linear regression without time trend: # régression de log(invpc) sur log(price) sans tenir compte de la Tendance
reg_wot = smf.ols(formula='log_invpc ~ log_price', data=hseinv)
results_wot = reg_wot.fit()

# print regression table:
table_wot = pd.DataFrame({'b': round(results_wot.params, 4),
                        'se': round(results_wot.bse, 4),
                        't': round(results_wot.tvalues, 4),
                        'pval': round(results_wot.pvalues, 4)})
print(f'table_wot: \n{table_wot}\n') 

# linear regression with time trend (data set includes a time variable t): # régression log(invpc) sur log(price) et Trend t
if 't' not in hseinv.columns:
    hseinv['t'] = range(1, len(hseinv) + 1)
reg_wt = smf.ols(formula='log_invpc ~ log_price + t', data=hseinv)
results_wt = reg_wt.fit()

# print regression table:
table_wt = pd.DataFrame({'b': round(results_wt.params, 4),
                        'se': round(results_wt.bse, 4),
                        't': round(results_wt.tvalues, 4),
                        'pval': round(results_wt.pvalues, 4)})
print(f'table_wt: \n{table_wt}\n')



# Script 10.7: Example-10-11.py (dummies pour les saisons afin de tenir cpte des var° saisonnières)
barium = woo.dataWoo('barium')

# linear regression with seasonal effects:
reg = smf.ols(formula='np.log(chnimp) ~ np.log(chempi) + np.log(gas) +'
							           'np.log(rtwex) + befile6 + affile6 + afdec6 +'
									   'feb + mar + apr + may + jun + jul +'
									   'aug + sep + oct + nov + dec',
						data=barium)
results = reg.fit()

# print regression table:
table = pd.DataFrame({'b': round(results.params, 4),
					'se': round(results.bse, 4),
					't': round(results.tvalues, 4),
					'pval': round(results.pvalues, 4)})
print(f'table: \n{table}\n')