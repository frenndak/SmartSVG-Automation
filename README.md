# SmartSVG Automation

Public workflow-only repository for coordinating work on the private `frenndak/SmartSVG-Studio` repository. **No SmartSVG application source code belongs here.**

- Cadence: GitHub Actions every 30 minutes (`20,50 * * * *`, UTC), best-effort schedule.
- Independent ChatGPT audit: once an hour; reads the private repo and its PRs.
- Gate: source code and frozen roadmap must be uploaded to private repo, then `.automation/READY` added after verification.
- The workflow will require `SMARTSVG_PRIVATE_REPO_TOKEN` (fine-grained token for private repository, Contents + Pull requests read/write) and `OPENAI_API_KEY` (paid API billing, **not** a ChatGPT Plus or Copilot subscription).
- Never print private diffs, source, prompts, API responses or secrets into public workflow logs. Never upload artifacts containing private source.
- Draft PRs only; no automatic merges or direct pushes to the default branch. While ANY private SmartSVG PR remains open, new cycles skip development to enforce WIP=1 and avoid conflicting changes.
- In the absence of a valid source/bootstrap gate, credentials or API key, or both explicit activation variables, do not start autonomous development.

Security: protect default branch, restrict write access, limit secret availability. AI actions incur API charges even when GitHub-hosted public Actions minutes are free.

## Operator configuration

1. Import the actual full V21.15.2 source tree into the private repository and verify its archive manifest, then create `.automation/READY` in the **private** repository. Never create that marker based solely on the presence of a README.
2. In this **public** repository's Settings → Secrets and variables → Actions, create repository secrets `SMARTSVG_PRIVATE_REPO_TOKEN` (fine-grained GitHub PAT for **only** `frenndak/SmartSVG-Studio`, Contents and Pull requests read/write) and `OPENAI_API_KEY` (OpenAI API billed separately).
3. In the same Actions page, create **two repository variables**: `SMARTSVG_AUTOMATION_ENABLED=true` and `SMARTSVG_PUBLIC_RUNNER_RISK_ACCEPTED=true` **only if** you knowingly accept that public workflow runs and logs are publicly readable. The full private source is checked out on the public runner; tool or test output might disclose portions despite suppression measures. If source confidentiality is essential, do not enable this workflow: move execution to the private repo (consumes private runner minutes) or a secured self-hosted runner.
4. Run the workflow manually once from the Actions tab, inspect status, confirm it proposes **private draft PRs**, then watch normal scheduled runs. Scheduled invocations may be delayed or skipped under GitHub load.
5. Protect the public default branch and restrict who can edit Actions workflows; public workflow logs may expose diagnostics, even when we attempt to suppress them. Prefer private-runner architecture if disclosure of any private code is unacceptable.

**No execution guarantee:** cron schedules are best effort; paid Codex API access is required; unattended actions do not guarantee complete or correct features.

**Preflight hardening:** the development job refuses to start unless the canonical roadmap v3.2 SHA-256 matches `0e503a55fa622d7acea44d8e742205fb6a71119262c309a0b5a2bd48f0ab28a3` and the private maintainer has placed a nonempty `.automation/READY` marker. Passing these checks does not attest code quality, real source provenance, or machine-validated cutting.
