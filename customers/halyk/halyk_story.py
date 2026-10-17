"""Halyk Bank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from halyk_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Central Asia's largest bank as five discs that stack into one platform, from KZT 22 trillion of assets and about "
       "30% of Kazakh loans and deposits at the bottom to the Halyk Super-App, Onlinebank and 530 branches at the top. "
       "Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up "
       "across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("prem", "Premium clients & travellers", "plane"),
    ("saver", "Savers & investors", "coins"),
    ("merch", "Merchants", "store"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Six kinds of customer: 11.5 million active retail clients, from everyday app users to premium travellers "
              "and savers, and 514,000 active businesses, from corner-shop merchants and small firms to the corporates "
              "behind nearly half of Kazakhstan's real-economy lending.")

WHO = {"con": "A Halyk customer", "prem": "A premium client", "saver": "A saver", "merch": "A merchant",
       "sme": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: the Super-App, a digital debit card, QR payments, phone-number transfers, bonuses and fraud checks.",
     "steps": [("5.1", "superapp", "Open the Halyk Super-App"), ("2.1", "debit", "Open a digital debit card"),
               ("2.4", "halykqr", "Pay with Halyk QR"), ("2.5", "p2p", "Send money by phone number"),
               ("3.4", "loyalty", "Earn Halyk+ bonuses"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "travel", "who": "prem", "name": "Travel on a premium card",
     "why": "Mastercard World Elite or Visa Infinite Ultra, a phone wallet abroad and money sent home.",
     "steps": [("2.2", "mcpremium", "Choose Mastercard World Elite"), ("2.2", "visapremium", "Or Visa Infinite Ultra"),
               ("2.4", "wallets", "Pay with Apple Pay abroad"), ("2.5", "xborder", "Send money abroad")]},
    {"id": "borrow", "who": "con", "name": "Borrow in the app",
     "why": "Digital loans, credit cards and instalments, 88% issued online.",
     "steps": [("5.1", "superapp", "Apply in the app"), ("4.1", "retaillending", "Take a loan online"),
               ("2.3", "credit", "Get a My!Card credit card"), ("2.3", "bnpl", "Spread a purchase")]},
    {"id": "shop", "who": "con", "name": "Shop and live in the ecosystem",
     "why": "Halyk Market, Travel and government services, paid in instalments and rewarded with bonuses.",
     "steps": [("4.5", "lifestyle", "Shop on Halyk Market"), ("2.3", "bnpl", "Pay in instalments"),
               ("3.2", "halykid", "Log in with Halyk ID"), ("3.4", "loyalty", "Collect bonuses")]},
    {"id": "save", "who": "saver", "name": "Save, invest and insure",
     "why": "Online deposits, Halyk Invest and the country's leading life insurer.",
     "steps": [("4.1", "deposits", "Open a deposit online"), ("4.4", "invest", "Invest with Halyk Invest"),
               ("4.4", "insurance", "Insure with Halyk Life")]},
    {"id": "merchant", "who": "merch", "name": "Run a shop",
     "why": "Take cards and QR, fiscalise with re:Kassa, restock through OnlineDuken and borrow on acquiring data.",
     "steps": [("2.6", "acquiring", "Take cards and QR"), ("2.6", "rekassa", "Fiscalise with re:Kassa"),
               ("4.3", "onlineduken", "Order stock on OnlineDuken"), ("4.3", "sme", "Borrow on acquiring data")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "Onlinebank, business and fuel cards, and digital loans and guarantees.",
     "steps": [("5.2", "onlinebank", "Run the business in Onlinebank"), ("4.3", "bizcards", "Issue business and fuel cards"),
               ("4.3", "sme", "Take a digital loan"), ("3.2", "baas", "Link the accounts")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "Corporate lending, Onlinebank payments, digital tenge and trade with Uzbekistan.",
     "steps": [("4.2", "corporate", "Bank with Halyk"), ("5.2", "onlinebank", "Pay through Onlinebank"),
               ("2.7", "dtenge", "Settle in digital tenge"), ("4.6", "tenge", "Trade with Uzbekistan")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The premium top tier, an option in the basic debit pack, wallet tokens, acceptance on Halyk POS, and the CEO's advisory-board seats.",
     "steps": [("2.2", "mcpremium", "World Elite and Imperial"), ("2.1", "debit", "MasterCard World in the basic pack"),
               ("2.4", "wallets", "Mastercard tokens in phone wallets"), ("2.6", "acquiring", "Mastercard accepted on Halyk POS"),
               ("1.2", "leadership", "CEO on Mastercard's advisory boards")]},
    {"id": "mcnext", "who": "mc", "name": "Where cross-border, fraud and agents could land",
     "why": "Where Halyk has needs and Mastercard is not yet in: transfers now on Visa Direct, fraud on account-to-account payments, AI agents, loyalty offers, business cards and SoftPOS.",
     "steps": [("2.5", "xborder", "Mastercard Move against Visa Direct"), ("3.1", "fraud", "Scam scoring for A2A and QR"),
               ("3.3", "ai", "Agent Pay for Halyk's AI agents"), ("3.4", "loyalty", "Card-linked offers in Halyk+"),
               ("4.3", "bizcards", "Commercial and fuel cards"), ("2.6", "acquiring", "Tap on Phone for Halyk Pos")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Halyk Bank's map",
    "title": "Mastercard at the top, Visa underneath, QR everywhere",
    "lead": "Halyk issues Visa, Mastercard, UnionPay and American Express. Mastercard holds the premium top with World Elite and Imperial, sits in the basic debit pack and the phone wallets, and the CEO sits on its Europe and EEMEA advisory boards. Visa carries more: the digital mass card ⚠, Infinite credit, the digital-tenge card and Visa Direct transfers. Behind both, Halyk QR, Kaspi and the national instant-payment system move most of Kazakhstan's money. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Halyk's own (1H 2026 results, 18 August 2026; annual report 2025) or from its card pages and tariffs, the National Bank and Kaspi.kz. Halyk publishes no card count by network; product pages for the digital and credit cards do not name the network.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Premium", "Mastercard World Elite", "Beside Visa Infinite Ultra and UnionPay Diamond"],
        ["Debit", "Visa-led, multi-network", "Digital card Visa Gold ⚠; basic pack Visa or Mastercard"],
        ["Credit", "Mostly unstated", "Infinite Credit on Visa"],
        ["Cross-border", "Visa Direct", "Alipay and WeChat wallets"],
        ["Digital tenge", "Visa", "First card, November 2023"],
        ["Country cards", "Visa 40.6m, Mastercard 14.1m", "Local systems 28.3m (1 June 2026)"],
        ["A2A", "Halyk QR, national QR", "Nationwide from 19 July 2026"],
        ["Board ties", "CEO on Mastercard boards", "Europe since 2019, EEMEA since 2022 ⚠"],
    ],
    "sides": {
        "neo": {"dir": "World Elite and Imperial cards, a basic-pack debit option, wallet tokens, acceptance on Halyk's terminals, and the CEO's advisory-board seats.",
                "deals": "What it does not do: the digital mass card, cross-border transfers, the digital tenge, QR, fraud, AI or loyalty."},
        "snb": {"dir": "Visa for the digital card, Infinite credit, Visa Direct and the digital tenge; UnionPay and Amex beside it; Halyk QR, Kaspi and the national instant-payment system for most payments.",
                "deals": "Where they meet: premium travel cards and the basic debit pack, where Visa and Mastercard are offered side by side."},
    },
    "tl": [
        ["2019", "CEO joins Mastercard Europe Advisory Board ⚠"],
        ["Jun 2022", "National Instant Payment System launched"],
        ["Jul 2022", "CEO joins Mastercard EEMEA Advisory Board ⚠"],
        ["Sep 2023", "Mastercard Almaty hub and Digital Country Partnership"],
        ["Nov 2023", "Halyk and Visa issue the first digital-tenge card"],
        ["Oct 2025", "Visa She's Next lending, KZT 600 million"],
        ["Nov 2025", "National unified QR launched"],
        ["Mar 2026", "Uzbek HUMO cards accepted on Halyk terminals"],
        ["Jun 2026", "re:Kassa bought"],
        ["Jul 2026", "Interbank instant payments and QR go nationwide"],
        ["Aug 2026", "1H results: net income down 15.3%"],
        ["Oct 2026", "OIY Tech: AI agents, with a Visa speaker"],
    ],
    "l": {
        "U": {"d": 1, "s": "Premium travellers and some basic-pack holders carry Mastercard.",
              "gap": "World Elite holders and basic-pack customers who choose it carry Mastercard; the digital mass card and most credit leans Visa; QR users carry no card at all.",
              "neo": "Premium travellers, some debit holders.", "snb": "Digital card holders, Visa premium holders, QR and transfer users, savers, corporates."},
        "L5": {"d": 0, "s": "The front doors are Halyk's.", "gap": "Super-App, Onlinebank and branches are the bank's own.", "neo": "None.", "snb": "Super-App, Onlinebank, branches, partners."},
        "L4": {"d": 0, "s": "The business lines carry no network role.", "gap": "Loans, deposits, insurance and the ecosystem are Halyk's; business card networks are not stated.",
               "neo": "None confirmed.", "snb": "Retail and corporate lending, SME, insurance, lifestyle, Tenge Bank."},
        "L3": {"d": 0, "s": "Fraud, identity, AI and loyalty are Halyk's own.", "gap": "No Mastercard fraud, identity, data or loyalty service is public.",
               "neo": "None.", "snb": "Anti-fraud hub, Halyk ID, AI agents, Halyk Club and Halyk+."},
        "L2": {"d": 1, "s": "Mastercard at the premium top; Visa and QR carry more.", "gap": "Mastercard has World Elite, a debit option, tokens and acceptance; Visa has the digital card, Infinite credit, Visa Direct and the digital tenge; QR and transfers are account-to-account.",
               "neo": "World Elite, basic-pack debit, wallets, acceptance.", "snb": "Visa cards, Visa Direct, digital tenge, Halyk QR, instant payments."},
        "L1": {"d": 0, "s": "The group's own foundation, with a Mastercard tie at the top.", "gap": "Nothing in the foundation runs on Mastercard; the CEO sits on its advisory boards.", "neo": "CEO advisory-board seats.", "snb": "Capital, ownership, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
