# 17. Modèles à Variable Dépendante Limitée et Corrections de Sélection d'Échantillon
<font color="#00b0f0">Une variable dépendante limitée (LDV) ne peut prendre qu'un ensemble limité de valeurs</font>. <font color="#7030a0">Un cas extrême est une variable binaire qui ne peut prendre que deux valeurs.</font> 
Nous avons déjà utilisé de telles variables muettes comme régresseurs au Chapitre 7. 
<font color="#00b050">La Section 17.1 discute de comment les utiliser comme variables dépendantes</font>. 
<font color="#00b050">La Section 17.2 couvre  les comptages;</font> ce sont un autre exemple de LDV qui ne prennent que des entiers non négatifs. 
<font color="#00b050">La Section 17.3 couvre les modèles Tobit</font> qui  traitent des variables dépendantes ne pouvant prendre que des valeurs positives (ou sont restreintes de manière similaire), mais sont continues.
<font color="#00b050">Les Sections 17.4 et 17.5 concernent les variables dépendantes qui sont continues mais pas parfaitement observées.</font> Pour certaines unités des observations censurées, tronquées ou sélectionnées, nous savons seulement qu'elles sont au-dessus ou en dessous d'un certain seuil ou nous ne savons rien à leur sujet.

## 17.1 Réponses Binaires

Les variables dépendantes binaires sont fréquemment étudiées en économétrie appliquée. 
<font color="#c0504d">Parce qu'une variable muette</font> $y$ <font color="#c0504d">ne peut prendre que les valeurs 0 et 1</font>, <font color="#00b0f0">son espérance (conditionnelle) est égale à la probabilité (conditionnelle) que </font>$y = 1$ :  
   $$\text{E}(y|/mathbf{x}) = 0 \cdot \text{P}(y = 0|/mathbf{x}) + 1 \cdot \text{P}(y = 1|/mathbf{x}) = \text{P}(y = 1|/mathbf{x}) \tag{17.1}$$
Ainsi, <font color="#c0504d">lorsque nous étudions l'espérance conditionnelle, il est logique d'y penser comme à la probabilité du résultat</font> $y = 1$. <font color="#00b0f0">De même, la valeur prédite</font> $\hat{y}$ <font color="#00b0f0">doit être considérée comme une probabilité prédite.</font>

### 17.1.1. Modèles de Probabilité Linéaire
<font color="#7030a0">Si une variable muette est utilisée comme variable dépendante </font>$y$, <font color="#00b0f0">nous pouvons toujours utiliser MCO pour estimer sa relation avec les régresseurs</font> $\mathbf{x}$. Ces modèles de probabilité linéaire sont couverts par Wooldridge (2019) dans la Section 7.5.

<font color="#c0504d">Si nous écrivons le modèle de régression linéaire habituel</font> : $y = \beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k + u \tag{17.2}$
et faisons les hypothèses habituelles, en particulier MLR.4 : $\text{E}(u | /mathbf{x}) = 0$, cela implique pour l'espérance conditionnelle (qui est la probabilité que $y = 1$) et les probabilités prédites  
$\text{P}(y = 1|/mathbf{x}) = \text{E}(y|/mathbf{x}) = \beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k \tag{17.3}$
$\hat{\text{P}} (y = 1|/mathbf{x}) = \hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x_1 + \cdots + \hat{\beta}_k x_k \tag{17.4}$
<font color="#c0504d">L'interprétation des paramètres est simple</font> : 
$\beta_j$ <font color="#00b0f0">est une mesure du changement moyen de probabilité d'un "succès" </font>($y = 1$)<font color="#00b0f0"> lorsque</font> $x_j$ <font color="#00b0f0">augmente d'une unité et les autres déterminants restent constants.</font> 
<font color="#c0504d">Les modèles de probabilité linéaire souffrent automatiquement d'hétéroscédasticité,</font> <font color="#00b050">donc avec MCO, nous devrions utiliser des inférences robustes à l'hétéroscédasticité</font>, voir Section 8.1.

### Wooldridge, Exemple 17.1 : Participation des Femmes Mariées à la Population Active
<font color="#c0504d">Nous étudions la probabilité qu'une femme participe à la population active en fonction de caractéristiques sociodémographiques.</font> 
<font color="#00b0f0">Le Script 17.1 (Example-17-1-1.R) estime un modèle de probabilité linéaire en utilisant le data set mroz.dta.</font> 
<font color="#c0504d">Le coefficient estimé de educ peut être interprété comme </font>: <font color="#00b050">une année supplémentaire de scolarité augmente la probabilité qu'une femme participe à la population active ceteris paribus de 0,038 en moyenne.</font>

```
Script 17.1: Example-17-1-1.R

 library(car); library(lmtest) # pour les erreurs-types robustes
 data(mroz, package='wooldridge')
 
 # Estimer le modèle de probabilité linéaire
 linprob <- lm(inlf~nwifeinc+educ+exper+I(exper^2)+age+kidslt6+kidsge6,data=mroz)
 
 # Tableau de régression avec erreurs-types robustes à l'hétéroscédasticité et tests t :
 coeftest(linprob,vcov=hccm)
```

<font color="#c0504d">Un problème avec les modèles de probabilité linéaire</font> est que 
- $\text{P}(y = 1 | /mathbf{x})$ est spécifiée comme une fonction linéaire des régresseurs. 
- Par construction, il existe des combinaisons (+ ou - réalistes) de valeurs de régresseurs qui donnent $\hat{y} < 0$ ou $\hat{y} > 1$
- Puisque ce sont des probabilités, cela n'a pas vraiment de sens.

<font color="#00b050">Comme exemple, le Script 17.2</font> (Example-17-1-2.R)<font color="#00b050"> calcule les valeurs prédites pour deux femmes </font>(<font color="#00b0f0">Section 6.2 explique comment effectuer une</font> `prediction`<font color="#00b0f0"> après une estimation MCO</font>) : 
- La femme 1 a 20 ans, n'a pas d'expérience professionnelle, 5 ans d'éducation, deux enfants de moins de 6 ans et a un revenu familial supplémentaire de 100 000 USD. 
- La femme 2 a 52 ans, a 30 ans d'expérience professionnelle, 17 ans d'éducation, pas d'enfants et aucune autre source de revenu. 
<font color="#c0504d">La "probabilité" prédite pour la femme 1 est de -41 %</font>, <font color="#6425d0">la probabilité pour la femme 2 est de 104 %</font> comme on peut aussi facilement vérifier avec une calculatrice.
Pour effectuer la prédiction, on crée une list avec les valeurs des paramètres de chacune des femmes. Puis la liste est fournie, en même temps que le type de fonction (ici linprob) comme argument à la fonction `predict`.
```
Script 17.2: Example-17-1-2.R

# prédictions pour deux femmes "extrêmes" (exécutez d'abord Example-17-1-1.R !) :
 xpred <- list(nwifeinc=c(100,0),educ=c(5,17),exper=c(0,30),
                age=c(20,52),kidslt6=c(2,0),kidsge6=c(0,0))
                
 predict(linprob,xpred)
```

### 17.1.2. Modèles Logit et Probit : Estimation

<font color="#c0504d">Des modèles spécialisés pour les réponses binaires s'assurent que les probabilités implicites sont restreintes entre 0 et 1.</font> Une classe importante de modèles spécifie la probabilité de succès comme  $\text{P}(y = 1|/mathbf{x}) = G(/beta_0 + /beta_1 x_1 + /cdots + /beta_k x_k) = G(/mathbf{x}/boldsymbol{/beta}) \tag{17.5}$
où <font color="#00b0f0">la "fonction de lien"</font> $G(z)$ <font color="#00b0f0">renvoie toujours des valeurs entre 0 et 1</font>. Dans la littérature statistique, <font color="#c00000">ce type de modèles est souvent appelé modèle linéaire généralisé (GLM)</font> car une partie linéaire $\mathbf{x}\boldsymbol{\beta}$ apparaît à l'intérieur de la fonction non linéaire $G$.

Pour les modèles à réponse binaire, de loin <font color="#00b0f0">les spécifications les plus largement utilisées pour </font>$G$ sont
- <font color="#00b050">le modèle</font> **probit** <font color="#00b050">avec</font> $G(z) = \Phi(z)$, <font color="#00b050">la cdf normale standard</font> et
- <font color="#00b050">le modèle</font> **logit** <font color="#00b050">avec</font> $G(z) = \Lambda(z) = \frac{\exp(z)}{1+\exp(z)}$, <font color="#00b050">la cdf de la distribution logistique</font>.

Wooldridge (2019, Section 17.1) fournit des discussions utiles sur la dérivation et l'interprétation de ces modèles. Ici, nous nous intéressons à l'implémentation pratique. 
<font color="#c0504d">Dans</font> $R$,<font color="#c0504d"> de nombreux modèles linéaires généralisés peuvent être estimés avec la commande</font> `glm` qui fonctionne de manière similaire à `lm`. Elle accepte les <font color="#00b0f0">options supplémentaires</font>
- `family=binomial(link=logit)`<font color="#00b0f0"> pour le modèle logit</font> ou
- `family=binomial(link=probit)`<font color="#00b0f0"> pour le modèle</font> probit.

<font color="#00b050">L'estimation du maximum de vraisemblance (MLE) des paramètres est faite automatiquement et le</font> `summary` <font color="#00b050">des résultats contient le tableau de régression le plus important et des informations supplémentaires. </font>

<font color="#c0504d">Les Scripts 17.3 </font>(Example-17-1-3.R)<font color="#c0504d"> et 17.4</font> (Example-17-1-4.R) <font color="#c0504d">implémentent cela pour les modèles logit et probit,</font> respectivement. 
- La valeur de log-vraisemblance $L(/hat{/boldsymbol{/beta}})$ n'est pas rapportée par défaut mais peut être demandée avec la fonction `logLik`
- Au lieu de cela, une statistique appelée Déviance résiduelle est rapportée dans la sortie standard. 
	- Elle est simplement définie comme $D(/hat{/boldsymbol{/beta}}) = -2L(/hat{/boldsymbol{/beta}})$. 
	- La déviance nulle signifie $D_0 = -2L_0$ où $L_0$ est la vraisemblance d'un modèle avec seulement une constante.

<font color="#00b050">Les deux statistiques de déviance peuvent être accessées </font>pour des calculs supplémentaires à partir d'un résultat stocké res avec `res$deviance` et `res$null.deviance`. 
<font color="#00b0f0">Les Scripts 17.3 </font>(Example-17-1-3.R) et 17.4 (Example-17-1-4.R)<font color="#00b0f0"> présentent le calcul de différentes statistiques dérivées de ces résultats.</font>

<font color="#d83931">Le pseudo R-carré de McFadden peut être calculé comme  </font>
$\text{pseudo } R^2 = 1 - \frac{L(/hat{/boldsymbol{/beta}})}{L_0} = 1 - \frac{D(/hat{/boldsymbol{/beta}})}{D_0}. \tag{17.6}$
 
```
Script 17.3: Example-17-1-3.R

 data(mroz, package='wooldridge')
 
 # Estimer le modèle logit
 logitres<-glm(inlf~nwifeinc+educ+exper+I(exper^2)+age+kidslt6+kidsge6,
                family=binomial(link=logit),data=mroz)
                
 # Résumé des résultats :
 summary(logitres)

 # Valeur de log-vraisemblance :
 logLik(logitres)

 # Pseudo R2 de McFadden :
 1 - logitres$deviance/logitres$null.deviance
```

```
Script 17.4: Example-17-1-4.R

 data(mroz, package='wooldridge')
 
 # Estimer le modèle probit
 probitres<-glm(inlf~nwifeinc+educ+exper+I(exper^2)+age+kidslt6+kidsge6,
                 family=binomial(link=probit),data=mroz)
                 
 # Résumé des résultats :
 summary(probitres)

 # Valeur de log-vraisemblance :
 logLik(probitres)

 # Pseudo R2 de McFadden :
 1 - probitres$deviance/probitres$null.deviance
```

### 17.1.3 Inférence

<font color="#00b0f0">L'output </font>`summary` <font color="#00b0f0">des résultats ajustés</font> `glm` <font color="#00b0f0">contient un tableau de régression standard avec </font>
- des paramètres et des erreurs-types (asymptotiques). 
- La colonne suivante est étiquetée z value au lieu de t value dans la sortie de `lm`. 
	- L'interprétation est la même. 
	- La différence est que les erreurs-types n'ont qu'une base asymptotique et la distribution utilisée pour calculer les valeurs $p$ est la distribution normale standard (qui est égale à la distribution $t$ avec un très grand nombre de degrés de liberté). 
La conclusion est que les tests pour des paramètres uniques peuvent être faits comme avant, voir Section 4.1.

<font color="#c0504d">Pour tester des hypothèses multiples,</font> <font color="#00b050">le test du rapport de vraisemblance est populaire</font>. Similaires au test $F$ (voir Section 4.3),  <font color="#00b0f0">il est basé sur la comparaison des valeurs de log-vraisemblance du modèle non restreint et du modèle restreint</font>. 

<font color="#c0504d">La statistique de test es</font>t  $LR = 2(L_{ur} - L_r) = D_r - D_{ur} \tag{17.7}$
- où $L_{ur}$ et $L_r$ sont les valeurs de log-vraisemblance du modèle non restreint et restreint, respectivement, 
- et $D_{ur}$ et $D_r$ sont les statistiques de déviance rapportées correspondantes. 
Sous $H_0$, la statistique de test $LR$ est asymptotiquement distribuée comme $\chi^2$ avec les degrés de liberté égaux au nombre de restrictions à tester. 
L<font color="#c0504d">e test de significativité globale est un cas particulier comme avec les tests-</font>$F$.<font color="#00b0f0"> L'hypothèse nulle est que tous les paramètres sauf la constante sont égaux à zéro</font>. Avec la notation ci-dessus, la statistique de test est  
$LR = 2\left[ L(/hat{/boldsymbol{/beta}}) - L_0 \right] = D_0 - D(/hat{/boldsymbol{/beta}}). \tag{17.8}$
<font color="#00b0f0">Traduit en $R$ avec des résultats de modèle ajustés stockés dans res, cela correspond à</font>  
`LR = res$null.deviance - res$deviance`

<font color="#00b050">Le package </font>_**lmtest**_ <font color="#00b050">offre également le test LR comme fonction</font> `lrtest` <font color="#00b050">incluant le calcul pratique des valeurs</font> $p$. 
<font color="#c0504d">La syntaxe est</font>
- `lrtest(res)` pour un test de significativité globale pour le modèle res
- `lrtest(restr, unrestr)` pour un test du modèle restreint restr vs. le modèle non restreint unrestr

<font color="#00b050">Le Script 17.5 (Example-17-1-5.R)</font> 
- <font color="#c00000">implémente le test de significativité globale pour le modèle probit</font> <font color="#00b0f0">en utilisant à la fois des calculs manuels et automatiques.</font> 
- <font color="#c0504d">Il teste également l'hypothèse nulle conjointe</font> que l'expérience et l'âge ne sont pas pertinents 
	- en estimant d'abord le modèle restreint 
	- puis en exécutant le test LR automatisé.

```
Script 17.5: Example-17-1-5.R

# Test de significativité globale :
# Calcul manuel de la statistique de test LR :
 probitres$null.deviance - probitres$deviance

# Calculs automatiques incluant valeurs p,... :
 library(lmtest)
 lrtest(probitres)
 
# Test de H0: l'expérience et l'âge ne sont pas pertinents
 restr <- glm(inlf~nwifeinc+educ+ kidslt6+kidsge6,
                family=binomial(link=probit),data=mroz)
 lrtest(restr,probitres)
```

### 17.1.4. Prédictions
<font color="#00b050">La commande</font> `predict`<font color="#00b050"> peut calculer</font> 
- les valeurs prédites pour l'échantillon d'estimation ("valeurs ajustées") 
- ou des ensembles arbitraires de valeurs de régresseurs également pour les modèles à réponse binaire estimés avec `glm`
Étant donné que les résultats sont stockés dans la variable res, nous pouvons calculer
- $\mathbf{x}_i \hat{\boldsymbol{\beta}}$ pour l'échantillon d'estimation avec `predict(res)`
- $\mathbf{x}_i \hat{\boldsymbol{\beta}}$ pour les valeurs de régresseurs stockées dans xpred avec `predict(res, xpred)`
- $\hat{y} = G(/mathbf{x}_i /hat{/boldsymbol{/beta}})$ pour l'échantillon d'estimation avec `predict(res, type = "response")`
- $\hat{y} = G(/mathbf{x}_i /hat{/boldsymbol{/beta}})$ pour les valeurs de régresseurs stockées dans xpred avec `predict(res, xpred, type = "response")`

<font color="#00b0f0">Les prédictions pour les deux femmes hypothétiques introduites dans la Section 17.1.1 sont répétées pour les modèles de probabilité linéaire, logit et probit dans le Script 17.6</font> (Example-17-1-6.R).

Contrairement au modèle de probabilité linéaire, les probabilités prédites des modèles logit et probit restent entre 0 et 1.
```
Script 17.6: Example-17-1-6.R

# Prédictions à partir des modèles de probabilité linéaire, probit et logit :
# (exécutez d'abord 17-1-1.R à 17-1-4.R pour définir les variables !)
 predict(linprob, xpred,type = "response")

 predict(logitres, xpred,type = "response")

 predict(probitres,xpred,type = "response")
```

**Figure 17.1.** Prédictions des modèles à réponse binaire (données simulées)  
_Légende : Graphique montrant les probabilités prédites en fonction de x pour les modèles de probabilité linéaire, logit et probit. Les modèles logit et probit restent entre 0 et 1, contrairement au modèle linéaire._

Si nous n'avons qu'un seul régresseur, les valeurs prédites peuvent être tracées élégamment contre lui. La Figure 17.1 montre une telle figure pour un data set simulées. 
Pour les lecteurs intéressés, le script utilisé pour générer les données et la figure est imprimé comme Script 17.7 (Binary-Predictions.R) dans l'Annexe IV (p. 351). Dans cet exemple, 
- le modèle de probabilité linéaire prédit clairement des probabilités en dehors de la zone "légale" entre 0 et 1. 
- Les modèles logit et probit donnent des prédictions presque identiques. 
C'est un constat général qui vaut pour la plupart des ensembles de données.

### 17.1.5. Effets Partiels
<font color="#c0504d">Les paramètres des modèles de régression linéaire ont des interprétations simples</font> : $\beta_j$ mesure l'effet _ceteris paribus_ de $x_j$ sur $\text{E}(y|/mathbf{x})$. 
<font color="#c0504d">Les paramètres des modèles non linéaires comme logit et probit ont une interprétation moins simple</font> 
- puisque l'indice linéaire $\mathbf{x}\boldsymbol{\beta}$ affecte $\hat{y}$ 
- à travers la fonction de lien $G$.

<font color="#00b0f0">Une mesure utile de l'influence est l'effet partiel (ou effet marginal) </font><font color="#00b050">qui dans un graphique comme la Figure 17.1 est la pente et a la même interprétation que les paramètres dans le modèle linéaire</font>. En raison de la règle de la chaîne, c'est  
$\frac{\partial \hat{y}}{\partial x_j} = \frac{\partial G(/hat{/beta}_0 + /hat{/beta}_1 x_1 + /cdots + /hat{/beta}_k x_k)}{\partial x_j} = \hat{\beta}_j \cdot g(/hat{/beta}_0 + /hat{/beta}_1 x_1 + /cdots + /hat{/beta}_k x_k), \tag{17.9}$ 
où $g(z)$ est la dérivée de la fonction de lien $G(z)$. 

<font color="#c0504d">Donc</font>
- <font color="#00b050">pour le modèle probit, l'effet partiel est</font> $\frac{\partial \hat{y}}{\partial x_j} = \hat{\beta}_j \cdot \phi(/mathbf{x}/hat{/boldsymbol{/beta}})$
- <font color="#00b050">pour le modèle logit, c'es</font>t $\frac{\partial \hat{y}}{\partial x_j} = \hat{\beta}_j \cdot \lambda(/mathbf{x}/hat{/boldsymbol{/beta}})$  
  où $\phi(z)$ et $\lambda(z)$ sont les pdf de la distribution normale standard et de la distribution logistique, respectivement.
  
L'effet partiel dépend de la valeur de $\mathbf{x}\hat{\boldsymbol{\beta}}$. Les pdf ont la fameuse forme en cloche avec les valeurs les plus élevées au milieu et des valeurs proches de zéro dans les queues. Cela est déjà évident d'après la Figure 17.1.

**Figure 17.2.** Effets partiels pour les modèles à réponse binaire (données simulées)  
_Légende : Graphique montrant l'effet partiel (pente) en fonction de x pour les modèles de probabilité linéaire, logit et probit. L'effet n'est constant que pour le modèle linéaire._

En fonction de la valeur de $x$, la pente de la probabilité diffère. Pour notre data set simulées, la Figure 17.2 montre les effets partiels estimés pour les 100 valeurs observées de $x$. Les lecteurs intéressés peuvent voir le code complet pour cela comme Script 17.8 (Binary-Margeff.R) dans l'Annexe IV (p. 352).

<font color="#c0504d">Le fait que les effets partiels diffèrent selon les valeurs des régresseurs rend plus difficile la présentation des résultats de manière concise et significative. </font><font color="#00b050">Il existe deux façons courantes d'agréger les effets partiels :</font>
- <font color="#00b050">Effets partiels à la moyenne</font> : $EPA = \hat{\beta}_j \cdot g(/bar{/mathbf{x}}/hat{/boldsymbol{/beta}})$
- <font color="#00b050">Effets partiels moyens</font> : $EPM = \frac{1}{n} \sum_{i=1}^{n} \hat{\beta}_j \cdot g(/mathbf{x}_i /hat{/boldsymbol{/beta}}) = \hat{\beta}_j \cdot \overline{g(/mathbf{x}/hat{/boldsymbol{/beta}})}$  
  où $\bar{\mathbf{x}}$ est le vecteur des moyennes d'échantillon des régresseurs et $\overline{g(/mathbf{x}/hat{/boldsymbol{/beta}})}$ est la moyenne d'échantillon de $g$ évaluée à l'indice linéaire individuel $\mathbf{x}_i \hat{\boldsymbol{\beta}}$. Les deux mesures multiplient chaque coefficient $\hat{\beta}_j$ par un facteur constant.

<font color="#00b0f0">Le Script 17.9 (Example-17-1-7.R) implémente les calculs EPM pour notre exemple de participation à la population active en utilisant des fonctions </font>$R$ déjà connues :
1. Les indices linéaires $\mathbf{x}_i \hat{\boldsymbol{\beta}}$ sont calculés en utilisant `predict`
2. Les facteurs $g(/mathbf{x}/hat{/boldsymbol{/beta}})$ sont calculés en utilisant les fonctions de densité `dlogis` et `dnorm` puis moyennés sur l'échantillon avec `mean`.
3. Les EPM sont calculés en multipliant le vecteur de coefficients obtenu avec `coef` par le facteur correspondant. Notez que pour le modèle de probabilité linéaire, les effets partiels sont constants et simplement égaux aux coefficients.

<font color="#00b0f0">Les résultats pour la constante n'ont pas d'interprétation significative directe.</font> <font color="#00b050">Les EPM pour les autres variables ne diffèrent pas trop entre les modèles</font>. 

<font color="#c0504d">Comme observation générale, le modèle de probabilité linéaire fonctionne souvent assez bien</font> 
- tant que nous nous intéressons uniquement aux EPM et non aux prédictions individuelles ou aux effets partiels 
- et tant que pas trop de probabilités sont proches de 0 ou 1, .

```
Script 17.9: Example-17-1-7.R

# EPM (exécutez d'abord 17-1-1.R à 17-1-4.R pour définir les variables !)

# Calcul de l'indice linéaire aux valeurs individuelles :
 xb.log <- predict(logitres)
 xb.prob<- predict(probitres)
 
# Facteurs EPM = moyenne(g(xb))
 factor.log <- mean( dlogis(xb.log) )
 factor.prob<- mean( dnorm(xb.prob) )
 cbind(factor.log,factor.prob)

# effets partiels moyens = beta*factor :
 APE.lin <- coef(linprob) * 1
 APE.log <- coef(logitres) * factor.log
 APE.prob<- coef(probitres) * factor.prob
 
# Tableau des EPM
 cbind(APE.lin, APE.log, APE.prob)
```

<font color="#00b050">Un package pratique pour calculer</font> EPA et EPM est _**mfx**_. <font color="#00b050">Entre autres, il fournit les commandes</font> `logitmfx` et `probitmfx`. <font color="#00b0f0">Elles estiment le modèle correspondant et affichent un tableau de régression non pas avec des estimations de paramètres mais avec des EPA avec l'option</font> `atmean=TRUE` <font color="#00b0f0">et des EPM avec l'option</font> `atmean=FALSE`. 

<font color="#00b050">Le Script 17.10 (Example-17-1-8.R) l'implémente pour le modèle logit de notre exemple de participation à la population active.</font> <font color="#00b0f0">Les EPM rapportés sont les mêmes que ceux calculés manuellement dans le Script 17.9 (Example-17-1-7.R).</font>

```
Script 17.10: Example-17-1-8.R

# Calculs automatiques des EPM avec le package mfx
 library(mfx)
 
 logitmfx(inlf~nwifeinc+educ+exper+I(exper^2)+age+kidslt6+kidsge6,
           data=mroz, atmean=FALSE)
```

## 17.2. Données de Comptage : Le Modèle de Régression de Poisson
<font color="#00b0f0">Au lieu de données binaires codées 0/1, les données de comptage peuvent prendre tout entier non négatif 0,1,2,. . . </font>
<font color="#c0504d">Quand elles prennent des nombres très grands</font> (comme le nombre d'élèves dans une école), 
- elles peuvent être raisonnablement bien approximées comme des variables continues dans des modèles linéaires 
- et estimées en utilisant MCO. 
<font color="#c0504d">Quand les nombres sont relativement petits</font> (comme le nombre d'enfants d'une mère), 
- cette approximation pourrait ne pas bien fonctionner. 
- Par exemple, les valeurs prédites peuvent devenir négatives.

<font color="#00b050">Le modèle de régression de Poisson est le modèle le plus basique et pratique explicitement conçu pour les données de comptage.</font> La probabilité que $y$ prenne n'importe quelle valeur $h \in {0, 1, 2, \ldots}$ pour ce modèle peut être écrite comme  
$$\text{P}(y = h|/mathbf{x}) = \frac{e^{-e^{\mathbf{x}\boldsymbol{\beta}}} \cdot e^{h \cdot \mathbf{x}\boldsymbol{\beta}}}{h!} \tag{17.11}$$
<font color="#00b0f0">Les paramètres du modèle de Poisson sont beaucoup plus faciles à interpréter que ceux d'un modèle probit ou logit.</font> 
<font color="#c0504d">Dans ce modèle, l'espérance conditionnelle de  </font>$y$ est  $\text{E}(y|/mathbf{x}) = e^{\mathbf{x}\boldsymbol{\beta}}, \tag{17.12}$
donc chaque paramètre de pente $\beta_j$ a l'interprétation d'une semi-élasticité : 

$\frac{\partial \text{E}(y|/mathbf{x})}{\partial x_j} = \beta_j \cdot e^{\mathbf{x}\boldsymbol{\beta}} = \beta_j \cdot \text{E}(y|/mathbf{x}) \tag{17.13}$  $\Leftrightarrow \beta_j = \frac{1}{\text{E}(y|/mathbf{x})} \cdot \frac{\partial \text{E}(y|/mathbf{x})}{\partial x_j}. \tag{17.14}$

<font color="#00b050">Si</font> $x_j$ <font color="#00b050">augmente d'une unité (et les autres régresseurs restent les mêmes),</font> $\text{E}(y|/mathbf{x})$ <font color="#00b050">augmentera approximativement de</font> $100 \cdot \beta_j$ <font color="#00b050">pour cent</font> <font color="#00b0f0">(la valeur exacte est encore une fois</font> $100 /cdot (e^{/beta_j} - 1)$).

<font color="#c0504d">Un problème avec le modèle de Poisson est qu'il est assez restrictif.</font> 
- La distribution de Poisson restreint implicitement la variance de $y$ à être égale à sa moyenne. 
- Si cette hypothèse est violée mais que l'espérance conditionnelle est toujours correctement spécifiée, 
	- les estimations des paramètres de Poisson sont convergentes, 
	- mais les erreurs-types et toutes les inférences basées sur elles ne sont pas valides. 
<font color="#00b050">Une solution simple est d'interpréter les estimateurs de Poisson comme des estimateurs du quasi-maximum de vraisemblance (QMLE).</font> Semblable à l'inférence robuste à l'hétéroscédasticité pour MCO discutée dans la Section 8.1, <font color="#c0504d">les erreurs-types peuvent être ajustées.</font>

<font color="#00b0f0">L'estimation des modèles de régression de Poisson</font> dans $R$ est simple. 
- Ils appartiennent  à la classe des modèles linéaires généralisés (GLM) et <font color="#00b0f0">peuvent être estimés en utilisant</font> `glm`. 
- L'option pour spécifier un modèle de Poisson est `family=poisson`. 
- Pour les erreurs-types QMLE plus robustes, nous spécifions simplement `family=quasipoisson`. 

Pour implémenter des modèles de données de comptage plus avancés, voir Kleiber et Zeileis (2008, Section 5.3).

### Wooldridge, Exemple 17.3 : Régression de Poisson pour le Nombre d'Arrestations
<font color="#c0504d">Nous appliquons le modèle de régression de Poisson pour étudier le nombre d'arrestations de jeunes hommes en 1986.</font> 
<font color="#00b0f0">Le Script 17.11 (Example-17-3-1.R) </font>importe les données et 
- estime d'abord un modèle de régression linéaire en utilisant MCO. 
- Ensuite, un modèle de Poisson est estimé en utilisant `glm` avec la spécification `poisson` pour la famille GLM. 
- Enfin, nous estimons le même modèle en utilisant la spécification `quasipoisson` pour ajuster les erreurs-types pour une violation potentielle de la distribution de Poisson. 
- Nous affichons les résultats conjointement dans le Script 17.12 (Example-17-3-2.R) en utilisant la commande `stargazer` pour un tableau commun. 
Par construction, les estimations de paramètres sont les mêmes, mais les erreurs-types sont plus grandes pour le QMLE.

```
Script 17.11: Example-17-3-1.R

data(crime1, package='wooldridge')

# Estimer le modèle linéaire
lm.res <- lm(narr86~pcnv+avgsen+tottime+ptime86+qemp86+inc86+
               black+hispan+born60, data=crime1)
               
# Estimer le modèle Poisson
Poisson.res <- glm(narr86~pcnv+avgsen+tottime+ptime86+qemp86+inc86+
                     black+hispan+born60, data=crime1, family=poisson)
                     
# Modèle Quasi-Poisson
QPoisson.res<- glm(narr86~pcnv+avgsen+tottime+ptime86+qemp86+inc86+
                     black+hispan+born60, data=crime1, family=quasipoisson)
```

```
Script 17.12: Example-17-3-2.R

# Exemple 17.3 : Tableau de régression (exécutez d'abord Example-17-3-1.R !)
 library(stargazer) # package pour la sortie de régression
 
 stargazer(lm.res,Poisson.res,QPoisson.res,type="text",keep.stat="n")
```
 

**Figure 17.3.** Espérances conditionnelles pour le modèle Tobit  
_Légende : Graphique montrant la relation entre x et les espérances conditionnelles de la variable latente y_ et de la variable observée y (limitée à zéro).*

## 17.3. Corner Solution Responses : Le Modèle Tobit
<font color="#00b0f0">Les Solutions de Corner décrivent des situations où la variable d'intérêt est continue mais restreinte en amplitude.</font> <font color="#c0504d">Typiquement, elle ne peut pas être négative.</font> 
Exemple : une part significative de personnes achètent exactement zéro quantité d'alcool, de tabac ou de couches. 
<font color="#00b050">Le modèle Tobit modélise explicitement des variables dépendantes comme celle-ci. </font>

<font color="#00b0f0">Le modèle Tobit peut être formulé en termes d'une variable latente</font> $y^*$ qui peut prendre toutes les valeurs réelles. 
Pour lui, les hypothèses classiques du modèle de régression linéaire MLR.1--MLR.6 sont supposées tenir. 
<font color="#00b050">Si</font> $y^*$ <font color="#00b050">est positive, nous observons</font> $y = y^*$. <font color="#00b050">Sinon</font>, $y = 0$. 
<font color="#245bdb">hr : si y* est positive, elle est prise en compte, sinon elle est considérée comme nulle.</font> 
Wooldridge (2019, Section 17.2) montre comment dériver les propriétés et la fonction de vraisemblance pour ce modèle.

<font color="#c0504d">Le problème d'interprétation des paramètres du modèle Tobit est similaire à celui de logit ou probit</font>. 
- Alors que $\beta_j$ mesure l'effet _ceteris paribus_ de $x_j$ sur $\text{E}(y^*|/mathbf{x})$, 
- l'intérêt est plutôt typiquement pour $y$ . 

<font color="#00b050">L'effet partiel d'intérêt peut être écrit comme </font> 
  $$\frac{\partial \text{E}(y|/mathbf{x})}{\partial x_j} = \beta_j \cdot \Phi \left( /frac{/mathbf{x}/boldsymbol{/beta}}{/sigma} /right) \tag{17.15}$$
<font color="#00b0f0">et dépend à nouveau des valeurs des régresseurs</font> $\mathbf{x}$. 
P<font color="#00b050">our les agréger sur l'échantillon, nous pouvons</font>, <font color="#7030a0">comme pour les modèles à variable binaire</font>,
- soit calculer les effets partiels à la moyenne (EPA) 
- soit l'effet partiel moyen (EPM) .

<font color="#c0504d">La Figure 17.3 illustre ces propriétés pour un data set simulées avec un seul régresseur</font>. 
- Chaque fois que $y^* > 0$, y = $y^*$ et les symboles $\circ$ et $+$ sont superposés. 
- Si $y^* < 0$, alors $y = 0$. Par conséquent, la pente de $\text{E}(y|x)$ devient proche de zéro pour des valeurs de $x$ très basses. 
<font color="#6425d0">Le code qui a généré le data set et le graphique est caché comme Script 17.13 (Tobit-CondMean.R) dans l'Annexe IV (p. 353).</font>

<font color="#c0504d">Pour l'estimation ML pratique dans </font>$R$,<font color="#c0504d"> il y a différentes options.</font> 
- Le package _**AER**_ fournit la commande `tobit` et le package _**censReg**_ offre la commande `censReg`. 
- Les deux fonctionnent de manière très similaire et sont faciles à utiliser. 
<font color="#00b0f0">Nous présenterons un exemple utilisant ce dernier</font>. 
- La commande `censReg` peut être utilisée comme `lm` avec la formule du modèle et l'option data. 
- Elle estimera le modèle Tobit standard discuté ici. 
<font color="#c00000">D'autres Solutions de Corner</font> ($y /ge a$ ou $y /le b$) <font color="#c00000">peuvent être spécifiées en utilisant les options</font> `left` et `right`. 
Après avoir stocké les résultats de `censReg` dans une variable res, l'EPA peut facilement être calculé avec `margEff(res)`.

### Wooldridge, Exemple 17.2 : Offre Annuelle de W des Femmes Mariées (Married Women's Annual Labor Supply)
<font color="#00b0f0">Nous avons déjà estimé des modèles d'offre de travail pour les femmes dans le data set mroz.dta,</font> <font color="#c0504d">ignorant le fait que les heures travaillées sont nécessairement non négatives.</font> 
<font color="#00b050">Le Script 17.14 (Example-17-2.R) estime un modèle Tobit prenant en compte ce fait.</font> 
<font color="#00b0f0">Il calcule également l'EPA en utilisant </font>`margEff`.

```
Script 17.14: Example-17-2.R

 data(mroz, package='wooldridge')
 
 '# Estimer le modèle Tobit en utilisant censReg :
 library(censReg)
 TobitRes <- censReg(hours~nwifeinc+educ+exper+I(exper^2)+
                       age+kidslt6+kidsge6, data=mroz )
 summary(TobitRes)
 
 '# Effets Partiels à la moyenne x :
 margEff(TobitRes)
```
 ``
<font color="#00b050">Une autre alternative pour estimer les modèles Tobit est la commande</font> `survreg` <font color="#00b050">du package </font>_**survival**_. Elle est moins simple à utiliser mais plus flexible. Nous ne pouvons pas discuter toutes les fonctionnalités mais montrer comment reproduire les mêmes résultats pour l'Exemple 17.2 dans le Script 17.15 (Example-17-2-survreg.R). Nous reviendrons sur cette commande dans la section suivante.

```
Script 17.15: Example-17-2-survreg.R

# Estimer le modèle Tobit en utilisant survreg :
 library(survival)
 res <- survreg(Surv(hours, hours0, type="left") ~ nwifeinc+educ+exper+
                 I(exper^2)+age+kidslt6+kidsge6, data=mroz, dist="gaussian")
 summary(res)
```

## 17.4. Modèles de Régression Censurée et Tronquée

Les modèles de régression censurée sont étroitement liés aux modèles Tobit. En fait, leurs paramètres peuvent être estimés avec les mêmes logiciels. 
- Les modèles de régression censurée généraux commencent également par une variable latente $y^*$. 
- La variable dépendante observée $y$ est égale à $y^*$ pour certaines (les observations non censurées) observations. 
- Pour les autres observations, nous savons seulement une borne supérieure ou inférieure pour $y^*$. 

Dans le modèle Tobit de base, 
- nous observons $y = y^*$ dans les cas "non censurés" avec $y^* > 0$ 
- et nous savons seulement que $y^* \le 0$ si nous observons $y = 0$. 
Les règles de censure peuvent être beaucoup plus générales. Il pourrait y avoir une censure par le haut ou les seuils peuvent varier d'une observation à l'autre.

La principale différence entre Tobit et les modèles de régression censurée est l'interprétation. 
- Dans le premier cas, nous nous intéressons au $y$ observé (les y* ⩽ 0 n'existent pas ou ne nous intéressent pas) 
- dans le second cas, nous nous intéressons au $y^*$ sous-jacent.$^1$  <font color="#00b0f0">La censure est simplement un problème de données qui doit être pris en compte</font> au lieu d'une caractéristique logique de la variable dépendante. 

<font color="#c0504d">Pour estimer une régression censurée, nous pouvons utiliser les mêmes outils que pour les modèles Tobit.</font>  <font color="#00b050">Le problème du calcul des effets partiels n'existe pas </font>dans ce cas puisque nous nous intéressons à l'espérance linéaire $\text{E}(y^*|/mathbf{x})$ et <font color="#00b0f0">les paramètres de pente sont directement égaux aux effets partiels d'intérêt.</font>

note11 Wooldridge (2019, Section 7.4) utilise la notation $w$ au lieu de $y$ et $y$ au lieu de $y^*$ .

### Wooldridge, Exemple 17.4 : Durée de la Récidive
<font color="#c00000">Nous nous intéressons au pronostic criminel des individus libérés de prison. </font><font color="#00b0f0">Nous modélisons le temps qu'il leur faut pour être à nouveau arrêtés.</font>
- Les variables explicatives incluent des caractéristiques démographiques ainsi qu'une variable muette workprg indiquant la participation à un programme de travail pendant leur temps en prison. 
- Les 1445 anciens détenus observés dans le data set recid.dta ont été suivis pendant un certain temps.

Durant cette période, 893 détenus n'ont pas été arrêtés à nouveau. 
- Pour ces ex détenus, nous savons seulement que $y^*$, leur vraie durée (avant récidive), est au moins `durat`, c-a-d le temps entre la libération et la fin de la période d'observation, 
- <font color="#00b0f0">donc nous avons une censure à droite.</font> 
- et <font color="#c0504d">le seuil de censure diffère selon l'individu en fonction de sa date de libération.</font>

<font color="#00b050">En raison de la règle de sélection plus compliquée, nous utilisons la commande</font> `survreg` <font color="#00b050">pour l'estimation du modèle</font> dans le Script 17.16 (Example-17-4.R). 
- Nous devons fournir la variable dépendante log(durat) ainsi qu'une variable muette indiquant les observations _non censurées_. 
- Nous générons une variable muette uncensored dans le data frame basée sur la variable existante cens qui représente la censure.
Les paramètres peuvent être interprétés directement. 
- En raison de la spécification logarithmique, ils représentent des semi-élasticités. 
- Par exemple, les individus mariés prennent environ  $100.\hat\beta \approx34$ % plus de temps pour être à nouveau arrêtés. (En fait, le nombre précis est $100 /cdot (e^{/hat{/beta}} - 1) \approx 40$%.) 
- Il n'y a pas d'effet significatif du programme de travail.

```
Script 17.16: Example-17-4.R

 library(survival)
 data(recid, package='wooldridge')
 
 # Définir une variable muette pour les observations NON censurées
 recid$uncensored <- recid$cens==0
 
 # Estimer le modèle de régression censurée :
 res<-survreg(Surv(log(durat),uncensored, type="right") ~ workprg+priors+
                tserved+felon+alcohol+drugs+black+married+educ+age,
                data=recid, dist="gaussian")
 # Output :
 summary(res)
```

**La troncature :**
La troncation est un problème plus sérieux que la censure puisque nos observations sont plus sévèrement affectées. 
<font color="#00b0f0">Si la vraie variable latente</font> $y^*$ <font color="#00b0f0">est au-dessus ou en dessous d'un certain seuil, l'individu n'est même pas échantillonné.</font> <font color="#c0504d">Nous n'avons donc même aucune information.</font> 

<font color="#00b050">Les modèles de régression tronquée classiques reposent sur des hypothèses paramétriques et de distribution pour corriger ce problème.</font> <font color="#00b0f0">Dans </font>$R$, <font color="#00b0f0">ils sont disponibles dans le package</font> _**truncreg**_.

**Figure 17.4.** Régression tronquée : exemple simulé  
_Légende : Graphique montrant les points de données (tous et seulement ceux observés), l'ajustement MCO biaisé et l'estimation par régression tronquée._

<font color="#00b0f0">La Figure 17.4 montre les résultats pour un data set simulées.</font> 
- Parce qu'il est simulé, nous connaissons en fait les valeurs pour tout le monde (points creux et pleins). 
- Dans notre échantillon, nous n'observons que ceux avec $y > 0$ (points pleins). 
<font color="#c0504d">Lorsque nous appliquons MCO à cet échantillon, nous obtenons une pente biaisée vers le bas (ligne pointillée). </font>
<font color="#00b050">La régression tronquée corrige ce problème et donne un estimateur de pente convergent (ligne pleine).</font> 
Le Script 17.17 (TruncReg-Simulation.R) qui a généré le data set et le graphique est montré dans l'Annexe IV (p. 354).

## 17.5. Corrections de Sélection d'Échantillon
Les modèles de sélection d'échantillon sont liés aux modèles de régression tronquée. 
- Nous avons un échantillon aléatoire de la population d'intérêt, 
- mais nous n'observons pas la variable dépendante $y$ pour un sous-échantillon non aléatoire. 
La sélection d'échantillon n'est pas basée sur un seuil pour $y$ mais sur un autre mécanisme de sélection.

Le modèle de sélection de Heckman consiste en 
- un modèle de type probit pour le fait binaire de savoir si $y$ est observé 
- et un modèle de type régression linéaire pour $y$. 
La sélection peut être déterminée par les mêmes déterminants que $y$ mais devrait avoir au moins un facteur supplémentaire exclu de l'équation pour $y$. 
Wooldridge (2019, Section 17.5) discute de la spécification et de l'estimation de ces modèles plus en détail.

Le modèle de sélection classique de Heckman peut être estimé 
- soit en deux étapes en utilisant un logiciel pour probit et MCO comme discuté par Wooldridge (2019), 
- soit par une commande spécialisée utilisant MLE. 
Dans $R$, le package _**sampleSelection**_ offre une estimation automatisée pour les deux approches.

### Wooldridge, Exemple 17.5 : Équation d'offre de salaire pour les femmes mariées
<font color="#c0504d">Nous regardons à nouveau l'échantillon de femmes dans le data set MROZ.dta. </font>
- Sur les 753 femmes, 428 ont travaillé (inlf=1) et le reste n'a pas travaillé (inlf=0). 
- Pour ces dernières, nous n'observons pas le salaire qu'elles auraient obtenu si elles avaient travaillé. 
Le Script 17.18 (Example-17-5.R) estime le modèle de sélection de Heckman en utilisant la commande `selection`. Elle attend deux formules : une pour la sélection et une pour l'équation de salaire. 
L'option `method="2step"` demande une estimation implicite en deux étapes pour rendre les résultats comparables à ceux rapportés par Wooldridge (2019). 
Avec l'option `method="ml"`, nous aurions obtenu le MLE plus efficace. 

Le résumé des résultats donne un tableau de régression typique pour les deux équations et des informations supplémentaires.

```
Script 17.18: Example-17-5.R

 library(sampleSelection)
 data(mroz, package='wooldridge')
 
 # Estimer le modèle de sélection de Heckman (version 2 étapes)
 res<-selection(inlf~educ+exper+I(exper^2)+nwifeinc+age+kidslt6+kidsge6,
                 log(wage)~educ+exper+I(exper^2), data=mroz, method="2step" )
                 
 # Résumé des résultats :
 summary(res)
```


