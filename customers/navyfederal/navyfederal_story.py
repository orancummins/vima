"""Navy Federal Credit Union's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from navyfederal_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("The world's largest credit union as five discs that stack into one platform, from 15.5 million members and $204 "
       "billion of assets at the bottom to the app, 392 branches and banks on overseas bases at the top. Click the stack to "
       "open it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("mil", "Service members", "flag"),
    ("vet", "Veterans & families", "users-round"),
    ("student", "Students & credit builders", "graduation-cap"),
    ("home", "Homebuyers", "house"),
    ("driver", "Car buyers", "target"),
    ("saver", "Savers & investors", "coins"),
    ("biz", "Business owners", "briefcase"),
]
USERS_DESC = ("Seven kinds of member, 15.5 million in all: service members at home and abroad, veterans and their families, "
              "students and credit builders, homebuyers, car buyers, savers and investors, and 638,700 business members.")

WHO = {"mil": "A service member", "vet": "A veteran", "student": "A student", "home": "A homebuyer", "driver": "A car buyer",
       "saver": "A saver", "biz": "A business owner"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "mil", "name": "Bank day to day",
     "why": "The everyday loop: Active Duty Checking, a Visa debit card, the app, Zelle and 24/7 fraud monitoring.",
     "steps": [("4.1", "checking", "Open Active Duty Checking"), ("2.1", "debit", "Pay with Visa debit"), ("5.1", "app", "Run it in the app"),
               ("2.4", "zelle", "Send money with Zelle"), ("3.1", "fraud", "Protected around the clock")]},
    {"id": "overseas", "who": "mil", "name": "Bank from a base abroad",
     "why": "On-base branches in 10 countries and territories, the debit card and the contact centre.",
     "steps": [("5.3", "ombp", "Bank at an on-base branch overseas"), ("2.1", "debit", "Spend with Visa debit"),
               ("5.4", "contact", "Call the 24/7 contact centre")]},
    {"id": "credit", "who": "vet", "name": "Earn on a credit card",
     "why": "cashRewards on Visa or Mastercard, the new Flagship Premier on Visa, and rewards.",
     "steps": [("2.2", "cashrewards", "Take cashRewards"), ("2.3", "flagship", "Move up to Flagship Premier"), ("3.4", "rewards", "Redeem rewards")]},
    {"id": "build", "who": "student", "name": "Build credit",
     "why": "Bloom+, a secured card and a student loan.",
     "steps": [("3.3", "bloom", "Report rent and bills with Bloom+"), ("2.2", "secured", "Start with cashRewards Secured"),
               ("4.3", "student", "Fund a degree")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "VA and no-money-down mortgages, through a branch.",
     "steps": [("5.2", "branches", "Talk to a loan officer"), ("4.2", "mortgage", "Take a VA or no-down-payment mortgage")]},
    {"id": "drive", "who": "driver", "name": "Buy and run a car",
     "why": "An auto loan and a card that earns on gas.",
     "steps": [("4.3", "auto", "Finance or refinance a car"), ("2.2", "goplat", "Fill up with GO REWARDS")]},
    {"id": "save", "who": "saver", "name": "Save and invest",
     "why": "Certificates, NFIS and a view of everything in My MakingCents.",
     "steps": [("4.1", "savings", "Open an EasyStart certificate"), ("4.5", "nfis", "Invest with NFIS"), ("3.3", "makingcents", "Track it in My MakingCents")]},
    {"id": "biz", "who": "biz", "name": "Run a small business",
     "why": "Business checking, a GO BIZ card on Visa or Mastercard, and card acceptance through Global Payments.",
     "steps": [("4.4", "business", "Open business checking"), ("4.4", "gobiz", "Pay with a GO BIZ card"), ("2.5", "merchant", "Take cards with Global Payments")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Mastercard versions of the everyday credit cards and the business card, the open-banking link, and acceptance at members' merchants.",
     "steps": [("2.2", "cashrewards", "cashRewards on Mastercard"), ("2.2", "goplat", "GO REWARDS and Platinum on Mastercard"),
               ("2.2", "secured", "Secured cards on Mastercard"), ("4.4", "gobiz", "GO BIZ Mastercard"),
               ("3.3", "openbanking", "Mastercard Open Banking links ⚠")]},
    {"id": "mcnext", "who": "mc", "name": "Where scams, agents and bases abroad could land",
     "why": "Where Navy Federal has needs and Mastercard is not yet in: scam scoring for instant payments, agentic payments for its AI, cross-border money for members overseas, card-linked offers and business card controls.",
     "steps": [("3.1", "cube", "Scam scoring beside the Cube bots"), ("2.4", "rtp", "Fraud scores for RTP and FedNow"),
               ("3.2", "ai", "Agent Pay for the AI assistant"), ("5.3", "ombp", "Cross-border transfers for members abroad"),
               ("3.4", "rewards", "Card-linked offers"), ("4.4", "gobiz", "Business payment controls")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Navy Federal Credit Union's map",
    "title": "Visa's credit union, with Mastercard as the second card",
    "lead": "Visa carries Navy Federal's debit for 11 million checking accounts, its prepaid and gift cards and the new Flagship Premier card, under a relationship renewed in 2009. Mastercard is the second network on credit: the most popular card, cashRewards, and GO REWARDS, Platinum, the secured card and GO BIZ Rewards all come in Mastercard versions. Amex has a card too. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Navy Federal's own (Q2 2026 statements, 30 June 2026; 2025 annual report; fact sheet, September 2026) or from Visa, Amex and press. Navy Federal does not publish how many credit cards sit on each network, and no Mastercard announcement naming it was found.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa", "11 million checking accounts; 3.7bn payments in 2025"],
        ["Everyday credit", "Visa or Mastercard", "cashRewards, GO REWARDS, Platinum, Secured ⚠ split"],
        ["Premium", "Visa Signature", "Flagship Premier, September 2026"],
        ["Amex", "More Rewards", "Since 2017"],
        ["Business credit", "Visa or Mastercard", "GO BIZ Rewards"],
        ["Open banking", "Mastercard Open Banking", "Direct API ⚠ third-party source"],
        ["Instant", "Zelle, RTP, FedNow", "21.4m instant payments in 2025"],
        ["Card book", "$33.2bn", "Over $50bn of spend in 2025"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard versions of cashRewards, GO REWARDS, Platinum, the secured card and GO BIZ Rewards, the open-banking link, and acceptance at members' merchants.",
               "deals": "What it does not do: debit, prepaid, the premium card, scam tools, AI or instant payments."},
        "snb": {"dir": "Visa debit, prepaid, gift and premium cards and the 2009 umbrella deal; Amex More Rewards; Zelle, RTP and FedNow; Cube for scams; Databricks for AI.",
                 "deals": "Where they meet: every everyday credit card can be issued on either network."},
    },
    "tl": [
        ["Feb 2009", "Visa renews credit and debit; prepaid and small business added"],
        ["Apr 2009", "TSYS renews processing for Visa and MasterCard credit"],
        ["May 2017", "More Rewards American Express Card announced"],
        ["Mar 2024", "Dietrich Kuhlmann becomes CEO"],
        ["2024", "Visa Class C shares sold for $169.6 million"],
        ["Nov 2024", "CFPB overdraft order"],
        ["Apr 2025", "cashRewards Secured on Visa or Mastercard"],
        ["Q1 2026", "Assets pass $200 billion"],
        ["Sep 2026", "Flagship Premier Visa Signature"],
        ["Oct 2026", "Cube AI scam bots"],
    ],
    "l": {
        "U": {"d": 1, "s": "Some credit cardholders carry Mastercard.",
              "gap": "Every checking member carries Visa debit; holders of the everyday credit cards and GO BIZ may carry Mastercard ⚠ split unknown.",
              "neo": "Holders of Mastercard versions of the credit and business cards.", "snb": "Debit holders, premium and Amex cardholders, borrowers and savers."},
        "L5": {"d": 0, "s": "The front doors are Navy Federal's.", "gap": "App, branches, overseas banks and the contact centre are its own.", "neo": "None.", "snb": "App, branches, overseas banks, contact centre."},
        "L4": {"d": 1, "s": "GO BIZ can be a Mastercard.", "gap": "Checking comes with Visa debit; the GO BIZ credit card is issued on either network; loans have no network role.",
               "neo": "GO BIZ Rewards Mastercard.", "snb": "Checking, savings, mortgages, auto and student loans, NFIS."},
        "L3": {"d": 1, "s": "An open-banking link and rewards on Mastercard cards.", "gap": "Fraud, AI and credit tools are Navy Federal's or other partners'; Mastercard Open Banking connects ⚠.",
               "neo": "Mastercard Open Banking ⚠, rewards on Mastercard cards.", "snb": "Fraud monitoring, Cube, Databricks, Bloom+."},
        "L2": {"d": 1, "s": "Visa debit; credit split between Visa and Mastercard.", "gap": "Visa has debit, prepaid and the premium card; Mastercard shares the everyday credit cards; Zelle and RTP run instant payments.",
               "neo": "Mastercard versions of everyday credit cards.", "snb": "Visa debit, prepaid and Flagship, Amex, Zelle, RTP and FedNow."},
        "L1": {"d": 0, "s": "The credit union's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Members' equity, charter, board, technology."},
    },
    "t": area_lens(LAYERS),
}
