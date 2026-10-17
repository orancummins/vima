"""DNB's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from dnb_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Norway's largest bank as five discs that stack into one platform, from NOK 2.3 trillion of loans and a 34% state "
       "shareholder at the bottom to the mobile bank, Sbanken and 52 branches at the top. Click the stack to open it. Choose "
       "who you are and what you want to do, and the areas that deliver it light up across the layers, joined in the order "
       "they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("home", "Homebuyers", "house"),
    ("aff", "Savers & private banking", "coins"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Large corporates", "factory"),
    ("inv", "Issuers & investors", "chart-candlestick"),
]
USERS_DESC = ("Six kinds of customer: 2.4 million personal customers, homebuyers, savers and Private Banking clients, about "
              "244,000 companies, the large corporates and shipping and energy clients LCI serves, and the issuers and "
              "investors DNB Carnegie works for.")

WHO = {"con": "A DNB customer", "home": "A homebuyer", "aff": "A saver", "sme": "A small business",
       "corp": "A corporate treasurer", "inv": "An issuer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: a package, a BankAxept and Visa card, the app, Aino and fraud checks.",
     "steps": [("4.1", "packages", "Open a Pluss package"), ("2.1", "debit", "Pay with BankAxept and Visa"), ("5.1", "app", "Run it in the mobile bank"),
               ("3.2", "aino", "Ask Aino"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "DNB's credit cards are all Mastercard, with fuel discounts and Priceless tickets.",
     "steps": [("2.2", "mccredit", "Take a DNB Mastercard"), ("3.4", "circlek", "Save on fuel and charging"), ("3.4", "priceless", "Buy concert tickets early")]},
    {"id": "wallet", "who": "con", "name": "Pay with a phone",
     "why": "Apple Pay, Google Pay and Vipps MobilePay, part-owned by DNB.",
     "steps": [("2.4", "wallets", "Add cards to Apple Pay or Google Pay"), ("2.4", "vipps", "Pay friends and shops with Vipps"),
               ("2.5", "instant", "Money arrives instantly")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "A quarter of Norway's mortgages and the group's own estate agents.",
     "steps": [("5.4", "branches", "Meet an adviser"), ("4.2", "mortgages", "Take a mortgage"), ("4.2", "eiendom", "Sell with DNB Eiendom")]},
    {"id": "save", "who": "aff", "name": "Save and invest",
     "why": "The Spare app, Norway's biggest fund house, pensions and Private Banking.",
     "steps": [("5.1", "spare", "Start a fund saving in Spare"), ("4.3", "wealth", "Invest in DNB funds"), ("4.3", "pension", "Build a pension"),
               ("2.2", "pbcard", "Carry a World Elite Mastercard")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A business account, Visa Business debit, a Corporate Mastercard and B2B checkout credit.",
     "steps": [("4.4", "sme", "Open a business account"), ("2.3", "visabiz", "Pay with Visa Business"),
               ("2.3", "corpmc", "Give staff a Corporate Mastercard"), ("2.6", "two", "Sell on invoice terms with Two")]},
    {"id": "corp", "who": "corp", "name": "Bank a large company",
     "why": "LCI lending, currency, leasing and instant settlement.",
     "steps": [("4.5", "lci", "Borrow from LCI"), ("2.6", "fx", "Trade currency"), ("4.5", "finans", "Lease assets with DNB Finans"),
               ("2.5", "instant", "Pay in real time")]},
    {"id": "raise", "who": "inv", "name": "Raise capital",
     "why": "DNB Carnegie, the Nordic investment bank built from DNB Markets and Carnegie.",
     "steps": [("4.6", "carnegie", "List or issue with DNB Carnegie"), ("4.3", "wealth", "Reach DNB's fund investors")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The whole consumer credit range, World Elite for Private Banking, Priceless, the SEB Kort corporate card and NICS clearing.",
     "steps": [("2.2", "mccredit", "Consumer credit on Mastercard"), ("2.2", "pbcard", "World Elite for Private Banking"),
               ("3.4", "priceless", "Priceless presales"), ("2.3", "corpmc", "Corporate Mastercard via SEB Kort"),
               ("2.5", "instant", "NICS clearing for Bits")]},
    {"id": "mcnext", "who": "mc", "name": "Where scam scores, agents and commercial cards could land",
     "why": "Where DNB has needs and Mastercard is not yet in: scams up 30% a year, agentic AI, large-corporate cards, offers for its programmes, open banking and, one day, debit.",
     "steps": [("3.1", "fraud", "Scam and fraud scoring"), ("1.4", "agentic", "Agent Pay alongside DNB's AI agents"),
               ("4.5", "lci", "Commercial and virtual cards for large corporates"), ("3.4", "programmes", "Card-linked offers"),
               ("3.3", "apis", "Open finance"), ("2.1", "debit", "Debit, if ever re-tendered")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across DNB's map",
    "title": "Mastercard on credit, Visa and BankAxept on debit",
    "lead": "Every DNB consumer credit card is a Mastercard, up to World Elite for Private Banking, and DNB pays its own fuel and charging discounts on them. Debit, for 2.4 million personal customers and for businesses, is BankAxept and Visa, and the wallet that matters most in Norway, Vipps MobilePay, is part-owned by DNB. The Corporate Mastercard is issued by SEB Kort, and Mastercard clears Norway's interbank payments for Bits. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are DNB's own (Q2 2026 report, 14 July 2026; 2025 annual report) or from Norges Bank and partners. No DNB network agreement with Mastercard or Visa is public; networks are read from DNB's card pages and terms.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "BankAxept + Visa", "Every personal package"],
        ["Business debit", "Visa Business", "Visa-only since October 2022"],
        ["Consumer credit", "Mastercard", "DNB, Pluss, Ung and SAGA"],
        ["Private Banking", "World Elite Mastercard", "Priceless and Fast Track"],
        ["Corporate cards", "Mastercard via SEB Kort", "Firms up to 250 staff"],
        ["Wallets", "Vipps MobilePay", "DNB owns 47.3% of Vipps Holding"],
        ["Clearing", "Mastercard for Bits", "NICS renewed May 2025"],
        ["Fraud", "NOK 3.3bn attempted in 2025", "Vendors not public ⚠"],
    ],
    "sides": {
        "neo": {"dir": "All consumer credit cards, World Elite for Private Banking, Priceless presales, the SEB Kort corporate card, and NICS clearing.",
                "deals": "What it does not do: debit, Vipps, fraud tools, AI, open banking or B2B checkout credit."},
        "snb": {"dir": "BankAxept and Visa debit, Visa Business, Vipps MobilePay, Nets processing, Two for B2B credit, and DNB's own fraud and AI.",
                "deals": "Where they meet: the same customer carries a Visa debit card and a Mastercard credit card in one package."},
    },
    "tl": [
        ["Feb 2019", "Nets framework agreement extended"],
        ["May 2019", "Google Pay, Visa cards first ⚠"],
        ["Apr 2020", "Corporate Mastercard terms via SEB Kort"],
        ["Jul 2020", "Vipps i terminal first for DNB customers"],
        ["Oct 2022", "Visa Business replaces Visa Partner"],
        ["Dec 2024", "Apple Pay for DNB and Sbanken"],
        ["Mar 2025", "DNB Carnegie formed"],
        ["May 2025", "Mastercard renews NICS clearing for Bits"],
        ["Mar 2026", "B2B BNPL with Two"],
        ["Jul 2026", "Luminor stake sale agreed"],
        ["Oct 2026", "Agentic AI and 400 job cuts in Technology"],
        ["Nov 2026", "Capital Markets Day"],
    ],
    "l": {
        "U": {"d": 1, "s": "Credit cardholders carry Mastercard; everyone carries Visa debit.",
              "gap": "The same customer often holds a BankAxept and Visa debit card and a Mastercard credit card.",
              "neo": "Credit cardholders, Private Banking clients, SME card users.", "snb": "Every debit holder, Vipps users, mortgage and pension customers."},
        "L5": {"d": 0, "s": "The front doors are DNB's.", "gap": "Mobile bank, Spare, Sbanken and branches are DNB's own; the Corporate Card app is SEB Kort's.",
               "neo": "None directly.", "snb": "Mobile bank, Spare, Sbanken, branches."},
        "L4": {"d": 1, "s": "Packages bundle Visa debit with Mastercard credit.", "gap": "Accounts and Private Banking carry Mastercard credit; mortgages, funds, pensions and Carnegie have no network role.",
               "neo": "Package credit cards, World Elite.", "snb": "Debit in every package, mortgages, wealth, Carnegie."},
        "L3": {"d": 1, "s": "Priceless and fuel discounts run on Mastercard.", "gap": "Loyalty rides on the Mastercard credit card; fraud, AI and identity are DNB's or BankID's.",
               "neo": "Priceless, Circle K discounts.", "snb": "Fraud prevention, Aino, BankID, open banking."},
        "L2": {"d": 1, "s": "Credit on Mastercard; debit on Visa and BankAxept.", "gap": "Mastercard has consumer and corporate credit and NICS clearing; Visa and BankAxept have debit; Vipps and Two sit outside the card rails.",
               "neo": "Credit cards, Corporate Mastercard, NICS clearing.", "snb": "Debit, Visa Business, Vipps, Nets, Two."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, state stake, brands, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
