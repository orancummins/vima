"""Vietcombank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from vietcombank_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Vietnam's most profitable bank as five discs that stack into one platform, from VND 2.66 quadrillion of assets "
       "and a state owner at the bottom to VCB Digibank, 667 branches and offices and co-brand partners at the top. Click "
       "the stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up across "
       "the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("young", "Young digital customers", "smartphone"),
    ("aff", "Priority customers", "gem"),
    ("travel", "Travellers & families abroad", "plane"),
    ("home", "Homebuyers", "house"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates & FDI firms", "factory"),
]
USERS_DESC = ("Seven kinds of customer: everyday account holders, young customers who live in the app, priority clients, "
              "travellers and families sending money home, homebuyers, small businesses, and the corporates and FDI firms "
              "the foreign-trade bank was built for. Vietcombank does not publish a total customer count.")

WHO = {"con": "A Vietcombank customer", "young": "A young customer", "aff": "A priority client", "travel": "A traveller",
       "home": "A homebuyer", "sme": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a Connect24 card on NAPAS, VietQR transfers, a phone wallet and biometric checks.",
     "steps": [("4.1", "deposits", "Open an account"), ("2.2", "connect24", "Get a Connect24 card"), ("5.1", "digibank", "Run it in VCB Digibank"),
               ("2.5", "napas247", "Pay by VietQR"), ("2.3", "wallets", "Tap with Apple Pay"), ("3.1", "security", "Confirm with a face scan")]},
    {"id": "digital", "who": "young", "name": "Get a card in a minute",
     "why": "A card-less Visa DigiCard in the app, Click to Pay online and points for spending.",
     "steps": [("5.1", "digibank", "Open VCB Digibank"), ("2.2", "visadebit", "Issue a DigiCard"), ("2.3", "ctp", "Check out with Click to Pay"),
               ("3.3", "rewards", "Earn VCB Rewards")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "Visa, Mastercard, Amex or JCB credit, with 0% instalments.",
     "steps": [("2.1", "visacredit", "Take a Visa credit card"), ("2.1", "mccredit", "Or a Mastercard"), ("3.4", "install", "Split a purchase at 0%"),
               ("3.3", "rewards", "Redeem points")]},
    {"id": "travel", "who": "travel", "name": "Spend and send abroad",
     "why": "Travel cards with overseas cashback, network offers, and remittances home.",
     "steps": [("2.1", "amex", "Carry a Vietnam Airlines Amex"), ("2.1", "mccredit", "Or World Mastercard"), ("3.3", "offers", "Use offers abroad"),
               ("2.5", "xqr", "Scan VietQR in Thailand or Laos"), ("2.6", "remit", "Send money home")]},
    {"id": "priority", "who": "aff", "name": "Grow wealth",
     "why": "Priority banking, insurance and investments through the group.",
     "steps": [("4.2", "priority", "Join priority banking"), ("4.2", "banca", "Insure with FWD"), ("4.5", "vcbs", "Invest through VCBS")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "A home loan from the branch network.",
     "steps": [("5.3", "branches", "Visit a branch"), ("4.1", "retailloans", "Take a home loan"), ("4.2", "banca", "Protect it")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "DigiBiz, card acceptance, QR collections and leasing.",
     "steps": [("5.2", "digibiz", "Bank in DigiBiz"), ("2.4", "acquiring", "Take cards"), ("2.5", "napas247", "Collect by VietQR"),
               ("4.5", "leasing", "Lease equipment")]},
    {"id": "corp", "who": "corp", "name": "Trade across borders",
     "why": "The foreign-trade bank's core: trade finance, FX and cash management.",
     "steps": [("4.3", "corporate", "Bank as an FDI firm"), ("2.6", "trade", "Finance trade and FX"), ("5.2", "cashup", "Manage cash in CashUp")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Two Mastercard credit cards, a debit card, acquiring for visitors and offers abroad.",
     "steps": [("2.1", "mccredit", "Mastercard and World Mastercard credit"), ("2.2", "mcdebit", "Mastercard debit ⚠"),
               ("2.4", "acquiring", "Leading acquirer for global travellers"), ("3.3", "offers", "Mastercard offers abroad")]},
    {"id": "mcnext", "who": "mc", "name": "Where tokens, Move and commercial cards could land",
     "why": "Where Vietcombank has needs and Mastercard is not yet in: tokens and Click to Pay for its cards, remittances, commercial cards in the new corporate platform, fraud and identity, and a carbon view.",
     "steps": [("2.3", "wallets", "Mastercard tokens in Apple Pay and Google Wallet"), ("2.3", "ctp", "Click to Pay beyond Visa"),
               ("2.6", "remit", "Mastercard Move for VCB Money"), ("5.2", "cashup", "Commercial and virtual cards in Corporate DigiBank"),
               ("3.1", "security", "Fraud and identity tools"), ("3.5", "green", "Carbon Calculator")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Vietcombank's map",
    "title": "Five card brands, Visa first, NAPAS and VietQR at home",
    "lead": "Vietcombank issues Visa, Mastercard, Amex and JCB, and NAPAS's domestic Connect24 card sits on every account. Visa is the default for new cards and came first to Google Wallet (2022), Apple Pay (2023) and Click to Pay (March 2026). Mastercard keeps two credit cards and a debit card, and ranks Vietcombank first for merchant acceptance and visitor acquiring (December 2025). Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (H1 2026 results, 31 July 2026; 2025 results at the AGM, 24 April 2026; 2024 annual report) or from Vietcombank's card pages, NAPAS and Vietnamese press, translated. No network agreement is public; card counts and app users are not published.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Domestic debit", "NAPAS", "Connect24 on every account"],
        ["International debit", "Visa", "DigiCard, eVer-link, MeGO"],
        ["Credit", "Visa, Amex, Mastercard, JCB", "Two Mastercard cards of about nine"],
        ["Wallets", "Visa first", "Google 2022, Apple 2023; Mastercard ⚠"],
        ["Click to Pay", "Visa", "March 2026"],
        ["Acquiring", "All brands", "Mastercard's top acquirer for visitors, 2025"],
        ["Transfers", "NAPAS & VietQR", "32m a day in 2025"],
        ["Agreements", "None public", "Awards only ⚠"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard and World Mastercard credit, Mastercard debit, acquiring for visitors and Mastercard offers abroad.",
                "deals": "What it does not do: the default debit card, wallets and Click to Pay in public, transfers, remittances or commercial cards."},
        "snb": {"dir": "Visa for new debit, credit, wallets and Click to Pay; NAPAS for Connect24 and VietQR; Amex for premium travel; JCB for Japan.",
                "deals": "Where they meet: acceptance at 121,000 points, which takes every brand."},
    },
    "tl": [
        ["Nov 2015", "Mastercard debit issuance and payment awards"],
        ["Nov 2022", "Google Wallet for Visa cards"],
        ["Aug 2023", "Apple Pay launches with Visa"],
        ["Oct 2024", "Takes over Construction Bank (VCBNeo)"],
        ["Mar 2025", "Lê Quang Vinh becomes CEO"],
        ["Oct 2025", "Eight Visa awards"],
        ["Dec 2025", "Three Mastercard awards"],
        ["Mar 2026", "Click to Pay for Visa cards"],
        ["Aug 2026", "Corporate DigiBank with Virtusa"],
        ["Sep 2026", "Visa MeGO for Hanoi Metro"],
    ],
    "l": {
        "U": {"d": 1, "s": "Some cardholders carry Mastercard; most carry NAPAS and Visa.",
              "gap": "Every account gets a NAPAS card and new digital customers get Visa; Mastercard reaches World and standard credit and some debit holders.",
              "neo": "Mastercard credit and debit holders, visitors paying at Vietcombank merchants.", "snb": "Connect24 and Visa debit holders, Amex and JCB travellers, VietQR users."},
        "L5": {"d": 0, "s": "The front doors are Vietcombank's.", "gap": "VCB Digibank, DigiBiz, CashUp and branches are the bank's; co-brands are Visa, Amex and NAPAS.",
               "neo": "None.", "snb": "Apps, branches, co-brands."},
        "L4": {"d": 0, "s": "The business lines carry NAPAS and Visa.", "gap": "Accounts come with Connect24; commercial volume is Visa's; loans, insurance and markets have no network role.",
               "neo": "Premium cards for priority clients, in part.", "snb": "Accounts, loans, FWD, corporate banking, VCBS."},
        "L3": {"d": 1, "s": "Mastercard offers and instalments; the rest is the bank's.", "gap": "Offers and instalments run on every brand; fraud, data, rewards and green are the bank's own or Visa's.",
               "neo": "Offers abroad, instalments.", "snb": "Security, data platform, VCB Rewards, MeGO carbon view."},
        "L2": {"d": 1, "s": "Mastercard credit, debit and acquiring; Visa and NAPAS lead.", "gap": "Visa has new cards, wallets first and Click to Pay; NAPAS has Connect24 and VietQR; Mastercard has three cards and visitor acquiring.",
               "neo": "Mastercard credit and debit, acquiring.", "snb": "Visa cards and tokens, NAPAS, VietQR, Amex, JCB, remittances."},
        "L1": {"d": 0, "s": "The state's and the bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, ownership, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
