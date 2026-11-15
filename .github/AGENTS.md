# Agents: GitHub automation

CI, deployment, and repository automation under `.github/`.

## Workflows

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| [workflows/ci.yml](workflows/ci.yml) | Push/PR to `main` | Markdown lint, repo hygiene, internal links, MkDocs build |
| [workflows/pages.yml](workflows/pages.yml) | Push to `main` | Build MkDocs site and deploy to GitHub Pages |
| [workflows/link-check-scheduled.yml](workflows/link-check-scheduled.yml) | Weekly + manual | External link check via Lychee |
| [workflows/release.yml](workflows/release.yml) | `v*.*.*` tag push + manual | Publish a GitHub release for the tag |

## Key config

| File | Purpose |
|------|---------|
| [lychee.toml](lychee.toml) | External link checker settings |
| [ISSUE_TEMPLATE/](ISSUE_TEMPLATE/) | Issue form for content problems |
| [PULL_REQUEST_TEMPLATE.md](PULL_REQUEST_TEMPLATE.md) | PR checklist for contributors |

## When editing workflows

- Pin actions to major version tags (e.g. `@v7`), consistent with existing files.
- CI must stay fast: this repo is markdown-only.
- Pages workflow runs `scripts/prepare-mkdocs.py` before building; do not commit `docs/CONTRIBUTING.md`, `docs/index.md`, or `docs/*/index.md`.
- Required permissions: `contents: read` for CI; add `pages: write` and `id-token: write` for Pages deploy.

## Dependency updates

Dependabot is turned off. Update pinned actions and `requirements-docs.txt` by hand, then run the validation checks before opening a PR. After changing `requirements-docs.txt`, regenerate `constraints-docs.txt` from a clean Python 3.12 venv (the steps are in the file header); CI and the Pages deploy install with `-c constraints-docs.txt`.

## Releases

Releases are cut by maintainers only, from `main`, with [workflows/release.yml](workflows/release.yml). Either push an annotated tag (`git tag -a v1.2.0 -m "What changed" && git push origin v1.2.0`) or run the Release workflow from the Actions tab with a version. The tag message is the top of the release notes; GitHub appends the pull requests merged since the last release.

Version numbers follow this rule for a documentation repo:

- **Major**: guides are reorganized or removed, or published URLs change.
- **Minor**: a new guide or a substantial new section.
- **Patch**: corrections, updated figures, and site fixes.

Do not tag or release unless the user asks.

## Parent context

[../AGENTS.md](../AGENTS.md)
