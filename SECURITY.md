# Security Policy — SmartSVG Automation

This repository is **PUBLIC**. Do not upload source code from `SmartSVG-Studio`, images supplied by users, customer data, API keys, PATs, ComfyUI logs, private diffs, or model weights here.

Secrets and protected branches are managed exclusively in GitHub Settings, never in a committed file. Review all changes to `.github/workflows/` before enabling schedules. Scheduled runs should not use `pull_request_target` and must not execute untrusted contributions with production credentials.

If a credential may have been exposed, revoke and rotate it promptly, disable the affected workflow, and review Actions logs and access history.

AI development is gated by two opt-in variables and a private source gate. Public Actions logs remain public despite those measures. Prefer a private executor for confidential code.

Report suspected exposure through GitHub's private security reporting for the repository if enabled, rather than posting secrets in an issue.
