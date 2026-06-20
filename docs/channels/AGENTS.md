# Agents: Channels

This directory contains **one guide per advertising channel**. Each file is a standalone reference for small businesses evaluating or running that channel.

## Files

| File | Topic |
|------|-------|
| `SEA.md` | Search engine advertising (Google Ads, Bing Ads) |
| `SOCIAL.md` | Social media advertising |
| `DISPLAY.md` | Display and banner advertising |
| `VIDEO.md` | Video advertising |
| `EMAIL.md` | Email marketing |
| `NATIVE.md` | Native advertising |
| `AFFILIATE.md` | Affiliate marketing |
| `INFLUENCER.md` | Influencer marketing |
| `PRINT.md` | Print advertising |
| `BROADCAST.md` | Television and radio |
| `OOH.md` | Out-of-home advertising |
| `DIRECT_MAIL.md` | Direct mail |
| `EVENT.md` | Event sponsorship |

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
- Link to **templates** when relevant: `../templates/TEMPLATES.md`.
- Do not move channel files out of this directory without updating all indexes and CI.

## When adding a new channel

1. Create `NEWCHANNEL.md` in this directory.
2. Update [../README.md](../README.md), [../../README.md](../../README.md), and [../meta/REPO_OUTLINE.md](../meta/REPO_OUTLINE.md).
3. Run the internal link checker.

## Parent context

[../AGENTS.md](../AGENTS.md) | [../../AGENTS.md](../../AGENTS.md)
