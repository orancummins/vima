"""Worldline's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from worldline_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("A European payments processor with 14% of the continent's acquiring volume, as five discs that stack into one platform, from €4 billion of "
       "revenue, a €500 million rescue raise and licences across Europe at the bottom to sales teams, partner banks, "
       "ISVs and gateways at the top. Click the stack to open it. Choose who you are and what you want to do, and the "
       "areas that deliver it light up across the layers, joined in the order they act. Switch to the Mastercard lens "
       "to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("smb", "Small merchants", "store"),
    ("ent", "Enterprise merchants", "building-2"),
    ("glob", "Global e-commerce", "globe"),
    ("isv", "ISVs & platforms", "code-xml"),
    ("bank", "Banks & issuers", "landmark"),
    ("shop", "Shoppers & cardholders", "user-round"),
]
USERS_DESC = ("Six kinds of user: about 1.2 million merchants from small shops to enterprises, the 800 global companies "
              "on Global Collect, 400 ISVs and platforms, more than 320 banks that outsource processing, and the "
              "cardholders and shoppers who pay.")

WHO = {"smb": "A small merchant", "ent": "An enterprise merchant", "glob": "A global e-commerce company", "isv": "An ISV",
       "bank": "A bank", "shop": "A shopper"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "shop", "who": "smb", "name": "Take cards in a shop",
     "why": "The core loop for a small merchant: onboard, take cards and domestic schemes on a terminal or a phone, and get paid.",
     "steps": [("5.1", "channels", "Sign up through a partner bank"), ("4.1", "smartpos", "Take payments on a SmartPOS"),
               ("4.1", "tapmobile", "Or on a phone with Tap on Mobile"), ("2.2", "domestic", "Accept Bancontact, Girocard or CB"),
               ("2.1", "acquiring", "Settled by Worldline")]},
    {"id": "grow", "who": "smb", "name": "Fund the business",
     "why": "Cash advances against card takings, and Wero beside cards.",
     "steps": [("4.1", "smb", "Bank with PAYONE or Worldline"), ("4.1", "financing", "Take a cash advance"), ("2.4", "wero", "Accept Wero too")]},
    {"id": "enterprise", "who": "ent", "name": "Sell across channels",
     "why": "One Commerce, the Acquiring Hub, smart routing and fraud tools for a large merchant.",
     "steps": [("4.2", "onecommerce", "Run One Commerce"), ("5.3", "gateways", "Connect through GoPay and Axis"),
               ("2.1", "hub", "Route through the Acquiring Hub"), ("3.5", "routing", "Lift approvals with smart routing"),
               ("3.2", "visadm", "Screen with Decision Manager")]},
    {"id": "global", "who": "glob", "name": "Sell in 150 markets",
     "why": "Global Collect, with tokens, Click to Pay, Klarna and stablecoin settlement.",
     "steps": [("2.5", "globalcollect", "Accept with Global Collect"), ("3.1", "tokens", "Store network tokens"),
               ("3.3", "c2p", "Offer Click to Pay for subscriptions"), ("2.5", "klarna", "Offer Klarna"),
               ("2.6", "stablecoins", "Settle in stablecoins")]},
    {"id": "agent", "who": "ent", "name": "Sell to AI agents",
     "why": "Worldline ran Europe's first live agentic payment on Mastercard Agent Pay.",
     "steps": [("3.4", "agentic", "Connect through MCP, AP2, ACP or UCP"), ("3.4", "agentpay", "Accept Agent Pay"),
               ("3.1", "acs", "Authenticate the agent's payment")]},
    {"id": "isv", "who": "isv", "name": "Embed payments in software",
     "why": "OPP for platforms, Launchpad onboarding and open-banking data.",
     "steps": [("5.2", "isv", "Embed with Worldline for Platforms"), ("5.2", "launchpad", "Onboard merchants with Launchpad"),
               ("3.5", "openbanking", "Add open-banking payments")]},
    {"id": "bank", "who": "bank", "name": "Outsource card processing",
     "why": "Issuer processing, 3-D Secure, tokens and fraud scoring for a bank.",
     "steps": [("4.3", "fi", "Outsource to Worldline"), ("2.3", "issuing", "Process cards"), ("3.1", "acs", "Authenticate with the ACS"),
               ("3.1", "tokens", "Tokenise for wallets"), ("3.2", "fraud", "Score fraud with Watcher")]},
    {"id": "a2a", "who": "bank", "name": "Run instant payments and Wero",
     "why": "Clearing, instant payments, Verification of Payee, Wero and the digital euro.",
     "steps": [("2.4", "instant", "Clear instant payments"), ("3.2", "vop", "Verify the payee"),
               ("2.4", "wero", "Join Wero"), ("2.6", "deuro", "Pilot the digital euro")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Agent Pay firsts with ING and Crédit Agricole, card acquiring and issuer processing, Click to Pay and tokens on Global Collect.",
     "steps": [("3.4", "agentpay", "Mastercard Agent Pay"), ("2.1", "acquiring", "Acquiring Mastercard"),
               ("2.3", "issuing", "Processing Mastercard issuers"), ("3.3", "c2p", "Click to Pay"), ("3.1", "tokens", "Tokens on Global Collect ⚠")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, risk and issuer services could land",
     "why": "Where Worldline has needs and Mastercard is not yet in: Agent Pay across its issuing book, merchant-risk tools for the remediation, tokens through the GoPay move, issuer services for a shrinking Financial Services arm, bank-led instalments and cross-border settlement.",
     "steps": [("3.4", "agentic", "Agent Pay across UCP and MCP"), ("1.6", "remediation", "Merchant monitoring and AML tools"),
               ("5.3", "gateways", "Tokens and Click to Pay on GoPay"), ("2.3", "issuing", "Issuer services and instalments"),
               ("2.5", "klarna", "Bank-led instalments at the till"), ("2.6", "stablecoins", "Cross-border settlement")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Worldline's map",
    "title": "Agent Pay's European first, on a home turf of domestic schemes",
    "lead": "Worldline acquires and processes Mastercard across Europe and ran Europe's first live agentic payments on Mastercard Agent Pay, with ING in June 2026 and Crédit Agricole later that month. It also carries Click to Pay and network tokens on Global Collect, Ogone and Saferpay. But its strongest markets run on Bancontact, Cartes Bancaires, Girocard and TWINT, it is an EPI shareholder pushing Wero, it uses Visa's Decision Manager and Klarna, and no framework deal with Mastercard is public. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Worldline's own (H1 2026 results, 30 July 2026; FY2025 results and Universal Registration Document) or from Mastercard and press. Mastercard's site was blocked, so some Mastercard items rest on search summaries. Worldline does not publish its network split.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Agentic", "Mastercard Agent Pay", "Europe's first live, ING, June 2026"],
        ["Acquiring", "Every network", "€245bn in H1 2026"],
        ["Domestic", "Bancontact, CB, Girocard, TWINT", "Core markets"],
        ["Issuing", "Every network", "156 million cards processed"],
        ["Checkout", "Click to Pay", "Recurring on Global Collect, 2026"],
        ["Fraud", "Visa Decision Manager", "And its own Watcher"],
        ["A2A", "Wero", "EPI shareholder since 2020"],
        ["Agreement", "None public", "No framework deal found ⚠"],
    ],
    "sides": {
        "neo": {"dir": "Card acquiring and issuer processing, Agent Pay with ING and Crédit Agricole, the Agent Suite plan, Click to Pay and tokens on Global Collect, and a history of MasterPass, SoftPOS and contactless firsts.",
                "deals": "What it does not do: domestic schemes, Wero, instant payments, fraud scoring, merchant risk, Klarna or stablecoins."},
        "snb": {"dir": "Bancontact, Cartes Bancaires, Girocard and TWINT, Wero and the digital euro, Visa's Decision Manager and Visa's own agentic payment with ING, Klarna, Fipto and Circle, and Worldline's own token service and fraud models.",
                "deals": "Where they meet: agentic commerce, where both networks ran live firsts through Worldline a month apart."},
    },
    "tl": [
        ["Oct 2013", "MasterPass distribution deal"],
        ["Jun 2020", "SoftPOS with Mastercard and Axis Bank in India"],
        ["Nov 2020", "Worldline becomes an EPI shareholder"],
        ["Mar 2021", "First certified for Mastercard Enhanced Contactless"],
        ["Oct 2024", "Visa Decision Manager partnership"],
        ["Jun 2025", "Named a Mastercard tokenisation and Click to Pay partner ⚠; press investigation"],
        ["Jun 2026", "Agent Pay live with ING and with Crédit Agricole; Click to Pay for recurring"],
        ["Jul 2026", "Visa agentic payment with ING in Germany; digital-euro pilot"],
        ["Sep 2026", "Named in Mastercard's Agent Suite for merchants"],
    ],
    "l": {
        "U": {"d": 1, "s": "Every merchant and bank touches Mastercard; few run only on it.",
              "gap": "Merchants accept Mastercard beside domestic schemes and Wero; banks process Mastercard and Visa cards through Worldline.",
              "neo": "Agent Pay merchants and issuers, Global Collect merchants on Click to Pay.", "snb": "Domestic-scheme merchants, Wero users, Visa issuers."},
        "L5": {"d": 1, "s": "The gateways carry every network; the channels are Worldline's.", "gap": "Sales teams, partner banks and ISVs are Worldline's; its gateways carry Mastercard among other methods.",
               "neo": "Card acceptance in the gateways.", "snb": "Sales, partner banks, ISVs, Launchpad."},
        "L4": {"d": 1, "s": "Every line takes Mastercard; none depends on it.", "gap": "Small merchants, enterprises and banks all carry Mastercard alongside domestic schemes and Visa.",
               "neo": "Card acceptance and issuer processing.", "snb": "Domestic schemes, cash advances, public-sector work."},
        "L3": {"d": 1, "s": "Agent Pay is Mastercard's; the rest is Worldline's or Visa's.", "gap": "Agent Pay and Click to Pay involve Mastercard; fraud, Verification of Payee and open banking do not, and Visa's Decision Manager is in.",
               "neo": "Agent Pay, Click to Pay, tokens ⚠.", "snb": "Watcher, Decision Manager, own token service, open banking."},
        "L2": {"d": 1, "s": "Mastercard in card rails; domestic schemes and Wero beside it.", "gap": "Card acquiring and issuing carry Mastercard; domestic schemes, Wero, Klarna and stablecoins do not.",
               "neo": "Acquiring, issuer processing, Global Collect.", "snb": "Domestic schemes, Wero, instant payments, Klarna, stablecoins."},
        "L1": {"d": 0, "s": "Worldline's own capital and licences.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, licences, strategy, remediation."},
    },
    "t": area_lens(LAYERS),
}
