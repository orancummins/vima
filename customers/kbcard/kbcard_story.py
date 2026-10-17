"""KB Kookmin Card's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from kbcard_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Korea's number-three card company by half-year profit as five discs that stack into one platform, from ₩31 trillion of "
       "assets and Kookmin Bank's card heritage at the bottom to the KB Pay app and bank branches at the top. Click the stack to "
       "open it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday cardholders", "user-round"),
    ("trav", "Travellers", "plane"),
    ("prem", "Premium customers", "gem"),
    ("young", "Young customers", "graduation-cap"),
    ("biz", "Companies & merchants", "briefcase-business"),
    ("corp", "Partners & investors", "building-2"),
]
USERS_DESC = ("Six kinds of user, about 13 million members in all: everyday cardholders, travellers, premium customers, "
              "young customers on their first cards, the companies and merchants that hold and accept KB cards, and the "
              "partners and investors behind them.")

WHO = {"con": "A KB cardholder", "trav": "A traveller", "prem": "A premium customer", "young": "A young customer",
       "biz": "A company or merchant", "corp": "A partner"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Pay day to day",
     "why": "The everyday loop: an ALL·YOU·NEED card, domestic-only or with a brand, paid through KB Pay, with points and controls.",
     "steps": [("2.1", "kball", "Take KB ALL"), ("2.3", "domestic", "Pay in Korea on Korean rails"), ("5.1", "kbpay", "Pay with KB Pay"),
               ("3.3", "points", "Earn Pointree points"), ("3.1", "overseassafe", "Set payment controls")]},
    {"id": "travel", "who": "trav", "name": "Spend abroad",
     "why": "The Travelers check card on Mastercard, Travel Rewards cashback, K-World or UnionPay for Asia.",
     "steps": [("2.4", "travelers", "Take the Travelers check card"), ("3.3", "mtr", "Register for Travel Rewards"), ("2.4", "macao", "Or the Macao Edition"),
               ("2.3", "kworld", "Or use K-World abroad"), ("2.5", "upi", "Pay with UnionPay in China")]},
    {"id": "premium", "who": "prem", "name": "Hold a premium card",
     "why": "HERITAGE and KB YOU Prime, on Mastercard, JCB or Visa.",
     "steps": [("2.2", "hclassic", "Take HERITAGE Classic"), ("2.2", "hsmart", "Or HERITAGE Smart"), ("2.1", "youprime", "Or KB YOU Prime"),
               ("3.3", "points", "Collect miles and points")]},
    {"id": "borrow", "who": "con", "name": "Borrow on a card",
     "why": "Card loans, cash advances and instalment finance.",
     "steps": [("4.1", "loans", "Take a card loan"), ("4.2", "lease", "Finance a car or lease"), ("5.1", "kbpay", "Manage it in KB Pay")]},
    {"id": "young", "who": "young", "name": "Get a first card",
     "why": "Youth Club and Star Teens check cards, the Travelers card from age 7, and KB NEED Pay for wallet users.",
     "steps": [("4.1", "youth", "Open a Youth Club check card"), ("2.4", "travelers", "Take a Travelers card on holiday"), ("2.1", "needpay", "Move to KB NEED Pay"),
               ("5.1", "kbpay", "Run it from KB Pay")]},
    {"id": "biz", "who": "biz", "name": "Run a company or a shop",
     "why": "Corporate cards, merchant services and data for small merchants.",
     "steps": [("4.3", "corpcard", "Issue corporate cards"), ("4.4", "merchant", "Take card payments"), ("3.2", "datalake", "Use KB's merchant data")]},
    {"id": "partner", "who": "corp", "name": "Partner with KB Card",
     "why": "Processing for other banks, linked wallets and tourism partners.",
     "steps": [("2.3", "processing", "Run cards on KB's system"), ("5.3", "partners", "Link a wallet or co-brand"), ("3.2", "tourism", "Share tourism data")]},
    {"id": "future", "who": "con", "name": "Let an agent or a stablecoin pay",
     "why": "Agent-payment tests with Visa's programme and K-AP, stablecoin tests with Mastercard and SBI.",
     "steps": [("2.7", "agentpoc", "Let an AI agent pay"), ("2.8", "cpp", "Pay from a stablecoin wallet"), ("2.8", "hybrid", "Fall back to credit"),
               ("2.8", "sbi", "Japanese visitors pay in stablecoins")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Premium cards, KB YOU Prime, the Travelers check card with Travel Rewards, the Macao Edition and the stablecoin test.",
     "steps": [("2.2", "hclassic", "HERITAGE on Mastercard"), ("2.1", "youprime", "KB YOU Prime on Mastercard"), ("2.4", "travelers", "Travelers check card"),
               ("3.3", "mtr", "Travel Rewards cashback"), ("2.4", "macao", "Macao Edition"), ("2.8", "cpp", "Crypto Partner Program")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, corporate cards and tokens could land",
     "why": "Where KB has needs and Mastercard is not yet in: agent payments, wallet tokens, corporate cards, scam tools, travel debit share and a stablecoin card.",
     "steps": [("2.7", "agentpoc", "Agent Pay for KB cards"), ("2.6", "applepay", "Tokens for Apple Pay"), ("4.3", "corpcard", "Commercial cards"),
               ("3.1", "overseassafe", "Fraud and scam tools"), ("2.4", "travelers", "Grow travel debit share"), ("2.8", "hybrid", "A stablecoin-linked card")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across KB Card's map",
    "title": "Mastercard is KB's premium and travel brand, but KB built its own to avoid it",
    "lead": "Mastercard is the brand on KB Kookmin Card's HERITAGE premium cards and its new KB YOU Prime, on the Travelers check card with Travel Rewards and a Macao edition, and the network for its 2026 stablecoin test. But every card comes domestic-only, KB's own K-World brand carries JCB and UnionPay at the domestic fee, JCB sits beside Mastercard on new cards, and KB is working with Visa on agent payments and Apple Pay. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are KB Financial Group's (H1 2026, July 2026) as reported by the Korean business press, or from KB Card's releases, translated. Network volumes are not disclosed; networks for several 2026 cards are not stated.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Premium", "Mastercard, JCB, Visa", "HERITAGE Classic (Dec 2024)"],
        ["KB YOU Prime", "Mastercard or K-World JCB", "Feb 2026"],
        ["Travel debit", "Mastercard", "Travelers check card; 11.4% of overseas check-card spend"],
        ["Own brand", "K-World (JCB, UnionPay)", "Since 2014, at the domestic fee"],
        ["Stablecoins", "Mastercard", "Crypto Partner Program (Sep 2026)"],
        ["Agent payments", "Visa, K-AP", "Visa programme; SY Polaris test (Sep 2026)"],
        ["Apple Pay", "Pending", "Visa test, Jun 2026 ⚠"],
        ["Corporate cards", "Not stated", "Korea's largest base ⚠"],
    ],
    "sides": {
        "neo": {"dir": "HERITAGE and KB YOU Prime on Mastercard, the Travelers check card with Travel Rewards, the Macao Edition with Mastercard Korea, and the Crypto Partner Program stablecoin test.",
                "deals": "What it does not do: domestic purchases, K-World, Visa options, agent payments, Apple Pay, fraud and data."},
        "snb": {"dir": "Korean rails for domestic spend, K-World on JCB and UnionPay, Visa on SkyPass cards, the Apple Pay test and the agentic programme, SY Polaris and SBI.",
                "deals": "Where they meet: agent payments, wallets and stablecoins, where KB is still choosing partners."},
    },
    "tl": [
        ["Mar 2011", "KB Kookmin Card spun off from the bank"],
        ["Jul 2014", "K-World own brand with JCB; UnionPay in Sep"],
        ["Oct 2020", "KB Pay launched"],
        ["Jan 2023", "HERITAGE Smart with Mastercard World services"],
        ["Jun 2023", "Apple Pay letter of intent"],
        ["Dec 2024", "HERITAGE Classic on Mastercard, JCB and Visa"],
        ["Jan 2025", "Kim Jae-kwan becomes CEO"],
        ["Oct 2025", "Macao Edition with Mastercard Korea"],
        ["Nov 2025", "Mastercard Travel Rewards on the Travelers card"],
        ["Feb 2026", "KB YOU Prime on Mastercard or K-World JCB"],
        ["Jun 2026", "KB cards in Apple Pay during Visa's test"],
        ["Sep 2026", "Mastercard Crypto Partner Program; agent test with Visa programme"],
        ["Oct 2026", "SBI stablecoin and agent-identity MOU"],
    ],
    "l": {
        "U": {"d": 1, "s": "Travellers and premium holders carry Mastercard.",
              "gap": "Travelers check card and premium holders mostly get Mastercard; domestic-only, K-World, Visa and UnionPay holders do not.",
              "neo": "Travelers card holders, HERITAGE and KB YOU Prime Mastercard holders.", "snb": "Domestic-only and K-World holders, Visa and UnionPay holders, merchants."},
        "L5": {"d": 0, "s": "The front doors are KB's.", "gap": "KB Pay, the bank's branches and partner wallets are KB's or its partners'.", "neo": "None.", "snb": "KB Pay, KB Star Banking, Naver Pay, Kakao Pay, Toss."},
        "L4": {"d": 1, "s": "Card spending partly; lending and corporate cards not shown.", "gap": "Consumer spending is partly on Mastercard; loans, leasing and merchant services have no network role; corporate card networks are not stated.",
               "neo": "International consumer card spend.", "snb": "Card loans, leasing, merchant acquiring, overseas finance."},
        "L3": {"d": 1, "s": "Travel Rewards is Mastercard's; the rest is KB's.", "gap": "Payment controls, data and AI are KB's own; only Travel Rewards cashback runs on Mastercard.",
               "neo": "Mastercard Travel Rewards.", "snb": "Overseas controls, data lake, Pointree, copilot."},
        "L2": {"d": 1, "s": "Mastercard on premium, travel debit and the stablecoin test.", "gap": "Korean rails carry domestic spend; K-World, Visa, UnionPay and JCB carry other cards; agent tests run with Visa's programme.",
               "neo": "HERITAGE, KB YOU Prime, Travelers card, Macao Edition, Crypto Partner Program.", "snb": "Domestic-only cards, K-World, Visa, UnionPay, K-AP, SBI."},
        "L1": {"d": 0, "s": "The company's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, funding, heritage, strategy."},
    },
    "t": area_lens(LAYERS),
}
