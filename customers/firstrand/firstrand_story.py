"""FirstRand's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from firstrand_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("A R546 billion South African banking group as five discs that stack into one platform, from R44.5 billion of "
       "continuing earnings at the bottom to the FNB App, branches and Pick n Pay counters at the top. Click the stack to "
       "open it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("priv", "Private clients", "gem"),
    ("home", "Homebuyers", "house"),
    ("driver", "Drivers & fleets", "target"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates", "factory"),
    ("afr", "Customers in broader Africa", "globe"),
]
USERS_DESC = ("Seven kinds of customer, about 12.8 million active at FNB and 19 million on its platforms: everyday customers, "
              "private clients, homebuyers, drivers and fleets, 1.4 million businesses, RMB's corporates and FNB's customers "
              "in eight other African countries.")

WHO = {"con": "An FNB customer", "priv": "A private client", "home": "A homebuyer", "driver": "A driver",
       "sme": "A small business", "corp": "A corporate treasurer", "afr": "A customer in broader Africa"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, an FNB card, the app, NAVi, eBucks and fraud checks.",
     "steps": [("4.1", "accounts", "Open an FNB account"), ("2.1", "cards", "Pay with an FNB card"), ("5.1", "app", "Run it in the FNB App"),
               ("3.2", "navi", "Ask NAVi"), ("3.3", "ebucks", "Earn eBucks"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "pay", "who": "con", "name": "Send money and pay instantly",
     "why": "PayShap by default, eWallet to any phone, and wallets at the till.",
     "steps": [("2.4", "payshap", "Pay with PayShap"), ("2.5", "ewallet", "Send to an eWallet"), ("2.2", "wallets", "Tap with a phone or watch")]},
    {"id": "abroad", "who": "priv", "name": "Send money abroad",
     "why": "Globba in the FNB and RMB Private Banking apps, on Mastercard Move.",
     "steps": [("5.1", "app", "Open the app"), ("2.6", "globba", "Send with Globba"), ("4.1", "private", "Bank as a private client")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "nav»Home and FNB's R296 billion mortgage book.",
     "steps": [("5.1", "app", "Search on nav»Home"), ("4.2", "homeloans", "Take a home loan"), ("4.4", "insure", "Insure it")]},
    {"id": "drive", "who": "driver", "name": "Finance a car",
     "why": "WesBank through dealers, with fleet cards for businesses.",
     "steps": [("5.3", "advisors", "Visit a dealer"), ("4.5", "wesbank", "Finance with WesBank"), ("2.1", "fleet", "Fuel with a Petro card")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A business account, card acceptance on SpeedPoint or a phone, and PayShap.",
     "steps": [("4.3", "commercial", "Open a business account"), ("2.3", "acquiring", "Take cards on SpeedPoint"),
               ("2.3", "speedee", "Or on a phone with SpeedeeApp"), ("2.4", "payshap", "Get paid by PayShap")]},
    {"id": "corp", "who": "corp", "name": "Bank as a corporate",
     "why": "RMB's corporate and investment bank, now with HSBC's former clients.",
     "steps": [("4.6", "rmb", "Bank with RMB"), ("1.3", "hsbc", "Move over from HSBC")]},
    {"id": "africa", "who": "afr", "name": "Bank with FNB elsewhere in Africa",
     "why": "FNB subsidiaries in eight countries, agencies and Globba corridors.",
     "steps": [("4.7", "africa", "Open an account with FNB"), ("5.2", "branches", "Use an AgencyPlus point"), ("2.6", "globba", "Receive money by Globba")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Globba on Mastercard Move, Scan to Pay on Masterpass and acceptance across FNB's merchants.",
     "steps": [("2.6", "globba", "Globba on Mastercard Move"), ("2.3", "scantopay", "Scan to Pay on Masterpass ⚠"),
               ("2.3", "acquiring", "Mastercard accepted at SpeedPoint")]},
    {"id": "mcnext", "who": "mc", "name": "Where Globba, fraud tools and agents could land",
     "why": "Where FirstRand has needs and Mastercard is not yet in: Globba across Africa, fraud and identity scoring, acquirer services, Agent Pay with NAVi, eBucks offers and commercial cards.",
     "steps": [("4.7", "africa", "Globba corridors across FNB's Africa"), ("3.1", "fraud", "Fraud and identity scoring"),
               ("2.3", "acquiring", "Acquirer risk and data"), ("3.2", "navi", "Agent Pay behind NAVi"),
               ("3.3", "ebucks", "Card-linked offers for eBucks"), ("4.6", "rmb", "Commercial cards for RMB clients")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across FirstRand's map",
    "title": "A Visa bank that sends money abroad on Mastercard",
    "lead": "FNB's relationship with Visa dates from 1966 and was renewed in October 2025; its cards are Visa as far as public sources show, and its first instant payments ran on Visa Direct. Mastercard's way in is Globba, FNB's cross-border transfer service launched on Mastercard Move in November 2025, with the Masterpass QR rail from 2019 and acceptance across FNB's merchants. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (results for the year to 30 June 2026, published 10 September 2026) or from Visa, Mastercard and press. FNB's product pages could not be read, so card networks are inferred from the Visa relationship and marked ⚠.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Cards", "Visa ⚠", "Relationship since 1966; renewed Oct 2025"],
        ["Card transactions", "1.39bn issuing", "Up 7%; scheme charges rising"],
        ["Cross-border", "Globba", "Mastercard Move, Nov 2025"],
        ["QR", "Scan to Pay", "Masterpass, Jan 2019 ⚠"],
        ["Instant", "PayShap default", "Volumes up more than 8x"],
        ["P2P", "Instant Pay", "Visa Direct, 2022"],
        ["Acquiring", "1.16bn transactions", "All networks"],
        ["Sponsorship", "Visa", "FIFA World Cup 2026"],
    ],
    "sides": {
        "neo": {"dir": "Globba on Mastercard Move, the Masterpass QR rail and acceptance at FNB's merchants.",
                "deals": "What it does not do: FNB's cards, wallets' tokens, Instant Pay, PayShap, eBucks or AI."},
        "snb": {"dir": "Visa cards and Visa Direct, PayShap and eWallet on domestic rails, FNB's own fraud, AI and rewards.",
                "deals": "Where they meet: acceptance, and cross-border corridors into the rest of Africa."},
    },
    "tl": [
        ["1966", "FNB's Visa relationship begins"],
        ["Jan 2019", "Scan to Pay on Masterpass"],
        ["2022", "Instant Pay on Visa Direct"],
        ["Mar 2023", "PayShap launches"],
        ["Oct 2025", "Visa partnership renewed"],
        ["Nov 2025", "Globba on Mastercard Move"],
        ["Apr 2026", "UK exit; Johnson FNB CEO"],
        ["Sep 2026", "FY2026: PayShap made default"],
    ],
    "l": {
        "U": {"d": 0, "s": "Customers carry FNB's Visa cards ⚠.",
              "gap": "Cardholders are on Visa as far as public sources show; Globba users send on Mastercard Move.",
              "neo": "Globba senders and recipients.", "snb": "FNB cardholders, eWallet and PayShap users."},
        "L5": {"d": 0, "s": "The front doors are FNB's.", "gap": "App, branches, agencies and dealers are the group's own.", "neo": "None.", "snb": "FNB App, branches, AgencyPlus, Pick n Pay counters."},
        "L4": {"d": 0, "s": "The business lines carry Visa cards ⚠.", "gap": "Accounts come with FNB's Visa cards; lending, insurance, WesBank and RMB have no network role.",
               "neo": "None.", "snb": "Accounts, home loans, WesBank, RMB, FNB Connect."},
        "L3": {"d": None, "s": "Fraud, AI and rewards are FNB's own.", "gap": "No public Mastercard service in fraud, AI or eBucks.",
               "neo": "Nothing public.", "snb": "Virtual cards, NAVi, eBucks, Optasia scoring."},
        "L2": {"d": 1, "s": "Globba and QR on Mastercard; cards on Visa.", "gap": "Visa issues the cards ⚠ and runs Instant Pay; PayShap carries low-value transfers; Mastercard has Globba and acceptance.",
               "neo": "Globba, Scan to Pay, acceptance.", "snb": "Visa cards and Visa Direct, PayShap, eWallet."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, ownership, strategy, Optasia."},
    },
    "t": area_lens(LAYERS),
}
