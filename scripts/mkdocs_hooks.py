#!/usr/bin/env python3
"""MkDocs hook: build nav from the filesystem catalog."""

from __future__ import annotations

import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from catalog import mkdocs_nav  # noqa: E402


def on_config(config):
    docs = Path(config["docs_dir"])
    config["nav"] = mkdocs_nav(docs)
    return config
