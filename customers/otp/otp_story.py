"""OTP Bank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from otp_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Hungary's biggest bank and the CEE group it heads, as five discs that stack into one platform, from HUF 46.7 "
       "trillion of assets at the bottom to the OTP app, Simple and 299 Hungarian branches at the top. Click the stack to "
       "open it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("young", "Young & digital customers", "smartphone"),
    ("home", "Homebuyers & borrowers", "house"),
    ("priv", "Private-banking clients", "gem"),
    ("sme", "Small businesses & merchants", "store"),
    ("corp", "Corporates", "factory"),
    ("abroad", "Customers abroad", "earth"),
]
USERS_DESC = ("Seven kinds of customer, about 17.5 million in all: almost 4 million in Hungary, from everyday and young "
              "digital customers to homebuyers, private-banking clients, small businesses, merchants and corporates, and the "
              "customers of ten foreign banks from Bulgaria to Uzbekistan.")

WHO = {"con": "An OTP customer", "young": "A young customer", "home": "A homebuyer", "priv": "A private-banking client",
       "sme": "A small business", "corp": "A corporate treasurer", "abroad": "A customer abroad"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a debit card that is usually a Mastercard, the app, cashback and fraud checks.",
     "steps": [("4.1", "accounts", "Open a current account"), ("2.1", "debit", "Pay with an OTP debit card"), ("5.1", "app", "Run it in the OTP app"),
               ("3.3", "loyalty", "Collect cashback"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "phone", "who": "young", "name": "Open an account and pay by phone",
     "why": "Selfie onboarding, a virtual card in the wallet in minutes, and qvik money requests.",
     "steps": [("5.1", "app", "Open an account by selfie"), ("2.1", "vcard", "Get a virtual card"), ("2.3", "wallets", "Add it to Apple Pay or Google Pay"),
               ("2.6", "qvik", "Request money by QR or NFC"), ("4.1", "piggy", "Round up into the Virtual Piggy Bank")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "Bonus cashback cards on Mastercard and co-branded cards with instalments.",
     "steps": [("2.2", "bonus", "Take a Bonus card"), ("2.2", "cobrand", "Or a Telekom or Otthon card"), ("3.3", "loyalty", "Earn cashback")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "A third of new Hungarian mortgages, many under Home Start, sold through branches and agents.",
     "steps": [("5.4", "agents", "Apply through an agent"), ("4.2", "mortgage", "Take a Home Start mortgage"), ("5.3", "branches", "Sign at a branch")]},
    {"id": "private", "who": "priv", "name": "Bank privately",
     "why": "Private banking with a World Elite debit card, Visa Infinite credit and OTP funds.",
     "steps": [("4.4", "privbank", "Join private banking"), ("2.1", "worldelite", "Carry a World Elite card"), ("2.2", "visainf", "Add Visa Infinite"),
               ("4.4", "funds", "Invest with OTP Fund Management")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A business loan, card acceptance in store and online, and qvik.",
     "steps": [("4.3", "msme", "Borrow under Széchenyi Card MAX+"), ("2.5", "pos", "Take cards on an OTP terminal"),
               ("2.5", "simplepay", "Sell online with SimplePay"), ("2.6", "qvik", "Take qvik payments")]},
    {"id": "corp", "who": "corp", "name": "Bank as a corporate",
     "why": "Hungary's largest corporate lender, at a record share.",
     "steps": [("4.3", "corporate", "Borrow and deposit with OTP"), ("4.4", "merkantil", "Lease equipment with Merkantil")]},
    {"id": "abroad", "who": "abroad", "name": "Bank with OTP abroad",
     "why": "DSK in Bulgaria, Ipoteka in Uzbekistan and eight more banks, with Luminor to come.",
     "steps": [("4.5", "dsk", "Bank with DSK"), ("2.7", "dskcards", "Swap a Mastercard for a Visa"), ("4.5", "ipoteka", "Bank with Ipoteka"),
               ("2.7", "ipocards", "Pay with Humo or a co-badged card")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Most Hungarian debit cards, Bonus credit cards, World Elite, the tokens in phone wallets, acceptance and foreign programmes.",
     "steps": [("2.1", "debit", "Most OTP debit cards"), ("2.2", "bonus", "Bonus credit cards"), ("2.1", "worldelite", "Private Banking World Elite"),
               ("2.3", "wallets", "Mastercard tokens in phone wallets"), ("2.7", "cardsabroad", "Programmes in Ukraine, Moldova and Serbia")]},
    {"id": "mcnext", "who": "mc", "name": "Where fraud tools, offers and Luminor could land",
     "why": "Where OTP has needs and Mastercard is not yet in: scam scoring beside OTP's own model, card-linked offers, merchant risk, agentic payments, business cards and Luminor's card portfolio.",
     "steps": [("3.1", "fraud", "Scam and identity scoring"), ("3.3", "loyalty", "Card-linked offers"), ("2.5", "pos", "Acquirer risk and merchant data"),
               ("3.2", "ai", "Agent Pay for OTP's AI"), ("4.3", "msme", "Commercial cards"), ("1.5", "luminor", "Luminor's card review")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across OTP Bank's map",
    "title": "Mastercard's bank in Hungary, Visa's in Bulgaria",
    "lead": "In Hungary most of OTP's debit cards, its Bonus credit cards and its World Elite private-banking cards run on Mastercard, and OTP has twice been Mastercard's Bank of the Year there. Visa sells two entry debit cards and Visa Infinite, and is taking every card at DSK Bank, the group's biggest foreign bank. qvik instant payments compete at the till. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (first-half 2026 report, 5 August 2026) or from OTP's card pages, Mastercard awards and press. No split of cards by network is published; the networks of the SZÉP, Telekom and Otthon cards and of several foreign banks are not stated.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Hungarian debit", "Mostly Mastercard", "Plus Visa Online and Classic"],
        ["Credit", "Bonus on Mastercard ⚠", "Visa Infinite for private banking"],
        ["Private banking", "World Elite", "Debit, Mastercard"],
        ["Bulgaria", "Mastercard to Visa", "DSK reissuing every card ⚠ date"],
        ["Wallets", "Both networks", "Apple Pay 2019, Google Pay 2023"],
        ["Instant", "qvik", "From September 2024"],
        ["Awards", "Bank of the Year", "Mastercard, 2020 and 2025"],
    ],
    "sides": {
        "neo": {"dir": "Most Hungarian debit cards, Bonus credit cards, World Elite, wallet tokens, acceptance, and programmes in Ukraine, Moldova, Serbia and Uzbekistan.",
                "deals": "What it does not do: fraud models, AI, loyalty, qvik, DSK's future cards or Visa Infinite."},
        "snb": {"dir": "Visa's two debit cards, Visa Infinite and DSK Bank; qvik and instant payments; Humo and Uzcard; OTP's own fraud, AI and cashback.",
                "deals": "Where they meet: OTP's terminals, SimplePay and phone wallets take both."},
    },
    "tl": [
        ["Jul 2011", "NFC alliance with Mastercard and Hungarian operators"],
        ["Mar 2014", "OTPay, Europe's first bank wallet with Masterpass"],
        ["May 2019", "Apple Pay, OTP first in Hungary"],
        ["2021", "Mastercard Bank of the Year 2020"],
        ["Sep 2023", "Google Pay, Garmin Pay, Xiaomi Pay"],
        ["Sep 2024", "qvik instant payments launch"],
        ["May 2025", "Péter Csányi becomes CEO"],
        ["Feb 2026", "Mastercard Bank of the Year 2025"],
        ["2026", "DSK Bank reissues cards on Visa ⚠"],
        ["Jul 2026", "Agreement to buy Luminor"],
    ],
    "l": {
        "U": {"d": 1, "s": "Most Hungarian cardholders carry Mastercard; DSK's move to Visa.",
              "gap": "Hungarian debit and Bonus cardholders mostly carry Mastercard; DSK's customers are moving to Visa.",
              "neo": "Hungarian debit and Bonus cardholders, private-banking clients.", "snb": "DSK cardholders, Visa Infinite holders, Humo and Uzcard users."},
        "L5": {"d": 0, "s": "The front doors are OTP's.", "gap": "The OTP app, Simple, branches and agents are the group's own.", "neo": "None.", "snb": "OTP app, Simple, branches, agents."},
        "L4": {"d": 1, "s": "Accounts come with Mastercard-led debit; loans have no network role.", "gap": "Accounts and private banking carry cards; mortgages, loans, leasing and funds do not.",
               "neo": "Accounts, private banking.", "snb": "Mortgages, cash loans, corporate, Merkantil, OTP funds, DSK."},
        "L3": {"d": 0, "s": "Fraud, AI and cashback are OTP's own.", "gap": "OTP built its own fraud model and AI; no Mastercard service is public.",
               "neo": "None public.", "snb": "Own fraud model, AI, Kedvezményprogram."},
        "L2": {"d": 1, "s": "Mastercard leads Hungarian cards; Visa takes Bulgaria; qvik grows.", "gap": "Mastercard carries most Hungarian debit and Bonus credit; Visa has Infinite and DSK; qvik bypasses cards.",
               "neo": "Debit, Bonus, World Elite, wallet tokens, acceptance.", "snb": "Visa Online, Classic and Infinite, DSK on Visa, qvik, Humo and Uzcard."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, owners, footprint, AI, deals."},
    },
    "t": area_lens(LAYERS),
}
