# Heiss 13 et 14. Panels_Fr
- Générer un échantillon poolé de 2 années (1978 et 1985) par le biais d'une variable muette [[SOURCES/Heiss R/Heiss 13 et 14. Data en coupe transversales poolées et Panels_Fr|Heiss 13 et 14. Data en coupe transversales poolées et Panels_Fr#^y85]]
- $β_1$ : rendt educ 78 et $β_1+δ_1$ : rendt educ 85 dans $lwage = \beta_0 + \delta_0 y85 + \beta_1 educ + \delta_1 (y85 /cdot educ)$ : [[SOURCES/Heiss R/Heiss 13 et 14. Data en coupe transversales poolées et Panels_Fr|Heiss 13 et 14. Data en coupe transversales poolées et Panels_Fr#^δ1]]
- Utiliser des variables transformées : <font color="#ff0000">I</font>((exper^2)/100) : diviser exper² par 100 multiplie $β_3$ par 100.
- La transformation log pour obtenir des effets en % (y augmente de 5%,,,) [[SOURCES/Heiss R/Heiss 13 et 14. Data en coupe transversales poolées et Panels_Fr|Heiss 13 et 14. Data en coupe transversales poolées et Panels_Fr#^2e761f]]
- Stargazer pour afficher en parallèle l'output de 2 rég : [[SOURCES/Heiss R/Heiss 13 et 14. Data en coupe transversales poolées et Panels_Fr|Heiss 13 et 14. Data en coupe transversales poolées et Panels_Fr#^74e7c9]]
- Créer un pdata.frame équilibré (n,T) [[SOURCES/Heiss R/Heiss 13 et 14. Data en coupe transversales poolées et Panels_Fr|Heiss 13 et 14. Data en coupe transversales poolées et Panels_Fr#^fcf4b6]]
- Afficher nbre choisi d'obs de col. choisie[[SOURCES/Heiss R/Heiss 13 et 14. Data en coupe transversales poolées et Panels_Fr|Heiss 13 et 14. Data en coupe transversales poolées et Panels_Fr#^obsETcol]]
- Calcul sur  variables de panel (et print "collectif") : lag(x), diff(x), between(x), within(x) [[SOURCES/Heiss R/Heiss 13 et 14. Data en coupe transversales poolées et Panels_Fr|Heiss 13 et 14. Data en coupe transversales poolées et Panels_Fr#^8b2fb9]]
- Paramètres pour semi log : si log(wage)$\sim$ F...  donne Coef= -0,37 cela signifie que wage_F = `exp(-0.37)-1 ≈ -27.1%` de moins que wage_H (il s'agit d'une dummy var) [[SOURCES/Heiss R/Heiss 13 et 14. Data en coupe transversales poolées et Panels_Fr|Heiss 13 et 14. Data en coupe transversales poolées et Panels_Fr#^66e961]]
# Heiss 15. Variables instrumentales
- Estimation de $β_1$ par OLS :  $\hat{\beta}_1^{OLS} = \frac{\text{Cov}(x,y)}{\text{Var}(x)}$ et par IV : $\hat{\beta}_1^{IV} = \frac{\text{Cov}(z, y)}{\text{Cov}(z, x)}. \tag{15.2}$ [[SOURCES/Heiss R/Heiss 15. Variables instrumentales|Heiss 15. Variables instrumentales#^521849]]
- Subset : extraire d'une var (col wage), une var sans obs manquantes (col "oursample") : oursample <- subset(mroz, !is.na(wage)) [[SOURCES/Heiss R/Heiss 15. Variables instrumentales|Heiss 15. Variables instrumentales#^54be7e]]
- Calcul Taux de mort…10000hab : Fatalities$ fatal_rate <- Fatalities$fatal / Fatalities $pop * 10000 $ [[ITER.10-Régression avec données de Panel (rwpd)#^121489]]
- Calculer la Moyenne de chq élément d'un groupe : Moy <- ave(Fatalities$income, "state") + Calcul de données centrées [[ITER.10-Régression avec données de Panel (rwpd)#^5b5c71]]
- 
- 
- 
- 










