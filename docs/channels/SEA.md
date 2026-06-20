# Search Engine Advertising (SEA)

Search Engine Advertising (SEA) involves placing ads on search engine results pages (SERPs). This method allows businesses to target users actively searching for specific keywords.

## Types of SEA

### 1. Google Ads

- **Search Ads / AI Max:** Text ads on Google SERPs. Google is phasing out Dynamic Search Ads (DSA) in favor of the **AI Max** framework, which combines broad match, keywordless matching, and Gemini-powered creative customization to expand query capture and dynamically generate headlines from landing page content. Auto-migration of DSA campaigns is scheduled for February 2027.
- **Display Ads:** Banner ads on the Google Display Network (GDN). Transitioning toward contextual and first-party audience targeting as third-party cookie signals weaken.
- **Shopping Ads:** Product listings on Google SERPs.
- **Performance Max (PMax):** Automated campaign type running across all Google surfaces — Search, Display, YouTube, Gmail, Maps, and Discover — within a single campaign.
- **Local Service Ads:** Pay-per-lead ads for local service businesses (plumbers, lawyers, cleaners, etc.).
- **Video Ads:** Ads served on YouTube (see [Video Advertising](VIDEO.md)).

#### AI Max: Key Mechanics

AI Max achieves efficiency through three coordinated layers:

1. **Search term matching** — analyzes site content, historical keywords, and creative assets to capture queries beyond standard keyword lists.
2. **Asset optimization** — uses Gemini-generated text to customize headlines and descriptions per ad group contextually.
3. **Final URL Expansion** — routes users to the landing page on your domain predicted to perform best, based on real-time intent signals.

> **Tracking warning:** Tracking templates that do not use standard `{lpurl}` parameters (e.g., `{lpurl}?`, `{lpurl}&`) can conflict with Final URL Expansion, causing tracking failure or 404 redirect errors. Audit templates before opting into AI Max.

### 2. Microsoft Advertising (Bing Ads)

- **Search Ads:** Text ads on Bing, Yahoo, and DuckDuckGo networks.
- **Performance Max:** Self-serve negative keyword lists (up to 5,000 terms per campaign or account) now available, resolving the previous "black-box" targeting limitation. Supports New Customer Acquisition (NCA) settings for bidding exclusively toward net-new buyers.
- **LinkedIn Profile Targeting:** Unique to Microsoft — layer company name, industry, or job function data over high-intent keywords for precise B2B reach.
- **Import from Google Ads:** Microsoft supports importing Google PMax campaigns with NCA settings, automatically converting audience lists into equivalent rule-based remarketing assets.

## 2026 Cost Benchmarks

| Channel | Pricing Model | Avg. CPC |
| :---- | :---- | :---- |
| Google Search / AI Max | Cost-Per-Click (CPC) | ~$5.42 (cross-industry avg) |
| Google Display Network | Cost-Per-Click (CPC) | ~$0.63 |
| Microsoft / Bing Ads | Cost-Per-Click (CPC) | ~$1.54 |

> CPCs vary widely by industry. Legal, finance, and insurance verticals can exceed $15–$50 per click on Google Search.

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
