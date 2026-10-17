"""Standard Bank Group's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from standardbank_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Africa's largest bank as five discs that stack into one platform, from R3.8 trillion of assets and 19.5 million "
       "active clients at the bottom to the banking app, branches and agents at the top. Click the stack to open it. Choose "
       "who you are and what you want to do, and the areas that deliver it light up across the layers, joined in the order "
       "they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday South Africans", "user-round"),
    ("priv", "Private & wealth clients", "gem"),
    ("glob", "Global South Africans", "earth"),
    ("cash", "Cash & unbanked users", "hand-coins"),
    ("sme", "Small & commercial businesses", "briefcase"),
    ("corp", "Corporates & institutions", "factory"),
    ("afr", "Clients across Africa", "globe"),
]
USERS_DESC = ("Seven kinds of client, 19.5 million active in all: about 12 million everyday South Africans, private and "
              "wealth clients, South Africans who bank across borders, people paid in cash through Instant Money, half a "
              "million South African businesses, the corporates CIB serves, and 4.4 million personal clients across Africa Regions.")

WHO = {"con": "A Standard Bank customer", "priv": "A Private Banking client", "glob": "A global South African", "cash": "An Instant Money user",
       "sme": "A small business", "corp": "A corporate treasurer", "afr": "A Stanbic customer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: a MyMo account, a Mastercard debit card, the phone, UCount and fraud checks.",
     "steps": [("4.1", "accounts", "Open a MyMo account"), ("2.2", "debit", "Pay with a Mastercard debit card"), ("2.5", "tokens", "Tap with a phone"),
               ("3.3", "ucount", "Earn UCount points"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "Blue to Platinum credit cards, all on Mastercard, with a virtual card for online shopping.",
     "steps": [("2.1", "credit", "Take a credit card"), ("2.5", "virtualcard", "Shop online with a virtual card"), ("3.3", "ucount", "Collect UCount Rewards")]},
    {"id": "send", "who": "cash", "name": "Send and spend without a bank account",
     "why": "Instant Money, PayShap and prepaid services for people who live mostly in cash.",
     "steps": [("5.3", "partners", "Collect cash at a retailer"), ("2.6", "instantmoney", "Receive Instant Money"), ("2.6", "payshap", "Pay by PayShap"),
               ("3.3", "vas", "Buy airtime and electricity")]},
    {"id": "private", "who": "priv", "name": "Bank privately",
     "why": "A Visa Private Banking card, a World Mastercard for travel, Diners Club, and Liberty for wealth.",
     "steps": [("2.2", "privdebit", "Bank with a Private Banking card"), ("2.1", "worldcitizen", "Travel on World Citizen"), ("2.1", "diners", "Add Diners Club"),
               ("4.5", "liberty", "Invest and insure with Liberty")]},
    {"id": "global", "who": "glob", "name": "Live and spend across borders",
     "why": "Shyft for foreign currency and an offshore account.",
     "steps": [("2.7", "shyft", "Buy dollars in Shyft"), ("2.7", "shyft", "Spend on a Shyft card"), ("4.5", "offshore", "Open an offshore account")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A business account, card acceptance, SimplyBlu online, SnapScan QR and business cards.",
     "steps": [("4.3", "bcb", "Open a business account in 15 minutes"), ("2.4", "acquiring", "Take cards in store"), ("2.4", "simplyblu", "Sell online with SimplyBlu"),
               ("2.4", "snapscan", "Take SnapScan QR"), ("2.3", "corpcards", "Give staff business cards")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "CIB's transaction banking, cross-border rails, APIs and digital assets.",
     "steps": [("4.4", "cib", "Bank with CIB"), ("3.4", "apis", "Connect by OneHub APIs"), ("2.7", "crossborder", "Pay across borders and to China"),
               ("2.8", "digitalassets", "Settle on blockchain rails")]},
    {"id": "africa", "who": "afr", "name": "Bank with Stanbic across Africa",
     "why": "The same app and mobile money across 20 other African countries.",
     "steps": [("5.2", "branches", "Visit a Stanbic branch"), ("5.1", "app", "Bank on the app"), ("2.6", "flexipay", "Pay by FlexiPay")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The South African retail card book, World Citizen, in-app tap-to-pay, Masterpass and SimplyBlu's gateway.",
     "steps": [("2.1", "credit", "Credit cards on Mastercard"), ("2.2", "debit", "MyMo and Achieva debit on Mastercard"), ("2.1", "worldcitizen", "World Citizen"),
               ("2.5", "tokens", "In-app tap for Mastercard cards"), ("2.4", "simplyblu", "SimplyBlu on Mastercard Gateway")]},
    {"id": "mcnext", "who": "mc", "name": "Where fraud tools, agents and remittances could land",
     "why": "Where Standard Bank has needs and Mastercard is not yet in: card fraud up 18%, agentic e-commerce, a growing acquiring book, remittances and intra-network settlement, and UCount offers.",
     "steps": [("3.1", "fraud", "Fraud and identity scoring"), ("3.2", "personalisation", "Agent Pay for agentic e-commerce"), ("2.4", "acquiring", "Acquirer risk and Click to Pay"),
               ("2.7", "crossborder", "Remittances and Blue-to-Blue on Mastercard Move"), ("3.3", "ucount", "Card-linked offers")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Standard Bank Group's map",
    "title": "Mastercard's retail card book, on a bank building its own rails",
    "lead": "Standard Bank's South African personal credit cards and mass-market debit cards carry Mastercard, and World Citizen is a World Mastercard. Visa holds Private Banking, offshore and fleet cards and the FX rails behind Shyft; UnionPay has the recent partnership news; Diners Club is the bank's own. Meanwhile the bank is pushing low-value payments onto PayShap and building Instant Money, mobile money and stablecoin rails. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (2026 interim results, 13 August 2026; Capital Markets Day, 26 March 2026). Card networks are read from card art on Standard Bank's product pages on 17 October 2026; Africa Regions card networks were not checked, and no Mastercard deal after 2013 is public.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Personal credit", "Mastercard", "Blue to World Citizen; R33bn book"],
        ["Mass-market debit", "Mastercard", "MyMo, Achieva ⚠ card art"],
        ["Private & offshore", "Visa", "Private, Professional, Offshore"],
        ["Commercial cards", "Mastercard or Visa", "Fleet on Visa"],
        ["Own scheme", "Diners Club", "Wholly owned in SA"],
        ["Real-time", "PayShap", "Low-value payments auto-routed, 2026"],
        ["Cross-border FX", "Visa (Currencycloud)", "Behind Shyft"],
        ["New partner", "UnionPay", "Renewed Apr 2025; nine markets Aug 2026"],
    ],
    "sides": {
        "neo": {"dir": "Personal credit and mass-market debit in South Africa, World Citizen, in-app tap-to-pay, Masterpass, SimplyBlu's gateway and half the commercial cards.",
                "deals": "What it does not do: Private Banking and offshore cards, fleet, Shyft's FX, PayShap, Instant Money, mobile money or stablecoins."},
        "snb": {"dir": "Visa for private, offshore, fleet and Shyft's FX; Diners Club; UnionPay acceptance; PayShap and PayInc; the bank's own Instant Money, FlexiPay and ZARU.",
                "deals": "Where they meet: acquiring, which takes every network, and the corporate cards clients choose between."},
    },
    "tl": [
        ["Aug 2013", "Five-year Mastercard agreement across Africa"],
        ["Aug 2018", "Masterpass; Samsung Pay for Mastercard cards"],
        ["Jun 2019", "SimplyBlu on Mastercard Gateway"],
        ["Oct 2020", "Standard Bank, Mastercard and Google for SMEs"],
        ["Mar 2023", "PayShap launches"],
        ["2023", "Visa case study: Shyft on Visa Cross-Border"],
        ["Apr 2025", "UnionPay partnership renewed"],
        ["Mar 2026", "Capital Markets Day: payments, AI, ZARU"],
        ["Aug 2026", "Low-value payments routed to PayShap; card interoperability moves to the SARB"],
    ],
    "l": {
        "U": {"d": 1, "s": "Most everyday cardholders carry Mastercard.", "gap": "Mass-market and credit cardholders carry Mastercard; private and offshore clients carry Visa; the unbanked use Instant Money.",
              "neo": "Everyday and credit cardholders.", "snb": "Private and offshore clients, Instant Money and mobile-money users, corporates."},
        "L5": {"d": 1, "s": "The app's tap-to-pay is Mastercard-only.", "gap": "Branches, ATMs and agents are the bank's; in-app tap works only for Mastercard cards.", "neo": "In-app tap-to-pay.", "snb": "Branches, ATMs, retailers, advisers."},
        "L4": {"d": 1, "s": "Accounts come with Mastercard or Visa cards.", "gap": "Mass-market accounts carry Mastercard, Private and Offshore Visa; lending, CIB and Liberty have no network role.",
               "neo": "Mass-market and business accounts.", "snb": "Private, Offshore, mortgages, CIB, Liberty."},
        "L3": {"d": 1, "s": "UCount runs mostly on Mastercard cards; the rest is the bank's own.", "gap": "Fraud, AI, APIs and value-added services are the bank's; no Mastercard service is public.",
               "neo": "UCount spend on cards.", "snb": "Fraud models, AI, APIs, value-added services."},
        "L2": {"d": 1, "s": "Retail cards on Mastercard; new rails are not.", "gap": "Mastercard holds personal credit and mass-market debit; Visa, Diners, UnionPay, PayShap and the bank's own rails hold the rest.",
               "neo": "Credit, debit, Masterpass, SimplyBlu.", "snb": "Visa private and fleet, Diners Club, PayShap, Instant Money, Shyft's FX, stablecoins."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's; card modernisation is the opening.", "neo": "None.", "snb": "Capital, ICBC, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
