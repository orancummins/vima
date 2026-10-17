"""CaixaBank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from caixabank_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Spain's largest bank as five discs that stack into one platform, from 20.9 million customers and €693 billion "
       "of assets at the bottom to the CaixaBank and imagin apps, branches and partners at the top. Click the stack to open it. "
       "Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined in the "
       "order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("young", "Young & digital customers", "smartphone"),
    ("saver", "Savers & investors", "coins"),
    ("sme", "Small businesses & merchants", "store"),
    ("corp", "Companies", "factory"),
    ("port", "Customers in Portugal", "flag"),
]
USERS_DESC = ("Six kinds of customer, 20.9 million in all: everyday customers in Spain, the 4.2 million on imagin, savers "
              "and investors, small businesses and merchants, companies, and BPI's customers in Portugal.")

WHO = {"con": "A CaixaBank customer", "young": "An imagin customer", "saver": "A saver", "sme": "A small business",
       "corp": "A company", "port": "A BPI customer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a debit card on Visa or Mastercard, a wallet, the app and fraud checks.",
     "steps": [("4.1", "retail", "Open an account"), ("2.2", "debit", "Pay with a debit card"), ("2.5", "wallets", "Tap with a phone"),
               ("5.1", "app", "Run it in the app"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "bizum", "who": "con", "name": "Pay with Bizum",
     "why": "Send money to friends, pay in shops from May 2026 and, soon, across borders through the Wero link.",
     "steps": [("2.7", "bizum", "Send a Bizum"), ("2.7", "bizumshop", "Pay at the till with Bizum"), ("2.7", "europa", "Pay someone abroad via Wero")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "MyCard and the co-brands from CaixaBank Payments & Consumer, on Visa, with instalments in Apple Pay.",
     "steps": [("2.1", "mycard", "Take MyCard"), ("2.5", "paylater", "Split a purchase in Apple Pay"), ("2.1", "cobrands", "Earn Avios on Vueling Visa"),
               ("4.2", "consumer", "Borrow with consumer finance")]},
    {"id": "travel", "who": "young", "name": "Travel without fees",
     "why": "imagin's Mastercard travel card and the MoneyToTravel prepaid card.",
     "steps": [("4.5", "imaginbank", "Join imagin"), ("2.3", "imagintravel", "Pay abroad with the imagin card"), ("2.3", "moneytotravel", "Top up MoneyToTravel")]},
    {"id": "save", "who": "saver", "name": "Save and invest",
     "why": "Spain's leader in pensions and savings insurance.",
     "steps": [("5.2", "branches", "See an adviser"), ("4.4", "wealth", "Invest and insure with VidaCaixa")]},
    {"id": "merchant", "who": "sme", "name": "Take payments",
     "why": "Comercia's terminals, Tap to Pay on iPhone and Bizum at the till.",
     "steps": [("4.3", "business", "Open a business account"), ("2.6", "comercia", "Get a Comercia terminal"), ("2.6", "taptopay", "Take cards on an iPhone"),
               ("2.7", "bizumshop", "Accept Bizum in store")]},
    {"id": "suppliers", "who": "corp", "name": "Pay suppliers",
     "why": "The B2B virtual card service built with Mastercard, and corporate cards.",
     "steps": [("4.3", "cib", "Bank with CaixaBank"), ("2.4", "virtualb2b", "Pay suppliers with virtual cards"), ("2.4", "corporate", "Travel on Mastercard Corporate")]},
    {"id": "portugal", "who": "port", "name": "Bank in Portugal",
     "why": "BPI's accounts, cards and MB WAY.",
     "steps": [("4.6", "bpi", "Bank with BPI"), ("2.8", "bpicards", "Pay with a BPI card"), ("2.8", "mbway", "Pay with MB WAY")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Part of debit, the imagin travel card, prepaid travel, corporate cards and the new B2B virtual card platform.",
     "steps": [("2.2", "debit", "Debit cards on Mastercard"), ("2.3", "imagintravel", "imagin travel card"), ("2.3", "moneytotravel", "MoneyToTravel prepaid"),
               ("2.4", "corporate", "Mastercard Corporate"), ("2.4", "virtualb2b", "B2B virtual cards")]},
    {"id": "mcnext", "who": "mc", "name": "Where B2B, agents and A2A could land",
     "why": "Where CaixaBank has needs and Mastercard is not yet in: scaling commercial payments, Agent Pay after Visa's pilot, travel and FX on imagin, acquirer tools at Comercia, and fraud tools as Bizum and Wero grow.",
     "steps": [("2.4", "virtualb2b", "Scale B2B virtual cards"), ("3.2", "agentic", "Agent Pay beside Visa's pilot"), ("2.3", "imagintravel", "FX and benefits on imagin"),
               ("2.6", "comercia", "Acquirer risk tools at Comercia"), ("3.1", "fraud", "Fraud scoring for A2A payments")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across CaixaBank's map",
    "title": "Spain's card giant runs on Visa; Mastercard holds the corners",
    "lead": "CaixaBank issues 34 million cards and has 31% of Spanish card turnover. Its consumer credit range, its co-brands and its first agentic payment are Visa. Mastercard carries part of debit, the imagin travel card, prepaid travel, corporate cards and, since June 2026, the B2B virtual card platform. Bizum, now in shops and linking to Wero, competes with both. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (H1 2026 results, 29 July 2026) or from CaixaBank, Bizum and press. No group-wide network contract is public; the debit split, BPI's networks and some business cards are not stated.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Credit", "Visa", "MyCard and co-brands; 34m cards in all"],
        ["Debit", "Visa and Mastercard", "Split not public ⚠"],
        ["Travel", "Mastercard", "imagin card, February 2025"],
        ["B2B", "Mastercard", "Virtual cards, June 2026"],
        ["Agentic", "Visa", "First agent payment, July 2026"],
        ["Acquiring", "Comercia", "805,000 POS, 30.5% share"],
        ["A2A", "Bizum", "In shops May 2026; Wero link"],
    ],
    "sides": {
        "neo": {"dir": "Part of debit, imagin travel, prepaid travel ⚠, Mastercard Corporate ⚠ and B2B virtual cards, plus acceptance at Comercia's merchants.",
                "deals": "What it does not do: consumer credit, co-brands, agentic payments, fraud or loyalty."},
        "snb": {"dir": "Visa credit, co-brands, the Braille card and the agentic pilot; Bizum, Wero and SEPA Instant for account-to-account; Global Payments in acquiring.",
                "deals": "Where they meet: debit, wallets and instalments, where both networks are carried."},
    },
    "tl": [
        ["Dec 2016", "Masterpass first in Spain in CaixaBank Pay"],
        ["Sep 2021", "Vueling Visa co-brand"],
        ["May 2022", "Braille card with Visa and ONCE"],
        ["Feb 2025", "imagin travel card with Mastercard"],
        ["Aug 2025", "Apple Pay instalments on Visa and Mastercard credit"],
        ["Feb 2026", "Bizum, EuroPA and Wero start their link"],
        ["May 2026", "Bizum in shops, CaixaBank among the first"],
        ["Jun 2026", "B2B virtual cards with Mastercard"],
        ["Jul 2026", "First agentic payment, with Visa"],
    ],
    "l": {
        "U": {"d": 1, "s": "imagin travellers, some debit holders and corporate cardholders carry Mastercard.",
              "gap": "Credit cardholders carry Visa; imagin's travel card and part of debit carry Mastercard.",
              "neo": "imagin travellers, some debit holders, B2B and corporate users.", "snb": "Credit and co-brand holders, Bizum users, BPI customers."},
        "L5": {"d": 0, "s": "The front doors are CaixaBank's.", "gap": "Apps, branches and partners are the group's; co-brand partners are on Visa.",
               "neo": "None.", "snb": "Apps, branches, Visa co-brand partners."},
        "L4": {"d": 1, "s": "Business banking and imagin carry some Mastercard.", "gap": "Retail debit is split; consumer finance is Visa; wealth, mortgages and BPI have no visible Mastercard role.",
               "neo": "imagin, B2B and corporate cards.", "snb": "Consumer finance, wealth, mortgages, BPI."},
        "L3": {"d": 0, "s": "Agentic, fraud and loyalty are Visa's or CaixaBank's own.", "gap": "The first agentic payment ran on Visa; no Mastercard fraud or offers product found ⚠.",
               "neo": "None.", "snb": "Visa Intelligent Commerce, own fraud models, Visa co-brand loyalty."},
        "L2": {"d": 1, "s": "Mastercard in travel, B2B and part of debit; Visa in credit.", "gap": "Visa has the credit book; Mastercard has imagin travel and B2B virtual cards; Bizum competes at the till.",
               "neo": "Debit share, imagin travel, MoneyToTravel, B2B virtual cards, Mastercard Corporate.", "snb": "Visa credit and co-brands, Bizum, Wero link, SEPA Instant."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, owners, brands, technology, plan."},
    },
    "t": area_lens(LAYERS),
}
