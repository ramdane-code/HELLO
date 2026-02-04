```rmd
# template_analyse_panel.Rmd
---
title: "Analyse de Données Panel"
output: html_document
params:
  data_path: "donnees.csv"
  y_var: "Y"
  x_vars: ["X1", "X2"]
---

```{r setup}
source("../01_METHODES_ESTIMATION/PANEL/effets_fixes_basique.R")
```