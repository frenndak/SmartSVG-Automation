# Mise en service SmartSVG — orchestration sécurisée

## État vérifié au 24 octobre 2026

L'archive **originale V21.15.2 est déjà intégrée** au dépôt privé `frenndak/SmartSVG-Studio` sous `source-releases/`, avec le moteur dans `engine/`. Le SHA-256 de référence est `9369656f0216cebb6dccce0d0155bffa16d8c384da6a984bf848cdd8aa003c54`, et les 651 empreintes du manifeste sont vérifiées. Le marqueur `.automation/READY` existe : il autorise seulement des **candidats de développement en PR**, pas une release ni une validation physique.

## Configuration requise (secrets jamais dans le code)

1. **Privé — SmartSVG-Studio** : créer `OPENAI_API_KEY` dans Settings → Secrets and variables → Actions → Secrets. L'utilisation de l'API OpenAI est facturée indépendamment d'un abonnement ChatGPT. Autoriser GitHub Actions à créer des pull requests et vérifier la politique GitHub Actions ; le workflow privé déclare déjà les permissions nécessaires à la mise à jour des branches et aux tests.
2. **Public — SmartSVG-Automation** : créer le secret `SMARTSVG_DISPATCH_TOKEN`, jeton GitHub **limité au seul dépôt privé**. Son autorisation nécessaire pour le POST `repository_dispatch` est **Contents: read/write** sur le dépôt privé. Ne pas lui ajouter de permissions pour d'autres dépôts.
3. **Les deux dépôts** : créer séparément `SMARTSVG_AUTOMATION_ENABLED=true` dans Settings → Secrets and variables → Actions → **Variables** seulement après la vérification des secrets, du budget et des permissions. Les jobs de développement ignorent toute autre valeur.
4. **Main privé** : activer dans Settings → Rules → Rulesets la protection de la branche `main`, l'interdiction des pushs directs/force-push et les contrôles CI obligatoires adaptés. Un résultat `skipped` ne vaut pas succès.
5. Ne jamais stocker le code privé, le ZIP, les exemples utilisateurs ou `OPENAI_API_KEY` dans le dépôt public.

Ces secrets, variables et rulesets doivent être renseignés dans **GitHub Settings** : le connecteur GitHub utilisé par ChatGPT ne dispose pas d'une action autorisée pour les écrire. Ne pas créer de jeton dans un commit ou commentaire.

## Test sûr AVANT activation

- Dans le **dépôt public**, Actions → **SmartSVG - Secure half-hour orchestration** → Run workflow → `dry_run=true` : vérifie le contrôle de déclenchement, **n'envoie aucun événement vers le privé**.
- Dans le **dépôt privé**, Actions → **SmartSVG - Private AI Development** → Run workflow → `execute=false` : contrôle SHA de la roadmap, l'archive V21.15.2, le manifeste et READY, **sans lancer Codex**. Même si l'automatisation est activée, le mode manuel `execute=false` interdit le job payant.
- Après configuration complète : déclenchement manuel public avec `dry_run=false`, puis examen de la PR privée et des CI **sur son SHA HEAD exact**. `workflow_dispatch` des tests G0/CPU peut être nécessaire pour une PR créée avec `GITHUB_TOKEN`.

## Cadence et revue

- **HH:05 UTC** : orchestration publique → développement privé d'un seul micro-lot, si aucune PR autonome déjà active.
- **HH:35 Europe/Paris** : tâche ChatGPT indépendante → inspection des changements et des CI, publication d'une revue. Les fuseaux UTC et Europe/Paris sont distincts ; cette configuration ne garantit **pas** une revue 30 minutes après le même run en toute saison.
- **HH:50 UTC** : correction **seulement** si une PR `smartsvg/auto-*` a reçu le label `bug` ou `smartsvg:repair` après une revue pertinente. Le label est retiré **avant** l'appel payant afin de ne pas répéter une correction indéfiniment.

IMPORTANT : dans cette configuration, la revue horaire doit privilégier les PR effectives et ne pas supposer que les trois créneaux forment nécessairement un cycle chronologique parfait pendant les changements d'heure. Les déclenchements GitHub sont best-effort et peuvent arriver en retard.

## Arrêt et diagnostics

- Pause immédiate : basculer `SMARTSVG_AUTOMATION_ENABLED=false` **dans les deux dépôts**. Pour stopper les audits GPT, désactiver sa tâche planifiée séparément.
- `skipped` public : variable d'activation absente/faux ou mode dry-run ; vérifier le job concerné.
- `skipped` privé : variable privée absente/faux, aucun lot admissible, PR autonome déjà ouverte, ou aucune demande de correction.
- `403` dispatch : vérifier le périmètre et Contents write du token privé, sans exposer sa valeur.
- Revue sans CI exact-HEAD : **NO GO**, ne pas confondre « dispatché » et « réussi ».
- Vérification G0/CPU : uniquement preuve logicielle L1. ComfyUI réel/RTX 3070 (L2), Design Space et coupe Cricut (L3) restent à éprouver.

Rappel : aucune API payante ne doit être activée sans clé valide, budget accepté et contrôle de confidentialité.
