"""Block's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from block_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Square, Cash App and Afterpay as five discs that stack into one platform, from $10.4 billion of gross profit "
       "and its own Utah bank at the bottom to the Cash App and Square apps, hardware and partners at the top. Click the "
       "stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the "
       "layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("seller", "Square sellers", "store"),
    ("chain", "Restaurant & retail chains", "building-2"),
    ("con", "Cash App customers", "user-round"),
    ("shop", "Afterpay shoppers", "hand-coins"),
    ("btc", "Bitcoiners", "coins"),
    ("dev", "Developers & builders", "code-xml"),
]
USERS_DESC = ("Six kinds of user: more than 4.5 million Square sellers, the restaurant and retail chains Square now sells "
              "to through field sales and ISOs, Cash App's 59 million monthly actives, Afterpay shoppers in five "
              "countries, bitcoin users and miners, and the developers building on Block's tools.")

WHO = {"seller": "A Square seller", "chain": "A restaurant chain", "con": "A Cash App customer", "shop": "An Afterpay shopper",
       "btc": "A bitcoiner", "dev": "A developer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "sell", "who": "seller", "name": "Take payments and get paid",
     "why": "The seller loop: Square hardware, every card network, money in Square Checking and a Mastercard debit card.",
     "steps": [("5.2", "hardware", "Set up Square hardware"), ("2.1", "acquiring", "Take any card"), ("2.5", "instant", "Get paid instantly"),
               ("4.2", "sqbanking", "Hold it in Square Checking"), ("2.2", "sqdebit", "Spend with the Square Debit Card")]},
    {"id": "grow", "who": "seller", "name": "Borrow and grow",
     "why": "Square Loans repaid from sales, the Amex credit card, Managerbot and Neighborhoods customers.",
     "steps": [("4.2", "sqloans", "Take a Square Loan"), ("2.2", "sqcredit", "Use the Square Credit Card"),
               ("3.3", "managerbot", "Let Managerbot run the back office"), ("3.4", "neighborhoods", "Win Cash App customers through Neighborhoods")]},
    {"id": "chain", "who": "chain", "name": "Run a chain on Square",
     "why": "Field sales and ISOs bring larger sellers; the Kiosk, partners and AI assistants bring orders.",
     "steps": [("5.3", "iso", "Sign through field sales"), ("4.1", "software", "Run every site on Square"), ("5.2", "hardware", "Add Square Kiosk"),
               ("5.3", "partners", "Take Uber Eats orders in Square"), ("3.5", "agentic", "Sell inside ChatGPT and Claude")]},
    {"id": "bank", "who": "con", "name": "Bank with Cash App",
     "why": "Paycheck in, Visa card out, Moneybot and Borrow when money runs short.",
     "steps": [("5.1", "apps", "Open Cash App"), ("4.3", "cashbanking", "Get paid into Cash App"), ("2.3", "cashcard", "Spend on the Cash App Card"),
               ("3.3", "moneybot", "Ask Moneybot"), ("4.4", "borrow", "Borrow a little")]},
    {"id": "send", "who": "con", "name": "Send and spend without a card",
     "why": "P2P, Cash App Pay at Uber and local cash at Square sellers.",
     "steps": [("2.5", "p2p", "Send money to friends"), ("2.6", "cashapppay", "Pay Uber with Cash App Pay"), ("3.4", "neighborhoods", "Earn local cash at a Square seller"),
               ("3.4", "green", "Unlock Cash App Green")]},
    {"id": "bnpl", "who": "shop", "name": "Pay later with Afterpay",
     "why": "Pay in 4 online, then on the Cash App Card in store.",
     "steps": [("2.4", "afterpay", "Pay in 4 with Afterpay"), ("2.4", "flex", "Use Afterpay on the Cash App Card"), ("3.2", "score", "Build a Cash App Score")]},
    {"id": "bitcoin", "who": "btc", "name": "Live on bitcoin",
     "why": "Buy and spend bitcoin, keep it safe, mine it.",
     "steps": [("2.6", "cashbitcoin", "Buy bitcoin in Cash App"), ("2.1", "sqbitcoin", "Pay a Square seller in bitcoin"), ("4.5", "proto", "Hold it in Bitkey, mine with Proto")]},
    {"id": "build", "who": "dev", "name": "Build with Block's agents",
     "why": "goose, Builderbot and Buzz, and Square's agentic channels.",
     "steps": [("3.3", "goose", "Build with goose"), ("3.5", "agentic", "Reach shoppers in AI assistants")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The Square Debit Card, acceptance across Square, instant transfers to Mastercard debit cards, and Afterpay repayments.",
     "steps": [("2.2", "sqdebit", "Square Debit Card on Mastercard"), ("4.2", "sqbanking", "Square Checking's card"),
               ("2.1", "acquiring", "Accepted by every Square seller"), ("2.5", "instant", "Instant transfers to Mastercard debit"),
               ("2.4", "afterpay", "Afterpay repaid on Mastercard cards")]},
    {"id": "mcnext", "who": "mc", "name": "Where payouts, agents and instalments could land",
     "why": "Where Block has needs and Mastercard is not yet in: Move for instant payouts, acquirer risk for the ISO channel, Agent Pay for Square's agentic channels, instalments against Visa Flex, dispute tools after the CFPB order, and stablecoin settlement.",
     "steps": [("2.5", "instant", "Mastercard Move for payouts"), ("5.3", "iso", "Merchant screening for ISO sellers"),
               ("3.5", "agentic", "Agent Pay for ChatGPT and Claude orders"), ("2.4", "flex", "Instalments against Visa Flex"),
               ("3.1", "fraud", "Disputes and scam tools"), ("2.6", "cashbitcoin", "Stablecoin settlement")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Block's map",
    "title": "Mastercard on the seller's card, Visa in the Cash App wallet",
    "lead": "Mastercard runs the Square Debit Card, is accepted by every Square seller and is one of the two debit networks Block pushes instant transfers to. Visa holds Block's biggest card, the Cash App Card with 26 million monthly actives, and the Afterpay Flex pilot on it. American Express holds the Square Credit Card. Block's own plan moves spending onto Cash App balances, Neighborhoods, bitcoin and USDC, away from every network. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Block's own (Q2 2026 letter, 5 August 2026; FY2025 10-K) or come from Square, Cash App, Afterpay and press. Block does not publish a network split, and no public scheme agreement was found.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Square Debit Card", "Mastercard", "Sutton Bank, since January 2019"],
        ["Cash App Card", "Visa", "26m monthly actives (Q3 2025)"],
        ["Square Credit Card", "American Express", "Celtic Bank"],
        ["Afterpay on card", "Visa Flex pilot", "November 2025"],
        ["Acceptance", "Every network", "$250bn Square GPV in 2025"],
        ["Instant transfers", "OCT to both", "Send or Move not named ⚠"],
        ["Own rails", "Cash App Pay, Neighborhoods", "Plus bitcoin and USDC"],
        ["Agentic", "UCP", "No Agent Pay link found"],
    ],
    "sides": {
        "neo": {"dir": "The Square Debit Card and Square Checking, acceptance across Square, instant transfers to Mastercard debit cards and Afterpay repayments.",
                "deals": "What it does not do: the Cash App Card, Afterpay's card products in the US, the Square Credit Card, fraud tools or agentic payments."},
        "snb": {"dir": "Visa on the Cash App Card and the Afterpay Flex pilot, American Express on the Square Credit Card, and Block's own closed loop: Cash App Pay, Neighborhoods, bitcoin and USDC.",
                "deals": "Where they meet: every Square payment, and the push of funds to debit cards."},
    },
    "tl": [
        ["Jan 2019", "Square Debit Card launched on Mastercard"],
        ["2021", "Afterpay card in Australia on Mastercard or eftpos ⚠"],
        ["Aug 2023", "Marqeta renews Cash App Card processing"],
        ["Jan 2025", "CFPB order on Cash App fraud"],
        ["Mar 2025", "Borrow moves to Block's own bank"],
        ["Oct 2025", "Square Bitcoin; push to bypass card fees"],
        ["Nov 2025", "Visa Debit Flex pilot for Afterpay"],
        ["Feb 2026", "Workforce cut to under 6,000"],
        ["Jul 2026", "Square in ChatGPT and Claude"],
        ["Sep 2026", "Cash App Score opened to lenders"],
    ],
    "l": {
        "U": {"d": 1, "s": "Sellers carry Mastercard; Cash App customers carry Visa.",
              "gap": "Square sellers spend on a Mastercard debit card and take every card; Cash App's 59 million actives hold a Visa card and are pushed towards balances.",
              "neo": "Square sellers, Afterpay repayers, instant-transfer recipients.", "snb": "Cash App cardholders, Afterpay Flex users, Square credit cardholders."},
        "L5": {"d": 0, "s": "The front doors are Block's.", "gap": "Apps, hardware, ISOs and partners are Block's own; the hardware takes every network.",
               "neo": "None.", "snb": "Cash App, Square apps, Kiosk, Uber, Google, Apple."},
        "L4": {"d": 0, "s": "Business lines run on Block's own bank.", "gap": "Square Checking carries a Mastercard card; Cash App banking and Borrow ride on the Visa card and SFS.",
               "neo": "Square Checking's debit card.", "snb": "Cash App banking, Borrow, loans, bitcoin, TIDAL."},
        "L3": {"d": 0, "s": "Services are Block's own.", "gap": "Fraud, Cash App Score, AI, Neighborhoods and agentic commerce use no Mastercard service found.",
               "neo": "None found.", "snb": "Own fraud models, Nova Credit, UCP, Neighborhoods."},
        "L2": {"d": 1, "s": "Mastercard on seller cards and payouts; Visa on Cash App.", "gap": "Mastercard has the Square Debit Card, acceptance and push to its debit cards; Visa has the Cash App Card and Flex; Block's own rails grow around both.",
               "neo": "Square Debit Card, acceptance, instant transfers.", "snb": "Cash App Card, Afterpay Flex, Amex credit, Cash App Pay, bitcoin, USDC."},
        "L1": {"d": 0, "s": "Block's own scale, bank and strategy.", "gap": "Nothing in the foundation is Mastercard's.",
               "neo": "None.", "snb": "SFS, licences, targets, network strategy."},
    },
    "t": area_lens(LAYERS),
}
