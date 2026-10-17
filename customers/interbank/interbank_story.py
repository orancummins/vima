"""Interbank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from interbank_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Peru's consumer-lending bank as five discs that stack into one platform, from S/52.6 billion of loans at the "
       "bottom to the Interbank app, One App Negocios and the branches at the top. Click the stack to open it. Choose who "
       "you are and what you want to do, and the areas that deliver it light up across the layers, joined in the order "
       "they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("home", "Homebuyers", "house"),
    ("merch", "Merchants", "store"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates", "factory"),
    ("aff", "Savers & policyholders", "coins"),
]
USERS_DESC = ("Six kinds of customer: everyday customers, 86% of them digital, homebuyers, merchants taking payments "
              "through Izipay, small businesses, corporates and the savers and policyholders served by Inteligo and Interseguro.")

WHO = {"con": "An Interbank customer", "home": "A homebuyer", "merch": "A merchant", "sme": "A small business",
       "corp": "A corporate treasurer", "aff": "A saver"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: the app, a Visa debit card, Plin and fraud alerts.",
     "steps": [("5.1", "app", "Open the Interbank app"), ("2.2", "debit", "Pay with Visa debit"), ("2.4", "plin", "Send money with Plin"),
               ("2.5", "interop", "Pay a Yape user"), ("3.1", "fraud", "Get a fraud alert")]},
    {"id": "card", "who": "con", "name": "Borrow on a card",
     "why": "Visa first, Amex for the premium end, a small Mastercard range, and miles on all of them.",
     "steps": [("2.1", "visacredit", "Take a Visa card"), ("2.1", "amex", "Or an Amex"), ("2.4", "plincredit", "Pay through Plin with it"),
               ("3.3", "millas", "Earn Millas Benefit")]},
    {"id": "loan", "who": "con", "name": "Take a loan against my salary",
     "why": "Payroll and personal loans, the heart of the consumer book.",
     "steps": [("3.2", "analytics", "Get a credit decision"), ("4.1", "payroll", "Take a payroll loan"), ("5.1", "app", "Track it in the app")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "A 16% share of mortgages, including MiVivienda.",
     "steps": [("5.3", "branches", "Talk to a branch"), ("4.2", "mortgages", "Take a mortgage"), ("4.5", "interseguro", "Insure it with Interseguro")]},
    {"id": "merchant", "who": "merch", "name": "Take payments",
     "why": "Izipay terminals, phones as POS and QR for every wallet.",
     "steps": [("2.3", "izipay", "Accept cards with Izipay"), ("2.3", "tapphone", "Use a phone as a terminal"),
               ("2.3", "izipayya", "Take wallet QR payments"), ("5.4", "ecosystem", "Sell Interbank products at the counter")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "Banking and acquiring sold together in one app.",
     "steps": [("4.3", "smallbiz", "Open a business account"), ("5.2", "oneapp", "Run it in One App Negocios"),
               ("2.3", "izipay", "Collect with Izipay"), ("4.1", "consumer", "Borrow to grow")]},
    {"id": "corp", "who": "corp", "name": "Finance a company",
     "why": "Commercial lending, trade finance and treasury.",
     "steps": [("4.4", "commercial", "Borrow for working capital"), ("4.4", "capmkts", "Hedge foreign exchange")]},
    {"id": "wealth", "who": "aff", "name": "Save and invest",
     "why": "Inteligo and Interseguro inside the IFS group.",
     "steps": [("4.5", "inteligo", "Invest with Inteligo"), ("4.5", "interseguro", "Buy an annuity")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "A small Mastercard credit range, Izipay acquiring with Mastercard roots, and card rails behind Plin at launch.",
     "steps": [("2.1", "mccredit", "Mastercard credit cards"), ("2.3", "izipay", "Izipay acquires Mastercard"),
               ("2.4", "plin", "Card rails behind Plin at launch")]},
    {"id": "mcnext", "who": "mc", "name": "Where Izipay, Plin and agents could land",
     "why": "Where Interbank has needs and Mastercard is not yet in: merchant data and risk at Izipay, tokenised cards in Plin, fraud controls, card-linked offers, agentic payments and business cards.",
     "steps": [("2.3", "izipay", "Merchant risk and data at Izipay"), ("2.4", "plincredit", "Tokenised cards in Plin"),
               ("3.1", "fraud", "Scam and fraud scoring"), ("3.3", "millas", "Card-linked offers"),
               ("3.2", "avi", "Agent Pay for the assistant"), ("4.3", "smallbiz", "Business cards")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Interbank's map",
    "title": "A Visa and Amex issuer that owns Mastercard's old acquirer",
    "lead": "Interbank's main credit and debit cards run on Visa, and it is one of Peru's two American Express issuers. Mastercard keeps a small credit range ⚠. Its deeper tie is Izipay, once Peru's Mastercard acquirer and now wholly owned by the group and accepting every network. Plin, the bank wallet, used card rails at launch ⚠. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (IFS 2Q26 results, 11 August 2026; Interbank 2025 annual report) or from Izipay, comparison sites and press. interbank.pe refused automated requests, so card networks rest partly on comparison sites.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Credit", "Visa", "Clásica to Infinite"],
        ["Premium", "American Express", "Issued with BCP, about 25 years ⚠"],
        ["Mastercard", "Clásica, Oro, Platinum", "Small range ⚠"],
        ["Debit", "Visa", "Débito Benefit ⚠"],
        ["Acquiring", "Izipay", "Mastercard's acquirer from 1999 ⚠; 45%+ share"],
        ["Wallet", "Plin", "2.8 million monthly users"],
        ["AI", "Anthropic", "August 2026"],
    ],
    "sides": {
        "neo": {"dir": "A small Mastercard credit range, Mastercard acceptance at Izipay's merchants, and card rails behind Plin at launch.",
                "deals": "What it does not do: the main credit and debit books, premium cards, loyalty, fraud tools or AI."},
        "snb": {"dir": "Visa credit, debit and the Vea co-brand, Amex at the premium end, Plin and Yape as account-to-account rails, and Interbank's own fraud, loyalty and AI.",
                "deals": "Where they meet: Izipay, which acquires every network."},
    },
    "tl": [
        ["1999", "PMP starts acquiring Mastercard ⚠"],
        ["2004", "Vea co-brand card"],
        ["Jan 2020", "Plin launched"],
        ["2020", "Izipay licensed for Visa"],
        ["Apr 2022", "IFS takes 100% of Izipay"],
        ["Sep 2023", "Wallet interoperability; Rappibank ends"],
        ["May 2024", "Carlos Tori, ex-payments head, becomes CEO"],
        ["2026", "Plin with credit card"],
        ["Aug 2026", "Anthropic agreement; 2Q26 ROE 15.6%"],
    ],
    "l": {
        "U": {"d": 1, "s": "A few cardholders and Izipay's merchants touch Mastercard.",
              "gap": "Most cardholders carry Visa or Amex; merchants accept Mastercard through Izipay.",
              "neo": "Mastercard cardholders, merchants accepting Mastercard.", "snb": "Visa and Amex cardholders, Plin users, borrowers, savers."},
        "L5": {"d": 0, "s": "The front doors are Interbank's.", "gap": "App, One App Negocios, branches and Intercorp retail are the group's.", "neo": "None.", "snb": "Apps, branches, Intercorp partners."},
        "L4": {"d": 0, "s": "The business lines carry Visa cards.", "gap": "Small business is partly touched through Izipay; lending, mortgages and insurance have no network role.",
               "neo": "Izipay acquiring for small businesses.", "snb": "Consumer, payroll, mortgages, commercial, insurance and wealth."},
        "L3": {"d": 0, "s": "Services are Interbank's own.", "gap": "Fraud alerts, AVI, data science and Millas Benefit are in-house; open banking has no public detail.",
               "neo": "None.", "snb": "Fraud tools, AVI, Millas Benefit, Visa Cashback."},
        "L2": {"d": 1, "s": "Visa issues; Izipay acquires every network.", "gap": "Visa has credit and debit and Amex the premium range; Mastercard has a small credit range, Izipay acceptance and Plin's launch rails ⚠.",
               "neo": "Mastercard credit, Izipay acceptance, Plin at launch ⚠.", "snb": "Visa credit and debit, Amex, wallet interoperability."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, ownership, brand, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
