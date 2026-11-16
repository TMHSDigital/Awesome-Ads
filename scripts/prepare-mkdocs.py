#!/usr/bin/env python3
"""Prepare generated files for the site build."""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from catalog import (  # noqa: E402
    BUILD_CONFIG,
    SECTIONS,
    SECTION_INTROS,
    generated_front_matter,
    mkdocs_nav,
    render_build_config,
    render_home_markdown,
    render_index_markdown,
    review_status,
    scan_docs,
)

CONTRIBUTING_SRC = ROOT / "CONTRIBUTING.md"
CONTRIBUTING_DST = ROOT / "docs" / "CONTRIBUTING.md"
DOCS = ROOT / "docs"


def rewrite_contributing(text: str) -> str:
    """Rewrite root-relative links in CONTRIBUTING.md for its place in docs/."""
    text = text.replace("](docs/README.md)", "](index.md)")
    text = text.replace("](docs/meta/", "](meta/")
    return text.replace(
        "](README.md)",
        "](https://github.com/TMHSDigital/Awesome-Ads/blob/main/README.md)",
    )


def prepare_contributing() -> None:
    text = rewrite_contributing(CONTRIBUTING_SRC.read_text(encoding="utf-8"))
    front_matter = generated_front_matter(source=CONTRIBUTING_SRC.name)
    CONTRIBUTING_DST.write_text(front_matter + text, encoding="utf-8")
    print(f"Wrote {CONTRIBUTING_DST.relative_to(ROOT)}")


def prepare_indexes() -> None:
    home = DOCS / "index.md"
    home.write_text(render_home_markdown(DOCS), encoding="utf-8")
    print(f"Wrote {home.relative_to(ROOT)}")

    scanned = scan_docs(DOCS)
    for folder, title in SECTIONS:
        path = DOCS / folder / "index.md"
        path.write_text(
            render_index_markdown(
                title,
                SECTION_INTROS[folder],
                scanned[folder],
                "",
            ),
            encoding="utf-8",
        )
        print(f"Wrote {path.relative_to(ROOT)}")


def prepare_build_config() -> None:
    path = ROOT / BUILD_CONFIG
    base = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    dates, notices = review_status(scan_docs(DOCS), date.today())
    for notice in notices:
        print(f"Warning: {notice}", file=sys.stderr)
    path.write_text(render_build_config(base, mkdocs_nav(DOCS), dates), encoding="utf-8")
    print(f"Wrote {path.relative_to(ROOT)}")


def main() -> int:
    prepare_contributing()
    prepare_indexes()
    prepare_build_config()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
