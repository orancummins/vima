"""Google's layers, areas and products, read through payments, as at 17 October 2026 (see page_data.py for the format).

Figures are Alphabet's own unless a source says otherwise: the Q2 2026 results (22 July 2026), the Q4 2025
results (4 February 2026) and the FY2025 10-K, with Google's blogs and developer pages, Axis Bank, NPCI data
via the press, the CFPB, PayPal and Mastercard for the payments products. Q3 2026 results are due in late
October. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it,
2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q2 = "https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000066/googexhibit991q22026.htm"
Q4 = "https://s206.q4cdn.com/479360582/files/doc_financials/2025/q4/2025q4-alphabet-earnings-release.pdf"
TENK = "https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm"
MCAP = "https://companiesmarketcap.com/alphabet-google/marketcap/"
AP2 = "https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol"
UCP = "https://www.theregister.com/2026/01/12/google_gemini_agentic_ai_shopping_protocol/"
CART = "https://blog.google/products-and-platforms/products/shopping/google-shopping-cart/"
MCUCP = "https://www.mastercard.com/content/mccom/global/en/news-and-trends/stories/2026/agentic-commerce-rules-of-the-road.html"
MA10K = "https://www.sec.gov/Archives/edgar/data/1141391/000114139126000013/ma-20251231.htm"
FLEX = "https://www.axis.bank.in/about-us/press-releases/google-pay-and-axis-bank-launch-flex"
UPISHARE = "https://currentaffairs.adda247.com/top-10-upi-apps-in-india-by-market-share-in-2026/amp/"
DUOPOLY = "https://www.outlookbusiness.com/economy-and-policy/phonepe-google-pay-combined-upi-market-share-drops-below-80-for-first-time"
MCINDIA = "https://www.electronicpaymentsinternational.com/news/mastercard-google-pay-drive-tokenisation-for-card-payments-in-india"
VISAINDIA = "https://www.easternmirrornagaland.com/google-pay-rolls-out-nfc-based-tokenised-card-payment-in-india"
CFPBW = "https://files.consumerfinance.gov/f/documents/cfpb_gpc-withdrawal_2025-05.pdf"
CFPBO = "https://www.consumerfinance.gov/about-us/newsroom/cfpb-orders-federal-supervision-of-google-following-contested-designation"
BNPL = "https://developers.google.com/pay/api/android/guides/resources/bnpl"
KLARNA = "https://www.paymentsdive.com/news/klarna-google-join-forces-BNPL-digital-wallets-google-pay/751483/"
WALLETIO = "https://developers.googleblog.com/en/explore-the-latest-updates-google-wallet-io-25/"
MONEY2020 = "https://blockchain.news/news/google-wallet-digital-id-payment-expansion"
CAPONE = "https://www.capitalone.com/about/newsroom/virtual-cards-on-chrome/"
PAYPAL = "https://newsroom.paypal-corp.com/2025-09-17-Google-and-PayPal-Forge-Multiyear-Partnership-to-Revolutionize-Commerce"
VISATAP = "https://developer.visa.com/use-cases/trusted-agent-protocol"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "scale · people · licences", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Alphabet's $402.8 billion of revenue in 2025, a payments team inside Google, the Google Payment companies that hold the licences, and very large AI bets.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & results", "blurb": "$402.8bn in 2025.", "div": "grp", "rev": "grp", "products": [
            P("results", "Revenue & segments", "Revenue of $402.8 billion in 2025 (+15%), the first year above $400 billion, with operating income of $129.0 billion; Q2 2026 revenue of $119.8 billion (+24%), Google Services $94.5 billion and Google Cloud $24.8 billion (+82%). Market value about $4.1 trillion in October 2026; 198,933 staff at 30 June 2026. Payments revenue is not reported separately.",
              s=["biz"], neo=[0, ""], src=[["Alphabet: Q2 2026 results", Q2], ["Alphabet: Q4 2025 results", Q4], ["CompaniesMarketCap: Alphabet, Oct 2026", MCAP]]),
        ]},
        {"id": "1.2", "ic": "users-round", "name": "Leadership", "blurb": "Pichai; Parikh for payments.", "div": "grp", "rev": "grp", "products": [
            P("leadership", "Executives in payments and commerce", "Sundar Pichai (CEO of Alphabet and Google), Stavan Parikh (VP/GM Payments), Vidhya Srinivasan (VP/GM Ads and Commerce), Rao Surapaneni (VP/GM, Google Cloud business applications) and Sharath Bulusu (Google Pay product, India). Anat Ashkenazi as CFO and Philipp Schindler as Chief Business Officer are from prior knowledge ⚠.",
              s=["biz"], neo=[0, ""], src=[["Alphabet: Q2 2026 results", Q2], ["Google Cloud: AP2, Sep 2025", AP2], ["Google: Universal Cart, May 2026", CART]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Licences & regulation", "blurb": "Google Payment Corp.", "div": "pay", "rev": "services", "products": [
            P("entities", "Google Payment entities", "Google Payment Corp. in the US, Google Payment Ireland and Google Payment Lithuania for e-money in Europe, and Google India Digital Services for UPI ⚠ entity list from prior knowledge.",
              s=["shop", "mer"], neo=[0, ""], src=[["CFPB: GPC order withdrawn, May 2025", CFPBW]]),
            P("cfpb", "CFPB supervision, ordered and withdrawn", "The CFPB ordered federal supervision of Google Payment Corp. in late 2024; Google sued. The order was withdrawn on 7 May 2025 because the US Google Pay peer-to-peer app had closed in June 2024.",
              s=["shop"], st="retired", neo=[0, ""], src=[["CFPB: supervision order", CFPBO], ["CFPB: GPC order withdrawn, May 2025", CFPBW]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy & AI bets", "blurb": "Gemini, capex, PayPal.", "div": "grp", "rev": "grp", "products": [
            P("aibets", "AI investment", "Gemini app at 950 million monthly users (Q2 2026), over 325 million paid subscriptions, and capital spending of $80.6 billion in H1 2026 against 2026 guidance first set at $175–185 billion.",
              s=["dev"], st="new", neo=[0, ""], src=[["Alphabet: Q2 2026 results", Q2], ["Alphabet: Q4 2025 results", Q4]]),
            P("paypal", "PayPal partnership", "A multi-year deal (17 September 2025): PayPal checkout, Hyperwallet and Payouts in Google products, PayPal Enterprise Payments as a leading card processor for Google Cloud, Ads and Play, joint work on AP2, and PayPal rebuilding on Google Cloud.",
              s=["biz", "mer"], ay="Sep 2025", o="P", at="PayPal", neo=[0, "PayPal."],
              mc="PayPal, not a network, sits between Google's own billing and the card schemes.",
              src=[["PayPal: Google partnership, Sep 2025", PAYPAL]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Google Pay at checkout, Google Wallet at the till, network tokens, BNPL on Visa virtual cards, UPI and RuPay credit in India, AP2 for agents, and Google's own billing as a merchant.",
    "tiles": [
        {"id": "2.1", "ic": "wallet", "name": "Google Pay checkout", "blurb": "Saved cards, any network.", "div": "pay", "rev": "services", "products": [
            P("gpay", "Google Pay online and in apps", "Checkout with cards saved to a Google account, on Android apps and the web through PSPs, as network tokens or card numbers. No network split is published.",
              s=["shop", "mer"], lc="move", neo=[1, "Holds cards on every network."],
              mc="Every Mastercard card saved to Google is a token Mastercard can enrich and protect.",
              src=[["Google Pay: BNPL developer guide", BNPL]]),
            P("chromevc", "Virtual cards in Chrome and Android", "Autofill replaces the real card number with a virtual one. Launched in 2022 with Visa, American Express and Capital One; Capital One's cards work for Visa and Mastercard accounts (12 May 2022). Wider Mastercard support was promised for later in 2022 ⚠ not confirmed.",
              s=["shop"], lc="move", ay="May 2022", o="P", at="Capital One, Visa, American Express", neo=[1, "Visa and Amex first; Mastercard through Capital One ⚠."],
              src=[["Capital One: virtual cards on Chrome, May 2022", CAPONE]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Google Wallet tap to pay", "blurb": "90+ countries.", "div": "pay", "rev": "services", "products": [
            P("tap", "Tap to pay", "Contactless payments with tokenised cards in more than 90 countries and territories, and tap to pay for children under Family Link (2025). No user count is published.",
              s=["shop"], lc="move", neo=[1, "Tokens on every network."], src=[["Google Wallet: I/O 2025", WALLETIO]]),
            P("transit", "Transit", "Open-loop tokenised cards at transit gates, with season passes linked to those cards and live train status on passes (2025).",
              s=["shop"], lc="everyday", neo=[1, "Open-loop cards on every network."], src=[["Google Wallet: I/O 2025", WALLETIO]]),
        ]},
        {"id": "2.3", "ic": "key-round", "name": "Card tokens", "blurb": "MDES in India since 2021.", "div": "pay", "rev": "services", "products": [
            P("tokens", "Network tokens on Android", "Cards in Google Wallet and Google Pay are held as network tokens from each scheme's token service; Mastercard cards use MDES ⚠ outside India, from prior knowledge.",
              s=["issuer", "shop"], lc="open", neo=[1, "Mastercard cards through MDES ⚠."],
              mc="Agent Pay's agentic tokens are built on the same MDES rails.",
              src=[["Mastercard 10-K FY2025", MA10K]]),
            P("indiatokens", "Card tokens in Google Pay India", "Visa came first (21 September 2020, Axis and SBI Card, tap to pay at 2.5 million Visa locations); Mastercard followed through MDES on 22 December 2021 for tap, Bharat QR and in-app payments.",
              s=["india", "issuer"], lc="move", ay="Dec 2021", o="P", at="Mastercard, Visa", neo=[1, "Mastercard MDES since 2021, Visa since 2020."],
              src=[["EPI: Mastercard and Google Pay India, Dec 2021", MCINDIA], ["Eastern Mirror: Visa tokens, Sep 2020", VISAINDIA]]),
        ]},
        {"id": "2.4", "ic": "hand-coins", "name": "Buy now, pay later", "blurb": "Four lenders, all on Visa.", "div": "pay", "rev": "services", "products": [
            P("bnpl", "BNPL in Google Pay", "Affirm ($35–$30,000), Klarna ($35–$5,000, added 2025), Zip and Afterpay inside Google Pay in USD and GBP, with no Google fee. Each loan reaches the merchant as a virtual card on the Visa network.", short="BNPL (Visa virtual cards)",
              s=["shop", "mer"], lc="borrow", o="P", at="Affirm, Klarna, Zip, Afterpay", neo=[0, "Visa."],
              mc="Every BNPL payment in Google Pay settles as a Visa virtual card.",
              src=[["Google Pay: BNPL developer guide", BNPL], ["Payments Dive: Klarna in Google Pay", KLARNA]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "UPI in India", "blurb": "32.7% of UPI.", "div": "india", "rev": "services", "products": [
            P("upi", "Google Pay UPI", "32.7% of UPI transactions in May 2026, behind PhonePe at 46.2%; the two together fell below 80% for the first time. UPI carries more than 23 billion payments a month.", short="UPI (no card network)",
              s=["india"], lc="move", neo=[0, "UPI."], src=[["Adda247: UPI shares, May 2026", UPISHARE], ["Outlook Business: UPI duopoly, Jun 2026", DUOPOLY]]),
            P("rupaycredit", "RuPay credit cards on UPI", "RuPay credit cards linked to UPI in Google Pay. Visa and Mastercard credit cards cannot be linked to UPI.",
              s=["india"], lc="borrow", neo=[0, "RuPay."], src=[["Axis Bank: Flex, Dec 2025", FLEX]]),
        ]},
        {"id": "2.6", "ic": "bot", "name": "Agent payments", "blurb": "AP2, with Mastercard.", "div": "agents", "rev": "cloud", "products": [
            P("ap2", "Agent Payments Protocol (AP2)", "An open protocol (16 September 2025) in which signed Intent and Cart mandates prove what the user asked an agent to buy. It works with cards, real-time bank transfers and stablecoins; more than 60 launch partners, including Mastercard, American Express, JCB, UnionPay, PayPal and Coinbase. Visa was not named.",
              s=["dev", "mer"], lc="move", st="new", ay="Sep 2025", o="B", neo=[1, "Mastercard a launch partner; payment-agnostic."],
              mc="Pablo Fourez quoted at launch on verifiable credentials for consumer intent.",
              src=[["Google Cloud: AP2, Sep 2025", AP2]]),
            P("x402", "A2A x402 extension", "Stablecoin and crypto payments for agents, built with Coinbase, the Ethereum Foundation and MetaMask, alongside AP2.",
              s=["dev"], lc="move", st="new", ay="Sep 2025", o="P", at="Coinbase", neo=[0, "Stablecoins."],
              src=[["Google Cloud: AP2, Sep 2025", AP2]]),
        ]},
        {"id": "2.7", "ic": "store", "name": "Google as a merchant", "blurb": "Cloud, Ads, Play billing.", "div": "cloud", "rev": "cloud", "products": [
            P("billing", "Card acceptance for Cloud, Ads and Play", "Google bills advertisers, cloud customers and Play buyers on cards; PayPal Enterprise Payments is to be a leading processor across the three (September 2025).",
              s=["biz"], lc="everyday", o="P", at="PayPal", neo=[1, "Accepts every network."],
              src=[["PayPal: Google partnership, Sep 2025", PAYPAL]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every payment: authentication without passcodes, digital IDs in the wallet, passes and card benefits, the commerce protocols and cart for agents, and the data behind them.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Authentication", "blurb": "SPA starts with Visa.", "div": "pay", "rev": "services", "products": [
            P("spa", "Secure Payment Authentication", "Removes one-time passcodes and redirect pages after checkout in Europe: 50% less authentication time and 3% more conversions in tests. Initial partners Visa, Checkout.com and Adyen; the UK and Poland first (4 June 2026).", short="SPA (Visa first)",
              s=["shop", "mer"], lc="move", st="new", ay="Jun 2026", o="P", at="Visa, Checkout.com, Adyen", neo=[0, "Visa."],
              mc="Mastercard is not among the launch partners.",
              src=[["Blockchain.News: Google Wallet at Money20/20, Jun 2026", MONEY2020]]),
            P("directcheckout", "Google Pay direct checkout", "Wallet credentials offered on merchants' own checkout pages, live with Airwallex merchants and coming to Adyen (June 2026).",
              s=["mer"], lc="move", st="new", ay="Jun 2026", o="P", at="Airwallex, Adyen", neo=[1, "Cards on every network."],
              src=[["Blockchain.News: Google Wallet at Money20/20, Jun 2026", MONEY2020]]),
        ]},
        {"id": "3.2", "ic": "fingerprint", "name": "Digital identity", "blurb": "ID passes in the wallet.", "div": "pay", "rev": "services", "products": [
            P("idpass", "ID Pass & mobile driving licences", "US state licences since 2023, UK passport ID passes (2025), Brazil, Singapore, Taiwan, Aadhaar credentials in India (April 2026), and Spain, Italy, France, Ireland and Estonia from summer 2026 ⚠ EU list from secondary press.",
              s=["shop"], lc="open", st="new", neo=[0, ""], src=[["Google Wallet: I/O 2025", WALLETIO], ["Blockchain.News: Google Wallet at Money20/20, Jun 2026", MONEY2020]]),
            P("dcapi", "Digital Credentials API", "A W3C framework that lets apps and websites ask any wallet on the device for proof of age or identity.",
              s=["dev", "mer"], lc="open", neo=[0, ""], src=[["Google Wallet: I/O 2025", WALLETIO]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Passes, offers & benefits", "blurb": "Loyalty in the wallet.", "div": "pay", "rev": "services", "products": [
            P("passes", "Loyalty passes & offers", "Loyalty, tickets and boarding passes, with field-update alerts, nearby-pass alerts and personalised offer modules on passes (2025).",
              s=["shop", "mer"], lc="grow", neo=[0, ""], src=[["Google Wallet: I/O 2025", WALLETIO]]),
            P("benefits", "Card perks at checkout", "Universal Cart reads card perks, loyalty status and merchant offers from Google Wallet when it suggests how to pay (May 2026).",
              s=["shop", "issuer"], lc="grow", st="new", neo=[1, "Perks of any network."],
              mc="Card benefits data could make Mastercard perks visible at the moment of choice.",
              src=[["Google: Universal Cart, May 2026", CART]]),
        ]},
        {"id": "3.4", "ic": "sparkles", "name": "Agentic commerce", "blurb": "UCP, Universal Cart.", "div": "commerce", "rev": "services", "products": [
            P("ucp", "Universal Commerce Protocol (UCP)", "An open standard (11 January 2026) for agents to discover, buy and handle after-sales, co-developed with Shopify, Etsy, Wayfair, Target and Walmart and supported by Mastercard, Visa and American Express. Checkout in AI Mode and Gemini in the US, then Canada, Australia and the UK.",
              s=["mer", "dev", "shop"], lc="move", st="new", ay="Jan 2026", o="P", at="Shopify, Walmart, Target", neo=[1, "Mastercard, Visa and Amex all support it."],
              src=[["The Register: UCP, Jan 2026", UCP], ["Mastercard: joins Google on UCP, Jan 2026 ⚠", MCUCP]]),
            P("ucart", "Universal Cart", "One cart across Search, Gemini, YouTube and Gmail, watching prices and stock and paying with Google Pay; the merchant stays merchant of record. US Search and Gemini from summer 2026; AP2 to reach Gemini Spark first.",
              s=["shop"], lc="move", st="new", ay="May 2026", neo=[1, "Pays with any card in Google Wallet."],
              mc="Agent Pay tokens could carry these purchases; no live integration is public.",
              src=[["Google: Universal Cart, May 2026", CART]]),
            P("bizagent", "Business Agent & Direct Offers", "Brands chat with shoppers in Search (Lowe's, Michaels, Reebok) and place shopper-specific discounts in AI Mode (January 2026).",
              s=["mer"], lc="grow", st="new", neo=[0, ""], src=[["The Register: UCP, Jan 2026", UCP]]),
        ]},
        {"id": "3.5", "ic": "brain", "name": "Data & AI", "blurb": "Gemini; PayPal on Cloud.", "div": "cloud", "rev": "cloud", "products": [
            P("gemini", "Gemini models", "First-party models processing more than 10 billion tokens a minute through the API (Q4 2025); the Gemini app at 950 million monthly users (Q2 2026).",
              s=["dev"], lc="beyond", st="new", neo=[0, ""], src=[["Alphabet: Q4 2025 results", Q4], ["Alphabet: Q2 2026 results", Q2]]),
            P("cloudpay", "Google Cloud for payments firms", "PayPal is rebuilding its payments platform on Google Cloud (September 2025). Other payments clients were not researched ⚠.",
              s=["dev", "issuer"], lc="beyond", o="P", at="PayPal", neo=[None, "Not researched ⚠."],
              src=[["PayPal: Google partnership, Sep 2025", PAYPAL]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What Google sells: search and YouTube advertising, subscriptions, Play and devices, Google Cloud, and in India a first co-branded credit card on RuPay.",
    "tiles": [
        {"id": "4.1", "ic": "chart-column", "name": "Search & ads", "blurb": "$224.5bn in 2025.", "div": "commerce", "rev": "services", "products": [
            P("search", "Search, YouTube & network ads", "Search & other $224.5 billion, YouTube ads $40.4 billion and Google Network $29.8 billion in 2025; Search & other $63.3 billion in Q2 2026 (+17%). Shopping ads and listings feed the commerce work.",
              s=["mer"], lc="grow", neo=[0, ""], src=[["Alphabet 10-K FY2025", TENK], ["Alphabet: Q2 2026 results", Q2]]),
        ]},
        {"id": "4.2", "ic": "monitor", "name": "Subscriptions, Play & devices", "blurb": "$48.0bn in 2025.", "div": "grp", "rev": "services", "products": [
            P("play", "Play, Google One, YouTube Premium & Pixel", "$48.0 billion in 2025 and $12.9 billion in Q2 2026 (+15%), with over 325 million paid subscriptions; buyers pay with cards, carrier billing and Google Play balance ⚠ methods from prior knowledge.",
              s=["shop", "biz"], lc="everyday", neo=[1, "Accepts every network."],
              src=[["Alphabet 10-K FY2025", TENK], ["Alphabet: Q4 2025 results", Q4]]),
        ]},
        {"id": "4.3", "ic": "database", "name": "Google Cloud", "blurb": "+82% in Q2 2026.", "div": "cloud", "rev": "cloud", "products": [
            P("cloud", "Google Cloud", "$58.7 billion of revenue in 2025 and $24.8 billion in Q2 2026 (+82%) with $8.8 billion of operating income; AP2 was launched through Google Cloud.",
              s=["dev", "biz"], lc="beyond", neo=[0, ""], src=[["Alphabet 10-K FY2025", TENK], ["Alphabet: Q2 2026 results", Q2]]),
        ]},
        {"id": "4.4", "ic": "credit-card", "name": "Flex credit in India", "blurb": "RuPay, with Axis Bank.", "div": "india", "rev": "services", "products": [
            P("flex", "Google Pay Flex Axis Bank Credit Card", "Google's first co-branded credit card (17 December 2025): a digital RuPay card used through UPI, with instant 'Stars' rewards and EMIs inside Google Pay; more issuers promised.", short="Flex (RuPay)",
              s=["india"], lc="borrow", st="new", ay="Dec 2025", o="P", at="Axis Bank, NPCI", neo=[0, "RuPay."],
              mc="Google's first own card went to RuPay because only RuPay credit runs on UPI.",
              src=[["Axis Bank: Flex, Dec 2025", FLEX]]),
            P("loans", "Loans through Google Pay India", "Personal and gold loans from partner lenders in the app ⚠ prior knowledge, not re-verified.",
              s=["india"], lc="borrow", st="unconf", neo=[None, ""]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How people reach Google's payments: the Wallet app on Android, the Google Pay app in India, Chrome autofill, Gemini and AI Mode, and the PSPs that put the Google Pay button on merchants' sites.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Google Wallet app", "blurb": "Android and Wear OS.", "div": "pay", "rev": "services", "products": [
            P("walletapp", "Google Wallet", "Cards, passes, IDs and transit in one app on Android phones and watches; the separate US Google Pay app closed in June 2024.",
              s=["shop"], lc="open", neo=[1, "Holds cards on every network."], src=[["Google Wallet: I/O 2025", WALLETIO], ["CFPB: GPC order withdrawn, May 2025", CFPBW]]),
        ]},
        {"id": "5.2", "ic": "smartphone", "name": "Google Pay app in India", "blurb": "UPI first.", "div": "india", "rev": "services", "products": [
            P("gpayapp", "Google Pay (India)", "The UPI app, with RuPay credit on UPI, tokenised cards, Flex and loans; one of two apps holding 79% of UPI (May 2026). The NPCI 30% cap is due to bite at the end of 2026 ⚠.",
              s=["india"], lc="open", neo=[0, "UPI first."], src=[["Outlook Business: UPI duopoly, Jun 2026", DUOPOLY]]),
        ]},
        {"id": "5.3", "ic": "globe", "name": "Chrome & Android", "blurb": "Autofill everywhere.", "div": "pay", "rev": "services", "products": [
            P("chrome", "Chrome autofill", "Saved cards, virtual cards and BNPL options offered at any web checkout in Chrome and in Android apps.",
              s=["shop"], lc="move", neo=[1, "Cards on every network; BNPL on Visa."], src=[["Capital One: virtual cards on Chrome, May 2022", CAPONE], ["Google Pay: BNPL developer guide", BNPL]]),
        ]},
        {"id": "5.4", "ic": "sparkles", "name": "Gemini & AI Mode", "blurb": "950m Gemini users.", "div": "commerce", "rev": "services", "products": [
            P("aimode", "Gemini app & AI Mode in Search", "Agentic checkout in AI Mode and the Gemini app for US shoppers since January 2026, with Universal Cart from summer 2026 and AP2 arriving through Gemini Spark.",
              s=["shop"], lc="open", st="new", neo=[None, "Network role not public."], src=[["The Register: UCP, Jan 2026", UCP], ["Google: Universal Cart, May 2026", CART]]),
        ]},
        {"id": "5.5", "ic": "plug", "name": "PSPs & partners", "blurb": "Adyen, Airwallex, Shopify.", "div": "pay", "rev": "services", "products": [
            P("psps", "Google Pay through PSPs", "Merchants add Google Pay through processors such as Adyen, Checkout.com and Airwallex, and UCP checkout through Shopify and large retailers.",
              s=["mer"], lc="open", o="P", at="Adyen, Checkout.com, Airwallex, Shopify", neo=[1, "Cards on every network."],
              src=[["Blockchain.News: Google Wallet at Money20/20, Jun 2026", MONEY2020], ["The Register: UCP, Jan 2026", UCP]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Google", "blurb": "Tokens, AP2, UCP.", "products": [
        P("mcatgoogle", "Mastercard at Google", "Mastercard cards are tokenised in Google Wallet and Google Pay (MDES in India since December 2021), and Mastercard was a launch partner of AP2 (September 2025) and backs UCP (January 2026). Where Google has picked one network, it has picked Visa: BNPL virtual cards, the first India tokens and Europe's Secure Payment Authentication. Google's own card in India is on RuPay.",
          s=["shop"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["EPI: Mastercard and Google Pay India, Dec 2021", MCINDIA], ["Google Cloud: AP2, Sep 2025", AP2], ["Google Pay: BNPL developer guide", BNPL]]),
    ]},
    {"id": "pillar-market", "name": "Agentic commerce", "blurb": "Protocols, tokens, stablecoins.", "products": [
        P("market", "The market", "Agent protocols compete: Google's AP2 and UCP, Visa's Trusted Agent Protocol (October 2025), and Mastercard's Agent Pay, live for all US cardholders in 2025 with a global launch scheduled for early 2026; stablecoins come in through x402.",
          s=["dev"], div="grp", rev="grp", src=[["Mastercard 10-K FY2025", MA10K], ["Visa: Trusted Agent Protocol", VISATAP], ["Google Cloud: AP2, Sep 2025", AP2]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
