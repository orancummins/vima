"""Credicorp's kinds of user, journeys and Mastercard lens (BCP, Yape and Mibanco at the core), as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from credicorp_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Peru's largest financial group as five discs that stack into one platform, from a bank founded in 1889 and ROE "
       "above 20% at the bottom to the BCP and Yape apps, 10,400 agents and WhatsApp at the top. Click the stack to open it. "
       "Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined in the "
       "order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("yaper", "Yape users", "smartphone"),
    ("micro", "Micro-entrepreneurs", "store"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates", "factory"),
    ("saver", "Savers & cardholders", "coins"),
]
USERS_DESC = ("Six kinds of customer: BCP's 16 million clients, 16.7 million monthly Yape users, Mibanco's 880,000 "
              "micro-entrepreneurs, 2.4 million small businesses, corporates reaching into the US, and savers, "
              "travellers and the insured.")

WHO = {"con": "A BCP customer", "yaper": "A Yape user", "micro": "A micro-entrepreneur", "sme": "A small business",
       "corp": "A corporate treasurer", "saver": "A saver"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: a BCP account, a debit card, the app and Apple Pay, and an emergency block at any agent.",
     "steps": [("4.1", "retail", "Open a BCP account"), ("2.2", "bcpdebit", "Pay with the debit card"), ("5.1", "app", "Run it in the app"),
               ("5.1", "applepay", "Tap with Apple Pay"), ("3.1", "bloqueo", "Block cards at an agent if the phone is stolen")]},
    {"id": "yape", "who": "yaper", "name": "Pay with Yape",
     "why": "16.7 million monthly users paying by phone number and QR, with promos and new rules on disputes.",
     "steps": [("5.2", "yapeapp", "Sign up with an ID"), ("2.3", "yapepay", "Yapear a friend or a bodega"), ("2.3", "interop", "Pay a Plin user"),
               ("3.3", "promos", "Use a Yape Promo"), ("3.1", "scams", "Report a scam")]},
    {"id": "firstloan", "who": "yaper", "name": "Take a first loan",
     "why": "Yape has lent to 4.1 million people, a third of them new to credit.",
     "steps": [("5.2", "yapeapp", "Open Yape"), ("4.2", "yapeloan", "Take a Crédito Yape"), ("4.1", "warda", "Save in a wardadito")]},
    {"id": "remit", "who": "con", "name": "Receive money from abroad",
     "why": "Remittances through 15+ operators into Yape, and transfers to Colombia.",
     "steps": [("2.4", "remit", "Receive a remittance in Yape"), ("2.3", "yapepay", "Spend it by QR")]},
    {"id": "card", "who": "saver", "name": "Travel on a card",
     "why": "BCP's Visa and Amex LATAM Pass cards and the Qore range.",
     "steps": [("2.1", "visacredit", "Take a BCP Visa"), ("2.1", "amex", "Or an Amex LATAM Pass"), ("3.3", "latam", "Earn LATAM Pass miles")]},
    {"id": "micro", "who": "micro", "name": "Grow a micro business",
     "why": "Mibanco loans, a Visa debit card and WhatsApp, with repayments by Yape.",
     "steps": [("5.4", "mibwa", "Ask Mibanco on WhatsApp"), ("4.5", "mibanco", "Take a Mibanco loan"), ("2.2", "mibdebit", "Spend with the debit card"),
               ("2.3", "yapepay", "Repay by Yape")]},
    {"id": "merchant", "who": "sme", "name": "Get paid as a small business",
     "why": "Culqi takes cards and wallets; sales data feeds new credit.",
     "steps": [("4.3", "smallbiz", "Bank with BCP"), ("2.5", "culqi", "Take cards and Yape with Culqi"), ("2.5", "niubiz", "Or a Niubiz terminal"),
               ("4.3", "r2", "Borrow against sales")]},
    {"id": "corp", "who": "corp", "name": "Pay suppliers abroad",
     "why": "Telecrédito, Kinexys and the group's new US presence.",
     "steps": [("4.4", "wholesale", "Bank with BCP Wholesale"), ("5.4", "telecredito", "Pay through Telecrédito"),
               ("2.4", "kinexys", "Settle over Kinexys"), ("4.4", "usexp", "Bank a US subsidiary at BCP Miami")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Tenpo's prepaid card in Chile, acceptance at Culqi and Niubiz, and the real-time hub under interbank transfers ⚠.",
     "steps": [("2.6", "tenpo", "Tenpo Prepago Mastercard"), ("2.5", "culqi", "Mastercard accepted at Culqi"),
               ("2.5", "niubiz", "Mastercard on Niubiz since 2020"), ("2.3", "interop", "CCE real-time hub ⚠")]},
    {"id": "mcnext", "who": "mc", "name": "Where remittances, agents and the neobank could land",
     "why": "Where Credicorp has needs and Mastercard is not yet in: Yape remittances, AI agents, scam scoring for account-to-account payments, SME cards and data, and Tenpo's network inside the neobank unit.",
     "steps": [("2.4", "remit", "Cross-border rails for Yape remittances"), ("3.2", "agents", "Agent Pay for BCP's agents"),
               ("3.1", "scams", "Scam scoring on Yape and transfers"), ("4.3", "smallbiz", "SME cards and transaction data"),
               ("2.6", "tenpo", "Tenpo's Mastercard across the neobank unit")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Credicorp's map",
    "title": "Visa issues the cards, Yape moves the money, Mastercard stands at the edges",
    "lead": "BCP is Peru's largest card issuer, and its credit cards, iO, Mibanco's debit card and BCP Bolivia's cards run on Visa, with the premium LATAM Pass range split with Amex. No BCP Mastercard programme and no joint announcement were found. Yape, with 16.7 million monthly users, moves money account to account with no card network at all. Mastercard's footholds are at the edges: Tenpo's prepaid card in Chile, acceptance at Culqi and Niubiz, and the real-time hub under Peru's interbank transfers ⚠. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (1Q26 release, 15 May 2026; 4Q25 release, 13 February 2026) or from Gestión, tarjetas.pe and a summary of the 2Q26 results. viabcp.com, Credicorp's investor site, sec.gov and mastercard.com refused automated requests; BCP debit's network, Niubiz's ownership and Tenpo's credit network are not confirmed.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Credit", "Visa and Amex", "Peru's largest book; 34% of revolving balances ⚠"],
        ["Debit", "Visa", "BCP ⚠, Mibanco, BCP Bolivia"],
        ["Yape", "Account to account", "16.7m monthly users, 2Q26"],
        ["Interbank transfers", "CCE hub", "Built on Mastercard real-time infrastructure ⚠"],
        ["Acceptance", "Culqi, Niubiz", "Multi-brand since 2020"],
        ["Tenpo (Chile)", "Mastercard prepaid", "Neobank licence, January 2026"],
        ["Cross-border", "Western Union, Kinexys", "No Mastercard rail found"],
    ],
    "sides": {
        "neo": {"dir": "Tenpo's prepaid card, acceptance at Culqi and Niubiz, and the real-time hub under interbank transfers ⚠.",
                "deals": "What it does not do: BCP credit and debit, iO, Mibanco, Bolivia, Yape, remittances, loyalty or AI."},
        "snb": {"dir": "Visa across BCP, iO, Mibanco and Bolivia; Amex at the top; Yape's own closed loop; Western Union and J.P. Morgan across borders.",
                "deals": "Where they meet: the neobank unit, where Yape and iO sit beside Tenpo's Mastercard."},
    },
    "tl": [
        ["Dec 2019", "Niubiz (then VisaNet) to accept Mastercard from 2020"],
        ["c. 2021", "Mastercard real-time infrastructure for the CCE hub ⚠"],
        ["2023", "BCRP interoperability links Yape and Plin"],
        ["Dec 2025", "BCP agrees to buy Helm Bank USA"],
        ["Jan 2026", "Tenpo, a Mastercard prepaid issuer, gets a Chilean bank licence"],
        ["Apr 2026", "Neobank unit joins Yape, iO, Tenpo and Yape Bolivia"],
        ["Jun 2026", "BCP adopts J.P. Morgan Kinexys for payments abroad"],
        ["Aug 2026", "Yape reaches 16.7 million monthly users"],
    ],
    "l": {
        "U": {"d": 1, "s": "Only Tenpo's customers in Chile carry a group Mastercard.",
              "gap": "In Peru, BCP and Mibanco cardholders carry Visa or Amex and Yape users carry no card; Tenpo's prepaid holders in Chile carry Mastercard.",
              "neo": "Tenpo prepaid cardholders.", "snb": "BCP, iO and Mibanco cardholders, Yape users, BCP Bolivia."},
        "L5": {"d": 0, "s": "The front doors are the group's.", "gap": "Apps, agents, branches and WhatsApp are Credicorp's own; Apple Pay carries Visa and Amex cards.",
               "neo": "None.", "snb": "BCP app, Yape app, agents, WhatsApp, Telecrédito."},
        "L4": {"d": 0, "s": "The business lines carry Visa cards or none.", "gap": "Accounts, Yape loans, SME and wholesale banking, Mibanco and insurance have no Mastercard role.",
               "neo": "None.", "snb": "Retail, Yape lending, SME, wholesale, Mibanco, Pacífico."},
        "L3": {"d": 0, "s": "Fraud, AI and loyalty are the group's own.", "gap": "No Mastercard fraud, data or offers product is public; LATAM Pass runs on Visa and Amex.",
               "neo": "None.", "snb": "Emergency block, AI, Yape Promos, LATAM Pass."},
        "L2": {"d": 1, "s": "Tenpo, acceptance and the CCE hub ⚠; the cards are Visa.", "gap": "Visa carries BCP's credit and debit; Yape is account to account; Mastercard has Tenpo, multi-brand acceptance and the real-time hub ⚠.",
               "neo": "Tenpo prepaid, Culqi and Niubiz acceptance, CCE hub ⚠.", "snb": "Visa and Amex cards, Yape, remittance operators, Kinexys."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, brands, technology, Krealo, strategy."},
    },
    "t": area_lens(LAYERS),
}
