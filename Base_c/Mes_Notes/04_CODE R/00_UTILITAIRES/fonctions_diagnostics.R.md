Fonction réutilisables

```r
# Exemple: fonctions_diagnostics.R
diagnostiquer_modele <- function(model, data) {
  # Retourne une liste avec tous les tests
  resultats <- list(
    heteroscedasticite = bptest(model),
    normalite = jarque.bera.test(residuals(model)),
    vif = vif(model)
  )
  return(resultats)
}
```