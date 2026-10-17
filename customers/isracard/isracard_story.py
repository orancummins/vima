"""Isracard's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from isracard_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Israel's largest card group as five discs that stack into one platform, from 4.8 million active cards and Delek's "
       "control at the bottom to the Isracard app, bank branches and the business site at the top. Click the stack to open "
       "it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined "
       "in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday cardholders", "user-round"),
    ("trav", "Travellers & flyers", "plane"),
    ("prem", "Premium & Amex members", "gem"),
    ("sme", "Merchants & small businesses", "store"),
    ("corp", "Employers & corporates", "factory"),
    ("partner", "Partner banks & brands", "users-round"),
]
USERS_DESC = ("Six kinds of user behind more than 4.8 million active cards: everyday cardholders, travellers and El Al flyers, "
              "premium and American Express members, the 100,000-plus businesses that take and use Isracard, employers, and "
              "the banks, clubs and owners it works with.")

WHO = {"con": "An Isracard cardholder", "trav": "A traveller", "prem": "A premium customer", "sme": "A merchant",
       "corp": "An employer", "partner": "A partner"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Pay day to day",
     "why": "The everyday loop: a TOP or BASIC Mastercard, paid by phone, with clubs and self-service.",
     "steps": [("2.1", "top", "Take a TOP or BASIC card"), ("2.7", "wallets", "Pay with Apple Pay or Google Pay"),
               ("3.3", "clubs", "Save through a club"), ("5.1", "app", "Run it in the app"), ("3.1", "fraud", "Block or dispute online")]},
    {"id": "fly", "who": "trav", "name": "Fly with El Al",
     "why": "FLY CARD, won from CAL in 2026: Mastercard premium tiers, an Amex tier, and travel insurance.",
     "steps": [("2.4", "flycard", "Join FLY CARD"), ("2.4", "flyamex", "Or the Amex Premium tier"),
               ("4.4", "insurance", "Insure the trip"), ("3.3", "benefits", "Use lounges and deals")]},
    {"id": "premium", "who": "prem", "name": "Hold a premium card",
     "why": "World Elite Mastercard, CashBack+ or the exclusive American Express range.",
     "steps": [("2.1", "cashback", "Take World Elite or CashBack+"), ("2.3", "amex", "Or an Amex Platinum or Gold"),
               ("3.3", "benefits", "Collect benefits")]},
    {"id": "shop", "who": "con", "name": "Shop with a store card",
     "why": "Co-brands with Rami Levy and Super-Pharm, and Mami on Visa.",
     "steps": [("4.5", "superfly", "Take Superfly at Rami Levy"), ("4.5", "lifestyle", "Or LifeStyle at Super-Pharm"),
               ("2.2", "visa", "Or Mami on Visa"), ("3.3", "igul", "Round up for charity")]},
    {"id": "borrow", "who": "con", "name": "Borrow",
     "why": "Non-bank loans and revolving credit from Isracard Finance.",
     "steps": [("4.1", "loans", "Take a non-bank loan"), ("4.1", "revolving", "Spread a charge"), ("3.2", "data", "Decided on Isracard's data")]},
    {"id": "sme", "who": "sme", "name": "Take payments as a business",
     "why": "Acquiring, the business payment account, business finance and cards.",
     "steps": [("5.3", "bizportal", "Sign up online"), ("2.6", "bizaccount", "Open a payment account"), ("2.6", "acquiring", "Take every card"),
               ("4.2", "bizfinance", "Discount card receipts"), ("4.2", "b2b", "Pay suppliers by card")]},
    {"id": "employer", "who": "corp", "name": "Give staff a card",
     "why": "The Corporate club card on Mastercard, Visa or American Express.",
     "steps": [("4.3", "corporate", "Offer the Corporate card"), ("4.3", "affinity", "Or a community card"), ("4.2", "b2b", "Issue purchasing cards")]},
    {"id": "partner", "who": "partner", "name": "Issue cards with Isracard",
     "why": "Banks and clubs that issue through Isracard.",
     "steps": [("2.5", "bankcards", "Issue bank cards"), ("5.2", "branches", "Sell them in branches"), ("2.4", "flycard", "Run a club card"),
               ("2.5", "digitalbank", "Launch a new bank's cards")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Most of Isracard's own and co-brand credit cards, the FLY CARD premium tiers, prepaid and a first agentic purchase.",
     "steps": [("2.1", "top", "TOP and BASIC on Mastercard"), ("2.1", "cashback", "World Elite and CashBack+"),
               ("2.4", "flycard", "FLY CARD Premium tiers"), ("4.5", "lifestyle", "LifeStyle and Superfly"), ("2.8", "agentpay", "Agent Pay ⚠")]},
    {"id": "mcnext", "who": "mc", "name": "Where FLY CARD, clubs and agents could land",
     "why": "Where Isracard has needs and Mastercard is not yet visible: moving FLY CARD cardholders, card-linked club offers, Agent Pay at scale, merchant risk and commercial cards.",
     "steps": [("2.4", "flycard", "Move FLY CARD cards with updater tools"), ("3.3", "clubs", "Card-linked offers for clubs"),
               ("2.8", "agentpay", "Agent Pay at scale"), ("2.6", "acquiring", "Merchant risk tools"), ("4.2", "b2b", "Commercial card controls")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Isracard's map",
    "title": "Mastercard's card group in Israel, with Amex in the same house",
    "lead": "Mastercard is the brand on most of Isracard's own and co-brand credit cards, from TOP and BASIC to the FLY CARD premium tiers won from CAL in 2026, a link that runs back to Eurocard in 1975. Visa carries a few cards, and American Express, licensed exclusively to Isracard, takes the premium Amex range. A first Agent Pay purchase is reported. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Card networks are read from card art on Isracard's site (17 October 2026). Ownership and deals are from Globes; 2025 and Q2 2026 results come from third-party summaries ⚠. The split of volume by network is not public.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Own-brand credit", "Mastercard", "TOP, BASIC, CashBack+, World Elite"],
        ["Co-brands", "Mastercard", "LifeStyle, Superfly, FLY CARD Premium"],
        ["FLY CARD", "Mastercard and Amex", "Ten-year deal, March 2026"],
        ["Visa", "W, Mami", "Small range"],
        ["Amex", "Exclusive licence", "Since 1995"],
        ["Prepaid", "Mastercard", "Nateanchik"],
        ["Agentic", "Agent Pay", "First purchase ⚠"],
        ["Volume split", "Not public", "About 47% card share in 2020 ⚠"],
    ],
    "sides": {
        "neo": {"dir": "Most own-brand and co-brand credit cards, FLY CARD Premium tiers, prepaid, a first Agent Pay purchase, and acceptance at Isracard's merchants.",
                "deals": "What it does not do: the Amex range, Visa cards, Bit and PayBox, loans, insurance or clubs."},
        "snb": {"dir": "American Express under exclusive licence, Visa on W and Mami, bank-run Bit and PayBox, and Isracard's own credit, clubs and service.",
                "deals": "Where they meet: FLY CARD, where Mastercard and Amex tiers sit side by side."},
    },
    "tl": [
        ["1975", "Eurocard Israel; Isracard begins ⚠"],
        ["1995", "American Express licence ⚠"],
        ["Apr 2019", "TASE listing"],
        ["May 2020", "First Digital Bank on Isracard Mastercard"],
        ["Jan 2024", "Harel bid dropped"],
        ["Jul 2025", "Delek takes control"],
        ["Mar 2026", "FLY CARD ten-year deal"],
        ["Jun 2026", "NIS 75m settlement with CAL"],
        ["Jul 2026", "Esh Bank MOU lapses"],
        ["End-2026", "CAL's FLY CARD contract ends"],
    ],
    "l": {
        "U": {"d": 2, "s": "Most cardholders carry Mastercard; Amex and Visa holders do not.",
              "gap": "Own-brand and co-brand holders carry Mastercard; Amex members and Mami and W holders do not.",
              "neo": "TOP, BASIC, World Elite, LifeStyle, Superfly and FLY CARD Premium holders.", "snb": "Amex members, Visa holders, borrowers, insurance customers."},
        "L5": {"d": 0, "s": "The front doors are Isracard's.", "gap": "App, website, branches and the business site are Isracard's or its banks'.", "neo": "None.", "snb": "App, website, bank branches, business site."},
        "L4": {"d": 1, "s": "Co-brands ride on Mastercard; loans and insurance do not.", "gap": "LifeStyle and Superfly are Mastercard; the Corporate card offers a choice; loans, insurance and savings have no network.",
               "neo": "LifeStyle, Superfly, Corporate (by choice).", "snb": "Loans, insurance, savings, Amex purchasing cards."},
        "L3": {"d": 0, "s": "Services are Isracard's own.", "gap": "Fraud handling, data, clubs and service are in-house; no Mastercard service is public.",
               "neo": "None public.", "snb": "Disputes, data, clubs, benefits, service."},
        "L2": {"d": 2, "s": "Mastercard carries most issuing; Amex and Visa the rest.", "gap": "Mastercard on most own cards, FLY CARD Premium, prepaid and Agent Pay; Amex exclusive; Visa on a few; Bit and PayBox on bank rails.",
               "neo": "Own-brand cards, FLY CARD Premium, prepaid, Agent Pay ⚠.", "snb": "Amex, Visa, Bit, PayBox."},
        "L1": {"d": 1, "s": "Mastercard is one of four licences.", "gap": "The Eurocard heritage and Mastercard licence sit beside Visa, Amex and the domestic Isracard brand.", "neo": "Mastercard licence via Europay.", "snb": "Ownership, capital, Amex and Visa licences."},
    },
    "t": area_lens(LAYERS),
}
