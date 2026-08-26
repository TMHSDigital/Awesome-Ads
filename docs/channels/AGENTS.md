# Agents: Channels

This directory contains **one guide per advertising channel**. Each file is a standalone reference for small businesses evaluating or running that channel.

The markdown files in this directory are the catalog. Site nav is generated from them at build time. Keep UPPERCASE names (`SEA.md`, `SOCIAL.md`).

## Expected structure

Follow the pattern used in existing guides (see [SEA.md](SEA.md)):

1. `# Title` and a short introduction
2. `## Types` or channel-specific sections describing formats and options
3. `## Benefits` when applicable
4. `## Setting Up` or equivalent practical steps
5. `## Tools and Resources` with external links where helpful

You may add sections when the channel warrants it, but keep the same tone and depth as sibling files.

## When editing

- Preserve filename casing (`SEA.md`, not `sea.md`).
- Link to related **resources** with relative paths: `../resources/BUDGETING.md`, `../resources/LEGAL.md`.
- Link to **ad-templates** when relevant: `../ad-templates/TEMPLATES.md`.
- Do not move channel files out of this directory without updating links that point here.

## When adding a new channel

1. Create `NEWCHANNEL.md` in this directory with an H1 on line 1.
2. Optional: `<!-- nav_order: 20 -->` on the next line. Omit it to sort last in the section.
3. Link to [BUDGETING.md](../resources/BUDGETING.md), [ANALYTICS.md](../resources/ANALYTICS.md), and [LEGAL.md](../resources/LEGAL.md).
4. Run the validation commands in [CONTRIBUTING.md](../../CONTRIBUTING.md).

## Parent context

[../AGENTS.md](../AGENTS.md) | [../../AGENTS.md](../../AGENTS.md)
