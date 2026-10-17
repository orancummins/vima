"""Klarna Group's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are Klarna's own unless a source says otherwise: the Q2 2026 results (18 August 2026), the Q1 2026
results (14 May 2026), the Q4 and full-year 2025 results (19 and 26 February 2026), the Klarna Holding AB
annual report 2025 and Klarna's newsroom. Q3 2026 results had not been released. ``neo`` is the Mastercard
lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

NEWS = "https://www.klarna.com/international/press/"
Q2 = "https://s205.q4cdn.com/644747736/files/doc_earnings/2026/q2/earnings-result/Q2-26-Klarna-Group-plc-Press-Release.pdf"
Q1 = "https://s205.q4cdn.com/644747736/files/doc_news/Klarna-Delivers-Strong-Start-to-2026-With-1Bn-Revenue-and-68M-Adj--Operating-Profit-2026.pdf"
Q4 = NEWS + "klarna-accelerates-u-s-growth-and-delivers-usd1bn-revenue-driven-by-rapid/"
FY25 = "https://s205.q4cdn.com/644747736/files/doc_news/Klarna-Group-plc-Publishes-Full-Year-2025-Results-2026.pdf"
AR25 = "https://s205.q4cdn.com/644747736/files/doc_financials/2025/q4/Klarna-KHAB-Annual-Report-2025-ENG.pdf"
Q3 = NEWS + "klarna-delivers-record-breaking-q3-as-ai-powered-digital-bank-usd903-million/"
IPO = NEWS + "klarna-announces-pricing-of-its-initial-public-offering/"
LICENCE = NEWS + "klarna-europes-newest-bank-is-born/"
RATING = NEWS + "klarna-assigned-investment-grade-credit-rating-from-sp-global/"
STOCK = "https://stockanalysis.com/stocks/klar/"
DROP = "https://www.webull.com/news/15429133989200896"
FCA = NEWS + "klarna-receives-fca-authorisation-paving-the-way-for-cashback-and-balance/"
USBANK = NEWS + "klarna-submits-application-for-u-s-banking-license/"
MORITZ = NEWS + "klarna-board-chair-michael-moritz-acquires-3-47-million-shares-for-usd50/"
CEOSHARES = NEWS + "klarna-ceo-sebastian-siemiatkowski-acquires-692-506-shares-for-10-million/"
NELNET = NEWS + "klarna-secures-scalable-funding-in-usd26bn-deal-to-drive-u-s-pay-in-4-growth/"
ELLIOTT = NEWS + "klarna-and-elliott-deepen-partnership-with-usd2bn-facility-supporting/"
SRT = NEWS + "klarna-agrees-to-usd1-7-billion-transaction-supporting-up-to-usd40b-of/"
GERFF = NEWS + "klarna-adds-germany-to-its-capital-efficiency-platform-with-eur900m-facility-supporting-eur5bn-of-german-financing-expansion/"
COINBASE = NEWS + "klarna-partners-with-coinbase-to-add-stablecoin-to-funding-mix/"
AIASSIST = NEWS + "klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/"
PRICERUNNER = NEWS + "klarna-has-received-a-favorable-ruling-in-pricerunner-litigation-awarding-damages-of-1-97-billion/"
KOSMA = "https://tech.eu/2023/07/31/klarna-scraps-open-banking-brand-klarna-kosma/"
SOFORT = NEWS + "klarna-combines-sofortuberweisung-with-klarna-payments-to-bring-customers-and-merchants-the-best-of-both-worlds/"
WORLDPAY = NEWS + "klarna-and-worldpay-expand-partnership-to-unlock-global-merchant-network/"
LINK = "https://support.link.com/questions/pay-with-klarna"
ONETIME = "https://coingate.com/en/gift-cards/articles/article/can-you-use-klarna-on-amazon"
ONEPAY = NEWS + "klarna-announces-partnership-with-onepay-to-exclusively-power-installment/"
APPLEUP = NEWS + "klarna-to-power-apple-upgrade-a-new-hardware-leasing-program-offered-by-apple/"
ELLIOTT25 = NEWS + "klarna-powers-fair-financing-hypergrowth-with-usd6-5bn-us-agreement/"
VISAPILOT = NEWS + "klarna-and-visa-launch-pilot-of-new-debit-card-with-increased-flexibility-at/"
CARD1M = NEWS + "klarna-card-passes-1-million-us-sign-ups-in-11-weeks/"
CARDEU = NEWS + "klarna-launches-debit-first-card-across-europe-for-everyday-spending/"
CARDUK = NEWS + "klarna-launches-flexible-debit-card-and-digital-wallet-in-uk/"
CARD5M = NEWS + "klarna-card-reaches-5-million-active-customers/"
MARQETA = "https://cxmtoday.com/news/marqeta-klarna-expand-klarna-card-across-15-new-european-markets/"
VISA2017 = NEWS + "visa-commits-to-strategic-investment-in-klarna-companies-plan-partnership-deal/"
P2P = NEWS + "klarna-expands-digital-bank-offer-with-peer-to-peer-payments/"
APPLEPAY = NEWS + "klarna-now-available-on-apple-pay-in-denmark-spain-and-sweden-with-france-to/"
ADYEN = NEWS + "adyen-and-klarna-go-to-the-shops-klarna-launches-on-adyen-in-store-terminals-across-europe-north-america-and-australia/"
LULU = NEWS + "klarna-gets-physical-with-lululemon-launching-in-store-in-the-uk-and-germany/"
USDK = NEWS + "klarna-launches-klarnausd-as-stablecoin-transactions-hit-usd27-trillion/"
PRIVY = NEWS + "klarna-partners-with-privy-to-develop-simple-secure-crypto-wallet-for-the/"
INBOX = NEWS + "klarna-launches-in-app-inbox-to-help-consumers-avoid-scams/"
CALL = NEWS + "klarna-expands-nordics-anti-fraud-toolkit-with-new-live-call-verification-tool/"
AP2 = NEWS + "klarna-strengthens-collaboration-with-google-to-support-agent-payments/"
UCP = NEWS + "klarna-backs-googles-universal-commerce-protocol-ucp-to-enable-agentic/"
APP = NEWS + "klarna-launches-agentic-product-protocol-the-open-standard-that-makes-100m/"
CHATGPT = NEWS + "klarna-launches-ai-powered-shopping-search-app-in-chatgpt/"
GEMINI = NEWS + "klarnas-flexible-payments-are-coming-to-google-search-and-the-gemini-app-within-google-pay/"
MEMB25 = NEWS + "klarna-launches-memberships-premium-perks-without-expensive-credit/"
MEMB26 = NEWS + "the-fairest-of-them-all-klarna-supercharges-memberships-removing-fees-boosting-cashback-and-increasing-annual-value-to-as-much-as-eur6-000/"
MOBILEUS = NEWS + "tap-to-switch-klarna-expands-into-mobile-phone-plans-with-flexible-no-hassle/"
MOBILEUK = NEWS + "klarna-adds-free-unlimited-mobile-plan-to-app-for-uk-max-members/"
SAVINGS = NEWS + "klarna-launches-high-yield-savings-account-turning-everyday-spend-into-everyday-savings/"
SOUTHWEST = NEWS + "klarna-lands-southwest-airlines-bringing-flexible-payments-to-millions-of-us-travelers-this-fall/"
TAP = NEWS + "tap-and-klarnas-partnership-takes-off-flexible-payments-now-available-in-the-us-spain-france-and-italy/"
BOLT = NEWS + "klarna-partners-with-bolt-to-grow-pay-in-full-for-rides-and-scooters/"
STRIPE = NEWS + "klarna-available-to-millions-of-new-businesses-in-strengthened-stripe/"
NEXI = NEWS + "nexi-and-klarna-partner-to-boost-merchant-growth/"
JPM = NEWS + "klarna-goes-live-with-j-p-morgan-payments-opening-flexible-checkout-to-u-s-merchants/"
WORLDLINE = NEWS + "worldline-and-klarna-partner-to-enable-flexible-online-and-in-store-payments-everywhere/"
SWEDBANK = NEWS + "klarna-blir-tillgaengligt-genom-swedbank-pay-foer-tusentals-handlare-i-norden/"
ECOMMPAY = NEWS + "ecommpay-adds-klarna-giving-consumers-a-more-flexible-way-to-pay/"
MPGS = "https://developer.mastercard.com/mastercard-gateway/documentation/payment-methods/alt-pay-methods/buynow-paylater/klarna-pay-later/"
UKREG = NEWS + "new-regulation-set-to-strengthen-consumer-trust-in-bnpl-survey-shows/"
AGENTPAY = "https://newsroom.mastercard.com/news/press/2025/april/mastercard-unveils-agent-pay-pioneering-agentic-payments-technology-to-power-commerce-in-the-age-of-ai"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "scale · licences · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: 120 million active consumers and $128 billion of volume in 2025, a Swedish bank since 2017 with a US charter applied for, a New York listing worth about a third of its IPO price, deposits and forward flows for funding, and a plan to turn checkout users into banking customers.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & results", "blurb": "120m consumers, $36.6bn a quarter.", "div": "grp", "rev": "grp", "products": [
            P("results", "Volume & earnings", "GMV of $127.9 billion (+22%) and revenue of $3.5 billion (+25%) in 2025, adjusted operating profit $65 million; Q2 2026 GMV $36.6 billion (+18%, US +27%), revenue $1.042 billion (+27%), transaction margin $446 million (+42%), net income $9 million. 120 million active consumers and 1.2 million merchants in 26 countries.",
              s=["shop", "mer"], neo=[0, ""], src=[["Klarna: Q2 2026 results", Q2], ["Klarna: full year 2025", FY25], ["Klarna Holding AB annual report 2025", AR25]]),
            P("guidance", "2026 guidance cut", "In August 2026 Klarna cut full-year GMV guidance to $149–151 billion (from more than $155 billion) and revenue to $4.08–4.16 billion, on currency and weaker German volumes, while raising transaction margin to $1.62–1.65 billion; Q3 is an 'investment quarter' for PSP launches. The shares fell about 23% that day.",
              s=["shop"], st="new", ay="Aug 2026", neo=[0, ""], src=[["Klarna: Q2 2026 results", Q2], ["Benzinga via Webull: shares fall, Aug 2026", DROP]]),
        ]},
        {"id": "1.2", "ic": "badge-check", "name": "Bank & licences", "blurb": "A Swedish bank since 2017.", "div": "bank", "rev": "grp", "products": [
            P("banklicence", "Klarna Bank AB", "Licensed by Finansinspektionen on 19 June 2017 and passported across the EEA, with branches in Denmark, France, Ireland, Germany and the UK; CET1 15.7% at Klarna Holding AB (end-2025); rated BBB by S&P since April 2023 ⚠ no later action found.",
              s=["bank"], o="B", ay="Jun 2017", neo=[0, ""], src=[["Klarna: Europe's newest bank, Jun 2017", LICENCE], ["Klarna Holding AB annual report 2025", AR25], ["Klarna: S&P rating, Apr 2023", RATING]]),
            P("fcaemi", "UK e-money licence", "Klarna Financial Services UK authorised by the FCA as an e-money institution in July 2025, for Klarna balance and cashback for 11 million UK consumers.",
              s=["bank"], ay="Jul 2025", neo=[0, ""], src=[["Klarna: FCA authorisation, Jul 2025", FCA]]),
            P("usbank", "Klarna Bank USA (proposed)", "A Utah industrial bank applied for with the Utah DFI and FDIC on 6 July 2026, to bring US banking in-house from partner banks; Gary Harding named president and CEO.",
              s=["bank"], st="new", ay="Jul 2026", neo=[None, "Network choice not yet made."],
              mc="An own US charter would put the US card issuing decision, now with WebBank on Visa, in Klarna's hands.",
              src=[["Klarna: US bank application, Jul 2026", USBANK]]),
        ]},
        {"id": "1.3", "ic": "scale", "name": "Leadership & listing", "blurb": "Founder-led, NYSE since 2025.", "div": "grp", "rev": "grp", "products": [
            P("leadership", "Board & executives", "Co-founder Sebastian Siemiatkowski CEO since 2005; Niclas Neglén CFO; David Sykes CCO; David Sandström CMO; David Fock CPDO; Camilla Giesecke COO; Michael Moritz chairs the plc board, Roger Ferguson Jr. the bank's ⚠ governance page not reachable.",
              s=["shop"], neo=[0, ""], src=[["Klarna Holding AB annual report 2025", AR25], ["Klarna: chair buys shares, Mar 2026", MORITZ], ["Klarna: CEO buys shares, Aug 2026", CEOSHARES]]),
            P("listing", "NYSE listing", "IPO priced at $40 on 9 September 2025 (34.3 million shares, 5 million new); shares closed at $13.02 on 16 October 2026, a market value of about $4.9 billion; 2,795 employees at end-2025.",
              s=["shop"], ay="Sep 2025", neo=[0, ""], src=[["Klarna: IPO pricing, Sep 2025", IPO], ["StockAnalysis: KLAR", STOCK], ["Klarna Holding AB annual report 2025", AR25]]),
        ]},
        {"id": "1.4", "ic": "coins", "name": "Funding", "blurb": "Deposits, forward flows.", "div": "bank", "rev": "grp", "products": [
            P("deposits", "Deposits", "About 90% of funding is consumer deposits: SEK 121.8 billion at end-2025, gathered mainly in Germany and Sweden; over $12.3 billion in eleven European markets (June 2026).",
              s=["bank"], neo=[0, ""], src=[["Klarna: Q2 2026 results", Q2], ["Klarna Holding AB annual report 2025", AR25], ["Klarna: US Savings, Jun 2026", SAVINGS]]),
            P("forwardflow", "Forward flows, SRTs & USDC", "Nelnet buys up to $26 billion of US Pay in 4 (August 2025); Elliott funds up to $17 billion of US Fair Financing (doubled March 2026); a Värde-led $1.7 billion SRT (April 2026); a €900 million German facility (July 2026); and USDC funding through Coinbase (December 2025).",
              s=["shop"], o="P", at="Nelnet, Elliott, Värde, Coinbase", st="new", neo=[0, ""],
              src=[["Klarna: Nelnet, Aug 2025", NELNET], ["Klarna: Elliott, Mar 2026", ELLIOTT], ["Klarna: SRT, Apr 2026", SRT], ["Klarna: German facility, Jul 2026", GERFF], ["Klarna: Coinbase, Dec 2025", COINBASE]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy, tech & deals", "blurb": "Payments first, then banking.", "div": "grp", "rev": "grp", "products": [
            P("strategy", "The everyday finance network", "Acquire customers through payments, then deepen them into banking: 15.8 million 'banking consumers' bring $107 of revenue each against $30 on average (Q4 2025). Managed on transaction margin dollars, about 1.09% of GMV in 2026.",
              s=["shop", "bank"], neo=[0, ""], src=[["Klarna: Q4 2025 results", Q4], ["Klarna: Q2 2026 results", Q2]]),
            P("platform", "Platform & AI", "One cloud-native platform with real-time machine-learning decisioning, 3.8 million transactions a day; an OpenAI-powered assistant (two-thirds of service chats in its first month, February 2024), a Google Cloud AI partnership (October 2025) and revenue per employee near $1.4 million.",
              s=["shop"], o="B", neo=[0, ""], src=[["Klarna Holding AB annual report 2025", AR25], ["Klarna: AI assistant, Feb 2024", AIASSIST], ["Klarna: Q1 2026 results", Q1]]),
            P("deals", "Deals & disposals", "PriceRunner bought in 2022 (awarded $1.97 billion against Google in July 2026, subject to appeal); the Kosma open-banking brand folded back in 2023; Sofort merged into Pay Now (2024); Klarna Checkout sold to the Kustom consortium (2024).",
              s=["mer"], o="A", neo=[0, ""], src=[["Klarna: PriceRunner ruling, Jul 2026", PRICERUNNER], ["Tech.eu: Kosma brand dropped, Jul 2023", KOSMA], ["Klarna: Sofort, Jul 2024", SOFORT], ["Klarna Holding AB annual report 2025", AR25]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Pay Now by card or bank, Pay Later on Klarna's own books, Fair Financing and leasing, the Klarna Card on Visa Flexible Credential in 16 countries, Balance and P2P transfers, Apple Pay and in-store QR, and a stablecoin on Stripe's Tempo.",
    "tiles": [
        {"id": "2.1", "ic": "zap", "name": "Pay Now", "blurb": "Card or bank, paid in full.", "div": "klarna", "rev": "paynow", "products": [
            P("paynow", "Pay Now & Sofort", "Pay in full at checkout from a saved card or bank account; about 30% of Klarna payments are immediate (2024); Sofortüberweisung folded into Pay Now in Germany in July 2024.",
              s=["shop", "mer"], lc="move", neo=[1, "Funded by cards on any network, Mastercard among them ⚠, or by bank."],
              src=[["Klarna and Worldpay, Oct 2024", WORLDPAY], ["Klarna: Sofort, Jul 2024", SOFORT], ["Link: pay with Klarna", LINK]]),
        ]},
        {"id": "2.2", "ic": "receipt-text", "name": "Pay Later", "blurb": "Pay in 4, Pay in 30.", "div": "klarna", "rev": "paylater", "products": [
            P("paylater", "Pay in 4, Pay in 3 & Pay in 30", "Interest-free short-term credit on Klarna's own balance sheet, about 40 days on average; 84% of loans are three months or less; provisions 0.52% of GMV (Q2 2026). Klarna says it is three times the nearest US rival in Pay in 4 volume.",
              s=["shop"], lc="borrow", neo=[1, "Klarna's own credit; repaid by card on any network or by bank ⚠."],
              src=[["Klarna Holding AB annual report 2025", AR25], ["Klarna: Q2 2026 results", Q2], ["Klarna: Q3 2025 results", Q3], ["Link: pay with Klarna", LINK]]),
            P("onetime", "One-time card", "A single-use virtual card in the US app, for paying in four at stores outside Klarna's network ⚠ Visa per third-party sources.", short="One-time card (Visa ⚠)",
              s=["shop"], lc="borrow", o="P", at="WebBank ⚠", neo=[0, "Visa ⚠."], src=[["CoinGate: Klarna on Amazon", ONETIME]]),
        ]},
        {"id": "2.3", "ic": "hand-coins", "name": "Fair Financing", "blurb": "3–36 months, +138%.", "div": "klarna", "rev": "financing", "products": [
            P("fairfin", "Fair Financing", "Fixed-term instalment loans for bigger purchases: GMV up 138% in Q1 2026 and 9% of GMV in 2025; 256,000 merchants offer it (+107%).",
              s=["big"], lc="borrow", neo=[0, "A loan, not a card payment."], src=[["Klarna: Q1 2026 results", Q1], ["Klarna: Q2 2026 results", Q2], ["Klarna: Elliott, Nov 2025", ELLIOTT25]]),
            P("onepay", "OnePay at Walmart", "Exclusive provider of OnePay instalment loans (3 to 36 months) at Walmart in the US, online and in store (announced March 2025).",
              s=["big"], lc="borrow", ay="Mar 2025", o="P", at="OnePay, Walmart", neo=[0, ""], src=[["Klarna: OnePay, Mar 2025", ONEPAY]]),
            P("appleupgrade", "Apple Upgrade leasing", "The leasing provider behind Apple Upgrade in the US: 12- to 36-month leases on iPhone, Mac, iPad and Apple Watch (July 2026).",
              s=["big"], lc="borrow", st="new", ay="Jul 2026", o="P", at="Apple", neo=[0, ""], src=[["Klarna: Apple Upgrade, Jul 2026", APPLEUP]]),
        ]},
        {"id": "2.4", "ic": "credit-card", "name": "Klarna Card", "blurb": "6.5m users, all on Visa.", "div": "klarna", "rev": "banking", "products": [
            P("cardus", "Klarna Card (US)", "Debit-first card with Pay in 4 and financing on request, powered by Visa Flexible Credential and issued by WebBank: piloted June 2025, launched 4 July 2025, a million sign-ups in 11 weeks. Earlier US Klarna Cards (2022, 2024) were also Visa.", short="Klarna Card US (Visa)",
              s=["bank"], lc="everyday", st="new", ay="Jul 2025", o="P", at="Visa, WebBank", neo=[0, "Visa."],
              mc="Klarna's fastest-growing product, on Visa's multi-mode credential.",
              src=[["Klarna and Visa: card pilot, Jun 2025", VISAPILOT], ["Klarna: 1 million US sign-ups, Sep 2025", CARD1M]]),
            P("cardeu", "Klarna Card (Europe & UK)", "Rolled out across ten EU countries from September 2025 and the UK, Denmark, Germany, Norway and Poland from October 2025, on Visa Flexible Credential with Marqeta as issuer processor; 6.5 million active users in 16 countries by Q2 2026, card payments 15% of Klarna transactions (October 2025).", short="Klarna Card Europe (Visa)",
              s=["bank"], lc="everyday", st="new", ay="Sep 2025", o="P", at="Visa, Marqeta", neo=[0, "Visa."],
              src=[["Klarna: card across Europe, Sep 2025", CARDEU], ["Klarna: UK card, Oct 2025", CARDUK], ["CX Today: Marqeta, Nov 2025", MARQETA], ["Klarna: Q2 2026 results", Q2]]),
        ]},
        {"id": "2.5", "ic": "arrow-left-right", "name": "Balance & P2P", "blurb": "Wallet and transfers.", "div": "bank", "rev": "banking", "products": [
            P("balance", "Klarna Balance", "A deposit or e-money wallet in 15 markets (UK from October 2025) for refunds, cashback and top-ups from a payment card; deposits rose from $9.5 billion to $14 billion between December 2024 and September 2025.",
              s=["bank"], lc="everyday", neo=[1, "Topped up from cards on any network ⚠."], src=[["Klarna: UK Balance, Oct 2025", CARDUK], ["Klarna: P2P, Jan 2026", P2P]]),
            P("p2p", "Peer-to-peer payments", "Instant transfers between Klarna users in 13 European countries (January 2026) on bank rails, with non-Klarna recipients, cross-border transfers and stablecoins being explored.",
              s=["bank"], lc="move", st="new", ay="Jan 2026", neo=[0, "Bank rails."],
              mc="Cross-border P2P and payouts to non-Klarna users are planned; Mastercard Move could carry them.",
              src=[["Klarna: P2P, Jan 2026", P2P]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "In-store & wallets", "blurb": "Apple Pay, QR at the till.", "div": "klarna", "rev": "paylater", "products": [
            P("applepay", "Klarna in Apple Pay & Google Pay", "Klarna as a pay-later choice inside Apple Pay in the US, UK, Canada, Denmark, Spain, Sweden, France and Italy (November 2025), and in Google Pay.",
              s=["shop"], lc="move", o="P", at="Apple, Google", neo=[None, "Mechanics not disclosed."], src=[["Klarna: Apple Pay in Europe, Nov 2025", APPLEPAY]]),
            P("instore", "In-store QR", "Pay with the Klarna app by scanning a QR code at the till: on Adyen terminals since September 2024, and at lululemon (UK and Germany, July 2026) and GARAGE and DYNAMITE.",
              s=["shop", "mer"], lc="move", o="P", at="Adyen", neo=[0, "Klarna's QR flow, not a card."], src=[["Klarna and Adyen, Sep 2024", ADYEN], ["Klarna: lululemon, Jul 2026", LULU]]),
        ]},
        {"id": "2.7", "ic": "coins", "name": "Digital money", "blurb": "KlarnaUSD on Tempo.", "div": "klarna", "rev": "grp", "products": [
            P("klarnausd", "KlarnaUSD & crypto wallet", "Klarna's first stablecoin, on Stripe and Paradigm's Tempo chain and Bridge's Open Issuance (November 2025; testnet, mainnet planned in 2026 ⚠ live status unknown), plus wallet research with Privy (December 2025).",
              s=["shop"], lc="move", st="new", ay="Nov 2025", o="P", at="Tempo, Bridge, Privy", neo=[0, "Stripe's Tempo and Bridge."],
              mc="Klarna says stablecoins can 'challenge old networks'.",
              src=[["Klarna: KlarnaUSD, Nov 2025", USDK], ["Klarna: Privy, Dec 2025", PRIVY]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every purchase: real-time underwriting on $0.5 trillion of history, scam tools in the app, Sign in with Klarna, an AI assistant and agentic protocols built with Google, cashback, and price comparison and ads from PriceRunner.",
    "tiles": [
        {"id": "3.1", "ic": "gauge", "name": "Underwriting", "blurb": "Every purchase re-scored.", "div": "bank", "rev": "paylater", "products": [
            P("underwriting", "Real-time underwriting", "Each transaction is underwritten in real time on 20 years and $0.5 trillion of history; realised losses 0.44% of GMV (Q3 2025), provisions 0.52% (Q2 2026).",
              s=["shop"], lc="borrow", o="B", neo=[0, ""], src=[["Klarna: Q1 2026 results", Q1], ["Klarna: Q3 2025 results", Q3]]),
        ]},
        {"id": "3.2", "ic": "shield-check", "name": "Fraud & identity", "blurb": "Inbox, call checks, sign-in.", "div": "klarna", "rev": "grp", "products": [
            P("inbox", "Klarna Inbox", "Every official email, SMS, push and letter mirrored in the app, so customers can check what is genuine (June 2026, all markets).",
              s=["bank"], lc="everyday", st="new", ay="Jun 2026", o="B", neo=[0, "Klarna's own."], src=[["Klarna: Inbox, Jun 2026", INBOX]]),
            P("callstatus", "Call Status Detection", "An in-app banner that shows whether a caller is really Klarna, live in Sweden, Norway, Finland and Denmark (September 2026).",
              s=["bank"], lc="everyday", st="new", ay="Sep 2026", o="B", neo=[0, "Klarna's own."],
              mc="Balance and P2P bring APP-scam exposure; Mastercard's scam scoring is not used here.",
              src=[["Klarna: Call Status Detection, Sep 2026", CALL]]),
            P("signin", "Sign in with Klarna & Express Checkout", "Password-free login and pre-filled one-click checkout with tokenised payments for merchants.",
              s=["mer", "shop"], lc="grow", o="B", neo=[0, "Klarna's own tokens."], src=[["Klarna Holding AB annual report 2025", AR25]]),
        ]},
        {"id": "3.3", "ic": "bot", "name": "AI & agentic", "blurb": "AP2, UCP, its own protocol.", "div": "klarna", "rev": "grp", "products": [
            P("assistant", "AI assistant", "An OpenAI-powered assistant for service, search, price comparison and delivery queries in 35+ languages: 2.3 million conversations in its first month, the work of 700 agents.",
              s=["shop"], lc="everyday", o="P", at="OpenAI", neo=[0, ""], src=[["Klarna: AI assistant, Feb 2024", AIASSIST], ["Klarna Holding AB annual report 2025", AR25]]),
            P("agentic", "Agentic protocols", "Supports Google's Agent Payments Protocol (October 2025) and Universal Commerce Protocol (February 2026), and launched its own Agentic Product Protocol: 100 million products and 400 million prices in 13 markets (December 2025).",
              s=["mer"], lc="grow", st="new", ay="Oct 2025", o="P", at="Google", neo=[0, "Google's protocols; no network agent programme."],
              mc="No public link to Mastercard Agent Pay, which launched with Microsoft, Braintree and Checkout.com.",
              src=[["Klarna: AP2, Oct 2025", AP2], ["Klarna: UCP, Feb 2026", UCP], ["Klarna: Agentic Product Protocol, Dec 2025", APP], ["Mastercard: Agent Pay, Apr 2025", AGENTPAY]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Cashback", "blurb": "Up to 10% in the app.", "div": "klarna", "rev": "banking", "products": [
            P("cashback", "Klarna Cashback & partner offers", "Up to 10% back on purchases through the app, paid into Klarna Balance; up to 4x cashback at featured stores for members, convertible to airline and hotel points (Flying Blue, British Airways, Hilton, IHG and others).",
              s=["shop", "mer"], lc="grow", neo=[0, ""],
              mc="Merchant-funded offers across 26 markets are the ground Mastercard's card-linked offers work on.",
              src=[["Klarna: FCA authorisation, Jul 2025", FCA], ["Klarna: memberships revamp, Aug 2026", MEMB26]]),
        ]},
        {"id": "3.5", "ic": "database", "name": "Search, ads & open banking", "blurb": "PriceRunner, Pay by Bank.", "div": "pricerunner", "rev": "grp", "products": [
            P("search", "Search & Compare and ads", "PriceRunner-powered comparison in 13 markets over 100 million products and 500 million merchant listings, with AI-driven ads, sponsored placements and affiliate and creator programmes for retailers.",
              s=["mer"], lc="grow", o="A", neo=[0, ""], src=[["Klarna: PriceRunner ruling, Jul 2026", PRICERUNNER], ["Klarna Holding AB annual report 2025", AR25]]),
            P("openbanking", "Open-banking platform", "Account access for Pay by Bank, verified mandates, personal finance and underwriting; branded Klarna Kosma in 2022–23, then folded back into Klarna.", short="Open banking (own)",
              s=["mer", "psp"], lc="move", o="B", neo=[0, "Klarna's own; a rival to Mastercard Open Finance."],
              mc="UK BNPL rules (July 2026) and EU CCD2 raise the bar on affordability data.",
              src=[["Klarna Holding AB annual report 2025", AR25], ["Tech.eu: Kosma brand dropped, Jul 2023", KOSMA]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What Klarna sells: a merchant network of 1.2 million retailers from Walmart to Southwest, everyday banking for 15.8 million customers, memberships and mobile plans, and two big markets, a fast-growing US and a slowing Germany.",
    "tiles": [
        {"id": "4.1", "ic": "store", "name": "Merchant network", "blurb": "1.2m merchants, +54%.", "div": "klarna", "rev": "paylater", "products": [
            P("merchants", "Merchants", "More than 1.2 million merchants (+54%), from Apple, Walmart (via OnePay), Uber, H&M, IKEA, Sephora, Nike and Airbnb to small shops switched on by default through PSPs.",
              s=["mer", "ent"], lc="grow", neo=[0, "Klarna's own network."], src=[["Klarna: Q2 2026 results", Q2]]),
            P("travel", "Travel & mobility", "Southwest Airlines (July 2026), TAP Air Portugal (US, Spain, France, Italy, October 2026), Lufthansa and Qatar Airways, hotels via Aven Hospitality, and Bolt rides on tokenised payments in four countries (June 2026).",
              s=["ent", "shop"], lc="grow", st="new", neo=[0, ""], src=[["Klarna: Southwest, Jul 2026", SOUTHWEST], ["Klarna: TAP, Oct 2026", TAP], ["Klarna: Bolt, Jun 2026", BOLT], ["Klarna: Q1 2026 results", Q1]]),
        ]},
        {"id": "4.2", "ic": "wallet", "name": "Everyday banking", "blurb": "15.8m banking customers.", "div": "bank", "rev": "banking", "products": [
            P("banking", "Banking customers", "15.8 million 'banking consumers' using the card, Fair Financing or savings (+101%, Q4 2025), each bringing about $107 of revenue; savings accounts in eleven European markets.",
              s=["bank"], lc="everyday", neo=[0, "Its card is on Visa."], src=[["Klarna: Q4 2025 results", Q4], ["Klarna: US Savings, Jun 2026", SAVINGS]]),
            P("ussavings", "Klarna Savings (US)", "FDIC-insured savings held at WebBank, from 3.28% APY with a member boost, no minimum and no monthly fee (June 2026).",
              s=["bank"], lc="grow", st="new", ay="Jun 2026", o="P", at="WebBank", neo=[0, ""], src=[["Klarna: US Savings, Jun 2026", SAVINGS]]),
        ]},
        {"id": "4.3", "ic": "gem", "name": "Memberships & mobile", "blurb": "2m paying members.", "div": "klarna", "rev": "banking", "products": [
            P("memberships", "Klarna memberships", "Premium and Max launched October 2025 (€17.99 and €44.99 a month) and revamped into four tiers in August 2026, with up to 1.5% cashback, lounge access, insurance and a metal Klarna Card; 2 million paying members, eight times a year earlier.",
              s=["bank"], lc="grow", st="new", ay="Oct 2025", neo=[0, "The metal card is a Visa Klarna Card."],
              mc="A paid tier with lounges and insurance is the World Elite space, run here without Mastercard.",
              src=[["Klarna: memberships, Oct 2025", MEMB25], ["Klarna: memberships revamp, Aug 2026", MEMB26], ["Klarna: Q2 2026 results", Q2]]),
            P("mobile", "Klarna Mobile", "Unlimited mobile plans in the app: US from June 2025 ($40 a month on AT&T through Gigs) and free for UK Max members from September 2026.",
              s=["bank"], lc="beyond", st="new", ay="Jun 2025", o="P", at="Gigs", neo=[0, ""], src=[["Klarna: US mobile, Jun 2025", MOBILEUS], ["Klarna: UK mobile, Sep 2026", MOBILEUK]]),
        ]},
        {"id": "4.4", "ic": "earth", "name": "Markets", "blurb": "US fastest, Germany largest.", "div": "klarna", "rev": "grp", "products": [
            P("usmarket", "United States", "About 30 million Americans a year, US GMV up 27% in Q2 2026 and 20% of 2025 GMV; served through partner banks such as WebBank until a charter is granted.",
              s=["shop"], lc="move", o="P", at="WebBank", neo=[0, "Visa card."], src=[["Klarna: Q2 2026 results", Q2], ["Klarna: US bank application, Jul 2026", USBANK], ["Klarna Holding AB annual report 2025", AR25]]),
            P("germany", "Germany & Europe", "Germany is the largest market by volume and weakened in 2026; Sweden and Germany supply most deposits; UK BNPL regulation applied from 15 July 2026.",
              s=["shop"], lc="move", st="flux", neo=[0, ""], src=[["Klarna: Q2 2026 results", Q2], ["Klarna: UK BNPL regulation, Jul 2026", UKREG]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How people and merchants reach Klarna: the Klarna app in 26 markets, payment platforms that switch Klarna on by default (Stripe, Adyen, Worldpay, Nexi, J.P. Morgan Payments, Worldline and Mastercard Gateway among them), and AI surfaces in ChatGPT, Gemini and Google Search.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Klarna app", "blurb": "26 markets, no branches.", "div": "klarna", "rev": "grp", "products": [
            P("app", "Klarna app", "The hub for Pay Later, the card, Balance, savings, P2P, cashback, search, Inbox and mobile plans, in 26 markets; no branches.",
              s=["shop", "bank"], lc="everyday", o="B", neo=[0, ""], src=[["Klarna Holding AB annual report 2025", AR25]]),
        ]},
        {"id": "5.2", "ic": "network", "name": "PSPs & acquirers", "blurb": "Klarna on by default.", "div": "klarna", "rev": "paylater", "products": [
            P("psps", "Stripe, Adyen, Worldpay & Nexi", "Default or near-default enablement: Stripe in 25 countries (January 2025), Adyen online and in-store, Worldpay as a default method alongside cards (October 2024), Nexi across Europe (February 2025).",
              s=["psp", "mer"], lc="open", o="P", at="Stripe, Adyen, Worldpay, Nexi", neo=[0, "Klarna is a method beside cards."],
              src=[["Klarna and Stripe, Jan 2025", STRIPE], ["Klarna and Worldpay, Oct 2024", WORLDPAY], ["Klarna and Nexi, Feb 2025", NEXI]]),
            P("jpm", "J.P. Morgan Payments", "Live on J.P. Morgan Payments' Commerce Platform from 6 August 2026, opening Klarna to merchants of the largest US acquirer ($2.6 trillion a year) with no integration.",
              s=["psp", "mer"], lc="open", st="new", ay="Aug 2026", o="P", at="J.P. Morgan Payments", neo=[0, ""], src=[["Klarna: J.P. Morgan Payments live, Aug 2026", JPM]]),
            P("worldline", "Worldline, Swedbank Pay & Ecommpay", "A Worldline framework to integrate and acquire Klarna online and then in store (May 2026); Swedbank Pay in the Nordics (Sweden 2026, others 2027); Ecommpay (October 2026).",
              s=["psp", "mer"], lc="open", st="new", ay="May 2026", o="P", at="Worldline, Swedbank Pay, Ecommpay", neo=[0, ""],
              src=[["Klarna and Worldline, May 2026", WORLDLINE], ["Klarna and Swedbank Pay, Apr 2026", SWEDBANK], ["Ecommpay and Klarna, Oct 2026", ECOMMPAY]]),
            P("mpgs", "Mastercard Gateway", "Klarna Pay Later, Pay Now and Financing are offered as browser payment methods on Mastercard Gateway; Klarna carries the credit and fraud risk and pays the merchant in full ⚠ volumes and start date not public.", short="Mastercard Gateway (Klarna method)",
              s=["psp", "mer"], lc="open", o="P", at="Mastercard", neo=[3, "Mastercard's gateway distributes Klarna ⚠ volumes unknown."],
              mc="Mastercard's one public product link with Klarna: as a distributor, not a network.",
              src=[["Mastercard Developers: Klarna Pay Later on Gateway", MPGS]]),
        ]},
        {"id": "5.3", "ic": "sparkles", "name": "AI surfaces", "blurb": "ChatGPT, Gemini, Search.", "div": "klarna", "rev": "grp", "products": [
            P("chatgpt", "Klarna in ChatGPT", "The Klarna Shopping Search app in ChatGPT (May 2026), on Klarna's Product Search MCP server over 100 million products and 400 million listings in 13 markets.",
              s=["shop", "mer"], lc="grow", st="new", ay="May 2026", o="P", at="OpenAI", neo=[0, ""], src=[["Klarna: ChatGPT app, May 2026", CHATGPT]]),
            P("gemini", "Klarna in Gemini & Google Search", "Klarna's pay-in-four and financing at checkout in the Gemini app and Google Search (AI Mode) through Google Pay in the US, built on UCP (May 2026).",
              s=["shop"], lc="move", st="new", ay="May 2026", o="P", at="Google", neo=[0, "Through Google Pay."], src=[["Klarna: Gemini and Search, May 2026", GEMINI]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Klarna", "blurb": "A Visa card, a gateway listing.", "products": [
        P("mcatklarna", "Mastercard at Klarna", "Every Klarna card found, from the 2021 German debit card to the 2025 Klarna Card in 16 countries, runs on Visa, which invested in Klarna in 2017. Mastercard appears at the edges: shoppers fund Pay Now and repayments with Mastercard cards ⚠, and Mastercard Gateway lists Klarna as a payment method. No Mastercard network agreement, agentic, fraud or open-finance deal was found.",
          s=["shop"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Klarna and Visa: card pilot, Jun 2025", VISAPILOT], ["Klarna and Visa, Jun 2017", VISA2017], ["Mastercard Developers: Klarna Pay Later on Gateway", MPGS]]),
    ]},
    {"id": "pillar-market", "name": "BNPL & digital banking", "blurb": "Regulation, rivals, agents.", "products": [
        P("market", "The market", "UK BNPL regulation from 15 July 2026 (Section 75, Ombudsman access); Affirm, Afterpay and PayPal Pay Later as rivals; card networks offering instalments and multi-mode credentials; agentic checkout protocols from Google, OpenAI, Visa and Mastercard.",
          s=["shop"], div="grp", rev="grp", src=[["Klarna: UK BNPL regulation, Jul 2026", UKREG], ["Mastercard: Agent Pay, Apr 2025", AGENTPAY]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
