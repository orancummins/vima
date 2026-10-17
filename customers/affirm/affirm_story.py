"""Affirm Holdings' kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from affirm_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("The pay-over-time lender as five discs that stack into one platform, from $50.2 billion of GMV and its partner "
       "banks at the bottom to the Affirm app, checkout integrations and processors at the top. Click the stack to open it. "
       "Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined in the "
       "order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("shop", "Shoppers", "user-round"),
    ("card", "Cardholders", "wallet-cards"),
    ("merch", "Merchants", "store"),
    ("ent", "Enterprises & platforms", "building-2"),
    ("bank", "Banks & credit unions", "landmark"),
    ("inv", "Capital partners", "briefcase"),
]
USERS_DESC = ("Six kinds of user: 27.8 million shoppers, the 5.2 million who carry the Affirm Card, about 571,000 merchants, "
              "enterprises and platforms from Amazon to Shopify, banks and credit unions through Fiserv, and the investors "
              "who fund the loans.")

WHO = {"shop": "A shopper", "card": "A cardholder", "merch": "A merchant", "ent": "An enterprise",
       "bank": "A bank", "inv": "A capital partner"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "buy", "who": "shop", "name": "Buy online over time",
     "why": "The core loop: Affirm at checkout, a decision in real time, a fixed monthly plan and repayments in the app.",
     "steps": [("5.2", "sdk", "See Affirm at checkout"), ("3.1", "underwriting", "Get a decision in real time"),
               ("2.1", "monthly", "Choose a monthly plan"), ("2.4", "repay", "Repay in the app")]},
    {"id": "split", "who": "shop", "name": "Split a smaller purchase",
     "why": "Pay in 4 through Shop Pay Installments, often with a merchant-funded offer.",
     "steps": [("4.4", "shopify", "Pick Shop Pay Installments"), ("2.1", "payin4", "Pay in 4 at 0%"),
               ("3.2", "adaptai", "Take a merchant-funded offer")]},
    {"id": "card", "who": "card", "name": "Use the Affirm Card",
     "why": "A Visa debit card that can turn any purchase into a plan, with Affirm Money beside it.",
     "steps": [("2.2", "affirmcard", "Pay with the Affirm Card (Visa)"), ("2.2", "visaflex", "Switch a purchase to a plan"),
               ("4.2", "cardoffers", "Use a 0% offer"), ("4.2", "money", "Keep savings in Affirm Money")]},
    {"id": "instore", "who": "shop", "name": "Pay later in a shop",
     "why": "Apple Pay, one-time Visa virtual cards and the card itself.",
     "steps": [("2.3", "applepay", "Choose Affirm in Apple Pay"), ("2.3", "vcn", "Pay with a one-time Visa card"),
               ("5.4", "instore", "Or tap the Affirm Card")]},
    {"id": "merch", "who": "merch", "name": "Offer Affirm at checkout",
     "why": "Switch Affirm on through a processor, show tailored plans and get paid up front.",
     "steps": [("5.3", "stripe", "Switch it on through Stripe"), ("5.3", "worldpay", "Or through Worldpay"),
               ("3.2", "adaptive", "Show tailored plans"), ("2.4", "settlement", "Get paid by Affirm")]},
    {"id": "ent", "who": "ent", "name": "Run an enterprise programme",
     "why": "Amazon-scale checkout, merchant-funded 0% and new channels in AI agents.",
     "steps": [("4.4", "amazon", "Offer Affirm on Amazon"), ("2.1", "zeroapr", "Fund 0% APR plans"),
               ("3.2", "adaptai", "Test offers with AdaptAI"), ("3.3", "ap2", "Sell through AI agents")]},
    {"id": "bank", "who": "bank", "name": "Add pay over time to our debit cards",
     "why": "Fiserv banks and credit unions offer Affirm plans on their own cards; Affirm Edge comes next.",
     "steps": [("2.5", "fiservdebit", "Offer Affirm plans via Fiserv"), ("3.1", "underwriting", "Let Affirm underwrite and fund"),
               ("3.4", "edge", "Run our own programme on Affirm Edge")]},
    {"id": "fund", "who": "inv", "name": "Fund Affirm's loans",
     "why": "Forward flow, securitisations and a $30 billion funding stack.",
     "steps": [("1.5", "forwardflow", "Buy loans through forward flow"), ("1.5", "funding", "Invest in Affirm's ABS"),
               ("4.1", "loanbook", "Track the loan book")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "At the edges: Mastercard Gateway lists Affirm, Fiserv banks' debit cards may carry Affirm plans, and both back Google's AP2.",
     "steps": [("5.3", "mcgw", "Affirm on Mastercard Gateway ⚠"), ("2.5", "fiservdebit", "Plans on banks' debit cards ⚠"),
               ("3.3", "ap2", "Both back Google's AP2")]},
    {"id": "mcnext", "who": "mc", "name": "Where Installments, Agent Pay and the bank could land",
     "why": "Where Affirm has needs and Mastercard is not yet in: instalments on bank debit, a network for Affirm Bank, agentic checkout, UK and European debit, fraud and identity, and merchant data.",
     "steps": [("2.5", "fiservdebit", "Mastercard Installments on bank debit"), ("1.4", "affirmbank", "A network for Affirm Bank"),
               ("3.3", "ap2", "Agent Pay for Affirm plans"), ("4.5", "uk", "UK and European debit"),
               ("3.1", "fraud", "Fraud and identity services"), ("4.3", "merchants", "Merchant data for 571,000 merchants")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Affirm's map",
    "title": "A Visa house: every Affirm card is Visa, and Mastercard sits at the edges",
    "lead": "The Affirm Card is a Visa debit card, the first US partner for Visa's Flexible Credential, and the one-time virtual cards behind Apple Pay, Google Pay and in-store sales are Visa too. Affirm's loans settle to merchants off the card networks. Mastercard's touchpoints are thin: Mastercard Gateway lists Affirm as a payment method, both back Google's AP2, and Affirm plans on Fiserv banks' debit cards may ride Mastercard. Mastercard Installments competes for the same bank-debit space. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Affirm's own (Q4 FY2026 results, 27 August 2026; FY2026 10-K) or from Visa, Fiserv and press. Affirm's investor site could not be fetched, and Mastercard's Affirm page could not be read in full. Affirm does not publish a network split.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Affirm Card", "Visa debit", "Evolve and Stride; 5.2m users"],
        ["Flexible Credential", "Visa", "First US partner, Nov 2024"],
        ["Virtual cards", "Visa", "Apple Pay, Google Pay, in store"],
        ["Loans", "Off-network", "Affirm settles to merchants"],
        ["Bank debit", "Fiserv, Jan 2026", "Bank's own network ⚠"],
        ["Acceptance", "Mastercard Gateway", "Affirm listed ⚠"],
        ["Agentic", "Google AP2", "Both support it"],
        ["Charter", "Affirm Bank", "Nevada ILC, pending"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard Gateway's listing of Affirm, any Mastercard debit cards in Fiserv bank programmes, and AP2 as a shared standard.",
                "deals": "What it does not do: the Affirm Card, the Flexible Credential, virtual cards, loans, settlement or underwriting."},
        "snb": {"dir": "Visa's card, credential and virtual cards; Affirm's own loans, underwriting and settlement; partner banks; Apple, Google, Shopify and Amazon.",
                "deals": "Where they meet: banks' debit cards, agent checkouts and the proposed Affirm Bank."},
    },
    "tl": [
        ["Jan 2021", "Nasdaq listing"],
        ["Nov 2021", "Amazon exclusive; card in beta"],
        ["Nov 2024", "UK launch; Visa Flexible Credential"],
        ["Mar 2025", "Walmart goes to Klarna"],
        ["Apr 2025", "Stride Bank joins as card issuer"],
        ["Sep 2025", "In store with Apple Pay"],
        ["Oct 2025", "Google AP2 supporter"],
        ["Jan 2026", "Affirm Bank filing; Fiserv debit deal"],
        ["Jun 2026", "CPP forward flow renewed"],
        ["Aug 2026", "FY2026: $50.2bn GMV; Linford President"],
    ],
    "l": {
        "U": {"d": 0, "s": "Shoppers and cardholders carry Visa or no card at all.",
              "gap": "Cardholders carry a Visa card; plan users borrow off-network; only Fiserv banks' debit customers might carry Mastercard ⚠.",
              "neo": "Fiserv banks' debit customers ⚠.", "snb": "Affirm Card holders, plan users, merchants."},
        "L5": {"d": 1, "s": "Mastercard Gateway is one of many ways in.", "gap": "Mastercard Gateway lists Affirm ⚠; the app, Stripe, Worldpay and J.P. Morgan are other routes.",
               "neo": "Mastercard Gateway ⚠.", "snb": "App, Stripe, Worldpay, J.P. Morgan, Apple Pay."},
        "L4": {"d": 0, "s": "The lines are Affirm's own.", "gap": "Loans, Affirm Money, merchants and partners do not run on Mastercard.",
               "neo": "None.", "snb": "Loan book, Affirm Money, Amazon, Shopify, Costco."},
        "L3": {"d": 0, "s": "Underwriting and promotions are Affirm's.", "gap": "Underwriting, fraud and AdaptAI are in-house; AP2 is Google's.",
               "neo": "AP2 as a shared standard.", "snb": "Underwriting, AdaptAI, Affirm Edge."},
        "L2": {"d": 1, "s": "Visa cards; Mastercard only through banks' debit ⚠.", "gap": "The Affirm Card, Flexible Credential and virtual cards are Visa; loans settle off-network; Fiserv bank debit may be Mastercard ⚠.",
               "neo": "Fiserv bank debit ⚠.", "snb": "Affirm Card, Flexible Credential, virtual cards, ACH."},
        "L1": {"d": 0, "s": "Affirm's own scale, banks and licences.", "gap": "Nothing in the foundation is Mastercard's; Affirm Bank would choose its network directly.", "neo": "None.", "snb": "Partner banks, licences, funding, Affirm Bank."},
    },
    "t": area_lens(LAYERS),
}
