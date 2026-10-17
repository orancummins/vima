"""Bank of America's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from bofa_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("America's largest consumer-deposit bank as five discs that stack into one platform, from $2 trillion of deposits and the "
       "bank that started BankAmericard at the bottom to one app for 42.6 million, 3,531 financial centres and CashPro at "
       "the top. Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it "
       "light up across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep "
       "Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("card", "Cardholders & travellers", "credit-card"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Companies & institutions", "factory"),
    ("wealth", "Wealth clients", "gem"),
]
USERS_DESC = ("Five kinds of client, nearly 70 million in all: everyday customers with 38.9 million checking accounts, "
              "cardholders and travellers, about four million small businesses, the companies and institutions Global "
              "Banking and Markets serve, and Merrill and Private Bank clients.")

WHO = {"con": "A Bank of America customer", "card": "A cardholder", "sme": "A small business",
       "corp": "A corporate treasurer", "wealth": "A wealth client"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "A checking account, a debit card, the app, Erica and fraud protection.",
     "steps": [("4.1", "checking", "Open a checking account"), ("2.4", "debit", "Pay with debit"), ("5.1", "app", "Run it in the app"),
               ("3.2", "erica", "Ask Erica"), ("3.1", "mycredit", "Watch my credit")]},
    {"id": "pay", "who": "con", "name": "Pay people and shop online",
     "why": "Zelle, Paze and cards in mobile wallets.",
     "steps": [("2.5", "zelle", "Send money with Zelle"), ("2.5", "paze", "Check out with Paze"), ("2.4", "wallets", "Tap a phone")]},
    {"id": "card", "who": "card", "name": "Earn on a card",
     "why": "The Visa cash-back cards, Custom Pay Plan and BofA Rewards.",
     "steps": [("2.1", "cashrewards", "Take Customized Cash"), ("2.1", "custompay", "Spread a purchase"),
               ("3.4", "bofarewards", "Earn a BofA Rewards bonus"), ("3.4", "bankamerideals", "Add deals")]},
    {"id": "travel", "who": "card", "name": "Travel on a co-brand",
     "why": "Atmos on Visa, the NCL card on Mastercard, and the travel centre.",
     "steps": [("5.3", "partners", "Apply through a partner"), ("2.2", "atmos", "Fly with Atmos"),
               ("2.2", "ncl", "Or cruise with NCL"), ("3.4", "travelcenter", "Book through the Travel Center")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "Business Banking, the Mastercard Business Advantage cards, merchant services and Zelle.",
     "steps": [("4.1", "smallbiz", "Open a business account"), ("2.3", "bizadvantage", "Spend on Business Advantage"),
               ("2.7", "bams", "Take cards with BofA Merchant Services"), ("2.5", "zelle", "Get paid by Zelle")]},
    {"id": "corp", "who": "corp", "name": "Move money as a company",
     "why": "CashPro, real-time and cross-border payments, commercial cards and data.",
     "steps": [("5.3", "platforms", "Log in to CashPro"), ("4.3", "globalbanking", "Bank with Global Banking"),
               ("2.6", "cashpro", "Pay through CashPro"), ("2.6", "rtp", "Pay in real time, across borders"),
               ("2.3", "commercial", "Pay suppliers by card"), ("3.3", "cashproai", "Read Payments Insights")]},
    {"id": "wealth", "who": "wealth", "name": "Grow wealth",
     "why": "Merrill, the Private Bank and AI tools for advisers.",
     "steps": [("4.2", "merrill", "Invest with Merrill"), ("3.2", "ericaassist", "Helped by adviser AI"),
               ("4.2", "privatebank", "Join the Private Bank"), ("3.4", "bofarewards", "Move up the Rewards tiers")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The small-business card line, the NCL card, the BankAmericard ⚠, and acceptance and PIN routing at BofA's merchants.",
     "steps": [("2.3", "bizadvantage", "Business Advantage on Mastercard"), ("2.2", "ncl", "NCL World Mastercard"),
               ("2.1", "bankamericard", "BankAmericard ⚠"), ("2.7", "bams", "Acceptance and Maestro routing")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, stablecoins and B2B could land",
     "why": "Where BofA has needs and Mastercard is not yet in: trust for agentic commerce, scam tools for Zelle and RTP, stablecoins, commercial virtual cards and offers for BofA Rewards.",
     "steps": [("3.3", "agentic", "Agent Pay for agentic commerce"), ("3.1", "security", "Scam and payee-risk tools"),
               ("2.6", "stablecoin", "Stablecoin rails"), ("2.3", "commercial", "Commercial virtual cards"),
               ("3.4", "bankamerideals", "Card-linked offers")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Bank of America's map",
    "title": "Visa's birthplace, with Mastercard on its small-business cards",
    "lead": "Bank of America launched BankAmericard, which became Visa, and its consumer book is still Visa-led: the flagship cash and travel cards, the Atmos and other co-brands, and debit ⚠, with joint FIFA marketing in 2026. Mastercard carries the whole Business Advantage small-business line, the NCL cruise card and, it appears, the BankAmericard ⚠. Zelle and Paze, which BofA co-owns, carry payments and checkout, and instalments, rewards and cross-border payments are built in-house. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (Q3 2026 results, 14 October 2026) or from BofA's newsroom, filings and Investor Day. The Mastercard newsroom could not be reached, so no Mastercard-side confirmation of joint work was possible; some card networks are read from card art and third-party sources.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Consumer credit", "Visa", "Cash, travel and premium cards"],
        ["Co-brands", "Visa, bar one", "Atmos, Royal Caribbean; NCL on Mastercard"],
        ["Small-business cards", "Mastercard", "The whole Business Advantage line"],
        ["BankAmericard", "Mastercard ⚠", "From card art"],
        ["Debit", "Visa ⚠", "Third-party sources"],
        ["Checkout & P2P", "Paze, Zelle", "$556 billion on Zelle in 2025"],
        ["Instalments", "Custom Pay Plan", "Built in-house, June 2026"],
        ["Acquiring", "All networks", "Maestro among PIN routes"],
    ],
    "sides": {
        "neo": {"dir": "Business Advantage cards, the NCL card, the BankAmericard ⚠, and acceptance and Maestro routing at BofA's merchants.",
                "deals": "What it does not do: flagship consumer credit, debit, Zelle, Paze, instalments, rewards or cross-border payments."},
        "snb": {"dir": "Visa consumer credit, co-brands and debit, Zelle and Paze, its own instalments, rewards and real-time payments, and Erica.",
                "deals": "Where they meet: agentic commerce, where BofA is setting principles, and stablecoins, on its roadmap."},
    },
    "tl": [
        ["1958", "BankAmericard launched; Visa spun out in 1976"],
        ["Aug 2007", "BofA–MasterCard pricing deal; NFL debit"],
        ["Jun 2020", "Merchant joint venture unwound"],
        ["Dec 2024", "All eligible cards in Paze"],
        ["Nov 2025", "Investor Day targets"],
        ["Mar 2026", "Visa FIFA sweepstakes"],
        ["Jun 2026", "Custom Pay Plan; cross-border RTP"],
        ["Sep 2026", "Agentic-commerce principles"],
        ["Oct 2026", "$1.2 billion consent orders"],
    ],
    "l": {
        "U": {"d": 1, "s": "Small-business cardholders carry Mastercard.",
              "gap": "Consumer cardholders and debit holders carry Visa; Business Advantage and NCL holders carry Mastercard.",
              "neo": "Small-business and NCL cardholders.", "snb": "Consumer card and debit holders, wealth and corporate clients."},
        "L5": {"d": 1, "s": "One partner card, NCL, is Mastercard.", "gap": "App, financial centres and CashPro are BofA's; partners are on Visa bar NCL.",
               "neo": "NCL.", "snb": "App, financial centres, CashPro, Atmos and other partners."},
        "L4": {"d": 1, "s": "Business Banking carries Mastercard cards.", "gap": "Checking comes with Visa debit ⚠; wealth, Global Banking and Markets have no network role.",
               "neo": "Business Advantage for business owners.", "snb": "Checking, wealth, Global Banking, Markets."},
        "L3": {"d": 0, "s": "Services are BofA's own.", "gap": "Erica, rewards, deals and fraud tools are BofA's; agentic principles name no network.",
               "neo": "None found.", "snb": "Erica, BofA Rewards, Deals, My Credit, CashPro data."},
        "L2": {"d": 1, "s": "Business and cruise cards on Mastercard; the consumer core on Visa.", "gap": "Visa has flagship credit, co-brands and debit; Mastercard has the small-business line; Zelle, Paze and RTP are bank-owned.",
               "neo": "Business Advantage, NCL, BankAmericard ⚠, acceptance.", "snb": "Visa credit and debit, Zelle, Paze, CashPro, RTP."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's; Visa began here.", "neo": "None.", "snb": "Capital, heritage, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
