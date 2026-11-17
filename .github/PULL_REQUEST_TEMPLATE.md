# Pull request

## Summary

<!-- What changed and why? -->

## Checklist

CI runs every check below. Running them first saves a round trip (see Prerequisites in CONTRIBUTING.md).

- [ ] Markdown lint passes (`npx markdownlint-cli2@0.24.0 "**/*.md"`)
- [ ] Unit tests pass (`python -m unittest scripts.test_catalog scripts.test_check_internal_links`)
- [ ] Repo hygiene check passes (`python scripts/check-public-repo-hygiene.py`)
- [ ] Links are relative and resolve (`python scripts/check-internal-links.py`)
- [ ] Site builds (`python scripts/prepare-mkdocs.py` then `zensical build --strict -f mkdocs.gen.yml`)
- [ ] New pages have an H1 (optional `nav_order` comment) and a row in the README guide tables. Do not add a nav to `mkdocs.yml`.
- [ ] Guides you reviewed against their sources have an updated `<!-- reviewed: YYYY-MM-DD -->` line after the H1.
