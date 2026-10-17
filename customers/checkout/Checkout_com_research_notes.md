# Checkout.com — research notes behind the platform (as at 17 October 2026)

Companion to `Checkout_com_Platform.html`. One research thread (company and Checkout.com × Mastercard), condensed. Checkout.com is private: figures are its own releases (FY2025 update, 24 Feb 2026; annualised revenue, 29 Sep 2026) and press. ⚠ marks items that rest on secondary sources or could not be confirmed.

## 1. Checkout.com — the company
- Checkout Ltd (London; FCA EMI), Checkout SAS (ACPR, EEA), Checkout US (money transmitter) and a Georgia MALPB charter (approved 12 Jan 2026; US direct acquiring live 9 Sep 2026); ten acquiring licences; 2,300 staff in 19 offices. Founder and CEO Guillaume Pousaz; CPO Meron Colbeci; CRO Antoine Nougué; CTO Mariano Albera; interim CFO Philip Symes ⚠.
- Scale: >$300bn volume in 2025 (+64%), adjusted EBITDA margin >10%; $750m annualised net revenue (Sep 2026, +28%); ~$150m adjusted EBITDA and $480bn volume guided for 2026 ⚠ scope; 63 merchants >$1bn; US 20% of volume. Internal valuation $12bn (Sep 2025).
- Deals: ProcessOut, Pin Payments (2020), Icefire (2021), ubble (2022), Blue EMI (euro-stablecoin issuer, Jan 2026). Legacy-system data incident (Nov 2025; ransom refused).
- Products: global and US direct acquiring; 50+ local methods; Apple/Google Pay; BNPL partners; issuing (dual-network UK/EU, $5bn run rate Q4 2025); Mastercard Wholesale virtual cards for OTAs (May 2024); Visa travel issuing (Jul 2025); Pay-to-Card on Mastercard Move (UAE Feb 2025, Canada Sep 2026) and Visa Direct; RTP/ACH payouts; Business Account; stablecoin acceptance (Coinbase), settlement (Fireblocks) and issuance (Blue EMI); Intelligent Acceptance ($15bn uplift); network tokens (11% uplift); 3DS, face authentication, identity; Fraud Detection Pro; Verifi RDR; Flow and Remember Me; agentic suite (ACP, UCP, AP2, Visa Intelligent Commerce, Agent Pay).
- Merchants: eBay, Uber, Spotify, Microsoft, Temu, Vinted, Trip.com, Agoda, Coinbase, Moomoo, Klarna.

## 2. Checkout.com × Mastercard
- Network tokens and acceptance; dual-network issuing; Mastercard Wholesale Program (May 2024); Mastercard Move in the UAE (26 Feb 2025; Mete Guney, Remo Giovanni Abbondandolo) and Canada (Sep 2026); Agent Pay launch partner (29 Apr 2025); Verifiable Intent (5 Mar 2026; Pablo Fourez, Meron Colbeci); Agent Pay for Machines (10 Jun 2026).
- Not found: Click to Pay, Ethoca, Mastercard open banking, Installments, stablecoin settlement with Mastercard.
- Visa: Visa Direct UAE first (Feb 2025), travel issuing (Jul 2025), Verifi, Moomoo funding (Oct 2026).

## 3. Where Mastercard could land
- Click to Pay and passkeys against Remember Me; Ethoca beside Verifi; Move and issuing in the US and UAE; services for US direct acquiring; production Agent Pay volume; stablecoin settlement; open banking.

## 4. How the page reads Checkout.com
- Five discs: L1 Foundation (scale, licences and charter, ownership, platform, strategy) · L2 Rails (acquiring, methods, issuing, payouts, stablecoins, business account) · L3 Services (Intelligent Acceptance, authentication, fraud, checkout, agentic) · L4 Business lines (enterprise, marketplaces, travel, fintech) · L5 Access (API, regions, partners). Five kinds of user.
- The lens's per-area entries are read from the inventory (`customers/lens_tiles.py`).
- Gaps: network split; absolute 2025 revenue; permanent CFO; principal memberships.
