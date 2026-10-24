# SmartSVG Automation — Déclencheur public sécurisé

Ce dépôt est **public** et sert uniquement à cadencer les cycles SmartSVG. Aucun code, image utilisateur, fichier PNG/SVG confidentiel, clé OpenAI ou modèle IA n'est lu/exécuté ici.

## Cycle validé

- À **HH:05 UTC**, `.github/workflows/development-cycle.yml` signale `develop` au dépôt privé.
- À **HH:50 UTC**, il signale `repair` : révision de la PR privée courante uniquement.
- À **HH:35 (Europe/Paris)**, la tâche ChatGPT fait la contre-expertise indépendante des diff/CI réels.
- GitHub peut retarder ou omettre une exécution planifiée. Un déclenchement ne garantit pas une modification.

## Préparation et activation

1. Importer l'authentique archive V21.15.2 dans `frenndak/SmartSVG-Studio` via une Release **privée** et le workflow d'import privé. SHA-256 du ZIP : `9369656f0216cebb6dccce0d0155bffa16d8c384da6a984bf848cdd8aa003c54`.
2. Vérifier les 651 empreintes du manifeste, les tests, les signatures des nœuds et les sorties ; fusionner la PR d'import uniquement après examen.
3. Dans le dépôt **privé**, définir le secret `OPENAI_API_KEY` (API facturée indépendamment de ChatGPT/Copilot), et ajouter `.automation/READY` seulement après contrôle de provenance.
4. Dans ce dépôt **public**, définir uniquement `SMARTSVG_DISPATCH_TOKEN` (jeton GitHub finement limité à la capacité de `repository_dispatch` du seul dépôt privé). **Ne pas** mettre l'API OpenAI dans le public.
5. Mettre `SMARTSVG_AUTOMATION_ENABLED=true` en variable Actions dans **chaque dépôt**, après vérification de la facturation/permissions.
6. Exécuter une fois manuellement le workflow public et vérifier le travail reçu dans les Actions du dépôt privé. Observer les premiers cycles et désactiver la variable en cas d'anomalie.

## Protections

Chaque cycle privé reste soumis aux gates de provenance, à WIP=1, aux changements de chemins interdits, aux tests locaux et à la création d'une PR privée. Aucun merge automatique par Codex et aucune certification machine sans essai physique.

Ce dépôt contient seulement les politiques d'orchestration, tests statiques et exemples **synthétiques**. Contact sécurité : utiliser l'option privée de signalement des vulnérabilités GitHub si disponible.
