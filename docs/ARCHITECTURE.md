# SmartSVG — Architecture de développement et de contre-expertise

```text
SmartSVG-Automation (PUBLIC)
  HH:20 UTC: schedule -> repository_dispatch (develop)
  HH:50 UTC: schedule -> repository_dispatch (repair)
  // Aucun checkout de moteur, aucun appel OpenAI, aucune sortie privée

SmartSVG-Studio (PRIVÉ)
  -> provenance ZIP et manifestes contrôlés
  -> readiness gate + roadmap SHA + WIP=1
  -> Codex sur checkout privé, tests, changements contrôlés
  -> nouvelle PR privée en brouillon, ou correction de la PR existante

Tâche GPT indépendante (Europe/Paris, HH:10)
  -> inspecter PR, commits et Actions réels
  -> analyse P0/P1/P2, ergonomie Express, compatibilité ComfyUI/Cricut
  -> commentaire de revue traçable, sans fausse preuve matérielle
```

## Invariants

La roadmap V3.2 reste figée : `0e503a55fa622d7acea44d8e742205fb6a71119262c309a0b5a2bd48f0ab28a3`. L'archive candidate V21.15.2 est `9369656f0216cebb6dccce0d0155bffa16d8c384da6a984bf848cdd8aa003c54`.

Les fichiers PNG pour Print Then Cut ne sont pas des SVG multicouches éditables ; SVG de silhouette et SVG de composition ont des critères de qualité différents. Ne pas prétendre disposer d'un moteur de pilotage Cricut alternatif ni garantir une découpe physique.

## Coûts et limites

Le déclencheur public emploie un runner public sans accès au code privé. Les traitements privés utilisent des minutes de runners privés (selon ton forfait GitHub) ou un runner auto-hébergé, en plus de l'API IA payante. Le planificateur GitHub fonctionne en effort raisonnable, pas comme une horloge temps réel ; WIP=1 et les vérifications peuvent légitimement suspendre une phase.

## Reprise

Une correction du code se fait sur la même PR privée ; le prochain cycle indépendant doit se baser sur les traces et non seulement sur les déclarations de l'agent. L'approbation/fusion nécessite validation indépendante des tests et du périmètre.
