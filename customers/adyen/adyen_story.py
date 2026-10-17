"""Adyen's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from adyen_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("A global payments platform as five discs that stack into one, from €1.39 trillion of volume and a Dutch banking "
       "licence at the bottom to APIs, 838,000 terminals and partners at the top. Click the stack to open it. Choose who "
       "you are and what you want to do, and the areas that deliver it light up across the layers, joined in the order "
       "they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("ent", "Enterprise merchants", "building-2"),
    ("uc", "Retailers & hospitality", "store"),
    ("plat", "Platforms & marketplaces", "users-round"),
    ("sme", "Businesses on platforms", "briefcase"),
    ("travel", "Travel & mobility", "plane"),
    ("shop", "Shoppers", "user-round"),
]
USERS_DESC = ("Six kinds of user: enterprise merchants online, retailers and hospitality chains selling in store and "
              "online, platforms and marketplaces, the 293,000 businesses on those platforms, travel and mobility "
              "companies, and the shoppers who pay them.")

WHO = {"ent": "An enterprise merchant", "uc": "A retailer", "plat": "A platform", "sme": "A business on a platform",
       "travel": "A travel company", "shop": "A shopper"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "accept", "who": "ent", "name": "Take payments worldwide",
     "why": "The core loop: one API, direct acquiring, tokens, Uplift and risk checks.",
     "steps": [("5.1", "apis", "Integrate the API"), ("2.1", "acquiring", "Acquire directly"), ("3.2", "tokens", "Pay with network tokens"),
               ("3.3", "uplift", "Lift conversion with Uplift"), ("3.1", "risk", "Screen for fraud")]},
    {"id": "store", "who": "uc", "name": "Sell in store and online",
     "why": "Terminals, Unified Commerce, offline resilience and loyalty.",
     "steps": [("5.2", "terminals", "Take payments on terminals"), ("4.2", "unified", "Join online and in-store"),
               ("5.2", "storeforward", "Keep selling through outages"), ("3.4", "talonone", "Run loyalty with Talon.One")]},
    {"id": "platform", "who": "plat", "name": "Embed payments in a platform",
     "why": "Platforms, accounts, capital and issuing for the businesses on it.",
     "steps": [("4.3", "platforms", "Embed payments"), ("4.4", "accounts", "Offer business accounts"),
               ("4.4", "capital", "Lend with Adyen Capital"), ("2.3", "issuing", "Issue cards")]},
    {"id": "sme", "who": "sme", "name": "Get paid and funded on a platform",
     "why": "Instant payouts, loans and virtual cards for the businesses on Toast, Vagaro and the like.",
     "steps": [("4.3", "platforms", "Sign up through a platform"), ("2.4", "cashout", "Get paid instantly with CashOut"),
               ("4.4", "capital", "Borrow"), ("2.3", "virtualcards", "Pay suppliers by virtual card")]},
    {"id": "travel", "who": "travel", "name": "Move travel money faster",
     "why": "Intelligent Money Movement, charge cards and payouts.",
     "steps": [("2.4", "imm", "Settle with IMM"), ("2.3", "chargecards", "Give staff charge cards"), ("2.4", "cardpayouts", "Pay out to cards")]},
    {"id": "checkout", "who": "shop", "name": "Pay in one click",
     "why": "Click to Pay, wallets and BNPL, with Dynamic Identification behind them.",
     "steps": [("3.2", "clicktopay", "Pay with Click to Pay"), ("2.5", "wallets", "Or Apple Pay or PayPal"),
               ("2.5", "bnpl", "Or split it with Klarna"), ("3.1", "dynamicid", "Recognised without a password")]},
    {"id": "local", "who": "ent", "name": "Pay the local way",
     "why": "Local schemes, Pix, UPI and pay-by-bank, routed for cost.",
     "steps": [("2.2", "localschemes", "Route to local schemes"), ("2.2", "usdebit", "Route US debit"),
               ("2.5", "pix", "Take Pix"), ("2.5", "upi", "Take UPI"), ("2.5", "paybybank", "Take Pay by Bank and Wero")]},
    {"id": "agent", "who": "ent", "name": "Sell to AI agents",
     "why": "Adyen Agentic, Agent Pay for Machines and usage-based billing.",
     "steps": [("3.5", "adyenagentic", "Connect to UCP, AP2 and ACP"), ("3.5", "ap4m", "Accept Agent Pay for Machines"),
               ("3.2", "tokens", "Keep tokens portable"), ("3.4", "orb", "Bill by usage with Orb")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Direct acquiring, Click to Pay, issuing, tokens, Agent Pay for Machines and the optimisation platform.",
     "steps": [("2.1", "acquiring", "Mastercard acquiring, India included"), ("3.2", "clicktopay", "Click to Pay, recurring only on Mastercard"),
               ("2.3", "issuing", "Adyen Issuing on Mastercard"), ("3.5", "ap4m", "Agent Pay for Machines supporter"),
               ("3.3", "pop", "Payment Optimization Platform ⚠")]},
    {"id": "mcnext", "who": "mc", "name": "Where virtual cards, Move and agents could land",
     "why": "Where Adyen has needs and Mastercard is not yet in, or not visibly: commercial cards on the fastest-growing product, Move for CashOut and IMM, agentic tokens in Adyen Agentic, offers through Talon.One and micropayments for Orb.",
     "steps": [("2.3", "virtualcards", "Commercial and virtual cards on Mastercard"), ("2.4", "cashout", "Mastercard Move for CashOut"),
               ("2.4", "imm", "Move for cross-border IMM"), ("3.5", "adyenagentic", "Agentic tokens and Verifiable Intent"),
               ("3.4", "talonone", "Offers through Talon.One"), ("3.4", "orb", "AI micropayments for Orb")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Adyen's map",
    "title": "Mastercard in every flow, Visa at parity, and a router that picks the cheaper rail",
    "lead": "Adyen acquires Mastercard directly, issues on it, uses its tokens and Click to Pay (recurring only on Mastercard), pays out to its cards, backed Agent Pay for Machines and made Mastercard an Adyen Agentic partner. No bilateral agreement was found, Visa matches it almost everywhere, and Adyen's routing sends volume to local schemes, US debit networks, Pix, UPI and Wero when they are cheaper. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Adyen's own (H1 2026 letter, 13 August 2026; 2025 Annual Report) or from Adyen's docs and Mastercard and Visa releases. Mastercard.com pages could not be fetched; items marked ⚠ rest on search snippets. Adyen does not publish a network split.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Acquiring", "Direct", "Visa, Mastercard, Amex; RuPay in India"],
        ["Click to Pay", "Both networks", "Recurring only on Mastercard"],
        ["Issuing", "Both networks", "8x in 2025; split not disclosed"],
        ["Agentic", "Both networks", "Agent Pay for Machines; Visa Trusted Agent Protocol"],
        ["Routing", "Local schemes", "eftpos, US debit, Cartes Bancaires"],
        ["Account-to-account", "Pix, UPI, Wero", "Pay by Bank in Europe and the US"],
        ["Payouts", "Cards and banks", "Rail not disclosed ⚠"],
        ["Agreement", "None found", "No bilateral deal published"],
    ],
    "sides": {
        "neo": {"dir": "Direct acquiring, issuing, tokens and Click to Pay, payouts to Mastercard cards, Agent Pay for Machines, Adyen Agentic and the optimisation platform ⚠.",
                "deals": "What it does not do, visibly: Move for payouts, commercial cards at scale, offers, or a bilateral deal."},
        "snb": {"dir": "Visa at parity in issuing, Click to Pay and agentic work, Amex, local schemes and US debit networks, Pix, UPI and Wero, BNPL, and Adyen's own risk and routing.",
                "deals": "Where they meet: every card payment, and the standards for agentic commerce."},
    },
    "tl": [
        ["Mar 2023", "Click to Pay embedded with Mastercard and Visa"],
        ["Aug 2024", "Meses sin intereses in Mexico ⚠"],
        ["Nov 2024", "Mastercard names Adyen a Click to Pay enabler"],
        ["Oct 2025", "Payment Optimization Platform ⚠; Visa Trusted Agent Protocol"],
        ["Jun 2026", "Agent Pay for Machines; Adyen Agentic launched"],
        ["Jul 2026", "Talon.One and Orb closed"],
        ["Sep 2026", "Mastercard agentic trust services, Adyen not named"],
        ["Oct 2026", "Q3 2026 update due 28 October"],
    ],
    "l": {
        "U": {"d": 1, "s": "Every merchant takes Mastercard; many also route around it.",
              "gap": "Every merchant accepts Mastercard; platforms issue on it and Visa; local methods and debit routing take share where cheaper.",
              "neo": "Merchants on Mastercard tokens and Click to Pay, platforms issuing cards.", "snb": "Pix, UPI and Wero payers, US debit routed elsewhere."},
        "L5": {"d": 1, "s": "Terminals take Mastercard; Mastercard is an agentic partner.", "gap": "APIs and offices are Adyen's; terminals accept every network; Mastercard is one of four agentic partners.",
               "neo": "Terminals, agentic partnership.", "snb": "APIs, Toast, Salesforce, Visa and Amex."},
        "L4": {"d": 1, "s": "Mastercard in every pillar through acceptance.", "gap": "Digital, Unified Commerce and Platforms accept Mastercard; accounts and Capital have no network role.",
               "neo": "Acceptance in every pillar.", "snb": "Accounts, Capital."},
        "L3": {"d": 1, "s": "Agent Pay for Machines is Mastercard's; risk and optimisation are Adyen's.", "gap": "Tokens and Click to Pay involve Mastercard; Uplift, Dynamic Identification, Talon.One and Orb are Adyen's own.",
               "neo": "Agent Pay for Machines, tokens, Click to Pay, optimisation platform ⚠.", "snb": "Uplift, Personalize, Dynamic Identification, Visa tokens."},
        "L2": {"d": 1, "s": "Shared with Visa, around local rails.", "gap": "Mastercard is in acquiring, issuing and card payouts; Visa is too; local schemes, Pix, UPI and Wero are in neither.",
               "neo": "Acquiring, issuing, card payouts, Maestro USA.", "snb": "Visa, local schemes, account-to-account, BNPL."},
        "L1": {"d": 0, "s": "Adyen's own scale and licences.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Licences, platform, strategy."},
    },
    "t": area_lens(LAYERS),
}
