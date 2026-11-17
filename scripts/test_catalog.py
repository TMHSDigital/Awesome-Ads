#!/usr/bin/env python3
"""Tests for the filesystem catalog."""

from __future__ import annotations

import importlib.util
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from datetime import date
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))

import catalog
from catalog import (
    BUILD_CONFIG,
    first_paragraph,
    first_sentence,
    generated_doc_paths,
    generated_front_matter,
    mkdocs_nav,
    parse_page,
    render_build_config,
    render_home_markdown,
    render_index_markdown,
    review_status,
    scan_docs,
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

    def test_review_date_is_optional_header_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            docs = _docs_tree(Path(tmp))
            guide = docs / "channels" / "SEA.md"
            _write(guide, "# Search\n<!-- nav_order: 20 -->\n<!-- reviewed: 2024-02-29 -->\n\nBody.\n")
            page = parse_page(guide, docs)
            self.assertEqual(page.reviewed_on, date(2024, 2, 29))
            self.assertEqual(page.nav_order, 20)
            for text in (
                "# Search\n",
                "# Search\n<!-- reviewed: 2023-02-29 -->\n",
                "# Search\n\nBody.\n\n<!-- reviewed: 2024-02-29 -->\n",
            ):
                with self.subTest(text=text):
                    _write(guide, text)
                    self.assertIsNone(parse_page(guide, docs).reviewed_on)

    def test_review_warnings_use_calendar_anniversary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            docs = _docs_tree(Path(tmp))
            for filename, marker in (
                ("fresh", "<!-- reviewed: 2025-11-16 -->"),
                ("stale", "<!-- reviewed: 2025-11-15 -->"),
                ("future", "<!-- reviewed: 2026-11-17 -->"),
                ("missing", ""),
            ):
                _write(docs / "resources" / f"{filename}.md", f"# {filename}\n{marker}\n")
            _write(docs / "meta" / "POLICY.md", "# Policy\n")
            dates, notices = review_status(scan_docs(docs), date(2026, 11, 16))
            self.assertEqual(dates, {"resources/fresh.md": "2025-11-16", "resources/stale.md": "2025-11-15"})
            self.assertEqual(notices, [
                "resources/future.md has a future review date",
                "resources/missing.md has no valid review date",
                "resources/stale.md has not been reviewed in the past 12 months",
            ])

    def test_review_anniversary_on_leap_day(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            docs = _docs_tree(Path(tmp))
            _write(docs / "channels" / "SEA.md", "# Search\n<!-- reviewed: 2023-02-28 -->\n")
            _dates, notices = review_status(scan_docs(docs), date(2024, 2, 29))
            self.assertEqual(notices, [])

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


class GuideListTests(unittest.TestCase):
    def test_index_lists_summary_after_link(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            docs = _docs_tree(Path(tmp))
            _write(docs / "channels" / "SEA.md", "# Search\n\nAds on results pages.\n")
            pages = scan_docs(docs)["channels"]
            rendered = render_index_markdown("Channels", "Intro.", pages, "")
            self.assertIn("- [Search](SEA.md): Ads on results pages.", rendered)

    def test_home_has_start_section_and_summaries(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            docs = _docs_tree(Path(tmp))
            _write(docs / "resources" / "LEGAL.md", "# Legal\n\nRules to follow.\n")
            home = render_home_markdown(docs)
            self.assertIn("## Where to start", home)
            self.assertIn("- [Legal](resources/LEGAL.md): Rules to follow.", home)
            self.assertLess(home.index("## Where to start"), home.index("## Channels"))


class GeneratedFrontMatterTests(unittest.TestCase):
    """overrides/partials/actions.html hides or redirects edit links using this."""

    def test_home_and_indexes_are_marked_generated(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            docs = _docs_tree(Path(tmp))
            _write(docs / "channels" / "SEA.md", "# Search\n\nAds.\n")
            pages = scan_docs(docs)["channels"]
            for rendered in (
                render_home_markdown(docs),
                render_index_markdown("Channels", "Intro.", pages, ""),
            ):
                self.assertTrue(rendered.startswith("---\ngenerated: true\n---\n"))
                self.assertNotIn("source:", rendered)

    def test_contributing_copy_points_at_root_file(self) -> None:
        prepare = _load_script("prepare-mkdocs.py")
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "CONTRIBUTING.md"
            dst = Path(tmp) / "docs" / "CONTRIBUTING.md"
            _write(src, "# Contributing\n")
            dst.parent.mkdir()
            with patch.object(prepare, "CONTRIBUTING_SRC", src), patch.object(
                prepare, "CONTRIBUTING_DST", dst
            ), patch.object(prepare, "ROOT", Path(tmp)), redirect_stdout(io.StringIO()):
                prepare.prepare_contributing()
            self.assertTrue(
                dst.read_text(encoding="utf-8").startswith(
                    "---\ngenerated: true\nsource: CONTRIBUTING.md\n---\n# Contributing"
                )
            )

    def test_generated_pages_still_have_summaries(self) -> None:
        text = generated_front_matter() + "# Title\n\nFirst line.\n"
        self.assertEqual(first_paragraph(text), "First line.")


class ReadmeTests(unittest.TestCase):
    """The root README lists every reader-facing guide."""

    def test_every_guide_is_linked_from_readme(self) -> None:
        root = Path(__file__).resolve().parent.parent
        readme = (root / "README.md").read_text(encoding="utf-8")
        scanned = scan_docs(root / "docs")
        missing = [
            page.rel
            for folder in ("channels", "resources", "ad-templates")
            for page in scanned[folder]
            if f"](docs/{page.rel})" not in readme
        ]
        self.assertEqual(
            missing,
            [],
            "Add these guides to the tables in README.md",
        )


class SummaryTests(unittest.TestCase):
    def test_skips_heading_and_nav_comment(self) -> None:
        text = "# Title\n<!-- nav_order: 10 -->\n\nFirst **bold** [link](a.md) line.\n\nSecond.\n"
        self.assertEqual(first_paragraph(text), "First bold link line.")

    def test_skips_lists_and_tables(self) -> None:
        text = "# Title\n\n- item\n\n| a |\n| --- |\n\nProse here.\n"
        self.assertEqual(first_paragraph(text), "Prose here.")

    def test_first_sentence(self) -> None:
        text = "# T\n\nPrint works in (some) cases. It is not a default.\n"
        self.assertEqual(first_sentence(text), "Print works in (some) cases.")

    def test_no_prose_returns_empty(self) -> None:
        self.assertEqual(first_sentence("# Title\n\n- only a list\n"), "")


def _load_script(filename: str):
    path = Path(__file__).resolve().parent / filename
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PrepareContributingTests(unittest.TestCase):
    def test_folder_names_are_not_rewritten(self) -> None:
        rewrite = _load_script("prepare-mkdocs.py").rewrite_contributing
        text = "│   ├── ad-templates/    # Template and design resources\n"
        self.assertEqual(rewrite(text), text)

    def test_root_links_point_into_docs(self) -> None:
        rewrite = _load_script("prepare-mkdocs.py").rewrite_contributing
        rewritten = rewrite(
            "[Docs](docs/README.md) [Guide](docs/meta/COMMUNITY_GUIDELINES.md)"
        )
        self.assertEqual(
            rewritten,
            "[Docs](index.md) [Guide](meta/COMMUNITY_GUIDELINES.md)",
        )


class GeneratedDocsTests(unittest.TestCase):
    def test_hygiene_rejects_tracked_index_for_new_section(self) -> None:
        index = "docs/new-section/index.md"
        stderr = io.StringIO()
        sections = (*catalog.SECTIONS, ("new-section", "New Section"))
        with patch.object(catalog, "SECTIONS", sections), redirect_stderr(stderr):
            hygiene = _load_script("check-public-repo-hygiene.py")
            with patch.object(hygiene, "tracked_files", return_value=[index]):
                result = hygiene.main()

        self.assertEqual(result, 1)
        self.assertIn(index, stderr.getvalue())

    def test_configs_exclude_generated_docs(self) -> None:
        root = Path(__file__).resolve().parent.parent
        gitignore = (root / ".gitignore").read_text(encoding="utf-8")
        lint_config = json.loads(
            (root / ".markdownlint-cli2.jsonc").read_text(encoding="utf-8")
        )


        expected = set(generated_doc_paths())
        for filename, exclusions in (
            (".gitignore", {line.strip().removeprefix("/") for line in gitignore.splitlines()}),
            (".markdownlint-cli2.jsonc", set(lint_config["ignores"])),
        ):
            with self.subTest(config=filename):
                missing = ", ".join(sorted(expected - exclusions))
                self.assertFalse(missing, f"{filename} must exclude generated paths: {missing}")


class BuildConfigTests(unittest.TestCase):
    def test_build_config_appends_catalog_nav(self) -> None:
        nav = [{"Home": "index.md"}, {"Channels": [{"Channels": "channels/index.md"}]}]
        rendered = render_build_config("site_name: Awesome Ads\r\ntheme:\r\n  name: material\r\n", nav)
        self.assertTrue(rendered.startswith("# Generated by scripts/prepare-mkdocs.py"))
        self.assertIn("site_name: Awesome Ads\ntheme:\n  name: material\n", rendered)
        nav_line = rendered.strip().splitlines()[-1]
        self.assertTrue(nav_line.startswith("nav: "))
        self.assertEqual(json.loads(nav_line.removeprefix("nav: ")), nav)

    def test_build_config_adds_review_dates_by_source_path(self) -> None:
        dates = {"channels/SEA.md": "2026-11-16", "resources/LEGAL.md": "2026-05-01"}
        rendered = render_build_config("site_name: Awesome Ads\n", [], dates)
        extra_line = next(line for line in rendered.splitlines() if line.startswith("extra: "))
        self.assertEqual(json.loads(extra_line.removeprefix("extra: ")), {"reviewed_dates": dates})

    def test_build_config_rejects_base_extra(self) -> None:
        for dates in ({"channels/SEA.md": "2026-11-16"}, {}):
            with self.subTest(dates=dates), self.assertRaisesRegex(ValueError, "extra"):
                render_build_config("site_name: X\nextra:\n  generator: false\n", [], dates)

    def test_base_config_has_no_hooks_nav_or_extra(self) -> None:
        root = Path(__file__).resolve().parent.parent
        base = (root / "mkdocs.yml").read_text(encoding="utf-8")
        self.assertNotRegex(
            base, r"(?m)^(hooks|nav|extra):", "mkdocs.yml must not set hooks, nav, or extra"
        )

    def test_build_config_is_ignored_and_rejected(self) -> None:
        root = Path(__file__).resolve().parent.parent
        gitignore = (root / ".gitignore").read_text(encoding="utf-8").splitlines()
        self.assertIn(BUILD_CONFIG, gitignore)
        hygiene = _load_script("check-public-repo-hygiene.py")
        stderr = io.StringIO()
        with patch.object(hygiene, "tracked_files", return_value=[BUILD_CONFIG]), redirect_stderr(stderr):
            self.assertEqual(hygiene.main(), 1)
        self.assertIn(BUILD_CONFIG, stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
