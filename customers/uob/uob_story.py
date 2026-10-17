"""UOB's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from uob_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("ASEAN's largest consumer card issuer by billings as five discs that stack into one platform, from S$572 billion "
       "of assets and a 1935 founding at the bottom to the TMRW app, UOB Infinity and branches in five markets at the top. "
       "Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up "
       "across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in "
       "every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("aff", "Affluent & private clients", "gem"),
    ("trav", "Travellers across ASEAN", "plane"),
    ("citi", "Former Citi customers", "refresh-cw"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Six kinds of customer, more than 8.5 million retail customers in all: everyday customers, affluent and "
              "private clients, travellers across ASEAN, the customers who came over from Citi, small businesses and "
              "the corporates UOB Infinity serves.")

WHO = {"con": "A UOB customer", "aff": "An affluent client", "trav": "A traveller", "citi": "A former Citi customer",
       "sme": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day in Singapore",
     "why": "An account, a One Debit card, TMRW, PayNow and NETS, with scam controls behind them.",
     "steps": [("4.1", "personal", "Open an account"), ("2.3", "sgdebit", "Pay with One Debit"), ("5.1", "tmrw", "Run it in TMRW"),
               ("2.6", "paynow", "Send by PayNow"), ("3.1", "fraud", "Protected from scams")]},
    {"id": "card", "who": "con", "name": "Choose a credit card",
     "why": "Visa for most of the range, Mastercard for Lady's and PRVI, Amex for cashback.",
     "steps": [("2.1", "sgvisa", "Take a Visa card"), ("2.1", "sgmc", "Or a Lady's Mastercard"), ("2.5", "smartpay", "Spread a purchase"),
               ("3.4", "rewards", "Earn UNI$ and Rewards+")]},
    {"id": "affluent", "who": "aff", "name": "Grow wealth and travel well",
     "why": "Privilege Banking, Visa Infinite tiers and Michelin-led privileges.",
     "steps": [("4.2", "wealth", "Invest with Privilege Banking"), ("2.2", "visainf", "Move up a Visa Infinite tier"),
               ("3.4", "rewards", "Book Michelin experiences")]},
    {"id": "travel", "who": "trav", "name": "Spend across ASEAN",
     "why": "FX+ and KrisFlyer debit on Mastercard, QR at 40 million touchpoints, and Korean privileges via Woori.",
     "steps": [("2.3", "fxplus", "Spend with FX+"), ("2.3", "krisdebit", "Earn miles on KrisFlyer debit"),
               ("2.6", "scantopay", "Scan to pay in Malaysia or Thailand"), ("3.4", "woori", "Use Woori privileges in Korea")]},
    {"id": "citi", "who": "citi", "name": "Move over from Citi",
     "why": "Four markets of Citi customers migrated and re-carded onto UOB.",
     "steps": [("4.3", "citi", "Become a UOB customer"), ("2.2", "mycards", "Get a UOB credit card"),
               ("2.3", "regdebit", "Bank with Mastercard debit"), ("5.1", "tmrw", "Switch to TMRW")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "SME banking, Mastercard business cards and UOB Infinity.",
     "steps": [("4.4", "sme", "Bank with UOB"), ("2.4", "regal", "Carry a Regal metal card"), ("2.4", "mybiz", "Or a Platinum Business card in Malaysia"),
               ("5.2", "infinity", "Pay suppliers on UOB Infinity")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "Transaction banking, commercial cards and tokenised deposits.",
     "steps": [("4.4", "gwb", "Use transaction banking"), ("2.4", "commercial", "Issue commercial cards"),
               ("2.7", "swift", "Settle with tokenised deposits")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Agent Pay, the Lady's and PRVI cards, regional debit, KrisFlyer debit and SME metal cards.",
     "steps": [("3.2", "agentpay", "Agent Pay, live since March 2026"), ("2.1", "sgmc", "Lady's and PRVI Mastercard"),
               ("2.3", "regdebit", "Debit in Malaysia, Thailand and Vietnam"), ("2.3", "krisdebit", "KrisFlyer debit"),
               ("2.4", "regal", "Regal World Elite business card")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, travel and business cards could land",
     "why": "Where UOB has needs and Mastercard is not yet in: agentic TMRW, scam tools, commercial cards on UOB Infinity, cross-border spend and card-linked offers.",
     "steps": [("3.3", "insights", "Agentic tokens for TMRW's AI"), ("3.1", "fraud", "Scam scores and passkeys"),
               ("2.4", "commercial", "Virtual cards on UOB Infinity"), ("2.3", "fxplus", "Cross-border spend tools"),
               ("3.4", "rewards", "Card-linked offers for Rewards+")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across UOB's map",
    "title": "Visa holds the premium tier; Mastercard holds debit and the agents",
    "lead": "UOB is ASEAN's top consumer credit card issuer by billings across Visa and Mastercard, and calls itself Visa's largest issuer in the region; in July 2026 it moved more than 300,000 Visa Infinite cards to Visa's new top tiers. Mastercard carries debit in Malaysia, Thailand and Vietnam, the Lady's and PRVI cards, the Regal and Platinum Business SME cards, and UOB's agentic payments, live in Singapore since March 2026. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are UOB's own (2Q26 results, 7 August 2026; Annual Report 2025) or from Visa, Mastercard and press. Networks were read from UOB card pages; Thai credit cards and the Citi books' networks were not readable, and no network contract has been published.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Credit billings", "Top in ASEAN", "Across Visa and Mastercard, three years"],
        ["Premium", "Visa", "300,000+ Visa Infinite cards moved up, July 2026"],
        ["Singapore credit", "Mostly Visa", "Lady's and PRVI on Mastercard; Amex for cashback"],
        ["Regional debit", "Mastercard", "Malaysia, Thailand, Vietnam"],
        ["SME cards", "Mastercard", "Regal World Elite (2019), Platinum Business"],
        ["Agentic", "Agent Pay", "Live March 2026; ASEAN testing from April"],
        ["Account-to-account", "PayNow, NETS, QR", "DuitNow and PromptPay links"],
        ["Digital money", "Swift ledger", "Tokenised deposits, Aug–Sep 2026"],
    ],
    "sides": {
        "neo": {"dir": "Regional debit, Lady's and PRVI Mastercard, KrisFlyer and FX+ debit, SME cards, wallet tokens and Agent Pay.",
                "deals": "What it does not do: the premium credit tier, PayNow, NETS, QR, tokenised deposits or UOB's own AI and fraud models."},
        "snb": {"dir": "Visa's premium and Singapore cards, Amex cashback, PayNow and NETS, national QR schemes, Swift's ledger and UOB's own AI.",
                "deals": "Where they meet: dual-network debit, commercial cards and Apple Pay tokens."},
    },
    "tl": [
        ["May 2019", "Regal Business Metal with Mastercard"],
        ["Jan 2022", "Citi ASEAN consumer deal agreed"],
        ["Nov 2023", "Citi Indonesia completed; four markets in"],
        ["Jul 2024", "Woori Card privileges, Mastercard first"],
        ["Mar 2026", "First live Agent Pay transaction in Singapore"],
        ["Apr 2026", "UOB leads Mastercard's ASEAN agentic testing"],
        ["Jul 2026", "Visa Infinite tiers across five markets"],
        ["Aug 2026", "UOBAM sale; Swift ledger with HSBC"],
        ["Oct 2026", "AWS cloud and AI MoU"],
    ],
    "l": {
        "U": {"d": 1, "s": "Debit holders outside Singapore and Lady's and PRVI cardholders carry Mastercard.",
              "gap": "Premium and most Singapore credit cardholders carry Visa; regional debit holders and SMEs carry Mastercard.",
              "neo": "Regional debit holders, Lady's and PRVI cardholders, SME card users.", "snb": "Visa Infinite and Singapore Visa cardholders, Amex users, PayNow users."},
        "L5": {"d": 0, "s": "The front doors are UOB's.", "gap": "TMRW, UOB Infinity and branches are UOB's; co-brands split across networks.",
               "neo": "KrisFlyer debit co-brand.", "snb": "TMRW, Infinity, branches, Visa co-brands."},
        "L4": {"d": 0, "s": "The business lines lean on Visa for premium.", "gap": "Wealth clients carry Visa Infinite; SME cards are Mastercard; the Citi books' networks are not public.",
               "neo": "SME cards.", "snb": "Wealth, wholesale and markets."},
        "L3": {"d": 1, "s": "Agent Pay is Mastercard's; fraud and AI are UOB's.", "gap": "Mastercard runs agentic payments and shares tokens with Visa; insights, fraud and rewards are UOB's own.",
               "neo": "Agent Pay, Mastercard tokens.", "snb": "Fraud models, TMRW insights, rewards."},
        "L2": {"d": 1, "s": "Debit and SME on Mastercard; premium on Visa.", "gap": "Visa has premium credit; Mastercard regional debit and SME cards; PayNow, NETS and QR carry account payments.",
               "neo": "Regional debit, Lady's, PRVI, Regal, Platinum Business.", "snb": "Visa Infinite, Singapore Visa cards, Amex, PayNow, NETS, QR, Swift."},
        "L1": {"d": 0, "s": "UOB's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, family ownership, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
