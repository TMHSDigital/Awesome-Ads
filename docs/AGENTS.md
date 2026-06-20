# Agents: Documentation

You are working inside the `docs/` tree. All user-facing guides live here.

## Subdirectories

| Directory | Contents | Agent instructions |
|-----------|----------|-------------------|
| [channels/](channels/) | Channel-specific advertising guides | [channels/AGENTS.md](channels/AGENTS.md) |
| [resources/](resources/) | Cross-cutting planning and compliance topics | [resources/AGENTS.md](resources/AGENTS.md) |
| [ad-templates/](ad-templates/) | Ad templates and design resources | [ad-templates/AGENTS.md](ad-templates/AGENTS.md) |
| [meta/](meta/) | Repository outline and community policy | [meta/AGENTS.md](meta/AGENTS.md) |

## Index

[README.md](README.md) is the canonical table of contents for this folder. Keep it in sync when adding or removing pages. Also update [mkdocs.yml](../mkdocs.yml) navigation and [index.md](index.md) when the change affects the published site.

## Link conventions

Links between docs should be **relative to the current file**:

- From `docs/README.md` to a channel: `channels/SEA.md`
- From `docs/channels/SEA.md` to a resource: `../resources/ANALYTICS.md`
- From `docs/ad-templates/SOCIAL_MEDIA.md` to the hub: `TEMPLATES.md`

Links from the root [README.md](../README.md) use the `docs/` prefix (e.g. `docs/channels/SEA.md`).

## Adding a new page

1. Place the file in the correct subdirectory (`channels/`, `resources/`, or `ad-templates/`).
2. Add an entry to [README.md](README.md) and [mkdocs.yml](../mkdocs.yml).
3. Update the root [README.md](../README.md) if the page should appear on the landing page.
4. Update [index.md](index.md) if the page should appear on the site home page.
5. Update [meta/REPO_OUTLINE.md](meta/REPO_OUTLINE.md) for structural changes.
6. Run validation from the repo root (see [CONTRIBUTING.md](../CONTRIBUTING.md)).

## Content standards

- One primary `#` heading per file matching the topic title.
- Use `##` and `###` for sections; keep hierarchy logical.
- End every file with a single trailing newline.
- External tool links (Google Ads, Meta, etc.) are welcome in "Tools and Resources" sections.
- Do not duplicate large blocks across files; cross-link instead.

## Parent context

Repo-wide agent instructions: [../AGENTS.md](../AGENTS.md)
