"""BIAT's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from biat_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Tunisia's largest bank as five discs that stack into one platform, from TND 22.3 billion of deposits at the bottom "
       "to MyBIAT, 206 branches and BIAT France at the top. Click the stack to open it. Choose who you are and what you "
       "want to do, and the areas that deliver it light up across the layers, joined in the order they act. Switch to the "
       "Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("young", "Young people & graduates", "graduation-cap"),
    ("aff", "Affluent customers", "gem"),
    ("tre", "Tunisians abroad", "earth"),
    ("pro", "Professionals & SMEs", "briefcase"),
    ("corp", "Corporates & institutions", "factory"),
]
USERS_DESC = ("Six kinds of customer, about 950,000 in all: everyday customers, young people and graduates, affluent "
              "Platinum and ELITE clients, Tunisians resident abroad, professionals and SMEs, and the corporates and "
              "institutions that make up about 62% of the bank's lending.")

WHO = {"con": "A BIAT customer", "young": "A young customer", "aff": "An affluent customer", "tre": "A Tunisian abroad",
       "pro": "A professional", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "An account, a Visa or Mastercard debit card, MyBIAT and card security.",
     "steps": [("4.1", "packs", "Open an account"), ("2.1", "classic", "Pay with a Visa or Mastercard debit card"),
               ("5.1", "mybiat", "Run it in MyBIAT"), ("3.1", "fraud", "Get alerts and block the card")]},
    {"id": "young", "who": "young", "name": "Start out",
     "why": "Pack FIRST with a free Mastercard, a FLY prepaid card and a first loan.",
     "steps": [("2.1", "mcnational", "Get Pack FIRST with a Mastercard"), ("2.4", "prepaid", "Use a FLY prepaid card"),
               ("4.2", "loans", "Take a first loan"), ("5.1", "mybiat", "Manage it in MyBIAT")]},
    {"id": "spread", "who": "con", "name": "Spread a purchase",
     "why": "Flexy instalments and TEMPO credit replace post-dated cheques.",
     "steps": [("3.1", "risk", "Get a limit"), ("2.3", "flexy", "Pay in six instalments with Flexy"),
               ("2.3", "tempo", "Or revolve on a TEMPO Visa")]},
    {"id": "travel", "who": "con", "name": "Travel abroad",
     "why": "Under exchange controls, the tourist allowance goes on a Mastercard.",
     "steps": [("5.3", "branches", "Show a passport in branch"), ("2.4", "travel", "Load the allowance on BIATRAVEL"),
               ("3.4", "assur", "Travel insured")]},
    {"id": "affluent", "who": "aff", "name": "Bank as a premium client",
     "why": "Classe Platinum on Mastercard or Classe ELITE on Visa Infinite, with offers and investments.",
     "steps": [("4.1", "packs", "Join Classe Platinum or ELITE"), ("2.2", "platinum", "Carry Mastercard Platinum"),
               ("2.2", "infinite", "Or Visa Infinite"), ("3.2", "privileges", "Use BIAT Privilèges"),
               ("4.5", "tunisievaleurs", "Invest with Tunisie Valeurs")]},
    {"id": "diaspora", "who": "tre", "name": "Bank from abroad",
     "why": "Tounessna, transfers through BIAT France and foreign-currency cards.",
     "steps": [("5.4", "trechannels", "Meet BIAT France in Paris"), ("4.1", "tounessna", "Open Pack Tounessna"),
               ("2.7", "biatfrance", "Send money home"), ("2.4", "fxprepaid", "Spend with a Tounessna card")]},
    {"id": "merchant", "who": "pro", "name": "Take payments",
     "why": "Terminals and e-commerce acceptance for every network, with a Business card for expenses.",
     "steps": [("2.6", "tpe", "Install a terminal"), ("2.6", "ecom", "Sell online with BIAT E-Commerce"),
               ("2.5", "business", "Pay expenses on a Mastercard Business card"), ("5.1", "mybiat", "Track it in MyBIAT")]},
    {"id": "corp", "who": "corp", "name": "Finance and trade as a corporate",
     "why": "Trade finance with the AfDB guarantee, syndications and MyBIAT Corporate.",
     "steps": [("5.2", "mybiatcorp", "Bank on MyBIAT Corporate"), ("4.3", "corporate", "Import under the AfDB guarantee"),
               ("4.4", "bfi", "Raise a syndicated loan"), ("4.5", "fx", "Hedge FX")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The travel-allowance card, the Business range, Platinum, entry-pack debit and half the classic choice, plus acceptance.",
     "steps": [("2.4", "travel", "BIATRAVEL on Mastercard"), ("2.5", "business", "Mastercard Business cards"),
               ("2.2", "platinum", "Mastercard Platinum"), ("2.1", "mcnational", "Entry-pack Mastercard"),
               ("2.6", "tpe", "Acceptance at BIAT merchants")]},
    {"id": "mcnext", "who": "mc", "name": "Where tokens, instalments and remittances could land",
     "why": "Where BIAT has needs and Mastercard is not yet in: tokens as SMT builds a tokenised national scheme, Click to Pay for e-commerce, instalments for Flexy, remittances through BIAT France, offers for BIAT Privilèges and fraud scoring.",
     "steps": [("5.1", "mybiat", "Tokenised cards in MyBIAT"), ("2.6", "ecom", "Click to Pay for BIAT E-Commerce"),
               ("2.3", "flexy", "Instalments on Flexy"), ("2.7", "biatfrance", "Mastercard Move for BIAT France"),
               ("3.2", "privileges", "Card-linked offers"), ("3.1", "fraud", "Fraud scoring against Visa's monitoring")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across BIAT's map",
    "title": "A Visa-first bank where Mastercard carries the travel and business cards",
    "lead": "Visa has backed BIAT's cards for more than 30 years and signed a six-year partnership in September 2022; it carries Visa Infinite, Premier, the TEMPO credit card, every prepaid card and most campaigns. Mastercard carries the travel-allowance card most customers use abroad, the Business range for companies, Platinum and the entry-pack debit, and is one of two choices for classic debit. No BIAT–Mastercard agreement or digital programme is public, and SMT is building a tokenised national scheme for the end of 2026. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are BIAT's own (2025 annual report, August 2026; H1 2026 shareholder letter, September 2026) or from BCT data reported in the Tunisian press. Networks come from BIAT's product pages; the split of cards between Visa and Mastercard is not published, and Flexy's network is not stated.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Scheme partner", "Visa", "30+ years; six-year deal, Sep 2022"],
        ["Classic debit", "Visa or Mastercard", "Customer's choice; split not published"],
        ["Top card", "Visa Infinite", "First in Tunisia, Nov 2014"],
        ["Travel allowance", "Mastercard", "BIATRAVEL, up to TND 6,000 a year"],
        ["Business cards", "Mastercard", "Business, Gold, Premium since 2016"],
        ["Credit & prepaid", "Visa", "TEMPO, CASH, FLY, H'DYA"],
        ["Split payment", "Flexy", "Oct 2025; network not stated ⚠"],
        ["Domestic switch", "SMT", "National scheme planned end-2026 ⚠"],
    ],
    "sides": {
        "neo": {"dir": "BIATRAVEL, the Business cards, Platinum, entry-pack debit, half of classic debit, and acceptance at BIAT's terminals and websites.",
                "deals": "What it does not do: the top card, credit, prepaid, fraud monitoring, campaigns, remittances or wallets."},
        "snb": {"dir": "Visa's Infinite, Premier, TEMPO and prepaid cards, fraud monitoring and campaigns; SMT's domestic switch, mobile wallets and TUNPAY; IYU Europe for remittances.",
                "deals": "Where they meet: classic debit, where customers choose either network, and SMT's planned tokenised scheme."},
    },
    "tl": [
        ["Nov 2014", "First Visa Infinite in Tunisia"],
        ["Jun 2016", "Mastercard Business cards launched"],
        ["Jan 2018", "BIATRAVEL Mastercard upgraded with Priceless"],
        ["Jun 2022", "National mobile-payment switch run by SMT ⚠"],
        ["Sep 2022", "Six-year Visa partnership"],
        ["Oct 2025", "BIAT Flexy split-payment card"],
        ["Dec 2025", "SMT plans a tokenised national scheme"],
        ["May 2026", "TUNPAY mobile-payment label"],
        ["Aug 2026", "BIAT Privilèges with FreeOui"],
        ["End-2026", "National scheme due ⚠"],
    ],
    "l": {
        "U": {"d": 1, "s": "Travellers, business cardholders and Platinum clients carry Mastercard.",
              "gap": "Travel-allowance and business cardholders carry Mastercard; Infinite, credit and prepaid holders carry Visa.",
              "neo": "Travellers, business cardholders, Platinum clients, entry-pack customers.", "snb": "ELITE clients, TEMPO and prepaid holders, diaspora senders."},
        "L5": {"d": 0, "s": "The front doors are BIAT's.", "gap": "MyBIAT, branches and BIAT France are the bank's own; no wallet or tokens yet.",
               "neo": "None.", "snb": "MyBIAT, MyBIAT Corporate, branches, BIAT France."},
        "L4": {"d": 0, "s": "The business lines carry cards but no network role.", "gap": "Entry packs carry Mastercard and ELITE Visa; loans, trade and markets have no network role.",
               "neo": "Entry packs.", "snb": "Classe ELITE, loans, trade finance, markets."},
        "L3": {"d": 0, "s": "Fraud, offers and campaigns are BIAT's or Visa's.", "gap": "Visa supplies fraud monitoring and runs card campaigns; BIAT Privilèges is built with FreeOui.",
               "neo": "None.", "snb": "Visa fraud monitoring and campaigns, FreeOui, Assurances BIAT."},
        "L2": {"d": 1, "s": "Mastercard in travel and business cards; Visa elsewhere.", "gap": "Mastercard carries BIATRAVEL, Business and Platinum; Visa carries Infinite, credit and prepaid; SMT switches domestic payments.",
               "neo": "BIATRAVEL, Business cards, Platinum, part of debit, acceptance.", "snb": "Visa premium, credit and prepaid cards, SMT, IYU Europe."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, owners, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
