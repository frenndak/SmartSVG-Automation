# Mise en service — SmartSVG V21.15.2

## 1. Source vérifiée, jamais inventée

ZIP utilisateur : `ComfyUI_SmartSVG_Studio_V21_15_2_Installation(1).zip` ; empreinte SHA-256 : `9369656f0216cebb6dccce0d0155bffa16d8c384da6a984bf848cdd8aa003c54`.
Manifeste du ZIP : `INSTALLATION_MANIFEST_V21_15_2.json`, 651 fichiers déclarés et 651 empreintes conformes en contrôle local ; 652 fichiers ZIP au total. L'archive n'est pas encore attestée comme asset d'une Release GitHub privée.

Déposer le ZIP original (nom d'asset sans `(1)`) dans une **Release privée** `smartsvg-v21.15.2-source`. Lancer ensuite le workflow privé `SmartSVG - Import private source release` ; l'import doit contrôler SHA ZIP + manifeste puis ouvrir une PR privée. Il ne crée jamais automatiquement `.automation/READY`.

## 2. Secrets et permissions

Dans **SmartSVG-Studio privé** : ajouter le secret `OPENAI_API_KEY`, vérifier les permissions du `GITHUB_TOKEN` pour Contents et Pull requests en écriture et permettre aux Actions d'ouvrir une PR.

Dans **SmartSVG-Automation public** : secret `SMARTSVG_DISPATCH_TOKEN` uniquement, finement limité au dépôt privé et à l'envoi `repository_dispatch`. Les logs de l'orchestrateur public ne doivent contenir ni code ni artefacts privés.

Dans les **deux dépôts** : variable `SMARTSVG_AUTOMATION_ENABLED=true` seulement après vérifications. Une valeur manquante ou différente de `true` laisse les jobs de développement désactivés.

## 3. Démarrage et arrêt

À HH:20 UTC, phase develop. À HH:50 UTC, phase repair. La tâche GPT à HH:10 Europe/Paris contre-expertise le travail (attention aux heures françaises d'été/hiver).

Le dépôt privé ne démarre aucune modification sans `engine/`, manifeste vérifié, rapport `docs/IMPORT_V21_15_2.json`, roadmap hashée et `.automation/READY`. Aucune validation ComfyUI graphique, RTX 3070 ni découpe Cricut n'est impliquée par les tests CI.

Pour stopper : `SMARTSVG_AUTOMATION_ENABLED=false` dans les deux dépôts et désactiver la tâche GPT si nécessaire. Révoquer rapidement un jeton compromis.

## 4. Diagnostic

- Workflow public skipped : variable absente / désactivée.
- Public 403 : jeton de dispatch non autorisé.
- Dépôt privé skipped : variable privée absente ou jeton de déclenchement non reconnu.
- Gate privé refusé : archive non importée, manifeste absent, référence roadmap ou approbation absente.
- PR sans progression : agent sans modifications sûres, dépendance non disponible ou tests KO ; examiner la PR privée.
- Déclenchement planifié retardé : limite normale de GitHub ; ne pas inventer de résultat.
