# BCEL — research notes behind the platform (as at 17 October 2026)

Companion to `BCEL_Platform.html`. One research thread (company and BCEL × Mastercard), condensed. Figures are the bank's own (2025 Annual Report, uploaded 5 May 2026; H1 2026 business-performance summary, 31 August 2026) unless marked. English sources are thin: BCEL publishes no card counts by network and no Mastercard press release with named Mastercard executives. ⚠ marks items that rest on secondary sources, could not be confirmed or are estimates.

## 1. The company
- Banque pour le Commerce Extérieur Lao Public (ທຄຕລ), Vientiane. Began 1975 as the State Bank's international division; commercial bank since 1 Nov 1989; first LSX listing (IPO Dec 2010). Ministry of Finance 60%, COFIBRED (BRED) 10%, others 30%; 1.545bn shares after a 1:5 split (Feb 2025) and a LAK 841.9bn offering (Oct 2025). Market value about LAK 1.9tn ⚠ (estimate). No rating found ⚠; headcount not disclosed ⚠.
- FY2025: assets LAK 160.8tn, deposits LAK 150.8tn, loans LAK 69.5tn, net profit LAK 932.5bn (2024: 449.6bn), ROE 20.3%, NPL 2.76%, CAR 10.2%. H1 2026: assets LAK 166.4tn, net profit LAK 625bn (+97%), NPL 2.06%.
- Network: 21 branches, 101 service units, 9 money changers, 734 BCOME agents; ATMs 287 or 400+ ⚠ (sources differ). BCEL One over 1.4m users, 2.5m e-banking users at end-2024 ⚠ (State Bank of Vietnam journal).
- Group: Lao-Viet Bank 25%, Lao-Viet Insurance 35%, Banque Franco-Lao 30% (sale approved ⚠), BCEL-KT 70%, Lao China Bank 39.9%, LAPNet 20% (UnionPay 15%), Lao Foreign Exchange 10%.
- Leadership: Chairman Soulivath Souvannachoumkham; MD Saysamone Chanthachack (since Aug 2022); Deputy MD Nanthalath Keopaseuth (ex-card centre head) signs payments deals.
- Strategy 2025–29: 50 projects, 8 for full digital banking, PCI DSS, Basel II, IFRS. 2026: profit +10%, NPL ≤3%. OceanBase core-banking MoU (Aug 2026). AI: nothing public ⚠.

## 2. BCEL × Mastercard
- Debit: UnionPay (since Jul 2011; UnionPay said 8 in 10 Lao cards in 2019). UnionPay virtual card 2025.
- Visa: issuer and acquirer since 2010; Visa Platinum credit and debit (Nov 2021); Visa Corporate, billed as Laos's first.
- Mastercard: World Mastercard credit and prepaid Mastercard (Apr 2019); Virtual Prepaid Mastercard in BCEL One (date ⚠); LoungeKey; Mastercard Campaign 2025 (draw Q2 2026); ATMs accept Mastercard, Maestro, Cirrus; POS acquiring ⚠ implied.
- JCB credit (May 2015) and a UnionPay co-brand ⚠ current status.
- QR: OnePay (10,000+ merchants in 2019 ⚠), UnionPay QR and WeChat Pay/Alipay (2019), PromptPay in Thailand, LAPNet links with UnionPay (Dec 2024), NAPAS (Jan 2025), Cambodia (2023 ⚠). EZyKip tourist wallet (Jan 2024) plans Mastercard top-ups ⚠.
- Remittances: MoneyGram, GLN (Korea), SWIFT.

## 3. Where Mastercard could land
- Debit and prepaid beside UnionPay; tourist top-ups in EZyKip; Move for remittances; tokens and fraud scoring alongside the PCI DSS project; commercial and virtual cards against Visa Corporate; card-linked offers.

## 4. How the page reads BCEL
- Five discs: Foundation · Rails (UnionPay debit, Visa, Mastercard, JCB, acquiring, OnePay, LAPNet and LAO QR, cross-border and remittances, EZyKip) · Services (security, onboarding, partners, loyalty) · Business lines (deposits, lending, treasury and FX, government and payroll) · Access (BCEL One and i-Bank, branches and ATMs, BCOME). Six kinds of user. Lens areas read from the inventory.
- Gaps: card counts and volumes by network; current OnePay merchant count; Mastercard's Laos lead; headcount; ratings.
