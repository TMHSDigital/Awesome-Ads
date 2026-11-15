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

Meta has established **Advantage+** as its default ad operations engine. All campaign types now run through this autonomous framework.

- **Advantage+ Sales Campaigns (ASC):** Formerly "Advantage+ Shopping Campaigns," now expanded to support lead generation and app installs alongside e-commerce catalogs. Budget allocation shifts dynamically between ad sets to maximize conversion probability in real time.
- **Photo/Video Ads:** Single images or videos in feed.
- **Carousel Ads:** Multiple images or videos in a swipeable format.
- **Stories Ads:** Full-screen vertical ads.
- **Reels Ads:** Short-form vertical video placements.
- **Collection Ads:** Showcase products directly in the ad.
- **Threads Ads:** Available globally via Meta Ads Manager as a native feed placement. Requires text-heavy, conversational copy; repurposed Instagram Reels generally underperform.

#### Advantage+ Best Practices

- Maintain at least **15 active creative combinations** per campaign to prevent creative fatigue.
- Set existing customer budget caps at **20–30%** to prevent over-allocation to prior buyers.
- Upload brand kits (logos, fonts, hex colors) to keep AI-generated creative variations on-brand.
- Use Meta's **Image-to-Video** tool to convert static product photos into animated video assets.
- Deploy **Meta Conversions API (CAPI)** for server-side signal collection — critical as browser-based pixel accuracy degrades with iOS privacy changes and ad blockers.

### 2. TikTok Ads

TikTok has expanded its ad suite to capture high-impact visual real estate and intent-driven search traffic.

- **In-Feed Ads:** Appear natively in the For You feed.
- **Spark Ads:** Boost organic creator or brand posts, preserving social proof. Because they run from a real account, they keep the post's likes and comments.
- **TopReach:** Combined app-open and top-feed placement for maximum one-day reach.
- **Prime Time:** Sequential storytelling format delivering up to three ads from one advertiser to the same user within a 15-minute window.
- **TikTok Search Ads:** Sponsored videos at the top of search results, capturing younger demographics who use TikTok as their primary search engine.
- **Branded Hashtag Challenges:** Encourage user-generated participation.
- **TopView Ads:** Full-screen takeover on app open.
- **Branded Effects:** Custom AR filters and effects.

#### Budget minimums
Daily budgets must exceed **$50 per campaign** and **$20 per ad group** ([TikTok Ads Manager Help Center](https://ads.tiktok.com/help/article/budget?lang=en), checked Nov 2026).

### 3. LinkedIn Ads

LinkedIn has pivoted to an **account-influence model** targeting entire buying groups within high-value companies — not just individual contacts.

- **Sponsored Content:** Promoted posts in the feed.
- **Document Ads:** Gated PDFs read natively in-feed. Useful for B2B lead generation because readers never leave LinkedIn.
- **Thought Leader Ads:** Promote posts from individual employees' personal profiles. They often feel more personal than ads from a company page.
- **Sponsored InMail / Message Ads:** Direct messages to targeted inboxes.
- **Dynamic Ads:** Personalized based on user profiles.
- **LinkedIn Accelerate:** AI-driven mode that automates audience curation, bidding, and creative assembly.

### 4. Pinterest Ads

Pinterest operates as a **hybrid social and visual search** platform.

- **Promoted Pins:** Boost standard pin visibility.
- **Idea Ads:** Now support direct outbound links, paid influencer placements, and "Shop the Look" product tags.
- **Try On Product Pins:** AR-powered virtual product testing for beauty and home decor (`.USDZ` for iOS, `.GLB` for Android).
- **Promoted Carousels:** Multiple images in a swipeable format.
- **Promoted Video Pins:** Video content in feed.
- **Promoted App Pins:** Drive directly to app store installs.

### 5. X (formerly Twitter) Ads

X rebuilt its ad delivery system in partnership with xAI and AWS, using real-time semantic processing to align creatives with active trends and discussions rather than static user profiles.

- **Promoted Tweets / Posts:** Boost individual posts into targeted feeds.
- **Promoted Accounts:** Grow follower counts.
- **Promoted Trends:** Feature in trending topics.

> **Note:** X updated its adult content policy in 2026, requiring age verification and enforcing moderate brand-safety adjacency controls by default. Advertisers should review brand safety settings before launching campaigns.

### 6. Reddit Ads

Reddit has become a place where people research purchases before they buy, and advertisers have followed: its ad revenue grew 74% to $2.1 billion in 2025 ([Reddit full-year 2025 results](https://www.businesswire.com/news/home/20260205441801/en/Reddit-Reports-Fourth-Quarter-and-Full-Year-2025-Results-Announces-%241-Billion-Share-Repurchase-Program), Feb 2026).

- **Promoted Posts:** Native ads appearing in subreddit feeds.
- **Collection Ads:** Lifestyle imagery paired with interactive, shoppable product tiles.
- **Conversation Overlay Ads:** Allow brands to feature community validation tags (e.g., "Redditors' Top Pick") directly on ad creatives.

### 7. Bluesky

Bluesky surpassed 41 million users in 2025 but **does not support paid advertising**. Built on the open AT Protocol with a chronological feed, the platform rewards organic brand building and authentic community engagement. Suitable for earned presence only.

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
