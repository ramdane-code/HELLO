
# 18. Sujets avancés en séries chronologiques

 Après avoir introduit les concepts de séries chronologiques dans les chapitres 10 à 12, ce chapitre aborde quelques sujets plus avancés en économétrie des séries temporelles. À savoir, nous examinons 
 - l<font color="#00b0f0">es modèles à retards distribués infinis</font> dans la section [18.1,](#infinite-distributed-lag-models) 
 - <font color="#00b0f0">les tests de racine unitaire</font> dans la section [18.2,](#testing-for-unit-roots) 
 - <font color="#00b0f0">la régression fallacieuse </font>dans la section [18.3,](#spurious-regression) 
 - <font color="#00b0f0">la cointégration</font> dans la section [18.4](#cointegration-and-error-correction-models) 
 - <font color="#00b0f0">et la prévision</font> dans la section [18.5.](#forecasting)

# Modèles à retards distribués infinis
 <font color="#7030a0">Nous avons couvert les modèles à retards distribués finis dans la section 10.3.</font> 
 Nous avons estimé ces modèles et des modèles connexes dans *R* en utilisant le package ***dynlm***. 
 
 <font color="#00b0f0">Dans les modèles à retards distribués</font> *infini*, 
 - <font color="#00b0f0">les chocs dans les régresseurs</font> $z_t$ <font color="#00b0f0">ont un impact infiniment long sur</font> $y_t$, $y_{t+1}$, . . . 
 - <font color="#00b050">La propension à long terme est l'effet futur total d'une augmentation de</font> $z_t$ <font color="#00b050">d'une unité et du maintien à ce niveau.</font>

 <font color="#c0504d">Sans restrictions supplémentaires, les modèles à retards distribués infinis ne peuvent pas être estimés. </font>
 Wooldridge (2019, Section 18.1) discute de <font color="#00b0f0">deux modèles différents.</font> 
 - <font color="#00b050">Le modèle à retards distribués</font> **géométrique (ou Koyck)** se ramène 
	 - à une équation de régression linéaire en termes de variables dépendantes retardées  $y_t = \alpha_0 + \gamma z_t + \rho y_{t-1} + v_t \tag{18.1}$   
	 - et a une propension à long terme de $LRP = \frac{\gamma}{1 - \rho}. \tag{18.2}$
- Le modèle à retards distribués **rationnel** 
	- peut s'écrire comme une équation un peu plus générale  $y_t = \alpha_0 + \gamma_0 z_t + \rho y_{t-1} + \gamma_1 z_{t-1} + v_t \tag{18.3}$  
	- et a une propension à long terme de $LRP = \frac{\gamma_0 + \gamma_1}{1 - \rho}. \tag{18.4}$

 <font color="#00b0f0">En termes de mise en œuvre de ces modèles, il n'y a rien de vraiment nouveau par rapport à la section 10.3</font>.<font color="#00b050"> La seule différence est que nous incluons des variables dépendantes retardées comme régresseurs.</font>

## Wooldridge, Exemple 18.1 : Investissement dans le logement et inflation des prix résidentiels 18.1

 <font color="#00b0f0">Le script 18.1 (Example-18-1.R) implémente les modèles à retards distribués géométrique et rationnel</font> <font color="#c0504d">pour l'équation d'investissement dans le logement.</font> 
 - La variable dépendante est d'abord désaisonnalisée en utilisant simplement le résidu d'une régression sur une tendance linéaire temporelle. 
 - Nous stockons cette variable désaisonnalisée dans le data frame qui est ensuite transformé en un objet de série temporelle en utilisant **ts**, voir chapitre 10.

<font color="#c0504d"> Les deux modèles sont estimés en utilisant</font> **dynlm** et<font color="#00b0f0"> un tableau de régression très similaire à Wooldridge (2019, Table 18.1) est produit avec </font>**stargazer**. 
<font color="#00b050">Enfin, nous estimons la LRP pour les deux modèles en utilisant les formules données ci-dessus.</font> 
- Nous extrayons d'abord le vecteur de coefficients (nommé) comme b, 
- puis nous effectuons les calculs avec les indices nommés. 
- Par exemple, **b["gprice"]** est le coefficient portant l'étiquette "gprice" qui, dans notre notation ci-dessus, correspond à $\gamma$ dans le modèle à retards distribués géométrique.

#### Output of Script 18.1: Example-18-1.R

```r
library(dynlm); library(stargazer)
data(hseinv, package='wooldridge')

# detrended variable: residual from a regression on the obs. index:
trendreg <- dynlm( log(invpc) ~ trend(hseinv), data=hseinv )
hseinv$linv.detr <- resid( trendreg )

# ts data:
hseinv.ts <- ts(hseinv)

# Koyck geometric d.l.:
gDL<-dynlm(linv.detr~gprice + L(linv.detr) ,data=hseinv.ts)

# rational d.l.:
rDL<-dynlm(linv.detr~gprice + L(linv.detr) + L(gprice),data=hseinv.ts)
stargazer(gDL,rDL, type="text", keep.stat=c("n","adj.rsq"))

# LRP geometric DL:
b <- coef(gDL)
b["gprice"] / (1-b["L(linv.detr)"])

# LRP rational DL:
b <- coef(rDL)
(b["gprice"]+b["L(gprice)"]) / (1-b["L(linv.detr)"])
```


# 18.2 Tests de racine unitaire
<font color="#7030a0">Nous avons couvert les processus à racine unitaire fortement dépendants dans le chapitre 11</font>, plusieurs tests de racines unitaires sont disponibles.
Conceptuellement, <font color="#00b0f0">le test de Dickey-Fuller (DF) est le plus simple</font>. 
- Si nous voulons tester si une variable $y$ a une racine unitaire, nous régressons $\Delta y_t$ sur $y_{t-1}$. 
- La statistique de test est la statistique $t$ habituelle du coefficient de pente. 
Un problème est qu'en raison de la racine unitaire, <font color="#c0504d">cette statistique de test *n'est pas* distribuée selon une $t$ ou une normale, même asymptotiquement.</font> Au lieu de cela, <font color="#00b0f0">nous devons utiliser des tables de distribution spéciales pour les valeurs critiques.</font> <font color="#de7802">La distribution dépend également du fait que nous autorisons ou non une tendance temporelle dans cette régression.</font>

 Le test de Dickey-Fuller augmenté (ADF) est une généralisation qui permet des dynamiques plus riches dans le processus de $y$. 
 Pour le mettre en œuvre, nous ajoutons des valeurs retardées $\Delta y_{t-1}$, $\Delta y_{t-2}$, . . . à l'équation de régression différenciée.

 Bien sûr, travailler avec les tables spéciales de valeurs critiques (A)DF est quelque peu gênant. 
<font color="#00b050"> Dans</font> *R*, <font color="#00b050">le package</font> ***tseries*** <font color="#00b050">propose des tests DF et ADF automatisés pour les modèles avec tendance temporelle.</font> 
- La commande **adf.test(y)** effectue un test ADF en sélectionnant automatiquement le nombre de retards dans $\Delta y$
- **adf.test(y,k=1)** choisit un retard et **adf.test(y,k=0)** demande zéro retard, c'est-à-dire un simple test DF. 

<font color="#00b050">Le package </font>***urca*** <font color="#00b050">propose également différents tests de racine unitaire</font>, y compris le test ADF avec et sans tendance en utilisant la commande **ur.df**.

## Wooldridge, Exemple 18.4 : Racine unitaire dans le PIB réel 18.4
 <font color="#00b0f0">Le script 18.2 (Example-18-4.R) implémente un test ADF pour le logarithme du PIB réel américain incluant une tendance linéaire temporelle. </font>
 <font color="#c0504d">Pour un test avec un retard dans</font> $\Delta y$ <font color="#c0504d">et une tendance temporelle, l'équation à estimer est</font>
$\Delta y = \alpha + \theta y_{t-1} + \gamma_1 \Delta y_{t-1} + \delta t + e_t.$
 Nous savons déjà comment implémenter une telle régression. 
 Les différents termes et leurs équivalents dans la syntaxe **dynlm** sont :
- $\Delta y$ = **d(y)**
- $y_{t-1}$ = **L(y)**
- $\Delta y_{t-1}$ = **L(d(y))**
- $t$ = **trend(data)**

 La statistique de test pertinente est $t = -2.421$ et les valeurs critiques sont données dans Wooldridge (2019, Table 18.3). 
 
 Plus commodément, <font color="#00b050">le script utilise également la commande automatique</font> **adf.test** qui rapporte une `pvaleur` de 0.41. <font color="#c0504d">Ainsi, l'hypothèse nulle de racine unitaire ne peut pas être rejetée à un niveau de signification raisonnable.</font> 

#### Output of Script 18.2: Example-18-4.R

```r
library(dynlm)
data(inven, package='wooldridge')
# variable to test: y=log(gdp)
inven$y <- log(inven$gdp)
inven.ts<- ts(inven)
# summary output of ADF regression:
summary(dynlm( d(y) ~ L(y) + L(d(y)) + trend(inven.ts), data=inven.ts))

# automated ADF test using tseries:
library(tseries)
adf.test(inven$y, k=1)
```

<font color="#00b0f0">Le script 18.3 (Example-18-4-urca.R) répète la même analyse mais utilise le package </font>***urca***.
#### Output of Script 18.3: Example-18-4-urca.R

```r
library(urca)
data(inven, package='wooldridge')
# automated ADF test using urca:
summary( ur.df(log(inven$gdp) , type = c("trend"), lags = 1) )
```

# Régression fallacieuse

 <font color="#c0504d">Les racines unitaires détruisent généralement les propriétés habituelles (en grand échantillon) des estimateurs et des tests.</font> <font color="#00b0f0">Un exemple important est la régression fallacieuse</font>. 
 Supposons que deux variables $x$ et $y$ soient complètement indépendantes mais que toutes deux suivent une marche aléatoire :
$x_t = x_{t-1} + a_t$   et   $y_t = y_{t-1} + e_t,$   où $a_t$ et $e_t$ sont des innovations aléatoires i.i.d. 

Si nous voulons <font color="#c0504d">tester si elles sont liées à partir d'un échantillon aléatoire</font>, 
- nous pourrions simplement régresser $y$ sur $x$. 
- Un test $t$ devrait rejeter l'hypothèse nulle (vraie) que le coefficient de pente est égal à zéro avec une probabilité de $\alpha$, par exemple 5 %. 
- <font color="#00b0f0">Le phénomène de régression fallacieuse implique que le rejet de l'hypothèse d'indépendance des 2 variables arrive souvent.</font>

<font color="#c0504d"> Le script 18.4 (Simulate-Spurious-Regression-1.R) simule ce modèle pour un échantillon.</font> 
La section 11.2 a expliqué comment <font color="#00b0f0">simuler une marche aléatoire de manière simple</font> :<font color="#00b050"> avec une valeur initiale de zéro, c'est simplement la somme cumulée des innovations. </font>
La série temporelle pour cet échantillon simulé de taille $n = 50$ est montrée dans la figure [18.1.](#_bookmark3) 
Lorsque nous régressons $y$ sur $x$, la statistique $t$ pour le paramètre de pente est supérieure à 4 avec une pvalue bien inférieure à 1 %. 
<font color="#c0504d">Nous rejetterions donc l'hypothèse nulle (correcte) que les variables sont indépendantes.</font>

**Figure 18.1.** Régression fallacieuse : données simulées du script 18.4


Script 18.4: Simulate-Spurious-Regression-1.R
```r
# Initialize Random Number Generator
set.seed(29846)

# i.i.d. N(0,1) innovations
n <- 50
e <- rnorm(n)
a <- rnorm(n)

# independent random walks
x <- cumsum(a)
y <- cumsum(e)

# plot
plot(x,type="l",lty=1,lwd=1)
lines(y,lty=2,lwd=2)
legend("topright",c("x","y"), lty=c(1,2), lwd=c(1,2))

# Regression of y on x
summary( lm(y~x) )
```

 Nous savons que par définition, un test valide doit rejeter une hypothèse nulle vraie avec une probabilité de $\alpha$, donc peut-être avons-nous simplement eu de la malchance avec l'échantillon spécifique que nous avons pris. 
- <font color="#c0504d"> Nous répétons donc la même analyse avec 10 000 échantillons du même processus de génération de données dans le script 18.5</font> (Simulate-Spurious-Regression-2.R). 
- Pour chacun des échantillons, nous stockons la pvalue du paramètre de pente dans un vecteur nommé pvals. 
- Après l'exécution de ces simulations, nous vérifions simplement combien de fois nous aurions rejeté $H_0 : \beta_1 = 0$ en comparant ces valeurs $p$ à 0.05.

 <font color="#00b050">Nous constatons que dans</font> 6 626 <font color="#00b050">échantillons, soit dans </font>66 % <font color="#00b050">au seuil de</font> $\alpha = 5$ %, <font color="#00b050">nous avons rejeté</font> $H_0$. 
 <font color="#c0504d">Ainsi, le test</font> $t$ <font color="#c0504d">compromet sérieusement l'inférence statistique </font><font color="#00b0f0">en raison des racines unitaires.</font>

**Script 18.5: Simulate-Spurious-Regression-2.R**

```r
# Initialize Random Number Generator
set.seed(29846)

# generate 10,000 independent random walks and store the p val of the t test
pvals <- numeric(10000)
for (r in 1:10000) {
  # i.i.d. N(0,1) innovations
  n <- 50
  a <- rnorm(n)
  e <- rnorm(n)
  # independent random walks
  x <- cumsum(a)
  y <- cumsum(e)
  # regression summary
  regsum <- summary(lm(y~x))
  # p value: 2nd row, 4th column of regression table
  pvals[r] <- regsum$coef[2,4]
}

# How often is p<5% ?
table(pvals<=0.05)
```


# Cointégration et modèles à correction d'erreur

 Dans la section [18.3,](#spurious-regression) <font color="#00b0f0">nous venons de voir que ce n'est pas une bonne idée de faire une régression linéaire avec des variables intégrées.</font> <font color="#c0504d">Ce n'est pas toujours vrai.</font> 
 - Si deux variables ne sont pas seulement intégrées (c'est-à-dire qu'elles ont une racine unitaire), mais *cointégrées*, 
 - la régression linéaire avec elles peut en fait avoir un sens. 
 
 <font color="#00b0f0">Souvent, la théorie économique suggère une relation stable à long terme entre variables intégrées</font>, <font color="#00b050">ce qui implique la cointégration.</font> 
 - La cointégration implique que dans l'équation de régression  $y_t = \beta_0 + \beta_1 x_t + u_t,$
 - le terme d'erreur $u$ n'a pas de racine unitaire, 
 - alors que $y$ et $x$ en ont une. 
 <font color="#00b050">Un test de cointégration peut être basé sur cette constatation</font> : 
 - nous estimons d'abord ce modèle par MCO, 
 - puis nous testons la racine unitaire dans les résidus $\hat u$. 
 Encore une fois, nous devons ajuster la distribution de la statistique de test et les valeurs critiques. 
 <font color="#00b0f0">Cette approche est appelée test d'Engle-Granger dans Wooldridge (2019, Section 18.4) ou test de Phillips-Ouliaris (PO).</font> 
<font color="#00b050">Elle est implémentée dans le package </font>***tseries*** <font color="#00b050">sous le nom de</font> **po.test** <font color="#00b050">et dans le package</font> ***urca*** <font color="#00b050">sous le nom de</font> **ca.po**.

<font color="#c0504d"> Si nous trouvons une cointégration</font>, <font color="#00b050">nous pouvons estimer des modèles à correction d'erreur.</font> 
- <font color="#00b0f0">Dans la procédure d'Engle-Granger, ces modèles peuvent être estimés en deux étapes en utilisant les MCO</font>. 
- Il y a aussi <font color="#7030a0">des commandes puissantes qui estiment automatiquement différents types de modèles à correction d'erreur.</font> 
	- Le package ***urca*** fournit **ca.jo** 
	- et pour les modèles structurels, le package ***vars*** offre la commande **SVEC**.

# Prévision
 Un objectif majeur de l'analyse des séries temporelles est la `prévision`. 
 - Étant donné les informations dont nous disposons aujourd'hui, nous voulons donner notre meilleure estimation de l'avenir et quantifier notre incertitude. 
 - Étant donné un modèle de série temporelle pour $y$, la meilleure estimation pour $y_{t+1}$ compte tenu de l'information $I_t$ est l'espérance conditionnelle de $E(y_{t+1} \mid I_t)$. 
 
 Pour un modèle comme  $y_t = \delta_0 + \alpha_1 y_{t-1} + \gamma_1 z_{t-1} + u_t, \tag{18.5}$
- supposons que nous soyons à la période $t$ et connaissions à la fois $y_t$ et $z_t$, et que nous voulions prédire $y_{t+1}$.
- Supposons également que $E(u_t \mid I_{t-1}) = 0$. 
Alors, $E(y_{t+1} \mid I_t) = \delta_0 + \alpha_1 y_t + \gamma_1 z_t \tag{18.6}$ , et notre prédiction à partir d'un modèle estimé serait $\hat y_{t+1} = \hat \delta_0 + \hat \alpha_1 y_t + \hat \gamma_1 z_t$.

 <font color="#00b050">Nous savons déjà comment obtenir des prédictions </font><font color="#c0504d">dans l'échantillon</font> et <font color="#00b050">(hypothétiques) hors échantillon</font>, <font color="#7030a0">y compris des intervalles de prévision</font>,<font color="#00b0f0"> à partir de modèles linéaires en utilisant la commande</font> **predict**. 
 Elle peut également être utilisée pour nos besoins.

<font color="#c0504d"> Il existe plusieurs façons d'évaluer la performance des modèles de prévision</font>. 
Il est logique de <font color="#4bacc6">regarder les performances de prévision hors échantillon</font> plutôt que l'ajustement du modèle dans l'échantillon d'estimation. 
- Supposons que nous ayons utilisé les observations $y_1, \ldots, y_n$ pour l'estimation 
- et que nous ayons également des observations $y_{n+1}, \ldots, y_{n+m}$. 
Pour cet ensemble d'observations, nous obtenons des prévisions hors échantillon $f_{n+1}, \ldots, f_{n+m}$ et calculons les $m$ erreurs de prévision  $e_t = y_t - f_t \quad \text{pour } t = n + 1, \ldots, n + m. \tag{18.7}$

 <font color="#c0504d">Nous voulons que ces erreurs de prévision soient aussi petites (en valeur absolue) que possible</font>. <font color="#00b050">Des mesures utiles sont</font> 
 - la racine carrée de l'erreur quadratique moyenne (*RMSE*) 
 - et l'erreur absolue moyenne (*MAE*) :

 $$RMSE = \sqrt{\frac{1}{m} \sum_{h=1}^{m} e_{n+h}^2} \tag{18.8}$$
 $$MAE = \frac{1}{m} \sum_{h=1}^{m} |e_{n+h}|. \tag{18.9}$$

## Wooldridge, Exemple 18.8 : Prévision du taux de chômage américain 18.8

 Le script 18.6 (Example-18-8.R) estime deux modèles simples pour la prévision du taux de chômage. Le premier est un modèle AR(1) de base avec seulement le chômage retardé comme régresseur, le second ajoute l'inflation retardée. Nous utilisons l'option **end** pour restreindre l'échantillon d'estimation aux années jusqu'à 1996. Après l'estimation, nous faisons des prédictions incluant des intervalles de prévision à 95 %. Wooldridge (2019) explique comment cela peut être fait manuellement. Nous sommes un peu paresseux et utilisons simplement la commande **predict**.

#### Script 18.6: Example-18-8.R

```r
# load updataed data from URfIE Website since online file is incomplete
library(dynlm); library(stargazer)
data(phillips, package='wooldridge')
tsdat=ts(phillips, start=1948)
# Estimate models and display results
res1 <- dynlm(unem ~ unem_1 , data=tsdat, end=1996)
res2 <- dynlm(unem ~ unem_1+inf_1, data=tsdat, end=1996)
stargazer(res1, res2 ,type="text", keep.stat=c("n","adj.rsq","ser"))

# Predictions for 1997-2003 including 95% forecast intervals:
predict(res1, newdata=window(tsdat,start=1997), interval="prediction")

predict(res2, newdata=window(tsdat,start=1997), interval="prediction")
```

## Wooldridge, Exemple 18.9 : Comparaison des performances de prévision hors échantillon 18.9

 <font color="#00b0f0">Le script 18.7 (Example-18-9.R) calcule les erreurs de prévision du taux de chômage pour les deux modèles utilisés dans l'exemple 18.8</font>. 
 - Les modèles sont estimés en utilisant le sous-échantillon jusqu'en 1996 
 - et les prédictions sont faites pour les sept autres années disponibles jusqu'en 2003. 
 - Le taux de chômage réel et les prévisions sont tracés 
 - le résultat est présenté dans la figure [18.2.](#_bookmark6) 
 - Enfin, nous calculons la *RMSE* et la *MAE* pour les deux modèles. 
 Les deux mesures suggèrent que le second modèle incluant l'inflation retardée est meilleur.

#### Output of Script 18.7: Example-18-9.R

```r
# Note: run Example-18-8.R first to generate the results res1 and res2
# Actual unemployment and forecasts:
y <- window(tsdat,start=1997)[,"unem"]
f1 <- predict( res1, newdata=window(tsdat,start=1997) )
f2 <- predict( res2, newdata=window(tsdat,start=1997) )

# Plot unemployment and forecasts:
matplot(time(y), cbind(y,f1,f2), type="l", col="black",lwd=2,lty=1:3)
legend("topleft",c("Unempl.","Forecast 1","Forecast 2"),lwd=2,lty=1:3)

# Forecast errors:
e1<- y - f1
e2<- y - f2

# RMSE:
sqrt(mean(e1^2))

sqrt(mean(e2^2))

# MAE:
mean(abs(e1))

mean(abs(e2))
```

 
 **Figure 18.2.** Out-of-sample forecasts for unemployment

