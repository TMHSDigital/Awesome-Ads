# Agents

Instructions for AI coding agents working in the Awesome Ads repository.

## Purpose

This repository is a **markdown documentation project**. There is no application runtime, package manager, or deployable service beyond GitHub Pages (Jekyll). Your job is usually to edit, add, or reorganize guides and keep links, CI, and navigation consistent.

## Repository layout

```
docs/
├── channels/     # One guide per advertising channel (SEA, SOCIAL, …)
├── resources/    # Cross-cutting topics (analytics, legal, FAQ, …)
├── templates/    # Template and design resources
└── meta/         # Repo documentation and community policy
.github/          # CI workflows, Dependabot, issue/PR templates
scripts/          # Maintenance scripts (internal link checker)
```

Each directory has its own `AGENTS.md` with scope-specific rules. Read the nearest `AGENTS.md` to the files you are editing.

## Before you change anything

1. Read [CONTRIBUTING.md](CONTRIBUTING.md) for contributor expectations.
2. Read [docs/meta/COMMUNITY_GUIDELINES.md](docs/meta/COMMUNITY_GUIDELINES.md) for tone and conduct.
3. Skim [docs/README.md](docs/README.md) and the root [README.md](README.md) to understand navigation.

## Editing rules

- **Audience:** Small-business owners and marketers. Write clearly; avoid jargon without explanation.
- **Links:** Use relative paths only so pages work on GitHub and GitHub Pages.
- **Filenames:** Keep existing UPPERCASE names for channel/resource files (e.g. `SEA.md`, `BUDGETING.md`).
- **Navigation:** When adding or renaming a page, update:
  - [docs/README.md](docs/README.md)
  - [README.md](README.md) (if the page is linked from the landing page)
  - [docs/meta/REPO_OUTLINE.md](docs/meta/REPO_OUTLINE.md) when structure changes
- **Style:** No emojis in prose unless already present in a file you are not rewriting. Prefer complete sentences. Avoid em dashes in new copy; use commas, periods, or hyphens instead.
- **Scope:** Do not expand scope into code, apps, or infrastructure unless explicitly requested.

## Validation

Run before opening a PR:

```bash
npx markdownlint-cli2 "**/*.md"
python scripts/check-internal-links.py
```

CI runs the same checks on pull requests. External link checking runs on a weekly schedule.

## GitHub Pages

Site config lives in [_config.yml](_config.yml). The [Deploy GitHub Pages](.github/workflows/pages.yml) workflow builds with Jekyll and publishes from `main`. Content under `docs/` is included in the site; root policy files and `AGENTS.md` files are excluded.

## Do not

- Commit secrets or credentials.
- Add unrelated tooling (frameworks, package.json, etc.) without explicit request.
- Break relative links or leave orphaned files out of the table of contents.
- Run destructive git commands unless the user explicitly asks.

## Related files

| File | Role |
|------|------|
| [AGENTS.md](AGENTS.md) | This file (repo root) |
| [docs/AGENTS.md](docs/AGENTS.md) | Documentation tree overview |
| [scripts/AGENTS.md](scripts/AGENTS.md) | Maintenance scripts |
| [.github/AGENTS.md](.github/AGENTS.md) | CI and automation |
