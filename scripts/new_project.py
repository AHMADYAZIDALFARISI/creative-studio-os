#!/usr/bin/env python3
"""Create a client project workspace from projects/_template and templates/.

Never overwrites: refuses to run if the target folder exists.
Rewrites relative Markdown links so they still resolve from the new folder.
Standard library only. Exit codes: 0 ok, 1 refused, 2 usage error.
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
from pathlib import Path

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"(\[[^\]]*\]\()([^)\s]+)(\))")
STAGE_FILES = [
    ("01-project-brief.md", "project-brief.md"),
    ("02-discovery.md", "client-discovery.md"),
    ("03-brand-strategy.md", "brand-strategy.md"),
    ("04-creative-brief.md", "creative-brief.md"),
    ("05-design-review.md", "design-review.md"),
    ("06-technical-specification.md", "technical-specification.md"),
    ("07-test-plan.md", "test-plan.md"),
    ("08-deployment-checklist.md", "deployment-checklist.md"),
    ("09-handover.md", "project-handover.md"),
    ("10-retrospective.md", "retrospective.md"),
]


def rewrite_links(text: str, source_dir: Path, target_dir: Path,
                  renamed: dict[str, str] | None = None) -> str:
    """Re-point relative links written for source_dir so they resolve from target_dir.

    renamed maps a source filename (in source_dir) to its copied filename in
    target_dir, so links between copied templates point at the project copy.
    """
    renamed = renamed or {}

    def replace(match: re.Match) -> str:
        target = match.group(2)
        if target.startswith(("http://", "https://", "mailto:", "#")) or "{{" in target:
            return match.group(0)
        path_part, _, anchor = target.partition("#")
        absolute = (source_dir / path_part).resolve()
        if absolute.parent == source_dir.resolve() and absolute.name in renamed:
            new = renamed[absolute.name]
        else:
            new = os.path.relpath(absolute, target_dir.resolve()).replace(os.sep, "/")
        return f"{match.group(1)}{new}{'#' + anchor if anchor else ''}{match.group(3)}"
    return LINK_RE.sub(replace, text)


def plan(root: Path, slug: str, client: str, today: str) -> dict[Path, str]:
    """Return {destination_path: content} without writing anything."""
    target = root / "projects" / slug
    files = {}
    readme = (root / "projects" / "_template" / "README.md").read_text(encoding="utf-8")
    readme = readme.replace("{{CLIENT_NAME}}", client).replace("{{CREATED_DATE}}", today)
    files[target / "README.md"] = readme
    templates_dir = root / "templates"
    renamed = {source: dest for dest, source in STAGE_FILES}
    for dest_name, source_name in STAGE_FILES:
        text = (templates_dir / source_name).read_text(encoding="utf-8")
        files[target / dest_name] = rewrite_links(text, templates_dir, target, renamed)
    return files


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Create a client project workspace.")
    parser.add_argument("slug", help="folder name: lowercase letters, numbers, hyphens")
    parser.add_argument("--client", required=True, help="client display name")
    parser.add_argument("--dry-run", action="store_true", help="show what would be created")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1],
                        help="repository root (default: parent of scripts/)")
    args = parser.parse_args(argv)

    if not SLUG_RE.match(args.slug) or args.slug in {"examples", "_template"}:
        print(f"error: invalid slug '{args.slug}'. Use e.g. 'acme-coffee'.", file=sys.stderr)
        return 2
    if not args.client.strip():
        print("error: --client must not be empty", file=sys.stderr)
        return 2
    target = args.root / "projects" / args.slug
    if target.exists():
        print(f"refused: {target} already exists. Nothing was changed.", file=sys.stderr)
        return 1

    files = plan(args.root, args.slug, args.client.strip(), dt.date.today().isoformat())
    for path in files:
        print(f"{'would create' if args.dry_run else 'create'}: {path.relative_to(args.root)}")
    if args.dry_run:
        return 0
    target.mkdir(parents=True)
    for path, content in files.items():
        path.write_text(content, encoding="utf-8")
    print(f"\nDone. Start with projects/{args.slug}/01-project-brief.md")
    print("Reminder: keep real client projects in a private repository.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
