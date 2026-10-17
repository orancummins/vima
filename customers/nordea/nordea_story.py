"""Nordea's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from nordea_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("The Nordics' largest bank group as five discs that stack into one platform, from EUR 400 billion of loans at "
       "the bottom to Nordea Mobile, Nordea Business and branches at the top. Click the stack to open it. Choose who "
       "you are and what you want to do, and the areas that deliver it light up across the layers, joined in the order "
       "they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("fam", "Families & young people", "users-round"),
    ("home", "Homebuyers", "house"),
    ("saver", "Savers & private banking", "coins"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Large corporates", "factory"),
]
USERS_DESC = ("Six kinds of customer across Denmark, Finland, Norway and Sweden: everyday customers (5 million of them "
              "digitally active), families, homebuyers, savers and private-banking clients, small businesses and the "
              "large corporates and institutions LC&I serves.")

WHO = {"con": "A Nordea customer", "fam": "A parent", "home": "A homebuyer", "saver": "A saver",
       "sme": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: the app, a Visa debit card, phone wallets, Click to Pay and Nordea ID.",
     "steps": [("5.1", "mobile", "Bank in Nordea Mobile"), ("2.1", "debitse", "Pay with Visa debit"), ("2.4", "wallets", "Tap with a phone wallet"),
               ("2.4", "c2p", "Check out with Click to Pay"), ("3.1", "nordeaid", "Confirm in Nordea ID")]},
    {"id": "credit", "who": "con", "name": "Borrow and travel on a card",
     "why": "Nordea Gold and Premium on Mastercard, with Mastercard's lounges.",
     "steps": [("2.2", "gold", "Take Nordea Gold"), ("2.2", "premium", "Upgrade to Premium"), ("3.4", "travel", "Use LoungeKey and Fast Track")]},
    {"id": "family", "who": "fam", "name": "Give a child their first card",
     "why": "Nordea Family: a debit card, a wristband and the Gimi app.",
     "steps": [("4.1", "family", "Open Nordea Family"), ("2.1", "dankort", "Pay with Nordea Pay or Nordea Debit"), ("3.4", "cashback", "Earn cashback")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "A loan promise on a property portal, then a mortgage and advice.",
     "steps": [("5.4", "portals", "Get a loan promise on a portal"), ("4.1", "mortgages", "Take a mortgage"), ("5.3", "branches", "Meet an adviser")]},
    {"id": "save", "who": "saver", "name": "Save and invest",
     "why": "Savings, pensions and private banking, the growth area in the 2030 plan.",
     "steps": [("5.1", "mobile", "Invest in the app"), ("4.4", "nam", "Buy BetaPlus funds"), ("4.4", "lp", "Save for a pension"), ("4.4", "pb", "Move to Private Banking")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "Digital onboarding, cards, Nordea Finance and card acceptance through Nets.",
     "steps": [("4.2", "sme", "Open a business account"), ("2.1", "bizdebit", "Pay with Business Visa Debit"), ("2.3", "bizmc", "Spend on Business Mastercard"),
               ("2.6", "acquiring", "Take cards through Nets"), ("4.2", "nfinance", "Finance with Nordea Finance")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "LC&I lending, transaction banking, ERP links and company cards.",
     "steps": [("4.3", "lci", "Bank with LC&I"), ("2.7", "txb", "Run cash management"), ("2.3", "firstcard", "Give staff First Cards"), ("3.3", "openbanking", "Connect by API")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The credit and combination cards, Business Mastercard, travel benefits, Click to Pay, open-banking connections and the Agent Pay pilot.",
     "steps": [("2.2", "gold", "Nordea Gold on Mastercard"), ("2.3", "bizmc", "Business Mastercard"), ("3.4", "travel", "LoungeKey and Airport Experiences"),
               ("2.4", "c2p", "Click to Pay"), ("3.3", "mcob", "Mastercard Open Banking"), ("3.2", "agentpay", "Agent Pay pilot")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, SMEs and payments scale could land",
     "why": "Where Nordea has needs and Mastercard is not yet in: Agent Pay across four countries, cards for 50,000 new small businesses, the payments scale programme, fraud tools, card-linked offers, and debit if it is ever tendered.",
     "steps": [("3.2", "agentpay", "Agent Pay across the Nordics"), ("4.2", "sme", "Cards and controls for new SMEs"), ("1.4", "processing", "Payments scale programme"),
               ("3.1", "fraud", "Fraud and scam scoring"), ("3.4", "cashback", "Card-linked offers"), ("2.1", "debitse", "Debit, if tendered ⚠")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Nordea's map",
    "title": "Visa for every day, Mastercard for credit and the first agent",
    "lead": "Visa carries Nordea's debit cards in all four countries, alongside Dankort in Denmark and BankAxept in Norway. Mastercard carries the credit and combination cards (Gold, Credit, Premium and Platinum), Business Mastercard and the premium travel benefits. In June 2026 the two ran Finland's first live Agent Pay transaction. Card processing sits with TietoEVRY and Nets, and acquiring with Nets. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (Q3 2026 report, 15 October 2026) or from Nordea's card pages in each country, Mastercard, Nets and press. No network agreement has been published; the split is read from current product pages. Norway's debit network is inferred from a fee table.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa", "Sweden, Finland; Visa/Dankort in Denmark"],
        ["Norway debit", "BankAxept + Visa", "Co-badged ⚠"],
        ["Credit", "Mastercard", "Gold, Credit, Premium, Platinum in four countries"],
        ["Company cards", "Mastercard; Visa debit", "Business Mastercard; First Card network not stated"],
        ["Agent Pay", "Mastercard", "First Finnish live payment, June 2026"],
        ["Click to Pay", "Mastercard and Visa", "Enrolled in Nordea Mobile"],
        ["Processing", "TietoEVRY, Nets", "Norway and Sweden; Denmark and Finland"],
        ["Acquiring", "Nets (Nexi)", "Sold in 2015"],
    ],
    "sides": {
        "neo": {"dir": "The credit and combination cards, Business Mastercard, the Stockmann co-brand, premium travel benefits, Click to Pay, open-banking connections and the Agent Pay pilot.",
                "deals": "What it does not do: debit, cashback, account-to-account payments, processing or acquiring."},
        "snb": {"dir": "Visa debit and cashback, Dankort and BankAxept, Swish and MobilePay, TietoEVRY and Nets processing, Nets acquiring, and Nordea's own platform and AI.",
                "deals": "Where they meet: Click to Pay and phone wallets, which carry both networks."},
    },
    "tl": [
        ["2008", "Stockmann Mastercard in Finland"],
        ["Jun 2015", "Merchant acquiring sold to Nets"],
        ["Oct 2018", "Head office moves to Helsinki"],
        ["Jun 2019", "Mastercard picked for P27"],
        ["Dec 2020", "TietoEVRY card processing for Norway and Sweden ⚠"],
        ["Jun 2021", "Nets partnership renewed for Denmark and Finland"],
        ["Nov 2025", "2030 strategy: payments a Nordic scale area"],
        ["Jun 2026", "First Finnish Agent Pay transaction"],
        ["Oct 2026", "Q3: payments and card fees up 4%"],
    ],
    "l": {
        "U": {"d": 1, "s": "Credit cardholders carry Mastercard; debit holders carry Visa.",
              "gap": "Every customer's everyday card is Visa (or Dankort, BankAxept); Gold, Premium and Business Mastercard holders carry Mastercard.",
              "neo": "Credit, combination and premium cardholders; Business Mastercard users.", "snb": "Debit holders, children on Nordea Pay, Swish and MobilePay users."},
        "L5": {"d": 0, "s": "The front doors are Nordea's.", "gap": "Nordea Mobile, Nordea Business, branches and portals are the group's own.", "neo": "None.", "snb": "Apps, branches, portals."},
        "L4": {"d": 1, "s": "Business Banking cards split; the rest has no network role.", "gap": "SMEs get Visa debit and Business Mastercard; mortgages, LC&I and wealth do not depend on a network.",
               "neo": "Business Mastercard for SMEs.", "snb": "Visa debit in Nordea Family and for SMEs; mortgages, LC&I, wealth."},
        "L3": {"d": 1, "s": "Agent Pay and travel benefits are Mastercard's; fraud is Nets'.", "gap": "Mastercard runs the Agent Pay pilot and premium travel benefits; fraud tools sit with Nets and Nordea; cashback is Visa's.",
               "neo": "Agent Pay, LoungeKey, Open Banking connection.", "snb": "Nets fraud, Nordea ID, Nordea AI, Visa Cashback."},
        "L2": {"d": 1, "s": "Credit on Mastercard, debit on Visa.", "gap": "Mastercard carries credit and combination cards; Visa, Dankort and BankAxept carry debit; Swish and MobilePay bypass cards.",
               "neo": "Gold, Credit, Premium, Business Mastercard, Click to Pay.", "snb": "Visa debit, Dankort, BankAxept, Swish, MobilePay, Nets acquiring."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Capital, leadership and platform are Nordea's; processing is outsourced to TietoEVRY and Nets.", "neo": "None.", "snb": "Capital, platform, TietoEVRY and Nets processing, strategy."},
    },
    "t": area_lens(LAYERS),
}
