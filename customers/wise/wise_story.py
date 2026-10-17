"""Wise's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from wise_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("A cross-border money network as five discs that stack into one, from $243 billion of transfers, more than 80 "
       "licences and a Nasdaq listing at the bottom to the Wise app and partner banks' apps at the top. Click the stack "
       "to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the "
       "layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("pers", "People sending money", "user-round"),
    ("trav", "Travellers & expats", "plane"),
    ("save", "Savers", "coins"),
    ("biz", "Small businesses", "briefcase-business"),
    ("bank", "Banks & fintechs", "landmark"),
    ("ent", "Enterprises & marketplaces", "building-2"),
]
USERS_DESC = ("Six kinds of user, 18.9 million active customers in FY26: people sending money home or abroad, "
              "travellers and expats spending on the card, savers holding balances, about 850,000 small businesses, "
              "and the banks, fintechs and enterprises that run on Wise Platform.")

WHO = {"pers": "A Wise customer", "trav": "A traveller", "save": "A saver", "biz": "A small business",
       "bank": "A partner bank", "ent": "An enterprise"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "send", "who": "pers", "name": "Send money abroad",
     "why": "The core loop: open an account, pay in locally, send at the mid-market rate over Wise's own domestic links.",
     "steps": [("5.1", "app", "Open the app"), ("2.5", "receive", "Pay in locally"), ("3.1", "fincrime", "Checked in under a second"),
               ("2.1", "xborder", "Send at the mid-market rate"), ("2.2", "direct", "Arrive over a direct link")]},
    {"id": "spend", "who": "trav", "name": "Spend abroad on the card",
     "why": "Hold 40 currencies and spend with a debit card, now mostly on Visa, or a phone wallet.",
     "steps": [("4.1", "account", "Hold 40 currencies"), ("2.3", "card", "Pay with the Wise card"), ("2.3", "digital", "Or tap a phone"),
               ("2.3", "fifa", "Collect the World Cup card")]},
    {"id": "save", "who": "save", "name": "Earn on balances",
     "why": "Balances earn interest or go into funds through Wise Assets; the float is Wise's second engine.",
     "steps": [("4.1", "account", "Hold money in Wise"), ("3.5", "interest", "Earn interest"), ("3.5", "assets", "Invest through Wise Assets"),
               ("1.5", "float", "Part of $41bn of holdings")]},
    {"id": "biz", "who": "biz", "name": "Run a business across borders",
     "why": "Pay suppliers and staff abroad, give the team cards, and sync receipts to the books.",
     "steps": [("4.2", "business", "Open Wise Business"), ("2.1", "xborder", "Pay suppliers abroad"), ("2.4", "bizcard", "Give the team cards"),
               ("3.6", "accounting", "Sync receipts to Xero"), ("3.6", "cashback", "Earn 0.5% cashback")]},
    {"id": "bank", "who": "bank", "name": "Power a bank's transfers",
     "why": "A bank plugs into Wise Platform by API or by Swift and sells Wise transfers under its own brand.",
     "steps": [("4.3", "platform", "Join Wise Platform"), ("3.3", "api", "Integrate the API"), ("3.4", "swiftcs", "Or send Swift messages"),
               ("3.1", "kyc", "Embed onboarding"), ("5.2", "partnerapps", "Sell it in the bank's app")]},
    {"id": "issue", "who": "bank", "name": "Issue cards through Wise",
     "why": "Platform partners can give their customers multi-currency accounts and cards on Wise.",
     "steps": [("4.3", "newpartners", "Sign as a partner bank"), ("4.3", "platcards", "Issue cards and accounts"), ("2.2", "direct", "Settle over Wise's rails")]},
    {"id": "payout", "who": "ent", "name": "Pay freelancers worldwide",
     "why": "Marketplaces and fintechs pay out through Wise Platform instead of building their own corridors.",
     "steps": [("4.4", "payouts", "Pay freelancers through Wise"), ("3.3", "api", "Call the Platform API"), ("2.2", "direct", "Land on local rails")]},
    {"id": "us", "who": "pers", "name": "Bank with Wise in North America",
     "why": "A Nasdaq listing, a trust bank charter to retry, sponsor-bank Visa cards, and a new Canadian chequing account.",
     "steps": [("1.3", "nasdaq", "Listed on Nasdaq"), ("1.2", "charter", "Reapply for a charter"), ("2.3", "card", "Visa cards through sponsor banks"),
               ("4.1", "chequing", "Open a Canadian chequing account")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The legacy Mastercard debit cards still in use, their tokens in phone wallets, and the Mastercard Send payouts of 2020.",
     "steps": [("2.3", "mccard", "Legacy Mastercard debit cards"), ("2.3", "digital", "Tokens on remaining Mastercard cards"),
               ("2.6", "mcsend", "Mastercard Send payouts (2020)")]},
    {"id": "mcnext", "who": "mc", "name": "Where business cards and AML tools could land",
     "why": "Where Wise has needs and Mastercard is not visibly in: business and Platform cards with no named network, fraud and AML tools after the OCC denial, cashback, and payouts where Wise has no direct link.",
     "steps": [("2.4", "bizcard", "Commercial cards for Wise Business"), ("4.3", "platcards", "Cards for Platform banks"),
               ("3.1", "fincrime", "Identity and AML tools"), ("3.6", "cashback", "Offers and cashback"), ("2.6", "mcsend", "Mastercard Move endpoints")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Wise's map",
    "title": "Mastercard launched the Wise card; Visa now carries it",
    "lead": "Mastercard carried the first Wise card in Europe (2018) and the US (2019), and by 2020 had more than 1 million cards and Mastercard Send payouts with Wise. In January 2021 Visa signed a global deal, and current UK and US cards are Visa, with Mastercard cards left in circulation. Wise's own rails (direct links in eight markets, Swift Correspondent Services, Wise Platform) compete with both networks' money-movement products. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Wise's own results, 20-F and pages, Mastercard's and Visa's releases and trade press. Wise does not publish a card network split.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Personal card", "Mostly Visa", "Mastercard until about 2023 ⚠; legacy cards still live"],
        ["US card", "Visa", "Lead Bank and CFSB sponsor banks"],
        ["Card spend", "$43.6bn FY26", "+37%; card revenue $391.6m"],
        ["Business card", "Network not stated", "Fastest-growing card line"],
        ["Payouts", "Own direct links", "Mastercard Send in 2020, Visa Direct too"],
        ["Banks", "Wise Platform", "Swift Correspondent Services; rival to Move"],
        ["Mastercard news", "Last in Aug 2020", "Nothing public since"],
        ["Visa news", "Jan 2021 global deal", "FIFA World Cup card, Jun 2026"],
    ],
    "sides": {
        "neo": {"dir": "The legacy Mastercard debit cards, their wallet tokens, and Mastercard Send payouts from 2020.",
                "deals": "What it does not have: current personal issuing, business cards, Platform cards, fraud tools or payouts."},
        "snb": {"dir": "Visa for current personal cards and the World Cup card, Wise's own direct links and Swift for transfers, and its own fraud and KYC models.",
                "deals": "Where they meet: every card payment abroad, and banks choosing between Wise Platform and network money-movement products."},
    },
    "tl": [
        ["2018", "First Wise card in Europe, on Mastercard"],
        ["Jun 2019", "US Mastercard debit card"],
        ["Aug 2020", "Mastercard deal widened; Mastercard Send payouts"],
        ["Jan 2021", "Visa global partnership, Visa Cloud Connect"],
        ["Sep 2023", "Swift Correspondent Services"],
        ["2023–24", "New cards move to Visa ⚠"],
        ["May 2026", "Nasdaq primary listing"],
        ["Jun 2026", "Wise Visa FIFA World Cup card"],
        ["Jul 2026", "OCC denies trust bank charter"],
    ],
    "l": {
        "U": {"d": 1, "s": "Card users on legacy Mastercard; most new cards on Visa.",
              "gap": "Holders of older cards still pay on Mastercard; new personal cards, the World Cup card and US cards are Visa; transfers use neither.",
              "neo": "Legacy Mastercard cardholders.", "snb": "New Visa cardholders, transfer customers, Platform banks."},
        "L5": {"d": 0, "s": "The front doors are Wise's and its partners'.", "gap": "App, partner apps and offices are its own.",
               "neo": "None.", "snb": "Wise app, partner apps, Swift."},
        "L4": {"d": 0, "s": "No business line runs on Mastercard.", "gap": "Accounts, Business and Platform are Wise's own; business and Platform card networks are not named.",
               "neo": "None confirmed.", "snb": "Wise Account, Wise Business, Wise Platform."},
        "L3": {"d": 0, "s": "Wise's own models and APIs.",
               "gap": "Fraud, KYC, AI, API and Correspondent Services are Wise's own or Swift's.",
               "neo": "None.", "snb": "Own fraud models, KYC, Swift."},
        "L2": {"d": 1, "s": "A Mastercard tail in cards; Visa ahead; transfers on Wise's rails.",
               "gap": "Legacy Mastercard cards and Mastercard Send; current cards on Visa; direct domestic links carry transfers.",
               "neo": "Legacy cards, Mastercard Send.", "snb": "Visa cards, Visa Direct, direct links."},
        "L1": {"d": 0, "s": "Wise's own scale, licences and stack.", "gap": "Nothing in the foundation is Mastercard's.",
               "neo": "None.", "snb": "Licences, listing, stack, float."},
    },
    "t": area_lens(LAYERS),
}
