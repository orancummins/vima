"""Bank of Cyprus's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from bankofcyprus_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Cyprus' largest financial group as five discs that stack into one platform, from €29 billion of assets at the "
       "bottom to the BoC Mobile App, 56 branches and Jinius at the top. Click the stack to open it. Choose who you are "
       "and what you want to do, and the areas that deliver it light up across the layers, joined in the order they act. "
       "Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("young", "Young people", "graduation-cap"),
    ("aff", "Savers, investors & policyholders", "coins"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates & international clients", "factory"),
    ("merch", "Merchants", "store"),
]
USERS_DESC = ("Six kinds of customer, reaching about three quarters of Cypriots: everyday customers, young people, savers "
              "and policyholders, small businesses, corporates and international clients, and the merchants JCC serves.")

WHO = {"con": "A Bank of Cyprus customer", "young": "A young customer", "aff": "A saver", "sme": "A small business",
       "corp": "A corporate treasurer", "merch": "A merchant"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "An account, a debit card on Visa or Mastercard, the app, wallets and alerts.",
     "steps": [("4.1", "accounts", "Open a QuickAccount"), ("2.1", "debitmc", "Pay with a debit card"), ("2.5", "wallets", "Tap with Apple Pay or Google Pay"),
               ("5.1", "app", "Run it in the app"), ("3.3", "security", "Get an alert on every payment")]},
    {"id": "pay", "who": "con", "name": "Pay friends and shop online",
     "why": "QuickPay by phone number, Click to Pay online and Fleksy instalments.",
     "steps": [("2.6", "quickpay", "Send with QuickPay"), ("2.5", "c2p", "Check out with Click to Pay"), ("3.2", "fleksy", "Spread the cost with Fleksy"),
               ("3.5", "marketplace", "Shop on Jinius")]},
    {"id": "travel", "who": "con", "name": "Travel and earn miles",
     "why": "The Aegean co-brand and the Elite card, both on Mastercard, with antamivi on top.",
     "steps": [("2.2", "aegean", "Take the Aegean Mastercard"), ("2.2", "elite", "Upgrade to Elite"), ("3.1", "antamivi", "Earn antamivi cashback")]},
    {"id": "young", "who": "young", "name": "Start banking young",
     "why": "Joey for children, then prepaid and youth cards.",
     "steps": [("4.1", "joey", "Start with Joey"), ("2.4", "prepaid", "Get a Prepaid Visa"), ("2.4", "youthcard", "Use the Youth Culture Card")]},
    {"id": "home", "who": "con", "name": "Buy a home or a car",
     "why": "Digital housing loans with an instant decision and car loans through the dealer.",
     "steps": [("4.1", "housing", "Apply for a digital housing loan"), ("4.2", "dealers", "Finance a car at the dealer"), ("4.4", "genins", "Insure it with Genikes")]},
    {"id": "save", "who": "aff", "name": "Save, invest and insure",
     "why": "EuroLife, private banking and Wealthyhood.",
     "steps": [("4.4", "lifeins", "Protect with EuroLife"), ("4.5", "wealthyhood", "Invest in stocks and ETFs"), ("4.5", "privatebank", "Use private banking")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A business account opened online, cards on both networks, Jinius invoicing and JCC acceptance.",
     "steps": [("4.2", "business", "Open a business account online"), ("2.3", "bizcards", "Order business cards"), ("3.5", "jiniusb2b", "Invoice on Jinius"),
               ("2.7", "jcc", "Take cards through JCC")]},
    {"id": "merchant", "who": "merch", "name": "Take payments",
     "why": "JCC terminals, gateway and JCCsmart, accepting every network.",
     "steps": [("2.7", "jcc", "Accept cards with JCC"), ("2.7", "jccsmart", "Collect bills with JCCsmart"), ("3.3", "security", "Screen fraud with JCC")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "A Mastercard version of each card family, the Aegean, Elite and business prepaid cards, JCC acceptance and wallet tokens.",
     "steps": [("2.1", "debitmc", "Mastercard debit"), ("2.2", "aegean", "Aegean co-brand"), ("2.2", "elite", "Elite Mastercard"),
               ("2.3", "topup", "Business Top Up"), ("2.7", "jcc", "Accepted at JCC merchants")]},
    {"id": "mcnext", "who": "mc", "name": "Where Click to Pay, agents and offers could land",
     "why": "Where Bank of Cyprus has needs and Mastercard is not yet in: Click to Pay for Mastercard cards, P2P beyond Visa+, Agent Pay for the conversational app, offers in antamivi and instalments behind Fleksy.",
     "steps": [("2.5", "c2p", "Click to Pay for Mastercard cards"), ("2.6", "quickpay", "Mastercard Move against Visa+"), ("3.4", "assistant", "Agent Pay for conversational banking"),
               ("3.1", "antamivi", "Card-linked offers"), ("3.2", "fleksy", "Installments behind Fleksy")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Bank of Cyprus's map",
    "title": "Every card on both networks, but the extras are Visa's",
    "lead": "Bank of Cyprus issues its debit, credit and business cards on both Visa and Mastercard and does not say how they split. Mastercard alone carries the Aegean co-brand, the Elite card and the business prepaid card, and JCC, the group's acquirer, takes every network. Visa has the services on top: Click to Pay, Visa+ behind QuickPay and the only personal prepaid card. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (H1 2026 results, 4 August 2026) or from the bank's card pages, JCC and Cypriot press. The bank publishes no card count by network; networks for the virtual, Joey, Youth Culture and Fleksy cards are not stated.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa and Mastercard", "Both offered; split not published ⚠"],
        ["Credit", "Visa and Mastercard", "Elite and Aegean on Mastercard only"],
        ["Business", "Visa and Mastercard", "Top Up prepaid on Mastercard"],
        ["Click to Pay", "Visa only", "Visa debit, credit and prepaid"],
        ["P2P", "Visa+", "QuickPay; 259,000 active users"],
        ["Acquiring", "JCC, 75% owned", "All networks; €9.2bn in H1 2026"],
        ["Digital euro", "JCC in ECB pilot", "July 2026"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard debit, credit and business cards, the Aegean co-brand, Elite and Business Top Up, wallet tokens and acceptance at JCC merchants.",
                "deals": "What it does not do: Click to Pay, P2P, prepaid for individuals, fraud scoring, AI or rewards."},
        "snb": {"dir": "Visa cards in every family, Visa Click to Pay and Visa+, SEPA instant transfers, the digital euro pilot, and the bank's own antamivi, Fleksy, Jinius and AI.",
                "deals": "Where they meet: the same card families, wallets, antamivi and JCC."},
    },
    "tl": [
        ["1989", "JCC starts processing cards"],
        ["Feb 2019", "Mastercard Blue closed to new customers"],
        ["2021", "Aegean Mastercard co-brand ⚠"],
        ["Sep 2024", "London delisted; Athens listing"],
        ["Sep 2025", "JCCsmart Mastercard bill-pay campaign"],
        ["Dec 2025", "Avenga agentic-AI banking"],
        ["Mar 2026", "2026–28 targets; CDB deal"],
        ["May 2026", "Aegean card benefits trimmed"],
        ["Jul 2026", "JCC in the digital euro pilot"],
        ["Sep 2026", "JCCsmart Visa promotion"],
    ],
    "l": {
        "U": {"d": 1, "s": "Cardholders carry Visa or Mastercard; travellers carry Mastercard.",
              "gap": "Every card family is on both networks; Aegean and Elite holders are Mastercard's, prepaid holders Visa's.",
              "neo": "Mastercard cardholders, Aegean and Elite holders, JCC merchants.", "snb": "Visa cardholders, QuickPay users, policyholders, investors."},
        "L5": {"d": 0, "s": "The front doors are the bank's.", "gap": "App, branches and Jinius are the group's own.", "neo": "None.", "snb": "BoC Mobile App, branches, Jinius."},
        "L4": {"d": 0, "s": "The business lines carry cards on both networks.", "gap": "Accounts and business banking come with either network's card; loans, insurance and investing have no network role.",
               "neo": "Mastercard debit and business cards.", "snb": "Loans, EuroLife, Genikes, Wealthyhood."},
        "L3": {"d": 0, "s": "Rewards, BNPL, fraud and AI are the group's own.", "gap": "antamivi spans both networks; Fleksy, JCC fraud monitoring and the AI assistant name no scheme.",
               "neo": "Mastercard cards inside antamivi.", "snb": "antamivi, Fleksy, JCC monitoring, Avenga AI, Jinius."},
        "L2": {"d": 1, "s": "Cards are shared; the extras are Visa's.", "gap": "Mastercard has a version of each card family and the co-brand; Visa has Click to Pay, Visa+ and prepaid.",
               "neo": "Mastercard debit and credit, Aegean, Elite, Top Up, JCC acceptance.", "snb": "Visa cards, Click to Pay, Visa+, SEPA Instant, digital euro."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, governance, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
