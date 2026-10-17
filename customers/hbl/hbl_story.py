"""HBL's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from hbl_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Pakistan's largest bank by customers as five discs that stack into one platform, from an Rs 8 trillion balance "
       "sheet at the bottom to HBL Mobile, about 2,000 branches and 54,000 Konnect agents at the top. Click the stack to "
       "open it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("aff", "Prestige & Premium clients", "gem"),
    ("sme", "Small businesses", "briefcase"),
    ("farm", "Farmers", "hand-coins"),
    ("unb", "Unbanked & benefit recipients", "users-round"),
    ("corp", "Corporates & government", "factory"),
]
USERS_DESC = ("Six kinds of customer, 40 million in all: everyday customers, Prestige and Premium clients, small businesses, "
              "farmers, the unbanked and benefit recipients Konnect reaches, and the corporates and government bodies HBL banks.")

WHO = {"con": "An HBL customer", "aff": "A Prestige client", "sme": "A small business", "farm": "A farmer",
       "unb": "A Konnect customer", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a debit card on one of four networks, the app, Raast and card controls.",
     "steps": [("4.1", "retail", "Open an account"), ("2.1", "debit", "Pay with an HBL debit card"), ("5.1", "app", "Run it in HBL Mobile"),
               ("2.4", "raast", "Send money by Raast"), ("3.1", "security", "Switch card use on and off")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "A third of Pakistan's credit-card spend, booked in the app, mostly on Visa.",
     "steps": [("5.1", "app", "Apply in HBL Mobile"), ("2.2", "credit", "Take an HBL CreditCard"), ("2.5", "hblpay", "Tap with HBL Pay"),
               ("3.2", "offers", "Earn points and offers")]},
    {"id": "prestige", "who": "aff", "name": "Bank as a Prestige client",
     "why": "Lounges, a Mastercard World debit card and a Visa Platinum credit card.",
     "steps": [("5.2", "branches", "Visit a Prestige lounge"), ("4.1", "prestige", "Join Prestige or Premium"), ("2.1", "world", "Carry a World debit card"),
               ("2.2", "platinum", "Add a Platinum credit card"), ("4.7", "wealth", "Invest with HBL Asset Management")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "SME banking, Mastercard business debit, the largest POS network and cash management.",
     "steps": [("4.3", "sme", "Open an SME relationship"), ("2.1", "bizdebit", "Pay with a business debit card"),
               ("2.3", "acquiring", "Take cards on SmartPOS"), ("4.4", "cashmgmt", "Collect and pay through HBL Pay Business")]},
    {"id": "farm", "who": "farm", "name": "Finance a farm",
     "why": "HBL and HBL Microfinance lend more to farmers than anyone; Zarai sells the inputs.",
     "steps": [("5.2", "branches", "Visit a farm branch"), ("4.3", "agri", "Borrow for the crop"), ("4.6", "mfb", "Or borrow from HBL Microfinance"),
               ("4.5", "g2p", "Receive a subsidy on a card")]},
    {"id": "unbanked", "who": "unb", "name": "Get paid and pay without a branch",
     "why": "Konnect agents, government payments, Raast and Visa QR.",
     "steps": [("5.3", "agents", "Open an account at an agent"), ("4.5", "konnect", "Use a Konnect account"), ("4.5", "g2p", "Receive a BISP payment"),
               ("2.4", "raast", "Send by Raast"), ("4.5", "kqr", "Pay a shop by Visa QR")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "Corporate lending, Rs 23.8 trillion of cash management, payroll and the China corridor.",
     "steps": [("4.4", "corporate", "Borrow from HBL"), ("4.4", "cashmgmt", "Run cash management"), ("4.4", "payroll", "Pay staff"),
               ("2.6", "remit", "Trade and settle with China")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Business and World debit, Mastercard debit alongside Visa, UnionPay and PayPak, Easy Savings and Priceless, and tokens.",
     "steps": [("2.1", "bizdebit", "Business debit on Mastercard"), ("2.1", "world", "World debit on Mastercard"), ("2.1", "debit", "Classic and Gold debit on Mastercard or Visa"),
               ("3.2", "offers", "Easy Savings and Priceless"), ("2.5", "hblpay", "Mastercard tokens in HBL Pay")]},
    {"id": "mcnext", "who": "mc", "name": "Where credit, acquiring and G2P could land",
     "why": "Where HBL has scale and Mastercard is thin: the credit book, the largest POS estate, government and subsidy cards, remittances, wallets and fraud tools.",
     "steps": [("2.2", "credit", "Mastercard credit and commercial cards"), ("2.3", "acquiring", "Acquirer risk and merchant data"),
               ("4.5", "g2p", "Social and subsidy cards"), ("2.6", "remit", "Inbound remittances on Move"),
               ("2.5", "gpay", "Tokens as Apple Pay arrives"), ("3.1", "security", "Scam and fraud scoring")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across HBL's map",
    "title": "One of four networks at Pakistan's biggest card bank",
    "lead": "HBL issues one in five Pakistani debit cards and carries a third of the country's credit-card spend. Mastercard, a partner since 2013, is one of four networks on its debit cards and owns the premium World debit card and, since August 2025, business debit. Visa holds the Platinum credit card and most credit card art, Konnect's QR and HBL's acceptance tie-ups; UnionPay signed a strategic MoU in September 2026; PayPak and Raast are the state-backed rails. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are HBL's own (2025 annual report; H1 2026 results) or from Mastercard, UnionPay, the SBP and press. HBL does not publish its card base by network; the credit-card split is read from a 2024 fact sheet and current card art.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Mastercard, Visa, UnionPay, PayPak", "6.4 million cards; split unknown ⚠"],
        ["Premium debit", "Mastercard World", "World and World Business"],
        ["Business debit", "Mastercard", "Launched August 2025"],
        ["Credit", "Visa (Platinum); Visa and Mastercard ⚠", "39% of Pakistan's card spend"],
        ["Co-badge", "PayPak + UnionPay", "Launched July 2026"],
        ["Acquiring", "All schemes; Visa mPOS", "26% of national POS volume"],
        ["Konnect QR", "Visa QR", "Branchless banking"],
        ["Instant", "Raast", "2,755 million payments in FY26"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard debit alongside Visa, World and business debit, Easy Savings and Priceless, Identity Check and tokens, and acceptance at HBL's POS.",
                "deals": "What it does not do: Platinum credit, Konnect QR, mPOS, the China corridor, PayPak, Raast or G2P cards in public view."},
        "snb": {"dir": "Visa credit, QR, mPOS and the PayZen gateway; UnionPay debit, co-badge and MoU; PayPak debit and the group's PayPak credit card; Raast.",
                "deals": "Where they meet: the debit card base and the POS estate, which take every scheme."},
    },
    "tl": [
        ["2013", "Mastercard partnership and UnionPay debit begin"],
        ["Mar 2022", "mPOS with Visa"],
        ["Jun 2024", "PayZen payments with Visa and PITB"],
        ["Aug 2025", "Business debit cards with Mastercard"],
        ["Nov 2025", "PayPak–UnionPay co-badge signed; Visa She's Next"],
        ["Jul 2026", "Co-badge card launched"],
        ["Sep 2026", "UnionPay strategic MoU"],
        ["Sep 2026", "HBL Microfinance to issue the first PayPak credit card"],
    ],
    "l": {
        "U": {"d": 1, "s": "Some debit and business cardholders carry Mastercard.",
              "gap": "Premium and SME debit holders carry Mastercard; credit, Konnect and microfinance customers mostly do not.",
              "neo": "World and business debit holders, some Classic and Gold debit holders.", "snb": "Credit cardholders, Konnect and microfinance customers, PayPak and UnionPay holders."},
        "L5": {"d": 0, "s": "The front doors are HBL's.", "gap": "App, WhatsApp, branches and agents are the bank's own.", "neo": "None.", "snb": "HBL Mobile, WhatsApp, branches, Konnect agents."},
        "L4": {"d": 1, "s": "SME and Prestige banking carry Mastercard debit.", "gap": "Business debit and World debit sit in SME and Prestige; Konnect, microfinance and corporate banking have no Mastercard role.",
               "neo": "SME business debit, Prestige World debit.", "snb": "Konnect Visa QR, PayPak credit at HBL Microfinance, corporate and treasury."},
        "L3": {"d": 1, "s": "Offers and Identity Check on Mastercard cards.", "gap": "Easy Savings and Priceless ride on Mastercard debit; fraud controls and data are HBL's own.",
               "neo": "Easy Savings, Priceless, Identity Check.", "snb": "Visa Offers, HBL controls, data lake, WhatsApp billers."},
        "L2": {"d": 1, "s": "Mastercard shares debit; Visa leads credit.", "gap": "Mastercard is one of four debit networks and owns premium and business debit; Visa holds Platinum and most credit, UnionPay and PayPak grow, Raast carries account payments.",
               "neo": "World and business debit, part of debit and credit, tokens.", "snb": "Visa credit and QR, UnionPay, PayPak, Raast."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, AKFED ownership, Temenos core, strategy."},
    },
    "t": area_lens(LAYERS),
}
