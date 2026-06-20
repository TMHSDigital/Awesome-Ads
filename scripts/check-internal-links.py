#!/usr/bin/env python3
"""Verify relative markdown links point to existing files."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

LINK_PATTERN = re.compile(r"\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#", "ftp://")


def collect_errors(root: Path) -> list[str]:
    errors: list[str] = []

    for md_file in sorted(root.rglob("*.md")):
        if ".git" in md_file.parts:
            continue

        content = md_file.read_text(encoding="utf-8")
        for match in LINK_PATTERN.finditer(content):
            target = match.group(1).strip().split("#", 1)[0].split("?", 1)[0]
            if not target or target.startswith(SKIP_PREFIXES):
                continue

            resolved = (md_file.parent / target).resolve()
            try:
                resolved.relative_to(root.resolve())
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
