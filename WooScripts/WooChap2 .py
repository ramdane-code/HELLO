import wooldridge as woo 
import numpy as np
import statsmodels.formula.api as smf 
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats


#Script2.1: Example-2-3.py : régression simple manuelle par fonction qui calcule ingrédients de la formule

#ceosal1 = woo.dataWoo('ceosal1'): data set enlevé d'ici car importée dans main_WooChap1.py
#dir(ceosal1) c'est le fichier de données.

def script1(ceosal): #Ajouté pour mise en fonction
    x = ceosal['roe']
    y = ceosal['salary']

    # ingredients to the OLS formulas:
    cov_xy = np.cov(x, y)[1, 0] # access 2. row and 1. column of covariance matrix 
    var_x = np.var(x, ddof=1)
    x_bar = np.mean(x) 
    y_bar = np.mean(y)

    # manual calculation of OLS coefficients:
    b1 = cov_xy / var_x 
    b0 = y_bar - b1 * x_bar 
    return b1, b0  #se substitue à print(f'b1: {b1}\n') et print(f'b0: {b0}\n')


#Script 2.2: Example-2-3-2.py (reg simple automat avec statsmodels de Salary sur ROE)

# La régression simple avec Statsmodels exécute plus facilement les calculs précédents
#ceosal1 = woo.dataWoo('ceosal1') :# fichier de données importé dans main_WooChap1.py
def script2(ceosal): #Ajouté pour mise en fonction
    reg = smf.ols(formula='salary ~ roe', data=ceosal) #smf pour statsmodels.formula
    results = reg.fit()
    b = results.params 
    return b # se substitue à print(f'b: \n{b}\n') dans le script original


# Script 2.3 Example 2.3 (régression de Salary sur ROE avec stats models et plots)

#ceosal1 = woo.dataWoo('ceosal1')
def script3(ceosal1): #Ajouté pour mise en fonction
   reg = smf.ols(formula='salary ~ roe', data=ceosal1) 
   results = reg.fit()
   # scatter plot and fitted values:
   plt.plot('roe', 'salary', data=ceosal1, color='grey', marker='o', linestyle='') 
   plt.plot(ceosal1['roe'], results.fittedvalues, color='black', linestyle='-') 
   plt.ylabel('salary')
   plt.xlabel('roe') 
   plt.savefig('PyGraphs/Example-2-3-3.pdf')
   return results 


#Script 2.4.py (reg linéaire simple de wage sur educ avec smf)
def script24(wage1):
#     wage1 = woo.dataWoo('wage1')

     reg = smf.ols(formula='wage ~ educ', data=wage1) 
     results = reg.fit()
     b = results.params 
     return b
     # print(f'b: \n{b}\n')

# Script 2.5 Example 2.5 (lien entre % des dépenses de campagne et % des voix puis plots)  
vote1 = woo.dataWoo('vote1')
# OLS regression:
reg = smf.ols(formula='voteA ~ shareA', data=vote1)
results = reg.fit() 
b = results.params 
print(f'b: \n{b}\n')
# scatter plot and fitted values:
plt.plot('shareA', 'voteA', data=vote1, color='grey', marker='o', linestyle='') 
plt.plot(vote1['shareA'], results.fittedvalues, color='black', linestyle='-') 
plt.ylabel('voteA')
plt.xlabel('shareA') 
plt.savefig('PyGraphs/Example-2-5.pdf')

# Script 2.6 Example 2.6 (Génère fitted value, resid et Table)
ceosal1 = woo.dataWoo('ceosal1')
# OLS regression:
reg = smf.ols(formula='salary ~ roe', data=ceosal1) 
results = reg.fit()
# obtain predicted values and residuals: 
salary_hat = results.fittedvalues
u_hat = results.resid
# Wooldridge, Table 2.2:
table = pd.DataFrame({'roe': ceosal1['roe'], 
                                      'salary': ceosal1['salary'], 
                                      'salary_hat': salary_hat, 
                                      'u_hat': u_hat})
print(f'table.head(15): \n{table.head(15)}\n')

#Script 2.7 (vérifie 3 hyp de la rég simple : moy nulle des résid, cov résid-xi nulle, ybar=hatb0+hatb1*xbar
wage1 = woo.dataWoo('wage1')
reg = smf.ols(formula='wage ~ educ', data=wage1) 
results = reg.fit()
# obtain coefficients, predicted values and residuals: 
b = results.params
wage_hat = results.fittedvalues 
u_hat = results.resid
# confirm property (1):
u_hat_mean = np.mean(u_hat) 
print(f'u_hat_mean: {u_hat_mean}\n')
# confirm property (2):
educ_u_cov = np.cov(wage1['educ'], u_hat)[1, 0] 
print(f'educ_u_cov: {educ_u_cov}\n')
# confirm property (3):
educ_mean = np.mean(wage1['educ']) 
wage_pred = b[0] + b[1] * educ_mean 
print(f'wage_pred: {wage_pred}\n')
wage_mean = np.mean(wage1['wage']) 
print(f'wage_mean: {wage_mean}\n')


#Script 2.8 (calcul des param, valeurs ajustées et R² , ce dernier par 3 méthodes)
ceosal1 = woo.dataWoo('ceosal1')
# OLS regression:
reg = smf.ols(formula='salary ~ roe', data=ceosal1)
results = reg.fit()
# calculate predicted values & residuals:
sal_hat = results.fittedvalues
u_hat = results.resid
# calculate R^2 in three different ways:
sal = ceosal1['salary']
R2_a = np.var(sal_hat, ddof=1) / np.var(sal, ddof=1)
R2_b = 1 - np.var(u_hat, ddof=1) / np.var(sal, ddof=1)
R2_c = np.corrcoef(sal, sal_hat)[1, 0] ** 2
print(f'R2_a: {R2_a}\n')
print(f'R2_b: {R2_b}\n')
print(f'R2_c: {R2_c}\n' )


#Script 2.9 ( (Régression avec smf %vote sur %dépenses puis afficher résultat par  summary et  par Table))
vote1 = woo.dataWoo('vote1')
# OLS regression:
reg = smf.ols(formula='voteA ~ shareA', data=vote1)
results = reg.fit()
# print results using summary: 
print(f'results.summary(): \n{results.summary()}\n')
# print regression table:
table = pd.DataFrame({'b': round(results.params, 4),
                                     'se': round(results.bse, 4), 
                                      't': round(results.tvalues, 4),
                                       'pval': round(results.pvalues, 4)}) 
print(f'table: \n{table}\n')


#Script 2.10 (avec smf, log (wage) expliqué par  educ)
wage1 = woo.dataWoo('wage1')
# estimate log-level model:
reg = smf.ols(formula='np.log(wage) ~ educ', data=wage1)
results = reg.fit() 
b = results.params 
print(f'b: \n{b}\n')


#Script 2.11 (np.log(salary) expliqué par np.log(sales))
ceosal1 = woo.dataWoo('ceosal1')
# estimate log-log model:
reg = smf.ols(formula='np.log(salary) ~ np.log(sales)', data=ceosal1)
results = reg.fit() 
b = results.params 
print(f'b: \n{b}\n')

#Script 2.12(régression simple sans constante et avec constante seulement, graph des fitted values)
ceosal1 = woo.dataWoo('ceosal1')
# usual OLS regression:
reg1 = smf.ols(formula='salary ~ roe', data=ceosal1)
results1 = reg1.fit() 
b_1 = results1.params 
print(f'b_1: \n{b_1}\n')
# regression without intercept (through origin):
reg2 = smf.ols(formula='salary ~ 0 + roe', data=ceosal1)
results2 = reg2.fit() 
b_2 = results2.params 
print(f'b_2: \n{b_2}\n')
# regression without slope (on a constant):
reg3 = smf.ols(formula='salary ~ 1', data=ceosal1)
results3 = reg3.fit()
b_3 = results3.params 
print(f'b_3: \n{b_3}\n')
# average y:
sal_mean = np.mean(ceosal1['salary']) 
print(f'sal_mean: {sal_mean}\n')
# scatter plot and fitted values:
plt.plot('roe', 'salary', data=ceosal1, color='grey', marker='o', linestyle='', label='')
plt.plot(ceosal1['roe'], results1.fittedvalues, color='black', linestyle='-', label='full')
plt.plot(ceosal1['roe'], results2.fittedvalues, color='black', linestyle=':', label='through origin')
plt.plot(ceosal1['roe'], results3.fittedvalues, color='black', linestyle='-.', label='const only')
plt.ylabel('salary')
plt.xlabel('roe')
plt.legend()
plt.grid()
# plt.savefig('PyGraphs/SLR-Origin-Const.pdf')
plt.show()


#Script 2.13(calcul manuel Standard error de regression SER puis SE de l'estimation des paramètres et calcul automat de SE )
meap93 = woo.dataWoo('meap93')
# estimate the model and save the results as "results":
reg = smf.ols(formula='math10 ~ lnchprg', data=meap93)
results = reg.fit()
# number of obs.: 
n = results.nobs
# SER:
u_hat_var = np.var(results.resid, ddof=1)
SER = np.sqrt(u_hat_var) * np.sqrt((n - 1) / (n - 2))
print(f'SER: {SER}\n')
# SE of b0 & b1, respectively:
lnchprg_sq_mean = np.mean(meap93['lnchprg'] ** 2)
lnchprg_var = np.var(meap93['lnchprg'], ddof=1) 
b1_se = SER / (np.sqrt(lnchprg_var)
                       * np.sqrt(n - 1)) * np.sqrt(lnchprg_sq_mean) 
b0_se = SER / (np.sqrt(lnchprg_var) * np.sqrt(n - 1))

print(f'b1_se: {b1_se}\n')
print(f'b0_se: {b0_se}\n')
# automatic calculations: 
print(f'results.summary(): \n{results.summary()}\n')


# Script 2.14 (Simulation : générer un échantillon cohérent avec les 5 hyp et plots)
# set the random seed: 
np.random.seed(1234567)
# set sample size:
n = 1000
# set true parameters (betas and sd of u):
beta0 = 1
beta1 = 0.5
su = 2
# draw a sample of size n:
x = stats.norm.rvs(4, 1, size=n) 
u = stats.norm.rvs(0, su, size=n)
y = beta0 + beta1 * x + u
df = pd.DataFrame({'y': y, 'x': x}) 
# estimate parameters by OLS:
reg = smf.ols(formula='y ~ x', data=df)
results = reg.fit() 
b = results.params 
print(f'b: \n{b}\n')
# features of the sample for the variance formula:
x_sq_mean = np.mean(x ** 2) 
print(f'x_sq_mean: {x_sq_mean}\n')
x_var = np.sum((x - np.mean(x)) ** 2)
print(f'x_var: {x_var}\n')
# graph:
x_range = np.linspace(0, 8, num=100)
plt.ylim([-2, 10])
plt.plot(x, y, color='lightgrey', marker='o', linestyle='')
plt.plot(x_range, beta0 + beta1 * x_range, color='black', linestyle='-', linewidth=2, label='pop. regr. fct.')
plt.plot(x_range, b[0] + b[1] * x_range, color='grey', linestyle='-', linewidth=2, label='OLS regr. fct.')
plt.ylabel('y')
plt.xlabel('x')
plt.legend()
plt.grid()
plt.show()
# plt.savefig('PyGraphs/SLR-Sim-Sample.pdf')


# Script 2.16 (génèrer 10000 échantillons de 1000 individus)

# set the random seed: 
def script216(seed,n,r,beta0,beta1,su):
     # np.random.seed(seed)
     # set sample size and number of simulations:
     # n = 1000 
     # r = 10000
     # set true parameters (betas and sd of u):
     # beta0 = 1
     # beta1 = 0.5
     # su = 2
     # initialize b0 and b1 to store results later:
     b0 = np.empty(r) 
     b1 = np.empty(r)
     # draw a sample of x, fixed over replications: 
     x = stats.norm.rvs(4, 1, size=n)
     # repeat r times:
     for i in range(r):
          # draw a sample of y:
          u = stats.norm.rvs(0, su, size=n)
          y = beta0 + beta1 * x + u
          df = pd.DataFrame({'y': y, 'x': x})
          # estimate and store parameters by OLS: 
          reg = smf.ols(formula='y ~ x', data=df)
          results = reg.fit()
          b0[i] = results.params['Intercept'] 
          b1[i] = results.params['x']
     return b0,b1
np.random.seed(1234567)
# set sample size and number of simulations:
n = 1000 
r = 10000
# set true parameters (betas and sd of u):
beta0 = 1
beta1 = 0.5
su = 2
# initialize b0 and b1 to store results later:
b0 = np.empty(r) 
b1 = np.empty(r)
# draw a sample of x, fixed over replications: 
x = stats.norm.rvs(4, 1, size=n)
# repeat r times:
for i in range(r):
     # draw a sample of y:
     u = stats.norm.rvs(0, su, size=n)
     y = beta0 + beta1 * x + u
     df = pd.DataFrame({'y': y, 'x': x})
     # estimate and store parameters by OLS: 
     reg = smf.ols(formula='y ~ x', data=df)
     results = reg.fit()
     b0[i] = results.params['Intercept'] 
     b1[i] = results.params['x']
# MC estimate of the expected values:
b0_mean = np.mean(b0) 
b1_mean = np.mean(b1)

print(f'b0_mean: {b0_mean}\n')
print(f'b1_mean: {b1_mean}\n')
# MC estimate of the variances: 
b0_var = np.var(b0, ddof=1) 
b1_var = np.var(b1, ddof=1)

print(f'b0_var: {b0_var}\n')
print(f'b1_var: {b1_var}\n')
# graph:
x_range = np.linspace(0, 8, num=100) 
plt.ylim([0, 6])
# add population regression line:
plt.plot(x_range, beta0 + beta1 * x_range, color='black', linestyle='-', linewidth=2, label='Population')
# add first OLS regression line (to attach a label):
plt.plot(x_range, b0[0] + b1[0] * x_range, color='grey', linestyle='-', linewidth=0.5, label='OLS regressions')
# add OLS regression lines no. 2 to 10:
for i in range(1, 10):
     plt.plot(x_range, b0[i] + b1[i] * x_range, color='grey', linestyle='-', linewidth=0.5)
plt.ylabel('y') 
plt.xlabel('x') 
plt.legend()
plt.savefig('PyGraphs/SLR-Sim-Model-Condx.pdf')

if False:
    b1, b0 = script1(ceosal1)
    print(f'b1: {b1}\n')
    print(f'b0: {b0}\n')
