"""Klarna Group's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from klarna_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("The world's biggest pay-later network as five discs that stack into one, from 120 million active consumers, a "
       "Swedish bank and $128 billion of yearly volume at the bottom to the Klarna app, payment platforms and AI "
       "assistants at the top. Click the stack to open it. Choose who you are and what you want to do, and the areas "
       "that deliver it light up across the layers, joined in the order they act. Switch to the Mastercard lens to see "
       "how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("shop", "Shoppers", "user-round"),
    ("bank", "Card & banking customers", "wallet-cards"),
    ("big", "Big-ticket buyers", "hand-coins"),
    ("mer", "Merchants", "store"),
    ("ent", "Enterprise & travel brands", "building-2"),
    ("psp", "PSPs & acquirers", "network"),
]
USERS_DESC = ("Six kinds of user: 120 million shoppers, the 15.8 million who bank with Klarna, buyers spreading big "
              "purchases, 1.2 million merchants, the enterprise and travel brands, and the payment platforms that switch "
              "Klarna on for their merchants.")

WHO = {"shop": "A shopper", "bank": "A Klarna Card holder", "big": "A big-ticket buyer", "mer": "A merchant",
       "ent": "An enterprise brand", "psp": "A payment platform"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "pay4", "who": "shop", "name": "Split a purchase into four",
     "why": "The core loop: pick Klarna at checkout, get a real-time decision, repay over six weeks from a card or bank.",
     "steps": [("5.2", "psps", "Find Klarna at checkout"), ("3.1", "underwriting", "Approved in real time"),
               ("2.2", "paylater", "Pay in four, interest-free"), ("2.1", "paynow", "Repay by card or bank"), ("5.1", "app", "Track it in the app")]},
    {"id": "card", "who": "bank", "name": "Spend everywhere with the Klarna Card",
     "why": "Debit by default, pay later on request, on Visa Flexible Credential in 16 countries.",
     "steps": [("2.5", "balance", "Top up Klarna Balance"), ("2.4", "cardeu", "Pay with the Klarna Card"),
               ("2.4", "cardus", "Or the US card"), ("3.4", "cashback", "Earn cashback"), ("3.2", "inbox", "Check messages are genuine")]},
    {"id": "member", "who": "bank", "name": "Join a membership",
     "why": "Cashback, lounges, insurance, subscriptions and a free UK mobile plan for a monthly fee.",
     "steps": [("4.3", "memberships", "Choose a tier"), ("3.4", "cashback", "Earn up to 1.5% back"), ("4.3", "mobile", "Add Klarna Mobile")]},
    {"id": "bigticket", "who": "big", "name": "Spread a big purchase",
     "why": "Fair Financing, OnePay at Walmart and Apple Upgrade leases.",
     "steps": [("4.1", "merchants", "Shop at a partner"), ("2.3", "fairfin", "Take Fair Financing"),
               ("2.3", "onepay", "Or OnePay at Walmart"), ("2.3", "appleupgrade", "Or lease from Apple")]},
    {"id": "save", "who": "bank", "name": "Save and send money",
     "why": "Savings in Europe and the US, and P2P in 13 European countries.",
     "steps": [("4.2", "ussavings", "Open a savings account"), ("2.5", "p2p", "Send money to a friend"), ("3.2", "callstatus", "Check a caller is Klarna")]},
    {"id": "merchant", "who": "mer", "name": "Offer Klarna at checkout and in store",
     "why": "Switched on by default through a PSP, with Sign in with Klarna, in-store QR and ads.",
     "steps": [("5.2", "jpm", "Turn Klarna on through J.P. Morgan Payments"), ("3.2", "signin", "Add Sign in with Klarna"),
               ("2.6", "instore", "Take Klarna at the till"), ("3.5", "search", "Reach shoppers through Search & Compare")]},
    {"id": "travel", "who": "ent", "name": "Sell flights and rides",
     "why": "Southwest, TAP and Bolt use Klarna for pay-in-full, pay in four and financing.",
     "steps": [("4.1", "travel", "Add Klarna to booking"), ("2.1", "paynow", "Pay in full"), ("2.3", "fairfin", "Or finance the trip")]},
    {"id": "agent", "who": "shop", "name": "Shop through an AI assistant",
     "why": "Klarna in ChatGPT, Gemini and Google Search, on Google's AP2 and UCP and its own product protocol.",
     "steps": [("5.3", "chatgpt", "Search in ChatGPT"), ("3.3", "agentic", "Products and payments via open protocols"),
               ("5.3", "gemini", "Pay with Klarna in Gemini")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "At the edges: Mastercard cards fund Pay Now and repayments, Balance top-ups take them, and Mastercard Gateway lists Klarna as a payment method.",
     "steps": [("2.1", "paynow", "Mastercard cards fund Pay Now ⚠"), ("2.2", "paylater", "Repayments by Mastercard debit ⚠"),
               ("2.5", "balance", "Balance top-ups by card ⚠"), ("5.2", "mpgs", "Klarna on Mastercard Gateway")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, a US bank and P2P could land",
     "why": "Where Klarna has needs and Mastercard is not yet in: a second network for the card once Klarna Bank USA issues, Agent Pay for its agentic checkout, Move for cross-border P2P, scam scoring for Balance and P2P, and offers for its members.",
     "steps": [("1.2", "usbank", "Network choice for Klarna Bank USA"), ("3.3", "agentic", "Agent Pay beside AP2 and UCP"),
               ("2.5", "p2p", "Mastercard Move for cross-border P2P"), ("3.2", "callstatus", "Scam scoring for transfers"),
               ("3.4", "cashback", "Card-linked offers for members")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Klarna's map",
    "title": "A Visa card company that Mastercard only touches at the till",
    "lead": "Klarna's card, the product turning a checkout button into a bank, runs on Visa Flexible Credential in all 16 card countries, and Visa has been a shareholder and partner since 2017. Klarna also sells its own network as an alternative to card schemes, and is building stablecoins and agent payments with Stripe and Google. Mastercard is present at the edges: its cards fund Pay Now and repayments, and Mastercard Gateway lists Klarna. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Klarna's own (Q2 2026 results, 18 August 2026; 2025 annual report) or from Klarna's newsroom, Mastercard's developer site and press. Klarna's governance pages and SEC filings were not reachable, and funding-card networks rest on third-party help pages ⚠.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Klarna Card", "Visa Flexible Credential", "6.5 million users, 16 countries"],
        ["US issuing", "WebBank on Visa", "Own charter applied for, July 2026"],
        ["Visa", "Shareholder since 2017", "Partnership planned at the time"],
        ["Funding cards", "Any network", "Mastercard debit included ⚠"],
        ["Gateway", "Mastercard Gateway", "Lists Klarna Pay Later, Pay Now, Financing"],
        ["Agentic", "Google AP2 and UCP", "No Agent Pay link found"],
        ["Stablecoin", "KlarnaUSD on Tempo", "Stripe's chain, Bridge issuance"],
        ["Distribution", "PSPs by default", "Stripe, Adyen, Worldpay, Nexi, J.P. Morgan"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard cards that fund Pay Now, repayments and Balance top-ups ⚠, and Mastercard Gateway as one more distributor of Klarna.",
                "deals": "What it does not do: the Klarna Card, agentic payments, scam tools, P2P, stablecoins or loyalty."},
        "snb": {"dir": "Visa Flexible Credential for every Klarna Card, WebBank and Marqeta for issuing, Stripe's Tempo for KlarnaUSD, Google for agent protocols, and Klarna's own credit, fraud and open-banking rails.",
                "deals": "Where they meet: card acceptance at Klarna's merchants and the cards shoppers use to pay Klarna back."},
    },
    "tl": [
        ["Jun 2017", "Swedish banking licence; Visa invests"],
        ["Feb 2021", "German account with a Visa debit card"],
        ["Jun 2022", "US Klarna Card on Visa"],
        ["Oct 2024", "Worldpay makes Klarna a default method"],
        ["Jun 2025", "Klarna Card on Visa Flexible Credential"],
        ["Sep 2025", "NYSE listing; card across Europe"],
        ["Oct 2025", "UK card; Google AP2"],
        ["Nov 2025", "KlarnaUSD on Tempo"],
        ["Jan 2026", "P2P in 13 countries"],
        ["Jul 2026", "US bank charter applied for"],
        ["Aug 2026", "J.P. Morgan Payments live; guidance cut"],
    ],
    "l": {
        "U": {"d": 1, "s": "Shoppers may pay Klarna back with Mastercard cards; cardholders carry Visa.",
              "gap": "Shoppers fund Pay Now and repayments with cards on any network ⚠; Klarna Card holders carry Visa; merchants and PSPs take Klarna as a separate method.",
              "neo": "Shoppers paying with Mastercard debit ⚠, Mastercard Gateway merchants.", "snb": "Klarna Card holders, members, savers, P2P users."},
        "L5": {"d": 1, "s": "Mastercard Gateway is one of many distributors.", "gap": "The app and AI surfaces are Klarna's; PSPs from Stripe to J.P. Morgan carry it, Mastercard Gateway among them.",
               "neo": "Mastercard Gateway.", "snb": "App, Stripe, Adyen, Worldpay, Nexi, J.P. Morgan, ChatGPT, Gemini."},
        "L4": {"d": 0, "s": "The business lines run on Klarna's own network and Visa.", "gap": "Merchants, banking, memberships and markets have no Mastercard role; the members' metal card is Visa.",
               "neo": "None.", "snb": "Merchant network, banking, memberships, Klarna Mobile."},
        "L3": {"d": 0, "s": "Klarna runs its own services.", "gap": "Underwriting, scam tools, sign-in, AI, cashback and open banking are Klarna's; agent protocols are Google's.",
               "neo": "None.", "snb": "Underwriting, Inbox, AP2/UCP, PriceRunner, open banking."},
        "L2": {"d": 1, "s": "Mastercard funds payments; Visa carries the card.", "gap": "Mastercard cards fund Pay Now and repayments ⚠; the Klarna Card is Visa; financing, P2P, QR and KlarnaUSD use neither.",
               "neo": "Funding cards ⚠.", "snb": "Visa Flexible Credential, bank rails, Tempo."},
        "L1": {"d": 0, "s": "Klarna's own bank, funding and strategy.", "gap": "Nothing in the foundation is Mastercard's; the US charter could reopen network choice.",
               "neo": "None.", "snb": "Klarna Bank AB, deposits, forward flows, NYSE listing."},
    },
    "t": area_lens(LAYERS),
}
