#!/usr/bin/env python3
"""Public-only repository preflight, using Python stdlib.

The checks look for obvious disclosure/coordination mistakes. They do not
replace a security audit of the runners or GitHub permissions.
"""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path


class PublicRepoRejected(ValueError):
    pass


def inspect_public_repo(root: Path) -> dict:
    if not root.is_dir():
        raise PublicRepoRejected("REPO_NOT_FOUND")
    workflow = root / ".github" / "workflows" / "development-cycle.yml"
    if not workflow.is_file():
        raise PublicRepoRejected("WORKFLOW_MISSING")
    content = workflow.read_text(encoding="utf-8")
    required = [
        '5 * * * *',
        '50 * * * *',
        "SMARTSVG_AUTOMATION_ENABLED",
        "secrets.SMARTSVG_DISPATCH_TOKEN",
        "repos/frenndak/SmartSVG-Studio/dispatches",
        "smartsvg-cycle",
        "dry_run:",
        "default: true",
        "inputs.dry_run == false",
        "Validate dispatcher without credentials or API calls",
    ]
    prohibited = [
        "secrets.OPENAI_API_KEY",
        "secrets.SMARTSVG_PRIVATE_REPO_TOKEN",
        "openai/codex-action",
        "working-directory: smartsvg",
        "checkout@v4",
        "gh pr merge",
        "pull_request_target:",
    ]
    leaked = [token for token in prohibited if token in content]
    if leaked:
        raise PublicRepoRejected("PRIVATE_EXECUTION_IN_PUBLIC_RUNNER: " + ", ".join(leaked))
    missing = [token for token in required if token not in content]
    if missing:
        raise PublicRepoRejected("WORKFLOW_DISPATCH_GATE_MISSING: " + ", ".join(missing))
    if "pull_request_target:" in content or "gh pr merge" in content:
        raise PublicRepoRejected("DANGEROUS_WORKFLOW_TRIGGER_OR_AUTOMERGE")
    forbidden_extensions = {".zip", ".png", ".jpg", ".jpeg", ".webp", ".exe", ".dll", ".safetensors", ".ckpt"}
    bad_files = []
    for file in root.rglob("*"):
        if not file.is_file() or ".git" in file.relative_to(root).parts:
            continue
        rel = file.relative_to(root)
        if file.suffix.lower() in forbidden_extensions or any(p.lower() in {"smartsvg_ai", "engine", "private_assets", "model_weights"} for p in rel.parts):
            bad_files.append(str(rel))
        if file.stat().st_size > 500_000:
            bad_files.append(str(rel) + ":too_large")
        if file.suffix in {".md", ".yml", ".yaml", ".json", ".py"}:
            raw = file.read_text(encoding="utf-8")
            if re.search(r"(?i)-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----|ghp_[A-Za-z0-9]{30,}|sk-proj-[A-Za-z0-9_-]{40,}", raw):
                bad_files.append(str(rel) + ":likely_secret")
    if bad_files:
        raise PublicRepoRejected("PRIVATE_FILE_OR_CREDENTIAL_IN_PUBLIC_TREE: " + ",".join(sorted(set(bad_files))))
    return {"status": "public_preflight_passed", "checked_workflow": str(workflow.relative_to(root)),
            "disclosed_private_files": 0, "ai_enabled": "unverified_at_runtime"}


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo", type=Path, default=Path("."))
    args = p.parse_args()
    try:
        print(json.dumps(inspect_public_repo(args.repo), sort_keys=True))
        return 0
    except PublicRepoRejected as exc:
        print(json.dumps({"status": "rejected", "reason": str(exc)}))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
