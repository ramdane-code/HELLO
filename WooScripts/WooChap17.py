import wooldridge as woo
import pandas as pd
import statsmodels.formula.api as smf
import scipy.stats as stats
import numpy as np
import statsmodels.api as sm
import patsy as pt
import statsmodels.base.model as smclass

# Script 17.1 : Example-17-1-1.py(estimer un modèle de probabilité linéaire)

mroz = woo.dataWoo('mroz')

# estimate linear probability model:
reg_lin = smf.ols(formula='inlf ~ nwifeinc + educ + exper +'
								'I(exper** 2) + age + kidslt6 + kidsge6',
								data=mroz)
results_lin = reg_lin.fit(cov_type='HC3')

# print regression table:
table = pd.DataFrame({'b': round(results_lin.params, 4),
                    'se': round(results_lin.bse, 4),
                    't': round(results_lin.tvalues, 4),
                    'pval': round(results_lin.pvalues, 4)})
print(f'table: \n{table}\n')


# Script 17.2: Example-17-1-2.py (calcul de valeurs prédites avec modèle de prob linéaire)
import wooldridge as woo
import pandas as pd
import statsmodels.formula.api as smf

# Charger les données
mroz = woo.dataWoo('mroz')

# Estimer le modèle de probabilité linéaire
reg_lin = smf.ols(formula='inlf ~ nwifeinc + educ + exper + I(exper**2) + age + kidslt6 + kidsge6',
                  data=mroz)
results_lin = reg_lin.fit(cov_type='HC3')

# Créer deux profils extrêmes de femmes
X_new = pd.DataFrame({
    'nwifeinc': [100, 0],
    'educ': [5, 17],
    'exper': [0, 30],
    'age': [20, 52],
    'kidslt6': [2, 0],
    'kidsge6': [0, 0]
})

# Prédire la probabilité de travailler pour ces profils
predictions = results_lin.predict(X_new)

print(f'Prédictions pour deux profils extrêmes :\n{predictions}\n')


#Script 17.3 : Example-17-1-3.py** 	: estimer par logit les facteurs qui influencent la prob qu'une femme mariée travaille.
import wooldridge as woo
import statsmodels.formula.api as smf

mroz = woo.dataWoo('mroz')

# estimate logit model:
reg_logit = smf.logit(formula='inlf ~ nwifeinc + educ + exper +'
							  'I(exper** 2) + age + kidslt6 + kidsge6',
					  data=mroz)

# disp = 0 avoids printing out information during the estimation:
results_logit = reg_logit.fit(disp=0)
print(f'results_logit.summary(): \n{results_logit.summary()}\n')

# log likelihood value:
print(f'results_logit.llf: {results_logit.llf}\n')

# McFadden's pseudo R2:
print(f'results_logit.prsquared: {results_logit.prsquared}\n')

# Average marginal effects (AME) : Effets marginaux moyens
margeff = results_logit.get_margeff(method='dydx', at='overall')
print(f'margeff.summary(): \n{margeff.summary()}\n') 

# odds ratios and 95% confidence intervals:
or_ = np.exp(results_logit.params)
ci = np.exp(results_logit.conf_int())
pd.DataFrame({'OR': or_, 'CI_low': ci[0], 'CI_high': ci[1]})
print(f'odds ratios and 95% confidence intervals: \n{pd.DataFrame({"OR": or_, "CI_low": ci[0], "CI_high": ci[1]})}\n')


# Script 17.4 : Example-17-1-4.py(estimer par probit la prob qu'une femme mariée travaille.)

mroz = woo.dataWoo('mroz')

# estimate probit model:
reg_probit = smf.probit(formula='inlf ~ nwifeinc + educ + exper +'
								'I(exper** 2) + age + kidslt6 + kidsge6',
						data=mroz)
results_probit = reg_probit.fit(disp=0)
print(f'results_probit.summary(): \n{results_probit.summary()}\n')

# log likelihood value:
print(f'results_probit.llf: {results_probit.llf}\n')

# McFadden's pseudo R2:
print(f'results_probit.prsquared: {results_probit.prsquared}\n')


#Script 17.5 : Example-17-1-5.py(test de signification globale manuel et automat pour Probit)	

mroz = woo.dataWoo('mroz')

# estimate probit model:
reg_probit = smf.probit(formula='inlf ~ nwifeinc + educ + exper +'
								'I(exper** 2) + age + kidslt6 + kidsge6',
						data=mroz)
results_probit = reg_probit.fit(disp=0)

# test of overall significance (test statistic and pvalue):
llr1_manual = 2 * (results_probit.llf - results_probit.llnull)
print(f'llr1_manual: {llr1_manual}\n')
print(f'results_probit.llr: {results_probit.llr}\n')
print(f'results_probit.llr_pvalue: {results_probit.llr_pvalue}\n')

# automatic Wald test of H0 (experience and age are irrelevant):
hypotheses = ['exper=0', 'I(exper ** 2)=0', 'age=0']
waldstat = results_probit.wald_test(hypotheses)
teststat2_autom = waldstat.statistic
pval2_autom = waldstat.pvalue
print(f'teststat2_autom: {teststat2_autom}\n')
print(f'pval2_autom: {pval2_autom}\n')

# manual likelihood ratio statistic test of H0 (experience and age are irrelevant):
reg_probit_restr = smf.probit(formula='inlf ~ nwifeinc + educ +'
									'kidslt6 + kidsge6',
							  data=mroz)
results_probit_restr = reg_probit_restr.fit(disp=0)

llr2_manual = 2 * (results_probit.llf - results_probit_restr.llf)
pval2_manual = 1 - stats.chi2.cdf(llr2_manual, 3)
print(f'llr2_manual2: {llr2_manual}\n')
print(f'pval2_manual2: {pval2_manual}\n')



#Script 17.6 : Example-17-1-6.py (prediction avec prob linéaire, logit et probit)	

mroz = woo.dataWoo('mroz')

# estimate models:
reg_lin = smf.ols(formula='inlf ~ nwifeinc + educ + exper +'
								 'I(exper** 2) + age + kidslt6 + kidsge6',
				  data=mroz)
results_lin = reg_lin.fit(cov_type='HC3')

reg_logit = smf.logit(formula='inlf ~ nwifeinc + educ + exper +'
							   'I(exper** 2) + age + kidslt6 + kidsge6',
					  data=mroz)
results_logit = reg_logit.fit(disp=0)

reg_probit = smf.probit(formula='inlf ~ nwifeinc + educ + exper +'
								'I(exper** 2) + age + kidslt6 + kidsge6',
						data=mroz)
results_probit = reg_probit.fit(disp=0)

# predictions for two "extreme" women:
X_new = pd.DataFrame(
		{'nwifeinc': [100, 0], 'educ': [5, 17],
		'exper': [0, 30], 'age': [20, 52],
		'kidslt6': [2, 0], 'kidsge6': [0, 0]})
predictions_lin = results_lin.predict(X_new)
predictions_logit = results_logit.predict(X_new)
predictions_probit = results_probit.predict(X_new)

print(f'predictions_lin: \n{predictions_lin}\n')
print(f'predictions_logit: \n{predictions_logit}\n')
print(f'predictions_probit: \n{predictions_probit}\n')



# Script 17.9: Example-17-1-7.py (calcul des Effets partiels moyens)

mroz = woo.dataWoo('mroz')

# estimate models:
reg_lin = smf.ols(formula='inlf ~ nwifeinc + educ + exper + I(exper** 2) +'
								 'age + kidslt6 + kidsge6', data=mroz)
results_lin = reg_lin.fit(cov_type='HC3')

reg_logit = smf.logit(formula='inlf ~ nwifeinc + educ + exper + I(exper** 2) +'
									 'age + kidslt6 + kidsge6', data=mroz)
results_logit = reg_logit.fit(disp=0)

reg_probit = smf.probit(formula='inlf ~ nwifeinc + educ + exper + I(exper** 2) +'
										'age + kidslt6 + kidsge6', data=mroz)
results_probit = reg_probit.fit(disp=0)

# manual average partial effects:
APE_lin = np.array(results_lin.params)

xb_logit = results_logit.fittedvalues
factor_logit = np.mean(stats.logistic.pdf(xb_logit))
APE_logit_manual = results_logit.params * factor_logit

xb_probit = results_probit.fittedvalues
factor_probit = np.mean(stats.norm.pdf(xb_probit))
APE_probit_manual = results_probit.params * factor_probit

table_manual = pd.DataFrame({'APE_lin': np.round(APE_lin, 4),
                            'APE_logit_manual': np.round(APE_logit_manual, 4),
                            'APE_probit_manual': np.round(APE_probit_manual, 4)})
print(f'table_manual: \n{table_manual}\n')

# automatic average partial effects:
coef_names = np.array(results_lin.model.exog_names)
coef_names = np.delete(coef_names, 0) # drop Intercept

APE_logit_autom = results_logit.get_margeff().margeff
APE_probit_autom = results_probit.get_margeff().margeff

table_auto = pd.DataFrame({'coef_names': coef_names,
                          'APE_logit_autom': np.round(APE_logit_autom, 4),
                          'APE_probit_autom': np.round(APE_probit_autom, 4)})
print(f'table_auto: \n{table_auto}\n')


# Script 17.10: Example-17-3.py(estimer modèle linéaire et modèle de Poisson)


crime1 = woo.dataWoo('crime1')

# estimate linear model:
reg_lin = smf.ols(formula='narr86 ~ pcnv + avgsen + tottime + ptime86 +'
									'qemp86 + inc86 + black + hispan + born60',
				  data=crime1)
results_lin = reg_lin.fit()

# print regression table:
table_lin = pd.DataFrame({'b': round(results_lin.params, 4),
                        'se': round(results_lin.bse, 4),
                        't': round(results_lin.tvalues, 4),
                        'pval': round(results_lin.pvalues, 4)})
print(f'table_lin: \n{table_lin}\n')

# estimate Poisson model:
reg_poisson = smf.poisson(formula='narr86 ~ pcnv + avgsen + tottime +'
                                  'ptime86 + qemp86 + inc86 + black +'
                                  'hispan + born60',
						 data=crime1)
results_poisson = reg_poisson.fit(disp=0)

# print regression table:
table_poisson = pd.DataFrame({'b': round(results_poisson.params, 4),
                            'se': round(results_poisson.bse, 4),
                            't': round(results_poisson.tvalues, 4),
                            'pval': round(results_poisson.pvalues, 4)})
print(f'table_poisson: \n{table_poisson}\n')

# estimate Quasi-Poisson model:
reg_qpoisson = smf.glm(formula='narr86 ~ pcnv + avgsen + tottime + ptime86 +'
										'qemp86 + inc86 + black + hispan + born60',
						family=sm.families.Poisson(),
						data=crime1)

# the argument scale controls for the dispersion in exponential dispersion models,
# see the module documentation for more details:
results_qpoisson = reg_qpoisson.fit(scale='X2', disp=0)

# print regression table:
table_qpoisson = pd.DataFrame({'b': round(results_qpoisson.params, 4),
                            'se': round(results_qpoisson.bse, 4),
                            't': round(results_qpoisson.tvalues, 4),
                            'pval': round(results_qpoisson.pvalues, 4)})
print(f'table_qpoisson: \n{table_qpoisson}\n')


# Script 17.12: Example-17-2.py(estimer modèle Tobit par max de vraisemblance avec contrainte)

mroz = woo.dataWoo('mroz')
y, X = pt.dmatrices('hours ~ nwifeinc + educ + exper +'
							'I(exper** 2)+ age + kidslt6 + kidsge6',
					data=mroz, return_type='dataframe')

# generate starting solution:
reg_ols = smf.ols(formula='hours ~ nwifeinc + educ + exper + I(exper** 2) +'
								  'age + kidslt6 + kidsge6', data=mroz)
results_ols = reg_ols.fit()
sigma_start = np.log(sum(results_ols.resid ** 2) / len(results_ols.resid))
params_start = np.concatenate((np.array(results_ols.params), sigma_start),
																axis=None)

# extend statsmodels class by defining nloglikeobs:
class Tobit(smclass.GenericLikelihoodModel):
    # define a function that returns the negative log likelihood per observation
    # for a set of parameters that is provided by the argument "params":
    def nloglikeobs(self, params):
        # objects in "self" are defined in the parent class:
        X = self.exog
        y = self.endog
        p = X.shape[1]
        # for details on the implementation see Wooldridge (2019), formula 17.22:
        beta = params[0:p]
        sigma = np.exp(params[p])
        y_hat = np.dot(X, beta)
        y_eq = (y == 0)
        y_g = (y > 0)
        ll = np.empty(len(y))
        ll[y_eq] = np.log(stats.norm.cdf(-y_hat[y_eq] / sigma))
        ll[y_g] = np.log(stats.norm.pdf((y[y_g] - y_hat[y_g]) / sigma)) - np.log(sigma)
        # return an array of log likelihoods for each observation:
        return -ll

# results of MLE:
reg_tobit = Tobit(endog=y, exog=X)
results_tobit = reg_tobit.fit(start_params=params_start, maxiter=10000, disp=0)
print(f'results_tobit.summary(): \n{results_tobit.summary()}\n')


#Script 17.13 : Example-17-4.py modèle de régression censurée (modèle Tobit généralisé) sur la durée de récidive

recid = woo.dataWoo('recid')

# define dummy for censored observations:
censored = recid['cens'] != 0
y, X = pt.dmatrices('ldurat ~ workprg + priors + tserved + felon +'
                    'alcohol + drugs + black + married + educ + age',
                    data=recid, return_type='dataframe')

# generate starting solution:
reg_ols = smf.ols(formula='ldurat ~ workprg + priors + tserved + felon +'
                         'alcohol + drugs + black + married + educ + age',
                  data=recid)
results_ols = reg_ols.fit()
sigma_start = np.log(sum(results_ols.resid ** 2) / len(results_ols.resid))
params_start = np.concatenate((np.array(results_ols.params), sigma_start), axis=None)

# Correction : définition correcte de la classe et de la méthode
class CensReg(smclass.GenericLikelihoodModel):
    def __init__(self, endog, cens, exog):
        self.cens = cens
        super().__init__(endog, exog, missing='none')

    def nloglikeobs(self, params):
        x = self.exog
        y = self.endog
        cens = self.cens
        p = x.shape[1]
        beta = params[0:p]
        sigma = np.exp(params[p])
        y_hat = np.dot(x, beta)
        ll = np.empty(len(y))
        # uncensored:
        ll[~cens] = np.log(stats.norm.pdf((y[~cens] - y_hat[~cens]) / sigma)) - np.log(sigma)
        # censored:
        ll[cens] = np.log(stats.norm.cdf(-(y[cens] - y_hat[cens]) / sigma))
        return -ll

# results of MLE:
reg_censReg = CensReg(endog=y, exog=X, cens=censored)
results_censReg = reg_censReg.fit(start_params=params_start,
                                  maxiter=10000, method='BFGS', disp=0)
print(f'results_censReg.summary(): \n{results_censReg.summary()}\n')


### Script 17.14: TruncReg-Simulation.py (Modèle de rég tronqué)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import scipy.stats as stats

# <font color="#c0504d">set the random seed:</font>
np.random.seed(1234567)
x = np.sort(stats.norm.rvs(0, 1, size=100) + 4)
y = -4 + 1 * x + stats.norm.rvs(0, 1, size=100)

# <font color="#c0504d">complete observations and observed sample:</font>
compl = pd.DataFrame({'x': x, 'y': y})
sample = compl.loc[y > 0]

# <font color="#c0504d">predictions OLS:</font>
reg_ols = smf.ols(formula='y ~ x', data=sample)
results_ols = reg_ols.fit()
yhat_ols = results_ols.fittedvalues

# <font color="#c0504d">predictions truncated regression:</font>
reg_tr = smf.ols(formula='y ~ x', data=compl)
results_tr = reg_tr.fit()
yhat_tr = results_tr.fittedvalues

#<font color="#c0504d"> plot data and conditional means:</font>
plt.axhline(y=0, linewidth=0.5, linestyle='-', color='grey')
plt.plot(compl['x'], compl['y'], color='black',
marker='o', fillstyle='none', linestyle='', label='all data')
plt.plot(sample['x'], sample['y'], color='black',
marker='o', fillstyle='full', linestyle='', label='sample data')
plt.plot(sample['x'], yhat_ols, color='black',
marker='', linestyle='--', label='OLS fit')
plt.plot(compl['x'], yhat_tr, color='black',
marker='', linestyle='-', label='Trunc. Reg. fit')
plt.ylabel('y')
plt.xlabel('x')
plt.legend()
plt.savefig('PyGraphs/TruncReg-Simulation.pdf')


#Script 17.15: Example-17-5.py(méthode de Heckman (Heckit) pour corriger le biais de sélection)

mroz = woo.dataWoo('mroz')

# step 1 (use all n observations to estimate a probit model of s_i on z_i):
reg_probit = smf.probit(formula='inlf ~ educ + exper + I(exper** 2) +'
										'nwifeinc + age + kidslt6 + kidsge6',
												data=mroz)
results_probit = reg_probit.fit(disp=0)
pred_inlf = results_probit.fittedvalues
mroz['inv_mills'] = stats.norm.pdf(pred_inlf) / stats.norm.cdf(pred_inlf)

# step 2 (regress y_i on x_i and inv_mills in sample selection):
reg_heckit = smf.ols(formula='lwage ~ educ + exper + I(exper** 2) + inv_mills',
										subset=(mroz['inlf'] == 1), data=mroz)
results_heckit = reg_heckit.fit()

# print results:
print(f'results_heckit.summary(): \n{results_heckit.summary()}\n')