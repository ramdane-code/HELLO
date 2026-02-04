Usage
-----

Script: `WooScripts/display_mroz.py`

But: ce script est générique et affiche/exporte n'importe quel dataset du package `wooldridge`.
Exemples (PowerShell, exécuter depuis la racine du workspace) :

# Afficher `mroz` et exporter vers le Bureau (CSV + XLSX)
```
.\.venv\Scripts\python.exe .\WooScripts\display_mroz.py --dataset mroz
AfficherDansExcel
------------------

But : exporter la totalité d'un dataset `wooldridge` vers Excel (ou CSV) sur le Bureau,
sans lancer d'application, et fournir un affichage contrôlé dans le terminal.

Script : `WooScripts/display_inxl.py` (générique)

Exemples (PowerShell, exécuter depuis la racine du workspace) :
Afficher et exporter `mroz` (Excel par défaut) :
```
.\.venv\Scripts\python.exe .\WooScripts\display_inxl.py --dataset mroz
```

Afficher `recid`, limiter l'affichage terminal à 100 lignes :
```
.\.venv\Scripts\python.exe .\WooScripts\display_inxl.py --dataset recid --max-rows 100
```

Afficher sans exporter :
```
.\.venv\Scripts\python.exe .\WooScripts\display_inxl.py --dataset recid --no-export
```

Exporter en CSV seulement vers un dossier précis :
```
.\.venv\Scripts\python.exe .\WooScripts\display_inxl.py --dataset recid --format csv --export-dir "C:/Users/ramda/Documents/Exports"
```

Remarques:
- L'export Excel utilise `openpyxl` (installé dans ton venv).
- Par défaut le script écrit le fichier Excel/CSV dans le Bureau de l'utilisateur.
- Le fichier Excel contient la totalité du DataFrame (toutes les lignes et colonnes).
- Pour éviter d'afficher des milliers de lignes, contrôle `--max-rows` (0 = pas d'affichage).

Souhaites-tu que j'ajoute aussi une option `--head N` pour afficher exactement N lignes (au lieu de `--max-rows`)?

Options ajoutées:
- `--head N` : afficher exactement les N premières lignes (prend le pas sur `--max-rows`).
- `--index`  : inclure l'index du DataFrame dans les fichiers exportés (CSV/XLSX).

Exemple : afficher 10 premières lignes et inclure l'index dans l'export Excel :
```
.\.venv\Scripts\python.exe .\WooScripts\display_inxl.py --dataset recid --head 10 --index
```
