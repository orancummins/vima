"""National Bank of Kuwait's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from nbk_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Kuwait's largest bank as five discs that stack into one platform, from KD 46 billion of assets and a 1952 "
       "charter at the bottom to the NBK app, 70 branches and co-brand partners at the top. Click the stack to open it. "
       "Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined in "
       "the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("aff", "Affluent cardholders", "gem"),
    ("youth", "Young people & students", "graduation-cap"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates", "factory"),
    ("hnw", "Wealth clients", "coins"),
]
USERS_DESC = ("Six kinds of customer: everyday customers, affluent cardholders, the young people Weyay and Jeel serve, "
              "small businesses, the corporates and foreign companies NBK banks, and NBK Wealth's private clients. NBK "
              "does not publish a customer count.")

WHO = {"con": "An NBK customer", "aff": "An affluent cardholder", "youth": "A student", "sme": "A small business",
       "corp": "A corporate treasurer", "hnw": "A wealth client"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account opened in the app, a KNET debit card in Apple Pay, WAMD transfers and fraud checks.",
     "steps": [("3.1", "ekyc", "Open an account with Mobile ID"), ("4.1", "accounts", "Hold an NBK account"), ("2.3", "debit", "Pay with a debit card"),
               ("2.3", "wallets", "Add it to Apple Pay"), ("2.6", "wamd", "Send money by phone number"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "cashback", "who": "aff", "name": "Earn on a credit card",
     "why": "The flagship KWT Visa Infinite, its cashback, and FlexiPay instalments.",
     "steps": [("5.1", "app", "Apply in the app"), ("2.1", "kwt", "Use KWT Visa Infinite"), ("3.4", "rewards", "Collect cashback and points"),
               ("3.4", "flexipay", "Spread a purchase with FlexiPay")]},
    {"id": "aura", "who": "con", "name": "Shop with Aura",
     "why": "The Alshaya co-brand on Mastercard: points at more than 50 brands.",
     "steps": [("5.3", "partners", "Shop at Alshaya brands"), ("2.2", "aura", "Pay with the NBK-Aura World Mastercard"), ("3.4", "rewards", "Earn Aura points")]},
    {"id": "travel", "who": "aff", "name": "Travel and spend abroad",
     "why": "Airline cards on Visa and Mastercard, lounges, and NBK's branches abroad.",
     "steps": [("2.1", "kac", "Earn Oasis Club miles"), ("2.2", "miles", "Use lounges with Miles World Mastercard"),
               ("2.1", "harrods", "Shop at Harrods"), ("1.3", "network", "Bank in 13 countries")]},
    {"id": "youth", "who": "youth", "name": "Start banking young",
     "why": "Jeel at 8, Weyay at 15, a SELECT card for allowances and WAMD for friends.",
     "steps": [("4.2", "jeel", "Get a Jeel card"), ("4.2", "weyay", "Open Weyay at 15"), ("2.3", "prepaid", "Spend on a prepaid card"),
               ("2.6", "wamd", "Split a bill on WAMD")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "Card acceptance, an online shop with UPayments, finance against sales and Visa commercial cards.",
     "steps": [("2.5", "acquiring", "Take cards on POS or Soft POS"), ("2.5", "upayments", "Sell online with UStore"),
               ("2.5", "posfin", "Borrow against card sales"), ("2.4", "commercial", "Give staff commercial cards")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "Transaction banking, AFAQ and the network across the Gulf and beyond.",
     "steps": [("4.3", "corporate", "Bank with NBK corporate"), ("2.6", "afaq", "Pay across the GCC"), ("4.6", "gulf", "Use branches abroad")]},
    {"id": "wealth", "who": "hnw", "name": "Grow wealth",
     "why": "NBK Wealth, Islamic options through Boubyan, and premium cards.",
     "steps": [("4.5", "wealth", "Invest with NBK Wealth"), ("4.4", "boubyan", "Add Islamic products"), ("2.1", "harrods", "Carry a premium card")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The Aura co-brand, the Miles, World and UEFA cards, Mastercard prepaid, Cirrus on debit ⚠, acceptance and the 2018 biometrics first.",
     "steps": [("2.2", "aura", "NBK-Aura World Mastercard"), ("2.2", "miles", "Miles World Mastercard"), ("2.2", "worldmc", "World, Platinum and UEFA cards"),
               ("2.3", "prepaid", "Aura and UEFA prepaid"), ("2.5", "acquiring", "Acceptance at NBK merchants"), ("3.1", "idcheck", "Identity Check, 2018 ⚠")]},
    {"id": "mcnext", "who": "mc", "name": "Where Aura, commercial cards and Weyay could land",
     "why": "Where NBK has needs and Mastercard is not yet in: deeper Aura offers, commercial and virtual cards, fraud and identity, Weyay's cards, UPayments checkout, fintech issuing and cross-border flows.",
     "steps": [("3.4", "rewards", "Offers on the Aura programme"), ("2.4", "commercial", "Virtual and commercial cards"), ("3.1", "fraud", "Network fraud scores"),
               ("4.2", "weyay", "Weyay and Jeel cards"), ("2.5", "upayments", "Merchant tools for UPayments"), ("3.3", "baas", "Issuing for fintechs"),
               ("2.6", "afaq", "Cross-border with Mastercard Move")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across National Bank of Kuwait's map",
    "title": "A Visa-led bank where Mastercard owns the Aura co-brand",
    "lead": "Visa renewed its NBK partnership for seven years in December 2022 and carries the flagship KWT, Harrods and Kuwait Airways credit cards, premium debit and commercial cards. KNET switches domestic debit and runs the WAMD instant-payment rail. Mastercard holds a solid second place: the Aura co-brand with Alshaya, the Miles, World, Platinum and UEFA cards, Mastercard prepaid, and a 2018 first in biometric cards. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are NBK's own (H1 2026 results, 20 July 2026; 2025 Annual Report) or from NBK's card pages and press. NBK publishes no split of cards or volumes by network; the debit card's scheme brand is inferred from the Cirrus sign, and Weyay's card networks are not stated.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Flagship credit", "Visa", "KWT, Harrods, Kuwait Airways, KPC"],
        ["Visa deal", "Seven years", "Renewed December 2022"],
        ["Co-brand", "Mastercard", "NBK-Aura with Alshaya, 2025 ⚠"],
        ["Travel credit", "Both", "Miles World Mastercard; Oasis Club Visa"],
        ["Debit", "KNET; Visa premium", "Cirrus abroad on standard debit ⚠"],
        ["Commercial", "Visa", "Visa Spend Clarity for Business"],
        ["Instant", "WAMD (KNET)", "In the app since June 2024"],
        ["Biometrics", "Mastercard", "GCC first, May 2018 ⚠"],
    ],
    "sides": {
        "neo": {"dir": "The Aura co-brand, the Miles, World, Platinum, UEFA and Titanium cards, Mastercard prepaid, Cirrus on debit ⚠, acceptance at NBK merchants and Identity Check ⚠.",
                "deals": "What it does not do: the flagship credit cards, premium debit, commercial cards, WAMD, AFAQ, or NBK's fraud and AI work."},
        "snb": {"dir": "Visa's flagship credit, premium debit and commercial cards under a seven-year deal, KNET for domestic debit, WAMD and Apple Pay routing, Diners Club, and NBK's own fraud, data and APIs.",
                "deals": "Where they meet: rewards and partner points, prepaid, wallets and acceptance."},
    },
    "tl": [
        ["May 2018", "Biometric card trial and Identity Check with Mastercard"],
        ["Mar 2021", "UEFA Champions League Mastercard cards ⚠"],
        ["2022", "KWT Visa Infinite launched"],
        ["Dec 2022", "Visa partnership renewed for seven years"],
        ["Dec 2022", "Apple Pay live in Kuwait, tested with KNET"],
        ["Jun 2024", "WAMD instant payments in the NBK app"],
        ["2025", "UPayments stake; Aura Mastercard and Harrods Visa cards"],
        ["Jun 2025", "Mastercard foreign-spend campaign"],
        ["Jul 2026", "Visa summer travel campaign; H1 profit KD 324.8m"],
        ["Sep 2026", "Aura cards' Mastercard benefits promoted"],
    ],
    "l": {
        "U": {"d": 1, "s": "Aura, Miles and World cardholders carry Mastercard.",
              "gap": "Most flagship credit and premium debit holders carry Visa; standard debit runs on KNET; Aura and travel cardholders carry Mastercard.",
              "neo": "Aura, Miles, World, Platinum and UEFA cardholders.", "snb": "KWT, Harrods and Kuwait Airways cardholders, premium debit, Weyay ⚠, wealth and corporate clients."},
        "L5": {"d": 1, "s": "The app and branches are NBK's; Aura is a Mastercard partner.", "gap": "App, branches and ATMs are NBK's own; of the co-brand partners only Alshaya's Aura is on Mastercard.",
               "neo": "The Aura partnership.", "snb": "App, branches, ITMs, Harrods, Kuwait Airways, KPC."},
        "L4": {"d": 0, "s": "The business lines carry KNET and Visa cards.", "gap": "Accounts come with KNET or Visa debit; Weyay's networks are not public; lending, wealth and corporate banking have no network role.",
               "neo": "Cirrus on standard debit ⚠.", "snb": "Accounts, loans, Weyay, corporate, Boubyan, NBK Wealth, international."},
        "L3": {"d": 1, "s": "Identity Check in 2018 ⚠; the rest is NBK's.", "gap": "NBK runs its own fraud platform, e-KYC, data and APIs; Mastercard's 2018 biometrics and the Aura points are its foothold.",
               "neo": "Identity Check ⚠, Aura and Miles points.", "snb": "Fraud platform, e-KYC, data and AI, BaaS, Visa-linked rewards."},
        "L2": {"d": 1, "s": "Mastercard is second to Visa in cards; KNET owns transfers.", "gap": "Visa has the flagship, premium-debit and commercial cards; Mastercard has Aura and the travel cards; KNET runs debit and WAMD.",
               "neo": "Aura, Miles, World and UEFA cards, prepaid, acceptance.", "snb": "Visa credit, debit and commercial cards, Diners, KNET, WAMD, AFAQ, UPayments."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's; the card-switch upgrade serves every scheme.", "neo": "None.", "snb": "Capital, heritage, network, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
