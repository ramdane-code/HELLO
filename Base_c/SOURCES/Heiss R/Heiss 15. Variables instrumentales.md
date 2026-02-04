# 15. Instrumental Variables Estimation and Two Stage Least Squares

 <font color="#00b0f0">Instrumental variables are potentially powerful tools for the identification and estimation of causal effects.</font> 
 - Section [15.1](#instrumental-variables-in-simple-regression-models) the <font color="#7030a0">simplest case of one endogenous regressor and one instrumental variable. </font>
 - Section [15.2](#more-exogenous-regressors) shows how to implement <font color="#7030a0">models with additional exogenous regressors.</font> 
 - Section [15.3,](#two-stage-least-squares) introduces <font color="#00b0f0">2 stage least squares</font> which deals with several endogenous variables and several instruments.
 - <font color="#c0504d">Tests of the exogeneity </font>of the regressors and instruments are presented in Sections [15.4](#testing-for-exogeneity-of-the-regressors) and [15.5,](#testing-overidentifying-restrictions) respectively. 
 - Section [15.6](#instrumental-variables-with-panel-data) shows how to conveniently <font color="#00b050">combine panel data estimators with instrumental variables.</font>

## 15.1 Instrumental Variables in Simple Regression Models
### <font color="#c0504d">Quand le terme d'erreur μ est corrélé au régresseur x, les paramètres issus de la rég OLS sont biaisés</font>
 We start the discussion of instrumental variables (IV) regression with the most straightforward case of <font color="#00b0f0">only one regressor and only one instrumental variable</font>. 
 Consider <font color="#00b050">the simple linear regression model for cross-sectional data</font> : $y = \beta_0 + \beta_1 x + u. \tag{15.1}$
 - The OLS estimator for the slope parameter is $\hat{\beta}_1^{OLS} = \frac{\text{Cov}(x,y)}{\text{Var}(x)}$, see Equation 2.3. 
 - <font color="#00b0f0">Suppose the regressor </font>$x$<font color="#00b0f0"> is correlated with the error term </font>$u$, <font color="#c0504d">so OLS parameter estimators will be biased and inconsistent.</font>
### <font color="#c0504d">Une bonne IV est corrélée au régresseur et est non corrélée au terme d'erreur</font> $u$
 <font color="#7030a0">If we have a valid instrumental variable</font> $z$, <font color="#00b050">we can consistently estimate</font> $\beta_1$ <font color="#00b0f0">using the IV estimator</font>
 $\hat{\beta}_1^{IV} = \frac{\text{Cov}(z, y)}{\text{Cov}(z, x)}. \tag{15.2}$  ^521849

<font color="#c00000"> A valid instrument is</font> 
- <font color="#00b0f0">correlated with the regressor</font> $x$ ("relevant"), so the denominator of Equation [15.2] is nonzero. 
- It is also<font color="#00b0f0"> uncorrelated with the error term</font> $u$ ("exogenous"). 
Wooldridge (2019, Section 15.1) provides more discussion and examples.

### <font color="#c0504d">Implémenter une rég IV dans R avec la commande ivreg du package AER</font>
 <font color="#00b050">To implement IV regression in</font> $R$, <font color="#00b050">the package</font> ***AER*** <font color="#00b050">offers the convenient command</font> `ivreg`. 
 - <font color="#00b0f0">It works similar to</font> `lm`. 
 - In the formula specification, <font color="#00b0f0">the regressor(s) are separated from the instruments with a vertical line</font> `|` (like in "conditional on $z$"):    `ivreg( y ~ x | z )`
 <font color="#00b050">Note that we can easily deal with heteroscedasticity</font>: 
 - <font color="#c0504d">Results obtained by</font> `ivreg` <font color="#00b0f0">can be directly used with robust standard errors from</font> `hccm` (Package ***car***) 
 - <font color="#00b050">or </font>`vcovHC` (<font color="#00b050">package</font> ***sandwich***), see Section 8.1.

### <font color="#c0504d">Woo.ex  15.1: utiliser une IV dans l'implémentation de la régression simple (données du pb).</font>
L'exemple porte sur le rendement de l'éducation pour une femme mariée (Return to Education for Married Women)
 <font color="#00b0f0">Script 15.1 (Example-15-1.R) uses data from MROZ.dta.</font> 
 - We only analyze<font color="#6425d0"> women with non-missing wage,</font> 
	 - <font color="#6425d0">so we extract a </font>`subset`<font color="#6425d0"> from our data.</font> 
 - <font color="#00b0f0">We want to estimate the return to education for these women.</font> 
 - <font color="#c0504d">As an instrumental variable for education</font>, <font color="#00b050">we use the education of her father fatheduc.</font>

### <font color="#c0504d">Utiliser une IV dans la régression simple (procédure d'implémentation)</font>
- <font color="#00b0f0">D'abord, calculer les paramètres de pente MCO et VI </font>selon les Équations 2.3 et 15.2, respectivement. 
	- NB : la commande `with` définit que tous les noms de variables se réfèrent au data frame `oursample`. 
- <font color="#00b0f0">Ensuite, calculer les estimations MCO et VI complètes en utilisant les routines encadrées</font> `lm` et `ivreg`, respectivement.
- <font color="#00b0f0">Les résultats  sont affichés en utilisant</font> `stargazer`. 
<font color="#00b050">Sans surprise, les paramètres de pente correspondent aux résultats manuels.</font>
### <font color="#c0504d">Script 15.1 Prépare les données, calcul manuel de β, puis reg avec OLS et avec IV, enfin Stargazer</font>

```
Script 15.1: Example-15-1.R

 library(AER);library(stargazer)
 data(mroz, package='wooldridge')
 
 # restreindre aux observations avec salaire non manquant
 oursample <- subset(mroz, !is.na(wage)) ^dee35f
 
 # Paramètre de pente MCO manuellement (cov(x,y)/var(x))
 with(oursample, cov(log(wage),educ) / var(educ) )

 # Paramètre de pente VI manuellement (cov(x,y)/(cov(z,x)))
 with(oursample, cov(log(wage),fatheduc) / cov(educ,fatheduc) )

 # MCO automatiquement
 reg.ols <- lm(log(wage) ~ educ, data=oursample)
 
 # VI automatiquement
 reg.iv <- ivreg(log(wage) ~ educ | fatheduc, data=oursample)
 
 # Joli tableau de régression
 stargazer(reg.ols,reg.iv, type="text")
```

^54be7e


## 15.2 Plus de Régresseurs Exogènes

### <font color="#c0504d">ivreg permet d'utiliser plusieurs régresseurs en plus de l'instrument</font>
<font color="#00b0f0">L'approche VI peut facilement être généralisée pour inclure des régresseurs exogènes supplémentaires,</font> <font color="#00b050">c'est-à-dire des régresseurs supposés non liés au terme d'erreur.</font> 

<font color="#c0504d">Dans</font> `ivreg`, <font color="#c0504d">nous devons inclure ces variables à la fois </font>
- dans la liste des régresseurs à gauche du symbole `|` 
- et dans la liste des instruments exogènes à droite du symbole `|`.

### <font color="#c0504d">Woo.ex  15.4 : Utiliser nearc4 comme IV (proxy) de Educ puis Estimation OLS et  IV</font> 
#### <font color="#00b050">Régresser Educ sur tous les autres rég yc nearc4 pour évaluer la pertinence de ce dernier</font>
<font color="#00b0f0">Utilisation de la Proximité d'un Collège comme VI pour l'Éducation</font>
<font color="#6425d0">Dans le Script 15.2 (Example-15-4.R), nous utilisons CARD.dta pour estimer le rendement de l'éducation. </font>
- L'éducation est autorisée à être endogène (donc corrélée à μ ou à d'autres var?) 
- <font color="#00b0f0">Elle est instrumentée avec la variable muette</font> `nearc4` <font color="#00b0f0">qui indique si l'individu a grandi près d'un collège</font>. 
- <font color="#c00000">De plus, nous contrôlons pour l'expérience, la race et les informations régionales</font>. <font color="#6425d0">Ces variables sont supposées exogènes et agissent comme leurs propres instruments.</font>

<font color="#00b0f0">Nous vérifions d'abord la pertinence</font> en régressant la variable indépendante endogène educ sur toutes les variables exogènes incluant l'instrument nearc4. 
- <font color="#00b0f0">Son paramètre (celui de nearc4 probablement) est très significativement différent de zéro</font>, <font color="#00b050">donc la pertinence est soutenue.</font> 
<font color="#c0504d">Nous estimons ensuite l'équation du logarithme du salaire avec MCO et VI. </font>
<font color="#00b050">Tous les résultats sont affichés dans un tableau avec</font> `stargazer`.
#### <font color="#00b050">Script 15.2 : charge libraries et data, vérifie pertinence du proxy, estimations mco et iv, stargazer</font>

```
Script 15.2: Example-15-4.R

 library(AER);library(stargazer)
 data(card, package='wooldridge')
 
 # Vérification de la pertinence : forme réduite (redf)
 redf<-lm(educ ~ nearc4+exper+I(exper^2)+black+smsa+south+smsa66+reg662+
            reg663+reg664+reg665+reg666+reg667+reg668+reg669, data=card)

 # Estimation MCO (avec educ et sans nearc)
 ols<-lm(log(wage)~educ+exper+I(exper^2)+black+smsa+south+smsa66+reg662+
           reg663+reg664+reg665+reg666+reg667+reg668+reg669, data=card)
           
 # Estimation VI (educ+tous les autres rég (sans nearce4)|nearc4+tous les autres rég (sans educ))
 iv <-ivreg(log(wage)~educ+exper+I(exper^2)+black+smsa+south+smsa66+
              reg662+reg663+reg664+reg665+reg666+reg667+reg668+reg669
              | nearc4+exper+I(exper^2)+black+smsa+south+smsa66+
                reg662+reg663+reg664+reg665+reg666+reg667+reg668+reg669
              , data=card)
              
 # Joli tableau de régression de coefficients sélectionnés
 stargazer(redf,ols,iv,type="text",
            keep=c("ed","near","exp","bl"),keep.stat=c("n","rsq"))
```

## 15.3 Moindres Carrés en Deux Étapes

<font color="#00b050">Les moindres carrés en deux étapes (2SLS) sont une approche générale pour l'estimation VI </font>
- <font color="#c0504d">lorsque nous avons un ou plusieurs régresseurs endogènes</font> 
- <font color="#00b050">et au moins autant de variables instrumentales supplémentaires</font>. 

<font color="#00b0f0">Considérons le modèle de régression</font>   $y_1 = \beta_0 + \beta_1 y_2 + \beta_2 y_3 + \beta_3 z_1 + \beta_4 z_2 + \beta_5 z_3 + u_1 \tag{15.3}$
  - <font color="#c0504d">Les régresseurs</font> $y_2$ et $y_3$ <font color="#c0504d">sont potentiellement corrélés avec le terme d'erreur</font> $u_1$, 
  - <font color="#00b050">les régresseurs</font> $z_1$, $z_2$ et $z_3$ <font color="#00b050">sont supposés exogènes.</font> 
  - <font color="#00b0f0">Parce que nous avons deux régresseurs endogènes, nous avons besoin d'au moins deux variables instrumentales supplémentaires, disons</font> $z_4$ et $z_5$.

<font color="#c0504d">Le nom de 2SLS vient du fait qu'il peut être réalisé en deux étapes de régressions MCO :</font>
1. Régressez séparément $y_2$ et $y_3$ sur $z_1$ à $z_5$. Obtenez les valeurs ajustées $\hat{y}_2$ et $\hat{y}_3$.
2. Régressez $y_1$ sur $\hat{y}_2$, $\hat{y}_3$ et $z_1$ à $z_3$.
<font color="#00b050">Si les instruments sont valides, cela donnera des estimations convergentes des paramètres</font> $\beta_0$ à $\beta_5$. 

<font color="#00b0f0">Généraliser cela à plus de régresseurs endogènes et de variables instrumentales est évident.</font>

<font color="#00b050">Cette procédure peut être facilement implémentée dans</font> $R$, 
- en se rappelant que <font color="#7030a0">les valeurs ajustées sont obtenues avec</font> `fitted` 
- <font color="#7030a0">qui peut être appelé directement depuis la</font> `formula` de `lm`. 
<font color="#c0504d">Un des problèmes de cette approche manuelle est que la matrice de variance-covariance résultante et les analyses basées sur elles ne sont pas valides</font>. 
<font color="#00b050">Heureusement, `ivreg` effectuera automatiquement ces calculs et calculera des erreurs-types correctes et autres.</font>

### Woo.ex  15.5 : Rendement de l'Éducation pour les Femmes Actives (working women)
<font color="#00b0f0">Continuer l'Exemple 15.1 et  estimer le rendement de l'éducation pour les femmes en utilisant les données de MROZ.dta. </font><font color="#c0504d">Nous allons utiliser à la fois l'éducation de la mère et du père comme instruments pour l'éducation des femmes actives. </font>

Le Script 15.3 (Example-15-5.R), <font color="#00b0f0">deux manières d'estimer le modèle 2SLS</font> : 
- <font color="#c0504d">Effectuer les deux étapes manuellement</font>, avec l'éducation ajustée `fitted(stage1)` comme régresseur dans la deuxième étape. 
- `ivreg` <font color="#00b050">exécute ces opérations de façon automatique</font> et donne les mêmes estimations de paramètres (cf.tableau de sortie}. Mais les erreurs-types diffèrent légèrement car la version manuelle en deux étapes ne les a pas corrigées.

### Script 15.3 Estimation en 2 étapes et Estimation automatique d'un rég IV (Var instrumentale)
```
Script 15.3: Example-15-5.R

 library(AER);library(stargazer)
 data(mroz, package='wooldridge')
 
 # restreindre aux observations avec salaire non manquant
 oursample <- subset(mroz, !is.na(wage))
 
 # 1ère étape : forme réduite
 stage1 <- lm(educ~exper+I(exper^2)+motheduc+fatheduc, data=oursample)
 
 # 2ème étape
 man.2SLS<-lm(log(wage)~fitted(stage1)+exper+I(exper^2), data=oursample)
 
 # Estimation 2SLS automatique
 aut.2SLS<-ivreg(log(wage)~educ+exper+I(exper^2)
                 | motheduc+fatheduc+exper+I(exper^2) , data=oursample)

 # Joli tableau de régression
 stargazer(stage1,man.2SLS,aut.2SLS,type="text",keep.stat=c("n","rsq"))
```

## 15.4. Test d'Exogénéité des Régresseurs
<font color="#00b0f0">Autre façon d'obtenir les mêmes estimations de paramètres VI qu'avec 2SLS. </font>
Dans le même cadre que ci-dessus, <font color="#00b0f0">cette "approche par fonction de contrôle" consiste également en deux étapes :</font>
1. <font color="#c0504d">Comme dans 2SLS, régressez</font> $y_2$ et $y_3$ sur $z_1$ à $z_5$. <font color="#00b050">Obtenez les résidus</font> $\hat{v}_2$ et $\hat{v}_3$ <font color="#7030a0">au lieu des valeurs ajustées </font>$\hat{y}_2$ et $\hat{y}_3$.
2. <font color="#00b050">Régressez</font> $y_1$ <font color="#00b050">sur</font> $y_2$, $y_3$, $z_1$, $z_2$, $z_3$ <font color="#00b050">et les résidus de la première étape</font> $\hat{v}_2$ <font color="#00b050">et</font> $\hat{v}_3$.

<font color="#c0504d">Cette approche</font> est aussi simple à implémenter que 2SLS et <font color="#c0504d">aboutira aux mêmes estimations de paramètres</font> <font color="#00b050">et à des erreurs-types MCO invalides dans la deuxième étape </font>(<font color="#c0504d">à moins que les régresseurs douteux</font> $y_2$ et $y_3$ <font color="#c0504d">ne soient en fait exogènes</font>).

Après cette régression de deuxième étape, <font color="#00b0f0">nous pouvons tester l'exogénéité  en supposant que les instruments sont valides.</font> <font color="#00b050">Nous avons juste besoin de faire un test $t$ ou $F$ de l'hypothèse nulle que les paramètres des résidus de première étape sont égaux à zéro.</font> <font color="#00b0f0">Si nous rejetons cette hypothèse, cela indique une endogénéité de</font> $y_2$ <font color="#00b050">et</font> $y_3$.

### Woo.ex  15.7 : Rendement de l'Éducation pour les Femmes Actives
Dans le Script 15.4 (Example-15-7.R), <font color="#c0504d">nous continuons l'Exemple 15.5 en utilisant l'approche par fonction de contrôle</font>. 
Encore une fois, <font color="#c0504d">nous utilisons à la fois l'éducation de la mère et du père comme instruments</font>. 
- <font color="#c0504d">La régression de première étape est identique à celle du Script 15.3</font> (Example-15-5.R). 
- <font color="#00b050">La deuxième étape ajoute les résidus de première étape à la liste originale des régresseurs</font>. 

Les estimations de paramètres sont identiques à la fois aux résultats 2SLS manuels et aux résultats automatiques `ivreg`. 
<font color="#00b0f0">Nous pouvons interpréter directement le test $t$ du tableau de régression comme un test d'exogénéité</font>. 
- Ici, $t = 1.6711$ avec une valeur $p$ bilatérale de $p = 0.095$, <font color="#00b050">indiquant une évidence marginalement significative d'endogénéité.</font>

```
Script 15.4: Example-15-7.R

 library(AER);library(lmtest)
 data(mroz, package='wooldridge')
 
 # restreindre aux observations avec salaire non manquant
 oursample <- subset(mroz, !is.na(wage))
 
 # 1ère étape : forme réduite
 stage1<-lm(educ~exper+I(exper^2)+motheduc+fatheduc, data=oursample)
 
 # 2ème étape
 stage2<-lm(log(wage)~educ+exper+I(exper^2)+resid(stage1),data=oursample)
 
 # résultats incluant les tests t
 coeftest(stage2)
```

## 15.5. Test des Restrictions de Surodentification
<font color="#c0504d">Si nous avons plus d'instruments que de variables endogènes, nous pouvons utiliser tous ou seulement certains d'entre eux. </font>
- Si tous sont valides, utiliser tous améliore la précision de l'estimateur 2SLS et réduit ses erreurs-types. 
- Si l'exogénéité de certains est douteuse, les inclure pourrait causer une inconsistance. 
<font color="#00b0f0">Il est donc utile de tester l'exogénéité d'un ensemble d'instruments douteux</font> 
- <font color="#c0504d">à condition d'avoir un autre ensemble (suffisamment grand)</font>
- <font color="#00b050">qui est incontestablement exogène</font>. 

<font color="#c0504d">La procédure est décrite par Wooldridge (2019, Section 15.5) </font>:
1. Estimez le modèle par 2SLS et obtenez les résidus $\hat{u}_1$.
2. Régressez $\hat{u}_1$ sur toutes les variables exogènes et calculez $R_1^2$.
3. La statistique de test $n R_1^2$ est asymptotiquement distribuée comme $\chi_q^2$, où $q$ est le nombre de restrictions de _surodentification_, c'est-à-dire le nombre d'instruments moins le nombre de régresseurs endogènes.

### Woo.ex  15.8 : Rendement de l'Éducation pour les Femmes Actives
Nous utiliserons à nouveau les données et le modèle des Exemples 15.5 et 15.7. 
- Le Script 15.5 (Example-15-8.R) estime le modèle en utilisant `ivreg`. 
	- Les résultats sont stockés dans la variable res.2sls et leur `summary` est imprimé. 
- Nous exécutons ensuite la régression auxiliaire (2) et calculons son $R^2$ comme r2. 
	- La statistique de test est calculée comme teststat=0.378. 
- Nous calculons également la valeur $p$ à partir de la distribution $\chi_1^2$. 

<font color="#00b0f0">Nous ne pouvons pas rejeter l'exogénéité des instruments en utilisant ce test</font>. <font color="#00b050">Mais soyez conscient du fait que l'hypothèse sous-jacente qu'au moins un instrument est valide pourrait être violée ici.</font>

## 15.6. Variables Instrumentales avec Données de Panel
Les variables instrumentales peuvent également être utilisées pour les données de panel. 
- nous pouvons<font color="#00b0f0"> éliminer l'hétérogénéité individuelle constante dans le temps par différenciation ou transformations within</font>, 
- <font color="#00b050">puis corriger les problèmes d'endogénéité restants avec des variables instrumentales.</font>
Nous savons comment obtenir des estimations de données de panel en utilisant MCO sur les données transformées, donc nous pouvons facilement utiliser VI comme avant. 

Mais nous pouvons le faire encore plus commodément : 
<font color="#00b050">La commande</font> `plm` <font color="#00b050">du package</font> _**plm**_ <font color="#00b050">permet d'entrer directement les instruments.</font> <font color="#c0504d">Comme avec</font> `ivreg`, <font color="#c0504d">nous pouvons simplement ajouter une liste d'instruments après le signe </font>`|` <font color="#c0504d">dans la formule.</font>

### Woo.ex  15.10 : Formation Professionnelle et Productivité des Travailleurs
<font color="#00b0f0">Nous utilisons le data set JTRAIN.dta pour estimer l'effet de la formation professionnelle hrsemp sur le taux de rebut.</font> 
Dans le Script 15.6 (Example-15-10.R), 
- nous chargeons les données, 
- choisissons un `subset` des années 1987 et 1988 
- et stockons les données comme un `pdata.frame` en utilisant les variables d'index fcode et year, voir Section 13.3. 
- Ensuite, nous estimons les paramètres en utilisant la différenciation avec la variable instrumentale grant.

```
Script 15.5: Example-15-8.R
 library(AER)
 data(mroz, package='wooldridge')
 
 '# restreindre aux observations avec salaire non manquant
 oursample <- subset(mroz, !is.na(wage))
 
 '# Régression VI
 summary( res.2sls <- ivreg(log(wage) ~ educ+exper+I(exper^2)
                            | exper+I(exper^2)+motheduc+fatheduc,data=oursample) )

 '# Régression auxiliaire
 res.aux <- lm(resid(res.2sls) ~ exper+I(exper^2)+motheduc+fatheduc
                , data=oursample)
 '# Calculs pour le test
 ( r2 <- summary(res.aux)$r.squared )

 ( n <- nobs(res.aux) )

 ( teststat <- n*r2 )

 ( pval <- 1-pchisq(teststat,1) )
```


```
Script 15.6: Example-15-10.R
 library(plm)
 data(jtrain, package='wooldridge')
 
 # Définir les données de panel (pour 1987 et 1988 seulement)
 jtrain.87.88 <- subset(jtrain,year<=1988)
 
 jtrain.p<-pdata.frame(jtrain.87.88, index=c("fcode","year"))
 
 #  IV FD Régression
 summary( plm(log(scrap)~hrsemp|grant, model="fd",data=jtrain.p) )
```