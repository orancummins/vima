"""HDFC Bank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from hdfc_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("India's largest private bank as five discs that stack into one platform, from a ₹45.8 trillion balance sheet and "
       "103.6 million customers at the bottom to the app, PayZapp, 9,706 branches and co-brand partners at the top. Click the "
       "stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("card", "Cardholders", "credit-card"),
    ("home", "Homebuyers", "house"),
    ("nri", "Non-resident Indians", "plane"),
    ("sme", "Small businesses", "briefcase"),
    ("mer", "Merchants", "store"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Seven kinds of customer, 103.6 million in all: everyday customers, more than 2 crore cardholders, homebuyers, "
              "Indians abroad, small businesses, 20 lakh merchants on SmartHub Vyapar and the corporates wholesale banking serves.")

WHO = {"con": "An HDFC Bank customer", "card": "A cardholder", "home": "A homebuyer", "nri": "An Indian abroad",
       "sme": "A small business", "mer": "A merchant", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a debit card, UPI, the app and fraud checks.",
     "steps": [("5.3", "branches", "Open an account"), ("2.4", "debit", "Pay with a debit card"), ("2.5", "upi", "Pay by UPI"),
               ("5.1", "app", "Run it in the app"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "card", "who": "card", "name": "Spend on a co-brand card",
     "why": "Swiggy on Mastercard, Tata Neu and Pixel on Visa and RuPay, all in the app.",
     "steps": [("5.4", "partners", "Apply in a partner's app"), ("2.2", "swiggy", "Take a Swiggy card"), ("3.2", "tokens", "Add it to a phone wallet"),
               ("3.4", "rewards", "Earn rewards")]},
    {"id": "premium", "who": "card", "name": "Travel on a premium card",
     "why": "Infinia and Regalia Gold, or Diners Club at the top end.",
     "steps": [("2.1", "premium", "Hold Infinia or Regalia Gold"), ("2.3", "diners", "Or a Diners Black Metal"), ("3.4", "rewards", "Book through SmartBuy")]},
    {"id": "upi", "who": "con", "name": "Pay on UPI with credit",
     "why": "RuPay credit cards on UPI QR codes, and EMI on bigger buys.",
     "steps": [("2.5", "upicc", "Link a RuPay credit card to UPI"), ("5.2", "payzapp", "Scan and pay in PayZapp"), ("3.4", "easyemi", "Turn it into EMI")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "The mortgage book that came with HDFC Ltd, and insurance from the group.",
     "steps": [("5.3", "branches", "Apply at a branch"), ("4.1", "mortgages", "Take a mortgage"), ("4.4", "insurance", "Insure it with HDFC Life or ERGO")]},
    {"id": "nri", "who": "nri", "name": "Bank in India from abroad",
     "why": "PayZapp for Indians abroad, cross-border payments and investments at home.",
     "steps": [("5.2", "payzapp", "Use PayZapp from abroad"), ("2.7", "xborder", "Send money home"), ("4.4", "amc", "Invest with HDFC AMC")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "Business Banking, business cards and credit on UPI.",
     "steps": [("4.2", "bizbank", "Borrow from Business Banking"), ("4.2", "bizcards", "Spend on a business card"), ("2.5", "upicc", "Pay suppliers with UPI RuPay Biz")]},
    {"id": "merchant", "who": "mer", "name": "Take payments",
     "why": "SmartHub Vyapar in the shop and SmartGATEWAY online: cards of every network, UPI and e-rupee.",
     "steps": [("2.6", "vyapar", "Accept in store with SmartHub Vyapar"), ("2.6", "gateway", "Sell online with SmartGATEWAY"), ("2.7", "cbdc", "Take e-rupee"),
               ("2.2", "bizcobrand", "Borrow on a Pine Labs card")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The Swiggy cards, Mastercard variants across the card book, tokens and mandates, and the 2021 MSME facility.",
     "steps": [("2.2", "swiggy", "Swiggy BLCK and ORNGE on Mastercard"), ("2.1", "millennia", "Millennia, launched on Mastercard"),
               ("3.2", "tokens", "Mastercard tokens"), ("3.2", "recurring", "Recurring mandates"), ("4.2", "msmefund", "MSME credit facility")]},
    {"id": "mcnext", "who": "mc", "name": "Where network choice, agents and cross-border could land",
     "why": "Where HDFC has needs and Mastercard is not yet in: the choice of network on each new card, agentic payments, cross-border rails, acquirer tools and business cards.",
     "steps": [("2.1", "cards", "Win the choice of network at issue and renewal"), ("3.3", "bots", "Agent Pay for HDFC's agents"),
               ("2.7", "xborder", "Cross-border on Mastercard Move"), ("2.6", "vyapar", "Acquirer risk tools for a third of acquiring"),
               ("4.2", "bizcards", "Commercial and virtual cards")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across HDFC Bank's map",
    "title": "One network of four at India's biggest card issuer",
    "lead": "HDFC Bank issues 22% of India's credit cards and handles about a third of its card acquiring, on Visa, Mastercard, RuPay and Diners Club side by side. Mastercard carries the Swiggy co-brands relaunched in March 2026, launched the Millennia range in 2019 and tokenises HDFC cards; Visa has the Pixel and FIFA 2026 cards, and RuPay takes credit onto UPI. Since September 2024 the RBI has made every new card a choice of network. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (Q2 FY27 results, 17 October 2026; Annual Report 2025-26) or from Mastercard, card-market data and press. HDFC's card pages rarely state the network, and no split by network is published; several networks are inferred and marked ⚠.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Credit cards", "Four networks", "22% of India's cards; 29% of spend"],
        ["Swiggy", "Mastercard", "BLCK and ORNGE, March 2026"],
        ["Pixel, Tata Neu", "Visa and RuPay", "FIFA 2026 Visa card, April 2026"],
        ["Top end", "Diners Club", "Issuer and acquirer since 2011"],
        ["UPI credit", "RuPay", "UPI RuPay and Bharat cards"],
        ["Acquiring", "All networks", "About 35–36% of India"],
        ["Network choice", "RBI rule", "In force since September 2024"],
        ["Agent Pay", "Not HDFC", "India's first payments used Axis and RBL"],
    ],
    "sides": {
        "neo": {"dir": "Swiggy co-brands, Mastercard variants of proprietary and debit cards, tokens and mandates, and acceptance at HDFC's merchants.",
                "deals": "What it does not do: UPI, RuPay credit, Diners, Pixel and Tata Neu, the cross-border build or the bank's AI."},
        "snb": {"dir": "Visa on Pixel, Tata Neu and the FIFA card; RuPay on UPI credit and debit; Diners at the top end; UPI and HDFC's own platforms.",
                "deals": "Where they meet: the choice of network on each card HDFC issues or renews."},
    },
    "tl": [
        ["Oct 2011", "Diners Club issuing and acquiring deal"],
        ["Mar 2017", "HDFC Mastercards in Samsung Pay's launch"],
        ["Aug 2019", "Millennia range on Mastercard"],
        ["Jul 2021", "RBI bars Mastercard from new cardholders"],
        ["Aug 2021", "RBI lifts HDFC's card curbs"],
        ["Oct 2021", "MSME facility with Mastercard, USAID and DFC"],
        ["Dec 2021", "Google Pay tokens for HDFC Mastercards"],
        ["Jun 2022", "Mastercard curbs lifted"],
        ["Jul 2023", "Merger with HDFC Ltd"],
        ["Sep 2024", "Choice of card network in force"],
        ["Feb 2026", "Mastercard's first Agent Pay payments in India, not HDFC"],
        ["Mar 2026", "Swiggy BLCK and ORNGE on Mastercard"],
        ["Apr 2026", "Visa FIFA World Cup Pixel card"],
        ["Oct 2026", "Anup Bagchi named CEO; UPI merchant fee starts"],
    ],
    "l": {
        "U": {"d": 1, "s": "Some cardholders carry Mastercard; many carry Visa, RuPay or Diners.",
              "gap": "Swiggy and Mastercard-variant cardholders are Mastercard's; UPI users, RuPay and Diners holders are not.",
              "neo": "Swiggy cardholders, Mastercard-variant and debit holders.", "snb": "UPI users, Pixel, Tata Neu and Diners holders, mortgage and loan customers."},
        "L5": {"d": 1, "s": "The front doors are HDFC's; Swiggy is a Mastercard partner.", "gap": "App, PayZapp and branches are the bank's own; PayZapp holds cards of every network.",
               "neo": "Swiggy as a partner; Mastercards in PayZapp.", "snb": "App, NetBanking, branches, other co-brand partners."},
        "L4": {"d": 0, "s": "The business lines have no network role, bar the 2021 MSME facility.", "gap": "Loans, wholesale and the group are HDFC's; business cards are not public by network.",
               "neo": "MSME facility ⚠.", "snb": "Mortgages, loans, wholesale, insurance, AMC, NBFC."},
        "L3": {"d": 1, "s": "Mastercard tokens and mandates for Mastercards; the rest is HDFC's.", "gap": "Tokens and recurring payments run on each network; fraud, AI and rewards are in-house.",
               "neo": "Tokens, recurring mandates.", "snb": "Fraud tools, Neev and agentic bots, SmartBuy, EasyEMI."},
        "L2": {"d": 1, "s": "One network of four on cards; none on UPI.", "gap": "Mastercard has Swiggy and variants; Visa, RuPay and Diners share the rest; UPI and cross-border are outside the card networks.",
               "neo": "Swiggy, Millennia, Mastercard variants, acceptance.", "snb": "Visa Pixel and Tata Neu, RuPay on UPI, Diners, UPI, cross-border, e-rupee."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, leadership, merger, Neev, strategy."},
    },
    "t": area_lens(LAYERS),
}
