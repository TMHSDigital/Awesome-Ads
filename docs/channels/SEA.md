# Search Engine Advertising (SEA)
<!-- nav_order: 10 -->

Search Engine Advertising (SEA) involves placing ads on search engine results pages (SERPs). This method allows businesses to target users actively searching for specific keywords.

## Types of SEA

### 1. Google Ads

- **Search Ads / AI Max:** Text ads on Google SERPs. Google is replacing Dynamic Search Ads (DSA) with **AI Max**, which combines broad match, keywordless matching, and AI-written text customization to reach more searches and build headlines from your landing pages. Remaining DSA campaigns are scheduled to be upgraded automatically in February 2027 ([Google Ads Developer Blog](https://developers.google.com/ads/blog/posts/2026/06/dynamic-search-ads-dsa-automigration), June 2026).
- **Display Ads:** Banner ads on the Google Display Network (GDN). Transitioning toward contextual and first-party audience targeting as third-party cookie signals weaken.
- **Shopping Ads:** Product listings on Google SERPs.
- **Performance Max (PMax):** Automated campaign type that runs across Google's surfaces (Search, Display, YouTube, Gmail, Maps, and Discover) from a single campaign.
- **Local Service Ads:** Pay-per-lead ads for local service businesses (plumbers, lawyers, cleaners, etc.).
- **Video Ads:** Ads served on YouTube (see [Video Advertising](VIDEO.md)).

#### AI Max: Key Mechanics

AI Max achieves efficiency through three coordinated layers:

1. **Search term matching:** Uses your site content, keywords, and ads to match searches beyond your keyword list.
2. **Text customization:** Writes variations of your headlines and descriptions with Google's AI.
3. **Final URL expansion:** Sends each visitor to the page on your site that Google predicts will perform best.

> **Tracking check:** Before you turn on AI Max, make sure your tracking templates build URLs from the `{lpurl}` parameter, so tracking still works when visitors land on pages other than your final URL.

### 2. Microsoft Advertising (Bing Ads)

- **Search Ads:** Text ads on Bing, Yahoo, and DuckDuckGo networks.
- **Performance Max:** Supports negative keywords and a new customer acquisition goal, so you can bid higher for, or only for, people who have not bought from you before.
- **LinkedIn Profile Targeting:** Unique to Microsoft — layer company name, industry, or job function data over high-intent keywords for precise B2B reach.
- **Import from Google Ads:** Microsoft supports importing Google PMax campaigns with NCA settings, automatically converting audience lists into equivalent rule-based remarketing assets.

## Costs

In the 2026 search benchmarks from LocaliQ and WordStream, the average cost per click across industries was $5.42 and the average cost per lead was $66.69, for Google Ads and Microsoft Ads campaigns combined. Costs vary widely by industry, so check the figure for yours. Sources and other channels are in [Ad Budgeting and Planning](../resources/BUDGETING.md#platform-cost-benchmarks).

## Benefits

- **High purchase intent:** Ads reach users actively searching for your product or service.
- **Cost control:** Flexible CPC or CPM bidding with daily budget caps.
- **Measurable results:** Detailed conversion tracking across the full customer journey.
- **AI-driven scale:** AI Max and PMax reduce manual keyword management overhead while expanding reach.

## Setting Up SEA

1. **Keyword research:** Identify core transactional terms; build a thorough negative keyword list.
2. **Campaign structure:** For budgets under $5K/month, consolidate into one or two campaigns to feed algorithmic learning thresholds.
3. **Creative assets:** Provide multiple headline and description variants; supply landing page URLs with clean `{lpurl}` tracking templates.
4. **Conversion tracking:** Install Google Tag or Ads conversion tags; consider server-side Tag Gateway for cookieless environments.
5. **Monitor and optimize:** Review search term reports weekly; add negatives to prevent wasted spend on AI-expanded irrelevant queries.

## Tools and Resources

- [Google Ads](https://ads.google.com/)
- [Microsoft Advertising](https://ads.microsoft.com/)
- [Google AI Max documentation](https://support.google.com/google-ads/answer/15910187)
- [WordStream PPC Benchmarks](https://www.wordstream.com/ppc-benchmarks)

## Related guides

- [Analytics and Reporting](../resources/ANALYTICS.md)
- [Ad Budgeting and Planning](../resources/BUDGETING.md)
- [Legal and Ethical Considerations](../resources/LEGAL.md)
