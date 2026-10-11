"""Unit tests for scripts/new_project.py."""
import io
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import new_project as np_  # noqa: E402

REPO = Path(__file__).resolve().parents[1]


class NewProjectTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        shutil.copytree(REPO / "templates", self.root / "templates")
        shutil.copytree(REPO / "projects" / "_template", self.root / "projects" / "_template")
        (self.root / "engineering" / "architecture").mkdir(parents=True)
        (self.root / "engineering" / "architecture" / "stack-selection.md").write_text("x")

    def tearDown(self):
        self.tmp.cleanup()

    def call(self, *args):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            try:
                code = np_.main([*args, "--root", str(self.root)])
            except SystemExit as exc:  # argparse usage errors
                code = exc.code
        return code, out.getvalue(), err.getvalue()

    def test_creates_workspace_with_filled_readme(self):
        code, _, _ = self.call("acme-coffee", "--client", "Acme Coffee")
        self.assertEqual(code, 0)
        target = self.root / "projects" / "acme-coffee"
        self.assertEqual(len(list(target.glob("*.md"))), 11)
        readme = (target / "README.md").read_text()
        self.assertIn("Acme Coffee", readme)
        self.assertNotIn("{{CLIENT_NAME}}", readme)

    def test_dry_run_writes_nothing(self):
        code, out, _ = self.call("acme", "--client", "Acme", "--dry-run")
        self.assertEqual(code, 0)
        self.assertIn("would create", out)
        self.assertFalse((self.root / "projects" / "acme").exists())

    def test_refuses_existing_folder(self):
        existing = self.root / "projects" / "acme"
        existing.mkdir()
        (existing / "keep.md").write_text("client work")
        code, _, err = self.call("acme", "--client", "Acme")
        self.assertEqual(code, 1)
        self.assertIn("refused", err)
        self.assertEqual((existing / "keep.md").read_text(), "client work")

    def test_rejects_invalid_and_reserved_slugs(self):
        for slug in ("Acme Coffee", "acme_coffee", "-acme", "examples", "_template"):
            code, _, _ = self.call(slug, "--client", "X")
            self.assertEqual(code, 2, slug)

    def test_links_are_rewritten_to_resolve(self):
        self.call("acme", "--client", "Acme")
        project = self.root / "projects" / "acme"
        spec = (project / "06-technical-specification.md").read_text()
        self.assertIn("](07-test-plan.md)", spec)  # copied sibling -> numbered copy
        self.assertIn("](../../templates/api-contract.md)", spec)  # not copied -> template
        handover = (project / "09-handover.md").read_text()
        self.assertIn("](../../client-operations/handover/handover-and-maintenance.md)", handover)

    def test_rewrite_links_keeps_external_and_anchor(self):
        src, dst = self.root / "templates", self.root / "projects" / "x"
        text = "[a](https://e.org) [b](../docs/g.md#part) [c](#local)"
        result = np_.rewrite_links(text, src, dst)
        self.assertIn("(https://e.org)", result)
        self.assertIn("(../../docs/g.md#part)", result)
        self.assertIn("(#local)", result)


if __name__ == "__main__":
    unittest.main()
