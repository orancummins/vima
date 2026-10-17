"""Garanti BBVA's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from garanti_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Turkey's second-largest private bank as five discs that stack into one platform, from TL 5.2 trillion of assets "
       "and BBVA's 86% stake at the bottom to Garanti BBVA Mobile, branches and Bonus's partner merchants at the top. Click "
       "the stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up across "
       "the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("aff", "Affluent & travellers", "plane"),
    ("inv", "Savers & investors", "coins"),
    ("sme", "Small businesses", "briefcase"),
    ("mer", "Merchants", "store"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Six kinds of customer, 31.2 million in all: everyday customers, affluent customers and frequent flyers, savers "
              "and investors, small businesses, the merchants behind 932,000 POS terminals, and corporates.")

WHO = {"con": "A Garanti BBVA customer", "aff": "A frequent flyer", "inv": "A saver", "sme": "A small business",
       "mer": "A merchant", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: the app, a Paracard debit card, FAST transfers and the UGİ assistant.",
     "steps": [("5.1", "mobile", "Open an account in the app"), ("2.4", "paracard", "Pay with Paracard"), ("2.6", "fast", "Send money by FAST"),
               ("3.2", "ugi", "Ask UGİ")]},
    {"id": "bonus", "who": "con", "name": "Shop and earn with Bonus",
     "why": "Turkey's best-known credit card: instalments and bonus at 600,000 merchants, managed in BonusFlaş.",
     "steps": [("2.1", "bonus", "Take a Bonus card"), ("3.4", "bonusprog", "Earn bonus at partner merchants"), ("2.7", "bonusflas", "Pay and manage in BonusFlaş"),
               ("3.1", "token", "Control where the card is stored")]},
    {"id": "travel", "who": "aff", "name": "Earn miles and travel",
     "why": "Miles&Smiles, Shop&Fly and American Express, with the best card picked at checkout.",
     "steps": [("2.2", "miles", "Fly with Miles&Smiles"), ("2.3", "amex", "Add an American Express card"), ("2.7", "smart", "Let S.M.A.R.T. pick the card")]},
    {"id": "borrow", "who": "con", "name": "Buy a home or a car",
     "why": "The largest private lender for mortgages and car loans.",
     "steps": [("5.2", "branches", "Apply in a branch"), ("4.1", "retaillend", "Take a mortgage or car loan"), ("5.1", "mobile", "Repay in the app")]},
    {"id": "save", "who": "inv", "name": "Save and invest",
     "why": "Deposits, pensions, funds and crypto in one app.",
     "steps": [("4.2", "deposits", "Open a deposit"), ("4.2", "wealth", "Invest and save for a pension"), ("4.2", "kripto", "Hold crypto in Garanti BBVA Kripto")]},
    {"id": "sme", "who": "sme", "name": "Run and export as a small business",
     "why": "A business account and loans, a Mastercard commercial card and the e-export package, and open banking across banks.",
     "steps": [("4.3", "sme", "Bank with My Banker"), ("4.3", "commcard", "Export with a Mastercard commercial card"), ("3.5", "openbank", "See other banks' accounts")]},
    {"id": "merchant", "who": "mer", "name": "Take payments as a merchant",
     "why": "Turkey's top private acquirer, TAMİ's multi-bank POS and the Bonus merchant network.",
     "steps": [("2.5", "acquiring", "Accept cards on a Garanti POS"), ("2.5", "tami", "Use TAMİ's multi-bank POS"), ("5.3", "partners", "Join Bonus as a member merchant")]},
    {"id": "corp", "who": "corp", "name": "Collect and finance as a corporate",
     "why": "Request-to-pay on FAST, FX finance and sustainable loans.",
     "steps": [("2.6", "odemeiste", "Collect bills by Ödeme İste"), ("4.4", "cib", "Borrow in foreign currency"), ("1.4", "sustain", "Finance the transition")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Most Bonus credit cards, Miles&Smiles Platinum and commercial cards, plus tokens, Masterpass, AI collections and the agentic pilot.",
     "steps": [("2.1", "bonus", "Bonus credit cards"), ("2.2", "miles", "Miles&Smiles Platinum"), ("3.1", "token", "Tokenisation"),
               ("3.1", "masterpass", "Masterpass"), ("3.3", "collections", "AI collections"), ("4.3", "commcard", "Commercial cards and e-export")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, offers and acquiring could land",
     "why": "Where Garanti BBVA has needs and Mastercard is not yet, or only partly, in: Agent Pay for customers, offers on the Bonus programme, debit and travel cards now on Visa, the acquiring book and TAMİ, and A2A collections.",
     "steps": [("3.2", "agentpay", "Agent Pay from pilot to customers"), ("3.4", "bonusprog", "Card-linked offers across eight banks"),
               ("2.4", "paracard", "Debit, now on Visa"), ("2.5", "acquiring", "Acquirer risk and merchant data"), ("2.6", "odemeiste", "Open-finance tools for A2A")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Garanti BBVA's map",
    "title": "Mastercard's credit-card partner of 30 years, in a four-network bank",
    "lead": "Mastercard carries most of Garanti BBVA's Bonus credit cards, Miles&Smiles Platinum and some commercial cards, in Turkey's largest private card business, and the two have launched tokenisation, Masterpass controls, AI collections and an agentic-commerce pilot together. Visa carries the Paracard debit range and Shop&Fly, American Express has a full Garanti-issued range, and Troy versions sit beside the main cards. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (1H 2026 results, 30 July 2026) or from Garanti BBVA, Mastercard Turkey and the Turkish press. Networks are read from the bank's card catalogue; no split by card count or volume is published.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Credit", "Mastercard-led", "Bonus core range; 20.6 million credit cards in all"],
        ["Debit", "Visa", "Paracard range; Troy version too"],
        ["Travel", "Mastercard, Visa, Amex", "Miles&Smiles on Mastercard and Amex; Shop&Fly on Visa and Amex"],
        ["Amex", "Garanti-issued", "Licensed partner for 20 years"],
        ["Troy", "Domestic versions", "Troy took 25% of Turkish card spending in 2025"],
        ["Firsts", "Mastercard", "Tokens 2021, Masterpass 2024, Agent Pay pilot 2025"],
        ["Acquiring", "#1 private", "932,000 POS, every network"],
        ["Instant", "FAST", "Ödeme İste API, May 2026"],
    ],
    "sides": {
        "neo": {"dir": "Most Bonus credit cards, Miles&Smiles Platinum, commercial cards, tokenisation, Masterpass, AI collections and the agentic pilot.",
                "deals": "What it does not do: debit, Shop&Fly, the Amex range, Troy cards, FAST or the UGİ assistant."},
        "snb": {"dir": "Visa debit and Shop&Fly, American Express issuing, Troy cards, FAST and request-to-pay, and the bank's own AI and apps.",
                "deals": "Where they meet: Bonus, carried by several networks, and the acquiring book that takes them all."},
    },
    "tl": [
        ["2000", "Bonus and Miles&Smiles launched"],
        ["Jul 2021", "Mastercard tokenisation in BonusFlaş, a Turkish first"],
        ["Feb 2024", "Bonus Platinum Biometric ⚠"],
        ["May 2024", "Masterpass merchant view"],
        ["May 2025", "E-export package for Mastercard commercial cards"],
        ["Aug 2025", "Bonus at 25 with Mastercard"],
        ["Nov 2025", "Visa World Cup deal for Shop&Fly"],
        ["Dec 2025", "AI collections; agentic commerce pilot"],
        ["Jul 2026", "20 years of American Express"],
    ],
    "l": {
        "U": {"d": 1, "s": "Credit cardholders mostly carry Mastercard; debit holders carry Visa.",
              "gap": "14 million credit-card customers lean to Mastercard; debit, Shop&Fly and Amex holders do not.",
              "neo": "Bonus and Miles&Smiles cardholders, commercial cardholders.", "snb": "Debit holders, Shop&Fly and Amex holders, Troy users."},
        "L5": {"d": 0, "s": "The front doors are Garanti's.", "gap": "App, branches and contact centre are the bank's; Bonus partner merchants take every network.",
               "neo": "None.", "snb": "Garanti BBVA Mobile, branches, ATMs."},
        "L4": {"d": 1, "s": "Card lending and commercial cards lean to Mastercard.", "gap": "Consumer card balances are mostly Mastercard; mortgages, deposits and corporate lending have no network role.",
               "neo": "Credit-card lending, commercial cards and e-export.", "snb": "Mortgages, deposits, pensions, crypto, CIB."},
        "L3": {"d": 2, "s": "Mastercard runs tokens, Masterpass, collections AI and the agent pilot.", "gap": "Joint firsts from 2021 to 2025; UGİ and open banking are the bank's own.",
               "neo": "Tokenisation, Masterpass, AI collections, Agent Pay pilot.", "snb": "UGİ on OpenAI, open banking, APIs."},
        "L2": {"d": 1, "s": "Credit on Mastercard; debit on Visa; Amex and Troy beside.", "gap": "Mastercard leads credit; Visa has debit and Shop&Fly; FAST carries transfers.",
               "neo": "Bonus core range, Miles&Smiles Platinum, biometric card.", "snb": "Paracard, Shop&Fly, Amex, Troy, FAST, TAMİ."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, BBVA, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
