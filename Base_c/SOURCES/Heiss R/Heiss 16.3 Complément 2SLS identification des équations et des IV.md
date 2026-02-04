### Wooldridge, Example 16.3: Labor Supply of Married, Working Women16.3

 <font color="#c0504d">We have the two endogenous variables hours and wage</font> which influence each other.
$hours= \alpha_{12} \log(/text{wage}) + \beta_{10} + \beta_{11} \text{educ} + \beta_{12} \text{age} + \beta_{13}\text{kidslt6} + \beta_{14} \text{nwifeinc} + \beta_{15} \text{exper} + \beta_{16} \text{exper}^2 + u_1$
$log(wage)= \alpha_{21} \text{hours} + \beta_{20} + \beta_{21} \text{educ} + \beta_{22} \text{age} + \beta_{23} \text{kidslt6} + \beta_{24} \text{nwifeinc} + \beta_{25} \text{exper} + \beta_{26} \text{exper}^2 + u_2$

<font color="#00b0f0">Pour que les deux équations soient identifiées, nous devons exclure au moins un régresseur exogène de chaque équation.</font> 
- l'équation 1 a un régresseur endogène (wage), il doit être instrumenté par au moins un régresseur exogène, qui ne soit pas présent ( exclu) dans l'équation). il va être ajouté aux IV de l'équation (après | ). 
- l'équation 2 a un régresseur endogène (hours), idem

Wooldridge (2019) discute un modèle dans lequel <font color="#00b0f0">l'analyse économique met en évidence</font>
- $\beta_{15} = \beta_{16} = 0$ dans la première équation (il s'agit de $/beta_{15} /text{exper} + /beta_{16} /text{exper}^2$) peuvent servir de vi
- et $\beta_{22} = \beta_{23} = \beta_{24} = 0$ dans la deuxième équation (il s'agit de $/beta_{22} /text{age} + /beta_{23} /text{kidslt6} + /beta_{24} /text{nwifeinc}$ ) peuvent servir de vi.

<font color="#00b0f0">Commentaire hr :</font>
- Les régresseurs exclus sont ceux de var exogènes (ne figurant pas dans la gauche du système, cad non des yi)
- <font color="#00b050">Les régresseurs exclus d'une équation ne le sont pas (pas nécessairement?) de l'autre équation.</font>
- <font color="#c0504d">Ces régresseurs exclus ne figurent plus dans la partie de régresseurs de l'équation</font>, 
	- <font color="#00b050">mais dans la partie des variables instrumentales</font> 
	- tous les autres régresseurs sont également repris dans cette partie VI
	- <font color="#00b0f0">les 2 parties étant séparées par |</font>
- Chaque équation est résolue "seule" sans ajouts d'éléments de l'autre équation.
- Le nombre d'exogènes exclues peut dépasser le nombre d'endogènes incluses.
### Supplément sur des Questions cruciales que je me pose à propos de l'identification : 
<font color="#00b0f0">Comment est répartie l'exclusion des régresseurs exclus entre les équations ?</font> <font color="#c0504d">Peut-on exclure les mêmes régresseurs des 2 équations ? Réponse de DeepSeek :</font>

Ces questions  touchent à une subtilité cruciale de l'identification dans les systèmes d'équations simultanées (2SLS ou plus généralement par la méthode des variables instrumentales).
#### 1. Règle d'identification (Condition d'ordre)
La règle de base : au moins autant d'instruments exclus qu'il y a de variables endogènes dans l'équation, c'est la condition d'ordre nécessaire (<font color="#c0504d">mais pas suffisante</font>).

La vérification, effectuée équation par équation, est purement mécanique :
<font color="#c0504d"><u>Pour une équation donnée du système :</u></font>
  Soit <font color="#00b0f0">M</font> = nombre total de variables <font color="#00b0f0">endogènes dans le système entier</font>.
  Soit <font color="#00b0f0">m</font> = nombre de variables <font color="#00b0f0">endogènes incluses dans l'équation à estimer.</font>
  Soit <font color="#de7802">K</font> = nombre total de variables <font color="#de7802">exogènes (constante incluse) dans le système entier</font>.
  Soit<font color="#de7802"> k</font> = nombre de variables <font color="#de7802">exogènes incluses dans cette même équation.</font>
<font color="#c00000"><u>La condition d'ordre nécessaire pour l'identification de cette équation est</u> </font>:
<font color="#00b0f0">Nombre d'instruments (cad de var exogènes) exclus ≥ Nombre de régresseurs endogènes</font>
<font color="#00b050">Nbre d'exogènes du syst entier exclues de l'équation (ne faisant pas partie de l'équation) ⩾Nbre d'endogènes de l'équation</font>.
<font color="#c00000">Ce qui se traduit par </font>: (K - k) ⩾ m
- `(K - k)` est le nombre de variables exogènes du système qui ne font pas partie ('exclues') de l'équation considérée, 
- et `m` est le nombre de variables endogènes incluses (figurant dans l'équation).
<font color="#00b0f0">L'important est que cette condition s'applique équation par équation.</font> 
- Il faut vérifier cette condition pour chaque équation du système à estimer.
<font color="#c00000">rem hr : le mot "exclues" prête à confusion</font> : <font color="#00b0f0">il s'agit d'exogènes du système qui ne font pas partie de l'équation, </font><font color="#ff0000">donc un fait à vérifier</font> <font color="#7030a0">plutôt qu'un choix à effectuer</font>.
#### 2. Comment "répartir" les exogènes exclues ? (La logique économique pour trouver les instruments)
<font color="#00b0f0">La "répartition" n'est pas un choix arbitraire. Elle découle de la théorie économique que vous modélisez.</font> 
- <font color="#00b050"><u>Chaque équation représente un comportement</u> (offre, demande, réaction, etc.) </font>
- <font color="#c00000">et seules les variables pertinentes pour ce comportement doivent y figurer (mais toutes les pertinentes doivent être maintenues).</font>
- 
**Exemple classique** : Marché d'un bien (Offre et Demande)
   <font color="#00b0f0">Système</font> : <font color="#c0504d">commencer par écrire le système d'équations</font>
    1.  Équation de Demande :        $Q_d = \alpha_0 + \alpha_1 P + \alpha_2 Revenu + u_1$
    2.  Équation d'Offre :                  $Q_s = \beta_0 + \beta_1 P + \beta_2 Coût\_Production + u_2$
    3.  Condition d'équilibre :           $Q_d = Q_s = Q$
  
   <font color="#00b0f0">Variables</font> : <font color="#c0504d">trouver le nbre d'endogènes et exogènes du système,</font> <font color="#00b050">mais aussi en faire la liste, cela servira par la suite</font>
       Endogènes du système : Q  (quantité) et  P  (prix), soit M = 2 
       Exogènes du système  : Constante, Revenu, Coût_Production,  soit K=3
   <font color="#ff0000">Rem hr </font>: <font color="#c00000">la qualification d'endogène ou exogène n'est pas donnée a priori (par la règle : les endogènes sont à gauche, les exogènes à droite),</font> <font color="#00b050">mais par l'objectif visé : expliquer le prix et la quantité d'équilibre, par le revenu, le Coût de pn et l'intercept</font>
   
  <font color="#00b0f0">Vérification pour chaque équation</font> :
  <font color="#00b0f0">Équation de Demande</font> :
- Variables endogènes incluses (m) : P  (et  Q ) → `m = 1` (<font color="#c0504d">le fait que</font> `Q`<font color="#c0504d"> soit à gauche n'en fait pas un régresseur endogène inclus de la même façon. Ici, l'endogène explicative est </font>`P`). hr : <font color="#00b0f0">quand on raisonne au niveau de l'équation </font> <font color="#c0504d">une endogène située à gauche n'est pas considérée comme telle</font>. <font color="#00b0f0">Alors qu'au niveau du système</font> <font color="#00b050">elle est comptée comme endogène.</font>
- Variables exogènes incluses (k) : <font color="#7030a0">Constante</font>, Revenu → `k = 2`.
- Variables exogènes excluses (K - k) : `3 - 2 = 1` : <u>trouver laquelle</u>, ici <font color="#c00000">Coût_Production est la var exclue</font>. 
- Condition : `(K-k) = 1 ≥ m = 1` → Identifiée (<font color="#00b050">juste identifiée</font>). 
<font color="#ff0000">L'instrument naturel pour</font> `P`(le regresseur endogène) <font color="#ff0000">dans l'équation de demande est Coût_Production</font> (<font color="#00b050">qui affecte P via l'offre, mais est exclu de l'équation de demande</font>).
Ainsi, le choix des instruments n'est pas arbitraire, mais suppose un raisonnement : ici, la var "Coûts de pn" ne fait pas partie de l'équation de demande (en est exclue), donc n'affecte pas directement la demande,  mais affectent le prix donc peut en être l'instrument.

  <font color="#00b0f0">Équation d'Offre :</font>
	 Variables endogènes incluses (m) : \( P /) → `m = 1`.
	 Variables exogènes incluses (k) : Constante, Coût_Production → `k = 2`.
	 Variables exogènes excluses (K - k) : `3 - 2 = 1` (<font color="#c00000">Revenu est exclu</font>).
	 Condition : `(K-k) = 1 ≥ m = 1` → Identifiée (juste identifiée). 
	<font color="#c00000"> L'instrument naturel pour</font> `P` <font color="#c00000">dans l'équation d'offre est Revenu des consommateurs</font>

<font color="#00b050">Conclusion sur la répartition</font> : Elle est dictée par la logique du modèle. 
- L'offre dépend des coûts, pas du revenu des consommateurs. 
- La demande dépend du revenu des consommateurs, pas des coûts de production. 
<font color="#00b050">Ce sont ces exclusions théoriques (découlant des hypothèses du modèle éco sous jacent) qui créent les instruments nécessaires.</font>
#### 3. Peut-on exclure les mêmes régresseurs de différentes équations ?
<font color="#00b0f0">Oui, absolument</font>, <font color="#00b050">mais attention aux conséquences pour l'identification, et surtout pas de toutes</font>
Reprenons l'exemple précédent et modifions l'équation de demande pour en voir les conséquence :
1.  Demande : $Q = \alpha_0 + \alpha_1 P + \alpha_2 Revenu + u_1$
2.  Offre :        $Q = \beta_0 + \beta_1 P + \beta_2 Coût\_Production + u_2$
<font color="#c0504d">Supposons que le Revenu n'affecte ni l'offre ni la demande </font>(cas improbable). <font color="#00b050">On l'exclurait alors des deux équations.</font> 
<font color="#00b0f0">Il ferait partie des variables exogènes du système mais n'apparaîtrait dans aucune équation structurelle.</font>
<font color="#00b0f0">Variables exogènes du système</font> (K=3) : Constante, Revenu, Coût_Production.
<font color="#00b0f0">Équation de Demande </font>:
   `m = 1` (P), `k = 1` (constante uniquement). `K - k = 2` (Revenu et Coût_Production sont exclus). 
   Condition : `2 ≥ 1` → Vérifiée (sur-identifiée).
<font color="#00b0f0">Équation d'Offre</font> :
  `m = 1` (P), `k = 2` (constante + Coût_Production). `K - k = 1` (Revenu est exclu). 
  Condition : `1 ≥ 1` → Vérifiée (juste identifiée).
  
<font color="#c0504d">Le problème</font> : 
- <font color="#7030a0">Si une variable exogène est exclue de toutes les équations structurelles</font>, <font color="#00b0f0">elle devient un instrument candidat pour toutes les variables endogènes dans toutes les équations. </font>
- Dans l'exemple, Revenu pourrait théoriquement instrumenter `P` dans l'équation d'offre. <font color="#c00000">Cela peut mener à une sur-identification, ce qui est testable (test de Sargan/Hansen).</font>
<font color="#ff0000">Le vrai danger</font> :<font color="#00b050"> le sous-identification.</font> <font color="#c00000">Si une variable cruciale pour l'identification (comme Coût_Production) était exclue des deux équations,</font> <font color="#00b050">on perdrait un instrument. </font>
Par exemple, si on avait :
   Exogènes du système : Constante, Revenu, Coût_Production.
   Demande : `Q = α0 + α1 P + α2 Revenu` (exclut Coût_Production)
   Offre :        `Q = β0 + β1 P + β2 Revenu` (exclut Coût_Production)
  → Aucune équation n'aurait d'instrument exclu valide (`(K-k) = 1 < m = 1` pour les deux) : 
  <font color="#ff0000">Le système ne serait pas identifiable.</font>
#### En résumé :
1.  Vérifiez la condition d'ordre (`K-k ≥ m`) pour chaque équation séparément.
2.  La "répartition" des variables exclues vient de la théorie économique qui justifie qu'une variable affecte une équation mais pas l'autre.
3.  Une même variable exogène peut être exclue de plusieurs équations. Elle servira alors d'instrument potentiel pour ces équations. Cela peut être une force (plus d'instruments) si la condition de validité (exogénéité) est respectée, mais ne doit pas conduire à une situation où aucune équation n'a suffisamment d'instruments exclus.
4.  La condition nécessaire et suffisante est la condition de rang, plus difficile à vérifier, qui garantit que les instruments exclus sont corrélés avec les variables endogènes. La condition d'ordre ne garantit que la possibilité théorique de l'identification.
Votre réflexion montre que vous avez dépassé la recette simple pour comprendre la logique d'identification, ce qui est essentiel en économétrie structurelle.

<font color="#ff0000">J'ai ensuite soumis à DeepSeek le traitement que j'ai effectué à Woo.ex 16.3 pour identifier les équations, et pour trouver les VI,</font>

Vous avez bien compris la **condition d'ordre**, mais il y a une confusion importante dans l'application.

## Correction de votre analyse
1. **Décompte correct des variables**
	<u>Pour le système</u> :
- Variables endogènes du système** : `hours` et `log(wage)` (M = 2)
- Variables exogènes du système** (K = 8) : `constante, educ, age, kidslt6, nwifeinc, exper, exper²`
 1. **Vérification équation par équation**
	<u>Équation 1 (hours)</u> :
- Variables **endogènes incluses** (m₁) : `log(wage)` → m₁ = 1
- Variables **exogènes incluses** (k₁) : `constante, educ, age, kidslt6, nwifeinc, exper, exper²` → k₁ = 7
- Variables exogènes **excluses** (K - k₁) = 8 - 7 = 1
  Condition : (K - k₁) = 1 ≥ m₁ = 1 → **juste identifiée**
	<u>Équation 2 (log(wage))</u> :
- Variables **endogènes incluses** (m₂) : `hours` → m₂ = 1
- Variables **exogènes incluses** (k₂) : `constante, educ, age, kidslt6, nwifeinc, exper, exper²` → k₂ = 7
- Variables exogènes **excluses** (K - k₂) = 8 - 7 = 1
  Condition : (K - k₂) = 1 ≥ m₂ = 1 → **juste identifiée**

## Votre raisonnement sur les exclusions n'est pas correct
- Vous dites "je choisis d'exclure..." comme si c'était un choix arbitraire. 
- Les variables que vous excluez d'une équation doivent être **exclues théoriquement** de cette équation par les hypothèses du  modèle économique que vous utilisez.
Vous ne pouvez pas décider arbitrairement d'exclure `age, kidslt6, nwifeinc` de l'équation 2 si votre théorie économique dit qu'ils affectent les salaires. Si ces variables déterminent le salaire dans votre modèle, vous **devez** les inclure dans l'équation 2 !

Pour que votre système soit identifiable, vous devez avoir **des exclusions fondées théoriquement** :
- Si vous croyez que `exper` et `exper²` affectent le salaire mais **pas directement** les heures travaillées (en dehors de leur effet via le salaire), alors vous les **excluez de l'équation 1**.
- Si vous croyez que `kidslt6` et `nwifeinc` affectent l'offre de travail (hours) mais **pas directement** le salaire (en dehors de leur effet via hours), alors vous les **excluez de l'équation 2**.

Votre système deviendrait alors :
```
text
Équation 1 (hours) = α₁₂ log(wage) + β₁₀ + β₁₁ educ + β₁₂ age + u₁
Équation 2 (log(wage)) = α₂₁ hours + β₂₀ + β₂₁ educ + β₂₂ age + β₂₅ exper + β₂₆ exper² + u₂
Avec exclusions :
- Éq1 exclut : `kidslt6, nwifeinc, exper, exper²` (K-k₁ = 4 ≥ m₁ = 1)
- Éq2 exclut : `kidslt6, nwifeinc` (K-k₂ = 2 ≥ m₂ = 1)
```
hr : le système d'équation est ainsi amputé de certaines de ses variables jugées non directement pertinentes pour leur équation, mais qui reviendront sous forme d'IV.

### "<font color="#ff0000">Comment décider quelles variables exclure de quelle équation ?</font>"
La réponse : **C'est une question de théorie économique, pas de statistique.**
1. **L'équation des salaires (wage)** : Quels déterminants théoriques du salaire ? `educ`, `exper`, `age` sont classiques. `kidslt6` ? Peut-être pas (sauf discrimination). `nwifeinc` ? Pas directement.
2. **L'équation des heures (hours)** : Quels déterminants de l'offre de travail ? `kidslt6` (garde d'enfants), `nwifeinc` (effet revenu), `age`, `educ` (via le salaire potentiel).
**La clé** : <font color="#00b050">Pour instrumenter</font> `log(wage)` <font color="#00b050">dans l'équation 1, il faut des variables qui affectent le salaire mais</font> **pas directement** <font color="#00b050">les heures</font> (ex: `exper`, <font color="#6425d0">peut-être certains aspects de</font> `educ`). <font color="#6425d0">Ces variables seront dans l'équation 2 mais exclues de l'équation 1.</font>


## En pratique avec votre exemple actuel
**Avec votre spécification actuelle** (où toutes les variables exogènes apparaissent dans les deux équations) :
- k₁ = 7, k₂ = 7
- K - k₁ = 1, K - k₂ = 1
- Mais **quelle est la variable exclue ?** Il n'y en a aucune ! Vous avez inclus les 7 variables dans chaque équation.
**En réalité, votre système actuel n'est PAS identifiable** car il n'y a **aucune exclusion** ! Chaque équation a (K - k) = 0, pas 1.
DeepSeek m'a mal compris : en réalité, les variables exclues sont retirées de la liste des régresseurs de l'équation pour être placés dans la partie variables instrumentales.

**Conclusion** : Vous avez compris la condition d'ordre, mais vous devez :
1. **Justifier théoriquement** chaque exclusion
2. **Réellement exclure** des variables (pas juste dire que vous les excluez)
3. Comprendre que `K-k` est le nombre de variables **réellement absentes** de l'équation, pas un choix d'instrumentation

## <font color="#c00000">Traitement du problème par DeepSeek</font>
Voulez-vous que nous construisions une spécification théoriquement plausible pour votre modèle d'offre de travail et de salaire ?
Parfait. Construisons ensemble une spécification théoriquement plausible pour votre modèle d'offre de travail et de salaire, qui sera identifiable.
## Modèle théorique plausible
Nous modélisons les décisions conjointes d'une personne sur :
1. **Combien d'heures travailler** (`hours`) - équation d'offre de travail
2. **Quel salaire obtenir** (`log(wage)`) - équation de détermination du salaire
### Justifications théoriques des exclusions
**Variables qui affectent le SALAIRE mais PAS DIRECTEMENT l'offre de travail :
1. **`exper` et `exper²`** : L'expérience sur le marché du travail affecte directement la productivité et donc le salaire. Son effet sur l'offre de travail passe **uniquement** par le salaire (effet revenu et substitution). C'est l'exclusion la plus classique et solide.
2. **`educ`** : L'éducation affecte principalement le salaire via la productivité. Son effet sur l'offre de travail est indirect (via le salaire). Mais certains modèles l'incluent directement dans l'offre de travail pour capter des préférences. Nous allons être prudents.
**Variables qui affectent l'OFFRE DE TRAVAIL mais PAS DIRECTEMENT le salaire :**
3. **`kidslt6`** : La présence de jeunes enfants affecte fortement la disponibilité pour le travail (coûts de garde, préférences). Elle n'affecte pas directement la productivité/salaire (sauf discrimination potentielle, que nous supposons absente).
4. **`nwifeinc`** : Le revenu du conjoint crée un "effet revenu" pur qui affecte l'offre de travail (loi de l'offre de travail classique). Il n'affecte pas directement le salaire de la personne.
**Variables ambiguës :**
- **`age`** : Peut affecter à la fois la productivité (salaire) et les préférences pour le loisir vs travail. Difficile à exclure d'une équation.
### Spécification identifiable proposée
```
text
Équation 1 (Offre de travail - hours) :
hours = α₁₂ log(wage) + β₁₀ + β₁₁ educ + β₁₂ age + β₁₃ kidslt6 + β₁₄ nwifeinc + u₁
Équation 2 (Équation de salaire - log(wage)) :
log(wage) = α₂₁ hours + β₂₀ + β₂₁ educ + β₂₂ age + β₂₅ exper + β₂₆ exper² + u₂
```
### Vérification de l'identification
<u>Variables exogènes du SYSTÈME (K = 7)</u> :  
`constante, educ, age, kidslt6, nwifeinc, exper, exper²`
<u>Équation 1 (hours)</u> :
- Variables endogènes incluses (m₁) : `log(wage)` → **m₁ = 1**
- Variables exogènes incluses (k₁) : `constante, educ, age, kidslt6, nwifeinc` → **k₁ = 5**
- Variables exogènes **excluses** : `exper, exper²` → **K - k₁ = 7 - 5 = 2**
- Condition d'ordre** : 2 ≥ 1 → **Sur-identifiée ✓**
- Instruments naturels pour `log(wage)` dans l'équation 1 : `exper` et `exper²`

<u>Équation 2 (log(wage)) </u>:
- Variables endogènes incluses (m₂) : `hours` → **m₂ = 1**
- Variables exogènes incluses (k₂) : `constante, educ, age, exper, exper²` → **k₂ = 5**
- Variables exogènes **excluses** : `kidslt6, nwifeinc` → **K - k₂ = 7 - 5 = 2**
- Condition d'ordre : 2 ≥ 1 → **Sur-identifiée ✓**
- Instruments naturels pour `hours` dans l'équation 2** : `kidslt6` et `nwifeinc`

### Justification économique de chaque exclusion
**Pourquoi `exper` et `exper²` sont exclus de l'équation 1 (hours) ?**
- **Théorie du capital humain** : L'expérience accumule des compétences spécifiques qui augmentent la productivité, donc le salaire.
- **Effet sur l'offre de travail** : Seulement indirect via l'effet sur le salaire (effet revenu vs substitution).
- **Validation** : <font color="#c0504d">On peut tester si</font> `exper` <font color="#c0504d">a un effet direct sur</font> `hours` <font color="#c0504d">en l'incluant</font> <font color="#c0504d">et en faisant un test de sur-identification</font> <font color="#00b050">(test de Sargan).</font>
 **Pourquoi `kidslt6` et `nwifeinc` sont exclus de l'équation 2 ?**
- **`kidslt6`** : Affecte les coûts fixes du travail (garde d'enfants) et les préférences temps-famille vs travail. N'affecte pas la productivité marginale (hypothèse de non-discrimination).
- **`nwifeinc`** : Crée un revenu non-laborieux qui décale la contrainte budgétaire (effet revenu pur). N'affecte pas la productivité de l'individu.
### Approche en pratique (comment procéder)**
#### Étape 1 : Estimation par 2SLS**
1. **Estimer l'équation 1** :
    - Première étape : Régression de `log(wage)` sur tous les exogènes du système
```text
  log(wage) ~ constante + educ + age + kidslt6 + nwifeinc + exper + exper²
```
  - Obtenir les valeurs prédites `log(wage)_hat`
  - Deuxième étape : Régression de `hours` sur `log(wage)_hat` et les autres exogènes de l'équation 1
  
2. **Estimer l'équation 2** :
  - Première étape : Régression de `hours` sur tous les exogènes du système
  - Obtenir `hours_hat`
  - Deuxième étape : Régression de `log(wage)` sur `hours_hat` et les autres exogènes de l'équation 2
#### Étape 2 : Tests de validité**
1. **Test de sur-identification** (Sargan/Hansen) : Pour vérifier que les instruments exclus sont valides (non corrélés avec l'erreur).
2. **Test de faiblesse des instruments** (F-statistique première étape) : Vérifier que `exper` et `exper²` sont de bons instruments pour `log(wage)` (F > 10).
3. **Test d'endogénéité** (Hausman) : Confirmer que `log(wage)` et `hours` sont bien endogènes.

## **Alternative plus parcimonieuse (si problèmes d'identification)**
Si les instruments sont faibles, on peut simplifier :
```
text
Équation 1 : hours = α₁₂ log(wage) + β₁₀ + β₁₁ educ + β₁₃ kidslt6 + β₁₄ nwifeinc + u₁
Équation 2 : log(wage) = α₂₁ hours + β₂₀ + β₂₁ educ + β₂₅ exper + β₂₆ exper² + u₂
Exclusions :
- Éq1 exclut : `age, exper, exper²` (K-k₁ = 3 ≥ 1)
- Éq2 exclut : `age, kidslt6, nwifeinc` (K-k₂ = 3 ≥ 1)
```
Cette spécification est aussi identifiable et souvent plus robuste.

### Points d'attention importants
1. **La condition de rang** : Il faut que `exper` et `exper²` soient effectivement corrélés avec `log(wage)` après contrôle des autres variables (test F de la première étape).
2. **L'exclusion stricte** : L'hypothèse que `kidslt6` n'affecte pas le salaire est forte (risque de discrimination salariale contre les mères). À tester.
3. **Simultanéité** : Votre modèle suppose que les décisions sont simultanées. C'est plausible sur un marché flexible.

<font color="#00b0f0">Cette spécification vous donne un point de départ théoriquement fondé</font>.
<font color="#00b050"> L'étape suivante est de tester empiriquement ces hypothheses avec vos données.</font>

