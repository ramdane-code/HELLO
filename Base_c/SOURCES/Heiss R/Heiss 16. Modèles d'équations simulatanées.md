# 16. Modèles d'Équations Simultanées

Dans les modèles d'équations simultanées (SEM), <font color="#00b0f0">à la fois la variable dépendante et au moins un régresseur sont déterminés conjointement (sont endogènes). </font> 
<font color="#c0504d">Cela conduit à un problème d'endogénéité (de régresseurs) et à des estimateurs de paramètres MCO non convergents.</font> 

<font color="#00b050">Le principal défi pour utiliser avec succès les SEM est de spécifier un modèle sensé et de s'assurer qu'il est identifié,</font> voir Wooldridge (2019, Sections 16.1--16.3). 
- La Section 16.1 introduit brièvement un<font color="#00b050"> modèle général et la notation</font> .
- La  Section 16.2 donne un exemple. Il montre que <font color="#00b050">la régression 2SLS peut résoudre les problèmes d'endogénéité </font>s'il y a suffisamment de variables instrumentales exogènes(voir Chapitre 15) . 
- La Section 16.3 présente<font color="#00b050"> la commande spécialisée</font>  `systemfit` dans $R$ pour estimer l'ensemble du système simultanément. 
- La Section 16.4 montre qu'en utilisant ce package, des commandes d'estimation plus avancées sont simples à implémenter. L'exemple présenté est<font color="#00b050"> l'estimation par triple moindres carrés (3SLS)</font>.

## 16.1. Configuration et Notation

Considérons le SEM général avec $q$ variables endogènes $y_1, \ldots, y_q$ <font color="#00b0f0">et</font> $k$ variables exogènes $x_1, \ldots, x_k$. Le système d'équations est :
 $$\begin{aligned}
y_1 &= \alpha_{12} y_2 + \alpha_{13} y_3 + \cdots + \alpha_{1q} y_q + \beta_{10} + \beta_{11} x_1 + \cdots + \beta_{1k} x_k + u_1 \\
y_2 &= \alpha_{21} y_1 + \alpha_{23} y_3 + \cdots + \alpha_{2q} y_q + \beta_{20} + \beta_{21} x_1 + \cdots + \beta_{2k} x_k + u_2 \\
&\vdots \\
y_q &= \alpha_{q1} y_1 + \alpha_{q2} y_2 + \cdots + \alpha_{q,q-1} y_{q-1} + \beta_{q0} + \beta_{q1} x_1 + \cdots + \beta_{qk} x_k + u_q
\end{aligned}$$
**Noter hr :** <font color="#00b0f0">les</font> $a_{ij}$ <font color="#00b0f0">sont des coefficients (paramètres) des régresseurs (variables) endogènes </font>$y_i$ et les $b_{ij}$ sont les coefficients des régresseurs exogènes.

<font color="#c0504d">This system is not identified without restrictions on the parameters</font>  (cf. Wooldridge (2019, Section 16).
<font color="#6425d0">The order condition for identification of any equation is that</font>
- <font color="#00b0f0">if we have</font> $m$ <font color="#00b0f0">included endogenous regressors (i.e.</font> $\alpha$<font color="#00b0f0"> parameters that are not restricted to 0)</font>, 
- <font color="#00b050">we need to exclude at least </font>$m$ <font color="#00b050">exogenous regressors (i.e. restrict their </font>$\beta$ <font color="#00b050">parameters to 0). </font>
- cela en vertu de la règle à vérifier par équation (K-k)⩾ m (donc K-k (nbre rég exogènes exclus) est au minimum égal à m)
- <font color="#00b050">This excluded exogenous regressors can then be used as instrumental variables.</font>
Attention le choix des règresseurs exclus n'est pas arbitraire, mais à des considérations de théorie économique.
### Wooldridge, Example 16.3: Labor Supply of Married, Working Women16.3

 <font color="#c0504d">We have the two endogenous variables hours and wage</font> which influence each other.
$$\begin{aligned}
\text{hours} &= \alpha_{12} \log(\text{wage}) + \beta_{10} + \beta_{11} \text{educ} + \beta_{12} \text{age} + \beta_{13} \text{kidslt6} + \beta_{14} \text{nwifeinc} + \beta_{15} \text{exper} + \beta_{16} \text{exper}^2 + u_1 \\
\log(\text{wage}) &= \alpha_{21} \text{hours} + \beta_{20} + \beta_{21} \text{educ} + \beta_{22} \text{age} + \beta_{23} \text{kidslt6} + \beta_{24} \text{nwifeinc} + \beta_{25} \text{exper} + \beta_{26} \text{exper}^2 + u_2
\end{aligned}$$

<font color="#00b0f0">Pour que les deux équations soient identifiées, nous devons exclure au moins un régresseur exogène de chaque équation.</font> 
- l'équation 1 a un régresseur endogène (wage), il faut exclure au moins 1 régresseur exogène (cf plus loin comment)
  ce que j'ai compris : c'est régresseurs exogènes exclus vont servir de IV pour
- l'équation 2 a un régresseur endogène (hours), idem

Wooldridge (2019) discute un modèle dans lequel <font color="#00b0f0">nous imposons</font>
- $\beta_{15} = \beta_{16} = 0$ dans la première équation (il s'agit de $\beta_{15} \text{exper} + \beta_{16} \text{exper}^2$)
- et $\beta_{22} = \beta_{23} = \beta_{24} = 0$ dans la deuxième équation (il s'agit de $\beta_{22} \text{age} + \beta_{23} \text{kidslt6} + \beta_{24} \text{nwifeinc}$ )

<font color="#00b0f0">Commentaire hr :</font>
- Les régresseurs exclus sont ceux de var exogènes (ne figurant pas dans la gauche du système, cad non des yi)
- <font color="#00b050">Les régresseurs exclus d'une équation ne le sont pas (pas nécessairement?) de l'autre équation.</font>
- <font color="#c0504d">Ces régresseurs exclus ne figurent plus dans la partie de régresseurs de l'équation</font>, 
	- <font color="#00b050">mais dans la partie des variables instrumentales</font> 
	- tous les autres régresseurs sont également repris dans cette partie VI
	- <font color="#00b0f0">les 2 parties étant séparées par |</font>
- Chaque équation est résolue "seule" sans ajouts d'éléments de l'autre équation.
- Le nombre d'exogènes exclues peut dépasser le nombre d'endogènes incluses.

## 16.2 Estimation par 2SLS

<font color="#c0504d">L'estimation de</font><font color="#00b0f0"> chaque équation séparément</font> <font color="#c0504d">par 2SLS</font> est simple <font color="#00b0f0">une fois que nous avons mis en place le système</font> et ==assuré l'identification==. 
<font color="#00b050">Les régresseurs exclus dans chaque équation servent de variables instrumentales.</font> 
Comme montré dans le Chapitre 15, <font color="#c0504d">la commande </font>`ivreg` <font color="#c0504d">du package</font> _**AER**_ <font color="#c0504d">fournit une estimation 2SLS pratique.</font>

### Wooldridge, Exemple 16.5 : Offre de Travail des Femmes Mariées Actives
<font color="#c0504d">Le Script 16.1 (Example-16-5-ivreg.R) estime les paramètres des deux équations de l'Exemple 16.3 séparément en utilisant </font>`ivreg`.

```
Script 16.1: Example-16-5-ivreg.R

 library(AER)
 data(mroz, package='wooldridge')

 oursample <- subset(mroz,!is.na(wage))
 
 # Régressions 2SLS
 summary(ivreg(hours~log(wage)+educ+age+kidslt6+nwifeinc
                |educ+age+kidslt6+nwifeinc+exper+I(exper^2), data=oursample))
 summary( ivreg(log(wage)~hours+educ+exper+I(exper^2)
                |educ+age+kidslt6+nwifeinc+exper+I(exper^2), data=oursample))
```


## 16.3. Estimation Conjointe du Système
<font color="#00b050">Nous pouvons utiliser la commande spécialisée </font>`systemfit` <font color="#00b050">du package</font> **systemfit**, au lieu de l'estimation manuelle de chaque équation par `ivreg`. 
Plus pratique à utiliser, elle offre une implémentation simple d'estimateurs supplémentaires. 

- Nous définissons le système d'équations comme une `list` de formules. Le Script 16.2 fait cela 
	- en stockant d'abord chaque équation comme une formule, 
	- puis en les combinant dans la liste eq.system. 
- Nous devons également définir l'ensemble des régresseurs exogènes et instruments 
	- en utilisant une formule avec seulement un côté droit. 
	- Le Script 16.2 stocke cette spécification dans la variable instrum.

Avec ces préparations, `systemfit` est simplement appelée avec le système d'équations et l'ensemble d'instruments comme arguments. 
L'option `method="2SLS"` demande une estimation 2SLS. 

Les résultats produits par le Script 16.3  sont les mêmes qu'avec les régressions `ivreg` séparées vues précédemment.

```
Script 16.2: Example-16-5-systemfit-prep.R

library(systemfit)
data(mroz, package='wooldridge')

oursample <- subset(mroz,!is.na(wage))

# Définir le système d'équations et les instruments
eq.hrs <- hours ~ log(wage)+educ+age+kidslt6+nwifeinc
eq.wage <- log(wage)~ hours +educ+exper+I(exper^2)
eq.system<- list(eq.hrs, eq.wage)
instrum <- ~educ+age+kidslt6+nwifeinc+exper+I(exper^2)

# 2SLS de l'ensemble du système (exécutez d'abord Example-16-5-systemfit-prep.R !)
 summary(systemfit(eq.system,inst=instrum,data=oursample,method="2SLS"))
```

## 16.4. Perspective : Estimation par 3SLS

<font color="#00b050">Les résultats de</font> `systemfit` <font color="#00b050">fournissent des informations supplémentaires</font>, voir le Script 16.3 (Example-16-5-systemfit.R). <font color="#00b0f0">Une information intéressante est la corrélation entre les résidus des équations</font>. 
- Dans l'exemple, elle est rapportée comme substantiellement négative à -0,90. 
- Nous pouvons tenir compte de la corrélation entre les termes d'erreur pour obtenir un estimateur de paramètres potentiellement plus efficace que 2SLS. 
Sans entrer dans les détails ici, <font color="#00b0f0">l'estimateur des triple moindres carrés (3SLS) ajoute une autre étape à 2SLS</font> <font color="#00b050">en estimant la corrélation et en en tenant compte en utilisant une approche FGLS.</font> 
Pour une discussion détaillée de cette méthode et d'autres méthodes connexes, voir par exemple Wooldridge (2010, Chapitre 8).

<font color="#c0504d">Utiliser 3SLS dans</font> $R$ <font color="#c0504d">est simple</font> : <font color="#00b050">l'option</font> `method="3SLS"` de `systemfit` <font color="#00b050">est tout ce que nous avons à faire</font> comme le montre la sortie du Script 16.4 (Example-16-5-3sls.R).

```
Script 16.4: Example-16-5-3sls.R

# 3SLS de l'ensemble du système (exécutez d'abord Example-16-5-systemfit-prep.R !)
 summary(systemfit(eq.system,inst=instrum,data=oursample,method="3SLS"))
```