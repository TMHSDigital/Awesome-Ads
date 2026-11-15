#!/usr/bin/env python3
"""Tests for the filesystem catalog."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from catalog import (
    first_paragraph,
    mkdocs_nav,
    parse_page,
    render_index_markdown,
    scan_docs,
    summarize,
)


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _docs_tree(root: Path) -> Path:
    docs = root / "docs"
    for folder in ("channels", "resources", "ad-templates", "meta"):
        (docs / folder).mkdir(parents=True)
    return docs


class CatalogTests(unittest.TestCase):
    def test_sea_title_from_h1(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            docs = _docs_tree(Path(tmp))
            _write(
                docs / "channels" / "SEA.md",
                "# Search Engine Advertising (SEA)\n\nBody.\n",
            )
            pages = scan_docs(docs)["channels"]
            self.assertEqual(len(pages), 1)
            self.assertEqual(pages[0].title, "Search Engine Advertising (SEA)")
            self.assertEqual(pages[0].rel, "channels/SEA.md")
            self.assertEqual(pages[0].stem, "SEA")

    def test_skips_agents_and_readme(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            docs = _docs_tree(Path(tmp))
            _write(docs / "channels" / "SEA.md", "# Search\n")
            _write(docs / "channels" / "AGENTS.md", "# Agents\n")
            _write(docs / "channels" / "README.md", "# Readme\n")
            pages = scan_docs(docs)["channels"]
            self.assertEqual([page.stem for page in pages], ["SEA"])

    def test_skips_generated_index(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            docs = _docs_tree(Path(tmp))
            _write(docs / "channels" / "SEA.md", "# Search\n")
            _write(docs / "channels" / "index.md", "# Channels\n")
            pages = scan_docs(docs)["channels"]
            self.assertEqual([page.stem for page in pages], ["SEA"])

    def test_nav_order_before_unordered(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            docs = _docs_tree(Path(tmp))
            _write(docs / "channels" / "ZETA.md", "# Zeta\n")
            _write(
                docs / "channels" / "ALPHA.md",
                "# Alpha\n\n<!-- nav_order: 20 -->\n",
            )
            pages = scan_docs(docs)["channels"]
            self.assertEqual([page.stem for page in pages], ["ALPHA", "ZETA"])

    def test_unordered_sorts_by_title(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            docs = _docs_tree(Path(tmp))
            _write(docs / "channels" / "B.md", "# Bravo\n")
            _write(docs / "channels" / "A.md", "# Alpha\n")
            pages = scan_docs(docs)["channels"]
            self.assertEqual([page.title for page in pages], ["Alpha", "Bravo"])

    def test_missing_h1_raises(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            docs = _docs_tree(Path(tmp))
            path = docs / "channels" / "EMPTY.md"
            _write(path, "No heading here.\n")
            with self.assertRaises(ValueError) as ctx:
                parse_page(path, docs)
            self.assertIn(str(path), str(ctx.exception))

    def test_mkdocs_nav_shape(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            docs = _docs_tree(Path(tmp))
            _write(
                docs / "channels" / "SEA.md",
                "# Search Engine Advertising (SEA)\n\n<!-- nav_order: 10 -->\n",
            )
            _write(docs / "resources" / "LEGAL.md", "# Legal\n")
            nav = mkdocs_nav(docs)
            self.assertEqual(nav[0], {"Home": "index.md"})
            self.assertEqual(nav[-1], {"Contributing": "CONTRIBUTING.md"})
            keys = [next(iter(item)) for item in nav]
            self.assertEqual(
                keys,
                ["Home", "Channels", "Resources", "Templates", "Meta", "Contributing"],
            )
            channels = nav[1]["Channels"]
            self.assertEqual(channels[0], {"Channels": "channels/index.md"})
            self.assertEqual(
                channels[1],
                {"Search Engine Advertising (SEA)": "channels/SEA.md"},
            )
            resources = nav[2]["Resources"]
            self.assertEqual(resources[0], {"Resources": "resources/index.md"})
            templates = nav[3]["Templates"]
            self.assertEqual(templates[0], {"Templates": "ad-templates/index.md"})
            meta = nav[4]["Meta"]
            self.assertEqual(meta[0], {"Meta": "meta/index.md"})

    def test_render_index_uses_prefix(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            docs = _docs_tree(Path(tmp))
            _write(docs / "channels" / "SEA.md", "# Search\n")
            pages = scan_docs(docs)["channels"]
            rendered = render_index_markdown(
                "Channels",
                "Channel guides.",
                pages,
                "channels/",
            )
            self.assertIn("# Channels", rendered)
            self.assertIn("[Search](channels/SEA.md)", rendered)
            self.assertIn("Generated by scripts/prepare-mkdocs.py", rendered)


class SummaryTests(unittest.TestCase):
    def test_skips_heading_and_nav_comment(self) -> None:
        text = "# Title\n<!-- nav_order: 10 -->\n\nFirst **bold** [link](a.md) line.\n\nSecond.\n"
        self.assertEqual(first_paragraph(text), "First bold link line.")

    def test_skips_lists_and_tables(self) -> None:
        text = "# Title\n\n- item\n\n| a |\n| --- |\n\nProse here.\n"
        self.assertEqual(first_paragraph(text), "Prose here.")

    def test_no_prose_returns_empty(self) -> None:
        self.assertEqual(summarize("# Title\n\n- only a list\n"), "")

    def test_short_text_unchanged(self) -> None:
        self.assertEqual(summarize("# T\n\nShort line.\n"), "Short line.")

    def test_long_text_ends_on_sentence(self) -> None:
        first = "A" * 100 + " ends here."
        text = f"# T\n\n{first} " + "More words follow " * 10 + "\n"
        self.assertEqual(summarize(text), first)

    def test_long_text_without_sentence_cut_on_word(self) -> None:
        text = "# T\n\n" + "word " * 60 + "\n"
        result = summarize(text)
        self.assertLessEqual(len(result), 155)
        self.assertTrue(result.endswith("word..."))


def _load_prepare_mkdocs():
    path = Path(__file__).resolve().parent / "prepare-mkdocs.py"
    spec = importlib.util.spec_from_file_location("prepare_mkdocs", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PrepareContributingTests(unittest.TestCase):
    def test_folder_names_are_not_rewritten(self) -> None:
        rewrite = _load_prepare_mkdocs().rewrite_contributing
        text = "│   ├── ad-templates/    # Template and design resources\n"
        self.assertEqual(rewrite(text), text)

    def test_root_links_point_into_docs(self) -> None:
        rewrite = _load_prepare_mkdocs().rewrite_contributing
        rewritten = rewrite(
            "[Docs](docs/README.md) [Guide](docs/meta/COMMUNITY_GUIDELINES.md)"
        )
        self.assertEqual(
            rewritten,
            "[Docs](index.md) [Guide](meta/COMMUNITY_GUIDELINES.md)",
        )


if __name__ == "__main__":
    unittest.main()
