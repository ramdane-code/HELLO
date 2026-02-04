import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import warnings
warnings.filterwarnings('ignore')

# Chargement des données (adapter si le nom du fichier et de la col changent)
file_path = r"C:\Users\ramda\Desktop\PibpHab.xlsx" # Mettez à jour ce chemin si nécessaire

try:
    # Lecture sans index pour voir les colonnes disponibles
    df_temp = pd.read_excel(file_path)
    print("Colonnes disponibles:", df_temp.columns.tolist())
    
    # Définir le nom de la colonne d'année (ajustez selon votre fichier)
    year_column = 'Year'  # Changez ceci si nécessaire (ex: 'Année', 'Date', etc.)

    # Relire avec la colonne d'année comme index
    df = pd.read_excel(file_path, index_col=year_column)

    # Récupérer la série pibpHab # 
    if 'PibpHab' in df.columns:
        series = df['PibpHab']
    else:
        # Si la colonne n'a pas le nom attendu, prenez la première colonne numérique
        series = df.iloc[:, 0]
        print(f"Utilisation de la colonne: {df.columns[0]}")
    
    # Nettoyage des données (suppression des valeurs manquantes)
    series = series.dropna()
    
    print(f"Nombre d'observations: {len(series)}")
    print(f"Période: {series.index[0]} à {series.index[-1]}")
    print(f"Valeurs statistiques:\n{series.describe()}")
    
    # Création de la figure avec les corrélogrammes
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    # Corrélogramme ACF (Autocorrelation Function)
    plot_acf(series, ax=ax1, lags=min(20, len(series)//2), alpha=0.05)
    ax1.set_title('Fonction d\'Autocorrélation (ACF) - PibpHab', fontsize=14)
    ax1.set_ylabel('Corrélation')
    
    # Corrélogramme PACF (Partial Autocorrelation Function)
    plot_pacf(series, ax=ax2, lags=min(20, len(series)//2), alpha=0.05, method='ywm')
    ax2.set_title('Fonction d\'Autocorrélation Partielle (PACF) - PibpHab', fontsize=14)
    ax2.set_ylabel('Corrélation Partielle')
    ax2.set_xlabel('Décalages (Lags)')
    
    plt.tight_layout()
    plt.show()
    plt.savefig('PyGraphs/ACF_PACF_PibpHab.pdf')
    
    # Affichage de la série temporelle
    plt.figure(figsize=(12, 6))
    plt.plot(series.index, series.values, marker='o', linewidth=2, markersize=4)
    plt.title('Série Temporelle - PibpHab', fontsize=14)
    plt.xlabel('Temps')
    plt.ylabel('PibpHab')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    plt.savefig('PyGraphs/PibpHab.pdf') 

except FileNotFoundError:
    print(f"Erreur: Le fichier {file_path} n'a pas été trouvé.")
    print("Vérifiez le chemin d'accès et le nom du fichier.")
    
except Exception as e:
    print(f"Une erreur s'est produite: {e}")
    print("\nDépannage:")
    print("1. Vérifiez que le fichier Excel existe bien à l'emplacement spécifié")
    print("2. Vérifiez que la colonne 'PibpHab' existe dans le fichier")
    print("3. Vérifiez que les données sont numériques")
    print("4. Si le nom de colonne est différent, modifiez le script en conséquence")