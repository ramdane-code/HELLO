---
aliases:
  - "[ ]"
tags:
  - workflow
created: "{{date}}"
links: "[ ]"
---

# WORKFLOW — {{Thème économétrique}}
> Objectif : organiser raisonnement  pb économique → estimation → interprétation causale
---
## 1️⃣ OBJECTIF ÉCONOMIQUE
👉 *Pourquoi on fait ça ?*
- [[_templates/OBJECTIF|OBJECTIF]] {{Question causale principale}}
- Variable d’intérêt :  
- Effet recherché (court / long terme, moyenne, hétérogénéité ?)  
📌 Exemple :  
[[_templates/OBJECTIF|OBJECTIF]] Estimer l’effet causal de X sur Y avec données panel
---
## 2️⃣ PROBLÈME(S) ÉCONOMÉTRIQUE(S)
👉 *Pourquoi l’OLS naïf ne marche pas ?*
Lister explicitement :
- [[PROBLÈME]] Biais de variables omises  
- [[PROBLÈME]] Endogénéité  
- [[PROBLÈME]] Sélection  
- [[PROBLÈME]] Causalité inverse  
✍️ Pour chaque problème :
- Quelle variable pose problème ?
- Pourquoi le biais apparaît ?
---
## 3️⃣ CONCEPT(S) MOBILISÉ(S)
👉 *Quels outils théoriques permettent de répondre au problème ?*
- [[CONCEPT]] {{Méthode principale}}  
- [[CONCEPT]] {{Méthode alternative / comparaison}}
📌 Exemple :
- [[CONCEPT]] Effets fixes
- [[CONCEPT]] Effets aléatoires
---
## 4️⃣ HYPOTHÈSE(S) CLÉS
👉 *Qu’est-ce qu’on doit croire pour identifier l’effet ?*
- [[_templates/HYPOTHÈSE|HYPOTHÈSE]] {{Hypothèse centrale}}
- Hypothèses secondaires :
  - support commun
  - absence de chocs anticipés
  - stabilité temporelle
Pour chaque hypothèse :
- Est-elle testable ?
- Plausible économiquement ?
- Que se passe-t-il si elle est violée ?
---
## 5️⃣ PATTERN(S) DE RAISONNEMENT
👉 *Schémas standards de comparaison / identification*
- [[_templates/PATTERN|PATTERN]] {{Pattern principal}}
- Comparaison implicite :
  - within vs between
  - traité vs contrôle
  - avant vs après
📌 Exemple :
[[_templates/PATTERN|PATTERN]] Comparer within vs between  
→ identification via variation intra-individuelle

---
## 6️⃣ SPÉCIFICATION ÉCONOMÉTRIQUE
👉 *Traduction formelle du raisonnement*
- Modèle estimé :
```math
y_{it} = \beta x_{it} + \alpha_i + \gamma_t + \varepsilon_{it}

- Variables absorbées ?
- Que mesure exactement β ?

## 7️⃣ IMPLÉMENTATION (R / Stata / Python)
👉 _Comment on le fait concrètement_
- [[R]] {{Commande ou fonction clé}}
```r
feols(y ~ x | id + time, data = df)
```
À vérifier :
- colinéarités
- variables invariantes
- clustering des SE
---
## 8️⃣ INTERPRÉTATION CAUSALE
👉 _Que peut-on dire — et ne pas dire ?_
- Interprétation du coefficient
- Population concernée
- Effet local ou global ?
⚠️ Ce que le modèle **n’identifie pas**
---
## 9️⃣ ROBUSTESSES / ALTERNATIVES
👉 _Est-ce que le résultat tient ?_
- Spécifications alternatives
- Méthodes concurrentes :
    - [[CONCEPT]] Diff-in-diff
    - [[CONCEPT]] IV
- Tests de placebo / falsification
---
## 🔟 SYNTHÈSE (1 paragraphe)
👉 _Si tu devais l’expliquer à l’oral ou à l’exam_
> “Le problème principal est […].  
> On utilise […], qui repose sur […].  
> L’effet est identifié grâce à […].  
> Sous l’hypothèse […], on peut interpréter β comme […].”
---
## 🔗 GRAPHE OBSIDIAN — liens attendus
- OBJECTIF ↔ PROBLÈME
- PROBLÈME ↔ CONCEPT
- CONCEPT ↔ HYPOTHÈSE
- CONCEPT ↔ PATTERN
- CONCEPT ↔ R


