"""Erste's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from erste_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Austria's savings-bank group as five discs that stack into one platform, from 23.2 million customers in eight "
       "markets and €283 billion of loans at the bottom to George, branches and George Business at the top. Click the "
       "stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the "
       "layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("inv", "Savers & investors", "coins"),
    ("home", "Homebuyers", "house"),
    ("trav", "Frequent flyers", "plane"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Six kinds of customer, 4.4 million of them in Austria and 23.2 million across the group: everyday customers, "
              "savers and investors, homebuyers, frequent flyers, small businesses and corporates.")

WHO = {"con": "An Erste customer", "inv": "A saver", "home": "A homebuyer", "trav": "A frequent flyer",
       "sme": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "An account, a Debit Mastercard, George and card security.",
     "steps": [("4.1", "accounts", "Open an account in George"), ("2.1", "debit", "Pay with Debit Mastercard"),
               ("5.1", "george", "Run it in George"), ("3.1", "idcheck", "Approve online payments"), ("3.1", "geo", "Protected by Geo-Control")]},
    {"id": "card", "who": "con", "name": "Pay by credit card",
     "why": "A Smartcard on Mastercard or Visa, instalments, cashback and a phone wallet.",
     "steps": [("2.2", "credit", "Choose a Smartcard"), ("2.4", "wallets", "Add it to Apple Pay or Google Pay"),
               ("3.4", "moneyback", "Collect Moneyback cashback")]},
    {"id": "fly", "who": "trav", "name": "Earn miles",
     "why": "The Austrian Miles & More card, issued by Erste since early 2026.",
     "steps": [("2.3", "miles", "Take a Miles & More Mastercard"), ("5.1", "george", "Get it instantly in George"),
               ("2.4", "wallets", "Pay by phone abroad")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "Home loans and building-society savings through Erste Bank and the Sparkassen.",
     "steps": [("5.2", "branches", "See an adviser"), ("4.1", "housing", "Take a home loan")]},
    {"id": "invest", "who": "inv", "name": "Save and invest",
     "why": "George Invest, savings plans and Move & Save.",
     "steps": [("5.1", "george", "Open a depot in George"), ("4.2", "invest", "Start a savings plan"),
               ("3.4", "movesave", "Save as you move")]},
    {"id": "health", "who": "con", "name": "Get finances in shape",
     "why": "George FIT for budgets, the Zweite Sparkasse for people in difficulty.",
     "steps": [("3.4", "georgefit", "Use George FIT"), ("3.4", "zweite", "Restart with the Zweite Sparkasse")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "George Business, business and virtual cards, expense software and card acceptance.",
     "steps": [("5.3", "gbiz", "Bank in George Business"), ("4.3", "bizcards", "Give staff business cards"),
               ("4.3", "virtual", "Issue virtual cards"), ("4.3", "yokoy", "Automate expenses"), ("2.5", "accept", "Take cards with Global Payments")]},
    {"id": "corp", "who": "corp", "name": "Bank across Central Europe",
     "why": "Corporates & Markets, Poland and the Santander alliance.",
     "steps": [("4.4", "corp", "Borrow and raise capital"), ("4.5", "ebp", "Bank in Poland"), ("4.6", "ceebanks", "Use the CEE network")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Every Austrian debit card, the Miles & More co-brand, half of the credit range and Identity Check.",
     "steps": [("2.1", "debit", "Debit Mastercard on every account"), ("2.3", "miles", "Miles & More on Mastercard"),
               ("2.2", "credit", "Smartcard and Premiumcard Mastercard"), ("3.1", "idcheck", "Identity Check online")]},
    {"id": "mcnext", "who": "mc", "name": "Where Wero, virtual cards and AI could land",
     "why": "Where Erste has needs and Mastercard is not yet in: living alongside Wero, virtual commercial cards, card-linked offers, agentic payments for Hey George and Erste Bank Polska's cards.",
     "steps": [("2.6", "wero", "Open banking and Move alongside Wero"), ("4.3", "virtual", "Virtual cards with spend controls"),
               ("3.4", "moneyback", "Card-linked offers"), ("3.3", "heygeorge", "Agent Pay for Hey George"), ("4.5", "ebp", "Erste Bank Polska's card book")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Erste's map",
    "title": "Mastercard debit in every Austrian wallet, and Wero at the door",
    "lead": "Erste Bank and the Sparkassen moved their debit cards from Maestro to Debit Mastercard in 2019–20, and in 2025 won the Austrian Miles & More cards, which stayed on Mastercard. Credit is split: every Smartcard and Premiumcard comes on Mastercard or Visa, and Visa has the GÖD union cards and the Business Smartcard. In June 2026 Erste Bank Oesterreich became a shareholder in Wero. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (H1 2026 report, 30 July 2026) or from Erste Bank's product pages, read 17 October 2026, and press. Card counts by network are not published; networks for Erste Bank Polska and the other CEE banks were not researched.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Mastercard", "Since April 2019; all Austrian accounts"],
        ["Credit", "Mastercard and Visa", "Customer's choice; split not public"],
        ["Miles & More", "Mastercard", "Erste issuer from early 2026"],
        ["Union cards", "Visa", "GÖD Smartcard and Premiumcard"],
        ["Business credit", "Visa", "Business Smartcard; others ⚠"],
        ["Online security", "Identity Check", "All debit cards"],
        ["Acceptance", "Global Payments", "Joint venture since 2016"],
        ["Account-to-account", "Wero", "EPI shareholder, June 2026"],
    ],
    "sides": {
        "neo": {"dir": "Debit for every Austrian account, the Miles & More co-brand, the Mastercard half of credit, and Identity Check.",
                "deals": "What it does not do: the Visa half of credit, business Visa cards, Wero, rewards, AI or Poland's cards as far as public sources show."},
        "snb": {"dir": "Visa credit and business cards, Wero for account-to-account payments, Global Payments for acceptance, Dateio for cashback and OpenAI for Hey George.",
                "deals": "Where they meet: every credit card sale, where the customer picks the network."},
    },
    "tl": [
        ["2016", "Global Payments acquiring joint venture"],
        ["Apr 2019", "Debit Mastercard replaces Maestro"],
        ["Mid-2020", "Maestro retired at Erste Bank and Sparkassen"],
        ["Aug 2025", "Erste wins Miles & More cards; Mastercard stays"],
        ["Jan 2026", "Santander Bank Polska stake completed"],
        ["Early 2026", "Miles & More Mastercard issued by Erste"],
        ["Apr 2026", "Erste Bank Polska brand"],
        ["Jun 2026", "Erste Bank Oesterreich joins Wero's owner"],
    ],
    "l": {
        "U": {"d": 1, "s": "Every Austrian debit holder carries Mastercard; credit holders split.",
              "gap": "Debit and Miles & More customers carry Mastercard; credit customers choose; GÖD and business Smartcard holders carry Visa.",
              "neo": "Debit holders, frequent flyers, Mastercard credit holders.", "snb": "Visa credit holders, GÖD members, Business Smartcard users, Polish customers ⚠."},
        "L5": {"d": 0, "s": "The front doors are Erste's.", "gap": "George, branches and George Business are the group's own.", "neo": "None.", "snb": "George, branches, George Business."},
        "L4": {"d": 0, "s": "Accounts carry Debit Mastercard; business cards lean to Visa.", "gap": "Accounts come with Debit Mastercard; the Business Smartcard is Visa; virtual cards' network is not stated.",
               "neo": "Debit on accounts.", "snb": "Business Smartcard, home loans, investing, Poland and CEE."},
        "L3": {"d": 1, "s": "Identity Check is Mastercard's; the rest is Erste's or partners'.", "gap": "Identity Check secures debit online; Geo-Control, George ID, Moneyback and Hey George are not Mastercard's.",
               "neo": "Identity Check.", "snb": "Geo-Control, George ID, Dateio cashback, OpenAI."},
        "L2": {"d": 1, "s": "Debit and Miles & More on Mastercard; credit split; Wero coming.", "gap": "Mastercard holds debit and the co-brand; Visa shares credit; Wero is the account-to-account challenger.",
               "neo": "Debit, Miles & More, Mastercard credit.", "snb": "Visa credit, GÖD Visa, Wero, Global Payments."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, foundation, Sparkassen, George, strategy."},
    },
    "t": area_lens(LAYERS),
}
