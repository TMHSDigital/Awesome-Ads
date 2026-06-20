# Agents: Scripts

Maintenance utilities for repository quality checks.

## Files

| File | Purpose |
|------|---------|
| `check-internal-links.py` | Validates that relative `markdown` links resolve to existing files |
| `check-public-repo-hygiene.py` | Fails if local-only paths or secret-like content are tracked in git |
| `prepare-mkdocs.py` | Generates `docs/CONTRIBUTING.md` with site-relative links for MkDocs builds |

## check-internal-links.py

- Scans all `*.md` files under the repo root (skips `.git`).
- Resolves relative link targets from the containing file's directory.
- Skips `http://`, `https://`, `mailto:`, `#`, and `ftp://` URLs.
- Exit code `0` on success, `1` when broken links are found.
- Runs `prepare-mkdocs.py` first so generated files such as `docs/CONTRIBUTING.md` exist before link resolution.

Run from the repository root:

```bash
python scripts/check-internal-links.py
```

## When modifying

- Keep the script dependency-free (stdlib only) so CI can run it with `actions/setup-python` and no `pip install`.
- If link syntax rules change, update this script and [.github/workflows/ci.yml](../.github/workflows/ci.yml) together.
- Do not use this script for external URL validation; that is handled by the scheduled Lychee workflow.

## Parent context

[../AGENTS.md](../AGENTS.md)
