# Agents: GitHub automation

CI, deployment, and repository automation under `.github/`.

## Workflows

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| [workflows/ci.yml](workflows/ci.yml) | Push/PR to `main` | Markdown lint, repo hygiene, internal links, MkDocs build |
| [workflows/pages.yml](workflows/pages.yml) | Push to `main` | Build MkDocs site and deploy to GitHub Pages |
| [workflows/link-check-scheduled.yml](workflows/link-check-scheduled.yml) | Weekly + manual | External link check via Lychee |

## Key config

| File | Purpose |
|------|---------|
| [dependabot.yml](dependabot.yml) | Weekly GitHub Actions version updates |
| [lychee.toml](lychee.toml) | External link checker settings |
| [ISSUE_TEMPLATE/](ISSUE_TEMPLATE/) | Issue form for content problems |
| [PULL_REQUEST_TEMPLATE.md](PULL_REQUEST_TEMPLATE.md) | PR checklist for contributors |

## When editing workflows

- Pin actions to major version tags (e.g. `@v7`), consistent with existing files.
- CI must stay fast: this repo is markdown-only.
- Pages workflow runs `scripts/prepare-mkdocs.py` before building; do not commit `docs/CONTRIBUTING.md`.
- Required permissions: `contents: read` for CI; add `pages: write` and `id-token: write` for Pages deploy.

## Dependabot PRs

If Dependabot PRs conflict with recent `main` changes, apply version bumps directly on `main`, run CI locally, push, and close the PRs with a short comment.

## Parent context

[../AGENTS.md](../AGENTS.md)
