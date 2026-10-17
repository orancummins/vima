"""Adyen's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are Adyen's own unless a source says otherwise: the H1 2026 shareholder letter (13 August 2026), the
H2 2025 letter (12 February 2026), the Q1 2026 update and the 2025 Annual Report, with Adyen's product and docs
pages and Mastercard and Visa releases. The Q3 2026 update is due on 28 October. ``neo`` is the Mastercard lens:
[depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1 = "https://investors.adyen.com/financials/h1-2026-c2a1a"
H2 = "https://investors.adyen.com/financials/h2-2025-4r9rc"
Q1 = "https://investors.adyen.com/financials/q1-2026-4jxrap"
AR = "https://investors.adyen.com/financials/2025"
IR = "https://investors.adyen.com/"
CLOSE = "https://www.adyen.com/press-and-media/adyen-closes-talonone-and-orb-acquisitions-announces-leadership-updates"
CFO = "https://www.adyen.com/press-and-media/adyen-cfo-ethan-tandowsky-to-step-down-to-pursue-opportunity-outside-fintech"
INVDAY = "https://www.adyen.com/press-and-media/adyen-hosts-investor-day-2025-in-amsterdam"
AGENTIC = "https://www.adyen.com/press-and-media/adyen-agentic"
AP4M = "https://investor.mastercard.com/investor-news/investor-news-details/2026/Mastercard-Launches-Agent-Pay-for-Machines-to-Unlock-Super-Fast-Always-On-Payments/default.aspx"
MC2030 = "https://investor.mastercard.com/investor-news/investor-news-details/2024/Mastercard-Reinvents-Checkout-With-Password-and-Number-Free-Payments/default.aspx"
MCTRUST = "https://investor.mastercard.com/investor-news/investor-news-details/2026/Mastercard-Advances-Agentic-Commerce-With-New-Trust-and-Intelligence-Services/default.aspx"
VISATAP = "https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.21716.html"
C2P = "https://www.adyen.com/en_GB/press-and-media/click-to-pay"
C2PDOCS = "https://docs.adyen.com/payment-methods/cards/click-to-pay"
TOKENS = "https://docs.adyen.com/online-payments/network-tokenization/"
ISSDOCS = "https://docs.adyen.com/issuing/"
ISSUING = "https://www.adyen.com/issuing"
UPLIFT = "https://www.adyen.com/uplift"
RISK = "https://www.adyen.com/risk-management"
CAPITAL = "https://www.adyen.com/capital"
ACCOUNTS = "https://www.adyen.com/accounts"
PAYOUTS = "https://docs.adyen.com/payouts/payout-service/pay-out-to-cards/"
METHODS = "https://docs.adyen.com/payment-methods/"
ABOUT = "https://www.adyen.com/about"
YAHOO = "https://finance.yahoo.com/quote/ADYEN.AS"
POP = "https://www.mastercard.com/us/en/news-and-trends/press/2025/october/Mastercard-Payment-Optimization-Platform-uses-the-power-of-data-to-drive-more-approvals.html"
MSI = "https://www.mastercard.com/br/pt/news-and-trends/press/2024/august/adyen-amplia-el-acceso-a-meses-sin-intereses-para-grandes-empresas.html"
VI = "https://developer.mastercard.com/merchant-cloud/documentation/tutorials-and-guides/ai-revolution/14/"
TSAO = "https://www.bankingdive.com/news/adyen-names-interim-cfo-tsao/824485/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "volume · licences · one platform", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: €1.39 trillion of volume in 2025 and €803.8 billion in the first half of 2026, a Dutch banking licence with US and UK branches, co-CEOs and an interim CFO, and one platform built in-house.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & results", "blurb": "€803.8bn in H1 2026.", "div": "adyen", "rev": "grp", "products": [
            P("results", "Volume & earnings", "€803.8 billion processed in H1 2026 (+24%), net revenue of €1,302.9 million (+19%), EBITDA margin 49% and a take rate of 16.2 basis points; €1,394.3 billion and €2,364.2 million in 2025 (53% margin). Market value about €29.9 billion at 16 October 2026 ⚠ own calculation; S&P rating A-.",
              s=["ent"], neo=[0, ""], src=[["Adyen: H1 2026 letter", H1], ["Adyen: H2 2025 letter", H2], ["Yahoo Finance: ADYEN.AS", YAHOO]]),
        ]},
        {"id": "1.2", "ic": "badge-check", "name": "Licences", "blurb": "A Dutch bank, branches abroad.", "div": "adyen", "rev": "grp", "products": [
            P("licences", "Banking licences", "A credit institution licensed by De Nederlandsche Bank and passported across the EEA, a US federal branch, a UK branch, a Brazilian acquiring licence, a Bank of England reserve account and a UAE Category II licence (2026). No full list of acquiring licences is published ⚠.",
              s=["ent"], neo=[0, ""], src=[["Adyen: H1 2026 letter", H1], ["Adyen: Annual Report 2025", AR]]),
        ]},
        {"id": "1.3", "ic": "scale", "name": "Leadership", "blurb": "Co-CEOs, interim CFO.", "div": "adyen", "rev": "grp", "products": [
            P("leadership", "Management", "Co-founder and co-CEO Pieter van der Does and co-CEO Ingo Uytdehaage; Hwa Tsao interim CFO from 1 September 2026 after Ethan Tandowsky left; Gayathri Rajan CPO from 1 July 2026; Roelant Prins, Mariëtte Swart, Brooke Nayden and Tom Adams. 5,020 staff at 30 June 2026.",
              s=["ent"], st="flux", neo=[0, ""], src=[["Adyen: acquisitions and leadership, Jul 2026", CLOSE], ["Adyen: CFO to step down, May 2026", CFO], ["Banking Dive: interim CFO, Jul 2026", TSAO]]),
            P("board", "Supervisory Board", "Chaired by Piero Overmars, with Herna Verhagen nominated in January 2026 to succeed him ⚠ AGM outcome not verified.",
              s=["ent"], neo=[0, ""], src=[["Adyen: Annual Report 2025", AR]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Platform & strategy", "blurb": "Margin above 55% by 2028.", "div": "adyen", "rev": "grp", "products": [
            P("platform", "One platform", "One platform built in-house: 99.9999% uptime over Black Friday and Cyber Monday 2025, with 837 million transactions; data centres are the main capital spend (about 7% of revenue in 2026).",
              s=["ent"], o="B", neo=[0, ""], src=[["Adyen: H2 2025 letter", H2], ["Adyen: H1 2026 letter", H1]]),
            P("strategy", "Strategy & targets", "'The complete financial operating system for modern commerce', built on one platform, its own licences and Dynamic Identification; EBITDA margin above 55% by 2028 and about 20% revenue growth after 2026; 2026 guidance raised to 21–23% (constant currency) in August.",
              s=["ent"], st="new", neo=[0, ""], src=[["Adyen: Investor Day, Nov 2025", INVDAY], ["Adyen: H1 2026 letter", H1]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Five ways money moves: card acquiring on direct connections, routing to local schemes and debit networks, issuing on Mastercard and Visa, payouts and Intelligent Money Movement, and local methods from Pix and UPI to wallets and BNPL.",
    "tiles": [
        {"id": "2.1", "ic": "store", "name": "Card acquiring", "blurb": "Visa, Mastercard, Amex direct.", "div": "adyen", "rev": "digital", "products": [
            P("acquiring", "Card acquiring", "Direct connections to Visa, Mastercard and American Express, and its own acquiring rails in India (2025) with RuPay.",
              s=["ent", "uc"], lc="move", neo=[1, "Accepts every network."], src=[["Adyen: Annual Report 2025", AR]]),
            P("installments", "Card instalments", "Credit-card instalments, including Mexico's meses sin intereses, which a Mastercard release says Adyen widened for large businesses (August 2024 ⚠ title only).",
              s=["ent", "shop"], lc="borrow", ay="Aug 2024", neo=[1, "Mastercard announced it ⚠; all networks."], src=[["Mastercard: meses sin intereses, Aug 2024", MSI], ["Adyen: payment methods", METHODS]]),
        ]},
        {"id": "2.2", "ic": "network", "name": "Local schemes & routing", "blurb": "eftpos, US debit, CB.", "div": "adyen", "rev": "uc", "products": [
            P("localschemes", "Local card schemes", "RuPay in India, direct Cartes Bancaires membership and STET clearing in France (2026), and eftpos routing in Australia for 92 customers, saving AU$0.14 a transaction.",
              s=["ent", "uc"], lc="move", st="new", neo=[0, "Local schemes."],
              mc="Routing to local schemes competes with Mastercard on cost.",
              src=[["Adyen: H1 2026 letter", H1], ["Adyen: Annual Report 2025", AR]]),
            P("usdebit", "US debit routing", "Routes co-badged US debit over Accel, Maestro USA, NYCE, PULSE and STAR, tokens included: 9.2% cost savings and 25 basis points more approvals, about $14.5 million saved for customers in 2025.",
              s=["ent", "uc"], lc="move", neo=[1, "Maestro USA among the networks."], src=[["Adyen: network tokens", TOKENS], ["Adyen: Annual Report 2025", AR]]),
        ]},
        {"id": "2.3", "ic": "credit-card", "name": "Issuing", "blurb": "8x in 2025.", "div": "adyen", "rev": "platforms", "products": [
            P("issuing", "Adyen Issuing", "Virtual and physical cards on Mastercard and Visa in the EEA, UK and US since 2019; volume up eight times in 2025, with Spendesk and BILL among customers. The product page shows only a Visa logo.", short="Issuing (Mastercard and Visa)",
              s=["plat"], lc="move", neo=[1, "Mastercard and Visa."],
              mc="Adyen's fastest-growing product; the network split is not disclosed.",
              src=[["Adyen: Issuing docs", ISSDOCS], ["Adyen: Issuing", ISSUING], ["Adyen: H2 2025 letter", H2]]),
            P("chargecards", "Charge cards with Navan", "Charge cards built with Navan, whose issuing volume grew more than five times in H2 2025 across the US, EU and UK.",
              s=["travel"], lc="borrow", st="new", o="P", at="Navan", neo=[None, "Network not disclosed ⚠."], src=[["Adyen: H2 2025 letter", H2]]),
            P("virtualcards", "Virtual supplier cards", "One virtual card per invoice for paying suppliers.",
              s=["sme", "plat"], lc="move", neo=[1, "Issued on Mastercard or Visa."], src=[["Adyen: Accounts", ACCOUNTS]]),
        ]},
        {"id": "2.4", "ic": "send", "name": "Payouts & money movement", "blurb": "CashOut, IMM.", "div": "adyen", "rev": "platforms", "products": [
            P("cardpayouts", "Payouts to cards", "Payouts to Mastercard and Visa cards, usually within 30 minutes, in the EEA, US and UK; the docs do not say which network service carries them ⚠.",
              s=["plat", "sme"], lc="move", neo=[1, "Mastercard and Visa cards; rail not named ⚠."],
              mc="Mastercard Move could carry CashOut and IMM.",
              src=[["Adyen: payouts to cards", PAYOUTS]]),
            P("bankpayouts", "Bank payouts", "Payouts over SEPA, ACH and BACS, up about 40% in 2025, with 'tens of billions of euros' a month.",
              s=["plat"], lc="move", neo=[0, "Bank rails."], src=[["Adyen: Accounts", ACCOUNTS], ["Adyen: Annual Report 2025", AR]]),
            P("cashout", "CashOut", "Instant payouts around the clock, a run rate of several hundred million euros within nine months in pilot; Vagaro is an early user.",
              s=["sme"], lc="move", st="new", neo=[None, "Rails not disclosed."], src=[["Adyen: H2 2025 letter", H2], ["Adyen: Annual Report 2025", AR]]),
            P("imm", "Intelligent Money Movement", "Money in, held and out in one flow for marketplaces, travel, mobility and insurance (launched H1 2026), with Etsy, Expedia and Vinted; aiming at near-real-time travel settlement against four days or more today.",
              s=["travel", "plat"], lc="move", st="new", neo=[None, "Rails not disclosed."], src=[["Adyen: H1 2026 letter", H1], ["Adyen: H2 2025 letter", H2]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Local methods", "blurb": "Pix, UPI, Wero, wallets.", "div": "adyen", "rev": "digital", "products": [
            P("paybybank", "Pay by Bank & European methods", "Pay by Bank in Europe and the US, iDEAL | Wero, Bancontact and Bizum.",
              s=["ent", "shop"], lc="move", neo=[0, "Account-to-account."], src=[["Adyen: payment methods", METHODS], ["Adyen: Annual Report 2025", AR]]),
            P("pix", "Pix", "Pix, Pix Recurring and Pix Open Finance in Brazil (2025); LATAM revenue up 43% in H1 2026.",
              s=["ent", "shop"], lc="move", st="new", neo=[0, "Pix."], src=[["Adyen: Annual Report 2025", AR], ["Adyen: H1 2026 letter", H1]]),
            P("upi", "UPI", "UPI in India (2025).",
              s=["ent", "shop"], lc="move", st="new", neo=[0, "UPI."], src=[["Adyen: Annual Report 2025", AR]]),
            P("wallets", "Wallets", "Apple Pay, Google Pay, PayPal, Alipay+, PayPay (Japan, 2025) and Cash App Pay.",
              s=["shop"], lc="move", neo=[1, "Card-funded wallets on every network."], src=[["Adyen: payment methods", METHODS]]),
            P("bnpl", "Buy now, pay later", "Klarna, Afterpay and Clearpay, Affirm, Atome, Alma and others.",
              s=["shop"], lc="borrow", o="P", at="Klarna, Affirm and others", neo=[0, ""], src=[["Adyen: payment methods", METHODS]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every payment: Dynamic Identification and risk, network tokens and Click to Pay, Uplift's optimisation and Mastercard's optimisation platform, Talon.One loyalty and Orb billing, and agentic commerce.",
    "tiles": [
        {"id": "3.1", "ic": "fingerprint", "name": "Identity & risk", "blurb": "Dynamic Identification.", "div": "adyen", "rev": "digital", "products": [
            P("dynamicid", "Dynamic Identification", "A behavioural identity layer from 'trillions of interactions' (2025), recognising about 95% of some 400 million shoppers over Black Friday weekend; it powers Uplift, policy-abuse detection and agentic trust.",
              s=["ent", "shop"], lc="open", st="new", neo=[0, "Adyen's own."], src=[["Adyen: H2 2025 letter", H2]]),
            P("risk", "Protect & Authenticate", "AI risk scoring with backtesting and A/B tests, 3DS and adaptive authentication, and policy-abuse detection (one shopper had about 70% of purchases refunded).",
              s=["ent"], lc="everyday", neo=[0, "Adyen's own models."], src=[["Adyen: risk management", RISK], ["Adyen: H2 2025 letter", H2]]),
        ]},
        {"id": "3.2", "ic": "key-round", "name": "Tokens & Click to Pay", "blurb": "Recurring only on Mastercard.", "div": "adyen", "rev": "digital", "products": [
            P("tokens", "Network tokens", "Adyen-managed or merchant-managed tokens from Visa, Mastercard and American Express, with sharing and forwarding; the docs do not name MDES ⚠.",
              s=["ent"], lc="grow", neo=[1, "Visa, Mastercard and Amex tokens."], src=[["Adyen: network tokens", TOKENS]]),
            P("clicktopay", "Click to Pay", "Embedded in checkout in every available market with Mastercard and Visa (March 2023), processed as token transactions at no extra fee; recurring payments only on Mastercard. Mastercard named Adyen a Click to Pay enabler (November 2024).", short="Click to Pay",
              s=["shop", "ent"], lc="grow", ay="Mar 2023", o="P", at="Mastercard, Visa", neo=[1, "Mastercard and Visa; recurring only on Mastercard."],
              src=[["Adyen: Click to Pay, Mar 2023", C2P], ["Adyen: Click to Pay docs", C2PDOCS], ["Mastercard: number-free checkout, Nov 2024", MC2030]]),
        ]},
        {"id": "3.3", "ic": "gauge", "name": "Optimisation", "blurb": "Uplift +0.9 points.", "div": "adyen", "rev": "digital", "products": [
            P("uplift", "Adyen Uplift", "AI that balances conversion, fraud and cost: an average of 0.9 points more conversion by the end of H1 2026.",
              s=["ent"], lc="grow", neo=[0, "Adyen's own."], src=[["Adyen: Uplift", UPLIFT], ["Adyen: H1 2026 letter", H1]]),
            P("optimize", "Optimize & Intelligent Payment Routing", "Routing that saved an average 9.62% on scheme fees and interchange, with 42% fewer false positives in 2025.",
              s=["ent", "uc"], lc="grow", neo=[0, "Adyen's own; cuts scheme fees."], src=[["Adyen: Annual Report 2025", AR]]),
            P("personalize", "Personalize", "Piloted in 2025: up to 6% more conversion and 3% lower cost, partly by steering shoppers to cheaper methods ⚠ inference.",
              s=["ent"], lc="grow", st="new", neo=[0, "Steers to cheaper methods ⚠."], src=[["Adyen: H2 2025 letter", H2]]),
            P("pop", "Mastercard Payment Optimization Platform", "Adyen named as a roll-out partner with Worldpay and others (October 2025) ⚠ search snippet only.", short="Payment Optimization Platform",
              s=["ent"], lc="grow", st="unconf", ay="Oct 2025", o="P", at="Mastercard", neo=[3, "Mastercard's own platform ⚠."], src=[["Mastercard: Payment Optimization Platform, Oct 2025", POP]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Loyalty & billing", "blurb": "Talon.One, Orb.", "div": "talon", "rev": "uc", "products": [
            P("talonone", "Talon.One", "A promotions and loyalty engine for more than 300 brands, bought for €750 million (closed 1 July 2026).",
              s=["uc", "ent"], lc="grow", st="new", ay="Jul 2026", o="A", neo=[0, ""],
              mc="Mastercard offers could run through Talon.One across 838,000 terminals ⚠ speculative.",
              src=[["Adyen: acquisitions and leadership, Jul 2026", CLOSE], ["Adyen: H1 2026 letter", H1]]),
            P("orb", "Orb", "Usage-based billing for AI and software companies, bought for $335 million (closed 1 July 2026).",
              s=["ent"], lc="grow", st="new", ay="Jul 2026", o="A", neo=[0, ""],
              mc="AI micropayments could ride Agent Pay for Machines.",
              src=[["Adyen: acquisitions and leadership, Jul 2026", CLOSE]]),
        ]},
        {"id": "3.5", "ic": "bot", "name": "Agentic commerce", "blurb": "Mastercard a launch partner.", "div": "na", "rev": "digital", "products": [
            P("adyenagentic", "Adyen Agentic", "Agentic Feed, Cart and Payments (16 June 2026) with token portability and the merchant of record kept, supporting Meta AI checkout, UCP, AP2 and ACP; Amex, Mastercard, Salesforce and Visa as early partners; limited availability for US enterprises.",
              s=["ent"], lc="move", st="new", ay="Jun 2026", neo=[1, "Mastercard, Visa and Amex as partners."],
              mc="Agentic tokens and Verifiable Intent could sit inside 'token portability'.",
              src=[["Adyen: Adyen Agentic, Jun 2026", AGENTIC]]),
            P("ap4m", "Mastercard Agent Pay for Machines", "One of 32 supporters at launch (10 June 2026), settling across cards, accounts and stablecoins; Adyen is also listed as a Verifiable Intent partner ⚠ undated snippet.", short="Agent Pay for Machines",
              s=["ent"], lc="move", st="new", ay="Jun 2026", o="P", at="Mastercard", neo=[3, "Mastercard Agent Pay for Machines."],
              mc="Mastercard's September 2026 agentic trust services did not name Adyen.",
              src=[["Mastercard: Agent Pay for Machines, Jun 2026", AP4M], ["Mastercard developers: Verifiable Intent", VI], ["Mastercard: agentic trust services, Sep 2026", MCTRUST]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What Adyen sells, by its three reported pillars: Digital for online merchants, Unified Commerce for online and in-store together, and Platforms for embedded payments, with accounts and capital for the businesses on them.",
    "tiles": [
        {"id": "4.1", "ic": "monitor", "name": "Digital", "blurb": "€719.7m, +13%.", "div": "adyen", "rev": "digital", "products": [
            P("digital", "Digital", "Online merchants: €719.7 million of net revenue in H1 2026 (+13%) on €427.9 billion of volume, with Google, Microsoft, Spotify, Uber and OpenAI.",
              s=["ent"], lc="everyday", neo=[1, "Accepts every network."], src=[["Adyen: H1 2026 letter", H1]]),
        ]},
        {"id": "4.2", "ic": "store", "name": "Unified Commerce", "blurb": "€417.7m, +25%.", "div": "emea", "rev": "uc", "products": [
            P("unified", "Unified Commerce", "Online and in store together: €417.7 million in H1 2026 (+25%) on €240.9 billion; in-person volume of €175.7 billion; Starbucks (943 stores), LVMH, Lufthansa and GOV.UK Pay.",
              s=["uc"], lc="everyday", neo=[1, "Accepts every network."], src=[["Adyen: H1 2026 letter", H1], ["Adyen: H2 2025 letter", H2]]),
        ]},
        {"id": "4.3", "ic": "users-round", "name": "Platforms", "blurb": "€165.5m, +37%.", "div": "na", "rev": "platforms", "products": [
            P("platforms", "Platforms", "Embedded payments: €165.5 million in H1 2026 (+37%) on €135.0 billion, 37 platforms above €1 billion and 293,000 active business customers; Toast extended to the US.",
              s=["plat", "sme"], lc="everyday", neo=[1, "Accepts every network."], src=[["Adyen: H1 2026 letter", H1]]),
        ]},
        {"id": "4.4", "ic": "landmark", "name": "Financial products", "blurb": "Accounts and Capital.", "div": "adyen", "rev": "platforms", "products": [
            P("accounts", "Business accounts", "Embedded business accounts in the US, EU and UK, with interest in the US and EU.",
              s=["sme", "plat"], lc="everyday", neo=[0, ""], src=[["Adyen: Accounts", ACCOUNTS]]),
            P("capital", "Adyen Capital", "Loans up to $100,000 in the US, UK, EU, Australia and Canada; loan volume more than doubled in 2025 and over 80% of businesses borrow again.",
              s=["sme"], lc="borrow", neo=[0, ""], src=[["Adyen: Capital", CAPITAL], ["Adyen: H2 2025 letter", H2]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How merchants reach Adyen: APIs and drop-in components, 838,000 terminals and Tap to Pay on iPhone, partners from Toast to the card networks, and 29 offices.",
    "tiles": [
        {"id": "5.1", "ic": "code-xml", "name": "APIs", "blurb": "Checkout, Transfers.", "div": "adyen", "rev": "grp", "products": [
            P("apis", "APIs & components", "The Checkout API, web Drop-in and Components, the Transfers API, and plugins such as Salesforce Commerce Cloud.",
              s=["ent", "plat"], lc="open", neo=[0, ""], src=[["Adyen: payment methods", METHODS]]),
        ]},
        {"id": "5.2", "ic": "smartphone", "name": "Terminals", "blurb": "838,000 transacting.", "div": "adyen", "rev": "uc", "products": [
            P("terminals", "Terminals & Tap to Pay", "838,000 transacting terminals (+27%), new S1E4 Pro and S1F4 Pro models (H2 2025), Tap to Pay on iPhone and Uber's airport kiosks.",
              s=["uc"], lc="open", neo=[1, "Accepts every network."], src=[["Adyen: H1 2026 letter", H1], ["Adyen: H2 2025 letter", H2]]),
            P("storeforward", "Store and Forward", "Keeps taking payments through outages; it saved more than 45,000 Starbucks transactions.",
              s=["uc"], lc="everyday", neo=[0, ""], src=[["Adyen: H2 2025 letter", H2]]),
        ]},
        {"id": "5.3", "ic": "plug", "name": "Partners", "blurb": "Toast, networks, Salesforce.", "div": "adyen", "rev": "platforms", "products": [
            P("partners", "Partners", "Toast in hospitality, Amex, Mastercard, Salesforce and Visa as agentic partners, and Globant for integration ⚠ search result only.",
              s=["plat", "ent"], lc="open", neo=[1, "Mastercard among the agentic partners."], src=[["Adyen: Adyen Agentic, Jun 2026", AGENTIC], ["Adyen: H1 2026 letter", H1]]),
        ]},
        {"id": "5.4", "ic": "earth", "name": "Regions", "blurb": "EMEA 55% of revenue.", "div": "adyen", "rev": "grp", "products": [
            P("regions", "Regions & offices", "29 offices in 21 countries; H1 2026 revenue 55% EMEA, 27% North America (+23%), 11% APAC (+23%) and 7% LATAM (+43%).",
              s=["ent"], lc="open", neo=[0, ""], src=[["Adyen: H1 2026 letter", H1], ["Adyen: Annual Report 2025", AR]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Adyen", "blurb": "In every flow, no bilateral deal.", "products": [
        P("mcatadyen", "Mastercard at Adyen", "Adyen acquires Mastercard directly, issues on it, uses its tokens and Click to Pay (recurring only on Mastercard), pays out to its cards, and backed Agent Pay for Machines and made Mastercard an Adyen Agentic partner. No bilateral agreement was found, and Visa is at parity almost everywhere: issuing, Click to Pay, its Trusted Agent Protocol and Adyen Agentic. Adyen holds Visa preferred shares from 2016, the last to be sold in 2027.",
          s=["ent"], div="adyen", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Adyen: Adyen Agentic, Jun 2026", AGENTIC], ["Visa: Trusted Agent Protocol, Oct 2025", VISATAP], ["Adyen: Annual Report 2025", AR]]),
    ]},
    {"id": "pillar-market", "name": "Enterprise acquiring", "blurb": "Agents, local rails, peers.", "products": [
        P("market", "The market", "Stripe, Checkout.com, Worldpay, Fiserv and others named beside Adyen in network releases; agentic standards from both networks; PSD3 and the EU AI Act; a delayed settlement by an unnamed scheme in October 2025 led Adyen to build liquidity buffers.",
          s=["ent"], div="adyen", rev="grp", src=[["Adyen: Annual Report 2025", AR], ["Mastercard: Agent Pay for Machines, Jun 2026", AP4M]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
