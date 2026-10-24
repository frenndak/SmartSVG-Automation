# SmartSVG Automation

Public workflow-only repository for coordinating work on the private `frenndak/SmartSVG-Studio` repository. **No SmartSVG application source code belongs here.**

- Cadence: GitHub Actions every 30 minutes (`17,47 * * * *`, UTC), best-effort schedule.
- Independent ChatGPT audit: once an hour; reads the private repo and its PRs.
- Gate: source code and frozen roadmap must be uploaded to private repo, then `.automation/READY` added after verification.
- The workflow will require `SMARTSVG_PRIVATE_REPO_TOKEN` (fine-grained token for private repository, Contents + Pull requests read/write) and `OPENAI_API_KEY` (paid API billing, **not** a ChatGPT Plus or Copilot subscription).
- Never print private diffs, source, prompts, API responses or secrets into public workflow logs. Never upload artifacts containing private source.
- Draft PRs only; no automatic merges or direct pushes to the default branch.
- In absence of a valid source/bootstrap gate, credentials or API key, do not start autonomous development.

Security: protect default branch, restrict write access, limit secret availability. AI actions incur API charges even when GitHub-hosted public Actions minutes are free.
