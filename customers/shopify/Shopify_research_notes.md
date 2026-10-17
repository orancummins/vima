# Shopify — research notes behind the platform (as at 17 October 2026)

Companion to `Shopify_Platform.html`. One research thread (company and Shopify × Mastercard), condensed. Figures are Shopify's own (Q2 2026 results, 5 Aug 2026; Q1 2026 results, 5 May 2026; FY2025 10-K, Feb 2026) unless marked, with the help centre, Editions pages (Winter '26, Spring '26) and partners' releases for products. Shopify's IR PDFs (investor presentation, 10-Q, annual report) and OpenAI's and Affirm's pages blocked fetching, so Q2 2026 operating metrics come from a call summary ⚠. ⚠ marks items that rest on prior knowledge or secondary sources. Q3 2026 results are due on 3 November 2026.

## 1. The company
- Shopify Inc., Ottawa; Nasdaq: SHOP (also TSX ⚠). Founded 2006 ⚠; IPO 2015. Market value ≈$218bn (Oct 2026); ≈7,600 staff (end 2025). Tobi Lütke holds 40.09% of votes through Class B shares and the Founder Share.
- FY2025: GMV $378.4bn (+29%); revenue $11,556m (+30%): subscription $2,752m, merchant $8,804m; operating income $1,468m; MRR $205m; Shopify Payments processed $248.1bn, 65.6% of GMV; transaction and loan losses $417m (+84%). Merchants: US 44%, EMEA 31%, APAC 16%, Canada 5%, LatAm 5%.
- Q2 2026: GMV $115.6bn (+32%); revenue $3,583m (+34%); operating income $488m; FCF $654m (18%); MRR $221m; loans and MCAs $2,184m. Call summary ⚠: payments penetration 68%, Shop Pay GMV +53%, international +37%, offline +32%, B2B +76%.
- Leadership: Tobi Lütke (CEO), Harley Finkelstein (President), Jeff Hoffmeister (CFO). COO (Jessica Hertz) and CTO (Mikhail Parakhin) not confirmed ⚠.
- Payments stack: Shopify Payments in 41 countries, processed by Stripe and PayPal; Shop Pay (250m+ shoppers); Shop Pay Installments (Affirm, US/Canada/UK); Klarna and local methods; USDC on Base (Coinbase, Stripe, Jun 2025); POS with Tap to Pay; Shopify Capital in nine countries; Shopify Balance (Stripe, Fifth Third Bank) and two Visa cards from Celtic Bank.
- AI: Sidekick; Shopify Catalog; Agentic Storefronts (ChatGPT, Copilot, Perplexity, Google); UCP with Google (12 Jan 2026); checkout in Copilot with Shop Pay; approvals for personal agents through Shop. ChatGPT Instant Checkout announced Sep 2025, but fewer than 30 Shopify stores live in-chat by mid-2026 ⚠.

## 2. Shopify × Mastercard
- Acceptance: Shopify Payments, Shop Pay and POS take Visa, Mastercard, Amex and others. Shopify does not publish a network split.
- Shopify's own cards: Shopify Balance Visa Commercial card and Shopify Credit, both issued by Celtic Bank under a Visa licence. Whether the Balance card was ever on Mastercard is not verified ⚠.
- Joint work: Digital Doors (8 Jul 2020, with BigCommerce and Hello Alice; Jess Turner quoted); Mastercard endorses UCP (Jan 2026) but is not a named payment handler.
- Visa: Shopify among early partners of Visa's Trusted Agent Protocol (14 Oct 2025).
- Off-network: Affirm, Klarna, USDC, ACH, local schemes (Cartes Bancaires on POS in France, iDEAL, Blik and others).
- No Shopify announcement found on Agent Pay, network tokens, Click to Pay (after 2020) or commercial cards with Mastercard. PayPal, one of Shopify's two processors, plans to integrate Agent Pay.

## 3. Where Mastercard could land
- Agent Pay and agentic tokens behind Shop Pay in UCP channels and personal-agent approvals; agent identity beside Visa's protocol; Decision Intelligence and Ethoca against card testing and rising losses; a Mastercard option for Balance and Credit ⚠ (contract terms unknown); tokens for Shop Pay on other platforms; cross-border FX; B2B virtual cards.

## 4. How the page reads Shopify
- Five discs: Foundation (scale, leadership, regulated partners, strategy) · Rails (Shopify Payments, Shop Pay, instalments, in-store, cross-border, stablecoins) · Services (fraud, agentic commerce, Catalog and checkout tools, Sidekick) · Business lines (subscriptions, merchant solutions, B2B, Capital, Balance and Credit, Collective and agentic plan) · Access (admin, Shop app, apps and partners, AI channels). Six kinds of user. Lens areas read from the inventory.
- Revenue keys are Shopify's two reported streams plus corporate; it reports no operating segments.
- Gaps: Q2 2026 KPIs from the official deck; COO and CTO; Capital's lending bank; earlier Balance card network; Interac in Canada; Q3 2026 actuals.
