# Publication du code SmartSVG Studio — plan de migration

**Intention validée par le propriétaire le 26 octobre 2026 :** SmartSVG Studio sera gratuit et son code accessible publiquement. Aucun objectif de commercialisation. Ce document n'est **pas** une preuve que le dépôt moteur est déjà public.

## Situation observée
- `frenndak/SmartSVG-Studio` : dépôt **privé**, source intégrale V21.15.2 et développements G2 en PR.
- `frenndak/SmartSVG-Automation` : dépôt **public**, actuellement orchestration GitHub Actions uniquement.
- Une tâche ChatGPT distincte est programmée **chaque heure** ; elle vérifie le code réel avant de proposer un changement. L'horaire n'est pas une garantie de 24 modifications utiles/jour.
- L'archive V21.15.2 ne contient pas de fichier `LICENSE` identifié ; pas de licence open-source attribuée à la source complète pour le moment.

## Architecture cible : un seul dépôt source public
Conserver **SmartSVG-Studio comme dépôt principal**, après contrôle de l'historique et changement de visibilité par l'administrateur GitHub (Settings → General → Danger Zone → Change repository visibility). En l'absence de permission administrative/API permettant cette action, **ne pas annoncer la publication comme faite**.

Puis regrouper `engine/`, `docs/`, `tests/`, `example_workflows/` et les workflows publics de contribution/CI sous ce même dépôt. L'ancien dépôt `SmartSVG-Automation` reste un relais temporaire tant que la consolidation n'est pas terminée ; le supprimer ou l'archiver uniquement lorsque le nouveau mécanisme a été testé.

## Audits obligatoires AVANT mise en public
1. **Historique complet et branches, pas seulement le dernier commit** : chercher secrets, `.env`, jetons, identités ou journaux sensibles. Changer/révoquer toute clé qui aurait été exposée dans l'historique.
2. **Droits des fichiers et des images** : exclure les illustrations d'utilisateurs, Pokémon/personnages tiers, fichiers soumis à licence non redistribuable et poids IA. Utiliser des images synthétiques sous droits contrôlés pour les tests.
3. **Licence du code** : choisir explicitement une licence adaptée (par exemple MIT pour le code dont l'auteur détient les droits), vérifier les dépendances et notices tierces, puis ajouter le fichier `LICENSE`. Public et open source ne sont pas synonymes en l'absence de licence.
4. **Sécurité Actions** : limiter `GITHUB_TOKEN` au minimum, séparer PR non fiables et code privilégié, protéger `main`, ne jamais exposer `OPENAI_API_KEY`, `SMARTSVG_DISPATCH_TOKEN` ni d'autres secrets dans des workflows publics ou leurs logs.
5. **Historique Git** : si impossible d'en garantir l'innocuité, préférer un **nouveau dépôt public propre** et une importation de sources filtrées à un changement de visibilité du dépôt historique. Ne pas rendre le dépôt historique public prématurément.

## Plan d'exécution après audit
- Qualifier les PR #25 (SVG) et #26 → #27 → #28 (inspection → zones → éditeur) selon leurs dépendances, CI et revue. Ne pas fusionner les brouillons automatiquement.
- Exporter un manifeste de fichiers autorisés, empreintes SHA-256 et attributions de licences.
- Publier le code source autorisé dans **un dépôt public unique**, avec CI Python/JavaScript, exemple synthétique, guide ComfyUI et politique de contribution.
- Simplifier l'orchestration : travail planifié ChatGPT toutes les heures, une PR courte à la fois, pas de dépendance secrète à un dépôt privé après migration.
- Vérifier concrètement une exécution de tâche planifiée avec écriture GitHub, tests et rapport. Échec d'écriture = rapport de blocage, jamais succès fictif.

**Important :** le présent dépôt public ne reçoit pas la copie de l'archive privée, d'images personnelles ou d'un `OPENAI_API_KEY`. Un changement de visibilité du dépôt privé nécessite l'action administrative décrite ci-dessus ; cette étape n'est pas automatisée par la connexion GitHub actuelle.
