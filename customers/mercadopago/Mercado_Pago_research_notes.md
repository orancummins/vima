# Mercado Pago — research notes behind the platform (as at 17 October 2026)

Companion to `Mercado_Pago_Platform.html`. One research thread (the company, and Mercado Pago × Mastercard), condensed. Mercado Pago is the fintech business of MercadoLibre, Inc. (NASDAQ: MELI). Figures come from the group's releases (FY2025 on 24 Feb 2026; Q2 2026 on 5 Aug 2026), its IR newsletters and Mercado Pago's own country sites, read on 17 Oct 2026. ⚠ marks items that rest on secondary sources or could not be confirmed. SEC EDGAR was not reachable, so the 10-K was not read directly.

## 1. Mercado Pago — the company
- **Scale.**
  - 2025: revenue $12.6bn (+46%; $5.0bn in 2022) and TPV $278bn.
  - Q2 2026: revenue $4.4bn (+49%), TPV $101bn (+56%) and acquiring TPV $64bn (+44%).
  - Users and assets: 88m MAU (+30%; Brazil +38%, Mexico +45%) and $23bn of AUM (+68%).
  - Credit: a book of more than $16bn (+75%), of which cards are $7.7bn (+91%), with 2.6m cards issued in the quarter. The 15–90-day NPL is 4.6% for cards and 7.0% overall. At the end of 2025 the mix was about 45% cards, 36% consumer and 16% merchant ⚠.
  - Mexico has 1.4m active POS devices.
- **Licences.**
  - Brazil: a payment institution, a financial institution (Mercado Crédito) and a DTVM (2024). A bank licence is "not a priority" (Feb 2026).
  - Mexico: MP Agregador and Mercado Lending. It is applying to be a bank (process since 2024, about halfway in Sep 2026).
  - Argentina: a payment-service provider. It applied for a bank licence in May 2025. The BCRA said on 23 Sep 2026 it would have one "before year-end"; one outlet says it has already been granted ⚠, but the site still says it is not a financial institution.
  - Chile: a prepaid issuer, and it has asked the CMF to extend this to credit.
- **Parent and leaders.**
  - MELI is rated BBB- (S&P), Baa3 (Moody's) and BBB- (Fitch) and issued $1bn of 2036 notes (Sep 2026).
  - Galperin is Executive Chairman, Szarfsztejn CEO (from 1 Jan 2026), de los Santos CFO and Giménez Fintech President (since 2020; he has run Mercado Pago since 2004).
  - Fintech: SVP Anavi; André Chaves (Brazil); Matías Spagui (Chile).
- **Products.**
  - Acquiring: Point, Point Tap and Tap to Pay (Mexico 2026); checkout, links and subscriptions.
  - Credit cards: Visa in Brazil (2021) and Mexico (2023), Mastercard in Argentina (launch date ⚠). Chile is planned, network not stated ⚠.
  - Debit and prepaid: Visa in Brazil; Mastercard in Mexico (debit), Argentina (prepaid) and Chile (prepaid, 9m+ cards).
  - Off the cards: Pix, QR and SPEI; card-free instalments.
  - Savings, crypto and service: crypto and Meli Dólar via Paxos; savings (Cofrinhos, GBM fund, Mercado Fondo with 20m+ accounts, BICE); insurance; AI assistant (Oct 2025) and Mago; Meli+.

## 2. Mercado Pago × Mastercard
- **History:**
  - 2016: payment facilitator in Argentina with First Data (Diego Newell, Mastercard).
  - Feb 2018: prepaid Mastercard in Argentina, Brazil and Mexico, with more than 1m cards in under a year and biometrics and tokens from 2019 ⚠.
  - Nov 2022: Chile prepaid on Mastercard.
- **Today:** Mexican Debit Mastercard, the Argentine Mastercard credit card and prepaid card ⚠, Chilean prepaid, and acceptance everywhere.
- **Visa:** the Brazilian credit card (Mar 2021) and debit card (the switch from Mastercard prepaid is undated ⚠), the Mexican credit card (2023, with Visa Token Service) and Vai de Visa. It agreed to buy Argentina's Prisma and Newpay (Feb 2026). A 2024 Modo dispute was over Visa tokenisation on QR.
- **Not found:** Click to Pay, Agent Pay (Mercado Pago is not among the Dec 2025 LAC partners ⚠), Move/Send, Installments, Ethoca, open finance, World tiers or a renewal announcement.

## 3. Where Mastercard could land
- Network choices for the Mexican and Argentine bank programmes (payroll and debit) and the Chilean credit card.
- Issuer services (Consumer Clarity, notifications) on the Mastercard books.
- Acquirer risk and merchant data for $64bn a quarter.
- Tokens, Click to Pay and Agent Pay on Mercado Libre's checkout.
- Identity and fraud services against phone theft.
- Open finance for payroll capture.
- In the long run, the Brazilian card.

## 4. How the page reads Mercado Pago
- **Five discs:**
  - L1 Foundation: scale, licences, ownership, technology, strategy.
  - L2 Rails: acquiring, checkout, credit cards, debit and prepaid, Pix/QR/transfers, crypto.
  - L3 Services: credit, tokens, security, AI, loyalty, savings.
  - L4 Business lines: consumers, merchants, marketplace, salaries and benefits.
  - L5 Access: app, resellers, developers and partners.
- **Six kinds of user.** The lens's per-area entries are read from the inventory (`customers/lens_tiles.py`).
- **Gaps:** the network split by volume; the card book by country; the Argentine card launch date; the Brazilian switch date; the Argentine licence status; the current Mexico head.
