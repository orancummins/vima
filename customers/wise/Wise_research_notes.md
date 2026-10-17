# Wise — research notes behind the platform (as at 17 October 2026)

Companion to `Wise_Platform.html`. One research thread (company and Wise × Mastercard), condensed. Wise Group plc reports in US dollars under US GAAP from FY26 (year to 31 Mar 2026): FY26 results and Form 20-F (25 Jun 2026), Q1 FY27 update (17 Jul 2026), Wise's own pages, and Mastercard's and Visa's releases. ⚠ marks items that rest on secondary sources or could not be confirmed.

## 1. Wise — the company
- Wise Group plc (Jersey; HQ London), holding company since 8 May 2026; Nasdaq primary listing as WSE from 11 May 2026, secondary listing in London (listed there since Jul 2021). Founded 2011 as TransferWise. Over 8,000 staff in 11 key locations; over 1,000 engineers; about 53 subsidiaries.
- Control: Class B shares about 58% of votes (May 2026); 10-year dual-class extension approved Jul 2025 (90.58% of Class A votes) over co-founder Taavet Hinrikus's objection. CEO Kristo Käärmann; CFO Emmanuel Thomassin (since Oct 2024); CPO Nilan Peiris; CTO Harsh Sinha; Chair David Wells. Market cap ⚠ about $19bn on first-day price.
- Licences: 80+ (FCA EMI, NBB PI, US MTLs in 48 states + 4 territories, MAS MPI, AFSL; new South Africa, UAE, Thailand). OCC trust bank charter applied Jun 2025, denied Jul 2026 (AML weaknesses; $4.2m multistate penalty Jul 2025); reapplication planned under the GENIUS Act.
- FY26: net revenue $2,502.8m (+19%); income before tax $660.4m (26%); 18.9m active customers; cross-border volume $243.5bn (+31%); card spend $43.6bn (+37%); card revenue $391.6m; holdings $39.0bn; take rate 0.52%.
- Q1 FY27: 11.9m actives (11.26m personal, 608k business); volume $69.3bn (+26%); net revenue $714.0m (+25%); holdings $41.2bn; take rate 0.50%; 77% instant; Platform about 6% of volume.
- Rails: direct access in 8 markets (UK Faster Payments 2018 first non-bank; Europe, Hungary, Australia, Singapore, Philippines; Japan and Brazil in FY26); over half of transactions on direct links.
- Products: Wise Account (40 currencies), Wise Card, Business card (0.5% UK cashback), Wise Assets ($9.0bn AUC), interest (3.40% APY USD in US), Canada Chequing (Sep 2026), Mexico (Jan 2025), Chile (Jul 2026), Wise Platform (Morgan Stanley, Standard Chartered, Nubank, Mandiri, Monzo, N26, Google Pay, Bolt, Itaú, Upwork, Wealthsimple, UniCredit, Raiffeisen, MBSB, Capitec), Swift Correspondent Services (Sep 2023). AI: LLM copilots in financial crime and support; no customer AI product.

## 2. Wise × Mastercard
- First Wise card in Europe on Mastercard (2018); US Mastercard debit Jun 2019 (CFSB). 20 Aug 2020: partnership widened to issue in any market Mastercard accepts and Wise is licensed; over 1m Mastercard cards; Mastercard Send to cards in 10 European markets (Andrea Scerch, Mastercard; Kristo Käärmann).
- 27 Jan 2021: Visa global partnership, first on Visa Cloud Connect (Jack Forestell, Visa). Current UK card "wherever they accept Visa"; US card "pursuant to licensing by Visa U.S.A." (Lead Bank, CFSB). Cards switch to Visa at renewal ⚠ (French comparison site, Feb 2024; no Wise announcement). Wise Visa FIFA World Cup 26 card (Jun 2026). Visa Direct push-to-card ⚠ about 2019.
- No Mastercard–Wise announcement found since Aug 2020. Business card and Platform card networks not stated ⚠. A $20m guarantee to an unnamed "card scheme provider" ⚠.

## 3. Where Mastercard could land
- Win back personal issuing at renewal; commercial cards and spend controls for 850k Wise Business customers; card issuing for Platform banks; identity, fraud and AML tools after the OCC denial; cashback and offers; Move endpoints where Wise has no direct link.

## 4. How the page reads Wise
- Five discs: L1 Foundation (scale, licences and charter, listing and control, technology, float, strategy) · L2 Rails (transfers, direct access, Wise Card, business cards, receive, push to card) · L3 Services (financial crime and KYC, AI, Platform API, Correspondent Services, interest and Assets, business tools) · L4 Business lines (Wise Account, Wise Business, Wise Platform, enterprises) · L5 Access (app, partner channels, offices). Six kinds of user.
- The lens's per-area entries are read from the inventory (`customers/lens_tiles.py`).
- Gaps: Visa/Mastercard split of cards in circulation; date of the switch to Visa; business and Platform card networks; market cap and ratings.
