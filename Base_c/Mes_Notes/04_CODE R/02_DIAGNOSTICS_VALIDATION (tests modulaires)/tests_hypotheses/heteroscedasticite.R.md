```r
# Exemple: tests_hypotheses/heteroscedasticite.R
tester_heteroscedasticite <- function(model) {
  library(lmtest)
  
  tests <- list(
    breusch_pagan = bptest(model),
    white = bptest(model, ~ fitted(model) + I(fitted(model)^2)),
    score = ncvTest(model)
  )
  
  # Recommandation automatique
  if (tests$breusch_pagan$p.value < 0.05) {
    message("Hétéroscédasticité détectée. Utiliser des erreurs robustes.")
  }
  
  return(tests)
}
```