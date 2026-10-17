"""Barclays' kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

SUB = ("Britain's first card issuer as five discs that stack into one platform, from a £1.7 trillion balance sheet and "
       "three centuries since Lombard Street at the bottom to an app for 14 million people, 206 branches and partners "
       "from Tesco to JetBlue at the top. Click the stack to open it. Choose who you are and what you want to do, and "
       "the areas that deliver it light up across the layers, joined in the order they act. Switch to the Mastercard "
       "lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "UK customers", "user-round"),
    ("home", "Homebuyers", "house"),
    ("aff", "Premier & private clients", "gem"),
    ("sme", "Small businesses", "briefcase"),
    ("merch", "Merchants", "store"),
    ("corp", "Corporates & institutions", "factory"),
    ("us", "US cardholders", "flag"),
]
USERS_DESC = ("Seven kinds of customer: more than 20 million in the UK, homebuyers through branches and brokers, Premier "
              "and private clients, small businesses, 160,000 merchants on Barclaycard Payments, corporates and "
              "institutions, and more than 25 million US customers through partner cards.")

WHO = {
    "con": "A UK customer", "home": "A homebuyer", "aff": "A Premier client", "sme": "A small business",
    "merch": "A merchant", "corp": "A corporate treasurer", "us": "A US cardholder",
}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop for 20 million UK customers: an account, a Visa debit card, the app and scam screening.",
     "steps": [("4.1", "accounts", "Open a current account"), ("2.1", "debit", "Pay with Visa debit"),
               ("5.1", "app", "Run it in the app"), ("3.1", "fraud", "Payments screened for scams")]},
    {"id": "credit", "who": "con", "name": "Borrow on a Barclaycard",
     "why": "Britain's leading credit-card issuer: Barclaycard, Avios and Tesco cards.",
     "steps": [("2.2", "barclaycard", "Transfer a balance to Platinum"), ("2.2", "tesco", "Or take a Tesco Clubcard card"),
               ("2.2", "avios", "Or collect Avios"), ("3.3", "loyalty", "Earn the rewards")]},
    {"id": "buy", "who": "home", "name": "Buy a home",
     "why": "A £177 billion mortgage book, through branches, brokers and Kensington.",
     "steps": [("4.1", "accounts", "Save in an ISA"), ("5.4", "portals", "Apply through a broker"),
               ("4.1", "mortgages", "Take a mortgage")]},
    {"id": "wealth", "who": "aff", "name": "Grow your wealth",
     "why": "Premier, Planning & Advice, Direct Investing and the Private Bank.",
     "steps": [("4.1", "accounts", "Bank with Premier"), ("4.4", "pbwm", "Invest and get advice"),
               ("2.2", "avios", "Carry Avios Plus"), ("3.3", "loyalty", "Use Barclays Experiences")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A business account, a business card and card acceptance from Barclaycard Payments.",
     "steps": [("4.2", "bizbank", "Open a business account"), ("2.5", "commcards", "Carry a business card"),
               ("2.4", "bcpayments", "Take cards with Barclaycard Payments")]},
    {"id": "merchant", "who": "merch", "name": "Take card payments",
     "why": "Barclaycard Payments for 160,000 UK businesses, rebuilt with Brookfield.",
     "steps": [("2.4", "bcpayments", "Sign up for Barclaycard Payments"), ("3.1", "fraud", "Screen for fraud"),
               ("3.4", "agentic", "Get ready for agents")]},
    {"id": "corp", "who": "corp", "name": "Run a company's money",
     "why": "Transaction banking in the Corporate Bank, markets in the Investment Bank, and iPortal.",
     "steps": [("4.3", "ukcb", "Bank with the UK Corporate Bank"), ("2.5", "txbanking", "Pay and collect"),
               ("5.4", "portals", "Use iPortal"), ("4.5", "ib", "Hedge and raise capital"), ("2.6", "ubyx", "Settle tokenised money")]},
    {"id": "us", "who": "us", "name": "Earn miles with a US partner card",
     "why": "Barclays in the US is a partner-card bank: JetBlue, Emirates, GM, Frontier and more.",
     "steps": [("5.3", "partners", "Apply at the partner"), ("2.3", "usmc", "Carry a JetBlue Premier Mastercard"),
               ("2.3", "usvisa", "Or a Samsung or Wyndham Visa"), ("4.6", "usbank", "Borrow with Best Egg, save online")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "No group agreement, but programme by programme: most US co-brands, the UK Avios cards and the Tesco book.",
     "steps": [("2.3", "usmc", "US co-brands on Mastercard"), ("2.2", "avios", "Barclaycard Avios"),
               ("2.2", "tesco", "Tesco Bank's cards"), ("2.4", "bcpayments", "Acceptance at Barclaycard Payments")]},
    {"id": "mcnext", "who": "mc", "name": "Where scams, agents and Tesco could land",
     "why": "Where Barclays has needs and Mastercard is not yet in: scam scores under 50:50 reimbursement, agentic payments, keeping Tesco, services for Barclaycard Payments, new US co-brands, and UK debit if Visa's deal comes up.",
     "steps": [("3.1", "fraud", "Consumer Fraud Risk on Faster Payments"), ("3.4", "agentic", "Agent Pay on the Mastercard cards"),
               ("2.2", "tesco", "Keep Tesco on Mastercard"), ("2.4", "bcpayments", "Ethoca and Click to Pay for merchants"),
               ("2.3", "usvisa", "The next US co-brands"), ("2.1", "debit", "UK debit, if the Visa deal comes up")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Barclays' map",
    "title": "A Visa bank at home, a Mastercard bank in the US",
    "lead": "Barclays launched Britain's first credit card with BankAmericard, now Visa, in 1966, and renewed Visa as its UK scheme partner in 2020: UK debit and most Barclaycards are Visa. Mastercard has the Avios cards, Tesco Bank's book and most US partner cards (JetBlue, Emirates, Frontier, GM, AARP), though American Airlines left for Citi in 2026. No joint initiative with Mastercard has been announced. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (H1 2026 results, 28 July 2026) or come from Barclays, partner and press pages. Several card pages do not name the network; the term of the 2020 Visa agreement is not public.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["UK debit", "Visa", "Multi-year European partnership, renewed February 2020"],
        ["Barclaycard UK", "Mostly Visa", "Avios and Tesco on Mastercard"],
        ["US partner cards", "Mostly Mastercard", "JetBlue, Emirates, Frontier, GM, AARP; Wyndham and Samsung on Visa"],
        ["Lost", "AAdvantage", "To Citi, April 2026; stays on Mastercard"],
        ["Acquiring", "Barclaycard Payments", "160,000 businesses; Brookfield partnership"],
        ["Scams", "Barclays' own models", "Not named among Consumer Fraud Risk banks"],
        ["Agentic", "Nothing announced", "Neither network chosen"],
        ["Tokenised money", "Ubyx", "First stablecoin stake, January 2026"],
    ],
    "sides": {
        "neo": {"dir": "Most US partner cards, the UK Avios cards and Tesco Bank's credit cards, and acceptance at Barclaycard Payments.",
                "deals": "What it does not do: UK debit, most of Barclaycard, scam scoring, agentic payments, or any group agreement."},
        "snb": {"dir": "Visa debit and most Barclaycards, Visa co-brands in the US, Barclays' own fraud models and AI, Faster Payments, Ubyx.",
                "deals": "Where they meet: the co-brand renewals, the Tesco book, and the merchants at Barclaycard Payments."},
    },
    "tl": [
        ["1966", "Barclaycard launches with BankAmericard (Visa)"],
        ["Feb 2020", "Visa renewed as UK scheme partner"],
        ["Jul 2022", "Barclaycard Avios cards on Mastercard"],
        ["Nov 2024", "Tesco Bank, with its Mastercard book, joins Barclays"],
        ["Jan 2025", "JetBlue Premier World Elite Mastercard"],
        ["2025", "GM cards move from Goldman Sachs to Barclays, on Mastercard"],
        ["Apr 2026", "AAdvantage Mastercards leave for Citi"],
        ["Jun 2026", "Frontier and Barnes & Noble renewed"],
        ["Jul 2026", "Samsung Galaxy Card on Visa"],
    ],
    "l": {
        "U": {"d": 1, "s": "US cardholders mostly carry Mastercard; UK customers mostly Visa.",
              "gap": "Mastercard reaches US partner-card holders, Avios and Tesco cardholders; UK current-account customers carry Visa debit.",
              "neo": "US co-brand holders, Avios and Tesco cardholders.", "snb": "UK debit holders, most Barclaycard holders, homebuyers, corporates."},
        "L5": {"d": 0, "s": "The front doors are the bank's and its partners'.", "gap": "Apps, branches, broker platforms and iPortal are Barclays'; partners' cards are partly Mastercard.",
               "neo": "Partner channels for Mastercard co-brands.", "snb": "Apps, branches, brokers, iPortal."},
        "L4": {"d": 0, "s": "Mastercard only inside the US Consumer Bank.",
               "gap": "UK retail, business banking, the Corporate Bank, wealth and the Investment Bank have no Mastercard role; the US cards mostly do.",
               "neo": "US Consumer Bank cards.", "snb": "UK retail, mortgages, Corporate Bank, wealth, Investment Bank."},
        "L3": {"d": 0, "s": "The engine room is Barclays' own.", "gap": "Fraud models, AI and loyalty are Barclays'; no agentic or scam-scoring role for Mastercard.",
               "neo": "Rewards on the Mastercard cards.", "snb": "Fraud models, AI platform, Avios and Clubcard."},
        "L2": {"d": 1, "s": "Mastercard on US co-brands, Avios and Tesco; Visa on UK debit and Barclaycard.",
               "gap": "Mastercard carries the US co-brands and two UK credit portfolios; Visa carries UK debit and most of Barclaycard; Ubyx and transaction banking are off the networks.",
               "neo": "US co-brands, Avios, Tesco, acceptance.", "snb": "UK debit, Barclaycard, Wyndham and Samsung, transaction banking, Ubyx."},
        "L1": {"d": 0, "s": "The balance sheet and strategy are Barclays'.", "gap": "Nothing in the foundation is Mastercard's.",
               "neo": "None.", "snb": "Capital, ring-fence, heritage, cloud and AI, 2028 plan."},
    },
    "t": {
        "1.1": {"d": 0, "why": "The group's own capital.", "v": [["Balance sheet", "No Mastercard role.", "0", ""]]},
        "1.2": {"d": 0, "why": "The legal entities and leadership.", "v": [["Entities", "No Mastercard role.", "0", ""]]},
        "1.3": {"d": 0, "why": "Barclaycard began with BankAmericard, now Visa.", "v": [["Heritage", "Visa since 1966.", "0", ""]]},
        "1.4": {"d": 0, "why": "Cloud and AI partners.", "v": [["Technology", "No Mastercard role.", "0", ""]]},
        "1.5": {"d": 0, "why": "Strategy and deals.", "v": [["Group agreement", "None public.", "u", ""]]},
        "2.1": {"d": 0, "why": "UK debit is Visa.", "v": [["Debit", "Visa.", "0", ""]]},
        "2.2": {"d": 1, "why": "Avios and Tesco on Mastercard; the rest of Barclaycard on Visa.", "v": [
            ["Avios", "Mastercard.", "", ""], ["Tesco Bank", "Mastercard ⚠.", "u", ""], ["Platinum, Rewards", "Visa.", "0", ""]]},
        "2.3": {"d": 2, "why": "Most US co-brands are Mastercard.", "v": [
            ["JetBlue, Emirates, Frontier, GM", "Mastercard.", "", ""], ["Wyndham, Samsung", "Visa.", "0", ""], ["AAdvantage", "Gone to Citi.", "0", ""]]},
        "2.4": {"d": 1, "why": "Barclaycard Payments accepts every network.", "v": [["Acceptance", "All networks.", "", ""], ["Ethoca, Click to Pay", "Not announced.", "u", ""]]},
        "2.5": {"d": None, "why": "Commercial-card network not stated.", "v": [["Commercial cards", "Not verified.", "u", ""]]},
        "2.6": {"d": 0, "why": "Ubyx is off the card networks.", "v": [["Ubyx", "No Mastercard role.", "0", ""]]},
        "3.1": {"d": 0, "why": "Barclays' own fraud models.", "v": [["Consumer Fraud Risk", "Not named as a user.", "u", ""]]},
        "3.2": {"d": 0, "why": "Barclays' own AI.", "v": [["AI", "No Mastercard role.", "0", ""]]},
        "3.3": {"d": 1, "why": "Rewards on the Mastercard Avios and Tesco cards.", "v": [["Avios", "On Mastercard.", "", ""]]},
        "3.4": {"d": 0, "why": "No agentic network chosen.", "v": [["Agent Pay", "Not announced.", "0", ""]]},
        "4.1": {"d": 0, "why": "UK retail comes with Visa debit.", "v": [["Retail", "Visa debit.", "0", ""], ["GoHenry", "Not verified.", "u", ""]]},
        "4.2": {"d": 0, "why": "Business banking.", "v": [["Business debit", "Visa ⚠.", "0", ""]]},
        "4.3": {"d": 0, "why": "The Corporate Bank.", "v": [["Corporate", "No Mastercard role.", "0", ""]]},
        "4.4": {"d": 0, "why": "Wealth.", "v": [["Wealth", "No Mastercard role.", "0", ""]]},
        "4.5": {"d": 0, "why": "The Investment Bank.", "v": [["Markets", "No Mastercard role.", "0", ""]]},
        "4.6": {"d": 1, "why": "Most US cards Mastercard; Best Egg and savings not.", "v": [["US cards", "Mostly Mastercard.", "", ""], ["Best Egg", "No Mastercard role.", "0", ""]]},
        "5.1": {"d": 0, "why": "The apps.", "v": [["Apps", "No Mastercard role.", "0", ""]]},
        "5.2": {"d": 0, "why": "Branches.", "v": [["Branches", "No Mastercard role.", "0", ""]]},
        "5.3": {"d": 1, "why": "Several partner cards are Mastercard.", "v": [["Partners", "Mixed networks.", "", ""]]},
        "5.4": {"d": 0, "why": "Broker and corporate portals.", "v": [["Portals", "No Mastercard role.", "0", ""]]},
    },
}
