"""Westpac New Zealand's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from westpacnz_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("New Zealand's fourth-largest bank as five discs that stack into one platform, from NZ$108 billion of lending and "
       "an Australian parent at the bottom to the Westpac One app, branches, banking vans and partners at the top. Click the "
       "stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the "
       "layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("home", "Homebuyers", "house"),
    ("saver", "Savers & KiwiSaver members", "coins"),
    ("sme", "Small businesses", "briefcase"),
    ("agri", "Farmers & growers", "factory"),
    ("corp", "Corporates & institutions", "building-2"),
]
USERS_DESC = ("Six kinds of customer: everyday customers, homebuyers, savers and KiwiSaver members, small businesses, "
              "farmers and growers, and the corporates and institutions served with WBC's NZ Branch.")

WHO = {"con": "A Westpac NZ customer", "home": "A homebuyer", "saver": "A saver", "sme": "A small business",
       "agri": "A farmer", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a debit Mastercard with EFTPOS, Westpac One and fraud defences.",
     "steps": [("4.2", "accounts", "Open an everyday account"), ("2.1", "debit", "Pay with debit Mastercard or EFTPOS"),
               ("2.4", "wallets", "Tap with Apple Pay or Google Pay"), ("5.1", "app", "Run it in Westpac One"),
               ("3.1", "fraud", "Protected from fraud and scams")]},
    {"id": "fly", "who": "con", "name": "Earn Airpoints as I spend",
     "why": "The Air New Zealand partnership, carried on Mastercard credit and debit cards.",
     "steps": [("2.2", "airpoints", "Take an Airpoints Mastercard"), ("2.1", "airdebit", "Or earn on debit"),
               ("3.3", "airnz", "Collect with Air New Zealand"), ("3.3", "hotpay", "Or spend hotpoints like cash")]},
    {"id": "safe", "who": "con", "name": "Stay in control of my cards",
     "why": "Instant digital cards, dynamic codes, gambling and online blocks, and payee name checks.",
     "steps": [("2.4", "digicard", "Get a digital card instantly"), ("3.2", "controls", "Turn off gambling or online use"),
               ("3.2", "substrap", "Blocked from subscription traps"), ("3.1", "cop", "Check the payee's name")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "NZ$73 billion of home lending, through branches, the app, Dosh, and insurance with Tower.",
     "steps": [("5.2", "branches", "Talk to a home-loan expert"), ("4.1", "homeloans", "Take a home loan"),
               ("4.1", "dosh", "Or apply through Dosh"), ("4.5", "insurance", "Insure it with Tower")]},
    {"id": "save", "who": "saver", "name": "Save and invest",
     "why": "Notice Saver and the Westpac KiwiSaver Scheme run by BT.",
     "steps": [("4.2", "accounts", "Open a Notice Saver"), ("4.5", "kiwisaver", "Join Westpac KiwiSaver"), ("5.1", "app", "Watch it in the app")]},
    {"id": "send", "who": "con", "name": "Send money home",
     "why": "Fee-free international transfers to 137 countries since December 2025.",
     "steps": [("5.1", "app", "Open Westpac One"), ("2.7", "intl", "Send overseas with no transfer fee")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A new business platform, start-up lending, business Mastercards, card acceptance and open-banking payments.",
     "steps": [("4.3", "sme", "Bank on Westpac One for Business"), ("4.3", "startup", "Borrow to start up"),
               ("2.3", "bizcards", "Spend on a BusinessPLUS Mastercard"), ("2.5", "merchant", "Take card payments"),
               ("2.6", "openbanking", "Get paid by bank")]},
    {"id": "farm", "who": "agri", "name": "Finance the farm",
     "why": "Sustainable Farm Loans and agri bankers, reached through branches and vans.",
     "steps": [("5.2", "branches", "Meet an agri banker"), ("4.3", "agri", "Take a Sustainable Farm Loan"), ("2.3", "bizcards", "Pay farm costs by card")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Every card Westpac NZ issues: debit, the Airpoints and hotpoints credit range, business cards and the wallets on top.",
     "steps": [("2.1", "debit", "Debit Mastercard"), ("2.2", "airpoints", "Airpoints Mastercard"), ("2.2", "hotpoints", "hotpoints Mastercard"),
               ("2.3", "bizcards", "Business Mastercards"), ("2.4", "wallets", "Mastercard tokens in Apple Pay and Google Pay")]},
    {"id": "mcnext", "who": "mc", "name": "Where Mastercard services could land",
     "why": "Where Westpac NZ has needs and Mastercard is not yet in: scam scoring, Click to Pay on its digital cards, commercial virtual cards, cross-border transfers, open banking and Air NZ offers.",
     "steps": [("3.1", "fraud", "Scam and identity scoring"), ("2.4", "digicard", "Click to Pay and full tokenisation"),
               ("4.3", "sme", "Virtual cards and spend controls for SMEs"), ("2.7", "intl", "Mastercard Move for remittances"),
               ("2.6", "openbanking", "Open-banking connectivity"), ("3.3", "airnz", "Offers for the renewed Air NZ deal")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Westpac New Zealand's map",
    "title": "Every card is a Mastercard; the services are not",
    "lead": "While its Australian parent went Visa-only in 2013, Westpac NZ signed a five-year Mastercard partnership in 2014, and in July 2026 every card it issues is still a Mastercard: debit (with EFTPOS for PIN payments), the Airpoints, hotpoints and Fee Free credit cards, and business cards. Beyond the cards, Mastercard is not visible: fraud, data, open banking, international transfers and AI are Westpac's own or other partners'. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Westpac NZ's own (half-year release, 5 May 2026) or from the parent's 2025 annual report, the credit-card key-information brochure (31 July 2026), Payments NZ and press. westpac.co.nz could not be read directly; items seen only in search summaries are marked ⚠.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Credit", "Mastercard", "Whole range, terms of 31 July 2026"],
        ["Debit", "Mastercard + EFTPOS", "Airpoints debit since 2015"],
        ["Business cards", "Mastercard", "BusinessPLUS, Airpoints Business"],
        ["Network deal", "Mastercard", "Five years from 2014; renewal not public ⚠"],
        ["Loyalty", "Air New Zealand", "Since 2015; extended June 2026 ⚠"],
        ["Open banking", "Westpac APIs", "Free calls; POLi on board, 2025"],
        ["Acceptance", "Verifone, Worldline", "All networks ⚠"],
        ["Interchange", "Capped", "Credit 0.3% in person from Dec 2025"],
    ],
    "sides": {
        "neo": {"dir": "Every debit, credit and business card, the wallet tokens on them, and the card data behind gambling and subscription blocks.",
                "deals": "What it does not do: EFTPOS, fraud models, Confirmation of Payee, open banking, international transfers, AI or data enrichment."},
        "snb": {"dir": "Domestic EFTPOS via Paymark, Westpac's own fraud and card controls, Akahu, POLi and open-banking APIs, Microsoft AI, Verifone and Worldline terminals.",
                "deals": "Where they meet: the cards that carry Air NZ and hotpoints rewards, and the digital cards that could take Click to Pay."},
    },
    "tl": [
        ["2013", "Parent goes Visa-only in Australia"],
        ["Apr 2014", "Five-year Mastercard partnership"],
        ["Mar 2015", "Air New Zealand picks Westpac"],
        ["Oct 2015", "Airpoints Debit Mastercard and PayTag"],
        ["Nov 2021", "Catherine McGrath becomes CEO"],
        ["Mar 2025", "Dynamic security codes on digital cards"],
        ["Jul 2025", "POLi on Westpac's open-banking APIs"],
        ["Oct 2025", "Gambling and online card controls"],
        ["Dec 2025", "Interchange caps cut; international fee removed"],
        ["May 2026", "Foreign-card caps; HY26 profit NZ$545m"],
        ["Jun 2026", "Air NZ partnership extended ⚠"],
        ["Jul 2026", "Credit-card terms reissued, all Mastercard"],
        ["Sep 2026", "API Centre closes; MBIE runs open banking"],
    ],
    "l": {
        "U": {"d": 2, "s": "Every Westpac NZ cardholder carries a Mastercard.",
              "gap": "Debit, credit and business cardholders are all on Mastercard; EFTPOS PIN payments and bank transfers are not.",
              "neo": "Debit, credit and business cardholders.", "snb": "EFTPOS PIN payments, open-banking and international payers, home-loan and KiwiSaver customers."},
        "L5": {"d": 0, "s": "The front doors are Westpac's.", "gap": "App, branches, vans, contact centres and partners are Westpac's own.",
               "neo": "None.", "snb": "Westpac One, branches and vans, Microsoft CCaaS, Air NZ, Dosh, POLi."},
        "L4": {"d": 1, "s": "Accounts and business banking carry Mastercard cards.", "gap": "Everyday and business accounts come with Mastercard; home loans, agri, institutional and KiwiSaver have no network role.",
               "neo": "Cards on everyday and business accounts.", "snb": "Home loans, agri, institutional banking, KiwiSaver, insurance."},
        "L3": {"d": 1, "s": "Controls and rewards run on card data; fraud is Westpac's.", "gap": "Gambling and subscription blocks and Airpoints earning ride on Mastercard cards; fraud models, payee checks and Akahu data are not Mastercard's.",
               "neo": "Card data behind controls and rewards.", "snb": "Fraud models, Confirmation of Payee, Akahu enrichment."},
        "L2": {"d": 2, "s": "Every card is Mastercard; transfers are not.", "gap": "Debit, credit, business cards and wallets are Mastercard; EFTPOS, open banking, acquiring and international transfers run elsewhere.",
               "neo": "Debit, credit, business cards, wallet tokens.", "snb": "EFTPOS, open-banking APIs, POLi, terminals, international transfers."},
        "L1": {"d": 0, "s": "The foundation is the bank's and its parent's.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, parent, leadership, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
