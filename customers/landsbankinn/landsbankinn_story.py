"""Landsbankinn's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from landsbankinn_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Iceland's largest bank as five discs that stack into one platform, from ISK 2.4 trillion of assets and a 98.2% state "
       "owner at the bottom to the app, 34 branches and partners at the top. Click the stack to open it. Choose who you are "
       "and what you want to do, and the areas that deliver it light up across the layers, joined in the order they act. "
       "Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("young", "Young people", "graduation-cap"),
    ("home", "Homebuyers", "house"),
    ("inv", "Savers & investors", "coins"),
    ("sme", "Small businesses & merchants", "store"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Six kinds of customer: about 132,800 active retail customers, young people from age 9, homebuyers, savers and "
              "investors, and 18,305 corporate customers from shops taking cards to fisheries and builders.")

WHO = {"con": "A Landsbankinn customer", "young": "A young customer", "home": "A homebuyer", "inv": "A saver",
       "sme": "A merchant", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a Visa debit card in the phone, the app, Ellí and the fraud hotline.",
     "steps": [("4.1", "accounts", "Open an account"), ("2.1", "debit", "Pay with Visa debit"), ("2.4", "wallets", "Add it to Apple Pay or Google Pay"),
               ("5.1", "app", "Run it in the app"), ("3.2", "elli", "Ask Ellí"), ("3.1", "fraud", "Call the fraud hotline")]},
    {"id": "travel", "who": "con", "name": "Earn on a credit card",
     "why": "Visa credit cards that earn Aukakrónur or Saga Points, with Click to Pay online.",
     "steps": [("2.2", "credit", "Take a credit card"), ("2.2", "saga", "Collect Saga Points"), ("3.3", "aukakronur", "Or collect Aukakrónur"),
               ("2.4", "c2p", "Pay online with Click to Pay"), ("3.4", "cardops", "Manage the card in the app")]},
    {"id": "young", "who": "young", "name": "Start banking young",
     "why": "Free debit cards to age 24, pocket-money cards and double Aukakrónur in summer.",
     "steps": [("2.1", "youth", "Get a first card"), ("2.3", "prepaid", "Top up a pocket-money card"), ("5.1", "app", "Use the app"),
               ("3.3", "aukakronur", "Collect Aukakrónur")]},
    {"id": "home", "who": "home", "name": "Buy a first home",
     "why": "Digital mortgage applications, most new loans to first-time buyers, and TM to insure the home.",
     "steps": [("5.1", "app", "Apply in the app"), ("4.2", "mortgages", "Take a mortgage"), ("4.5", "tm", "Insure it with TM")]},
    {"id": "save", "who": "inv", "name": "Save and invest",
     "why": "Smart Savings with round-ups from card spending, and Landsbréf funds.",
     "steps": [("4.1", "savings", "Save with round-ups"), ("4.4", "landsbref", "Invest in Landsbréf funds"), ("3.3", "vild", "Earn Vild rewards")]},
    {"id": "merchant", "who": "sme", "name": "Take card payments",
     "why": "Landsbankinn Acquiring, three years old and 27% of the market, taking Visa and Mastercard in store and online.",
     "steps": [("4.3", "corpnb", "Bank online"), ("2.5", "acquiring", "Take cards on a Verifone terminal"), ("2.5", "ecom", "Sell online and in-app"),
               ("3.5", "apis", "Book settlements by API"), ("3.3", "aukakronur", "Join Aukakrónur as a partner")]},
    {"id": "corp", "who": "corp", "name": "Run a corporate's money",
     "why": "Corporate lending, Visa business cards and cross-border payments.",
     "steps": [("4.3", "corporate", "Borrow for fisheries or construction"), ("2.3", "bizcards", "Issue Visa business cards"),
               ("2.6", "crossborder", "Pay abroad by SWIFT or SEPA"), ("4.4", "cf", "Raise capital with Corporate Finance")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Acceptance only: Landsbankinn's acquiring takes Mastercard cards, and Click to Pay uses a standard shared with the schemes.",
     "steps": [("2.5", "acquiring", "Mastercard accepted at 27% of the market"), ("2.5", "ecom", "Mastercard accepted online"),
               ("2.4", "c2p", "Click to Pay, a shared standard")]},
    {"id": "mcnext", "who": "mc", "name": "Where merchants, scams and loyalty could land",
     "why": "Where Landsbankinn has needs and Mastercard is not yet in: merchant risk and disputes for a fast-growing acquirer, scam tools, card-linked offers, prepaid cards with no network named, and the next card tender.",
     "steps": [("2.5", "acquiring", "Merchant risk and dispute tools"), ("3.1", "fraud", "Scam scoring on transfers"),
               ("3.3", "aukakronur", "Card-linked offers"), ("2.3", "prepaid", "Prepaid cards with Yayland"), ("2.2", "credit", "A credit range at reissue")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Landsbankinn's map",
    "title": "A Visa issuer where Mastercard only shows up at the till",
    "lead": "Every sign points to Landsbankinn's debit, credit and business cards being Visa, with bills produced by Rapyd, formerly Valitor. Separate Mastercard credit-card terms were dropped in 2019. Mastercard's place is acceptance: the bank's acquiring business, launched in 2023 and now 27% of the market, takes Mastercard and Visa. No joint initiative is public. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (H1 2026 results, 23 July 2026; 2025 annual report). No Landsbankinn page names a card network; Visa is inferred from the price list, card artwork and the Visa emergency line. The prepaid network is not stated.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa", "Inferred; free to age 24"],
        ["Credit", "Visa ⚠", "Mastercard terms dropped 2019"],
        ["Business cards", "Visa", "Business and Business Premium"],
        ["Prepaid", "Not stated ⚠", "Yayland since June 2025"],
        ["Acquiring", "Visa & Mastercard", "27% share, Q1 2026"],
        ["Processing", "Rapyd (ex-Valitor)", "Visa bills since 2023"],
        ["Click to Pay", "Visa cards", "End-2025"],
        ["Domestic rail", "Central Bank A2A", "Planned ⚠"],
    ],
    "sides": {
        "neo": {"dir": "Acceptance of Mastercard cards across Landsbankinn's merchants, in store and online.",
                "deals": "What it does not do: any card Landsbankinn issues, processing, fraud tools, loyalty or AI."},
        "snb": {"dir": "Visa debit, credit and business cards, Rapyd processing, Verifone terminals, the bank's own fraud hotline, Ellí, Aukakrónur and Vild.",
                "deals": "Where they meet: the acquiring business, which takes both."},
    },
    "tl": [
        ["Mar 2019", "Separate Visa and Mastercard credit terms merged and dropped"],
        ["Nov 2021", "Verified by Visa codes sent by Valitor"],
        ["2023", "Acquiring launched, taking Visa and Mastercard"],
        ["Apr 2023", "Visa bills from Rapyd Europe"],
        ["Jan 2025", "Central Bank plans a domestic payment option ⚠"],
        ["Feb 2025", "TM bought"],
        ["Jun 2025", "Yayland takes over prepaid cards"],
        ["End-2025", "Click to Pay; acquiring at 25%"],
        ["Q1 2026", "Acquiring at 27%"],
        ["Summer 2026", "Vild loyalty programme"],
    ],
    "l": {
        "U": {"d": 0, "s": "Customers carry Visa cards.", "gap": "Debit, credit and business cardholders carry Visa; Mastercard reaches merchants, not cardholders.",
              "neo": "Merchants accepting Mastercard.", "snb": "Every cardholder, homebuyer, saver and TM customer."},
        "L5": {"d": 0, "s": "The front doors are the bank's.", "gap": "App, online banking, branches and partners are Landsbankinn's.", "neo": "None.", "snb": "App, branches, Icelandair, Verifone, Rapyd."},
        "L4": {"d": 0, "s": "The business lines carry Visa cards.", "gap": "Accounts come with Visa debit; mortgages, funds and TM have no network role.",
               "neo": "None.", "snb": "Accounts, mortgages, corporate lending, Landsbréf, TM."},
        "L3": {"d": 0, "s": "Services are the bank's own or Visa's.", "gap": "Fraud hotline, Ellí, Aukakrónur and Vild are Landsbankinn's; processing is Rapyd's for Visa.",
               "neo": "None.", "snb": "Fraud hotline, Ellí, Aukakrónur, Vild, Rapyd."},
        "L2": {"d": 1, "s": "Acquiring takes Mastercard; every issued card is Visa.", "gap": "Visa has debit, credit and business cards; Mastercard is accepted by the 27%-share acquirer.",
               "neo": "Acquiring, online acceptance.", "snb": "Visa cards, wallets, Click to Pay, transfers."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, state owner, heritage, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
