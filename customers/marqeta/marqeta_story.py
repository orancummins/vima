"""Marqeta's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from marqeta_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("A card-issuing processor as five discs that stack into one platform, from $383 billion of volume, Sutton Bank "
       "and network agreements with Visa, Mastercard and PULSE at the bottom to open APIs and a white-label app at the "
       "top. Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it light "
       "up across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes "
       "in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("fin", "Fintechs & digital banks", "smartphone"),
    ("lend", "Lenders & BNPL firms", "hand-coins"),
    ("biz", "Expense & commercial platforms", "briefcase-business"),
    ("gig", "On-demand & gig platforms", "store"),
    ("ent", "Enterprises & banks", "building-2"),
    ("card", "Cardholders", "user-round"),
]
USERS_DESC = ("Six kinds of user: the fintechs and digital banks that issue cards on Marqeta, lenders and BNPL firms, "
              "expense and commercial platforms, on-demand and gig platforms, enterprises and banks, and the "
              "cardholders who carry the cards.")

WHO = {"fin": "A fintech", "lend": "A BNPL lender", "biz": "An expense platform", "gig": "A gig platform",
       "ent": "An enterprise", "card": "A cardholder"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "launch", "who": "fin", "name": "Launch a debit card",
     "why": "The core loop: one API, an issuing bank, a branded card, real-time rules and wallet tokens.",
     "steps": [("5.1", "api", "Integrate the open APIs"), ("1.3", "banks", "Issue through Sutton Bank"), ("2.2", "debit", "Launch a branded debit card"),
               ("3.1", "rtd", "Decide each transaction in real time"), ("3.3", "tokens", "Push it into mobile wallets")]},
    {"id": "flex", "who": "lend", "name": "Offer pay now or pay later on one card",
     "why": "Flexible credentials: Visa's for Klarna and Affirm, Mastercard's One Credential now arriving.",
     "steps": [("4.2", "bnpl", "Run a BNPL business"), ("2.4", "vfc", "Issue on Visa Flexible Credential"),
               ("2.4", "onecred", "Or on Mastercard One Credential"), ("2.4", "hub", "Show BNPL in the wallet with Hub")]},
    {"id": "credit", "who": "lend", "name": "Launch a credit card",
     "why": "Credit issuing since 2023, with three new programmes coming.",
     "steps": [("2.3", "credit", "Issue a revolving card"), ("2.3", "creditnew", "Add a secured credit-builder"), ("3.4", "rewards", "Reward spending")]},
    {"id": "expense", "who": "biz", "name": "Run corporate cards",
     "why": "Virtual cards funded at authorisation, with spend controls and payouts by any rail.",
     "steps": [("4.3", "expense", "Offer an expense card"), ("2.1", "virtual", "Issue virtual cards"), ("2.1", "jit", "Fund each payment just in time"),
               ("2.5", "payouts", "Reimburse by ACH, RTP or push to card")]},
    {"id": "europe", "who": "biz", "name": "Take a card to Europe",
     "why": "TransactPay's licence and Banking Circle's accounts, on the same integration.",
     "steps": [("2.6", "europe", "Issue in the UK and EU"), ("1.3", "licences", "Under TransactPay's e-money licence"), ("2.6", "multinational", "Reach 40+ countries")]},
    {"id": "gig", "who": "gig", "name": "Pay workers fast",
     "why": "Cards and instant payouts for drivers and couriers.",
     "steps": [("4.4", "ondemand", "Run an on-demand platform"), ("2.5", "payouts", "Pay out instantly"), ("2.5", "accounts", "Give workers an account")]},
    {"id": "stable", "who": "card", "name": "Spend stablecoins with a card",
     "why": "Stablecoin-backed cards with zerohash, Coinbase and Mastercard's BVNK.",
     "steps": [("2.7", "stablecoin", "Hold a stablecoin balance"), ("2.7", "bvnk", "Spend it on a BVNK card"), ("3.1", "riskscore", "Checked by the AI risk score")]},
    {"id": "agent", "who": "ent", "name": "Let an AI agent pay",
     "why": "The MCP server issues a virtual card for each task, with controls.",
     "steps": [("3.5", "mcp", "Connect the agent to the MCP server"), ("2.1", "virtual", "Issue a single-use card"), ("3.2", "risk", "Dispute if it goes wrong")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The 2020 agreement and stake, Square's debit card, the first One Credential programmes, BVNK's stablecoin cards and enablement in Asia Pacific.",
     "steps": [("1.4", "mcagr", "Strategic agreement to 2028"), ("2.2", "squaredebit", "Square Debit Card on Mastercard"),
               ("2.4", "onecred", "One Credential programmes"), ("2.7", "bvnk", "BVNK stablecoin cards"), ("2.6", "multinational", "Enablement in Asia Pacific")]},
    {"id": "mcnext", "who": "mc", "name": "Where One Credential, agents and stablecoins could land",
     "why": "Where Marqeta has needs and Mastercard is not yet in: flexible credentials at Visa's scale, Agent Pay behind the MCP server, the network on Coinbase and zerohash cards, fraud scores, push-to-card payouts and commercial cards.",
     "steps": [("2.4", "onecred", "One Credential at scale"), ("3.5", "mcp", "Agent Pay for the MCP server"),
               ("2.7", "stablecoin", "The network for stablecoin cards"), ("3.1", "riskscore", "Mastercard fraud scores"),
               ("2.5", "payouts", "Move for push to card"), ("4.3", "expense", "Commercial cards")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Marqeta's map",
    "title": "A Mastercard investee whose biggest cards are Visa",
    "lead": "Mastercard has worked with Marqeta since 2014, took a stake in 2020 and holds a volume agreement to 2028. Square's debit card, the first One Credential programmes and BVNK's stablecoin cards run on Mastercard. But the largest programmes, Cash App, Klarna, Affirm and Ramp, are Visa, Marqeta leads on Visa Flexible Credential, and Visa also competes with it through DPS and Pismo. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Marqeta's own (Q2 2026 results, 4 August 2026; 10-K for 2025) or from Mastercard, card issuers' disclosures and trade press. Marqeta does not publish its volume by network; several programmes do not name a network.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Agreements", "Visa 2017, Mastercard 2020", "Mastercard term to 2028; PULSE to 2031"],
        ["Investment", "Mastercard stake", "October 2020, undisclosed ⚠"],
        ["Cash App", "Visa", "Largest programme; new issuance leaving"],
        ["Square Debit", "Mastercard", "Sutton Bank"],
        ["Flexible credentials", "Visa first", "Affirm, Klarna, Block; One Credential from 2026"],
        ["BNPL & expense", "Visa", "Klarna, Affirm, Ramp"],
        ["Stablecoins", "BVNK on Mastercard", "Coinbase and zerohash network not named"],
        ["Agents", "MCP server", "No Agent Pay link"],
    ],
    "sides": {
        "neo": {"dir": "The strategic agreement and stake, Square's debit card, One Credential, BVNK stablecoin cards, and certification in Europe and Asia Pacific.",
                "deals": "What it does not do: Cash App, Klarna, Affirm or Ramp cards, Visa Flexible Credential, Marqeta's AI risk score or the MCP server."},
        "snb": {"dir": "Visa for the largest programmes and flexible credentials, PULSE for debit routing, ACH, RTP and FedNow, zerohash and Coinbase, and Marqeta's own risk models.",
                "deals": "Where they meet: every card Marqeta processes, and the race to replace Cash App's growth."},
    },
    "tl": [
        ["2014", "Marqeta and Mastercard start working together"],
        ["2017", "Visa strategic alliance"],
        ["Oct 2020", "Mastercard agreement and investment"],
        ["Jun 2022", "Mastercard Network Enablement Partner, Asia Pacific"],
        ["Feb 2023", "Visa agreement extended five years"],
        ["Jul 2024", "First US processor on Visa Flexible Credential"],
        ["Jul 2025", "TransactPay bought for Europe"],
        ["Nov 2025", "Klarna card to 15 more European markets on Visa"],
        ["May 2026", "One Credential early adopter"],
        ["Jun 2026", "Block starts moving Cash App issuance"],
        ["Sep 2026", "BVNK stablecoin cards on Mastercard"],
        ["Oct 2026", "Coinbase stablecoin cards"],
    ],
    "l": {
        "U": {"d": 1, "s": "Square sellers and BVNK cardholders carry Mastercard; most others carry Visa.",
              "gap": "Cash App, Klarna, Affirm and Ramp cardholders carry Visa; Square Debit and the new One Credential and BVNK cards are Mastercard.",
              "neo": "Square sellers, One Credential and BVNK cardholders.", "snb": "Cash App, Klarna, Affirm and Ramp cardholders."},
        "L5": {"d": 0, "s": "The front doors are Marqeta's.", "gap": "APIs, the dashboard and UX Toolkit are its own; BVNK is the one Mastercard partner.",
               "neo": "BVNK as a partner.", "snb": "APIs, dashboard, UX Toolkit, Banking Circle."},
        "L4": {"d": 0, "s": "The biggest business lines run on Visa.", "gap": "BNPL and expense customers issue on Visa; digital banking is split; on-demand networks are not stated.",
               "neo": "Square in digital banking.", "snb": "Cash App, Klarna, Affirm, Ramp."},
        "L3": {"d": 1, "s": "Network services are shared; the risk models are Marqeta's.", "gap": "Tokens, disputes and network risk scores touch both networks; the AI score, merchant data and MCP server are Marqeta's.",
               "neo": "Tokens, disputes, network risk scores ⚠.", "snb": "AI risk score, Riskified and Signifyd, MCP server."},
        "L2": {"d": 1, "s": "Mastercard in Square, One Credential and BVNK; Visa in the largest cards.",
               "gap": "Visa carries Cash App and flexible credentials; Mastercard has Square, One Credential and BVNK; bank rails and most stablecoin cards are network-neutral.",
               "neo": "Square Debit, One Credential, BVNK, virtual cards.", "snb": "Cash App, Visa Flexible Credential, ACH, RTP, FedNow."},
        "L1": {"d": 1, "s": "A Mastercard agreement and stake beside Visa's and PULSE's.", "gap": "Mastercard's 2020 agreement runs to 2028; Visa's dates from 2017 and PULSE's to 2031.",
               "neo": "2020 agreement and stake.", "snb": "Visa alliance, PULSE, Sutton Bank."},
    },
    "t": area_lens(LAYERS),
}
