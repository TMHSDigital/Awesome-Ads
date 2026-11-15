#!/usr/bin/env python3
"""Verify relative markdown links point to existing files."""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

from catalog import SECTIONS

LINK_PATTERN = re.compile(r"\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#", "ftp://")


def _markdown_files(root: Path) -> list[Path]:
    tracked = subprocess.check_output(["git", "ls-files", "-z", "--", "*.md"], cwd=root)
    paths = {root / os.fsdecode(name) for name in tracked.split(b"\0") if name}

    docs = root / "docs"
    paths.update((docs / "CONTRIBUTING.md", docs / "index.md"))
    paths.update(docs / section / "index.md" for section, _ in SECTIONS)
    return sorted(path for path in paths if path.is_file())


def collect_errors(root: Path) -> list[str]:
    errors: list[str] = []
    repo_root = root.resolve()

    for md_file in _markdown_files(root):

        content = md_file.read_text(encoding="utf-8")
        for match in LINK_PATTERN.finditer(content):
            parts = match.group(1).split(maxsplit=1)
            if not parts:
                continue
            target = parts[0].split("#", 1)[0].split("?", 1)[0]
            if not target or target.startswith(SKIP_PREFIXES):
                continue

            resolved = (md_file.parent / target).resolve()
            try:
                resolved.relative_to(repo_root)
            except ValueError:
                errors.append(f"{md_file}: external-style path {target!r}")
                continue

            if not resolved.exists():
                errors.append(f"{md_file}: missing target {target!r}")

    return errors


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    prepare_script = root / "scripts" / "prepare-mkdocs.py"
    if prepare_script.exists():
        subprocess.run([sys.executable, str(prepare_script)], check=True)

    errors = collect_errors(root)

    if errors:
        print("Internal link check failed:\n", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print("All internal markdown links resolve.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
