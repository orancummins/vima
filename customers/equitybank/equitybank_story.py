"""Equity Bank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from equitybank_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Kenya's second-largest bank and East and Central Africa's broadest banking group as five discs that stack into one "
       "platform, from KES 2.16 trillion of assets and six banks at the bottom to the Equity Mobile app, Equitel and 92,572 "
       "agents at the top. Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver "
       "it light up across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard "
       "goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("sme", "Small businesses & merchants", "store"),
    ("farm", "Farmers & value chains", "hand-coins"),
    ("corp", "Corporates & traders", "briefcase-business"),
    ("dia", "Diaspora & cross-border senders", "earth"),
    ("ins", "Policyholders & patients", "shield-check"),
]
USERS_DESC = ("Six kinds of customer behind 23.3 million accounts in six countries: everyday customers, small businesses and "
              "1.4 million merchants, farmers in value chains, corporates and traders, the diaspora, and insurance "
              "policyholders and clinic patients.")

WHO = {"con": "An Equity customer", "sme": "A small business", "farm": "A farmer", "corp": "A corporate treasurer",
       "dia": "A Kenyan abroad", "ins": "A policyholder"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a Visa or Mastercard debit card, the app and USSD, Equitel and mobile loans.",
     "steps": [("4.1", "accounts", "Open an account"), ("2.1", "debit", "Choose Visa or Mastercard debit"),
               ("5.1", "app", "Bank in the app or on *247#"), ("2.5", "equitel", "Pay on Equitel"), ("4.1", "eazzyloan", "Borrow on the phone")]},
    {"id": "cards", "who": "con", "name": "Pay and borrow on a card",
     "why": "Visa credit, Amex Green and Gold, and Mastercard World Elite debit at the top.",
     "steps": [("2.1", "premiumdebit", "Carry a World Elite debit card"), ("2.2", "visacredit", "Take a Visa credit card"),
               ("2.2", "amexcredit", "Or an Amex Gold"), ("3.4", "carddeals", "Use Equity Deals")]},
    {"id": "merchant", "who": "sme", "name": "Get paid as a merchant",
     "why": "A Pay With Equity till for every wallet, a card terminal for every network, and the Jenga gateway online.",
     "steps": [("2.4", "pwe", "Take M-Pesa, Equitel and PesaLink on one till"), ("2.3", "posacq", "Accept cards"),
               ("2.3", "jenga", "Sell online through Jenga"), ("4.2", "msme", "Borrow for stock")]},
    {"id": "fanikisha", "who": "sme", "name": "Grow a woman-run business",
     "why": "Fanikisha tiers bundle loans, health cover and a card that steps up to Mastercard World Elite.",
     "steps": [("4.2", "fanikisha", "Join a Fanikisha tier"), ("2.1", "premiumdebit", "Step up the card"),
               ("4.5", "insurance", "Cover the family")]},
    {"id": "farm", "who": "farm", "name": "Farm inside a value chain",
     "why": "Ecosystem loans through buyers such as KTDA, agents near the farm, and foundation programmes.",
     "steps": [("5.3", "agents", "Bank at an agent"), ("4.3", "agri", "Borrow against the value chain"),
               ("1.5", "egf", "Join a SASTAIN programme")]},
    {"id": "corp", "who": "corp", "name": "Run a company's money",
     "why": "Equity Online for Business, trade finance, Eazzy FX and Mastercard corporate cards.",
     "steps": [("5.2", "online", "Pay on Equity Online for Business"), ("4.4", "corporate", "Finance trade"),
               ("2.6", "eazzyfx", "Deal FX on Eazzy FX"), ("2.2", "corpcard", "Give staff Mastercard corporate cards")]},
    {"id": "diaspora", "who": "dia", "name": "Send money home and abroad",
     "why": "Mastercard Cross-Border Services at the branch, Western Union in the app, partners paying into M-Pesa.",
     "steps": [("5.3", "diaspora", "Bank as a Kenyan abroad"), ("2.6", "remit", "Receive through Western Union or Remitly"),
               ("2.6", "mccbs", "Send from a branch with Mastercard")]},
    {"id": "health", "who": "ins", "name": "Insure and get care",
     "why": "Life, general and health insurance sold mostly digitally, and Equity Afya clinics.",
     "steps": [("5.1", "app", "Buy cover on the phone"), ("4.5", "insurance", "Hold an Equity policy"), ("4.5", "afya", "Visit an Equity Afya clinic")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Debit beside Visa, World and World Elite at the top, corporate credit, prepaid, branch remittances and acceptance.",
     "steps": [("2.1", "debit", "Mastercard debit beside Visa"), ("2.1", "premiumdebit", "World and World Elite debit"),
               ("2.2", "corpcard", "Corporate credit"), ("2.6", "mccbs", "Cross-Border Services"), ("2.3", "posacq", "Acceptance at Equity terminals")]},
    {"id": "mcnext", "who": "mc", "name": "Where the 2023 agreement could land",
     "why": "Where Equity has needs and Mastercard is contracted but not yet visible: Community Pass for value chains, QR and tap on phone for tills, digital cross-border send, virtual cards, cyber defence and AI agents.",
     "steps": [("3.1", "communitypass", "Community Pass for farmers and traders"), ("2.4", "pwe", "QR and tap on phone at tills"),
               ("2.6", "mccbs", "Cross-border send in the app"), ("2.2", "virtual", "Virtual commercial cards"),
               ("3.2", "cyber", "Fraud and cyber tools"), ("3.3", "aidata", "Agent Pay for an AI-first bank")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Equity Bank's map",
    "title": "A ten-year Mastercard deal in a market that pays by phone",
    "lead": "Equity has issued Mastercard since 2013 and signed a ten-year agreement in September 2023 for all six of its countries. Mastercard sits beside Visa on debit, holds the World and World Elite tier and corporate credit, and runs branch remittances. Visa holds consumer credit and dollar debit, and Amex holds premium credit and exclusive Kenyan acquiring. Most of Equity's money moves on Equitel, Pay With Equity tills, M-Pesa and PesaLink, with no card network involved. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (HY 2026 investor booklet, 19 August 2026) or from Equity's July 2025 products handbook, Mastercard and press. Channel figures are read from booklet charts. Equity does not publish card volumes by network, and the live status of Community Pass, QR and tap on phone is not public.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Agreement", "Ten years, six countries", "Signed 18 September 2023"],
        ["Debit", "Visa and Mastercard", "Customer's choice; World Elite at the top"],
        ["Consumer credit", "Visa; Amex premium", "Amex exclusive issuer in Kenya"],
        ["Corporate credit", "Mastercard", "Corporates and SMEs"],
        ["Acquiring", "Every network", "Exclusive Amex acquirer in Kenya"],
        ["Remittances", "Mastercard Cross-Border Services", "Branches, April 2024"],
        ["Mobile money", "Equitel, PWE, M-Pesa", "213.6m PWE payments in H1 2026 ⚠"],
        ["Community Pass", "Contracted", "No live deployment found ⚠"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard debit beside Visa, World and World Elite debit, corporate credit, prepaid, branch remittances and acceptance.",
                "deals": "Contracted but not yet visible: Community Pass, QR, tap on phone, virtual cards and joint cyber work."},
        "snb": {"dir": "Visa consumer credit and dollar debit, Amex premium credit and acquiring, Equitel, PWE tills, M-Pesa and PesaLink, and Western Union.",
                "deals": "Where they meet: the debit counter, where customers choose Visa or Mastercard."},
    },
    "tl": [
        ["Jan 2013", "Mastercard debit and prepaid partnership"],
        ["2013–14", "Exclusive Amex issuer in Kenya"],
        ["Oct 2014", "Equitel SIMs issued"],
        ["Feb 2015", "Mastercard prepaid card"],
        ["Jun 2018", "Exclusive Amex acquiring extended"],
        ["Jun 2021", "Visa Infinite in Rwanda"],
        ["Sep 2023", "Ten-year Mastercard agreement"],
        ["Apr 2024", "Mastercard Cross-Border Services"],
        ["Sep 2025", "M-Pesa to banks via PesaLink"],
        ["Aug 2026", "H1 2026: 2030 plan for 100 million customers"],
    ],
    "l": {
        "U": {"d": 1, "s": "Many cardholders carry Mastercard; most payers use phones.",
              "gap": "Debit holders choose Visa or Mastercard; credit holders carry Visa or Amex; most customers pay through Equitel, tills and M-Pesa.",
              "neo": "Mastercard debit, World Elite and corporate cardholders.", "snb": "Visa and Amex credit holders, Equitel and M-Pesa users."},
        "L5": {"d": 1, "s": "Branches and ATMs take Mastercard; the rest is Equity's.", "gap": "App, USSD, Equity Online and agents are Equity's own; branch remittances use Mastercard.",
               "neo": "ATMs, branch remittances.", "snb": "App, USSD, Equity Online, agents."},
        "L4": {"d": 1, "s": "Cards ride along with accounts and business banking.", "gap": "Accounts and Fanikisha come with Visa or Mastercard; loans, insurance and investment banking have no network role.",
               "neo": "Debit with accounts, corporate cards, Fanikisha premium debit.", "snb": "Eazzy loans, agri finance, insurance, EIB."},
        "L3": {"d": None, "s": "Community Pass and cyber work are contracted, not visible.", "gap": "KYC, AI and APIs are Equity's own; the Mastercard clauses have no public deployment.",
               "neo": "Community Pass and joint cyber work, contracted ⚠.", "snb": "Unified KYC, AI engines, Jenga APIs."},
        "L2": {"d": 1, "s": "Split cards; mobile money dominates.", "gap": "Mastercard shares debit and holds corporate credit and branch remittances; Visa and Amex hold consumer credit; Equitel, PWE and PesaLink carry the volume.",
               "neo": "Debit, World Elite, corporate credit, prepaid, Cross-Border Services.", "snb": "Visa and Amex credit, Equitel, PWE, M-Pesa, PesaLink, Western Union."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's; the Mastercard Foundation is a separate body.", "neo": "None.", "snb": "Capital, six banks, technology group, strategy."},
    },
    "t": area_lens(LAYERS),
}
