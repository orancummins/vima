"""Banca Intesa Beograd's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from intesabeograd_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Serbia's largest bank as five discs that stack into one platform, from RSD 1 trillion of assets and its Intesa "
       "Sanpaolo parent at the bottom to Intesa Mobi, 134 branches and the country's biggest merchant network at the top. "
       "Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up "
       "across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in "
       "every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("young", "Young customers", "graduation-cap"),
    ("aff", "Magnifica & affluent", "gem"),
    ("sb", "Small businesses & farmers", "briefcase"),
    ("merch", "Merchants", "store"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Six kinds of customer, about 1.34 million in all: everyday customers, young people on the IN account, "
              "Magnifica and affluent clients, small businesses and farmers, the merchants on its acquiring network, "
              "and the corporates and SMEs it lends to.")

WHO = {"con": "A Banca Intesa customer", "young": "A young customer", "aff": "A Magnifica client", "sb": "A small business",
       "merch": "A merchant", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: a Hit package, Visa or Dina debit, a phone wallet, Intesa Mobi and 3-D Secure.",
     "steps": [("4.1", "packages", "Open an Intesa Hit package"), ("2.1", "visadebit", "Pay with Visa debit"),
               ("2.4", "applepay", "Tap with Apple Pay or Google Pay"), ("5.1", "mobi", "Run it in Intesa Mobi"),
               ("3.1", "tds", "Confirm online payments")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "Mastercard, Visa or Amex credit, split into instalments, with coupons in the app.",
     "steps": [("2.2", "mccredit", "Take a Mastercard credit card"), ("2.7", "cardinst", "Split a purchase into instalments"),
               ("3.3", "galerija", "Use coupons from Galerija popusta")]},
    {"id": "young", "who": "young", "name": "Start banking young",
     "why": "The IN account for 16 to 26-year-olds, its Visa Inspire card and #withSAVE goals.",
     "steps": [("4.1", "packages", "Open an IN account"), ("2.1", "visadebit", "Get a Visa Inspire card"),
               ("4.3", "savings", "Save with #withSAVE"), ("2.6", "ips", "Pay friends and shops by IPS QR")]},
    {"id": "loan", "who": "con", "name": "Take a loan from the phone",
     "why": "A cash loan signed with a state e-signature, or a mortgage approved in a week.",
     "steps": [("3.1", "consentid", "Activate ConsentID and an e-signature"), ("4.2", "cashloan", "Sign an online cash loan"),
               ("4.2", "mortgage", "Apply for a mortgage")]},
    {"id": "premium", "who": "aff", "name": "Bank as a Magnifica client",
     "why": "Premium banking with Visa Infinite debit, Mastercard Platinum credit and Intesa Invest funds.",
     "steps": [("4.1", "magnifica", "Join Magnifica"), ("2.1", "visainfinite", "Carry Visa Infinite debit"),
               ("2.2", "mcplatinum", "Travel with Mastercard Platinum"), ("4.3", "funds", "Invest in Intesa Invest funds")]},
    {"id": "sme", "who": "sb", "name": "Run a small business or farm",
     "why": "A Biz package, business cards, the Biz portal and subsidised farm loans.",
     "steps": [("4.4", "smallbiz", "Open a BizPRO package"), ("2.3", "bizdebit", "Pay with a Visa business card"),
               ("2.3", "mcbusiness", "Defer costs on Mastercard Business"), ("5.2", "bizportal", "Manage it on the Biz portal"),
               ("4.4", "farmer", "Borrow as an Intesa Farmer")]},
    {"id": "merchant", "who": "merch", "name": "Take payments",
     "why": "Serbia's largest acquiring network: POS, Soft POS, a web gateway and IPS.",
     "steps": [("5.4", "partners", "Join through 'Bolji način'"), ("2.5", "acquiring", "Take cards on a POS"),
               ("2.5", "softpos", "Turn a phone into a POS"), ("2.5", "ecom", "Sell online"), ("2.6", "ips", "Accept IPS instant payments")]},
    {"id": "corp", "who": "corp", "name": "Bank as a corporate",
     "why": "Corporate lending, euro payments over SEPA and leasing.",
     "steps": [("4.5", "corporate", "Borrow from Corporate & SME"), ("2.6", "sepa", "Pay suppliers by SEPA"),
               ("4.5", "leasing", "Lease equipment")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Credit cards from Standard to Platinum, Mastercard Business, tokens in Apple Pay and Google Pay, and acceptance across the largest network.",
     "steps": [("2.2", "mccredit", "Mastercard credit cards"), ("2.2", "mcplatinum", "Mastercard Platinum benefits"),
               ("2.3", "mcbusiness", "Mastercard Business credit"), ("2.4", "applepay", "Mastercard tokens in wallets"),
               ("2.5", "acquiring", "Acceptance on 20,000 POS"), ("5.4", "partners", "'Bolji način' with Visa")]},
    {"id": "mcnext", "who": "mc", "name": "Where Air Serbia, merchants and instalments could land",
     "why": "Where Banca Intesa has needs and Mastercard is not yet in: the Air Serbia co-brand card, offers in Galerija popusta, online acceptance, instalments, commercial cards and fraud signals.",
     "steps": [("3.3", "airserbia", "Air Serbia co-brand on Mastercard"), ("3.3", "galerija", "Card-linked offers"),
               ("2.5", "ecom", "Click to Pay and tokens online"), ("2.7", "cardinst", "Instalments online"),
               ("2.3", "mcbusiness", "Virtual and corporate cards"), ("3.1", "fraud", "Scam and identity signals")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Banca Intesa Beograd's map",
    "title": "Serbia's first Mastercard bank, now Visa on debit",
    "lead": "Banca Intesa brought Mastercard to Serbia in 2002 and once carried more than 90% of the country's Mastercard turnover. It joined Visa in 2003 and moved its everyday cards there: Visa made up 78.7% of its cards by 2017, and its May 2026 tariff lists only Visa and DinaCard debit. Mastercard keeps the credit range, Mastercard Business, wallet tokens and acceptance on the largest merchant network; American Express is exclusive to the bank. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (2024 annual report; card tariff from 4 May 2026) or from the Serbian press and Intesa Sanpaolo. No 2025 annual report or local H1 2026 results were found. Card counts by network have not been published since 2017.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa and DinaCard", "No Mastercard debit on the May 2026 tariff"],
        ["Credit", "Mastercard, Visa, Amex", "Mastercard Standard to Platinum; Amex exclusive since 2006"],
        ["Premium", "Visa Infinite and Mastercard Platinum", "Debit 2017; credit 2021"],
        ["Business", "Visa debit, Mastercard credit", "Mastercard Business the only credit card"],
        ["Wallets", "Apple Pay, Google Pay", "Visa Dec 2020; Mastercard Apr 2021"],
        ["Acceptance", "All networks", "20,000 POS; 71% of online acquiring (2024)"],
        ["Instant", "NBS IPS and SEPA", "QR payments; SEPA from May 2026"],
        ["Co-brand", "Air Serbia", "Letter of intent May 2026 ⚠ network open"],
    ],
    "sides": {
        "neo": {"dir": "Credit cards from Standard to Platinum, Mastercard Business, wallet tokens, 3-D Secure, and acceptance across the bank's merchants.",
                "deals": "What it does not do: debit, premium debit, business debit, instalments on debit, instant payments or offers."},
        "snb": {"dir": "Visa debit (Inspire to Infinite) and Visa credit, DinaCard debit, American Express credit, NBS IPS, SEPA and the bank's own offers and fraud tools.",
                "deals": "Where they meet: the Air Serbia co-brand card, still open."},
    },
    "tl": [
        ["2002", "First Mastercard cards in Serbia ⚠"],
        ["Oct 2003", "Joins Visa"],
        ["Jun 2006", "First chip Mastercard; 670,000 Mastercard cards"],
        ["2006", "Exclusive American Express deal"],
        ["Sep 2012", "Visa Inspire becomes the packaged debit card"],
        ["Nov 2017", "Visa Infinite; Visa 78.7% of cards"],
        ["Dec 2020", "Apple Pay for Visa"],
        ["Apr 2021", "Apple Pay for Mastercard"],
        ["2021", "Mastercard Platinum credit card"],
        ["May 2026", "SEPA live; Air Serbia co-brand LoI"],
        ["Oct 2026", "Popović chairs the bank association"],
    ],
    "l": {
        "U": {"d": 1, "s": "Credit cardholders carry Mastercard; debit holders carry Visa or Dina.",
              "gap": "Every package's debit card is Visa or DinaCard; Mastercard arrives through credit and business credit.",
              "neo": "Credit and business credit cardholders.", "snb": "Debit holders, Amex holders, IPS users."},
        "L5": {"d": 0, "s": "The front doors are the bank's.", "gap": "Intesa Mobi, the portals and branches are its own; 'Bolji način' is shared with Visa.",
               "neo": "Bolji način (with Visa).", "snb": "Intesa Mobi, portals, branches."},
        "L4": {"d": 1, "s": "Packages bundle Visa debit with Mastercard or Amex credit.", "gap": "Accounts carry Visa and Dina debit; loans, savings and corporate lending have no network role.",
               "neo": "Mastercard Standard and Gold in packages.", "snb": "Visa and Dina debit, Amex Blue, loans, funds."},
        "L3": {"d": 0, "s": "Security, data and offers are the bank's own.", "gap": "3-D Secure is shared; antifraud, AI and Galerija popusta are in-house; Air Serbia is undecided.",
               "neo": "3-D Secure.", "snb": "Antifraud, ConsentID, Data & AI, Galerija popusta."},
        "L2": {"d": 1, "s": "Mastercard on credit and acceptance; Visa and Dina on debit.", "gap": "Visa holds debit and premium debit; Mastercard holds most credit and business credit.",
               "neo": "Mastercard credit, Platinum, Business, tokens, acceptance.", "snb": "Visa debit and credit, DinaCard, Amex, IPS, SEPA."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's, though its card history began with it.",
               "neo": "None.", "snb": "Capital, parent, leadership, technology."},
    },
    "t": area_lens(LAYERS),
}
