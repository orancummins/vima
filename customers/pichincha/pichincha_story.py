"""Banco Pichincha's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from pichincha_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Ecuador's largest bank as five discs that stack into one platform, from about 28% of the country's banking "
       "assets at the bottom to Banca Móvil, branches and 8,500 Mi Vecino agents at the top. Click the stack to open it. "
       "Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined in "
       "the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("aff", "Premium cardholders", "gem"),
    ("micro", "Micro-entrepreneurs", "hand-coins"),
    ("sme", "Small businesses & merchants", "store"),
    ("corp", "Corporates", "factory"),
    ("migr", "Migrants & families abroad", "earth"),
]
USERS_DESC = ("Six kinds of customer, about 6.5 million in all: everyday customers, premium cardholders, micro-entrepreneurs, "
              "small businesses and merchants, corporates, and Ecuadorian families with money moving to and from abroad.")

WHO = {"con": "A Pichincha customer", "aff": "A premium cardholder", "micro": "A micro-entrepreneur", "sme": "A small business",
       "corp": "A corporate treasurer", "migr": "A family abroad"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a Visa debit card, the app, Deuna QR and fraud checks.",
     "steps": [("4.1", "accounts", "Open an account"), ("2.1", "debit", "Pay with Visa debit"), ("5.1", "app", "Run it in Banca Móvil"),
               ("2.5", "deuna", "Pay a friend with Deuna"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "Visa or Mastercard credit, miles on both, and instalments in the app.",
     "steps": [("2.2", "mccredit", "Take a Mastercard or Visa card"), ("3.2", "miles", "Earn Pichincha Miles"), ("5.1", "app", "Spread purchases over 12 months")]},
    {"id": "premium", "who": "aff", "name": "Travel on a premium card",
     "why": "Quantum by invitation, Black cards and Priceless draws.",
     "steps": [("2.2", "quantum", "Get Quantum by invitation"), ("3.2", "mccampaigns", "Enter Priceless draws"), ("3.2", "miles", "Redeem miles"),
               ("5.4", "contact", "Book the airport fast track")]},
    {"id": "micro", "who": "micro", "name": "Run a micro-business",
     "why": "Agents, microcredit, a microfinance card and Deuna QR.",
     "steps": [("5.3", "mivecino", "Bank at a Mi Vecino agent"), ("4.3", "microfinance", "Borrow for the business"),
               ("2.3", "microcards", "Pay with a microfinance card"), ("2.5", "deunamerchant", "Collect with a Deuna QR")]},
    {"id": "sme", "who": "sme", "name": "Get paid as a merchant",
     "why": "Cards through the bank's acquiring, payment links online and Deuna QR at the counter.",
     "steps": [("4.2", "cashmgmt", "Open Banca Empresas"), ("2.4", "acquiring", "Take Visa and Mastercard"),
               ("2.4", "paylink", "Sell online with a payment link"), ("2.5", "deunamerchant", "Take QR payments")]},
    {"id": "corp", "who": "corp", "name": "Run a company's money",
     "why": "Cash management, corporate cards on both networks and trade lines.",
     "steps": [("4.2", "cashmgmt", "Pay payroll and suppliers"), ("2.3", "mcbiz", "Give staff Black Corporate cards"),
               ("4.2", "trade", "Finance trade with IFC and IDB lines")]},
    {"id": "migr", "who": "migr", "name": "Move money across borders",
     "why": "Banco Pichincha España, money received from abroad and Visa Direct out.",
     "steps": [("4.5", "spain", "Bank with Banco Pichincha España"), ("2.7", "swift", "Receive money in Ecuador"),
               ("2.7", "visadirect", "Send abroad from the app")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Credit cards up to Black, Quantum, corporate cards, Priceless campaigns and a quarter of acquiring fees.",
     "steps": [("2.2", "mccredit", "Mastercard credit, five tiers"), ("2.2", "quantum", "Quantum on Mastercard"),
               ("2.3", "mcbiz", "Black Corporate and Business Black"), ("3.2", "mccampaigns", "Priceless and Spend And Get"),
               ("2.4", "acquiring", "About 24% of merchant commissions")]},
    {"id": "mcnext", "who": "mc", "name": "Where remittances, debit and offers could land",
     "why": "Where Pichincha has needs and Mastercard is not yet in: a second remittance rail, digital debit, virtual corporate cards, offers for Pichincha Miles, QR and instant payments, and fraud scoring.",
     "steps": [("2.7", "visadirect", "Mastercard Move beside Visa Direct"), ("2.1", "debitdigital", "A Mastercard digital debit option"),
               ("2.3", "mcbiz", "Virtual cards and spend controls"), ("3.2", "miles", "Card-linked offers for Miles"),
               ("2.6", "sip", "QR and instant-payment services"), ("3.1", "fraud", "Risk scoring for digital payments")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Banco Pichincha's map",
    "title": "Visa first, Mastercard a strong second card",
    "lead": "Every Banco Pichincha debit card is Visa, Visa earned about three times Mastercard's merchant commissions at the bank in 2025, and in September 2026 the bank chose Visa Direct for remittances from its app. Mastercard is the second network: five consumer credit tiers up to Black, Quantum on either network, four corporate cards and 2026 campaigns with Priceless. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (audited 2025 report, February 2026; BankWatch, May 2026) or from Ecuadorian press. The bank does not publish card counts or volumes by network; the acquiring split comes from merchant-commission income.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa", "Every debit card, including digital"],
        ["Consumer credit", "Visa and Mastercard", "Six Visa tiers, five Mastercard up to Black"],
        ["Corporate cards", "Visa and Mastercard", "Four Mastercard products, Black Corporate"],
        ["Acquiring", "Visa about 76%", "Merchant commissions 2025: $40.8m vs $12.6m"],
        ["Remittances", "Visa Direct", "In the app from September 2026"],
        ["Wallet", "Deuna", "Account-to-account QR, the bank's own"],
        ["Loyalty", "Pichincha Miles", "Priceless draws in 2026"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard credit cards up to Black, Quantum, corporate and microfinance cards, Priceless experiences and Airport Experiences, and a quarter of acquiring fees.",
                "deals": "What it does not do: debit, remittances, Deuna, transfers or fraud tooling in public sources."},
        "snb": {"dir": "Visa debit and most credit tiers, Visa Direct, the World Cup campaign, Deuna QR, central-bank instant payments and Diners Club through an associated bank.",
                "deals": "Where they meet: credit, Quantum, microfinance cards, Pichincha Miles and the acquiring business."},
    },
    "tl": [
        ["2019", "Deuna wallet launched"],
        ["Dec 2024", "Instant-payments mandate"],
        ["Feb 2026", "Ribadeneira becomes general manager"],
        ["May 2026", "Mastercard Priceless Father's Day draw; Visa World Cup cards"],
        ["Jun 2026", "Fitch upgrade to B"],
        ["Jul 2026", "Spend And Get Mastercard 2026"],
        ["Sep 2026", "Visa Direct remittances in the app"],
        ["Nov 2026", "Real-time payments standard due"],
    ],
    "l": {
        "U": {"d": 1, "s": "Mastercard credit and corporate cardholders; every debit holder carries Visa.",
              "gap": "Debit holders and remitters use Visa; Mastercard reaches part of the credit and corporate base.",
              "neo": "Mastercard credit, Quantum and corporate cardholders.", "snb": "Debit holders, Visa cardholders, Deuna users, remitters."},
        "L5": {"d": 0, "s": "The front doors are the bank's.", "gap": "App, branches, ATMs and Mi Vecino agents are Pichincha's own.", "neo": "None.", "snb": "Banca Móvil, branches, Mi Vecino."},
        "L4": {"d": 0, "s": "The business lines carry Visa debit.", "gap": "Accounts come with Visa debit; loans, cash management and international banks have no network role.",
               "neo": "None.", "snb": "Accounts, loans, cash management, Spain, Colombia."},
        "L3": {"d": 1, "s": "Priceless in campaigns; Miles on both networks.", "gap": "Mastercard's Priceless features in 2026 campaigns; fraud tooling and partnerships are not Mastercard's.",
               "neo": "Priceless, Airport Experiences, Miles on Mastercard cards.", "snb": "Fraud and cyber defence, Visa World Cup, Diners Club, cooperatives."},
        "L2": {"d": 1, "s": "Credit and corporate cards on Mastercard; debit and remittances on Visa.", "gap": "Visa has all debit, Visa Direct and three-quarters of acquiring fees; Deuna and transfers are account-to-account.",
               "neo": "Mastercard credit, corporate and microfinance cards, Quantum, acquiring.", "snb": "Visa debit and credit, Visa Direct, Deuna, instant transfers."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, ratings, family ownership, strategy."},
    },
    "t": area_lens(LAYERS),
}
