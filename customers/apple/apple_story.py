"""Apple's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from apple_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Apple read through payments, as five discs that stack into one platform, from $416.2 billion of sales at the "
       "bottom to the Wallet app, Apple's stores and partner banks at the top. Click the stack to open it. Choose who you "
       "are and what you want to do, and the areas that deliver it light up across the layers, joined in the order they "
       "act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "iPhone users", "user-round"),
    ("cardh", "Apple Card holders", "credit-card"),
    ("mer", "Merchants", "store"),
    ("iss", "Banks & issuers", "landmark"),
    ("dev", "Wallet developers", "code-xml"),
]
USERS_DESC = ("Five kinds of user: iPhone and Apple Watch users in 101 countries and regions, Apple Card holders in the US, "
              "merchants taking payments on an iPhone in 59 countries, the banks whose cards sit in Apple Pay, and the "
              "developers building other wallets on the iPhone's NFC chip.")

WHO = {"con": "An iPhone user", "cardh": "An Apple Card holder", "mer": "A merchant", "iss": "A bank",
       "dev": "A wallet developer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "pay", "who": "con", "name": "Pay with my iPhone",
     "why": "The everyday loop: a card in Wallet, a token, Face ID and a tap.",
     "steps": [("5.1", "walletapp", "Add a card to Wallet"), ("3.1", "tokens", "Get a device token"),
               ("3.1", "devauth", "Approve with Face ID"), ("2.1", "applepay", "Tap to pay")]},
    {"id": "checkout", "who": "con", "name": "Check out online and spread the cost",
     "why": "The Apple Pay sheet in apps and browsers, with instalments and rewards from partners.",
     "steps": [("2.1", "applepayweb", "Pay in an app or browser"), ("2.4", "instalments", "Choose instalments"),
               ("2.4", "rewards", "Pay with points")]},
    {"id": "card", "who": "cardh", "name": "Carry Apple Card",
     "why": "Apple Card on Mastercard, its instalments, Family sharing and Savings, moving to Chase.",
     "steps": [("2.2", "applecard", "Get Apple Card"), ("2.2", "acmi", "Buy an iPhone at 0%"), ("2.2", "family", "Share it with family"),
               ("4.3", "savings", "Save the Daily Cash"), ("2.2", "chase", "Move to Chase")]},
    {"id": "cash", "who": "con", "name": "Send money to a friend",
     "why": "Apple Cash in Messages, Tap to Cash and bill splitting.",
     "steps": [("2.3", "applecash", "Hold Apple Cash"), ("2.3", "taptocash", "Tap to send or split a bill")]},
    {"id": "id", "who": "con", "name": "Prove who I am",
     "why": "A passport-based Digital ID, state licences and passes in Wallet.",
     "steps": [("3.2", "digitalid", "Add a Digital ID"), ("3.2", "licences", "Add a driver's licence"), ("3.3", "passes", "Board with a pass")]},
    {"id": "merchant", "who": "mer", "name": "Take payments on an iPhone",
     "why": "Tap to Pay through a PSP, and loyalty with Tap to Share.",
     "steps": [("4.4", "psps", "Sign up with a PSP"), ("2.6", "taptopay", "Accept a tap"), ("3.4", "taptoshare", "Collect loyalty details")]},
    {"id": "issuer", "who": "iss", "name": "Put our cards in Apple Pay",
     "why": "What a bank does to be in the wallet, from India's first issuer to instalments and rewards.",
     "steps": [("4.5", "issuers", "Join Apple Pay"), ("3.1", "tokens", "Tokenise the card"), ("2.5", "india", "Launch in a new market"),
               ("2.4", "instalments", "Offer instalments"), ("2.4", "rewards", "Offer points at checkout")]},
    {"id": "dev", "who": "dev", "name": "Build my own wallet on the iPhone",
     "why": "HCE in the EEA, the NFC & SE Platform elsewhere, and the default-app setting.",
     "steps": [("3.5", "hce", "Use HCE in the EEA"), ("3.5", "nfcse", "Or the NFC & SE Platform"),
               ("5.3", "thirdwallets", "Become the default wallet")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Apple Card and its move to Chase, Apple Pay Later on Mastercard Installments, every Mastercard in Apple Pay, the India launch and Tap to Pay acceptance.",
     "steps": [("2.2", "applecard", "Apple Card on Mastercard"), ("2.2", "chase", "Kept through the move to Chase"),
               ("2.4", "paylater", "Apple Pay Later on Mastercard Installments"), ("3.1", "tokens", "Mastercard tokens in Apple Pay"),
               ("2.5", "india", "One of two networks in India"), ("2.6", "taptopay", "Accepted by Tap to Pay")]},
    {"id": "mcnext", "who": "mc", "name": "Where the Apple Card move, instalments and open NFC could land",
     "why": "Where Apple and its partners have needs and Mastercard is not yet in: the Apple Card conversion, issuer instalments and rewards on the new Apple Pay sheet, loyalty at the tap, credentials for HCE wallets, and more Indian issuers.",
     "steps": [("2.2", "chase", "Tokens, benefits and disputes for the Chase move"), ("2.4", "instalments", "Mastercard Installments on the sheet"),
               ("3.4", "taptoshare", "Loyalty and offers at the tap"), ("3.5", "hce", "Credentials for HCE wallets"),
               ("2.5", "india", "More Indian issuers on Mastercard")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Apple's map",
    "title": "Mastercard owns Apple's card, but Apple owns the wallet",
    "lead": "Mastercard is the network on Apple Card and kept it through the move from Goldman Sachs to Chase, a mostly Visa issuer. It also ran Apple Pay Later, Apple's only in-house loan, through Mastercard Installments. Apple Pay itself carries every network, and its checkout sheet competes with Click to Pay. Visa carries Apple Cash, and Apple controls the wallet, the device checks and the terms on which other wallets reach the NFC chip. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Apple's own (Q3 FY2026 results, 30 July 2026; FY2025 statements) or from Apple's newsroom, product, support and developer pages, JPMorgan Chase, the European Commission and the CFPB. Apple publishes no network split, Apple Pay volumes or users.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Apple Card", "Mastercard", "Since March 2019; $20bn+ of balances"],
        ["Apple Card issuer", "Goldman Sachs to Chase", "About 24 months from January 2026"],
        ["Apple Pay Later", "Mastercard Installments", "March 2023 to June 2024"],
        ["Apple Cash", "Visa", "Green Dot Bank"],
        ["Apple Pay", "Every network", "101 countries and regions"],
        ["Apple Pay India", "Visa and Mastercard", "Axis Bank, 30 September 2026; not RuPay"],
        ["Tap to Pay", "Every network", "59 countries, 100+ PSPs"],
        ["EEA NFC", "Open to HCE wallets", "Ten years from July 2024"],
    ],
    "sides": {
        "neo": {"dir": "Apple Card through the move to Chase, the retired Apple Pay Later, Mastercard tokens for every Mastercard in Apple Pay, the India launch, and acceptance on Tap to Pay.",
                "deals": "What it does not do: Apple Cash, Click to Pay at Apple's checkout, agentic payments, loyalty at the tap, or credentials for the new HCE wallets."},
        "snb": {"dir": "Visa on Apple Cash and alongside Mastercard everywhere else, American Express and Discover in Apple Pay, Affirm's instalments, Green Dot and Goldman Sachs behind Apple's products, and rival wallets, UPI and RuPay outside Apple Pay.",
                "deals": "Where they meet: the Apple Pay sheet, Tap to Pay acceptance, and the third-party wallets now allowed onto the iPhone."},
    },
    "tl": [
        ["Sep 2014", "Apple Pay launches with Mastercard, Visa and Amex"],
        ["Jul 2015", "Apple Pay for UK Mastercard holders"],
        ["Mar 2019", "Apple Card with Goldman Sachs on Mastercard"],
        ["Feb 2022", "Tap to Pay on iPhone announced"],
        ["Mar 2023", "Apple Pay Later on Mastercard Installments"],
        ["Jun 2024", "Apple Pay Later ends"],
        ["Jul 2024", "EU makes NFC commitments binding"],
        ["Oct 2024", "CFPB orders Apple and Goldman to pay $89m+"],
        ["Nov 2025", "Digital ID in Wallet"],
        ["Jan 2026", "Chase to issue Apple Card; Mastercard stays"],
        ["Sep 2026", "John Ternus becomes CEO"],
        ["Sep 2026", "Apple Pay in India with Axis Bank"],
        ["~2028", "Apple Card move to Chase expected"],
    ],
    "l": {
        "U": {"d": 1, "s": "Apple Card holders carry Mastercard; everyone else carries any network.",
              "gap": "Every Apple Card holder is on Mastercard; iPhone users carry cards on every network; Apple Cash users are on Visa; merchants and wallet developers have no Mastercard tie.",
              "neo": "Apple Card holders, Mastercard holders in Apple Pay.", "snb": "Apple Cash users, Visa and other card holders, HCE wallet users."},
        "L5": {"d": 1, "s": "The Wallet holds Mastercard; the doors are Apple's.", "gap": "The Wallet app and Apple's stores carry and accept Mastercard; the third-party wallets now allowed on iPhone have no public Mastercard role.",
               "neo": "Mastercard cards in Wallet, acceptance in stores.", "snb": "Wallet app, stores, partner banks, third-party wallets."},
        "L4": {"d": 1, "s": "The card book is Mastercard; the rest is Apple's.", "gap": "The Apple Card book is on Mastercard; Services and devices are Apple's; acceptance and issuer services carry every network.",
               "neo": "Apple Card book, Mastercard issuers and acceptance.", "snb": "Services, iPhone, Savings, Visa and other issuers."},
        "L3": {"d": 1, "s": "Mastercard tokens sit behind Mastercard cards; identity and NFC are Apple's.", "gap": "Mastercard's tokens serve Mastercard cards; Digital ID, passes, Tap to Share and the opened NFC chip have no Mastercard role.",
               "neo": "Tokens for Mastercard cards.", "snb": "Device checks, Digital ID, passes, Tap to Share, HCE wallets."},
        "L2": {"d": 1, "s": "Apple Card and Pay Later on Mastercard; Apple Cash on Visa.", "gap": "Apple Card rides on Mastercard and Apple Pay Later ran on Mastercard Installments; Apple Pay, Tap to Pay and India carry several networks; Apple Cash is Visa.",
               "neo": "Apple Card, Apple Pay Later, Mastercard in Apple Pay, India, Tap to Pay.", "snb": "Apple Cash on Visa, Affirm, other networks in Apple Pay."},
        "L1": {"d": 0, "s": "Apple's own scale, entities and rules.", "gap": "Nothing in the foundation is Mastercard's; regulators are opening Apple's NFC chip to rival wallets.",
               "neo": "None.", "snb": "Results, leadership, entities, Secure Element, EU and US cases."},
    },
    "t": area_lens(LAYERS),
}
