from WooChap1 import script1, script2, script3, script24, script216
import wooldridge as woo
import numpy as np

if __name__ == '__main__':
    ceosal1 = woo.dataWoo('ceosal1')  #Necessaire dans Script1 mais extraite pour ici car on a besoin de charger ceosal1, ici.
    # Affiche les attributs de l'objet ceosal1, utile pour comprendre la structure des données.
    b1, b0 = script1(ceosal1)   # C'est un appel à la fonction script1 du fichier WooChap1.py et importée dans ce fichier. Elle calcule b1 et b0.
    print(f'b1: {b1}\n') 
    print(f'b0: {b0}\n')    #Ces 3 derniers résultats peuvent être stockés pour utilisation ultérieure.
  
    b = script2(ceosal1)    # b est la variable qui résume le résultat de la régression linéaire simple.
    print(f'b from script2: {b}\n')
    
    results = script3(ceosal1)
    print(results.summary())  # Affiche le résumé de la régression

    b = script24(woo.dataWoo('wage1'))
    print(f'b from script24: {b}\n')
    seed = np.random.seed(1234567)
    n = 1000

    r = 10000
    beta0 = 1
    beta1 = 0.5
    su = 2
    b0, b1 = script216(seed, n, r, beta0, beta1, su)
    print(f'b0: {b0}\n')
    print(f'b1: {b1}\n')
    
    
