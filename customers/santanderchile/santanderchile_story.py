"""Banco Santander Chile's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from santanderchile_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Chile's largest bank by loans as five discs that stack into one platform, from a Ch$70 trillion balance sheet, "
       "two-thirds owned by Santander Group, at the bottom to the app, Work/Cafés and Getnet terminals at the top. Click the "
       "stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the "
       "layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("traveller", "Travellers & cardholders", "plane"),
    ("home", "Homebuyers", "house"),
    ("driver", "Car buyers", "gauge"),
    ("wealth", "Private-bank clients", "gem"),
    ("sme", "SMEs & merchants", "store"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Seven kinds of customer, about 4.8 million in all (2.7 million active): everyday customers, travellers and "
              "cardholders, homebuyers, car buyers, private-bank clients, 478,000 SMEs and merchants, and corporates.")

WHO = {"con": "A Santander Chile customer", "traveller": "A traveller", "home": "A homebuyer", "driver": "A car buyer",
       "wealth": "A private-bank client", "sme": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: open a Life account online, pay with its debit card, run it in the app, protected by changing card codes.",
     "steps": [("5.1", "app", "Open an account in the app"), ("2.2", "lifedebit", "Pay with the Life debit card"),
               ("2.3", "ecocards", "Shop online with a dynamic CVV"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "travel", "who": "traveller", "name": "Earn miles on a card",
     "why": "The LATAM Pass co-brand, renewed for five years in 2025, with miles by Santander Rewards level and a dollar account for trips.",
     "steps": [("2.1", "latampass", "Take a LATAM Pass card"), ("3.2", "rewards", "Earn miles by Rewards level"),
               ("2.5", "usd", "Spend from a dollar account")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card or loan",
     "why": "Chile's number one in consumer lending and card purchases.",
     "steps": [("2.1", "lifecredit", "Take a Life credit card"), ("4.2", "consumer", "Take a consumer loan"), ("3.3", "redec", "Checked against REDEC")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "A fifth of Chile's mortgages, sold through branches and Work/Cafés.",
     "steps": [("5.2", "branches", "Visit a Work/Café"), ("4.1", "mortgages", "Take a mortgage"), ("3.4", "brokerage", "Insure it")]},
    {"id": "drive", "who": "driver", "name": "Finance a car",
     "why": "Santander Consumer Finance, Ch$1.13 trillion of car and fleet loans.",
     "steps": [("4.6", "autofin", "Finance a car with Santander Consumer")]},
    {"id": "wealth", "who": "wealth", "name": "Invest with the private bank",
     "why": "Santander Private Bank, funds and The Platinum Card.",
     "steps": [("4.5", "wealth", "Invest with Santander Private Bank"), ("3.4", "brokerage", "Buy funds and insurance"),
               ("2.1", "amexplat", "Carry The Platinum Card")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A digital business account, Getnet terminals that sell top-ups and settle the same day, and Office Banking.",
     "steps": [("4.3", "sme", "Open a digital business account"), ("2.4", "getnet", "Take cards with Getnet"),
               ("2.4", "smartpos", "Sell top-ups and bill payments"), ("4.3", "officebanking", "Run it in Office Banking")]},
    {"id": "corp", "who": "corp", "name": "Trade and move money as a corporate",
     "why": "Corporate and investment banking, trade finance and dollars.",
     "steps": [("4.4", "cib", "Bank with CIB"), ("2.5", "trade", "Finance foreign trade"), ("4.3", "officebanking", "Pay through Office Banking")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Life debit at launch, LATAM Pass cards beside Visa and Amex, the Pulsera Chip, and acceptance through Getnet.",
     "steps": [("2.2", "lifedebit", "Life debit on Mastercard"), ("2.1", "latampass", "LATAM Pass Mastercard versions"),
               ("2.3", "pulsera", "Pulsera Chip"), ("2.4", "getnet", "Accepted through Getnet")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, tokens and Getnet could land",
     "why": "Where Santander Chile has needs and Mastercard is not yet in: AI-agent payments after Visa's pilot, tokens and Click to Pay, tools for Getnet as fees fall, rewards after Mérito Life, and open finance before July 2027.",
     "steps": [("2.6", "agentpay", "Agent Pay, as in Spain and Brazil"), ("2.3", "wallets", "Tokens and Click to Pay"),
               ("2.4", "getnet", "Merchant and fraud tools for Getnet"), ("3.2", "rewards", "Card-linked offers"),
               ("3.3", "openfinance", "Open finance for 2027")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Banco Santander Chile's map",
    "title": "One of three networks, with Visa first to the agents",
    "lead": "Santander Chile has the largest share of Chile's credit-card purchases, 24.4%, on cards branded Mastercard, Visa and American Express. No network deal for Chile is public. Mastercard carried the Life debit card at launch in 2020 and the Pulsera Chip, and shares the LATAM Pass co-brand. Getnet accepts every network. Mastercard's group is live on Agent Pay in Spain and Brazil, but in Chile Visa ran Santander's first agent purchase in March 2026. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (Q2 2026 management commentary, July 2026) or come from Santander, Mastercard, Visa and the Chilean press. The bank's card pages could not be read; networks by tier are inferred from press reports and marked ⚠.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Credit cards", "Mastercard, Visa, Amex", "24.4% of Chile's card purchases; split not public ⚠"],
        ["LATAM Pass", "Three networks", "688,000 clients; renewed Aug 2025"],
        ["Life debit", "Mastercard at launch", "August 2020; Visa mark now shown ⚠"],
        ["Platinum Card", "American Express", "Private bank, 2025"],
        ["Acquiring", "Getnet", "229,000 merchants; all networks"],
        ["AI agents", "Visa first", "Chile purchase, March 2026"],
        ["Agent Pay", "Mastercard tests", "Six banks in Chile, Sep 2026 ⚠"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard versions of LATAM Pass and other credit cards, Life debit at launch, the Pulsera Chip, and acceptance at Getnet's merchants.",
                "deals": "What it does not do: a Chile network deal, the first agent purchase, card processing, rewards, or fraud tools that are public."},
        "snb": {"dir": "Visa and American Express cards, Visa's agentic pilot, the group's Plard processor, Getnet's own services and the bank's own fraud controls and rewards.",
                "deals": "Where they meet: the LATAM Pass co-brand, issued on all three networks."},
    },
    "tl": [
        ["Jul 2020", "Getnet Chile set up; Pulsera Chip on Mastercard"],
        ["Aug 2020", "Cuenta Life with Mastercard debit"],
        ["Jan 2022", "Cards without printed numbers, dynamic CVV"],
        ["Apr 2023", "Mastercard and Klap bring Tap on Phone to Chile"],
        ["Feb 2024", "Mastercard Click to Pay arrives in Chile"],
        ["Jul 2025", "Andrés Trautmann becomes chief executive"],
        ["Aug 2025", "LATAM Pass renewed for five years"],
        ["Nov 2025", "Card range simplified; Mérito Life ends"],
        ["Mar 2026", "Visa agentic purchase in Chile"],
        ["Sep 2026", "Mastercard agent payments with six banks in Chile ⚠"],
        ["Jul 2027", "Open Finance System due"],
    ],
    "l": {
        "U": {"d": 1, "s": "Cardholders carry Mastercard, Visa or Amex.",
              "gap": "Some LATAM Pass and Life customers carry Mastercard; others carry Visa or American Express, in unknown proportions.",
              "neo": "Mastercard cardholders, Life debit holders from 2020.", "snb": "Visa and Amex cardholders, borrowers, savers and SMEs."},
        "L5": {"d": 0, "s": "The front doors are the bank's.", "gap": "App, Work/Cafés and Getnet service points are Santander's own.", "neo": "None.", "snb": "App, branches, partners."},
        "L4": {"d": 0, "s": "Cards sit inside the lending book.", "gap": "Consumer lending carries cards on three networks; mortgages, CIB, wealth and car finance have no network role.",
               "neo": "Mastercard cards inside consumer lending.", "snb": "Mortgages, SMEs, CIB, wealth, car finance."},
        "L3": {"d": 0, "s": "Services are the bank's own.", "gap": "Fraud controls, rewards and brokerage are Santander's; no Mastercard service is public.",
               "neo": "None public.", "snb": "Fraud controls, Santander Rewards, open-finance readiness, brokerage."},
        "L2": {"d": 1, "s": "Cards on three networks; Getnet takes all.", "gap": "Mastercard shares credit and debit with Visa and Amex; Visa ran the first agent purchase.",
               "neo": "Life debit, Pulsera Chip, LATAM Pass versions, Getnet acceptance.", "snb": "Visa and Amex cards, Visa agent pilot, dollar accounts."},
        "L1": {"d": 0, "s": "The bank's and the group's foundation.", "gap": "Capital, leadership, Gravity and Plard are Santander's.", "neo": "None.", "snb": "Capital, ownership, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
