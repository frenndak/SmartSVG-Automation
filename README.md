# SmartSVG Automation — public scheduler only

This **public** repository contains no SmartSVG engine source and runs no AI code.
GitHub Actions dispatches private engineering cycles to `frenndak/SmartSVG-Studio`:
- `5 * * * *` UTC: development candidate cycle.
- `50 * * * *` UTC: repair cycle for an existing AI-created private draft PR.
- Separate ChatGPT scheduled independent review: once an hour at minute **35** (Europe/Paris), between development and repair. Review reads the actual SHA and CI rather than assuming runs started.

GitHub schedule execution is **best effort** and may be delayed or skipped.

## Required configuration

In THIS PUBLIC repository (Settings → Secrets and variables → Actions):
- Repository **secret** `SMARTSVG_DISPATCH_TOKEN`: fine-grained token with **Contents: read/write** permissions ONLY for the private SmartSVG-Studio repo, sufficient for GitHub repository_dispatch. Prefer a GitHub App installation token where feasible.
- Repository **variable** `SMARTSVG_AUTOMATION_ENABLED=true`: enable only after the private runner is ready and tested.

In the PRIVATE repository, configure `OPENAI_API_KEY` as an Actions secret (separately billed); configure its own `SMARTSVG_AUTOMATION_ENABLED=true` after verified engine import and an independent operator-approved `.automation/READY`. Protected branches, private PRs, tests, Codex output, and logs belong ONLY in the private repository.

The dispatcher deliberately NEVER uses `OPENAI_API_KEY`, checks out the private source, or executes Codex. **No private source code, customer images, model weights or API credentials** belong in the public tree, public logs, or public artifacts.

## Baseline source — now imported

SmartSVG V21.15.2 is **present in the private repository main branch**: original ZIP plus 652 extracted files, 651 internal manifest hashes verified, SHA-256 `9369656f0216cebb6dccce0d0155bffa16d8c384da6a984bf848cdd8aa003c54`. Private G0 CI passes; 876 Python unit tests and 12 JavaScript test scripts passed in a controlled local environment. The private admission marker `.automation/READY` is restricted to drafting development PRs; it is not certification of ComfyUI UI, GPU or Cricut hardware. Once the engine evolves, the original source ZIP is still SHA/manifeste-verified separately and changed engine code is checked by private G0 and targeted CPU smoke tests. Bot-created private PRs are explicitly qualified via workflow_dispatch on the candidate branch; dispatch is not a successful test result.

**Remaining activation:** valid private OpenAI API key and private GitHub variable, plus a narrowly scoped dispatch token and activation variable in this public repository. GitHub Actions execution requires those to be configured in Settings; merely connecting GitHub to ChatGPT does not set them.

Do not activate the scheduler solely because its public tests are green. Ensure OpenAI API usage and budget are approved. Private code is not validated by public CI.

## Status and safe first test (24 October 2026)

The authentic source archive V21.15.2 and working `engine/` are already present in the private repository. The private admission G0 CI passed; physical machine tests are not implied.

The public **Run workflow** action defaults to `dry_run=true`: it validates phase handling without dispatching or making an OpenAI API call. An actual manual dispatch requires `dry_run=false`, an enabled public variable, and a valid scoped GitHub dispatch token.

The private workflow similarly defaults to `execute=false` for a no-cost manual integrity preflight. With automation explicitly enabled, only `execute=true` starts a manual paid Codex job. Scheduled private jobs are separately gated by their private `SMARTSVG_AUTOMATION_ENABLED` variable and readiness evidence.

An hourly repair invocation is **not** an hourly guaranteed paid Codex call: it requires an autonomous `smartsvg/auto-*` PR with an explicit review label `bug` or `smartsvg:repair`. The label is claimed and removed before the paid call to avoid unbounded replay. See `docs/ACTIVATION.md` and `docs/ARCHITECTURE.md`.
