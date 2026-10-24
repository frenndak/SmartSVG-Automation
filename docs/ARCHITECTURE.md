# SmartSVG — Architecture d'orchestration

## Frontières de responsabilité

- **Dépôt public** : déclencheur planifié, politiques non confidentielles, diagnostics de disponibilité et CI du déclencheur. Il ne doit contenir ni moteur SmartSVG, ni archive de release, ni jeux de données utilisateurs.
- **Dépôt privé** : code de SmartSVG, roadmap V3.2 figée, baseline historique, corpus de validation, rapports détaillés, outils de vérification et pull requests.
- **Agent GPT horaire** : contre-expertise externe, examen des diffs réels, commentaires ciblés dans les PR privées si les droits le permettent.
- **Codex GitHub Actions** : seulement après import et validation de V21.15.2, avec clé API facturée séparément et jeton GitHub limité au dépôt privé.

## Cycle et ordre prévu

```text
20 / 50 min UTC : GitHub schedule (best effort)
  -> vérifier deux variables de consentement et les secrets
  -> checkout privé et SHA de la roadmap
  -> vérifier engine/smartsvg_ai + .automation/READY
  -> éviter une deuxième PR ouverte
  -> exécuter un micro-lot Codex autorisé
  -> tests locaux, modifications uniquement sur branche
  -> créer une PR brouillon dans SmartSVG-Studio

15 min chaque heure : audit GPT indépendant
  -> lire les modifications réelles et résultats de CI
  -> relever P0/P1/P2 et les risques
  -> consigner des corrections vérifiables dans la PR privée
```

**Attention :** le fonctionnement continu est conditionnel. En l'état, la règle WIP=1 empêche de relancer Codex lorsqu'une PR reste ouverte. Un processus de revue/fusion ou de révision sur la même branche est nécessaire pour augmenter la cadence réelle. Ce compromis évite des développements divergents et des fusions aveugles.

## Confidentialité, runners et facturation

Un dépôt public bénéficie de minutes GitHub Actions standards gratuites selon les conditions GitHub, mais **son historique de jobs et ses logs sont publics**. Charger du code source privé dans un runner public est une décision sensible. Les secrets GitHub masquent certaines chaînes, pas tous les dérivés de code, traces, noms de fichiers ou sorties de commandes. Les variables explicites `SMARTSVG_AUTOMATION_ENABLED` et `SMARTSVG_PUBLIC_RUNNER_RISK_ACCEPTED` restent donc des garde-fous obligatoires.

Pour confidentialité stricte, déplacer **le travail IA** vers un workflow exécuté en privé ou vers un runner autosuffisant contrôlé personnellement et laisser le public comme orchestrateur de cadence, même si le coût/exploitation change. **Ne pas publier les logs, artefacts ou rapports du moteur dans ce dépôt.**

## Gates de qualité

G0 : vérification de l'archive de référence, manifeste interne et non-régression ; G1 : inventaire du graphe et des anciens nœuds ComfyUI ; G2 : interface Express ; G3+ : extraction/IA et fabrication selon roadmap V3.2. Aucun résultat SVG/PDF/PNG ne vaut preuve d'import ou de découpe Cricut avant un essai matériel indépendant.
