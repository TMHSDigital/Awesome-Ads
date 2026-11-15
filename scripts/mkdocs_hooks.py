#!/usr/bin/env python3
"""MkDocs hooks: build nav from the filesystem catalog and fill page descriptions."""

from __future__ import annotations

import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from catalog import mkdocs_nav, summarize  # noqa: E402


def on_config(config):
    docs = Path(config["docs_dir"])
    config["nav"] = mkdocs_nav(docs)
    return config


def on_page_markdown(markdown, page, config, files):
    """Give each page its own meta description from its first paragraph.

    A `description` set in front matter wins. Pages with no prose fall back
    to the site description.
    """
    if not page.meta.get("description"):
        summary = summarize(markdown)
        if summary:
            page.meta["description"] = summary
    return markdown
