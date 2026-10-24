# SmartSVG Automation — public scheduler only

This **public** repository contains no SmartSVG engine source and runs no AI code.
GitHub Actions dispatches private engineering cycles to `frenndak/SmartSVG-Studio`:
- `20 * * * *` UTC: development candidate cycle.
- `50 * * * *` UTC: repair cycle for an existing AI-created private draft PR.
- Separate ChatGPT scheduled independent review: once an hour at minute 10.

GitHub schedule execution is **best effort** and may be delayed or skipped.

## Required configuration

In THIS PUBLIC repository (Settings → Secrets and variables → Actions):
- Repository **secret** `SMARTSVG_DISPATCH_TOKEN`: fine-grained token with **Contents: read/write** permissions ONLY for the private SmartSVG-Studio repo, sufficient for GitHub repository_dispatch. Prefer a GitHub App installation token where feasible.
- Repository **variable** `SMARTSVG_AUTOMATION_ENABLED=true`: enable only after the private runner is ready and tested.

In the PRIVATE repository, configure `OPENAI_API_KEY` as an Actions secret (separately billed); configure its own `SMARTSVG_AUTOMATION_ENABLED=true` after verified engine import and an independent operator-approved `.automation/READY`. Protected branches, private PRs, tests, Codex output, and logs belong ONLY in the private repository.

The dispatcher deliberately NEVER uses `OPENAI_API_KEY`, checks out the private source, or executes Codex. **No private source code, customer images, model weights or API credentials** belong in the public tree, public logs, or public artifacts.

## Import prerequisite

The ZIP previously provided by the user has SHA-256 `9369656f0216cebb6dccce0d0155bffa16d8c384da6a984bf848cdd8aa003c54`. The private repo records this checksum. Put the actual ZIP as an asset of a **private release** `smartsvg-v21.15.2-source` before dispatches can work; the dedicated private bootstrap action checks the exact digest, 651 manifest hashes and never activates itself.

Do not activate the scheduler solely because its public tests are green. Ensure OpenAI API usage and budget are approved. Private code is not validated by public CI.
