"""Banreservas' kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from banreservas_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("The Dominican Republic's state-owned bank as five discs that stack into one platform, from RD$1.28 trillion of "
       "assets and a third of the country's loans at the bottom to the app, 458 locations, 971 ATMs and 1,300 sub-agents "
       "at the top. Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it "
       "light up across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard "
       "goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("incl", "Newly banked & grant recipients", "hand-coins"),
    ("pref", "Preferred clients", "gem"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates, hotels & the state", "factory"),
    ("dias", "Diaspora & remittance families", "earth"),
]
USERS_DESC = ("Six kinds of customer, about 8 million in all: everyday customers, the newly banked and the families "
              "who receive state grants, preferred clients, about 88,000 small businesses, corporates, hotel groups "
              "and the state itself, and Dominicans abroad and the families their remittances reach.")

WHO = {"con": "A Banreservas customer", "incl": "A newly banked customer", "pref": "A preferred client",
       "sme": "A small business", "corp": "A corporate treasurer", "dias": "A Dominican abroad"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a Mastercard debit card, a phone wallet, the app and security.",
     "steps": [("4.5", "digitalacct", "Open an account"), ("2.1", "debit", "Pay with Mastercard debit"),
               ("2.4", "wallets", "Tap with Apple or Google Pay"), ("5.1", "app", "Run it in the app"),
               ("3.1", "token", "Confirm with the digital token")]},
    {"id": "inclusion", "who": "incl", "name": "Join the banking system",
     "why": "Bancarizar es Patria, the MIO e-wallet, sub-agents in every municipality and state grants paid into accounts.",
     "steps": [("4.5", "bancarizar", "Sign up at a Bancarizar event"), ("2.4", "mio", "Open MIO on the phone"),
               ("2.7", "govpay", "Receive a state grant"), ("5.3", "subagents", "Cash out at a sub-agent")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "Visa or Mastercard credit, instalments with Credimás and points on every purchase.",
     "steps": [("2.2", "credit", "Take a Visa or Mastercard card"), ("2.2", "credimas", "Split a purchase with Credimás"),
               ("3.4", "puntos", "Earn Puntos Banreservas")]},
    {"id": "rebuild", "who": "incl", "name": "Rebuild my credit",
     "why": "The Preserva card and the lower-rate Visa SER for people the market has turned away.",
     "steps": [("2.2", "preserva", "Take a Preserva card"), ("2.2", "ser", "Move up to Visa SER")]},
    {"id": "premium", "who": "pref", "name": "Travel with a premium card",
     "why": "Visa Infinite or Mastercard Black, airport lounges and network promotions.",
     "steps": [("2.2", "premium", "Hold Visa Infinite or Mastercard Black"), ("3.4", "promos", "Use network offers"),
               ("5.2", "branches", "Get preferred service")]},
    {"id": "home", "who": "con", "name": "Buy a home or a car",
     "why": "Pre-qualify with Alma, then borrow at the bank's housing and car fairs.",
     "steps": [("3.2", "alma", "Pre-qualify with Alma"), ("4.1", "fairs", "Apply at Expo Hogar or Expo Móvil"),
               ("4.1", "personal", "Take the loan")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "SME loans, the new Mastercard Comercial card, CardNet acceptance and collections.",
     "steps": [("4.2", "sme", "Borrow as an SME"), ("2.3", "mccomercial", "Spend on Mastercard Comercial"),
               ("2.5", "cardnet", "Take cards through CardNet"), ("3.3", "cashmgmt", "Collect and deposit")]},
    {"id": "corp", "who": "corp", "name": "Finance a hotel or a fleet",
     "why": "Tourism and corporate lending, Visa corporate and fleet cards, and cash management.",
     "steps": [("4.4", "tourism", "Finance a hotel"), ("4.3", "corporate", "Bank with corporate banking"),
               ("2.3", "fleet", "Run vehicles on Visa Flotilla"), ("3.3", "cashmgmt", "Manage cash")]},
    {"id": "diaspora", "who": "dias", "name": "Send money home",
     "why": "Remittances paid into accounts, the Remesas Reservas app and diaspora banking.",
     "steps": [("5.2", "diaspora", "Open an account from abroad"), ("2.7", "remesasapp", "Send with Remesas Reservas"),
               ("2.7", "remit", "Family receives it in savings"), ("4.1", "personal", "Borrow against remittances")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "All debit, half the credit tiers, MIO for new clients, the new commercial card and the inclusion programme.",
     "steps": [("2.1", "debit", "Mastercard debit for 3.8 million"), ("2.2", "credit", "Mastercard credit tiers"),
               ("2.2", "premium", "Mastercard Black"), ("2.4", "mio", "MIO's Mastercard credential"),
               ("2.3", "mccomercial", "Mastercard Comercial"), ("4.5", "bancarizar", "Bancarizar es Patria")]},
    {"id": "mcnext", "who": "mc", "name": "Where fleet, fraud and remittances could land",
     "why": "Where Banreservas has needs and Mastercard is not yet in: Visa-held fleet and corporate cards, fraud tools for a fast-growing token base, remittances and grants, acceptance as QR instant payments arrive, card-linked offers and agentic payments.",
     "steps": [("2.3", "fleet", "Fleet and corporate cards"), ("3.1", "cyber", "Fraud and identity tools"),
               ("2.7", "remit", "Move for remittances"), ("2.7", "govpay", "Prepaid for state grants"),
               ("2.6", "instant", "Acceptance as QR arrives"), ("3.4", "puntos", "Card-linked offers"),
               ("3.2", "alma", "Agent Pay for Alma")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Banreservas' map",
    "title": "Mastercard holds the debit; Visa shares the credit",
    "lead": "Every Banreservas debit card in the live catalogue is a Mastercard: 3.8 million of them, almost half the country's. Credit is shared: most tiers come in Visa and Mastercard, Visa has Infinite, the SER inclusion card and most commercial and fleet cards, and Mastercard has Black. Mastercard won new MIO e-wallet issuance in 2025 and launched a commercial card with the bank on 5 October 2026. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (Memoria Institucional 2025) or from banreservas.com and the Dominican press. The bank does not publish its credit split by network, and no 2026 half-year report was found.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Mastercard", "3.8 million cards; 47% of the market"],
        ["Credit", "Visa and Mastercard", "1.47 million cards; split not published ⚠"],
        ["Premium", "Visa Infinite; Mastercard Black", "Both networks at the top"],
        ["Commercial", "Visa; Mastercard Comercial", "Mastercard card launched 5 Oct 2026"],
        ["MIO e-wallet", "Visa, then Mastercard", "Mastercard for new clients from 2025"],
        ["Acceptance", "CardNet", "All networks"],
        ["Instant payments", "Central bank", "New system with QR due 2027"],
        ["Remittances", "Accounts", "US$1.65 billion in 2025"],
    ],
    "sides": {
        "neo": {"dir": "All debit, half the consumer credit tiers and Black, MIO for new clients, Mastercard Comercial with Easy Savings and My Cyber Risk, and the inclusion programme.",
                "deals": "What it does not do: fleet and most corporate cards, Visa Infinite and SER, fraud tools, remittances or the new instant payments."},
        "snb": {"dir": "Visa credit, premium, SER, corporate and fleet cards; CardNet acceptance; the central bank's instant payments; the bank's own security, AI and loyalty.",
                "deals": "Where they meet: every credit tier and the MIO wallet, where customers get one brand or the other."},
    },
    "tl": [
        ["1941", "Banco de Reservas founded"],
        ["2014", "Visa Infinite launched ⚠"],
        ["2021", "Bancarizar es Patria starts, Mastercard a partner"],
        ["Nov 2022", "MIO launches on Visa; Visa SER"],
        ["Apr 2024", "Organic Law 13-24"],
        ["Mid-2025", "Mastercard credential on MIO"],
        ["Aug 2025", "Leonardo Aguilera named executive president"],
        ["Dec 2025", "3.8m debit cards (47%), 1.47m credit (33%)"],
        ["Mar 2026", "Banco Popular launches Toke"],
        ["5 Oct 2026", "Mastercard Comercial launched"],
        ["H1 2027", "Central-bank instant payments due"],
    ],
    "l": {
        "U": {"d": 1, "s": "Almost every customer's debit card is a Mastercard.", "gap": "Debit holders carry Mastercard; credit holders carry either brand; fleet and corporate users mostly Visa.",
              "neo": "Debit holders, Mastercard credit and Black holders, new MIO users.", "snb": "Visa credit, SER, Infinite and corporate holders; remittance families."},
        "L5": {"d": 0, "s": "The front doors are the bank's.", "gap": "App, branches, ATMs and sub-agents are Banreservas' own.", "neo": "None.", "snb": "App, branches, ATMs, sub-agents."},
        "L4": {"d": 1, "s": "Accounts come with Mastercard debit; lending has no network role.", "gap": "SME and inclusion accounts carry Mastercard debit; Mastercard is a Bancarizar partner; loans, tourism and subsidiaries are network-free.",
               "neo": "Bancarizar es Patria, account debit cards.", "snb": "Loans, tourism, government business, insurance and pensions."},
        "L3": {"d": 1, "s": "Points and promotions run on both networks; the rest is the bank's.", "gap": "Security, AI and APIs are in-house; no Mastercard fraud or data tools are named.",
               "neo": "Network promotions, points on Mastercard cards.", "snb": "Cybersecurity, Alma, APIs, cash management."},
        "L2": {"d": 1, "s": "Debit on Mastercard; credit shared; commercial mostly Visa.", "gap": "Mastercard has debit and the new commercial card; Visa has SER, Infinite, fleet and corporate; instant payments and remittances run elsewhere.",
               "neo": "Debit, Mastercard credit and Black, MIO, Mastercard Comercial.", "snb": "Visa credit and commercial, CardNet, central-bank rails, remittances."},
        "L1": {"d": 0, "s": "The state bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, governance, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
