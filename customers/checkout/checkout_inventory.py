"""Checkout.com's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Checkout.com is private: figures are its own releases (FY2025 update, 24 February 2026; annualised revenue,
29 September 2026) and press. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own
product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

NEWS = "https://www.checkout.com/newsroom/"
REV26 = NEWS + "checkout-com-reaches-750m-in-annualised-net-revenue-for-2026-and-increases-profitability"
FY25 = NEWS + "checkout-com-returns-to-full-year-profitability-and-surpasses-300b-in-volume-as-it-positions-for-the-era-of-agentic-commerce"
VAL = NEWS + "checkout-com-accelerates-towards-full-year-profitability-and-announces-employee-share-buy-back-and-a-new-12bn-valuation"
US = NEWS + "checkout-com-records-triple-digit-us-growth-and-launches-new-products-to-support-merchants-across-north-america"
MALPB = NEWS + "checkout-com-goes-live-with-us-direct-acquiring-under-malpb-charter"
BLUE = "https://www.checkout.com/en-ae/news/checkout-com-acquires-blue-emi-a-licensed-issuer-of-euro-stablecoins-and-establishes-lithuania-technology-centre"
COINBASE = NEWS + "checkout-com-enables-stablecoin-acceptance-for-merchants-in-partnership-with-coinbase"
FIREBLOCKS = NEWS + "checkout-com-scales-stablecoin-settlement-for-us-merchants-in-partnership-with-fireblocks"
REMEMBER = NEWS + "checkout-com-launches-flow-remember-me-a-one-click-solution-for-global-digital-payments"
ACP = NEWS + "checkout-adopts-acp-backed-by-openai-to-power-agentic-commerce-for-enterprise-merchants"
INCIDENT = NEWS + "statement-regarding-a-legacy-system-incident"
VISAISS = NEWS + "checkout-com-and-visa-partner-to-launch-card-issuing"
VISADIRECT = NEWS + "checkout-com-becomes-the-first-acquirer-in-the-uae-to-launch-visa-direct-push-to-card-solution"
MOVE = "https://newsroom.mastercard.com/news/eemea/en/newsroom/press-releases/en/2025-1/february/checkout-com-teams-up-with-mastercard-move-to-transform-money-transfers-in-the-uae"
WHOLESALE = "https://thepaypers.com/payments-general/checkoutcom-partners-with-mastercard--1267998"
VI = "https://www.pymnts.com/mastercard/2026/mastercard-unveils-open-standard-to-verify-ai-agent-transactions/"
AP4M = "https://thepaypers.com/payments/news/mastercard-launches-agent-pay-for-machines-for-ai-commerce"
AGENTBLOG = "https://www.checkout.com/blog/mastercard-checkout-discuss-agentic-commerce-agent-pay"
CERTS = "https://www.checkout.com/legal/certificates"
IA = "https://www.checkout.com/products/intelligent-acceptance"
TOKENS = "https://www.checkout.com/products/network-tokens"
FRAUD = "https://www.checkout.com/products/fraud-detection"
TDS = "https://www.checkout.com/products/authentication-3ds"
APAC = NEWS + "checkout-com-builds-on-apac-momentum-with-71-tpv-growth"
HOME = "https://www.checkout.com/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "volume · licences · platform", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: more than $300 billion of volume in 2025 and $750 million of annualised revenue, ten acquiring licences and a new US bank charter, a founder-led company valued at $12 billion, and one platform built in-house.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & profit", "blurb": "$300bn+, back to profit.", "div": "grp", "rev": "grp", "products": [
            P("scale", "Volume & revenue", "More than $300 billion of payments in 2025 (+64%), $750 million of annualised net revenue by September 2026 (+28%), adjusted EBITDA margin above 10% in 2025 and about $150 million guided for 2026; 63 merchants above $1 billion a year.",
              s=["ent"], neo=[0, ""], src=[["Checkout.com: FY2025, Feb 2026", FY25], ["Checkout.com: $750m annualised, Sep 2026", REV26]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Licences & charter", "blurb": "Ten acquiring licences.", "div": "grp", "rev": "grp", "products": [
            P("licences", "Licences", "An FCA e-money institution (Checkout Ltd), Checkout SAS passported across the EEA, US money-transmitter licences, and licences in Australia, Singapore, Hong Kong, Japan, the UAE, Canada and Brazil: ten acquiring licences in all.",
              s=["ent"], neo=[0, ""], src=[["Checkout.com: certificates", CERTS], ["Checkout.com: $750m annualised, Sep 2026", REV26]]),
            P("malpb", "US bank charter", "A Georgia merchant-acquirer bank charter (approved 12 January 2026), live for US direct acquiring on 9 September 2026, with direct US network access.",
              s=["ent"], st="new", ay="Sep 2026", neo=[1, "Direct access to every network."],
              mc="Direct US acquiring needs network connectivity, data quality and authorisation services.",
              src=[["Checkout.com: MALPB live, Sep 2026", MALPB]]),
        ]},
        {"id": "1.3", "ic": "users-round", "name": "Ownership & leadership", "blurb": "$12bn, founder-led.", "div": "grp", "rev": "grp", "products": [
            P("ownership", "Valuation & leadership", "Founder and CEO Guillaume Pousaz; an internal $12 billion valuation for an employee buyback (September 2025), down from $40 billion in 2022 ⚠; CPO Meron Colbeci, CRO Antoine Nougué, CTO Mariano Albera; 2,300 staff in 19 offices.",
              s=["ent"], neo=[0, ""], src=[["Checkout.com: $12bn valuation, Sep 2025", VAL], ["Checkout.com: $750m annualised, Sep 2026", REV26]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Platform", "blurb": "One stack, 2.5bn cards vaulted.", "div": "cko", "rev": "grp", "products": [
            P("platform", "Unified platform", "One in-house platform for acceptance, issuing and payouts, 99.999% uptime in 2025, a card vault of more than 2.5 billion cards, and AI writing 2.7 million lines of code a month.",
              s=["ent"], o="B", neo=[0, ""], src=[["Checkout.com: FY2025, Feb 2026", FY25]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "US, beyond acquiring.", "div": "grp", "rev": "grp", "products": [
            P("strategy", "Strategy & acquisitions", "Grow in the US (now 20% of volume) and beyond acquiring into issuing, payouts, accounts and platforms; acquisitions of ProcessOut and Pin Payments (2020), ubble (2022) and Blue EMI, a euro-stablecoin issuer (January 2026).",
              s=["ent"], neo=[0, ""], src=[["Checkout.com: US growth, Sep 2026", US], ["Checkout.com: Blue EMI, Jan 2026", BLUE]]),
            P("incident", "2025 security incident", "Attackers reached a legacy cloud file store holding old merchant onboarding documents (November 2025); no payment data was affected, and Checkout.com refused the ransom.",
              s=["ent"], neo=[0, ""], src=[["Checkout.com: legacy system incident, Nov 2025", INCIDENT]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: acquiring in 50 countries and now directly in the US, more than 50 local methods and wallets, issuing on both networks, payouts on Mastercard Move and Visa Direct, stablecoin acceptance and settlement, and a business account.",
    "tiles": [
        {"id": "2.1", "ic": "store", "name": "Acquiring", "blurb": "50 countries, US direct.", "div": "cko", "rev": "accept", "products": [
            P("acquiring", "Global acquiring", "Local acquiring in more than 50 countries and 150 currencies, direct in Canada (2025), Japan and, since September 2026, the US, where volume grew more than 120% this year.",
              s=["ent", "mkt"], lc="move", neo=[1, "Accepts every network."], src=[["Checkout.com: US growth, Sep 2026", US], ["Checkout.com", HOME]]),
        ]},
        {"id": "2.2", "ic": "wallet", "name": "Payment methods", "blurb": "50+ methods, wallets, BNPL.", "div": "cko", "rev": "accept", "products": [
            P("apms", "Local methods, wallets & BNPL", "More than 50 methods (BLIK, TWINT, Swish, Tabby, Octopus) with alternative-method volume up 104% in 2025, Apple Pay and Google Pay, and Klarna and other BNPL partners.",
              s=["ent", "shop"], lc="move", neo=[0, "Off the card networks."], src=[["Checkout.com: FY2025, Feb 2026", FY25]]),
        ]},
        {"id": "2.3", "ic": "credit-card", "name": "Issuing", "blurb": "$5bn run rate.", "div": "cko", "rev": "move", "products": [
            P("issuing", "Card issuing", "Issuing since 2023, a dual-network issuer in the UK and Europe, expanding to the UAE and US in 2026; a $5 billion run rate in the fourth quarter of 2025.",
              s=["mkt", "fin"], lc="move", neo=[1, "Both networks."], src=[["Checkout.com: Flow Remember Me and issuing, Oct 2025", REMEMBER], ["Checkout.com: FY2025, Feb 2026", FY25]]),
            P("wholesale", "Mastercard Wholesale virtual cards", "Virtual cards for online travel agents on the Mastercard Wholesale Program (May 2024), combining Checkout.com's acquiring and issuing; Holiday Extras first.", short="Mastercard Wholesale",
              s=["travel"], lc="move", ay="May 2024", o="P", at="Mastercard", neo=[3, "Mastercard's own programme."],
              src=[["The Paypers: Checkout.com and Mastercard, May 2024", WHOLESALE]]),
            P("visatravel", "Visa travel issuing", "Card issuing for travel and hospitality merchants with Visa (July 2025), highlighted on Visa's earnings call.",
              s=["travel"], lc="move", ay="Jul 2025", o="P", at="Visa", neo=[0, "Visa."], src=[["Checkout.com and Visa, Jul 2025", VISAISS]]),
        ]},
        {"id": "2.4", "ic": "send", "name": "Payouts", "blurb": "Move and Visa Direct.", "div": "cko", "rev": "move", "products": [
            P("move", "Pay-to-Card on Mastercard Move", "Payouts to Mastercard cards in the UAE (February 2025; gig pay, insurance, wallet cash-outs) and Canada (September 2026).", short="Mastercard Move",
              s=["mkt", "fin"], lc="move", ay="Feb 2025", o="P", at="Mastercard", neo=[3, "Mastercard Move."],
              mc="Not yet in the US, where RTP and ACH payouts just launched.",
              src=[["Mastercard: Checkout.com and Move, Feb 2025", MOVE], ["Checkout.com: US growth, Sep 2026", US]]),
            P("payouts", "Visa Direct, RTP & ACH", "First UAE acquirer on Visa Direct (February 2025) with more than a million account-funding transactions a month, Canada on Visa Direct, and RTP and ACH payouts in the US (2026).",
              s=["mkt", "fin"], lc="move", o="P", at="Visa", neo=[0, "Visa and bank rails."], src=[["Checkout.com: Visa Direct UAE, Feb 2025", VISADIRECT], ["Checkout.com: US growth, Sep 2026", US]]),
        ]},
        {"id": "2.5", "ic": "coins", "name": "Stablecoins", "blurb": "Coinbase, Fireblocks, Blue EMI.", "div": "eu", "rev": "move", "products": [
            P("stablecoins", "Stablecoin acceptance, settlement & issuance", "USDC acceptance with Coinbase and 24/7 US settlement with Fireblocks (June 2026), and a MiCA euro-stablecoin issuer through Blue EMI (January 2026).",
              s=["fin", "ent"], lc="move", st="new", neo=[0, "Off the card networks."],
              mc="Agent Pay for Machines settles in stablecoins too.",
              src=[["Checkout.com and Coinbase, Jun 2026", COINBASE], ["Checkout.com and Fireblocks, Jun 2026", FIREBLOCKS]]),
        ]},
        {"id": "2.6", "ic": "wallet-cards", "name": "Business account", "blurb": "Same-day settlement.", "div": "cko", "rev": "move", "products": [
            P("account", "Checkout Business Account", "Same-day settlement into a Checkout.com account (2024), with yield and expense features coming and US issuing funded from acquired balances.",
              s=["ent", "mkt"], lc="borrow", neo=[0, ""], src=[["Checkout.com: US growth, Sep 2026", US]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every payment: Intelligent Acceptance and network tokens, 3-D Secure and identity, fraud detection and disputes, the Flow checkout with Remember Me, and agentic commerce across every protocol.",
    "tiles": [
        {"id": "3.1", "ic": "gauge", "name": "Intelligent Acceptance", "blurb": "$15bn recovered.", "div": "cko", "rev": "protect", "products": [
            P("ia", "Intelligent Acceptance", "AI optimisation of payloads, authentication, tokens, routing and retries, credited with $15 billion of extra revenue for merchants by late 2025.",
              s=["ent"], lc="grow", neo=[1, "Optimises across networks."], src=[["Checkout.com: Intelligent Acceptance", IA]]),
            P("tokens", "Network tokens", "Visa and Mastercard tokens with an average 11% acceptance uplift, more than 200 million provisioned for more than 400 enterprise merchants.",
              s=["ent"], lc="grow", neo=[1, "Mastercard and Visa tokens."], src=[["Checkout.com: network tokens", TOKENS]]),
        ]},
        {"id": "3.2", "ic": "fingerprint", "name": "Authentication & identity", "blurb": "3DS, face, video ID.", "div": "cko", "rev": "protect", "products": [
            P("auth", "3-D Secure & identity", "3DS 2.2 (first certified on 2.3.1), redirectionless 3DS, Google device biometrics, face authentication (2025) and video identity verification from ubble.",
              s=["ent", "shop"], lc="open", neo=[1, "3DS works with Identity Check."], src=[["Checkout.com: authentication", TDS]]),
        ]},
        {"id": "3.3", "ic": "shield-check", "name": "Fraud & disputes", "blurb": "Fraud Detection Pro, Verifi.", "div": "cko", "rev": "protect", "products": [
            P("fraud", "Fraud Detection & disputes", "Machine-learning risk scores with backtesting and an AI autopilot, and dispute handling through Visa's Verifi Rapid Dispute Resolution.",
              s=["ent"], lc="everyday", neo=[0, "Own models; Visa's Verifi."],
              mc="Only Visa's Verifi is visible; Ethoca and Consumer Clarity are the gap.",
              src=[["Checkout.com: fraud detection", FRAUD]]),
        ]},
        {"id": "3.4", "ic": "zap", "name": "Checkout", "blurb": "Flow, Remember Me.", "div": "cko", "rev": "accept", "products": [
            P("flow", "Flow & Remember Me", "A low-code checkout with 35-plus methods (2024) and Remember Me (October 2025), one-click saved credentials across Checkout.com merchants in 194 countries.",
              s=["ent", "shop"], lc="grow", neo=[0, "Own network of saved cards."],
              mc="Remember Me does what Click to Pay does.",
              src=[["Checkout.com: Flow Remember Me, Oct 2025", REMEMBER]]),
        ]},
        {"id": "3.5", "ic": "bot", "name": "Agentic commerce", "blurb": "Agent Pay launch partner.", "div": "cko", "rev": "accept", "products": [
            P("agentpay", "Mastercard Agent Pay & Verifiable Intent", "A launch partner of Agent Pay (April 2025), backer of Verifiable Intent (March 2026) and an initial participant in Agent Pay for Machines (June 2026).", short="Agent Pay",
              s=["ent"], lc="move", st="new", o="P", at="Mastercard", neo=[3, "Mastercard Agent Pay."],
              mc="No live Agent Pay volume through Checkout.com has been published.",
              src=[["PYMNTS: Verifiable Intent, Mar 2026", VI], ["The Paypers: Agent Pay for Machines, Jun 2026", AP4M], ["Checkout.com blog with Mastercard, May 2026", AGENTBLOG]]),
            P("agentic", "Every agentic protocol", "Agent onboarding, credentials and liability tools (2025); OpenAI's ACP (November 2025), Google's UCP and AP2, and Visa Intelligent Commerce alongside Agent Pay.",
              s=["ent"], lc="move", st="new", neo=[1, "Protocol-neutral."], src=[["Checkout.com: ACP, Nov 2025", ACP]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "Who buys: large digital merchants (eBay, Uber, Spotify, Microsoft), marketplaces and platforms, travel companies, and fintechs and crypto exchanges, with 1,700 enterprise merchants in all.",
    "tiles": [
        {"id": "4.1", "ic": "building-2", "name": "Enterprise merchants", "blurb": "1,700 of them.", "div": "cko", "rev": "accept", "products": [
            P("enterprise", "Enterprise digital merchants", "More than 1,700 enterprise merchants, including eBay, Uber, Spotify, Microsoft, Pinterest, ASOS and HelloFresh.",
              s=["ent"], lc="everyday", neo=[1, "Accepts every network."], src=[["Checkout.com: $750m annualised, Sep 2026", REV26], ["Checkout.com: FY2025, Feb 2026", FY25]]),
        ]},
        {"id": "4.2", "ic": "users-round", "name": "Marketplaces & platforms", "blurb": "Temu, Vinted, Best Buy.", "div": "us", "rev": "accept", "products": [
            P("platforms", "Marketplaces & Platforms", "Marketplaces such as Temu, Vinted, SHEIN and Best Buy Marketplace (2026), and Platforms for software companies to embed payments without becoming payment facilitators (US first, 2026).",
              s=["mkt"], lc="everyday", st="new", neo=[1, "Accepts every network."], src=[["Checkout.com: US growth, Sep 2026", US]]),
        ]},
        {"id": "4.3", "ic": "plane", "name": "Travel", "blurb": "Trip.com, Agoda.", "div": "apac", "rev": "accept", "products": [
            P("travel", "Travel & hospitality", "Trip.com, Agoda, Minor Hotels, GetYourGuide and Rail Europe, with virtual cards for agents and APAC volume up 71% in 2025.",
              s=["travel"], lc="everyday", neo=[1, "Wholesale virtual cards on Mastercard."], src=[["Checkout.com: APAC, Mar 2026", APAC]]),
        ]},
        {"id": "4.4", "ic": "coins", "name": "Fintech & crypto", "blurb": "Coinbase, Moomoo, Klarna.", "div": "cko", "rev": "move", "products": [
            P("fintech", "Fintech, crypto & gaming", "Coinbase, Moomoo (real-time deposits through Visa, October 2026), Klarna and NetEase.",
              s=["fin"], lc="everyday", neo=[1, "Funding on Visa; acceptance on both."], src=[["Checkout.com newsroom", NEWS]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How merchants reach Checkout.com: one API and dashboard, 19 offices from London to São Paulo, and partners from SAP to Standard Chartered.",
    "tiles": [
        {"id": "5.1", "ic": "code-xml", "name": "API & dashboard", "blurb": "One integration.", "div": "cko", "rev": "grp", "products": [
            P("api", "Unified API & dashboard", "One API for every product, and a dashboard with natural-language analytics (2025).",
              s=["ent", "mkt"], lc="open", neo=[0, ""], src=[["Checkout.com", HOME]]),
        ]},
        {"id": "5.2", "ic": "earth", "name": "Regions", "blurb": "US, APAC, MENA, LatAm.", "div": "us", "rev": "grp", "products": [
            P("regions", "Regional hubs", "Nineteen offices: new hubs in San Francisco, Atlanta, São Paulo, Vilnius and Mexico, and teams for North America, APAC and MENA.",
              s=["ent"], lc="open", st="new", neo=[0, ""], src=[["Checkout.com: US growth, Sep 2026", US]]),
        ]},
        {"id": "5.3", "ic": "plug", "name": "Partners", "blurb": "SAP, banks, platforms.", "div": "cko", "rev": "grp", "products": [
            P("partners", "Integration & bank partners", "SAP's open payment framework (2026), BigCommerce, TeamSystem, and Standard Chartered in MENA.",
              s=["ent", "mkt"], lc="open", neo=[0, ""], src=[["Checkout.com newsroom", NEWS]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Checkout.com", "blurb": "Agent Pay, Move, Wholesale.", "products": [
        P("mcatcko", "Mastercard at Checkout.com", "Checkout.com accepts and tokenises Mastercard, issues on it, pays out on Mastercard Move (UAE, Canada), issues Wholesale virtual cards, and was a launch partner of Agent Pay, Verifiable Intent and Agent Pay for Machines. Visa has more public firsts in money movement and issuing: Visa Direct, travel issuing, Verifi and Moomoo.",
          s=["ent"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Mastercard: Checkout.com and Move, Feb 2025", MOVE], ["PYMNTS: Verifiable Intent, Mar 2026", VI]]),
    ]},
    {"id": "pillar-market", "name": "Enterprise acquiring", "blurb": "Stripe, Adyen, agents.", "products": [
        P("market", "The market", "Stripe ($1.9 trillion in 2025) and Adyen far larger; a race to set agentic standards; stablecoins under MiCA and the GENIUS Act; merchant-acquirer bank charters in the US.",
          s=["ent"], div="grp", rev="grp", src=[["Checkout.com: FY2025, Feb 2026", FY25]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
