"""Swedbank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from swedbank_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Swedbank as five discs that stack into one platform, across four home markets: Sweden, Estonia, Latvia and "
       "Lithuania, from SEK 1,934 billion of loans at the bottom to the app, branches and savings banks at the top. "
       "Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up "
       "across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes "
       "in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("home", "Homebuyers", "house"),
    ("saver", "Savers & investors", "coins"),
    ("sme", "Small businesses", "briefcase"),
    ("merchant", "Merchants", "store"),
    ("corp", "Corporates & institutions", "factory"),
]
USERS_DESC = ("Six kinds of customer, about 7.3 million private and 548,000 corporate customers in all, across Sweden, "
              "Estonia, Latvia and Lithuania: everyday customers, homebuyers, savers, small businesses, the merchants "
              "Swedbank Pay serves and the corporates and institutions of C&I.")

WHO = {"con": "A Swedbank customer", "home": "A homebuyer", "saver": "A saver", "sme": "A small business",
       "merchant": "A merchant", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day in Sweden",
     "why": "An account, a Mastercard debit card, Swish, the app and fraud checks.",
     "steps": [("4.2", "deposits", "Open an account"), ("2.1", "sedebit", "Pay with Bankkort Mastercard"),
               ("2.6", "swish", "Swish a friend"), ("5.1", "app", "Run it in the app"), ("3.2", "fraud", "Protected from fraud")]},
    {"id": "baltic", "who": "con", "name": "Bank day to day in the Baltics",
     "why": "Mastercard cards in Estonia, Latvia and Lithuania, Click to Pay, Identity Check and fast transfers.",
     "steps": [("2.3", "ltcards", "Pay with a Debit Mastercard"), ("2.4", "c2p", "Check out with Click to Pay"),
               ("3.1", "idcheck", "Confirm with Smart-ID and Identity Check"), ("2.6", "balticpay", "Send money at home and abroad")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "Mastercard Standard to Platinum, issued by Entercard, with Priceless and travel benefits.",
     "steps": [("2.2", "secredit", "Take a Mastercard credit card"), ("3.4", "priceless", "Use Priceless"),
               ("3.4", "benefits", "Travel with lounge access and insurance")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "About a fifth of Swedish and two-fifths of Baltic mortgages, through branches, estate agents and Stabelo.",
     "steps": [("5.3", "savingsbanks", "Meet Fastighetsbyrån"), ("4.1", "semort", "Take a Swedbank mortgage"),
               ("4.1", "balticmort", "Or get a digital offer in the Baltics"), ("4.5", "insurance", "Insure it")]},
    {"id": "save", "who": "saver", "name": "Save and invest",
     "why": "Round-ups into Robur funds, and pensions with Swedbank Försäkring.",
     "steps": [("3.4", "mikroinvest", "Round up card payments"), ("4.5", "robur", "Invest in Robur funds"),
               ("4.5", "insurance", "Save for a pension"), ("5.1", "app", "Follow it in the app")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A business account, company cards, Swish and card acceptance.",
     "steps": [("4.4", "sme", "Open a business account"), ("2.2", "bizcards", "Give staff company cards"),
               ("2.6", "swish", "Get paid by Swish"), ("2.5", "swpay", "Take cards with Swedbank Pay")]},
    {"id": "merchant", "who": "merchant", "name": "Take payments",
     "why": "Swedbank Pay in-store and online, with Click to Pay at checkout.",
     "steps": [("2.5", "swpay", "Accept cards with Swedbank Pay"), ("2.4", "c2p", "Offer Click to Pay online"),
               ("2.6", "swish", "Take Swish")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "C&I lending, cash management on ISO 20022 and cross-border payments.",
     "steps": [("4.4", "corporate", "Bank with C&I"), ("3.5", "cashmgmt", "Manage liquidity"),
               ("2.6", "sepay", "Pay in ISO 20022"), ("2.6", "balticpay", "Pay across the Baltics")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Every consumer card in four markets, Click to Pay, Identity Check and Priceless.",
     "steps": [("2.1", "sedebit", "Swedish debit on Mastercard"), ("2.2", "secredit", "Credit on Mastercard"),
               ("2.3", "eecards", "Baltic cards on Mastercard"), ("2.4", "c2p", "Click to Pay"),
               ("3.1", "idcheck", "Identity Check"), ("3.4", "priceless", "Priceless")]},
    {"id": "mcnext", "who": "mc", "name": "Where Entercard, scams and account rails could land",
     "why": "Where Swedbank has needs and Mastercard is not yet in: the Entercard card consolidation, scam scoring, recurring and open-finance payments next to Swish, card-linked savings, Baltic cross-border flows and agentic payments.",
     "steps": [("2.2", "entercard", "One card business on Mastercard"), ("3.2", "fraud", "Scam and fraud scoring"),
               ("2.6", "swish", "Open-finance and recurring payments"), ("3.4", "mikroinvest", "Card-linked savings and offers"),
               ("2.6", "balticpay", "Cross-border with Mastercard Move"), ("3.3", "oken", "Agent Pay")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Swedbank's map",
    "title": "Mastercard on every consumer card in four markets; the rivals are account rails",
    "lead": "Every consumer debit and credit card Swedbank sells in Sweden, Estonia, Latvia and Lithuania is a Mastercard, about 8.6 million cards plus Entercard's 1.4 million, with Click to Pay, Identity Check and Priceless on top. No public network agreement was found. The pressure comes from Swish and Baltic account transfers, which carry most domestic payments, and from Swedbank Pay's shrinking Nordic acquiring. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Swedbank's own (Q2 2026 interim report and Factbook, 17 July 2026). Networks are read from each market's card pages on 17 October 2026; Entercard's partner cards and Swedish company cards do not state a network.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Sweden debit", "Mastercard", "4.6 million cards; Maestro retired"],
        ["Sweden credit", "Mastercard", "Issued by Entercard"],
        ["Estonia", "Mastercard", "1.1 million cards"],
        ["Latvia", "Mastercard, some Visa ⚠", "1.1 million cards"],
        ["Lithuania", "Mastercard", "1.9 million cards"],
        ["Entercard", "Wholly owned", "Dec 2025; 1.4 million cards"],
        ["Click to Pay", "All four markets", "Mastercard"],
        ["Swish", "Account rail", "Recurring payments, Q1 2026"],
    ],
    "sides": {
        "neo": {"dir": "Every consumer card in four markets, Click to Pay and wallet tokens, Identity Check, Priceless and card benefits, and acceptance at Swedbank Pay's merchants.",
                "deals": "What it does not do: Swish and Bankgirot, Baltic transfers, fraud models, AI, identity, lending and savings."},
        "snb": {"dir": "Swish, Bankgirot and Baltic account transfers, BankID and Smart-ID, Swedbank's own fraud and AI, and residual Visa cards ⚠.",
                "deals": "Where they meet: Entercard's card consolidation and Swish Recurring against card-on-file."},
    },
    "tl": [
        ["2005", "Hansabank bought; Baltic home markets"],
        ["2012", "Swish launched with five other banks"],
        ["Sep 2016", "UnionPay acceptance through Swedbank acquiring"],
        ["Aug 2025", "Barclays' Entercard stake agreed ⚠"],
        ["Q4 2025", "Card insurance added in all three Baltic states"],
        ["Dec 2025", "Entercard wholly owned"],
        ["Q1 2026", "Swish Recurring Payments"],
        ["Apr 2026", "Card and consumer-credit review; PayEx for sale"],
        ["Jul 2026", "DFS settlement closes investigations"],
        ["Sep 2026", "Bankgirot formats end; ISO 20022"],
    ],
    "l": {
        "U": {"d": 2, "s": "Every card-holding customer carries Mastercard.",
              "gap": "About 8.6 million Swedbank cards and Entercard's 1.4 million; savers and borrowers meet no network.",
              "neo": "Cardholders in all four markets.", "snb": "Swish users, mortgage and fund customers."},
        "L5": {"d": 0, "s": "The front doors are Swedbank's.", "gap": "App, branches and the savings banks are the bank's own.", "neo": "None.", "snb": "App, branches, savings banks."},
        "L4": {"d": 1, "s": "Accounts come with Mastercard debit.", "gap": "Deposits carry a Mastercard card; mortgages, Robur and corporate lending have no network role.",
               "neo": "Debit attached to accounts.", "snb": "Mortgages, consumer loans, C&I, Robur."},
        "L3": {"d": 1, "s": "Identity Check and Priceless are Mastercard's.", "gap": "Fraud models, AI and BankID are Swedbank's or the market's.",
               "neo": "Identity Check, Priceless, card benefits.", "snb": "BankID, Smart-ID, fraud, Oken."},
        "L2": {"d": 1, "s": "Cards on Mastercard; account rails are not.", "gap": "Every consumer card is Mastercard; Swish, Bankgirot and Baltic transfers carry most domestic payments.",
               "neo": "Debit, credit, Baltic cards, Click to Pay.", "snb": "Swish, Bankgirot, Baltic transfers, Swedbank Pay's other schemes."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, markets, governance, strategy."},
    },
    "t": area_lens(LAYERS),
}
