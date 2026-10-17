"""Synchrony's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

SUB = ("America's largest private-label card issuer as five discs that stack into one platform, from $102 billion of "
       "receivables and partner agreements running to 2035 at the bottom to the tills and apps of Amazon, Lowe's, Walmart "
       "and 290,000 care providers at the top. Click the stack to open it. Choose who you are and what you want to do, and "
       "the areas that deliver it light up across the layers, joined in the order they act. Switch to the Mastercard lens "
       "to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Shoppers", "user-round"),
    ("home", "Homeowners & drivers", "house"),
    ("health", "Patients & pet owners", "shield-check"),
    ("save", "Savers", "coins"),
    ("sme", "Small businesses & pros", "briefcase"),
    ("partner", "Retail & health partners", "store"),
    ("fin", "Platforms & fintechs", "code-xml"),
    ("corp", "Investors & regulators", "landmark"),
]
USERS_DESC = ("Eight kinds of user around 68 million active accounts: shoppers at hundreds of partners, homeowners and "
              "drivers, patients and pet owners, savers with $83 billion on deposit, small businesses and pros, the "
              "partners themselves, the platforms Synchrony embeds in, and its investors and regulators.")

WHO = {
    "con": "A shopper", "home": "A homeowner", "health": "A patient", "save": "A saver", "sme": "A contractor",
    "partner": "A retail partner", "fin": "A platform", "corp": "An investor",
}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "shop", "who": "con", "name": "Get credit at the checkout",
     "why": "The core loop: apply at the partner, get an answer in seconds, and pay over time or in four.",
     "steps": [("5.1", "pos", "Apply at the till or online"), ("3.1", "underwriting", "Get an instant decision"),
               ("2.1", "privatelabel", "Use a store card"), ("2.3", "paylater", "Or Pay in 4"),
               ("3.3", "loyalty", "Earn the partner's rewards")]},
    {"id": "walmart", "who": "con", "name": "Shop Walmart with OnePay",
     "why": "Synchrony's newest flagship: the Walmart card back in the OnePay app, on Mastercard.",
     "steps": [("5.2", "apps", "Apply in the OnePay app"), ("2.2", "onepay", "Get the OnePay CashRewards Mastercard"),
               ("2.5", "wallets", "Tap it from the wallet"), ("4.3", "sams", "Use Sam's Club too")]},
    {"id": "home", "who": "home", "name": "Furnish or fix a home",
     "why": "Lowe's, furniture and flooring, financed by promotion, with the next lender ready if Synchrony says no.",
     "steps": [("4.2", "lowes", "Shop Lowe's"), ("4.2", "homeauto", "Furnish with Ashley or Bob's"),
               ("2.3", "instalment", "Take a deferred-interest promotion"), ("3.1", "versatile", "Or the next lender via Versatile")]},
    {"id": "care", "who": "health", "name": "Pay for care",
     "why": "CareCredit at 290,000 providers, from dentists to vets, with pet insurance paid straight to the card.",
     "steps": [("5.3", "providers", "Apply at the dentist or vet"), ("2.4", "ccnetwork", "Pay with CareCredit"),
               ("4.4", "carecredit", "Or the CareCredit Rewards Mastercard"), ("4.4", "walgreens", "Get pet insurance reimbursed")]},
    {"id": "save", "who": "save", "name": "Save with Synchrony Bank",
     "why": "The deposits that fund 83% of the book.",
     "steps": [("4.6", "deposits", "Open a high-yield savings account"), ("4.6", "premier", "Add the Premier Mastercard")]},
    {"id": "pro", "who": "sme", "name": "Buy for the business",
     "why": "Commercial cards for Lowe's pros and Sam's Club members.",
     "steps": [("4.2", "lowes", "Use the Lowe's Pro card"), ("2.2", "visaamex", "On American Express"),
               ("4.3", "sams", "Or Sam's Club business cards")]},
    {"id": "partner", "who": "partner", "name": "Run a card programme as a partner",
     "why": "What a retailer gets: a card, underwriting, loyalty run for it, and a share of the economics.",
     "steps": [("1.5", "partners", "Sign a ten-year agreement"), ("2.2", "mcdual", "Choose private label, Dual or co-brand"),
               ("3.1", "underwriting", "Let Synchrony decide"), ("3.3", "loyalty", "Run loyalty"), ("3.3", "rsa", "Share the economics")]},
    {"id": "embed", "who": "fin", "name": "Embed Synchrony credit",
     "why": "Credit inside someone else's software: OnePay, Clover, Vetspire and Dental Intelligence.",
     "steps": [("3.5", "embedded", "Embed the application"), ("3.1", "versatile", "Add a lender waterfall"),
               ("3.4", "agentic", "Get ready for agents")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Mastercard carries most of Synchrony's named general-purpose programmes, signed one by one.",
     "steps": [("2.2", "mcdual", "Most Dual and co-brand cards"), ("2.2", "onepay", "OnePay for Walmart"),
               ("4.1", "paypal", "The PayPal Cashback Mastercard"), ("4.3", "sams", "The Sam's Club Mastercard"),
               ("4.4", "carecredit", "CareCredit Rewards"), ("4.5", "lifestyle", "J.Crew"), ("3.4", "agentic", "Agentic pilots")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, tokens and fraud tools could land",
     "why": "Where Synchrony has needs and Mastercard is not yet in: agent payments, tokens for private label, fraud at instant credit, instalments, loyalty costs, and the programmes on Visa and Amex.",
     "steps": [("3.4", "agentic", "Agent Pay at scale"), ("2.5", "wallets", "Tokens and Click to Pay for private label"),
               ("3.2", "fraud", "Identity and fraud at instant credit"), ("2.3", "paylater", "Pay Later on Mastercard Installments"),
               ("3.3", "loyalty", "Merchant-funded offers"), ("2.2", "visaamex", "Venmo, Verizon and Lowe's Pro at renewal")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Synchrony's map",
    "title": "Mastercard on the co-brands, private label off-network",
    "lead": "Synchrony chooses a network programme by programme, and most of its named Dual and co-brand cards (PayPal, Sam's Club, Walmart through OnePay, Walgreens, J.Crew, Virgin Red, CareCredit Rewards) run on Mastercard. Visa has Venmo and Verizon, and Amex arrived with Lowe's Pro in 2026. About two-thirds of the book is private label and instalment credit that uses no network at all. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Synchrony's own (2Q26 results, 21 July 2026; FY2025 10-K) or come from partner card pages and press releases. No enterprise network agreement with Mastercard or Visa is public.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Co-brand book", "$35.7bn, +25%", "34% of receivables; most named programmes on Mastercard"],
        ["Private label", "About two-thirds", "With instalments; no network"],
        ["Newest flagship", "OnePay / Walmart", "Mastercard, live September 2025"],
        ["Visa", "Venmo, Verizon", "Synchrony also holds Visa Class B shares"],
        ["Amex", "Lowe's Pro", "Commercial co-brand, April 2026"],
        ["Agentic", "Testing", "With Mastercard, Visa and Google"],
        ["Pay Later", "Synchrony's own", "Single-use virtual cards"],
        ["Credit", "NCO 5.43%", "Operational losses rising"],
    ],
    "sides": {
        "neo": {"dir": "Most of the Dual and co-brand cards, the tokens behind them in wallets, and a seat in Synchrony's agentic pilots.",
                "deals": "What it does not do: private label, Pay Later, CareCredit's network, fraud, loyalty, or the Visa and Amex programmes."},
        "snb": {"dir": "Private-label and instalment credit, Synchrony's own tokens, CareCredit and Car Care networks, Venmo and Verizon on Visa, Lowe's Pro on Amex, and the deposits.",
                "deals": "Where they meet: every co-brand renewal, and the move to agentic payments."},
    },
    "tl": [
        ["2018", "Belk Rewards Mastercard"],
        ["Jan 2021", "Walgreens, Synchrony and Mastercard"],
        ["Nov 2023", "J.Crew co-brand on Mastercard"],
        ["May 2024", "Virgin Red World Elite Mastercard"],
        ["Jan 2025", "Sam's Club renewed"],
        ["Jun 2025", "OnePay and Walmart, powered by Mastercard"],
        ["Oct 2025", "Agent-pay frameworks with Mastercard and Visa"],
        ["Apr 2026", "Lowe's Pro on American Express"],
        ["Aug 2026", "Agentic payments 'still in testing'"],
    ],
    "l": {
        "U": {"d": 1, "s": "Co-brand holders carry Mastercard; most customers carry a store card.",
              "gap": "Mastercard reaches the shoppers with a Dual or co-brand card; private-label holders, CareCredit patients, savers and Lowe's pros do not touch it.",
              "neo": "PayPal, Walmart, Sam's, Walgreens and J.Crew cardholders.", "snb": "Store-card holders, CareCredit patients, savers, Venmo and Verizon holders."},
        "L5": {"d": 0, "s": "The front doors are the partners'.", "gap": "Applications happen at partner tills, in partner apps and at care providers.",
               "neo": "None.", "snb": "Partner checkouts, OnePay, providers, dealers."},
        "L4": {"d": 1, "s": "Mastercard inside many programmes, none wholly.",
               "gap": "Each platform mixes private label with co-brands; Mastercard is the network on PayPal, Sam's, Walgreens, CareCredit Rewards, J.Crew and Premier.",
               "neo": "PayPal Cashback, Sam's, Walgreens, J.Crew, CareCredit Rewards, Premier.", "snb": "Amazon, Lowe's, CareCredit, deposits."},
        "L3": {"d": 0, "s": "The engine room is Synchrony's own.", "gap": "Underwriting, fraud, loyalty and embedded finance are Synchrony's; Mastercard is one of three agentic partners.",
               "neo": "Agentic pilots.", "snb": "Underwriting, Versatile, fraud models, loyalty, embedded finance."},
        "L2": {"d": 1, "s": "Co-brands on Mastercard; private label off-network.",
               "gap": "Mastercard carries most co-brands; Visa and Amex a few; private label, Pay Later and CareCredit use no network.",
               "neo": "Dual and co-brand cards, tokens.", "snb": "Private label, Pay Later, CareCredit, Car Care, Venmo, Verizon, Lowe's Pro."},
        "L1": {"d": 0, "s": "The balance sheet and partner contracts are Synchrony's.", "gap": "Nothing in the foundation is Mastercard's.",
               "neo": "None.", "snb": "Capital, charter, partners, technology."},
    },
    "t": {
        "1.1": {"d": 0, "why": "Synchrony's own capital.", "v": [["Balance sheet", "No Mastercard role.", "0", ""]]},
        "1.2": {"d": 0, "why": "The charter and leadership.", "v": [["Charter", "No Mastercard role.", "0", ""]]},
        "1.3": {"d": 0, "why": "GE heritage.", "v": [["Heritage", "No Mastercard role.", "0", ""]]},
        "1.4": {"d": 0, "why": "Synchrony's own technology and tokens.", "v": [["Tokenisation", "Synchrony's own.", "0", ""]]},
        "1.5": {"d": 0, "why": "Partner contracts; networks chosen programme by programme.", "v": [["Enterprise network deal", "None public.", "u", ""]]},
        "2.1": {"d": 0, "why": "Private label uses no network.", "v": [["Store cards", "Closed loop.", "0", ""]]},
        "2.2": {"d": 2, "why": "Most named Dual and co-brand programmes are Mastercard.", "v": [
            ["Mastercard programmes", "PayPal, Sam's, OnePay, Walgreens, J.Crew, Virgin Red, Belk.", "", ""], ["Visa", "Venmo, Verizon.", "0", ""], ["Amex", "Lowe's Pro.", "0", ""]]},
        "2.3": {"d": 0, "why": "Pay Later runs on Synchrony's own virtual cards.", "v": [["Mastercard Installments", "Not used.", "0", ""]]},
        "2.4": {"d": 0, "why": "CareCredit, Car Care and HOME are Synchrony's networks.", "v": [["CareCredit", "Own network.", "0", ""]]},
        "2.5": {"d": 1, "why": "Mastercard tokens on the Mastercard cards; Synchrony's own for private label.", "v": [["Network tokens", "On co-brands.", "", ""], ["Click to Pay", "Not announced.", "u", ""]]},
        "3.1": {"d": 0, "why": "Synchrony's own underwriting.", "v": [["Decisions", "No Mastercard role.", "0", ""]]},
        "3.2": {"d": 0, "why": "Synchrony's own fraud models.", "v": [["Fraud tools", "None announced.", "u", ""]]},
        "3.3": {"d": 0, "why": "Loyalty is run for partners by Synchrony.", "v": [["Offers", "Not used.", "0", ""]]},
        "3.4": {"d": 1, "why": "Mastercard is one of three agentic partners.", "v": [["Agent Pay", "Frameworks and pilots.", "", ""]]},
        "3.5": {"d": 0, "why": "Embedded finance is Synchrony's.", "v": [["Embedded", "No Mastercard role.", "0", ""]]},
        "4.1": {"d": 1, "why": "PayPal Cashback and Virgin Red are Mastercard; Amazon is private label.", "v": [["PayPal Cashback", "Mastercard.", "", ""], ["Venmo", "Visa.", "0", ""]]},
        "4.2": {"d": 0, "why": "Lowe's is private label and Amex.", "v": [["Lowe's", "Private label, Amex.", "0", ""]]},
        "4.3": {"d": 1, "why": "Sam's, OnePay and Belk are Mastercard; TJX likely.", "v": [["Sam's Club", "Mastercard.", "", ""], ["TJX", "Not verified.", "u", ""]]},
        "4.4": {"d": 1, "why": "CareCredit Rewards and myWalgreens are Mastercard; CareCredit itself is closed.", "v": [["CareCredit Rewards", "Mastercard.", "", ""]]},
        "4.5": {"d": 1, "why": "J.Crew is Mastercard.", "v": [["J.Crew", "Mastercard.", "", ""]]},
        "4.6": {"d": 1, "why": "Premier is Mastercard; deposits are not.", "v": [["Premier", "Mastercard.", "", ""], ["Deposits", "No Mastercard role.", "0", ""]]},
        "5.1": {"d": 0, "why": "Partner checkouts.", "v": [["Checkouts", "No Mastercard role.", "0", ""]]},
        "5.2": {"d": 0, "why": "Apps and wallets.", "v": [["Apps", "No Mastercard role.", "0", ""]]},
        "5.3": {"d": 0, "why": "Providers and dealers.", "v": [["Providers", "No Mastercard role.", "0", ""]]},
        "5.4": {"d": 0, "why": "Synchrony's service.", "v": [["Service", "No Mastercard role.", "0", ""]]},
    },
}
