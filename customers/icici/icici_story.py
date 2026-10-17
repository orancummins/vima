"""ICICI Bank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from icici_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("India's second-largest private bank as five discs that stack into one platform, from a ₹24 trillion balance sheet "
       "and 124,324 staff at the bottom to iMobile, InstaBIZ, 7,608 branches and co-brand partners at the top. Click the "
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
USERS_DESC = ("Seven kinds of customer: everyday customers, about 2 crore credit-card holders ⚠, homebuyers, Indians abroad, "
              "small businesses growing 28% a year, merchants on ICICI terminals and the corporates and MNCs wholesale banking serves.")

WHO = {"con": "An ICICI Bank customer", "card": "A cardholder", "home": "A homebuyer", "nri": "An Indian abroad",
       "sme": "A small business", "mer": "A merchant", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a debit card, UPI in iMobile and fraud controls.",
     "steps": [("5.3", "branches", "Open an account"), ("2.5", "debit", "Pay with a debit card"), ("2.4", "upi", "Pay by UPI"),
               ("5.1", "imobile", "Run it in iMobile"), ("3.1", "fraud", "Lock unused channels")]},
    {"id": "amazon", "who": "card", "name": "Shop with the Amazon Pay card",
     "why": "The no-fee Visa co-brand sold on amazon.in, with rewards paid into Amazon Pay balance.",
     "steps": [("5.4", "partners", "Apply on amazon.in"), ("2.3", "amazonpay", "Get the Amazon Pay ICICI card"), ("3.4", "rewards", "Earn up to 5% back")]},
    {"id": "upi", "who": "con", "name": "Pay on UPI with credit",
     "why": "RuPay credit cards on UPI QR codes since December 2023.",
     "steps": [("2.4", "rupayupi", "Link a RuPay credit card to UPI"), ("5.1", "imobile", "Scan and pay in iMobile"), ("3.4", "rewards", "Earn reward points")]},
    {"id": "premium", "who": "card", "name": "Travel at the top end",
     "why": "Emeralde Private Metal on Mastercard, or Times Black and 1838 Reserve on Visa.",
     "steps": [("2.1", "emeralde", "Hold Emeralde Private Metal"), ("2.2", "timesblack", "Or a Times Black or 1838 Reserve"),
               ("2.3", "makemytrip", "Book on a MakeMyTrip card")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "A ₹5.1 trillion mortgage book, insurance from the group.",
     "steps": [("5.3", "branches", "Apply at a branch"), ("4.1", "mortgages", "Take a mortgage"), ("4.4", "insurance", "Insure it with ICICI Lombard or ICICI Life")]},
    {"id": "nri", "who": "nri", "name": "Bank in India from abroad",
     "why": "Money2India, GIFT City and investments at home.",
     "steps": [("2.7", "xborder", "Send money home with Money2India"), ("2.5", "debit", "Use an NRI debit card"), ("4.4", "amc", "Invest with ICICI Pru AMC")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "Business banking, InstaBIZ and business cards.",
     "steps": [("5.2", "instabiz", "Bank in InstaBIZ"), ("4.2", "bizbank", "Borrow from business banking"), ("2.5", "bizcards", "Spend on a business card")]},
    {"id": "merchant", "who": "mer", "name": "Take payments",
     "why": "ICICI terminals and Merchant STACK accept cards of every network and UPI.",
     "steps": [("2.6", "acquiring", "Accept cards and UPI in store"), ("5.2", "instabiz", "Manage it in InstaBIZ"), ("4.2", "bizbank", "Borrow against sales")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The Mastercard leg of the gemstone pairs, Emeralde Private Metal, Diamant, MakeMyTrip, NRI debit and a debit-activation campaign.",
     "steps": [("2.1", "gemstone", "Coral, Rubyx and Sapphiro with Amex"), ("2.1", "emeralde", "Emeralde Private Metal"),
               ("2.2", "diamant", "Diamant on Mastercard World"), ("2.3", "makemytrip", "MakeMyTrip with RuPay"),
               ("3.4", "mcmarketing", "Debit-activation campaign")]},
    {"id": "mcnext", "who": "mc", "name": "Where network choice, premium and tokens could land",
     "why": "Where ICICI has needs and Mastercard is not yet in: the network on each new card and the Visa co-brand's renewals, the top end, Apple Pay tokens, agentic payments, commercial cards and NRI remittances.",
     "steps": [("2.3", "amazonpay", "Win the network choice on co-brand renewals"), ("2.2", "timesblack", "A World Legend answer to 1838 Reserve"),
               ("3.2", "wallets", "Mastercard tokens for Apple Pay"), ("3.3", "genai", "Agent Pay for ICICI's AI"),
               ("2.5", "bizcards", "Purchase and travel cards"), ("2.7", "xborder", "Remittances on Mastercard Move")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across ICICI Bank's map",
    "title": "The other half of ICICI's card pairs, while Visa holds Amazon and the top end",
    "lead": "ICICI Bank issues 16.1% of India's credit cards, many of them in pairs: Mastercard with American Express on the Coral, Rubyx, Sapphiro and Emeralde range, or Visa with RuPay. Mastercard also carries Emeralde Private Metal, the MakeMyTrip co-brand and the old Diamant card. Visa holds the Amazon Pay co-brand and the new Times Black and 1838 Reserve cards; RuPay takes credit onto UPI. Since September 2024 the RBI has made every new card a choice of network. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (Q1 FY27 presentation and Annual Report 2025-26, both 18 July 2026) or from card pages, card-market data and press. No split by network is published; Mastercard's newsroom could not be read, and the 2025 case study is marked ⚠.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Credit cards", "Four networks", "16.1% of India's cards; book −1.9% y/y"],
        ["Gemstone range", "Mastercard + Amex", "Coral, Rubyx, Sapphiro, Emeralde"],
        ["Amazon Pay", "Visa", "Since October 2018; 2m+ by 2021"],
        ["Top end", "Visa", "Times Black; 1838 Reserve, October 2026"],
        ["MakeMyTrip", "Mastercard + RuPay", "Travel co-brand"],
        ["UPI credit", "RuPay", "Live since December 2023"],
        ["Network choice", "RBI rule", "In force since September 2024"],
        ["Apple Pay", "Not live", "Launched in India 30 September 2026 without ICICI"],
    ],
    "sides": {
        "neo": {"dir": "The Mastercard leg of the gemstone pairs, Emeralde Private Metal, Diamant, MakeMyTrip, NRI debit, acceptance at ICICI terminals and marketing services on debit activation.",
                "deals": "What it does not do: Amazon Pay, Times Black and 1838 Reserve, RuPay on UPI, UPI itself, Amex business cards or the bank's AI."},
        "snb": {"dir": "Visa on Amazon Pay, the super-premium cards and Wealth Select debit; Amex on the other half of each pair; RuPay on UPI credit and NCMC debit; UPI and ICICI's own platforms.",
                "deals": "Where they meet: the choice of network on each card ICICI issues or renews."},
    },
    "tl": [
        ["Nov 2012", "Diamant on Mastercard World"],
        ["Oct 2018", "Amazon Pay ICICI card on Visa"],
        ["Oct 2020", "Amazon Pay card passes 1 million"],
        ["Jul 2021", "RBI bars Mastercard from new cardholders"],
        ["Jun 2022", "Mastercard curbs lifted"],
        ["Dec 2023", "RuPay credit cards live on UPI"],
        ["Sep 2024", "Choice of card network in force"],
        ["Apr 2025", "Merchant Services stake sold to Fiserv"],
        ["2025", "Mastercard debit-activation campaign ⚠"],
        ["Dec 2025", "ICICI Pru AMC listed"],
        ["Feb 2026", "Mastercard's first Agent Pay payments in India, not ICICI"],
        ["May 2026", "RBI approves Bakhshi to 2028"],
        ["30 Sep 2026", "Apple Pay launches without ICICI"],
        ["Oct 2026", "1838 Reserve on Visa"],
    ],
    "l": {
        "U": {"d": 1, "s": "Many cardholders carry a Mastercard; many carry Visa, Amex or RuPay.",
              "gap": "Gemstone and MakeMyTrip holders carry Mastercard; Amazon Pay, Times Black and UPI users do not.",
              "neo": "Gemstone, Emeralde and MakeMyTrip cardholders, NRI debit holders.", "snb": "Amazon Pay and super-premium holders, UPI users, mortgage and loan customers."},
        "L5": {"d": 1, "s": "The front doors are ICICI's; MakeMyTrip is a Mastercard partner.", "gap": "iMobile, InstaBIZ and branches are the bank's own; Amazon and Times sell Visa cards.",
               "neo": "MakeMyTrip as a partner.", "snb": "iMobile, InstaBIZ, branches, Amazon, Times Internet, Adani One."},
        "L4": {"d": 0, "s": "The business lines have no network role.", "gap": "Loans, wholesale and the group are ICICI's; commercial cards sit in Rails.",
               "neo": "None.", "snb": "Mortgages, loans, business banking, insurers, AMC, broker."},
        "L3": {"d": 1, "s": "One Mastercard marketing campaign ⚠; the rest is ICICI's.", "gap": "Fraud, AI and rewards are in-house; tokens by network are not public and Apple Pay is not live.",
               "neo": "Debit-activation campaign ⚠.", "snb": "Fraud controls, GenAI, rewards and EMI."},
        "L2": {"d": 1, "s": "Half of many card pairs; none of UPI.", "gap": "Mastercard has the gemstone legs, Emeralde, MakeMyTrip and NRI debit; Visa has Amazon and the top end; RuPay has UPI credit.",
               "neo": "Gemstone pairs, Emeralde, Diamant, MakeMyTrip, acceptance.", "snb": "Visa Amazon Pay and Times Black, Amex pairs, RuPay on UPI, UPI, FASTag, remittances."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, leadership, listing, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
