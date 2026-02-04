# Chap.13. <font color="#c00000">Pooling Coupes Transversales dans le Tps et Panel data</font>
## 13.0 <font color="#00b050">Voir une coupe transversale </font> + définir Pooling et Panel data
### Visualisation d'un Tableau en coupes transversales

| Country | Year | Pib | Cons | Epargne | Export |
| ------- | ---- | --- | ---- | ------- | ------ |
| Alg     | 2020 |     |      |         |        |
| Alg     | 2021 |     |      |         |        |
| Tunis   | 2020 |     |      |         |        |
| Tunis   | 2021 |     |      |         |        |
| Maroc   | 2020 |     |      |         |        |
| Maroc   | 2021 |     |      |         |        |
|         |      |     |      |         |        |
<font color="#00b0f0">Pour obtenir ce tableau en coupe transversale</font>, <font color="#00b050">concaténer 3 Tableaux TS :</font>
- prendre 3 tableaux en série chronologique, avec la col. year devant,
- ajouter le nom du pays pour chacun des pays, 
- les coller les uns sous les autres pour former un grand tableau.

### <font color="#c0504d">Points communs (échantillons aléat à +ieurs périodes) et différences (Panel : tjours m échantillon)</font>
<font color="#00b0f0">Coupes transversales poolées : échantillons aléatoires tirés de la même population à différents moments.</font>
- La Section 13.1 <font color="#f79646">présente ce type de data set </font>et comment l'utiliser pour <font color="#00b050">estimer les changements dans le temps</font>.
- La Section 13.2 couvre les <font color="#f79646">estimateurs de différence des différences</font><font color="#00b050">pour identifier des effets causaux.</font> C'est une application importante des coupes transversales poolées

<font color="#00b0f0">Les données de panel ressemblent aux données de coupes transversales poolées en ce que nous avons des observations à différents moments. </font><font color="#c0504d">La différence clé est que nous observons les mêmes unités transversales, par exemple des individus ou des entreprises.</font>

### <font color="#c0504d">Organisation particulière des Panels datas : col=var, lignes=obs, index de col et index de ligne</font>
- Les méthodes de données de <font color="#00b0f0">panel</font> nécessitent une <font color="#00b0f0">organisation systématique des données</font>  (cf.Section 13.3).
- Cela permet des<font color="#de7802"> calculs spécifiques utilisés pour les analyses présentés dans la Section 13.4. </font>
- <font color="#00b0f0">La Section 13.5 introduit la première méthode de données de panel, l'estimation par premières différences.</font>

## 13.1 <font color="#00b050">Estimer coupes Transversale Poolées avec lm</font> (concaténer +ieurs coupes transv)

### <font color="#c0504d">Avantage : augmente taille, précision, analyse des variations</font>
Si nous avons des <font color="#00b0f0">échantillons aléatoires à différents moments</font>, 
- <font color="#00b050">cela augmente la taille globale de l'échantillon et donc la précision statistique</font> de nos analyses. 
- Cela permet également d'<font color="#6425d0">étudier les changements dans le temps </font>
- et de jeter un éclairage supplémentaire sur les relations entre les variables.
### <font color="#c0504d">Estimer 2 coupes transversales poolées (78 et 85) : données du pb et procédure</font>
Estimer la variation temporelle du  Rendement de l'Éducation et de l'Écart Salarial entre les Sexes
<font color="#00b0f0">Le data set CPS78_85.dta de Wooldridge inclut deux coupes transversales poolées pour les années 1978 et 1985.</font>  
<font color="#c0504d">La variable muette y85 est égale à 1 pour les observations de 1985 et à 0 pour 1978.</font> ^y85
(sachant qu'il existe une col."year" qui indique si une obs relève de 78 ou 85)

Nous estimons un modèle pour le logarithme du salaire lwage de la forme
$lwage = \beta_0 + \delta_0 y85 + \beta_1 educ + \delta_1 (y85 \cdot educ) + \beta_2 exper + \beta_3 exper^2 + \beta_4 union + \beta_5 female + \delta_5(y85 \cdot female) + u$
Notez que nous divisons $exper^2$ par 100 et donc multiplions $\beta_3$ par 100 par rapport aux résultats rapportés dans Wooldridge (2019).  

<font color="#00b0f0">Le paramètre</font> $\beta_1$ <font color="#00b0f0">mesure le rendement de l'éducation en 1978</font> <font color="#00b0f0">et</font> $\delta_1$ <font color="#00b050">mesure la différence du rendement de l'éducation en 1985 par rapport à 1978.  </font> : rendement 85 = $β_1+δ_1$
De même, $\beta_5$ est l'écart salarial entre les sexes en 1978 et $\delta_5$ est le changement de cet écart.  Donc l'écart en 85 est $β_5+δ_5$ .

<font color="#00b050">Conclusions  du Script 13.1 (Example-13-2.R) qui estime le modèle :</font>
- Le rendement de l'éducation est estimé avoir augmenté de $\hat{\delta}_1 = 0.018$ 
- et l'écart salarial entre les sexes a diminué en valeur absolue de $\hat{\beta}_5 (ici,\,female) = 0.317$ à $\hat{\beta}_5 + \hat{\delta}_5 (ici,\,y85:female) = 0.232$, même si ce changement n'est que marginalement significatif (y85:female évalué à ".") 
<font color="#7030a0">Cf. la Section 6.1.6. qui détaille l'interprétation et la mise en œuvre des interactions </font> 

### <font color="#c00000">Script 13.1 : Estimer pooling data : charger data, reg lm, termes d'interaction, summary</font>

```text
Script 13.1: Example-13-2.R
data(cps78_85, package='wooldridge')  # alternative:charger woold puis data(cps78_85)

# Résultats OLS détaillés incluant les termes d'interaction
summary( lm(lwage ~ y85*(educ+female) +exper+ I((exper^2)/100) + union,
						data=cps78_85) )
```
rem : y85*(educ+female) : y85*educ + y85*female 
### <font color="#c00000">Interprétation de l'output par DeepSeek</font>
                  Estimate Std. Error t value Pr(>|t|)    
(Intercept)               0.458933   0.093449   4.911 1.05e-06 ***
y85                          0.117806   0.123782   0.952   0.3415    
educ                        0.074721   0.006676  11.192  < 2e-16 ***
female                    -0.316709   0.036621  -8.648  < 2e-16 ***
exper                       0.029584   0.003567   8.293 3.27e-16 ***
I((exper^2)/100)    -0.039943   0.007754  -5.151 3.08e-07 ***
union                      0.202132   0.030294   6.672 4.03e-11 ***
y85:educ                 0.018461   0.009354   1.974   0.0487 *  
y85:female              0.085052   0.051309   1.658   0.0977 .

#### 1. Contexte du modèle
Modèle de régression sur échantillon combiné (*pooled*) de 2 années : 1978 et 1985, avec `y85 = 1` si l’observation vient de 1985, `y85 = 0` si elle vient de 1978.
La variable dépendante est `lwage` (log du salaire).
**Le modèle est de la forme :**$lwage = \beta_0 + \beta_1 y85 + \beta_2 educ + \beta_3 female + \beta_4 exper + \beta_5 \frac{exper^2}{100}$
                             $+ \beta_6 union + \beta_7 (y85 \times educ) + \beta_8 (y85 \times female) + u$ 
**Il inclut** :
- `educ` (années d’éducation)
- `female` (=1 si femme)
- `exper` (années d'expérience)
- `exper²/100` (pour éviter des coefficients trop petits)
- `union` (=1 si syndiqué)
- `Interactions` :` y85 *(educ+female)` qui signifie `y85:educ` et `y85:female`
#### 2. Interprétations sans les interactions

**Coefficients sans interaction**
- `educ` : 0.0747 → chaque année d’éducation supplémentaire **en 1978** (`y85=0`) augmente le salaire d’environ **7.47%** (puisque log-linéaire).
- `female` : -0.3167 → en 1978, être femme (vs homme) est associé à un salaire inférieur d’environ **31.67%** (approximé par `exp(-0.3167)-1 ≈ -27.1%`  si on veut une interprétation exacte en pourcentage, mais en approximation lin-log on dit parfois ~31.7% moins).^66e961
- `exper` : effet positif, mais décroissant à cause du terme carré négatif.

**Effets temporels captés par `y85`**
- `y85` seul = 0.1178 → en 1985, la constante (`intercept`) pour les hommes avec `educ=0`, `exper=0`, non syndiqués, est plus élevée de 0.1178 par rapport à 1978.
- Mais **attention** : `y85` interagit avec `educ` et `female`, donc l’effet global de 1985 dépend de ces variables.
#### 3. Interprétation des interactions

**Interaction `y85:educ` = 0.01846**
Cela signifie qu’en 1985, **le rendement de l’éducation** est plus élevé qu’en 1978 de 0.01846.
- Rendement de l’éducation en 1978 : 0.0747
- Rendement de l'éducation en 1985 : 0.0747 + 0.01846 = **0.09316**
→ Donc chaque année d’éducation supplémentaire augmente le salaire d’environ **9.32%** en 1985 contre 7.47% en 1978.
Le coefficient est significatif à 5% (`p=0.0487`).

**Interaction `y85:female` = 0.08505**
Ce coefficient mesure comment **l’écart salarial homme/femme** a changé entre 1978 et 1985.
- Écart femmes/hommes en 1978 : -0.3167
- Écart femmes/hommes en 1985 : -0.3167 + 0.08505 = **-0.23165**
Donc l’écart (négatif) s’est réduit : les femmes gagnaient 31.67% de moins en 1978, et seulement **23.17% de moins** en 1985 (toutes choses égales par ailleurs).
Le coefficient `y85:female` a une `p-value=0.0977`, donc significatif seulement à 10% — réduction statistiquement faiblement significative.
#### 4. Exemple numérique**
Pour une femme en 1985 avec 12 ans d’éducation, `exper=10`, syndiquée :
- Effet d’être 1985 = 0.1178 (changement de constante)
- Effet d’éducation en 1985 = 12 × (0.0747 + 0.01846)
- Effet d’être femme en 1985 = -0.3167 + 0.08505
On ne peut pas interpréter `y85` seul sans tenir compte des interactions avec `educ` et `female`.
#### 5. Interprétation de `(Intercept) = 0.458933`: crucial dans le cadre des intéractions
Le modèle est : $lwage = 0.4589 + 0.1178 \times y85 + 0.0747 \times educ + \dots + interactions$
**Quand `y85 = 0` (année 1978) :**
L’intercept = `0.4589` correspond au salaire (log) prédit pour un individu de **référence** en **1978** avec : `educ = 0`, `female = 0` (man), `exper = 0`, `union = 0` (non syndiqué),`exper²/100 = 0`.
En **niveau** (après exponentiation) :  $\exp(0.4589) \approx 1.582$
Cela signifie que pour un tel individu, le **niveau de salaire prédit** est environ **1.582** (dans l’unité du salaire avant log — par exemple, en dollars horaires).
**Quand `y85 = 1` (année 1985) :**
L’intercept pour man sans éduc, expérience nulle, non syndiqué devient :  $0.4589 + 0.1178 = 0.5767$
Mais attention, il y a aussi les interactions avec `educ` et `female`. Si on reste avec `educ=0`, l’interaction `y85:educ` est nulle. Donc pour cet individu précis (homme, éducation nulle, etc.), le salaire log prédit en 1985 est `0.5767`. Exponentié :  $\exp(0.5767) \approx 1.780$
Ainsi, entre 1978 et 1985, pour ce profil extrême (homme sans éducation ni expérience), le salaire prédit augmente de 1.582 à 1.780 (soit une hausse d’environ 12.5%).
**Remarque importante** :  
L’intercept dans un modèle avec interactions entre `y85` et `educ`/`female` n’a de sens concret **que pour `educ=0` et `female=0`**.  
Pour d’autres valeurs, il faut calculer l’ordonnée à l’origine correspondante en tenant compte de tous les termes.
**Donc pour résumer :**
- **Intercept seul = 0.4589** : log-salaire prédit en **1978** pour un homme sans éducation, sans expérience, non syndiqué.
- **Intercept + y85 = 0.5767** : log-salaire prédit en **1985** pour un homme sans éducation, sans expérience, non syndiqué.
- L’effet de 1985 (`y85=1`) sur l’intercept est **positif (+0.1178)**, mais non significatif seul (p=0.3415) — donc cette hausse pour ce profil particulier n’est pas statistiquement certaine au seuil habituel.

#### 5. Synthèse
1. **`y85` seul** n’est pas significatif (p=0.3415) → pas de changement général de salaire entre 1978 et 1985 **pour un homme sans éducation, expérience nulle, non syndiqué**.
2. **Éducation** → rendement accru en 1985.
3. **Écart hommes-femmes** → s’est réduit entre 1978 et 1985 (d’environ 8.5 points de log).
4. `union` → effet positif stable dans le temps (pas d’interaction avec `y85` dans ce modèle).
5. `exper` → effet concave stable dans le temps.

**Conclusion** : Quand tu as des interactions avec une variable binaire de période (`y85`), il faut toujours calculer l’effet total pour chaque année :
- Pour 1978 : `y85=0` → interactions nulles
- Pour 1985 : `y85=1` → ajouter les coefficients d’interaction aux coefficients de base correspondants.

## 13.2. <font color="#00b050">Estimateur Différence des Différences</font> évalue la corrélation avant et après une action

### <font color="#c00000"> Estimer l'effet d'une intervention politique avec DiD</font>**
Type important d'applications pour les coupes transversales poolées. 
<font color="#00b0f0">Les estimateurs de différence de différences (DiD)</font> <font color="#c0504d">estiment l'effet d'une intervention politique (au sens large) en comparant le changement dans le temps d'une variable d'intérêt entre un groupe affecté et un groupe non affecté d'observations.</font> (cf Wooldridge (2019, Section 13.2) )

Dans un cadre de régression, <font color="#c00000">nous régressons la variable d'intérêt sur</font> 
- une variable muette pour le groupe affecté ("traitement"), 
- une variable muette indiquant les observations après le traitement 
- et un terme d'interaction entre les deux. 
Le coefficient de ce terme d'interaction peut alors être un bon estimateur de l'effet d'intérêt, contrôlant pour les différences initiales entre les groupes et les changements contemporains dans le temps.

###<font color="#c00000"> Woo.ex  13.3 : installer un incinérateur de déchets affecte-t-il les prix des maisons proches</font>
Exemple estime l'Effet de l'Emplacement d'un Incinérateur de Déchets sur les Prix Immobiliers
Nous nous intéressons à <font color="#c0504d">savoir si et dans quelle mesure la construction d'un nouvel incinérateur de déchets a affecté la valeur des maisons à proximité. </font>
#### <font color="#00b050">Estimer avec lm la diff avant, la diff après et faire la diff des différences</font>
Le Script 13.2 (Example-13-3-1.R) utilise le <font color="#00b0f0">data set  KIELMC</font>.dta. 
<font color="#00b0f0">Nous estimons d'abord des modèles séparés </font>pour 1978 (avant toute rumeur sur le nouvel incinérateur) et 1981 (lorsque la construction a commencé). 
- En 1981, les maisons proches du site de construction étaient moins chères en moyenne de 30 688,27 $. 
- Mais cela n'était pas seulement dû au nouvel incinérateur puisque même en 1978, les maisons à proximité étaient moins chères en moyenne de 18 824,37 $. 
-<font color="#00b050"> La différence de ces différences</font> $\hat{\delta} = 30,688.27 - 18,824.37$ = $11,863.90$ <font color="#00b050">est l'estimateur DiD</font> et est sans doute un meilleur indicateur de l'effet réel.
#### <font color="#00b050">Estimer  DiD par rég lm conjointe avec terme d'intéraction (le coef donne l'écart avec la situation de départ)</font>
<font color="#00b0f0">L'estimateur DiD peut être obtenu plus commodément</font> <font color="#00b050">en utilisant un modèle de régression conjoint avec le terme d'interaction :</font> coeftest( lm(rprice~nearinc* y81, data=kielmc) ) où <font color="#00b050">le regresseur correspond à l'écart entre 78 et 81.</font>
L'estimateur $\hat{\delta}$ = $11,863.90$ peut être vu directement comme le coefficient du terme d'interaction. 

#### **<font color="#00b050"> L'output de la rég inclut le test t (H0 : l'effet réel=0)</font>**
**Pratiquement**, <font color="#de7802">les tableaux de régression standards incluent des tests t de l'hypothèse que l'effet réel est égal à zéro.</font> 
Pour un test unilatéral, la valeur $p$ est $\frac{1}{2} \cdot 0.112 = 0.056$,  (0,112 est la Pr(>|t|) cad la p-value? de nearinc:y81) : il y a donc une certaine évidence statistique d'un impact négatif.
### <font color="#c0504d">Script 13.2 : 2 façons de calculer DiD : rég lm séparées et rég lm conjointes avec terme d'intéraction</font>
```
Script 13.2: Example-13-3-1.R

 # Régressions séparées pour 1978 et 1981 : rapporte seulement les coefficients
 coef( lm(rprice~nearinc, data=kielmc, subset=(year==1978)) )

 coef( lm(rprice~nearinc, data=kielmc, subset=(year==1981)) )

 # Régression conjointe incluant un terme d'interaction
 library(lmtest)
 coeftest( lm(rprice~nearinc*y81, data=kielmc) )
```


### <font color="#c0504d">Améliorer l'estimateur DiD </font>par transformation log et ajout de régresseurs
  - <font color="#00b050">une spécification logarithmique est plus plausible</font> puisqu'elle implique un effet en _pourcentage_ constant sur la valeur des maisons.^transf log
 ^2e761f
 - Nous pouvons <font color="#00b050">ajouter des régresseurs supplémentaires pour contrôler les changements fortuits</font> dans la composition des maisons échangées. 
<font color="#00b050"> Le Script 13.3 (Example-13-3-2.R) implémente les deux améliorations :</font>
 - Le modèle incluant des caractéristiques des maisons implique une diminution estimée de la valeur des maisons d'environ 13,2 %. 
 - Cet effet est également significativement différent de zéro.
 
### <font color="#c0504d">Script 13.3 : DiD avec lm sur log et plus de régresseurs. Stargazer affiche en m tps l'output de 2 rég</font>

^74e7c9

```
text

Script 13.3: Example-13-3-2.R
DiD <- lm(log(rprice)~nearinc*y81 , data=kielmc)
DiDcontr <- lm(log(rprice)~nearinc*y81+age+I(age^2)+log(intst)+
                           log(land)+log(area)+rooms+baths, data=kielmc)
library(stargazer)
stargazer(DiD,DiDcontr,type="text")
```

<font color="#c0504d"> <u>NB</u> : noter cette présentation comparée de deux régressions avec stargazer avec la fonction stargazer(Did,DiDcontr. type="text)</font>

## 13.3 <font color="#00b050">Structure des Données de Panel et création d'un pdata.fram avec plm</font>
### <font color="#c0504d">La présence d'Effets spécifiques non observés constants dans le tps distingue les données de Panel</font>
<font color="#00b0f0">Un  panel data set inclut plusieurs observations à différents moments t pour le même (ou au moins un ensemble qui se recoupe) d'unités transversales</font> $i$. 
Un modèle de régression (de données de panel) "poolé" simple  pourrait ressembler à  :
$y_{it} = \beta_0 + \beta_1 x_{it1} + \beta_2 x_{it2} + \cdots + \beta_k x_{itk} + v_{it}; \quad t = 1, \ldots, T; \quad i = 1, \ldots, n, \tag{13.1}$    (13.1)
où le double indice indique maintenant les valeurs pour l'individu (ou autre unité transversale) $i$ au temps $t$. 

<font color="#6425d0">Nous pourrions estimer ce modèle par MCO, en ignorant essentiellement la structure de panel.</font> <font color="#c0504d">Mais au moins l'hypothèse que les termes d'erreur sont indépendants est très difficile à justifier </font>puisqu'ils contiennent des <font color="#00b0f0">traits individuels non observés susceptibles d'être constants ou au moins corrélés dans le temps</font>. 
<font color="#00b050">Par conséquent, nous avons besoin de méthodes spécifiques pour les données de panel.</font>
### <font color="#c0504d">Organiser les Données de Panels : Col=variable, Ligne=obs. + Index de col et Index de ligne.</font>
<font color="#c00000">Pour effectuer les calculs par les méthodes de données de panel,</font> <font color="#00b0f0">nous devons nous assurer que le data set est organisé systématiquement</font> <font color="#00b050">et que les routines d'estimation comprennent sa structure. </font>
- Habituellement, <font color="#00b0f0">un data set de panel est sous une forme "longue"</font> où <font color="#00b050">chaque ligne de données correspond à une combinaison de</font> $i$ et $t$. 
- Nous devons <font color="#c00000">définir quelles observations vont ensemble en introduisant</font> 
	- une <font color="#c00000">variable d'index pour les unités transversales </font>$i$ 
	- et <font color="#c00000">de préférence aussi l'index de temps</font> $t$.
### **<font color="#c0504d">Créer un pdata.frame à partir d'un DF avec le package plm, dédié aux données de Panel</font>**
^fcf4b6
<font color="#00b050">Le package</font> _**plm**_ (<font color="#00b0f0">pour panel linear model</font>) <font color="#00b050">est une collection complète de commandes traitant des données de panel.</font> 
- <font color="#0070c0">il offre un data type  nommé </font>`pdata.frame`, à l'instar des data types spécifiques pour les séries chronologiques. 
- `pdata.frame`  est un  `data.frame` doté d'attributs supplémentaires décrivant les dim individuelles et temporelles. 

Supposons que nous ayons <font color="#7030a0">nos données dans un data frame standard nommé mydf. </font>
- Il inclut une <font color="#f79646">variable ivar indiquant les unités transversales </font>
- et une <font color="#9bbb59">variable tvar indiquant le temps</font>. 
<font color="#00b0f0"><u>Nous pouvons alors créer un data frame de panel avec la commande </u> :</font>

	`mypdf <- pdata.frame( mydf, index=c("ivar","tvar") )`

<font color="#00b0f0">Si nous avons un panel équilibré </font>(même nombre d'observations $T$ pour chaque "individu" $i = 1, \ldots, n$) <font color="#00b0f0">et que les observations sont d'abord triées par i puis par t,</font> nous pouvons alternativement appeler  
`mypdf <- pdata.frame( mydf, index=n )`
<font color="#c0504d">Dans ce cas, les nouvelles variables id et time sont générées comme variables d'index.</font>

Une fois notre data set défini, nous <font color="#00b0f0">pouvons vérifier les dimensions avec</font> `pdim(mypdf)`. Il indiquera 
- si le panel est équilibré, 
- le nombre d'unités transversales $n$, 
- le nombre d'unités de temps $T$ 
- et le nombre total d'observations $N$ (qui est $n T$ dans les panels équilibrés).
### <font color="#c0504d"> Script 13.4 : import data set, déf un pdata.frame, utilise pdim(), affiche les obs 1 à 6 de col. choisies</font>
<font color="#c0504d">Appliquons cela au data set CRIME2.dta discuté par Wooldridge (2019, Section 13.3). </font> C'est un panel équilibré de 46 villes, correctement trié. 
- Le Script 13.4 (PDataFrame.R) importe le data set. 
- <font color="#00b0f0">Nous définissons notre nouveau data frame de panel crime2.p </font><font color="#c0504d">et vérifions ses dimensions. </font>
- $R$ rapporte un panel équilibré avec deux observations sur 46 villes chacune. 
- <font color="#7030a0">Nous affichons également les six premières lignes</font> de données pour les nouvelles variables d'index id et time et d'autres variables sélectionnées. 
Maintenant, nous sommes prêts à travailler avec ce data set.

```
text
Script 13.4: PDataFrame.R
 library(plm)
 
 data(crime2, package='wooldridge')
 # Définir le data frame de panel
 crime2.p <- pdata.frame(crime2, index=46 )
 # Dimensions du panel :
 pdim(crime2.p)
# Afficher les obs1-6 pour "id" et "time" et quelques autres variables :
 crime2.p[1:6,c("id","time","year","pop","crimes","crmrte","unem")]^obsETcol
```

## 13.4 <font color="#00b050">Calculs Spécifiques au Panel </font>(peuvent se faire aussi par routines automatiques)
### <font color="#c0504d"> Nbre d'obs, lag, diff, Moy temporelle individuelle (betwin), var centrée ou demeaned (within)</font>
Une fois que nous avons défini notre data set de panel, nous pouvons effectuer des calculs utiles spécifiques aux données de panel. Ils seront utilisés par les estimateurs discutés ci-dessous.
- <font color="#00b0f0">les routines pré-établies  effectuent automatiquement ces calculs</font> pour une grande partie des régressions de données de panel appliquées,
- mais ils est instructif de les réaliser manuellement et cela nous donne plus de flexibilité à les implémenter nous-mêmes.

<font color="#00b0f0">Considérons un data set de panel avec les unités transversales (individus,...)</font> : $i = 1, \ldots, n$. 
Il y a $T_i$ observations pour l'individu $i$. Comme il y a n individus, le nombre total d'observations est $N = \sum_{i=1}^{n} T_i$. Dans le cas particulier d'un panel équilibré, tous les individus ont le même $T_i = T$ et $N = n T$.

<font color="#00b0f0">Le Tableau 13.1 liste les fonctions spéciales les plus importantes.</font> 
- <font color="#c0504d">Nous pouvons calculer les retards et les premières différences</font> en utilisant respectivement `lag` et `diff`. Contrairement aux données de séries temporelles pures, les retards et différences sont calculés pour chaque individu séparément, donc les premières observations pour chaque $i = 1, \ldots, n$ sont `NA`. <font color="#7030a0">Les retards d'ordre supérieur peuvent être spécifiés comme deuxième argument.</font>
- <font color="#00b050">Les moyennes individuelles</font> $\bar{x}_i = \frac{1}{T_i} \sum_{t=1}^{T_i} x_{it}$ sont calculées en utilisant la fonction `between` qui renvoie une valeur pour chaque _individu_ dans un vecteur de longueur $n$. Souvent, nous avons besoin de cette valeur pour chacune des N observations. La commande `Between` renvoie ce vecteur de longueur $N$ où chaque $\bar{x}_i$ est répété $T_i$ fois. 
- <font color="#00b0f0">La transformation within calculée avec</font> `Within` <font color="#00b0f0">soustrait la moyenne individuelle</font> $\bar{x}_i$ <font color="#00b0f0">de l'observation </font>$x_{it}$. <font color="#7030a0">Ces variables "décentrées"</font> jouent un rôle important dans le Chapitre 14.

**Tableau 13.1.** Calculs spécifiques au panel ^8b2fb9

| Commande       | Transformation         | Description                                   |
| -------------- | ---------------------- | --------------------------------------------- |
| `l=lag(x)`     | Retard                 | $l_{it} = x_{i,t-1}$                          |
| `d=diff(x)`    | Différence             | $d_{it} = x_{it} - x_{i,t-1}$                 |
| `b=between(x)` | Between (longueur $n$) | $b_i = \frac{1}{T_i} \sum_{t=1}^{T_i} x_{it}$ |
| `B=Between(x)` | Between (longueur $N$) | $B_{it} = b_i$                                |
| `w=Within(x)`  | Within (décentrement)  | $w_{it} = x_{it} - B_{it}$                    |
### <font color="#c0504d">Script 13.5 : data.set Crime4 et col crmrte (taux de crimes) : Nbre obs, lags, diff, between, within </font>
- Le data set CRIME4.dta contient des données sur 90 comtés pendant sept ans.  
- Il inclut les variables d'index county et year qui sont utilisées dans la définition de notre `pdata.frame`. 
- Nous calculons les retards, différences, transformations between et within du <font color="#c0504d">taux de criminalité</font> (<font color="#00b050">crmrte</font>). 
- Les résultats sont stockés dans le data frame de panel. 
- Les premières lignes de données sont ensuite présentées à titre d'illustration.

<font color="#c0504d">La variable retardée</font> (lagged variable) <font color="#00b050">vcr.l</font> est juste égale à crmrte mais décalée d'une ligne vers le bas. 
<font color="#c0504d">La différence entre ces deux variables</font> est <font color="#00b050">cr.d</font>. 
<font color="#c0504d">La moyenne crmrte au sein des sept premières lignes</font> (c'est-à-dire pour le comté 1) est donnée comme les sept premières valeurs de <font color="#00b050">cr.B</font> 
et <font color="#00b050">cr.W</font> est <font color="#c0504d">la différence entre crmrte et cr.B.</font>

Manipuler avec plm une col. d'un DF Panel data (différents calculs : lag(), diff(), Between(), Within())
```text
Script 13.5: Example-PLM-Calcs.R

 library(plm)
 data(crime4, package='wooldridge')
 # Générer pdata.frame :
 crime4.p <- pdata.frame(crime4, index=c("county","year") )
 # Calculs dans le pdata.frame :
 crime4.p$cr.l <- lag(crime4.p$crmrte)
 crime4.p$cr.d <- diff(crime4.p$crmrte)
 crime4.p$cr.B <- Between(crime4.p$crmrte)
 crime4.p$cr.W <- Within(crime4.p$crmrte)
 # Afficher les variables sélectionnées pour les observations 1-16 :
 crime4.p[1:16,c("county","year","crmrte","cr.l","cr.d","cr.B","cr.W")]
```

## 13.5 <font color="#00b050">Estimateur des Premières Différences</font> pour Panel
### <font color="#c0504d">L'effet spécifique inobservé constant dans le tps viole l'hyp d'indép de l'erreur par rapport aux régresseurs</font>
Wooldridge (2019, Sections 13.3 -- 13.5) discute des <font color="#c00000">modèles à effets inobservés de base</font> et de<font color="#c00000"> leur estimation par premières différences (FD).</font> <font color="#00b0f0">Considérons le modèle </font>   $$y_{it} = \beta_0 + \beta_1 x_{it1} + \cdots + \beta_k x_{itk} + a_i + u_{it}; \quad t = 1, \ldots, T; \quad i = 1, \ldots, n, \tag{13.2}$$
qui <font color="#00b0f0">diffère de l'Équation </font>[13.1]<font color="#00b0f0"> en ce qu'il implique explicitement un effet inobservé</font> $a_i$ <font color="#00b0f0">qui est constant dans le temps (puisqu'il n'a pas d'indice </font>$t$). 
- <font color="#c0504d">Si </font>$a_i$ <font color="#c0504d">est corrélé avec un ou plusieurs des régresseurs</font> $x_{it1}, \ldots, x_{itk}$, <font color="#c0504d">nous ne pouvons pas  ignorer </font>$a_i$, <font color="#c0504d">le laisser dans le terme d'erreur composite</font> $v_{it} = a_i + u_{it}$ <font color="#c0504d">et estimer l'équation par MCO</font>. 
- <font color="#4bacc6"> Le terme d'erreur</font> $v_{it}$ <font color="#4bacc6">serait lié aux régresseurs</font>, violant l'hypothèse MLR.4 (et MLR.4') et créant des biais et des inconséquences. 
<font color="#8064a2">Ce problème n'est pas propre aux données de panel, et des solutions sont possibles</font>.
### <font color="#c0504d">Les (FD) neutralisent l'effet spécifique; l'équation différenciée est estimé par MCO</font>
<font color="#00b0f0">L'estimateur des premières différences (FD) est basé sur la première différence de toute l'équation</font> :  
$$\Delta y_{it} \equiv y_{it} - y_{i,t-1} = \beta_1 \Delta x_{it1} + \cdots + \beta_k \Delta x_{itk} + \Delta u_{it}; \quad t = 2, \ldots, T; \quad i = 1, \ldots, n. \tag{13.3}$$
Notez que nous ne pouvons pas évaluer cette équation pour la première observation $t = 1$ pour tout $i$ puisque les valeurs retardées leur sont inconnues. 
<font color="#00b050">L'astuce est que</font> $a_i$ <font color="#00b050">disparaît de l'équation par différenciation puisqu'il ne change pas dans le temps</font>. Peu importe à quel point il est corrélé avec les régresseurs, il ne peut plus nuire à l'estimation. 
<font color="#00b050">L'équation issue de la différenciation est ensuite estimée par MCO</font>. Nous régressons simplement la variable dépendante différenciée $\Delta y_{it}$ sur les variables indépendantes différenciées $\Delta x_{it1}, \ldots, \Delta x_{itk}$.
<font color="#00b050">L'estimation mesure le lien entre la variation de la var dépendante et celle des régresseurs.</font>
### <font color="#c0504d">Partir d'un pdata.frame, utiliser diff() sur la var dépendante et les régresseurs, appliquer MCO</font>
<font color="#c0504d">Le Script 13.6 (Example-FD.R) ouvre le data set CRIME2.dta déjà utilisé ci-dessus.</font> 
- Au sein d'un `pdata.frame`, nous utilisons la fonction `diff` pour calculer les premières différences de la variable dépendante taux de criminalité (crmrte) et de la variable indépendante taux de chômage (unem) dans notre data set.
- Une liste des six premières observations révèle que les différences ne sont pas disponibles (`NA`) pour la première année de chaque ville. Les autres différences sont également calculées comme prévu :
- Par exemple, la variation du taux de criminalité pour la ville 1 est $70.11729 - 74.65756 = -4.540268$ et le changement du taux de chômage pour la ville 2 est $5.4 - 8.1 = -2.7$.
<font color="#c0504d">L'estimateur FD peut maintenant être calculé en appliquant  MCO à ces valeurs différenciées.</font> 
- <font color="#7030a0">Les observations pour la première année avec des informations manquantes sont automatiquement supprimées</font> de l'échantillon d'estimation. 
- <font color="#00b050">Les résultats montrent une relation significativement positive entre la variation du chômage et celle de la criminalité.</font>
### <font color="#c0504d">Script 13.6 : estimer avec plm sur données originelles et arg : model="fd"plutôt qu'avec lm sur datas différenciées.</font>
```text
Script 13.6: Example-FD.R

 library(plm); library(lmtest)
 data(crime2, package='wooldridge')
 
 crime2.p <- pdata.frame(crime2, index=46 )
 
 # calculer manuellement les premières différences :
 crime2.p$dyear <- diff(crime2.p$year) # il semble que différencier year est inutile.
 crime2.p$dcrmrte <- diff(crime2.p$crmrte)
 crime2.p$dunem <- diff(crime2.p$unem)
 
 # Afficher les variables sélectionnées pour les observations 1-6 :
 crime2.p[1:6,c("id","time","year","dyear","crmrte","dcrmrte","unem","dunem")]

 # Estimer le modèle FD avec lm sur les données différenciées :
 coeftest( lm(dcrmrte~dunem, data=crime2.p) )
 
 # Estimer le modèle FD avec plm sur les données originales:rég avec plm, avec arg : model="fd"
coeftest(plm(crmrte~unem, data=crime2.p, model="fd") )  # "fd" pour first difference, je suppose.
```

### <font color="#c0504d">plm avec option model="pooling" et plm avec option model="fd"</font>
Générer les valeurs différenciées et utiliser `lm` sur elles est en fait inutile. 
<font color="#00b0f0">Le package</font> _**plm**_ <font color="#00b0f0">fournit la commande polyvalente</font> `plm` <font color="#00b0f0">qui implémente FD et d'autres estimateurs, dont certains que nous utiliserons au chapitre 14</font>. 
- plm fonctionne comme `lm` mais est appliquée directement aux variables originales et effectue les calculs nécessaires en interne. 
- Avec l'option `model="pooling"`, l'estimateur MCO poolé est demandé, 
- l'option `model="fd"` produit l'estimateur FD. 
Comme le montre la sortie du Script 13.6 (Example-FD.R), les estimations des paramètres sont exactement les mêmes que nos calculs pédestres.
### <font color="#c0504d">Woo.ex  13.9 : Estimer modèle pooling avec plm, option model="pooling" (à revoir, pas clair)</font>
Taux de Criminalité des Comtés en Caroline du Nord
<font color="#c0504d">Le Script 13.7 (Example-13-9.R) analyse les données CRIME4.dta</font> déjà utilisées dans le Script 13.5 (Example-PLM-Calcs.R). 
- Juste pour illustration, nous calculons la <font color="#c0504d">1ère différence de crmrte</font> et affichons les 9 premières lignes de données. La première différence est `NA` pour la première année de chaque comté. 
- Ensuite, <font color="#c0504d">nous estimons le modèle en premières différences</font> en utilisant `plm`.

Notez que <font color="#00b0f0">dans cette spécification, toutes les variables sont automatiquement différenciées</font>, <font color="#00b050">elles ont donc l'interprétation intuitive dans l'équation de niveau</font>. 

Dans les résultats rapportés par Wooldridge (2019), les variables muettes d'année ne sont pas différenciées, ce qui affecte seulement l'interprétation des coefficients d'année. Pour reproduire exactement les mêmes résultats que Wooldridge (2019), nous pourrions utiliser un estimateur MCO poolé et différencier explicitement les autres variables :

```text
plm(diff(log(crmrte)) ~ d83+d84+d85+d86+d87+diff(lprbarr)+diff(lprbconv)+
                          diff(lprbpris)+diff(lavgsen)+diff(lpolpc), 
                          data=pdata, model="pooling")
```
message d'erreur : "pdata" introuvable

Nous répéterons cet exemple avec des erreurs-types "robustes" dans la Section 14.4.
### <font color="#c0504d">Script 13.7 : estimer le modèle précédent avec plm et option = "fd"</font>
```text
Script 13.7: Example-13-9.R

 library(plm);library(lmtest)
 data(crime4, package='wooldridge')
 crime4.p <- pdata.frame(crime4, index=c("county","year") )
 pdim(crime4.p)  # dimensions du panel
  # [] Balanced Panel: n = 90, T = 7, N = 630
  
 # calculer manuellement les premières différences du taux de criminalité :
 crime4.p$dcrmrte <- diff(crime4.p$crmrte)
 
 # Afficher les variables sélectionnées pour les observations 1-9 :
 crime4.p [1:9, c("county","year","crmrte","dcrmrte")]

'# Estimer le modèle FD : 
coeftest( plm(log(crmrte)~d83+d84+d85+d86+d87+lprbarr+lprbconv+ lprbpris+lavgsen+lpolpc,data=crime4.p, model="fd") )
```
<font color="#c0504d">rem hr : les rég d83, d84...: influence non prise en compte par les autres variables du passage de 82 à 83.</font>

# Chap.14. <font color="#c00000">Méthodes Avancées de Données de Panel</font>
## 14.0 <font color="#00b050">Contenu du chap </font>: estimateurs FE et RE, CRE(correlated random effects), erreurs standards robuste 
Dans ce chapitre, nous examinons des modèles et méthodes de données de panel supplémentaires. 
- Nous commençons par<font color="#00b0f0"> l'estimateur à effets fixes (FE)</font> largement utilisé dans la Section 14.1, 
- suivi par<font color="#00b0f0"> l'estimateur des effets aléatoires (RE)</font> dans la Section 14.2. 
- La <font color="#00b0f0">régression avec variables muettes (dummy variable regression</font> et <font color="#00b0f0">l'approche des effets aléatoires corrélés (correlated random effects)</font> présentées dans la Section 14.3 peuvent être utilisées comme alternatives et généralisations de FE. 
- Enfin, nous couvrons des <font color="#00b0f0">formules robustes pour la matrice de variance-covariance</font> et <font color="#00b0f0">les erreurs-types "agrégées"impliquées (robust formulas for the variance-covariance matrix and the implied “clustered” standard errors)</font> dans la Section 14.4. 
Nous reviendrons sur les données de panel en combinaison avec les variables instrumentales dans la Section 15.6.

## 14.1<font color="#00b050"> Estimation à Effets Fixes </font>: utilise la transformation within pour neutraliser a_i
### <font color="#c0504d">Générer des valeurs centrées (demeaned) par la commande within puis utiliser pooled OLS</font>
Nous partons des mêmes modèles à effets inobservés de base que l'Équation [13.2]. <font color="#00b050">Au lieu de différencier, nous nous débarrassons de l'effet individuel inobservé a_i en utilisant la transformation within :</font>
 $$\begin{aligned}
y_{it} &= \beta_0 + \beta_1 x_{it1} + \cdots + \beta_k x_{itk} + a_i + u_{it}; \quad t = 1, \ldots, T; \quad i = 1, \ldots, n, \\
\bar{y}_i &= \beta_0 + \beta_1 \bar{x}_{i1} + \cdots + \beta_k \bar{x}_{ik} + a_i + \bar{u}_i \\
\ddot{y}_{it} &= y_{it} - \bar{y}_i = \beta_1 \ddot{x}_{it1} + \cdots + \beta_k \ddot{x}_{itk} + \ddot{u}_{it},
\end{aligned} \tag{14.1}$$
where $\bar{y}_i$ is the average of $y_{it}$ over time for cross-sectional unit $i$ and for the other variables accordingly. 
The within transformation subtracts these individual averages from the respective observations $y_{it}$. 
We already know how to conveniently calculate these <font color="#4f81bd">demeaned variables</font> like $\ddot{y}_{it}$ using the command `Within` from Section [13.4.](#panel-specific-computations) : appliquer within() aux régresseurs et à la var dépendante.
<font color="#00b0f0">The fixed effects (FE) estimator simply estimates the demeaned Equation [14.1] </font><font color="#00b050"> using pooled OLS.</font>
### <font color="#c0504d">Mieux vaut estimer FE avec plm sur original data et option : model="within"</font>
 <font color="#c00000">We can simply use</font> `plm` <font color="#c00000">on the original data with the option </font>`model="within"`, <font color="#632423">instead of applying the within transformation to all variables and running `lm`</font>.  
 This has the additional <font color="#00b050">advantage</font> that 
 - the degrees of freedom are adjusted to the demeaning 
 - and the variance-covariance matrix and standard errors are adjusted accordingly. 
 We will come back to different ways to get the same estimates in Section [14.3.](#dummy-variable-regression-and-correlated-random-effects)

### <font color="#c0504d">Woo. ex 14.2: Modéle FE avec plm : effet des années d'éducation (fixes) sur le revenu à travers le temps</font>
Has the Return to Education Changed over Time? note14.2
<font color="#c0504d">We estimate the change of the return to education over time using a fixed effects estimator. </font> : variation du rendement des années(fixes) d'éducation sur plusieurs années
<font color="#00b0f0">Script 14.1 (Example-14-2.R) shows the implementation.</font> 
- <font color="#00b050">The data set WAGEPAN.dta</font> is a balanced panel for $n = 545$ individuals over $T = 8$ years. 
- It includes the <font color="#00b050">index variables</font> <font color="#c0504d">nr</font> and <font color="#c0504d">year</font> for individuals and years, respectively. 
- <font color="#c0504d">Since educ does not change over time,</font> <font color="#8064a2">we cannot estimate its overall impact.</font> <font color="#00b0f0">However, we can interact it with time dummies to see how the impact changes over time.</font>

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
<font color="#00b0f0">Remarque </font>: intéraction factor(year)*educ :
factor(year): year est traitée comme facteur (et non variable continue) avec 7 catégories (80-87) avec 80 comme catég de réf.
L'intéraction avec éduc génère l'effet de chq année seule, de éduc pour l'année (éduc seul n'est pas affiché car ne variant pas)

### <font color="#c0504d">Plus d'explication sur factor dans le modéle à Effets fixes individuels.</font>
#### <font color="#00b050">Notion de "factor" en R</font>
En R, **`factor`** est une classe de données utilisée pour représenter des **variables catégorielles** (qualitatives).
- Un facteur possède des **niveaux** (levels) qui correspondent aux différentes catégories.
- R traite les variables texte (character) comme facteurs dans les modèles statistiques, mais il est souvent nécessaire de les convertir explicitement en `factor` pour contrôler l'ordre des niveaux ou inclure toutes les catégories attendues.
<font color="#00b0f0">Dans un modèle de régression, les facteurs sont automatiquement transformés en </font>**variables binaires (dummy variables)**. <font color="#00b050">Si un facteur a k niveaux, il génère généralement k-1 variables indicatrices (la première catégorie sert de référence).</font>
#### <font color="#00b050">Signification dans l'estimation donnée</font>
Dans la commande :  `plm(lwage ~ married + union + factor(year) * educ, ...)`
1. **`factor(year)`** :
    - <font color="#00b0f0">La variable </font>`year`<font color="#00b0f0"> est traitée comme</font> **catégorielle** <font color="#00b0f0">(et non continue)</font>.
    - Les données étant un panel (périodes 1980-1987), elle capture des **effets temporels non linéaires** propres à chaque année.
2. **Interaction `factor(year) * educ`** :
    - L'opérateur `*` signifie que l'on inclut à la fois les effets  de `factor(year)` et de `educ`, ainsi que leur **interaction**.
    - Cela revient à estimer un **coefficient distinct d'`educ` pour chaque année** 
    - Formellement, le modèle devient :
        $lwage_{it}=α_i+β_1married_{it}+β_2union_{it}+γ_t+δ_t⋅educ_{it}+ϵ_{it}$
        où $γ_t$ est l'effet fixe temporel (année) et $δ_t$​ l'interaction année-éducation.
3. **Dans les résultats** :
    - On voit les coefficients pour `married` et `union` (effets moyens).
    - Les termes `factor(year)1981` à `factor(year)1987` sont les **effets fixes temporels** (relatifs à l'année de référence 1980, omise).
    - Les termes d'interaction `factor(year)1981:educ` à `factor(year)1987:educ` mesurent **comment le rendement de l'éducation (coefficient d'`educ`) varie chaque année par rapport à 1980**.
    - L'année de base (1980) est incluse dans l'effet principal d'`educ` (qui n'apparaît pas car il est absorbé par l'interaction et les effets fixes individuels dans ce modèle "within").
#### <font color="#00b050">Pourquoi utiliser `factor(year)` ici ? : sans factor, year serait traité comme var continue</font>
- Sans `factor()`, `year` serait traité comme variable continue, imposant un effet linéaire du temps sur `lwage`.
- Avec `factor(year)`, on autorise une forme libre de l'effet temporel (chaque année a son propre effet).
- L'interaction avec `educ` permet de tester si le rendement de l'éducation **évolue dans le temps** (par exemple, <font color="#00b0f0">si l'effet d'une année supplémentaire d'études sur le salaire change d'une année à l'autre</font>).
#### <font color="#00b050">Note sur le modèle  : "within" dans plm c'est Effets fixes individuels (les caract spécifiques invariant dans le tps sont éliminés)</font>
- <font color="#00b0f0">Le modèle est estimé avec</font> `model="within"` dans `plm()`, ce qui signifie **effets fixes individuels** (l<font color="#00b0f0">es caractéristiques invariantes dans le temps des individus sont éliminées</font>).  
- <font color="#00b050">C’est pourquoi on ne voit pas de constante ni d'effet principal d'</font>`educ`<font color="#00b050"> seul</font> (<font color="#00b050">car</font> `educ` <font color="#00b050">est constant dans le temps pour chaque individu, donc absorbé par les effets fixes individuels</font>). <font color="#00b0f0">Les interactions restent identifiables car elles varient dans le temps.</font>
En résumé, **`factor(year)`** permet une modélisation flexible des effets temporels et de leurs interactions avec l'éducation, capturant ainsi des changements annuels dans la structure des salaires.

## 14.2 <font color="#00b050">Modéles à effets aléatoires </font>ou Random Effects Models (RE models)
### <font color="#c0504d">RE suppose que a_i n'est pas corrélé aux régresseurs : plus besoin de FD ou FE pour éliminer a_i</font> 
We again base our analysis on the basic unobserved effects model in Equation [13.2]. 
<font color="#00b0f0">The random effects (RE) model assumes that the unobserved effects</font> $a_i$ <font color="#00b0f0">are independent of (or at least uncorrelated with) the regressors </font>$x_{itj}$ <font color="#00b0f0">for all </font>$t$ <font color="#00b0f0">and</font> $j = 1, \ldots, k$. 
<font color="#c00000">Therefore, our main motivation for using FD (first difference) or FE (fixed effects) disappears</font>: <font color="#00b050">Sous cette hyp supplémentaires, MCO estiment de manière cohérente les paramètres du modèle.</font>
### <font color="#c0504d">La transfo GLS conduit à spécification quasi demeaned ( ne soustrait des var qu'une fraction $\theta$ de la moyenne)</font>
However, like the situation with heteroscedasticity (see Section 8.3) and autocorrelation (see Section 12.2),<font color="#00b0f0"> we can obtain more efficient estimates if we take into account the structure of the variances and covariances of the error term.</font> Wooldridge (2019, Section 14.2) shows that <font color="#c0504d">the GLS transformation that takes care of their special structure implied by the RE model leads to a <u>quasi-demeaned specification</u></font>
 $$y_{it}^\circ = y_{it} - \theta \bar{y}_i = \beta_0 (1 - \theta) + \beta_1 x_{it1}^\circ + \cdots + \beta_k x_{itk}^\circ + v_{it}^\circ, \tag{14.2}$$
<font color="#00b0f0">where</font> $y_{it}^\circ$ <font color="#00b0f0">is similar to the demeaned</font> $\ddot{y}_{it}$ <font color="#00b0f0">from Equation</font> [14.1]<font color="#00b050"> but subtracts only a fraction</font> $\theta$ <font color="#00b050">of the individual averages</font>. <font color="#c00000">The same holds for the regressors </font>$x_{itj}$ <font color="#c00000">and the composite error term</font> $v_{it} = a_i + u_{it}$.

<font color="#7030a0">The parameter</font> $\theta = 1 - \sqrt{\frac{\sigma_u^2}{\sigma_u^2 + T \sigma_a^2}}$ <font color="#7030a0">depends on the variances of </font>$u_{it}$ <font color="#7030a0">and</font> $a_i$ <font color="#7030a0">and the length of the time series dimension </font>$T$. 
<font color="#c0504d">It is unknown and has to be estimated</font>. 
### <font color="#c0504d">Estimation du modèle RE (comprenant les Effets fixes) par plm avec l'option model="random"</font>
<font color="#00b050">We can estimate the RE model parameters using the command</font> `plm` <font color="#00b050">with the option</font> `model="random"`. 
<font color="#7030a0">Different versions of estimating the random effects parameter</font> $\theta$ <font color="#7030a0">are implemented and can be chosen with the option</font> `random.method`, see Croissant and Millo (2008) for details.
### <font color="#c0504d">pvar affiche la liste des variables constantes dans le temps et celles qui ne le sont pas</font>
<font color="#00b0f0"> Unlike with FD and FE estimators, we can include variables in our model that are constant over time for each cross-sectional unit</font>. <font color="#00b050"><u>The command</u></font> `pvar` <font color="#00b050"><u>provides a list of these variables as well as of those that do not vary within each point in time.</u></font>

###  <font color="#c0504d">Woo. ex 14.4: Estimer Panel Data avec plm pour resp. OLS. RE et FE estimateurs (récapitulation)</font>
#### <font color="#00b050">Etapes : charger les Datas, vérifier le pdata.frame, pvar, plm avec les 3 options, stargazer pour afficher</font>
A Wage Equation Using Panel Data ( Exemple rég pooling, random, within)
<font color="#c0504d">The data set WAGEPAN.dta was already used in Example 14.2.</font> 
- Script 14.2 (Example-14-4-1.R) loads the data set and defines the panel structure. 
- Then, <font color="#00b050">we check the panel dimensions and get a list of time-constant variables using</font> `pvar`. 
With these preparations, we get estimates using OLS, RE, and FE estimators in Script 14.3 (Example-14-4-2.R). 
- We use `plm` with the options `pooling`, `random`, and `within`, respectively. 
- <font color="#00b050">We  use </font>`stargazer` <font color="#00b050">to display the results (de plusieurs rég en même temps)</font>, with additional options for labeling the estimates (`column.labels`), and selecting variables (`keep`) and statistics (`keep.stat`).
#### <font color="#00b050">Script 14.2 implémente les étapes pour estimer wage selon les 3 modèles (comparés grâce à stargazer)</font>
```
Script 14.2: Example-14-4-1.R

 library(plm);library(stargazer)
 data(wagepan, package='wooldridge')
 
 # Generate pdata.frame:
 wagepan.p <- pdata.frame(wagepan, index=c("nr","year") )
 pdim(wagepan.p)   

 # Check variation of variables within individuals
 pvar(wagepan.p)  # var constantes dans le tps et celles const par entité (la m quque soit l' entité)

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

### <font color="#c0504d">plm propose Test de Hausman comparant FE et RE (plus efficace, mais avec hyp plus exigeante)</font>
<font color="#00b0f0"> The RE estimator needs stronger assumptions to be consistent than the FE estimator. </font>
 On the other hand, 
 - <font color="#c0504d">it is more efficient if these assumptions hold</font> 
 - <font color="#00b050">and we can include time constant regressors</font>. 
 
 <font color="#c0504d">A widely used test of this additional assumption is the Hausman test</font>. 
 - It is based on the comparison between the FE and RE parameter estimates. 
 - <font color="#00b0f0">Package</font> ***plm***<font color="#00b0f0"> offers the simple command</font> `phtest` <font color="#00b0f0">for automated testing.</font> 
 - It expects both estimates and reports test results including the appropriate $p$ values.
### <font color="#c0504d">Script 14.4 implémente test de Hausman (H0 : RE is consistent est rejetée)</font>
 <font color="#c0504d">Script 14.4 (Example-HausmTest.R) to run the Hausman test for this model </font>
 - using the estimates obtained in Script 14.3 (Example-14-4-2.R) 
 - and stored in variables reg.re and reg.fe  
 Conclusion : with the $p$ value of 0.0033, the null hypothesis that the RE model is consistent is clearly rejected with sensible significance levels like $\alpha = 5\%$ or $\alpha = 1\%$.

```
Script 14.4: Example-HausmTest.R

# Note that the estimates "reg.fe" and "reg.re" are calculated in Example 14.4.
# The scripts have to be run first.

# Hausman test of RE vs. FE:
 phtest(reg.fe, reg.re)
```

**Output :**
data:  lwage ~ I(exper^2) + married + union + yr
chisq = 26.361, df = 10, p-value = 0.003284
alternative hypothesis: one model is inconsistent

### Commentaire sur résultat du test de Hausman (rejet de H0 et donc de RE car pvalue <0,05.

Ce résultat du test de Hausman indique que **vous devez rejeter l'hypothèse nulle** (p-value = 0.0033 < 0.05).
1. **Hypothèse nulle (H₀) :** <font color="#00b0f0">Les estimateurs des modèles à effets aléatoires (RE) et à effets fixes (FE) sont tous deux cohérents</font>. Autrement dit, <font color="#c0504d">les effets individuels non observés ne sont pas corrélés avec les variables explicatives</font> →<font color="#00b050"> le modèle RE est préférable (plus efficace).</font>
2. **Hypothèse alternative (H₁) :** <font color="#00b0f0">Seul le modèle à effets fixes est cohérent </font>→<font color="#c0504d"> le modèle RE est biaisé (inconsistant) à cause d'une corrélation entre les effets individuels et les régresseurs.</font>
**Conclusion :**
- Puisque p-value = 0.0033 (< 0.05), on rejette H₀, 
- donc il existe une corrélation entre les effets individuels non observés et les variables explicatives.
- **le modèle à effets fixes (FE) est approprié**, et le modèle à effets aléatoires (RE) donnerait des estimateurs biaisés.
- <font color="#00b0f0">Conclusion pratique</font> : il faut utiliser les résultats de la régression à effets fixes (`reg.fe`), car elle contrôle pour les caractéristiques individuelles non observées corrélées avec les variables explicatives.

## 14.3 <font color="#00b050">Dummy Variable Regression and Correlated Random Effects</font>
### <font color="#c0504d">3 façons d'estimer les paramètres de FE : within, dummy et CRE (correlated random effects)</font>
<font color="#00b0f0">We can get the FE parameter estimates in two other ways than the within transformation we used in Section </font>[14.1.](#fixed-effects-estimation) 

 #### <font color="#00b050">La rég avec dummy variable utilise OLS sans transfo des var, mais ajoute n-1 dummies </font>
 - <font color="#c0504d">uses OLS on the original variables in Equation</font> [13.2]
 - <font color="#c0504d">instead of the transformed ones</font>.
 - <font color="#00b0f0">But it adds</font> $n - 1$ <font color="#00b0f0">dummy variables (or n dummies and removes the constant), one for each cross-sectional unit</font> $i = 1, \ldots, n$. 
 <font color="#c0504d">The simplest (although not the computationally most efficient) way to implement this in</font> $R$ <font color="#c0504d">is to use the cross-sectional index as another</font> `factor` <font color="#c0504d">variable</font>.

 #### <font color="#00b050">Dans la correlated random effects (CRE) approach, a_i est corrélé à la moy temp des régresseurs </font>
 - <font color="#c00000">Instead of assuming that the individual effects </font>$a_i$ <font color="#c00000">are independent of the regressors</font> $x_{itj}$, (ce que fait RE)
 - <font color="#00b0f0">we assume that they only depend on the averages over time</font> $\bar{x}_{ij} = \frac{1}{T} \sum_{t=1}^{T} x_{itj}$ :
 -<font color="#00b050"> plus simplement </font>(hr) : <font color="#00b050">les</font> $a_i$ <font color="#00b050">sont corrélés non pas aux</font> $x_{ij}$ <font color="#00b050">mais à  aux moyennes temporelles</font> $\bar x_{ij}$
 $α_i = γ_0 + γ_1 \bar x_{i1}+.... + γ_k \bar x_{ik}+r_i$   # $a_i$ fonction linéaire des $\bar x_{ij}$
$y_{it} = \beta_0 + \beta_1 x_{it1} + \cdots + \beta_k x_{itk} + a_i + u_{it} \tag{14.4a}$ (14.3)
$y_{it} = \beta_0 + \gamma_0 + \beta_1 x_{it1} + \cdots + \beta_k x_{itk} + \gamma_1 \bar{x}_{i1} + \cdots + \gamma_k \bar{x}_{ik} + r_i + u_{it} \tag{14.4b}$ (14.4)

 <font color="#00b0f0">If</font> $r_i$ <font color="#00b0f0">is uncorrelated with the regressors,</font> 
 - <font color="#00b050">we can consistently estimate the parameters of this model using the RE estimator. </font>
 - <font color="#c0504d">In addition to the original regressors, we include their averages over time.</font> 
 - Remember from Section [13.4](#panel-specific-computations) that these averages are computed with the function `Between`.

### <font color="#c0504d">Estimations within, dummy, cre d'un modèle FE + une RE :</font>
**NB** : <font color="#00b0f0">Script 14.5 (Example-Dummy-CRE-1.R) uses WAGEPAN.dta again. </font><font color="#00b050">We estimate the FE parameters using</font> 
- <font color="#00b050">the within transformation</font> (reg.fe), 
- <font color="#00b050">the dummy variable approach</font> (reg.dum), 
- <font color="#00b050">and the CRE approach</font> (reg.cre). 
- <font color="#00b0f0">We also estimate the RE version of this model</font> (reg.re). 

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
```
rappel : Between, avec B majuscule, moyenne temporelle.
### <font color="#c0504d">Stargazer pour afficher en parallèle les paramètres des 4 estimations du script 14.5</font>
<font color="#c0504d">Script 14.6 (Example-Dummy-CRE-2.R) produces the regression table using </font>`stargazer`. The results confirm that 
- <font color="#00b050">the first three methods deliver exactly the same parameter estimates,</font> 
- <font color="#6425d0">while the RE estimates differ</font>.

```
Script 14.6: Example-Dummy-CRE-2.R (suite )

stargazer(reg.fe,reg.dum,reg.cre,reg.re,type="text",model.names=FALSE,
          keep=c("married","union",":educ"),keep.stat=c("n","rsq"),
          column.labels=c("Within","Dummies","CRE","RE"))

```

### **<font color="#c0504d">Tester si RE model est plus cohérent que CRE model (H0 : RE consistent)</font>**
 <font color="#7030a0">Given we have estimated the CRE model,</font> <font color="#00b050">it is easy to test the null hypothesis that the RE estimator is consistent.</font> 
 - The additional assumptions needed are $\gamma_1 = \cdots = \gamma_k = 0$. 
 - They can easily be tested using an $F$ test as demonstrated in Script 14.7 (Example-CRE-test-RE.R). 
<font color="#c0504d"> Conclusion :</font> Like Hausman test, we clearly reject the null hypothesis that the RE model is appropriate with a tiny  $p$ value of about 0.00005.

```
Script 14.7: Example-CRE-test-RE.R
# Note that the estimates "reg.cre" are calculated in Script "Example-Dummy-CRE-1.R" 
# which has to be run first.

# RE test as an F test on the "Between" coefficients
library(car)

 linearHypothesis(reg.cre, matchCoefs(reg.cre,"Between"))
```

### <font color="#c0504d">CRE approach can add time-constant regressors to the model.</font>** 
<font color="#7030a0">Since we cannot control for average values</font> $\bar{x}_{ij}$ <font color="#7030a0">for these variables</font>, <font color="#c0504d">they have to be uncorrelated with </font>$a_i$ <font color="#c0504d">for consistent estimation of *their* coefficients.</font> <font color="#00b0f0">For the other coefficients of the time-varying variables, we still don't need these additional RE assumptions.</font>

 <font color="#c0504d">Script 14.8 (Example-CRE2.R) estimates another version of the wage equation using the CRE approach</font>. 
 - The variables married and union vary over time, so we can control for their between effects. 
 - The variables educ, black, and hisp do not vary. For a causal interpretation of *their* coefficients, we have to rely on uncorrelatedness with $a_i$. Given $a_i$ includes intelligence and other labor market success factors, this uncorrelatedness is more plausible for some variables (like gender or race) than for other variables (like education).

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

## 14.4 <font color="#00b050">Robust (Clustered) Standard Errors</font>

### <font color="#c0504d">Utiliser OLS, au lieu de RE, à condition d'ajuster l'erreur type par Clustered Standard Errors</font>

<font color="#00b0f0">We argued above that under the RE assumptions, OLS is inefficient but consistent (cohérente)</font>. 

<font color="#7030a0">Instead of using RE,</font> 
- <font color="#00b0f0">we could simply use OLS</font>
- <font color="#00b050"> but would have to adjust the standard errors</font> 
- for the fact that the composite error term $v_{it} = a_i + u_{it}$ is correlated over time (autocorrélation ?)
- <font color="#00b050">because of the constant individual effect</font> $a_i$. 

In fact, the variance-covariance matrix could be more complex than the RE assumption with i.i.d. $u_{it}$ implies. 
- These error terms could be serially correlated and/or heteroscedastic. 
- This would invalidate the standard errors not only of OLS but also of FD, FE, RE, and CRE.
### <font color="#c0504d">Formule pour la matrice VC de Panel data robuste à l'hétéroscéd et autocorrélations arbitraires du terme d'erreur</font>
 <font color="#00b0f0">There is an elegant solution, especially in panels with a large cross-sectional dimension</font>. 
 <font color="#c0504d">Similar to standard errors that are robust with respect to heteroscedasticity in cross-sectional data (Section 8.1)</font> <font color="#7030a0">and serial correlation in time series (Section 12.3),</font> <font color="#00b050">there are formulas for the variance-covariance matrix for panel data that are robust with respect to heteroscedasticity and</font> *arbitrary* <font color="#00b050">correlations of the error term within a cross-sectional unit (or "cluster").</font>
 <font color="#7030a0">These "clustered" standard errors are mentioned in Wooldridge (2019,</font> Section 14.4 and Example 13.9). 
### <font color="#c0504d">La commande vcovHC de plm pour obtenir un terme d'erreur robuste à l'hétéroscédasticité </font>
  -  `vcovHC` from the package ***plm***, see Croissant and Millo (2008) for details. (ne pas confondre avec `vcovHC` du package ***sandwich*** qui a même nom mais ne donne que des résultats robustes à l'hétéroscédasticité.) 
  - It works for all estimates obtained by `plm` 
  - and can be used as an input for regression tables using `coeftest` or `stargazer` or testing commands like `linearHypothesis`.

### <font color="#c0504d"> Script 14.9 (Example-13-9-ClSE.R) implémente la formule pour clustered standard errors</font>
#### <font color="#00b050">Le Script 14.9 génère Table de paramètres avec clustered SE (en plus de SE normal)</font>
- It repeats the FD regression from Example 13.9 
- <font color="#00b0f0">but also reports the regression table with clustered standard errors</font> 
- and respective t statistics 
- in addition to the usual standard errors. 

<font color="#c0504d">There are different versions of formulas for clustered standard errors. </font> This is similar to the heteroscedasticity-robust standard errors discussed in Section 8.1, 
- We first use the default type 
- and then a type called `"sss"` (for "Stata small sample") that makes a particular small sample adjustment applied by Stata by default. 

These are the exact numbers reported by Wooldridge (2019).
#### <font color="#00b050">Script 14.9 : Rég table avec SE(standard errors) et avec "Clustered" SE </font>

```
Script 14.9: Example-13-9-ClSE.R
 library(plm);library(lmtest)
 
 data(crime4, package='wooldridge')
 
 # Generate pdata.frame
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

