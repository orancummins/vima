"""Grupo Financiero Galicia's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from galicia_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Argentina's largest private financial group as five discs that stack into one platform, from about 16% of the "
       "country's loans and deposits at the bottom to the Galicia and Naranja X apps at the top. Click the stack to open "
       "it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined "
       "in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("prem", "Éminent clients", "gem"),
    ("nx", "Naranja X customers", "wallet"),
    ("sme", "Merchants & SMEs", "store"),
    ("corp", "Corporates & agri", "factory"),
    ("inv", "Savers & investors", "trending-up"),
]
USERS_DESC = ("Six kinds of customer: 4.6 million individuals at Banco Galicia, its Éminent premium clients, Naranja X's "
              "card and app customers, merchants and SMEs, corporates and farmers, and savers in Fima funds and Inviu.")

WHO = {"con": "A Galicia customer", "prem": "An Éminent client", "nx": "A Naranja X customer", "sme": "A merchant",
       "corp": "A corporate treasurer", "inv": "A saver"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "An account, a debit card, the Galicia App with MODO and QR, and tokens and biometrics.",
     "steps": [("4.1", "retail", "Open an account"), ("2.3", "gdebit", "Pay with the debit card"), ("2.4", "galiciawallet", "Pay by QR or contactless"),
               ("5.1", "gapp", "Run it in the Galicia App"), ("3.1", "security", "Protected by token and biometrics")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "Galicia credit cards on Visa, Mastercard or Amex, with Quiero! points.",
     "steps": [("2.1", "gcredit", "Take a Galicia credit card"), ("3.3", "quiero", "Collect Quiero! points"), ("5.1", "gapp", "Pay in instalments from the app")]},
    {"id": "premium", "who": "prem", "name": "Bank as an Éminent client",
     "why": "Mastercard Black, Visa Signature or Amex Platinum, an adviser and network events.",
     "steps": [("2.1", "eminent", "Hold an Éminent card"), ("5.4", "conecta", "Talk to a Conecta adviser"), ("3.3", "experiences", "Go to a card-brand event")]},
    {"id": "naranja", "who": "nx", "name": "Join Naranja X from the app",
     "why": "A virtual card on day one, then a physical card without printed data, credit and loans.",
     "steps": [("5.2", "nxapp", "Sign up in the app"), ("3.1", "infoless", "Receive an Infoless card"), ("2.2", "nxcredit", "Use a Naranja X Visa or Mastercard"),
               ("2.3", "nxdebit", "Spend from the account with Visa debit"), ("4.2", "nxloans", "Take a loan")]},
    {"id": "merchant", "who": "sme", "name": "Get paid as a merchant",
     "why": "Nave terminals and Naranja X readers, with advances on card sales.",
     "steps": [("2.5", "nave", "Take payments with Nave"), ("2.5", "nxaccept", "Collect with Toque or TAP"), ("4.3", "sme", "Advance card receivables"),
               ("5.1", "office", "Manage it in Office Banking")]},
    {"id": "corp", "who": "corp", "name": "Finance a company or a farm",
     "why": "Wholesale lending, export finance, Nera for agri payments and corporate cards.",
     "steps": [("4.4", "wholesale", "Borrow and pre-finance exports"), ("4.3", "nera", "Pay and finance through Nera"), ("4.3", "commercial", "Equip staff with business cards")]},
    {"id": "invest", "who": "inv", "name": "Save and invest",
     "why": "Fima funds, Galicia Securities and Inviu advisers.",
     "steps": [("4.6", "fima", "Invest in Fima funds"), ("4.4", "securities", "Trade through Galicia Securities"), ("4.6", "inviu", "Use an Inviu adviser")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "A Mastercard credit book close to Visa's at the bank, a fast-growing one at Naranja X, Infoless cards, Mastercard Black and the Mexican card.",
     "steps": [("2.1", "gcredit", "2.46 million Galicia Mastercard cards"), ("1.3", "galiciamas", "The HSBC cards brought across"), ("2.2", "nxcredit", "1.13 million Naranja X Mastercard cards"),
               ("3.1", "infoless", "Infoless with Mastercard"), ("2.6", "mexico", "Naranja X Mexico on Mastercard")]},
    {"id": "mcnext", "who": "mc", "name": "Where own-brand cards, debit and risk could land",
     "why": "Where Galicia has needs and Mastercard is not yet in: 4.8 million own-brand Naranja cards, Visa debit, credit and fraud risk with NPLs of 10–20%, acquiring tools for Nave, and offers for Quiero!",
     "steps": [("2.2", "naranjabrand", "Convert own-brand Naranja cards"), ("2.3", "nxdebit", "Win debit from Visa"), ("1.1", "risk", "Fraud and credit-risk scoring"),
               ("2.5", "nave", "Merchant data and risk for Nave"), ("3.3", "quiero", "Card-linked offers for Quiero!")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Grupo Financiero Galicia's map",
    "title": "Second to Visa, and closing in at the bank",
    "lead": "Mastercard carries 3.6 million of the group's 15 million credit cards, against Visa's 6.0 million and 4.8 million on Naranja's own brand. At Banco Galicia its book doubled in 2025 as the HSBC cards came over and is now close to Visa's. At Naranja X it grows fast, it was the technology provider for the 2022 card renewal and Infoless cards, and it carries the card in Mexico. Debit and Click to Pay are Visa's at Naranja X. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (2025 Form 20-F, 16 April 2026; Q2 2026 results, 25 August 2026) or from press. Mastercard's and Visa's newsrooms were not checked; Galicia's debit network and the HSBC card migration to Mastercard are inferred.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Group credit cards", "Visa 40%, Mastercard 24%", "Naranja own brand 32%, Amex 4%"],
        ["Banco Galicia", "Mastercard 2.46m", "Visa 3.01m; Mastercard up 101% in 2025"],
        ["Naranja X", "Mastercard 1.13m", "Up 253% in 2024; Visa 2.97m"],
        ["Debit", "Visa", "Naranja X confirmed; Galicia believed ⚠"],
        ["Card issuing", "Mastercard", "2022 renewal, Infoless 2025"],
        ["Click to Pay", "Visa", "Certified at Naranja X, 2025"],
        ["Mexico", "Mastercard", "Naranja X credit card, 2026"],
    ],
    "sides": {
        "neo": {"dir": "Galicia and Naranja X credit cards, Mastercard Black, Infoless issuing, the Mexican card and acceptance on Nave and Naranja X terminals.",
                "deals": "What it does not do: debit, own-brand Naranja cards, Click to Pay, MODO, fraud scoring or loyalty."},
        "snb": {"dir": "Visa's larger credit book, debit and Click to Pay, Naranja's closed loop, Amex at the top end, and MODO and QR on bank accounts.",
                "deals": "Where they meet: every Galicia and Naranja X customer chooses between Visa and Mastercard."},
    },
    "tl": [
        ["Feb 2020", "Galicia Mastercard on Garmin watches"],
        ["Sep 2022", "Naranja X renews 10m+ cards with Mastercard technology"],
        ["2024", "Naranja X Mastercard cards up 253%"],
        ["Dec 2024", "HSBC Argentina bought"],
        ["Jun 2025", "Galicia Más merged; 1.5m cards migrated"],
        ["2025", "Infoless with Mastercard; Visa Click to Pay at Naranja X"],
        ["2025", "Galicia Mastercard book doubles to 2.46m"],
        ["Jun 2026", "Naranja X Mastercard card in Mexico"],
    ],
    "l": {
        "U": {"d": 1, "s": "Mastercard holders sit beside Visa, Amex and Naranja holders.",
              "gap": "About a quarter of the group's credit cards are Mastercard; debit holders carry Visa.",
              "neo": "Galicia and Naranja X Mastercard holders, Éminent Black clients, Naranja X in Mexico.", "snb": "Visa holders, debit holders, Naranja own-brand holders, Amex holders."},
        "L5": {"d": 0, "s": "The front doors are the group's.", "gap": "Apps, branches and advisers are Galicia's and Naranja X's.", "neo": "None.", "snb": "Galicia App, Naranja X app, branches, Conecta."},
        "L4": {"d": 0, "s": "The business lines carry no network.", "gap": "Lending, insurance and funds have no network role; business cards are Visa.",
               "neo": "None.", "snb": "Retail and wholesale lending, Naranja X loans, Galicia Seguros, Fima, Visa Business."},
        "L3": {"d": 1, "s": "Infoless issuing is Mastercard's; the rest is Galicia's.", "gap": "Infoless was built with Mastercard; fraud, AI and loyalty have no named Mastercard role.",
               "neo": "Infoless, Mastercard client events.", "snb": "Token and biometrics, AI agents, Quiero!, Visa and Amex events."},
        "L2": {"d": 1, "s": "Mastercard in credit and Mexico; Visa in debit and the larger credit book.", "gap": "Visa leads credit and holds debit; Naranja's own brand needs no network.",
               "neo": "Galicia and Naranja X Mastercard, Naranja X Mexico, acceptance on Nave.", "snb": "Visa credit and debit, Naranja own brand, Amex, MODO."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, families, brands, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
