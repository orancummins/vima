"""Banco Bradesco's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from bradesco_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("One of Brazil's largest private banks as five discs that stack into one platform, from 74 million clients, "
       "R$1.14 trillion of loans and stakes in Elo and Cielo at the bottom to 1,844 branches, 39,000 correspondents and "
       "the app at the top. Click the stack to open it. Choose who you are and what you want to do, and the areas that "
       "deliver it light up across the layers, joined in the order they act. Switch to the Mastercard lens to see how "
       "deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("hnw", "High-income clients", "gem"),
    ("mei", "Small firms & MEIs", "briefcase"),
    ("merch", "Merchants", "store"),
    ("corp", "Corporates & agribusiness", "factory"),
    ("ins", "Policyholders", "shield-check"),
]
USERS_DESC = ("Six kinds of client, 74.3 million in all at the end of 2025: everyday customers, high-income clients in "
              "Principal, Prime and Private, small firms and micro-entrepreneurs (MEIs), merchants, corporates and "
              "agribusiness, and insurance and pension customers.")

WHO = {"con": "A Bradesco customer", "hnw": "A high-income client", "mei": "A small firm", "merch": "A merchant",
       "corp": "A corporate treasurer", "ins": "A policyholder"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The app, a debit card, Pix and BIA, with fraud monitoring behind them.",
     "steps": [("5.3", "app", "Open the app"), ("2.4", "debit", "Pay with a debit card"), ("2.5", "pix", "Send a Pix"),
               ("3.1", "bia", "Ask BIA to pay a bill"), ("3.2", "fraud", "Protected from fraud")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "Elo, Visa, Mastercard or Amex cards, co-brands and points.",
     "steps": [("2.1", "credit", "Take a credit card"), ("2.3", "amazon", "Choose the Amazon card"), ("2.4", "wallets", "Add it to a phone wallet"),
               ("3.3", "livelo", "Earn Livelo points")]},
    {"id": "loan", "who": "con", "name": "Borrow for life's big costs",
     "why": "Payroll loans, mortgages and vehicle finance, through branches and correspondents.",
     "steps": [("5.2", "expresso", "Visit a correspondent"), ("4.1", "payroll", "Take a payroll loan"), ("4.1", "homeauto", "Finance a home or car")]},
    {"id": "premium", "who": "hnw", "name": "Bank as a high-income client",
     "why": "Principal, a premium card and an international account.",
     "steps": [("4.4", "principal", "Join Principal"), ("2.2", "mcblack", "Carry Mastercard Black"), ("2.2", "amex", "Or The Centurion Card"),
               ("2.8", "intlaccount", "Open a US account"), ("4.4", "invest", "Invest with Ágora")]},
    {"id": "mei", "who": "mei", "name": "Run a small firm",
     "why": "Empresas e Negócios, Pix Automático and Cielo machines.",
     "steps": [("4.2", "smes", "Open a business account"), ("5.3", "channels", "Run it in Net Empresa"), ("2.5", "pixauto", "Bill customers by Pix Automático"),
               ("2.6", "alelo", "Give staff Alelo meal cards")]},
    {"id": "merch", "who": "merch", "name": "Take payments",
     "why": "Cielo and Net Empresa acceptance, cards and Pix.",
     "steps": [("2.7", "netempresa", "Sign up online"), ("2.7", "cielo", "Take cards with Cielo"), ("2.5", "pix", "Take Pix by QR code")]},
    {"id": "corp", "who": "corp", "name": "Finance a corporate or a farm",
     "why": "BBI and corporate banking, agribusiness and trade finance.",
     "steps": [("4.3", "corporate", "Bank with BBI"), ("4.3", "agri", "Finance a harvest"), ("2.8", "fx", "Export and import")]},
    {"id": "insure", "who": "ins", "name": "Insure and save for retirement",
     "why": "Bradesco Seguros and Bradsaúde.",
     "steps": [("4.5", "seguros", "Buy insurance or a pension"), ("4.5", "health", "Get health cover")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Mastercard Black, the Amazon co-brand, part of the credit book and Surpreenda promotions.",
     "steps": [("2.2", "mcblack", "Mastercard Black"), ("2.3", "amazon", "Amazon co-brand ⚠"), ("2.1", "credit", "Part of the credit book"),
               ("3.3", "surpreenda", "Surpreenda promotions")]},
    {"id": "mcnext", "who": "mc", "name": "Where Principal, agents and Digio could land",
     "why": "Where Bradesco has needs and Mastercard is not yet in: Principal's premium card, Agent Pay for BIA, fraud across cards and Pix, Digio's white label, the US account and small-firm cards.",
     "steps": [("2.2", "principalcard", "World Elite for Principal"), ("3.1", "bia", "Agent Pay for BIA"), ("3.2", "fraud", "Fraud and scam scores"),
               ("4.6", "digio", "Processing for Digio's white label"), ("2.8", "intlaccount", "Cards for the US account"), ("4.2", "smes", "Small-business cards")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Bradesco's map",
    "title": "Elo's co-owner, with Mastercard at the edges",
    "lead": "Bradesco co-owns Elo and is paid to issue Elo cards until 2034; Visa carries its top premium tiers and the Disney co-brand, and Bradesco issues American Express. Mastercard is visible in Mastercard Black, the Amazon co-brand and Surpreenda promotions, and no network split is published. Visa named Bradesco in its agentic programme; Mastercard's first Agent Pay partners did not include it. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (2Q26 results, 6 August 2026; 2025 Form 20-F) or from Bradesco's card pages and Brazilian press. Bradesco publishes no split of cards by network; debit, Digio, Bradescard and Principal card networks are not disclosed.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Credit", "Elo, Visa, Mastercard, Amex", "R$360bn in 2025; no split published"],
        ["Elo", "Co-owned", "Incentive deal to 31 Dec 2034"],
        ["Premium", "Visa and Amex", "Mastercard Black relaunched Feb 2024"],
        ["Co-brands", "Amazon on Mastercard", "Disney on Visa"],
        ["Debit", "Visa and Elo promoted", "Mastercard not mentioned ⚠"],
        ["Acceptance", "Cielo", "Co-controlled with Banco do Brasil"],
        ["Agentic", "Visa Agentic Ready", "Not in Mastercard's first Agent Pay wave"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard Black, the Amazon co-brand, a share of the credit book, Surpreenda promotions, and acceptance at Cielo.",
                "deals": "What it does not do: Elo cards and incentives, Visa premium and Disney, Amex, Pix, Livelo or BIA."},
        "snb": {"dir": "Elo (co-owned) and Alelo, Visa premium tiers, Disney and debit promotion, Amex issuing, Pix and Pix Automático, and Livelo.",
                "deals": "Where they meet: the premium and Principal cards, and agentic payments."},
    },
    "tl": [
        ["2011", "Elo launched by Bradesco, BB and Caixa"],
        ["Aug 2023", "Amazon co-brand on Mastercard"],
        ["Feb 2024", "Lifetime-free Mastercard Black"],
        ["Nov 2024", "Bradesco Principal launched"],
        ["Apr 2025", "Elo incentive deal to 2034; Pix Automático"],
        ["Dec 2025", "Mastercard Agent Pay in Latin America"],
        ["Aug 2026", "Bradesco in Visa Agentic Ready"],
        ["Oct 2026", "R$10bn capital increase approved"],
    ],
    "l": {
        "U": {"d": 1, "s": "Some cardholders carry Mastercard.",
              "gap": "Black and Amazon holders carry Mastercard; most see Elo, Visa or Amex, and Pix carries everyday transfers.",
              "neo": "Black, Amazon and some credit cardholders.", "snb": "Elo, Visa and Amex holders, Pix users, policyholders."},
        "L5": {"d": 0, "s": "The front doors are Bradesco's.", "gap": "Branches, correspondents and the app are the bank's.", "neo": "None.", "snb": "Branches, Expresso, app."},
        "L4": {"d": 0, "s": "Business lines carry no network.", "gap": "Loans, wealth, insurance and Digio have no stated Mastercard role.",
               "neo": "None.", "snb": "Lending, wealth, insurance, Digio."},
        "L3": {"d": 1, "s": "Surpreenda is Mastercard's; BIA and Livelo are not.", "gap": "Surpreenda promotions run on Mastercard; BIA, fraud and Livelo are Bradesco's or Elopar's.",
               "neo": "Surpreenda.", "snb": "BIA, fraud monitoring, Livelo, Viva Prime."},
        "L2": {"d": 1, "s": "One network of four, behind Elo.", "gap": "Elo is co-owned and incentivised; Visa leads premium; Mastercard has Black and Amazon.",
               "neo": "Black, Amazon, part of credit, Cielo acceptance.", "snb": "Elo, Visa, Amex, Pix, Alelo."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's; its stakes are in Elo and Cielo.", "neo": "None.", "snb": "Capital, control, Elopar, Cielo."},
    },
    "t": area_lens(LAYERS),
}
