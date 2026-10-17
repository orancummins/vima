"""National Commercial Bank Jamaica's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from ncb_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Jamaica's largest bank as five discs that stack into one platform, from J$2.43 trillion of group assets at the "
       "bottom to the NCB app, 27 branches and 300-plus ABMs at the top. Click the stack to open it. Choose who you are "
       "and what you want to do, and the areas that deliver it light up across the layers, joined in the order they act. "
       "Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("unb", "Cash users & Lynk wallet", "wallet"),
    ("mer", "Merchants", "store"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates & government", "factory"),
    ("inv", "Savers & policyholders", "coins"),
]
USERS_DESC = ("Six kinds of customer: everyday account and card holders, people who mostly use cash and the Lynk wallet, "
              "the merchants on about 70% of the island's terminals, small businesses, corporates and government, and "
              "savers and policyholders across the group.")

WHO = {"con": "An NCB customer", "unb": "A Lynk user", "mer": "A merchant", "sme": "A small business",
       "corp": "A corporate treasurer", "inv": "A saver"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a Visa debit card, the app, NCB Miles and card security.",
     "steps": [("4.1", "retail", "Open an account"), ("2.1", "debit", "Pay with Visa debit"), ("5.1", "app", "Run it in the app"),
               ("3.2", "miles", "Earn NCB Miles"), ("3.1", "fraud", "Protected by chip and PIN")]},
    {"id": "travel", "who": "con", "name": "Spend abroad on a card",
     "why": "Mastercard Platinum Travel and Standard USD, or Visa cash back, applied for online.",
     "steps": [("5.4", "onboard", "Check eligibility online"), ("2.2", "mccredit", "Take a Mastercard travel card"),
               ("2.2", "visacredit", "Or a Visa cash-back card"), ("3.2", "miles", "Redeem miles for flights")]},
    {"id": "cashless", "who": "unb", "name": "Pay without a bank account",
     "why": "Lynk, its Visa virtual card, Jam-Dex and the Mastercard prepaid card.",
     "steps": [("2.5", "lynk", "Join Lynk with an ID"), ("2.6", "remit", "Collect a remittance"),
               ("2.5", "lynkcard", "Pay online with the Lynk Visa card"), ("2.3", "prepaid", "Or load a Mastercard Prepaid"),
               ("5.3", "branches", "Cash in at an ABM")]},
    {"id": "merchant", "who": "mer", "name": "Take payments",
     "why": "Terminals, Tap on Phone, links and QR, on every network.",
     "steps": [("2.4", "mcmsme", "Get a phone through the Mastercard programme"), ("2.4", "epos", "Take taps with ePOS"),
               ("2.4", "acquiring", "Or a POS terminal"), ("2.4", "ecom", "Sell online with links and QR"),
               ("5.4", "merchantportal", "Track sales in the portal")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A loan from the SME fund, a business card with instalments and bills collected by PaySmart.",
     "steps": [("4.1", "smefund", "Borrow from the SME Growth Fund"), ("2.2", "bizcards", "Use a business card"),
               ("2.2", "flexipay", "Spread a big purchase with FlexiPay Biz"), ("2.4", "paysmart", "Collect bills with PaySmart")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "Corporate banking, treasury and the move off cheques.",
     "steps": [("4.2", "corporate", "Bank with Corporate Banking"), ("2.6", "clearing", "Switch from cheques to RTGS and ACH"),
               ("4.3", "treasury", "Manage liquidity and FX")]},
    {"id": "save", "who": "inv", "name": "Save, invest and insure",
     "why": "NCB Capital Markets, Guardian insurance and pensions, and Clarien offshore.",
     "steps": [("4.3", "wealth", "Invest with NCB Capital Markets"), ("4.4", "insurance", "Insure and save for a pension"),
               ("4.5", "clarien", "Bank offshore with Clarien")]},
    {"id": "borrow", "who": "con", "name": "Borrow quickly",
     "why": "Digital loans paid out on approval, and relief after Melissa.",
     "steps": [("5.4", "onboard", "See a pre-approved offer"), ("3.3", "digiloans", "Take a digital loan"),
               ("1.5", "melissa", "Get relief after the hurricane")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The Mastercard credit and prepaid cards, the business Mastercards, NCB Pay and the micro-merchant programme.",
     "steps": [("2.2", "mccredit", "Mastercard travel and USD credit"), ("2.3", "prepaid", "Mastercard Prepaid"),
               ("2.2", "bizcards", "Business Elite and Executive Travel"), ("2.5", "ncbpay", "Mastercard cards in NCB Pay"),
               ("2.4", "mcmsme", "Phones for unbanked merchants")]},
    {"id": "mcnext", "who": "mc", "name": "Where wallets, remittances and commercial cards could land",
     "why": "Where NCB has needs and Mastercard is not yet in: tokens for phone wallets, remittances into cards and Lynk, micro-merchant and toll acceptance, commercial cards as cheques end, and fraud tools after Melissa.",
     "steps": [("2.5", "ncbpay", "Tokens for Apple Pay and Google Pay"), ("2.6", "remit", "Mastercard Move into cards and Lynk"),
               ("2.4", "epos", "Scale Tap on Phone and tolling"), ("2.6", "clearing", "Commercial cards as cheques end"),
               ("3.1", "fraud", "Fraud and identity scoring")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across National Commercial Bank Jamaica's map",
    "title": "Mastercard in the wallet's credit slot, Visa on every debit card",
    "lead": "NCB moved all its debit cards to Visa when it retired Keycard and the Multilink Midas card (switched off in March 2025), and its Lynk wallet chose Visa for a virtual card in 2026. Mastercard carries the prepaid card, the travel and US-dollar credit cards and two business cards, and backs a 2025 programme putting NCB's acceptance app on phones for unbanked merchants. NCB's acquiring, about 70% of the island's terminals, takes every network. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are NCB Financial Group's own (H1 FY2026 results, 7 May 2026; FY2025 results, 13 November 2025) or from NCB's website and the Jamaican press. The Q3 FY2026 results, market value, ratings and any network contract were not found.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa", "All accounts; Midas off March 2025"],
        ["Personal credit", "Mastercard and Visa", "Mastercard travel and USD; Visa cash back"],
        ["Business credit", "Mastercard and Visa", "Business Elite, Executive Travel; Visa Platinum Business"],
        ["Prepaid", "Mastercard", "Since April 2021"],
        ["Lynk card", "Visa", "April 2026"],
        ["Acquiring", "All networks", "About 70% of Jamaica's POS"],
        ["Merchants", "Mastercard MSME phones", "February 2025"],
        ["Remittances", "Visa Direct, WU, MoneyGram", "Into debit and Lynk"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard credit and prepaid cards, the business Mastercards, Mastercard cards in NCB Pay, and phones for unbanked merchants.",
                "deals": "What it does not do: debit, the Lynk card, remittances, fraud tools or rewards."},
        "snb": {"dir": "Visa debit and cash-back credit, Visa Direct and the Lynk virtual card; Lynk and Jam-Dex as NCB's own rails; Western Union and MoneyGram.",
                "deals": "Where they meet: NCB's terminals and ePOS, which take every network."},
    },
    "tl": [
        ["Nov 2020", "Keycard retired into Visa and Mastercard"],
        ["Apr 2021", "NCB Mastercard Prepaid; Midas debit moving to Visa"],
        ["Dec 2021", "Lynk launched, first Jam-Dex wallet"],
        ["Mar 2023", "NCB Pay wallet"],
        ["Jun 2024", "ePOS Tap on Phone"],
        ["Feb 2025", "Mastercard phones for unbanked merchants"],
        ["Mar 2025", "Midas switched off; debit all Visa"],
        ["Oct 2025", "Hurricane Melissa"],
        ["Apr 2026", "Lynk Virtual Card on Visa"],
        ["Sep 2026", "Sheree Martin CEO; high-value cheques end"],
    ],
    "l": {
        "U": {"d": 1, "s": "Credit and prepaid holders carry Mastercard; debit holders carry Visa.",
              "gap": "Every account holder has Visa debit; Mastercard reaches travel, USD and prepaid cardholders and some merchants.",
              "neo": "Mastercard credit and prepaid holders, MSME merchants.", "snb": "Debit holders, Visa credit holders, Lynk users."},
        "L5": {"d": 0, "s": "The front doors are NCB's.", "gap": "App, online banking, branches and portals are NCB's own.", "neo": "None.", "snb": "App, online banking, branches, ABMs."},
        "L4": {"d": 0, "s": "The business lines carry Visa debit.", "gap": "Accounts come with Visa debit; lending, wealth and insurance have no network role.",
               "neo": "None.", "snb": "Accounts, SME fund, corporate, wealth, Guardian."},
        "L3": {"d": 1, "s": "NCB Miles spans both networks; the rest is NCB's.", "gap": "Rewards run on Visa debit and Mastercard credit; no network fraud tools named.",
               "neo": "NCB Miles on Mastercard credit.", "snb": "Fraud controls, digital lending, servicing."},
        "L2": {"d": 1, "s": "Credit split, prepaid on Mastercard, debit and Lynk on Visa.", "gap": "Visa has debit, the Lynk card and Visa Direct; Mastercard has prepaid, half the credit range and an acceptance programme.",
               "neo": "Mastercard credit, prepaid, business cards, MSME phones.", "snb": "Visa debit and credit, Lynk, Jam-Dex, clearing."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, owners, heritage, strategy."},
    },
    "t": area_lens(LAYERS),
}
