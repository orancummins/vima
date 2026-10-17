"""Eurobank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from eurobank_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("One of Greece's four big banks as five discs that stack into one platform, from €113 billion of assets across "
       "Greece, Cyprus and Bulgaria at the bottom to the Eurobank app, branches and partners at the top. Click the stack "
       "to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("home", "Homebuyers", "house"),
    ("wealth", "Savers & private clients", "gem"),
    ("sme", "Small businesses & merchants", "store"),
    ("corp", "Corporates", "factory"),
    ("intl", "Customers in Cyprus & Bulgaria", "earth"),
]
USERS_DESC = ("Six kinds of customer: everyday customers and homebuyers in Greece, savers and private-banking clients, "
              "small businesses and merchants, corporates, and the customers of Eurobank Cyprus and Postbank in Bulgaria. "
              "No group customer count is published.")

WHO = {"con": "A Eurobank customer", "home": "A homebuyer", "wealth": "A private client", "sme": "A small business",
       "corp": "A corporate treasurer", "intl": "A customer in Cyprus or Bulgaria"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "Open an account in the app, pay with a Eurobank card in a wallet, and earn €pistrofi.",
     "steps": [("3.4", "onboard", "Open an account in the app"), ("2.1", "grcards", "Pay with a Eurobank card"),
               ("2.4", "wallets", "Tap with a phone wallet"), ("5.1", "app", "Run it in the app"), ("3.3", "epistrofi", "Earn €pistrofi")]},
    {"id": "card", "who": "con", "name": "Get the most from a card",
     "why": "A Mastercard from Eurobank, with Priceless and the EVA assistant.",
     "steps": [("2.1", "grcards", "Take a Eurobank Mastercard"), ("3.3", "priceless", "Book Priceless experiences"),
               ("3.2", "eva", "Ask EVA"), ("3.3", "epistrofi", "Collect cashback")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "Through a branch or the app, with AI in the mortgage assessment.",
     "steps": [("5.2", "branches", "Visit a branch"), ("4.1", "mortgages", "Take a mortgage"), ("4.4", "eurolife", "Insure it with Eurolife")]},
    {"id": "wealth", "who": "wealth", "name": "Save and invest",
     "why": "Private banking, funds, Luxembourg and life insurance.",
     "steps": [("4.3", "wealth", "Invest with private banking"), ("4.4", "eurolife", "Save with Eurolife"), ("2.2", "worldelite", "Carry World Elite")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "Business cards, acceptance through Worldline or a phone, and pay-later for shoppers from 2027.",
     "steps": [("4.2", "business", "Bank with Eurobank"), ("2.1", "bizcards", "Use a business card"),
               ("2.5", "worldline", "Take cards with Worldline"), ("2.5", "smartpos", "Or with Smart POS on a phone"), ("2.7", "inbank", "Offer pay-later")]},
    {"id": "corp", "who": "corp", "name": "Finance a company",
     "why": "€36 billion of business loans and instant payments.",
     "steps": [("4.2", "business", "Borrow"), ("2.6", "iris", "Move money on IRIS"), ("2.1", "bizcards", "Equip staff with cards")]},
    {"id": "intl", "who": "intl", "name": "Bank in Cyprus or Bulgaria",
     "why": "Eurobank Cyprus after Hellenic Bank, and Postbank in the eurozone.",
     "steps": [("4.5", "cyprus", "Bank with Eurobank Cyprus"), ("2.2", "cycards", "Pick a Visa or Mastercard"),
               ("3.1", "controls", "Control it in the app"), ("2.3", "bgcards", "Or a Postbank card in Bulgaria")]},
    {"id": "remit", "who": "con", "name": "Send money home",
     "why": "Remittances from Greece to India on UPI.",
     "steps": [("5.1", "app", "Open the app"), ("2.6", "upi", "Send to India on UPI")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Greek cards moving to Mastercard, Priceless, World Elite and half the Cyprus and Bulgarian ranges.",
     "steps": [("2.1", "grcards", "All Greek cards on Mastercard"), ("2.1", "bizcards", "Business cards"),
               ("3.3", "priceless", "Priceless"), ("2.2", "worldelite", "World Elite in Cyprus"), ("2.3", "bgcards", "Postbank Mastercard")]},
    {"id": "mcnext", "who": "mc", "name": "Where the migration, agents and instalments could land",
     "why": "Where Eurobank has needs and Mastercard is not yet in: keeping tokens through the reissue, Cyprus and Bulgaria still split, instalments beside the Inbank JV, agentic payments for EVA, fraud, and the India corridor.",
     "steps": [("2.4", "wallets", "Token and billing continuity through the reissue"), ("2.2", "cycards", "Cyprus range to Mastercard"),
               ("2.7", "inbank", "Installments beside pay-later"), ("3.2", "eva", "Agent Pay for EVA"),
               ("3.1", "fraud", "Fraud and identity tools"), ("2.6", "upi", "Mastercard Move for remittances")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Eurobank's map",
    "title": "A dual-network bank going all-Mastercard in Greece",
    "lead": "Until 2026 Eurobank issued on both Visa and Mastercard. On 1 July 2026 it expanded a multi-year partnership with Mastercard: all its payment cards in Greece, for people and businesses, will carry Mastercard, and its cardholders get Priceless. Visa stays on cards not yet reissued and on half of the Cyprus and Bulgarian ranges, and acquiring now belongs to Worldline. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own as reported in the press (H1 2026, 30–31 July 2026). Eurobank's websites refused automated reads; the July 2026 release was seen through coverage, and whether it reaches Cyprus and Bulgaria is not stated.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Greek cards", "Visa and Mastercard to Mastercard", "All cards, July 2026 ⚠ timetable"],
        ["Business cards", "Mastercard", "Covered by the July 2026 deal"],
        ["Rewards", "Priceless", "First Greek bank, July 2026"],
        ["Cyprus", "Visa and Mastercard", "New range, May 2026"],
        ["Bulgaria", "Visa and Mastercard", "Postbank credit cards"],
        ["Acceptance", "Worldline", "100% Worldline since May 2026"],
        ["Pay later", "Inbank JV", "Launch Q1 2027"],
        ["Remittances", "UPI to India", "Cyprus to follow"],
    ],
    "sides": {
        "neo": {"dir": "Every new Eurobank card in Greece, business cards, Priceless, World Elite in Cyprus and Mastercard credit cards at Postbank.",
                "deals": "What it does not do: acceptance, IRIS, UPI remittances, the Inbank pay-later JV, €pistrofi or AI."},
        "snb": {"dir": "Visa on legacy Greek cards and half the Cyprus and Bulgarian ranges, Worldline for acceptance, IRIS and UPI, Inbank, and Eurobank's own rewards and AI.",
                "deals": "Where they meet: Smart POS, launched with Visa, takes both networks; wallets tokenise both."},
    },
    "tl": [
        ["Oct 2021", "Google Pay for Visa and Mastercard cards"],
        ["Nov 2021", "Smart POS with IBA Group and Visa"],
        ["Dec 2021", "80% of acquiring to Worldline"],
        ["Jun 2025", "100% of Hellenic Bank"],
        ["Dec 2025", "Eurobank S.A. becomes the listed parent"],
        ["Jan 2026", "Bulgaria joins the euro"],
        ["May 2026", "Worldline buys the last 20%; Cyprus card range"],
        ["Jul 2026", "All cards to Mastercard; Priceless"],
        ["Jul 2026", "Inbank pay-later JV"],
        ["Q1 2027", "Inbank JV launch targeted"],
    ],
    "l": {
        "U": {"d": 1, "s": "Greek cardholders are moving to Mastercard; Cyprus and Bulgaria are split.",
              "gap": "New Greek cards carry Mastercard; legacy Visa cards and half the Cyprus and Bulgarian ranges stay on Visa for now.",
              "neo": "Greek cardholders after reissue, World Elite and Postbank Mastercard holders.", "snb": "Legacy Visa holders, Cypriot youth and prepaid, Postbank Visa holders."},
        "L5": {"d": 0, "s": "The front doors are Eurobank's.", "gap": "App, branches and partners are the group's or Worldline's.", "neo": "None.", "snb": "App, branches, Worldline, intermediaries."},
        "L4": {"d": 1, "s": "Business lines carry cards moving to Mastercard.", "gap": "Business banking and the Cyprus and Bulgarian banks issue cards; mortgages, wealth and insurance have no network role.",
               "neo": "Business cards; part of Cyprus and Bulgaria.", "snb": "Mortgages, wealth, Eurolife, Visa in Cyprus and Bulgaria."},
        "L3": {"d": 1, "s": "Priceless is Mastercard's; the rest is Eurobank's.", "gap": "Priceless arrived in July 2026; €pistrofi, EVA, card controls and onboarding are Eurobank's own, and no fraud partner is public.",
               "neo": "Priceless.", "snb": "€pistrofi, EVA, card controls, onboarding."},
        "L2": {"d": 1, "s": "Cards going Mastercard; acceptance, IRIS and UPI are not.", "gap": "Mastercard takes Greek issuing; Visa keeps legacy and part of Cyprus and Bulgaria; Worldline, IRIS, UPI and Inbank sit outside.",
               "neo": "Greek cards, business cards, World Elite, Postbank Mastercard.", "snb": "Visa legacy, Worldline, IRIS, UPI, Inbank."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, Fairfax, heritage, Banking Forward."},
    },
    "t": area_lens(LAYERS),
}
