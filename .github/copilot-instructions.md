# Copilot Instructions for This Workspace

## Vue d'ensemble
Ce workspace est centré sur l'analyse de données avec Python, principalement via la bibliothèque Pandas. Il contient des scripts, des notebooks, des jeux de données et des tutoriels pour l'apprentissage et la manipulation de données.

## Structure principale
- `Autres/complete-pandas-tutorial-master/` : Tutoriel complet sur Pandas, avec des notebooks, des scripts, des données d'exemple et un README détaillé.
- `MesData/` : Jeux de données supplémentaires, souvent utilisés dans les notebooks et scripts.
- `MesScripts/` et `WooScripts/` : Scripts Python pour l'analyse, la manipulation ou l'exploration de données.
- `PyGraphs/` : Probablement des scripts ou notebooks pour la visualisation de données.

## Conventions et patterns
- Les notebooks (`.ipynb`) sont utilisés pour des tutoriels interactifs et des analyses exploratoires.
- Les scripts Python (`.py`) sont organisés par thème ou chapitre, souvent pour des analyses spécifiques ou des exercices.
- Les données sont stockées dans des sous-dossiers `data/`, `datasets/` ou directement dans le dossier principal du tutoriel.
- Les noms de fichiers et de dossiers sont explicites : ils reflètent le contenu ou le chapitre traité.

## Workflows critiques
- **Installation des dépendances** :
  - Utiliser `pip install -r requirements.txt` dans le dossier du tutoriel pour installer les librairies nécessaires.
  - Les environnements virtuels sont recommandés (`python -m venv myenv`, puis activation selon l'OS).
- **Exécution des notebooks** :
  - Ouvrir les fichiers `.ipynb` dans VS Code ou lancer `jupyter notebook` pour une interface web.
- **Chargement des données** :
  - Les scripts et notebooks chargent les données via `pd.read_csv`, `pd.read_parquet`, etc. Les chemins sont relatifs au dossier du script ou notebook.
- **Manipulation avancée** :
  - Utilisation fréquente de `groupby`, `pivot`, `merge`, `concat`, et gestion des valeurs manquantes (`fillna`, `dropna`).
  - Les notebooks montrent des exemples concrets de ces opérations.

## Points d'intégration et dépendances
- **Pandas** est la dépendance centrale. D'autres librairies comme NumPy ou PyArrow peuvent être utilisées pour des opérations avancées ou des optimisations.
- Les données sont locales, mais certains notebooks peuvent être adaptés pour Google Colab.

## Exemples de patterns spécifiques
- Les notebooks du tutoriel (`tutorial.ipynb`, `Pandas Data Science Tutorial.ipynb`) illustrent les bonnes pratiques Pandas : création de DataFrame, filtrage, agrégation, fusion, gestion des valeurs manquantes, etc.
- Les scripts dans `WooScripts/` et `MesScripts/` sont souvent indépendants et peuvent être exécutés séparément pour des analyses ciblées.

## Conseils pour agents IA
- Toujours vérifier le chemin des fichiers de données lors de la génération de code.
- Respecter la structure des dossiers pour faciliter la réutilisation des scripts et des données.
- S'inspirer des exemples du tutoriel pour proposer des manipulations Pandas idiomatiques.
- Documenter les workflows spécifiques (ex : activation d'environnement, installation des dépendances) dans les réponses si pertinent.

---

Pour toute ambiguïté ou besoin d'exemples supplémentaires, demander à l'utilisateur des précisions sur le workflow ou le script cible.
