"""Commercial Bank of Ceylon's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from combank_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Sri Lanka's largest private bank as five discs that stack into one platform, from Rs 3.74 trillion of assets "
       "at the bottom to ComBank Digital, 272 branches and agents at the top. Click the stack to open it. Choose who "
       "you are and what you want to do, and the areas that deliver it light up across the layers, joined in the order "
       "they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("prem", "Prestige & premium clients", "gem"),
    ("migr", "Migrant workers & digital earners", "plane"),
    ("sme", "Small businesses", "briefcase"),
    ("merch", "Merchants", "store"),
    ("corp", "Corporates & traders", "factory"),
]
USERS_DESC = ("Six kinds of customer, more than 4 million in all: everyday customers, Prestige and premium clients, "
              "migrant workers and freelancers sending money home, the SMEs ComBank lends most to, the merchants it "
              "acquires for, and the corporates behind a fifth of Sri Lanka's exports.")

WHO = {"con": "A ComBank customer", "prem": "A Prestige client", "migr": "A migrant worker", "sme": "A small business",
       "merch": "A merchant", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank and pay day to day",
     "why": "The everyday loop: open an account by video, a debit card on one of four networks, Google Pay, Q+ for QR and 3DS on top.",
     "steps": [("3.1", "onboarding", "Open an account by video"), ("2.1", "debit", "Get a debit card"), ("2.6", "gpaymc", "Tap with Google Pay"),
               ("2.9", "qplus", "Scan a LANKAQR code with Q+"), ("3.1", "threeds", "Shop online with 3DS")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "Gold, Silver and Platinum cards on four networks, instalments and Max Rewards.",
     "steps": [("2.2", "credit", "Take a credit card"), ("3.3", "epp", "Split a purchase into instalments"), ("3.3", "rewards", "Collect Max Rewards")]},
    {"id": "national", "who": "con", "name": "Pay on the national scheme",
     "why": "LankaPay JCB cards, fee-free in 2026, and LANKAQR through Q+.",
     "steps": [("2.5", "lankapay", "Take a LankaPay JCB card"), ("2.9", "qplus", "Pay by LANKAQR"), ("2.9", "cefts", "Move money on CEFTS")]},
    {"id": "premium", "who": "prem", "name": "Bank as a Prestige client",
     "why": "Prestige, the premium Visa, Mastercard and UnionPay cards, and airline miles.",
     "steps": [("4.1", "prestige", "Join Prestige"), ("2.2", "premium", "Carry Visa Infinite"), ("2.2", "worldmc", "Or World Mastercard"),
               ("2.2", "unionpay", "Take UnionPay for China"), ("3.3", "rewards", "Turn points into miles")]},
    {"id": "remit", "who": "migr", "name": "Send money home or earn abroad",
     "why": "Remittances through Gulf exchange houses, GIG+ accounts and PayPal withdrawals.",
     "steps": [("3.1", "onboarding", "Open an account from abroad"), ("2.10", "remit", "Send a remittance home"),
               ("2.10", "gig", "Withdraw PayPal earnings"), ("5.2", "branches", "Collect cash at a branch or ATM")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "The largest SME lender, AI underwriting, a BIZ Club Visa debit card and a Mastercard SME card.",
     "steps": [("4.2", "sme", "Bank with the biggest SME lender"), ("3.2", "ai", "Get a loan through AI underwriting"),
               ("2.1", "bizdebit", "Spend with BIZ Club debit"), ("2.4", "smecard", "Borrow on an SME card")]},
    {"id": "merchant", "who": "merch", "name": "Take payments",
     "why": "From a Soundbox for a market stall to POS, QR and the online gateway.",
     "steps": [("2.7", "soundbox", "Start with a Soundbox"), ("2.7", "pos", "Take cards on POS"), ("2.9", "qplus", "Accept QR"),
               ("2.8", "ipg", "Sell online with DCC")]},
    {"id": "corp", "who": "corp", "name": "Trade and pay as a corporate",
     "why": "TradeLink for trade, corporate and fuel cards, and bulk payments.",
     "steps": [("4.3", "trade", "Trade through TradeLink"), ("2.4", "corpcard", "Give staff corporate cards"),
               ("2.4", "fuelcard", "Run a fleet on fuel cards"), ("2.9", "cefts", "Pay salaries with Paymaster")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The co-brands, World Mastercard, the MPGS gateway, Google Pay tokens, Soundbox and fuel cards.",
     "steps": [("2.3", "cobrand", "Co-brand and affinity cards"), ("2.2", "worldmc", "World Mastercard"), ("2.8", "ipg", "MPGS and online DCC"),
               ("2.6", "gpaymc", "Google Pay tokens"), ("2.7", "soundbox", "Soundbox for micro merchants"), ("2.4", "fuelcard", "Corporate fuel cards")]},
    {"id": "mcnext", "who": "mc", "name": "Where tokens, fraud tools and remittances could land",
     "why": "Where ComBank has needs and Mastercard is not yet in: Click to Pay and card-on-file tokens, the gateway against Bancstac, AI fraud tools, commercial virtual cards, Move for remittances, offers and a Prestige card.",
     "steps": [("2.6", "gpaymc", "Click to Pay and card-on-file tokens"), ("2.8", "bancstac", "Keep e-commerce on MPGS"),
               ("3.1", "threeds", "AI fraud scoring"), ("2.4", "corpcard", "Commercial virtual cards"), ("2.10", "remit", "Mastercard Move for remittances"),
               ("3.3", "rewards", "Card-linked offers"), ("4.1", "prestige", "World Elite and Priceless for Prestige")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Commercial Bank of Ceylon's map",
    "title": "Four networks, and Mastercard holds the co-brands and the gateway",
    "lead": "ComBank issues debit and credit cards on Visa, Mastercard, UnionPay and the national LankaPay/JCB scheme, and does not publish the split. Visa holds the top consumer tiers, the corporate-card push and the first Google Pay launch. Mastercard holds World Mastercard, every co-brand and affinity card, the fuel card and ComBank's gateway since 2007, and it powers the new Soundbox. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (H1 2026 results, 13 August 2026; annual report 2025) or from CBSL, Visa, Mastercard and press. ComBank does not publish cards by network; networks come from its card pages.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Four networks", "No. 1 issuer; split not published ⚠"],
        ["Premium credit", "Visa, World Mastercard, UnionPay", "Visa Infinite and Signature on top"],
        ["Co-brands", "Mastercard", "Anagi, affinity, NEGC, Mobitel"],
        ["Corporate cards", "Visa and Mastercard", "Visa tiers 2024; Mastercard fuel card"],
        ["Gateway", "MPGS since 2007", "Online DCC Dec 2025; Bancstac Apr 2026 ⚠"],
        ["Wallets", "Google Pay", "Visa Nov 2025; Mastercard Feb 2026"],
        ["Micro merchants", "Soundbox", "Powered by Mastercard, Oct 2026"],
        ["Domestic", "LankaPay/JCB, LANKAQR", "Pushed by ComBank and the state"],
    ],
    "sides": {
        "neo": {"dir": "World Mastercard, the co-brands, fuel and SME cards, a share of debit and credit, MPGS and online DCC, Google Pay tokens, Soundbox, and acceptance everywhere ComBank acquires.",
                "deals": "What it does not do: the top Visa tiers, corporate-card growth, UnionPay, LankaPay, LANKAQR, remittances, fraud tools or rewards."},
        "snb": {"dir": "Visa premium, corporate and travel cards and the first Google Pay; UnionPay's travel cards; LankaPay/JCB and LANKAQR on domestic rails; Bancstac's gateway; ComBank's own 3DS, AI and rewards.",
                "deals": "Where they meet: debit, credit, POS and Google Pay, all on several networks at once."},
    },
    "tl": [
        ["2007", "First local bank on Mastercard MPGS"],
        ["Apr 2019", "World Mastercard Boingo Wi-Fi"],
        ["Mar 2023", "First LankaPay credit cards with JCB"],
        ["Sep 2023", "Mastercard Rugby World Cup promotion"],
        ["Feb 2024", "Visa corporate credit cards"],
        ["Nov 2025", "Google Pay for Visa cards"],
        ["Dec 2025", "Online DCC on MPGS"],
        ["Jan 2026", "UnionPay SplendorPlus"],
        ["Feb 2026", "Google Pay for Mastercard cards"],
        ["Apr 2026", "Bancstac gateway; national QR launch"],
        ["Jun 2026", "Amarasuriya becomes Mastercard Country Manager"],
        ["Oct 2026", "Soundbox powered by Mastercard"],
    ],
    "l": {
        "U": {"d": 1, "s": "Co-brand, World and fuel cardholders carry Mastercard; most others hold a mix.",
              "gap": "Debit and credit holders may carry any of four networks; premium clients lean to Visa and UnionPay.",
              "neo": "Co-brand, World Mastercard and fuel cardholders; merchants on Soundbox.", "snb": "Visa premium and corporate cardholders, UnionPay travellers, LankaPay and Q+ users."},
        "L5": {"d": 0, "s": "The front doors are ComBank's.", "gap": "Apps, branches and agents are the bank's; Soundbox reaches merchants through Payable.", "neo": "Soundbox via Payable.", "snb": "ComBank Digital, Flash, branches, Shakthi agents."},
        "L4": {"d": 1, "s": "The business lines carry mixed cards.", "gap": "SME cards are partly Mastercard; Prestige and corporate lean to Visa; trade and overseas have no network role.",
               "neo": "SME credit cards ⚠.", "snb": "Prestige's Visa debit, corporate cards, trade, Bangladesh."},
        "L3": {"d": 1, "s": "3DS and Goldnet serve every network; the rest is ComBank's.", "gap": "No Mastercard fraud, data or loyalty product is named; Goldnet processes all brands.",
               "neo": "Mastercard Identity Check through ComBank's 3DS ⚠.", "snb": "Own ACS, CardinalCommerce, AI underwriting, Max Rewards."},
        "L2": {"d": 1, "s": "Mastercard everywhere, Visa on top, domestic rails rising.", "gap": "Mastercard runs the gateway and Soundbox and owns the co-brands; Visa leads premium and corporate; LankaPay and LANKAQR grow.",
               "neo": "Co-brands, World, MPGS, Soundbox, Google Pay tokens.", "snb": "Visa premium and corporate, UnionPay, LankaPay/JCB, LANKAQR, Bancstac."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, owners, Euronet switch, IDEMIA, strategy."},
    },
    "t": area_lens(LAYERS),
}
