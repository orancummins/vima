"""PKO Bank Polski's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from pko_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Poland's largest bank as five discs that stack into one platform, from PLN 608 billion of assets and the State "
       "Treasury's anchor stake at the bottom to the IKO app, 954 branches and partners such as Allegro at the top. Click "
       "the stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up across "
       "the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("young", "Children & young people", "graduation-cap"),
    ("home", "Homebuyers", "house"),
    ("saver", "Savers & investors", "coins"),
    ("sme", "Small firms", "briefcase"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Six kinds of customer, 12.6 million in all: everyday customers, children and young people on PKO Junior, "
              "homebuyers, savers and investors, 679,000 small firms and 32,000 corporates.")

WHO = {"con": "A PKO customer", "young": "A young customer", "home": "A homebuyer", "saver": "A saver",
       "sme": "A small firm", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a Visa debit card, the IKO app, contactless BLIK and fraud checks.",
     "steps": [("4.2", "accounts", "Open Konto za Zero"), ("2.1", "debit", "Pay with the Visa debit card"), ("5.1", "iko", "Run it in IKO"),
               ("2.3", "blikc", "Tap to pay with contactless BLIK"), ("3.1", "pkoid", "Approve with PKO ID")]},
    {"id": "shop", "who": "con", "name": "Shop online and pay later",
     "why": "BLIK codes, Allegro Klik and PKO Pay Later, with phone wallets for cards.",
     "steps": [("2.3", "blik", "Pay with a BLIK code"), ("3.3", "allegro", "Link the account to Allegro"),
               ("2.3", "paylater", "Spread it with PKO Pay Later"), ("2.4", "wallets", "Or tap a card in a wallet")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "A credit book split between Mastercard Platinum, the two-network Przejrzysta card and Visa Infinite.",
     "steps": [("2.2", "przejrzysta", "Take the Przejrzysta card"), ("2.2", "mcplat", "Trade up to Mastercard Platinum"),
               ("3.3", "benefits", "Collect Priceless points")]},
    {"id": "junior", "who": "young", "name": "Start a child's money life",
     "why": "PKO Junior: an account, a Visa card and contactless BLIK in the children's app.",
     "steps": [("4.2", "accounts", "Open a PKO Junior account"), ("2.1", "junior", "Get a Visa card"),
               ("5.1", "juniorapp", "Pay by phone in PKO Junior")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "Poland's biggest mortgage lender, online or through intermediaries, with insurance alongside.",
     "steps": [("5.4", "partners", "Apply through an intermediary"), ("4.1", "mortgages", "Take a Digital Mortgage"),
               ("4.1", "hipo", "Funded by PKO Bank Hipoteczny"), ("4.3", "insurance", "Insure it with PKO Dom")]},
    {"id": "save", "who": "saver", "name": "Save and invest",
     "why": "Deposits, Treasury bonds, PKO TFI funds and the brokerage, from the app.",
     "steps": [("4.3", "deposits", "Save and buy Treasury bonds"), ("4.3", "tfi", "Invest with PKO TFI"), ("5.1", "iko", "Track it in IKO")]},
    {"id": "sme", "who": "sme", "name": "Run a small firm",
     "why": "A free start-up account, a Visa business card, a terminal with eService and loans through Allegro.",
     "steps": [("4.4", "firms", "Open a business account"), ("2.1", "bizdebit", "Pay with a Visa business card"),
               ("2.5", "terminals", "Take cards and BLIK on a terminal"), ("4.5", "leasing", "Lease a van")]},
    {"id": "corp", "who": "corp", "name": "Bank as a corporate",
     "why": "Syndicated loans, FX and SEPA Instant through iPKO biznes, and branches abroad.",
     "steps": [("4.5", "cib", "Borrow from CIB"), ("5.2", "ipko", "Run treasury in iPKO biznes"),
               ("2.6", "sepainst", "Pay instantly in euro"), ("1.4", "intl", "Bank abroad with PKO")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Contactless BLIK, the Platinum and Przejrzysta credit cards, wallet tokens and acceptance at PKO's merchants.",
     "steps": [("2.3", "blikc", "Contactless BLIK on Mastercard terminals"), ("2.2", "mcplat", "Mastercard Platinum"),
               ("2.2", "przejrzysta", "Przejrzysta, Mastercard version"), ("2.4", "wallets", "Mastercard tokens in wallets"),
               ("2.5", "terminals", "Acceptance with eService")]},
    {"id": "mcnext", "who": "mc", "name": "Where BLIK, scams and fleets could land",
     "why": "Where PKO has needs and Mastercard is not yet in: BLIK abroad, scam tools, offers for the ecosystem pillar, fleet and commercial cards, and support for the push into Europe.",
     "steps": [("2.3", "blikc", "Contactless BLIK as the travel wallet"), ("3.1", "behav", "Scam and identity scores"),
               ("3.3", "allegro", "Card-linked offers for ecosystems"), ("4.5", "leasing", "Fleet and commercial cards"),
               ("1.4", "intl", "Cards and acceptance for EU expansion")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across PKO Bank Polski's map",
    "title": "A Visa debit bank whose phones tap on Mastercard",
    "lead": "PKO Bank Polski's 9.9 million debit cards, its business cards and its premium card are Visa, and its new Żabka card went to Visa in 2026. Mastercard holds the Platinum credit card and half of the Przejrzysta card, and carries contactless BLIK: 516.6 million phone payments by PKO customers on Mastercard terminals. Mastercard has owned part of BLIK's operator since 2020. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (1H 2026 results, 13 August 2026) or from the bank's card pages and BLIK. Card counts by network are not published; networks are read from each product page.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa", "9.9 million cards, personal and business"],
        ["Credit", "Split", "Mastercard Platinum; Przejrzysta on both; Visa Infinite"],
        ["Contactless BLIK", "Mastercard acceptance", "516.6 million payments to June 2026"],
        ["BLIK", "Domestic scheme", "Mastercard a shareholder since April 2020"],
        ["New cards", "Visa", "Żappka Pay card, April 2026"],
        ["Acceptance", "eService", "Visa, Mastercard and BLIK"],
        ["Fraud", "PKO's own", "PKO ID, interbank behavioural checks"],
    ],
    "sides": {
        "neo": {"dir": "Contactless BLIK, the Platinum card and Mastercard versions of Przejrzysta, wallet tokens, and acceptance at PKO's merchants.",
                "deals": "What it does not do: debit, business cards, premium credit, fraud tools, AI or rewards."},
        "snb": {"dir": "Visa debit, business and premium cards, Visa Mobile and the Żappka card; BLIK codes; PKO's own fraud, AI and rewards.",
                "deals": "Where they meet: BLIK, co-owned by PKO and Mastercard."},
    },
    "tl": [
        ["2010", "6.5 million Visa payWave debit cards"],
        ["Nov 2013", "EVO buys 66% of eService"],
        ["Apr 2020", "Mastercard joins BLIK's operator"],
        ["Oct 2024", "Strategy: The Number 1, full stop"],
        ["Feb 2026", "BLIK's first euro transfer from Bizum lands at PKO"],
        ["Apr 2026", "Żappka Pay card with Visa"],
        ["Jun 2026", "Kropka app; 516.6m contactless BLIK payments"],
        ["Aug 2026", "1H 2026: profit PLN 5.29bn"],
    ],
    "l": {
        "U": {"d": 1, "s": "Phone payers ride Mastercard; card holders mostly carry Visa.",
              "gap": "Debit, business and premium cardholders carry Visa; contactless BLIK users and Platinum holders use Mastercard.",
              "neo": "Contactless BLIK users, Platinum and some Przejrzysta holders.", "snb": "Debit, business and Visa Infinite holders."},
        "L5": {"d": 1, "s": "IKO hosts contactless BLIK on Mastercard.", "gap": "The app carries the Mastercard flow; branches, online banking and partners are PKO's.",
               "neo": "Contactless BLIK in IKO and PKO Junior.", "snb": "Branches, iPKO, partners."},
        "L4": {"d": 0, "s": "The business lines carry Visa cards.", "gap": "Accounts come with Visa debit; mortgages, savings, leasing and corporate banking have no network role.",
               "neo": "None.", "snb": "Accounts, mortgages, savings, leasing, CIB."},
        "L3": {"d": 1, "s": "Priceless points on Platinum; the rest is PKO's.", "gap": "Fraud, AI and rewards are built in-house or with Allegro.",
               "neo": "Priceless points.", "snb": "PKO ID, behavioural checks, bots, Allegro Klik, Kropka."},
        "L2": {"d": 1, "s": "Contactless BLIK and some credit on Mastercard; debit on Visa.", "gap": "Visa holds debit and the newest card; Mastercard holds contactless BLIK and part of credit.",
               "neo": "Contactless BLIK, Platinum, Przejrzysta, tokens, acceptance.", "snb": "Visa debit, Visa Infinite, Visa Mobile, Żappka card, BLIK codes."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, ownership, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
