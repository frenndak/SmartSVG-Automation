# SmartSVG — Architecture d'automatisation et contre-expertise

```text
SmartSVG-Automation (PUBLIC)                       SmartSVG-Studio (PRIVÉ)
  cron :05 UTC / phase develop  ───────────────>  repository_dispatch smartsvg-cycle
  cron :50 UTC / phase repair   ───────────────>  private-ai-development.yml
  workflow_dispatch dry_run=true                  preflight de provenance / READY / PR WIP=1
  aucune source privée ni API OpenAI               Codex + tests sur branche privée
                                                   PR privée en brouillon
                                                   workflow_dispatch G0 + CPU sur HEAD

ChatGPT — tâche de revue indépendante chaque heure :35 (Europe/Paris)
  relit PR auto et SHA exacts, rapports CI et code ;
  publie NO GO + correctif reproductible et label de réparation si nécessaire,
  ou GO conditionnel pour revue humaine ; aucun auto-merge.
```

## Sécurité et invariants

Le dépôt public ne possède que le jeton de **dispatch**. Il n'exécute ni source privée, ni Codex, ni tests avec artefacts confidentiels. Le privé conserve son propre `OPENAI_API_KEY`, `engine/`, les tests et les branches de travail.

- Roadmap V3.2 gelée : `0e503a55fa622d7acea44d8e742205fb6a71119262c309a0b5a2bd48f0ab28a3`.
- Source originale V21.15.2 : `9369656f0216cebb6dccce0d0155bffa16d8c384da6a984bf848cdd8aa003c54`, archive immuable sous `source-releases/`.
- `engine/` est une **copie de travail évolutive** : son changement via PR est autorisé ; il ne doit pas modifier l'archive de référence.
- Les PR automatiques respectent WIP=1 entre branches `smartsvg/auto-*` ; une PR humaine indépendante ne bloque pas le traitement de la PR autonome.
- Réparation déclenchée seulement avec une demande explicite sous label `bug` ou `smartsvg:repair`, retirée **avant** d'utiliser l'API payante. Un défaut P0/P1 doit être vérifié sur le SHA HEAD ; les PR non automatiques ne sont jamais corrigées par ce worker.
- Les PR créées avec `GITHUB_TOKEN` peuvent nécessiter un `workflow_dispatch` explicite pour les tests. La publication d'un dispatch n'est pas une preuve de succès, et l'approbation d'une PR ne découle jamais d'un check ancien.
- Mode manuel sûr : `dry_run=true` sur le public, `execute=false` sur le privé. Ils permettent de tester les garde-fous **sans appel Codex**.
- L0 documentation ; L1 CPU/synthétique ; L2 ComfyUI/GPU matériel ; L3 Design Space / Cricut physique. L1 ne suffit jamais à prétendre L2/L3.

## Performances et coûts

Les tâches GitHub planifiées sont **best effort** : possibles retards/suppressions. Les minutes privées GitHub et l'API OpenAI peuvent être facturées, distinctement. Le WIP=1 et la demande de réparation consommable évitent des boucles de coûts ; ils ne constituent pas une limite budgétaire universelle.

## Ordonnancement

Chaque heure, à la minute **:05 UTC**, le développeur peut ouvrir un candidat. À **:35 en Europe/Paris**, l'auditeur vérifie les changements observables. À **:50 UTC**, le worker répare seulement si le label de défaut a été apposé sur une PR automatisée. CET/CEST décale l'heure mais pas la minute ; les retards GitHub et la durée de Codex peuvent modifier l'ordre effectif. En cas de PR ou tests encore en cours, l'auditeur classe les preuves en attente, pas comme PASS.
