"""HSBC Holdings' kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from hsbc_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("A bank built on Hong Kong and London as five discs that stack into one platform, from $3.4 trillion of assets "
       "at the bottom to the UK and Hong Kong apps, HSBCnio and the branches at the top. Click the stack to open it. "
       "Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined "
       "in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("premier", "Premier & private clients", "gem"),
    ("intl", "People living across borders", "plane"),
    ("sme", "Businesses", "briefcase"),
    ("corp", "Corporates & institutions", "factory"),
]
USERS_DESC = ("Five kinds of customer, about 41 million in all: everyday customers in the UK and Hong Kong, Premier and "
              "private clients, people moving money across borders, businesses, and the corporates and institutions CIB serves.")

WHO = {"con": "An HSBC customer", "premier": "A Premier client", "intl": "Someone living across borders",
       "sme": "A business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day in the UK",
     "why": "The everyday loop at HSBC UK: an account, a Visa debit card ⚠, a Mastercard credit card, the app and fraud checks.",
     "steps": [("4.2", "ukretail", "Open an HSBC UK account"), ("2.1", "ukdebit", "Pay with a debit card"), ("2.1", "ukcredit", "Add a credit card"),
               ("5.1", "ukapp", "Run it in the app"), ("3.1", "fincrime", "Protected by AI monitoring")]},
    {"id": "hongkong", "who": "con", "name": "Bank and pay in Hong Kong",
     "why": "HSBC and Hang Seng, Mastercard debit, PayMe and the RedCoin stablecoin due this year.",
     "steps": [("4.1", "hkbank", "Bank with HSBC or Hang Seng"), ("2.3", "hkdebit", "Pay with a Mastercard debit card"),
               ("2.8", "payme", "Pay friends and shops with PayMe"), ("2.8", "redcoin", "Hold and spend RedCoin"), ("5.1", "hkapp", "Run it in the HK app")]},
    {"id": "spread", "who": "con", "name": "Spread the cost",
     "why": "A Mastercard credit card, Flexipay instalments and rewards.",
     "steps": [("2.1", "ukcredit", "Take a credit card"), ("4.2", "flexipay", "Split a purchase with Flexipay"), ("3.3", "ukrewards", "Spend points with Pay with Rewards")]},
    {"id": "premier", "who": "premier", "name": "Bank as a Premier client",
     "why": "Premier and Privé cards on Mastercard, wealth across borders and Wealth Centres.",
     "steps": [("4.4", "iwpb", "Become a Premier client"), ("2.1", "ukcredit", "Carry Premier World Elite"), ("2.3", "hkmc", "Carry Privé World Legend in Hong Kong"),
               ("3.3", "hkrewards", "Get Priceless access"), ("5.3", "branches", "Meet in a Wealth Centre")]},
    {"id": "abroad", "who": "intl", "name": "Spend and send abroad",
     "why": "Global Money, on Visa, took over from Zing.",
     "steps": [("2.2", "globalmoney", "Hold 18 currencies"), ("2.2", "zing", "Move over from Zing"), ("5.1", "ukapp", "Send from the app")]},
    {"id": "sme", "who": "sme", "name": "Run a business",
     "why": "Business banking, multi-currency business debit on Mastercard, and Sage for tax.",
     "steps": [("4.2", "ukcomm", "Bank with UK Commercial or Innovation Bank"), ("2.4", "hsbizdebit", "Pay with a multi-currency business debit card"),
               ("2.6", "trackc2a", "Pay suppliers' accounts by card"), ("5.3", "partners", "File tax through Sage")]},
    {"id": "corp", "who": "corp", "name": "Run treasury across markets",
     "why": "Global Payments Solutions, virtual cards, tokenised deposits and HSBCnio.",
     "steps": [("4.3", "cib", "Bank with CIB"), ("2.7", "gps", "Move cash in 130 currencies"), ("2.6", "hkvirtual", "Pay with virtual cards"),
               ("2.8", "tds", "Settle with tokenised deposits"), ("5.2", "hsbcnio", "Connect your own AI through HSBCnio")]},
    {"id": "collect", "who": "corp", "name": "Collect from customers",
     "why": "Digital Merchant Services in Asia, expanding to six more markets.",
     "steps": [("2.7", "dms", "Take payments online and by wallet"), ("2.7", "gps", "Receive the funds"), ("5.2", "hsbcnet", "Reconcile on HSBCnet")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "UK credit, Hong Kong debit and premium credit, Hang Seng, and virtual and commercial cards in the UK, Hong Kong and the Gulf.",
     "steps": [("2.1", "ukcredit", "UK credit on Mastercard"), ("2.3", "hkmc", "Premium Hong Kong credit"), ("2.3", "hkdebit", "Hong Kong debit"),
               ("2.4", "mmpower", "Hang Seng MMPOWER"), ("2.6", "hkvirtual", "Virtual cards on In Control"), ("3.3", "ukrewards", "Pay with Rewards and Priceless")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, virtual cards and stablecoins could land",
     "why": "Where HSBC has needs and Mastercard is not yet in: agentic payments on the UK credit book, scam tools, virtual cards across GPS markets, merchant services in six new markets, and on and off ramps for RedCoin.",
     "steps": [("3.2", "agentic", "Agent Pay against Visa's trial"), ("3.1", "fincrime", "Scam and fraud scores"), ("2.7", "gps", "Virtual cards across GPS markets"),
               ("2.7", "dms", "Gateway, tokens and Click to Pay"), ("2.8", "redcoin", "Multi-Token Network for RedCoin")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across HSBC's map",
    "title": "Mastercard on credit and corporate cards, Visa on debit and the first agent",
    "lead": "Mastercard carries HSBC UK's credit cards, Hong Kong debit and the top of the Hong Kong credit range, Hang Seng's MMPOWER, and the group's virtual and commercial cards in the UK, Hong Kong and the Gulf. Visa carries UK debit ⚠, Global Money and Gulf cards, and ran HSBC UK's first live agentic payment in July 2026; UnionPay shares Hong Kong credit. HSBC's own rails, PayMe, tokenised deposits and the RedCoin stablecoin, sit beside the cards. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (2026 interim results, 4 August 2026) or from HSBC, Mastercard, Visa and press. Several card pages do not name a scheme; the UK debit network is inferred and Mexico's split rests on secondary sources.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["UK credit", "Mastercard", "Premier World Elite, October 2024"],
        ["UK debit", "Visa ⚠", "Inferred from the product page"],
        ["Global Money", "Visa", "18 currencies"],
        ["Hong Kong", "Mastercard, Visa, UnionPay", "Mastercard debit and Privé World Legend"],
        ["Gulf", "Visa", "Exclusive debit renewal, 2013"],
        ["Commercial cards", "Mastercard", "Track, In Control, Wholesale"],
        ["Agentic", "Visa", "First live trial, July 2026"],
        ["Stablecoin", "RedCoin", "HSBC's own, due 2H 2026"],
    ],
    "sides": {
        "neo": {"dir": "UK credit and Pay with Rewards, Hong Kong debit and premium credit, Hang Seng, Mexico premium ⚠, and virtual and commercial cards in three regions.",
                "deals": "What it does not do: UK debit ⚠, Global Money, Gulf cards, the agentic trial, fraud monitoring or HSBC's own digital money."},
        "snb": {"dir": "Visa debit and Global Money, Visa's agentic trial, UnionPay in Hong Kong, Google Cloud's AI, PayMe, tokenised deposits and RedCoin.",
                "deals": "Where they meet: Hong Kong and Mexico, where networks split by card."},
    },
    "tl": [
        ["Oct 2008", "Visa debit deal for Asia-Pacific and the Middle East"],
        ["May 2010", "Mastercard renews the Premier credit card"],
        ["Jul 2013", "Visa renews exclusive Gulf debit"],
        ["Mar 2022", "Track Card-to-Account, HSBC first in the UK"],
        ["Oct 2024", "Premier World Elite Mastercard, UK"],
        ["Jun 2025", "Hong Kong virtual corporate card on In Control"],
        ["May 2026", "Privé World Legend Mastercard"],
        ["Jun 2026", "UAE mobile virtual cards"],
        ["Jul 2026", "First live agentic payment, with Visa"],
        ["Sep 2026", "HSBC RedCoin named; HSBCnio launched"],
    ],
    "l": {
        "U": {"d": 1, "s": "Credit and Hong Kong debit carry Mastercard.",
              "gap": "UK and Hong Kong credit holders and Hong Kong debit holders carry Mastercard; UK debit ⚠, Global Money and Gulf customers carry Visa.",
              "neo": "UK credit, Hong Kong debit, Premier, business card users.", "snb": "UK debit ⚠, Global Money, Gulf and Visa or UnionPay Hong Kong holders."},
        "L5": {"d": 0, "s": "The front doors are HSBC's.", "gap": "Apps, HSBCnet, HSBCnio and branches are the group's.", "neo": "None.", "snb": "Apps, portals, branches, partners."},
        "L4": {"d": 1, "s": "The business lines carry a mix of cards.", "gap": "Hong Kong and UK banking carry Mastercard alongside Visa; CIB uses Mastercard virtual cards; Flexipay is HSBC's own.",
               "neo": "Cards inside Hong Kong, UK, CIB and Premier.", "snb": "Lending, deposits, Flexipay, wealth."},
        "L3": {"d": 1, "s": "Rewards and recycling with Mastercard; agents with Visa.", "gap": "Pay with Rewards, Priceless and card recycling are Mastercard's; fraud runs on Google Cloud and the agentic trial ran on Visa.",
               "neo": "Pay with Rewards, Priceless, card recycling.", "snb": "Fraud monitoring, agentic trial, RewardCash."},
        "L2": {"d": 1, "s": "Mastercard on credit and B2B; Visa on debit; HSBC's own tokens.", "gap": "Mastercard leads UK credit, Hong Kong debit and commercial cards; Visa holds UK debit ⚠, Global Money and the Gulf; RedCoin and tokenised deposits are HSBC's.",
               "neo": "UK credit, Hong Kong cards, Hang Seng, virtual cards, Track.", "snb": "Visa debit, Global Money, UnionPay, PayMe, RedCoin, tokenised deposits."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, entities, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
