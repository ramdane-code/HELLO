**Fichier :** Heiss Panels.docx

# 13. Pooling Cross-Sections Across Time: Simple Panel Data Methods

 Pooled cross sections consist of random samples from the same population at different points in time.

*   La Section [13.1](#pooled-cross-sections) présente ce type de jeu de données et comment l'utiliser pour estimer les changements dans le temps.
*   La Section [13.2](#difference-in-differences) couvre les estimateurs de différence de différences, une application importante des coupes transversales poolées pour identifier des effets causaux.

 Panel data resemble pooled cross sectional data in that we have observations at different points in time. The key difference is that we observe the *same* cross-sectional units, for example individuals or firms.

 Panel data methods require the data to be organized in a systematic way, as discussed in Section [13.3.](#organizing-panel-data)

 This allows specific calculations used for panel data analyses that are presented in Section [13.4.](#panel-specific-computations) Section [13.5](#first-differenced-estimator) introduces the first panel data method, first differenced estimation.

## 13.1 Pooled Cross-Sections

 If we have random samples at different points in time, this does not only increase the overall sample size and thereby the statistical precision of our analyses. It also allows to study changes over time and shed additional light on relationships between variables.

### Wooldridge, Example 13.2: Changes to the Return to Education and the Gender Wage Gap13.2

 The data set CPS78_85.dta includes two pooled cross-sections for the years 1978 and 1985.
 The dummy variable y85 is equal to one for observations in 1985 and to zero for 1978.
 We estimate a model for the log wage lwage of the form

 $lwage = \beta_0 + \delta_0 y85 + \beta_1 educ + \delta_1 (y85 /cdot educ) + \beta_2 exper + \beta_3 exper^2 + \beta_4 union + \beta_5 female + \delta_5(y85 /cdot female) + u$

 Note that we divide $exper^2$ by 100 and thereby multiply $\beta_3$ by 100 compared to the results reported in Wooldridge (2019).
 The parameter $\beta_1$ measures the return to education in 1978 and $\delta_1$ is the *difference* of the return to education in 1985 relative to 1978.
 Likewise, $\beta_5$ is the gender wage gap in 1978 and $\delta_5$ is the change of the wage gap.
 Script 13.1 (Example-13-2.R) estimates the model.
 The return to education is estimated to have increased by $\hat{\delta}_1 = 0.018$ and the gender wage gap decreased in absolute value from $\hat{\beta}_5 = 0.317$ to $\hat{\beta}_5 + \hat{\delta}_5 = 0.232$, even though this change is only marginally significant. The interpretation and implementation of interactions were covered in more detail in Section 6.1.6.

```
Script 13.1: Example-13-2.R
data(cps78_85, package=’wooldridge’)
# Detailed OLS results including interaction terms
summary( lm(lwage ~ y85*(educ+female) +exper+ I((exper^2)/100) + union,
						data=cps78_85) )


Residual standard error: 0.4127 on 1075 degrees of freedom
Multiple R-squared:  0.4262,	Adjusted R-squared:  0.4219
F-statistic: 99.8 on 8 and 1075 DF,  p-value: < 2.2e-16
```

## 13.2. Difference-in-Differences

 Wooldridge (2019, Section 13.2) discusses an important type of applications for pooled cross-sections. Difference-in-differences (DiD) estimators estimate the effect of a policy intervention (in the broadest sense) by comparing the change over time of an outcome of interest between an affected and an unaffected group of observations.

 In a regression framework, we regress the outcome of interest on a dummy variable for the affected ("treatment") group, a dummy indicating observations after the treatment and an interaction term between both. The coefficient of this interaction term can then be a good estimator for the effect of interest, controlling for initial differences between the groups and contemporaneous changes over time.

### Wooldridge, Example 13.3: Effect of a Garbage Incinerator's Location on Housing Prices 13.3

 We are interested in whether and how much the construction of a new garbage incinerator affected the value of nearby houses. Script 13.2 (Example-13-3-1.R) uses the data set KIELMC.dta. We first estimate separate models for 1978 (before there were any rumors about the new incinerator) and 1981 (when the construction began). In 1981, the houses close to the construction site were cheaper by an average of \$30,688.27. But this was not only due to the new incinerator since even in 1978, nearby houses were cheaper by an average of \$18,824.37. The difference of these differences $\hat{\delta} = \$30,688.27 - \$18,824.37 = \$11,863.90$ is the DiD estimator and is arguably a better indicator of the actual effect.

 The DiD estimator can be obtained more conveniently using a joint regression model with the interaction term as described above. The estimator $\hat{\delta} = \$11,863.90$ can be directly seen as the coefficient of the interaction term. Conveniently, standard regression tables include $t$ tests of the hypothesis that the actual effect is equal to zero. For a one-sided test, the $p$ value is $\frac{1}{2} \cdot 0.112 = 0.056$, so there is some statistical evidence of a negative impact.

 The DiD estimator can be improved. A logarithmic specification is more plausible since it implies a constant *percentage* effect on the house values. We can also add additional regressors to control for incidental changes in the composition of the houses traded. Script 13.3 (Example-13-3-2.R) implements both improvements. The model including features of the houses implies an estimated decrease in the house values of about 13.2%. This effect is also significantly different from zero.

```
Script 13.2: Example-13-3-1.R

 # Separate regressions for 1978 and 1981: report coefficients only
 coef( lm(rprice~nearinc, data=kielmc, subset=(year==1978)) )

 coef( lm(rprice~nearinc, data=kielmc, subset=(year==1981)) )

 # Joint regression including an interaction term
 library(lmtest)
 coeftest( lm(rprice~nearinc*y81, data=kielmc) )

```

```
Script 13.3: Example-13-3-2.R
DiD <- lm(log(rprice)~nearinc*y81 , data=kielmc)
DiDcontr <- lm(log(rprice)~nearinc*y81+age+I(age^2)+log(intst)+
                           log(land)+log(area)+rooms+baths, data=kielmc)
library(stargazer)
stargazer(DiD,DiDcontr,type="text")

```

## 13.3 Organizing Panel Data
 A panel data set includes several observations at different points in time $t$ for the same (or at least an overlapping) set of cross-sectional units $i$. A simple "pooled" regression model could look like
 $$y_{it} = \beta_0 + \beta_1 x_{it1} + \beta_2 x_{it2} + \cdots + \beta_k x_{itk} + v_{it}; \quad t = 1, \ldots, T; \quad i = 1, \ldots, n, \tag{13.1}$$
 where the double subscript now indicates values for individual (or other cross-sectional unit) $i$ at time $t$. We could estimate this model by OLS, essentially ignoring the panel structure. But at least the assumption that the error terms are unrelated is very hard to justify since they contain unobserved individual traits that are likely to be constant or at least correlated over time. Therefore, we need specific methods for panel data.

 For the calculations used by panel data methods, we have to make sure that the data set is systematically organized and the estimation routines understand its structure. Usually, a panel data set comes in a "long" form where each row of data corresponds to one combination of $i$ and $t$. We have to define which observations belong together by introducing an index variable for the cross-sectional units $i$ and preferably also the time index $t$.

 The package ***plm*** (for panel linear models) is a comprehensive collection of commands dealing with panel data. Similar to specific data types for time series, it offers a data type named `pdata.frame`. It essentially corresponds to a standard `data.frame` but has additional attributes that describe the individual and time dimensions. Suppose we have our data in a standard data frame named mydf. It includes a variable ivar indicating the cross-sectional units and a variable tvar indicating the time. Then we can create a panel data frame with the command
 `mypdf <- pdata.frame( mydf, index=c("ivar","tvar") )`

 If we have a balanced panel (i.e. the same number of observations $T$ for each "individual" $i = 1, /ldots, n$) and the observations are first sorted by $i$ and then by $t$, we can alternatively call
 `mypdf <- pdata.frame( mydf, index=n )`

 In this case, the new variables id and time are generated as the index variables.

 Once we have defined our data set, we can check the dimensions with `pdim(mypdf)`. It will report whether the panel is balanced, the number of cross-sectional units $n$, the number of time units $T$, and the total number of observations $N$ (which is $n T$ in balanced panels).

 Let's apply this to the data set CRIME2.dta discussed by Wooldridge (2019, Section 13.3). It is a balanced panel of 46 cities, properly sorted. Script 13.4 (PDataFrame.R) imports the data set. We define our new panel data frame crime2.p and check its dimensions. Apparently, $R$ understood us correctly and reports a balanced panel with two observations on 46 cities each. We also display the first six rows of data for the new id and time index variables and other selected variables. Now we're ready to work with this data set.

```
Script 13.4: PDataFrame.R

 library(plm)
 data(crime2, package='wooldridge')
 # Define panel data frame
 crime2.p <- pdata.frame(crime2, index=46 )
 # Panel dimensions:
 pdim(crime2.p)

 # Observation 1-6: new "id" and "time" and some other variables:
 crime2.p[1:6,c("id","time","year","pop","crimes","crmrte","unem")]

```

## 13.4 Panel-specific computations

 Once we have defined our panel data set, we can do useful computations specific to panel data. They will be used by the estimators discussed below. While we will see that for much of applied panel data regressions, the canned routines will take care of these calculations, it is still instructive and gives us more flexibility to be able to implement them ourselves.

 Consider a panel data set with the cross-sectional units (individuals,...) $i = 1, \ldots, n$. There are $T_i$ observations for individual $i$. The total number of observations is $N = \sum_{i=1}^{n} T_i$. In the special case of a balanced panel, all individuals have the same $T_i = T$ and $N = n T$.

 Table [13.1](#_bookmark5) lists the most important special functions. We can calculate lags and first differences using `lag` and `diff`, respectively. Unlike in pure time series data, the lags and differences are calculated for the individuals separately, so the first observations for each $i = 1, \ldots, n$ is `NA`. Higher-order lags can be specified as a second argument.

 The individual averages $\bar{x}_i = \frac{1}{T_i} \sum_{t=1}^{T_i} x_{it}$ are calculated using the function `between` which returns one value for each *individual* in a vector of length $n$. Often, we need this value for each of the $N observations$. The command `Between` returns this vector of length $N$ where each $\bar{x}_i$ is repeated $T_i$ times. The within transformation conveniently calculated with `Within` subtracts the individual mean $\bar{x}_i$ from observation $x_{it}$. These "demeaned" variables play an important role in Chapter [14.](#advanced-panel-data-methods)

 **Table 13.1.** Panel-specific computations

 | Commande     | Transformation | Description                                                                 |
 |--------------|----------------|-----------------------------------------------------------------------------|
 | `l=lag(x)`   | Lag                                        | $l_{it} = x_{i,t-1}$                                                         |
 | `d=diff(x)`  | Difference                            | $d_{it} = x_{it} - x_{i,t-1}$                                                |
 | `b=between(x)` | Between (length $n$)          | $b_i = \frac{1}{T_i} \sum_{t=1}^{T_i} x_{it}$                                  |
 | `B=Between(x)`| Between (length $N$)          | $B_{it} = b_i$                                                              |
 | `w=Within(x)`  | Within (demeaning)          | $w_{it} = x_{it} - B_{it}$                                                    |

 Script 13.5 (Example-PLM-Calcs.R) demonstrates these functions. The data set CRIME4.dta has data on 90 counties for seven years. The data set includes the index variables county and year which are used in the definition of our `pdata.frame`. We calculate lags, differences, between and within transformations of the crime rate (crmrte). The results are stored back into the panel data frame. The first rows of data are then presented for illustration.

 The lagged variable vcr.l is just equal to crmrte but shifted down one row. The difference between these two variables is cr.d. The average crmrte within the first seven rows (i.e. for county 1) is given as the first seven values of cr.B and cr.W is the difference between crmrte and cr.B.

```
Script 13.5: Example-PLM-Calcs.R

 library(plm)
 data(crime4, package='wooldridge')
 # Generate pdata.frame:
 crime4.p <- pdata.frame(crime4, index=c("county","year") )
 # Calculations within the pdata.frame:
 crime4.p$cr.l <- lag(crime4.p$crmrte)
 crime4.p$cr.d <- diff(crime4.p$crmrte)
 crime4.p$cr.B <- Between(crime4.p$crmrte)
 crime4.p$cr.W <- Within(crime4.p$crmrte)
 # Display selected variables for observations 1-16:
 crime4.p[1:16,c("county","year","crmrte","cr.l","cr.d","cr.B","cr.W")]
```

## 13.5 First Differenced Estimator

 Wooldridge (2019, Sections 13.3 -- 13.5) discusses basic unobserved effects models and their estimation by first-differencing (FD). Consider the model
 $$y_{it} = \beta_0 + \beta_1 x_{it1} + \cdots + \beta_k x_{itk} + a_i + u_{it}; \quad t = 1, \ldots, T; \quad i = 1, \ldots, n, \tag{13.2}$$
 which differs from Equation [13.1] in that it explicitly involves an unobserved effect $a_i$ that is constant over time (since it has no $t$ subscript). If it is correlated with one or more of the regressors $x_{it1}, \ldots, x_{itk}$, we cannot simply ignore $a_i$, leave it in the composite error term $v_{it} = a_i + u_{it}$ and estimate the equation by OLS. The error term $v_{it}$ would be related to the regressors, violating assumption MLR.4 (and MLR.4') and creating biases and inconsistencies. Note that this problem is not unique to panel data, but possible solutions are.

 The first differenced (FD) estimator is based on the first difference of the whole equation:
 $$\Delta y_{it} \equiv y_{it} - y_{i,t-1} = \beta_1 \Delta x_{it1} + \cdots + \beta_k \Delta x_{itk} + \Delta u_{it}; \quad t = 2, \ldots, T; \quad i = 1, \ldots, n. \tag{13.3}$$

 Note that we cannot evaluate this equation for the first observation $t = 1$ for any $i$ since the lagged values are unknown for them. The trick is that $a_i$ drops out of the equation by differencing since it does not change over time. No matter how badly it is correlated with the regressors, it cannot hurt the estimation anymore. This estimating equation is then analyzed by OLS. We simply regress the differenced dependent variable $\Delta y_{it}$ on the differenced independent variables $\Delta x_{it1}, \ldots, \Delta x_{itk}$.

 Script 13.6 (Example-FD.R) opens the data set CRIME2.dta already used above. Within a `pdata.frame`, we use the function `diff` to calculate first differences of the dependent variable crime rate (crmrte) and the independent variable unemployment rate (unem) within our data set.

 A list of the first six observations reveals that the differences are unavailable (`NA`) for the first year of each city. The other differences are also calculated as expected. For example the change of the crime rate for city 1 is $70.11729 - 74.65756 = -4.540268$ and the change of the unemployment rate for city 2 is $5.4 - 8.1 = -2.7$.

 The FD estimator can now be calculated by simply applying OLS to these differenced values. The observations for the first year with missing information are automatically dropped from the estimation sample. The results show a significantly positive relation between unemployment and crime.

```
Script 13.6: Example-FD.R

 library(plm); library(lmtest)
 data(crime2, package='wooldridge')
 crime2.p <- pdata.frame(crime2, index=46 )
 # manually calculate first differences:
 crime2.p$dyear <- diff(crime2.p$year)
 crime2.p$dcrmrte <- diff(crime2.p$crmrte)
 crime2.p$dunem <- diff(crime2.p$unem)
 # Display selected variables for observations 1-6:
 crime2.p[1:6,c("id","time","year","dyear","crmrte","dcrmrte","unem","dunem")]

# Estimate FD model with lm on differenced data:
 coeftest( lm(dcrmrte~dunem, data=crime2.p) )

# Estimate FD model with plm on original data:
 coeftest( plm(crmrte~unem, data=crime2.p, model="fd") )
```
 Generating the differenced values and using `lm` on them is actually unnecessary. Package ***plm*** provide the versatile command `plm` which implements FD and other estimators, some of which we will use in chapter [14.](#advanced-panel-data-methods) It works just like `lm` but is directly applied to the original variables and does the necessary calculations internally. With the option `model="pooling"`, the pooled OLS estimator is requested, option `model="fd"` produces the FD estimator. As the output of Script 13.6 (Example-FD.R) shows, the parameter estimates are exactly the same as our pedestrian calculations.

### Wooldridge, Example 13.9: County Crime Rates in North Carolina13.9
 Script 13.7 (Example-13-9.R) analyzes the data CRIME4.dta already used in Script 13.5 (Example-PLM-Calcs.R). Just for illustration, we calculate the first difference of crmrte and display the first nine rows of data. The first difference is `NA` for the first year for each county. Then we estimate the model in first differences using `plm`.

 Note that in this specification, all variables are automatically differenced, so they have the intuitive interpretation in the level equation. In the results reported by Wooldridge (2019), the year dummies are not differenced which only affects the interpretation of the year coefficients. To reproduce the exact same results as Wooldridge (2019), we could use a pooled OLS estimator and explicitly difference the other variables:

 `plm(diff(log(crmrte)) ~ d83+d84+d85+d86+d87+diff(lprbarr)+diff(lprbconv)+ diff(lprbpris)+diff(lavgsen)+diff(lpolpc), data=pdata, model="pooling")`

 We will repeat this example with "robust" standard errors in Section [14.4.](#robust-clustered-standard-errors)

```
Output of Script 13.7: Example-13-9.R

 library(plm);library(lmtest)
 data(crime4, package='wooldridge')
 crime4.p <- pdata.frame(crime4, index=c("county","year") )
 pdim(crime4.p)

 # manually calculate first differences of crime rate:
 crime4.p$dcrmrte <- diff(crime4.p$crmrte)
 # Display selected variables for observations 1-9:
 crime4.p[1:9, c("county","year","crmrte","dcrmrte")]

'# Estimate FD model:
coeftest( plm(log(crmrte)~d83+d84+d85+d86+d87+lprbarr+lprbconv+ lprbpris+lavgsen+lpolpc,data=crime4.p, model="fd") )
```

# 14. Advanced Panel Data Methods

In this chapter, we look into additional panel data models and methods. We start with the widely used fixed effects (FE) estimator in Section [14.1,](#fixed-effects-estimation) followed by random effects (RE) in Section [14.2.](#random-effects-models) The dummy variable regression and correlated random effects approaches presented in Section [14.3](#dummy-variable-regression-and-correlated-random-effects) can be used as alternatives and generalizations of FE. Finally, we cover robust formulas for the variance-covariance matrix and the implied "clustered" standard errors in Section [14.4.](#robust-clustered-standard-errors) We will come back to panel data in combination with instrumental variables in Section [15.6.](#instrumental-variables-with-panel-data)

## 14.1 Fixed Effects Estimation
 We start from the same basic unobserved effects models as Equation [13.2]. Instead of first differencing, we get rid of the unobserved individual effect $a_i$ using the within transformation:
 $$\begin{aligned}
y_{it} &= \beta_0 + \beta_1 x_{it1} + \cdots + \beta_k x_{itk} + a_i + u_{it}; \quad t = 1, \ldots, T; \quad i = 1, \ldots, n, \\
\bar{y}_i &= \beta_0 + \beta_1 \bar{x}_{i1} + \cdots + \beta_k \bar{x}_{ik} + a_i + \bar{u}_i \\
\ddot{y}_{it} &= y_{it} - \bar{y}_i = \beta_1 \ddot{x}_{it1} + \cdots + \beta_k \ddot{x}_{itk} + \ddot{u}_{it},
\end{aligned} \tag{14.1}$$
where $\bar{y}_i$ is the average of $y_{it}$ over time for cross-sectional unit $i$ and for the other variables accordingly. The within transformation subtracts these individual averages from the respective observations $y_{it}$. We already know how to conveniently calculate these demeaned variables like $\ddot{y}_{it}$ using the command `Within` from Section [13.4.](#panel-specific-computations)

The fixed effects (FE) estimator simply estimates the demeaned Equation [14.1] using pooled OLS. Instead of applying the within transformation to all variables and running `lm`, we can simply use `plm` on the original data with the option `model="within"`. This has the additional advantage that the degrees of freedom are adjusted to the demeaning and the variance-covariance matrix and standard errors are adjusted accordingly. We will come back to different ways to get the same estimates in Section [14.3.](#dummy-variable-regression-and-correlated-random-effects)

### Wooldridge, Example 14.2: Has the Return to Education Changed over Time?14.2
We estimate the change of the return to education over time using a fixed effects estimator. Script 14.1 (Example-14-2.R) shows the implementation. The data set WAGEPAN.dta is a balanced panel for $n = 545$ individuals over $T = 8$ years. It includes the index variables nr and year for individuals and years, respectively. Since educ does not change over time, we cannot estimate its overall impact. However, we can interact it with time dummies to see how the impact changes over time.

```
Script 14.1: Example-14-2.R

 library(plm)
 data(wagepan, package='wooldridge')
 # Generate pdata.frame:
 wagepan.p <- pdata.frame(wagepan, index=c("nr","year") )
 pdim(wagepan.p)

 # Estimate FE model
 summary( plm(lwage~married+union+factor(year)*educ, data=wagepan.p, model="within") )
```

## 14.2 Random Effects Models

We again base our analysis on the basic unobserved effects model in Equation [13.2]. The random effects (RE) model assumes that the unobserved effects $a_i$ are independent of (or at least uncorrelated with) the regressors $x_{itj}$ for all $t$ and $j = 1, \ldots, k$. Therefore, our main motivation for using FD or FE disappears: OLS consistently estimates the model parameters under this additional assumption.

However, like the situation with heteroscedasticity (see Section 8.3) and autocorrelation (see Section 12.2), we can obtain more efficient estimates if we take into account the structure of the variances and covariances of the error term. Wooldridge (2019, Section 14.2) shows that the GLS transformation that takes care of their special structure implied by the RE model leads to a quasi-demeaned specification
 $$y_{it}^\circ = y_{it} - \theta \bar{y}_i = \beta_0 (1 - /theta) + \beta_1 x_{it1}^\circ + \cdots + \beta_k x_{itk}^\circ + v_{it}^\circ, \tag{14.2}$$
where $y_{it}^\circ$ is similar to the demeaned $\ddot{y}_{it}$ from Equation [14.1] but subtracts only a fraction $\theta$ of the individual averages. The same holds for the regressors $x_{itj}$ and the composite error term $v_{it} = a_i + u_{it}$.

The parameter $\theta = 1 - \sqrt{\frac{\sigma_u^2}{\sigma_u^2 + T \sigma_a^2}}$ depends on the variances of $u_{it}$ and $a_i$ and the length of the time series dimension $T$. It is unknown and has to be estimated. Given our experience with FD and FE estimation, it should not come as a surprise that we can estimate the RE model parameters using the command `plm` with the option `model="random"`. Different versions of estimating the random effects parameter $\theta$ are implemented and can be chosen with the option `random.method`, see Croissant and Millo (2008) for details.

 Unlike with FD and FE estimators, we can include variables in our model that are constant over time for each cross-sectional unit. The command `pvar` provides a list of these variables as well as of those that do not vary within each point in time.

### Wooldridge, Example 14.4: A Wage Equation Using Panel Data14.4
The data set WAGEPAN.dta was already used in Example 14.2. Script 14.2 (Example-14-4-1.R) loads the data set and defines the panel structure. Then, we check the panel dimensions and get a list of time-constant variables using `pvar`. With these preparations, we get estimates using OLS, RE, and FE estimators in Script 14.3 (Example-14-4-2.R). We use `plm` with the options `pooling`, `random`, and `within`, respectively. We once again use `stargazer` to display the results, with additional options for labeling the estimates (`column.labels`), and selecting variables (`keep`) and statistics (`keep.stat`).

```
Script 14.2: Example-14-4-1.R

 library(plm);library(stargazer)
 data(wagepan, package='wooldridge')
 # Generate pdata.frame:
 wagepan.p <- pdata.frame(wagepan, index=c("nr","year") )
 pdim(wagepan.p)

 # Check variation of variables within individuals
 pvar(wagepan.p)

# Estimate different models
wagepan.p$yr<-factor(wagepan.p$year)
reg.ols<-(plm(lwage~educ+black+hisp+exper+I(exper^2)+married+union+yr,
             data=wagepan.p, model="pooling") )
reg.re <-(plm(lwage~educ+black+hisp+exper+I(exper^2)+married+union+yr,
             data=wagepan.p, model="random") )
reg.fe <- (plm(lwage~ I(exper^2)+married+union+yr,
             data=wagepan.p, model="within") )

# Pretty table of selected results (not reporting year dummies)
stargazer(reg.ols,reg.re,reg.fe, type="text",
          column.labels=c("OLS","RE","FE"),keep.stat=c("n","rsq"),
          keep=c("ed","bl","hi","exp","mar","un"))
```

 The RE estimator needs stronger assumptions to be consistent than the FE estimator. On the other hand, it is more efficient if these assumptions hold and we can include time constant regressors. A widely used test of this additional assumption is the Hausman test. It is based on the comparison between the FE and RE parameter estimates. Package ***plm*** offers the simple command `phtest` for automated testing. It expects both estimates and reports test results including the appropriate $p$ values.

 Script 14.4 (Example-HausmTest.R) uses the estimates obtained in Script 14.3 (Example-14-4-2.R) and stored in variables reg.re and reg.fe to run the Hausman test for this model. With the $p$ value of 0.0033, the null hypothesis that the RE model is consistent is clearly rejected with sensible significance levels like $\alpha = 5\%$ or $\alpha = 1\%$.

```
Script 14.4: Example-HausmTest.R

# Note that the estimates "reg.fe" and "reg.re" are calculated in
# Example 14.4. The scripts have to be run first.

# Hausman test of RE vs. FE:
 phtest(reg.fe, reg.re)
```

## 14.3 Dummy Variable Regression and Correlated Random Effects

 It turns out that we can get the FE parameter estimates in two other ways than the within transformation we used in Section [14.1.](#fixed-effects-estimation) The dummy variable regression uses OLS on the original variables in Equation [13.2] instead of the transformed ones. But it adds $n - 1$ dummy variables (or $n$ dummies and removes the constant), one for each cross-sectional unit $i = 1, \ldots, n$. The simplest (although not the computationally most efficient) way to implement this in $R$ is to use the cross-sectional index as another `factor` variable.

 The third way to get the same results is the correlated random effects (CRE) approach. Instead of assuming that the individual effects $a_i$ are independent of the regressors $x_{itj}$, we assume that they only depend on the averages over time $\bar{x}_{ij} = \frac{1}{T} \sum_{t=1}^{T} x_{itj}$:
 $α_i = γ_0 + γ_1 \bar x_{i1}+.... + γ_k \bar x_{ik}+r_i$
$y_{it} = \beta_0 + \beta_1 x_{it1} + \cdots + \beta_k x_{itk} + a_i + u_{it} \tag{14.4a}$ (14.3)
$y_{it} = \beta_0 + \gamma_0 + \beta_1 x_{it1} + \cdots + \beta_k x_{itk} + \gamma_1 \bar{x}_{i1} + \cdots + \gamma_k \bar{x}_{ik} + r_i + u_{it} \tag{14.4b}$ (14.4)

 If $r_i$ is uncorrelated with the regressors, we can consistently estimate the parameters of this model using the RE estimator. In addition to the original regressors, we include their averages over time. Remember from Section [13.4](#panel-specific-computations) that these averages are computed with the function `Between`.

Script 14.5 (Example-Dummy-CRE-1.R) uses WAGEPAN.dta again. We estimate the FE parameters using the within transformation (reg.fe), the dummy variable approach (reg.dum), and the CRE approach (reg.cre). We also estimate the RE version of this model (reg.re). Script 14.6 (Example-Dummy-CRE-2.R) produces the regression table using `stargazer`. The results confirm that the first three methods deliver exactly the same parameter estimates, while the RE estimates differ.

```
Script 14.5: Example-Dummy-CRE-1.R

library(plm);library(stargazer)
data(wagepan, package='wooldridge')
# Generate pdata.frame:
wagepan.p <- pdata.frame(wagepan, index=c("nr","year") )
# Estimate FE parameter in 3 different ways:
wagepan.p$yr<-factor(wagepan.p$year)
reg.fe <-(plm(lwage~married+union+year*educ,data=wagepan.p, model="within"))
reg.dum<- (lm(lwage~married+union+year*educ+factor(nr), data=wagepan.p))
reg.re <-(plm(lwage~married+union+year*educ,data=wagepan.p, model="random"))
reg.cre<-(plm(lwage~married+union+year*educ+Between(married)+Between(union)
             ,data=wagepan.p, model="random"))

stargazer(reg.fe,reg.dum,reg.cre,reg.re,type="text",model.names=FALSE,
          keep=c("married","union",":educ"),keep.stat=c("n","rsq"),
          column.labels=c("Within","Dummies","CRE","RE"))

```

 Given we have estimated the CRE model, it is easy to test the null hypothesis that the RE estimator is consistent. The additional assumptions needed are $\gamma_1 = \cdots = \gamma_k = 0$. They can easily be tested using an $F$ test as demonstrated in Script 14.7 (Example-CRE-test-RE.R). Like the Hausman test, we clearly reject the null hypothesis that the RE model is appropriate with a tiny $p$ value of about 0.00005.

```
Script 14.7: Example-CRE-test-RE.R

# Note that the estimates "reg.cre" are calculated in
# Script "Example-Dummy-CRE-1.R" which has to be run first.

# RE test as an F test on the "Between" coefficients
library(car)
 linearHypothesis(reg.cre, matchCoefs(reg.cre,"Between"))
```

 Another advantage of the CRE approach is that we can add time-constant regressors to the model. Since we cannot control for average values $\bar{x}_{ij}$ for these variables, they have to be uncorrelated with $a_i$ for consistent estimation of *their* coefficients. For the other coefficients of the time-varying variables, we still don't need these additional RE assumptions.

 Script 14.8 (Example-CRE2.R) estimates another version of the wage equation using the CRE approach. The variables married and union vary over time, so we can control for their between effects. The variables educ, black, and hisp do not vary. For a causal interpretation of *their* coefficients, we have to rely on uncorrelatedness with $a_i$. Given $a_i$ includes intelligence and other labor market success factors, this uncorrelatedness is more plausible for some variables (like gender or race) than for other variables (like education).

```
Script 14.8: Example-CRE2.R

library(plm)
data(wagepan, package='wooldridge')
# Generate pdata.frame:
wagepan.p <- pdata.frame(wagepan, index=c("nr","year") )
# Estimate CRE parameters
wagepan.p$yr<-factor(wagepan.p$year)
summary(plm(lwage~married+union+educ+black+hisp+Between(married)+
            Between(union), data=wagepan.p, model="random"))
```

## 14.4 Robust (Clustered) Standard Errors

We argued above that under the RE assumptions, OLS is inefficient but consistent. Instead of using RE, we could simply use OLS but would have to adjust the standard errors for the fact that the composite error term $v_{it} = a_i + u_{it}$ is correlated over time because of the constant individual effect $a_i$. In fact, the variance-covariance matrix could be more complex than the RE assumption with i.i.d. $u_{it}$ implies. These error terms could be serially correlated and/or heteroscedastic. This would invalidate the standard errors not only of OLS but also of FD, FE, RE, and CRE.

 There is an elegant solution, especially in panels with a large cross-sectional dimension. Similar to standard errors that are robust with respect to heteroscedasticity in cross-sectional data (Section 8.1) and serial correlation in time series (Section 12.3), there are formulas for the variance-covariance matrix for panel data that are robust with respect to heteroscedasticity and *arbitrary* correlations of the error term within a cross-sectional unit (or "cluster").

 These "clustered" standard errors are mentioned in Wooldridge (2019, Section 14.4 and Example 13.9). Different versions of the clustered variance-covariance matrix can be computed with the command `vcovHC` from the package ***plm***, see Croissant and Millo (2008) for details.[1](#_bookmark14) It works for all estimates obtained by `plm` and can be used as an input for regression tables using `coeftest` or `stargazer` or testing commands like `linearHypothesis`.

 Script 14.9 (Example-13-9-ClSE.R) repeats the FD regression from Example 13.9 but also reports the regression table with clustered standard errors and respective $t$ statistics in addition to the usual standard errors. Similar to the heteroscedasticity-robust standard errors discussed in Section 8.1, there are different versions of formulas for clustered standard errors. We first use the default type and then a type called `"sss"` (for "Stata small sample") that makes a particular small sample adjustment applied by Stata by default. These are the exact numbers reported by Wooldridge (2019).

1[1](#_bookmark14) Ne pas confondre avec `vcovHC` du package ***sandwich*** qui ne donne que des résultats robustes à l'hétéroscédasticité et a malheureusement le même nom.

```
Script 14.9: Example-13-9-ClSE.R

 library(plm);library(lmtest)
 data(crime4, package='wooldridge')
 # Generate pdata.frame:
 crime4.p <- pdata.frame(crime4, index=c("county","year") )
 # Estimate FD model:
 reg <- ( plm(log(crmrte)~d83+d84+d85+d86+d87+lprbarr+lprbconv+
               lprbpris+lavgsen+lpolpc,data=crime4.p, model="fd") )
 # Regression table with standard SE
 coeftest(reg)

 # Regression table with "clustered" SE (default type HC0):
 coeftest(reg, vcovHC)

 # Regression table with "clustered" SE (small-sample correction)
 # This is the default version used by Stata and reported by Wooldridge:
 coeftest(reg, vcovHC(reg, type="sss"))
```

# 15. Instrumental Variables Estimation and Two Stage Least Squares

 Instrumental variables are potentially powerful tools for the identification and estimation of causal effects. We start the discussion in Section [15.1](#instrumental-variables-in-simple-regression-models) with the simplest case of one endogenous regressor and one instrumental variable. Section [15.2](#more-exogenous-regressors) shows how to implement models with additional exogenous regressors. In Section [15.3,](#two-stage-least-squares) we will introduce two stage least squares which efficiently deals with several endogenous variables and several instruments.

 Tests of the exogeneity of the regressors and instruments are presented in Sections [15.4](#testing-for-exogeneity-of-the-regressors) and [15.5,](#testing-overidentifying-restrictions) respectively. Finally, Section [15.6](#instrumental-variables-with-panel-data) shows how to conveniently combine panel data estimators with instrumental variables.

## 15.1 Instrumental Variables in Simple Regression Models

 We start the discussion of instrumental variables (IV) regression with the most straightforward case of only one regressor and only one instrumental variable. Consider the simple linear regression model for cross-sectional data
 $$y = \beta_0 + \beta_1 x + u. \tag{15.1}$$
 The OLS estimator for the slope parameter is $\hat{\beta}_1^{OLS} = \frac{\text{Cov}(x,y)}{\text{Var}(x)}$, see Equation 2.3. Suppose the regressor $x$ is correlated with the error term $u$, so OLS parameter estimators will be biased and inconsistent.

 If we have a valid instrumental variable $z$, we can consistently estimate $\beta_1$ using the IV estimator
 $$\hat{\beta}_1^{IV} = \frac{\text{Cov}(z, y)}{\text{Cov}(z, x)}. \tag{15.2}$$

 A valid instrument is correlated with the regressor $x$ ("relevant"), so the denominator of Equation [15.2] is nonzero. It is also uncorrelated with the error term $u$ ("exogenous"). Wooldridge (2019, Section 15.1) provides more discussion and examples.

 To implement IV regression in $R$, the package ***AER*** offers the convenient command `ivreg`. It works similar to `lm`. In the formula specification, the regressor(s) are separated from the instruments with a vertical line `|` (like in "conditional on $z$"):
 `ivreg( y ~ x | z )`

 Note that we can easily deal with heteroscedasticity: Results obtained by `ivreg` can be directly used with robust standard errors from `hccm` (Package ***car***) or `vcovHC` (package ***sandwich***), see Section 8.1.

### Wooldridge, Example 15.1: Return to Education for Married Women15.1
 Script 15.1 (Example-15-1.R) uses data from MROZ.dta. We only analyze women with non-missing wage, so we extract a `subset` from our data. We want to estimate the return to education for these women. As an instrumental variable for education, we use the education of her father fatheduc.

 First, we calculate the OLS and IV slope parameters according to Equations 2.3 and [15.2,](#_bookmark17) respectively. Remember that the `with` command defines that all variables names refer to our data frame oursample. Then, the full OLS and IV estimates are calculated using the boxed routines `lm` and `ivreg`, respectively. The results are once again displayed using `stargazer`. Not surprisingly, the slope parameters match the manual results.

```
Script 15.1: Example-15-1.R

 library(AER);library(stargazer)
 data(mroz, package='wooldridge')
 # restrict to non-missing wage observations
 oursample <- subset(mroz, !is.na(wage))
 # OLS slope parameter manually
 with(oursample, cov(log(wage),educ) / var(educ) )

 # IV slope parameter manually
 with(oursample, cov(log(wage),fatheduc) / cov(educ,fatheduc) )

 # OLS automatically
 reg.ols <- lm(log(wage) ~ educ, data=oursample)
 
 # IV automatically
 reg.iv <- ivreg(log(wage) ~ educ | fatheduc, data=oursample)
 
 # Pretty regression table
 stargazer(reg.ols,reg.iv, type="text")
```

## 15.2 More Exogenous Regressors

 The IV approach can easily be generalized to include additional exogenous regressors, i.e. regressors that are assumed to be unrelated to the error term. In `ivreg`, we have to include these variables both to the list of regressors left of the `|` symbol and to the list of exogenous instrument to the right of the `|` symbol.

### Wooldridge, Example 15.4: Using College Proximity as an IV for Education15.4
 In Script 15.2 (Example-15-4.R), we use CARD.dta to estimate the return to education. Education is allowed to be endogenous and instrumented with the dummy variable nearc4 which indicates whether the individual grew up close to a college. In addition, we control for experience, race, and regional information. These variables are assumed to be exogenous and act as their own instruments.

 We first check for relevance by regressing the endogenous independent variable educ on all exogenous variables including the instrument nearc4. Its parameter is highly significantly different from zero, so relevance is supported. We then estimate the log wage equation with OLS and IV. All results are displayed in one table with `stargazer`.

```
Script 15.2: Example-15-4.R

 library(AER);library(stargazer)
 data(card, package='wooldridge')
 # Checking for relevance: reduced form
 redf<-lm(educ ~ nearc4+exper+I(exper^2)+black+smsa+south+smsa66+reg662+
            reg663+reg664+reg665+reg666+reg667+reg668+reg669, data=card)
 # OLS
 ols<-lm(log(wage)~educ+exper+I(exper^2)+black+smsa+south+smsa66+reg662+
           reg663+reg664+reg665+reg666+reg667+reg668+reg669, data=card)
 # IV estimation
 iv <-ivreg(log(wage)~educ+exper+I(exper^2)+black+smsa+south+smsa66+
              reg662+reg663+reg664+reg665+reg666+reg667+reg668+reg669
              | nearc4+exper+I(exper^2)+black+smsa+south+smsa66+
                reg662+reg663+reg664+reg665+reg666+reg667+reg668+reg669
              , data=card)
 # Pretty regression table of selected coefficients
 stargazer(redf,ols,iv,type="text",
            keep=c("ed","near","exp","bl"),keep.stat=c("n","rsq"))

```

## 15.3 Two Stage Least Squares

 Two stage least squares (2SLS) is a general approach for IV estimation when we have one or more endogenous regressors and at least as many additional instrumental variables. Consider the regression model
 $y_1 = \beta_0 + \beta_1 y_2 + \beta_2 y_3 + \beta_3 z_1 + \beta_4 z_2 + \beta_5 z_3 + u_1 \tag{15.3}$
 The regressors $y_2$ and $y_3$ are potentially correlated with the error term $u_1$, the regressors $z_1$, $z_2$, and $z_3$ are assumed to be exogenous. Because we have two endogenous regressors, we need at least two additional instrumental variables, say $z_4$ and $z_5$.

 The name of 2SLS comes from the fact that it can be performed in two stages of OLS regressions:

1.  Separately regress $y_2$ and $y_3$ on $z_1$ through $z_5$. Obtain fitted values $\hat{y}_2$ and $\hat{y}_3$.
2.  Regress $y_1$ on $\hat{y}_2$, $\hat{y}_3$, and $z_1$ through $z_3$.

 If the instruments are valid, this will give consistent estimates of the parameters $\beta_0$ through $\beta_5$. Generalizing this to more endogenous regressors and instrumental variables is obvious.

 This procedure can of course easily be implemented in $R$, remembering that fitted values are obtained with `fitted` which can be directly called from the `formula` of `lm`. One of the problems of this manual approach is that the resulting variance-covariance matrix and analyses based on them are invalid. Conveniently, `ivreg` will automatically do these calculations and calculate correct standard errors and the like.

### Wooldridge, Example 15.5: Return to Education for Working Women15.5
 We continue Example 15.1 and still want to estimate the return to education for women using the data in MROZ.dta. Now, we use both mother's and father's education as instruments for their own education. In Script 15.3 (Example-15-5.R), we obtain 2SLS estimates in two ways: First, we do both stages manually, including fitted education as `fitted(stage1)` as a regressor in the second stage. `ivreg` does this automatically and delivers the same parameter estimates as the output table reveals. But the standard errors differ slightly because the manual two stage version did not correct them.

```
Script 15.3: Example-15-5.R

 library(AER);library(stargazer)
 data(mroz, package='wooldridge')
 # restrict to non-missing wage observations
 oursample <- subset(mroz, !is.na(wage))
 # 1st stage: reduced form
 stage1 <- lm(educ~exper+I(exper^2)+motheduc+fatheduc, data=oursample)
 # 2nd stage
 man.2SLS<-lm(log(wage)~fitted(stage1)+exper+I(exper^2), data=oursample)
 # Automatic 2SLS estimation
 aut.2SLS<-ivreg(log(wage)~educ+exper+I(exper^2)
                 | motheduc+fatheduc+exper+I(exper^2) , data=oursample)
 # Pretty regression table
 stargazer(stage1,man.2SLS,aut.2SLS,type="text",keep.stat=c("n","rsq"))
```

## 15.4. Testing for Exogeneity of the Regressors

 There is another way to get the same IV parameter estimates as with 2SLS. In the same setup as above, this "control function approach" also consists of two stages:

1.  Like in 2SLS, regress $y_2$ and $y_3$ on $z_1$ through $z_5$. Obtain residuals $\hat{v}_2$ and $\hat{v}_3$ instead of fitted values $\hat{y}_2$ and $\hat{y}_3$.
2.  Regress $y_1$ on $y_2$, $y_3$, $z_1$, $z_2$, $z_3$, and the first stage residuals $\hat{v}_2$ and $\hat{v}_3$.

 This approach is as simple to implement as 2SLS and will also result in the same parameter estimates and invalid OLS standard errors in the second stage (unless the dubious regressors $y_2$ and $y_3$ are in fact exogenous).

 After this second stage regression, we can test for exogeneity in a simple way assuming the instruments are valid. We just need to do a $t$ or $F$ test of the null hypothesis that the parameters of the first-stage residuals are equal to zero. If we reject this hypothesis, this indicates endogeneity of $y_2$ and $y_3$.

### Wooldridge, Example 15.7: Return to Education for Working Women15.7
 In Script 15.4 (Example-15-7.R), we continue Example 15.5 using the control function approach. Again, we use both mother's and father's education as instruments. The first stage regression is identical as in Script 15.3 (Example-15-5.R). The second stage adds the first stage residuals to the original list of regressors. The parameter estimates are identical to both the manual 2SLS and the automatic `ivreg` results. We can directly interpret the $t$ test from the regression table as a test for exogeneity. Here, $t = 1.6711$ with a two-sided $p$ value of $p = 0.095$, indicating a marginally significant evidence for endogeneity.

```
Script 15.4: Example-15-7.R

 library(AER);library(lmtest)
 data(mroz, package='wooldridge')
 # restrict to non-missing wage observations
 oursample <- subset(mroz, !is.na(wage))
 # 1st stage: reduced form
 stage1<-lm(educ~exper+I(exper^2)+motheduc+fatheduc, data=oursample)
 # 2nd stage
 stage2<-lm(log(wage)~educ+exper+I(exper^2)+resid(stage1),data=oursample)
 # results including t tests
 coeftest(stage2)
```

## 15.5. Testing Overidentifying Restrictions

 If we have more instruments than endogenous variables, we can use either all or only some of them. If all are valid, using all improves the accuracy of the 2SLS estimator and reduces its standard errors. If the exogeneity of some is dubious, including them might cause inconsistency. It is therefore useful to test for the exogeneity of a set of dubious instruments if we have another (large enough) set that is undoubtedly exogenous. The procedure is described by Wooldridge (2019, Section 15.5):

1.  Estimate the model by 2SLS and obtain residuals $\hat{u}_1$.
2.  Regress $\hat{u}_1$ on all exogenous variables and calculate $R_1^2$.
3.  The test statistic $n R_1^2$ is asymptotically distributed as $\chi_q^2$, where $q$ is the number of *overidentifying* restrictions, i.e. number of instruments minus number of endogenous regressors.

### Wooldridge, Example 15.8: Return to Education for Working Women15.8
 We will again use the data and model of Examples 15.5 and 15.7. Script 15.5 (Example-15-8.R) estimates the model using `ivreg`. The results are stored in variable res.2sls and their `summary` is printed. We then run the auxiliary regression (2) and compute its $R^2$ as r2. The test statistic is computed to be teststat=0.378. We also compute the $p$ value from the $\chi_1^2$ distribution. We cannot reject exogeneity of the instruments using this test. But be aware of the fact that the underlying assumption that at least one instrument is valid might be violated here.

## 15.6. Instrumental Variables with Panel Data

 Instrumental variables can be used for panel data, too. In this way, we can get rid of time-constant individual heterogeneity by first differencing or within transformations and then fix remaining endogeneity problems with instrumental variables.

 We know how to get panel data estimates using OLS on the transformed data, so we can easily use IV as before. But we can do it even more conveniently: The `plm` command from the ***plm*** package allows to directly enter instruments. As with `ivreg`, we can simply add a list of instruments after the `|` sign in the formula.

### Wooldridge, Example 15.10: Job Training and Worker Productivity15.10
 We use the data set JTRAIN.dta to estimate the effect of job training hrsemp on the scrap rate. In Script 15.6 (Example-15-10.R), we load the data, choose a `subset` of the years 1987 and 1988 and store the data as a `pdata.frame` using the index variables fcode and year, see Section [13.3.](#organizing-panel-data) Then we estimate the parameters using first-differencing with the instrumental variable grant.
 ```
Script 15.5: Example-15-8.R

 library(AER)
 data(mroz, package='wooldridge')
 # restrict to non-missing wage observations
 oursample <- subset(mroz, !is.na(wage))
 # IV regression
 summary( res.2sls <- ivreg(log(wage) ~ educ+exper+I(exper^2)
                            | exper+I(exper^2)+motheduc+fatheduc,data=oursample) )

-------------
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
Residual standard error: 0.6747 on 424 degrees of freedom
Multiple R-Squared: 0.1357,	Adjusted R-squared: 0.1296
Wald test: 8.141 on 3 and 424 DF,  p-value: 2.787e-05
-------------
 # Auxiliary regression
 res.aux <- lm(resid(res.2sls) ~ exper+I(exper^2)+motheduc+fatheduc
                , data=oursample)
 # Calculations for test
 ( r2 <- summary(res.aux)$r.squared )

 ( n <- nobs(res.aux) )

 ( teststat <- n*r2 )

 ( pval <- 1-pchisq(teststat,1) )
 ```
 
```
Script 15.6: Example-15-10.R
 library(plm)
 data(jtrain, package='wooldridge')
 # Define panel data (for 1987 and 1988 only)
 jtrain.87.88 <- subset(jtrain,year<=1988)
 jtrain.p<-pdata.frame(jtrain.87.88, index=c("fcode","year"))
 # IV FD regression
 summary( plm(log(scrap)~hrsemp|grant, model="fd",data=jtrain.p) )
```

# 16. Simultaneous Equations Models

 In simultaneous equations models (SEM), both the dependent variable and at least one regressor are determined jointly. This leads to an endogeneity problem and inconsistent OLS parameter estimators. The main challenge for successfully using SEM is to specify a sensible model and make sure it is identified, see Wooldridge (2019, Sections 16.1--16.3). We briefly introduce a general model and the notation in Section [16.1.](#setup-and-notation)

 As discussed in Chapter [15,](#instrumental-variables-estimation-and-two-stage-least-squares) 2SLS regression can solve endogeneity problems if there are enough exogenous instrumental variables. This also works in the setting of SEM, an example is given in Section [16.2.](#estimation-by-2sls) For estimating the whole system simultaneously, specialized commands such as `systemfit` in $R$ can be handy. It is demonstrated in Section [16.3.](#joint-estimation-of-system) Using this package, more advanced estimation commands are straightforward to implement. We will show this for three-stage-least-squares (3SLS) estimation in Section [16.4.](#outlook-estimation-by-3sls)

## 16.1. Setup and Notation

 Consider the general SEM with $q$ endogenous variables $y_1, \ldots, y_q$ and $k$ exogenous variables $x_1, \ldots, x_k$. The system of equations is
 $$\begin{aligned}
y_1 &= \alpha_{12} y_2 + \alpha_{13} y_3 + \cdots + \alpha_{1q} y_q + \beta_{10} + \beta_{11} x_1 + \cdots + \beta_{1k} x_k + u_1 \\
y_2 &= \alpha_{21} y_1 + \alpha_{23} y_3 + \cdots + \alpha_{2q} y_q + \beta_{20} + \beta_{21} x_1 + \cdots + \beta_{2k} x_k + u_2 \\
&\vdots \\
y_q &= \alpha_{q1} y_1 + \alpha_{q2} y_2 + \cdots + \alpha_{q,q-1} y_{q-1} + \beta_{q0} + \beta_{q1} x_1 + \cdots + \beta_{qk} x_k + u_q
\end{aligned}$$

 As discussed in more detail in Wooldridge (2019, Section 16), this system is not identified without restrictions on the parameters. The order condition for identification of any equation is that if we have $m$ included endogenous regressors (i.e. $/alpha$ parameters that are not restricted to 0), we need to exclude at least $m$ exogenous regressors (i.e. restrict their $/beta$ parameters to 0). They can then be used as instrumental variables.

### Wooldridge, Example 16.3: Labor Supply of Married, Working Women16.3

 We have the two endogenous variables hours and wage which influence each other.
 $$\begin{aligned}
\text{hours} &= \alpha_{12} \log(/text{wage}) + \beta_{10} + \beta_{11} \text{educ} + \beta_{12} \text{age} + \beta_{13} \text{kidslt6} + \beta_{14} \text{nwifeinc} + \beta_{15} \text{exper} + \beta_{16} \text{exper}^2 + u_1 \\
\log(/text{wage}) &= \alpha_{21} \text{hours} + \beta_{20} + \beta_{21} \text{educ} + \beta_{22} \text{age} + \beta_{23} \text{kidslt6} + \beta_{24} \text{nwifeinc} + \beta_{25} \text{exper} + \beta_{26} \text{exper}^2 + u_2
\end{aligned}$$

 For both equations to be identified, we have to exclude at least one exogenous regressor from each equation. Wooldridge (2019) discusses a model in which we restrict $\beta_{15} = \beta_{16} = 0$ in the first and $\beta_{22} = \beta_{23} = \beta_{24} = 0$ in the second equation.

## 16.2 Estimation by 2SLS

 Estimation of each equation separately by 2SLS is straightforward once we have set up the system and ensured identification. The excluded regressors in each equation serve as instrumental variables. As shown is Chapter [15,](#instrumental-variables-estimation-and-two-stage-least-squares) the command `ivreg` from the package ***AER*** provides convenient 2SLS estimation.

### Wooldridge, Example 16.5: Labor Supply of Married, Working Women16.5

 Script 16.1 (Example-16-5-ivreg.R) estimates the parameters of the two equations from Example 16.3 separately using `ivreg`.

```
Script 16.1: Example-16-5-ivreg.R

 library(AER)
 data(mroz, package='wooldridge')
 oursample <- subset(mroz,!is.na(wage))
 # 2SLS regressions
 summary( ivreg(hours~log(wage)+educ+age+kidslt6+nwifeinc
                |educ+age+kidslt6+nwifeinc+exper+I(exper^2), data=oursample))

 summary( ivreg(log(wage)~hours+educ+exper+I(exper^2)
                |educ+age+kidslt6+nwifeinc+exper+I(exper^2), data=oursample))
```

## 16.3. Joint Estimation of System

 Instead of manual estimation of each equation by `ivreg`, we can make use of the specialized command `systemfit` from the package ***systemfit***. It is more convenient to use and offers straightforward implementation of additional estimators. We define the system of equations as a `list` of formulas. Script 16.2 (Example-16-5-systemfit-prep.R) does this by first storing each equation as a formula and then combining them in the list eq.system. We also need to define the set of exogenous regressors and instruments using a formula with a right-hand side only. Script 16.2 (Example-16-5-systemfit-prep.R) stores this specification in the variable instrum.

 With these preparations, `systemfit` is simply called with the equation system and the instrument set as arguments. Option `method="2SLS"` requests 2SLS estimation. As expected, the results produced by Script 16.3 (Example-16-5-systemfit.R) are the same as with the separate `ivreg` regressions seen previously.

```
Script 16.2: Example-16-5-systemfit-prep.R

library(systemfit)
data(mroz, package='wooldridge')
oursample <- subset(mroz,!is.na(wage))
# Define system of equations and instruments
eq.hrs <- hours ~ log(wage)+educ+age+kidslt6+nwifeinc
eq.wage <- log(wage)~ hours +educ+exper+I(exper^2)
eq.system<- list(eq.hrs, eq.wage)
instrum <- ~educ+age+kidslt6+nwifeinc+exper+I(exper^2)

# 2SLS of whole system (run Example-16-5-systemfit-prep.R first!)
 summary(systemfit(eq.system,inst=instrum,data=oursample,method="2SLS"))
```

## 16.4. Outlook: Estimation by 3SLS

 The results of `systemfit` provides additional information, see the Script 16.3 (Example-16-5-systemfit.R). An interesting piece of information is the correlation between the residuals of the equations. In the example, it is reported to be a substantially negative -0.90. We can account for the correlation between the error terms to derive a potentially more efficient parameter estimator than 2SLS. Without going into details here, the three stage least squares (3SLS) estimator adds another stage to 2SLS by estimating the correlation and accounting for it using a FGLS approach. For a detailed discussion of this and related methods, see for example Wooldridge (2010, Chapter 8).

 Using 3SLS in $R$ is simple: Option `method="3SLS"` of `systemfit` is all we need to do as the output of Script 16.4 (Example-16-5-3sls.R) shows.

```
Script 16.4: Example-16-5-3sls.R

# 3SLS of whole system (run Example-16-5-systemfit-prep.R first!)
 summary(systemfit(eq.system,inst=instrum,data=oursample,method="3SLS"))
```

# 17. Limited Dependent Variable Models and Sample Selection Corrections

 A limited dependent variable (LDV) can only take a limited set of values. An extreme case is a binary variable that can only take two values. We already used such dummy variables as regressors in Chapter 7. Section [17.1](#binary-responses) discusses how to use them as dependent variables. Another example for LDV are counts that take only non-negative integers, they are covered in Section [17.2.](#count-data-the-poisson-regression-model) Similarly, Tobit models discussed in Section [17.3](#corner-solution-responses-the-tobit-model) deal with dependent variables that can only take positive values (or are restricted in a similar way), but are otherwise continuous.

 Sections [17.4](#censored-and-truncated-regression-models) and [17.5](#sample-selection-corrections) are concerned with dependent variables that are continuous but not perfectly observed. For some units of the censored, truncated, or selected observations we only know that they are above or below a certain threshold or we don't know anything about them.

## 17.1 Binary Responses

 Binary dependent variables are frequently studied in applied econometrics. Because a dummy variable $y$ can only take the values 0 and 1, its (conditional) expected value is equal to the (conditional) probability that $y = 1$:
 $$\text{E}(y|/mathbf{x}) = 0 \cdot \text{P}(y = 0|/mathbf{x}) + 1 \cdot \text{P}(y = 1|/mathbf{x}) = \text{P}(y = 1|/mathbf{x}) \tag{17.1}$$
 So when we study the conditional mean, it makes sense to think about it as the probability of outcome $y = 1$. Likewise, the predicted value $\hat{y}$ should be thought of as a predicted probability.

### 17.1.1. Linear Probability Models

 If a dummy variable is used as the dependent variable $y$, we can still use OLS to estimate its relation to the regressors $\mathbf{x}$. These linear probability models are covered by Wooldridge (2019) in Section 7.5.

 If we write the usual linear regression model
 $$y = \beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k + u \tag{17.2}$$
 and make the usual assumptions, especially MLR.4: $\text{E}(u | /mathbf{x}) = 0$, this implies for the conditional mean (which is the probability that $y = 1$) and the predicted probabilities
 $$\text{P}(y = 1|/mathbf{x}) = \text{E}(y|/mathbf{x}) = \beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k \tag{17.3}$$
 $$\hat{\text{P}} (y = 1|/mathbf{x}) = \hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x_1 + \cdots + \hat{\beta}_k x_k \tag{17.4}$$

 The interpretation of the parameters is straightforward: $\beta_j$ is a measure of the average change in probability of a "success" ($y = 1$) as $x_j$ increases by one unit and the other determinants remain constant. Linear probability models automatically suffer from heteroscedasticity, so with OLS, we should use heteroscedasticity-robust inference, see Section 8.1.

### Wooldridge, Example 17.1: Married Women's Labor Force Participation17.1
 We study the probability that a woman is in the labor force depending on socio-demographic characteristics. Script 17.1 (Example-17-1-1.R) estimates a linear probability model using the data set mroz.dta. The estimated coefficient of educ can be interpreted as: an additional year of schooling increases the probability that a woman is in the labor force *ceteris paribus* by 0.038 on average.

```
Script 17.1: Example-17-1-1.R

 library(car); library(lmtest) # for robust SE
 data(mroz, package='wooldridge')
 # Estimate linear probability model
 linprob <- lm(inlf~nwifeinc+educ+exper+I(exper^2)+age+kidslt6+kidsge6,data=mroz)
 # Regression table with heteroscedasticity-robust SE and t tests:
 coeftest(linprob,vcov=hccm)
```

 One problem with linear probability models is that $\text{P}(y = 1 | /mathbf{x})$ is specified as a linear function of the regressors. By construction, there are (more or less realistic) combinations of regressor values that yield $\hat{y} < 0$ or $\hat{y}  1$. Since these are probabilities, this does not really make sense.

 As an example, Script 17.2 (Example-17-1-2.R) calculates the predicted values for two women (see Section 6.2 for how to `predict` after OLS estimation): Woman 1 is 20 years old, has no work experience, 5 years of education, two children below age 6 and has additional family income of 100,000 USD. Woman 2 is 52 years old, has 30 years of work experience, 17 years of education, no children and no other source of income. The predicted "probability" for woman 1 is -41%, the probability for woman 2 is 104% as can also be easily checked with a calculator.

```
Script 17.2: Example-17-1-2.R

# predictions for two "extreme" women (run Example-17-1-1.R first!):
 xpred <- list(nwifeinc=c(100,0),educ=c(5,17),exper=c(0,30),
                age=c(20,52),kidslt6=c(2,0),kidsge6=c(0,0))
 predict(linprob,xpred)

```

### 17.1.2. Logit and Probit Models: Estimation

 Specialized models for binary responses make sure that the implied probabilities are restricted between 0 and 1. An important class of models specifies the success probability as
 $$\text{P}(y = 1|/mathbf{x}) = G(/beta_0 + /beta_1 x_1 + /cdots + /beta_k x_k) = G(/mathbf{x}/boldsymbol{/beta}) \tag{17.5}$$
 where the "link function" $G(z)$ always returns values between 0 and 1. In the statistics literature, this type of models is often called generalized linear model (GLM) because a linear part $\mathbf{x}\boldsymbol{\beta}$ shows up within the nonlinear function $G$.

 For binary response models, by far the most widely used specifications for $G$ are
 *   the **probit** model with $G(z) = \Phi(z)$, the standard normal cdf and
 *   the **logit** model with $G(z) = \Lambda(z) = \frac{\exp(z)}{1+\exp(z)}$, the cdf of the logistic distribution.

 Wooldridge (2019, Section 17.1) provides useful discussions of the derivation and interpretation of these models. Here, we are concerned with the practical implementation. In $R$, many generalized linear models can be estimated with the command `glm` which works similar to `lm`. It accepts the additional option
 *   `family=binomial(link=logit)` for the logit model or
 *   `family=binomial(link=probit)` for the probit model.

 Maximum likelihood estimation (MLE) of the parameters is done automatically and the `summary` of the results contains the most important regression table and additional information. Scripts 17.3 (Example-17-1-3.R) and 17.4 (Example-17-1-4.R) implement this for the logit and probit model, respectively. The log likelihood value $L(/hat{/boldsymbol{/beta}})$ is not reported by default but can be requested with the function `logLik`. Instead, a statistic called Residual deviance is reported in the standard output. It is simply defined as $D(/hat{/boldsymbol{/beta}}) = -2L(/hat{/boldsymbol{/beta}})$. Null deviance means $D_0 = -2L_0$ where $L_0$ is the likelihood of a model with an intercept only.

 The two deviance statistics can be accessed for additional calculations from a stored result res with `res$deviance` and `res$null.deviance`. Scripts 17.3 (Example-17-1-3.R) and 17.4 (Example-17-1-4.R) demonstrate the calculation of different statistics derived from these results.

 McFadden's pseudo R-squared can be calculated as
 $$\text{pseudo } R^2 = 1 - \frac{L(/hat{/boldsymbol{/beta}})}{L_0} = 1 - \frac{D(/hat{/boldsymbol{/beta}})}{D_0}. \tag{17.6}$$

```
Script 17.3: Example-17-1-3.R

 data(mroz, package='wooldridge')
 # Estimate logit model
 logitres<-glm(inlf~nwifeinc+educ+exper+I(exper^2)+age+kidslt6+kidsge6,
                family=binomial(link=logit),data=mroz)
 # Summary of results:
 summary(logitres)

 # Log likelihood value:
 logLik(logitres)

 # McFadden's pseudo R2:
 1 - logitres$deviance/logitres$null.deviance

```

```
Script 17.4: Example-17-1-4.R

 data(mroz, package='wooldridge')
 # Estimate probit model
 probitres<-glm(inlf~nwifeinc+educ+exper+I(exper^2)+age+kidslt6+kidsge6,
                 family=binomial(link=probit),data=mroz)
 # Summary of results:
 summary(probitres)

 # Log likelihood value:
 logLik(probitres)

 # McFadden's pseudo R2:
 1 - probitres$deviance/probitres$null.deviance

```

### 17.1.3 Inference

 The `summary` output of fitted `glm` results contains a standard regression table with parameters and (asymptotic) standard errors. The next column is labeled z value instead of t value in the output of `lm`. The interpretation is the same. The difference is that the standard errors only have an asymptotic foundation and the distribution used for calculating $p$ values is the standard normal distribution (which is equal to the $t$ distribution with very large degrees of freedom). The bottom line is that tests for single parameters can be done as before, see Section 4.1.

 For testing multiple hypotheses similar to the $F$ test (see Section 4.3), the likelihood ratio test is popular. It is based on comparing the log likelihood values of the unrestricted and the restricted model. The test statistic is
 $$LR = 2(L_{ur} - L_r) = D_r - D_{ur} \tag{17.7}$$
 where $L_{ur}$ and $L_r$ are the log likelihood values of the unrestricted and restricted model, respectively, and $D_{ur}$ and $D_r$ are the corresponding reported deviance statistics. Under $H_0$, the $LR$ test statistic is asymptotically distributed as $\chi^2$ with the degrees of freedom equal to the number of restrictions to be tested. The test of overall significance is a special case just like with $F$-tests. The null hypothesis is that all parameters except the constant are equal to zero. With the notation above, the test statistic is
 $$LR = 2\left[ L(/hat{/boldsymbol{/beta}}) - L_0 \right] = D_0 - D(/hat{/boldsymbol{/beta}}). \tag{17.8}$$

 Translated to $R$ with fitted model results stored in res, this corresponds to
 `LR = res$null.deviance - res$deviance`

 The package ***lmtest*** also offers the LR test as the function `lrtest` including the convenient calculation of $p$ values. The syntax is
 *   `lrtest(res)` for a test of overall significance for model res
 *   `lrtest(restr, unrestr)` for a test of the restricted model restr vs. the unrestricted model unrestr

 Script 17.5 (Example-17-1-5.R) implements the test of overall significance for the probit model using both manual and automatic calculations. It also tests the joint null hypothesis that experience and age are irrelevant by first estimating the restricted model and then running the automated LR test.

```
Script 17.5: Example-17-1-5.R

# Test of overall significance:
# Manual calculation of the LR test statistic:
 probitres$null.deviance - probitres$deviance

# Automatic calculations including p-values,...:
 library(lmtest)
 lrtest(probitres)
 

# Test of H0: experience and age are irrelevant
 restr <- glm(inlf~nwifeinc+educ+ kidslt6+kidsge6,
                family=binomial(link=probit),data=mroz)
 lrtest(restr,probitres)

```

### 17.1.4. Predictions

 The command `predict` can calculate predicted values for the estimation sample ("fitted values") or arbitrary sets of regressor values also for binary response models estimated with `glm`. Given the results are stored in variable res, we can calculate
 *   $\mathbf{x}_i \hat{\boldsymbol{\beta}}$ for the estimation sample with `predict(res)`
 *   $\mathbf{x}_i \hat{\boldsymbol{\beta}}$ for the regressor values stored in xpred with `predict(res, xpred)`
 *   $\hat{y} = G(/mathbf{x}_i /hat{/boldsymbol{/beta}})$ for the estimation sample with `predict(res, type = "response")`
 *   $\hat{y} = G(/mathbf{x}_i /hat{/boldsymbol{/beta}})$ for the regressor values stored in xpred with `predict(res, xpred, type = "response")`

 The predictions for the two hypothetical women introduced in Section [17.1.1](#linear-probability-models) are repeated for the linear probability, logit, and probit models in Script 17.6 (Example-17-1-6.R). Unlike the linear probability model, the predicted probabilities from the logit and probit models remain between 0 and 1.

```
Script 17.6: Example-17-1-6.R

# Predictions from linear probability, probit and logit model:
# (run 17-1-1.R through 17-1-4.R first to define the variables!)
 predict(linprob, xpred,type = "response")

 predict(logitres, xpred,type = "response")

 predict(probitres,xpred,type = "response")
```

**Figure 17.1.** Predictions from binary response models (simulated data)
 *Légende : Graphique montrant les probabilités prédites en fonction de x pour les modèles de probabilité linéaire, logit et probit. Les modèles logit et probit restent entre 0 et 1, contrairement au modèle linéaire.*

 If we only have one regressor, predicted values can nicely be plotted against it. Figure [17.1](#_bookmark29) shows such a figure for a simulated data set. For interested readers, the script used for generating the data and the figure is printed as Script 17.7 (Binary-Predictions.R) in Appendix IV (p. 351). In this example, the linear probability model clearly predicts probabilities outside of the "legal" area between 0 and 1. The logit and probit models yield almost identical predictions. This is a general finding that holds for most data sets.

### 17.1.5. Partial Effects

 The parameters of linear regression models have straightforward interpretations: $\beta_j$ measures the *ceteris paribus* effect of $x_j$ on $\text{E}(y|/mathbf{x})$. The parameters of nonlinear models like logit and probit have a less straightforward interpretation since the linear index $\mathbf{x}\boldsymbol{\beta}$ affects $\hat{y}$ through the link function $G$.

 A useful measure of the influence is the partial effect (or marginal effect) which in a graph like Figure [17.1](#_bookmark29) is the slope and has the same interpretation as the parameters in the linear model. Because of the chain rule, it is
 $$\frac{\partial \hat{y}}{\partial x_j} = \frac{\partial G(/hat{/beta}_0 + /hat{/beta}_1 x_1 + /cdots + /hat{/beta}_k x_k)}{\partial x_j} = \hat{\beta}_j \cdot g(/hat{/beta}_0 + /hat{/beta}_1 x_1 + /cdots + /hat{/beta}_k x_k), \tag{17.9}$$
 where $g(z)$ is the derivative of the link function $G(z)$. So
 *   for the probit model, the partial effect is $\frac{\partial \hat{y}}{\partial x_j} = \hat{\beta}_j \cdot \phi(/mathbf{x}/hat{/boldsymbol{/beta}})$
 *   for the logit model, it is $\frac{\partial \hat{y}}{\partial x_j} = \hat{\beta}_j \cdot \lambda(/mathbf{x}/hat{/boldsymbol{/beta}})$
 where $\phi(z)$ and $\lambda(z)$ are the pdfs of the standard normal and the logistic distribution, respectively.

 The partial effect depends on the value of $\mathbf{x}\hat{\boldsymbol{\beta}}$. The pdfs have the famous bell-shape with highest values in the middle and values close to zero in the tails. This is already obvious from Figure [17.1.](#_bookmark29)

**Figure 17.2.** Partial effects for binary response models (simulated data)
 *Légende : Graphique montrant l'effet partiel (pente) en fonction de x pour les modèles de probabilité linéaire, logit et probit. L'effet n'est constant que pour le modèle linéaire.*

 Depending on the value of $x$, the slope of the probability differs. For our simulated data set, Figure [17.2](#_bookmark30) shows the estimated partial effects for all 100 observed $x$ values. Interested readers can see the complete code for this as Script 17.8 (Binary-Margeff.R) in Appendix IV (p. 352).

 The fact that the partial effects differ by regressor values makes it harder to present the results in a concise and meaningful way. There are two common ways to aggregate the partial effects:
 *   Partial effects at the average: $PEA = \hat{\beta}_j \cdot g(/bar{/mathbf{x}}/hat{/boldsymbol{/beta}})$
 *   Average partial effects: $APE = \frac{1}{n} \sum_{i=1}^{n} \hat{\beta}_j \cdot g(/mathbf{x}_i /hat{/boldsymbol{/beta}}) = \hat{\beta}_j \cdot \overline{g(/mathbf{x}/hat{/boldsymbol{/beta}})}$
 where $\bar{\mathbf{x}}$ is the vector of sample averages of the regressors and $\overline{g(/mathbf{x}/hat{/boldsymbol{/beta}})}$ is the sample average of $g$ evaluated at the individual linear index $\mathbf{x}_i \hat{\boldsymbol{\beta}}$. Both measures multiply each coefficient $\hat{\beta}_j$ with a constant factor.

 Script 17.9 (Example-17-1-7.R) implements the APE calculations for our labor force participation example using already known $R$ functions:
 1.  The linear indices $\mathbf{x}_i \hat{\boldsymbol{\beta}}$ are calculated using `predict`
 2.  The factors $g(/mathbf{x}/hat{/boldsymbol{/beta}})$ are calculated by using the pdf functions `dlogis` and `dnorm` and then averaging over the sample with `mean`.
 3.  The APEs are calculated by multiplying the coefficient vector obtained with `coef` with the corresponding factor. Note that for the linear probability model, the partial effects are constant and simply equal to the coefficients.

 The results for the constant do not have a direct meaningful interpretation. The APEs for the other variables don't differ too much between the models. As a general observation, as long as we are interested in APEs only and not in individual predictions or partial effects and as long as not too many probabilities are close to 0 or 1, the linear probability model often works well enough.

```
Script 17.9: Example-17-1-7.R

# APEs (run 17-1-1.R through 17-1-4.R first to define the variables!)

# Calculation of linear index at individual values:
 xb.log <- predict(logitres)
 xb.prob<- predict(probitres)
# APE factors = average(g(xb))
 factor.log <- mean( dlogis(xb.log) )
 factor.prob<- mean( dnorm(xb.prob) )
 cbind(factor.log,factor.prob)

# average partial effects = beta*factor:
 APE.lin <- coef(linprob) * 1
 APE.log <- coef(logitres) * factor.log
 APE.prob<- coef(probitres) * factor.prob
# Table of APEs
 cbind(APE.lin, APE.log, APE.prob)
```

 A convenient package for calculating PEA and APE is ***mfx***. Among others, it provides the commands `logitmfx` and `probitmfx`. They estimate the corresponding model and display a regression table not with parameter estimates but with PEAs with the option `atmean=TRUE` and APEs with the option `atmean=FALSE`. Script 17.10 (Example-17-1-8.R) demonstrates this for the logit model of our labor force participation example. The reported APEs are the same as those manually calculated in Script 17.9 (Example-17-1-7.R).

```
Script 17.10: Example-17-1-8.R

# Automatic APE calculations with package mfx
 library(mfx)
 logitmfx(inlf~nwifeinc+educ+exper+I(exper^2)+age+kidslt6+kidsge6,
           data=mroz, atmean=FALSE)
```

## 17.2. Count Data: The Poisson Regression Model

 Instead of just 0/1-coded binary data, count data can take any non-negative integer 0,1,2,. . . If they take very large numbers (like the number of students in a school), they can be approximated reasonably well as continuous variables in linear models and estimated using OLS. If the numbers are relatively small (like the number of children of a mother), this approximation might not work well. For example, predicted values can become negative.

 The Poisson regression model is the most basic and convenient model explicitly designed for count data. The probability that $y$ takes any value $h \in \{0, 1, 2, \ldots\}$ for this model can be written as
 $$\text{P}(y = h|/mathbf{x}) = \frac{e^{-e^{\mathbf{x}\boldsymbol{\beta}}} \cdot e^{h \cdot \mathbf{x}\boldsymbol{\beta}}}{h!} \tag{17.11}$$

 The parameters of the Poisson model are much easier to interpret than those of a probit or logit model. In this model, the conditional mean of $y$ is
 $$\text{E}(y|/mathbf{x}) = e^{\mathbf{x}\boldsymbol{\beta}}, \tag{17.12}$$
 so each slope parameter $\beta_j$ has the interpretation of a semi elasticity:
 $$\frac{\partial \text{E}(y|/mathbf{x})}{\partial x_j} = \beta_j \cdot e^{\mathbf{x}\boldsymbol{\beta}} = \beta_j \cdot \text{E}(y|/mathbf{x}) \tag{17.13}$$
 $$\Leftrightarrow \beta_j = \frac{1}{\text{E}(y|/mathbf{x})} \cdot \frac{\partial \text{E}(y|/mathbf{x})}{\partial x_j}. \tag{17.14}$$

 If $x_j$ increases by one unit (and the other regressors remain the same), $\text{E}(y|/mathbf{x})$ will increase roughly by $100 \cdot \beta_j$ percent (the exact value is once again $100 /cdot (e^{/beta_j} - 1)$).

 A problem with the Poisson model is that it is quite restrictive. The Poisson distribution implicitly restricts the variance of $y$ to be equal to its mean. If this assumption is violated but the conditional mean is still correctly specified, the Poisson parameter estimates are consistent, but the standard errors and all inferences based on them are invalid. A simple solution is to interpret the Poisson estimators as quasi-maximum likelihood estimators (QMLE). Similar to the heteroscedasticity-robust inference for OLS discussed in Section 8.1, the standard errors can be adjusted.

 Estimating Poisson regression models in $R$ is straightforward. They also belong to the class of generalized linear models (GLM) and can be estimated using `glm`. The option to specify a Poisson model is `family=poisson`. For the more robust QMLE standard errors, we simply specify `family=quasipoisson`. For implementing more advanced count data models, see Kleiber and Zeileis (2008, Section 5.3).

### Wooldridge, Example 17.3: Poisson Regression for Number of Arrests17.3
 We apply the Poisson regression model to study the number of arrests of young men in 1986. Script 17.11 (Example-17-3-1.R) imports the data and first estimates a linear regression model using OLS. Then, a Poisson model is estimated using `glm` with the `poisson` specification for the GLM family. Finally, we estimate the same model using the `quasipoisson` specification to adjust the standard errors for a potential violation of the Poisson distribution. We display the results jointly in Script 17.12 (Example-17-3-2.R) using the `stargazer` command for a joint table. By construction, the parameter estimates are the same, but the standard errors are larger for the QMLE.

```
Script 17.11: Example-17-3-1.R

data(crime1, package='wooldridge')
# Estimate linear model
lm.res <- lm(narr86~pcnv+avgsen+tottime+ptime86+qemp86+inc86+
               black+hispan+born60, data=crime1)
# Estimate Poisson model
Poisson.res <- glm(narr86~pcnv+avgsen+tottime+ptime86+qemp86+inc86+
                     black+hispan+born60, data=crime1, family=poisson)
                     
# Quasi-Poisson model
QPoisson.res<- glm(narr86~pcnv+avgsen+tottime+ptime86+qemp86+inc86+
                     black+hispan+born60, data=crime1, family=quasipoisson)
```

```
Script 17.12: Example-17-3-2.R

# Example 17.3: Regression table (run Example-17-3-1.R first!)
 library(stargazer) # package for regression output
 stargazer(lm.res,Poisson.res,QPoisson.res,type="text",keep.stat="n")
 
```

**Figure 17.3.** Conditional means for the Tobit model
  *Légende : Graphique montrant la relation entre x et les espérances conditionnelles de la variable latente y* et de la variable observée y (limitée à zéro).*

## 17.3. Corner Solution Responses: The Tobit Model

 Corner solutions describe situations where the variable of interest is continuous but restricted in range. Typically, it cannot be negative. A significant share of people buy exactly zero amounts of alcohol, tobacco, or diapers. The Tobit model explicitly models dependent variables like this. It can be formulated in terms of a latent variable $y^*$ that can take all real values. For it, the classical linear regression model assumptions MLR.1--MLR.6 are assumed to hold. If $y^*$ is positive, we observe $y = y^*$. Otherwise, $y = 0$. Wooldridge (2019, Section 17.2) shows how to derive properties and the likelihood function for this model.

 The problem of interpreting the parameters is similar to logit or probit models. While $\beta_j$ measures the *ceteris paribus* effect of $x_j$ on $\text{E}(y^*|/mathbf{x})$, the interest is typically in $y$ instead. The partial effect of interest can be written as
 $$\frac{\partial \text{E}(y|/mathbf{x})}{\partial x_j} = \beta_j \cdot \Phi \left( /frac{/mathbf{x}/boldsymbol{/beta}}{/sigma} /right) \tag{17.15}$$
 and again depends on the regressor values $\mathbf{x}$. To aggregate them over the sample, we can either calculate the partial effects at the average (PEA) or the average partial effect (APE) just like with the binary variable models.

 Figure [17.3](#_bookmark32) depicts these properties for a simulated data set with only one regressor. Whenever $y^*  0$, $y = y^*$ and the symbols $\circ$ and $+$ are on top of each other. If $y^* < 0$, then $y = 0$. Therefore, the slope of $\text{E}(y|x)$ gets close to zero for very low $x$ values. The code that generated the data set and the graph is hidden as Script 17.13 (Tobit-CondMean.R) in Appendix IV (p. 353).

 For the practical ML estimation in $R$, there are different options. Package ***AER*** provides the command `tobit` and package ***censReg*** offers the command `censReg`. Both work very similarly and are easy to use. We will present an example using the latter. The command `censReg` can be used just like `lm` with the model formula and the data option. It will estimate the standard Tobit model discussed here. Other corner solutions ($y /ge a$ or $y /le b$) can be specified using the options `left` and `right`. After storing the results from `censReg` in a variable res, the PEA can easily be calculated with `margEff(res)`.

### Wooldridge, Example 17.2: Married Women's Annual Labor Supply17.2
 We have already estimated labor supply models for the women in the data set mroz.dta, ignoring the fact that the hours worked is necessarily non-negative. Script 17.14 (Example-17-2.R) estimates a Tobit model accounting for this fact. It also calculates the PEA using `margEff`.

```
Script 17.14: Example-17-2.R

 data(mroz, package='wooldridge')
 # Estimate Tobit model using censReg:
 library(censReg)
 TobitRes <- censReg(hours~nwifeinc+educ+exper+I(exper^2)+
                       age+kidslt6+kidsge6, data=mroz )
 summary(TobitRes)

# Partial Effects at the average x:
 margEff(TobitRes)

```

Another alternative for estimating Tobit models is the command `survreg` from package ***survival***. It is less straightforward to use but more flexible. We cannot comprehensively discuss all features but just show how to reproduce the same results for Example 17.2 in Script 17.15 (Example-17-2-survreg.R). We will come back to this command in the next section.

```
Script 17.15: Example-17-2-survreg.R

# Estimate Tobit model using survreg:
 library(survival)
 res <- survreg(Surv(hours, hours0, type="left") ~ nwifeinc+educ+exper+
                 I(exper^2)+age+kidslt6+kidsge6, data=mroz, dist="gaussian")
 summary(res)
```

## 17.4. Censored and Truncated Regression Models

 Censored regression models are closely related to Tobit models. In fact, their parameters can be estimated with the same software packages. General censored regression models also start from a latent variable $y^*$. The observed dependent variable $y$ is equal to $y^*$ for some (the uncensored) observations. For the other observations, we only know an upper or lower bound for $y^*$. In the basic Tobit model, we observe $y = y^*$ in the "uncensored" cases with $y^*  0$ and we only know that $y^* \le 0$ if we observe $y = 0$. The censoring rules can be much more general. There could be censoring from above or the thresholds can vary from observation to observation.

 The main difference between Tobit and censored regression models is the interpretation. In the former case, we are interested in the observed $y$, in the latter case, we are interested in the underlying $y^*$.[1](#_bookmark35) Censoring is merely a data problem that has to be accounted for instead of a logical feature of the dependent variable. We already know how to estimate Tobit models. With censored regression, we can use the same tools. The problem of calculating partial effects does not exist in this case since we are interested in the linear $\text{E}(y^*|/mathbf{x})$ and the slope parameters are directly equal to the partial effects of interest.

note1[1](#_bookmark35) Wooldridge (2019, Section 7.4) uses the notation $w$ instead of $y$ and $y$ instead of $y^*$ .

### Wooldridge, Example 17.4: Duration of Recidivism17.4
 We are interested in the criminal prognosis of individuals released from prison. We model the time it takes them to be arrested again. Explanatory variables include demographic characteristics as well as a dummy variable workprg indicating the participation in a work program during their time in prison. The 1445 former inmates observed in the data set recid.dta were followed for a while.

 During that time, 893 inmates were not arrested again. For them, we only know that their true duration $y^*$ is at least durat, which for them is the time between the release and the end of the observation period, so we have right censoring. The threshold of censoring differs by individual depending on when they were released.

 Because of the more complicated selection rule, we use the command `survreg` for the estimation of the model in Script 17.16 (Example-17-4.R). We need to supply the dependent variable log(durat) as well as a dummy variable indicating *uncensored* observations. We generate a dummy variable uncensored within the data frame based on the existing variable cens that represents censoring.

 The parameters can directly be interpreted. Because of the logarithmic specification, they represent semi-elasticities. For example married individuals take around $100 \cdot \hat{\beta} \approx 34\%$ longer to be arrested again. (Actually, the accurate number is $100 /cdot (e^{/hat{/beta}} - 1) \approx 40\%$.) There is no significant effect of the work program.

```
Script 17.16: Example-17-4.R

 library(survival)
 data(recid, package='wooldridge')
 # Define Dummy for UNcensored observations
 recid$uncensored <- recid$cens==0
 # Estimate censored regression model:
 res<-survreg(Surv(log(durat),uncensored, type="right") ~ workprg+priors+
                tserved+felon+alcohol+drugs+black+married+educ+age,
                data=recid, dist="gaussian")
 # Output:
 summary(res)

```

 Truncation is a more serious problem than censoring since our observations are more severely affected. If the true latent variable $y^*$ is above or below a certain threshold, the individual is not even sampled. We therefore do not even have any information. Classical truncated regression models rely on parametric and distributional assumptions to correct this problem. In $R$, they are available in the package ***truncreg***.

**Figure 17.4.** Truncated regression: simulated example
*Légende : Graphique montrant les points de données (tous et seulement ceux observés), l'ajustement MCO biaisé et l'estimation par régression tronquée.*

 Figure [17.4](#_bookmark36) shows results for a simulated data set. Because it is simulated, we actually know the values for everybody (hollow and solid dots). In our sample, we only observe those with $y  0$ (solid dots). When applying OLS to this sample, we get a downward biased slope (dashed line). Truncated regression fixes this problem and gives a consistent slope estimator (solid line). Script 17.17 (TruncReg-Simulation.R) which generated the data set and the graph is shown in Appendix IV (p. 354).

## 17.5. Sample Selection Corrections

 Sample selection models are related to truncated regression models. We do have a random sample from the population of interest, but we do not observe the dependent variable $y$ for a non-random sub-sample. The sample selection is not based on a threshold for $y$ but on some other selection mechanism.

 Heckman's selection model consists of a probit-like model for the binary fact whether $y$ is observed and a linear regression-like model for $y$. Selection can be driven by the same determinants as $y$ but should have at least one additional factor excluded from the equation for $y$. Wooldridge (2019, Section 17.5) discusses the specification and estimation of these models in more detail.

 The classical Heckman selection model can be estimated either in two steps using software for probit and OLS as discussed by Wooldridge (2019) or by a specialized command using MLE. In $R$, the package ***sampleSelection*** offers automated estimation for both approaches.

### Wooldridge, Example 17.5: Wage offer equation for married women17.5
 We once again look at the sample of women in the data set MROZ.dta. Of the 753 women, 428 worked (inlf=1) and the rest did not work (inlf=0). For the latter, we do not observe the wage they would have gotten had they worked. Script 17.18 (Example-17-5.R) estimates the Heckman selection model using the command `selection`. It expects two formulas: one for the selection and one for the wage equation. The option `method="2step"` requests implicit 2-step estimation to make the results comparable to those reported by Wooldridge (2019). With the option `method="ml"`, we would have gotten the more efficient MLE. The summary of the results gives a typical regression table for both equations and additional information.

```
Script 17.18: Example-17-5.R

 library(sampleSelection)
 data(mroz, package='wooldridge')
 # Estimate Heckman selection model (2 step version)
 res<-selection(inlf~educ+exper+I(exper^2)+nwifeinc+age+kidslt6+kidsge6,
                 log(wage)~educ+exper+I(exper^2), data=mroz, method="2step" )
 # Summary of results:
 summary(res)
```
