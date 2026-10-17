# Ant International — research notes behind the platform (as at 17 October 2026)

Companion to `Ant_International_Platform.html`. One research thread (company and Ant International × Mastercard), condensed. Ant International is private and publishes no financial statements: figures are its own releases (MoMents, 30 Apr 2026; VOYAGE, 18 Sep 2026), its 2025 Sustainability Report (May 2026), partner releases and press. Ant Group and Alipay in mainland China are context only. ⚠ marks items that rest on secondary sources or could not be confirmed.

## 1. Ant International — the company
- Singapore-headquartered international arm of Ant Group; own board since 2023, independent operation since 2024. Series A of about $1.2bn closed 21 Jul 2026 (Ant Group, Alibaba, unnamed institutions); ~$10bn valuation reported ⚠; possible Hong Kong listing ⚠. Headcount, ratings and full licence list not published ⚠.
- Leadership: CEO Peng Yang; President Douglas Feagin; CFO Yi Zhou; CIO Jiangming Yang; Gary Liu (Antom), Clara Shi (WorldFirst), Huaisheng Chen (Bettr), Kai Qiu (ANEXT Bank). Chairman Eric Jing (2025) ⚠.
- Scale: 150m+ merchants, 2bn+ accounts, 300+ methods, 220+ markets (Apr 2026); 25m+ transactions a day (Sep 2026). Revenue ~$3bn in 2024, +~25% in 2025, adjusted profit two years running ⚠ (Bloomberg, unnamed people).
- Pillars: Alipay+ (53 wallets, 10 national QR schemes; Alipay+ NFC on Mastercard); Antom (acquiring in 200+ markets, 2C2P, MultiSafepay with 20,000+ merchants); WorldFirst (1.6m+ SMEs, World Account, World Card); Bettr (credit tech for 49 institutions; ANEXT Bank; settlement token).
- Tech: 3-in-1 Transformer, FalconTST (93% FX accuracy; Barclays BARX, May 2025), AI SHIELD; WhaleRTP blockchain treasury (45% of 2025 cross-border volume; HSBC tokenised deposits in Singapore, Hong Kong, UAE). Stablecoin licences sought (Jun 2025) ⚠ status unknown.
- Agentic: Agentic Mobile Protocol (Apr 2026; 10 wallets, 7 acquirers incl. Adyen, Checkout.com, Fiserv, Worldline); co-developed Google's UCP; Antom AgentSafePay; WorldFirst Account for Agent.
- 2026 deals: Brazil Payment Institution licence (4 Sep), SAMA/mada cross-border QR plan, NAPAS/Vietcombank, R2 stake.

## 2. Ant International × Mastercard
- Alipay+ NFC: wallets tap at 150m+ Mastercard contactless locations via a token; GCash Tap to Pay (19 Aug 2025; Ren-Ren Reyes, Douglas Feagin) and Kakao Pay (22–23 Sep 2025; Sandeep Malhotra, Mastercard). Android only; iOS coming.
- Antom among the first APAC partners piloting Mastercard Agent Pay (and Visa Intelligent Commerce), Sep 2025 (Gary Liu).
- Know-Your-Agent interoperability with Mastercard and Visa through MAS's BuildFin.ai (10 Sep 2026; Pablo Fourez, Mastercard; Jiang-Ming Yang, Ant International).
- WorldFirst World Card is Mastercard in the UK; other markets ⚠. Antom accepts all networks. China inbound (Ant Group): Consumer Friendly Zones with Mastercard (2024); foreign Visa, Mastercard, JCB, Discover, Diners and Amex cards on Alipay.
- Not found: Move, Click to Pay, Ethoca, open banking, network-token detail, any network agreement or switch.

## 3. Where Mastercard could land
- NFC for more of 53 wallets and on iOS; live Agent Pay through Antom; Ethoca and Consumer Clarity for Antom's disputes; Move for WorldFirst payouts; World Card beyond the UK; network tokens and Click to Pay for Antom.

## 4. How the page reads Ant International
- Five discs: L1 Foundation (scale, ownership, leadership, licences, AI, strategy) · L2 Rails (wallet gateway, NFC on Mastercard, acquiring, accounts and cards, blockchain treasury, bank-to-wallet) · L3 Services (risk, disputes, optimisation, agentic, FX AI, marketing) · L4 Business lines (wallets, merchants, SMEs, credit, China inbound) · L5 Access (portal, apps, regions, partners). Six kinds of user.
- The lens's per-area entries are read from the inventory (`customers/lens_tiles.py`).
- Gaps: audited financials; headcount; network for 2C2P issuing and non-UK World Cards; stablecoin licences.
