"""Attijariwafa bank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from attijariwafa_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Morocco's largest bank as five discs that stack into one platform, from MAD 825 billion of assets and banks in "
       "27 countries at the bottom to Attijariwafa Mobile, the Simple app and more than 8,000 branches at the top. Click the "
       "stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the "
       "layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("young", "Young & digital", "smartphone"),
    ("mre", "Moroccans abroad", "plane"),
    ("unb", "Newly banked", "wallet"),
    ("vse", "Small businesses & merchants", "store"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Six kinds of customer, more than 12 million in all: everyday customers, young people moving to Simple, "
              "Moroccans abroad, the newly banked reached through Wafacash, small businesses and merchants, and corporates.")

WHO = {"con": "An Attijariwafa customer", "young": "A young Simple user", "mre": "A Moroccan abroad",
       "unb": "A newly banked customer", "vse": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a Wafa card, the app, a phone wallet and the bank's fraud checks.",
     "steps": [("4.1", "retail", "Open an account"), ("2.1", "wafavisa", "Pay with a Wafa Visa card"), ("5.1", "mobile", "Run it in Attijariwafa Mobile"),
               ("2.3", "tokenwallets", "Pay with Apple Pay"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "simple", "who": "young", "name": "Join Simple",
     "why": "The neobank launched in May 2026: open in minutes, a Mastercard in hand, QR payments, deals and travel.",
     "steps": [("3.2", "onboarding", "Open an account in minutes"), ("5.2", "simpleapp", "Choose a Simple tier"),
               ("2.2", "simplecards", "Get a Simple Mastercard"), ("2.3", "simplepay", "Pay friends by QR"), ("3.3", "deals", "Use Simple Deals")]},
    {"id": "abroad", "who": "mre", "name": "Bank from abroad",
     "why": "Attijariwafa bank Europe, Simple for the diaspora, and Wafacash for money home.",
     "steps": [("4.5", "europe", "Bank with Attijariwafa bank Europe"), ("3.2", "onboarding", "Open Simple remotely"),
               ("2.7", "wafacash", "Send money home through Wafacash"), ("2.1", "ram", "Fly on a Royal Air Maroc card")]},
    {"id": "inclusion", "who": "unb", "name": "Open a first account",
     "why": "Economic banking and the Wafacash network reach rural Morocco.",
     "steps": [("5.3", "branches", "Walk into a Wafacash point"), ("2.7", "hissab", "Open a Hissab Bikhir account"), ("2.6", "instant", "Receive an instant transfer")]},
    {"id": "borrow", "who": "con", "name": "Borrow for a purchase",
     "why": "Wafasalaf consumer credit, Islamic finance at Bank Assafa, and Wafa Assurance cover.",
     "steps": [("4.3", "wafasalaf", "Borrow with Wafasalaf"), ("4.3", "assafa", "Or finance a home with Bank Assafa"), ("4.4", "wafaassurance", "Insure it with Wafa Assurance")]},
    {"id": "merchant", "who": "vse", "name": "Take payments as a merchant",
     "why": "Support from Dar Al Moukawil, terminals from Attijari Payment, QR and instant transfers, all on CMI's platform.",
     "steps": [("3.4", "darmoukawil", "Get help from Dar Al Moukawil"), ("2.4", "attpay", "Take cards with Attijari Payment"),
               ("2.5", "cmi", "Processed through CMI"), ("2.3", "simplepay", "Accept QR payments")]},
    {"id": "corp", "who": "corp", "name": "Finance a company",
     "why": "Corporate loans, investment banking and leasing, at home and across Africa.",
     "steps": [("4.2", "cib", "Borrow from the corporate bank"), ("4.2", "markets", "Raise capital with Attijari Finances"),
               ("4.3", "leasing", "Lease equipment with Wafabail"), ("4.5", "westafrica", "Bank subsidiaries in West Africa")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Simple's three Mastercard tiers, AWB Black World Elite, the UEFA card, and Mastercard cards in phone wallets.",
     "steps": [("2.2", "simplecards", "Simple Go, Plus and Prime on Mastercard"), ("2.1", "awbblack", "AWB Black World Elite"),
               ("2.1", "ucl", "UEFA Champions League Mastercard"), ("2.3", "tokenwallets", "Mastercard cards in Apple Pay")]},
    {"id": "mcnext", "who": "mc", "name": "Where acquiring, Simple and Africa could land",
     "why": "Where Attijariwafa has needs and Mastercard is not yet in: a new acquirer, Simple's instalments and AI, the diaspora's transfers, corporate cards and the African banks.",
     "steps": [("2.4", "attpay", "Acquirer risk and SoftPOS for Attijari Payment"), ("4.3", "wafasalaf", "Instalments for Simple"),
               ("3.2", "simpleai", "Agent Pay for Simple AI"), ("2.7", "wafacash", "Cross-border send for Moroccans abroad"),
               ("4.2", "cib", "Commercial cards"), ("4.5", "westafrica", "One card platform for the African banks")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Attijariwafa bank's map",
    "title": "Visa's partner, but its new neobank runs on Mastercard",
    "lead": "Visa signed a strategic partnership with Attijariwafa bank in December 2024 and carries the core Wafa Visa range ⚠ and the Royal Air Maroc co-brand. Mastercard holds the top of the range (AWB Black World Elite ⚠), the 2019 UEFA Champions League card and, since May 2026, three of the four tiers of Simple, the group's neobank. Underneath, CMI switches domestic payments, the bank now acquires merchants itself, and interchange is capped at 0.50%. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (H1 2026 results, 27 July 2026) or from Moroccan press, the Competition Council and Bank Al-Maghrib. The bank's own card pages could not be read; card networks rest on press and an independent guide, and no split of cards by network is published.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Core cards", "Visa", "Wafa Visa Classic, Gold, Platinum ⚠"],
        ["Premium", "Mastercard", "AWB Black World Elite ⚠"],
        ["Simple", "Mostly Mastercard", "Three of four tiers; May 2026"],
        ["Partnership", "Visa", "Strategic deal, December 2024"],
        ["Domestic switch", "CMI", "Monopoly ended; multi-acquirer May 2025"],
        ["Acquiring", "Attijari Payment", "Licensed March 2025"],
        ["Interchange", "0.50% cap", "From 1 October 2026"],
        ["A2A", "Instant transfers, QR", "Since June 2023; Simple Pay 2026"],
    ],
    "sides": {
        "neo": {"dir": "Simple's Go, Plus and Prime cards, AWB Black, the UEFA card, Mastercard cards in phone wallets and acceptance at Attijari Payment's merchants.",
                "deals": "What it does not do: the core Wafa range, the airline co-brand, the domestic switch, QR and instant transfers, fraud and AI."},
        "snb": {"dir": "Visa's core range, co-brand and 2024 partnership; CMI and the group's own processor; instant transfers, Simple Pay QR and Wafacash; the bank's own fraud models and AI.",
                "deals": "Where they meet: Simple, which mixes Mastercard tiers with a metal card whose network is not stated."},
    },
    "tl": [
        ["Sep 2019", "UEFA Champions League Mastercard"],
        ["Mar 2021", "JCB on ATMs, after UnionPay in 2018"],
        ["Jun 2023", "Instant interbank transfers go live"],
        ["Aug 2023", "Apple Pay launched"],
        ["Feb 2024", "Royal Air Maroc Visa co-brand ⚠"],
        ["Oct 2024", "CMI monopoly ended; interchange capped at 0.65%"],
        ["Dec 2024", "Strategic partnership with Visa"],
        ["May 2025", "Attijari Payment starts acquiring"],
        ["Apr 2026", "CIH's Lana Cash signs with Mastercard"],
        ["May 2026", "Simple launched, mostly on Mastercard"],
        ["Jul 2026", "GOAL 2030 launched"],
        ["Oct 2026", "Interchange cap falls to 0.50%"],
    ],
    "l": {
        "U": {"d": 1, "s": "Simple users and premium clients carry Mastercard; most cardholders carry Visa ⚠.",
              "gap": "Simple's young and diaspora users get Mastercard; the core range and airline co-brand are Visa; the newly banked use wallets and cash.",
              "neo": "Simple users, AWB Black holders, UEFA cardholders.", "snb": "Wafa Visa holders, Royal Air Maroc cardholders, Wafacash users."},
        "L5": {"d": 1, "s": "The Simple app carries Mastercard cards; the other doors are the bank's.", "gap": "Attijariwafa Mobile, branches and Wafacash points have no network role; Simple ships Mastercard cards.",
               "neo": "Simple app.", "snb": "Attijariwafa Mobile, branches, Wafacash, retail partners."},
        "L4": {"d": 1, "s": "Retail cards are split; the other lines have no network role.", "gap": "Retail carries Visa and Mastercard; corporate, consumer credit, insurance and Europe have no public card programme; African banks not researched.",
               "neo": "Retail premium and Simple cards.", "snb": "Wafa Visa range; corporate, Wafasalaf, Wafa Assurance."},
        "L3": {"d": 0, "s": "Fraud, AI and rewards are the bank's own.", "gap": "Real-time fraud models, AI assistants and Simple Deals run without a Mastercard service in public sources.",
               "neo": "None.", "snb": "Fraud models, Simple AI, Simple Deals, Dar Al Moukawil."},
        "L2": {"d": 1, "s": "Simple and the top cards on Mastercard; core cards on Visa; CMI and A2A underneath.", "gap": "Visa has the core range and a 2024 partnership; Mastercard has Simple and the premium tier; CMI switches, instant transfers and QR bypass cards.",
               "neo": "Simple cards, AWB Black, UEFA card, wallets, acceptance.", "snb": "Wafa Visa, RAM co-brand, CMI, instant transfers, Simple Pay, Wafacash."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, owners, ratings, GOAL 2030, AI."},
    },
    "t": area_lens(LAYERS),
}
