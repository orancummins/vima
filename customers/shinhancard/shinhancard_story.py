"""Shinhan Card's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from shinhancard_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Korea's number-two card company by half-year profit as five discs that stack into one platform, from ₩44 trillion of "
       "assets and LG Card's franchise at the bottom to the SOL Pay app and partner channels at the top. Click the stack to "
       "open it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday cardholders", "user-round"),
    ("trav", "Travellers", "plane"),
    ("prem", "Premium customers", "gem"),
    ("foreign", "Foreigners in Korea", "earth"),
    ("merch", "Merchants & sole traders", "store"),
    ("corp", "Partners & investors", "briefcase-business"),
]
USERS_DESC = ("Six kinds of user, about 28 million cardholders in all ⚠: everyday cardholders, travellers, premium customers, "
              "foreign residents and visitors, the merchants and sole traders who take and use Shinhan cards, and the partners "
              "and investors behind them.")

WHO = {"con": "A Shinhan cardholder", "trav": "A traveller", "prem": "A premium customer", "foreign": "A foreigner in Korea",
       "merch": "A merchant", "corp": "A partner"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Pay day to day",
     "why": "The everyday loop: a Plan card, domestic-only or on Mastercard, paid through SOL Pay, with points and scam checks.",
     "steps": [("2.1", "plan", "Take a Plan card"), ("2.3", "domestic", "Pay in Korea on Korean rails"), ("5.1", "solpay", "Pay with SOL Pay"),
               ("3.3", "points", "Earn MyShinhan points"), ("3.1", "fame", "Protected from scams")]},
    {"id": "travel", "who": "trav", "name": "Spend abroad",
     "why": "SOL Travel on Mastercard, Haru on JCB for Japan, UnionPay QR for China.",
     "steps": [("2.4", "soltravel", "Take SOL Travel"), ("2.4", "soltj", "Use SOL Travel J in Japan"), ("2.5", "haru", "Or Haru on JCB"),
               ("2.5", "upi", "Scan UnionPay QR in China"), ("2.6", "nfc", "Tap with SOL Pay abroad")]},
    {"id": "premium", "who": "prem", "name": "Hold a premium card",
     "why": "The BEST-X and The CLASSIC NEO on Mastercard, the Mercedes-Benz card, The CLASSIC Air on Amex.",
     "steps": [("2.2", "bestx", "Take The BEST-X"), ("2.2", "benz", "Or the Mercedes-Benz card"), ("2.2", "cair", "Or The CLASSIC Air"),
               ("3.3", "points", "Collect miles and gifts")]},
    {"id": "borrow", "who": "con", "name": "Borrow on a card",
     "why": "Card loans, cash advances and car finance.",
     "steps": [("4.1", "loans", "Take a card loan"), ("4.2", "mycar", "Finance a car with MyCar"), ("3.2", "mydata", "Track it in MyData")]},
    {"id": "foreign", "who": "foreign", "name": "Live in or visit Korea",
     "why": "TripPASS for visitors, the E9pay card for residents.",
     "steps": [("4.4", "trippass", "Use TripPASS as a visitor"), ("4.4", "e9pay", "Get the E9pay card as a resident"), ("5.3", "partners", "Apply through E9pay's app")]},
    {"id": "merch", "who": "merch", "name": "Run a small business",
     "why": "Business cards, MySHOP tools and fraud checks.",
     "steps": [("4.3", "biz", "Take a business card"), ("4.3", "myshop", "Use MySHOP Partner"), ("3.2", "databiz", "Draw on Shinhan's data")]},
    {"id": "partner", "who": "corp", "name": "Partner with Shinhan Card",
     "why": "PLCCs with fintechs and brands, and Shinhan Bank's channels.",
     "steps": [("3.3", "plcc", "Launch a partner card"), ("5.3", "partners", "Sell it in the partner's app"), ("5.2", "supersol", "Reach Super SOL users")]},
    {"id": "future", "who": "con", "name": "Let an AI agent pay",
     "why": "Agent Pay with Mastercard, and stablecoin tests.",
     "steps": [("2.7", "agentpay", "Let an agent book and pay"), ("2.8", "stablepoc", "Pay from a stablecoin wallet"), ("2.8", "solana", "On Solana")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The international version of the Plan and premium cards, SOL Travel, Agent Pay, the hybrid-card test and Vietnam.",
     "steps": [("2.1", "plan", "Plan cards on Mastercard"), ("2.2", "bestx", "Premium cards on Mastercard"), ("2.4", "soltravel", "SOL Travel with Travel Rewards"),
               ("2.7", "agentpay", "Agent Pay"), ("4.5", "svfc", "THE FIRST in Vietnam")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, wallets and scam tools could land",
     "why": "Where Shinhan has needs and Mastercard is not yet in: Agent Pay at scale, Apple Pay tokens, scam prevention, stablecoin cards, business cards and foreigners in Korea.",
     "steps": [("2.7", "agentpay", "Agent Pay in travel and shopping"), ("2.6", "applepay", "Tokens for Apple Pay"), ("3.1", "solfds", "Scam and identity tools"),
               ("2.8", "stablepoc", "A stablecoin-linked card"), ("4.3", "biz", "Commercial cards"), ("4.4", "trippass", "Cards and transfers for foreigners")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Shinhan Card's map",
    "title": "Mastercard is the default overseas brand, but home is Korean rails",
    "lead": "Mastercard is the brand on the international version of Shinhan Card's flagship Plan cards and its 2025–26 premium cards, and on the SOL Travel check card, 3 million strong. In March 2026 the two ran Korea's first live Agent Pay transaction. But every card also comes domestic-only, purchases in Korea run on Korean rails, older cards carry Visa, and Amex, JCB and UnionPay each have a card. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Shinhan Financial Group's (2Q 2026 results, 23 July 2026) or from Shinhan Card's Korean press releases, translated. Network volumes are not disclosed; the Visa line-up comes from an undated product page.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Flagship cards", "Domestic or Mastercard", "Plan series, 1 million+ (Sep 2025)"],
        ["Premium", "Mastercard, Amex, Visa", "BEST-X and CLASSIC NEO on Mastercard; CLASSIC Air on Amex"],
        ["Travel debit", "Mastercard", "SOL Travel, 3 million cards (Mar 2026)"],
        ["Agent Pay", "Mastercard", "Korea's first live transaction (Mar 2026)"],
        ["Older mass cards", "Visa", "B.Big, YOLO, Mr.Life ⚠ undated"],
        ["Japan, China", "JCB, UnionPay", "Haru (Jun 2025); UnionPay QR"],
        ["Stablecoins", "Mastercard and Visa tests", "Hybrid card; cross-border settlement (Apr 2026)"],
        ["Apple Pay", "Pending", "Terms approved Jun 2025 ⚠"],
    ],
    "sides": {
        "neo": {"dir": "The international version of new flagship and premium cards, SOL Travel and Travel Rewards, Agent Pay, the stablecoin hybrid-card test, and Vietnam's THE FIRST card.",
                "deals": "What it does not do: domestic purchases, older Visa cards, The CLASSIC Air, Haru, UnionPay QR, fraud and data."},
        "snb": {"dir": "Korean rails for domestic spend, Visa on older cards and the settlement test, Amex, JCB, UnionPay, SK Telecom for fraud, Solana for stablecoins.",
                "deals": "Where they meet: wallets and agentic payments, where Shinhan is still choosing partners."},
    },
    "tl": [
        ["Oct 2007", "Shinhan Card and LG Card integrated"],
        ["Nov 2015", "Visa VCP mobile card"],
        ["Sep 2020", "Visa data MOU"],
        ["Aug 2022", "THE FIRST card with Mastercard in Vietnam"],
        ["Sep 2023", "UnionPay QR in SOL Pay"],
        ["Feb 2024", "SOL Travel check card on Mastercard"],
        ["Feb 2025", "The BEST-X on Mastercard"],
        ["Jun 2025", "Haru on JCB; Apple Pay terms approved"],
        ["Mar 2026", "Agent Pay live with Mastercard"],
        ["Apr 2026", "Stablecoin tests with Mastercard and Visa; Solana MOU"],
        ["Sep 2026", "The CLASSIC Air on Amex"],
    ],
    "l": {
        "U": {"d": 1, "s": "Travellers and international-card holders carry Mastercard.",
              "gap": "Cardholders who pay for overseas use mostly get Mastercard on new cards; domestic-only holders, older Visa holders and Amex, JCB and UnionPay holders do not.",
              "neo": "SOL Travel holders, international Plan and premium cardholders.", "snb": "Domestic-only holders, Visa, Amex, JCB and UnionPay holders, merchants."},
        "L5": {"d": 0, "s": "The front doors are Shinhan's.", "gap": "SOL Pay, Super SOL and partner apps are Shinhan's or its partners'.", "neo": "None.", "snb": "SOL Pay, Super SOL, Kakao Bank, Toss, Naver Pay."},
        "L4": {"d": 1, "s": "Vietnam's card is Mastercard; lending is not.", "gap": "THE FIRST and the E9pay card use Mastercard; card loans, MyCar and merchant services have no network role.",
               "neo": "THE FIRST, E9pay card.", "snb": "Card loans, MyCar, MySHOP, overseas finance."},
        "L3": {"d": 0, "s": "Services are Shinhan's own.", "gap": "Fraud runs with SK Telecom, data and MyData are Shinhan's, Visa signed a data MOU.",
               "neo": "None.", "snb": "FAME, SOL Pay scam guard, GranData, MyData, AI-SOLa."},
        "L2": {"d": 1, "s": "Mastercard on new international cards, SOL Travel and Agent Pay.", "gap": "Korean rails carry domestic spend; Visa, Amex, JCB and UnionPay carry other cards.",
               "neo": "Plan and premium cards, SOL Travel, Agent Pay, hybrid-card test.", "snb": "Domestic-only cards, Visa mass cards, Amex, JCB, UnionPay, Solana."},
        "L1": {"d": 0, "s": "The company's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, funding, heritage, strategy."},
    },
    "t": area_lens(LAYERS),
}
