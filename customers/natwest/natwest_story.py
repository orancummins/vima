"""NatWest Group's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

SUB = ("The UK's largest bank for business as five discs that stack into one platform, from a £745 billion balance sheet "
       "and three centuries of Coutts and the Royal Bank of Scotland at the bottom to apps used by 11.4 million people at "
       "the top. Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it "
       "light up across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard "
       "goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("young", "Children & young people", "graduation-cap"),
    ("home", "Homebuyers", "house"),
    ("aff", "Premier, Coutts & Evelyn clients", "gem"),
    ("sme", "Small businesses & sole traders", "store"),
    ("corp", "Corporates & institutions", "factory"),
    ("fin", "Fintechs & partners", "code-xml"),
]
USERS_DESC = ("Seven kinds of customer, more than 20 million in all: 19 million in Retail Banking, 2.4 million young "
              "people, Premier, Coutts and Evelyn clients with £131 billion of assets, about 1.5 million businesses and "
              "the fintechs that build on the bank.")

WHO = {
    "con": "A UK customer", "young": "A young customer", "home": "A first-time buyer", "aff": "A private client",
    "sme": "A small business", "corp": "A corporate treasurer", "fin": "A fintech",
}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day on your phone",
     "why": "The everyday loop for 19 million retail customers: an account, a Mastercard debit card, Cora when you need help, and scam scoring on every transfer.",
     "steps": [("4.1", "accounts", "Open a current account"), ("2.1", "mcdebit", "Pay with a Mastercard debit card"),
               ("5.1", "apps", "Run it in the app"), ("3.2", "spendingchat", "Ask Cora where the money went"),
               ("3.1", "cfr", "Transfers scored for scams")]},
    {"id": "young", "who": "young", "name": "Learn money young",
     "why": "Rooster Money for pocket money and chores, then a first account and a Junior ISA.",
     "steps": [("4.1", "youth", "Start with Rooster Money"), ("2.1", "rooster", "Spend with the Rooster Card"),
               ("4.3", "savings", "Save in a Junior ISA"), ("4.1", "accounts", "Open a first account")]},
    {"id": "buy", "who": "home", "name": "Buy a first home",
     "why": "The UK's third-largest mortgage lender: £8.2 billion to first-time buyers in half a year, and a mortgage app inside ChatGPT.",
     "steps": [("4.3", "savings", "Save in an ISA"), ("3.2", "spendingchat", "Explore in ChatGPT"),
               ("4.2", "mortgages", "Take a mortgage"), ("5.2", "branches", "Talk it through in a branch")]},
    {"id": "wealth", "who": "aff", "name": "Grow your wealth",
     "why": "The growth bet: Premier, Coutts and £2.2 billion of Evelyn Partners, £131 billion of client assets.",
     "steps": [("4.1", "accounts", "Bank with Premier"), ("4.4", "coutts", "Move up to Coutts"),
               ("4.4", "evelyn", "Plan with Evelyn Partners"), ("2.2", "credit", "Carry Reward Black"),
               ("3.5", "loyalty", "Collect Reward")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "One in five UK start-ups: Mettle for sole traders, a business account and Mastercard card, Tyl to take payments, Payit to get paid by bank.",
     "steps": [("5.3", "mettle", "Start on Mettle"), ("4.5", "smebank", "Open a business account"),
               ("2.3", "tyl", "Take cards with Tyl"), ("2.4", "payit", "Get paid by bank with Payit"),
               ("3.5", "loyalty", "Save with Business Savings from Mastercard")]},
    {"id": "corp", "who": "corp", "name": "Run a company's money",
     "why": "Commercial & Institutional: lending, Bankline, FX and virtual cards, with a relationship manager.",
     "steps": [("5.4", "rms", "Work with a relationship manager"), ("4.6", "midmarket", "Borrow to grow"),
               ("2.5", "bankline", "Pay on Bankline"), ("2.5", "approval2buy", "Issue virtual cards on Approval2Buy"),
               ("4.7", "markets", "Hedge with NatWest Markets")]},
    {"id": "green", "who": "corp", "name": "Finance the transition",
     "why": "£200 billion of climate and transition finance by 2030, and £10 billion for social housing.",
     "steps": [("4.6", "climatefin", "Raise transition finance"), ("4.6", "midmarket", "Borrow for infrastructure"),
               ("2.5", "approval2buy", "Control spend with virtual cards")]},
    {"id": "fintech", "who": "fin", "name": "Build on NatWest",
     "why": "Payit's open-banking rails, NatWest Boxed for embedded banking, and an accelerator for AI firms.",
     "steps": [("2.4", "payit", "Connect to Payit"), ("3.4", "boxed", "Embed with NatWest Boxed"),
               ("3.4", "agentic", "Follow the agentic principles"), ("1.4", "tech", "Meet the AI partners")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Since 2021 Mastercard has carried the group's 16 million debit cards and most of its credit cards; it scores NatWest's transfers for scams and runs its virtual cards.",
     "steps": [("2.1", "mcdebit", "16 million debit cards since 2021"), ("2.2", "credit", "Most credit cards"),
               ("3.1", "cfr", "Consumer Fraud Risk on transfers"), ("2.5", "approval2buy", "Approval2Buy virtual cards"),
               ("3.5", "loyalty", "Business Savings from Mastercard"), ("5.3", "mettle", "The Mettle card")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, data and open banking could land",
     "why": "Where the bank has needs and Mastercard is not yet in: agentic payments (Visa went first), merchant data for Cora, open-banking payments, the credit cards Visa has taken, and carbon on card spend.",
     "steps": [("3.4", "agentic", "Agent Pay, where Visa went first"), ("3.2", "spendingchat", "Clean merchant data for Cora"),
               ("2.4", "payit", "Open-banking payments and VRPs"), ("2.2", "travelreward", "Win back Travel Reward and Nectar"),
               ("2.3", "tyl", "Acceptance with Tyl"), ("4.6", "climatefin", "A carbon footprint on card spend"),
               ("2.1", "mcdebit", "Renew the 2021 debit agreement")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across NatWest Group's map",
    "title": "A Mastercard bank, with Visa at the edges",
    "lead": "In 2021 NatWest Group moved about 16 million debit cards from Visa to Mastercard, the third-largest debit book in Europe, and most of its credit cards were already Mastercard. Mastercard also scores its transfers for scams and runs its virtual cards. Visa has the Travel Reward card, reportedly the Sainsbury's Nectar cards, the Rooster Card and the first agentic transactions. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (H1 2026 results, 31 July 2026) or come from NatWest, Mastercard, Visa and press reports. The 2021 debit agreement's term is not public.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit cards", "Mastercard, since 2021", "About 16 million personal and business cards, converted from Visa"],
        ["Credit cards", "Mostly Mastercard", "Travel Reward on Visa (2024); Nectar cards reportedly moving to Visa"],
        ["Scams", "Consumer Fraud Risk", "Live since 2023; best of 20 UK firms for scam money received"],
        ["Virtual cards", "Approval2Buy", "Mastercard's mobile virtual card app, November 2024"],
        ["Acquiring", "Tyl", "Built with Pollinate, in which Mastercard invested"],
        ["Open banking", "Payit", "NatWest's own; also on Mastercard's Pay by Bank app (2021)"],
        ["Agentic", "Visa first", "Live on Visa's agentic payments, July 2026; principles name no network"],
        ["AI", "OpenAI", "Cora, Spending Chat and a mortgage app in ChatGPT"],
        ["Youth", "Rooster Card on Visa", "2.4 million young customers"],
    ],
    "sides": {
        "neo": {"dir": "Every debit card in the group, most of the credit cards, scam scoring on transfers, virtual cards for companies and merchant savings for businesses.",
                "deals": "What it does not do: agentic payments, open-banking payments, Cora's data, acquiring itself, or the Visa credit and youth cards."},
        "snb": {"dir": "Visa on Travel Reward, Nectar and Rooster; Payit and Faster Payments; OpenAI behind Cora; the bank's own lending, wealth and markets.",
                "deals": "Where they meet: the cards, the scam scores, and the wallets that hold the cards."},
    },
    "tl": [
        ["2019", "Tyl launched with Pollinate; Mastercard and RBS invest in Pollinate"],
        ["Feb 2021", "16 million debit cards to move from Visa to Mastercard"],
        ["Aug 2021", "NatWest joins Mastercard's Pay by Bank app"],
        ["2023", "Consumer Fraud Risk live on transfers"],
        ["Aug 2024", "Travel Reward credit card on Visa"],
        ["Nov 2024", "Approval2Buy virtual cards on Mastercard"],
        ["2025", "Sainsbury's Bank cards bought; reportedly to Visa"],
        ["Jul 2026", "NatWest live on Visa's agentic payments"],
        ["Sep 2026", "Principles for trusted agentic commerce, no network named"],
    ],
    "l": {
        "U": {"d": 2, "s": "Almost every customer carries a Mastercard.",
              "gap": "Every current-account customer, personal or business, has a Mastercard debit card; young customers on Rooster and Travel Reward holders carry Visa.",
              "neo": "Debit-card holders, most credit-card holders, Mettle and business customers.", "snb": "Rooster Card users, Travel Reward and Nectar holders."},
        "L5": {"d": 0, "s": "The front doors are the bank's.", "gap": "Apps, branches, relationship managers and the niche brands are the bank's own; Mettle's card is Mastercard.",
               "neo": "The Mettle card.", "snb": "Apps, branches, relationship managers, Holt's, Isle of Man Bank."},
        "L4": {"d": 1, "s": "Accounts come with Mastercard; lending and wealth do not.",
               "gap": "Current and business accounts carry Mastercard debit, and Coutts' Silk card is Mastercard; mortgages, savings, Evelyn and markets have no network role.",
               "neo": "Current accounts, business accounts, Coutts Silk.", "snb": "Mortgages, savings, Evelyn, corporate lending, markets."},
        "L3": {"d": 1, "s": "Mastercard scores scams and saves businesses money; AI and agents are elsewhere.",
               "gap": "Consumer Fraud Risk and Business Savings are Mastercard's; Cora runs on OpenAI, and the first agentic payments were Visa's.",
               "neo": "Consumer Fraud Risk, Business Savings from Mastercard.", "snb": "Cora and OpenAI, colleague AI, Visa agentic, NatWest Boxed."},
        "L2": {"d": 2, "s": "Debit and most credit on Mastercard; open banking is the bank's.",
               "gap": "Mastercard carries debit, most credit and the virtual cards; Visa has Travel Reward and Rooster; Payit and Bankline are the bank's.",
               "neo": "Debit, credit, Approval2Buy, acceptance through Tyl.", "snb": "Travel Reward, Rooster Card, Payit, Bankline, FX."},
        "L1": {"d": 0, "s": "The balance sheet and strategy are the bank's.", "gap": "Nothing in the foundation is Mastercard's.",
               "neo": "None.", "snb": "Capital, ownership, brands, OpenAI and AWS, 2028 targets."},
    },
    "t": {
        "1.1": {"d": 0, "why": "The bank's own capital.", "v": [["Balance sheet", "No Mastercard role.", "0", ""]]},
        "1.2": {"d": 0, "why": "The bank's board and shareholders.", "v": [["Ownership", "No Mastercard role.", "0", ""]]},
        "1.3": {"d": 0, "why": "The bank's heritage and brands.", "v": [["Brands", "No Mastercard role.", "0", ""]]},
        "1.4": {"d": 0, "why": "OpenAI, AWS, Accenture and Google.", "v": [["Technology", "No Mastercard role.", "0", ""]]},
        "1.5": {"d": 0, "why": "The 2028 targets say nothing about networks.", "v": [["Strategy", "No Mastercard role.", "0", ""]]},
        "2.1": {"d": 2, "why": "Every debit card has been Mastercard since 2021; only the Rooster Card is Visa.", "v": [
            ["Debit cards", "About 16 million.", "", ""], ["Rooster Card", "Visa prepaid.", "0", ""]]},
        "2.2": {"d": 2, "why": "The core credit range is Mastercard; Travel Reward and Nectar are Visa.", "v": [
            ["Core credit cards", "Mastercard.", "", ""], ["Travel Reward", "Visa, 2024.", "0", ""], ["Nectar cards", "Reportedly moving to Visa.", "u", ""]]},
        "2.3": {"d": 1, "why": "Tyl accepts Mastercard and was built with Pollinate, which Mastercard backed.", "v": [["Tyl", "Accepts all networks.", "", ""]]},
        "2.4": {"d": 0, "why": "Payit is the bank's own account-to-account rail.", "v": [["Payit", "No card network.", "0", ""], ["Pay by Bank app", "Joined 2021.", "u", ""]]},
        "2.5": {"d": 1, "why": "Approval2Buy runs on Mastercard; Bankline and FX are the bank's.", "v": [
            ["Approval2Buy", "Mastercard's virtual card app.", "", ""], ["Bankline", "No Mastercard role.", "0", ""]]},
        "3.1": {"d": 3, "why": "Consumer Fraud Risk is Mastercard's own product.", "v": [["Consumer Fraud Risk", "Since 2023.", "", ""]]},
        "3.2": {"d": 0, "why": "Cora runs on OpenAI models.", "v": [["Cora", "No Mastercard role.", "0", ""]]},
        "3.3": {"d": 0, "why": "Colleague AI is the bank's.", "v": [["AI at work", "No Mastercard role.", "0", ""]]},
        "3.4": {"d": 0, "why": "The first agentic payments were Visa's; the principles name no network.", "v": [["Agent Pay", "Not announced.", "0", ""]]},
        "3.5": {"d": 2, "why": "Business Savings from Mastercard for business cardholders.", "v": [["Business Savings", "Mastercard.", "", ""]]},
        "4.1": {"d": 2, "why": "Current accounts come with Mastercard debit.", "v": [["Debit", "Mastercard.", "", ""]]},
        "4.2": {"d": 0, "why": "Mortgages.", "v": [["Mortgages", "No Mastercard role.", "0", ""]]},
        "4.3": {"d": 0, "why": "Savings and investing.", "v": [["Savings", "No Mastercard role.", "0", ""]]},
        "4.4": {"d": 1, "why": "Coutts' Silk card is Mastercard; Evelyn is not.", "v": [["Coutts Silk", "Mastercard.", "", ""], ["Evelyn", "No Mastercard role.", "0", ""]]},
        "4.5": {"d": 2, "why": "Business accounts come with Mastercard debit.", "v": [["Business debit", "Mastercard.", "", ""]]},
        "4.6": {"d": 1, "why": "Commercial virtual cards are Mastercard; the lending is the bank's.", "v": [["Virtual cards", "See 2.5.", "", ""], ["Carbon on card spend", "Not offered.", "0", ""]]},
        "4.7": {"d": 0, "why": "Markets and offshore banking.", "v": [["Markets", "No Mastercard role.", "0", ""]]},
        "5.1": {"d": 0, "why": "The bank's own apps.", "v": [["Apps", "No Mastercard role.", "0", ""]]},
        "5.2": {"d": 0, "why": "Branches.", "v": [["Branches", "No Mastercard role.", "0", ""]]},
        "5.3": {"d": 2, "why": "Mettle's card is Mastercard.", "v": [["Mettle card", "Mastercard.", "", ""]]},
        "5.4": {"d": 0, "why": "Relationship managers.", "v": [["Relationship managers", "No Mastercard role.", "0", ""]]},
        "5.5": {"d": 0, "why": "Niche brands.", "v": [["Niche brands", "Not verified.", "u", ""]]},
    },
}
