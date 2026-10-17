"""UniCredit Bulbank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from bulbank_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Bulgaria's leading corporate bank as five discs that stack into one platform, from a million customers and "
       "about a quarter of the banking system's profit at the bottom to Bulbank Mobile, branches and remote bankers at "
       "the top. Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it "
       "light up across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep "
       "Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("fam", "Families & young people", "users-round"),
    ("home", "Homebuyers", "house"),
    ("aff", "Private clients", "gem"),
    ("sme", "Small businesses & merchants", "briefcase"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Six kinds of customer, more than a million in all: everyday customers, families with children's cards, "
              "homebuyers, private clients, small businesses and merchants, and the corporates that make Bulbank "
              "Bulgaria's number one corporate lender.")

WHO = {"con": "A Bulbank customer", "fam": "A parent", "home": "A homebuyer", "aff": "A private client",
       "sme": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: a daily-banking plan, a Mastercard debit card in a phone wallet, the app and fraud checks.",
     "steps": [("4.3", "plans", "Open a daily-banking plan"), ("2.1", "debit", "Pay with Debit Mastercard"),
               ("2.3", "wallets", "Tap with Apple Pay or Google Pay"), ("5.1", "app", "Run it in Bulbank Mobile"),
               ("3.1", "fraud", "Protected from fraud")]},
    {"id": "corp", "who": "corp", "name": "Run a company's finances",
     "why": "Bulgaria's largest corporate lender: online banking, loans, payments and trade finance.",
     "steps": [("5.2", "online", "Bank in Bulbank Online"), ("4.1", "corp", "Borrow from the number one corporate lender"),
               ("2.6", "cashmgmt", "Pay in bulk in ISO 20022"), ("4.1", "trade", "Trade and factor receivables")]},
    {"id": "borrow", "who": "con", "name": "Borrow on a card",
     "why": "Mastercard credit cards with instalments and cashback.",
     "steps": [("2.2", "credit", "Take a Shopping Card or Smart Credit"), ("2.2", "instal", "Split a purchase into instalments"),
               ("3.4", "offers", "Earn Mastercard Day cashback")]},
    {"id": "family", "who": "fam", "name": "Give a child a card",
     "why": "Debit Mastercard Kids and Teens with parental controls in the app.",
     "steps": [("4.3", "plans", "Open a plan"), ("2.1", "kids", "Order Debit Mastercard Kids or Teens"), ("5.1", "app", "Set limits in the app")]},
    {"id": "send", "who": "con", "name": "Send money instantly",
     "why": "Blink by phone number at home and SEPA Instant across the euro area.",
     "steps": [("5.1", "app", "Open Bulbank Mobile"), ("2.5", "blink", "Send by Blink to a phone number"), ("2.5", "sepainst", "Pay into Europe by SEPA Instant")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "A mortgage from the Virtual Mortgage Center or a branch, with savings and insurance alongside.",
     "steps": [("5.4", "comfort", "Talk to a remote banker"), ("4.2", "mortgages", "Take a mortgage"), ("4.3", "invest", "Protect and save")]},
    {"id": "private", "who": "aff", "name": "Bank privately",
     "why": "Private banking with Mastercard World Elite and onemarkets funds.",
     "steps": [("4.4", "private", "Join private banking"), ("4.3", "invest", "Invest in onemarkets funds")]},
    {"id": "sme", "who": "sme", "name": "Take payments as a small business",
     "why": "Terminals, e-commerce and peer benchmarks from the bank's own card data.",
     "steps": [("4.5", "smebiz", "Open a business package"), ("2.4", "pos", "Take cards on a POS or phone"),
               ("2.4", "ecom", "Sell online with Pay by Link"), ("3.3", "p2p", "Benchmark shoppers against peers")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Every card the bank issues after the 2024 switch, the wallets they sit in, private-banking World Elite and Mastercard-branded cashback.",
     "steps": [("2.1", "debit", "Debit Mastercard since 2024"), ("2.2", "credit", "Mastercard credit cards"),
               ("2.3", "wallets", "Mastercard tokens in phone wallets"), ("4.4", "private", "Mastercard World Elite"),
               ("3.4", "offers", "Your Mastercard Day cashback")]},
    {"id": "mcnext", "who": "mc", "name": "Where checkout, scams and corporates could land",
     "why": "Where Bulbank has needs and Mastercard is not yet in: Click to Pay and instalments at checkout, scam scores for instant transfers, merchant data, acquiring services, corporate cards and payouts, and agentic payments.",
     "steps": [("2.3", "wallets", "Click to Pay, as at UniCredit Italy"), ("2.2", "instal", "Instalments at online checkout"),
               ("3.1", "fraud", "Scam scores for Blink and SEPA Instant"), ("3.3", "p2p", "Mastercard data in merchant analytics"),
               ("2.4", "pos", "Gateway and risk tools for acquiring"), ("4.1", "corp", "Commercial cards and Mastercard Move"),
               ("3.2", "ai", "Agent Pay for the app assistant")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across UniCredit Bulbank's map",
    "title": "Every card on Mastercard, every instant transfer on BORICA",
    "lead": "Under UniCredit's May 2023 group deal, Bulbank moved its whole card book to Mastercard in 2024. Mastercard paid BGN 28 million of migration support, and the bank spent BGN 4.4 million ending Visa issuing. Debit, credit, children's, digital and World Elite cards are now Mastercard Touch Cards, and Mastercard-branded cashback runs through 2026. Instant payments run on BORICA's Blink and SEPA Instant, whose board includes Bulbank's CEO. Acquiring, fraud, AI and merchant analytics are the bank's own. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (2025 and 2024 Annual Reports) or from the Bulgarian National Bank's bulletin for 30 June 2026. Card counts by network are not published; one legacy Visa debit card is still listed, and business-card networks are not stated.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Mastercard", "Whole book switched in 2024"],
        ["Credit", "Mastercard", "Shopping, Gold and Platinum Smart Credit"],
        ["Visa", "Issuing ended 2024", "BGN 4.4m exit cost; one Visa Gold still listed ⚠"],
        ["Migration support", "BGN 28m", "From Mastercard in 2024, more in 2025"],
        ["Group deal", "UniCredit and Mastercard", "May 2023; 13 banks, about 20m cards"],
        ["Instant payments", "BORICA Blink, SEPA Instant", "Not Mastercard"],
        ["Acquiring", "All schemes", "Merchants up 13.6% in 2025"],
        ["Click to Pay", "Not seen in Bulgaria ⚠", "Live at UniCredit Italy and Romania"],
    ],
    "sides": {
        "neo": {"dir": "Every card the bank issues, the wallet tokens on them, World Elite for private clients, Mastercard-branded cashback, and acceptance at Bulbank's merchants.",
                "deals": "What it does not do: instant transfers, acquiring processing, fraud models, AI or merchant analytics."},
        "snb": {"dir": "BORICA's Blink and SEPA Instant, the bank's own acquiring, fraud, AI and analytics, a legacy Visa debit card, and Revolut and A2A competing for payments.",
                "deals": "Where they meet: checkout, where Blink and cards compete for the same payment."},
    },
    "tl": [
        ["May 2023", "UniCredit–Mastercard group deal covers Bulbank"],
        ["Apr 2024", "Mastercard Touch Cards across UniCredit"],
        ["2024", "Card book moved to Mastercard; Visa issuing ended"],
        ["2024", "Joins Blink P2P; digital debit card"],
        ["Aug 2024", "BGN 100,000 for guide dogs with Mastercard"],
        ["2025", "Mastercard Consumer Card Award; Fitch A-"],
        ["1 Jan 2026", "Euro adoption: cards, POS and ATMs in euro"],
        ["2026", "Your Mastercard Day cashback"],
        ["Jun 2026", "H1 profit €268.7m; third by assets"],
    ],
    "l": {
        "U": {"d": 2, "s": "Cardholders carry Mastercard.", "gap": "Every consumer card is Mastercard; instant-transfer users ride BORICA.",
              "neo": "Debit, credit, children's and private cardholders.", "snb": "Blink and SEPA Instant users, merchants on all schemes, corporates."},
        "L5": {"d": 0, "s": "The front doors are the bank's.", "gap": "App, online banking, branches, ATMs and remote bankers are Bulbank's own.",
               "neo": "None.", "snb": "Bulbank Mobile, Bulbank Online, branches, ATMs, Comfort, agents."},
        "L4": {"d": 1, "s": "Private banking and plans carry Mastercard; lending does not.", "gap": "World Elite and plan debit cards are Mastercard; corporate, mortgage and leasing books have no network role.",
               "neo": "Private banking, daily-banking plans.", "snb": "Corporate lending, mortgages, UCFin, investments, leasing."},
        "L3": {"d": 1, "s": "Cashback is Mastercard's; the rest is the bank's.", "gap": "Mastercard Day and Premium cashback run on Mastercard; fraud, AI and analytics are in-house.",
               "neo": "Mastercard-branded offers.", "snb": "Fraud prevention, identity, AI, merchant analytics."},
        "L2": {"d": 2, "s": "Every card is Mastercard; instant payments are BORICA's.", "gap": "Cards and wallet tokens ride Mastercard after the 2024 switch; Blink, SEPA Instant and corporate payments do not, and acquiring takes all schemes.",
               "neo": "Debit, credit, digital and children's cards, wallet tokens.", "snb": "Blink, SEPA Instant, PSP clearing, legacy Visa Gold."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Capital, ownership, technology and the euro switch are the bank's and the group's.",
               "neo": "None.", "snb": "Capital, UniCredit ownership, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
