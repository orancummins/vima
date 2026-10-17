"""Banamex's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from banamex_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Mexico's second-largest card issuer as five discs that stack into one platform, from a Ps 1.4 trillion balance "
       "sheet, a bank founded in 1884 and owners preparing an IPO at the bottom to the app, 1,261 branches and 9,112 ATMs "
       "at the top. Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it "
       "light up across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard "
       "goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday Mexicans", "user-round"),
    ("young", "Young digital customers", "smartphone"),
    ("aff", "Priority & private clients", "gem"),
    ("home", "Homebuyers", "house"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Companies & governments", "factory"),
    ("saver", "Savers & policyholders", "coins"),
]
USERS_DESC = ("Seven kinds of customer, more than 20 million in all: everyday account and card holders, young customers "
              "on Switch and LineUp, Priority, Beyond and private clients, homebuyers, SMEs, companies and governments, "
              "and the 8 million+ Afore savers and policyholders.")

WHO = {
    "con": "A Banamex customer", "young": "A young customer", "aff": "A Priority client", "home": "A homebuyer",
    "sme": "A small business", "corp": "A company treasurer", "saver": "A saver",
}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: a payroll account and debit card, the app, SPEI transfers and fraud protection.",
     "steps": [("2.4", "debit", "Get paid into a payroll account"), ("5.1", "app", "Run it in the app"),
               ("2.7", "spei", "Send money by SPEI"), ("3.1", "securecall", "Protected by Secure Call"),
               ("3.2", "clarity", "See who you paid")]},
    {"id": "young", "who": "young", "name": "Open an account on the phone",
     "why": "Switch for younger customers, a phone wallet and the entertainment cards.",
     "steps": [("2.4", "switch", "Open Switch remotely"), ("2.5", "wallets", "Add it to Google Pay or Apple Pay"),
               ("2.2", "lineup", "Get presales with LineUp"), ("2.1", "joy", "Or carry Joy")]},
    {"id": "credit", "who": "con", "name": "Borrow and earn on a card",
     "why": "The own-brand Mastercard range and Momentos points.",
     "steps": [("2.1", "credit", "Take Descubre, Explora or Conquista"), ("3.3", "momentos", "Earn Momentos points"),
               ("2.5", "wallets", "Pay by phone"), ("3.1", "controls", "Lock it in the app")]},
    {"id": "shop", "who": "con", "name": "Shop with a store card",
     "why": "Co-brands with Costco on Visa and La Comer and Home Depot on Mastercard.",
     "steps": [("2.2", "costco", "Carry Costco Banamex"), ("2.2", "lacomer", "Or La Comer Card"),
               ("2.2", "retailcards", "Or Home Depot")]},
    {"id": "travel", "who": "aff", "name": "Travel as a Priority client",
     "why": "Beyond on Visa, Platinum and Priority on Mastercard, and the lounges each brings.",
     "steps": [("2.3", "priority", "Bank as Priority"), ("2.1", "platinum", "Carry Platinum"),
               ("3.3", "mcbenefits", "Use LoungeKey and Concierge"), ("2.3", "beyond", "Or step up to Beyond"),
               ("4.4", "wealth", "Invest with Private Banking")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "Instant approval for payroll customers and income checks through Belvo.",
     "steps": [("3.2", "belvo", "Verify income through Belvo"), ("4.1", "mortgage", "Take a mortgage"),
               ("4.5", "seguros", "Insure it with Seguros Banamex")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "An SME account and loans, card acceptance through Global Payments and an online shop.",
     "steps": [("4.2", "sme", "Open an SME account"), ("2.6", "acquiring", "Take cards on a terminal"),
               ("2.6", "pagoshops", "Sell online with Pago Shops"), ("2.8", "commcards", "Give staff a company card")]},
    {"id": "corp", "who": "corp", "name": "Run a company's cash",
     "why": "Commercial and government banking, cash management and CIB.",
     "steps": [("4.3", "commercial", "Borrow from Banamex"), ("2.8", "cashmgmt", "Pay and collect on BancaNet Empresarial"),
               ("4.3", "cib", "Raise capital with CIB")]},
    {"id": "retire", "who": "saver", "name": "Save for retirement",
     "why": "Afore Banamex, Seguros and the new Pensiones annuities.",
     "steps": [("4.6", "afore", "Save in Afore Banamex"), ("4.5", "seguros", "Build Plan Patrimonial"),
               ("4.5", "pensiones", "Take an annuity")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The own-brand credit cards, Priority and debit ⚠, La Comer, Mastercard benefits and Pago Shops.",
     "steps": [("2.1", "credit", "Own-brand cards on Mastercard"), ("2.3", "priority", "Priority on Mastercard"),
               ("2.4", "debit", "Debit ⚠"), ("2.2", "lacomer", "La Comer co-brand"),
               ("3.3", "mcbenefits", "LoungeKey and Concierge"), ("2.6", "pagoshops", "Pago Shops tokens")]},
    {"id": "mcnext", "who": "mc", "name": "Where tokens, scam checks and corporate cards could land",
     "why": "Where Banamex has needs and Mastercard is not yet in: wallet tokens and Click to Pay, scam checks on SPEI, merchant data, corporate cards, and the Visa programmes as new owners review contracts.",
     "steps": [("2.5", "wallets", "Token services and Click to Pay"), ("3.1", "securecall", "Scam scores on SPEI transfers"),
               ("3.2", "clarity", "Merchant data for Instant Clarity"), ("2.8", "commcards", "Commercial cards"),
               ("2.2", "costco", "Bid for Costco at renewal"), ("1.2", "ipo", "Lock in terms before the IPO")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Banamex's map",
    "title": "Mastercard's card bank, with Visa at the top and the IPO ahead",
    "lead": "Ten of the fourteen credit cards Banamex sells run on Mastercard, including the whole own-brand range and the 2025 La Comer card, and Priority and everyday debit carry Mastercard benefits ⚠. Visa holds the top Beyond card and the Costco, LineUp and Affinity co-brands. With Citi down to about 51%, a new CEO since June 2026 and an IPO aimed at January 2027 ⚠, contracts are open to review. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (2Q26 report, July 2026; 2025 Integrated Annual Report). Networks were read from Banamex's card pages on 17 October 2026; no volume split by network is published, and debit is read from its Mastercard offers ⚠.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Credit cards", "10 Mastercard, 4 Visa", "Ps 173.5bn book, 24% share"],
        ["Own brands", "Mastercard", "Clásica to Platinum; Descubre, Explora, Conquista"],
        ["Top card", "Visa", "Beyond"],
        ["Co-brands", "Split", "Costco and LineUp on Visa; La Comer, Home Depot on Mastercard"],
        ["Debit", "Mastercard ⚠", "Priority confirmed; everyday inferred"],
        ["Acceptance", "Global Payments", "Pago Shops with Mastercard, 2025"],
        ["Owners", "Citi about 51%", "Chico Pardo 25%, investors 24%"],
        ["IPO", "January 2027 ⚠", "More than US$3bn reported"],
    ],
    "sides": {
        "neo": {"dir": "The own-brand credit range, Priority and debit ⚠, La Comer and Home Depot, LoungeKey and Concierge, and tokenised processing for Pago Shops.",
                "deals": "What it does not do: Beyond, Costco, LineUp, SPEI and CoDi, fraud models, or commercial cards (network not stated)."},
        "snb": {"dir": "Visa on Beyond, Costco, LineUp and Affinity; Banxico's SPEI and CoDi; Global Payments for acceptance; Banamex's own fraud and AI tools.",
                "deals": "Where they meet: phone wallets and acceptance, which carry both networks."},
    },
    "tl": [
        ["Feb 2016", "Banamex Wallet with Mastercard"],
        ["Jun 2021", "Simplicity Mastercard with dynamic CVC"],
        ["Jan 2022", "Citi announces its exit"],
        ["Dec 2024", "Separation from Citi México"],
        ["Mar 2025", "Banamex brand relaunched"],
        ["Jul 2025", "Global Payments renewed; Pago Shops with Mastercard"],
        ["Sep 2025", "La Comer card with Mastercard ⚠ date"],
        ["Dec 2025", "Chico Pardo buys 25%"],
        ["Apr 2026", "22.6% sold to investors"],
        ["Jun 2026", "Edgardo del Rincón CEO"],
        ["Jan 2027", "IPO target ⚠"],
    ],
    "l": {
        "U": {"d": 1, "s": "Most cardholders carry Mastercard.",
              "gap": "Own-brand credit, Priority and debit ⚠ carry Mastercard; Beyond, Costco and LineUp holders carry Visa.",
              "neo": "Own-brand cardholders, Priority clients, debit ⚠.", "snb": "Beyond, Costco, LineUp and Affinity holders; Afore and insurance customers."},
        "L5": {"d": 0, "s": "The front doors are Banamex's.", "gap": "App, branches, ATMs and partners are the bank's; co-brand partners are split.",
               "neo": "Co-brand partners La Comer and Home Depot.", "snb": "App, branches, Costco and LineUp."},
        "L4": {"d": 0, "s": "The business lines carry no network.", "gap": "Loans, mortgages, wealth, insurance and the Afore have no network role.",
               "neo": "None.", "snb": "Loans, mortgages, SME and corporate banking, Seguros, Afore."},
        "L3": {"d": 1, "s": "Mastercard benefits on the cards; the rest is Banamex's.", "gap": "LoungeKey and Concierge are Mastercard's; fraud, AI and points are Banamex's own.",
               "neo": "LoungeKey, Elite Lounge, Concierge, insurance.", "snb": "Secure Call, AI models, Belvo, Momentos."},
        "L2": {"d": 1, "s": "Credit and debit lean Mastercard; Visa has the top and Costco.", "gap": "Ten of fourteen credit cards are Mastercard; SPEI, CoDi and cash management are not card rails.",
               "neo": "Own-brand credit, Priority, debit ⚠, La Comer, Pago Shops.", "snb": "Beyond, Costco, LineUp, SPEI, CoDi."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's; the IPO resets the owners.", "neo": "None.", "snb": "Capital, owners, brand, strategy."},
    },
    "t": area_lens(LAYERS),
}
