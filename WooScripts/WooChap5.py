import scipy.stats as stats
import numpy as np
import statsmodels.formula.api as smf
import wooldridge as woo
import pandas as pd


### Script 5.1: Sim-Asy-OLS-norm.py (générer 10000 échant de taille n respectant hyp 1à6)

# set the random seed:
np.random.seed(1234567)  #fixe la graine (seed) pour la reproductibilité

# set sample size and number of simulations:
n = 100     #taille de l'échantillon
r = 1000    #nombre de simulations

# set true parameters:#fixer les vrais paramètres du modèle
beta0 = 1  # intercept
beta1 = 0.5 #pente
sx = 1  # écart-type de x
ex = 4  # espérance de x

# initialize b1 to store results later: #préparer tableau pour stocker les estimateurs simulés de la
b1 = np.empty(r)

# draw a sample of x, fixed over replications: # Générer un échantillon de x, fixe pour toutes les répétitions
x = stats.norm.rvs(ex, sx, size=n) # Générer un vecteur x de taille n=100, tiré d'une loi normale de moyenne ex=4 et d'écart-type sx=1

# repeat r times: #boucle de simulation
for i in range(r):
    # draw a sample of u (std. normal): # à chaque itération, on génère un bruit aléatoire u tiré d'une loi normale standard
    u = stats.norm.rvs(0, 1, size=n)
    y = beta0 + beta1 * x + u   # on construit la variable dépendante y selon le modèle linéaire
    df = pd.DataFrame({'y': y, 'x': x})  # créer un DataFrame avec les variables y et x de la régression
    # estimate conditional OLS:
    reg = smf.ols(formula='y ~ x', data=df)
    results = reg.fit()
    b1[i] = results.params['x'] # on stocke l'estimateur de la pente dans b1[i]


#Script 5.2: Sim-Asy-OLS-chisq.py (générer 10000 échant de taille n respectant hyp 1à6 dist Khi2)
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import scipy.stats as stats

# set the random seed:
np.random.seed(1234567)

# set sample size and number of simulations:
n = 100
r = 10000

# set true parameters:
beta0 = 1
beta1 = 0.5
sx = 1
ex = 4

# initialize b1 to store results later:
b1 = np.empty(r)

# draw a sample of x, fixed over replications:
x = stats.norm.rvs(ex, sx, size=n)

# repeat r times:
for i in range(r):
    # draw a sample of u (standardized chi-squared[1]):
    u = (stats.chi2.rvs(1, size=n) - 1) / np.sqrt(2)
    y = beta0 + beta1 * x + u
    df = pd.DataFrame({'y': y, 'x': x})
    # estimate conditional OLS:
    reg = smf.ols(formula='y ~ x', data=df)
    results = reg.fit()
    b1[i] = results.params['x']



# Script 5.3: Sim-Asy-OLS-uncond.py (autre simulation des 10000 échantillons)

# set the random seed:
np.random.seed(1234567)

# set sample size and number of simulations:
n = 100
r = 10000

# set true parameters:
beta0 = 1
beta1 = 0.5
sx = 1
ex = 4

# initialize b1 to store results later:
b1 = np.empty(r)

# repeat r times:
for i in range(r):
     # draw a sample of x, varying over replications:
     x = stats.norm.rvs(ex, sx, size=n)
     # draw a sample of u (std. normal):
     u = stats.norm.rvs(0, 1, size=n)
     y = beta0 + beta1 * x + u
     df = pd.DataFrame({'y': y, 'x': x})
     # estimate unconditional OLS:
     reg = smf.ols(formula='y ~ x', data=df)
     results = reg.fit()
     b1[i] = results.params['x']


# Script 5.4: Example-5-3.py: test LM

crime1 = woo.dataWoo('crime1')

# 1. estimate restricted model:
reg_r = smf.ols(formula='narr86 ~ pcnv + ptime86 + qemp86', data=crime1)
fit_r = reg_r.fit()
r2_r = fit_r.rsquared
print(f'r2_r: {r2_r}\n')

# 2. regression of residuals from restricted model:
crime1 = crime1.copy()  # pour éviter SettingWithCopyWarning
crime1['utilde'] = fit_r.resid
reg_LM = smf.ols(formula='utilde ~ pcnv + ptime86 + qemp86 + avgsen + tottime', data=crime1)
fit_LM = reg_LM.fit()
r2_LM = fit_LM.rsquared
print(f'r2_LM: {r2_LM}\n')

# 3. calculation of LM test statistic:
LM = r2_LM * fit_LM.nobs
print(f'LM: {LM}\n')

# 4. critical value from chi-squared distribution, alpha=10%:
cv = stats.chi2.ppf(1 - 0.10, 2)
print(f'cv: {cv}\n')

# 5. p value (alternative to critical value):
pval = 1 - stats.chi2.cdf(LM, 2)
print(f'pval: {pval}\n')

# 6. compare to F-test:
reg = smf.ols(formula='narr86 ~ pcnv + ptime86 + qemp86 + avgsen + tottime', data=crime1)
results = reg.fit()
hypotheses = ['avgsen = 0', 'tottime = 0']
ftest = results.f_test(hypotheses)
fstat = float(ftest.statistic)
fpval = ftest.pvalue
print(f'fstat: {fstat}\n')
print(f'fpval: {fpval}\n')