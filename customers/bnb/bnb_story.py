"""Banco Nacional de Bolivia's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from bnb_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Bolivia's third-largest bank as five discs that stack into one platform, from USD5.4 billion of assets and a "
       "licence dating from 1872 at the bottom to the BNB Móvil app, online banking and 663 service points at the top. "
       "Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up "
       "across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes "
       "in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Personal customers", "user-round"),
    ("home", "Homebuyers", "house"),
    ("inv", "Savers & investors", "coins"),
    ("micro", "Microentrepreneurs", "store"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Six kinds of customer: personal customers, homebuyers, savers and investors, microentrepreneurs, small "
              "businesses and the corporates that make up a third of the loan book. BNB does not publish customer numbers.")

WHO = {"con": "A BNB customer", "home": "A homebuyer", "inv": "A saver", "micro": "A microentrepreneur",
       "sme": "A small business", "corp": "A company finance team"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: a savings account, a debit card, QR payments in the app, and cash back.",
     "steps": [("4.4", "savings", "Open a savings account"), ("2.1", "debit", "Pay with a debit card"), ("2.4", "qr", "Pay by QR"),
               ("5.1", "app", "Run it in BNB Móvil"), ("3.4", "cashback", "Earn Cashback")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "Visa cards from Classic to Excellence, points and annual-fee discounts.",
     "steps": [("2.2", "visacredit", "Take a Visa credit card"), ("3.4", "puntos", "Collect BNB Puntos"), ("3.1", "security", "Set limits and stay safe")]},
    {"id": "abroad", "who": "con", "name": "Send money abroad",
     "why": "SWIFT and remittance partners, or USDT as a bridge, in a year the boliviano floated.",
     "steps": [("2.6", "cripto", "Buy USDT in Cuenta Cripto"), ("2.5", "intl", "Send dollars abroad")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "Mortgages are 38% of the book, with social-housing terms up to 30 years.",
     "steps": [("5.3", "branches", "Apply in a branch"), ("4.1", "mortgage", "Take a mortgage"), ("4.5", "insurance", "Insure it")]},
    {"id": "invest", "who": "inv", "name": "Save and invest",
     "why": "Term deposits online, funds from BNB SAFI and stockbroking from BNB Valores.",
     "steps": [("4.4", "deposits", "Open a term deposit online"), ("4.5", "safi", "Buy a fund with QR SAFI"), ("4.5", "valores", "Trade through BNB Valores")]},
    {"id": "micro", "who": "micro", "name": "Run a market stall",
     "why": "Microcredit, QR collection with Bille's Mi Negocio and the app.",
     "steps": [("4.3", "sme", "Take a microcredit"), ("2.6", "bille", "Collect with Bille"), ("2.4", "qr", "Get paid by QR")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "SME loans, leasing, QR acceptance, online banking and cash back for customers.",
     "steps": [("4.3", "sme", "Borrow for the business"), ("4.5", "leasing", "Lease equipment"), ("2.4", "qr", "Take QR payments"),
               ("5.2", "net", "Bank online"), ("3.4", "cashback", "Bring customers back with Cashback")]},
    {"id": "corp", "who": "corp", "name": "Manage company spending",
     "why": "Corporate lending, the new Mastercard card range, APIs and trade finance.",
     "steps": [("4.2", "corporate", "Bank with BNB"), ("2.3", "mccorp", "Give staff Mastercard corporate cards"), ("2.3", "cta", "Book travel on the CTA"),
               ("3.3", "apis", "Connect by API"), ("4.2", "trade", "Issue guarantees and letters of credit")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The corporate range launched in September 2025, and a processor BNB part-owns.",
     "steps": [("2.3", "mccorp", "Corporate and Corporate Black on Mastercard"), ("2.3", "cta", "CTA travel card on Mastercard"),
               ("3.5", "atc", "Processing through ATC ⚠")]},
    {"id": "mcnext", "who": "mc", "name": "Where company cards, cross-border and offers could land",
     "why": "Where BNB has needs and Mastercard is not yet in: payouts abroad against USDT bridges, card-linked offers for Cashback, QR acceptance risk, fraud tools for a 97%-digital bank, and the Visa consumer book.",
     "steps": [("2.5", "intl", "Cross-border payouts and FX"), ("2.6", "cripto", "Stablecoin settlement"), ("3.4", "cashback", "Card-linked offers"),
               ("2.4", "qr", "Acceptance and QR"), ("3.1", "security", "Fraud and token services"), ("2.2", "visacredit", "A consumer card choice")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Banco Nacional de Bolivia's map",
    "title": "A Visa bank that gave Mastercard its company cards",
    "lead": "BNB's consumer credit cards, from Classic to Excellence, are Visa, as are Visa Empresarial and the Presto BNPL card it issues, and its debit cards probably are too. In September 2025 it launched a corporate range with Mastercard: Corporate Black, Corporate, T&E, B2B and a travel account. Everyday money increasingly moves by QR Simple, the Bille wallet and USDT, outside any card network. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (2025 annual report; statements to 30 June 2026; tariff from 16 October 2026). BNB publishes no customer, card or spend counts. The debit network is inferred from a 2025 'Paga con Visa y gana' campaign, and no Mastercard press release on the corporate launch was found.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Consumer credit", "Visa", "Classic, Platinum, Signature, Excellence"],
        ["Debit", "Visa ⚠", "Inferred from a 2025 campaign"],
        ["Corporate cards", "Mastercard", "Corporate Black, Corporate, T&E, B2B, CTA; Sep 2025"],
        ["Business card", "Visa", "Visa Empresarial"],
        ["BNPL", "Visa", "Presto card issued by BNB, 2023"],
        ["Everyday payments", "QR Simple", "Domestic QR, no network"],
        ["Abroad", "SWIFT and USDT", "Cuenta Cripto, 2026"],
    ],
    "sides": {
        "neo": {"dir": "The corporate card range and travel account, acceptance at BNB's merchants, and possibly processing through ATC ⚠.",
                "deals": "What it does not do: consumer credit, debit, BNPL, QR, the wallet or transfers abroad."},
        "snb": {"dir": "Visa consumer, business and BNPL cards and probably debit; QR Simple; Bille; USDT and SWIFT for payments abroad.",
                "deals": "Where they meet: company spending, where Visa Empresarial sits beside the Mastercard range."},
    },
    "tl": [
        ["1872", "Banco Nacional de Bolivia incorporated"],
        ["2023", "Immediate QR payments"],
        ["May 2023", "Presto BNPL card on Visa"],
        ["Jan 2025", "Electronic payment instruments manager appointed"],
        ["Sep 2025", "Mastercard corporate card range"],
        ["2025", "'Paga con Visa y gana' campaign"],
        ["May 2026", "Cuenta Cripto BNB for USDT"],
        ["Jun 2026", "Boliviano floated at Bs9.73"],
        ["Oct 2026", "Tariff keeps Visa consumer and Mastercard corporate ranges"],
    ],
    "l": {
        "U": {"d": 1, "s": "Company cardholders carry Mastercard; personal customers carry Visa.",
              "gap": "Corporates using the new range carry Mastercard; consumers, small businesses on Visa Empresarial and Presto users carry Visa.",
              "neo": "Corporate cardholders.", "snb": "Personal customers, small businesses, Presto users, QR and wallet users."},
        "L5": {"d": 0, "s": "The front doors are BNB's.", "gap": "App, online banking, branches and partners are the bank's own.", "neo": "None.", "snb": "BNB Móvil, BNB Net+, branches, ATMs."},
        "L4": {"d": 0, "s": "The business lines have no network role, except corporate spending.", "gap": "Mortgages, loans, deposits and group companies carry no card network; corporate clients now get Mastercard cards.",
               "neo": "Corporate clients' cards.", "snb": "Mortgages, loans, deposits, leasing, funds."},
        "L3": {"d": 0, "s": "Services are BNB's own.", "gap": "Cashback runs on debit and QR, BNB Puntos on Visa cards; no Mastercard fraud or data tools are public; ATC may process both networks ⚠.",
               "neo": "ATC processing ⚠.", "snb": "Cashback, BNB Puntos, APIs, analytics, security."},
        "L2": {"d": 1, "s": "Corporate cards on Mastercard; the rest on Visa, QR or USDT.", "gap": "Mastercard carries the corporate range; Visa has consumer, business and BNPL cards and probably debit; QR Simple and USDT bypass cards.",
               "neo": "Corporate Black, Corporate, T&E, B2B, CTA.", "snb": "Visa cards, QR Simple, Bille, USDT, SWIFT."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, licence, board, core and AI."},
    },
    "t": area_lens(LAYERS),
}
