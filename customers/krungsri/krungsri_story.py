"""Krungsri's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from krungsri_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Thailand's fifth-largest bank and largest card issuer as five discs that stack into one platform, from a 1.94 trillion "
       "baht loan book and MUFG's stake at the bottom to the krungsri app, U CHOOSE and 555 branches at the top. Click the "
       "stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the "
       "layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("card", "Cardholders & shoppers", "credit-card"),
    ("driver", "Car buyers & borrowers", "target"),
    ("sme", "Small businesses & merchants", "store"),
    ("corp", "Thai, Japanese & global corporates", "factory"),
    ("asean", "ASEAN consumers", "earth"),
]
USERS_DESC = ("Six kinds of customer: everyday account holders, 2.4 million credit-card customers and the shoppers of Central "
              "and Lotus's, car buyers and title-loan borrowers, small businesses and the merchants on 50,000 terminals, the "
              "corporates MUFG brings, and about 19 million consumers in five ASEAN countries.")

WHO = {"con": "A Krungsri customer", "card": "A cardholder", "driver": "A car buyer", "sme": "A small business",
       "corp": "A corporate treasurer", "asean": "An ASEAN borrower"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "An account in the krungsri app, a Visa debit card, PromptPay and fraud limits.",
     "steps": [("5.1", "app", "Open the krungsri app"), ("2.3", "debit", "Pay with a Visa debit card"),
               ("2.5", "promptpay", "Pay by PromptPay QR"), ("3.1", "fraud", "Protected by transaction limits")]},
    {"id": "shop", "who": "card", "name": "Shop on a store card",
     "why": "Central The 1 on Mastercard, T1 points and Mastercard offers at Central Retail.",
     "steps": [("5.5", "partners", "Apply at Central"), ("2.2", "central", "Pay with Central The 1"),
               ("3.4", "points", "Earn T1 Dynamic Points"), ("3.4", "mcperks", "Use Mastercard Friday and lounges"), ("5.2", "uchoose", "Track it in U CHOOSE")]},
    {"id": "cards", "who": "card", "name": "Pay and borrow on a Krungsri card",
     "why": "The Krungsri card range, First Choice instalments and personal loans.",
     "steps": [("2.1", "kccards", "Take a Krungsri card"), ("2.1", "firstchoice", "Spread a purchase with First Choice"),
               ("4.2", "ploan", "Top up with a personal loan"), ("3.2", "ai", "Get offers built from card data")]},
    {"id": "travel", "who": "con", "name": "Spend abroad",
     "why": "The Visa Boarding Card, QR payments in eight markets and premium card lounges.",
     "steps": [("2.3", "boarding", "Load currencies on the Boarding Card"), ("2.5", "qrx", "Pay by QR in Japan or Korea"),
               ("3.4", "mcperks", "Use airport lounges on Central The 1")]},
    {"id": "drive", "who": "driver", "name": "Finance a car",
     "why": "Krungsri Auto's hire purchase and TIDLOR's title loans.",
     "steps": [("4.1", "autohp", "Buy on hire purchase"), ("4.1", "tidlor", "Borrow against the car at TIDLOR"), ("5.3", "branches", "Pay at a branch")]},
    {"id": "sme", "who": "sme", "name": "Run a shop",
     "why": "Card terminals that now take Amex, PromptPay and an SME loan.",
     "steps": [("5.4", "kbol", "Bank on Krungsri Biz Online"), ("2.4", "edc", "Take cards on Krungsri EDC"),
               ("2.4", "amexaccept", "Accept American Express"), ("2.5", "promptpay", "Take PromptPay"), ("4.3", "sme", "Borrow for stock")]},
    {"id": "corp", "who": "corp", "name": "Run a Japanese or Thai corporate",
     "why": "MUFG's network, transaction banking, APIs and green loans.",
     "steps": [("4.4", "corp", "Bank with Krungsri and MUFG"), ("2.5", "txn", "Pool cash across ASEAN"),
               ("3.3", "baas", "Connect by API"), ("4.4", "ssf", "Finance the transition")]},
    {"id": "asean", "who": "asean", "name": "Borrow in the Philippines or Cambodia",
     "why": "Home Credit, SB Finance and Hattha Bank.",
     "steps": [("4.6", "homecredit", "Buy a phone on Home Credit"), ("4.6", "hattha", "Bank with Hattha")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Central The 1, the Krungsri Platinum Mastercard, Mastercard's travel and retail benefits, and acceptance on Krungsri terminals.",
     "steps": [("2.2", "central", "Central The 1 on Mastercard"), ("2.1", "kplatmc", "Krungsri Platinum Mastercard"),
               ("3.4", "mcperks", "Priority Pass and Mastercard Friday"), ("2.4", "edc", "Mastercard accepted on 50,000 terminals")]},
    {"id": "mcnext", "who": "mc", "name": "Where new cards, data and fraud tools could land",
     "why": "Where Krungsri has needs and Mastercard is not yet in: the new cards planned for 2026, Lotus's and ASEAN card launches, data-built offers, Bank of Thailand fraud rules and travel FX.",
     "steps": [("2.1", "kccards", "New 2026 cards on Mastercard"), ("2.2", "lotus", "Lotus's card network"),
               ("3.2", "ai", "Merchant data for segment offers"), ("3.1", "fraud", "Scam and alert tools"),
               ("2.3", "boarding", "Travel FX against the Visa Boarding Card"), ("4.6", "homecredit", "ASEAN co-brand cards")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Krungsri's map",
    "title": "Thailand's top card issuer, Visa-led, with Central The 1 on Mastercard",
    "lead": "Krungsri is Thailand's largest card issuer by number of cards (15%). Its own-brand premium cards, debit cards and the Boarding Card run on Visa, with JCB alongside. Mastercard's anchor is Central The 1, about 960,000 cards issued by Krungsri's General Card Services, plus a Krungsri Platinum Mastercard. No network agreement or Mastercard services deal is public. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (1H 2026 results, 20 July 2026; analyst briefings, February and August 2026) or Krungsri Consumer's via Thairath. Networks come from card pages read on 17 October 2026; Lotus's cards name both Mastercard and Visa, and the overall split by volume is not disclosed.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Credit cards", "#1 by number", "15% share; 2.4m customers"],
        ["Own-brand premium", "Visa", "Signature, Infinite, Platinum"],
        ["Central The 1", "Mastercard", "About 960,000 cards, 5.8% share"],
        ["Lotus's", "Mastercard or Visa ⚠", "50% joint venture"],
        ["Debit & travel", "Visa", "Boarding Card, 16 currencies"],
        ["Acceptance", "50,127 terminals", "Amex added Sep 2026"],
        ["Real-time", "PromptPay", "2.38bn payments, Dec 2025"],
        ["2026 plan", "New credit cards", "Network not announced"],
    ],
    "sides": {
        "neo": {"dir": "Central The 1 and the Krungsri Platinum Mastercard, Priority Pass and Mastercard Friday offers, and acceptance on Krungsri's terminals.",
                "deals": "What it does not do: Krungsri-branded premium cards, debit, the Boarding Card, First Choice, or any fraud, data or token service in public."},
        "snb": {"dir": "Visa on premium, debit and travel cards, JCB with MUFG's Japan links, Amex on the terminals, and PromptPay and QR for everyday payments.",
                "deals": "Where they meet: the new cards planned for 2026 and the Lotus's programme."},
    },
    "tl": [
        ["Dec 2013", "MUFG becomes majority owner"],
        ["Jun 2022", "Boarding Card on Visa ⚠ date"],
        ["Mar 2024", "Visa Paris campaign on debit and Boarding cards"],
        ["2025", "T1 Dynamic Points on Central The 1"],
        ["Aug 2025", "TIDLOR consolidated"],
        ["Feb 2026", "#1 card issuer, 15% share"],
        ["Aug 2026", "Central The 1 at 960,000 cards; new cards planned"],
        ["Sep 2026", "Amex on Krungsri EDC; Mastercard Friday at Central"],
    ],
    "l": {
        "U": {"d": 1, "s": "Central The 1 holders carry Mastercard; most others carry Visa.",
              "gap": "Shoppers at Central carry Mastercard; Krungsri-branded and debit cardholders carry Visa or JCB.",
              "neo": "Central The 1 and Platinum Mastercard holders.", "snb": "Debit holders, Krungsri premium and First Choice cardholders, borrowers."},
        "L5": {"d": 1, "s": "The front doors are Krungsri's; the Central partnership runs on Mastercard.", "gap": "App, U CHOOSE and branches are the bank's; Central Retail is the Mastercard partner.",
               "neo": "Central Retail partnership.", "snb": "krungsri app, U CHOOSE, branches, Biz Online."},
        "L4": {"d": 0, "s": "The business lines carry no network.", "gap": "Car finance, loans, mortgages, corporate and ASEAN lending have no network role; ASEAN card launches are open.",
               "neo": "None.", "snb": "Krungsri Auto, TIDLOR, loans, corporate, wealth, Hattha Visa debit."},
        "L3": {"d": 1, "s": "Mastercard's travel and retail benefits on Central The 1; the rest is Krungsri's.", "gap": "Fraud, AI and APIs are in-house; Mastercard runs lounges and Mastercard Friday offers.",
               "neo": "Priority Pass, Travel & Lifestyle, Mastercard Friday.", "snb": "Fraud limits, AI, BaaS, Krungsri Points."},
        "L2": {"d": 1, "s": "Central The 1 on Mastercard; premium, debit and travel on Visa.", "gap": "Visa leads the own-brand range, debit and travel; Mastercard holds Central The 1 and one Platinum card.",
               "neo": "Central The 1, Krungsri Platinum Mastercard, acceptance.", "snb": "Visa cards, JCB, Amex acceptance, PromptPay, QR."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, MUFG, technology, plan."},
    },
    "t": area_lens(LAYERS),
}
