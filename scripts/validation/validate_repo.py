#!/usr/bin/env python3
"""Validate the structure and content hygiene of the Creative Studio OS repository.

Checks: required files, internal Markdown links, empty directories, leftover
TODO/TBD markers, unfilled placeholders in the fictional example, fictional
labels, (with --public) client folders and legal placeholders, duplicate prompt IDs and bodies, em dashes, Claude Code frontmatter,
and common secret patterns.

Exit codes: 0 = all checks pass, 1 = one or more problems found.
Standard library only.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

REQUIRED_FILES = [
    "README.md", "CONTRIBUTING.md", "LICENSE", "CHANGELOG.md", "SECURITY.md",
    ".gitignore", ".editorconfig", ".gitattributes", "CLAUDE.md",
    "docs/getting-started.md", "docs/repository-architecture.md",
    "docs/workflow-overview.md", "docs/glossary.md", "docs/quality-standards.md",
    "design/google-stitch/README.md", "design/google-stitch/capabilities.md",
    "studio/creative-direction/anti-slop-audit.md",
    "projects/README.md", "projects/_template/README.md",
    "scripts/README.md", "scripts/new_project.py",
] + [f"templates/{name}" for name in (
    "project-brief.md", "client-discovery.md", "brand-strategy.md",
    "creative-brief.md", "design-review.md", "technical-specification.md",
    "api-contract.md", "database-design.md", "test-plan.md",
    "deployment-checklist.md", "project-handover.md", "retrospective.md",
)]

SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv"}
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
FENCE_RE = re.compile(r"^\s*```")
MARKER_RE = re.compile(r"\b(TODO|TBD|FIXME)\b|lorem ipsum", re.IGNORECASE)
PROMPT_ID_RE = re.compile(r"^(?:#{2,3}\s+|\*\*|\|\s*)([A-Z]-\d{2}|P-\d{2})\b")
SECRET_PATTERNS = {
    "private key block": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}\b"),
    "Anthropic API key": re.compile(r"\bsk-ant-[A-Za-z0-9_\-]{20,}"),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9]{32,}\b"),
    "assigned secret": re.compile(
        r"(?i)\b(api[_-]?key|secret|password|token)\b\s*[:=]\s*['\"][^'\"\s{}]{12,}['\"]"
    ),
}
EM_DASH = "\u2014"


def iter_files(root: Path, suffixes: tuple[str, ...] | None = None):
    for path in sorted(root.rglob("*")):
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        if path.is_file() and (suffixes is None or path.suffix in suffixes):
            yield path


def strip_code(text: str) -> list[tuple[int, str]]:
    """Return (line_number, line) pairs outside fenced code blocks, with inline code removed."""
    lines, in_fence = [], False
    for number, line in enumerate(text.splitlines(), start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            lines.append((number, re.sub(r"`[^`]*`", "", line)))
    return lines


def check_required(root: Path) -> list[str]:
    return [f"missing required file: {rel}" for rel in REQUIRED_FILES if not (root / rel).is_file()]


def check_links(root: Path) -> list[str]:
    problems = []
    for md in iter_files(root, (".md",)):
        for number, line in strip_code(md.read_text(encoding="utf-8")):
            for target in LINK_RE.findall(line):
                if target.startswith(("http://", "https://", "mailto:", "#")) or "{{" in target:
                    continue
                path_part = target.split("#", 1)[0]
                if path_part and not (md.parent / path_part).exists():
                    problems.append(f"{md.relative_to(root)}:{number}: broken link -> {target}")
    return problems


def check_empty_dirs(root: Path) -> list[str]:
    problems = []
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if path.is_dir() and not any(p in SKIP_DIRS for p in rel.parts) and not any(path.iterdir()):
            problems.append(f"empty directory: {rel}")
    return problems


def check_markers(root: Path) -> list[str]:
    problems = []
    for md in iter_files(root, (".md",)):
        for number, line in strip_code(md.read_text(encoding="utf-8")):
            if MARKER_RE.search(line):
                problems.append(f"{md.relative_to(root)}:{number}: unfinished marker: {line.strip()[:80]}")
    return problems


def check_examples(root: Path) -> list[str]:
    problems = []
    examples = root / "projects" / "examples"
    if not examples.is_dir():
        return ["missing projects/examples directory"]
    for project in sorted(p for p in examples.iterdir() if p.is_dir()):
        readme = project / "README.md"
        if not readme.is_file() or "FICTIONAL" not in readme.read_text(encoding="utf-8"):
            problems.append(f"{readme.relative_to(root)}: example must be labeled FICTIONAL")
        for md in iter_files(project, (".md",)):
            for number, line in strip_code(md.read_text(encoding="utf-8")):
                if "{{" in line:
                    problems.append(f"{md.relative_to(root)}:{number}: unfilled placeholder in example")
    return problems


def check_prompts(root: Path) -> list[str]:
    problems, seen_ids, seen_bodies = [], {}, {}
    prompt_dirs = [root / "ai", root / "design" / "google-stitch"]
    for base in prompt_dirs:
        if not base.is_dir():
            continue
        for md in iter_files(base, (".md",)):
            text = md.read_text(encoding="utf-8")
            for number, line in enumerate(text.splitlines(), start=1):
                match = PROMPT_ID_RE.match(line)
                if match:
                    pid = match.group(1)
                    where = f"{md.relative_to(root)}:{number}"
                    if pid in seen_ids:
                        problems.append(f"{where}: duplicate prompt ID {pid} (first at {seen_ids[pid]})")
                    else:
                        seen_ids[pid] = where
            for block in re.findall(r"```[a-z]*\n(.*?)```", text, re.DOTALL):
                normalized = " ".join(block.split())
                if len(normalized) < 120:
                    continue
                digest = hashlib.sha1(normalized.encode()).hexdigest()
                where = str(md.relative_to(root))
                if digest in seen_bodies and seen_bodies[digest] != where:
                    problems.append(f"{where}: duplicate prompt body (also in {seen_bodies[digest]})")
                seen_bodies.setdefault(digest, where)
    return problems


def check_em_dash(root: Path) -> list[str]:
    problems = []
    for md in iter_files(root, (".md",)):
        for number, line in enumerate(md.read_text(encoding="utf-8").splitlines(), start=1):
            if EM_DASH in line:
                problems.append(f"{md.relative_to(root)}:{number}: em dash violates the writing rule")
    return problems


def parse_frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    data = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith((" ", "-")):
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data


def check_claude_config(root: Path) -> list[str]:
    problems = []
    for agent in sorted((root / ".claude" / "agents").glob("*.md")):
        meta = parse_frontmatter(agent.read_text(encoding="utf-8"))
        rel = agent.relative_to(root)
        if meta is None:
            problems.append(f"{rel}: missing YAML frontmatter")
            continue
        for key in ("name", "description"):
            if not meta.get(key):
                problems.append(f"{rel}: frontmatter needs '{key}'")
        if meta.get("name") and meta["name"] != agent.stem:
            problems.append(f"{rel}: name '{meta['name']}' should match filename '{agent.stem}'")
    for skill in sorted((root / ".claude" / "skills").glob("*/SKILL.md")):
        meta = parse_frontmatter(skill.read_text(encoding="utf-8"))
        rel = skill.relative_to(root)
        if meta is None:
            problems.append(f"{rel}: missing YAML frontmatter")
            continue
        for key in ("name", "description"):
            if not meta.get(key):
                problems.append(f"{rel}: frontmatter needs '{key}'")
        if meta.get("name") and meta["name"] != skill.parent.name:
            problems.append(f"{rel}: name '{meta['name']}' should match folder '{skill.parent.name}'")
    for rule in sorted((root / ".claude" / "rules").glob("*.md")):
        text = rule.read_text(encoding="utf-8")
        if text.startswith("---") and parse_frontmatter(text) is None:
            problems.append(f"{rule.relative_to(root)}: unterminated frontmatter")
    return problems


def check_secrets(root: Path) -> list[str]:
    problems = []
    for path in iter_files(root):
        if path.suffix in {".png", ".jpg", ".webp", ".pdf", ".woff2"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for number, line in enumerate(text.splitlines(), start=1):
            for label, pattern in SECRET_PATTERNS.items():
                if pattern.search(line):
                    problems.append(f"{path.relative_to(root)}:{number}: possible {label}")
    return problems


PUBLIC_PROJECT_ENTRIES = {"README.md", "_template", "examples"}


def check_public(root: Path) -> list[str]:
    """Extra checks for the public repository: no client folders, no unfilled legal placeholders."""
    problems = []
    projects = root / "projects"
    if projects.is_dir():
        for entry in sorted(projects.iterdir()):
            if entry.name not in PUBLIC_PROJECT_ENTRIES:
                problems.append(f"projects/{entry.name}: client workspace in a public repository; move it to a private copy")
    for rel in ("LICENSE", "SECURITY.md", "CODE_OF_CONDUCT.md"):
        path = root / rel
        if not path.is_file():
            problems.append(f"missing {rel} for public release")
        elif "{{" in path.read_text(encoding="utf-8"):
            problems.append(f"{rel}: unfilled placeholder")
    return problems


CHECKS = [
    ("required files", check_required),
    ("internal links", check_links),
    ("empty directories", check_empty_dirs),
    ("unfinished markers", check_markers),
    ("fictional example", check_examples),
    ("prompt duplicates", check_prompts),
    ("em dashes", check_em_dash),
    ("Claude Code frontmatter", check_claude_config),
    ("secret patterns", check_secrets),
]


def run(root: Path, public: bool = False) -> int:
    total = 0
    checks = CHECKS + ([("public release", check_public)] if public else [])
    for label, check in checks:
        problems = check(root)
        status = "ok" if not problems else f"{len(problems)} problem(s)"
        print(f"[{'PASS' if not problems else 'FAIL'}] {label}: {status}")
        for problem in problems:
            print(f"    - {problem}")
        total += len(problems)
    print(f"\n{'All checks passed.' if total == 0 else f'{total} problem(s) found.'}")
    return 0 if total == 0 else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2],
                        help="repository root (default: two levels above this script)")
    parser.add_argument("--public", action="store_true",
                        help="also run public-release checks (no client folders, no legal placeholders)")
    args = parser.parse_args(argv)
    if not args.root.is_dir():
        print(f"error: root not found: {args.root}", file=sys.stderr)
        return 2
    return run(args.root.resolve(), public=args.public)


if __name__ == "__main__":
    sys.exit(main())
