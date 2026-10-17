"""Banco Itaú Paraguay's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from itauparaguay_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Paraguay's largest card issuer by balances as five discs that stack into one platform, from Gs 40.7 trillion of "
       "assets and an Itaú Unibanco parent at the bottom to the Itaú PY app, 25 branches and WhatsApp agencies at the top. "
       "Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up "
       "across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday Paraguayans", "user-round"),
    ("pb", "Personal Bank clients", "gem"),
    ("sme", "Small & medium businesses", "briefcase-business"),
    ("merch", "Merchants on Pik", "store"),
    ("agro", "Farmers & ranchers", "flag"),
    ("corp", "Corporates & institutions", "factory"),
]
USERS_DESC = ("Six kinds of client, more than 726,000 in all: everyday account and card holders, Personal Bank's affluent "
              "clients, SMEs, the shops and entrepreneurs taking payments on Pik, Itaú Campo's farmers and ranchers, and "
              "Itaú BBA's corporates and state institutions.")

WHO = {
    "con": "A Paraguayan customer", "pb": "A Personal Bank client", "sme": "A small business", "merch": "A merchant",
    "agro": "A rancher", "corp": "A corporate treasurer",
}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank and pay day to day",
     "why": "An account with a Mastercard debit card, the app, transfers by alias and QR, and fraud checks behind it.",
     "steps": [("4.3", "accounts", "Open an account"), ("2.1", "debit", "Pay with Mastercard debit"), ("5.1", "app", "Run it in the Itaú PY app"),
               ("2.5", "transfers", "Transfer by alias or pay by QR"), ("3.1", "fraud", "Protected by fraud monitoring")]},
    {"id": "cards", "who": "con", "name": "Carry a card and collect rewards",
     "why": "Paraguay's largest card book by balances: Visa, Mastercard or the only American Express, with points and promotions.",
     "steps": [("2.2", "credit", "Take an Itaú credit card"), ("2.3", "cobrands", "Choose a co-brand"), ("3.3", "interventajas", "Earn Interventajas points"),
               ("3.3", "offers", "Use the month's promotions"), ("2.4", "wallets", "Add it to the phone")]},
    {"id": "travel", "who": "pb", "name": "Travel as a Personal Bank client",
     "why": "A premium card, miles, wallets abroad and FX at the bank's desk.",
     "steps": [("4.3", "pbank", "Bank with Personal Bank"), ("2.2", "premium", "Carry Infinite, Black or Platinum"),
               ("2.3", "cobrands", "Earn AAdvantage or LATAM miles"), ("2.5", "qrpix", "Pay by Pix in Brazil"), ("2.7", "fx", "Buy dollars")]},
    {"id": "home", "who": "con", "name": "Buy a home or a car",
     "why": "The leader in housing credit, with AFD funding, pre-approved loans and electric-car finance.",
     "steps": [("4.2", "mortgage", "Take a mortgage"), ("4.1", "auto", "Finance a car, even an EV"), ("4.1", "preapproved", "Draw a pre-approved loan")]},
    {"id": "merchant", "who": "merch", "name": "Take payments on Pik",
     "why": "QR or a SmartPOS from Itaú, daily settlement, and customers from Tienda Naranja.",
     "steps": [("2.6", "pik", "Accept cards and QR on Pik"), ("3.3", "tiendanaranja", "Sell on Tienda Naranja"), ("4.4", "sme", "Borrow for stock")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "Payroll, suppliers, direct debits and cards for staff, run from the web or the API.",
     "steps": [("4.4", "sme", "Open as an Empresas client"), ("4.4", "cashmgmt", "Pay staff and suppliers"),
               ("4.4", "corpcard", "Give executives company cards"), ("3.2", "openapi", "Connect the ERP by API")]},
    {"id": "agro", "who": "agro", "name": "Finance a harvest or a herd",
     "why": "Itaú Campo lends for soy, maize and cattle cycles, with a spend-control card and FX cover.",
     "steps": [("4.5", "campo", "Borrow with Itaú Campo"), ("4.5", "procampo", "Control spend on Pro Campo"),
               ("2.7", "fx", "Hedge with FX forwards"), ("5.2", "branches", "Meet the banker in the Chaco")]},
    {"id": "corp", "who": "corp", "name": "Fund and run a company",
     "why": "Itaú BBA for syndicated loans and debt, with cash management and APIs.",
     "steps": [("4.6", "ibba", "Raise a loan or bond"), ("4.4", "cashmgmt", "Run payroll and payments"),
               ("3.2", "openapi", "Automate by API"), ("4.7", "invest", "Place the treasury with Itaú Invest")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Every debit card, Mastercard Black at the top, co-brands on either network, Apple Pay since 2024 and 3D Secure.",
     "steps": [("2.1", "debit", "Mastercard Debit on every account"), ("2.2", "premium", "Mastercard Black"),
               ("2.3", "cobrands", "AAdvantage and Centenario on Mastercard"), ("2.4", "wallets", "Apple Pay for Mastercard cardholders"),
               ("3.1", "threeds", "3D Secure on Mastercard cards")]},
    {"id": "mcnext", "who": "mc", "name": "Where tokens, fraud and acceptance could land",
     "why": "Where Itaú Paraguay has needs and Mastercard is not yet in: Click to Pay is Visa-only, transfers are booming on rules-based checks, Pik is building acquiring, and business cards have no stated network.",
     "steps": [("2.4", "c2p", "Click to Pay for Mastercard debit"), ("3.1", "fraud", "Scam and fraud scoring"),
               ("2.6", "pik", "Acceptance and risk tools for Pik"), ("4.4", "corpcard", "Commercial and virtual cards"),
               ("3.3", "offers", "Card-linked offers"), ("2.2", "premium", "A World Elite tier"), ("2.7", "fx", "Cross-border payouts")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Itaú Paraguay's map",
    "title": "Debit on Mastercard, the digital edge on Visa",
    "lead": "Every Itaú Paraguay debit card is a Mastercard, and Mastercard Black, AAdvantage and Centenario sit in the credit book. But Visa carries most credit programmes, the prepaid card and the bank's only Click to Pay, and American Express, issued by Itaú alone, drives its card leadership. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (2025 sustainability report; balance sheets to 30 September 2026) or FIX SCR's (April 2026). Mastercard's newsroom could not be read directly, and no source gives the split of cards or volume by network.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Mastercard", "Every account; Maestro, Cirrus and Infonet"],
        ["Credit", "Visa, Mastercard, Amex", "496,360 cards; 35.6% of balances; no split published"],
        ["Premium", "Mastercard Black", "Beside Visa Infinite and Amex Platinum"],
        ["Amex", "Sole issuer", "Platinum, Green, Práctica"],
        ["Click to Pay", "Visa only", "Mastercard debit not enrolled"],
        ["Wallets", "Apple Pay, Google Pay", "Mastercard Apple Pay, Nov 2024 ⚠; FAQ lists Visa"],
        ["Processor", "Bancard", "Itaú owns 9.09%"],
        ["Parent", "Itaú Unibanco", "Mastercard deal and Agent Pay in Brazil only"],
    ],
    "sides": {
        "neo": {"dir": "Debit for every account, Mastercard Black, AAdvantage and Centenario by choice, Apple Pay for Mastercard cardholders and 3D Secure.",
                "deals": "What it does not yet do at Itaú Paraguay: Click to Pay, fraud and scam tools, Pik's acceptance tools, commercial cards, offers or cross-border, by any public account."},
        "snb": {"dir": "Visa on Infinite, LATAM, Touring, Interventajas Platinum, prepaid, Pro Campo and Click to Pay; Amex exclusive; Bancard processing; SIPAP transfers and QR; Pix into Brazil.",
                "deals": "Where they meet: the credit book, co-brands on either network, the phone wallets and Pik's terminals."},
    },
    "tl": [
        ["Jul 2010", "Interbanco becomes Banco Itaú Paraguay"],
        ["Mar 2015", "Parent signs a Mastercard network deal in Brazil"],
        ["Apr 2023", "Pik launches"],
        ["Nov 2024", "Apple Pay for Itaú Mastercard cardholders ⚠"],
        ["Jun 2025", "Open Banking APIs for companies"],
        ["Feb 2026", "Continental passes Itaú in 2025 profit"],
        ["Mar 2026", "Parent runs live Agent Pay in Brazil"],
        ["Sep 2026", "Nine-month profit Gs 1,014 billion"],
    ],
    "l": {
        "U": {"d": 1, "s": "Every account holder carries Mastercard debit; credit holders split three ways.",
              "gap": "Account holders meet Mastercard through debit; credit cardholders are split between Visa, Mastercard and Amex; merchants, farmers and corporates deal mostly with Itaú's own rails.",
              "neo": "Debit holders, Black and co-brand holders.", "snb": "Visa and Amex cardholders, Pik merchants, borrowers, corporates."},
        "L5": {"d": 0, "s": "The front doors are Itaú's.", "gap": "Apps, branches, ATMs and digital agencies are the bank's own.",
               "neo": "None.", "snb": "Itaú PY app, branches, ATMs, WhatsApp agencies."},
        "L4": {"d": 1, "s": "Accounts carry Mastercard debit; lending has no network role.",
               "gap": "Accounts and Personal Bank bring Mastercard cards; mortgages, Itaú Campo, Itaú BBA and investments do not, and the business cards' networks are unstated or Visa.",
               "neo": "Accounts, Personal Bank.", "snb": "Lending, Itaú Campo, Itaú BBA, invest and insure."},
        "L3": {"d": 1, "s": "3D Secure covers Mastercard; fraud and rewards are Itaú's.",
               "gap": "3D Secure runs on Visa and Mastercard; fraud monitoring, Open Banking APIs, Interventajas and Tienda Naranja are the bank's own.",
               "neo": "3D Secure.", "snb": "Fraud monitoring, APIs, Interventajas, Tienda Naranja."},
        "L2": {"d": 1, "s": "Debit is Mastercard; credit, prepaid and Click to Pay lean Visa.",
               "gap": "Mastercard has debit and part of credit; Visa has most credit programmes, prepaid and Click to Pay; Amex is exclusive; transfers and Pix run on SIPAP and Bancard.",
               "neo": "Debit, Black, co-brands, wallets.", "snb": "Visa credit and Click to Pay, Amex, SIPAP, Pix, Pik."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's; Itaú owns part of Bancard and Visa shares.",
               "neo": "None.", "snb": "Capital, the parent, Bancard stake, strategy."},
    },
    "t": area_lens(LAYERS),
}
