"""Chime Financial's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from chime_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("A US digital bank as five discs that stack into one platform, from 10.4 million active members, two "
       "partner banks and its own processor at the bottom to a mobile-only app and employers at the top. Click the stack "
       "to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday members", "user-round"),
    ("worker", "Paycheck earners", "hand-coins"),
    ("builder", "Credit builders", "credit-card"),
    ("prime", "Prime members", "gem"),
    ("saver", "Savers & investors", "trending-up"),
    ("employer", "Employers", "building-2"),
]
USERS_DESC = ("Six kinds of user, 10.4 million active members in all: everyday members, paycheck earners who use SpotMe and "
              "MyPay, credit builders on the Chime Card, Prime members with $3,000 of monthly pay, savers and new investors, "
              "and the employers that offer Chime Workplace.")

WHO = {"con": "A Chime member", "worker": "A paycheck earner", "builder": "A credit builder", "prime": "A Prime member",
       "saver": "A saver", "employer": "An employer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: direct deposit into a fee-free account, the Chime Visa debit card, alerts and the app.",
     "steps": [("2.4", "directdeposit", "Get paid up to two days early"), ("4.1", "checking", "Keep it in Chime Checking"),
               ("2.1", "debit", "Pay with the Visa debit card"), ("3.1", "alerts", "See every purchase in real time"),
               ("5.1", "app", "Run it in the app")]},
    {"id": "payday", "who": "worker", "name": "Bridge to payday",
     "why": "Liquidity for members paid by the hour: SpotMe, MyPay and instant transfers out.",
     "steps": [("2.4", "directdeposit", "Set up direct deposit"), ("4.2", "spotme", "Overdraft fee-free with SpotMe"),
               ("4.2", "mypay", "Draw pay early with MyPay"), ("2.3", "oit", "Send it out instantly")]},
    {"id": "borrow", "who": "worker", "name": "Borrow a little",
     "why": "Instant Loans, underwritten on Chime's own data and the risk models behind it.",
     "steps": [("4.2", "instantloans", "Take an Instant Loan"), ("3.1", "riskmodels", "Approved on Chime's models"), ("5.1", "app", "Repay in the app")]},
    {"id": "credit", "who": "builder", "name": "Build credit",
     "why": "The secured Chime Card on Visa, reported to the three bureaus.",
     "steps": [("2.2", "chimecard", "Get the Chime Card"), ("3.3", "creditscore", "Build a credit score"), ("3.2", "chimeplus", "Earn 2% with Chime Plus")]},
    {"id": "prime", "who": "prime", "name": "Move my whole paycheck",
     "why": "Chime Prime: 5% cash back, a higher savings rate and a metal Visa card for $3,000 of monthly pay.",
     "steps": [("2.4", "directdeposit", "Move $3,000 of pay to Chime"), ("3.2", "chimeprime", "Unlock Chime Prime"),
               ("2.2", "primecard", "Spend on the onyx card"), ("4.1", "savings", "Save at the Prime rate")]},
    {"id": "invest", "who": "saver", "name": "Save and start investing",
     "why": "Savings, Trump Accounts and Chime Invest from $1.",
     "steps": [("4.1", "savings", "Save automatically"), ("3.4", "trumpaccounts", "Open a Trump Account at tax time"),
               ("4.3", "invest", "Invest from $1")]},
    {"id": "employer", "who": "employer", "name": "Offer pay on demand to staff",
     "why": "Chime Enterprise and Chime Workplace, sold through employers and channel partners.",
     "steps": [("5.2", "channels", "Sign up through Chime Enterprise"), ("4.4", "workplace", "Offer Chime Workplace"),
               ("4.2", "mypay", "Staff draw pay early"), ("4.4", "employers", "Join Allied Universal and First Student")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Only at the edges: money pulled in from Mastercard debit cards, and instant transfers to Mastercard cards ⚠.",
     "steps": [("2.4", "linkcards", "Fund from a Mastercard debit card ⚠"), ("2.3", "oit", "Instant transfers to Mastercard cards ⚠")]},
    {"id": "mcnext", "who": "mc", "name": "Where Chime Bank, payouts and identity could land",
     "why": "Where Chime has needs and Mastercard is not yet in: the network choice at Chime Bank, instant payouts, identity and scam tools, open-finance underwriting, premium benefits for Prime and agentic payments.",
     "steps": [("1.3", "chimebank", "A network decision at Chime Bank"), ("2.3", "oit", "Mastercard Move for instant payouts"),
               ("3.1", "riskmodels", "Identity and scam scoring"), ("4.2", "instantloans", "Open finance for cash-flow underwriting"),
               ("3.2", "chimeprime", "World Elite benefits for Prime"), ("1.4", "ai", "Agent Pay for an AI-first bank")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Chime's map",
    "title": "An all-Visa neobank about to own its own issuer",
    "lead": "Every Chime card is Visa: the debit card 10.4 million active members carry, the secured Chime Card that is now 27% of spend, and the ATM network. No Chime–Mastercard programme was found. Chime now runs its own processor and, once it buys Stride Bank in 2027, will own its issuer, so the network becomes its own choice. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Chime's own (Q2 2026 results, 5 August 2026; Stride agreement, 8 September 2026) or from regulators and press. Chime's investor site and parts of its help centre could not be read; network terms are not disclosed.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa", "Every member; issued by Bancorp and Stride"],
        ["Credit", "Chime Card on Visa", "27% of purchase volume, Q2 2026"],
        ["Prime perks", "Visa Signature", "Launched April 2026"],
        ["ATMs", "Visa Plus Alliance, Allpoint", "47,000+ fee-free"],
        ["Money in", "Visa and Mastercard debit", "Linked-card funding ⚠"],
        ["Instant out", "Not disclosed", "OIT, 1.75% fee ⚠"],
        ["Mastercard deals", "None found", "2015–2026"],
        ["Issuer", "Chime Bank, N.A.", "Stride deal closes 1H 2027"],
    ],
    "sides": {
        "neo": {"dir": "Funding from Mastercard debit cards ⚠ and any instant transfers out to Mastercard cards ⚠.",
                "deals": "What it does not do: debit, credit, ATMs, premium benefits, fraud, payouts or data."},
        "snb": {"dir": "Visa debit, the Chime Card and Visa Signature perks, Visa Plus Alliance ATMs, ACH direct deposit, Chime's own processor and models.",
                "deals": "Where they meet: the network choice once Chime owns Chime Bank."},
    },
    "tl": [
        ["2012", "Founded as 1debit"],
        ["2019", "SpotMe launched"],
        ["2020", "Credit Builder on Visa"],
        ["May 2024", "CFPB order"],
        ["Jul 2024", "MyPay launched"],
        ["Jun 2025", "Nasdaq IPO"],
        ["Q3 2025", "Chime Card on Visa, on ChimeCore"],
        ["Q4 2025", "Galileo exited; own processor"],
        ["Apr 2026", "Chime Prime with Visa Signature perks"],
        ["Jul 2026", "Chime Invest; 10% job cut"],
        ["Sep 2026", "Agreement to buy Stride Bank"],
        ["1H 2027", "Chime Bank, N.A. expected"],
    ],
    "l": {
        "U": {"d": 0, "s": "Members carry Visa cards.", "gap": "All 10.4 million active members hold a Chime Visa debit card; credit builders and Prime members hold the Chime Card on Visa.",
              "neo": "None as cardholders.", "snb": "Every member, credit builder and Prime member."},
        "L5": {"d": 0, "s": "The front doors are Chime's.", "gap": "The app, employers and sponsorships are Chime's own.", "neo": "None.", "snb": "App, employers, brand."},
        "L4": {"d": 0, "s": "The business lines carry Visa.", "gap": "Checking comes with Visa debit; SpotMe, MyPay, Instant Loans and investing have no Mastercard role.",
               "neo": "None.", "snb": "Checking, savings, MyPay, Instant Loans, Chime Invest, Chime Enterprise."},
        "L3": {"d": 0, "s": "Services are Chime's own and Visa's.", "gap": "Fraud models are in-house, Prime perks are Visa Signature, and no Mastercard fraud or identity tool is public.",
               "neo": "None.", "snb": "Risk models, Visa Zero Liability, Visa Signature, credit reporting."},
        "L2": {"d": 0, "s": "Visa rails; Mastercard only on money in.", "gap": "Debit, credit and ATMs are Visa; Mastercard appears only on linked-card funding and possibly instant transfers out ⚠.",
               "neo": "Linked Mastercard debit cards ⚠, transfers to Mastercard cards ⚠.", "snb": "Visa debit and credit, Visa Plus Alliance, ACH."},
        "L1": {"d": 0, "s": "Chime's own foundation, with an issuer coming.", "gap": "Nothing in the foundation is Mastercard's; Chime Bank in 2027 reopens the network question.",
               "neo": "None.", "snb": "Partner banks, ChimeCore, capital and strategy."},
    },
    "t": area_lens(LAYERS),
}
