"""CTBC Bank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from ctbc_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Taiwan's largest card issuer as five discs that stack into one platform, from NT$7.55 trillion of assets and "
       "60 years of history at the bottom to the CTBC app, branches and partners' stores at the top. Click the stack to "
       "open it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("wealth", "Wealth clients", "gem"),
    ("home", "Homebuyers", "house"),
    ("abroad", "Travellers", "plane"),
    ("merch", "Merchants", "store"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Six kinds of customer: more than 8 million digital users and Taiwan's largest base of cardholders, "
              "wealth clients, homebuyers, travellers, the merchants CTBC acquires for and the corporates it banks at home "
              "and in 14 markets.")

WHO = {"con": "A CTBC customer", "wealth": "A wealth client", "home": "A homebuyer", "abroad": "A traveller",
       "merch": "A merchant", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank and pay day to day",
     "why": "The everyday loop: the app, a debit or credit card, a phone wallet and CTBC's own fraud alerts.",
     "steps": [("5.1", "app", "Open the CTBC app"), ("2.1", "cards", "Pay with a CTBC card"), ("2.6", "wallets", "Tap with a phone wallet"),
               ("3.1", "cardalerts", "Confirm a held payment"), ("3.3", "recurring", "See every subscription")]},
    {"id": "cobrand", "who": "con", "name": "Earn on a co-brand card",
     "why": "The uniopen card at 7-Eleven, the LINE Pay card online, points that move between partners.",
     "steps": [("5.3", "ecosystems", "Shop at a partner"), ("2.2", "uniopen", "Pay with the uniopen card"),
               ("2.2", "linepay", "Or the LINE Pay card"), ("3.4", "points", "Spend the points")]},
    {"id": "travel", "who": "abroad", "name": "Travel and spend abroad",
     "why": "Hotel and airline co-brands, foreign-currency accounts and the overseas network.",
     "steps": [("2.2", "marriott", "Book with the Marriott card"), ("2.2", "travelcards", "Earn miles"), ("2.8", "fx", "Hold foreign currency")]},
    {"id": "wealth", "who": "wealth", "name": "Grow and protect wealth",
     "why": "Half of CTBC's fee income: advisers, AI support and a premium card.",
     "steps": [("4.1", "wealthmgmt", "Invest with an adviser"), ("4.1", "aiadviser", "Adviser backed by AI"), ("2.1", "premium", "Carry a Ding Ji or Wealth Diamond card")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "NT$1.52 trillion of mortgages, through branches and the app.",
     "steps": [("5.2", "branches", "Visit a branch"), ("4.2", "mortgages", "Take a mortgage"), ("5.1", "app", "Repay in the app")]},
    {"id": "merchant", "who": "merch", "name": "Take payments",
     "why": "NT$930 billion acquired in 2025, from terminals to Tap to Pay on iPhone.",
     "steps": [("2.5", "acquiring", "Sign up for acquiring"), ("2.5", "softpos", "Accept on a phone"), ("5.3", "ecosystems", "Reach cardholders through partners")]},
    {"id": "corp", "who": "corp", "name": "Run a company's money",
     "why": "Corporate lending, API Banking and the Visa virtual card.",
     "steps": [("4.3", "corporate", "Borrow from CTBC"), ("4.3", "apibanking", "Connect the ERP"), ("2.4", "smartpay", "Pay with virtual cards")]},
    {"id": "asia", "who": "corp", "name": "Bank across Asia",
     "why": "Tokyo Star Bank, LH Financial Group and branches from India to the US.",
     "steps": [("4.4", "overseasnet", "Use the overseas network"), ("4.4", "tokyostar", "Bank in Japan"), ("4.4", "lhbank", "Bank in Thailand"),
               ("2.8", "fx", "Move money across borders")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The uniopen co-brand, the World tier of Ding Ji, part of the main card book, acceptance and wallet tokens.",
     "steps": [("2.2", "uniopen", "uniopen on Mastercard ⚠"), ("2.1", "premium", "World Mastercard tier"), ("2.1", "cards", "Part of the card book"),
               ("2.5", "acquiring", "Acceptance"), ("2.6", "wallets", "Tokens in phone wallets")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, scams and subscriptions could land",
     "why": "Where CTBC has needs and Mastercard is not yet in: Agent Pay for the AI card secretary, scam scoring, subscription controls, commercial cards, cross-border payouts and offers.",
     "steps": [("3.3", "aisecretary", "Agent Pay for the AI card secretary"), ("3.1", "cardalerts", "Scam scoring and alerts"),
               ("3.3", "recurring", "Subscription controls"), ("2.4", "smartpay", "Commercial cards against Visa"),
               ("4.4", "overseasnet", "Cross-border payouts"), ("3.4", "points", "Card-linked offers")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across CTBC Bank's map",
    "title": "Taiwan's biggest issuer, with Mastercard on uniopen and Visa on the showcases",
    "lead": "CTBC is Taiwan's largest card issuer and acquirer and issues on Visa, Mastercard, JCB and American Express. Mastercard's main programme is the uniopen co-brand with Uni-President, which passed 1 million cards in a year (World and Titanium tiers ⚠). Visa carries the LINE Pay card, Taiwan's biggest co-brand, with JCB, and won the newest launches: foodpanda, Marriott Bonvoy and a commercial virtual card in 2026. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are CTBC's own (2Q26 results, 18 August 2026; monthly results to September 2026; press releases) or FSC data via the Taipei Times. Many card pages were not reachable; networks for several co-brands are inferred from tier names or comparison sites.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Credit cards", "Visa, Mastercard, JCB, Amex", "NT$890bn spent in 2025"],
        ["uniopen", "Mastercard ⚠", "1 million cards, Aug 2026"],
        ["LINE Pay card", "Visa, JCB", "4 million+ cards by 2021"],
        ["Marriott Bonvoy", "Visa", "Launched Sep 2026"],
        ["Commercial", "Visa", "Smart Pay virtual card, Jul 2026"],
        ["Acquiring", "All networks", "NT$930bn in 2025"],
        ["Agent Pay", "Not CTBC", "DBS Taiwan first, Mar 2026"],
    ],
    "sides": {
        "neo": {"dir": "The uniopen co-brand, the World tier of Ding Ji, part of the main card book, tokens in phone wallets and acceptance at CTBC's merchants.",
                "deals": "What it does not do: the LINE Pay card, the 2023–26 showcase co-brands, commercial cards, fraud tools, AI or open banking."},
        "snb": {"dir": "Visa on LINE Pay, Marriott, foodpanda and the Smart Pay card; JCB on LINE Pay and Ding Ji; FISC's domestic rails; CTBC's own fraud models and AI.",
                "deals": "Where they meet: the main card book and the Ding Ji premium card, issued on several networks."},
    },
    "tl": [
        ["1974", "Taiwan's first credit card"],
        ["Feb 2017", "First-wave Apple Pay bank"],
        ["Jul 2021", "LINE Pay card (Visa, JCB) passes 4 million"],
        ["Dec 2023", "foodpanda card on Visa"],
        ["Aug 2025", "uniopen card launched (Mastercard ⚠)"],
        ["Nov 2025", "AI card secretary; open banking phase 3"],
        ["Mar 2026", "Mastercard's first Taiwan Agent Pay, with DBS Taiwan"],
        ["Jul 2026", "Smart Pay commercial card with Visa"],
        ["Aug 2026", "uniopen passes 1 million cards"],
        ["Sep 2026", "Marriott Bonvoy card on Visa"],
    ],
    "l": {
        "U": {"d": 1, "s": "uniopen holders carry Mastercard; LINE Pay holders carry Visa or JCB.",
              "gap": "Cardholders are split across four networks; uniopen's million are Mastercard's.",
              "neo": "uniopen holders, some Ding Ji and other cardholders.", "snb": "LINE Pay, Marriott and foodpanda holders, corporates on Smart Pay."},
        "L5": {"d": 0, "s": "The front doors are CTBC's and its partners'.", "gap": "App, branches, ATMs and partners' apps have no network role.", "neo": "None.", "snb": "App, LINE account, branches, partners."},
        "L4": {"d": 0, "s": "The business lines carry no Mastercard role.", "gap": "Wealth, mortgages, corporate banking and overseas banks are CTBC's; API Banking feeds a Visa card.",
               "neo": "None.", "snb": "Wealth, mortgages, corporate and overseas banking."},
        "L3": {"d": 0, "s": "Fraud, identity and AI are CTBC's own.", "gap": "Card alerts, AI ATMs, Fast-ID and the AI card secretary are built in-house; no Mastercard service is public.",
               "neo": "None public.", "snb": "CTBC's fraud models, AI, Fast-ID, points."},
        "L2": {"d": 1, "s": "uniopen on Mastercard; LINE Pay and the new launches on Visa.", "gap": "Visa has LINE Pay, Marriott, foodpanda and the commercial card; Mastercard has uniopen, part of the card book and acceptance.",
               "neo": "uniopen, Ding Ji World tier, acceptance, tokens.", "snb": "Visa and JCB co-brands, Visa commercial card, FISC rails."},
        "L1": {"d": 0, "s": "CTBC's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, group, heritage, AI, strategy."},
    },
    "t": area_lens(LAYERS),
}
