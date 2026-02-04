Base_c — Résumé et plan d'action
================================

Résumé
------
Le dossier `Base_c` contient principalement :
- Notes Obsidian (Markdown) organisées sous `Mes_Notes/`.
- Fichiers de référence et résumés dans `SOURCES/Heiss R`.
- Templates et scripts R dans `Mes_Notes/04_CODE R/`.

Objectif
--------
Rendre cette base de connaissances plus fonctionnelle et consultable (index, export, automatisation).

Actions proposées
-----------------
1. Ignorer les plugins Obsidian (`.obsidian/`) dans le dépôt (déjà appliqué).
2. Générer un sommaire JSON (`toc_headings.json`) listant les titres des fichiers Markdown.
3. Normaliser les extensions et nettoyer les doublons (`*.md.md`).
4. Extraire un sous-ensemble prioritaire pour analyses détaillées (ex: `Mes_Notes/00_CENTRAL`).

Comment l'utiliser
-------------------
- Le fichier `toc_headings.json` permet d'alimenter un UI ou un script d'indexation.
- Un script PowerShell `Base_c/generate_toc.ps1` est fourni pour régénérer le sommaire.

Prochaines étapes recommandées
-----------------------------
- Valider les fichiers sensibles à exclure (données privées) avant partage.
- Mettre en place un job git périodique (cron / scheduled task) pour regénérer le sommaire.
