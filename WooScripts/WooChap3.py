#Script 3.1: Example-3-1.py**(Multiple régression : expliquer colGPA par hsGPA et ACT)
import wooldridge as woo
import statsmodels.formula.api as smf 

gpa1 = woo.dataWoo('gpa1')

reg = smf.ols(formula='colGPA ~ hsGPA + ACT', data=gpa1) 
results = reg.fit()
print(f'results.summary(): \n{results.summary()}\n')


#Script 3.2: Example-3-2.py ((expliquer log(wage) par edu+exper+tenure))
import wooldridge as woo
import numpy as np
import statsmodels.formula.api as smf

wage1 = woo.dataWoo('wage1')

reg = smf.ols(formula='np.log(wage) ~ educ + exper + tenure', data=wage1)
results = reg.fit()
print(f'results.summary(): \n{results.summary()}\n')
      

#Script 3.3: Example-3-3.py (expliquer prate par mrate+age)
import wooldridge as woo
import numpy as np
import statsmodels.formula.api as smf

k401k = woo.dataWoo('401k')

reg = smf.ols(formula='prate ~ mrate + age', data=k401k)
results = reg.fit()
print(f'results.summary(): \n{results.summary()}\n')
      

#Script 3.4: Example-3-5a.py (expliquer narr86 par pcnv+ptime86+qemp86)
import wooldridge as woo
import statsmodels.formula.api as smf

crime1 = woo.dataWoo('crime1')

# model without avgsen:
reg = smf.ols(formula='narr86 ~ pcnv + ptime86 + qemp86', data=crime1)
results = reg.fit()
print(f'results.summary(): \n{results.summary()}\n')
      

#Script 3.5: Example-3-5b.py (explique narr86 par pcnv+avgsen+ptime86+qemp86)
import wooldridge as woo
import statsmodels.formula.api as smf

crime1 = woo.dataWoo('crime1')

# model with avgsen:
reg = smf.ols(formula='narr86 ~ pcnv + avgsen + ptime86 + qemp86', data=crime1)
results = reg.fit()
print(f'results.summary(): \n{results.summary()}\n')
      

#Script 3.6: Example-3-6.py (explique log(wage) par educ)
import wooldridge as woo
import numpy as np
import statsmodels.formula.api as smf

wage1 = woo.dataWoo('wage1')

reg = smf.ols(formula='np.log(wage) ~ educ', data=wage1)
results = reg.fit()
print(f'results.summary(): \n{results.summary()}\n')
      

#Script 3.7: OLS-Matrices.py  (calcul matriciel de régression taux  réussite scolaire avec patsy)
import wooldridge as woo
import numpy as np
import pandas as pd
import patsy as pt

gpa1 = woo.dataWoo('gpa1')

# determine sample size & number of regressors:
n = len(gpa1)
k = 2

# extract y:
y = gpa1['colGPA']

# extract X & add a column of ones:
X = pd.DataFrame({'const': 1, 'hsGPA': gpa1['hsGPA'], 'ACT': gpa1['ACT']})

# alternative with patsy:
y2, X2 = pt.dmatrices('colGPA ~ hsGPA + ACT', data=gpa1, return_type='dataframe')

# display first rows of X:
print(f'X.head(): \n{X.head()}\n')

# parameter estimates:
X = np.array(X)
y = np.array(y).reshape(n, 1) # creates a row vector
b = np.linalg.inv(X.T @ X) @ X.T @ y  # équivaut à (X'X)puissance(-1) X'y
print(f'b: \n{b}\n')

# residuals, estimated variance of u and SER:
u_hat = y - X @ b
sigsq_hat = (u_hat.T @ u_hat) / (n - k - 1)  #hat sigma2 (hat sigma squared)
SER = np.sqrt(sigsq_hat)   #Standard error of the regression = racine de sigsq_hat
print(f'SER: {SER}\n')

# estimated variance of the parameter estimators and SE:
Vbeta_hat = sigsq_hat * np.linalg.inv(X.T @ X) #Variance beta_hat :matrice varcovar estimée par OLS
se = np.sqrt(np.diagonal(Vbeta_hat)) #standard errors des param. estimés :racine de main diagonal de Vbeta_hat
print(f'se: {se}\n')
#rem : ne pas confondre SER (standard error of regression) et se (standard error of parameter estimates)

#Script 3.8: Omitted-Vars.py (biais de variable explicative omise; dans expliquer colGPA par ACT et hsGPA)
import wooldridge as woo
import statsmodels.formula.api as smf

gpa1 = woo.dataWoo('gpa1')

# parameter estimates for full and simple model:
reg = smf.ols(formula='colGPA ~ ACT + hsGPA', data=gpa1)
results = reg.fit()
b = results.params
print(f'b: \n{b}\n')

# relation between regressors:
reg_delta = smf.ols(formula='hsGPA ~ ACT', data=gpa1)
results_delta = reg_delta.fit()
delta_tilde = results_delta.params
print(f'delta_tilde: \n{delta_tilde}\n')

# omitted variables formula for b1_tilde:
b1_tilde = b['ACT'] + b['hsGPA'] * delta_tilde['ACT']
print(f'b1_tilde: \n{b1_tilde}\n')

# actual regression with hsGPA omitted:
reg_om = smf.ols(formula='colGPA ~ ACT', data=gpa1)
results_om = reg_om.fit()
b_om = results_om.params
print(f'b_om: \n{b_om}\n')


#Script 3.9: MLR-SE.py (extraire les résultats inclus dans la méthode fit : params, resid...)
import wooldridge as woo
import numpy as np
import statsmodels.formula.api as smf
gpa1 = woo.dataWoo('gpa1')

# full estimation results including automatic SE:
reg = smf.ols(formula='colGPA ~ hsGPA + ACT', data=gpa1)
results = reg.fit()

# extract SER (instead of calculation via residuals):
SER = np.sqrt(results.mse_resid)

# regressing hsGPA on ACT for calculation of R2 & VIF:
reg_hsGPA = smf.ols(formula='hsGPA ~ ACT', data=gpa1)
results_hsGPA = reg_hsGPA.fit()
R2_hsGPA = results_hsGPA.rsquared
VIF_hsGPA = 1 / (1 - R2_hsGPA)
print(f'VIF_hsGPA: {VIF_hsGPA}\n')

# manual calculation of SE of hsGPA coefficient:
n = results.nobs
sdx = np.std(gpa1['hsGPA'], ddof=1) * np.sqrt((n - 1) / n)
SE_hsGPA = 1 / np.sqrt(n) * SER / sdx * np.sqrt(VIF_hsGPA)
print(f'SE_hsGPA: {SE_hsGPA}\n')
      

#Script 3.10: MLR-VIF.py (calcul du VIF)
import wooldridge as woo
import numpy as np
import statsmodels.stats.outliers_influence as smo
import patsy as pt

wage1 = woo.dataWoo('wage1')

# extract matrices using patsy:
y, X = pt.dmatrices('np.log(wage) ~ educ + exper + tenure',
data=wage1, return_type='dataframe')

# get VIF:
K = X.shape[1]
VIF = np.empty(K)
for i in range(K):
    VIF[i] = smo.variance_inflation_factor(X.values, i)
print(f'VIF: \n{VIF}\n')

