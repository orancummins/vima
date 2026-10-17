"""Scotiabank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from scotiabank_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Canada's most international bank as five discs that stack into one platform, from C$1.55 trillion of assets and "
       "stakes in KeyCorp and Davivienda at the bottom to the Scotia app, 1,984 branches and partners at the top. Click the "
       "stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the "
       "layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("tang", "Tangerine clients", "smartphone"),
    ("latam", "Clients in Latin America & the Caribbean", "earth"),
    ("aff", "Wealth clients", "gem"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates & institutions", "factory"),
]
USERS_DESC = ("Six kinds of client: more than 11 million everyday customers in Canada, 2 million Tangerine clients, more "
              "than 8 million in Latin America and the Caribbean, 2 million wealth clients, small businesses, and the "
              "corporates Global Banking and Markets serves.")

WHO = {"con": "A Scotiabank customer", "tang": "A Tangerine client", "latam": "A client in Latin America", "aff": "A wealth client",
       "sme": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, an Interac and Visa Debit card, the Scotia app, AI prompts and scam alerts.",
     "steps": [("5.2", "branches", "Open an account"), ("2.2", "debitca", "Pay with Interac or Visa Debit"), ("5.1", "app", "Run it in the Scotia app"),
               ("3.2", "predictive", "Get AI payment prompts"), ("3.1", "fraud", "Protected from scams")]},
    {"id": "rewards", "who": "con", "name": "Earn Scene+ on a card",
     "why": "Scene+ Visa and Amex cards, Shell fuel savings and rent through Casa.",
     "steps": [("2.1", "visacredit", "Take a Scene+ or Passport Visa"), ("3.3", "sceneplus", "Earn at Sobeys and Cineplex"),
               ("3.3", "shell", "Save at Shell"), ("5.3", "partners", "Pay rent through Casa")]},
    {"id": "tangerine", "who": "tang", "name": "Bank digitally with Tangerine",
     "why": "A no-fee account with Visa Debit and Mastercard credit cards that now earn Scene+.",
     "steps": [("2.3", "tangdebit", "Open a no-fee chequing account"), ("2.3", "tangworldelite", "Earn Scene+ on a World Elite Mastercard"),
               ("2.7", "wallets", "Add it to a mobile wallet")]},
    {"id": "home", "who": "con", "name": "Buy a home",
     "why": "Mortgage+ bundles a mortgage, an everyday account and a card.",
     "steps": [("4.1", "mortgages", "Take a Mortgage+ bundle"), ("2.1", "visacredit", "Add a Scotiabank credit card"), ("4.1", "hisa", "Save in the Scotia HISA")]},
    {"id": "latam", "who": "latam", "name": "Bank in Mexico, Peru or Chile",
     "why": "Fourth-ranked banks with digital onboarding, Visa-led cards, both networks in Peru and PLIN.",
     "steps": [("5.1", "intlapp", "Open an account in the app"), ("2.4", "mexicocards", "Pay with a Scotiabank Mexico card"),
               ("2.5", "perucards", "Choose Visa or Mastercard in Peru"), ("2.7", "plin", "Send money with PLIN")]},
    {"id": "carib", "who": "latam", "name": "Bank in the Caribbean",
     "why": "Mastercard debit since 2020, with Visa and Mastercard credit.",
     "steps": [("2.6", "caribdebit", "Pay with a ScotiaCard Mastercard Debit"), ("2.6", "caribcredit", "Take a Visa or Mastercard credit card"),
               ("4.3", "intl", "Bank with International Banking")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A business account, the new no-fee business Visa, cash management and fuel savings.",
     "steps": [("4.2", "bizbanking", "Open a business account"), ("2.1", "bizvisa", "Spend on a business Visa"),
               ("2.8", "scotiaconnect", "Manage cash in ScotiaConnect"), ("3.3", "shell", "Save on fuel at Shell")]},
    {"id": "corp", "who": "corp", "name": "Move money across the corridor",
     "why": "Global Banking and Markets, ScotiaConnect in Canada, the US and Mexico, tokenised deposits and Davivienda's footprint.",
     "steps": [("4.5", "gbm", "Bank with Global Banking and Markets"), ("2.8", "scotiaconnect", "Run US and Mexico cash management"),
               ("2.8", "digitalmoney", "Settle with tokenised deposits"), ("1.5", "davivienda", "Reach clients through Davivienda")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Tangerine's credit cards, Caribbean debit, half of Peru's range, a World Elite tier in Mexico and a legacy Canadian portfolio.",
     "steps": [("2.3", "tangworldelite", "Tangerine World Elite Mastercard"), ("2.3", "tangmoneyback", "Tangerine Money-Back Mastercard"),
               ("2.6", "caribdebit", "Caribbean Mastercard Debit"), ("2.5", "perucards", "Peru's Mastercard range"),
               ("2.4", "mexicocards", "World Elite tier in Mexico ⚠")]},
    {"id": "mcnext", "who": "mc", "name": "Where Scene+, scams and the corridor could land",
     "why": "Where Scotiabank has needs and Mastercard is not yet in: Scene+ offers, scam scoring for the Real-Time Rail, the Caribbean renewal, commercial cards, agentic payments and tokenised money.",
     "steps": [("3.3", "sceneplus", "Card-linked offers for Scene+"), ("3.1", "fraud", "Real-time scam scoring"),
               ("2.6", "caribdebit", "Renew Caribbean debit around 2027"), ("4.2", "bizbanking", "Commercial and virtual cards"),
               ("3.2", "predictive", "Agent Pay for AI prompts"), ("2.8", "digitalmoney", "Multi-Token Network for tokenised deposits")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Scotiabank's map",
    "title": "Visa and Amex at home, Mastercard at Tangerine and abroad",
    "lead": "Scotiabank's own Canadian cards run on Visa and American Express, and its debit on Interac and Visa Debit; Visa launched the premium Infinite Privilege card with it in 2025 and the new business card in 2026. Mastercard carries Tangerine's credit cards, now including a World Elite card that earns Scene+, Caribbean debit under a 2020 deal, half of Peru's range and a World Elite tier in Mexico. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (Q3 2026 results, 25 August 2026) or from Scotiabank, Tangerine and subsidiary product pages and releases. Web search was capped and the Mastercard and Visa newsrooms were not checked; Mexico's World Elite network and the legacy 2015 portfolio are inferred.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Scotiabank credit", "Visa and Amex", "Infinite Privilege with Visa, Mar 2025"],
        ["Business cards", "Visa", "New no-fee card, Aug 2026"],
        ["Canadian debit", "Interac and Visa Debit", "Scotiabank and Tangerine"],
        ["Tangerine credit", "Mastercard", "World Elite launched Apr 2026"],
        ["Caribbean debit", "Mastercard", "Seven-year deal, Mar 2020"],
        ["Peru", "Visa and Mastercard", "Both full ranges"],
        ["Mexico and Chile", "Visa-led", "World Elite tier in Mexico ⚠"],
        ["Loyalty", "Scene+", "15 million+ members; network-neutral"],
    ],
    "sides": {
        "neo": {"dir": "Tangerine's cards, Caribbean debit, Peru's Mastercard range, Mexico's World Elite tier ⚠ and a legacy Canadian portfolio ⚠.",
                "deals": "What it does not do: Scotiabank-brand credit, business cards or debit in Canada, Chile, cash management, AI or tokenised money."},
        "snb": {"dir": "Visa for Scotiabank credit, business and debit co-badge, Mexico and Chile; Amex for Scene+ Gold and Platinum; Interac and PLIN for instant payments; Scotiabank's own fraud and AI.",
                "deals": "Where they meet: Scene+, earned on all three networks, and Peru and the Caribbean, where both issue."},
    },
    "tl": [
        ["Oct 2015", "JPMorgan Chase Canada Mastercard portfolio bought"],
        ["2016", "Tangerine Money-Back Mastercard"],
        ["Nov 2017", "Scotiabank Masterpass"],
        ["Dec 2019", "Seven-year Visa deal, Central America and Caribbean"],
        ["Mar 2020", "Seven-year Mastercard debit deal, four Caribbean markets"],
        ["Dec 2024", "KeyCorp stake completed"],
        ["Mar 2025", "Passport Visa Infinite Privilege"],
        ["Dec 2025", "Davivienda deal closes"],
        ["Apr 2026", "Tangerine World Elite Mastercard"],
        ["Aug 2026", "No-fee business Visa; record Q3"],
        ["Sep 2026", "CAD tokenised deposits; Project Agorá"],
        ["Q4 2026", "Real-Time Rail due"],
    ],
    "l": {
        "U": {"d": 1, "s": "Tangerine, Caribbean and some Peru clients carry Mastercard.",
              "gap": "Most Scotiabank-brand cardholders in Canada carry Visa or Amex; Tangerine's credit clients and Caribbean debit holders carry Mastercard.",
              "neo": "Tangerine credit clients, Caribbean debit holders, Peru Mastercard holders.", "snb": "Scotiabank Canada cardholders, Mexico and Chile clients, businesses."},
        "L5": {"d": 0, "s": "The front doors are Scotiabank's.", "gap": "Apps, branches and partners such as Casa are the bank's own.", "neo": "None.", "snb": "Scotia app, branches, Casa."},
        "L4": {"d": 0, "s": "The business lines lean on Visa.", "gap": "Mortgages bundle Visa cards and business banking issues Visa; International Banking is the exception.",
               "neo": "Peru and the Caribbean within International Banking.", "snb": "Mortgages, business banking, wealth, GBM."},
        "L3": {"d": 1, "s": "Scene+ is network-neutral; the rest is Scotiabank's.", "gap": "Fraud, onboarding and AI are in-house; Scene+ is earned on Mastercard only through Tangerine.",
               "neo": "Scene+ on Tangerine Mastercard.", "snb": "Fraud tools, Nova Credit, Predictive UX."},
        "L2": {"d": 1, "s": "Mastercard at Tangerine, in the Caribbean and in Peru.", "gap": "Visa and Amex hold Scotiabank Canada; Mastercard holds Tangerine credit and Caribbean debit; Interac, PLIN and tokens sit outside cards.",
               "neo": "Tangerine cards, Caribbean debit, Peru, Mexico World Elite ⚠.", "snb": "Visa and Amex credit, Interac and Visa Debit, ScotiaConnect, tokens."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, leadership, AI, stakes."},
    },
    "t": area_lens(LAYERS),
}
