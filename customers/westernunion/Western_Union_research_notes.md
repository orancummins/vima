# Western Union — research notes behind the platform (as at 17 October 2026)

Companion to `Western_Union_Platform.html`. One research thread (company and Western Union × Mastercard), condensed. Figures are Western Union's own (Q2 2026 results, 30 Jul 2026; FY2025 results and 2025 Form 10-K, 20 Feb 2026; 2026 proxy) unless marked. Q3 2026 results are due on 4 November 2026. ⚠ marks items that rest on secondary sources or could not be confirmed.

## 1. The company
- The Western Union Company (NYSE: WU), Denver. About 9,600 staff in 50+ countries; 200+ countries and territories, nearly 130 currencies; about 360,000 locations active in the last 12 months, 90% outside the US. Market cap about $1.92bn at $6.17 (16 Oct 2026) ⚠.
- Licences: almost every US state; WU Payment Services Ireland (PSD2); Western Union International Bank (Austria); FCA payment institution; Brazil bank. Consent orders; 1% US remittance excise tax from Jan 2026.
- FY2025: revenue $4,050.7m (−4%); CMT $3,507.4m (−8%), 285.9m transfers; Consumer Services $543.3m (+32%); GAAP EPS $1.52, adjusted $1.75; Iraq revenue $115.3m → $15.8m.
- Q2 2026: revenue $1,013.2m (−1%); Branded Digital 32% of CMT revenue and 43% of transactions (transactions +25%); GAAP margin 13%; adjusted EPS $0.31. 2026 outlook cut to adjusted EPS $1.25–1.35 (from $1.75–1.85).
- Leadership: Devin McGranahan (CEO), Matt Cagwin (CFO), Benjamin Hawksworth (COO), Giovanni Angelini (President EMEA), Benjamin Adams (CLO, retiring 2 Nov 2026), Malcolm Clarke (Head of Digital Assets); chair Jeffrey Joerres.
- Strategy: "Beyond" (Nov 2025): $4.8–5.3bn revenue and adjusted EPS $2.15–2.45 by 2028; digital-first two-sided network; stablecoins.
- Deals: Business Solutions sold ($910m; completed Jul 2023); stc bank stake (2021); Eurochange (Apr 2025, 230+ UK stores); Intermex agreed 10 Aug 2025 ($16/share, ~$500m, ~6m customers).
- **Intermex is not closed:** NYDFS approved (Aug 2026), California DFPI suspended its approval (13 Aug 2026), HSR refiled 2 Oct 2026; outside date 10 Nov 2026 ⚠.
- Digital assets: USDPT (Solana; issued by Anchorage Digital Bank) announced Oct 2025, live 4 May 2026 for treasury and 24/7 agent settlement (Philippines and Bolivia first ⚠; Fireblocks ⚠); Digital Asset Network; Bybit first major exchange (Jun 2026); Stablecard with Rain on **Visa**, 37 markets (Aug 2026), 60+ targeted.
- Cards and wallets: Western Union Prepaid Visa (Pathward); Western Union Netspend Prepaid Mastercard; Vigo Money (US wallet, network not published ⚠); wallets in Brazil, Argentina, Singapore, Philippines, Israel ⚠; European Digital Banking with a Visa debit card, closed ⚠ date.

## 2. Western Union × Mastercard
- 2011 global agreement (prepaid, money transfer) ⚠; 2013 SME international payments ⚠.
- Nov 2021: Mastercard Send integrated (US redirect to any debit card; 16 European send markets to Mastercard debit cards) and Cross-Border Services payouts via Business Solutions (Gabriella Fitzgerald, WU; Leigh Amaro, Mastercard). That payout leg left with the 2023 sale.
- Netspend Prepaid Mastercard (US); Mastercard cards fund digital sends.
- Visa: Visa Direct (Jun 2019; US extension Aug 2022), Prepaid Visa, European debit card, Stablecard (Aug 2026).
- Not found: Mastercard Move, tokenisation programme, Click to Pay, fraud tools, crypto or stablecoin cards, offers. MoneyGram took Mastercard Move in Apr 2025 ⚠.

## 3. Where Mastercard could land
- Move to wallets and more corridors; stablecoin cards where Stablecard is not; cards for Vigo Money and other wallets; card, push-to-card and fraud services for Intermex; scam scoring; card-linked offers for Rewards.

## 4. How the page reads Western Union
- Five discs: L1 Foundation (results, licences and regulation, leadership, Beyond, deals) · L2 Rails (retail, digital, pay to card, account and wallet payout, USDPT, cards and wallets) · L3 Services (compliance, identity, treasury, rewards and media, partner platform) · L4 Business lines (money transfer, bill pay, travel money, money orders and insurance, digital assets) · L5 Access (retail network, app and web, partners). Six kinds of user.
- The lens's per-area entries are read from the inventory (`customers/lens_tiles.py`).
- Gaps: network split; total customers; Vigo Money card network; Digital Banking closure date; credit ratings; Intermex close.
