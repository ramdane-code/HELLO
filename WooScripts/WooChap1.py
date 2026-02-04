#Script 1.1: First-Python-Script.py: commentaire, saisie et affiche texte et petit calcul
# This is a comment.
# in the next line, we try to enter Shakespeare:
'To be, or not to be: that is the question'
# let's try some sensible math:
print((1 + 2) * 5)
A = 16 ** 0.5
print(f'monA = {A} \n')

#Script 1.2: Python-as-a-Calculator.py et f-string (formatted string literal)
result1 = 1 + 1
print(f'result1: {result1}\n')
result2 = 5 * (4 - 1) ** 2
print(f'result2: {result2}\n')
result3 = [result1, result2]
print(f'result3: \n{result3}\n')

#Script 1.3: Module-Math.py (import module et son utilisation : sqrt, pi, e)
import math as someAlias

result1 = someAlias.sqrt(16)
print(f'result1: {result1}\n')

result2 = someAlias.pi
print(f'Pi: {result2}\n')

result3 = someAlias.e
print(f'Eulers number: {result3}\n')

#Script 1.4: Objects-in-Python.py (afficher le type d'un objet result)

result1 = 1 + 1
# determine the type:
type_result1 = type(result1)
# print the result:
print(f'type_result1: {type_result1}')

result2 = 2.5
type_result2 = type(result2)
print(f'type_result2: {type_result2}')

result3 = 'To be, or not to be: that is the question'
type_result3 = type(result3)
print(f'type_result3: {type_result3}\n')


#Script 1.5: Lists-Copy.py
# define a list:
example_list = [1, 5, 41.3, 2.0]

# be careful with changes on variables pointing on example_list:
duplicate_list = example_list #example_list devient duplicate_list
duplicate_list[3] = 10000
print(f'duplicate_list: {duplicate_list}\n')
print(f'example_list: {example_list}\n')

# work on a copy of example_list:
example_list = [1, 5, 41.3, 2.0]
duplicate_list = example_list[:] #duplicate_list récupère les élément de example_list
duplicate_list[3] = 10000
print(f'duplicate_list: {duplicate_list}\n')
print(f'example_list: {example_list}\n')
#La différence entre les 2 opérations est que la première transforme l'objet example_list, alors que la 2ème crée un nouvel objet.add(element)


#Script 1.6: Lists.py (définir, accéder, remplacer, supprimer, appliquer fonction et méthode)

# define a list:
example_list = [1, 5, 41.3, 2.0]
print(f'type(example_list): {type(example_list)}\n')

# access first entry by index:
first_entry = example_list[0]
print(f'first_entry: {first_entry}\n')

# access second to fourth entry by index:
range2to4 = example_list[1:4] #le premier terme est 1 car l'index commence à 0, le second est 4 car le dernier terme est exclu, soit index 0,1,2,3
print(f'range2to4: {range2to4}\n')

# replace third entry by new value:
example_list[2] = 3
print(f'example_list: {example_list}\n')

# apply a function:
function_output = min(example_list)
print(f'function_output: {function_output}\n')

# apply a method:
example_list.sort()
print(f'example_list: {example_list}\n')

# delete third element of sorted list:
del example_list[2]
print(f'example_list: {example_list}\n')


#Script 1.7: Dicts-Copy.py: créer dict, afficher type, accéder, ajouter, supprimer éléments

# define and print a dict:
var1 = ['Florian', 'Daniel']
var2 = [96, 49]
var3 = [True, False]
example_dict = dict(name=var1, points=var2, passed=var3)
print(f'example_dict: {example_dict}\n')

# if you want to work on a copy:
import copy   #copy est un module
copied_dict = copy.deepcopy(example_dict) #deepcopy crée un nouvel objet distinct de example_dict
copied_dict['points'][1] = copied_dict['points'] [1]-40 # On modifie les points du 2ème (cad [1]) en leur retranchant 40
print(f'example_dict: \n{example_dict}\n')
print(f'copied_dict: \n{copied_dict}\n')


#Script 1.8: Dicts.py:déf, type, accéder, modifier, supprimer éléments
# define and print a dict:
var1 = ['Florian', 'Daniel']
var2 = [96, 49]
var3 = [True, False]
example_dict = dict(name=var1, points=var2, passed=var3)
print(f'example_dict: \n{example_dict}\n')
# another way to define the dict:
example_dict2 = {'name': var1, 'points': var2, 'passed': var3}
print(f'example_dict2: \n{example_dict2}\n')
# get data type:
print(f'type(example_dict): {type(example_dict)}\n')
# access 'points':
points_all = example_dict['points']
print(f'points_all: {points_all}\n')
# access 'points' of Daniel:
points_daniel = example_dict['points'][1]
print(f'points_daniel: {points_daniel}\n')
# add 4 to 'points' of Daniel and let him pass:
example_dict['points'][1] = example_dict['points'][1] + 4
example_dict['passed'][1] = True
print(f'example_dict: \n{example_dict}\n')
# add a new variable 'grade':
example_dict['grade'] = [1.3, 4.0]
# delete variable 'points':
del example_dict['points']
print(f'example_dict: \n{example_dict}\n')


#Script 1.9: Numpy-Arrays.py  (définir un np.array, ses dimensions, afficher éléments par index, liste et bool)

import numpy as np

# define arrays in numpy:
testarray1D = np.array([1, 5, 41.3, 2.0])
print(f'type(testarray1D): {type(testarray1D)}\n')

testarray2D = np.array([[4, 9, 8, 3],
                        [2, 6, 3, 2],
                        [1, 1, 7, 4]])

# get dimensions of testarray2D:
dim = testarray2D.shape
print(f'dimensions: {dim}\n')

# access elements by indices:
third_elem = testarray1D[2]
print(f'third_elem: {third_elem}\n')
second_third_elem = testarray2D[1, 2] # element in 2nd row and 3rd column
print(f'second_third_elem: {second_third_elem}\n')
second_to_third_col = testarray2D[:, 1:3] # each row in the 2nd and 3rd column (col index 1 à 2 (l'index3 étant exclu))
print(f'second_to_third_col: \n{second_to_third_col}\n')

# access elements by lists:
first_third_elem = testarray1D[[0, 2]] #third_elem : index 0, 1, 2 soit 41,3
print(f'first_third_elem: {first_third_elem}\n')

# same with Boolean lists:
first_third_elem2 = testarray1D[[True, False, True, False]]
print(f'first_third_elem2: {first_third_elem2}\n')
k = np.array([[True, False, False, False],
[False, False, True, False],
[True, False, True, False]])
elem_by_index = testarray2D[k] # 1st elem in 1st row, 3rd elem in 2nd row...
print(f'elem_by_index: {elem_by_index}\n')


#Script 1.10: Numpy-SpecialCases.py (créer listes et tableaux : linspace, arange, np.zeros, np.ones, np.empty)
import numpy as np
# array of integers defined by the arguments start, end and sequence length:
sequence = np.linspace(0, 2, num=11)
print(f'sequence: \n{sequence}\n')

# sequence of integers starting at 0, ending at 5-1:
sequence_int = np.arange(5)
print(f'sequence_int: \n{sequence_int}\n')

# initialize array with each element set to zero:
zero_array = np.zeros((4, 3))
print(f'zero_array: \n{zero_array}\n')

# initialize array with each element set to one:
one_array = np.ones((2, 5))
print(f'one_array: \n{one_array}\n')

# uninitialized array (filled with arbitrary nonsense elements):
empty_array = np.empty((2, 3))
print(f'empty_array: \n{empty_array}\n')


#Script 1.11: Numpy-Operations.py: algèbre matricielle : créer matrices, transformations et opérations sur matrices

import numpy as np

# define an arrays in numpy:
mat1 = np.array([[4, 9, 8],
                 [2, 6, 3]])
mat2 = np.array([[1, 5, 2],
                 [6, 6, 0],
                 [4, 8, 3]])

# use a numpy function:
result1 = np.exp(mat1) # exp(chaque élément) par exemple exp(4)= 54,59815
print(f'result1: \n{result1}\n')

result1bis = mat2[[0, 1]] # je décompose calcul de result2 en 2 étapes pour plus de clarté.
print(f'result1bis: \n{result1bis}\n')

result1bbis= result1bis + mat1
print(f'result1bbis : \n{result1bbis}\n')

result2 = mat1 + mat2[[0, 1]] # same as np.add(mat1, mat2[[0, 1]])
print(f'result2: \n{result2}\n')

# use a method:
mat1_tr = mat1.transpose()
print(f'mat1_tr: \n{mat1_tr}\n')

# matrix algebra:
matprod = mat1 @ mat2  # same as mat1.dot(mat2)
print(f'matprod: \n{matprod}\n')


#Script 1.12: Pandas.py:NB DataFrame et Index :de 3 listes np.array (Ventes glaces, clients, météo) créer et manipuler DataFrame

import numpy as np
import pandas as pd

# define a pandas DataFrame:
icecream_sales = np.array([30, 40, 35, 130, 120, 60])
weather_coded = np.array([0, 1, 0, 1, 1, 0])
customers = np.array([2000, 2100, 1500, 8000, 7200, 2000])
df = pd.DataFrame({'icecream_sales': icecream_sales,
                    'weather_coded': weather_coded,
                    'customers': customers})

# define and assign an index (six ends of month starting in April, 2010)
# (details on generating indices are given in Chapter 10):
ourIndex = pd.date_range(start='04/2010', freq='M', periods=6)
df.set_index(ourIndex, inplace=True)

# print the DataFrame
print(f'df: \n{df}\n')

# access columns by variable names:
subset1 = df[['icecream_sales', 'customers']]
print(f'subset1: \n{subset1}\n')

# access second to fourth row:
subset2 = df[1:4] # same as df['2010-05-31':'2010-07-31']
print(f'subset2: \n{subset2}\n')

# access rows and columns by index and variable names:
subset3 = df.loc['2010-05-31', 'customers'] # same as df.iloc[1,2]
print(f'subset3: \n{subset3}\n')

# access rows and columns by index and variable integer positions:
subset4 = df.iloc[1:4, 0:2] # same as df.loc['2010-05-31':'2010-07-31', ['icecream_sales','weather']]
print(f'subset4: \n{subset4}\n')


#Script 1.13: Très important : Pandas-Operations.py

import numpy as np
import pandas as pd

# define a pandas DataFrame:
icecream_sales = np.array([30, 40, 35, 130, 120, 60])
weather_coded = np.array([0, 1, 0, 1, 1, 0])
customers = np.array([2000, 2100, 1500, 8000, 7200, 2000])
df = pd.DataFrame({'icecream_sales': icecream_sales,
                   'weather_coded': weather_coded,
                   'customers': customers})

# define and assign an index (six ends of month starting in April, 2010)
# (details on generating indices are given in Chapter 10):
ourIndex = pd.date_range(start='04/2010', freq='ME', periods=6)
df.set_index(ourIndex, inplace=True)

# include sales two months ago:
df['icecream_sales_lag2'] = df['icecream_sales'].shift(2)
print(f'df: \n{df}\n')

# use a pandas.Categorical object to attach labels (0 = bad; 1 = good):
df['weather'] = pd.Categorical.from_codes(codes=df['weather_coded'],
categories=['bad', 'good'])
print(f'df: \n{df}\n')

# mean sales for each weather category:
group_means = df.groupby('weather').mean()
print(f'group_means: \n{group_means}\n')


#Script 1.14: Wooldridge.py (charger fichier de données, afficher le type et 5 lignes (wage1.head))
import wooldridge as woo
import pandas as pd

# load data (charger les données):
wage1 = woo.dataWoo('wage1')

# get type (obtenir le type d'objet):
print(f'type(wage1): \n{type(wage1)}\n')

# get an overview (obtenir vue d'ensemble):
print(f'wage1.head(): \n{wage1.head()}\n')


#Script ajouté: Afficher tous les fichiers présents dans Wooldridge
import wooldridge as woo
print(woo.data())

#Script 1.15: Import-Export.py (pd.read_csv, import DataFrame, afficher tout ou partie, ajouter ligne, col et index)
#(il n'a pas fonctionné car je n'arrive pas à lire les fichiers)
import wooldridge as woo
import pandas as pd

# import csv with pandas:
df1 = pd.read_csv('data/sales.csv.bz2', delimiter=',', header=None,
                   names=['year', 'product1', 'product2', 'product3'])
print(f'df1: \n{df1}\n')

# import txt with pandas:
df2 = pd.read_table('data/sales.txt', delimiter=' ')
print(f'df2: \n{df2}\n')
#pd.read_csv est plus universel que pd.read_table, header=0 si ligne1 contient titre des col

# add a row to df1:
df3 = df1.append({'year': 2014, 'product1': 10, 'product2': 8, 'product3': 2}, ignore_index=True)
print(f'df3: \n{df3}\n')

# export with pandas:
df3.to_csv('data/sales2.csv')


#Script ajouté pour prévoir le cas le fichier à importer n'existe pas
import wooldridge as woo
import pandas as pd

# Importer CSV avec Pandas :
import os

file_path = 'datasets/wage1.csv.bz2'
if os.path.exists(file_path):
    df1 = pd.read_csv(file_path, delimiter=',', header=0)  # delimiter est le même que sep
    print(f'df1 : \n{df1} \n')
else:
    print(f"File not found: {file_path}")


#Script 1.16: Import-StockData.py (utiliser panda_datareader pour import et voir contenu importé)
import pandas_datareader as pdr

# download data for 'F' (= Ford Motor Company) and define start and end:
tickers = ['F']
start_date = '2014-01-01'
end_date = '2015-12-31'

# use pandas_datareader for the import:
F_data = pdr.data.DataReader(tickers, 'yahoo', start_date, end_date)

# look at imported data:
print(f'F_data.head(): \n{F_data.head()}\n')
print(f'F_data.tail(): \n{F_data.tail()}\n')

#Script 1.17: Graphs-Basics.py (créer et formater graph à partir de 2 séries : x et y)
import matplotlib.pyplot as plt

# create data:
x = [1, 3, 4, 7, 8, 9]
y = [0, 3, 6, 9, 7, 8]

# plot and save:
plt.plot(x, y, color='black')
plt.savefig('PyGraphs/Graphs-Basics-a.pdf')
plt.close()

#Script 1.18: Graphs-Basics2.py (créer et formater un graphe à partir de 2 séries: couleurs et styles de lignes)
import matplotlib.pyplot as plt

# create data:
x = [1, 3, 4, 7, 8, 9]
y = [0, 3, 6, 9, 7, 8]

# plot and save:
plt.plot(x, y, color='black', linestyle='--')
plt.savefig('PyGraphs/Graphs-Basics-b.pdf')
plt.close()

plt.plot(x, y, color='black', linestyle=':')
plt.savefig('PyGraphs/Graphs-Basics-c.pdf')
plt.close()

plt.plot(x, y, color='black', linestyle='-', linewidth=3)
plt.savefig('PyGraphs/Graphs-Basics-d.pdf')
plt.close()

plt.plot(x, y, color='black', marker='o')
plt.savefig('PyGraphs/Graphs-Basics-e.pdf')
plt.close()

plt.plot(x, y, color='black', marker='v', linestyle='')
plt.savefig('PyGraphs/Graphs-Basics-f.pdf')

#Script 1.19: Graphs-Functions.py (créer fonction quadratique et faire son graphe)
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

# support of quadratic function
# (creates an array with 100 equispaced elements from -3 to 2):
x1 = np.linspace(-3, 2, num=100)

# function values for all these values:
y1 = x1 ** 2

# plot quadratic function:
plt.plot(x1, y1, linestyle='-', color='black')
plt.savefig('PyGraphs/Graphs-Functions-a.pdf')
plt.close()

# same for normal density:
x2 = np.linspace(-4, 4, num=100)
y2 = stats.norm.pdf(x2)

# plot normal density:
plt.plot(x2, y2, linestyle='-', color='black')
plt.savefig('PyGraphs/Graphs-Functions-b.pdf')

#Script 1.20: Graphs-BuildingBlocks.py
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

# support for all normal densities:
x = np.linspace(-4, 4, num=100)

# get different density evaluations:
y1 = stats.norm.pdf(x, 0, 1)
y2 = stats.norm.pdf(x, 1, 0.5)
y3 = stats.norm.pdf(x, 0, 2)

# plot:
plt.plot(x, y1, linestyle='-', color='black', label='standard normal')
plt.plot(x, y2, linestyle='--', color='0.3', label='mu = 1, sigma = 0.5')
plt.plot(x, y3, linestyle=':', color='0.6', label='$\mu = 0$, $\sigma = 2$')
plt.xlim(-3, 4)
plt.title('Normal Densities')
plt.ylabel('$\phi(x)$')
plt.xlabel('x')
plt.legend()
plt.savefig('PyGraphs/Graphs-BuildingBlocks.pdf')

#Script 1.21: Graphs-Export.py (créer fonction Normale avec différentes densités, créer et exporter graphes)
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
# support for all normal densities:
x = np.linspace(-4, 4, num=100)
# get different density evaluations:
y1 = stats.norm.pdf(x, 0, 1)
y2 = stats.norm.pdf(x, 0, 3)
# plot (a):
plt.figure(figsize=(4, 6))
plt.plot(x, y1, linestyle='-', color='black')
plt.plot(x, y2, linestyle='--', color='0.3')
plt.savefig('PyGraphs/Graphs-Export-a.pdf')
plt.close()
# plot (b):
plt.figure(figsize=(6, 4))
plt.plot(x, y1, linestyle='-', color='black')
plt.plot(x, y2, linestyle='--', color='0.3')
plt.savefig('PyGraphs/Graphs-Export-b.png')


#Script ajouté hr : charger et afficher lignes et colonnes d'un tableau DataFrame
import wooldridge as woo
df= woo.dataWoo('affairs') # df peut être remplacé par affairs, c'est le Tableau contenant les données.
print(f'«colonnes :», df.columns')
print(f'«index : », df.index')




#Script 1.22: Descr-Tables.py : TRES IMPORTANT EXPLOITER RESULTATS D'UNE ENQUETE (Questionnaire) 
import wooldridge as woo
import numpy as np
import pandas as pd

affairs = woo.dataWoo('affairs')

# adjust codings to [0-4] (Categoricals require a start from 0):
affairs['ratemarr'] = affairs['ratemarr'] - 1

# use a pandas.Categorical object to attach labels for "haskids":
affairs['haskids'] = pd.Categorical.from_codes(affairs['kids'],
                                               categories=['no', 'yes'])

# ... and "marriage" (for example: 0 = 'very unhappy', 1 = 'unhappy',...):
mlab = ['very unhappy', 'unhappy', 'average', 'happy', 'very happy']
affairs['marriage'] = pd.Categorical.from_codes(affairs['ratemarr'],
                                                categories=mlab)

# frequency table in numpy (alphabetical order of elements):
ft_np = np.unique(affairs['marriage'], return_counts=True)
unique_elem_np = ft_np[0]
counts_np = ft_np[1]
print(f'unique_elem_np: \n{unique_elem_np}\n')
print(f'counts_np: \n{counts_np}\n')

# frequency table in pandas:Pour chq appréc son nbre.(plus pertinent que numpy)
ft_pd = affairs['marriage'].value_counts()
print(f'ft_pd: \n{ft_pd}\n')

# frequency table with groupby:(Pour chq appréc son nbre selon kids ou pas)
ft_pd2 = affairs['marriage'].groupby(affairs['haskids']).value_counts()
print(f'ft_pd2: \n{ft_pd2}\n')

# contingency table in pandas: en ligne0 haskids(no,yes,all) et en col0 marriage(les 5 valeurs)               
ct_all_abs = pd.crosstab(affairs['marriage'], affairs['haskids'], margins=3)
print(f'ct_all_abs: \n{ct_all_abs}\n')
ct_all_rel = pd.crosstab(affairs['marriage'], affairs['haskids'], normalize='all') # en % du total
print(f'ct_all_rel: \n{ct_all_rel}\n')

# share within "marriage" (i.e. within a row):chq appréc =100% divisés entre kids et non kids 
ct_row = pd.crosstab(affairs['marriage'], affairs['haskids'], normalize='index')
print(f'ct_row: \n{ct_row}\n')

# share within "haskids" (i.e. within a column):
ct_col = pd.crosstab(affairs['marriage'], affairs['haskids'], normalize='columns')
print(f'ct_col: \n{ct_col}\n')


#Script 1.23: Descr-Figures.py: création graph à secteurs et à barres
import wooldridge as woo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

affairs = woo.dataWoo('affairs')

# corriger ratemarr et remplacer par des labels les appréc par des chiffres:
affairs['ratemarr'] = affairs['ratemarr'] - 1
affairs['haskids'] = pd.Categorical.from_codes(affairs['kids'],
                                               categories=['no', 'yes'])
mlab = ['very unhappy', 'unhappy', 'average', 'happy', 'very happy'] # marriage labels 
affairs['marriage'] = pd.Categorical.from_codes(affairs['ratemarr'],
                                                categories=mlab)

# comptage pour tous les graphs (counts for all graphs):
counts = affairs['marriage'].value_counts()
print(f'counts: \n{counts}\n') # nbre total pour chaque appréciation
counts_bykids = affairs['marriage'].groupby(affairs['haskids']).value_counts()
print(f'counts_bykids: \n{counts_bykids}\n') # no kids : nbre no kids puis sa répartit° par appréciation, et kids : nbre kids puis sa répartit° par appréciation
counts_yes = counts_bykids['yes']
print(f'counts_yes: \n{counts_yes}\n') #kids : nbre kids puis sa répartit par appréciation (c précédent)
counts_no = counts_bykids['no']
print(f'counts_no: \n{counts_no}\n') #nbre no kids puis sa répartit par appréciation (c précédent)

# Graphs en secteurs (pie chart) (a):
grey_colors = ['0.3', '0.4', '0.5', '0.6', '0.7'] # intensité du gris par appréc (label ou secteur)
plt.pie(counts, labels=mlab, colors=grey_colors) # chq secteur selon nbre, couleur et son label(appréc)indiqué
plt.savefig('PyGraphs/Descr-Pie.pdf')
plt.close()

# horizontal bar chart (b):
y_pos = [0, 1, 2, 3, 4] # the y locations for the bars
plt.barh(y_pos, counts, color='0.6') #barh pour horiz. Param : position, marr label, nbre, une seule couleur 
plt.yticks(y_pos, mlab, rotation=60) # add and adjust labeling:indication du label(appréc) et sa position
plt.savefig('PyGraphs/Descr-Bar1.pdf')
plt.close()

# Graph en barres verticales empilées (stacked bar plot) (c):
x_pos = [0, 1, 2, 3, 4] # the x locations (position) for the bars:disposition des barres sur l'axe des x
plt.bar(x_pos, counts_yes, width=0.4, color='0.6', label='Yes') #Graph des 5 appréciations pour les yes_kids

# with 'bottom=counts_yes' bars are added on top of previous ones:
plt.bar(x_pos, counts_no, width=0.4, bottom=counts_yes, color='0.3', label='No') # Graph des 5 appréciation pour les no kids, empilés sur les yes car bottom=counts
plt.ylabel('Counts') # étiquette "counts" sur l'axe des y
plt.xticks(x_pos, mlab) # add labels on x axis( étiquettes des labels sur l'axe des x)
plt.legend() # ajouter une légende indiquant la couleur des yes et des no kids
plt.savefig('PyGraphs/Descr-Bar2.pdf')
plt.close()

## Graph en barres verticales groupées(grouped bar plot) (d):pour chq appréc (label) la barre yes kids à côté de la barre no kids
# add left bars first and move bars to the left:Positionner les barres de gauche (celles des yes kids)
x_pos_leftbar = [-0.2, 0.8, 1.8, 2.8, 3.8] # indique l'emplacement des barres de gauche (celles des yes kids) sur l'axe des x
plt.bar(x_pos_leftbar, counts_yes, width=0.4, color='0.6', label='Yes') #graph des barres de gauche(yes kids),
#count": la taille de la barre depuis l'axe des x (niveau 0), yes dans Légende

# add right bars first and move bars to the right:
x_pos_rightbar = [0.2, 1.2, 2.2, 3.2, 4.2] # positionner les barres de droite (no kids) sur l'axe des x
plt.bar(x_pos_rightbar, counts_no, width=0.4, color='0.3', label='No') #Graph des barres de droite (no kids), No dans légende
# count_no : ne pas empiler(ne pas ajouter) la taille avec le leftbar 
plt.ylabel('Counts') # "Counts" comme étiquette de l'axe y
plt.xticks(x_pos, mlab) # Les étiquettes de l'axe des x selon mlab et le positionnement
plt.legend()
plt.savefig('PyGraphs/Descr-Bar3.pdf')



#Script 1.24: Histogram.py(générer des histogrammes sur rapport entre ROE et Salaires dirigeants SEOSAL1)
import wooldridge as woo
import matplotlib.pyplot as plt

ceosal1 = woo.dataWoo('ceosal1')

# extract roe:
roe = ceosal1['roe']

# subfigure a (histogram with counts):hist très simple: coul:grise, "roe" et "counts" sur x et y.
plt.hist(roe, color='grey')
plt.ylabel('Counts')
plt.xlabel('roe')
plt.savefig('PyGraphs/Histogram1.pdf')
plt.close()

# subfigure b (histogram with density and explicit breaks):
breaks = [0, 5, 10, 20, 30, 60] #rupture sur axe des x fixant intervalles (largeurs des barres)
plt.hist(roe, color='grey', bins=breaks, density=True) #Graph: intervalles fixés dans variable breaks, 
                                                       #densité dans l'aire de la barre et non sa hauteur
plt.ylabel('density')
plt.xlabel('roe')
plt.savefig('PyGraphs/Histogram2.pdf')


#Script 1.25: KDensity.py:Kernel density plot):histog sophistiqué
import wooldridge as woo
import statsmodels.api as sm
import matplotlib.pyplot as plt

ceosal1 = woo.dataWoo('ceosal1')

# extract roe:
roe = ceosal1['roe']

# estimate kernel density: estimer la densité du noyau
kde = sm.nonparametric.KDEUnivariate(roe)
kde.fit()

# subfigure a (kernel density):Graph de la densité du noyau(courbe de la densité en fonction de roe)
plt.plot(kde.support, kde.density, color='black', linewidth=2)
plt.ylabel('density')
plt.xlabel('roe')
plt.savefig('PyGraphs/Density1.pdf')
plt.close()

# subfigure b (kernel density with overlayed histogram):(superposition d'une courbe à l'histogramme)
plt.hist(roe, color='grey', density=True)
plt.plot(kde.support, kde.density, color='black', linewidth=2)
plt.ylabel('density')
plt.xlabel('roe')
plt.savefig('PyGraphs/Density2.pdf')



#Script 1.26: Descr-ECDF.py (Calcul et Graph fonction distribution cumulative empirique (ECDF) : valeurs cumulées ⩽ valeur x.)
import wooldridge as woo
import numpy as np
import matplotlib.pyplot as plt

ceosal1 = woo.dataWoo('ceosal1')

# extract roe:
roe = ceosal1['roe']

# calculate ECDF:
x = np.sort(roe) # trier (classement) la série roe (ordre croissant?)
n = x.size # taille de l'échantillon dans la variable n
y = np.arange(1, n + 1) / n # generates cumulative shares of observations

# plot a step function:
plt.step(x, y, linestyle='-', color='black')
plt.xlabel('roe')
plt.savefig('PyGraphs/ecdf.pdf')



#Script 1.27: Descr-Stats.py: stat descript avec Numpy (Moyenne, Médiane, écart type, corrélation)
import wooldridge as woo
import numpy as np

ceosal1 = woo.dataWoo('ceosal1')

# extract roe and salary:
roe = ceosal1['roe']
salary = ceosal1['salary']

# sample average:
roe_mean = np.mean(salary)
print(f'roe_mean: {roe_mean}\n')

# sample median:
roe_med = np.median(salary)
print(f'roe_med: {roe_med}\n')

# standard deviation:
roe_s = np.std(salary, ddof=1)
print(f'roe_s: {roe_s}\n')

# correlation with ROE:
roe_corr = np.corrcoef(roe, salary)
print(f'roe_corr: \n{roe_corr}\n')


#Script 1.28: Descr-Boxplot.py : créer des boxplot, un genre de graphs à revoir
import wooldridge as woo
import matplotlib.pyplot as plt

ceosal1 = woo.dataWoo('ceosal1')

# extract roe and salary:
roe = ceosal1['roe']
consprod = ceosal1['consprod']

# plotting descriptive statistics:
plt.boxplot(roe, vert=False) # mettre vert=True pour obtenir Box plot horizontal (plus pertinent)
plt.ylabel('roe')
plt.savefig('PyGraphs/Boxplot1.pdf')
plt.close()


# plotting descriptive statistics:comparer Boxplots de 2 sous ens (entrep de BC et entrep non BC)
roe_cp0 = roe[consprod == 0] #: roe des entrep non BC dans la variable roe_cp0
roe_cp1 = roe[consprod == 1] #: roe des entrep de BC dans la variable roe_cp1

plt.boxplot([roe_cp0, roe_cp1])
plt.ylabel('roe')
plt.savefig('PyGraphs/Boxplot2.pdf')



#Script 1.29: PMF-binom.py (utiliser fonction binom.pmf  de scipy pour calculer prob tirer 2 boules blanches)
import scipy.stats as stats
import math

# pedestrian approach:
c = math.factorial(10) / (math.factorial(2) * math.factorial(10 - 2))
p1 = c * (0.2 ** 2) * (0.8 ** 8)
print(f'p1: {p1}\n')

# scipy function:
p2 = stats.binom.pmf(2, 10, 0.2)
print(f'p2: {p2}\n')



#Script 1.30: PMF-example.py (Binomiale : sa PMF pour 10 valeurs et son graph )
import scipy.stats as stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# values for x (all between 0 and 10):
x = np.linspace(0, 10, num=11)

# PMF for all these values:
fx = stats.binom.pmf(x, 10, 0.2)

# collect values in DataFrame:
result = pd.DataFrame({'x': x, 'fx': fx}) # x:liste des valeurs, fx: liste des prob calculées.
print(f'result: \n{result}\n')

# plot:
plt.bar(x, fx, color='0.6')
plt.ylabel('x')
plt.ylabel('fx')
plt.savefig('PyGraphs/PMF-example.pdf')



#Script 1.31: PDF-example.py (générer fonction Normale et son graph avec scipy)
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

# support of normal density:générer liste de valeurs pour fonction de densité normale
x_range = np.linspace(-4, 4, num=100)

# PDF for all these values:
pdf = stats.norm.pdf(x_range)

# plot:
plt.plot(x_range, pdf, linestyle='-', color='black')
plt.xlabel('x')
plt.ylabel('dx')
plt.savefig('PyGraphs/PDF-example.pdf')



#Script 1.32: CDF-example.py (calcul FDCumulative binomiale et normale avec statsmodels)
import scipy.stats as stats

# binomial CDF:
p1 = stats.binom.cdf(3, 10, 0.2)
print(f'p1: {p1}\n')

# normal CDF: de l'intervalle entre -1,96 et +1.96 d'une dist Normale Standard
p2 = stats.norm.cdf(1.96) - stats.norm.cdf(-1.96)
print(f'p2: {p2}\n')



#Script 1.33: Example-B-6.py(X ∼ Normal(4,9) et voulons avec scipy calculer P(2 < X ≤ 6).
#Transf des données en Normale Standart : P(2<X⩽6)=P((2-μ)/σ) < ((X-μ)/σ) ⩽ ((6-μ)/σ)
#P(2<X⩽6)=P((2-μ)/σ) < Z ⩽ ((6-μ)/σ)= φ(2/3)-φ(-2/3) Cf Obsidian
import scipy.stats as stats

# first example using the transformation:
p1_1 = stats.norm.cdf(2 / 3) - stats.norm.cdf(-2 / 3) # ce calcul vient après la transform φ précédente
print(f'p1_1: {p1_1}\n')

# first example working directly with the distribution of X:
p1_2 = stats.norm.cdf(6, 4, 3) - stats.norm.cdf(2, 4, 3) # 6 et 2 :bornes sup et inf, 4:μ et 3:σ
print(f'p1_2: {p1_2}\n')

# second example:transformer un calcul de prob complexe en une suite de prob cumulées faciles à calculer
# Ce deuxième exemple calcule P(|X| >2)= P(X>2)+ P(X < -2).  or P(X>2)=1- P(X<2), donc  P(|X| >2)= 1- P(X<2)  +P(X < -2) 
# hr : le princ est d'avoir des P(X<à des valeurs) pour utiliser la fonction des prob cumulées.
p2 = 1 - stats.norm.cdf(2, 4, 3) + stats.norm.cdf(-2, 4, 3)
print(f'p2: {p2}\n')


#Script 1.34: CDF-figure.py  (Générer dist binomiale et dist continue, leurs CDF et plots)
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

# binomial:Générer la distrib, sa PMF (CDF plutôt?) et son graph
# support of binomial PMF:1000 points entre -1 et 10
x_binom = np.linspace(-1, 10, num=1000) # Génèrer 1000 valeurs entre -1 et 10

# PMF for all these values: C'est très certainement CDF et non PMF
cdf_binom = stats.binom.cdf(x_binom, 10, 0.2) # n=10 (nbre de tirage), p=0.2

# plot:
plt.step(x_binom, cdf_binom, linestyle='-', color='black')
plt.xlabel('x')
plt.ylabel('Fx')
plt.savefig('PyGraphs/CDF-figure-discrete.pdf')
plt.close()

# normal:Générer la distrib, sa PDF (ou plutôt sa CDF?) et son graph
# support of normal density:
x_norm = np.linspace(-4, 4, num=1000)

# PDF (CDF plutôt?) for all these values:
cdf_norm = stats.norm.cdf(x_norm)

# plot:
plt.plot(x_norm, cdf_norm, linestyle='-', color='black')
plt.xlabel('x')
plt.ylabel('Fx')
plt.savefig('PyGraphs/CDF-figure-cont.pdf')


#Script 1.35: Quantile-example.py: calculer q-quantile X suit N(0,1) : x[0,975] ≈ 1,96
import scipy.stats as stats

q_975 = stats.norm.ppf(0.975)  # quantile 0,975: x_{0,975} est 1,96
print(f'q_975: {q_975}\n')


#Script 1.36 : smpl-bernoulli.py (avec rvs de scipy, générer échant à 2 issues possibles (P et F) taille n=10 )
import scipy.stats as stats

sample = stats.bernoulli.rvs(0.5, size=10)
print(f'sample: {sample}\n')



#Script 1.37: smpl-norm.py(générer avec scipy un échantillon de 10 éléments qui suivra un loi normale)
import scipy.stats as stats

sample = stats.norm.rvs(size=10)
print(f'sample: {sample}\n')



#Script 1.38: Random-Numbers.py: avec "seed", obtenir des échantillons aléatoires identiques 
import numpy as np
import scipy.stats as stats

# sample from a standard normal RV with sample size n=5:
sample1 = stats.norm.rvs(size=5)
print(f'sample1: {sample1}\n')

# a different sample from the same distribution:
sample2 = stats.norm.rvs(size=5)
print(f'sample2: {sample2}\n')

# set the seed of the random number generator and take two samples:
np.random.seed(6254137)
sample3 = stats.norm.rvs(size=5)
print(f'sample3: {sample3}\n')

sample4 = stats.norm.rvs(size=5)
print(f'sample4: {sample4}\n')

# reset the seed to the same value to get the same samples again:
np.random.seed(6254137)
sample5 = stats.norm.rvs(size=5)
print(f'sample5: {sample5}\n')

sample6 = stats.norm.rvs(size=5)
print(f'sample6: {sample6}\n')



#Script 1.39: Example-C-2.py effet d'une subvention sur l'évolution taux de rebuts (calcul IC)

import numpy as np
import scipy.stats as stats

# manually enter raw data from Wooldridge, Table C.3: Taux de rebuts 87 et 88
SR87 = np.array([10, 1, 6, .45, 1.25, 1.3, 1.06, 3, 8.18, 1.67,
                 .98, 1, .45, 5.03, 8, 9, 18, .28, 7, 3.97])
SR88 = np.array([3, 1, 5, .5, 1.54, 1.5, .8, 2, .67, 1.17, .51,
                 .5, .61, 6.7, 4, 7, 19, .2, 5, 3.83])

# calculate change:variation taux de rebuts de l'échantillon
Change = SR88 - SR87

# ingredients to CI formula:
avgCh = np.mean(Change) # moyenne des variations des taux de rebuts
print(f'avgCh: {avgCh}\n')

n = len(Change)  # taille de l'échantillon
sdCh = np.std(Change, ddof=1) # écart type de l'échantillon
se = sdCh / np.sqrt(n) # erreur type sur la moyenne de l'échantillon
print(f'se: {se}\n')

c = stats.t.ppf(0.975, n - 1)  # quantile c0,025 de la Dist t à n-1 ddl
print(f'c: {c}\n')

# confidence interval:
lowerCI = avgCh - c * se # ybar- c0,025*se(ybar)
print(f'lowerCI: {lowerCI}\n')

upperCI = avgCh + c * se # ybar + c0,025*se(ybar)
print(f'upperCI: {upperCI}\n')



#Script 1.40: Example-C-3.py : estimer la Discrim raciale moyenne par calcul de  l'IC à 95% et à 99%
import wooldridge as woo
import numpy as np
import scipy.stats as stats

audit = woo.dataWoo('audit')
y = audit['y']

# ingredients to CI formula:
avgy = np.mean(y)
n = len(y)
sdy = np.std(y, ddof=1)
se = sdy / np.sqrt(n)
c95 = stats.norm.ppf(0.975)
c99 = stats.norm.ppf(0.995)

# 95% confidence interval:
lowerCI95 = avgy - c95 * se
print(f'lowerCI95: {lowerCI95}\n')
upperCI95 = avgy + c95 * se
print(f'upperCI95: {upperCI95}\n')

# 99% confidence interval:
lowerCI99 = avgy - c99 * se
print(f'lowerCI99: {lowerCI99}\n')

upperCI99 = avgy + c99 * se
print(f'upperCI99: {upperCI99}\n')



#Script 1.41: Critical-Values-t.py  (tests t pour une hyp sur moy (taux de rebuts) d'une var aléat normalt distribuée) 
import numpy as np
import pandas as pd
import scipy.stats as stats

# degrees of freedom = n-1:
df = 19 # échantillon de 20 taux de rebut et nous en calculons la moyenne.

# significance levels:
alpha_one_tailed = np.array([0.1, 0.05, 0.025, 0.01, 0.005, .001]) # liste les seuils pour test unilatéral.
alpha_two_tailed = alpha_one_tailed * 2 # seuil de signification bilat= seuil unilat * 2

# critical values & table:
CV1 = stats.t.ppf(1 - alpha_one_tailed, df) # valeurs critiques de t pour chq niveau de risque. df = ddl
CV2 = stats.t.ppf(1 - alpha_two_tailed, df) # la formule donne la valeur de t telle que Prob d'être au-dessus est alpha_one tailled
table = pd.DataFrame({'alpha_one_tailed': alpha_one_tailed,'CV1': CV1,
                      'alpha_two_tailed': alpha_two_tailed, 'CV2': CV2})
print(f'table: \n{table}\n')
#crée et affiche DataFrame présentant : seuil pour test unilat, bilat, et valeurs critiques t correspondantes
# Rem hr : La table ne donne qu'une seule liste de valeurs critiques pour test unilat et bilat. 
# Probablement unilat à multiplier par 2 (à confirmer)


#Script 1.42: Example-C-5.py (discrimination raciale : test t unilatéral sur la Moyenne écarts d'embauche entre N et B)
import wooldridge as woo
import numpy as np
import pandas as pd
import scipy.stats as stats

audit = woo.dataWoo('audit')  #charger le dataFrame "audit"
y = audit['y']  #la col y du taux de discrim (0=absence, 1=discrim positive, -1=discrim négative)

# automated calculation of t statistic for H0 (mu=0):
test_auto = stats.ttest_1samp(y, popmean=0) #effectuer le test t sur l'échantillon y, hypothèse: H0 : popmean=0
t_auto = test_auto.statistic #la statistique t de test_auto dans la variable t_auto
p_auto = test_auto.pvalue # two-sided p value (p.value, pour test bilatéral) de test_auto dans la variable p_auto
print(f't_auto: {t_auto}\n')
print(f'p_auto/2: {p_auto / 2}\n')

# manual calculation of t statistic for H0 (mu=0): t_empirique = bar y/se(bar y)
avgy = np.mean(y) #calcule average y soit bar y
n = len(y)   #taille de l'échantillon de y dans la variable n
sdy = np.std(y, ddof=1) #écart type de y pour 1 ddl
se = sdy / np.sqrt(n) #erreur type de bar y
t_manual = avgy / se # t empirique
print(f't_manual: {t_manual}\n')

# critical values for t distribution with n-1=240 d.f.: t tabulés pour 6 niveaux de risque et test unilatéral
alpha_one_tailed = np.array([0.1, 0.05, 0.025, 0.01, 0.005, .001]) 
CV = stats.t.ppf(1 - alpha_one_tailed, 240)
table = pd.DataFrame({'alpha_one_tailed': alpha_one_tailed, 'CV': CV})
print(f'table: \n{table}\n')



#Script 1.43: Example-C-6.py (Variation taux de rebuts : test t et p-value)
import numpy as np
import scipy.stats as stats
# manually enter raw data from Wooldridge, Table C.3:
SR87 = np.array([10, 1, 6, .45, 1.25, 1.3, 1.06, 3, 8.18, 1.67,
.98, 1, .45, 5.03, 8, 9, 18, .28, 7, 3.97])
SR88 = np.array([3, 1, 5, .5, 1.54, 1.5, .8, 2, .67, 1.17, .51,
.5, .61, 6.7, 4, 7, 19, .2, 5, 3.83])
Change = SR88 - SR87
# automated calculation of t statistic for H0 (mu=0):
test_auto = stats.ttest_1samp(Change, popmean=0)
t_auto = test_auto.statistic
p_auto = test_auto.pvalue
print(f't_auto: {t_auto}\n')
print(f'p_auto/2: {p_auto / 2}\n')
# manual calculation of t statistic for H0 (mu=0):
avgCh = np.mean(Change)
n = len(Change)
sdCh = np.std(Change, ddof=1)
se = sdCh / np.sqrt(n)
t_manual = avgCh / se
print(f't_manual: {t_manual}\n')
# manual calculation of p value for H0 (mu=0):
p_manual = stats.t.cdf(t_manual, n - 1)
print(f'p_manual: {p_manual}\n')


#Script 1.44: Example-C-7.py : calcul automatique et manuel de test t et p-value
import wooldridge as woo
import numpy as np
import pandas as pd
import scipy.stats as stats
audit = woo.dataWoo('audit')
y = audit['y']
# automated calculation of t statistic for H0 (mu=0):
test_auto = stats.ttest_1samp(y, popmean=0)
t_auto = test_auto.statistic
p_auto = test_auto.pvalue
print(f't_auto: {t_auto}\n')
print(f'p_auto/2: {p_auto/2}\n')
# manual calculation of t statistic for H0 (mu=0):
avgy = np.mean(y)
n = len(y)
sdy = np.std(y, ddof=1)
se = sdy / np.sqrt(n)
t_manual = avgy / se
print(f't_manual: {t_manual}\n')
# manual calculation of p value for H0 (mu=0):
p_manual = stats.t.cdf(t_manual, n - 1)
print(f'p_manual: {p_manual}\n')



#Script 1.45: Adv-Loops.py : utilisation élémentaire de la boucle for (tant que condition) if else
seq = [1, 2, 3, 4, 5, 6]
for i in seq:
    if i < 4:
       print(i ** 3)
    else:
       print(i ** 2)


#Script 1.46: Adv-Loops2.py : utilisation simple de la boucle for...if...else.
seq = [1, 2, 3, 4, 5, 6]
for i in range(len(seq)):
    if seq[i] < 4:
       print(seq[i] ** 3)
    else:
       print(seq[i] ** 2)


#Script 1.47: Adv-Functions.py: définir et appeler une fonction
# define function:
def mysqrt(x):
    if x >= 0:
         result = x ** 0.5
    else:
         result = 'You fool!'
    return result
# call function and save result:
result1 = mysqrt(4)
print(f'result1: {result1}\n')

result2 = mysqrt(-1.5)
print(f'result2: {result2}\n')  


#Script 1.48: Adv-ObjOr.py: création d'une classe, d'une instance et d'une méthode
# use the predefined class 'list' to create an object:
a = [2, 6, 3, 6]

# access a local variable (to find out what kind of object we are dealing with):
check = type(a).__name__
print(f'check: {check}\n')

# make use of a method (how many 6 are in a?):
count_six = a.count(6)
print(f'count_six: {count_six}\n')

# use another method (sort data in a):
a.sort()
print(f'a: {a}\n')


#Script 1.49: Adv-ObjOr2.py (utiliser la méthode dot de numpy dans calcul matriciel (à revoir))
import numpy as np

# multiply these two matrices:
a = np.array([[3, 6, 1], [2, 7, 4]])
b = np.array([[1, 8, 6], [3, 5, 8], [1, 1, 2]])

# the numpy way:
result_np = a.dot(b)
print(f'result_np: \n{result_np}\n')

# or, do it yourself by defining a class:
class myMatrices:
     def __init__(self, A, B):
         self.A = A
         self.B = B

     def mult(self):
         N = self.A.shape[0] # number of rows in A
         K = self.B.shape[1] # number of cols in B
         out = np.empty((N, K)) # initialize output
         for i in range(N):
             for j in range(K):
                 out[i, j] = sum(self.A[i, :] * self.B[:, j])
        return out

# create an object:
test = myMatrices(a, b)

# access local variables:
print(f'test.A: \n{test.A}\n')
print(f'test.B: \n{test.B}\n')

# use object method:
result_own = test.mult()
print(f'result_own: \n{result_own}\n')


#Script 1.50: Adv-ObjOr3.py: méthode pour matrice, héritage et get TotalElem
import numpy as np

# multiply these two matrices:
a = np.array([[3, 6, 1], [2, 7, 4]])
b = np.array([[1, 8, 6], [3, 5, 8], [1, 1, 2]])

# define your own class:
class myMatrices:
     def __init__(self, A, B):
         self.A = A
         self.B = B
     def mult(self):
         N = self.A.shape[0] # number of rows in A
         K = self.B.shape[1] # number of cols in B
         out = np.empty((N, K)) # initialize output
        for i in range(N):
            for j in range(K):
                out[i, j] = sum(self.A[i, :] * self.B[:, j])
        return out

# define a subclass:
class myMatNew(myMatrices):
     def getTotalElem(self):
         N = self.A.shape[0] # number of rows in A
         K = self.B.shape[1] # number of cols in B
         return N * K
     
# create an object of the subclass:
test = myMatNew(a, b)

# use a method of myMatrices:
result_own = test.mult()
print(f'result_own: \n{result_own}\n')

# use a method of myMatNew:
totalElem = test.getTotalElem()
print(f'totalElem: {totalElem}\n')


#Script 1.51: Simulate-Estimate.py. Expérience de simulation(seed-générer échantillon-moyenne échantillon...)
import numpy as np
import scipy.stats as stats

# set the random seed:
np.random.seed(123456)

# set sample size:
n = 100
# draw a sample given the population parameters:
sample1 = stats.norm.rvs(10, 2, size=n)
# estimate the population mean with the sample average:
estimate1 = np.mean(sample1)
print(f'estimate1: {estimate1}\n')
# draw a different sample and estimate again:
sample2 = stats.norm.rvs(10, 2, size=n)
estimate2 = np.mean(sample2)
print(f'estimate2: {estimate2}\n')
# draw a third sample and estimate again:
sample3 = stats.norm.rvs(10, 2, size=n)
estimate3 = np.mean(sample3)
print(f'estimate3: {estimate3}\n')


#Script 1.52: Simulation-Repeated.py (simulation complexe à revoir)
import numpy as np
import scipy.stats as stats

# set the random seed:
np.random.seed(123456)

# set sample size:
n = 100

# initialize ybar to an array of length r=10000 to later store results:
r = 10000
ybar = np.empty(r)

# repeat r times:
for j in range(r):
    # draw a sample and store the sample mean in pos. j=0,1,... of ybar:
    sample = stats.norm.rvs(10, 2, size=n)
    ybar[j] = np.mean(sample)


#Script 1.53: Simulation-Repeated-Results.py (simulation d'une distribution, calculer ses param, graphs)
import numpy as np
import statsmodels.api as sm
import scipy.stats as stats
import matplotlib.pyplot as plt

# set the random seed:
np.random.seed(123456)

# set sample size:
n = 100

# initialize ybar to an array of length r=10000 to later store results:
r = 10000
ybar = np.empty(r)

# repeat r times:
for j in range(r):
    # draw a sample and store the sample mean in pos. j=0,1,... of ybar:
    sample = stats.norm.rvs(10, 2, size=n)
    ybar[j] = np.mean(sample)

# the first 20 of 10000 estimates:
print(f'ybar[0:19]: \n{ybar[0:19]}\n')

# simulated mean:
print(f'np.mean(ybar): {np.mean(ybar)}\n')

# simulated variance:
print(f'np.var(ybar, ddof=1): {np.var(ybar, ddof=1)}\n')

# simulated density:
kde = sm.nonparametric.KDEUnivariate(ybar)
kde.fit()

# normal density:
x_range = np.linspace(9, 11)
y = stats.norm.pdf(x_range, 10, np.sqrt(0.04))

# create graph:
plt.plot(kde.support, kde.density, color='black', label='ybar')
plt.plot(x_range, y, linestyle='--', color='black', label='normal distribution')
plt.ylabel('density')
plt.xlabel('ybar')
plt.legend()
plt.savefig('PyGraphs/Simulation-Repeated-Results.pdf')


#Script 1.54: Simulation-Inference-Figure.py (simulation complexe, à revoir)
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# set the random seed:
np.random.seed(123456)

# set sample size and MC simulations:
r = 10000
n = 100

# initialize arrays to later store results:
CIlower = np.empty(r)
CIupper = np.empty(r)
pvalue1 = np.empty(r)
pvalue2 = np.empty(r)

# repeat r times:
for j in range(r):
    # draw a sample:
    sample = stats.norm.rvs(10, 2, size=n)
    sample_mean = np.mean(sample)
    sample_sd = np.std(sample, ddof=1)
    # test the (correct) null hypothesis mu=10:
    testres1 = stats.ttest_1samp(sample, popmean=10)
    pvalue1[j] = testres1.pvalue
    cv = stats.t.ppf(0.975, df=n - 1)
    CIlower[j] = sample_mean - cv * sample_sd / np.sqrt(n)
    CIupper[j] = sample_mean + cv * sample_sd / np.sqrt(n)
    # test the (incorrect) null hypothesis mu=9.5 & store the p value:
    testres2 = stats.ttest_1samp(sample, popmean=9.5)
    pvalue2[j] = testres2.pvalue
##################
## correct H0 ##
##################
plt.figure(figsize=(3, 5)) # set figure ratio
plt.ylim(0, 101)
plt.xlim(9, 11)
for j in range(1, 101):
    if 10 > CIlower[j] and 10 < CIupper[j]:
       plt.plot([CIlower[j], CIupper[j]], [j, j], linestyle='-', color='grey')
    else:
       plt.plot([CIlower[j], CIupper[j]], [j, j], linestyle='-', color='black')
plt.axvline(10, linestyle='--', color='black', linewidth=0.5)
plt.ylabel('Sample No.')
plt.savefig('PyGraphs/Simulation-Inference-Figure1.pdf')
##################
## incorrect H0 ##
##################
plt.figure(figsize=(3, 5)) # set figure ratio
plt.ylim(0, 101)
plt.xlim(9, 11)
for j in range(1, 101):
    if 9.5 > CIlower[j] and 9.5 < CIupper[j]:
        plt.plot([CIlower[j], CIupper[j]], [j, j], linestyle='-', color='grey')
    else:
        plt.plot([CIlower[j], CIupper[j]], [j, j], linestyle='-', color='black')
plt.axvline(9.5, linestyle='--', color='black', linewidth=0.5)
plt.ylabel('Sample No.')
plt.savefig('PyGraphs/Simulation-Inference-Figure2.pdf')


#Script 1.55: Simulation-Inference.py (simulation complexe, à revoir)
import numpy as np
import scipy.stats as stats

# set the random seed:
np.random.seed(123456)

# set sample size and MC simulations:
r = 10000
n = 100

# initialize arrays to later store results:
CIlower = np.empty(r)
CIupper = np.empty(r)
pvalue1 = np.empty(r)
pvalue2 = np.empty(r)

# repeat r times:
for j in range(r):
    # draw a sample:
    sample = stats.norm.rvs(10, 2, size=n)
    sample_mean = np.mean(sample)
    sample_sd = np.std(sample, ddof=1)
    # test the (correct) null hypothesis mu=10:
    testres1 = stats.ttest_1samp(sample, popmean=10)
    pvalue1[j] = testres1.pvalue
    cv = stats.t.ppf(0.975, df=n - 1)
    CIlower[j] = sample_mean - cv * sample_sd / np.sqrt(n)
    CIupper[j] = sample_mean + cv * sample_sd / np.sqrt(n)
    # test the (incorrect) null hypothesis mu=9.5 & store the p value:
    testres2 = stats.ttest_1samp(sample, popmean=9.5)
    pvalue2[j] = testres2.pvalue
# test results as logical value:
reject1 = pvalue1 <= 0.05
count1_true = np.count_nonzero(reject1) # counts true
count1_false = r - count1_true
print(f'count1_true: {count1_true}\n')
print(f'count1_false: {count1_false}\n')

reject2 = pvalue2 <= 0.05
count2_true = np.count_nonzero(reject2)
count2_false = r - count2_true
print(f'count2_true: {count2_true}\n')
print(f'count2_false: {count2_false}\n')
