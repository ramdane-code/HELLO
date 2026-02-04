Utilisation de R :Florian Heiss

# Introduction

Commencer 
Microsoft R Open (MRO) is available at https://mran.microsoft.com/open/ for all relevant operating systems.

Tabulation, après 1 commande pour  brève description.  
sq   suivi de Tabulation donne une liste des cdes R commençant par SQ.
Ctrl +la flèche vers le haut, ↑ vous donnera une liste de toutes les commandes précédentes. 
Egalement disponible dans la fenêtre " History " (en haut à droite par défaut).

Si nous sélectionnons plusieurs lignes, elles seront toutes évaluées par R

# Packages
La liste des packages installés est visible dans la fenêtre " Packages " (en bas à droite par défaut). Un clic sur le nom du package ouvre le fichier d'aide correspondant qui décrit la fonctionnalité qu'il offre et son fonctionnement. Cet index de package peut également être activé avec help(package="nom du package ").
Les serveurs officiels " Comprehensive R Archive Network " (CRAN) à http://cran.r-project.org. 
Le téléchargement et l'installation des ces packages : 
-	dans la fenêtre Packages de RStudio, cliquez sur " Installer des packages ", 
-	saisissez le nom du package et cliquez sur " Installer ". 
-	Ou bien : install.packages(" nom du package "). 
Pour utiliser un package, il faut l'activer. 
-	en cliquant sur la case à cocher à côté du nom du packages.
-	ou: library(nom du package).
Pour n'utiliser qu'une seule fonction d'un package
-	soit charger le package et appeler la fonction :
		Bibliothèque(Rio)	
		import(nom de fichier)
-	ou appeler la fonction sans charger tout le package :
		 rio ::import(nom du fichier)
Les packages peuvent également contenir des data sets (exemple de Wooldridge)
Charger un data set, par exemple celui nommé affairs, avec 
	data(affairs, package="wooldridge "). 

Voici une liste des packages utilisés dans le livre. Des milliers sont fournis au CRAN.


# Noms de fichiers et Working Directory (répertoire de w)
Inclure le chemin complet sur l'ordinateur quand on fournit un nom à R. 
Le séparateur  est / est non \ utilisé par Microsoft Windows. 
Windows reconnait le chemin ~/MyRProject/MyScript.R. ~ fait référence au dossier " Documents " de l'utilisateur actuel.
Si on ne fournit pas le chemin, R utilisera le " répertoire de travail " actuel pour lire ou écrire des fichiers. 
Obtenir le répertoire de travail actuel : getwd(). Il est galement affiché en haut de la fenêtre Console. 
Changer le répertoire de travail : setwd(path). 
Conseil : un répertoire pour chaque projet (par exemple MyRProject) avec plusieurs sous-répertoires (par exemple Rscripts, données et figures). 
<font color="#00b0f0">Au début de notre script</font>, utiliser setwd(~/MyRProject) <font color="#00b0f0">puis</font> nous référer à un data set dans le sous-répertoire correspondant sous data/MyData.RData et à un fichier graphique sous forme de figures/MyFigure.png .5
Sur le moteur de recherche, chercher rstats et non pas R. Le hashtag Twitter pertinent est # rstats.

# Objets dans R

## Calculs et objets de base

Tableau 1.1. <font color="#00b0f0">Fonctions R pour des calculs arithmétiques importants</font>
abs(v)	Valeur absolue v
sqrt(v)	Racine carrée de v
exp(v)	Fonction exponentielle EV
log(v)	Logarithme naturel ln (v) 
log(v,b)	Logarithme base b: logé_b (v) 
round(v,s)	Round to s chiffres
Factorial(n) Factorial n !
choose(n,k)	Coefficient binomial  (n et en-dessous k)


Mettre l'expression entière entre parenthèses pour afficher immédiatement le résultat : (x <- 5). 
 ls() : donne liste de tous les noms d'objets actuellement définis. cf." Espace de travail " (en haut à droite par défaut). 
exist (" nom ") vérifie si un objet portant le nom " nom " est défini et renvoie soit TRUE soit FALSE
rm(x) supprime l'objet x de l'espace de travail,  et rm(list = ls()) supprime tous les objets.

## Vecteurs
c(value1,value2,...) pour définir un vecteur. 
Tous les opérateurs et fonctions s'appliquent aux vecteurs (ils sont appliqués séparément à chacun des éléments.) 

Script 1.4 : Vectors.R
	# Définissons un vecteur a avec une sortie immédiate via les parantheses :
	(a <- c(1,2,3,4,5,6))
	(b <- a+1)   # ajoute 1 à chacun des éléments
	(c <- a+b)
	(d <- b*c)    # multiplie élément par élément
	sqrt(d)

Tableau 1.2. <font color="#00b0f0">Fonctions R spécifiquement pour les vecteurs</font>
length(v)	: Nombre d'éléments dans v max(v), min(v)	
sort : 
sum(v), prod(v)                               
numeric(n)	: vecteur avec n Zéros
rep(z,n) : vecteur avec n éléments égaux z
seq(t) : suite de 1 à t: {1, 2, ..., t}, alternative : 1 :t 
seq(f,t) : séquence à partir f à t: {f, f + 1, ..., t}, alternative : f :t 
seq(f,t,s) : séquence de f à t, intervalle s

Sortie du script 1.5 : Fonctions-Vectorielles.R 	
'# Définir un vecteur
	(a <- c(7,2,6,9,4,1,3))
'# Fonctions de base :
	sort(a)
	length(a)
	min(a)
	max(a)
	sum(a)
	prod(a)
Création de vecteurs spéciaux :
	numéric(20)
	rep(1,20)
	seq(50)									
	5:15
	seq(4,20,2)


**Tableau 1.3. Opérateurs logiques**
x==y  :   x est égal à y	                      x !=y       x n'est PAS égal à y
x<y	x est inférieur à y	                !b	NON b (c'est-à-dire b est FALSE)
x<=y  x est inférieur ou égal à y	a|b	Soit un ou b est TRUE (ou les deux)
xy	x est plus grand que y	            a&b	a  et b sont TRUE 
x⩾y   x est supérieur ou égal à y

**Types particuliers de vecteurs**
<font color="#00b0f0">Vecteurs de caractères</font>. Pour les manipuler, il suffit que le contenu soit mis entre guillemets :
   cities < c(" New York ", " Los Angeles ", " Chicago ")
<font color="#00b0f0">Vecteurs logiques</font>.  Chaque élément ne peut prendre que TRUE ou FALSE. La façon la plus simple de les générer est de formuler des affirmations qui sont TRUE ou FALSE et de laisser R décider.
 # Basic comparisons:
 0 == 1        [1] FALSE
 0 < 1           [1] TRUE
 # Logical vectors:
 ( a <- c(7,2,6,9,4,1,3) )         [1] 7 2 6 9 4 1 3
 ( b <- a<3 | a=6 )                [1] TRUE TRUE TRUE TRUE FALSE TRUE FALSE

En interne, FALSE est égal à 0 et TRUE égale à 1, et nous pouvons effectuer des calculs en conséquence. 


**Variables qualitatives et Categories (factors)** 
Des variables économique peuvent avoir une interprétation qualitative plutôt que quantitative. Elle prennent un nombre fini de valeurs  et leur résultat n'a pas nécessairement une signification numérique.
Elles  représentent des informations qualitatives.  
Exemples : genre, la spécialité académique, le niveau scolaire, l'état civil, le statut, le type de produit ou la marque. 
Parfois, l'ordre des résultats a une signification (ex: les notes), dans d'autres, pas (comme le statut).
Exemple : on demande aux clients d'évaluer un produit sur une échelle : 1 (= " bad "), 2 (= " ok ") et 3 (= " good "). 
On stocke les réponses de dix répondants en termes de chiffres 1, 2 et 3 dans un vecteur. Nous pourrions travailler avec ces chiffres, mais il est plus  pratique d'utiliser les  factors.
Générer un nouveau vecteur xf à l'aide de la <font color="#00b0f0">commande</font> xf <- factor(x, labels = mylabels) à partir d'un vecteur x composé d'un ensemble fini de valeurs, 
xf <- factor(x, labels=c(" bad ", " ok ", " good ") ).
Dans cet exemple, les résultats sont ordonnés, donc l'étiquetage n'est pas arbitraire. Dans ce genre de cas, nous devrions ajouter l'option ordered=TRUE. 
	# Notes originelles :
	x <- c(3,2,2,3,1,2,3,2,2,1,2)  # R reconnaît qu'il y a 3 catégories
	xf <- factor(x, labels=c(" bad ", " ok ", " bon "))
	x
   [1] 3 2 2 3 1 2 3 2 1 2
	xf
   [1] bon ok mal ok mauvais ok Niveaux : mauvais ok ok bon


## Nommage (Naming) et indexation des vecteurs
<font color="#00b0f0">Les éléments d'un vecteur peuvent être nommés</font>, ce qui peut augmenter la lisibilité de la sortie. 
Étant donné un vecteur vec et un string vector namevec de même longueur, les noms sont attachés aux éléments vectoriels à l'aide de names(vec) <- namevec.
<font color="#00b0f0">Pour accéder à un élément ou à un sous-ensemble</font> à partir d'un vecteur, nous pouvons travailler avec des indices, écrits entre crochets à côté du nom du vecteur : myvector[4] retourne le 4e élément de myvector et <font color="#00b0f0">myvector</font>[6] <-8 <font color="#00b0f0">change le 6e élément pour prendre la valeur 8.</font> 
Pour extraire plus d'un élément, les indices peuvent être fournis eux-mêmes sous forme de vecteur. 
Si les éléments vectoriels ont des noms, nous pouvons aussi les utiliser comme indices comme dans myvector["elementname"].
Les vecteurs logiques peuvent aussi être utilisés comme indices. Si un vecteur général vec et un vecteur logique b ont la même longueur, alors vec[b] retourne les éléments de vec pour lesquels b a la valeur TRUE. 

**Output of Script 1.8: Vector-Indices.R**
 # Create a vector "avgs":
 avgs <- c(.366, .358, .356, .349, .346)
 # Create a string vector of names:
 players <- c("Cobb","Hornsby","Jackson","O'Doul","Delahanty")
 # Assign names to vector and display vector:
 names(avgs) <- players
 avgs
 # Indices by number:
 avgs[2]
 avgs[1:4]
 # Indices by name:
 avgs["Jackson"]
 # Logical indices:
 avgs[ avgs=0.35 ]

# Matrices
R possède un puissant système d'algèbre matricielle. Cf l'annexe D de Wooldridge (2019) 
Matrix(vec,nrow=m) prend nombres stockés dans vector vec et les met dans une matrice avec m lignes.
    rbind(r1,r2,...) prend vecteurs r1,r2,..(qui devraient avoir m longueur) que les rangées de matrice.
    cbind(c1,c2,...) prend les vecteurs c1,c2,..(devrait avoir m longueur que les colonnes de matrice.
.
Script 1.9 : Matrices.R
 # Generating matrix A from one vector with all values:
 v <- c(2,-4,-1,5,7,0)
 ( A <- matrix(v,nrow=2) )

 # Generating matrix A from two vectors corresponding to rows:
 row1 <- c(2,-1,7); row2 <- c(-4,5,0)
 ( A <- rbind(row1, row2) )

 # Generating matrix A from three vectors corresponding to columns:
 col1 <- c(2,-4); col2 <- c(-1,5); col3 <- c(7,0)
 ( A <- cbind(col1, col2, col3) )

 # Giving names to rows and columns:
 colnames(A) <- c("Alpha","Beta","Gamma")
 rownames(A) <- c("Aleph","Bet")
 A

 # Diaginal and identity matrices:
 diag( c(4,2,6) )
 diag( 3 )

 # Indexing for extracting elements (still using A from above):
 A[2,1]
 A[,2]
 A[,c(1,3)]

**Créer Matrices spéciales :**
•	Diag(vec) (où vec est un vecteur) : matrice diagonale avec les éléments sur la diag princ donnés dans le vecteur vec.
•	Diag(N) (où  n est un scalaire) crée la matrice identité N×N.
Si, au lieu d'un vecteur ou d'un scalaire, une matrice M est donnée comme argument à la fonction diag, elle retournera la diagonale principale de M.

Le Script 1.9 (Matrices.R) montre <font color="#00b0f0">comment accéder à un sous-ensemble d'éléments matriciels. </font>
C'est avec des indices donnés entre parenthèses , comme pour les vecteurs. On peut donner une ligne puis un index colonne (ou des vecteurs d'indices), séparés par une virgule :
A[2,3] est l'élément de la ligne 2, colonne 3
A[2, c(1,2)] est un vecteur composé des éléments de la ligne 2, colonnes 1 et 2
A[2, ] est un vecteur composé des éléments de la ligne 2, tous les colonnes

**L'algèbre matricielle de base comprend** :
•	Addition matricielle en utilisant l'opérateur + tant que les matrices ont les mêmes dimensions.
•	L'opérateur *  ne fait pas de multiplication matricielle mais plutôt une multiplication élément par élément.
•	La multiplication matricielle se fait avec l'opérateur un peu maladroit %*% , si les dimensions des matrices correspondent.
•	Transposée d'une matrice X : as t(X)
•	Inverse d'une matrice X : as solve(X)

**Script 1.10: Matrix-Operators.R**
 A <- matrix( c(2,-4,-1,5,7,0), nrow=2)
 B <- matrix( c(2,1,0,3,-1,5), nrow=2)
 A
 B
 A*B
 # Transpose:
 (C <- t(B) )
 # Matrix multiplication:
 (D <- A %*% C )
 # Inverse:
 solve(D)

# Listes 
C'est une collection générique d'objets. Contrairement aux vecteurs, les composants sont nommés et peuvent avoir différents types. 

<font color="#00b0f0">Générer une liste</font> : mylist <- list( nom1=composant1, nom2=composant2, ... )
Les noms des composants sont retournés par names(mylist). 
Un composant peut être adressé par son nom en utilisant mylist$name. 
Les Outputs des analyses (régression...) sont une classes spéciales de listes : 
Les commandes pour les analyses statistiques retournent souvent une liste contenant des characters (comme la commande appelante), des vecteurs (comme les estimations des paramètres) et des matrices (comme les matrices variance-covariance). 

**Script 1.11: Lists.R**
 # Generate a list object:
 mylist <- list( A=seq(8,36,4), this="that", idm = diag(3))
 # Print whole list:
 mylist

 # Vector of names:
 names(mylist)

 # Print component "A":
 mylist$A

# Les Data Frames

<font color="#00b0f0">Distinguer :</font>
-	un <font color="#c0504d">data set</font> (= data frame en  R) : collection de variables sur les mêmes unités d'observation, 
-	et un <font color="#c0504d">data file</font> (fichier de données) pouvant inclure plusieurs data sets et d'autres objets.
Techniquement, <font color="#00b0f0">un data frame n'est qu'une classe spéciale d'une liste de variables</font>. C'est la raison pour laquelle la syntaxe $ est la même que pour la liste générale.
**Script 1.12: Data-frames.R**
 # Define one x vector for all:
 year <- c(2008,2009,2010,2011,2012,2013)
 # Define a matrix of y values:
 product1<-c(0,3,6,9,7,8); product2<-c(1,2,3,5,9,6); product3<-c(2,4,4,2,3,2)
 sales_mat <- cbind(product1,product2,product3)
 rownames(sales_mat) <- year
 # The matrix looks like this:
 sales_mat

 # Create a data frame and display it:
 sales <- as.data.frame(sales_mat)

 sales

Les Output de la matrice sales_mat et data frame sales sont les mêmes, mais se comportent différemment.
Nous pouvons adresser une variable var d'un data frame df en utilisant la syntaxe matricielle df [,"var"]
ou en déclarant df$var.
Parfois, il est pratique de ne pas avoir à taper le nom de data frame plusieurs fois dans une commande. La fonction with(df, some expression using vars of df) le permet. 
Une autre méthode (mais non recommandée) pour travailler facilement avec les dataframes est de les attacher (attach) avant de faire différents calculs utilisant les variables ainsi stockées. Ne pas omettre de les détacher à la fin. 

L'approche " tidyverse ", voir les Sections 1.5.4–1.5.6, est une manière puissante de manipuler les data frame.

**Script 1.13: Data-frames-vars.R**
 # <font color="#00b0f0">Accessing a single variable:</font>
 sales$product2
 # <font color="#00b0f0">Generating a new variable in the data frame</font>:
 sales$ totalv1 <- sales$ product1 + sales$product2 + sales$product3
 # <font color="#00b0f0">The same but using "with"</font>:
 sales$totalv2 <- with(sales, product1+product2+product3)
 <font color="#00b0f0"># The same but using "attach"</font>:
 attach(sales)
 sales$totalv3 <- product1+product2+product3
 detach(sales)
 # Result:
 sales

## Sous-data sets
<font color="#00b0f0">Pour générer un sous ensemble d'un data set</font> : subset(df,criterion), where criterion is a logical expression which evaluates to TRUE for the rows which are to be selected.
Output of Script 1.14: Data-frames-subsets.R
 # Full data frame (from Data-frames.R, has to be run first)
 sales
 # Subset: all years in which sales of product 3 were =3
 subset(sales, product3=3)

## R Data Files (Fichiers de données)
R  possèdes son propre format pour fichiers de données. L'extension usuelle du nom de fichier est .RData
Un fichier R.Data peut contenir un ou plus d'objets de type arbitraire (scalaires, vecteurs, matrices, data frames, ...). 

Si les objets v1,v2,... sont dans l'espace de travail, ils peuvent être enregistrés avec :  save(v1,v2,..., file="mydata. RData ")
Le nom du fichier peut aussi contenir un chemin absolu ou relatif 
Pour enregistrer (sauvegarder) tous les objets actuellement définis : save(list=ls(), file="mydata. RData ")
Tout objet stocké dans mydata. RData peut être chargé dans l'espace de travail avec  : load("mydata.Rdata)
## Informations de base sur un data set
Après avoir chargé un data set dans un data frame : head(df) affiche les premières lignes de données.
str(df) : liste la structure, c'est-à-dire les noms des variables, les types de variables (numériques, strings, logiques, factoriels,...), ainsi que les premières valeurs.
colMeans(df) : rapporte les moyennes de toutes les variables 
summary(df) : montre les statistiques sommaires, voir la section 1.6.4.

**Script 1.15 : RData-Example.R** 
 # Note: "sales" is defined in Data-frames.R, so it has to be run first!
 # save data frame as RData file (in the current working directory)
 save(sales, file = "oursalesdata.RData")
 # remove data frame "sales" from memory
 rm(sales)
 # Does variable "sales" exist?
 exists("sales")
 # Load data set (in the current working directory):
 load("oursalesdata.RData")
 # Does variable "sales" exist?
 exists("sales")
 sales
 # averages of the variables:
 colMeans(sales)	

## Importation et exportation de fichiers texte
Les logiciels qui gèrent des données sont capables de fonctionner avec des données stockées sous forme de fichiers texte. Cela en fait un moyen naturel d'échanger des données entre différents programmes et utilisateurs. 
Les extensions courantes de noms de fichiers pour ces fichiers de données sont RAW, CSV ou TXT.

<font color="#00b050">La  commande R read.table</font> <font color="#00b0f0">offre la possibilité de lire de nombreuses variantes de fichiers texte qui sont ensuite stockées sous forme de data frames.</font>
newdataframe <- read.table(nom du fichier, ...)
Les arguments optionnels qui peuvent être ajoutés, séparés par virgule :
header=TRUE : Le fichier texte inclut les noms des variables comme première ligne
sep= ", " ou ";" : Au lieu d'espaces ou de tabulations, les colonnes sont séparées par une virgule ou point virgule. 
dec= ", " : <font color="#00b0f0">Au lieu d'un point décimal, une virgule décimale est utilisée</font>. 
row.names=numéro : <font color="#6425d0">Les valeurs de la colonne numéro  sont utilisées comme noms de lignes.</font>

Les commandes <font color="#00b050">read.csv</font> et <font color="#00b050">read.delim</font> fonctionnent de manière très similaire mais ont des paramètres par défaut différents pour des options comme header et sep.

<font color="#c0504d">RStudio propose une interface graphique pour importer des fichiers texte </font>qui permet également de prévisualiser les effets de la modification des options : 
Dans la fenêtre de l'espace de travail (menu File), cliquez sur " Importer un data set ".
Le dossier sales.txt contient un en-tête avec les noms des variables. Il peut être importé avec
mydata <- read.table("sales.txt", header=TRUE)
Dans le fichier sales.csv, les colonnes sont séparées par une virgule; la commande pour l'importer 
mydata <- read.table("sales.csv", sep=",")
Quand le fichier de données csv ne contient pas de variable, elles sont définies à leurs valeurs par défaut V1 à V4 dans la data frames résultant mydata. Ces noms peuvent être modifiés manuellement avec :
colnames(mydata) <- c(" year ", " prod1 ", " prod2 ", " prod3 ").

Les données du dataframe mydata peuvent être exportées en fichier texte avec des options similaires à celles de read.table : write.table(mydata, file = "myfilename", ...)

## Importation et exportation d'autres formats de données
R doit pouvoir lire ou écrire directement des données dans le format natif d'un autre logiciel. 
**Le package rio** est très pratique pour l'importation et l'exportation de données. 
-	Il détermine le type de format de données à partir de l'extension de nom de fichier : *.csv pour CSV... 
-	Il appelle ensuite un package approprié pour effectuer l'importation ou l'exportation réelle. 
-	La syntaxe est aussi simple que possible :
" myfilename " est le nom complet du fichier incluant l'extension et le chemin, sauf s'il se trouve dans le répertoire de travail actuel.
rio::import("myfilename")
rio::export("myfilename")

## Data sets dans les exemples de Wooldridge

**Script 1.16 : Example-Data.R**
'# The data set is stored on the local computer in : ~/Documents/R/data/wooldridge/affairs.dta

 # Version 1: from package. make sure to install.packages(wooldridge)
 data(affairs, package='wooldridge')

 # Version 2: Adjust path
 affairs2 <- rio::import("~/Documents/R/data/wooldridge/affairs.dta")

 # Version 3: Change working directory
 setwd("~/Documents/R/data/wooldridge/")
 affairs3 <- rio::import("affairs.dta")

 # Version 4: directly load from internet
 affairs4 <- rio::import("http://fmwww.bc.edu/ec-p/data/wooldridge/affairs.dta")

 # Compare, e.g. avg. value of naffairs:
 mean(affairs$naffairs)
 mean(affairs2$naffairs)
 mean(affairs3$naffairs)
 mean(affairs4$naffairs)


# Graphismes de base
Dans cette section, nous discutons de l'approche globale de base R pour produire des graphes et des types généraux les plus importants de graphes. 
Section 1.5 introduira une approche différente basée sur le package ggplot2. 
Certains graphiques spécifiques utilisés pour les statistiques descriptives seront introduits dans la Section 1.6.

## Graphes de base
Graphes bidirectionnels possèdent une abscissa et une ordonnée qui représentent deux variables : x et y. 
Exemple : tracer y =  f (x). Dans R, un diagramme de fonctions peut être généré par la commande

xmin et xmax sont les limites pour l'axe des x. 
Exemple : la commande curve( x^2, -2, 2 ) mais aussi curve( dnorm(x), -3, 3 )

Si nous avons des données dans deux vecteurs x et y, nous pouvons générer des nuages de points, des graphiques ou des graphiques bidirectionnels similaires. 

L'option la plus fondamentale de ces plots est type. Il peut prendre les valeurs " p " (par défaut), " l ", " b ", " o ", " s ", " h ", et plus encore. Les graphiques obtenus sont présentés à la Figure 1.6.



## Personnalisation des graphiques avec des options
Ces graphiques, ainsi que ceux créés par curve, peuvent être ajustés. 
Le symbole de point peut être modifié en utilisant l'option pch. 
Le type de ligne peut être modifié en utilisant l'option lty. 
La taille des points et des textes peut être modifiée avec l'option cex. Il représente un factor (standard : cex=1).
La largeur des lignes peut être modifiée en utilisant l'option lwd. Représente un facteur (standard :
lwd=1).
La couleur des lignes et des symboles peut être changée en utilisant l'option col=valeur. Elle peut être spécifiée de plusieurs manières :
   Par nom : Une liste des noms de couleurs disponibles peut être obtenue par colors() et inclura plusieurs centaines de noms de couleurs, allant des évidents " black ", " blue ", " green " ou " red " à des plus exotiques comme " papayawhip ".
   Par un nombre correspondant à une liste de couleurs (palette) qui peut être ajustée.
   Par Gray scale (échelle des gris) : grey (level) avec level = 0 pour noir et level = 1  pour le blanc.
   Par des valeurs RVB avec une string de la forme  "#RRGGBB " où chacune des paires RR, GG, BB est constituée de deux chiffres hexadécimaux. C'est utile pour l'ajustement fin des couleurs.
   Par la fonction rgb(red. green. blue).....
Un titre principal et un sous-titre peuvent être ajoutés avec main="Mon Titre " et sub="Mon sous-titre ".
Les axes horizontal et vertical peuvent être identifiés à l'aide de xlab="My x axis label " et
ylab="My y axis label" .
Les limites de l'axe horizontal et vertical peuvent être choisies en utilisant xlim=c(min,max) et
ylim=c(min,max).
Les labels des axes peuvent être définis pour être parallèles à l'axe (las=0), horizontales (las=1), perpendiculaires à l'axe (las=2) ou verticales (las=3).

Quelques options supplémentaires doivent être définies avant la création du graphe en utilisant la commande par(option1=value1, option2=value2, ...). 
Pour certaines options, c'est la seule possibilité. Un exemple important est la marge autour de la zone de tracé. 
Un autre exemple est la possibilité de placer plusieurs courbes en dessous ou côte à côte dans un même graphe en utilisant les options mfcol ou mfrow.

## Superposant plusieurs plots
Pour tracer plus d'une fonction ou un ensemble de variables, utiliser plusieurs  commandes curve et/ou plot séquentiellement. 
Par défaut, chaque plots remplace la précédente. Pour éviter cela et superposer les graphiques, utilisez l'  option add=TRUE. 
Voici un exemple qui illustre également les options lwd et lty. Son résultat est montré à la Figure 1.7(a) :

Il y a également des commandes spécialisées pour ajouter des éléments à un graphe existant, chacun pouvant être ajusté avec les mêmes options de formatage présentées ci-dessus :
points (x,y,...) et lines (x,y,...) Ajoute des points et des lignes un peu comme  l' option add=TRUE de plot .
text(x,y,"montexte,...) Ajoute du texte aux coordonnées (x,y). L'option pos=nombre positionne le texte, à gauche, au-dessus ou à droite des coordonnées spécifiées si pos est réglé à 1, 2, 3 ou 4, respectivement.
abline(a=valeur,b=valeur,...) ajoute une droite avec un intercept a et une pente b.
abline(h=valeur(s),...) ajoute 1 ou +ieurs droites horizontales à la position h (qui peut être un vecteur).
abline(v=valeur(s),...) ajoute 1 ou plusieurs droites verticales à la position v (qui peut être un vecteur).
arrows (x0, y0, x1, y1, ...) ajoute une flèche du point x0,y0 au point x1,y1.

Le Script 1.17 (Plot-Overlays.R) combine différentes commandes et options de tracé pour générer la Figure 1.7(b).

**Script 1.17 : Superpositions de graphs(plot-overlays.R)**
plot(x,y, main="Example for an Outlier")
points(8,1)
abline(a=0.31,b=0.97,lty=2,lwd=2)
text(7,2,"outlier",pos=3)
arrows(7,2,8,1,length=0.15)

La commande matplot est alternative pratique pour spécifier les graphiques séparément. 

**Script 1.18: Plot-Matplot.R**
'# Define one x vector for all:
year <- c(2008,2009,2010,2011,2012,2013)
'# Define a matrix of y values:
product1 <- c(0,3,6,9,7,8)
product2 <- c(1,2,3,5,9,6)
product3 <- c(2,4,4,2,3,2)
sales <- cbind(product1,product2,product3)
'# plot
matplot(year,sales, type="b", lwd=c(1,2,3), col="black" )
## Legends
Si l'on combine plusieurs graphiques en un seul, il est souvent utile d'ajouter une légende à un graphique. 
La commande est   <font color="#c0504d">legend(position, labels, formats,...) </font>où position détermine le placement. Il peut s'agir d'un ensemble de coordonnées x et  y, mais il est plus pratique d'utiliser l'un des <font color="#c0504d">mots-clés </font>
"bottomright", "bottom", "bottomleft", "left", "topleft", "top", "topright", "right", or "center"
<font color="#c0504d">labels</font> : vecteur de strings qui servent de labels pour la légende.  Il doit être spécifié comme suit
c(" first label ","second label ",...).
<font color="#c0504d">formats</font> reproduit les styles de lignes et de marqueurs utilisés dans le graph. Utiliser les mêmes options listées dans la Section 1.4.2 comme pch et lty.

Dans la légende, mais aussi partout dans un graphique (titre, labels d'axes, textes, ...) nous pouvons aussi <font color="#c0504d">utiliser des lettres grecques</font>,<font color="#c0504d"> des équations et des caractéristiques similaires</font>. Cela se fait en utilisant la commande <font color="#00b0f0">expression(specific syntax)</font>. Une liste complète de cette syntaxe se trouve dans les <font color="#00b0f0">fichiers d'aide quelque peu cachés sous plotmath. </font>

# Exportation vers un fichier
RStudio a une <font color="#c0504d">fenêtre Plots </font>(en bas à droite par défaut). Cette fenêtre dispose également d'un <font color="#c0504d">bouton Export</font>, qui permet d'enregistrer le graphique généré dans différents formats graphiques. 
Il est incommode d'exporter les graphismes manuellement de cette façon, surtout si un script génère plusieurs figures. R offre la possibilité d'exporter les graph générés à l'aide de commandes spécifiques dans le script.
<font color="#00b0f0">Le format PNG </font>(Portable Network Graphics) est très utile. 
Pour les utilisateurs LaTeX, les fil-es PS, EPS et SVGsont disponibles, et le PDF est très utile. 
<font color="#c0504d">Exporter les graphs en trois étapes </font>:
1.<font color="#00b0f0">Lancez le fichier graphique et choisir quelques options</font> :
<font color="#6425d0">Pour un fichier PNG</font> : png(nom de fichier="myfilename.png ",largeur=valeur,hauteur=valeur,...)
Pour le nom du fichier, les règles concernant les chemins et le répertoire de travail s'appliquent. La largeur et la hauteur sont spécifiées en pixels et par défaut sont égales à 48. Même approche pour les formats BMP, JPEG et TIFF.
<font color="#6425d0">Pour un fichier PDF</font>: pdf(fichier = " myfilename.pdf ", largeur = valeur, hauteur = valeur ,...)
La différence est que le nom du fichier est spécifié comme fichier et que la largeur et la hauteur sont spécifiés en  pouces et sont tous deux égaux à 7 par défaut.
<font color="#00b0f0">Dites à R avoir terminé le fichier graphique avec la commande</font><font color="#00b050"> dev.off().</font> <font color="#c0504d">Cela créera des problèmes avec le fichier si elle est oubliée.</font>

# Manipulation et visualisation des données : Le Tidyverse
La visualisation des données fournit des informations importantes sur leur structure et relations.
" tidyverse " est une approche pour la manipulation et la visualisation des données, mise en œuvre dans un ensemble de packages. 
Pour une introduction plus détaillée, cf. Wickham et Grolemund (2016).
## Visualisation des données : Bases de ggplot 
Le New York Times génère ses visualisations avec ggplot2.
<font color="#00b0f0">Le point de départ pour un  graphique ggplot2 est un data frame" soigné " (tidy)</font> : les unités d'observation dans les lignes et les variables dans les colonnes. 
<font color="#7030a0">À titre d'exemple, considérons le data set mpg du  package ggplot2</font> et disponible après le chargement du package avec library(ggplot2). Il contient des *informations sur 224 modèles de voitures de 1999 ou 2008*, pour plus de détails, voir aide(mpg). Script 1.21 (mpg-data. R) <font color="#c0504d">affiche les premières lignes de données</font>. 
<font color="#7030a0">L'objectif est de visualiser la relation entre la cylindrée (displ) et la consommation sur autoroute (autoroute)</font>.

**Script 1.21 : mpg-data. R**
	# charger le packages
	library (ggplot2)
	# Premières lignes de données du data set mpg :
	head (mpg)
'# Un <font color="#c0504d">tibble</font> : 6 x 11 (output)

<font color="#00b0f0">" gg " dans ggplot2 fait référence à une " grammaire des graphiques " </font>: 
- un graphe se compose d'un ou plusieurs objets géométriques (ou geoms) : points, lignes ou autres objets. 
- Ils sont ajoutés au graphe avec une fonction spécifique au type du geom :
	•	geom_point() : points
	•	geom_line() : lignes
	•	geom_smooth() : régression non paramétrique
	•	geom_area() : ruban
	•	geom_boxplot() : boxplot
Il existe de nombreux autres geoms pour des besoins spécifiques. 
<font color="#00b0f0">Ces objets possèdent des caractéristiques visuelles comme la position sur les axes x et y</font> ,<font color="#00b050"> données sous forme de variables dans le référentiel</font>. <font color="#7030a0">Des caractéristiques comme la couleur, la forme ou la taille des points peuvent être liées à des variables dans le data set</font> – au lieu de les définir globalement . 
Ces connexions sont appelées applications <font color="#00b0f0">aesthetic mappings</font> et sont définies dans une <font color="#00b0f0">fonction aes(feature=variable, ...)</font>. Par exemple :
•	<font color="#00b0f0">x=...:</font> Variable pour mapper l'axe x 
•	<font color="#00b0f0">y=...: </font>Variable pour mapper l'axe y 
•	<font color="#00b0f0">colour=...:</font> Variable à appliquer à la couleur (par exemple du point) 
•	<font color="#00b0f0">shape=...:</font> Variable pour mapper la forme (par exemple du point)

<font color="#00b0f0">Un  graphe ggplot2 est toujours initialisé avec un appel ggplot()</font>. <font color="#c0504d">Les geoms s'ajoutent avec un +</font>.
The geoms a added with  +. 
As a basic example, we would like to <font color="#00b050">use the data set mpg and map displ on the x axis and hwy on the</font>
<font color="#00b050">y axis</font> (utiliser le data set mpg pour mapper displ sur l'axe des x et hwy sur l'axe des y)

<font color="#c0504d">Script 1.22: mpg-scatter.R</font>
'# load package
library(ggplot2)
'# Generate ggplot2 graph:
ggplot() + geom_point( data=mpg, mapping=aes(x=displ, y=hwy) )

<font color="#00b0f0">Ajoutons un second " geom " au graphique. </font>
La <font color="#c0504d">régression non paramétrique</font> est un sujet non abordé dans Wooldridge (2019), mais il est facile de la mettre en œuvre avec ggplot2. Nous utiliserons ces outils <font color="#c0504d">pour visualiser la relation entre deux variables</font>. Pour plus de détails, voir par exemple Pagan et Ullah (2008).
L<font color="#c0504d">a figure 1.10(b) montre le même nuage de points, avec une fonction de régression non paramétrique ajoutée</font>. Cela représente quelque chose comme la moyenne de hwy étant  donné que displ est proche de la valeur respective sur l'axe. Le ruban gris autour de la ligne visualise l'incertitude et est relativement large pour des valeurs de dissipation très élevées  lorsque les données sont rares. Pour la majeure partie de la zone concernée, il semble y avoir une <font color="#c0504d">relation clairement négative entre le déplacement et le kilométrage sur autoroute.</font>

La figure 1.10(b) peut être générée en ajoutant le geom approprié au nuage de points avec
<font color="#c0504d">+geom_smooth(...):</font>

ggplot() +
geom_point( data=mpg, mapping=aes(x=displ, y=hwy) ) +
geom_smooth(data=mpg, mapping=aes(x=displ, y=hwy) )

Notez que<font color="#c0504d"> le code du graphique s'étend sur trois lignes, ce qui facilite sa lecture.</font> <font color="#4bacc6">Nous ajoutons simplement les +</font>
<font color="#4bacc6">à la fin de la ligne précédente pour préciser explicitement que nous n'avons pas encore fini.</font>

Output : Figure 1.10. Simple graphs created by ggplot2

<font color="#c0504d">La répétition de " data=mpg, mapping=aes(x=displ, y=hwy) "</font> dans les deux geoms rend notre code plus long que nécessaire et sujet aux erreurs : si nous changeons le data sets ou de variables, nous devons faire des modifications (cohérentes) en différents endroits.  <font color="#00b050">ggplot2 a une solution : </font>
-	<font color="#00b050">définir data et mapping dans l'appel initial de la  fonction ggplot()</font> : elle sera valide pour tous les geoms du graphe. 
<font color="#6425d0">Nous pouvons aussi omettre les noms des arguments si nous respectons l'ordre des arguments.</font>
De même, <font color="#6425d0">si l'on ne nomme pas les arguments de aes, le premier argument est le mapping de l'axe x,  et le second celui de l' axe y :</font>

**Script 1.23: mpg-regr.R**
ggplot(mpg, aes(displ, hwy)) +
geom_point() +
geom_smooth()

## Couleurs et formes dans  les graphiques ggplot 
Nous pouvons changer la couleur de tous les points ou de la courbe de régression de façon similaire à celle décrite pour les graphiques de base dans la Section 1.4.2. 

**Script 1.24: mpg-color1.R**
ggplot(mpg, aes(displ, hwy)) +
geom_point(color=gray(0.5)) +
geom_smooth(color="black")

Nous pouvons utiliser différentes couleurs pour des groupes de points définis par une troisième variable afin d'explorer et visualiser les relations. 
Par exemple, on peut distinguer les points par la <font color="#6425d0">class</font> de variables avec des couleurs différentes. Le Script 1.25 (mpg-colo2.R) définit `aes(color=class` comme option de `geom_point`. R attribue une couleur à chaque valeur de `class`
On peut aussi ajouter l'intensité par exemple de la couleur grise avec `+scale_color_grey()`.
La legend est ajoutée automatiquement.

Script 1.25 : mpg-color2. R
ggplot(mpg, aes(displ, hwy)) +
geom_point( aes(color=class) ) +
geom_smooth(color="black") +
scale_color_grey()

On peut utiliser différentes formes de points.
Le script 1.26 (mpg-color3.R) associe donc la classe à la fois à la couleur et à la forme.
Nous choisissons les formes numérotées de 1 à 7 avec l'option supplémentaire +scale_shape_manual(values=1:7).note18
Le résultat est présenté sur la figure 1.12(a). 
On distingue désormais plus clairement deux types de voitures à très forte cylindrée :
- les SUV et les pick-up, grands consommateurs d'essence, affichent une faible consommation
- et les voitures biplaces, une consommation relativement élevée.

Script 1.26 : MPG-COLOR3. R
ggplot(mpg, aes(displ, hwy)) +
geom_point( aes(color=class, shape=class) ) +
geom_smooth(color="black") +
scale_color_grey() +
scale_shape_manual(values=1:7)

Examinons à nouveau les correspondances esthétiques : dans le script 1.26 (mpg-color3.R), x et y sont
associés dans l’appel à ggplot() et sont valides pour toutes les géométries, tandis que la forme et la couleur ne sont actives que dans geom_point(). Nous pouvons les spécifier directement dans l’appel à ggplot() pour les rendre
valides pour toutes les géométries, comme c’est le cas dans le script 1.27 (mpg-color4.R). 
Le graphique résultant est présenté dans la figure 1.12(b). Le lissage est désormais effectué séparément pour chaque classe et indiqué par la couleur.
La correspondance avec la forme est ignorée par geom_smooth() car elle n’a aucun sens pour la fonction de régression.

**Script 1.27 : mpg-color4. R**
ggplot(mpg, aes(displ, hwy, color=class, shape=class)) +
geom_point() +
geom_smooth(se=FALSE) +
scale_color_grey() +
scale_shape_manual(values=1:7)

Ce graphique semble surchargé d’informations ; si nous trouvons ce type de graphique
utile, nous pourrions envisager de regrouper les classes de voitures en trois ou quatre types plus larges.19

## Ajustement fin des graphes ggplot 
Tous les aspects des  graphes ggplot2 peuvent être ajustés. Au lieu d'essayer de faire une liste exhaustive, donnons quelques exemples. (cf explications p.40)

**Script 1.28: mpg-advanced.R**
ggplot(mpg, aes(displ, hwy, color=class, shape=class)) +
	geom_point() +
	geom_smooth(se=FALSE) +
	scale_color_grey() +
	scale_shape_manual(values=1:7) +
	theme_light() +
	labs(title="Displacement vs. Mileage",
		subtitle="Model years 1988 - 2008",
		caption="Source: EPA through the ggplot2 package",
		x = "Displacement [liters]",
		y = "Miles/Gallon (Highway)",
		color="Car type",
		shape="Car type"
		) +
	coord_cartesian(xlim=c(0,7), ylim=c(0,45)) +
	theme(legend.position = c(0.15, 0.3))
	ggsave("my_ggplot.png", width = 7, height = 5)

# Manipulation de données de base avec dplyr

<font color="#00b0f0">Le package  WDI permet de rechercher et de télécharger des données provenant des indicateurs de développement mondial de la Banque mondiale. </font>Les détails et instructions du  package WDI sont disponibles à https://github.com/vincentarelbundock/WDI.
<font color="#00b050">Notre objectif ici est d'examiner l'évolution de l'espérance de vie féminine aux États-Unis. </font>
<font color="#c0504d">Les séries de données WDI portent des noms cryptiques.</font> <font color="#00b050">La commande WDIsearch ("life exp") révèle que notre série s'appelle SP.DYN.LE00.FE.IN. </font>
<font color="#c0504d">Script 1.29 (wdi-data. R) télécharge les données </font>pour les années 1960–2014 en utilisant la commande WDI et affiche les six première et dernière lignes. Nous avons un total de 14 520 lignes correspondant à différents groupes de pays (comme le monde arabe) et à des pays (comme l'Algérie)

**Script 1.29: wdi-data.R**
 # <font color="#c0504d">packages: WDI for raw data, dplyr for manipulation</font>
 library(WDI);
 wdi_raw <- WDI(indicator=c("SP.DYN.LE00.FE.IN"), start = 1960, end = 2014)
 head(wdi_raw)
 tail(wdi_raw)
<font color="#00b0f0">Affiche un en-tête DF avec</font> : iso2c (indicatif pays ou groupe de pays),  SP.DYN.LE00.FE.IN., year.

**Nous aimerions utiliser les outils dplyr afin de :** 
- extraire les variables pertinentes, 
- filtrer uniquement les données pour les États-Unis, 
- renommer la variable d'intérêt, 
- trier par année dans un ordre croissant, 
- et générer une nouvelle variable. 

<font color="#00b0f0">Les fonctions ont des verbes comme noms </font>, assez intuitifs à comprendre. Elles sont axés sur les Data Frames et ont toutes la <font color="#00b0f0">même structure</font> : <font color="#c0504d">le premier argument est toujours un data frame</font> <font color="#00b050">et le résultat en est un aussi</font>. 
Ainsi, <font color="#7030a0">la structure générale des commandes dplyr est</font> : new_data_frame <- some_verb(old_data_frame, details)

**Script 1.30 (manipulation wdi.R) effectue plusieurs manipulations du data set**. 
- La première étape est de <font color="#00b050">filtrer les  lignes</font> (rows) pour les États-Unis. La fonction pour cela est <font color="#00b050">filter</font>. Nous lui fournissons nos données brutes et la condition, et obtenons la data frames filtrée. 
- Nous aimerions<font color="#00b050"> remplacer le nom de variable</font> SP.DYN.LE00.FE.IN par LE_fem. Dans le tidyverse, cela se fait avec <font color="#00b050">rename</font>(old_data, new_var=old_var). 
- L'étape suivante consiste à <font color="#00b050">sélectionner les variables pertinentes</font> , year et LE_fem. Le verbe approprié est <font color="#00b050">select</font> et nous listons les variables choisies dans l'ordre préféré. 
- Enfin, <font color="#00b050">nous ordonnons la data frames</font> par année avec la fonction <font color="#00b050">arrange</font>.
<font color="#c0504d">Dans ce script, nous écrasons à plusieurs reprises la data frames</font>. la Section 1.5.5 introduit une manière plus élégante d'obtenir le même résultat. 
<font color="#00b050">Nous imprimons les six premières et six dernières lignes </font>de données après toutes les étapes de manipulation : elles sont désormais  adaptées à la plupart des tâches d'analyse de données ou à produire un plot avec ggplot. 

**Script 1.30: wdi-manipulation.R**
library(dplyr)
<font color="#c0504d"> # filter: only US data</font>
 ourdata <- filter(wdi_raw, iso2c == "US")
<font color="#c0504d"> # rename lifeexpectancy variable</font>
 ourdata <- rename(ourdata, LE_fem=SP.DYN.LE00.FE.IN)
<font color="#c0504d"> # select relevant variables</font>
 ourdata <- select(ourdata, year, LE_fem)
<font color="#c0504d"> # order by year (increasing)</font>
 ourdata <- arrange(ourdata, year)
<font color="#c0504d"> # Head and tail of data</font>
 head(ourdata)
 tail(ourdata)

<font color="#c0504d"> # Graph</font>
 library(ggplot2)
 ggplot(ourdata, aes(year, LE_fem)) +
 geom_line() +
 theme_light() +
 labs(title="Life expectancy of females in the US",
 subtitle="World Bank: World Development Indicators",
 x = "Year",
 y = "Life expectancy [years]"
 )



## Pipes
Les Pipes sont un concept important dans le tidyverse. Ils sont en fait introduits dans le package magrittr qui est automatiquement chargé avec dplyr. 
<font color="#00b050">Les pipes permettent de remplacer la réécriture répétée de la data frames dans le Script 1.30 (wdi-manipulation.R) par un Script plus concis, moins sujet aux erreurs et plus efficace sur le plan informatique.</font>

Pour comprendre le concept de pipe, <font color="#c0504d">considérons un exemple un peu absurde de calculs séquentiels</font> : <font color="#4bacc6">calculer exp(log10(6154)), arrondi à deux chiffres.</font> Cela peut s'écrire : <font color="#c0504d">round(exp(log(6154,10),2)</font>
Bien que cela donne le résultat correct 44.22, il est assez difficile à écrire, lire et déboguer. 
Une alternative serait de <font color="#7030a0">faire les calculs séquentiellement et de stocker les résultats dans une variable temporaire :</font>
	temp <- log(6154, 10)
	temp <- exp(temp)
	temp <- round(temp, 2)
	temp
Cependant, cela est loin d'être optimal.
C'est là que le <font color="#00b050">pipe</font> entre en jeu. Il est un <font color="#00b050">opérateur qui s'écrit % %</font>. 
- Il <font color="#00b050">prend l'expression du côté gauche </font>
- et l'utilise comme <font color="#00b050">premier argument pour la fonction du côté de droite.</font> 
- Raccourci : <font color="#00b050">Ctrl+Shift+M</font>
<font color="#7030a0">Exemple</font> :   25 % % sqrt() correspond à sqrt(25) 
**L'exemple** <font color="#c0504d">round(exp(log(6154,10),2)</font> peut se traduire par :
log(6154,10)  % %
exp() % %
round(2)
<font color="#00b0f0">Explication :</font>
-	log(6154,10) est évalué en premier. 
-	Son résultat est ensuite " canalisé " dans la  fonction exp() à droite.  
-	le pipe suivant prend ce résultat comme premier argument de la  fonction round à droite. 
Ainsi, on peut <font color="#00b050">lire le pipe comme  and then</font> : Calculer le log, <font color="#00b050">and then</font> prendre l'exposant <font color="#00b050">and then</font> faire l'arrondi à deux chiffres. 
Cette approche est utilisée avec **dplyr**, puisque ses fonctions attendent (expect) <font color="#00b050">l'ancienne data frames comme première entrée</font> et <font color="#00b050">retournent la nouvelle trame</font>. 
<font color="#c0504d">Script 1.31 (wdi-pipes. R) effectue les mêmes calculs que 1.30 (wdi-manipulation.R) mais utilise des Pipes. </font>
• <font color="#c0504d">Take</font> the data set wdi_raw and then ...
• <font color="#c0504d">filter</font> the US data and then ...
• <font color="#c0504d">rename</font> the variable and then ...
• <font color="#c0504d">select</font> the variables and then ...
• <font color="#c0504d">order</font> by year

**Script 1.31: wdi-pipes.R**
library(dplyr)
<font color="#c0504d">'# All manipulations with pipes:</font>
   ourdata <- wdi_raw % %    
   filter(iso2c== "US") % %    # ne retenir que les obs pour lesquelles la col. iso2c est "US"
   rename(LE_fem=SP.DYN.LE00.FE.IN) % %
   select(year, LE_fem) % %    # ne retenir que les col. year et LE_fem
   arrange(year)                      # ordonner les deux col par year

## Manipulation avancée des données avec dplyr
<font color="#c0504d">Calculer la moyenne de l'espérance de vie des femmes sur des groupes de pays, et graphe Figure 1.15</font>
<font color="#00b0f0">La première étape consiste à classer les pays en groupes de revenus. </font>
- L<font color="#d83931">e package WDI</font> stocke les données spécifiques à chaque pays dans la <font color="#d83931">matrice</font>  *WDI_data$country*, 
- celle-ci comprend une <font color="#d83931">classification des revenus dans la colonne </font> *income*. 

<font color="#6425d0">Script 1.32 (wdi-ctryinfo. R) </font>
<font color="#00b0f0">Commence par manipuler 2 matrices wdi</font> qu'il convertit en DF (*le_data* et *ctryinfo*) puis en extrait les informations pertinences et générer un DF combiné *alldata.*
-	<font color="#6425d0">télécharge life expectancy data</font> dans la data frames *le_data* et <font color="#6425d0">renomme</font> la main variable. 
-	télécharche la matrice *country-level* dans une data frame *ctryinfo* et sélectionne les col. countryname et  income classification (exemple : le Zimbabwe est classé pays à faible revenu). 
<font color="#00b0f0">Le défi prochain est de combiner ces deux data sets</font> : garder *le_data* et lui ajouter la  classification revenus des pays à partir de *ctryinfo*. C'est <font color="#00b0f0">ce que fait left_join, une fonction de dplyr.</font> 
- Elle suppose (figure) que <font color="#7030a0">la variable country  existe dans les deux data sets</font> <font color="#00b050">et les fusionne donc par cette variable</font>. 
- Le <font color="#00b050">data set combiné</font>, **alldata** dans l'exemple,  correspond à *le_data*, mais comporte la colonne income en plus.
<font color="#00b0f0">Il existe d'autres fonctions pour combiner des data sets : </font>
-	right_join <font color="#00b0f0">conserve les lignes de la seconde data frames</font>, 
-	inner_join <font color="#00b0f0">ne conserve que les lignes existantes dans les deux data sets</font>, 
-	full_join <font color="#00b0f0">conserve toutes les lignes présentes dans l'un des data sets. </font>
Voir Wickham et Grolemund (2016) et la cheat sheet sur la manipulation des données 
<font color="#00b050">Les cheat sheet se trouvent</font> sur https://www.rstudio.com/resources/cheatsheets/

**Output of Script 1.32: wdi-ctryinfo.R**
 library(WDI); library(dplyr)
 <font color="#00b0f0"># Download raw life expectency data</font>
 le_data <- WDI(indicator=c("SP.DYN.LE00.FE.IN"), start = 1960, end = 2014) % %
 rename(LE = SP.DYN.LE00.FE.IN)
 tail(le_data)
<font color="#00b0f0"> # Country-data on income classification</font>
 ctryinfo <- as.data.frame(WDI_data$country, stringsAsFactors = FALSE) % %
 select(country, income)
 tail(ctryinfo)
<font color="#00b0f0"> # Join:</font>
 alldata <- left_join(le_data, ctryinfo)
Joining, by = "country"
 tail(alldata)
 
<font color="#c00000">Ensuite, calculer l'espérance de vie moy par année de chacun des pays partageant la même classification de revenus. </font>
<font color="#00b050">dplyr propose la fonction summerize où somefunc est toute fonction qui accepte un vecteur et retourne un scalaire. </font>
- <font color="#7030a0">nous voulons calculer la moyenne</font>, donc nous choisissons la fonction mean (voir la section 1.6). 
- Comme il<font color="#de7802"> manque quelques valeurs</font> dans la série life expectancy, il faut <font color="#7030a0">utiliser l'option</font> na.rm=TRUE. 
<font color="#c00000">Nous obtiendrions alors la moyenne globale</font> sur tous les pays et toutes les années (environ 65,5 ans).
Ce n'est pas exactement ce que nous cherchions: <font color="#00b0f0">nous devons nous assurer que la moyenne est calculée séparément par revenu et par année. </font>
+ commencer par <font color="#00b0f0">regrouper les données du data frame avec</font> group_by(income, year). Cela indique aux fonctions comme summarize d'effectuer les calculs par groupe. 
+ Un tel regroupement peut être supprimé avec ungroup().

<font color="#00b0f0">Le script 1.33 (wdi-ctryavg.R) effectue ces calculs</font>. 
-	Il <font color="#00b0f0">supprime d'abord les lignes correspondant à des agrégats</font> (comme le Monde arabe) plutôt qu'à des pays individuels, ainsi que les pays non classés par la Banque mondiale. 
-	Ensuite, <font color="#00b0f0">le regroupement est ajouté à l'ensemble de données et la moyenne est calculée</font>.
- <font color="#00b0f0">Les six dernières lignes de données sont affichées</font> : elles correspondent au groupe de revenu « Revenu moyen supérieur » pour les années 2009 à 2014. 

<font color="#c00000">On peut maintenant prêts représenter graphiquement les données avec la commande ggplot</font>. 
<font color="#00b050">Le résultat est présenté dans la figure 1.16.</font> Nous avons presque obtenu la figure 1.15. Les personnes intéressées par les dernières étapes d'amélioration peuvent consulter le script 1.34 (wdi-ctryavg-beautify.R) dans l'annexe IV.

**Script 1.33: wdi-ctryavg.R**
<font color="#c00000"> # Note: run wdi-ctryinfo.R first to define "alldata"!</font>
 <font color="#c00000"># Summarize by country and year</font>
 avgdata <- alldata % %
 filter(income != "Aggregates") % %                                        # <font color="#7030a0">remove rows for aggregates</font>
 filter(income != "Not classified") % %                                    #<font color="#7030a0"> remove unclassified ctries</font>
 group_by(income, year) % %                                                  # <font color="#7030a0">group by income classification</font>
 summarize(LE_avg = mean(LE, na.rm=TRUE)) % %                # <font color="#7030a0">average by group</font>
 ungroup()                                                                               # <font color="#7030a0">remove grouping</font>

<font color="#c00000"> # First 6 rows:</font>
 tail(avgdata)
'# Output : a tibble: 6 x 3

<font color="#c00000"> # plot</font>
 ggplot(avgdata, aes(year, LE_avg, color=income)) +
 geom_line() +
 scale_color_grey()


# Statistiques descriptives

# Distributions discrètes : fréquences et tables de contingence
Soit un échantillon des variables aléatoires X et Y stocké dans les <font color="#00b0f0">vecteurs x et y</font>, respectivement. 

<font color="#00b0f0">Pour les variables discrètes, les statistiques les plus fondamentales sont les fréquences des résultats</font>. 
<font color="#00b050">La commande table(x) </font>donne un tableau des comptages (fréquences absolues : nbre d'éléments par critère).  
<font color="#00b050">table(x,y)</font> : 2 arg donne la<font color="#c00000"> table de contingence</font>, <font color="#7030a0"> nbre de chaque combinaison de résultats pour les variables x et y</font>. 
<font color="#00b050">prop.table(table(x))</font> donne les parts d'échantillon (%)  au lieu des comptages . 
	Pour les tables à double  dimensions (two-way tables) , on peut obtenir  :
	   <font color="#6425d0">l'overall sample share</font> : prop.table(table(x,y))
	   <font color="#6425d0">la share within x values</font> (% en lignes) : prop.table(table(x,y),margin=1)
	   <font color="#6425d0">la share within y </font>(% en colonnes) : prop.table(table(x,y),margin=2)

**A titre exemple, regardons data set affairs.dta.** 
Il contient <font color="#6425d0">deux variables que nous examinons dans Script 1.35</font> (Descr-Tables.R) pour montrer le fonctionnement des  commandes table et prop.table :
•	<font color="#6425d0">kids = 1 si le répondant a au moins un enfant</font>
•	<font color="#6425d0">ratemarr = évaluation de 1 à 5  de son propre mariage</font> (1=très malheureux à 5=très heureux)

**Output of Script 1.35: Descr-Tables.R**
 <font color="#c00000"># load data set</font>
 data(affairs, package="wooldridge")
<font color="#c00000"> # Generate "Factors" to attach labels</font>
 haskids <- factor(affairs$kids,labels=c("no","yes"))
 mlab <- c("very unhappy","unhappy","average","happy", "very happy")
 marriage <- factor(affairs$ratemarr, labels=mlab)
<font color="#c00000"> # Frequencies for having kids:</font>
 table(haskids)
<font color="#c00000"> # Marriage ratings (share):</font>
 prop.table(table(marriage))
 # <font color="#c00000">Contigency table: counts (display & store in var.)</font>
 (countstab <- table(marriage,haskids))
<font color="#c00000"> # Share within "marriage" (i.e. within a row):</font>
 prop.table(countstab, margin=1)
<font color="#c00000"> # Share within "haskids" (i.e. within a column):</font>
 prop.table(countstab, margin=2)

<font color="#00b0f0">Nous générons d'abord  des transformations factorielles (factor versions) des deux variables d'intérêt</font> : des tableaux avec des labels pertinentes au lieu de chiffres pour les résultats. <font color="#00b0f0">Ensuite, différentes tables et tableaux de contingences sont produits. </font>

Le tableau avec l'option margin = 1 nous indique que, par exemple, 81,25 % des personnes très malheureuses ont des enfants et seulement 58,6 % des répondants très heureux en ont. 

Il y a plusieurs façons de représenter (depict) graphiquement les informations dans ces tableaux. 

(a) pie (table (mariage), col=gray(seq(.2,1,.2))	
(b) Barplot (table (mariage),horiz=TRUE,las=1, main="Distribution of Happiness"
(c) Barplot (table, a des enfants, mariage),horiz=TRUE,las=1,legend=TRUE,	args.legend=c(x="bottomright"), main="Happiness by Kids")
(d) barplot(table(haskids,marriage), beside=TRUE,las=2,legend=TRUE, args.legend=c(x="top"))


# Distributions continues : histogramme et densité

Pour les variables continues, chaque observation a une valeur distincte. En pratique, les variables ayant de nombreuses (mais pas infiniment) de valeurs différentes peuvent être traitées comme continues. 
<font color="#c0504d">Puisque chaque valeur n'apparaît qu'une seule fois (ou très rarement) dans les données, les tables de fréquences ou les graphiques à barres ne sont pas utiles</font>. <font color="#00b0f0">À la place, les valeurs peuvent être regroupées en intervalles.</font> <font color="#00b050">La fréquence des valeurs dans ces intervalles peut alors être tabuée ou représentée dans un histogramme.</font>

Dans R, <font color="#00b0f0">la fonction hist(x, options) assigne des observations à des intervalles</font> qui peuvent être définis manuellement ou automatiquement choisis, et crée un histogramme qui trace (représente) les valeurs de x par rapport au nombre ou à la densité dans le bin correspondant. 
<font color="#00b0f0">Les options les plus pertinentes sont</font>
<font color="#00b050">breaks =</font>...: définir les limits d'intervalles (interval boundaries) :
        <font color="#00b050">no breaks</font> specified : laissons R choisir le nombre et la position
        <font color="#00b050">breaks=n</font> <font color="#c0504d">pour un scalaire n</font> : sélectionnez le nombre de bins, mais laissez R choisir la position.
        <font color="#00b050">breaks=v</font> <font color="#c0504d">pour un vecteur v</font> : fixer explicitement les frontières
	    <font color="#00b050">une fonction</font> du nom de l'algorithme pour choisir automatiquement les ruptures
<font color="#00b050">freq=FALSE</font> : ne pas utiliser le comptage mais la densité sur l'axe vertical. Option par défaut si les coupures ne sont pas espacées également.
<font color="#00b050">options générales pour des graphiques </font>comme <font color="#00b050">lwd</font> ou <font color="#00b050">ylim</font> mentionnés dans la Section 1.4.2 pour ajuster l'apparence.

<font color="#6425d0">Le data set CEOSAL1.dta contient des informations sur le salaire des PDG et d'autres informations</font>. Objectif: <font color="#c00000">représenter la répartition du rendement sur capitaux propres (ROE), en pourcentage. </font>

Script 1.36: Histogram.R
<font color="#c00000">'# Load data</font>
data(ceosal1, package="wooldridge")
<font color="#c00000">'# Extract ROE to single vector</font>
ROE <- ceosal1$roe
<font color="#c00000">'# Subfigure (a): histogram (counts)</font>
hist(ROE)
<font color="#c00000">'# Subfigure (b): histogram (densities, explicit breaks)</font>
hist(ROE, breaks=c(0,5,10,20,30,60) )

<font color="#00b050">Un kernel density plo</font>t (graphique de densité de grains) : <font color="#00b050">version sophistiquée d'un histogramme</font> : il est possible de créer un histogram bin (brique d'histogramme?) d'une certaine largeur, centré en un point arbitraire de x. Nous allons le faire pour de nombreux points et  tracer ces valeurs x par rapport aux densités résultantes. 
<font color="#245bdb">Ce graphique, ici, ne servira pas comme estimateur d'une distribution de population, mais plutôt comme alternative à un histogramme pour la caractérisation descriptive de la distribution de l'échantillon</font> (Cf. Silverman (1986)). 
<font color="#00b050">Dans R, générer un diagramme de densité du noyau est simple </font>: <font color="#c0504d">plot( density(x) )</font> choisira automatiquement les paramètres de l'algorithme appropriés aux data. Ces paramètres (comme le noyau et la bande passante)
peut être réglé manuellement. On peut aussi utiliser des options générales de plot.

<font color="#00b0f0">Le script 1.37 (KDensity.R) génère les Kernel Density Plots de la Figure 1.19</font>. Dans la sous-figure (b), un histogramme est superposé à un graphique de densité de noyau en utilisant lines au lieu de la  commande plot. Nous ajustons les limites Ylim de l'axe et augmentons la largeur de la ligne en utilisant lwd. 

**Script 1.37: KDensity.R**
<font color="#c0504d">'# Subfigure (c): kernel density estimate</font>
plot( density(ROE) )
'<font color="#c0504d"># Subfigure (d): overlay</font>
hist(ROE, freq=FALSE, ylim=c(0,.07))
lines( density(ROE), lwd=3 )

## Fonction de distribution cumulative empirique  (ECDF)
L'ECDF (Empirical Cumulative Distribution Function) est un <font color="#00b0f0">graphe de toutes les valeurs x d'une variable par rapport à la part (au %) d'observations dont la valeur est inférieure ou égale à x.</font> 
Une façon simple de tracer l'ECDF pour une variable x est  <font color="#00b050">plot (ecdf(x))</font>. 
Pour la variable ROE, l'ecdf créé par la commande plot(ecdf(ROE)) est présenté à la Figure 1.20.
<font color="#c00000">Ainsi, la valeur de l'ECDF pour un taux de ROE = 15,5 est de 0,5</font>. <font color="#00b0f0">La moitié de l'échantillon est inférieure ou égale à un ROE de 15,5 %. En d'autres termes : le ROE médian est de 15,5 %</font>.

# Statistiques fondamentales
Tableau 1.4. liste les fonctions pour calculer les statistiques descriptives les plus importantes.
![[../../zImages/Pasted image 20260111174913.png]]
<font color="#c0504d">La commande summary est générique</font>, elle accepte différents types d'objets et rapporte les informations résumées appropriées. Pour les vecteurs numériques, summary affiche la moyenne, la médiane, les quartiles et les valeurs extrêmes (cf. script 1.38) (Descr-Stats.R) 
<font color="#c0504d">summary(df)</font> affiche les statistiques résumées pour toutes les variables si df est une data frames. 
<font color="#c0504d">colSums, rowSums, colMeans et rowMeans</font> pour calculer toutes les moyennes des lignes ou colonnes de matrices ou de data frames, 

**Output of Script 1.38: Descr-Stats.R**
 data(ceosal1, package="wooldridge")
<font color="#c0504d"> # sample average:</font>
 mean(ceosal1$salary)
<font color="#c0504d"> # sample median:</font>
 median(ceosal1$salary)
<font color="#c0504d"> # standard deviation:</font>
 sd(ceosal1$salary)
<font color="#c0504d"> # summary information:</font>
 summary(ceosal1$salary)
<font color="#a5a5a5"> # correlation with ROE:</font>
 cor(ceosal1$ salary, ceosal1$roe)

<font color="#00b050">Une box plot</font> affiche graphiquement 
- la médiane (la ligne grasse), 
- le quartile supérieur et inférieur (la boîte) 
- ainsi que les points extrêmes. 
<font color="#00b050">Exemple de box plot</font> présenté figure 1.21 : 
- 50 % des observations se situent dans l'intervalle couvert par la boîte, 25 % sont au-dessus et 25 % en dessous. 
- Les points extrêmes sont indiqués par les " whiskers " 
- et les valeurs aberrantes sont imprimées sous forme de points séparés. 

<font color="#8064a2">La définition d'un cas atypique (outlier)  est arbitraire</font>. <font color="#c0504d">Ici, une valeur est considérée comme exception si elle est plus éloignée de la boîte que 1,5 fois la plage interquartile (c'est-à-dire la hauteur/largeur de la boîte).</font>

Dans R, les diagrammes de boxplot sont générés en utilisant la commande boxplot
**(1.21 a) Box plot horizontale :** Boxplot(ROE, horizontal=TRUE)
**(1.21 b) Box plot verticale**
ceosal1$consprod
boxplot(ROE~df$consprod)

La figure 1.21(b) montre comment produire différents graphiques par sous-groupe défini par une seconde variable. La variable consprod à partir du data set ceosal1 est égale à 1 si l'entreprise est dans le secteur des produits grand public et à 0 sinon. 

# Distributions de probabilité
**NB :** <font color="#c0504d">L'annexe B de Wooldridge (2019) présente les concepts de variables aléatoires et leurs distributions de probabilité. </font>
<font color="#00b0f0">Le tableau 1.5 (cf p(56 du pdf) présente les principales distributions de probabilités</font> :<font color="#00b050"> les commandes R pour leur (pdf ou pmf), leur cdf, la valeur du quantile, la génération des nombres aléatoires, :</font>
**Table 1.5. R functions for statistical distributions**
![[../../zImages/Pasted image 20260112064403.png]]

## 5 Distributions discrètes : BBGHP
Les variables aléatoires discrètes <font color="#c0504d">ne peuvent prendre qu'un ensemble fini (ou " infini dénombrable ") de valeurs.</font> 
<font color="#00b0f0">Leur pmf f (x) = P(X = x)</font> <font color="#00b050">donne la probabilité qu'elle prenne une valeur donnée x. </font>
<font color="#c0504d">Les plus 5 importantes distributions sont</font> : Bernoulli, Binomiale, Hypergéométrique, Poisson et Géométrique.
**Exemple de Distribution binomiale :**  
- soit X le nombre de boules blanches que l'on obtient en tirant avec remplacement 10 boules d'une urne contenant 20 % de boules blanches. 
- Alors X possède la distribution binomiale avec les paramètres n = 10 et p = 20 % = 0,2. 
La probabilité d'obtenir  x ∈ {0, 1, . . . , 10} boules blanches pour cette distribution est : cf la formule.
Par exemple, la probabilité d'obtenir exactement x = 2 boules blanches est f (2) = ( formule)  = 0,302. 
On peut utiliser cette formule avec R pour calculer le résultat :
<font color="#7030a0">Pedestrian approach </font>: choose(10,2) * 0.2^2 * 0.8^8
<font color="#c00000">On peut utiliser la fonction interne (built-in function) pour Distribution binomiale de la table 1.5</font> : <font color="#00b0f0">dbinom(x.n,p)</font>
<font color="#00b0f0">Built-in function:</font> <font color="#00b050">dbinom(2,10,0.2) </font> : <font color="#7030a0">prob de tirer 2 bb quand on tire avec remise 10 b d'une urne contenant 10% de bb</font>

Nous pouvons également <font color="#00b0f0">donner des vecteurs comme arguments à dbinom(x,n,p) </font>et <font color="#00b050">obtenir les résultats sous forme de vecteur. </font>
<font color="#00b0f0">Le script 1.39 (PMF-exemple.R)</font> 
- calcule la pmf pour notre exemple à toutes les valeurs possibles de x (0 à 10). 
- Il affiche le tableau des probabilités et crée un graphique à barres de ces probabilités, figure 1.22(a).  
- L'option = " h " du graphique de commande  dessine des lignes verticales au lieu de points.

**Script 1.39: PMF-example.R**
<font color="#c0504d"> # Values for x: all between 0 and 10</font>
 x <- seq(0,10)
<font color="#c0504d"> # pmf for all these values</font>
 fx <- dbinom(x, 10, 0.2)
<font color="#c0504d"> # Table(matrix) of values:</font>
 cbind(x, fx)
<font color="#c0504d"> # Plot</font>
 plot(x, fx, type="h")


## Distributions continues (NTFULEX)
<font color="#c0504d">Exemple de distributions continues</font> : <font color="#00b0f0">normale, t, F, uniforme, logistique, exponentielle, χ2 . </font>
Leurs fonctions de densité de probabilité f (x) peuvent être implémentées pour <font color="#c0504d">leur représentation graphique à l'aide de la commande curve </font> (voir Section 1.4). La figure 1.22(b) montre la PDF de la distribution normale standard, créée avec curve ( dnorm(x), - 4,4 ).
 
## Fonction de distribution cumulative (CDF)
<font color="#7030a0">Pour toutes les distributions, </font> 
- <font color="#c0504d">cdf F(x) = P(X⩽x)</font> :  <font color="#00b0f0">probabilité que la variable aléatoire X prenne une valeur d'au plus x. </font>
- <font color="#c0504d">P(a < X< b) = F(b)-F(a)</font> : probabilité que X  prenne une valeur située entre deux valeurs a et b.

Dans notre exemple, <font color="#00b0f0">la probabilité d'obtenir 3 boules blanches ou moins est F(3)</font> en utilisant l<font color="#c0504d">a cdf de la distribution binomiale, elle est de 87,9 % :</font>
pbinom(3, 10, 0,2)
[1] 0.879126

<font color="#00b0f0">La probabilité qu'une variable aléatoire normale standard prenne une valeur comprise entre −1,96  et 1,96 est 95%</font>
 pnom(1,96) - pnom(-1,96)
[1] 0.9500042

## Wooldridge, Exemple B.6 : Probabilités pour une variable aléatoire normal
<font color="#7030a0">X ∼ Normal(4, 9)</font> et <font color="#00b050">on veut calculer</font> P(2 < X ≤ 6). 

<font color="#00b0f0">Réécrire le problème</font> dans les termes d'une distribution<font color="#c0504d"> normale standard</font> : P(2 < X ≤ 6) = Φ( 2/3 ) − Φ(− 2/3 ).
 <font color="#c0504d"># Using the transformation:</font>
 pnorm(2/3) - pnorm(-2/3)
[1] 0.4950149

Ou <font color="#00b0f0">utiliser directement </font><font color="#c0504d">la non standard normale</font> distribution : P(|X| >  2) = P(X>2) +P(X<-2) = [1 − P(X ≤ 2)] + P(X < −2)
Nb : le troisième argument pour la distribution normale n'est pas la variance σ2 = 9 mais l'écart-type σ = 3. 

Rappel : <font color="#7030a0">X ∼ Normal(4, 9)</font> et <font color="#00b050">on veut calculer</font> P(2 < X ≤ 6).
<font color="#c0504d"> # Working directly with the distribution of X:</font>
 pnorm(6,4,3) - pnorm(2,4,3) # <font color="#4bacc6">6:max; 2:min; 4:μ;  3:σ</font>
[1] 0.4950149

Même approche pour le second probléme : P(|X| >  2) = P(X>2) +P(X<-2) = [1 − P(X ≤ 2)] + P(X < −2)
 1 - pnorm(2,4,3) + pnorm(-2,4,3) # <font color="#c0504d">la symétrie fait que </font>P(X>2) = 1-P(X<2)
[1] 0.7702576

<font color="#00b0f0">Le graphe de la cdf est en escalier pour les distributions discrètes,</font> <font color="#c0504d">il sera mieux généré en utilisant l'option type ="s " de plot</font> (voir la section 1.4.)

'#<font color="#7030a0">Graphique (exemple de l'urne ) de la cdf d'une Dist discrète (vecteur : -1 à 10)</font> : je ne comprends pas le -1
x <- seq(-1,10)
Fx <- pbinom(x, 10, 0.2)
plot(x, Fx, type="s")

<font color="#00b0f0">La cdf d'une  distribution continue peut être tracée à l'aide de la  commande curve.</font> La cdf en forme de S de la distribution normale est illustré à la Figure 1.23(b). Elle a été générée par :
curve ( pnorm(x), -4,4 ).

## Fonction quantile
<font color="#00b050">Le q-quantile x[q] d'une variable aléatoire est sa valeur dont la probabilité cumulée (probabilité d'obtenir une valeur  x ⩽ x[q]) est q.</font> Ces valeurs (les q-quantiles) sont importantes pour trouver les valeurs critiques des statistiques de test.

<font color="#c0504d">Exemple</font> : soit X une Distribution <u>normale standard</u>, 
- le 0,975-quantile de cette distribution est x[0,975] = 1,96. 
- Ainsi, la probabilité d'échantillonner une valeur inférieure ou égale à 1,96 est de 97,5 % :
		 qnorm(0.975)
		[1] 1.959964

## Tirages aléatoires à partir de distributions de probabilité
Random Draws from Probability Distributions.
<font color="#00b0f0">On peut simuler des résultats aléatoires en générant un échantillon d'une variable aléatoire qui suit une distribution donnée. </font>
<font color="#c0504d">Une machine déterministe comme un ordinateur ne peut jamais produire de résultats véritablement aléatoires</font>, <font color="#7030a0">les nombres générés sont dits pseudo-aléatoires.</font> Mais pour notre objectif, il suffit que les échantillons générés se comportent comme de vrais nombres aléatoires. 
<font color="#00b0f0">Nous présentons ici la mécanique de génération de nombres pseudo-aléatoire.</font> 

<font color="#00b050">Le Tableau 1.5 (p56 du pdf) :</font> <font color="#00b0f0">commandes R pour extraire un échantillon aléatoire suivant les distributions les plus importantes</font>. 

Pour simuler le résultat d'un lancer de 10 pièces équitables (Bernoulli)  
<font color="#00b050">Nous pouvons utiliser une distribution de Bernoulli </font>
- pour tirer un échantillon de taille n = 10 
- avec paramètre p = 1/2 . 
- Chacun des 10 nombres générés aura la valeur 1 avec une probabilité de p=0.5 et la valeur 0 avec une probabilité de 1-p = 0.5.
<font color="#c0504d">Formule</font> : rbinom(x, <font color="#00b050">1</font>, p) car Bernoulli. La formule Binomiale : rbinom(x,<font color="#00b050">n</font>,p)),
rbinom(10,1,0.5)    # <font color="#8064a2">le r pour signifier random, un tirage aléatoire.</font>
[1] 1 1 0 0 0 0 1 0 1 0
*Attention à ne pas confondre avec Binomiale : rbinom(1,10,0.5) donne comme résultat : 4.*

<font color="#6425d0">Le résultat de la simulation suivant la Distribution Bernoulli a le même comportement que si nous avions jeté 10 fois une pièce (flipped a coin) et enregistré les heads=1 et les tails=0.</font> Ce qui n'est pas le cas avec la Distribution binomiale.

<font color="#00b050">Faire des tirages à partir de la distribution normale standard est tout aussi simple :</font>
rnorm(10)
[1] 0.83446013 1.31241551 2.50264541 1.16823174 -0.42616558
[6] -0.99612975 -1.11394990 -0.05573154 1.17443240 1.05321861
<font color="#00b0f0">Le pourquoi des chiffres</font> : rnorm(10) utilise la Dist normale standard dont la moyenne est 0, et l'e.t=1. Cela fait que 68% des valeurs $\in$ [-1,1], 95% des valeurs $\in$ [-2,2] et 99% des valeurs $\in$ [-3,3]. Mais théoriquement le résultat $\in [-\infty,\infty]$

<font color="#c0504d">La reproductibilité des résultats est nécessaire pour travailler avec des échantillons aléatoires</font>. Les échantillons générés à partir des mêmes paramètres sont différents (car aléatoires). Il est possible de surmonter ce problème en exploitant la manière dont les nombres aléatoires sont réellement générés, ce qui en fait des nombres pseudo-aléatoires. 
<font color="#00b050">Nous obtiendrons toujours la même séquence de nombres (le même échantillon)</font> <font color="#00b0f0">si nous réinitialisons le générateur de nombres aléatoires à un état spécifique ("seed"). </font>
Dans R, cela se fait avec<font color="#00b050"> set.seed(number)</font>, où <font color="#7030a0">number est un nbre arbitraire qui définit l'état initial sans autre signification : </font>
-	Si <font color="#00b0f0">nous définissons seed</font> à un nombre arbitraire, 
-	que nous <font color="#00b0f0">prenons un échantillon</font>, 
-	que nous <font color="#00b0f0">réinitialisons le seed</font> au même état 
-	et que nous en <font color="#00b0f0">prenons un autre échantillon</font>, 
-  <font color="#00b050">Alors, les deux échantillons seront identiques. </font>

<font color="#7030a0">De même,</font> <font color="#c0504d">si 2 personnes utilisent le même seed pour tirer un échantillon</font>, <font color="#00b050">ce dernier sera le même pour les 2 personnes.</font>  
Le script 1.40 (Random-Numbers.R) montre le fonctionnement de set.seed.

**Script 1.40: Random-Numbers.R**
<font color="#c0504d">'# Sample from a standard normal RV with sample size n=5:</font>
rnorm(5)    # tirer échantillon de 5 nombres aléatoires suivant la loi normale standard
<font color="#c0504d">'# A different sample from the same distribution:</font>
rnorm(5)    # autre extraction de 5 nbres aléatoires : résultat différent
<font color="#c0504d">'# Set the seed of the random number generator and take two samples:</font>
set.seed(6254137)   # inialiser le seed
rnorm(5)                  # extraction1 : 5 nbre aléatoires suivant la loi normale standard
rnorm(5)                  # extraction2 :  idem, mais résultat différent
<font color="#c0504d">'# Reset the seed to the same value to get the same samples again:</font>
set.seed(6254137)   # reinitialiser le seed
rnorm(5)                  # extraction de 5 nombres : les mêmes que extraction1
rnorm(5)                  # extraction de 5 nombres : les mêmes que extraction2

## Intervalles de confiance et inférence statistique
Wooldridge (2019) propose un aperçu concis de l'échantillonnage, de l'estimation et des tests de base. 

### Intervalles de confiance
<font color="#00b0f0">Les intervalles de confiance (IC) couvrent le véritable paramètre de population d'intérêt avec une probabilité donnée, par exemple 95 %.</font> <font color="#00b050">Plus clairement : pour 95 % de tous les échantillons, l'IC implicite inclut le paramètre de population.</font>

Pour une population normale dont la μ moyenne  et la variance σ2 sont inconnues, l'IC 100(1-α)% pour μ est :
 $\left[\bar{y}-c_{\frac{\alpha}{2}}\cdot s e(\bar{y}),\quad\bar{y}+c_{\frac{\alpha}{2}}\cdot s e(\bar{y})\right]$
 
où $\bar y$  est la moyenne de l'échantillon, se($\bar y$ ̄) = (Racine de s)/n est l'erreur standard de $\bar y$ (s étant l'écart-type de l'échantillon de y), n est la taille de l'échantillon et cα/2,  le  quantile (1 – α) de la  distribution t_(n−1). 
Pour obtenir l'IC à 95 % (α = 5 %), nous avons besoin de c_0,025 , qui est   le quantile de 0,975 ou 97,5e quantile.
Nous savons déjà comment calculer tous ces ingrédients. 
<font color="#00b0f0">Si notre échantillon est stocké sous forme de vecteur y,</font> <font color="#c0504d">le code suivant les calculera ainsi que l'intervalle de confiance</font> :
$\left[\bar{y}-c_{\frac{\alpha}{2}}\cdot s e(\bar{y}),\quad\bar{y}+c_{\frac{\alpha}{2}}\cdot s e(\bar{y})\right]$

```
$\bar y$ <-  mean(y)
n <- length(y)
s <- sd(y)
se <- s/sqrt(n)
c <- qt(.975, n-1)
CI <- c( $\bar y$ - c*se, $\bar y$ + c*se )
```

<font color="#00b050">Une méthode plus pratique pour calculer l'IC, avec  le test t correspondant est proposée dans Section 1.8.4.</font>
Dans  la section 1.10.3, nous calculerons des intervalles de confiance dans une expérience de simulation afin de comprendre la signification des intervalles ce confidents.

## Wooldridge, Exemple C.2 : Effet des subventions de formation prof sur la productivité des travailleurs  
Analyse des <font color="#c0504d">taux de rebut des entreprises ayant reçu une subvention de formation professionnelle en 1988. </font>
- Les taux de rebut pour 1987 et 1988 sont saisis au début du script 1.41 (Exemple-C-2.R). 
- Nous sommes intéressés par la variation entre les 2 années. 
- Le calcul de la moyenne et de l'intervalle de confiance sont effectués comme montré ci-dessous. 

**Script 1.41: Example-C-2.R**
<font color="#c0504d"> # Manually enter raw data from Wooldridge, Table C.3:</font> 
 SR87<-c(10,1,6,.45,1.25,1.3,1.06,3,8.18,1.67,.98,1,.45,
                            5.03,8,9,18,.28,7,3.97)
 SR88<-c(3,1,5,.5,1.54,1.5,.8,2,.67,1.17,.51,.5,.61,6.7,
                              4,7,19,.2,5,3.83)     # <font color="#7030a0">taux de rebuts</font>
<font color="#c0504d"> # Calculate Change (the parentheses just display the results):</font>
 (Change <- SR88 - SR87)  # <font color="#7030a0">variation des taux de rebut</font>
<font color="#c0504d"> # Ingredients to CI formula</font>
 (avgCh<- mean(Change))   # <font color="#7030a0">calcul de la moyenne</font>
 (n <- length(Change))
 (sdCh <- sd(Change))
 (se <- sdCh/sqrt(n))
 (c <- qt(.975, n-1))
<font color="#c0504d"> # Confidence interval de la moyenne:</font>
 c( avgCh - c*se, avgCh + c*se )
[1] -2.27803369 -0.03096631  #<font color="#7030a0"> Intervalle de confiance de la variation moyenne du taux de rebut</font>

## Wooldridge, Exemple C.3 : Discrimination raciale dans l'embaucheC.3
Nous étudions la discrimination raciale en utilisant le<font color="#c0504d"> data set AUDIT.dta. </font>
<font color="#00b050">La variable y</font> : <font color="#c0504d">différence de taux d'embauche entre les candidats noirs et blancs ayant le même CV.</font> 

**Script 1.42: Example-C-3.R**
 data(audit, package="wooldridge")
<font color="#c0504d"> # Ingredients to CI formula</font>
 (avgy<- mean(audit$y))
 (n <- length(audit$y))
 (sdy <- sd(audit$y))
 (se <- sdy/sqrt(n))
 (c <- qnorm(.975))
<font color="#c0504d"> # 95% Confidence interval:</font>
 avgy + c * c(-se,+se)
<font color="#c0504d"> # 99% Confidence interval:</font>
 avgy + qnorm(.995) * c(-se,+se)
[1] -0.21275051 -0.05280966

## Tests t 
Équation C.35 donne la formule pour la  statistique du test t permettant de tester une hypothèse sur μ la moyenne  d'une variable aléatoire Y normalement distribuée . 
<font color="#c0504d">Étant donné l'hypothèse nulle H0 :</font> μ = $μ_0$,      
t=  $\frac {\bar y – y_0 }{se\bar y}$
Étant donné les calculs présentés à la Section 1.8.1., t <font color="#00b0f0">pour l'hypothèse nulle H0 : μ = 1</font> serait 
t <- ($\bar y$-1) / se

<font color="#c00000">La valeur critique de cette statistique de test dépend du fait que le test soit unilatéral ou bilatéral.</font>
La valeur nécessaire pour un test bilatéral ($c_{α/2}$) a déjà été calculée pour l'intervalle de confiance ; les autres valeurs peuvent être générées en conséquence. 
Les valeurs pour différents degrés de liberté (n − 1) et seuils de signification (α) sont indiquées dans Wooldridge (2019, tableau G.2). 
<font color="#00b0f0">Le script 1.43 (Critical-Values-t.R) montre comment calculer notre propre tableau de valeurs critiques pour l'exemple de 19 degrés de liberté.</font>

**Script 1.43: Critical-Values-t.R**
<font color="#c0504d">'# degrees of freedom = n-1:</font>
df <- 19
<font color="#c0504d">'# significance levels:</font>
alpha.one.tailed = c(0.1, 0.05, 0.025, 0.01, 0.005, .001)
alpha.two.tailed = alpha.one.tailed * 2
<font color="#c0504d">'# critical values & table:</font>
CV <- qt(1 - alpha.one.tailed, df)
cbind(alpha.one.tailed, alpha.two.tailed, CV)

## Wooldridge, Exemple C.5 : Discrimination raciale dans l'embauche
Nous poursuivons<font color="#c0504d"> l'exemple C.3 (discrimination à l'embauche)</font> et réalisons  
- un <font color="#00b0f0">test t unilatéral de l'hypothèse nulle H0</font> : μ = 0 <font color="#00b0f0">contre</font> H1 : μ < 0 <font color="#00b0f0">pour le même échantillon</font>. 
Nous devons donc exécuter préalablement le script Example-C-3.R pour réutiliser les variables avgy, se et n. 

<font color="#00b0f0">L'Output indique que la statistique du test t est égale à 4,27</font>.  
- <font color="#00b050">Une telle valeur est plus faible que le négatif de la valeur critique pour tout niveau de signification sensé.</font>
- Par conséquent, <font color="#00b0f0">nous rejetons H0 : μ = 0 pour ce test unilatéral</font>, voir Wooldridge (2019, Équation C.38).

**Script 1.44: Example-C-5.R**
<font color="#c0504d"> # Note: we reuse variables from Example-C-3.R. It has to be run first!</font>
<font color="#c0504d"> # t statistic for H0: mu=0:</font>
 (t <- avgy/se)
 <font color="#c0504d"># Critical values for t distribution with n-1=240 d.f.:</font>
 alpha.one.tailed = c(0.1, 0.05, 0.025, 0.01, 0.005, .001)
 CV <- qt(1 - alpha.one.tailed, n-1)
 cbind(alpha.one.tailed, CV)

## p Values

<font color="#00b0f0">Le p-value d'un test est la probabilité qu'un autre échantillon aléatoire produirait la même ou encore plus extrême valeur de la statistique du test</font> (sous les hyp nécessaires pour dériver la distribution de la statistique de test) . 
<font color="#00b050">L'avantage de la p-value est qu'elle est pratique à utiliser</font>. 
- nous comparons directement p avec α. 
- au lieu de devoir comparer la statistique de test avec les valeurs critiques impliquées par le niveau de signification α. 

<font color="#00b0f0">Pour le  test t bilatéral (two sided test t), la formule de calcul de la valeur p </font>est donnée dans Wooldridge (2019, Équation C.42) :  p = 2 · P(T(n−1)  |t|) = 2 · 1 – Ft(n−1) (|t|)  ,   (1.4)
où Ft(n−1) (·) est la cdf de la  distribution t(n−1) que nous savons calculer à partir du tableau 1.5. 

De même, un test unilatéral rejette l'hypothèse nulle uniquement si la valeur de l'estimation est « trop élevée » ou "trop basse" par rapport à l'hypothèse nulle. Les p-value pour ce type de tests sont :
**p=**
 $\begin{array}{l l}{{\mathrm{P}(T_{n-1}<t)=F_{t_{n-1}}(t)}}&{{\mathrm{for}\ H_{1}:\mu<\mu_{0}}}\\ {{\mathrm{P}(T_{n-1}>t)=1-F_{t_{n-1}}(t)}}&{{\mathrm{for}\ H_{1}:\mu>\mu_{0}}}\end{array}$
 
Etant donné que nous avons déjà calculé la  statistique t ci-dessus, la  valeur p serait simplement l'une des expressions suivantes, selon le type de l'hypothèse nulle :
p <- 2 * ( 1 - pt(abs(t), n-1) ): Test t bilatéral
p <- pt(t, n-1) test t unilatéral à gauche ('less')
p <- 1 - pt(t, n-1) test t unilatéral à droite ('greater)

## Wooldridge, Exemple C.6 : Effet des subventions de formation prof sur la productivité des travailleurs
Suite de l'exemple C.2.  Avant d' exécuter le script 1.41 (Example-C-2.R), il faut exécuter Example-C-2.R afin de pouvoir réutiliser les variables avgCh et se. 
Nous testons H0 : μ = 0 contre H1 : μ < 0. 
La  t statistique pour ce test unilatéral est de 2,15. La p-value pour ce test unilatéral est d'environ 0,022.

**Output of Script 1.45: Example-C-6.R**
<font color="#c0504d"> # Note: we reuse variables from Example-C-2.R. It has to be run first!</font>
<font color="#c0504d"> # t statistic for H0: mu=0:</font>
 (t <- avgCh/se)
<font color="#c0504d"> # p value</font>
 (p <- pt(t,n-1))

**Wooldridge, Exemple C.7 : Discrimination raciale dans l'embauche**
Dans l'exemple C.5, nous avons trouvé que la statistique t pour H0 : μ = 0 contre H1 : μ < 0 était de t = −4,276816. 
La p-valeur est 1,369271e-05, notation scientifique de 1,369271 × 10−5 = 0,00001369271. La p-valeur est donc d'environ 0,0014 %, bien inférieure à tout seuil de signification raisonnable. 
Nous rejetons l'hypothèse nulle d'absence de discrimination.

**Output of Script 1.46: Example-C-7.R**
 <font color="#c0504d"># t statistic for H0: mu=0:</font>
 t <- -4.276816
<font color="#c0504d"> # p value</font>
 (p <- pt(t,240))

## Calculs automatiques
<font color="#00b0f0">R dispose d'un grand nombre de commandes qui effectuent automatiquement tous types de calculs pour différents types de problèmes d'estimation et de test.</font>
Concernant le test d'hypothèse sur la moyenne de la population, la commande t.test fournit automatiquement, pour différentes hypothèses :
-	the sample average $\bar Y$
-	the sample size n
-	the confidence interval (95% by default)
-	the t statistic
-	the p value

<font color="#00b0f0">Nous obtenons donc toutes les informations que nous avions calculées précédemment en plusieurs étapes avec un seul appel de cette commande. </font>
<font color="#00b050">Avec le vecteur y contenant les données de l'échantillon, on peut simplement appeler</font>
t.test(y)

Cela calculerait implicitement les résultats pertinents pour le test bilatéral de H0 : $μ_y = μ_0$, contre H1 : $μ_y ≠ μ_0$, où $μ_0$ = 0 par défaut. L'IC à 95 % est rapporté. 

<font color="#00b0f0">Nous pouvons choisir différents tests grâce aux options</font>
•	alternative="greater " pour H0 : $μ_y = μ_0$, H1 : $μ_y > μ_0$
•	alternative="less " pour H0 :$μ_y = μ_0$, H1 : $μ_y < μ_0$
•	mu = value  pour définir μ0 =value au lieu de μ_0 = 0
•	pour définir le niveau de confiance à valeur·100 % au lieu de conf.level=0,95
Exemple complet : tester H0 : $μ_y$ = 5 contre l'alternative unilatérale H1 : $μ_y > 5$ et obtenir un IC à 99 %. La commande serait :
t.test(y, mu=5, alternative="greater", conf.level=0.99)

**Exemples C.2 – C.7 revisités**
Le script 1.47 (Examples-C2-C6.R) reproduit les mêmes résultats que ceux déjà présentés dans Examples
C.2 et C.6 en utilisant l'appel de t.test. 
Le script 1.48 (Exemples-C3-C5-C7.R) fait de même pour les résultats des exemples C.3, C.5 et C.7.

**Script 1.47: Examples-C2-C6.R**
<font color="#c0504d"> # data for the scrap rates examples:</font>
 SR87<-c(10,1,6,.45,1.25,1.3,1.06,3,8.18,1.67,.98,1,.45,5.03,8,9,18,.28, 7,3.97)
 SR88<-c(3,1,5,.5,1.54,1.5,.8,2,.67,1.17,.51,.5,.61,6.7,4,7,19,.2,5,3.83)
 Change <- SR88 - SR87
<font color="#c0504d"> # Example C.2: two-sided CI</font>
 t.test(Change)
<font color="#c0504d"> # Example C.6: 1-sided test:</font>
 t.test(Change, alternative="less")

**Output of Script 1.48: Examples-C3-C5-C7.R**
 data(audit, package=’wooldridge’)
<font color="#c0504d"> # Example C.3: two-sided CI</font>
 t.test(audit$y)
<font color="#c0504d"> # Examples C.5 & C.7: 1-sided test:</font>
 t.test(audit$y, alternative="less")

<font color="#00b0f0">La commande t.test est notre premier exemple de fonction renvoyant list. </font>
Les résultats peuvent être stockés dans un objet pour une utilisation ultérieure.  La section 1.2.6 décrit le fonctionnement général de ce type d'objet. 
<font color="#c0504d">Si nous stockons les résultats, par exemple avec</font> testres <- t.test(...), <font color="#00b050">l'objet testres va contenir toutes les informations pertinentes concernant les résultats du test. </font>
Comme pour une liste classique, <font color="#00b0f0">les noms de tous ses composants peuvent être affichés avec names(testres)</font>. 
<font color="#c0504d">Ces noms incluent </font>: <font color="#00b050">statistic</font> (valeur de la statistique de test), <font color="#00b050">p.value</font> (valeur de la p-valeur du test) et <font color="#00b050">conf.int</font> (intervalle de confiance). 
<font color="#7030a0">Un composant, par exemple p.value, est accessible via testres$p.value. </font>

Le script 1.49 (Test-Results-List.R) illustre cela pour le test de l'exemple C.3.

**Script 1.49: Test-Results-List.R**
 data(audit, package=’wooldridge’)
 <font color="#c0504d"># store test results as a list "testres"</font>
 testres <- t.test(audit$y)
<font color="#c0504d"> # print results:</font>
 testres
<font color="#c0504d"> # component names: which results can be accessed?</font>
 names(testres)
<font color="#c0504d"> # p-value</font>
 testres$p.value

# R plus avancé 

## Exécution conditionnelle
<font color="#00b0f0">Pour qu'une parties de notre code ne soit exécutée que sous certaines conditions, on peut insérer une instruction if : </font>
if (condition) expression1 else expression2

<font color="#6425d0">La condition doit être une valeur logique</font> (TRUE ou FALSE). 
- Si c'est TRUE, alors expression1 est exécuté, 
- sinon expression2 qui peut également être omise. 
Un exemple simple serait :
if (p<=0.05) decision<-"reject H0!" else decision<-"don’t reject H0!"

L'objet character `décision` prendra la valeur respective selon la valeur du scalaire numérique p. 

<font color="#00b0f0">Si nous voulons exécuter conditionnellement plusieurs lignes de code</font>. <font color="#00b050">Cela peut être réalisé en regroupant les expressions entre crochets {...}. </font>
<font color="#c0504d">L'instruction else (si elle est utilisée) doit suivre sur la même ligne que le crochet de clôture de l'instruction if. </font>
if (condition) {
	[several...
	...lines...
	... of code]
} else {
	[different...
	...lines...
	... of code]
}

## Boucles (loops)
Pour exécuter de manière répétée une expression entre accolades {...}, différents types de boucles sont disponibles. La boucle « for » en est un exemple. 


La variable de loop loopvar prendra la valeur de chaque élément de vector, l'un après l'autre. Pour chacun de ces éléments, [some commands] sont exécutées. Souvent, vector est une séquence telle 1:100.
Un exemple absurde qui combine les boucles for avec une instruction if est le suivant :
for (i in 1:6) {
      if (i < 4) {
         print(i^3)
    }   else  {
       print(i ^ 2)
   }
}

La  commande print est nécessaires pour imprimer tout résultat dans les expressions groupées par des crochets. 
Autres expression de boucles : look up commands like repeat, while, replicate, apply or lapply

## Fonctions
Les fonctions sont des types particuliers d'objets dans R. 
Il existe de nombreuses fonctions prédéfinies. Les packages offrent plus encore de fonctions pour étendre les capacités de R. 
<font color="#00b0f0">On peut définir notre propre fonction. </font>
<font color="#00b050">La commande function (arg1, arg2,...) définit une nouvelle fonction qui accepte les arguments arg1, arg2,. . . </font>
La définition de la fonction suit un <font color="#c00000">nombre arbitraire de lignes de code enfermées entre crochets en spirale.</font> 
La commande <font color="#c00000">return(stuff) signifie que stuff doit être retourné à la suite de l'appel de fonction</font>.  

Par exemple,  <font color="#00b0f0">définir la fonction mysqrt qui attend un argument interne nommé x</font> : 
mysqrt <- function(x) <font color="#c0504d">{</font> 
  if(x>=0)<font color="#00b0f0">{</font>
return(sqrt(x))
<font color="#00b0f0">}</font> else<font color="#00b050"> {</font>
return (« Idiot ! »)
<font color="#00b050">}</font>
<font color="#c0504d">}</font>
<font color="#7030a0">rem hr : 3 doubles crochets : ceux qui enferment le corps de la fonction, ceux qui suivent if, ceux qui suit else.</font>

<font color="#00b0f0">Une fois la définition de fonction exécutée, mysqrt est connu du système et peut être exécutée c toute fonction:</font>
 mysqrt(4)
[1] 2
 mysqrt(-1)
[1] "You fool!"

**Perspectives (outlook)**

L' optimisation de la vitesse de calcul est un autre sujet avancé. Comme la plupart des autres logiciels utilisés pour l'économétrie, R est un langage interprété. Un inconvénient par rapport aux langages compilés comme C++ ou Fortran est que la vitesse d'exécution pour les tâches à forte intensité de calcul est plus faible. 

# Monte Carlo Simulation
- <font color="#c0504d">Dans les applications réelles,</font> nous disposons généralement d'un data set correspondant à un échantillon aléatoire issu d'une certaine population. <font color="#c0504d">Nous ne connaissons pas les paramètres de la population et utilisons l'échantillon pour les estimer.</font>
- <font color="#6425d0">Lorsque nous générons un échantillon à l'aide d'un programme informatique,</font>  <font color="#00b0f0">nous connaissons les paramètres de la population puisque nous avons dû les choisir pour effectuer les tirages aléatoires. </font>
- <font color="#00b050">Il est possible d'appliquer ces mêmes estimateurs (paramètres) à cet échantillon artificiel pour estimer les paramètres de la population.</font> 
-<font color="#c00000"> Les tâches seraient : </font>
	- (1) <font color="#00b0f0">Sélectionner une distribution de population</font> <font color="#c0504d">et ses paramètres</font>. 
	- (2) <font color="#00b0f0">Générer un échantillon</font> à partir de cette distribution. 
	- (3) Utiliser l'échantillon pour<font color="#00b0f0"> estimer les paramètres de la population</font>.
Nous obtenons une estimation "bruyante" de quelque chose que nous connaissons précisément auparavant.  Ce genre d'analyse a du sens :<font color="#c0504d"> parce que nous estimons quelque chose que nous connaissons réellement</font>, <font color="#00b050">nous sommes capables d'étudier le comportement de notre estimateur.</font>

Dans la recherche de pointe, ce procédé est largement utilisé car il est souvent le seul moyen de connaître les caractéristiques importantes des estimateurs et des tests statistiques. <font color="#00b050">Ce type d'analyses est nommé simulation de Monte Carlo </font><font color="#8064a2">en référence au " jeu " impliqué dans la génération d'échantillons aléatoires.</font>

## Propriétés finies des estimateurs dans l'échantillon
Simulons une situation dans laquelle <font color="#00b0f0">nous voulons estimer, pour une population, la moyenne μ  d'une variable aléatoire normalement distribuée Y ∼ Normal(μ, σ2)</font>	(1.6)
<font color="#f79646">Nous prélevons de cette population normalement distribuée un échantillon de taille n.</font> <font color="#6425d0">L'estimateur évident pour la moyenne de la population serait la Moyenne d'échantillon </font>$\bar Y$.	<font color="#c00000">Mais quelles sont les propriétés de cet estimateur ? </font>

<font color="#00b050">La simulation permet de vérifier que</font> <font color="#00b0f0">la distribution d'échantillonnage de</font> $\bar Y$  <font color="#00b0f0">est</font> $\bar y$ ∼ Normal(μ, σ2/n)

**Le script 1.50 (Simule-Estimate.R) montre une expérience de simulation en action :** 
-	fixer la graine (seed) pour assurer la reproductibilité 
-   tirer de la distribution normale de la pop (paramètres μ = 10 et σ = 2)) un échantillon de taille n = 100
-	calculer la moyenne de l'échantillon et considérer cette moyenne comme une estimation de μ. 
-  Comparer pour trois échantillons différents cette moyenne estimée à la moyenne réelle de la population.

**Script 1.50 : Simulate-Estimate.R**
<font color="#c0504d"> # Set the random seed</font>
 set.seed(123456)
<font color="#c0504d"> # Draw a sample given the population parameters</font>
 sample <- rnorm(100,10,2)   # <font color="#7030a0">tirer un échantillon de taille 100 d'une pop suivant la Distribution N(10,4)</font>
 # <font color="#c0504d">Estimate the population mean with the sample average</font>
 mean(sample)
[1] <font color="#00b050">10.03364</font>
 <font color="#c0504d"># Draw a different sample and estimate again:</font>
 sample <- rnorm(100,10,2)
 mean(sample)
[1] <font color="#00b050">9.913197</font>
 <font color="#c0504d"># Draw a third sample and estimate again:</font>
 sample <- rnorm(100,10,2)
 mean(sample)
[1] <font color="#00b050">10.21746</font>	

<font color="#00b0f0">Toutes les moyennes de l'échantillon de</font> $\bar y$  <font color="#00b0f0">se situent autour de la moyenne réelle</font> μ = 10. 
- aucune n'est égale au paramètre exact de la population  à cause du bruit d'échantillonnage. 
- De même les résultats sont sensés donner une variance qui se situent autour de la variance réelle σ2/n = 0.04. 

<font color="#c0504d">Trois cas de ce type ne suffisent pas à tirer des conclusions solides sur la validité de l'équation 1.7.</font> 
<font color="#00b0f0">De bonnes études de simulation Monte Carlo devraient utiliser autant d'échantillons que possible.</font>

Dans la section 1.9.2, nous avons introduit les boucles for. Bien qu'elles ne soient pas la technique la plus puissante disponible dans R pour mettre en œuvre une étude de Monte-Carlo, nous nous en tiendrons car elles sont assez transparentes et directes. 

<font color="#c0504d">Le code montré dans le Script 1.51 </font>(Simulation-Repeated.R)
- <font color="#c0504d"> utilise une boucle for</font> <font color="#00b0f0">pour générer 10 000 échantillons</font> <font color="#00b050">de taille n = 100</font> 
- puis <font color="#7030a0">calcule la moyenne de l'échantillon pour tous (les échantillons)</font>.  

**La procédure est la suivante :**
- définir le seed aléatoire, 
- initialiser un vecteur $\bar y$ à 10 000 zéros en utilisant la commande numeric.	
- utiliser la boucle for pour répéter dans chacune de ses  réplications j (j = 1, 2, . . . , 10 000), les opérations suivante :
	- prélever un échantillon, 
	- calculer sa moyenne et la stocker dans la position numéro  j du vecteur $\bar y$. 
- Ainsi,  nous obtenons un vecteur de 10 000 estimations de $\bar y$ provenant de différents échantillons. 

**Script 1.51: Simulation-Repeated.R**
<font color="#c0504d">'# Set the random seed</font>
set.seed(123456)
<font color="#c0504d">'#initialize</font> $\bar y$ <font color="#c0504d">to a vector of length r=10000 to later store results:</font>
r <- 10000
$\bar y$ <- numeric(r)
<font color="#c0504d">'# repeat r times:</font>
for(j in 1:r) {
	<font color="#c0504d">'# Draw a sample and store the sample mean in pos. j=1,2,... of</font> $\bar y$:
	sample <- rnorm(100,10,2)
	$\bar y$[j] <- mean(sample)
}


<font color="#00b0f0">Le script 1.52 (Simulation-Repeated-Results.R) analyse ces 10 000 estimations. </font>
- leur Espérance est très proche de la présomption  μ   = 10    de l'équation 1.7. 
- la variance de l'échantillonnage simulé est proche du résultat théorique σ2/n = 0,04. 
- la densité estimée (en utilisant un kernel density estimate) est comparée à la distribution normale théorique. 

<font color="#00b0f0">L'option add=TRUE de la commande curve demande que la courbe normale soit dessinée au-dessus du graphique précédent</font> au lieu d'en créer un nouveau et <font color="#00b0f0">lty=2 change le type de ligne en courbe pointillée. </font>

<font color="#c0504d">Le résultat est montré à la figure 1.24.</font> <font color="#00b050">Les deux droites sont presque indiscernables,</font> <font color="#7030a0">sauf pour la zone proche du mode (où l'estimateur de densité du noyau a souvent des problèmes).</font>

**Output of Script 1.52: Simulation-Repeated-Results.R**
 <font color="#c0504d"># The first 20 of 10000 estimates:</font>
 $\bar y$[1:20]
<font color="#c0504d"> # Simulated mean:</font>
 mean($\bar y$)
<font color="#c0504d"> # Simulated variance:</font>
 var($\bar y$)
<font color="#c0504d"> # Simulated density:</font>
 plot(density($\bar y$))
 curve( dnorm(x,10,sqrt(.04)), add=TRUE,lty=2)	

Rappelez-vous : <font color="#00b050">pour la plupart des estimateurs avancés, de telles simulations sont la seule façon d'étudier certaines de leurs caractéristiques,</font> <font color="#c0504d">car il est impossible d'obtenir des résultats théoriques intéressants. </font>

## Propriétés asymptotiques des estimateurs
<font color="#7030a0">Les analyses asymptotiques concernent de grands échantillons</font> et <font color="#00b0f0">le comportement des estimateurs et autres statistiques à mesure que la taille de l'échantillon n augmente sans borne.</font> 

Selon la `loi des grands nombres` <font color="#00b0f0">la moyenne d'échantillonnage </font>$\bar Y$ <font color="#00b0f0">converge en probabilité vers la moyenne de population </font>μ <font color="#00b0f0">quand </font>n → ∞. <font color="#c0504d">Pour un échantillon (infiniment) grand</font> , <font color="#00b050">cela implique que</font> E($\bar Y$) <font color="#00b050">tend vers</font> μ <font color="#00b050">et</font> Var($\bar Y$) <font color="#00b050">tend vers 0.</font>
<font color="#00b0f0">Afin de vérifier cette loi des grands nombres avec la simulation de Monte Carlo</font>, <font color="#c0504d">on va changer la taille de l'échantillon de l'exemple précédent</font> et voir ce qu'il en résulte. 
- Changer la taille de l'échantillon dans la ligne de code `sample <- rnorm(100,10,2)` de 100 à un nombre autre 
- et réexécuter le code de simulation.
<font color="#00b0f0">Les résultats pour des tailles de l'échantillon n = 10, 50, 100 et 1000 sont présentés à la Figure 1.25.</font> 
- la variance de $\bar Y$ diminue en fait. Le graphique de la densité pour n = 1000 est déjà très étroit et élevé, indiquant une faible variance. Il semble plausible que la densité finira par s'effondrer en une seule droite verticale correspondante à Var($\bar Y$ =  0 qand n tend vers ∞.
- <font color="#00b0f0">Le théorème central limite (CLT) énonce que quand n (la taille d'un échantillon aléatoire) tend vers l'infini, sa moyenne (l'Espérance) </font>$\bar Y$<font color="#c0504d"><u>sera normalement distribuée quelle que soit la distribution de Y.</u></font> <font color="#00b050">Ce phénomène est appelé convergence dans la distribution.</font>
- Dans l'exemple utilisé pour les simulations, la variable aléatoire Y est normalement distribuée, donc la moyenne de l'échantillon $\bar Y$ doit également être normalement distribuée pour n'importe quelle taille d'échantillon. 

<font color="#c0504d">Vérifions ce théorème de la convergence  sur une distribution non normale</font>, <font color="#00b0f0"> la distribution</font> χ2 <font color="#00b0f0">avec 1 degré de liberté.  </font>
- la densité de la Distribution de χ² , représentée à la Figure 1.26.(note35),  est très différente de celle, en forme de cloche, de la densité normale .  
- pour voir l'effet de la taille de l'échantillon pour une distribution de χ², la seule ligne que nous devons modifier dans le code de simulation du Script 1.51 (Simulation-Répétée.R) est `sample <- rnorm(n, 10,2)` à remplacer par `sample <- rchisq(n,1)`
- <font color="#c0504d">Conclusion</font> : <font color="#00b0f0">la forme de la distribution de χ² est très différente de celle de la distribution normale pour de petits échantillon</font>, <font color="#00b050">mais elle s'en rapproche à mesure qu'augmente la taille de l'échantillon</font>. Pour n=1000, il est difficile de les distinguer.
- L'effet d'une variance décroissante fonctionne ici exactement de la même manière qu'avec la population normale.

## Simulation des intervalles de confiance et tests t 
Sur les échantillons simulés, il est possible,
- non seulement d'estimer de façon répétée les paramètres de la population, 
- mais aussi de calculer des intervalles de confiance et effectuer des tests . 

<font color="#c0504d">La routine de simulation présentée ici est assez avancée.</font> L'avantage de parcourir ce matériel est qu'il pourrait améliorer notre compréhension du fonctionnement de l'inférence statistique.

<font color="#00b0f0">Nous partons du même exemple que dans la Section 1.10.1</font> : 
- une population, et une variable Y qui suit une distribution Normale(10, 4). 
- Nous tirons de cette population 10 000 échantillons de taille n = 100 . 
- Pour chacun des échantillons nous calculons :
	-	L'intervalle de confiance à 95 % et stockons les limites dans les vecteurs CIlower et CIupper.
	-	La  p-value pour test bilatéral de  H0 : μ = 10 ⇒ vector pvalue1 
	-	La  p-value pour le test bilatéral de l'hypothèse nulle incorrecte H0 : μ = vecteur 9,5  ⇒ pvalue2
	-     Enfin, nous calculons les vecteurs logiques reject1 et reject2 qui sont TRUE si nous rejetons H0 au seuil α = 5 %, c'est-à-dire si pvalue1 ou pvalue2 est respectivement < à 0,05.
<font color="#00b0f0">Le script 1.53 (Simulation-Inference.R) présente le code R de ces simulations </font><font color="#c0504d">ainsi qu'un tableau de fréquences des résultats reject1 et reject2.</font>

Si la théorie et l'implémentation en R sont exactes, 
- la probabilité de rejeter H0 correcte (erreur de type I) devrait être égale au seuil de signification α choisi. 
- Dans notre simulation, nous rejetons l'hypothèse correcte dans 508 des 10 000 échantillons, soit dans 5,08 %.

<font color="#c0504d">La probabilité de rejeter une hypothèse fausse est appelée power of the test</font> (puissance du test). 
- Elle dépend de nombreux facteurs, comme la taille de l'échantillon et l'ampleur de l'erreur de H0, c'est-à-dire l'écart entre $μ_0$ et la vraie valeur de μ. 
- La théorie nous indique simplement que la puissance est supérieure à α. 
- Dans notre simulation, l'hypothèse nulle erronée H0 : μ= 9,5 est rejetée dans 69,57 % des échantillons. 

<font color="#00b0f0">Le lecteur est fortement encouragé à modifier le code de simulation</font> <font color="#c00000">pour vérifier les résultats théoriques selon lesquels cette puissance augmente si</font> $μ_0$ <font color="#c00000">s'éloigne de 10 et si la taille de l'échantillon n augmente.</font>

<font color="#00b0f0">La figure 1.28 présente graphiquement l'intervalle de confiance à 95 % pour les 100 premiers échantillons simulés. </font>
- Chaque ligne horizontale représente un intervalle de confiance. 
- Dans ces 100 premiers échantillons, la véritable hypothèse nulle a été rejetée dans 3 cas. Ce fait signifie que pour ces trois échantillons, l'intervalle de confiance ne couvre pas $μ_0$ = 10  Ces trois cas sont représentés en noir dans la partie gauche de la figure, tandis que les autres sont en gris.

<font color="#00b0f0">Le test t rejette la fausse hypothèse nulle H0 </font>: μ = 9,5 <font color="#00b0f0">dans 72 des 100 premiers échantillons</font>. Leurs intervalles de confiance ne couvrent pas 9,5 et sont dessinés en noir dans la partie droite de la figure 1.28.

**Script 1.53: Simulation-Inference.R**
<font color="#c0504d"> # Set the random seed</font>
 set.seed(123456)
<font color="#c0504d"> # initialize vectors to later store results:</font>
 r <- 10000
 CIlower <- numeric(r); CIupper <- numeric(r)
 pvalue1 <- numeric(r); pvalue2 <- numeric(r)
<font color="#c0504d"> # repeat r times:</font>
 for(j in 1:r) {
      # <font color="#c00000">Draw a sample</font>
      sample <- rnorm(100,10,2)
	 # <font color="#c00000">test the (correct) null hypothesis mu=10:</font>
	 testres1 <- t.test(sample,mu=10)
	'# <font color="#c00000">store CI & p value:</font>
	 CIlower[j] <- testres1$conf.int[1]
	 CIupper[j] <- testres1$conf.int[2]
	 pvalue1[j] <- testres1$p.value
	'# <font color="#c00000">test the (incorrect) null hypothesis mu=9.5 & store the p value:</font>
	 pvalue2[j] <- t.test(sample,mu=9.5)$p.value
   }

<font color="#c00000"> '# Test results as logical value</font>
 reject1<-pvalue1<=0.05; reject2<-pvalue2<=0.05
 table(reject1)
 table(reject2)
