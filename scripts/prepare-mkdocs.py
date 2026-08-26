#!/usr/bin/env python3
"""Prepare generated files for MkDocs build."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from catalog import (  # noqa: E402
    SECTIONS,
    SECTION_INTROS,
    render_home_markdown,
    render_index_markdown,
    scan_docs,
)

CONTRIBUTING_SRC = ROOT / "CONTRIBUTING.md"
CONTRIBUTING_DST = ROOT / "docs" / "CONTRIBUTING.md"
DOCS = ROOT / "docs"


def prepare_contributing() -> None:
    text = CONTRIBUTING_SRC.read_text(encoding="utf-8")
    text = text.replace("](docs/README.md)", "](index.md)")
    text = text.replace("](docs/meta/", "](meta/")
    text = text.replace(
        "](README.md)",
        "](https://github.com/TMHSDigital/Awesome-Ads/blob/main/README.md)",
    )
    text = text.replace("templates/", "ad-templates/")
    CONTRIBUTING_DST.write_text(text, encoding="utf-8")
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


def main() -> int:
    prepare_contributing()
    prepare_indexes()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
