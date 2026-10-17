"""Al Rajhi Bank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from alrajhi_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("The world's largest Islamic bank as five discs that stack into one platform, from SAR 1,055 billion of assets "
       "at the bottom to the alrajhi app, 513 branches and the urpay wallet at the top. Click the stack to open it. Choose "
       "who you are and what you want to do, and the areas that deliver it light up across the layers, joined in the "
       "order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("expat", "Expatriates & remitters", "globe"),
    ("aff", "Affluent & private clients", "gem"),
    ("home", "Homebuyers & borrowers", "house"),
    ("sme", "SMEs & merchants", "store"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Six kinds of customer, about 22 million in all: everyday customers, expatriates sending money home, "
              "affluent and private clients, homebuyers and borrowers, SMEs and merchants, and large corporates.")

WHO = {"con": "An Al Rajhi customer", "expat": "An expatriate worker", "aff": "A private-banking client",
       "home": "A homebuyer", "sme": "A merchant", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account opened in the app, a mada card, phone wallets, instant transfers and fraud checks.",
     "steps": [("4.2", "accounts", "Open an account in the app"), ("2.1", "madadebit", "Pay with mada"), ("2.7", "wallets", "Tap with a phone wallet"),
               ("2.5", "sarie", "Send money instantly on sarie"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "card", "who": "con", "name": "Spend on an Islamic credit card",
     "why": "A Murabaha-based Visa card, 0% instalments and mokafaa points.",
     "steps": [("5.1", "app", "Apply in the app"), ("2.2", "credit", "Take a Visa credit card"), ("3.4", "tasaheal", "Split purchases at 0%"),
               ("3.3", "mokafaa", "Earn mokafaa points")]},
    {"id": "remit", "who": "expat", "name": "Send money home",
     "why": "The region's largest remittance bank, Visa Direct, and urpay on Mastercard Move.",
     "steps": [("2.7", "urpay", "Open a urpay wallet"), ("2.6", "tahweel", "Send through Tahweel Al Rajhi"), ("2.6", "visadirect", "Pay to a card or account with Visa Direct"),
               ("2.6", "move", "Pay out cash or to a wallet with Mastercard Move")]},
    {"id": "travel", "who": "aff", "name": "Travel and earn miles",
     "why": "Infinite, AlFursan, flynas and Marriott Bonvoy cards, a multi-currency prepaid card and private banking.",
     "steps": [("4.3", "corporate", "Bank privately"), ("2.2", "cobrand", "Earn miles on a co-brand card"), ("2.1", "prepaid", "Carry Travel Plus currencies"),
               ("2.1", "premiumdebit", "Use a premium debit card")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "The Kingdom's largest mortgage lender, with Takaful cover.",
     "steps": [("5.2", "branches", "Visit a branch"), ("4.1", "mortgages", "Take home finance"), ("4.2", "takaful", "Protect it with Takaful")]},
    {"id": "merchant", "who": "sme", "name": "Take payments as a merchant",
     "why": "Al Rajhi POS, online acceptance through four gateways, neoleap services and POS financing.",
     "steps": [("4.3", "sme", "Open an SME account"), ("2.4", "pos", "Take cards on Al Rajhi POS"), ("2.4", "ecom", "Sell online through a gateway"),
               ("2.4", "neoleappay", "Offer Tashaeel instalments"), ("3.3", "mokafaa", "Accept mokafaa points")]},
    {"id": "corp", "who": "corp", "name": "Run treasury as a corporate",
     "why": "Cash management, corporate cards, open banking and the business channels.",
     "steps": [("5.3", "bizapp", "Bank on the business app"), ("4.3", "cashmgmt", "Run payroll and collections"), ("2.3", "corpcards", "Issue corporate cards"),
               ("3.2", "neotek", "Connect through open banking")]},
    {"id": "invest", "who": "aff", "name": "Invest and track money",
     "why": "Al Rajhi Capital and Drahim.",
     "steps": [("4.4", "capital", "Trade with Al Rajhi Capital"), ("3.2", "drahim", "Track and invest with Drahim")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Acceptance on the bank's terminals and online, Mastercard Payment Gateway Services, and Mastercard Move in urpay.",
     "steps": [("2.4", "pos", "Mastercard accepted on Al Rajhi POS"), ("2.4", "ecom", "MPGS for online merchants"),
               ("2.6", "move", "Mastercard Move in urpay"), ("2.7", "urpay", "urpay transfers")]},
    {"id": "mcnext", "who": "mc", "name": "Where cards, wallets and agents could land",
     "why": "Where Al Rajhi has needs and Mastercard is not yet in: a franchise holding 38% of the Kingdom's credit cards on one network, urpay's cards, commercial cards for a fast-growing SME book, scam scoring for instant payments, open finance and Agent Pay for the app.",
     "steps": [("2.2", "credit", "A premium or segment card"), ("2.7", "urpaycards", "urpay cards"), ("2.3", "corpcards", "Commercial and virtual cards"),
               ("3.1", "fraud", "Scam scoring for instant payments"), ("3.2", "neotek", "Open finance with neotek"), ("5.1", "app", "Agent Pay for the app")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Al Rajhi Bank's map",
    "title": "A mada-and-Visa bank where Mastercard works the till",
    "lead": "Every Al Rajhi account card is mada, and every credit, charge, prepaid, co-brand and business card checked carries Visa, which also powers its remittances through Visa Direct and its Asian Cup 2027 sponsorship. Mastercard is accepted across the bank's 43.5% share of POS terminals and online, offers its gateway to the bank's merchants, and has run cross-border transfers in the urpay wallet since June 2024. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (H1 2026 earnings release, 21 July 2026; Integrated Annual Report 2025) or from Al Rajhi's card pages, SAMA and press. No Mastercard-branded card was found on any current Al Rajhi product page; urpay's card network rests on an app listing.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "mada", "Every account card; Visa on premium tiers ⚠"],
        ["Credit", "Visa", "38.4% market share in 2025"],
        ["Business cards", "Visa", "Business and corporate range"],
        ["Acquiring", "All networks", "43.5% of POS terminals"],
        ["Gateway", "MPGS one of four", "With neoleap, Cybersource, Moyasar"],
        ["Remittances", "Visa Direct; Mastercard Move", "Bank 2025 ⚠; urpay June 2024"],
        ["Instant", "sarie", "22.6 million a month"],
        ["Sponsorship", "Visa", "AFC Asian Cup 2027"],
    ],
    "sides": {
        "neo": {"dir": "Acceptance on the bank's terminals and online, MPGS for merchants, and Mastercard Move for urpay transfers.",
                "deals": "What it does not do: issue any Al Rajhi card, carry the bank's own remittances, or run its fraud, data or loyalty."},
        "snb": {"dir": "mada for debit, Visa for every credit, prepaid and business card and for Visa Direct, sarie for instant payments, and the bank's own fraud, AI and mokafaa.",
                "deals": "Where they meet: the POS estate and urpay, where both networks are present."},
    },
    "tl": [
        ["Feb 2019", "Mastercard and mada bring Apple Pay to the Kingdom ⚠"],
        ["2021", "neoleap founded for payments"],
        ["2023", "Visa Direct transfers to cards"],
        ["Jan 2024", "Amex access to 4,500+ Al Rajhi ATMs"],
        ["Jun 2024", "urpay signs with Mastercard Move"],
        ["Dec 2024", "Marriott Bonvoy Visa Infinite card"],
        ["2025", "Multi-year Visa Direct deal ⚠ date; credit share 38.4%"],
        ["Jun 2026", "AFC Asian Cup 2027 partner, through Visa"],
        ["Jul 2026", "Malaysia launches Visa credit cards"],
        ["Sep 2026", "Money20/20 founding partner; neotek's open-banking licence"],
        ["End-2026", "New group strategy due"],
    ],
    "l": {
        "U": {"d": 0, "s": "Customers carry mada and Visa cards.",
              "gap": "About 22 million customers hold mada debit and Visa credit; Mastercard reaches them only as urpay remitters.",
              "neo": "urpay users sending money abroad.", "snb": "Debit, credit, prepaid and business cardholders."},
        "L5": {"d": 0, "s": "The front doors are Al Rajhi's.", "gap": "App, branches and business channels are the bank's; its sponsorship runs through Visa.",
               "neo": "None.", "snb": "App, branches, ATMs, Asian Cup with Visa."},
        "L4": {"d": 0, "s": "The business lines carry mada and Visa.", "gap": "Accounts come with mada; SME and corporate cards are Visa; finance and wealth have no network role.",
               "neo": "None.", "snb": "Accounts, finance, corporate and SME, Al Rajhi Capital, international."},
        "L3": {"d": 0, "s": "Fraud, data and loyalty are the bank's own.", "gap": "SAS fraud tools, the real-time engine, neotek, Drahim and mokafaa are all in-house.",
               "neo": "None.", "snb": "Fraud, AI, open banking, mokafaa, Tasaheal."},
        "L2": {"d": 1, "s": "Mastercard at the till and in urpay transfers.", "gap": "Issuing is mada and Visa; Mastercard is accepted on POS and online, offers MPGS and runs Mastercard Move.",
               "neo": "Acceptance, MPGS, Mastercard Move.", "snb": "mada debit, Visa cards, Visa Direct, sarie."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, Shariah model, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
