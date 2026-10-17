"""ANZ Group's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from anz_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("ANZ Group as five discs that stack into one platform, from A$1.3 trillion of assets and the ANZ 2030 reset at "
       "the bottom to ANZ Plus, branches, brokers and Transactive at the top. Click the stack to open it. Choose who "
       "you are and what you want to do, and the areas that deliver it light up across the layers, joined in the order "
       "they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("home", "Homebuyers", "house"),
    ("sme", "Businesses & merchants", "briefcase"),
    ("corp", "Corporates & institutions", "factory"),
    ("kiwi", "ANZ NZ customers", "earth"),
    ("sun", "Suncorp Bank customers", "refresh-cw"),
]
USERS_DESC = ("Six kinds of customer, more than 11 million in all: 6.5 million everyday customers in Australia, homebuyers, "
              "580,000 businesses and the merchants on ANZ Worldline, corporates and institutions in 29 markets, 2.7 million "
              "ANZ New Zealand customers and Suncorp Bank's 1.26 million on their way to ANZ.")

WHO = {"con": "An ANZ customer", "home": "A homebuyer", "sme": "A business owner", "corp": "A corporate treasurer",
       "kiwi": "An ANZ NZ customer", "sun": "A Suncorp Bank customer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a Visa debit card in a wallet, ANZ Plus and Falcon watching for fraud.",
     "steps": [("4.1", "accounts", "Open an everyday account"), ("2.1", "plusdebit", "Pay with ANZ Plus Visa Debit"), ("2.1", "wallets", "Tap with a phone"),
               ("5.1", "plusapp", "Run it in ANZ Plus"), ("3.1", "falcon", "Protected by Falcon")]},
    {"id": "card", "who": "con", "name": "Borrow and earn on a card",
     "why": "A Visa credit card, Qantas or ANZ Reward Points and Everyday Rewards, with caps arriving in October 2026.",
     "steps": [("2.2", "credit", "Take an ANZ Visa credit card"), ("3.3", "rewards", "Earn points"), ("2.2", "cardchanges", "Live with the new caps")]},
    {"id": "send", "who": "con", "name": "Pay and send money safely",
     "why": "PayID and PayTo at home, International Money Transfers abroad, with name checks and scam controls.",
     "steps": [("2.6", "npp", "Pay by PayID"), ("2.6", "cop", "Check the payee's name"), ("2.7", "imt", "Send money overseas"), ("3.1", "scams", "Get help from First Responders")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "A$348 billion of home loans, mostly through brokers.",
     "steps": [("5.3", "brokers", "Apply through a broker"), ("4.1", "homeloans", "Take an ANZ home loan"), ("5.2", "branches", "See a lender in a branch")]},
    {"id": "sme", "who": "sme", "name": "Run a business and take payments",
     "why": "A business account, Visa business cards, ANZ Worldline terminals and a banker with an AI CRM.",
     "steps": [("4.2", "bpb", "Bank with Business & Private Bank"), ("2.5", "worldline", "Take cards with ANZ Worldline"),
               ("2.3", "bizcards", "Spend on a business card"), ("3.2", "agentforce", "Get a better-prepared banker"), ("3.1", "security", "Guard against invoice scams")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "Transactive Global, institutional banking and tokenised deposits on Swift's ledger.",
     "steps": [("5.4", "transactive", "Manage cash in Transactive"), ("4.3", "institutional", "Bank with Institutional"), ("2.7", "tokenised", "Settle with tokenised deposits")]},
    {"id": "kiwi", "who": "kiwi", "name": "Bank with ANZ in New Zealand",
     "why": "New Zealand's largest bank: Visa cards, goMoney and ANZ Loop cashback.",
     "steps": [("4.4", "anznz", "Bank with ANZ NZ"), ("5.1", "gomoney", "Use goMoney"), ("3.3", "loop", "Earn cashback with ANZ Loop")]},
    {"id": "suncorp", "who": "sun", "name": "Move from Suncorp Bank to ANZ",
     "why": "Suncorp Bank customers keep their Visa debit card until they move to ANZ's systems by June 2027.",
     "steps": [("4.5", "suncorpbank", "Bank with Suncorp Bank"), ("2.4", "sundebit", "Pay with Suncorp Visa Debit"), ("5.1", "plusapp", "Move onto ANZ's app")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Only in acceptance: ANZ Worldline takes Mastercard cards at Australian merchants, and the RBA's rules now apply equally to Mastercard, Visa and eftpos.",
     "steps": [("2.5", "worldline", "Mastercard acquired by ANZ Worldline"), ("2.2", "cardchanges", "The RBA's caps, the same for Mastercard and Visa")]},
    {"id": "mcnext", "who": "mc", "name": "Where Mastercard could land at ANZ",
     "why": "Where ANZ has needs and Mastercard is not yet in: acquirer services for the newly owned ANZ Worldline, scam and identity scoring, cross-border transfers, commercial cards and card-linked offers.",
     "steps": [("2.5", "worldline", "Acquirer risk and data for ANZ Worldline"), ("3.1", "security", "Identity and mule-account scoring"),
               ("2.6", "cop", "Scam scores on NPP payments"), ("2.7", "imt", "Mastercard Move for remittances"),
               ("2.3", "commercial", "Commercial cards at the 0.8% cap"), ("3.3", "rewards", "Merchant-funded offers")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across ANZ Group's map",
    "title": "A Visa group where Mastercard is only accepted",
    "lead": "Every ANZ, ANZ Plus, ANZ New Zealand and Suncorp Bank card found is Visa. Debit has been Visa-exclusive since 2010, ANZ NZ dropped Mastercard credit cards in 2019, and in April 2026 ANZ NZ launched card-linked cashback on Visa Offers Exchange. Mastercard reaches ANZ through ANZ Worldline, the acquirer ANZ took full control of in July 2026, just as the RBA banned surcharges and cut credit interchange to 0.3%. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (1H26 results, 1 May 2026; 3Q26 update, 12 August 2026) or from ANZ, Suncorp Bank and ANZ NZ product pages, Worldline, the RBA and AP+. No ANZ–Mastercard initiative was found for 2020–2026; ANZ's business and corporate card networks in Australia are not confirmed on ANZ's own pages.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Consumer debit", "Visa (+ eftpos ⚠)", "Visa-exclusive since 2010"],
        ["Consumer credit", "Visa", "Seven cards; points capped from 28 Oct 2026"],
        ["Business cards", "Visa ⚠", "Corporate network unconfirmed"],
        ["Suncorp Bank", "Visa debit", "Credit cards left for NAB, Nov 2025"],
        ["ANZ New Zealand", "Visa", "Mastercard dropped April 2019"],
        ["Acquiring", "ANZ Worldline", "All networks; 100% ANZ from Jul 2026"],
        ["Card-linked offers", "Visa Offers Exchange", "ANZ Loop, NZ, Apr 2026"],
        ["Regulation", "RBA", "Surcharge ban and 0.3% credit cap, 1 Oct 2026"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard cards taken by ANZ Worldline's merchants, and the same RBA rules as Visa and eftpos.",
                "deals": "What it does not do: issue a single ANZ card, run ANZ's offers, fraud tools or cross-border transfers."},
        "snb": {"dir": "Visa on every card in Australia and New Zealand and in ANZ Loop, eftpos on dual-network debit, AP+'s NPP and PayTo, Swift's ledger for tokenised deposits, and ANZ's own Falcon.",
                "deals": "Where they meet: ANZ Worldline's terminals, which take every network."},
    },
    "tl": [
        ["Feb 2010", "Visa Debit exclusive deal across Asia-Pacific"],
        ["Apr 2019", "ANZ NZ stops issuing Mastercard credit cards"],
        ["Dec 2020", "ANZ Worldline joint venture agreed"],
        ["Jul 2024", "Suncorp Bank bought"],
        ["Oct 2025", "ANZ 2030 strategy"],
        ["Nov 2025", "Suncorp credit cards move to NAB"],
        ["Mar 2026", "RBA: surcharge ban and 0.3% credit cap"],
        ["Apr 2026", "ANZ Loop on Visa Offers Exchange"],
        ["Jul 2026", "ANZ Worldline fully ANZ's"],
        ["Sep 2026", "Tokenised deposits on Swift's ledger"],
        ["1 Oct 2026", "Surcharging ends; new interchange caps"],
        ["Jun 2027", "Suncorp Bank customers on ANZ"],
    ],
    "l": {
        "U": {"d": 0, "s": "ANZ's customers carry Visa.", "gap": "No ANZ, ANZ Plus, ANZ NZ or Suncorp Bank customer was found holding a Mastercard from the group.",
              "neo": "Merchants on ANZ Worldline accept Mastercard.", "snb": "Cardholders in Australia and New Zealand, Suncorp Bank customers."},
        "L5": {"d": 0, "s": "The front doors are ANZ's.", "gap": "ANZ Plus, goMoney, branches, brokers and Transactive are the group's own.", "neo": "None.", "snb": "ANZ Plus, apps, branches, brokers, Transactive."},
        "L4": {"d": 0, "s": "The business lines carry Visa cards.", "gap": "Accounts come with Visa debit; home loans, Institutional and Suncorp Bank have no network role.",
               "neo": "None.", "snb": "Accounts, home loans, business banking, Institutional, ANZ NZ, Suncorp Bank."},
        "L3": {"d": 0, "s": "Fraud, AI and offers are ANZ's or Visa's.", "gap": "Falcon and scam controls are ANZ's own; ANZ Loop runs on Visa Offers Exchange.",
               "neo": "None.", "snb": "Falcon, scam teams, Agentforce, rewards, ANZ Loop."},
        "L2": {"d": 1, "s": "Mastercard only through acquiring.", "gap": "Visa issues every card; ANZ Worldline acquires Mastercard among all networks; A2A runs on AP+.",
               "neo": "ANZ Worldline acceptance.", "snb": "Visa cards, eftpos, NPP and PayTo, Swift ledger."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, brands, technology, ANZ 2030."},
    },
    "t": area_lens(LAYERS),
}
