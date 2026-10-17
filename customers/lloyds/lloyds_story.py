"""Lloyds Banking Group's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from lloyds_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Britain's biggest retail bank as five discs that stack into one platform, from half of UK adults and £491 billion "
       "of loans at the bottom to the Lloyds app, branches and brokers at the top. Click the stack to open it. Choose who "
       "you are and what you want to do, and the areas that deliver it light up across the layers, joined in the order "
       "they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("home", "Homebuyers", "house"),
    ("driver", "Drivers & fleets", "target"),
    ("aff", "Savers & pension members", "coins"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Six kinds of customer, about 28 million in all: everyday customers, homebuyers, drivers and fleets, savers "
              "and pension members, a million businesses and the corporates CIB serves.")

WHO = {"con": "A Lloyds customer", "home": "A homebuyer", "driver": "A driver", "aff": "A saver", "sme": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a Visa debit card, the app, the AI assistant and fraud checks.",
     "steps": [("4.1", "accounts", "Open a current account"), ("2.1", "debit", "Pay with Visa debit"), ("5.1", "app", "Run it in the app"),
               ("3.2", "assistant", "Ask the AI assistant"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "wallet", "who": "con", "name": "Put every card in one wallet",
     "why": "Curve, now Lloyds', and the Smart Wallet coming in late 2026.",
     "steps": [("2.3", "curve", "Use Curve"), ("2.3", "smartwallet", "Move to the Smart Wallet"), ("3.3", "rewards", "Earn rewards")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "Lloyds, Halifax, Bank of Scotland and MBNA cards, moving to Visa.",
     "steps": [("2.2", "credit", "Take a credit card"), ("3.3", "rewards", "Collect Lloyds Rewards")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "The UK's largest mortgage lender, through branches and brokers.",
     "steps": [("5.3", "brokers", "Apply through a broker"), ("4.1", "mortgages", "Take a mortgage"), ("4.4", "widows", "Protect it with Scottish Widows")]},
    {"id": "drive", "who": "driver", "name": "Finance or lease a car",
     "why": "Lloyds Auto: one in eight UK EVs.",
     "steps": [("5.3", "brokers", "Visit a dealer"), ("4.2", "auto", "Finance or lease with Lloyds Auto")]},
    {"id": "pension", "who": "aff", "name": "Save for retirement",
     "why": "Scottish Widows and Lloyds Wealth.",
     "steps": [("4.4", "widows", "Save in a workplace pension and ISA"), ("5.1", "app", "See it in the app")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A business account, card acceptance with Stripe, open-banking payments and Connected Commerce.",
     "steps": [("4.3", "business", "Open a business account"), ("2.4", "accept", "Take cards with Lloyds Accept"),
               ("2.5", "payfrom", "Collect by bank"), ("3.3", "rewards", "Reach Lloyds customers with cashback")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "Transaction banking and the group's tokenised-money work.",
     "steps": [("4.3", "cib", "Bank with CIB"), ("2.6", "digitalmoney", "Settle with tokenised deposits")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Curve, the credit cards still to be reissued, PayFrom Bank and scam scoring.",
     "steps": [("2.3", "curve", "Curve on Mastercard"), ("2.2", "credit", "Credit cards until reissued"),
               ("2.5", "payfrom", "PayFrom Bank on Mastercard Open Banking"), ("3.1", "cfr", "Consumer Fraud Risk")]},
    {"id": "mcnext", "who": "mc", "name": "Where Curve, agents and stablecoins could land",
     "why": "Where Lloyds has needs and Mastercard is not yet in: the Smart Wallet built on Curve, agentic payments, stablecoin settlement, Connected Commerce offers and fleet cards.",
     "steps": [("2.3", "smartwallet", "Smart Wallet on Curve's Mastercard rails"), ("3.2", "assistant", "Agent Pay for the assistant"),
               ("2.6", "digitalmoney", "Stablecoin settlement against Visa's pilot"), ("3.3", "rewards", "Card-linked offers"), ("4.2", "auto", "Fleet and fuel cards")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Lloyds Banking Group's map",
    "title": "A Visa bank buying a Mastercard wallet",
    "lead": "Visa has carried Lloyds' debit cards for about 40 years, and a June 2024 deal moves the group's 10 million credit cards from Mastercard to Visa by the end of 2026. In May 2026 Lloyds bought Curve, a Mastercard issuer, and is building its Smart Wallet on it. Mastercard also powers PayFrom Bank and scored Lloyds' transfers for scams from 2023. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (H1 2026 results, 30 July 2026) or from Lloyds, Visa, Curve and press. Several card pages were not reachable; current networks for Halifax and MBNA cards are inferred from the 2024 Visa deal.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa", "About 40 years; 30 million accounts"],
        ["Credit", "Mastercard to Visa", "10 million cards by end-2026"],
        ["Curve", "Mastercard", "Bought May 2026; 6 million customers"],
        ["Open banking", "PayFrom Bank", "Mastercard Open Banking Connect, 2021 ⚠"],
        ["Scams", "Consumer Fraud Risk", "Launch bank, 2023 ⚠"],
        ["Stablecoins", "Visa pilot", "September 2026"],
        ["Acceptance", "Stripe", "Lloyds Accept, June 2026"],
    ],
    "sides": {
        "neo": {"dir": "Curve and the credit cards not yet reissued, PayFrom Bank, scam scores, and acceptance at Lloyds' merchants.",
                "deals": "What it does not do: debit, the future credit book, stablecoin settlement, AI or rewards."},
        "snb": {"dir": "Visa debit and credit and the stablecoin pilot, Stripe for acceptance, Lloyds' own fraud models, AI and tokenised deposits.",
                "deals": "Where they meet: Curve and the Smart Wallet built on it."},
    },
    "tl": [
        ["Jul 2021", "PayFrom Bank on Mastercard Open Banking"],
        ["Jul 2023", "Consumer Fraud Risk with Lloyds, Halifax and Bank of Scotland"],
        ["Jun 2024", "Credit cards to move to Visa"],
        ["Nov 2025", "Curve acquisition announced"],
        ["May 2026", "Curve joins Lloyds"],
        ["Jul 2026", "Halifax brand to retire; Accelerate 2030"],
        ["Sep 2026", "Visa stablecoin settlement pilot"],
        ["End-2026", "Credit migration to Visa due"],
    ],
    "l": {
        "U": {"d": 1, "s": "Curve users and unconverted credit cardholders carry Mastercard.",
              "gap": "Debit holders carry Visa and credit cardholders are moving to it; Curve's 6 million carry Mastercard.",
              "neo": "Curve users, credit cardholders until reissue.", "snb": "Debit holders, future credit holders, mortgage and pension customers."},
        "L5": {"d": 0, "s": "The front doors are Lloyds'.", "gap": "App, branches and brokers are the group's.", "neo": "None.", "snb": "App, branches, brokers."},
        "L4": {"d": 0, "s": "The business lines carry Visa cards.", "gap": "Accounts come with Visa debit; mortgages, Lloyds Auto and pensions have no network role.",
               "neo": "None.", "snb": "Accounts, mortgages, Lloyds Auto, Scottish Widows."},
        "L3": {"d": 1, "s": "Scam scores are Mastercard's ⚠; the rest is Lloyds'.", "gap": "Consumer Fraud Risk was adopted in 2023; AI and rewards are Lloyds' own.",
               "neo": "Consumer Fraud Risk ⚠.", "snb": "Fraud models, AI assistant, rewards."},
        "L2": {"d": 1, "s": "Curve and PayFrom on Mastercard; cards moving to Visa.", "gap": "Visa has debit and is taking credit; Mastercard keeps Curve and open-banking payments.",
               "neo": "Curve, PayFrom Bank, credit until reissue.", "snb": "Visa debit and credit, Stripe, tokenised money."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, brands, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
