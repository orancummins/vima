# Marqeta — research notes behind the platform (as at 17 October 2026)

Companion to `Marqeta_Platform.html`. One research thread (company and Marqeta × Mastercard), condensed. Figures are Marqeta's own: Q2 2026 results (4 Aug 2026), Q1 and Q2 2026 earnings calls, FY2025 results (24 Feb 2026) and the 2025 10-K, plus product pages and trade press. ⚠ marks items that rest on secondary sources or could not be confirmed.

## 1. Marqeta — the company
- Marqeta, Inc. (Oakland, California); Nasdaq MQ since June 2021; about $1.95bn market value in October 2026 ⚠ third-party quote; one-for-four reverse split 30 Jun 2026; 938 staff (end-2025). Founded by Jason Gardner (2009–10); open APIs and JIT Funding in 2014.
- Leadership: CEO Mike Milotich (interim from 26 Feb 2025 after Simon Khalaf left; permanent Sep 2025); CFO Patti Kangwankij ⚠ start date; CPO Eugenia Gibbons (from 31 Aug 2026); CRO Todd Pollak; CTO Lukasz Strozek; CSO Anthony Peculic; chair Jud Linville.
- Scale: TPV $382.5bn in 2025 (+31%), $120.4bn in Q2 2026 (+32%); net revenue $624.9m (2025, +23%), $176.0m (Q2 2026, +17%); GAAP profit in Q1 and Q2 2026 ($8m, $7.6m); adjusted EBITDA $37.4m in Q2; take rate about 10bp; international 20% of TPV. 2026 guide: revenue +12–13%.
- Banks and licences: not a bank; Sutton Bank settles 64% of TPV (contract to 2029); TransactPay e-money licence and BIN sponsorship in UK, Gibraltar and the EEA (bought July 2025; price not disclosed ⚠); Canadian PSP registration.
- Concentration: Block 68% of revenue (2023), 45% (2025), 41% (Q2 2026). Block began cutting new Cash App issuance on Marqeta in mid-June 2026; little or none expected by year-end; contract to June 2028.
- Products: issuer processing, JIT Funding, virtual cards, debit/prepaid, credit (Power Finance, 2023; three new programmes coming), flexible credentials (Visa first; Mastercard One Credential), Marqeta Hub, accounts and ACH/RTP/FedNow/push-to-card (Sep 2026), FPS and SEPA, stablecoin cards (zerohash, BVNK, Coinbase), Real-Time Decisioning with an AI score (Mar 2026) and Adyen/Riskified/Signifyd data, KYC/3DS/disputes, tokens, Google Wallet for kids (Aug 2026), programme management, rewards, MCP server, UX Toolkit.
- Customers: Block, Klarna, Affirm, Afterpay, Ramp, Expensify, Bill, DoorDash, Instacart, Uber, Google, Coinbase, Western Union.

## 2. Marqeta × Mastercard
- Network agreements: Visa 2017 (extended Feb 2023 for five years); Mastercard strategic relationship and minority investment, 8 Oct 2020 (Sherri Haymond, Jason Gardner), term to 2028 or a volume milestone; PULSE 2013 to 2031.
- Mastercard: work since 2014; Fintech Express in Europe (Mar 2021); Network Enablement Partner in APAC (2 Jun 2022; Melissa Keir, Ben Gilbey); Square Debit Card on Mastercard; One Credential early adopter (Q1 2026) and secured credit-builder with BNPL (Q2 2026); BVNK stablecoin cards accepted wherever Mastercard is (9 Sep 2026; Anthony Peculic, Chris Harmse) after Mastercard completed the BVNK purchase in August 2026.
- Visa: Cash App Visa Debit Flex, Klarna Card, Affirm Card and Ramp cards are Visa; first US processor on Visa Flexible Credential (2024), live with Affirm, Klarna, Block; Visa DPS and Pismo compete with Marqeta.
- Not found: Agent Pay, Click to Pay, Move, Installments, Decision Intelligence or Priceless links with Marqeta. No TPV split by network ⚠.

## 3. Where Mastercard could land
- One Credential at Visa Flexible Credential's scale; Agent Pay behind the MCP server; the network role on Coinbase and zerohash stablecoin cards; Mastercard fraud scores in Real-Time Decisioning; Move for push-to-card payouts; commercial cards in Europe (Expensify, Banking Circle); programmes to replace Cash App's growth under the 2028 milestone.

## 4. How the page reads Marqeta
- Five discs: L1 Foundation (scale, ownership, banks and licences, network agreements, strategy) · L2 Rails (issuing, debit, credit, flexible credentials, money movement, Europe, stablecoins) · L3 Services (Real-Time Decisioning, KYC and disputes, tokens and wallets, programme management, agentic) · L4 Business lines (digital banking, BNPL, expense, on-demand and enterprise) · L5 Access (APIs, UX Toolkit, partners). Six kinds of user.
- The lens's per-area entries are read from the inventory (`customers/lens_tiles.py`).
- Gaps: network split by volume; networks for Expensify, Uber, DoorDash, Google and Coinbase programmes; Mastercard's stake size; TransactPay price.
