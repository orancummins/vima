"""Bancolombia's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from bancolombia_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Colombia's biggest bank as five discs that stack into one platform, from Grupo Cibest's COP 363 trillion of "
       "assets at the bottom to the Mi Bancolombia and Nequi apps at the top. Click the stack to open it. Choose who "
       "you are and what you want to do, and the areas that deliver it light up across the layers, joined in the order "
       "they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("prem", "Premium clients", "gem"),
    ("nequi", "Nequi users", "smartphone"),
    ("sme", "Businesses & merchants", "store"),
    ("corp", "Corporates", "factory"),
    ("ca", "Central American customers", "earth"),
]
USERS_DESC = ("Six kinds of customer: more than 16 million people and businesses at Bancolombia, its premium clients, "
              "about 29 million Nequi users, the merchants on Wompi and the QR, corporates, and the clients of Banco "
              "Agrícola and BAM in Central America.")

WHO = {"con": "A Bancolombia customer", "prem": "A premium client", "nequi": "A Nequi user", "sme": "A merchant",
       "corp": "A corporate treasurer", "ca": "A customer in El Salvador"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a Mastercard debit card, the app, a phone wallet and fraud checks.",
     "steps": [("4.1", "personal", "Open an account"), ("2.1", "debit", "Pay with Mastercard debit"), ("2.3", "wallets", "Add it to a phone wallet"),
               ("5.1", "app", "Run it in Mi Bancolombia"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "Colombia's largest credit-card book, on Mastercard, Visa or Amex.",
     "steps": [("2.2", "credit", "Choose a credit card"), ("3.2", "ai", "Approved with AI"), ("3.3", "points", "Earn Puntos Colombia")]},
    {"id": "premium", "who": "prem", "name": "Travel as a premium client",
     "why": "World Legend, Black, Visa Infinite or a metal Amex Platinum.",
     "steps": [("4.1", "premium", "Join premium banking"), ("2.2", "legend", "Carry World Legend"), ("2.2", "visaco", "Or fly on LifeMiles Visa"),
               ("3.3", "points", "Use lounges and points")]},
    {"id": "pay", "who": "con", "name": "Send money instantly",
     "why": "Bre-B keys and the Bancolombia QR, account to account.",
     "steps": [("5.1", "app", "Register a key in the app"), ("2.5", "breb", "Send through Bre-B"), ("2.5", "qr", "Pay a shop by QR")]},
    {"id": "nequi", "who": "nequi", "name": "Bank for the first time with Nequi",
     "why": "A wallet, a Visa card and credit for people new to it.",
     "steps": [("5.2", "nequiapp", "Open Nequi"), ("2.4", "nequicard", "Get the Nequi Visa card"), ("4.3", "nequicredit", "Borrow at the till"),
               ("2.7", "wenia", "Buy COPW on Wenia")]},
    {"id": "merchant", "who": "sme", "name": "Take payments as a merchant",
     "why": "Wompi, the QR and the business app.",
     "steps": [("4.2", "business", "Open a business account"), ("2.6", "wompi", "Take cards with Wompi"), ("2.5", "qr", "Take QR payments on Bre-B"),
               ("5.1", "negocios", "Manage it in Bancolombia Negocios")]},
    {"id": "fleet", "who": "corp", "name": "Finance or lease vehicles",
     "why": "Sufi and Renting Colombia.",
     "steps": [("4.4", "renting", "Lease a fleet"), ("4.4", "sufi", "Finance a vehicle with Sufi")]},
    {"id": "ca", "who": "ca", "name": "Bank in El Salvador",
     "why": "Banco Agrícola and Nequi El Salvador with a Mastercard debit card.",
     "steps": [("4.5", "agricola", "Bank with Banco Agrícola"), ("2.4", "nequisv", "Receive remittances on Nequi")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "All of debit, the biggest share of credit, World Legend and Nequi in El Salvador.",
     "steps": [("2.1", "debit", "Debit on Mastercard"), ("2.1", "transit", "Transit on Mastercard Transporte"), ("2.2", "credit", "About 1.2m credit cards"),
               ("2.2", "legend", "World Legend, first issuer"), ("2.4", "nequisv", "Nequi El Salvador")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, Bre-B and Nequi could land",
     "why": "Where Bancolombia has needs and Mastercard is not yet in: purchasing agents, scam scoring for Bre-B, Nequi's point-of-sale credit, Wompi merchants and fleet cards.",
     "steps": [("3.2", "agents", "Agent Pay for purchasing agents"), ("2.5", "breb", "Scam scoring on Bre-B"), ("4.3", "nequicredit", "Tokens for Nequi credit"),
               ("2.6", "wompi", "Merchant risk for Wompi"), ("4.4", "renting", "Fleet cards")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Bancolombia's map",
    "title": "Mastercard owns the debit, shares the credit, and faces Bre-B",
    "lead": "Every Bancolombia debit card is Mastercard, and Mastercard is the largest of three networks on Colombia's biggest credit-card book, about 1.2 million of 2.76 million active cards in April 2026. In May 2026 Bancolombia became the first issuer of World Legend. Visa holds Nequi's Colombian card, the travel and football co-brands and the first Tap to Add Card; Amex has seven cards; and the Bancolombia QR now runs on Bre-B. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (Q2 2026 results, 10 August 2026) as reported by Colombian financial press, and Superintendencia Financiera card data (30 April 2026) as reported by La República. Banco Agrícola and BAM card networks and any Bancolombia network contract were not found.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Mastercard", "All six cards; Maestro retired"],
        ["Credit", "Mastercard, Visa, Amex", "About 1.2m / 888k / 573k active"],
        ["Premium", "World Legend", "First issuer, May 2026"],
        ["Nequi Colombia", "Visa", "Debit card, 2024"],
        ["Nequi El Salvador", "Mastercard", "Digital debit, July 2024"],
        ["Wallets", "Visa Tap to Add", "January 2025"],
        ["Instant", "Bre-B", "116m keys; QR moved May 2026"],
        ["Acceptance", "Wompi", "83,000+ businesses"],
    ],
    "sides": {
        "neo": {"dir": "All of debit and transit, the largest share of credit, World Legend, Nequi El Salvador, and acceptance through Wompi.",
                "deals": "What it does not do: Nequi in Colombia, Bre-B and the QR, Wenia's stablecoin, AI or fraud."},
        "snb": {"dir": "Visa credit, co-brands and Nequi's card, Amex cards, Bre-B and the QR, Wenia, and the bank's own AI and fraud models.",
                "deals": "Where they meet: credit, where three networks share one book."},
    },
    "tl": [
        ["2017", "La Guajira hunger campaign with Mastercard"],
        ["Jul 2023", "Bancolombia QR opens to other banks"],
        ["Jan 2024", "Mastercard launches Click to Pay in Colombia"],
        ["Jul 2024", "Nequi El Salvador with Mastercard debit"],
        ["Oct 2024", "Nequi Visa card in Colombia"],
        ["Jan 2025", "Visa Tap to Add Card with Bancolombia"],
        ["Sep 2025", "Visa Avianca LifeMiles card"],
        ["Oct 2025", "Bre-B goes live"],
        ["May 2026", "World Legend; QR moves to Bre-B"],
        ["Jun 2026", "Banistmo sale closes"],
        ["Sep 2026", "Nequi licensed separately"],
    ],
    "l": {
        "U": {"d": 1, "s": "Debit holders carry Mastercard; credit and Nequi are split.",
              "gap": "Every debit holder and most premium clients carry Mastercard; Nequi's Colombian users carry Visa.",
              "neo": "Debit holders, about 45% of credit cardholders, World Legend clients, Nequi in El Salvador.", "snb": "Nequi users in Colombia, Visa and Amex cardholders."},
        "L5": {"d": 0, "s": "The front doors are the group's.", "gap": "Apps, branches, agents and partners are Bancolombia's and Nequi's.", "neo": "None.", "snb": "Mi Bancolombia, Negocios, Nequi, branches."},
        "L4": {"d": 1, "s": "Personal and premium banking carry Mastercard debit and much of credit.", "gap": "Nequi lending, vehicles and Central America show no Mastercard role.",
               "neo": "Personal and premium cards, the closed Sufi card.", "snb": "Nequi credit, Renting, Banco Agrícola, BAM."},
        "L3": {"d": 0, "s": "Fraud, AI and points are Bancolombia's own.", "gap": "No Mastercard fraud or AI tool is public; purchasing agents are planned with no network named.",
               "neo": "Card benefits on Mastercard tiers.", "snb": "Fraud models, AI credit, Puntos Colombia."},
        "L2": {"d": 1, "s": "Debit on Mastercard; credit split; Bre-B and Nequi elsewhere.", "gap": "Mastercard has debit and the largest credit share; Visa has Nequi and co-brands; Bre-B is account to account.",
               "neo": "Debit, transit, about 45% of credit, World Legend, Nequi El Salvador.", "snb": "Visa and Amex credit, Nequi Visa, Bre-B, QR, Wenia."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, holding, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
