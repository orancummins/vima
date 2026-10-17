"""Access Bank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from accessbank_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Nigeria's largest bank as five discs that stack into one platform, from N51 trillion of assets and a pan-African "
       "group at the bottom to AccessMore, USSD, branches and 750,000 agents at the top. Click the stack to open it. "
       "Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined in "
       "the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("women", "Women (W)", "users-round"),
    ("sme", "Small businesses", "briefcase"),
    ("diaspora", "Nigerians abroad", "plane"),
    ("hnw", "Private clients", "gem"),
    ("corp", "Corporates & traders", "factory"),
]
USERS_DESC = ("Six kinds of customer, more than 60 million across the group: everyday customers, women served by W, "
              "7.5 million small businesses, Nigerians abroad, private-bank clients, and the corporates and traders "
              "that corporate, commercial and international banking serve.")

WHO = {"con": "An Access Bank customer", "women": "A W customer", "sme": "A small business", "diaspora": "A Nigerian abroad",
       "hnw": "A private client", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: open an account in the app, pay by card or transfer, and stay protected.",
     "steps": [("3.1", "kyc", "Open an account digitally"), ("5.1", "app", "Run it in AccessMore"), ("2.1", "visadebit", "Pay with a debit card"),
               ("2.6", "nip", "Send a NIP transfer"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "domestic", "who": "con", "name": "Pay with a local card",
     "why": "Verve and AfriGO cards for spending in Nigeria, issued instantly at the branch.",
     "steps": [("5.3", "branches", "Collect a card at a branch"), ("2.2", "verve", "Pay with Verve"), ("2.2", "afrigo", "Or use AfriGO")]},
    {"id": "borrow", "who": "con", "name": "Borrow",
     "why": "QuickBucks loans in the app, a credit line on the debit card, or a Visa credit card.",
     "steps": [("4.1", "quickbucks", "Take a QuickBucks loan"), ("2.3", "dts", "Switch on DTS credit"), ("2.3", "visacredit", "Use a Visa credit card")]},
    {"id": "women", "who": "women", "name": "Grow a women-led business",
     "why": "W loans and cards, an agent nearby and SME tools.",
     "steps": [("4.1", "women", "Join W"), ("4.2", "sme", "Borrow for the business"), ("5.4", "closa", "Bank through a Closa agent")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "An SME account, POS, AccessPing alerts and pre-approved loans.",
     "steps": [("4.2", "sme", "Open an SME account"), ("2.5", "pos", "Take payments on POS"), ("3.2", "accessping", "Get WhatsApp payment alerts"),
               ("2.6", "nip", "Collect by transfer")]},
    {"id": "diaspora", "who": "diaspora", "name": "Bank from abroad",
     "why": "Remote onboarding, money sent home through Access Africa, and a diaspora mortgage.",
     "steps": [("2.7", "diaspora", "Open an account remotely"), ("2.7", "accessafrica", "Send money home"), ("4.1", "mortgages", "Take a diaspora mortgage")]},
    {"id": "private", "who": "hnw", "name": "Travel and spend as a private client",
     "why": "The private bank, the Black Card on Visa Infinite and Amex Platinum rewards.",
     "steps": [("4.4", "private", "Join the private bank"), ("2.3", "amex", "Carry Amex Platinum"), ("3.4", "rewards", "Use rewards abroad")]},
    {"id": "trade", "who": "corp", "name": "Trade across Africa and beyond",
     "why": "Corporate banking, cross-border payments, the UK bank and a Visa corporate card.",
     "steps": [("4.3", "cib", "Bank with CIB"), ("2.7", "accessafrica", "Pay across Africa"), ("4.5", "ukbank", "Finance trade through London or Hong Kong"),
               ("2.3", "visacorp", "Issue staff corporate cards")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Access Africa on Mastercard Move, Mastercard debit and prepaid in Nigeria, and AccessU in Ghana.",
     "steps": [("2.7", "accessafrica", "Cross-border on Mastercard Move"), ("2.1", "mcdebit", "Mastercard debit"),
               ("2.4", "prepaid", "Mastercard prepaid"), ("4.6", "accessu", "AccessU youth cards in Ghana")]},
    {"id": "mcnext", "who": "mc", "name": "Where AccessMore, SMEs and the group could land",
     "why": "Where Access has needs and Mastercard is not yet in: tokenised virtual cards, scam and identity tools for transfer channels, SME and commercial cards, rewards, and AccessU across the group.",
     "steps": [("2.4", "virtual", "Tokenised virtual cards"), ("3.1", "fraud", "Scam and identity scoring"),
               ("4.2", "sme", "SME and commercial cards"), ("3.4", "rewards", "Card-linked offers for AccessRewards+"),
               ("4.6", "subsidiaries", "AccessU across the subsidiaries")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Access Bank's map",
    "title": "A Visa-led bank whose cross-border runs on Mastercard",
    "lead": "Visa carries every Access Bank credit card, the premium debit tiers, the Black Card and the corporate card launched in January 2026. Verve and the CBN's AfriGO carry domestic cards, Amex holds the top travel cards, and most money moves as NIBSS instant transfers. Mastercard has a naira debit and prepaid card, Access Africa's cross-border payments on Mastercard Move since May 2024, and AccessU youth cards in Ghana. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Access Bank's own (2025 annual report, June 2026; Q1 2026 results, April 2026) or from Access Holdings, NIBSS, Interswitch and the press. H1 2026 results were not found. Card volumes by network are not published; Mastercard's newsroom could not be read directly.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Credit", "Visa", "Naira, USD, Black Card, corporate (Jan 2026)"],
        ["Debit", "Visa, Mastercard, Verve", "Visa holds the premium tiers"],
        ["Domestic", "Verve, AfriGO", "First live AfriGO card, March 2023"],
        ["Premium travel", "American Express", "First Amex cards in Nigeria, 2023"],
        ["Cross-border", "Mastercard Move", "Access Africa, May 2024"],
        ["Transfers", "NIBSS NIP", "11.2 billion a year, nationally"],
        ["Ghana", "Mastercard", "AccessU youth cards, July 2025"],
    ],
    "sides": {
        "neo": {"dir": "Cross-border payments on Mastercard Move, Mastercard debit and naira prepaid, AccessU in Ghana, and acceptance at Access POS.",
                "deals": "What it does not do: credit, premium or corporate cards, domestic cards, instant transfers, fraud, AI or rewards."},
        "snb": {"dir": "Visa credit, premium debit and corporate cards; Verve and AfriGO domestic cards; Amex travel cards; NIBSS NIP for transfers; Access's own fraud, AI and APIs.",
                "deals": "Where they meet: debit and prepaid, where Visa, Mastercard and Verve sit side by side."},
    },
    "tl": [
        ["2019", "Amex acquiring agreement; Diamond merger"],
        ["Dec 2020", "Visa business debit for SMEs"],
        ["Mar 2023", "First live AfriGO card"],
        ["Jun 2023", "First Amex cards in Nigeria"],
        ["May 2024", "Access Africa on Mastercard Move"],
        ["Jul 2025", "AccessU Mastercard cards in Ghana; AfrAsia bought"],
        ["Dec 2025", "Verve passes 100 million cards"],
        ["Jan 2026", "Visa Corporate Credit Card"],
        ["Jul 2026", "16 Euromoney awards"],
    ],
    "l": {
        "U": {"d": 1, "s": "Some debit and prepaid holders and cross-border senders use Mastercard.",
              "gap": "Credit, private and corporate clients carry Visa or Amex; most customers pay by transfer or Verve.",
              "neo": "Mastercard debit and prepaid holders, Access Africa users, AccessU in Ghana.", "snb": "Visa and Verve cardholders, Amex and Black Card clients, transfer users."},
        "L5": {"d": 0, "s": "The front doors are Access's own.", "gap": "AccessMore, USSD, branches and agents run on Access and NIBSS rails.",
               "neo": "None.", "snb": "AccessMore, USSD, branches, Closa agents."},
        "L4": {"d": 1, "s": "AccessU in Ghana is Mastercard; the rest is Visa or no network.", "gap": "Private banking is Visa Infinite and Amex; SME cards are Visa; AccessU shows a Mastercard model in Ghana.",
               "neo": "AccessU, Ghana.", "snb": "Retail loans, SME, CIB, private bank, UK bank."},
        "L3": {"d": 0, "s": "Services are Access's own.", "gap": "Fraud, KYC, AI and APIs are in-house; rewards lean on Amex and Visa.",
               "neo": "None found.", "snb": "Fraud controls, AccessPing, wallet APIs, Amex and Visa rewards."},
        "L2": {"d": 1, "s": "Move runs cross-border; Mastercard is one of three debit networks.", "gap": "Visa holds credit and premium debit; Verve and AfriGO hold domestic cards; NIP carries transfers.",
               "neo": "Access Africa on Move, Mastercard debit and prepaid.", "snb": "Visa credit and debit, Amex, Verve, AfriGO, NIBSS NIP."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, leadership, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
