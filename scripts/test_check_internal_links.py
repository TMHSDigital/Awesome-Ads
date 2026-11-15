#!/usr/bin/env python3
"""Exercise the internal link checker against temporary Git repositories."""

from __future__ import annotations

import runpy
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
collect_errors = runpy.run_path(str(SCRIPTS / "check-internal-links.py"))["collect_errors"]


class InternalLinkTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(self.enterContext(tempfile.TemporaryDirectory()))
        self.git("init", "--quiet")

    def git(self, *args: str) -> None:
        subprocess.run(["git", *args], cwd=self.root, check=True, capture_output=True)

    def write(self, name: str, text: str, *, tracked: bool = True) -> Path:
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        if tracked:
            self.git("add", "--", name)
        return path

    def test_relative_links_resolve_with_or_without_a_fragment_or_query(self) -> None:
        self.write("docs/channels/SEA.md", "# Search ads\n")
        self.write(
            "docs/README.md",
            "[Search](channels/SEA.md)\n"
            "[Search](channels/SEA.md?view=short#search-ads)\n"
            "[This page](#overview)\n"
            "[This page](?view=short)\n",
        )
        self.assertEqual(collect_errors(self.root), [])

    def test_uses_the_destination_of_a_link_with_a_title(self) -> None:
        self.write("docs/channels/SEA.md", "# Search ads\n")
        self.write(
            "docs/channels/README.md",
            "[Search](SEA.md \"Search ads\")\n"
            "[Search](SEA.md#search-ads 'Search ads')\n"
            "[Search](SEA.md (Search ads))\n",
        )
        self.assertEqual(collect_errors(self.root), [])

    def test_reports_a_missing_target_even_with_a_title(self) -> None:
        page = self.write("README.md", '[Missing](MISSING.md "A missing page")\n')
        self.assertEqual(collect_errors(self.root), [f"{page}: missing target 'MISSING.md'"])

    def test_reports_a_path_that_escapes_the_repository(self) -> None:
        page = self.write("README.md", "[Outside](../OUTSIDE.md)\n")
        self.assertEqual(
            collect_errors(self.root), [f"{page}: external-style path '../OUTSIDE.md'"]
        )

    def test_excludes_gitignored_drafts(self) -> None:
        self.write(".gitignore", "/research/\n/docs/drafts/\n")
        self.write("README.md", "# Tracked page\n")
        self.write("research/DRAFT.md", "[Missing](MISSING.md)\n", tracked=False)
        self.write("docs/drafts/DRAFT.md", "[Missing](MISSING.md)\n", tracked=False)
        self.assertEqual(collect_errors(self.root), [])

    def test_checks_generated_pages(self) -> None:
        names = ("docs/CONTRIBUTING.md", "docs/index.md", "docs/channels/index.md")
        self.write(".gitignore", "".join(f"/{name}\n" for name in names))
        pages = [self.write(name, "[Missing](MISSING.md)\n", tracked=False) for name in names]
        self.assertCountEqual(
            collect_errors(self.root), [f"{page}: missing target 'MISSING.md'" for page in pages]
        )


if __name__ == "__main__":
    unittest.main()
