```r
# Exemple: PANEL/effets_fixes_basique.R
template_effets_fixes <- function(data, y_var, x_vars, 
                                   entity_var, time_var) {
  library(fixest)
  library(modelsummary)
  
  # Formule dynamique
  formule <- as.formula(paste(y_var, "~", 
                             paste(x_vars, collapse = " + "),
                             "|", entity_var, "+", time_var))
  
  # Estimation
  model <- feols(formule, data = data)
  
  # Diagnostics automatiques
  diag <- diagnostiquer_modele(model, data)
  
  # Table de résultats
  table <- modelsummary(list("Effets Fixes" = model),
                        output = "latex")
  
  return(list(modele = model, 
              diagnostics = diag,
              table = table))
}
```