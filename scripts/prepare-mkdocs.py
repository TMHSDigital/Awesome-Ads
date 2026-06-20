#!/usr/bin/env python3
"""Prepare generated files for MkDocs build."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTRIBUTING_SRC = ROOT / "CONTRIBUTING.md"
CONTRIBUTING_DST = ROOT / "docs" / "CONTRIBUTING.md"


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


def main() -> int:
    prepare_contributing()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
