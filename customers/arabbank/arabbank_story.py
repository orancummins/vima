"""Arab Bank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from arabbank_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Jordan's largest bank as five discs that stack into one platform, from USD 80 billion of assets and a network "
       "of more than 600 branches at the bottom to Arabi Mobile, Reflect and the branches at the top. Click the stack to "
       "open it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("youth", "Young & digital customers", "smartphone"),
    ("expat", "Expatriates & travellers", "plane"),
    ("aff", "Affluent & private clients", "gem"),
    ("sme", "Small businesses & merchants", "store"),
    ("corp", "Corporates & institutions", "factory"),
]
USERS_DESC = ("Six kinds of customer across 28 countries: everyday customers, young people on Reflect and Shabab, "
              "expatriates moving money home, affluent and private clients, small businesses and merchants, and the "
              "corporates and institutions the network was built for.")

WHO = {"con": "An Arab Bank customer", "youth": "A Reflect user", "expat": "An expatriate", "aff": "A private client",
       "sme": "A merchant", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "A programme account, a Visa debit card, Arabi Mobile, CliQ transfers and Arabi Points.",
     "steps": [("4.1", "programmes", "Join a banking programme"), ("2.1", "debit", "Pay with Visa debit"), ("5.1", "arabimobile", "Run it in Arabi Mobile"),
               ("2.5", "cliq", "Send money by CliQ"), ("3.4", "points", "Earn Arabi Points")]},
    {"id": "digital", "who": "youth", "name": "Bank on the phone",
     "why": "Reflect: open with Sanad, pay with Visa cards, ask ReVA, buy later and trade crypto.",
     "steps": [("5.2", "reflect", "Open Reflect"), ("3.1", "sanad", "Verify with Sanad"), ("3.2", "reva", "Ask ReVA"),
               ("4.2", "instalments", "Split a purchase"), ("2.6", "crypto", "Trade crypto")]},
    {"id": "card", "who": "con", "name": "Borrow on a card",
     "why": "A mostly Visa credit range, two Mastercard cards, Amex and instalments.",
     "steps": [("2.2", "visacredit", "Take a Visa credit card"), ("2.2", "cobrand", "Or a football or airline co-brand"),
               ("2.3", "wallets", "Add it to a phone wallet"), ("4.2", "instalments", "Pay in instalments")]},
    {"id": "home", "who": "expat", "name": "Send money home and travel",
     "why": "The Cross Border account, RemitEx on Mastercard, Visa Direct and the Travel Mate card.",
     "steps": [("4.1", "crossborder", "Open a Cross Border account"), ("2.6", "remitex", "Remit with RemitEx"),
               ("2.6", "visadirect", "Or push to a Visa card"), ("2.2", "visacredit", "Spend abroad with Travel Mate")]},
    {"id": "house", "who": "con", "name": "Buy a home or go solar",
     "why": "Housing, EV and solar loans through the branches and the app.",
     "steps": [("5.4", "branches", "Visit a branch"), ("4.2", "housing", "Take a housing or solar loan"), ("5.1", "arabimobile", "Repay in the app")]},
    {"id": "wealth", "who": "aff", "name": "Grow wealth",
     "why": "Private Banking in Amman, a top-tier card and Arab Bank Switzerland.",
     "steps": [("4.3", "privatebank", "Join Private Banking"), ("2.2", "mccredit", "Carry World Elite Mastercard"),
               ("2.2", "amex", "Or Amex Platinum"), ("4.3", "swiss", "Book assets in Switzerland")]},
    {"id": "sme", "who": "sme", "name": "Run a shop",
     "why": "SME banking with loans repaid from card sales, acceptance for every network, online checkout and digital collections.",
     "steps": [("4.4", "sme", "Open SME banking"), ("2.4", "acquiring", "Take cards and CliQ at the till"),
               ("2.4", "ecom", "Sell online"), ("5.3", "cdg", "Collect payments digitally")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "The Corporate Digital Gateway, the Visa corporate card, 24/7 USD and Kinexys.",
     "steps": [("4.5", "cib", "Bank with CIB"), ("5.3", "cdg", "Run payments in the Gateway"),
               ("4.5", "corpcard", "Pay suppliers by Visa corporate card"), ("2.6", "usd247", "Clear USD around the clock")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "RemitEx, World Elite and UEFA Platinum, the regional card ranges, acceptance and campaigns.",
     "steps": [("2.6", "remitex", "RemitEx on Mastercard Cross-Border Services"), ("2.2", "mccredit", "World Elite and UEFA Platinum"),
               ("2.2", "regionalcards", "Mastercard ranges in the UAE, Egypt and Palestine"), ("2.4", "acquiring", "Mastercard accepted at the till"),
               ("3.4", "campaigns", "UEFA and Cannes campaigns")]},
    {"id": "mcnext", "who": "mc", "name": "Where remittances, BaaS and digital assets could land",
     "why": "Where Arab Bank has needs and Mastercard is not yet in: more corridors and push payments, issuing for Omnify's Cards as a Service, fraud tools for instant payments, commercial cards and crypto links.",
     "steps": [("2.6", "remitex", "More RemitEx corridors and push payments"), ("3.3", "omnify", "Cards as a Service on Mastercard"),
               ("3.1", "fraud", "Scam and identity scores for CliQ"), ("4.5", "corpcard", "Virtual and commercial cards"),
               ("2.6", "crypto", "Crypto-linked cards for Reflect")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Arab Bank's map",
    "title": "Visa's bank in Jordan, with Mastercard on remittances and the top tier",
    "lead": "Visa carries every Arab Bank debit card, Reflect, the corporate card, every co-brand and 12 of the 15 cards in Jordan, and launched Visa Direct and Click to Pay there first. Mastercard has the World Elite and UEFA Platinum cards, wider ranges in the UAE, Egypt and Palestine, and RemitEx, remittances to 28 countries on Mastercard Cross-Border Services since January 2024. Amex began issuing in 2025, and CliQ doubled in a year. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (H1 2026 results, 1 August 2026; 2025 Annual Report) or from Arab Bank's card pages, Mastercard's newsroom and JoPACC. No network agreement or card volumes by network are public; Reflect user numbers and big-three ratings were not found.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa", "All accounts and Reflect"],
        ["Credit (Jordan)", "Mostly Visa", "12 Visa, 2 Mastercard, 1 Amex"],
        ["Top tier", "World Elite Mastercard", "Beside Visa Infinite Privilege"],
        ["Remittances", "RemitEx", "Mastercard Cross-Border Services, 2024"],
        ["Push payments", "Visa Direct", "First in Jordan, 2023"],
        ["Checkout", "Click to Pay", "With Visa, September 2025"],
        ["Instant", "CliQ", "168 million payments in Jordan, 2025"],
        ["Corporate card", "Visa", "Payables automation, 2021"],
    ],
    "sides": {
        "neo": {"dir": "RemitEx, the World Elite and UEFA Platinum cards, Mastercard ranges in the UAE, Egypt and Palestine, acceptance at Arab Bank's terminals, and football and Cannes campaigns.",
                "deals": "What it does not do: debit, Reflect, co-brands, Click to Pay, the corporate card or instant payments."},
        "snb": {"dir": "Visa debit, credit, co-brands, Visa Direct, Click to Pay and CyberSource; Amex and JCB; CliQ and JoMoPay; Citi, J.P. Morgan and Fuze for USD, blockchain and crypto.",
                "deals": "Where they meet: the premium credit shelf and cross-border transfers."},
    },
    "tl": [
        ["Jan 2019", "Mastercard UEFA final campaign"],
        ["Dec 2021", "Visa corporate digital card"],
        ["Jun 2023", "Visa Direct; World Elite Cannes campaign"],
        ["Jan 2024", "RemitEx on Mastercard Cross-Border Services"],
        ["2025", "Amex issuing; Jaywan and Himyan"],
        ["Jun 2025", "Mastercard UEFA 2025 campaign"],
        ["Sep 2025", "Click to Pay with Visa"],
        ["May 2026", "LALIGA Visa card"],
        ["Oct 2026", "Reflect crypto; Citi 24/7 USD"],
    ],
    "l": {
        "U": {"d": 1, "s": "Top-tier and UEFA cardholders and RemitEx senders use Mastercard.",
              "gap": "Debit, Reflect and most credit holders carry Visa; private clients, football fans and expatriates sending money meet Mastercard.",
              "neo": "World Elite and UEFA cardholders, RemitEx senders, cardholders in the UAE, Egypt and Palestine.", "snb": "Debit holders, Reflect users, co-brand holders, corporates."},
        "L5": {"d": 0, "s": "The front doors are Arab Bank's.", "gap": "Arabi Mobile, Reflect, the Corporate Digital Gateway and branches are the bank's own; Reflect issues Visa.",
               "neo": "None.", "snb": "Apps, gateway, branches, partners."},
        "L4": {"d": 0, "s": "The business lines carry Visa cards.", "gap": "Programmes come with Visa debit, private banking with Visa Infinite and the corporate card is Visa; loans have no network role.",
               "neo": "None.", "snb": "Programmes, lending, private banking, SME, corporate."},
        "L3": {"d": 1, "s": "Campaigns run with both networks; the rest is the bank's own.", "gap": "Identity, fraud, AI, Omnify and Arabi Points are in-house; Mastercard appears in UEFA and Cannes promotions.",
               "neo": "Campaigns.", "snb": "Sanad, fraud models, Arabi GPT, ReVA, Omnify, Arabi Points."},
        "L2": {"d": 1, "s": "RemitEx and two card lines on Mastercard; Visa elsewhere.", "gap": "Visa has debit, most credit, Click to Pay and Visa Direct; Mastercard has RemitEx, the top tier and acceptance.",
               "neo": "RemitEx, World Elite, UEFA Platinum, regional ranges, acceptance.", "snb": "Visa cards, Amex, CliQ, Citi, Kinexys, Fuze."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, owners, network, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
