import wooldridge as woo
import pandas as pd

# Importer CSV avec Pandas :

df1 = pd.read_csv('data/wage1.csv.bz2', delimiter=',', header=None, 
                  names=['année', 'product1', 'product2', 'product3'])
print(f'df1 : \n{df1}\n')


