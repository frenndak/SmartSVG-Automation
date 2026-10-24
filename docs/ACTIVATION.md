# Mise en service progressive de SmartSVG

## État initial

Par défaut : **désactivé**. Ne pas activer tant que le dépôt privé ne contient pas réellement `engine/smartsvg_ai`, ses tests et la roadmap V3.2 complète.

## Vérifications préalables

1. Depuis le dépôt privé, examiner et fusionner les changements G0 de la PR #1 après CI verte et contre-expertise.
2. Déposer **l'archive originale V21.15.2** en asset d'une *release privée* sous le nom exact `ComfyUI_SmartSVG_Studio_V21_15_2_Installation.zip`. Les images utilisateur ne doivent pas être publiées dans ce dépôt public.
3. Lancer manuellement le workflow privé `SmartSVG - Import private source release`. Il ouvre une PR *draft*, **sans activer l'IA**.
4. Valider l'empreinte de l'archive, le manifeste interne, les nœuds ComfyUI et les tests existants ; examiner les chemins PNG/SVG et garder la version B0 gelée inchangée.
5. Une fois la branche d'import fusionnée, créer manuellement et documenter `.automation/READY` dans le dépôt privé, avec version, empreinte source et approbation.
6. Dans ce dépôt public, aller dans **Settings → Secrets and variables → Actions**. Ajouter en *secrets* : `SMARTSVG_PRIVATE_REPO_TOKEN` (fine-grained PAT limité à `frenndak/SmartSVG-Studio`, Contents et Pull requests read/write) et `OPENAI_API_KEY` (API payante distincte de ChatGPT et de Copilot).
7. Après audit de confidentialité, créer en *variables* `SMARTSVG_AUTOMATION_ENABLED=true` et `SMARTSVG_PUBLIC_RUNNER_RISK_ACCEPTED=true`. Ne pas activer si un runner public ne convient pas à la sensibilité du code.
8. Lancer le workflow public manuellement depuis Actions et vérifier le premier résultat, la PR privée et les coûts API avant de laisser la planification agir.

## Arrêt immédiat

Dans le dépôt public, basculer `SMARTSVG_AUTOMATION_ENABLED=false`. Désactiver le workflow au besoin. Révoquer les accès compromis sans les écrire dans une issue. Les PR existantes restent privées et ne sont pas fusionnées automatiquement.

## Échecs courants

- Aucun run : workflow non reconnu, Actions désactivées, cadence retardée, dépôt non initialisé, permissions insuffisantes.
- Job marqué *skipped* : variable d'activation absente ou refus de risque public.
- Absence de dépôt privé au checkout : installation GitHub App / PAT / autorisation Contents.
- Preflight `ready=false` : source non importée, roadmap SHA différent ou marqueur absent.
- Aucune nouvelle PR : une autre PR est ouverte, Codex ne produit rien ou tests échouent.
- Erreur API : clé absente, facturation inactive, quota, réseau, rôle ou modèle.

Le fait de voir un cron de 30 minutes ne prouve pas que 48 changements sont effectués par jour.
