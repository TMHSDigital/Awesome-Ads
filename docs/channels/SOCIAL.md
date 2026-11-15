# Social Media Advertising
<!-- nav_order: 20 -->

Social media advertising leverages various platforms to target specific audiences with tailored ads. The landscape has shifted from detailed interest-based targeting to autonomous AI optimization driven by conversion signals.

Terms such as CTR, CPM, CPC, and CAPI are defined in the [Glossary](../resources/GLOSSARY.md).

## Which Platform Fits

| Platform | Best fit |
| :---- | :---- |
| **Facebook** | Broad demographics, DTC catalogs |
| **Instagram** | Visual and lifestyle brands, DTC |
| **TikTok** | Under-35 consumers, vertical video |
| **LinkedIn** | B2B decision-makers, buying groups |
| **Pinterest** | Home, fashion, food, visual categories |
| **X / Twitter** | Real-time, tech, SaaS, events |
| **Threads** | Younger, text-driven conversational users |

Sourced cost figures for Facebook and TikTok's minimum budgets are in [Ad Budgeting and Planning](../resources/BUDGETING.md#platform-cost-benchmarks). We do not publish costs for the other platforms because no current primary source exists; use each platform's own estimates when you plan.

---

## Platforms and Ad Types

### 1. Meta Ads (Facebook and Instagram)

Meta now sets up most campaigns with **Advantage+** automation by default, which handles audience, placement, and budget decisions.

- **Advantage+ Sales Campaigns:** Formerly "Advantage+ Shopping Campaigns." Meta moves budget automatically toward the audiences and placements that produce sales.
- **Photo/Video Ads:** Single images or videos in feed.
- **Carousel Ads:** Multiple images or videos in a swipeable format.
- **Stories Ads:** Full-screen vertical ads.
- **Reels Ads:** Short-form vertical video placements.
- **Collection Ads:** Showcase products directly in the ad.
- **Threads Ads:** Available globally via Meta Ads Manager as a native feed placement. Requires text-heavy, conversational copy; repurposed Instagram Reels generally underperform.

#### Advantage+ Best Practices

- Give each campaign several images, videos, and text variations so the system can rotate them and avoid creative fatigue.
- Set existing customer budget caps at **20–30%** to prevent over-allocation to prior buyers.
- Upload brand kits (logos, fonts, hex colors) to keep AI-generated creative variations on-brand.
- Use Meta's **Image-to-Video** tool to convert static product photos into animated video assets.
- Deploy **Meta Conversions API (CAPI)** for server-side signal collection — critical as browser-based pixel accuracy degrades with iOS privacy changes and ad blockers.

### 2. TikTok Ads

TikTok has expanded its ad suite to capture high-impact visual real estate and intent-driven search traffic.

- **In-Feed Ads:** Appear natively in the For You feed.
- **Spark Ads:** Boost organic creator or brand posts, preserving social proof. Because they run from a real account, they keep the post's likes and comments.
- **TopReach:** One buy that combines TopView (the first ad on app open) and TopFeed (the first in-feed ad) for maximum one-day reach.
- **Prime Time:** A sequence of up to three ads from one advertiser shown to the same person within 15 minutes, for live events and big moments ([TikTok Newsroom](https://newsroom.tiktok.com/newfronts-26-tiktok-unveils-new-high-impact-ad-solutions?lang=en), March 2026). TopReach and Prime Time are premium buys aimed at larger budgets.
- **TikTok Search Ads:** Sponsored videos in TikTok's search results, for people who search for products inside the app.
- **Branded Hashtag Challenges:** Encourage user-generated participation.
- **TopView Ads:** Full-screen takeover on app open.
- **Branded Effects:** Custom AR filters and effects.

#### Budget minimums
Daily budgets must exceed **$50 per campaign** and **$20 per ad group** ([TikTok Ads Manager Help Center](https://ads.tiktok.com/help/article/budget?lang=en), checked Nov 2026).

### 3. LinkedIn Ads

LinkedIn's ad tools increasingly target **buying groups**, the several people inside one company who decide on a purchase, not just individual contacts.

- **Sponsored Content:** Promoted posts in the feed.
- **Document Ads:** Gated PDFs read natively in-feed. Useful for B2B lead generation because readers never leave LinkedIn.
- **Thought Leader Ads:** Promote posts from individual employees' personal profiles. They often feel more personal than ads from a company page.
- **Sponsored InMail / Message Ads:** Direct messages to targeted inboxes.
- **Dynamic Ads:** Personalized based on user profiles.
- **LinkedIn Accelerate:** AI-driven mode that automates audience curation, bidding, and creative assembly.

### 4. Pinterest Ads

Pinterest operates as a **hybrid social and visual search** platform.

- **Promoted Pins:** Boost standard pin visibility.
- **Try On Product Pins:** Augmented reality try-on for selected beauty and home decor products.
- **Promoted Carousels:** Multiple images in a swipeable format.
- **Promoted Video Pins:** Video content in feed.
- **Promoted App Pins:** Drive directly to app store installs.

### 5. X (formerly Twitter) Ads

- **Promoted Tweets / Posts:** Boost individual posts into targeted feeds.
- **Promoted Accounts:** Grow follower counts.
- **Promoted Trends:** Feature in trending topics.

> **Note:** X allows a wider range of content than most ad platforms. Review its brand safety and adjacency controls before you launch.

### 6. Reddit Ads

Reddit has become a place where people research purchases before they buy, and advertisers have followed: its ad revenue grew 74% to $2.1 billion in 2025 ([Reddit full-year 2025 results](https://www.businesswire.com/news/home/20260205441801/en/Reddit-Reports-Fourth-Quarter-and-Full-Year-2025-Results-Announces-%241-Billion-Share-Repurchase-Program), Feb 2026).

- **Promoted Posts:** Native ads appearing in subreddit feeds.
- **Collection Ads:** Lifestyle imagery paired with interactive, shoppable product tiles.
- **Conversation Summary Add-ons:** Show positive Reddit comments about your product beneath the ad. Announced in June 2025 and first tested with selected advertisers, so check whether your account has it.

### 7. Bluesky

Bluesky grew quickly in 2024 and 2025 but **does not sell advertising**. It is built on the open AT Protocol, and people choose which feeds they follow, so brands can only build a presence there organically.

---

## Setting Up Social Media Ads

1. **Select platform(s):** Match platform demographics to your audience and product type.
2. **Consolidate campaigns:** For budgets under $5K/month, run a maximum of one or two campaigns per platform to avoid starving the algorithm's learning phase.
3. **Create compelling content:** Maintain 15+ creative combinations; prioritize native-feeling video (especially vertical formats for TikTok, Reels, Stories).
4. **Define target audience:** Use platform-specific targeting; on Meta, let Advantage+ expand audiences — overly narrow targeting degrades performance.
5. **Server-side tracking:** Implement CAPI (Meta) or equivalent to maintain conversion signal quality under cookie and fingerprinting restrictions.
6. **Monitor and optimize:** Review performance weekly; refresh creatives regularly to combat fatigue.

---

## Tools and Resources

- [Meta Ads Manager](https://www.facebook.com/business/ads)
- [TikTok Ads](https://www.tiktok.com/business/en-US/ads)
- [LinkedIn Campaign Manager](https://business.linkedin.com/advertise/ads)
- [Pinterest Ads](https://business.pinterest.com/advertise/)
- [X Ads](https://ads.x.com/)
- [Reddit Ads](https://www.reddit.com/advertising/)

## Related guides

- [Analytics and Reporting](../resources/ANALYTICS.md)
- [Ad Budgeting and Planning](../resources/BUDGETING.md)
- [Legal and Ethical Considerations](../resources/LEGAL.md)
