"""National Bank of Egypt's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from nbe_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Egypt's largest bank as five discs that stack into one platform, from an EGP 9.2 trillion balance sheet at the "
       "bottom to Al Ahly Net, more than 700 branches and 7,572 ATMs at the top. Click the stack to open it. Choose who "
       "you are and what you want to do, and the areas that deliver it light up across the layers, joined in the order "
       "they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("aff", "Affluent cardholders", "gem"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates & traders", "factory"),
    ("exp", "Egyptians abroad", "plane"),
    ("unb", "Wallet & first-time users", "users-round"),
]
USERS_DESC = ("Six kinds of customer, about 22 million in all: everyday customers, affluent cardholders, small businesses, "
              "corporates and traders, Egyptians working abroad who send money home, and wallet and first-time users "
              "reached through Phone Cash and Meeza.")

WHO = {"con": "An NBE customer", "aff": "An affluent cardholder", "sme": "A small business", "corp": "A corporate treasurer",
       "exp": "An Egyptian abroad", "unb": "A Phone Cash user"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a Meeza or Visa debit card, the app, InstaPay and Apple Pay.",
     "steps": [("4.1", "retail", "Open an account"), ("2.1", "meezadebit", "Pay with a Meeza debit card"), ("5.1", "ahlynet", "Run it in NBE Mobile"),
               ("2.4", "instapay", "Send money by InstaPay"), ("2.5", "applepay", "Tap with Apple Pay")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "1.9 million credit cards, in parallel Visa and Mastercard ranges, plus the UEFA Champions League co-brand.",
     "steps": [("5.1", "ahlynet", "Apply in the app"), ("2.2", "credit", "Take an NBE credit card"), ("2.2", "uefa", "Or the UCL Mastercard"),
               ("3.2", "offers", "Enter spend draws"), ("3.1", "security", "Get SMS alerts")]},
    {"id": "premium", "who": "aff", "name": "Spend abroad on a top-tier card",
     "why": "World Elite or Infinite in the highest FX band, EgyptAir miles, or a Visa dollar card.",
     "steps": [("2.2", "mcprem", "Carry World or World Elite"), ("2.2", "visaprem", "Or Signature or Infinite"), ("2.2", "egyptair", "Fly on the EgyptAir card"),
               ("2.2", "usdcredit", "Spend dollars on a USD card")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "SME finance, EBRD money, USD debit with Mastercard, card acceptance and the online gateway.",
     "steps": [("4.4", "sme", "Borrow as an SME"), ("2.1", "usddebit", "Pay suppliers abroad on USD debit"),
               ("2.3", "pos", "Take cards in store"), ("2.3", "mpgs", "Sell online through the gateway")]},
    {"id": "corp", "who": "corp", "name": "Finance and pay as a corporate",
     "why": "The country's largest corporate book, corporate cards, trade through Saudi Arabia and beyond.",
     "steps": [("4.3", "corporate", "Borrow from NBE"), ("4.3", "corpcards", "Issue corporate cards"),
               ("2.1", "usddebit", "Pay in dollars"), ("4.6", "ksa", "Bank in Saudi Arabia")]},
    {"id": "remit", "who": "exp", "name": "Send money home",
     "why": "Gulf remittances into InstaPay, the UK subsidiary, and branches abroad.",
     "steps": [("4.6", "nbeuk", "Bank with NBE (UK)"), ("2.6", "remit", "Send a remittance"),
               ("2.4", "instapay", "Receive it by InstaPay"), ("2.5", "phonecash", "Or into Phone Cash")]},
    {"id": "wallet", "who": "unb", "name": "Pay with a wallet",
     "why": "Phone Cash for customers and non-customers, Meeza cards, ATMs and QR.",
     "steps": [("2.5", "phonecash", "Open Phone Cash"), ("5.3", "atms", "Cash in and out at an ATM"),
               ("2.1", "prepaid", "Link a prepaid card"), ("4.5", "momkn", "Pay bills through Momkn")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "A credit range to World Elite, the UCL and EgyptAir co-brands, USD corporate debit and the Mastercard Gateway.",
     "steps": [("2.2", "credit", "Credit beside Visa"), ("2.2", "mcprem", "World and World Elite"), ("2.2", "uefa", "UCL co-brand"),
               ("2.1", "usddebit", "USD corporate debit"), ("2.3", "mpgs", "Mastercard Gateway online")]},
    {"id": "mcnext", "who": "mc", "name": "Where commercial cards, acquiring and remittances could land",
     "why": "Where NBE has scale and Mastercard is thin: the corporate and SME books, the POS estate, Gulf remittances, tokens and fraud scoring on InstaPay.",
     "steps": [("4.3", "corpcards", "Commercial and virtual cards"), ("2.3", "pos", "Acquirer risk and merchant data"),
               ("2.6", "remit", "Inbound remittances on Move"), ("2.5", "applepay", "Tokens across wallets"),
               ("3.1", "security", "Scam and fraud scoring")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across NBE's map",
    "title": "Level with Visa on credit, while Meeza and InstaPay carry Egypt's everyday flows",
    "lead": "NBE is Egypt's largest bank, with 8.4 million debit cards, 1.9 million credit cards and 717 million InstaPay transfers in 2025. Mastercard runs a credit range beside Visa's, from Standard to World Elite. It holds the UEFA Champions League and EgyptAir co-brands, added a USD corporate debit card in July 2026 and powers the online gateway. Meeza, the national scheme, carries the mass debit base; InstaPay carries account transfers; Visa holds debit and a dollar credit card. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are NBE's own as reported in the Egyptian press (2025 results, October 2026), or from Mastercard, Visa, the CBE and press. NBE does not publish its card base by network, and its own site could not be read directly.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Meeza, Visa, Mastercard ⚠", "8.4 million cards; split unknown"],
        ["Credit", "Visa and Mastercard", "1.9 million cards; parallel ranges"],
        ["Premium credit", "World Elite and Infinite", "Same EGP 60,000 FX band"],
        ["Co-brands", "Mastercard", "UEFA Champions League (2024), EgyptAir"],
        ["Corporate USD debit", "Mastercard", "Launched July 2026"],
        ["USD credit", "Visa", "For dollar certificate holders ⚠"],
        ["Online acceptance", "Mastercard Gateway", "nbe.gateway.mastercard.com"],
        ["Instant", "InstaPay", "717 million NBE transfers in 2025"],
    ],
    "sides": {
        "neo": {"dir": "A credit range to World Elite, the UCL and EgyptAir co-brands, Mastercard debit, USD corporate debit, the Mastercard Gateway and acceptance at NBE's POS.",
                "deals": "What it does not do in public view: Meeza debit, InstaPay, Phone Cash, remittances, fraud scoring or commercial credit cards."},
        "snb": {"dir": "Meeza debit and wallets, InstaPay transfers, Visa debit, a Visa credit range to Infinite and the Visa dollar card, Fawry bills.",
                "deals": "Where they meet: credit, where both run full ranges, and the POS estate, which takes every scheme."},
    },
    "tl": [
        ["Mar 2021", "Al Ahly Capital buys 75% of Momken"],
        ["Apr 2022", "CBE launches InstaPay"],
        ["Feb 2024", "UEFA Champions League Mastercard credit card"],
        ["May 2024", "FX limits raised on Visa and Mastercard cards"],
        ["Sep 2024", "Mohamed El-Etreby becomes CEO"],
        ["Dec 2024", "Apple Pay goes live with NBE"],
        ["Oct 2025", "First branch in Saudi Arabia"],
        ["Feb 2026", "UCL trophy tour with Mastercard"],
        ["Jul 2026", "USD corporate debit with Mastercard"],
    ],
    "l": {
        "U": {"d": 1, "s": "Many credit cardholders carry Mastercard.",
              "gap": "Credit and co-brand cardholders and corporate USD debit users carry Mastercard; Meeza debit holders and wallet users do not.",
              "neo": "UCL, EgyptAir, World and World Elite cardholders; some debit holders.", "snb": "Meeza debit holders, Phone Cash users, Visa cardholders, InstaPay users."},
        "L5": {"d": 0, "s": "The front doors are NBE's.", "gap": "App, branches and ATMs are the bank's own.", "neo": "None.", "snb": "Al Ahly Net, NBE Mobile, branches, ATMs."},
        "L4": {"d": 1, "s": "SME and corporate banking now have a Mastercard USD debit card.", "gap": "USD debit sits in SME and corporate; corporate credit cards, Tamkeen, Momkn and the international network have no public Mastercard role.",
               "neo": "USD corporate debit for corporates and SMEs.", "snb": "Corporate lending, Tamkeen, Al Ahly Momkn, NBE (UK)."},
        "L3": {"d": 1, "s": "Co-brand campaigns run on Mastercard.", "gap": "UCL draws and spend campaigns ride on Mastercard; security, data and AI are NBE's own.",
               "neo": "UCL and Titanium campaigns.", "snb": "Visa points and cashback, SMS alerts, tokens, chatbot."},
        "L2": {"d": 1, "s": "Mastercard shares credit and runs the gateway; Meeza and InstaPay lead.", "gap": "Mastercard is level with Visa in credit, owns both co-brands, USD corporate debit and the online gateway; Meeza holds mass debit and InstaPay the transfers.",
               "neo": "Credit range, co-brands, USD debit, Mastercard Gateway.", "snb": "Meeza debit, Visa debit and USD credit, InstaPay, Phone Cash."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "State ownership, capital, leadership, strategy."},
    },
    "t": area_lens(LAYERS),
}
