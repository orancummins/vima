"""Wells Fargo's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from wellsfargo_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("A $2.25 trillion American bank as five discs that stack into one platform, from the balance sheet, a lifted asset cap "
       "and AI at the bottom to the app, 4,068 branches and Vantage at the top. Click the stack to open it. Choose who you are and "
       "what you want to do, and the areas that deliver it light up across the layers, joined in the order they act. Switch "
       "to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("card", "Cardholders & travellers", "credit-card"),
    ("home", "Home & car buyers", "house"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Companies & institutions", "factory"),
    ("wealth", "Wealth clients", "gem"),
]
USERS_DESC = ("Six kinds of customer: everyday customers, 34 million of them active on the app; cardholders and travellers; "
              "home and car buyers; small businesses; the companies and institutions Commercial Banking and CIB serve; and "
              "wealth clients with $2.45 trillion of assets.")

WHO = {"con": "A Wells Fargo customer", "card": "A cardholder", "home": "A buyer", "sme": "A small business",
       "corp": "A corporate treasurer", "wealth": "A wealth client"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "An account, a debit card, Zelle and Paze, the app and Fargo.",
     "steps": [("4.1", "cbb", "Open a checking account"), ("2.4", "debit", "Pay with debit"), ("2.6", "zelle", "Send money with Zelle"),
               ("2.6", "paze", "Check out online with Paze"), ("5.1", "app", "Run it in the app"), ("3.2", "fargo", "Ask Fargo")]},
    {"id": "card", "who": "card", "name": "Earn on a Wells Fargo card",
     "why": "The own-brand Visa suite and the points behind it.",
     "steps": [("2.1", "activecash", "Take Active Cash"), ("2.1", "autograph", "Or Autograph"), ("3.4", "rewards", "Transfer points"),
               ("5.1", "app", "Manage it in the app")]},
    {"id": "travel", "who": "card", "name": "Travel on a partner card",
     "why": "Choice Hotels and Expedia cards, both on Mastercard.",
     "steps": [("5.3", "partners", "Apply through a partner"), ("2.2", "choice", "Earn with Choice Privileges"),
               ("2.2", "onekey", "Or with One Key"), ("3.4", "rewards", "Use the points")]},
    {"id": "home", "who": "home", "name": "Buy a home or a car",
     "why": "Home lending through branches, and auto finance through dealers.",
     "steps": [("5.2", "branches", "Visit a branch"), ("4.2", "homelending", "Take a mortgage"),
               ("5.3", "partners", "Visit a Volkswagen or Audi dealer"), ("4.2", "auto", "Finance the car")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "Business Banking, a Mastercard business card, Clover and Zelle.",
     "steps": [("4.1", "business", "Open a business account"), ("2.3", "signify", "Spend on Signify"),
               ("2.5", "merchant", "Take cards with Clover"), ("2.6", "zelle", "Get paid by Zelle")]},
    {"id": "corp", "who": "corp", "name": "Move money as a company",
     "why": "Vantage, instant and cross-border payments, tokenised deposits and fraud controls.",
     "steps": [("5.3", "vantage", "Log in to Vantage"), ("4.4", "cib", "Bank with CIB"), ("2.6", "instant", "Pay instantly"),
               ("2.7", "crossborder", "Pay across borders"), ("2.7", "tokdep", "Settle with tokenised deposits"),
               ("3.1", "fraud", "Check payees with Positive Pay")]},
    {"id": "wealth", "who": "wealth", "name": "Grow wealth",
     "why": "Premier, advisers with new AI tools, and the Private Bank.",
     "steps": [("4.1", "premier", "Move up to Premier"), ("5.3", "advisorgw", "Meet an adviser"), ("3.2", "aiteammate", "Helped by AI Teammate"),
               ("4.5", "wim", "Invest with Wells Fargo Advisors"), ("4.5", "privatebank", "Join the Private Bank")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The partner co-brands, the small-business card, Attune ⚠, an old Finicity data link and acceptance at Wells Fargo's merchants.",
     "steps": [("2.2", "choice", "Choice Privileges, exclusive Mastercard"), ("2.2", "onekey", "One Key, World Elite"),
               ("2.3", "signify", "Signify Business Cash"), ("2.2", "attune", "Attune ⚠"), ("3.3", "finicity", "Finicity data exchange ⚠"),
               ("2.5", "merchant", "Acceptance at Clover merchants")]},
    {"id": "mcnext", "who": "mc", "name": "Where acquiring, Premier cards and agents could land",
     "why": "Where Wells Fargo has needs and Mastercard is not yet in: services for the acquirer it now owns, Premier cards with no network named, rebuilt business and commercial cards, Agent Pay for Fargo, and cross-border and stablecoin links.",
     "steps": [("2.5", "merchant", "Risk and data services for the acquirer"), ("4.1", "premier", "World Elite benefits for Premier cards"),
               ("2.3", "commcard", "Commercial and virtual cards"), ("3.2", "fargo", "Agent Pay for Fargo"),
               ("2.7", "stablecoin", "Cross-border and stablecoin links")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Wells Fargo's map",
    "title": "Visa at the core, Mastercard on the partner cards",
    "lead": "Wells Fargo built its own consumer credit suite on Visa from 2021, and its debit cards are Visa too ⚠. Mastercard holds the partner and business lanes: the Choice Hotels cards, where it is the exclusive network, Expedia's One Key cards and the Signify business card. Bilt, its biggest Wells Fargo co-brand, left the bank in February 2026. Zelle and Paze, which Wells Fargo co-owns, carry its payments and online checkout. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the company's own (Q3 2026 results, 13 October 2026) or from Wells Fargo's newsroom, filings and press. The debit network is inferred from the account agreement; the commercial card network was not found; and no Wells Fargo network agreement with Visa or Mastercard has been made public.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Own-brand credit", "Visa", "Active Cash, Reflect, Autograph; from 2021"],
        ["Debit", "Visa ⚠", "$145 billion in Q3 2026"],
        ["Co-brands", "Mastercard", "Choice (exclusive, 2023), One Key (2024)"],
        ["Business card", "Mastercard", "Signify Business Cash, May 2024"],
        ["Bilt", "Left Wells Fargo", "February 2026; still Mastercard"],
        ["Commercial card", "Not found", "WellsOne and virtual card"],
        ["Acquiring", "All networks", "Wholly owned since April 2025"],
        ["Checkout & P2P", "Paze, Zelle", "Bank-owned, Wells Fargo co-owns"],
    ],
    "sides": {
        "neo": {"dir": "The Choice and One Key co-brands, Signify, Attune ⚠, a Finicity data link from 2017 ⚠, and acceptance at Wells Fargo's merchants.",
                "deals": "What it does not do: own-brand credit, debit, Zelle and Paze, tokenised deposits, stablecoins or AI."},
        "snb": {"dir": "Visa credit and debit, Zelle, Paze and RTP, its own tokenised deposits and a bank stablecoin venture, and Google Cloud for AI.",
                "deals": "Where they meet: the merchant business, which accepts every network, and the Premier cards still to come."},
    },
    "tl": [
        ["c. 2003", "Visa renewed as primary brand ⚠"],
        ["Apr 2017", "Finicity data-exchange deal ⚠"],
        ["Jun 2021", "Active Cash opens the Visa suite"],
        ["Mar 2022", "Bilt Mastercard"],
        ["Feb 2023", "Choice Privileges Mastercard"],
        ["May 2024", "Signify Business Cash Mastercard"],
        ["Jul 2024", "One Key cards with Expedia"],
        ["Apr 2025", "Merchant Services wholly owned"],
        ["Feb 2026", "Bilt leaves for Cardless"],
        ["Aug 2026", "Tokenized deposits launched"],
    ],
    "l": {
        "U": {"d": 1, "s": "Partner and small-business cardholders carry Mastercard.",
              "gap": "Own-brand credit and debit holders carry Visa; Choice, One Key and Signify holders carry Mastercard.",
              "neo": "Co-brand and business cardholders.", "snb": "Debit and own-brand credit holders, borrowers, wealth clients."},
        "L5": {"d": 1, "s": "The partner channel runs through Mastercard co-brands.", "gap": "App, branches and portals are Wells Fargo's; Choice and Expedia bring Mastercard cards.",
               "neo": "Co-brand partners.", "snb": "App, branches, Vantage, Advisor Gateway."},
        "L4": {"d": 1, "s": "Business Banking has a Mastercard card; the rest carries none or Visa.", "gap": "Premier cards are planned with no network named; loans and wealth have no network role.",
               "neo": "Signify for business owners.", "snb": "Accounts, loans, Commercial Banking, CIB, wealth."},
        "L3": {"d": 1, "s": "A Finicity data link ⚠; the rest is Wells Fargo's.", "gap": "Fraud controls, Fargo and rewards are Wells Fargo's own; Finicity's 2017 deal may still stand.",
               "neo": "Finicity data exchange ⚠.", "snb": "Fraud controls, Fargo, AI Teammate, Gateway, rewards."},
        "L2": {"d": 1, "s": "Co-brand and business cards on Mastercard; the core on Visa.", "gap": "Visa has own-brand credit and debit; Mastercard has the partner and business cards; Zelle, Paze and tokens are bank-owned.",
               "neo": "Choice, One Key, Signify, Attune ⚠, acceptance.", "snb": "Visa credit and debit, Zelle, Paze, RTP, tokenised deposits."},
        "L1": {"d": 0, "s": "The company's own foundation.", "gap": "Nothing in the foundation is Mastercard's; the head of cards once worked there.", "neo": "None.", "snb": "Capital, regulation, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
