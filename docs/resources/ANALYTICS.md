# Analytics and Reporting

Accurate measurement is the foundation of every advertising decision. The collapse of third-party cookie-based tracking has forced a structural split in web analytics: **GA4 remains the default for Google-integrated stacks**, while a growing ecosystem of **cookieless, privacy-first alternatives** captures 40–50% more traffic data by bypassing browser-level restrictions entirely.

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

| Tool | Audience | Starting Price | Consent Banner Required | Key Differentiators |
| :---- | :---- | :---- | :---- | :---- |
| **Google Analytics 4 (GA4)** | Standard marketers, Google Ads users | Free | Yes (requires CMP) | Deep integration with Google Ads stack; event-based data model |
| **Plausible Analytics** | Minimalist site owners | From $9/month | None (cookieless) | Single-page dashboard; lightweight script (<1KB); open source option |
| **Fathom Analytics** | Marketing agencies | From $15/month | None (cookieless) | Unlimited sites; automatic EU/US server compliance routing |
| **Swetrix** | Developers and growth teams | From $19/month | None (cookieless) | Combines traffic analytics, web experiments, and uptime monitoring |
| **Matomo** | Compliance-driven brands | Free (self-hosted) | None (if CNIL-configured) | Full data ownership; GA4-depth analytics; GDPR-ready by design |
| **PostHog** | Product and engineering teams | Free (up to 1M events) | None (cookieless) | Product analytics, session replays, feature flags, and A/B testing |

> **Note:** Matomo sunsetted its free Matomo Core hosted plan in February 2026, forcing smaller users to self-host or switch to a paid tier.

Cookieless platforms typically capture **40–50% more traffic** than GA4 in heavily restricted environments (Safari, Firefox, ad-blocker users) because they don't rely on browser-stored identifiers.

---

## The Status of Google Analytics After Universal Analytics

- **Google Analytics 4 (GA4)** is the current and only Google Analytics product. UA data is no longer processed.
- GA4 uses an event-based data model (replacing session-based UA).
- GA4 requires a Consent Management Platform (CMP) to comply with GDPR's Google Consent Mode v2 requirement for European traffic. Without proper consent signals, algorithmic bidding, remarketing, and audience modeling are disabled.
- For advertisers running Google Ads, GA4 remains the recommended tool due to direct integration with Smart Bidding and conversion import.

---

## First-Party Data Strategies

As browser-side identifiers erode, small businesses must build structured first-party data collection:

1. **Server-Side Tracking:** Send conversion events directly from your server to ad platforms (Meta Conversions API, Google Tag Gateway via server-side Google Tag Manager). This bypasses browser privacy restrictions and maintains signal quality regardless of cookie or fingerprint blocking.

2. **Consent Mode v2:** Required for all EU-targeted Google Ads. Implement a certified Consent Management Platform (CMP) to pass `ad_user_data` and `ad_personalization` consent signals. Without these signals, Google's bidding algorithms lose conversion modeling capability.

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
- [Meta Business Suite Insights](https://www.facebook.com/business/insights/tools)
- [Google Tag Manager](https://tagmanager.google.com/)
