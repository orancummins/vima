"""Grupo Financiero Banorte's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from banorte_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Mexico's second-largest financial group as five discs that stack into one platform, from Ps 1.27 trillion of "
       "loans and a bank founded in Monterrey in 1899 at the bottom to Banorte Móvil, 1,229 branches and 46,191 "
       "correspondents at the top. Click the stack to open it. Choose who you are and what you want to do, and the "
       "areas that deliver it light up across the layers, joined in the order they act. Switch to the Mastercard lens "
       "to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday Mexicans", "user-round"),
    ("young", "Young digital customers", "smartphone"),
    ("aff", "Premium & travel cardholders", "gem"),
    ("home", "Homebuyers & car buyers", "house"),
    ("sme", "Small businesses & merchants", "briefcase"),
    ("corp", "Companies & governments", "factory"),
    ("saver", "Savers & Afore members", "coins"),
]
USERS_DESC = ("Seven kinds of customer, 13.5 million banking clients and 8 million Afore members in all: everyday account "
              "and payroll customers, young RappiCard and app users, premium and travel cardholders, homebuyers and car "
              "buyers, small businesses and merchants, companies and governments, and savers.")

WHO = {
    "con": "A Banorte customer", "young": "A young customer", "aff": "A premium cardholder", "home": "A borrower", "sme": "A small business", "corp": "A company treasurer", "saver": "A saver",
}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "A payroll account, a debit card, Banorte Móvil, SPEI transfers and Maya.",
     "steps": [("4.3", "payroll", "Get paid into a payroll account"), ("2.4", "debit", "Pay with a debit card"),
               ("5.1", "app", "Run it in Banorte Móvil"), ("2.7", "spei", "Send money by SPEI"),
               ("3.2", "maya", "Ask Maya"), ("3.1", "fraud", "Protected by True ID")]},
    {"id": "young", "who": "young", "name": "Get a first card in an app",
     "why": "RappiCard inside Rappi, or OneUp and Banorte Conmigo, then a wallet.",
     "steps": [("5.3", "partners", "Find Banorte inside Rappi"), ("2.3", "rappicard", "Take a RappiCard"),
               ("2.1", "conmigo", "Or a OneUp card"), ("2.5", "wallets", "Add it to a wallet")]},
    {"id": "travel", "who": "aff", "name": "Earn on travel",
     "why": "Marriott on Mastercard, United and Infinite cards, and points.",
     "steps": [("2.2", "marriott", "Earn Bonvoy points"), ("2.2", "united", "Or United miles"),
               ("2.1", "premium", "Use an Infinite card's lounges"), ("3.3", "rewards", "Redeem Recompensa Total")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "The second-largest mortgage lender, with insurance from Seguros Banorte.",
     "steps": [("5.2", "branches", "Apply in a branch"), ("4.1", "mortgages", "Take a mortgage"),
               ("4.6", "seguros", "Insure it")]},
    {"id": "drive", "who": "home", "name": "Finance a car",
     "why": "Quotes inside dealer portals, and Hyundai's main finance partner.",
     "steps": [("5.3", "partners", "Visit a dealer"), ("3.2", "apis", "Get a quote by API"), ("4.2", "auto", "Take a car loan")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "SME loans, card acceptance on 269,000 terminals, and a bank feed into CONTPAQi.",
     "steps": [("4.4", "sme", "Borrow for the business"), ("2.6", "acquiring", "Take cards"),
               ("3.2", "apis", "Feed CONTPAQi"), ("2.7", "spei", "Pay suppliers by SPEI")]},
    {"id": "corp", "who": "corp", "name": "Bank a company or a state",
     "why": "Commercial, corporate and government lending, and Amex corporate cards.",
     "steps": [("4.5", "corporate", "Borrow and trade"), ("4.5", "government", "Refinance public debt"),
               ("4.5", "corpcards", "Issue corporate cards")]},
    {"id": "save", "who": "saver", "name": "Save for retirement",
     "why": "Afore XXI Banorte, annuities, insurance and funds.",
     "steps": [("4.6", "afore", "Save in Afore XXI Banorte"), ("4.6", "funds", "Invest in funds"),
               ("5.1", "app", "See it in the app")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The Marriott co-brand, Mujer Banorte and World Elite debit, partner prepaid cards, Priceless, and acceptance.",
     "steps": [("2.2", "marriott", "Marriott Bonvoy on Mastercard"), ("2.4", "mujer", "Mujer Banorte debit"),
               ("2.4", "worldelite", "World Elite debit"), ("2.4", "partnerdebit", "Amazon Recargable"),
               ("3.3", "rewards", "Priceless experiences"), ("2.6", "acquiring", "Acceptance at Banorte merchants")]},
    {"id": "mcnext", "who": "mc", "name": "Where RappiCard, tokens and agents could land",
     "why": "Where Banorte has needs and Mastercard is not yet in: RappiCard's rebuild, wallet tokens, scam scoring on SPEI, Maya as a buying agent, remittances and corporate cards.",
     "steps": [("2.3", "rappicard", "Win RappiCard's next reissue"), ("2.5", "wallets", "Token services and Click to Pay"),
               ("3.1", "fraud", "Scam scoring on transfers"), ("3.2", "maya", "Agent Pay for Maya"),
               ("2.7", "uniteller", "Move for remittances"), ("4.5", "corpcards", "Commercial and virtual cards")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Grupo Financiero Banorte's map",
    "title": "A Visa-led issuer with Mastercard on debit and a hotel card",
    "lead": "Banorte's core Clásica and Oro credit cards and its 1.3 million RappiCards are on Visa, Visa controls Prosa, in which Banorte holds 19.73%, and American Express issues its corporate cards. Mastercard carries the Marriott Bonvoy co-brand, the Mujer Banorte and World Elite debit cards with Priceless, and Amazon Recargable. No network agreement or volume split is public. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (2T26 report and 2Q26 presentation, July 2026; 2025 annual report). banorte.com and Mastercard's newsroom could not be read; networks come from Banorte's reports and press, and several are unconfirmed.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Core credit", "Visa", "Clásica and Oro, 2024"],
        ["RappiCard", "Visa", "1.3 million cards; Banorte's since Dec 2025"],
        ["Co-brand", "Mastercard", "Marriott Bonvoy, 2021 ⚠"],
        ["Debit", "Split", "Mujer Banorte and World Elite on Mastercard; Visa Platinum"],
        ["Prepaid", "Mastercard", "Amazon Recargable, 2018"],
        ["Processor", "Prosa", "Visa 51%; Banorte 19.73%"],
        ["Corporate cards", "American Express", "Since 2008 ⚠"],
        ["Acquiring", "All networks", "268,877 POS; Amex OptBlue"],
    ],
    "sides": {
        "neo": {"dir": "The Marriott co-brand, Mujer Banorte and World Elite debit, Amazon Recargable and Socio 7, Priceless, and acceptance at Banorte's merchants.",
                "deals": "What it does not do: core credit, RappiCard, corporate cards, processing, transfers or remittances."},
        "snb": {"dir": "Visa on Clásica, Oro, Infinite, RappiCard and Platinum debit, and control of Prosa; American Express on corporate cards and OptBlue; Banxico's SPEI; UniTeller.",
                "deals": "Where they meet: debit, wallets and acceptance, where both networks run."},
    },
    "tl": [
        ["Jul 2008", "American Express issues corporate cards"],
        ["Feb 2018", "Socio 7 debit with 7-Eleven ⚠"],
        ["Mar 2018", "Amazon Recargable on Mastercard"],
        ["Jan 2021", "RappiCard on Visa"],
        ["Apr 2021", "Marriott Bonvoy cards on Mastercard ⚠"],
        ["Dec 2023", "Visa agrees to buy 51% of Prosa"],
        ["Dec 2025", "RappiCard fully Banorte's"],
        ["Jul 2026", "New CFO; COO leads AI"],
    ],
    "l": {
        "U": {"d": 1, "s": "Marriott, Mujer Banorte and World Elite holders carry Mastercard.",
              "gap": "Core credit and RappiCard holders carry Visa; Mastercard reaches premium travellers and some debit customers.",
              "neo": "Marriott cardholders, Mujer Banorte and World Elite debit, Amazon Recargable.", "snb": "Clásica, Oro and RappiCard holders, corporates, savers."},
        "L5": {"d": 0, "s": "The front doors are Banorte's.", "gap": "App, branches, ATMs and correspondents are the group's; ATMs on Visa/Plus.",
               "neo": "None.", "snb": "Banorte Móvil, branches, ATMs, OXXO and partners."},
        "L4": {"d": 0, "s": "The business lines have no network role.", "gap": "Lending, insurance and the Afore are network-neutral; corporate cards are Amex.",
               "neo": "None.", "snb": "Mortgages, auto, payroll, SME, government, Amex corporate cards."},
        "L3": {"d": 1, "s": "Priceless on Mastercard programmes; the rest is Banorte's.", "gap": "Fraud, Maya and APIs are Banorte's own; loyalty uses Priceless.",
               "neo": "Priceless experiences.", "snb": "True ID, Cleafy, Maya, Recompensa Total."},
        "L2": {"d": 1, "s": "Visa on core credit and RappiCard; Mastercard on the hotel card and some debit.", "gap": "Visa leads credit and controls Prosa; Mastercard holds Marriott, Mujer Banorte, World Elite and prepaid.",
               "neo": "Marriott, Mujer Banorte, World Elite, Amazon Recargable, acceptance.", "snb": "Clásica, Oro, RappiCard, Prosa, SPEI, UniTeller."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's; the Prosa stake ties Banorte to Visa.",
               "neo": "None.", "snb": "Capital, ownership, technology, strategy, Prosa stake."},
    },
    "t": area_lens(LAYERS),
}
