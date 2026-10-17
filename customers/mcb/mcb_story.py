"""MCB Group's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from mcb_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Mauritius' largest bank as five discs that stack into one platform, from Rs 1.28 trillion of assets and a "
       "history back to 1838 at the bottom to MCB Juice, 63 branches and five African hubs at the top. Click the stack to "
       "open it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("aff", "Affluent & private clients", "gem"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Mauritian corporates", "factory"),
    ("afr", "African corporates & traders", "earth"),
    ("isl", "Island customers abroad", "globe"),
]
USERS_DESC = ("Six kinds of customer, about 1.29 million in all: everyday Mauritians, affluent and private clients, "
              "small businesses, Mauritian corporates, the African corporates and commodity traders that earn over half "
              "of group income, and customers of MCB's banks in Madagascar, Seychelles and Maldives.")

WHO = {"con": "An MCB customer", "aff": "A private client", "sme": "A small business", "corp": "A corporate treasurer",
       "afr": "An African corporate", "isl": "A customer in Seychelles or Madagascar"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank and pay day to day",
     "why": "The everyday loop: an account, a Mastercard debit card, Juice, QR and taps from the phone.",
     "steps": [("3.1", "onboard", "Open an account online"), ("4.1", "retail", "Hold a current account"), ("2.1", "debit", "Pay with Mastercard debit"),
               ("5.1", "juice", "Run it in Juice"), ("2.6", "maucasqr", "Scan a MauCAS QR code"), ("2.7", "juicetap", "Tap with Juice Tap")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "Classic on Mastercard or Visa, Primo on Mastercard, Apple Pay and MCB's own offers.",
     "steps": [("2.2", "credit", "Choose Mastercard or Visa"), ("2.2", "primo", "Or start with Primo"), ("2.7", "applepay", "Add it to Apple Pay"),
               ("3.3", "offers", "Use Sweet deals")]},
    {"id": "send", "who": "con", "name": "Send money",
     "why": "Instant transfers on the central bank's switch, and international transfers.",
     "steps": [("5.1", "juice", "Open Juice"), ("2.6", "transfers", "Send to a mobile number or account"), ("2.6", "remit", "Send abroad")]},
    {"id": "premium", "who": "aff", "name": "Bank as a private client",
     "why": "Visa Signature or Amex, and private wealth management.",
     "steps": [("2.2", "premium", "Carry Visa Signature"), ("2.2", "amex", "Or Amex Gold"), ("4.6", "wealth", "Invest with Private Wealth")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "SME banking, Visa business debit, JuicePro and acceptance for every network and QR.",
     "steps": [("4.2", "sme", "Get an express overdraft"), ("2.4", "smedebit", "Pay with Visa business debit"), ("5.2", "juicepro", "Run it in JuicePro"),
               ("2.5", "pos", "Take cards on an Android POS"), ("2.6", "maucasqr", "Take MauCAS QR"), ("3.2", "peach", "Take Juice online")]},
    {"id": "corp", "who": "corp", "name": "Run a Mauritian corporate",
     "why": "Lending, connectivity and a Mastercard card in four currencies.",
     "steps": [("4.3", "corporate", "Borrow and go green"), ("3.2", "h2h", "Connect host-to-host"), ("2.4", "corpcard", "Spend on a Mastercard FCY card"),
               ("2.4", "fleetman", "Fuel the fleet with Fleetman")]},
    {"id": "africa", "who": "afr", "name": "Trade across Africa",
     "why": "Commodity and structured finance, the USD 1 billion envelope and digital trade documents.",
     "steps": [("5.3", "hubs", "Meet a hub"), ("4.4", "cib", "Finance a commodity flow"), ("4.4", "trade1b", "Use an electronic Bill of Exchange"),
               ("3.2", "h2h", "Settle over SWIFT")]},
    {"id": "islands", "who": "isl", "name": "Bank in Seychelles or Madagascar",
     "why": "Visa cards, Juice and cashback in the overseas banks.",
     "steps": [("4.5", "seychelles", "Bank with MCB Seychelles"), ("4.5", "madagascar", "Or MCB Madagascar"), ("5.1", "juice", "Use Juice"),
               ("3.3", "offers", "Earn Visa cashback")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Mass-market debit, Primo and half the Classic credit cards, the corporate FCY card, Cash Passport ⚠, and tokens in Juice Tap and Apple Pay.",
     "steps": [("2.1", "debit", "Mastercard debit for the mass market"), ("2.2", "primo", "Primo and Classic credit"), ("2.4", "corpcard", "Corporate FCY card"),
               ("2.3", "cashpassport", "Cash Passport prepaid ⚠"), ("2.7", "applepay", "Mastercard tokens in Apple Pay")]},
    {"id": "mcnext", "who": "mc", "name": "Where tokens, trade and the islands could land",
     "why": "Where MCB has needs and Mastercard is thin: token growth past 1.4% of transactions, fraud for foreign e-commerce, a premium tier, cross-border payouts, commercial cards for the Africa push, and Visa-only overseas banks.",
     "steps": [("2.7", "juicetap", "Grow tokens in Juice Tap"), ("3.1", "security", "Fraud and identity for foreign e-commerce"),
               ("2.2", "premium", "A World Elite tier"), ("2.6", "remit", "Cross-border payouts"),
               ("4.4", "cib", "Commercial cards for African trade"), ("4.5", "seychelles", "Cards in the Visa-only islands")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across MCB Group's map",
    "title": "Mastercard in every Mauritian wallet, Visa on the premium and digital front",
    "lead": "Mastercard has carried MCB's mass-market debit card since at least 2015 and made it the first contactless card in Mauritius in 2016. It also runs the Primo card, half the Classic credit cards and a foreign-currency corporate card. Visa holds the premium tier, SME debit, prepaid and every overseas bank, and launched Juice Tap and Apple Pay first. The fastest growth is on MauCAS QR, a domestic rail. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (FY26 results, 28 September 2026; 2025 annual report) or from MCB's product pages, Visa, Mastercard and the Mauritian press. MCB publishes no card counts by network; network shares are inferred from product pages.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Mastercard", "Contactless since 2016; about 675,000 cards then"],
        ["Credit", "Mastercard and Visa", "Classic either; Primo Mastercard; premium Visa"],
        ["Corporate", "Mastercard", "FCY card in four currencies, FY 2024/25"],
        ["SME debit", "Visa", "21,000+ cards by June 2025"],
        ["Wallets", "Visa first", "Juice Tap Dec 2024; Apple Pay May 2026"],
        ["QR", "MauCAS", "QR payments up 67% in 2025"],
        ["Overseas", "Visa", "Seychelles, Madagascar; Maldives exits cards"],
        ["Acquiring", "All networks", "About 18,000 merchants"],
    ],
    "sides": {
        "neo": {"dir": "Mass-market debit, Primo and half the Classic credit cards, the corporate FCY card, Cash Passport ⚠, tokens in Juice Tap and Apple Pay, and acceptance at MCB's merchants.",
                "deals": "What it does not do: premium cards, SME debit, prepaid, the overseas banks, QR, transfers or offers."},
        "snb": {"dir": "Visa premium, SME debit, prepaid and island cards and the first wallet launches; Amex and UnionPay niches; MauCAS QR and instant transfers inside Juice.",
                "deals": "Where they meet: the Classic credit card, Juice Tap and Apple Pay, and MCB's acquiring."},
    },
    "tl": [
        ["Nov 2015", "Online payments on Mastercard debit"],
        ["Sep 2016", "675,000 Mastercard debit cards go contactless"],
        ["Aug 2019", "Central bank launches MauCAS instant payments"],
        ["Jun 2022", "Cash Passport prepaid with Mastercard ⚠"],
        ["Dec 2024", "Juice Tap launches with Visa"],
        ["FY 2024/25", "Mastercard corporate FCY card"],
        ["Jan 2026", "QR payments up 67% in 2025"],
        ["May 2026", "Apple Pay on Visa and Mastercard"],
        ["Sep 2026", "MCB Maldives ends card services"],
    ],
    "l": {
        "U": {"d": 1, "s": "Most Mauritian customers carry a Mastercard debit card.",
              "gap": "Everyday customers and corporates carry Mastercard; private clients, SMEs and island customers carry Visa or Amex.",
              "neo": "Everyday debit holders, Primo and Classic holders, corporates.", "snb": "Private clients, SMEs, Seychelles and Madagascar customers, African corporates."},
        "L5": {"d": 1, "s": "Juice holds Mastercard tokens; the rest is MCB's.", "gap": "Juice carries Mastercard and Visa cards; JuicePro, branches and hubs are MCB's own.",
               "neo": "Mastercard cards in Juice.", "snb": "JuicePro, branches, hubs, QR in Juice."},
        "L4": {"d": 0, "s": "Accounts come with Mastercard debit; the lines themselves are MCB's.", "gap": "Retail accounts and corporate cards touch Mastercard; African CIB, wealth and the island banks do not.",
               "neo": "Retail accounts, corporate cards.", "snb": "SME banking, African CIB, overseas banks, wealth."},
        "L3": {"d": 0, "s": "Security, offers and connectivity are MCB's own.", "gap": "3-D Secure runs on the networks; no Mastercard fraud, data or offers service found.",
               "neo": "Card 3-D Secure ⚠.", "snb": "Selfie checks, Sweet deals, Peach checkout, SWIFT."},
        "L2": {"d": 1, "s": "Mastercard debit and corporate; Visa premium and wallets; QR domestic.", "gap": "Mastercard holds debit and corporate credit; Visa holds premium, SME, prepaid and the islands; MauCAS holds QR and transfers.",
               "neo": "Debit, Primo, Classic, corporate FCY, Cash Passport ⚠, tokens.", "snb": "Visa premium and SME, Amex, UnionPay, MauCAS QR and transfers."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, heritage, technology, Vision 2030."},
    },
    "t": area_lens(LAYERS),
}
