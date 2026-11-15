# Analytics and Reporting
<!-- nav_order: 10 -->

Accurate measurement is the foundation of every advertising decision. Third-party cookie tracking keeps weakening (Safari and Firefox block it by default, and many users block it themselves), which has split web analytics in two: **GA4 remains the default for Google-integrated stacks**, while a growing set of **cookieless, privacy-first alternatives** counts visitors without relying on browser cookies.

---

## Key Metrics

- **Click-Through Rate (CTR):** Percentage of ad impressions that resulted in a click.
- **Conversion Rate:** Percentage of visitors who completed a desired action (purchase, lead form, call).
- **Cost Per Acquisition (CPA):** Total ad spend divided by conversions.
- **Return on Ad Spend (ROAS):** Revenue generated per dollar spent on ads.
- **Cost Per Lead (CPL):** Total spend divided by leads generated.
- **View-Through Rate (VTR):** Percentage of video ad viewers who watched to completion.

---

## Web Analytics Tools (2026)

Universal Analytics was sunsetted in 2023. GA4 is the current Google standard, but significant adoption of cookieless alternatives has occurred as privacy restrictions erode cookie-based accuracy.

| Tool | Audience | Pricing | Consent Banner Required | Key Differentiators |
| :---- | :---- | :---- | :---- | :---- |
| **Google Analytics 4 (GA4)** | Standard marketers, Google Ads users | Free | Yes (requires CMP) | Deep integration with Google Ads stack; event-based data model |
| **Plausible Analytics** | Minimalist site owners | Paid plans; self-hosted version available | None (cookieless) | Single-page dashboard; lightweight script (<1KB); open source option |
| **Fathom Analytics** | Marketing agencies | Paid plans | None (cookieless) | Unlimited sites; automatic EU/US server compliance routing |
| **Swetrix** | Developers and growth teams | Paid plans | None (cookieless) | Combines traffic analytics, web experiments, and uptime monitoring |
| **Matomo** | Compliance-driven brands | Free (self-hosted) | None (if CNIL-configured) | Full data ownership; GA4-depth analytics; GDPR-ready by design |
| **PostHog** | Product and engineering teams | Free tier, then usage-based | None (cookieless) | Product analytics, session replays, feature flags, and A/B testing |

Cookieless platforms often record visits that GA4 misses in browsers and setups that block cookies or trackers, such as Safari, Firefox, and ad blockers, because they do not rely on browser-stored identifiers. Check each vendor's pricing page for current plans.

---

## The Status of Google Analytics After Universal Analytics

- **Google Analytics 4 (GA4)** is the current and only Google Analytics product. UA data is no longer processed.
- GA4 uses an event-based data model (replacing session-based UA).
- For visitors in the EEA, the UK, and Switzerland, GA4 and Google Ads need consent signals from Google's consent mode, usually sent by a consent management platform (CMP). Without them, remarketing, personalized ads, and conversion measurement for those visitors are limited. See [Legal and Ethical Considerations](LEGAL.md).
- For advertisers running Google Ads, GA4 remains the recommended tool due to direct integration with Smart Bidding and conversion import.

---

## First-Party Data Strategies

As browser-side identifiers erode, small businesses must build structured first-party data collection:

1. **Server-Side Tracking:** Send conversion events directly from your server to ad platforms (Meta Conversions API, Google Tag Gateway via server-side Google Tag Manager). It is less affected by browser blocking than a browser pixel, but it still needs the visitor's consent where the law requires it.

2. **Consent mode:** If you advertise to visitors in the EEA, the UK, or Switzerland, pass the `ad_user_data` and `ad_personalization` consent signals through Google's consent mode, usually with a consent management platform (CMP). Without them, conversion measurement and modeling for those visitors are limited.

3. **First-Party Gated Content:** Exchange premium content (downloadable guides, video walkthroughs, calculators) for direct user email/consent. Builds an owned audience independent of platform algorithms.

4. **UTM-to-CRM Syncing:** Force UTM parameters (source, medium, campaign) directly into CRM contact fields at the time of form submission. This preserves attribution for leads through long sales cycles where last-click models break.

5. **Customer List Uploads:** Regularly export and upload customer email lists to Google, Meta, and LinkedIn for audience matching. Complements behavioral targeting with first-party identity signals.

---

## Campaign-Level Analytics by Platform

| Platform | Native Analytics Tool |
| :---- | :---- |
| Google Ads | Google Ads Reporting + GA4 |
| Meta (Facebook/Instagram) | Meta Ads Manager + Meta Business Suite |
| TikTok | TikTok Ads Manager |
| LinkedIn | LinkedIn Campaign Manager |
| Pinterest | Pinterest Analytics |
| X / Twitter | X Ads Manager |

---

## Best Practices

- **Regular monitoring:** Review campaign performance at least weekly; check for budget pacing issues and anomalous CTR drops.
- **A/B testing:** Test one variable at a time — headline, image, CTA, audience. Ensure statistical significance before making decisions.
- **Attribution hygiene:** Understand each platform's attribution window (e.g., Meta defaults to 7-day click / 1-day view). Compare cross-platform reports to avoid double-counting conversions.
- **Incrementality testing:** For channels without clear conversion paths (CTV, OOH, display), run holdout tests to measure true lift.

---

## Tools and Resources

- [Google Analytics 4](https://analytics.google.com/)
- [Plausible Analytics](https://plausible.io/)
- [Fathom Analytics](https://usefathom.com/)
- [Matomo](https://matomo.org/)
- [PostHog](https://posthog.com/)
- [Meta Business Help](https://www.facebook.com/business/help)
- [Google Tag Manager](https://tagmanager.google.com/)
