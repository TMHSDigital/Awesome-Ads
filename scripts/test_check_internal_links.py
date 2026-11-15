#!/usr/bin/env python3
"""Tests for the internal link checker."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

_MODULE_PATH = Path(__file__).resolve().with_name("check-internal-links.py")
_SPEC = importlib.util.spec_from_file_location("check_internal_links", _MODULE_PATH)
assert _SPEC is not None and _SPEC.loader is not None
check_internal_links = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(check_internal_links)


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _git(root: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)


class LinkTargetTests(unittest.TestCase):
    def test_plain_target(self) -> None:
        self.assertEqual(check_internal_links.link_target("SEA.md"), "SEA.md")

    def test_title_is_dropped(self) -> None:
        self.assertEqual(
            check_internal_links.link_target('SEA.md "Search ads"'), "SEA.md"
        )

    def test_angle_brackets_keep_spaces(self) -> None:
        self.assertEqual(
            check_internal_links.link_target('<my file.md> "Title"'), "my file.md"
        )

    def test_anchor_and_query_are_dropped(self) -> None:
        self.assertEqual(
            check_internal_links.link_target("SEA.md?utm=1#top"), "SEA.md"
        )


class CollectErrorsTests(unittest.TestCase):
    def test_valid_relative_link(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write(root / "docs" / "page.md", "[Other](other.md)\n")
            _write(root / "docs" / "other.md", "fine\n")
            self.assertEqual(check_internal_links.collect_errors(root), [])

    def test_missing_target(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write(root / "docs" / "page.md", "[Gone](gone.md)\n")
            errors = check_internal_links.collect_errors(root)
            self.assertEqual(len(errors), 1)
            self.assertIn("missing target", errors[0])
            self.assertIn("gone.md", errors[0])

    def test_link_with_title_resolves(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write(root / "docs" / "page.md", '[Search](SEA.md "Search ads")\n')
            _write(root / "docs" / "SEA.md", "sea\n")
            self.assertEqual(check_internal_links.collect_errors(root), [])

    def test_anchor_only_link_is_skipped(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write(root / "docs" / "page.md", "[Top](#top)\n")
            self.assertEqual(check_internal_links.collect_errors(root), [])

    def test_query_link_resolves(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write(root / "docs" / "page.md", "[Sea](SEA.md?utm=1)\n")
            _write(root / "docs" / "SEA.md", "sea\n")
            self.assertEqual(check_internal_links.collect_errors(root), [])

    def test_link_escaping_repo_root(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write(root / "docs" / "page.md", "[Out](../../outside.md)\n")
            errors = check_internal_links.collect_errors(root)
            self.assertEqual(len(errors), 1)
            self.assertIn("external-style path", errors[0])

    @unittest.skipUnless(shutil.which("git"), "git is not available")
    def test_untracked_drafts_are_skipped(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _git(root, "init")
            _write(root / "docs" / "page.md", "[Other](other.md)\n")
            _write(root / "docs" / "other.md", "fine\n")
            _write(root / "research" / "draft.md", "[Broken](../docs/missing.md)\n")
            _git(root, "add", "docs/page.md", "docs/other.md")
            self.assertEqual(check_internal_links.collect_errors(root), [])


if __name__ == "__main__":
    unittest.main()
