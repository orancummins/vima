# Block — research notes behind the platform (as at 17 October 2026)

Companion to `Block_Platform.html`. These notes condense one research thread: the company, then Block × Mastercard. Figures are Block's own: the Q2 2026 letter and presentation (5 Aug 2026), the Q1 2026 and Q4 2025 letters, the FY2025 10-K (26 Feb 2026) and the Investor Day release (19 Nov 2025). Card networks come from Square, Cash App and Afterpay pages and from press. ⚠ marks items that rest on secondary sources or could not be confirmed.

## 1. Block — the company
- **Corporate:**
  - Block, Inc. (NYSE: XYZ), formerly Square, Inc.; a "distributed workforce" with an Oakland address.
  - Market value about $47bn (Oct 2026). Credit ratings not found ⚠.
  - 10,205 staff at end-2025, cut to just under 6,000 from February 2026 ("AI-native teams").
- **Leadership:** Jack Dorsey (Block Head, chair); Amrita Ahuja (COO and CFO); Owen Jennings (Business Lead); Thomas Templeton (Hardware Lead); Andrea Acosta (CAO from 26 May 2026). Engineering lead Arnaud Weber left on 5 Jun 2026.
- **FY2025 scale:**
  - Revenue $24.19bn; gross profit $10.36bn (+17%), of which Cash App $6.34bn and Square $3.94bn.
  - Square GPV $250.5bn from more than 4.5m sellers.
  - Adjusted operating income $2.08bn; net income $1.30bn.
- **Q2 2026:**
  - Gross profit $3.17bn (+25%); adjusted operating margin 27%.
  - Square GPV $72.8bn (+13%).
  - Cash App: 59m monthly actives; 9.4m primary banking actives; lending originations $18.9bn (+59%).
  - 2026 guidance $12.51bn gross profit.
- **2028 targets (Investor Day):** gross profit about $15.8bn; adjusted operating income $4.6bn; adjusted EPS $5.50.
- **Entities:**
  - Square Financial Services: a Utah industrial bank (FDIC), which has made Cash App Borrow loans since March 2025.
  - Square Capital; Cash App Investing (broker-dealer); NY BitLicense.
  - Afterpay (US, AU, CA, NZ, UK); TIDAL (majority-owned); Proto; Bitkey.
- **Regulation:** CFPB order, 16 Jan 2025: up to $175m. State and NYDFS settlements ⚠ (not re-sourced).
- **Products:**
  - Square: payments, software, Kiosk (14 Oct 2026), Handheld and Register; Square Bitcoin (Oct 2025, 0% fee through 2026).
  - Square banking: Checking and Debit Card (Mastercard, Sutton Bank), Savings, Loans, Credit Card (Amex, Celtic Bank).
  - Cash App: Card (Visa, Sutton Bank, Marqeta; 26m actives in Q3 2025), P2P, Pay, Borrow, Tags, USDC, bitcoin.
  - AI and data: Cash App Score (sold to lenders through Nova Credit from Sep 2026), Moneybot, Managerbot, goose, Buzz.
  - Neighborhoods: $1bn annualised GPV; 30,000 sellers.
  - Afterpay: Pay in 4, and on the Cash App Card through the Visa Debit Flex pilot (Nov 2025).
  - Agentic: Square in ChatGPT and Claude (1 Jul 2026); takes part in UCP.

## 2. Block × Mastercard
- **Mastercard:**
  - Square Debit Card (Jan 2019, Sutton Bank) and Square Checking.
  - Acceptance across Square.
  - Instant transfers by OCT to Mastercard and Visa debit cards ⚠ (Send or Move not named).
  - Afterpay repayments on Mastercard cards.
  - A 2021 Westpac Afterpay card in Australia on Mastercard or eftpos ⚠ (current status unknown).
- **Visa:** the Cash App Card, the Afterpay Visa Debit Flex pilot, and the US Afterpay Card ⚠.
- **American Express:** the Square Credit Card.
- **Not found:** a scheme agreement, Agent Pay, Click to Pay, Mastercard Installments, Move, Ethoca, Open Finance, or stablecoin settlement with Block.
- **Block's own rails:** Cash App Pay, Neighborhoods (1% processing), balances, bitcoin and USDC. Bloomberg reported (10 Oct 2025) that Block is targeting card-network fees ⚠.

## 3. Where Mastercard could land
- Move for Square and Cash App instant payouts.
- Acquirer risk tools (MATCH, merchant identification) for Square's ISO channel (+150% new sellers quarter on quarter).
- Agent Pay for Square's ChatGPT, Claude and Kiosk orders.
- Instalments against the Visa Flex pilot.
- Dispute and scam tools after the CFPB order.
- Business payment controls on the Square Debit Card.
- Stablecoin settlement through BVNK's Mastercard Global Money (Oct 2026).

## 4. How the page reads Block
- **Five discs:**
  - L1 Foundation: scale, leadership, bank and licences, strategy.
  - L2 Rails: Square payments, seller cards, Cash App Card, Afterpay, P2P and instant transfers, Cash App Pay and digital money.
  - L3 Services: fraud, credit data, AI, Neighborhoods, agentic.
  - L4 Business lines: Square software, seller banking, Cash App banking, Borrow, bitcoin, Proto, Bitkey and TIDAL.
  - L5 Access: apps, hardware, sales and partners.
- **Users:** six kinds. **Journeys:** ten, two of them for Mastercard.
- **Lens title:** "Mastercard on the seller's card, Visa in the Cash App wallet".
- The lens's per-area entries are read from the inventory (`customers/lens_tiles.py`).
- **Gaps:**
  - Network split by volume.
  - Current Afterpay card networks.
  - Credit ratings.
  - Cash App Card actives for 2026.
  - Square Credit Card launch date.
  - Push-to-card branding.
