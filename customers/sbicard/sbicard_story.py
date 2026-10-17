"""SBI Card's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from sbicard_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("India's largest pure-play credit-card issuer as five discs that stack into one platform, from 2.26 crore cards "
       "and State Bank of India's ownership at the bottom to the SBI Card app, SBI branches and partner apps at the top. "
       "Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up "
       "across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday cardholders", "user-round"),
    ("tier2", "New & Tier 2+ customers", "house"),
    ("digi", "Digital-platform shoppers", "smartphone"),
    ("prem", "Premium travellers", "plane"),
    ("corp", "Corporates", "briefcase-business"),
    ("partner", "Co-brand partners", "store"),
]
USERS_DESC = ("Six kinds of customer behind 2.26 crore cards: everyday cardholders, new and Tier 2+ customers, shoppers who "
              "live in partner apps, premium travellers, corporates, and the 22 brands that co-brand with SBI Card.")

WHO = {"con": "A cardholder", "tier2": "A first-time customer", "digi": "A platform shopper", "prem": "A frequent flyer",
       "corp": "A corporate", "partner": "A co-brand partner"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Pay with a card every day",
     "why": "The everyday loop: a core card, the app, the assistant and fraud checks.",
     "steps": [("2.1", "core", "Carry a SimplySAVE or PRIME card"), ("2.6", "mdes", "Tap with a phone"), ("5.1", "app", "Run it in the app"),
               ("3.3", "ila", "Ask ILA"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "upi", "who": "tier2", "name": "Pay by UPI on credit",
     "why": "RuPay credit cards linked to UPI, strongest in Tier 2+ towns.",
     "steps": [("2.4", "upicc", "Link a RuPay card to UPI"), ("2.2", "tataneu", "Earn NeuCoins on UPI"), ("3.4", "offers", "Use merchant offers")]},
    {"id": "first", "who": "tier2", "name": "Get a first card",
     "why": "Through an SBI branch or YONO, with a secured card if needed.",
     "steps": [("5.2", "banca", "Apply at SBI or in YONO"), ("3.2", "sprint", "Onboard digitally"), ("4.4", "advantage", "Start with a secured card")]},
    {"id": "platform", "who": "digi", "name": "Get a card inside a favourite app",
     "why": "Co-brands applied for and run inside PhonePe, Flipkart, Google Pay and Zomato.",
     "steps": [("5.4", "partnerapps", "Apply in the partner app"), ("3.2", "sprint", "Instant approval"), ("2.2", "flipkart", "Shop with Flipkart SBI Card"),
               ("2.2", "gpay", "Pay with Google Pay Flex")]},
    {"id": "travel", "who": "prem", "name": "Fly and earn",
     "why": "Airline co-brands and the premium range.",
     "steps": [("2.3", "krisflyer", "Earn KrisFlyer miles"), ("2.3", "indigo", "Earn IndiGo BluChips"), ("2.1", "aurum", "Upgrade to AURUM"),
               ("5.1", "travelbook", "Book trips in the app")]},
    {"id": "emi", "who": "con", "name": "Spread a big purchase",
     "why": "EMIs are a third of SBI Card's receivables.",
     "steps": [("3.4", "offers", "Find a festive offer"), ("4.1", "retail", "Buy on the card"), ("3.5", "emi", "Convert to EMIs")]},
    {"id": "corp", "who": "corp", "name": "Pay as a company",
     "why": "Corporate cards, whose spends tripled in FY26.",
     "steps": [("2.5", "corpcards", "Issue corporate cards"), ("3.1", "risk", "Monitored exposure")]},
    {"id": "partner", "who": "partner", "name": "Launch a co-brand",
     "why": "From Eternal in October 2026 back to KrisFlyer in 2024.",
     "steps": [("1.5", "deals", "Sign with SBI Card"), ("2.7", "netselect", "Choose networks"), ("2.2", "eternal", "Launch the card"),
               ("3.3", "hyper", "Personalise offers"), ("5.4", "partnerapps", "Sell in the app")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The international network on five of the eight newest co-brands, ELITE since 2016, and app tokens since 2020.",
     "steps": [("2.2", "eternal", "Eternal SBI Card"), ("2.2", "flipkart", "Flipkart SBI Card"), ("2.3", "krisflyer", "KrisFlyer SBI Card"),
               ("4.2", "apollo", "Apollo SBI Card SELECT"), ("2.1", "elite", "SBI Card ELITE"), ("2.6", "mdes", "MDES tokens")]},
    {"id": "mcnext", "who": "mc", "name": "Where renewals, agents and corporates could land",
     "why": "Where SBI Card has needs and Mastercard is not yet in: network choice at each renewal, the next platform co-brand, agentic payments with Flipkart and Zomato, fraud and identity for digital onboarding, and corporate-card controls.",
     "steps": [("2.7", "netselect", "Win the choice at renewal"), ("2.2", "gpay", "The next platform co-brand"), ("2.2", "eternal", "Agent Pay with Zomato"),
               ("3.2", "sprint", "Identity checks for SPRINT"), ("3.1", "fraud", "Fraud scoring"), ("2.5", "corpcards", "Corporate-card controls")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across SBI Card's map",
    "title": "One of four networks, winning co-brands card by card",
    "lead": "SBI Card issues on Visa, Mastercard, RuPay and American Express and publishes no network split. Mastercard carried its first premium card in 2016 and its app tokens in 2020, and since 2024 has been the international network on KrisFlyer, Apollo, Flipkart, IndiGo and, in October 2026, Eternal. Visa has Tata Neu, PhonePe and Google Pay, and RuPay sits on almost every new card for UPI. Since September 2024 the RBI has made every issue and renewal a choice. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are SBI Card's own (Q1 FY27 presentation, 24 July 2026; Annual Report 2025-26) or from launch coverage. SBI Card's card pages could not be read, so networks for the core range, corporate and partner-bank cards are unconfirmed, and IndiGo's rests on one secondary source.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Networks", "Four", "Visa, Mastercard, RuPay, Amex; no split ⚠"],
        ["Newest co-brand", "Eternal", "Mastercard and RuPay, October 2026"],
        ["Co-brands since 2024", "Mastercard on five of eight", "Visa on four, RuPay on six"],
        ["Premium", "ELITE", "Mastercard World at launch, 2016"],
        ["Tokens", "MDES", "App tap-to-pay, 2020 ⚠"],
        ["UPI credit", "RuPay", "60%+ of RuPay base linked"],
        ["Rule", "Network choice", "At issue and renewal since Sep 2024"],
        ["Corporate cards", "Not disclosed", "₹76,595 crore spends in FY26"],
    ],
    "sides": {
        "neo": {"dir": "The international variant on Eternal, Flipkart, KrisFlyer, Apollo and IndiGo, ELITE and part of the core and premium range, and app tokens.",
                "deals": "What it does not do: UPI credit, fraud and credit models, onboarding, personalisation or offers."},
        "snb": {"dir": "Visa on Tata Neu, PhonePe, Google Pay and much of the core range, RuPay for UPI, Amex on KrisFlyer, and SBI Card's own AI and onboarding.",
                "deals": "Where they meet: every new card and renewal, chosen under the RBI rule."},
    },
    "tl": [
        ["Jul 2016", "SBI Card ELITE on Mastercard World"],
        ["Sep 2019", "RuPay partnership"],
        ["Nov 2020", "App contactless on Mastercard tokens"],
        ["Jul 2021", "RBI bars Mastercard from new cardholders (to Jun 2022)"],
        ["2023", "RuPay credit cards on UPI"],
        ["Sep 2024", "RBI network choice; KrisFlyer on Amex and Mastercard"],
        ["2025", "Tata Neu and PhonePe on Visa; Apollo, Flipkart, IndiGo on Mastercard"],
        ["Jul 2026", "Google Pay Flex on RuPay and Visa"],
        ["Oct 2026", "Eternal SBI Card on Mastercard and RuPay"],
    ],
    "l": {
        "U": {"d": 1, "s": "Many cardholders carry Mastercard; many carry Visa or RuPay.",
              "gap": "Network depends on the card and, since 2024, the customer's choice; no split is published.",
              "neo": "Platform shoppers on Flipkart and Eternal, frequent flyers, some core and premium cardholders.",
              "snb": "UPI users on RuPay, Tata Neu, PhonePe and Google Pay holders on Visa, KrisFlyer holders on Amex."},
        "L5": {"d": 0, "s": "The front doors are SBI Card's, SBI's and partners'.", "gap": "App, branches, sales force and partner apps carry no network.",
               "neo": "None.", "snb": "App, SBI and YONO, open market, partner apps."},
        "L4": {"d": 1, "s": "Card credit runs on every network.", "gap": "Apollo is on Mastercard; partner-bank and secured cards are undisclosed.",
               "neo": "Apollo SELECT, part of card spend.", "snb": "RuPay and Visa spend, partner-bank and secured cards."},
        "L3": {"d": 0, "s": "Services are SBI Card's own.", "gap": "Fraud, credit, onboarding, personalisation and offers are built in-house or with Oracle.",
               "neo": "None named.", "snb": "In-house AI, SPRINT, Oracle, Ask ILA."},
        "L2": {"d": 1, "s": "Mastercard shares most card rails; RuPay owns UPI.", "gap": "Mastercard is the international network on five new co-brands and ran app tokens; Visa has three platform co-brands.",
               "neo": "Eternal, Flipkart, KrisFlyer, IndiGo, ELITE, MDES.", "snb": "Visa co-brands, RuPay on UPI, Amex, undisclosed corporate cards."},
        "L1": {"d": 0, "s": "The company's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, SBI, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
