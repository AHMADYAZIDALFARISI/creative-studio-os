"""Unit tests for scripts/validation/validate_repo.py. Run from the repo root:
python3 -m unittest discover -s scripts -p "test_*.py"
"""
import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "validation"))
import validate_repo as v  # noqa: E402


def write(root: Path, rel: str, text: str) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_broken_link_detected_and_valid_link_ignored(self):
        write(self.root, "docs/a.md", "[ok](b.md) [bad](missing.md) [web](https://x.org)")
        write(self.root, "docs/b.md", "fine")
        problems = v.check_links(self.root)
        self.assertEqual(len(problems), 1)
        self.assertIn("missing.md", problems[0])

    def test_links_inside_code_blocks_and_placeholders_ignored(self):
        write(self.root, "a.md", "```\n[x](nope.md)\n```\n[y]({{LINK}}) `[z](nope.md)`")
        self.assertEqual(v.check_links(self.root), [])

    def test_anchor_links_resolve_to_file(self):
        write(self.root, "a.md", "[s](b.md#section)")
        write(self.root, "b.md", "# Section")
        self.assertEqual(v.check_links(self.root), [])

    def test_empty_directory_detected(self):
        (self.root / "empty").mkdir()
        self.assertEqual(v.check_empty_dirs(self.root), ["empty directory: empty"])

    def test_markers_detected_outside_code_only(self):
        write(self.root, "a.md", "Finish this " + "TO" + "DO\n```\n" + "TB" + "D in code\n```")
        problems = v.check_markers(self.root)
        self.assertEqual(len(problems), 1)
        self.assertIn("a.md:1", problems[0])

    def test_example_requires_label_and_no_placeholders(self):
        write(self.root, "projects/examples/demo/README.md", "Demo project")
        write(self.root, "projects/examples/demo/01.md", "Client: {{NAME}}")
        problems = v.check_examples(self.root)
        self.assertTrue(any("FICTIONAL" in p for p in problems))
        self.assertTrue(any("unfilled placeholder" in p for p in problems))

    def test_duplicate_prompt_id_detected(self):
        write(self.root, "ai/a.md", "## W-01 First\n")
        write(self.root, "ai/b.md", "## W-01 Second\n")
        problems = v.check_prompts(self.root)
        self.assertTrue(any("duplicate prompt ID W-01" in p for p in problems))

    def test_duplicate_prompt_body_detected(self):
        body = "```\n" + "Context: a detailed repeated prompt body for testing. " * 4 + "\n```\n"
        write(self.root, "ai/a.md", body)
        write(self.root, "ai/b.md", body)
        self.assertTrue(any("duplicate prompt body" in p for p in v.check_prompts(self.root)))

    def test_em_dash_detected(self):
        write(self.root, "a.md", "one \u2014 two")
        self.assertEqual(len(v.check_em_dash(self.root)), 1)

    def test_agent_frontmatter_rules(self):
        write(self.root, ".claude/agents/good.md", "---\nname: good\ndescription: d\n---\nbody")
        write(self.root, ".claude/agents/bad.md", "---\nname: other\n---\nbody")
        write(self.root, ".claude/skills/s1/SKILL.md", "no frontmatter")
        problems = v.check_claude_config(self.root)
        self.assertTrue(any("bad.md" in p and "description" in p for p in problems))
        self.assertTrue(any("bad.md" in p and "match filename" in p for p in problems))
        self.assertTrue(any("SKILL.md" in p and "missing YAML" in p for p in problems))
        self.assertFalse(any("good.md" in p for p in problems))

    def test_secret_patterns_detected(self):
        fake_aws = "AKIA" + "ABCDEFGHIJKLMNOP"
        fake_assign = "api_key = '" + "x9" * 10 + "'"
        write(self.root, "config.txt", fake_aws + "\n" + fake_assign + "\napi_key = '{{API_KEY}}'")
        problems = v.check_secrets(self.root)
        self.assertEqual(len(problems), 2)

    def test_public_mode_blocks_client_folders_and_placeholders(self):
        write(self.root, "projects/README.md", "x")
        write(self.root, "projects/examples/demo/README.md", "FICTIONAL")
        write(self.root, "projects/acme-client/README.md", "real client")
        write(self.root, "LICENSE", "Copyright {{OWNER}}")
        write(self.root, "SECURITY.md", "ok")
        write(self.root, "CODE_OF_CONDUCT.md", "ok")
        problems = v.check_public(self.root)
        self.assertTrue(any("acme-client" in p for p in problems))
        self.assertTrue(any("LICENSE" in p for p in problems))
        self.assertFalse(any("examples" in p for p in problems))

    def test_public_checks_only_run_with_flag(self):
        write(self.root, "projects/acme-client/README.md", "real client")
        with redirect_stdout(io.StringIO()) as out:
            v.run(self.root, public=False)
        self.assertNotIn("public release", out.getvalue())
        with redirect_stdout(io.StringIO()) as out:
            v.run(self.root, public=True)
        self.assertIn("public release", out.getvalue())

    def test_run_returns_nonzero_on_problems(self):
        (self.root / "empty").mkdir()
        with redirect_stdout(io.StringIO()):
            self.assertEqual(v.run(self.root), 1)


if __name__ == "__main__":
    unittest.main()
