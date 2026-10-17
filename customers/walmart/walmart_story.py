"""Walmart's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from walmart_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("The world's largest retailer, read through payments, as five discs that stack into one platform, from "
       "$713.2 billion of revenue at the bottom to the stores, apps and AI assistants at the top. Click the stack to "
       "open it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("shop", "Shoppers", "user-round"),
    ("plus", "Walmart+ members", "gift"),
    ("onepay", "OnePay customers", "wallet"),
    ("sams", "Sam's Club members", "building-2"),
    ("seller", "Marketplace sellers & advertisers", "store"),
    ("intl", "Customers in India, Mexico & Canada", "earth"),
]
USERS_DESC = ("Six kinds of user: shoppers at 11,000 stores and online, Walmart+ members, OnePay's banking and card "
              "customers, Sam's Club members, the sellers and brands on the marketplace and Walmart Connect, and the "
              "customers of PhonePe, super.money, Cashi and Walmart Canada.")

WHO = {"shop": "A shopper", "plus": "A Walmart+ member", "onepay": "A OnePay customer", "sams": "A Sam's Club member",
       "seller": "A seller", "intl": "A customer abroad"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "shop", "who": "shop", "name": "Shop and pay at Walmart",
     "why": "The everyday loop: a store or the app, then tap, Walmart Pay or any card.",
     "steps": [("5.1", "stores", "Walk into a store"), ("4.1", "walmartus", "Buy from Walmart"),
               ("2.3", "taptopay", "Tap a card or phone"), ("2.3", "walmartpay", "Or pay by QR with Walmart Pay")]},
    {"id": "plus", "who": "plus", "name": "Get the most from Walmart+",
     "why": "Membership, 5% back on the OnePay Mastercard and fuel discounts through the app.",
     "steps": [("3.1", "walmartplus", "Join Walmart+"), ("2.1", "cashrewards", "Earn 5% with the OnePay card"),
               ("5.2", "walmartapp", "Save on fuel in the app")]},
    {"id": "onepay", "who": "onepay", "name": "Bank with OnePay",
     "why": "An account, a card to build credit, crypto and AI tools in one app.",
     "steps": [("5.2", "onepayapp", "Open the OnePay app"), ("4.3", "onepaycash", "Get paid into OnePay Cash"),
               ("2.1", "buildercard", "Build credit with the Builder Card"), ("2.6", "crypto", "Buy bitcoin")]},
    {"id": "borrow", "who": "onepay", "name": "Spread the cost",
     "why": "Klarna instalments, Upgrade loans or the Walmart-only card.",
     "steps": [("2.4", "klarna", "Pay over time with Klarna"), ("2.4", "upgrade", "Take a personal loan"),
               ("2.1", "spendcard", "Or use the Spend Card")]},
    {"id": "sams", "who": "sams", "name": "Shop at Sam's Club",
     "why": "Membership, Scan & Go and the Sam's Club Mastercard.",
     "steps": [("3.1", "samsmembership", "Join Sam's Club"), ("4.2", "samsclub", "Shop the club"),
               ("2.2", "samsmc", "Pay with the Sam's Club Mastercard")]},
    {"id": "agent", "who": "shop", "name": "Let an assistant shop and plan",
     "why": "Sparky in ChatGPT and Gemini, UCP checkout, and OnePay's data for AI tools.",
     "steps": [("5.3", "aiplugins", "Ask in ChatGPT or Gemini"), ("3.2", "sparky", "Build a basket with Sparky"),
               ("3.2", "ucp", "Check out through UCP"), ("3.2", "onepayagents", "Share OnePay data with an agent")]},
    {"id": "seller", "who": "seller", "name": "Sell and advertise on Walmart",
     "why": "The marketplace, fulfilment and Walmart Connect.",
     "steps": [("4.1", "marketplace", "List on the marketplace"), ("3.4", "connect", "Advertise with Walmart Connect"),
               ("2.3", "accept", "Get paid for card sales")]},
    {"id": "intl", "who": "intl", "name": "Pay with Walmart abroad",
     "why": "UPI in India, Cashi in Mexico and a bank partner in Canada.",
     "steps": [("4.4", "phonepe", "Pay by UPI on PhonePe"), ("4.4", "supermoney", "Use super.money's RuPay card"),
               ("4.5", "cashi", "Open a Cashi account"), ("4.6", "bmo", "Bank with BMO at Walmart Canada")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Walmart's two flagship US credit cards, acceptance everywhere, contactless from August 2026, and the UCP standard.",
     "steps": [("2.1", "cashrewards", "OnePay CashRewards Mastercard"), ("2.2", "samsmc", "Sam's Club Mastercard"),
               ("2.3", "accept", "Mastercard accepted in every store"), ("2.3", "taptopay", "Contactless and wallet tokens"),
               ("3.2", "ucp", "A UCP supporter")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, tokens and OnePay could land",
     "why": "Where Walmart has needs and Mastercard is not yet in: agent payments for Sparky and OnePay, tokens on the new NFC estate, OnePay's unnamed debit and builder networks, instalments, fraud and remittances, and a way through the fee fight.",
     "steps": [("3.2", "onepayagents", "Agent Pay behind OnePay's AI tools"), ("3.2", "sparky", "Agentic tokens for Sparky"),
               ("2.1", "buildercard", "Network for the Builder Card"), ("4.3", "onepaycash", "Network for OnePay debit"),
               ("2.4", "klarna", "Instalments on the OnePay card"), ("2.5", "moneyservices", "Move for money transfers"),
               ("1.4", "objection", "A merchant deal beyond the settlement")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Walmart's map",
    "title": "Mastercard carries Walmart's cards while Walmart fights its fees",
    "lead": "Mastercard carries Walmart's two flagship US credit cards, the OnePay CashRewards card and the Sam's Club card, both issued by Synchrony, and every Walmart store takes Mastercard, now contactless too. But Walmart is the lead objector to the Visa–Mastercard fee settlement, and its fintech, OnePay, sends instalments to Klarna, crypto to Zerohash and stablecoin payouts to Tempo. Abroad, PhonePe and super.money run on UPI and RuPay. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Walmart's own (Q2 FY27 results, 20 August 2026; FY26 10-K) or from OnePay, Synchrony, Klarna and press. Walmart does not publish a network split. OnePay debit, the Builder Card, Cashi, Walmex co-brands, Flipkart's Axis card and Walmart Canada's card networks are unconfirmed.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["OnePay CashRewards", "Mastercard", "Synchrony, since autumn 2025"],
        ["Sam's Club card", "Mastercard", "Synchrony, renewed January 2025"],
        ["Previous Walmart card", "Mastercard", "Capital One, 2019 to 2024"],
        ["Instalments", "Klarna", "Exclusive via OnePay since March 2025"],
        ["In-store checkout", "Every network", "Contactless from 24 August 2026"],
        ["Fee settlement", "Walmart objects", "Final hearing 16 November 2026"],
        ["India", "UPI and RuPay", "PhonePe, super.money"],
        ["Stablecoins", "Tempo, Open USD", "OnePay, 2026"],
    ],
    "sides": {
        "neo": {"dir": "The OnePay CashRewards and Sam's Club credit cards, acceptance in every store and online, contactless and wallet tokens from August 2026, and a seat beside Walmart in UCP and Open USD.",
                "deals": "What it does not do: instalments, OnePay debit or credit-builder (networks unstated), agent payments, AML, money transfers, or anything in India."},
        "snb": {"dir": "Klarna's instalments, Synchrony's closed-loop Spend Card, Green Dot's MoneyCard (Visa named), Zerohash and Tempo for crypto and stablecoins, UPI and RuPay in India, Interac in Canada, and Visa as co-defendant in the fee case.",
                "deals": "Where they meet: every card payment at the till, and the courtroom in Brooklyn."},
    },
    "tl": [
        ["2016", "Walmart Pay launched, QR only"],
        ["2018", "Majority stakes in Flipkart and PhonePe"],
        ["2019", "Walmart card moves to Capital One, on Mastercard"],
        ["2021", "OnePay set up with Ribbit Capital"],
        ["Jan 2025", "Sam's Club Mastercard renewed with Synchrony"],
        ["Mar 2025", "Klarna exclusive for OnePay instalments"],
        ["Jun 2025", "OnePay CashRewards Mastercard announced"],
        ["Dec 2025", "Walmart asks to leave the merchant class"],
        ["Jan 2026", "UCP with Google; PhonePe IPO cleared"],
        ["Jun 2026", "Settlement preliminarily approved; OnePay for Agents"],
        ["Aug 2026", "Tap to pay arrives in US stores"],
        ["Oct 2026", "OnePay inside ChatGPT and Dots"],
        ["Nov 2026", "Final approval hearing (scheduled)"],
    ],
    "l": {
        "U": {"d": 1, "s": "Shoppers can pay with Mastercard; the flagship cards are Mastercard.",
              "gap": "OnePay CashRewards and Sam's Club card holders carry Mastercard; Klarna borrowers, Spend Card holders and India's UPI users do not.",
              "neo": "OnePay and Sam's Club cardholders, every card shopper.", "snb": "Klarna borrowers, Spend Card holders, PhonePe and super.money users."},
        "L5": {"d": 1, "s": "Stores take every network; the apps and AI doors are Walmart's.", "gap": "Contactless brings Mastercard tokens to the tills; the apps and AI plugins name no network.",
               "neo": "Wallet tokens at the till.", "snb": "Walmart, Sam's Club and OnePay apps, ChatGPT and Gemini."},
        "L4": {"d": 1, "s": "US stores and clubs take Mastercard; the fintech and India lines mostly do not.", "gap": "Stores accept every network; OnePay debit and Cashi networks are unstated; India runs on UPI and RuPay.",
               "neo": "Acceptance at Walmart U.S. and Sam's Club.", "snb": "PhonePe, super.money, BMO and Interac."},
        "L3": {"d": 1, "s": "Mastercard supports UCP; the agents and AML are Walmart's own.", "gap": "Sparky and OnePay for Agents name no payment rail; fraud and AML agents are built in-house.",
               "neo": "UCP support.", "snb": "Sparky, OnePay for Agents, OnePay's AML agent, Walmart Connect."},
        "L2": {"d": 2, "s": "The flagship credit cards ride on Mastercard; credit and crypto do not.", "gap": "CashRewards and Sam's Club are Mastercard; Klarna, Upgrade, Zerohash and Tempo are off the networks.",
               "neo": "OnePay CashRewards, Sam's Club Mastercard, acceptance.", "snb": "Klarna, Spend Card, Zerohash, Tempo, MoneyCard (Visa named)."},
        "L1": {"d": 0, "s": "Walmart's own scale, and a fight over fees.", "gap": "Nothing in the foundation is Mastercard's, and Walmart is the lead objector to the settlement on its fees.",
               "neo": "None.", "snb": "Revenue, leadership, partner banks, the settlement objection."},
    },
    "t": area_lens(LAYERS),
}
