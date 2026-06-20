#!/usr/bin/env python3
"""Fail if local-only or generated paths are tracked in git."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FORBIDDEN_TRACKED_PATHS = (
    "research/",
    "site/",
    "docs/CONTRIBUTING.md",
)

FORBIDDEN_TRACKED_SUFFIXES = (
    ".env",
    ".pem",
    ".key",
    ".p12",
    ".pfx",
)

SENSITIVE_CONTENT_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bghp_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk_(?:live|test)_[A-Za-z0-9]{10,}\b"),
)


def tracked_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return [entry for entry in result.stdout.decode("utf-8").split("\0") if entry]


def main() -> int:
    errors: list[str] = []

    for path in tracked_files():
        if path.startswith(FORBIDDEN_TRACKED_PATHS) or path in FORBIDDEN_TRACKED_PATHS:
            errors.append(f"Tracked local-only path must not be committed: {path}")
            continue

        if path.endswith(FORBIDDEN_TRACKED_SUFFIXES):
            errors.append(f"Tracked secret-like file must not be committed: {path}")
            continue

        file_path = ROOT / path
        if not file_path.is_file():
            continue

        try:
            content = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        for pattern in SENSITIVE_CONTENT_PATTERNS:
            if pattern.search(content):
                errors.append(
                    f"Possible secret pattern in tracked file: {path} ({pattern.pattern})"
                )
                break

    if errors:
        print("Public repo hygiene check failed:\n", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print("Public repo hygiene check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
