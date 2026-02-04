import scipy.stats as stats
import numpy as np
import statsmodels.formula.api as smf
import wooldridge as woo
import pandas as pd


# Script 4.1 Calcul valeurs critiques (cv) pour Dist Normale et Dist t.
# CV for alpha = 5% and 1% using the t distribution with 137 d.f.:
alpha = np.array([0.05, 0.01])
cv_t = stats.t.ppf(1 - alpha / 2, 137)
print(f'cv_t: {cv_t}\n')

# CV for alpha=5% and 1% using the normal approximation:
cv_n = stats.norm.ppf(1 - alpha / 2)
print(f'cv_n: {cv_n}\n')


# Script 4.2: Example-4-3.py (test t et p-value manuels et automatiques (fit ajouté dans la rég))
gpa1 = woo.dataWoo('gpa1')
# Régression multiple avec Statsmodels
reg = smf.ols(formula='colGPA ~ hsGPA + ACT + skipped', data=gpa1)
results = reg.fit()
print(f'results.summary(): \n{results.summary()}\n') 

# manually confirm the formulas, i.e. extract coefficients and SE:
b = results.params # les estimateurs des paramètres dans b cad les $\hat \beta_s$ 
se = results.bse  # se : standard error des paramètres cad $\hat\sigma_{\hat\beta}$
# reproduce t statistic:
tstat = b / se     # calcul du t* empirique
print(f'tstat: \n{tstat}\n')
# reproduce p value:
pval = 2 * stats.t.cdf(-abs(tstat), 137) # calcul de la p-value
print(f'pval: \n{pval}\n')

# Script 4.3 : Example-4-1-cv.py (utilisation approx normale et t pour test t unilatéral et p-value)
# Critical Value for alpha=5% and 1% using the t distribution with 522 d.f.:
alpha = np.array([0.05, 0.01])
cv_t = stats.t.ppf(1 - alpha, 522)
print(f'cv_t: {cv_t}\n')
# CV for alpha=5% and 1% using the normal approximation:
cv_n = stats.norm.ppf(1 - alpha)
print(f'cv_n: {cv_n}\n')    


### Script 4.4: Example 4-1.py (explique Log(wage) par educ , exper , tenure)

wage1 = woo.dataWoo('wage1')

reg = smf.ols(formula='np.log(wage) ~ educ + exper + tenure', data=wage1)
results = reg.fit()
print(f'Output résumé : \n{results.summary()}\n')


# Script 4.5: Example-4-8.py : calcul IC pour expliquer les Dépenses en R&D par les Ventes et la marge bénéficiaire.

rdchem = woo.dataWoo('rdchem')

# OLS regression:
reg = smf.ols(formula='np.log(rd) ~ np.log(sales) + profmarg', data=rdchem)
results = reg.fit()
print(f'Output résumé : \n{results.summary()}\n')

# 95% CI: # Intervalle de confiance à 95%
CI95 = results.conf_int(0.05)
print(f'Intervalle de confiance 95% : \n{CI95}\n')

# 99% CI:
CI99 = results.conf_int(0.01)
print(f'Intervalle de confiance 99%: \n{CI99}\n')

# Script 4.6: F-Test.py : restrictions sur les paramètres et calcul t, p-value, F-test.

mlb1 = woo.dataWoo('mlb1')
n = mlb1.shape[0]

# unrestricted OLS regression:
reg_ur = smf.ols(formula='np.log(salary) ~ years + gamesyr + bavg + hrunsyr + rbisyr',
                           data=mlb1)
fit_ur = reg_ur.fit()
r2_ur = fit_ur.rsquared
print(f'r2_ur: {r2_ur}\n')

# restricted OLS regression:
reg_r = smf.ols(formula='np.log(salary) ~ years + gamesyr', data=mlb1)
fit_r = reg_r.fit()
r2_r = fit_r.rsquared
print(f'r2_r: {r2_r}\n')

# F statistic:
fstat = (r2_ur - r2_r) / (1 - r2_ur) * (n - 6) / 3
print(f'fstat: {fstat}\n')

# CV for alpha=1% using the F distribution with 3 and 347 d.f.:
cv = stats.f.ppf(1 - 0.01, 3, 347)
print(f'cv: {cv}\n')

# p value = 1-cdf of the appropriate F distribution:
fpval = 1 - stats.f.cdf(fstat, 3, 347)
print(f'fpval: {fpval}\n')


### Script 4.7: F-Test-Automatic.py (calcul automatique de F, p-value et t du Script 4.6)

mlb1 = woo.dataWoo('mlb1')

# OLS regression:
reg = smf.ols(formula='np.log(salary) ~ years + gamesyr + bavg + hrunsyr + rbisyr',
                      data=mlb1)
results = reg.fit()

# automated F test:
hypotheses = ['bavg = 0', 'hrunsyr = 0', 'rbisyr = 0']
ftest = results.f_test(hypotheses)
fstat = float(ftest.statistic)
fpval = ftest.pvalue

print(f'fstat: {fstat}\n')
print(f'fpval: {fpval}\n')

### Script 4.8: F-Test-Automatic2.py (utiliser la fonction results.f_test(hypotheses)

mlb1 = woo.dataWoo('mlb1')

# OLS regression:
reg = smf.ols(
formula='np.log(salary) ~ years + gamesyr + bavg + hrunsyr + rbisyr',
data=mlb1)
results = reg.fit()

# automated F test:
hypotheses = ['bavg = 0', 'hrunsyr = 2* rbisyr']
ftest = results.f_test(hypotheses)
fstat = float(ftest.statistic)
fpval = ftest.pvalue
print(f'fstat: {fstat}\n')
print(f'fpval: {fpval}\n')
