"""Kaspi.kz's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from kaspi_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Kazakhstan's payments, marketplace and fintech super-app as five discs that stack into one, from $8 billion of "
       "revenue and a systemically important bank at the bottom to the Kaspi.kz and Kaspi Pay apps at the top. Click the "
       "stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the "
       "layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("cons", "Consumers", "user-round"),
    ("merch", "Merchants & micro-businesses", "store"),
    ("seller", "Marketplace sellers", "briefcase"),
    ("borrow", "Borrowers & savers", "hand-coins"),
    ("trav", "Travellers & senders abroad", "plane"),
    ("tr", "Shoppers in Türkiye", "globe"),
]
USERS_DESC = ("Six kinds of user, about 26.6 million active consumers in all: everyday consumers on the Kaspi.kz Super App, "
              "764,000 merchants on Kaspi Pay, sellers on the marketplace, borrowers and savers, people who travel or send "
              "money abroad, and Hepsiburada's shoppers in Türkiye.")

WHO = {"cons": "A Kaspi customer", "merch": "A merchant", "seller": "A marketplace seller", "borrow": "A borrower",
       "trav": "A traveller", "tr": "A shopper in Türkiye"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "cons", "name": "Pay every day",
     "why": "The everyday loop: a Kaspi Gold account, Kaspi QR or a palm in shops, free bills and transfers, all on Kaspi's own rails.",
     "steps": [("5.1", "app", "Open the Kaspi.kz app"), ("2.1", "gold", "Open Kaspi Gold"), ("2.2", "kaspiqr", "Pay by Kaspi QR"),
               ("2.2", "alaqan", "Or pay with a palm"), ("2.6", "bills", "Pay bills free"), ("3.3", "bonus", "Collect Kaspi Bonus")]},
    {"id": "shop", "who": "cons", "name": "Shop online and pay in instalments",
     "why": "Kaspi Magazin, Kasper and BNPL, delivered to a Postomat.",
     "steps": [("3.2", "kasper", "Ask Kasper what to buy"), ("4.4", "ecom", "Buy on Kaspi Magazin"), ("4.1", "bnpl", "Pay in instalments"),
               ("3.5", "delivery", "Collect from a Postomat")]},
    {"id": "accept", "who": "merch", "name": "Take payments in a shop",
     "why": "Kaspi QR and Kaspi POS, open to every bank's customers since July 2026, and the takings settled at once.",
     "steps": [("5.2", "payapp", "Join Kaspi Pay"), ("2.2", "kaspiqr", "Take Kaspi QR"), ("2.5", "interbank", "Take other banks' apps by QR"),
               ("2.4", "pos", "Take cards on Kaspi POS"), ("3.4", "register", "Issue receipts and file tax")]},
    {"id": "grow", "who": "seller", "name": "Sell more on the marketplace",
     "why": "Listings, ads, cashback, delivery and stock finance for sellers.",
     "steps": [("3.2", "aimerchant", "Build listings with AI"), ("3.3", "ads", "Advertise"), ("3.3", "cashback", "Offer cashback"),
               ("4.2", "merchfin", "Buy stock on credit"), ("2.6", "b2b", "Pay suppliers")]},
    {"id": "borrow", "who": "borrow", "name": "Borrow and save",
     "why": "Loans decided in seconds and deposits at high rates.",
     "steps": [("3.1", "kaspiid", "Confirm with a face"), ("3.1", "risk", "Get a decision in seconds"), ("4.1", "carloan", "Finance a car"),
               ("4.3", "deposits", "Save in Kaspi Deposit")]},
    {"id": "travel", "who": "trav", "name": "Travel and send money abroad",
     "why": "Kaspi Travel, QR payments in China, and transfers to cards abroad.",
     "steps": [("4.4", "travel", "Book with Kaspi Travel"), ("2.5", "alipay", "Pay by QR in China"), ("2.5", "intl", "Send money to a card abroad")]},
    {"id": "turkey", "who": "tr", "name": "Shop and borrow in Türkiye",
     "why": "Hepsiburada, its wallet, and the new Hepsi Bank.",
     "steps": [("4.5", "hepsiburada", "Shop on Hepsiburada"), ("4.5", "hepsipay", "Pay with Hepsipay"), ("4.5", "hepsibank", "Take a Hepsicredit shopping loan")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "At the edges: other banks' Mastercard cards on Kaspi POS and Kaspi Magazin, and transfers to Mastercard cards abroad.",
     "steps": [("2.4", "pos", "Mastercard accepted on Kaspi POS"), ("2.4", "magazincards", "Mastercard on Kaspi Magazin"),
               ("2.5", "intl", "Transfers to Mastercard cards abroad")]},
    {"id": "mcnext", "who": "mc", "name": "Where Hepsi Bank, transfers and Kasper could land",
     "why": "Where Kaspi has needs and Mastercard is not yet in: cards for Hepsi Bank, cross-border transfers, merchant risk on an open QR network, agentic payments for Kasper, and B2B cards.",
     "steps": [("4.5", "hepsibank", "Cards for Hepsi Bank"), ("2.5", "intl", "Mastercard Move for transfers"),
               ("2.4", "pos", "Acquirer risk and merchant data"), ("3.2", "kasper", "Agent Pay and tokens for Kasper"),
               ("2.6", "b2b", "Virtual cards for B2B")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Kaspi.kz's map",
    "title": "A closed loop with a Visa card, and Mastercard only at the edges",
    "lead": "Most of Kaspi's KZT44 trillion of payments runs on its own network: Kaspi QR, palm payments, P2P and B2B. Its Kaspi Gold card is a Visa card. Mastercard appears only where Kaspi touches other banks: it accepts their Mastercard cards and sends money to Mastercard cards abroad. No joint programme is public. The openings are in Türkiye, where Hepsi Bank has no cards yet, in cross-border transfers, and in Kaspi's AI shopping assistant. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Kaspi.kz's own (Q2 2026 results, 10 August 2026; Form 20-F for 2025) or from the National Bank of Kazakhstan and Kazakh press. Kaspi does not publish volumes by network; Kaspi Red's network is inferred.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Kaspi Gold", "Visa", "Debit card; Visa top-ups"],
        ["Kaspi QR", "Own network", "69% of TPV with cards"],
        ["Kaspi Red", "Local system ⚠", "Shopping-club instalments"],
        ["Acceptance", "Every network", "Other banks' cards 1.3–1.35%"],
        ["Transfers abroad", "Visa, Mastercard, UnionPay", "Rails not public ⚠"],
        ["China", "Alipay+", "Since April 2024"],
        ["Türkiye", "Hepsi Bank", "No cards yet"],
        ["Country", "Visa 49%, Mastercard 17%", "Cards, Sep 2026"],
    ],
    "sides": {
        "neo": {"dir": "Acceptance of other banks' Mastercard cards on Kaspi POS and Kaspi Magazin, transfers to Mastercard cards abroad, and a national Digital Country Partnership with the government.",
                "deals": "What it does not do: issue any Kaspi card, carry Kaspi QR, or run fraud, AI, loyalty or B2B services in public."},
        "snb": {"dir": "Kaspi's own QR, palm, P2P and B2B network; Visa on Kaspi Gold and its top-ups; Alipay+ and UnionPay for China; the National Bank's interbank QR.",
                "deals": "Where they meet: card acceptance, transfers abroad, and Hepsi Bank's first cards."},
    },
    "tl": [
        ["2019", "Kaspi QR network launched ⚠"],
        ["Sep 2023", "Mastercard Digital Country Partnership with Kazakhstan"],
        ["Jan 2024", "Nasdaq listing"],
        ["Apr 2024", "Alipay+ for Kaspi QR in China"],
        ["Jan 2025", "Hepsiburada control"],
        ["Sep 2025", "Other banks' Visa and Mastercard on Kaspi Magazin"],
        ["Nov 2025", "National unified QR live"],
        ["Dec 2025", "Kaspi Alaqan pay-by-palm"],
        ["Jan 2026", "Kaspi confirms Kaspi Gold is Visa"],
        ["Jul 2026", "Kasper; Hepsi Bank; Kaspi joins interbank QR"],
    ],
    "l": {
        "U": {"d": 0, "s": "Kaspi's customers pay with Kaspi Gold (Visa) or Kaspi QR.",
              "gap": "Consumers carry a Visa card or no card at all; merchants accept Mastercard from other banks; Turkish shoppers have no Hepsi Bank card yet.",
              "neo": "Merchants accepting other banks' Mastercard cards.", "snb": "Kaspi Gold holders, QR and palm users, borrowers."},
        "L5": {"d": 0, "s": "The front doors are Kaspi's.", "gap": "Two apps, kiosks, ATMs and Kartomats, all Kaspi's own.",
               "neo": "None.", "snb": "Super-apps, kiosks, partners."},
        "L4": {"d": 0, "s": "Lending, deposits and commerce run without a card scheme.", "gap": "BNPL and loans replace credit cards; Hepsi Bank has not chosen a network.",
               "neo": "None.", "snb": "BNPL, deposits, marketplace, Hepsiburada."},
        "L3": {"d": 0, "s": "The engine room is Kaspi's own.", "gap": "Biometrics, credit models, Kasper, bonuses and delivery are built in-house.",
               "neo": "None.", "snb": "Kaspi ID, credit models, Kasper, Kaspi Bonus."},
        "L2": {"d": 1, "s": "Mastercard only through acceptance and transfers.", "gap": "Kaspi QR and Visa carry the volume; Mastercard is accepted and sent to.",
               "neo": "Acceptance on POS and Kaspi Magazin; transfers abroad.", "snb": "Kaspi QR, Alaqan, Kaspi Gold on Visa, Alipay+, interbank QR."},
        "L1": {"d": 0, "s": "Kaspi's own scale, licences and owners.", "gap": "Nothing in the foundation is Mastercard's.",
               "neo": "None.", "snb": "Kaspi Bank, owners, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
