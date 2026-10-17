"""NLB Group's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from nlb_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Slovenia's biggest bank and its six sister banks in the Western Balkans as five discs that stack into one "
       "platform, from EUR 31.9 billion of assets at the bottom to NLB Klik, branches and partners at the top. Click the "
       "stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the "
       "layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("priv", "Premium & private clients", "gem"),
    ("saver", "Savers & investors", "coins"),
    ("sme", "Small businesses & merchants", "briefcase"),
    ("corp", "Corporates", "factory"),
    ("see", "Customers in the Western Balkans", "globe"),
]
USERS_DESC = ("Six kinds of customer, about 2.9 million active clients in all: everyday Slovenian customers, premium and "
              "private clients, savers and investors, small businesses and merchants, corporates, and 2.2 million "
              "customers of the six banks in Serbia, North Macedonia, Bosnia and Herzegovina, Kosovo and Montenegro.")

WHO = {"con": "An NLB customer", "priv": "A private client", "saver": "A saver", "sme": "A small business",
       "corp": "A corporate treasurer", "see": "A customer in the region"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "A package with a Debit Mastercard, NLB Klik and NLB Pay, and Flik for transfers.",
     "steps": [("3.1", "onboarding", "Open an account on the phone"), ("4.1", "packages", "Choose a package"),
               ("2.1", "debit", "Pay with Debit Mastercard"), ("2.5", "nlbpay", "Tap with NLB Pay"),
               ("2.6", "flik", "Send money with Flik"), ("5.1", "klik", "Run it in NLB Klik")]},
    {"id": "newcard", "who": "con", "name": "Get a card in minutes",
     "why": "The digital-first card lands in the wallet as soon as it is ordered.",
     "steps": [("2.1", "digitalcard", "Order a digital-first card"), ("2.5", "xpay", "Add it to Apple Pay or Google Pay"),
               ("3.1", "fraud", "Protected by wallet anti-fraud")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card or a loan",
     "why": "3v1 Mastercard revolving cards, Visa and Mastercard charge cards, and housing loans.",
     "steps": [("2.2", "credit", "Take a 3v1 or charge card"), ("4.1", "housing", "Take a housing or consumer loan")]},
    {"id": "private", "who": "priv", "name": "Bank privately",
     "why": "World Elite Mastercard, concierge and lounges, private banking and its own app.",
     "steps": [("4.2", "private", "Join NLB Private Banking"), ("2.2", "premium", "Use World Elite benefits"),
               ("5.1", "privateapp", "Follow it in the NLB Private app")]},
    {"id": "invest", "who": "saver", "name": "Save and invest",
     "why": "Slovenia's biggest fund manager, bancassurance and the trading app.",
     "steps": [("4.2", "skladi", "Invest in NLB Skladi funds"), ("4.2", "bancassurance", "Insure through the bank"),
               ("5.1", "privateapp", "Trade in NLB Trading")]},
    {"id": "merchant", "who": "sme", "name": "Run a small business",
     "why": "A business account, Visa business cards, Smart POS and Flik at the till.",
     "steps": [("4.4", "sme", "Open a business account"), ("2.3", "bizcards", "Pay with a business card"),
               ("2.7", "acquiring", "Take cards on Smart POS"), ("2.6", "flik", "Take Flik at the till"),
               ("5.2", "klikpro", "Manage it in Klikpro")]},
    {"id": "corporate", "who": "corp", "name": "Finance a corporate",
     "why": "Syndicated loans, trade finance, leasing and SEPA payments.",
     "steps": [("4.4", "cib", "Borrow through CIB"), ("4.4", "trade", "Use trade finance and factoring"),
               ("4.3", "lease", "Lease equipment"), ("2.6", "sepa", "Pay across SEPA")]},
    {"id": "region", "who": "see", "name": "Bank with NLB in the Balkans",
     "why": "Six banks with Visa, Mastercard and DinaCard cards, Apple Pay and SEPA arriving.",
     "steps": [("4.5", "seebanks", "Bank with an NLB bank"), ("2.4", "kbcards", "Choose a DinaCard, Visa or Mastercard card"),
               ("2.5", "xpay", "Pay with Apple Pay"), ("2.6", "sepa", "Send euros over SEPA")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Every Slovenian personal debit card, most credit cards, the premium tiers and part of the regional books.",
     "steps": [("2.1", "debit", "Debit Mastercard for every package"), ("2.2", "credit", "Mostly Mastercard credit"),
               ("2.2", "premium", "World and World Elite benefits"), ("2.4", "kbcards", "Mastercard alongside Visa and DinaCard in Serbia")]},
    {"id": "mcnext", "who": "mc", "name": "Where tokens, merchants and DBS could land",
     "why": "Where NLB has needs and Mastercard is not yet in: tokenisation in NLB Pay, small-merchant acquiring, the loyalty model, fraud tools, business cards lost to Visa, and DBS's customers after 2027.",
     "steps": [("2.5", "nlbpay", "Token services for NLB Pay"), ("2.7", "acquiring", "Acceptance and onboarding for Smart POS"),
               ("3.3", "loyalty", "Card-linked offers for the loyalty model"), ("3.1", "fraud", "Fraud scoring and identity"),
               ("2.3", "bizcards", "Commercial cards to win back business spend"), ("1.5", "dbs", "Cards for DBS customers")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across NLB Group's map",
    "title": "Mastercard owns the consumer wallet; Visa took business debit",
    "lead": "Since Maestro was retired in 2025, every Slovenian personal debit card at NLB is a Debit Mastercard, and most credit cards and the World and World Elite tiers are Mastercard too. Visa took the business debit book in June 2025, issues some credit and prepaid cards, and shares Serbia and Kosovo with Mastercard, where DinaCard also competes. No joint initiative is public. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (H1 2026 results, 6 August 2026; annual report 2025) or from NLB's card pages and press. Card networks in Skopje, Bosnia and Podgorica, and Bankart's processing role, are not public.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Personal debit, Slovenia", "Mastercard", "Replaced Maestro, 2025"],
        ["Credit, Slovenia", "Mostly Mastercard", "Visa and Premium Visa too"],
        ["Premium", "World & World Elite", "Concierge, LoungeKey"],
        ["Business debit", "Visa", "Migrated June 2025 ⚠"],
        ["Serbia", "DinaCard, Visa, Mastercard", "1 million active clients"],
        ["Tokenised share", "28.9%", "H1 2026, NLB Pay and wallets"],
        ["Instant", "Flik", "At every point of sale"],
    ],
    "sides": {
        "neo": {"dir": "Slovenian personal debit and most credit, the premium tiers, part of the cards in Serbia and Kosovo, and acceptance at NLB's merchants and ATMs.",
                "deals": "What it does not do: business debit, prepaid, Flik, fraud and loyalty tools, or anything outside cards."},
        "snb": {"dir": "Visa business debit, some credit and prepaid, and much of the regional books; DinaCard in Serbia; Flik and SEPA Instant; NLB's own wallet, AI and fraud tools.",
                "deals": "Where they meet: NLB Pay and the big wallets, which carry both networks."},
    },
    "tl": [
        ["Dec 2020", "Komercijalna banka joins with DinaCard, Visa and Mastercard"],
        ["Feb 2024", "Apple Pay in Slovenia"],
        ["Apr 2025", "Maestro retired; Debit Mastercard for consumers"],
        ["Jun 2025", "Business debit moves to Visa ⚠"],
        ["Jul 2025", "Apple Pay in every NLB bank"],
        ["Late 2025", "Digital-first debit card; LoungeKey on World Elite"],
        ["H1 2026", "28.9% of card payments tokenised"],
        ["Aug 2026", "Addiko bid fails"],
        ["Sep 2026", "DBS deal signed"],
    ],
    "l": {
        "U": {"d": 1, "s": "Slovenian consumers carry Mastercard; businesses carry Visa.",
              "gap": "Personal debit and most credit are Mastercard; business debit is Visa; the region is shared with Visa and DinaCard.",
              "neo": "Slovenian consumers, private clients, part of the region.", "snb": "Businesses, prepaid holders, many regional cardholders."},
        "L5": {"d": 0, "s": "The front doors are NLB's.", "gap": "NLB Klik, Klikpro, branches and partners are the group's own.", "neo": "None.", "snb": "Apps, branches, partners."},
        "L4": {"d": 1, "s": "Packages and private banking come with Mastercard.", "gap": "Every package carries a Debit Mastercard and private clients World Elite; loans, funds and leasing have no network role.",
               "neo": "Packages, private banking, part of the SEE banks.", "snb": "Loans, funds, leasing, CIB, SME (Visa debit)."},
        "L3": {"d": 0, "s": "Services are NLB's own or not public.", "gap": "No network fraud, identity or loyalty tools are public; the loyalty model is still being designed.",
               "neo": "None public.", "snb": "Own anti-fraud, AI assistant, onboarding."},
        "L2": {"d": 1, "s": "Consumer cards on Mastercard; business on Visa; Flik alongside.", "gap": "Mastercard holds Slovenian personal debit and most credit; Visa has business debit and prepaid; Flik and SEPA Instant compete for payments.",
               "neo": "Debit, most credit, premium, part of SEE cards, wallets.", "snb": "Visa business and prepaid, DinaCard, Flik, SEPA."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, ownership, technology, strategy, deals."},
    },
    "t": area_lens(LAYERS),
}
