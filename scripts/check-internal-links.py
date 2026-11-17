#!/usr/bin/env python3
"""Verify relative markdown links point to existing files."""

from __future__ import annotations

import re
import subprocess
import sys
import unicodedata
from pathlib import Path

LINK_PATTERN = re.compile(r"\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#", "ftp://")


def _link_url(raw: str) -> str:
    """Return the URL of a markdown link target, without title or `<...>`."""
    target = raw.strip()
    if target.startswith("<"):
        end = target.find(">")
        return target[1:end] if end != -1 else target[1:]
    # A link target cannot contain an unescaped space, so the first
    # whitespace-separated token is the target and the rest is the title.
    parts = target.split(None, 1)
    return parts[0] if parts else ""


def link_target(raw: str) -> str:
    """Return the file part of a markdown link target.

    Drops an optional title (`SEA.md "Search ads"`), an optional `<...>`
    wrapper, and any anchor or query string.
    """
    return _link_url(raw).split("#", 1)[0].split("?", 1)[0]


def link_fragment(raw: str) -> str:
    """Return the `#anchor` part of a markdown link target, without the `#`."""
    url = _link_url(raw)
    return url.split("#", 1)[1] if "#" in url else ""


HEADING_PATTERN = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$")
FENCE_PATTERN = re.compile(r"^\s*(```|~~~)")
CUSTOM_ID_PATTERN = re.compile(r"\s*\{[^}]*#([\w-]+)[^}]*\}\s*$")
INLINE_LINK_PATTERN = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")


def _slugify(text: str) -> str:
    """Python-Markdown's default `toc` slug: keep words, spaces, and hyphens."""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[-\s]+", "-", text)


def heading_ids(markdown: str) -> set[str]:
    """Anchor ids the `toc` extension gives this page's headings.

    Handles `{#custom-id}` attributes and the `_1`, `_2` suffixes added to
    repeated headings. Lines inside fenced code blocks are not headings.
    """
    ids: set[str] = set()
    in_fence = False
    for line in markdown.splitlines():
        if FENCE_PATTERN.match(line):
            in_fence = not in_fence
            continue
        match = None if in_fence else HEADING_PATTERN.match(line)
        if not match:
            continue
        text = match.group(1)
        custom = CUSTOM_ID_PATTERN.search(text)
        if custom:
            ids.add(custom.group(1))
            continue
        text = INLINE_LINK_PATTERN.sub(r"\1", text)
        slug = base = _slugify(re.sub(r"[*_`]", "", text))
        count = 0
        while slug in ids:
            count += 1
            slug = f"{base}_{count}"
        ids.add(slug)
    return ids


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
    anchors: dict[Path, set[str]] = {}

    def has_anchor(page: Path, fragment: str) -> bool:
        if page not in anchors:
            anchors[page] = heading_ids(page.read_text(encoding="utf-8"))
        return fragment in anchors[page]

    for md_file in iter_markdown_files(root):
        if not md_file.is_file():
            continue

        content = md_file.read_text(encoding="utf-8")
        for match in LINK_PATTERN.finditer(content):
            target = link_target(match.group(1))
            fragment = link_fragment(match.group(1))
            if not target:
                if fragment and not has_anchor(md_file, fragment):
                    errors.append(f"{md_file}: missing anchor {'#' + fragment!r}")
                continue
            if target.startswith(SKIP_PREFIXES):
                continue

            resolved = (md_file.parent / target).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                errors.append(f"{md_file}: external-style path {target!r}")
                continue

            if not resolved.exists():
                errors.append(f"{md_file}: missing target {target!r}")
            elif fragment and resolved.suffix == ".md" and not has_anchor(resolved, fragment):
                errors.append(f"{md_file}: missing anchor {target + '#' + fragment!r}")

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
