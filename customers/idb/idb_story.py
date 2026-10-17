"""International Development Bank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from idb_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("An Iraqi private bank as five discs that stack into one platform, from about USD 2.4 billion of assets and card "
       "licences from both Mastercard and Visa at the bottom to 27 branches and the e-IDB app at the top. Click the stack "
       "to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Salaried customers", "user-round"),
    ("prem", "Credit cardholders", "gem"),
    ("trav", "Travellers & tourists", "plane"),
    ("merch", "Merchants", "store"),
    ("corp", "Corporates & traders", "factory"),
    ("gov", "Government & employers", "landmark"),
]
USERS_DESC = ("Six kinds of customer, with no customer count published: salaried customers, credit cardholders, travellers "
              "and Arab tourists, merchants on about 5,000 terminals, corporates trading with Iraq and the UAE, and the "
              "government bodies and employers whose salaries it pays.")

WHO = {"con": "An IDB customer", "prem": "A credit cardholder", "trav": "A traveller", "merch": "A merchant",
       "corp": "A corporate treasurer", "gov": "A government employer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Get paid and spend",
     "why": "The everyday loop: a salary account, a Visa debit card, the ATM network and the app.",
     "steps": [("3.3", "salaries", "Receive a salary"), ("4.1", "accounts", "Hold an account"), ("2.1", "visaclassic", "Pay with Visa debit"),
               ("2.5", "atms", "Withdraw free at IDB ATMs"), ("5.2", "mobile", "Check it in the app")]},
    {"id": "credit", "who": "prem", "name": "Borrow on a card",
     "why": "The Mastercard Gold credit card, IDB's one named credit product.",
     "steps": [("5.1", "branches", "Apply in a branch"), ("2.2", "mcgold", "Take a Mastercard Gold card"), ("3.2", "protection", "Get SMS alerts")]},
    {"id": "travel", "who": "trav", "name": "Travel and visit Iraq",
     "why": "Visa Platinum lounges for Iraqis abroad and the Arab Tourist Card for visitors, both limited by the dollar bar.",
     "steps": [("2.1", "visaplat", "Travel with Visa Platinum"), ("3.1", "benefits", "Use lounges and discounts"),
               ("2.3", "arabtourist", "Visit on the Arab Tourist Card"), ("1.4", "usdbar", "Hit the dollar limits")]},
    {"id": "merchant", "who": "merch", "name": "Take card payments",
     "why": "Acquiring on about 5,000 terminals as the CBI pushes cash out.",
     "steps": [("2.4", "acquiring", "Take cards on an IDB terminal"), ("2.7", "switch", "Route through the national switch"), ("4.1", "accounts", "Settle to an account")]},
    {"id": "corp", "who": "corp", "name": "Finance a business in Iraq",
     "why": "Corporate lending, cash management and trade finance.",
     "steps": [("4.2", "corplending", "Borrow"), ("4.2", "cashmgmt", "Manage cash"), ("4.3", "tradefin", "Trade through correspondents")]},
    {"id": "uae", "who": "corp", "name": "Invest from the UAE",
     "why": "The Dubai branch for UAE firms working in Iraq.",
     "steps": [("4.5", "dubai", "Bank in Dubai"), ("4.6", "logistics", "Use logistics partners"), ("4.4", "treasury", "Use treasury services")]},
    {"id": "payroll", "who": "gov", "name": "Pay public salaries",
     "why": "Salary domiciliation for federal and Kurdistan employers, and the lost MyAccount mandate.",
     "steps": [("5.3", "partners", "Sign a salary programme"), ("3.3", "salaries", "Pay salaries into IDB accounts"), ("3.3", "myaccount", "MyAccount, ended 2025")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The issuing and acquiring licence, the Gold credit card, acceptance on IDB terminals and ATMs, and the Arab Tourist Card.",
     "steps": [("1.3", "cardlic", "Mastercard issuing and acquiring licence"), ("2.2", "mcgold", "Mastercard Gold credit"),
               ("2.4", "acquiring", "Acceptance on 5,000 terminals"), ("2.3", "arabtourist", "Named on the Arab Tourist Card ⚠")]},
    {"id": "mcnext", "who": "mc", "name": "Where salary cards, tokens and tourism could land",
     "why": "Where IDB has needs and Mastercard is not yet in: debit for salary customers, tokenised cards in the app, fraud tools, acquirer risk, tourism offers and compliance help with the dollar bar.",
     "steps": [("3.3", "salaries", "Mastercard debit for salary customers"), ("5.2", "mobile", "Tokenised cards ahead of Apple Pay"),
               ("3.2", "fraud", "Fraud and identity scoring"), ("2.4", "acquiring", "Acquirer risk tools"),
               ("2.3", "arabtourist", "Tourism offers on the Arab Tourist Card"), ("1.4", "usdbar", "Compliance advisory")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across the International Development Bank's map",
    "title": "Licensed by Mastercard, issuing mostly on Visa, cut off from the dollar",
    "lead": "IDB holds issuing and acquiring licences from both Mastercard and Visa. Its debit cards are Visa Classic and Platinum, its one named credit card is a Mastercard Gold, and its terminals and ATMs take both. In September 2025 it was reported among the Iraqi banks barred from US-dollar business, which restricts international card use on any network. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "IDB's website was behind bot protection in October 2026, so card details come from search extracts of its pages and figures from third parties. No 2025 or 2026 results, card counts or network split were found.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa", "Classic and Platinum"],
        ["Credit", "Mastercard", "Gold, IQD 6–12m limit"],
        ["Licences", "Mastercard and Visa", "Issuing and acquiring, from 2016 ⚠"],
        ["Acquiring", "Both networks", "About 5,000 terminals, May 2024"],
        ["Tourist card", "Visa and Mastercard ⚠", "Launched May 2025"],
        ["Dollar access", "Barred", "Reported Sep 2025 ⚠ status"],
        ["Market", "Qi Card", "16m people; Mastercard, Visa, UnionPay"],
    ],
    "sides": {
        "neo": {"dir": "The Gold credit card, acceptance on IDB terminals and ATMs, a share of the Arab Tourist Card, and the CBI partnership above the bank.",
                "deals": "What it does not have: debit, prepaid, sponsorship offers, tokenisation, fraud tools or salary cards."},
        "snb": {"dir": "Visa debit, prepaid and promotions, the CBI's national switch and card scheme, Qi Card's scale, and the dollar bar that limits every network abroad.",
                "deals": "Where they meet: acquiring and the Arab Tourist Card, where both networks are named."},
    },
    "tl": [
        ["2011", "IDB founded"],
        ["2016", "Mastercard and Visa licence process begins ⚠"],
        ["Aug 2018", "Mastercard memorandum with the Central Bank of Iraq"],
        ["Apr 2021", "Mastercard partnership with the CBI"],
        ["Nov 2022", "Dubai branch opens"],
        ["Sep 2023", "Arab Tourism Organization deal: a Visa prepaid card"],
        ["May 2024", "27th branch; 400 ATMs, 5,000 terminals"],
        ["May 2025", "Arab Tourist Card launched"],
        ["Aug 2025", "CBI sets out a national switch and card scheme"],
        ["Sep 2025", "Removed from MyAccount; dollar bar reported"],
    ],
    "l": {
        "U": {"d": 1, "s": "Credit cardholders carry Mastercard; debit holders carry Visa.",
              "gap": "Salaried customers hold Visa debit; the Gold credit card is Mastercard; tourists may hold either.",
              "neo": "Gold credit cardholders, some tourist cards.", "snb": "Debit and prepaid holders, salary customers."},
        "L5": {"d": 0, "s": "The front doors are IDB's.", "gap": "Branches, the app and partners have no network role; no wallet tokens.",
               "neo": "None.", "snb": "Branches, e-IDB, partners."},
        "L4": {"d": 0, "s": "The business lines carry no Mastercard product.", "gap": "Accounts come with Visa debit; lending, trade and the Dubai branch have no card role.",
               "neo": "None.", "snb": "Accounts, lending, trade, treasury, Dubai."},
        "L3": {"d": 0, "s": "Benefits are Visa's; the rest is IDB's or nothing public.", "gap": "Visa supplies benefits and promotions; no fraud or AI tools are published.",
               "neo": "None.", "snb": "Visa benefits and promotions, salaries, protection."},
        "L2": {"d": 1, "s": "Mastercard credit and acceptance; Visa debit and prepaid.", "gap": "Mastercard has the Gold card and acceptance; Visa has debit and prepaid; the CBI builds national rails.",
               "neo": "Gold credit, acquiring, ATMs, tourist card ⚠.", "snb": "Visa debit and prepaid, national switch, transfers."},
        "L1": {"d": 1, "s": "A Mastercard licence in the foundation.", "gap": "The issuing and acquiring licence is Mastercard's as well as Visa's; capital, leadership and the dollar bar are IDB's.",
               "neo": "Card licence.", "snb": "Capital, leadership, UAE licence, dollar bar."},
    },
    "t": area_lens(LAYERS),
}
