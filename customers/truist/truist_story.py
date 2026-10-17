"""Truist's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from truist_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("A top-10 US bank as five discs that stack into one platform, from $554 billion of assets and a new CEO at the "
       "bottom to Truist Mobile, 1,912 branches and One View at the top. Click the stack to open it. Choose who you are "
       "and what you want to do, and the areas that deliver it light up across the layers, joined in the order they act. "
       "Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("prem", "Premier & wealth clients", "gem"),
    ("borrow", "Homeowners & borrowers", "house"),
    ("sme", "Small businesses", "store"),
    ("corp", "Companies & institutions", "building-2"),
    ("dealer", "Dealers & contractors", "factory"),
]
USERS_DESC = ("Six kinds of client across the Southeast, the Mid-Atlantic and Texas: everyday customers, the mass-affluent "
              "Premier and wealth clients Truist is building branches for, borrowers, small businesses, the companies "
              "Wholesale Banking serves, and the dealers and contractors who sell its loans.")

WHO = {"con": "A Truist customer", "prem": "A Premier client", "borrow": "A borrower", "sme": "A small business",
       "corp": "A corporate treasurer", "dealer": "A dealer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: Truist One checking, a Visa debit card, the app, AI nudges and Zelle.",
     "steps": [("4.1", "checking", "Open Truist One checking"), ("2.1", "debit", "Pay with a Visa debit card"),
               ("5.1", "app", "Run it in Truist Mobile"), ("3.2", "insights", "Get a Truist Insights nudge"),
               ("3.2", "assist", "Ask Truist Assist"), ("2.5", "zelle", "Send money with Zelle")]},
    {"id": "switch", "who": "con", "name": "Make Truist your main bank",
     "why": "Open online, move your pay with Atomic, connect your apps through Mastercard and earn cashback.",
     "steps": [("5.1", "app", "Open an account online"), ("3.1", "dds", "Switch your direct deposit"),
               ("3.1", "openbanking", "Connect your fintech apps"), ("3.4", "offers", "Earn Truist Deals cashback")]},
    {"id": "cards", "who": "con", "name": "Borrow and earn on a card",
     "why": "Truist's consumer cards are all Visa; Delta debit cardholders move to a standard card after 31 October.",
     "steps": [("2.2", "enjoy", "Take an Enjoy card"), ("3.4", "offers", "Add Truist Deals"),
               ("2.1", "delta", "Swap a Delta SkyMiles debit card")]},
    {"id": "premier", "who": "prem", "name": "Step up to Premier and Wealth",
     "why": "The mass-affluent ladder the new branches are built for.",
     "steps": [("5.2", "advisors", "Meet a Premier adviser"), ("4.1", "premier", "Move up to Premier Banking"),
               ("4.5", "wealth", "Invest with Truist Wealth"), ("2.7", "crypto", "Add a spot bitcoin ETF")]},
    {"id": "borrow", "who": "borrow", "name": "Finance a home, a boat or a kitchen",
     "why": "Mortgages in the footprint, and specialty loans sold at the dealer or by the contractor.",
     "steps": [("4.3", "mortgage", "Take a mortgage or home-equity line"), ("5.4", "dealers", "Apply at the dealer"),
               ("4.3", "sheffield", "Finance a bike or boat with Sheffield"), ("4.3", "servicefinance", "Pay for a remodel with Service Finance")]},
    {"id": "smallbiz", "who": "sme", "name": "Run a small business",
     "why": "Business banking, a Visa Infinite card, card acceptance on Merchant Engage and Zelle.",
     "steps": [("4.2", "smallbiz", "Open business banking"), ("2.2", "bizcards", "Carry a Business Premium Visa Infinite"),
               ("2.4", "engage", "Run banking and payments in Merchant Engage"), ("2.4", "merchant", "Take cards"),
               ("2.5", "zelle", "Get paid by Zelle")]},
    {"id": "corp", "who": "corp", "name": "Run a company's payments",
     "why": "Wholesale Banking's core: a relationship banker, One View, treasury, commercial cards and RTP.",
     "steps": [("4.4", "commercial", "Bank with Commercial Banking"), ("5.3", "oneview", "Work in One View or the ERP"),
               ("2.6", "treasury", "Use treasury management"), ("2.3", "commcards", "Give staff One Cards"),
               ("2.3", "epayables", "Pay suppliers by virtual card"), ("2.5", "rtp", "Bill by Request for Payment")]},
    {"id": "dealer", "who": "dealer", "name": "Offer financing on the showroom floor",
     "why": "Sheffield and Service Finance sell Truist credit through manufacturers, dealers and contractors.",
     "steps": [("5.4", "dealers", "Join a manufacturer programme"), ("4.3", "sheffield", "Offer Sheffield finance"),
               ("2.4", "merchant", "Take card payments")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Open banking, part of the commercial card book and virtual payables, Mastercard-backed Pollinate and acceptance.",
     "steps": [("3.1", "openbanking", "Open banking on Mastercard's platform"), ("2.3", "commcards", "Truist Mastercard commercial cards"),
               ("2.3", "epayables", "ePayables on Visa or Mastercard"), ("2.4", "engage", "Merchant Engage on Pollinate"),
               ("2.4", "merchant", "Mastercard acceptance")]},
    {"id": "mcnext", "who": "mc", "name": "Where open finance, commercial cards and fraud tools could land",
     "why": "Where Truist has needs and Mastercard is not yet in: open finance for lending and pay-by-bank, a bigger commercial and virtual card share, acquirer tools in Merchant Engage, scam scoring on real-time rails, Agent Pay and cross-border.",
     "steps": [("3.1", "openbanking", "Open finance for thin-file lending and pay-by-bank"), ("2.3", "epayables", "Virtual cards for Wholesale Payments"),
               ("2.4", "engage", "Acquirer risk and SMB insights"), ("3.3", "fraud", "Scam scoring for Zelle and RTP"),
               ("3.2", "assist", "Agent Pay for Truist Assist"), ("2.7", "zelleusd", "Cross-border against ZelleUSD")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Truist's map",
    "title": "A Visa bank that opened its data to Mastercard",
    "lead": "Truist's consumer debit and credit cards, its small business cards and its gift cards are Visa, and in October 2025 it launched the first Visa Business Infinite card at a super-regional bank. Mastercard carries part of the commercial card book, became Truist's first open banking partner in February 2026, and backs Pollinate, which runs Truist Merchant Engage. A new CEO from Fiserv is reviewing the whole franchise. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Truist's own (3Q26 results, 16 October 2026; 2025 Form 10-K) or from Truist, Mastercard and press. Truist publishes no network agreement, no split of commercial cards by network and no network for the Delta debit card.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa", "Delta SkyMiles debit ends 31 Oct 2026"],
        ["Consumer credit", "Visa", "Enjoy, Future, Secured; about $4.9bn of card loans"],
        ["Small business", "Visa", "Business Premium Visa Infinite, Oct 2025"],
        ["Commercial cards", "Visa and Mastercard", "Split not published ⚠"],
        ["Open banking", "Mastercard", "First direct API partner, Feb 2026"],
        ["Merchant platform", "Pollinate", "Mastercard-backed ⚠; Merchant Engage, Jul 2025"],
        ["P2P and real time", "Zelle, RTP", "Truist co-owns Early Warning"],
        ["CEO", "Mike Lyons", "Ex-Fiserv, from 1 Sep 2026"],
    ],
    "sides": {
        "neo": {"dir": "Open banking for consumers and small businesses, part of the commercial and virtual card book, acceptance at Truist's merchants, and the Pollinate platform it backs.",
                "deals": "What it does not do: consumer debit and credit, small business cards, Zelle, RTP or Truist's AI."},
        "snb": {"dir": "Visa debit, credit, small business and gift cards; Zelle and RTP; TSYS processing; Atomic switching; Truist's own AI and fraud models.",
                "deals": "Where they meet: commercial cards, where both networks issue."},
    },
    "tl": [
        ["2019", "BB&T and SunTrust form Truist"],
        ["May 2020", "TSYS to process a Visa and Mastercard credit book"],
        ["Aug 2020", "Mastercard and Pollinate partner"],
        ["Apr 2025", "First alias-based Request for Payment on RTP"],
        ["Jul 2025", "Truist Merchant Engage on Pollinate"],
        ["Oct 2025", "Business Premium Visa Infinite"],
        ["Feb 2026", "Open banking on Mastercard's platform"],
        ["Jun 2026", "Mike Lyons named CEO; ZelleUSD unveiled ⚠"],
        ["Oct 2026", "LightStream sale; new consumer leaders"],
        ["31 Oct 2026", "Delta SkyMiles debit ends"],
    ],
    "l": {
        "U": {"d": 1, "s": "Some commercial cardholders carry Mastercard; consumers carry Visa.",
              "gap": "Consumer and small business cardholders carry Visa; part of the commercial card base carries Mastercard.",
              "neo": "Commercial cardholders on Mastercard, open banking users.", "snb": "Consumer, Premier and small business cardholders."},
        "L5": {"d": 0, "s": "The front doors are Truist's.", "gap": "Truist Mobile, branches, One View and dealers are Truist's own.",
               "neo": "None.", "snb": "App, branches, One View, dealers."},
        "L4": {"d": 1, "s": "Commercial banking carries some Mastercard cards.", "gap": "Accounts come with Visa debit; lending and wealth have no network role; commercial clients use cards on both.",
               "neo": "Commercial card clients.", "snb": "Checking, Premier, lending, Truist Securities, Wealth."},
        "L3": {"d": 1, "s": "Open banking is Mastercard's; the rest is Truist's.", "gap": "Mastercard runs open banking connections; AI, fraud and offers are Truist's or unnamed vendors'.",
               "neo": "Open banking.", "snb": "Truist Insights, Truist Assist, Atomic, fraud models."},
        "L2": {"d": 1, "s": "Commercial cards and acceptance partly Mastercard; the rest Visa or Zelle.", "gap": "Visa holds debit, consumer and small business credit; Mastercard shares commercial cards; Zelle and RTP move money between accounts.",
               "neo": "Commercial and virtual cards, acceptance, Pollinate.", "snb": "Visa cards, Zelle, RTP, treasury."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's; TSYS processes the cards.",
               "neo": "None.", "snb": "Capital, leadership, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
