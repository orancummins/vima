"""USAA's kinds of member, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from usaa_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("The military community's insurer and bank as five discs that stack into one platform, from 14.3 million "
       "member-owners and $38.6 billion of net worth at the bottom to the USAA app, contact centres and military "
       "bases at the top. Click the stack to open it. Choose who you are and what you want to do, and the areas that "
       "deliver it light up across the layers, joined in the order they act. Switch to the Mastercard lens to see how "
       "deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Serving members & families", "user-round"),
    ("vet", "Veterans", "flag"),
    ("young", "New recruits & young members", "graduation-cap"),
    ("driver", "Drivers & policyholders", "target"),
    ("home", "Homebuyers & PCS movers", "house"),
    ("saver", "Savers & retirees", "coins"),
]
USERS_DESC = ("Six kinds of member, more than 14.5 million in all: serving members and their families, veterans, new "
              "recruits and young members, drivers and policyholders, homebuyers on the move, and savers and retirees.")

WHO = {"con": "A serving member", "vet": "A veteran", "young": "A new recruit", "driver": "A policyholder",
       "home": "A homebuyer", "saver": "A saver"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: a fee-free checking account, a Visa debit card, the app, Zelle and fraud monitoring.",
     "steps": [("4.3", "deposits", "Open Classic Checking"), ("2.1", "debit", "Pay with Visa debit"), ("5.1", "app", "Run it in the app"),
               ("2.5", "zelle", "Send money with Zelle"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "card", "who": "con", "name": "Earn on a card",
     "why": "Visa and American Express cards, with 5% on base spending and Shop With Rewards.",
     "steps": [("2.3", "cashbackplus", "Take Cashback Rewards Plus Amex"), ("2.2", "eagleadapt", "Or Eagle Adapt Visa"),
               ("3.3", "cardrewards", "Redeem with Shop With Rewards"), ("3.3", "perks", "Save with USAA Perks")]},
    {"id": "recruit", "who": "young", "name": "Start out as a recruit",
     "why": "Join, open an account with nothing down, build credit and bank near base.",
     "steps": [("1.3", "heritage", "Become a member"), ("2.4", "funding", "Fund the account"), ("4.3", "deposits", "Open checking"),
               ("2.3", "eagleascend", "Build credit with Eagle Ascend"), ("5.3", "bases", "Bank on base")]},
    {"id": "drive", "who": "driver", "name": "Insure and finance a car",
     "why": "The fifth-largest US auto insurer, telematics discounts and an auto loan.",
     "steps": [("4.4", "autoloans", "Finance the car"), ("4.1", "autoins", "Insure it"), ("3.5", "safepilot", "Save with SafePilot"),
               ("3.2", "ai", "Claim with AI help")]},
    {"id": "move", "who": "home", "name": "Move and buy a home",
     "why": "A PCS move with an agent from HomeStory, a VA loan and home insurance.",
     "steps": [("5.4", "partners", "Find an agent"), ("4.4", "mortgages", "Take a VA loan"), ("4.1", "autoins", "Insure the home"),
               ("3.4", "advice", "Plan the PCS move")]},
    {"id": "relief", "who": "vet", "name": "Get help when pay stops",
     "why": "No-interest loans and fee waivers during the shutdown, and scam protection.",
     "steps": [("3.4", "relief", "Take a no-interest loan"), ("3.1", "scams", "Spot a scam"), ("5.2", "contact", "Call USAA")]},
    {"id": "save", "who": "saver", "name": "Save and protect the family",
     "why": "Savings, life cover and investments through Schwab.",
     "steps": [("4.3", "deposits", "Save without fees"), ("4.2", "life", "Buy life cover"), ("4.5", "invest", "Invest through Schwab")]},
    {"id": "deposit", "who": "vet", "name": "Deposit a cheque from anywhere",
     "why": "USAA's patented mobile deposit and a 100,000-ATM network.",
     "steps": [("5.1", "app", "Open the app"), ("2.6", "rdc", "Deposit with Deposit@Mobile"), ("2.6", "atm", "Withdraw fee-free")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Very little: the cards left for Visa in 2016, leaving account funding by Mastercard cards and whatever processing Mastercard kept ⚠.",
     "steps": [("2.4", "mcexit", "Thirty years of Mastercard cards, to 2016"), ("2.4", "funding", "Mastercard cards fund new accounts"),
               ("2.2", "visacredit", "The card book now on Visa")]},
    {"id": "mcnext", "who": "mc", "name": "Where scam tools, offers and agents could land",
     "why": "Where USAA has needs that do not depend on the brand on the card: scam scoring for transfers, card-linked offers beside Perks, Agent Pay for an AI-heavy insurer-bank, open finance as Section 1033 is rewritten, and a future network re-tender ⚠.",
     "steps": [("3.1", "fraud", "Scam and identity scoring"), ("2.5", "zelle", "Safer account-to-account transfers"),
               ("3.3", "perks", "Card-linked offers beside Perks"), ("3.2", "ai", "Agent Pay for AI service"),
               ("2.2", "visacredit", "A future network re-tender ⚠")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across USAA's map",
    "title": "Thirty years of Mastercard, then a clean break to Visa",
    "lead": "Mastercard carried USAA's credit and debit cards for about 30 years until USAA moved the whole portfolio to Visa through 2016. Today USAA Bank's debit is Visa and its nine credit cards are six Visa and three American Express, two of them launched in July 2026. No joint Mastercard initiative has been announced since. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are USAA's own (2025 Annual Report to Members) or FDIC call reports to 30 June 2026. usaa.com card pages were read on 17 October 2026; credit ratings and current processing arrangements could not be checked.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa", "Since the 2016 conversion"],
        ["Credit", "Visa and Amex", "Six Visa, three Amex cards; 4m+ cardholders"],
        ["Mastercard", "Left 2016", "About 30 years; some processing kept ⚠"],
        ["New cards", "Visa and Amex", "Eagle Adapt and Eagle Ascend, July 2026"],
        ["Transfers", "Zelle", "Higher limits from June 2026"],
        ["Fraud", "USAA's own", "8 billion threats blocked in 2025"],
        ["Regulator", "OCC order", "December 2024; new products need notice"],
    ],
    "sides": {
        "neo": {"dir": "Acceptance of members' outside Mastercard cards to fund accounts, and any processing kept in 2015 ⚠.",
                "deals": "What it does not do: debit, credit, wallets, transfers, fraud, rewards or AI."},
        "snb": {"dir": "Visa debit and credit, American Express cards and offers, Zelle, USAA's own fraud, AI and Deposit@Mobile.",
                "deals": "Where they could meet: network-neutral scam, offers, open-finance and agentic services."},
    },
    "tl": [
        ["c.1985", "Mastercard carries USAA's cards ⚠"],
        ["Oct 2015", "USAA announces move to Visa"],
        ["2016", "Cards converted to Visa"],
        ["Dec 2024", "OCC cease-and-desist order"],
        ["Apr 2025", "Juan C. Andrade becomes CEO"],
        ["Jun 2026", "Higher Zelle limits"],
        ["Jul 2026", "Eagle Adapt Visa, Eagle Ascend Amex"],
        ["Aug 2026", "BofA patent cross-licence; Melcher chairman"],
    ],
    "l": {
        "U": {"d": 0, "s": "Members carry Visa and Amex cards.",
              "gap": "Every USAA debit and credit card is Visa or American Express; Mastercard reaches members only through cards from other banks.",
              "neo": "Members' outside Mastercard cards.", "snb": "All USAA cardholders."},
        "L5": {"d": 0, "s": "The front doors are USAA's.", "gap": "App, contact centres and base branches are USAA's own.", "neo": "None.", "snb": "App, contact centres, bases, partners."},
        "L4": {"d": 0, "s": "The business lines carry Visa and Amex.", "gap": "Deposits come with Visa debit; insurance, loans and investments have no network role.",
               "neo": "None.", "snb": "Deposits, cards, loans, insurance."},
        "L3": {"d": 0, "s": "Fraud, AI and rewards are USAA's own.", "gap": "Fraud models, AI and Perks are in-house; Amex supplies card offers.",
               "neo": "None.", "snb": "Fraud monitoring, AI, Perks, Amex offers."},
        "L2": {"d": 0, "s": "Visa and Amex on the cards, Zelle for transfers.", "gap": "Mastercard left in 2016; only account funding and any kept processing remain ⚠.",
               "neo": "Account funding, legacy processing ⚠.", "snb": "Visa, Amex, Zelle, Deposit@Mobile."},
        "L1": {"d": 0, "s": "The association's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, members, patents, strategy."},
    },
    "t": area_lens(LAYERS),
}
