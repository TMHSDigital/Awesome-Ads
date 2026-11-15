# Legal and Ethical Considerations
<!-- nav_order: 30 -->

Advertising compliance has become more complex and higher-stakes: FTC enforcement covers endorsements and reviews, browsers block more tracking, and state consumer protection laws keep expanding. This guide covers the main requirements as of 2026. It is an overview, not legal advice.

---

## FTC Guidelines and Enforcement

### Truth in Advertising

- Ads must be truthful, non-deceptive, and substantiated with evidence.
- Unsubstantiated claims, particularly in health, finance, and performance categories, are a primary enforcement target.

### Endorsement and Influencer Disclosure Rules

Civil penalties for violating FTC rules can reach [$53,088 per violation](https://www.federalregister.gov/documents/2025/01/17/2025-01361/adjustments-to-civil-penalty-amounts) (the 2025 inflation-adjusted maximum, which the FTC kept for 2026).

What the FTC's [Disclosures 101 for Social Media Influencers](https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers) asks for:

- **Hard to miss:** Put the disclosure with the endorsement itself, not only on a profile page, at the end of a post, or behind a "more" link.
- **Plain words:** Terms like "ad", "advertisement", "sponsored", `#ad`, or `#sponsored` work, and so does a plain statement such as "Thanks to [Brand] for the free product". Avoid vague or shorthand tags such as `#sp`, `#spon`, or `#collab`, and stand-alone words like "thanks" or "ambassador".
- **In the video, not just the description:** For a video endorsement, the disclosure belongs in the video itself. Viewers are more likely to notice it when it is both spoken and shown on screen. In a livestream, repeat it periodically.
- **Platform tools are not enough on their own:** Do not assume a platform's built-in label (such as Instagram's "Paid partnership") is good enough. Use it in addition to the creator's own clear disclosure.

**Written disclosure policy:** Give every creator a short written disclosure policy before the campaign starts, and check their posts. It gives you a record that you took disclosure seriously.

### Native Advertising
The FTC Native Advertising Guidelines require that sponsored editorial and advertorial placements cannot mislead consumers by mimicking organic editorial formats. Sponsored articles, in-feed placements, and recommendation widget content must be conspicuously labeled with "Sponsored" or "Advertisement."

### FTC Consumer Review Rule
The FTC's [final rule on fake reviews and testimonials](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials), in effect since October 2024, lets it seek civil penalties for:

- Fake reviews and testimonials, including buying or selling them.
- Paying or rewarding customers for reviews that must be positive (or negative).
- Reviews by company insiders that do not disclose the connection.
- Suppressing negative reviews through threats, intimidation, or false accusations.
- Buying or selling fake followers or views.

[FTC Advertising Guidelines](https://www.ftc.gov/business-guidance/advertising-marketing)

---

## GDPR and International Data Privacy

### EU — GDPR

- **Data Protection:** Safeguard all personal data collected via ads or web analytics.
- **Consent and a lawful basis:** You need a lawful basis for any personal data you process, and EU rules require consent before setting advertising cookies or similar trackers.
- **Google consent mode:** Advertisers using Google Ads or GA4 with visitors in the EEA, the UK, or Switzerland should pass consent signals through Google's [consent mode](https://support.google.com/google-ads/answer/10000067), including `ad_user_data` and `ad_personalization`. Without them, remarketing, personalized ads, and conversion measurement for those visitors are limited. A consent management platform (CMP) that supports consent mode is the simplest way to do this.
- **Data breach notification:** Report a personal data breach to the supervisory authority within 72 hours of becoming aware of it, and tell the affected people directly when the breach is likely to put them at high risk.

[GDPR Overview](https://gdpr.eu/)

### Third-Party Cookie Status

- Chrome still allows third-party cookies by default. In 2025 Google dropped its plan to phase them out and retired most of its Privacy Sandbox replacement technologies. Safari and Firefox continue to block cross-site tracking by default.
- A significant share of web traffic is already effectively cookieless. Campaigns relying on cookie-based behavioral retargeting will see reduced scale.
- **Mitigation:** First-party data strategies, server-side tracking, and contextual targeting. See [Analytics and Reporting](ANALYTICS.md).

---

## iOS and Android Privacy Protections

### Apple (iOS / Safari 26)

- **Advanced Fingerprinting Protection:** Since Safari 26 it is on by default for all browsing, not only Private Browsing. It obscures the browser and device details that fingerprinting scripts use to recognize a visitor.
- **Link Tracking Protection:** On by default in Private Browsing, Mail, and Messages. Tests report that it strips click IDs such as `gclid`, `fbclid`, and `msclkid` from links (Apple does not publish the list). **Standard UTM parameters (`utm_source`, `utm_medium`, `utm_campaign`) are kept.**
- **Impact:** Advertisers lose click-level attribution for a portion of iOS traffic. Server-side conversion APIs (Meta CAPI, Google Tag Gateway) are the mitigation.

### Android

- In October 2025 Google retired the Privacy Sandbox technologies it had been building for Android, along with those for Chrome.
- **Advertising ID:** If a user deletes their advertising ID, or an app does not declare the `com.google.android.gms.permission.AD_ID` permission, the app receives a string of zeros instead of the ID, so the user cannot be targeted or measured with it.

---

## CAN-SPAM Act (Email Advertising)

- **Accurate sender information:** `From` lines and subject lines must be truthful.
- **Opt-out mechanism:** Every commercial email must include a functioning unsubscribe link that processes requests within 10 business days.
- **Physical address:** Commercial emails must include your current physical postal address.

[CAN-SPAM Compliance Guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business)

---

## State-Level Laws

### California Automatic Renewal Law (ARL)
Amendments that took effect on July 1, 2025 require:

- Explicit **affirmative consent** for any subscription or auto-renewal signup (pre-checked boxes are insufficient).
- A simple, accessible **click-to-cancel** mechanism.
- Clear disclosure of recurring charge terms before the purchase is finalized.

This applies to any advertiser promoting subscription-based products or services to California residents.

---

## Ethical Advertising

### Transparency

- Clearly disclose all sponsored content, affiliate relationships, and paid endorsements.
- Sponsored articles and native ad placements must be labeled conspicuously.

### Privacy

- Collect only the data you need; use it only for stated purposes.
- Respect user opt-outs and deletion requests under applicable regulations.

### Fairness

- Do not use dark patterns, false urgency, or deceptive framing.
- Ads targeting vulnerable populations (children, elderly) face heightened scrutiny.

---

## Best Practices

1. **Regular compliance audits:** Review all active influencer and affiliate partnerships quarterly for disclosure compliance.
2. **Legal consultation:** For campaigns with significant influencer, native, or cross-border components, consult an advertising attorney.
3. **Stay updated:** FTC guidance and state privacy laws are actively evolving. Subscribe to FTC press releases and IAB legal updates.
4. **Accessibility:** Make ad landing pages meet WCAG 2.2 AA, the current version of the accessibility standard.

---

## Tools and Resources

- [FTC Advertising Guidelines](https://www.ftc.gov/business-guidance/advertising-marketing)
- [Disclosures 101 for Social Media Influencers](https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers)
- [GDPR.eu Overview](https://gdpr.eu/)
- [CAN-SPAM Act Compliance Guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business)
- [IAB Legal Guidelines](https://www.iab.com/guidelines/)
- [Google Consent Mode documentation](https://support.google.com/google-ads/answer/10000067)
