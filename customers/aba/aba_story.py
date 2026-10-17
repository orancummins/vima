"""ABA Bank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from aba_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Cambodia's largest bank as five discs that stack into one platform, from US$16.2 billion of assets and National "
       "Bank of Canada's ownership at the bottom to ABA Mobile, 104 branches and the merchant app at the top. Click the "
       "stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the "
       "layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("aff", "Affluent cardholders", "gem"),
    ("mer", "Merchants & sellers", "store"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates", "factory"),
    ("pub", "Public bodies & associations", "landmark"),
]
USERS_DESC = ("Six kinds of customer, about 6 million in all: everyday customers on ABA Mobile, affluent cardholders, the "
              "merchants behind the country's largest QR and POS network, small businesses, corporates, and the ministries "
              "and associations that collect payments through PayWay.")

WHO = {"con": "An ABA customer", "aff": "An affluent cardholder", "mer": "A merchant", "sme": "A small business",
       "corp": "A corporate treasurer", "pub": "A public body"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account opened in the app, a card, QR payments and face checks.",
     "steps": [("5.1", "app", "Open an account in ABA Mobile"), ("4.1", "deposits", "Keep savings at ABA"),
               ("2.4", "abapay", "Pay by ABA PAY and KHQR"), ("2.1", "visadebit", "Tap a debit card"),
               ("3.1", "facepass", "Confirm big payments with FacePass")]},
    {"id": "card", "who": "con", "name": "Get a card in minutes",
     "why": "Card Machines and virtual cards, on Visa, Mastercard, UnionPay or CSS.",
     "steps": [("2.3", "kiosk", "Print a card at a Card Machine"), ("2.1", "mcdebit", "Choose Mastercard debit"),
               ("2.3", "virtual", "Add a virtual card in the app"), ("2.5", "c2c", "Send money card to card")]},
    {"id": "affluent", "who": "aff", "name": "Spend and travel as an affluent customer",
     "why": "Visa holds ABA's affluent debit and credit; insurance comes through Etiqa.",
     "steps": [("2.2", "visacredit", "Take a Visa credit card"), ("2.1", "visadebit", "Spend on affluent Visa debit"),
               ("3.4", "etiqa", "Buy travel cover in the app"), ("3.2", "analytics", "Track spending")]},
    {"id": "merchant", "who": "mer", "name": "Take payments in a shop",
     "why": "The country's largest QR and POS acceptance network.",
     "steps": [("5.3", "merchantapp", "Sign up on the ABA Merchant app"), ("2.4", "khqr", "Show a KHQR code"),
               ("2.6", "pos", "Take cards on ABA POS"), ("3.3", "paysound", "Hear each payment with PaySound")]},
    {"id": "online", "who": "mer", "name": "Sell online",
     "why": "PayWay inside Shopify, Grab and partner checkouts.",
     "steps": [("2.6", "payway", "Add PayWay to the shop"), ("5.4", "partners", "Sell through Shopify"),
               ("2.6", "grab", "Get paid through Grab"), ("3.3", "qrapi", "Print dynamic QR on receipts")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "Loans, ABA Business and QR tools.",
     "steps": [("4.2", "loans", "Borrow for the business"), ("4.4", "ababusiness", "Run payroll on ABA Business"),
               ("3.3", "qrapi", "Collect by QR at the till")]},
    {"id": "corp", "who": "corp", "name": "Bank as a corporate",
     "why": "Corporate and investment banking, ABA Business and USD clearing.",
     "steps": [("4.3", "cib", "Finance with corporate banking"), ("4.3", "bonds", "Raise money through a bond"),
               ("4.4", "ababusiness", "Connect the ERP host to host"), ("2.5", "swift", "Pay suppliers abroad")]},
    {"id": "public", "who": "pub", "name": "Collect fees online",
     "why": "PayWay inside ministry portals and the Hajj Fund.",
     "steps": [("5.4", "partners", "Put PayWay in the portal"), ("2.6", "payway", "Take KHQR and card payments"),
               ("3.1", "docverify", "Verify bank documents")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Mastercard debit, prepaid and virtual cards, card-to-card transfers, and acceptance across POS and PayWay.",
     "steps": [("2.1", "mcdebit", "Mastercard debit and prepaid"), ("2.3", "virtual", "Virtual Mastercard in the app"),
               ("2.5", "c2c", "Card-to-card transfers"), ("2.6", "pos", "Mastercard at ABA POS"),
               ("2.6", "payway", "Mastercard on PayWay")]},
    {"id": "mcnext", "who": "mc", "name": "Where affluent credit, security and remittances could land",
     "why": "Where ABA has needs and Mastercard is not yet in: affluent credit held by Visa, stronger authentication, remittances for returning migrant workers, commercial cards for ABA Business and card acceptance beside KHQR.",
     "steps": [("2.2", "visacredit", "A World credit card against Visa's affluent book"), ("3.1", "facepass", "Identity Check and fraud scoring"),
               ("2.5", "swift", "Cross-border services for remittances"), ("4.4", "ababusiness", "Commercial and virtual cards"),
               ("2.6", "pos", "Tap on Phone beside KHQR"), ("3.2", "analytics", "Merchant data for spending insights")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across ABA Bank's map",
    "title": "A Visa-first card book in a QR country, with Mastercard in debit",
    "lead": "ABA is Cambodia's largest bank and its largest card issuer and acquirer. It issues Mastercard debit, prepaid and virtual cards and runs card-to-card transfers with Mastercard. Visa, though, collects most of the awards, holds the affluent debit and credit book, and supplies the CyberSource engine behind PayWay Plus. Most everyday payments run on the central bank's KHQR and Bakong rails, not on cards. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are ABA's (2025 results, April 2026) and National Bank of Canada's (quarter to 31 July 2026). ababank.com could not be read, so the card lineup rests on press releases and search results; programme-level network splits and volumes are not public.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa and Mastercard", "Plus UnionPay and CSS, from Card Machines"],
        ["Affluent cards", "Visa", "Debit and credit spend awards, 2024–25"],
        ["Prepaid", "Mastercard ⚠", "Prepaid-volume award, 2023"],
        ["Virtual cards", "Visa or Mastercard", "Customer's choice in ABA Mobile ⚠"],
        ["Transfers", "Mastercard, UnionPay", "Card to card, up to US$20,000 a month ⚠"],
        ["Gateway", "PayWay Plus", "Powered by Visa CyberSource"],
        ["Everyday payments", "KHQR and Bakong", "1.33bn Bakong transactions in 2025"],
        ["Awards", "Visa 18, Mastercard 3+", "For 2023–25 ⚠"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard debit, prepaid and virtual cards, card-to-card transfers, card machines that issue them, and acceptance at ABA's POS, ATMs and PayWay.",
                "deals": "What it does not do: affluent credit, gateway processing, QR, authentication, AI or insurance."},
        "snb": {"dir": "Visa debit and credit and CyberSource, UnionPay and CSS cards, KHQR and Bakong, SWIFT clearing through J.P. Morgan, and ABA's own security and AI.",
                "deals": "Where they meet: the card machines and PayWay, which take every network."},
    },
    "tl": [
        ["2014", "National Bank of Canada buys 10%"],
        ["May 2015", "UnionPay cards launched ⚠"],
        ["Oct 2019", "National Bank of Canada at 100%"],
        ["Oct 2020", "Bakong launched"],
        ["Mar 2022", "KHQR in ABA PAY ⚠"],
        ["Nov 2022", "Card Machines: Visa, Mastercard, UnionPay, CSS"],
        ["Early 2024", "Three Mastercard awards for 2023 ⚠"],
        ["Nov 2024", "PayWay Plus on Visa CyberSource; Grab"],
        ["Mar 2026", "Ten Visa awards for 2025"],
        ["Sep 2026", "Canadia previews a Mastercard World card"],
    ],
    "l": {
        "U": {"d": 1, "s": "Mastercard debit and virtual cardholders carry it.",
              "gap": "Debit holders split between Visa and Mastercard; affluent cardholders are on Visa; most people pay by QR.",
              "neo": "Mastercard debit, prepaid and virtual cardholders.", "snb": "Affluent Visa holders, QR payers, borrowers and corporates."},
        "L5": {"d": 1, "s": "ATMs take Mastercard and kiosks issue it.", "gap": "ABA Mobile, branches and partner platforms are ABA's own.",
               "neo": "Self-banking machines.", "snb": "ABA Mobile, branches, merchant app, partners."},
        "L4": {"d": 0, "s": "The business lines carry no network.", "gap": "Deposits, loans, corporate banking and ABA Business have no card programme found.",
               "neo": "None.", "snb": "Deposits, loans, corporate and investment banking, ABA Business."},
        "L3": {"d": 0, "s": "The services are ABA's own.", "gap": "FacePass, Navi, Analytics and PaySound are built in-house; Visa leads the security roadmap.",
               "neo": "None.", "snb": "Security, AI, merchant tools, insurance."},
        "L2": {"d": 1, "s": "Mastercard in debit, virtual cards and transfers; Visa ahead.", "gap": "Visa holds affluent cards and the gateway engine; KHQR carries most payments.",
               "neo": "Debit, prepaid, virtual, card-to-card, acceptance.", "snb": "Visa debit and credit, UnionPay, CSS, KHQR, Bakong, SWIFT."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, owner, leadership, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
