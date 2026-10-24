import tempfile
import unittest
from pathlib import Path
from sys import path

ROOT = Path(__file__).resolve().parents[1]
path.insert(0, str(ROOT / "tools"))
from check_public_repo import inspect_public_repo, PublicRepoRejected


class PublicRepoTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.workflow = self.root / ".github/workflows/development-cycle.yml"
        self.workflow.parent.mkdir(parents=True)
        self.workflow.write_text(
            "\n".join([
                "cron: '5 * * * *'",
                "cron: '50 * * * *'",
                "SMARTSVG_AUTOMATION_ENABLED",
                "secrets.SMARTSVG_DISPATCH_TOKEN",
                "repos/frenndak/SmartSVG-Studio/dispatches",
                "smartsvg-cycle",
            ])
        )

    def test_valid_synthetic_tree(self):
        self.assertEqual(inspect_public_repo(self.root)["status"], "public_preflight_passed")

    def test_missing_dispatch_gate(self):
        self.workflow.write_text(self.workflow.read_text().replace("SMARTSVG_AUTOMATION_ENABLED", ""))
        with self.assertRaisesRegex(PublicRepoRejected, "DISPATCH_GATE"):
            inspect_public_repo(self.root)

    def test_private_zip_forbidden(self):
        (self.root / "secret.zip").write_bytes(b"ZIP")
        with self.assertRaisesRegex(PublicRepoRejected, "PRIVATE_FILE"):
            inspect_public_repo(self.root)

    def test_source_folder_forbidden(self):
        folder = self.root / "engine"
        folder.mkdir()
        (folder / "code.py").write_text("print(1)")
        with self.assertRaisesRegex(PublicRepoRejected, "PRIVATE_FILE"):
            inspect_public_repo(self.root)

    def test_no_private_key_literals(self):
        (self.root / "secret.md").write_text(("-----BEGIN " + "PRIVATE KEY-----"))
        with self.assertRaisesRegex(PublicRepoRejected, "PRIVATE_FILE"):
            inspect_public_repo(self.root)

    def test_no_codex_in_public(self):
        self.workflow.write_text(self.workflow.read_text() + "\nuses: openai/codex-action@v1")
        with self.assertRaisesRegex(PublicRepoRejected, "PRIVATE_EXECUTION"):
            inspect_public_repo(self.root)

    def test_no_merge_automation(self):
        self.workflow.write_text(self.workflow.read_text() + "\ngh pr merge 12")
        with self.assertRaisesRegex(PublicRepoRejected, "PRIVATE_EXECUTION|DANGEROUS"):
            inspect_public_repo(self.root)


if __name__ == "__main__":
    unittest.main()
