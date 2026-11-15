#!/usr/bin/env python3
"""Verify relative markdown links point to existing files."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

LINK_PATTERN = re.compile(r"\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#", "ftp://")


def link_target(raw: str) -> str:
    """Return the file part of a markdown link target.

    Drops an optional title (`SEA.md "Search ads"`), an optional `<...>`
    wrapper, and any anchor or query string.
    """
    target = raw.strip()
    if target.startswith("<"):
        end = target.find(">")
        target = target[1:end] if end != -1 else target[1:]
    else:
        # A link target cannot contain an unescaped space, so the first
        # whitespace-separated token is the target and the rest is the title.
        parts = target.split(None, 1)
        target = parts[0] if parts else ""
    return target.split("#", 1)[0].split("?", 1)[0]


def _git_markdown_files(root: Path) -> list[Path] | None:
    """Markdown files tracked by git, or None when root is not a git checkout."""
    try:
        completed = subprocess.run(
            ["git", "ls-files", "-z", "--", "*.md"],
            cwd=root,
            capture_output=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    names = completed.stdout.decode("utf-8").split("\0")
    return [root / name for name in names if name]


def iter_markdown_files(root: Path) -> list[Path]:
    """Markdown files worth checking.

    Tracked files only, plus the generated pages under `docs/`, so a local run
    does not fail on gitignored drafts such as `research/`.
    """
    tracked = _git_markdown_files(root)
    if tracked is None:
        return sorted(md for md in root.rglob("*.md") if ".git" not in md.parts)

    files = {md.resolve() for md in tracked}
    docs = root / "docs"
    if docs.is_dir():
        files.update(md.resolve() for md in docs.rglob("*.md"))
    return sorted(files)


def collect_errors(root: Path) -> list[str]:
    errors: list[str] = []

    for md_file in iter_markdown_files(root):
        if not md_file.is_file():
            continue

        content = md_file.read_text(encoding="utf-8")
        for match in LINK_PATTERN.finditer(content):
            target = link_target(match.group(1))
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
