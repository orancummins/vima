"""Maybank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from maybank_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Malaysia's largest bank as five discs that stack into one platform, from RM696 billion of loans across "
       "Malaysia, Singapore and Indonesia at the bottom to the MAE app, Maybank2u and branches at the top. Click the "
       "stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up across "
       "the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in "
       "every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("isl", "Islamic banking customers", "flag"),
    ("aff", "Wealth customers", "gem"),
    ("sme", "Small businesses & merchants", "store"),
    ("corp", "Corporates", "factory"),
    ("reg", "Customers in Singapore & Indonesia", "globe"),
]
USERS_DESC = ("Six kinds of customer: everyday Malaysians on MAE and cards, Maybank Islamic's customers, Premier and "
              "Private wealth clients, small businesses and merchants, the corporates Global Banking serves, and "
              "customers of Maybank Singapore and Maybank Indonesia. A total customer count is not published ⚠.")

WHO = {"con": "A Maybank customer", "isl": "A Maybank Islamic customer", "aff": "A Premier client",
       "sme": "A small business", "corp": "A corporate treasurer", "reg": "A customer in Singapore or Indonesia"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank and pay day to day",
     "why": "The everyday loop: the MAE app, a Visa or Mastercard debit card that also runs on MyDebit, DuitNow QR and fraud checks.",
     "steps": [("5.1", "mae", "Open MAE"), ("2.3", "debit", "Pay with a debit card"), ("2.4", "maeqr", "Scan & Pay with DuitNow QR"),
               ("2.4", "duitnow", "Send money with DuitNow"), ("3.1", "fraud", "Protected from scams")]},
    {"id": "card", "who": "con", "name": "Borrow on a card",
     "why": "Malaysia's largest card book: Visa co-brands, Mastercard cash back and World Elite, and Amex in every Maybank 2 Cards pair.",
     "steps": [("2.1", "ccvisa", "Take a Petronas or Shopee Visa"), ("2.1", "ccmc", "Or a Mastercard"), ("2.1", "ccamex", "Or Maybank 2 Cards"),
               ("2.7", "applepay", "Add it to a phone wallet"), ("3.3", "treats", "Earn TREATS Points")]},
    {"id": "islamic", "who": "isl", "name": "Bank the Shariah way",
     "why": "Maybank Islamic's accounts and Ikhwan cards, with the new Nadi card for first-time borrowers.",
     "steps": [("4.2", "islamicbank", "Open an Islamic account"), ("2.2", "nadi", "Get a first card with Nadi"), ("2.2", "ikhwan", "Move up the Ikhwan range")]},
    {"id": "wealth", "who": "aff", "name": "Grow and travel well",
     "why": "Premier and Private banking, World Elite Mastercard privileges and Etiqa cover.",
     "steps": [("4.3", "wealth", "Join Premier"), ("2.1", "ccmc", "Carry a World Elite Mastercard"), ("3.3", "wemc", "Fly Malaysia Airlines business class"),
               ("4.5", "etiqa", "Protect it with Etiqa")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "SME banking, card acceptance and DuitNow QR at the counter.",
     "steps": [("4.1", "sme", "Open a business account"), ("2.5", "acquiring", "Take cards"), ("2.5", "qrpaybiz", "Take QR with QRPayBiz"),
               ("5.2", "m2u", "Run it on Maybank2E")]},
    {"id": "corp", "who": "corp", "name": "Move money across ASEAN",
     "why": "Global Banking, transaction banking and a regional payments platform.",
     "steps": [("4.4", "gb", "Bank with Global Banking"), ("4.4", "txn", "Manage cash and trade"), ("2.6", "xborder", "Pay across borders")]},
    {"id": "region", "who": "reg", "name": "Bank in Singapore or Indonesia",
     "why": "Maybank Singapore's mixed card range and Maybank Indonesia's Mastercard debit, Visa credit and Travel Pass.",
     "steps": [("4.6", "sgcards", "Take an XL or Family & Friends card"), ("4.7", "iddebit", "Use Maybank Debit Mastercard"),
               ("4.7", "idcards", "Take a Visa credit card"), ("4.7", "travelpass", "Book lounges with Travel Pass")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "World Elite and Cash Back cards, the Islamic range and Nadi, debit, Indonesia's debit and Travel Pass, and the Grab base now without a partner.",
     "steps": [("2.1", "ccmc", "World Elite & Cash Back Mastercard"), ("2.2", "ikhwan", "Ikhwan Mastercard range"), ("2.2", "nadi", "Nadi Mastercard Card-i"),
               ("2.3", "debit", "Mastercard Platinum Debit"), ("4.7", "travelpass", "Travel Pass in Indonesia"), ("2.1", "grabnext", "The former Grab cards")]},
    {"id": "mcnext", "who": "mc", "name": "Where cross-border, agents and fraud tools could land",
     "why": "Where Maybank has needs and Mastercard is not yet in: RM465 billion of cross-border flows, a new co-brand for the Grab base, an AI-led app, scam defences and acquiring tools.",
     "steps": [("2.6", "xborder", "Mastercard Move for cross-border flows"), ("2.1", "grabnext", "A new co-brand for the Grab base"),
               ("3.2", "ai", "Agent Pay in the next MAE"), ("3.1", "fraud", "Scam and identity tools"), ("2.5", "acquiring", "Merchant risk and Tap on Phone")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Maybank's map",
    "title": "One of three networks at Malaysia's largest issuer, as QR takes the growth",
    "lead": "Maybank issues on Visa, Mastercard and American Express. Mastercard carries the World Elite card, most of the Islamic Ikhwan range and the new Nadi card, Mastercard debit beside Visa debit, and in Indonesia the debit card and Travel Pass. Visa holds the biggest co-brands (Petronas, Shopee, the football cards), Amex sits in every Maybank 2 Cards pair, and the Grab Mastercard ended in September 2026. Meanwhile DuitNow QR in MAE, which uses no card network, doubled in 2025. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (2Q FY26 results, 27 August 2026; ROAR30, January 2026) or from Bank Negara, PayNet and press. Maybank's Malaysian and Singapore card pages could not be read; networks there come from comparison sites, and volumes by network are not public.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Credit (Malaysia)", "Visa, Mastercard, Amex", "Largest issuer; over 20% share in 2018 ⚠"],
        ["Premium", "World Elite Mastercard", "Perks reset January 2026"],
        ["Islamic cards", "Mostly Mastercard", "Nadi Card-i, July 2026 ⚠"],
        ["Co-brands", "Visa", "Petronas, Shopee, football clubs"],
        ["Grab card", "Mastercard, ended", "7 September 2026"],
        ["Debit", "Visa and Mastercard, on MyDebit", "Indonesia: Mastercard and GPN"],
        ["QR", "DuitNow QR in MAE", "3 billion QR payments in Malaysia, 2025"],
        ["Cross-border", "No public network role", "RM465 billion in 1H FY26"],
    ],
    "sides": {
        "neo": {"dir": "World Elite and Cash Back cards, the Ikhwan range and Nadi, Mastercard debit, Indonesia's debit and Travel Pass, and the former Grab cards.",
                "deals": "What it does not do: the big Visa co-brands, Amex, MyDebit, DuitNow QR, cross-border flows or fraud."},
        "snb": {"dir": "Visa's Petronas, Shopee and football cards, Amex and Maybank 2 Cards, PayNet's MyDebit and DuitNow, GPN and QRIS in Indonesia, and Maybank's own fraud and AI.",
                "deals": "Where they meet: debit in Malaysia and the Singapore card range, split between Visa and Mastercard."},
    },
    "tl": [
        ["Sep 1960", "Maybank opens in Kuala Lumpur"],
        ["2006", "Buys Amex's Malaysian charge-card business"],
        ["2008", "Buys Bank Internasional Indonesia"],
        ["Jun 2015", "Visa Checkout with Maybank announced"],
        ["May 2018", "20% of credit cards, 40% of merchants"],
        ["Aug 2020", "Grab Mastercard Platinum launched"],
        ["Oct 2024", "World Elite Mastercard Ikhwan"],
        ["Jul 2025", "XL cards launched in Singapore"],
        ["Jan 2026", "ROAR30; World Elite perks reset"],
        ["Mar 2026", "DuitNow QR doubles to 3 billion (2025)"],
        ["Jul 2026", "Nadi Mastercard Card-i ⚠; MAE QR in Samsung Wallet"],
        ["Aug 2026", "2Q FY26: cross-border RM465bn in a half"],
        ["Sep 2026", "Grab Mastercard discontinued"],
    ],
    "l": {
        "U": {"d": 1, "s": "Many Maybank cardholders carry Mastercard; many carry Visa or Amex.",
              "gap": "Premium, Islamic and debit customers often carry Mastercard; co-brand and Amex holders do not; QR users need no card.",
              "neo": "World Elite, Ikhwan and Nadi holders, debit users, Indonesian debit holders.", "snb": "Petronas, Shopee and football card holders, Amex holders, MyDebit and QR users."},
        "L5": {"d": 0, "s": "The front doors are Maybank's.", "gap": "MAE, Maybank2u, M2U ID and branches are the group's own.", "neo": "None.", "snb": "MAE, Maybank2u, branches, partners."},
        "L4": {"d": 1, "s": "Indonesia's debit and Travel Pass are Mastercard's; the rest has no network role.",
               "gap": "Maybank Indonesia runs debit on Mastercard and GPN and credit mostly on Visa; Singapore cards are split.",
               "neo": "Indonesia debit, Travel Pass, part of Singapore's cards.", "snb": "Visa credit in Indonesia, wealth, Global Banking, Etiqa."},
        "L3": {"d": 1, "s": "World Elite privileges ride on Mastercard; fraud and AI are Maybank's.",
               "gap": "No public Mastercard fraud, data or AI service; World Elite perks are the main Mastercard service.",
               "neo": "World Elite privileges.", "snb": "Fraud models, PayNet's fraud portal, AI, football sponsorships on Visa."},
        "L2": {"d": 1, "s": "Mastercard shares the cards with Visa and Amex; QR and transfers run on PayNet.",
               "gap": "Mastercard has premium, Islamic and some debit; Visa the largest co-brands; DuitNow QR and cross-border flows use no card network.",
               "neo": "World Elite, Ikhwan, Nadi, debit, former Grab cards.", "snb": "Visa co-brands, Amex, MyDebit, DuitNow QR, cross-border."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, footprint, technology, ROAR30."},
    },
    "t": area_lens(LAYERS),
}
