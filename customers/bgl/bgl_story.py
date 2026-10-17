"""BGL BNP Paribas's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from bgl_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("BNP Paribas' Luxembourg bank as five discs that stack into one platform, from €64.6 billion of balance sheet "
       "and owners in Paris and the Luxembourg State at the bottom to the Web Banking app, 22 branches and My Business "
       "Banking at the top. Click the stack to open it. Choose who you are and what you want to do, and the areas that "
       "deliver it light up across the layers, joined in the order they act. Switch to the Mastercard lens to see how "
       "deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Residents & families", "user-round"),
    ("xb", "Cross-border workers", "earth"),
    ("home", "Homebuyers", "house"),
    ("hnw", "Private-banking clients", "gem"),
    ("pro", "Professionals & small firms", "briefcase"),
    ("corp", "Companies & institutions", "factory"),
]
USERS_DESC = ("Six kinds of customer, about 185,000 clients in all ⚠: residents and families, cross-border workers, "
              "homebuyers, private-banking clients, professionals and small firms, and the companies and institutions "
              "the corporate bank and leasing serve.")

WHO = {"con": "A BGL customer", "xb": "A cross-border worker", "home": "A homebuyer", "hnw": "A private-banking client",
       "pro": "A professional", "corp": "A company treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: a pack, Visa Debit, Apple Pay, the app and Genius.",
     "steps": [("4.1", "packs", "Open a pack"), ("2.1", "visadebit", "Pay with Visa Debit"), ("2.4", "applepay", "Pay with Apple Pay"),
               ("5.1", "app", "Run it in the app"), ("3.3", "genius", "Ask Genius"), ("3.1", "threeds", "Shop safely online")]},
    {"id": "credit", "who": "con", "name": "Choose a credit card",
     "why": "Visa Classic in Essentiel; Mastercard Gold or Visa Classic higher up.",
     "steps": [("4.1", "packs", "Pick a pack"), ("2.2", "visaclassic", "Take Visa Classic"), ("2.2", "mcgold", "Or take Mastercard Gold"),
               ("3.2", "retour", "Get return postage back")]},
    {"id": "xborder", "who": "xb", "name": "Live across a border",
     "why": "Paying and withdrawing in Luxembourg, France, Belgium and Germany.",
     "steps": [("2.1", "visadebit", "Pay abroad with Visa Debit"), ("2.7", "globalnet", "Withdraw in the group network"),
               ("2.5", "wero", "Send money with Wero"), ("5.1", "app", "Manage it in the app")]},
    {"id": "premium", "who": "hnw", "name": "Bank privately",
     "why": "Private banking with Mastercard's premium cards.",
     "steps": [("4.2", "privatebank", "Work with the private bank"), ("2.2", "mcpremium", "Carry Platinum or Elite"),
               ("3.2", "cardinsurance", "Travel insured"), ("4.5", "lifeins", "Plan with life insurance")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "A mortgage through a branch, protected with Cardif.",
     "steps": [("5.2", "branches", "Meet an adviser"), ("4.1", "homeloans", "Take a home loan"), ("4.5", "lifeins", "Protect it")]},
    {"id": "pro", "who": "pro", "name": "Run a small business",
     "why": "An account, a Visa Business card, Axepta terminals and Wero.",
     "steps": [("4.3", "corporates", "Open a business account"), ("2.3", "visabusiness", "Spend with Visa Business"),
               ("2.6", "axepta", "Take cards with Axepta"), ("2.6", "weropro", "Take Wero"), ("5.3", "mbb", "Manage in My Business Banking")]},
    {"id": "corp", "who": "corp", "name": "Finance a company",
     "why": "Corporate banking and international leasing.",
     "steps": [("4.3", "corporates", "Bank with the corporate team"), ("4.4", "leasing", "Lease equipment"), ("3.4", "ihub", "Onboard through i-Hub")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The mid and premium credit cards, Mastercard's return-postage cover, Mastercard cards in Apple Pay, and acceptance through Axepta.",
     "steps": [("2.2", "mcgold", "Mastercard Gold"), ("2.2", "mcpremium", "Platinum and Elite"), ("3.2", "retour", "Return-postage cover"),
               ("2.4", "applepay", "Mastercard cards in Apple Pay"), ("2.6", "axepta", "Accepted on Axepta")]},
    {"id": "mcnext", "who": "mc", "name": "Where business cards, agents and benefits could land",
     "why": "Where BGL has needs and Mastercard is not yet in: commercial and virtual cards, benefits for private clients, Agent Pay for Genius, open-finance data and the debit book in the long run.",
     "steps": [("5.3", "mbb", "Virtual cards and spend controls in My Business Banking"), ("2.3", "visabusiness", "A Mastercard business card"),
               ("4.2", "privatebank", "Benefits for private clients"), ("3.3", "genius", "Agent Pay for Genius"),
               ("3.3", "aggregator", "Open-finance data"), ("2.1", "visadebit", "Debit, in the long run")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across BGL BNP Paribas's map",
    "title": "Visa in every pocket, Mastercard in the premium one",
    "lead": "Visa carries BGL's debit card, launched with Visa in November 2020 and included in every pack, as well as Visa Classic and Visa Business. Mastercard carries the Gold, Platinum and Elite credit cards and Mastercard's return-postage cover. Wero replaced Payconiq in September 2026. No network agreement or joint Mastercard initiative has been announced. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (2025 results, 2 April 2026; tariffs from 1 October 2026) or the group's Luxembourg line (Q2 2026). BGL publishes no card volumes by network; the client count and the V PAY history rest on group and older documents ⚠.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa", "Visa Debit since November 2020, every pack"],
        ["Entry credit", "Visa", "Visa Classic, €2 a month"],
        ["Mid & premium credit", "Mastercard", "Gold, Platinum, Elite"],
        ["Business cards", "Visa", "Visa Business only"],
        ["Benefits", "Mastercard", "Return-postage cover"],
        ["Wallets", "Apple Pay", "First in Luxembourg, May 2019"],
        ["A2A", "Wero", "Payconiq off 30 September 2026"],
    ],
    "sides": {
        "neo": {"dir": "Gold, Platinum and Elite credit cards, the return-postage benefit, Mastercard cards in Apple Pay and acceptance on Axepta terminals.",
                "deals": "What it does not do: debit, entry credit, business cards, Wero, instant transfers, AI or KYC."},
        "snb": {"dir": "Visa Debit, Visa Classic and Visa Business; Wero and SEPA Instant; Axepta, Bancomat and the group's own technology.",
                "deals": "Where they meet: inside the packs, where Visa Classic and Mastercard Gold are offered side by side."},
    },
    "tl": [
        ["May 2019", "Apple Pay for V PAY, Visa and Mastercard"],
        ["Nov 2020", "Visa Debit launched with Visa"],
        ["Jul 2022", "Mastercard Elite terms"],
        ["Nov 2023", "Bancomat shared ATMs"],
        ["Jun 2025", "Joins EPI for Wero"],
        ["Jan 2026", "Nicolas Otton CEO"],
        ["Apr 2026", "2025 net income €514.5m"],
        ["Sep 2026", "Payconiq switched off"],
        ["Oct 2026", "New tariffs: Elite €28 a month"],
    ],
    "l": {
        "U": {"d": 1, "s": "Every customer carries Visa debit; premium clients carry Mastercard.",
              "gap": "Residents, cross-border workers and professionals carry Visa; private-banking clients and Gold holders carry Mastercard.",
              "neo": "Gold, Platinum and Elite cardholders.", "snb": "Debit holders, Visa Classic and Visa Business holders, Wero users."},
        "L5": {"d": 0, "s": "The front doors are BGL's.", "gap": "App, branches and My Business Banking are the bank's own.", "neo": "None.", "snb": "Web Banking, branches, My Business Banking."},
        "L4": {"d": 0, "s": "The business lines carry Visa debit.", "gap": "Packs come with Visa Debit and a choice of credit card; loans, leasing and insurance have no network role.",
               "neo": "Mastercard credit as a pack option.", "snb": "Packs, home loans, corporate banking, leasing, Cardif."},
        "L3": {"d": 1, "s": "The return-postage cover is Mastercard's; the rest is BGL's.", "gap": "Mastercard runs one benefit; Genius, aggregation and KYC are the bank's or shared.",
               "neo": "Return-postage cover.", "snb": "Genius, i-Hub, card controls."},
        "L2": {"d": 1, "s": "Mastercard in premium credit; Visa everywhere else.", "gap": "Visa has debit, entry credit and business; Wero takes person-to-person payments.",
               "neo": "Gold, Platinum, Elite; Apple Pay tokens.", "snb": "Visa Debit, Visa Classic, Visa Business, Wero, Bancomat."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, owners, cloud, GTS plan."},
    },
    "t": area_lens(LAYERS),
}
