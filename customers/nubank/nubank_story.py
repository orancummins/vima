"""Nu Holdings' kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from nubank_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Brazil's largest private financial institution by customers, as five discs that stack into one platform, from 139 million customers, "
       "a $39 billion credit book and new banking licences at the bottom to one app in four countries at the top. "
       "Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it light "
       "up across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard "
       "goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("affl", "Affluent customers", "gem"),
    ("saver", "Savers & investors", "coins"),
    ("sme", "Small businesses", "briefcase"),
    ("xb", "Cross-border customers", "plane"),
    ("merch", "Merchants on NuPay", "store"),
]
USERS_DESC = ("Six kinds of user, 139 million customers in all: everyday customers in Brazil, Mexico, Colombia and now "
              "the US, affluent Croma and Ultravioleta members, savers and investors, 6 million small businesses, "
              "people moving money across borders, and the merchants that take NuPay.")

WHO = {"con": "A Nu customer", "affl": "An Ultravioleta member", "saver": "A saver", "sme": "A small business",
       "xb": "A cross-border customer", "merch": "A merchant"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: the app, a Mastercard credit card, Pix and fraud protection.",
     "steps": [("5.1", "app", "Open the Nu app"), ("3.3", "kyc", "Onboard digitally"), ("2.1", "ccbr", "Get a Nu Mastercard"),
               ("2.4", "pix", "Send a Pix"), ("3.1", "security", "Turn on Street Mode")]},
    {"id": "tap", "who": "con", "name": "Pay in a shop",
     "why": "One tap that can be Pix, debit or credit, and Pix in instalments.",
     "steps": [("2.5", "paybytap", "Tap the phone"), ("2.3", "debitbr", "Pay by debit"), ("2.4", "pixcredit", "Or spread a Pix over 12 months")]},
    {"id": "premium", "who": "affl", "name": "Move up to Ultravioleta",
     "why": "Nu's push into mid- and high-income customers on Mastercard Black and Platinum.",
     "steps": [("2.2", "croma", "Start with Croma"), ("2.2", "ultravioleta", "Upgrade to Ultravioleta"),
               ("3.4", "points", "Earn points and cashback"), ("2.6", "contaglobal", "Spend abroad with Conta Global")]},
    {"id": "save", "who": "saver", "name": "Save and invest",
     "why": "Caixinhas, Nu Investimentos and crypto.",
     "steps": [("4.2", "nuconta", "Save in a Caixinha"), ("4.2", "investments", "Invest with Nu Investimentos"), ("2.6", "crypto", "Buy crypto")]},
    {"id": "borrow", "who": "con", "name": "Borrow",
     "why": "Loans priced by AI in under a second.",
     "steps": [("1.5", "aiagents", "Ask the AI Private Banker"), ("4.1", "loans", "Take a personal or payroll loan"), ("3.3", "nuscore", "Watch your score")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "Nu Empresas for 6 million companies.",
     "steps": [("4.3", "empresas", "Open a Nu Empresas account"), ("4.3", "smeaccept", "Take cards with Tap to Pay"),
               ("2.4", "pix", "Get paid by Pix"), ("2.1", "othercards", "Use the business card")]},
    {"id": "abroad", "who": "xb", "name": "Hold and send money abroad",
     "why": "Nu Global, US-to-LatAm transfers and the US card.",
     "steps": [("2.6", "nuglobal", "Hold dollars in Nu Global"), ("2.6", "remit", "Send home to a Pix key"), ("4.5", "uscard", "Spend on the US card")]},
    {"id": "nupay", "who": "merch", "name": "Take NuPay",
     "why": "A Nubank-only checkout reached through PPRO, EBANX and Uber.",
     "steps": [("5.3", "partners", "Connect through PPRO"), ("2.5", "nupay", "Offer NuPay")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Every named Nu card programme: credit and debit in Brazil and Mexico, Black and Platinum, Colombia, the US World Elite card and Nu Global's virtual card.",
     "steps": [("2.1", "ccbr", "Brazil credit card"), ("2.2", "ultravioleta", "Ultravioleta Black and Croma Platinum"),
               ("2.1", "ccmx", "Mexico credit card"), ("2.3", "debitmx", "Mexico debit card"),
               ("4.5", "uscard", "US World Elite card"), ("2.6", "nuglobal", "Nu Global virtual card")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, tokens and scam tools could land",
     "why": "Where Nu has needs and Mastercard is not yet in: Agent Pay for Nu's AI, tokens under Pay by Tap and NuPay, scam tools for Pix, cross-border payouts, small-business acceptance and premium benefits.",
     "steps": [("1.5", "aiagents", "Agent Pay for the AI Private Banker"), ("2.5", "paybytap", "Mastercard tokens under Pay by Tap"),
               ("3.1", "security", "Scam scoring for Pix and SPEI"), ("2.6", "nuglobal", "Move and stablecoin settlement"),
               ("4.3", "smeaccept", "Tap on Phone for small firms"), ("3.4", "points", "Priceless for Croma and Ultravioleta")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Nubank's map",
    "title": "Mastercard on every Nu card, while Pix takes the spend",
    "lead": "Nubank started in 2014 with a Mastercard card, when Mastercard was the only network willing to work with it, and every Nu card programme whose network is named is still Mastercard: credit and debit in Brazil and Mexico, Black and Platinum, Colombia, the US World Elite card under an 'exclusive relationship', and Nu Global's virtual card. No Visa or Elo programme was found. But Nu moves spend off the card rails with Pix, Pix financing, Pay by Tap and NuPay, the agreements found are trademark licences with no public terms, and its new CFO came from Visa. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Nu's own (Q2 2026 results, 13 August 2026; FY2025 results and 20-F) or from Nu's newsroom and press. Mastercard's newsroom was blocked. Networks for Nubank+, the SME and under-18 cards and the US debit card are not stated.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Credit", "Mastercard", "$26bn of cards, Brazil, Mexico, Colombia"],
        ["Premium", "Mastercard Black, Platinum", "Ultravioleta 2021, Croma July 2026"],
        ["Debit", "Mastercard", "Brazil, Mexico; Colombia ATM network ⚠"],
        ["US", "World Elite, exclusive", "September 2026"],
        ["Nu Global", "Virtual Mastercard", "Over USDC and EURC"],
        ["Pix", "Off the cards", "Transfers and 12-instalment credit"],
        ["Checkout", "NuPay", "Account-based, via PPRO"],
        ["Agreements", "Trademark licences", "Terms not public ⚠"],
    ],
    "sides": {
        "neo": {"dir": "Every named Nu card: credit, debit, Black and Platinum in Brazil, Mexico's cards, Colombia's cards, the US World Elite card and Nu Global's virtual card.",
                "deals": "What it does not do: Pix and Pix financing, SPEI and Bre-B, NuPay, open finance, Nu's fraud tools and AI, or tokens under Pay by Tap as far as is public."},
        "snb": {"dir": "Pix, SPEI and Bre-B, NuPay, open-finance initiation, stablecoins and crypto with Fireblocks, and Nu's own fraud, AI and rewards. No Visa or Elo programme was found.",
                "deals": "Where they meet: the card limit, which Nu lends against both on Mastercard and through Pix financing."},
    },
    "tl": [
        ["Apr 2014", "First Nu Mastercard transaction"],
        ["Jan 2019", "Mastercard licence for Mexico"],
        ["Apr 2020", "Mastercard licence for Colombia"],
        ["2021", "Ultravioleta Mastercard Black"],
        ["2022", "NuPay and Pix financing launched"],
        ["May 2023", "Mexico debit card with Mastercard"],
        ["Apr 2026", "Pay by Tap: Pix, debit and credit in one tap"],
        ["Jul 2026", "Rob Livingston, from Visa, becomes CFO; Croma Mastercard Platinum"],
        ["Sep 2026", "US World Elite card and Nu Global's virtual Mastercard"],
    ],
    "l": {
        "U": {"d": 2, "s": "Every Nu cardholder carries Mastercard.",
              "gap": "Cardholders in Brazil, Mexico, Colombia and the US carry Mastercard; much of their spending also goes by Pix, SPEI and NuPay.",
              "neo": "Credit and debit cardholders, Ultravioleta and Croma members, US and Nu Global customers.", "snb": "Pix and NuPay users, savers and investors, NuCel customers."},
        "L5": {"d": 0, "s": "The front doors are Nu's.", "gap": "The app and cash points are Nu's; Mastercard is its card partner.", "neo": "Card partner.", "snb": "App, cash points, Lead Bank, PPRO, Claro."},
        "L4": {"d": 1, "s": "The US card is Mastercard; the other lines are Nu's.", "gap": "Loans, deposits, investments and NuCel have no network role; the US card is World Elite; SME card networks are not stated.",
               "neo": "US World Elite card.", "snb": "Loans, deposits, investments, NuCel, insurance."},
        "L3": {"d": 1, "s": "Rewards ride on Mastercard cards; the services are Nu's.", "gap": "Points are earned on Mastercard cards; fraud tools, open finance and onboarding are Nu's own.",
               "neo": "Card rewards.", "snb": "Street Mode, open finance, NuScore, Vantagens Nu."},
        "L2": {"d": 1, "s": "Cards on Mastercard; Pix and NuPay beside them.", "gap": "Every named card programme is Mastercard; Pix, Pix financing, SPEI, Bre-B, NuPay and crypto are not.",
               "neo": "Credit, debit, premium cards, Nu Global.", "snb": "Pix, Pix financing, SPEI, Bre-B, NuPay, crypto."},
        "L1": {"d": 1, "s": "Nu's own scale, built on a Mastercard card.", "gap": "Capital, licences and AI are Nu's; the company began with a Mastercard card in 2014.", "neo": "The founding card.", "snb": "Capital, licences, AI, strategy."},
    },
    "t": area_lens(LAYERS),
}
