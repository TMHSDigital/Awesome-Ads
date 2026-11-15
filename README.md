# Awesome Ads

[![CI](https://github.com/TMHSDigital/Awesome-Ads/actions/workflows/ci.yml/badge.svg)](https://github.com/TMHSDigital/Awesome-Ads/actions/workflows/ci.yml)
[![Deploy GitHub Pages](https://github.com/TMHSDigital/Awesome-Ads/actions/workflows/pages.yml/badge.svg)](https://github.com/TMHSDigital/Awesome-Ads/actions/workflows/pages.yml)
[![License: Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

**A practical advertising playbook for small businesses.**

Free, open guides for planning, buying, and measuring ads across digital and traditional channels. They are written for owners and marketers who run their own campaigns without an agency. Each channel guide explains how the channel works, when it is worth the money, how to set it up, and which tools to use, then links to the related guides.

**[Read the guides on the web](https://tmhsdigital.github.io/Awesome-Ads/)**, or browse the Markdown in [docs/](docs/).

This is not a click-by-click manual for each ad platform. Platform screens change too often for that. The guides cover the decisions, and point you to each platform's official help center for the buttons.

## Where to start

New to paid advertising? Read these three guides before you pick a channel:

1. [Budgeting](docs/resources/BUDGETING.md): how much to spend and how to split it when you have less than $5,000 a month.
2. [Analytics](docs/resources/ANALYTICS.md): the metrics and tracking setup that tell you whether an ad paid for itself.
3. [Legal](docs/resources/LEGAL.md): FTC endorsement and review rules, privacy laws, and CAN-SPAM, so your ads do not create a problem later.

Then match the channel to the job. Search captures demand that already exists ([search ads](docs/channels/SEA.md), [Amazon Ads](docs/channels/AMAZON.md)). Social and video create demand ([social](docs/channels/SOCIAL.md), [video](docs/channels/VIDEO.md)). Email keeps the customers you already have ([email](docs/channels/EMAIL.md)). On a small budget, run one or two campaigns per platform so each one gets enough data to learn.

## What's inside

### Channels

| Guide | What you will learn |
| --- | --- |
| [Search Engine Advertising (SEA)](docs/channels/SEA.md) | Search ad types, what search clicks and leads cost, and campaign setup. |
| [Social Media Advertising](docs/channels/SOCIAL.md) | Which platform fits which audience, ad types for each, and how to set up campaigns. |
| [Display Advertising](docs/channels/DISPLAY.md) | Display formats, targeting approaches, and how display is priced. |
| [Video Advertising](docs/channels/VIDEO.md) | Video ad types across streaming, social, and connected TV, and how to set them up. |
| [Amazon Ads](docs/channels/AMAZON.md) | Sponsored ad types, listing and search hygiene, and what Amazon ads cost in 2026. |
| [Email Marketing](docs/channels/EMAIL.md) | Email program types, consent, and the list hygiene that keeps you out of spam folders. |
| [Native Advertising](docs/channels/NATIVE.md) | Native ad formats and the disclosure rules that keep them legal. |
| [Affiliate Marketing](docs/channels/AFFILIATE.md) | Commission models, shrinking cookie windows, and affiliate compliance. |
| [Influencer Marketing](docs/channels/INFLUENCER.md) | Collaboration types, how creators price their work, where to find creators, and FTC disclosure. |
| [Print Advertising](docs/channels/PRINT.md) | Print formats and the narrow cases where print is still worth it. |
| [Broadcast Advertising](docs/channels/BROADCAST.md) | TV and radio in 2026, and connected TV as the practical entry point for small businesses. |
| [Out-of-Home (OOH) Advertising](docs/channels/OOH.md) | Billboard, transit, and programmatic digital OOH, and how a small business can buy it. |
| [Direct Mail Advertising](docs/channels/DIRECT_MAIL.md) | Direct mail formats, mailing list hygiene, and campaign setup. |
| [Event Sponsorship](docs/channels/EVENT.md) | Sponsorship types and tiers, what to ask organizers for, and how to measure ROI. |

### Planning and compliance

| Guide | What you will learn |
| --- | --- |
| [Analytics and Reporting](docs/resources/ANALYTICS.md) | Key metrics, analytics tools after Universal Analytics, and first-party data. |
| [Ad Budgeting and Planning](docs/resources/BUDGETING.md) | Sourced 2026 ad costs and how to allocate a budget under $5,000 a month. |
| [Legal and Ethical Considerations](docs/resources/LEGAL.md) | FTC rules, GDPR and app privacy changes, CAN-SPAM, and state laws. |
| [Examples of Successful Ad Campaigns](docs/resources/EXAMPLES.md) | Patterns from well-known campaigns that still work on a small-business budget. |
| [FAQ and Troubleshooting](docs/resources/FAQ.md) | Quick answers, plus fixes for low click-through rates, high costs, and other common problems. |
| [Glossary](docs/resources/GLOSSARY.md) | Plain definitions of CPC, CPM, CTV, DOOH, ROAS, and the other abbreviations the guides use. |

### Creative

| Guide | What you will learn |
| --- | --- |
| [Ad Templates and Design Resources](docs/ad-templates/TEMPLATES.md) | Template types, design tools, and design tips for producing ads without a full creative team. |

## Help improve the guides

Ad costs, platform rules, and privacy laws change every year, so the most useful contribution is a correction. If a number is out of date, a claim is wrong, or a topic is missing, [open a content issue](https://github.com/TMHSDigital/Awesome-Ads/issues/new/choose) and say where it appears.

To edit a guide or add one, read [CONTRIBUTING.md](CONTRIBUTING.md) and the [Community Guidelines](docs/meta/COMMUNITY_GUIDELINES.md). A new guide is one Markdown file with an H1 in the right folder under `docs/`. The site navigation and indexes are generated from those folders when the site builds. Add the guide to the tables above too; a test checks that every guide is listed here.

Automated agents should read [AGENTS.md](AGENTS.md) before editing.

## Preview the site locally

The site is built with [Zensical](https://zensical.org/) and deployed to GitHub Pages on every push to `main`.

```bash
pip install -r requirements-docs.txt
python scripts/prepare-mkdocs.py
zensical serve -f mkdocs.gen.yml
```

## License

Apache License 2.0. See [LICENSE](LICENSE).
