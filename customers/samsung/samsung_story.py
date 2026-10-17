"""Samsung Wallet's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from samsung_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Samsung Electronics, read through Samsung Wallet, as five discs that stack into one platform, from a group "
       "heading for KRW 195 trillion of quarterly sales and a wallet in 62 markets at the bottom to the Wallet app, "
       "Galaxy Watch and banks' apps at the top. Click the stack to open it. Choose who you are and what you want to "
       "do, and the areas that deliver it light up across the layers, joined in the order they act. Switch to the "
       "Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("gal", "Galaxy users", "user-round"),
    ("kr", "Korean Wallet users", "smartphone"),
    ("trav", "Travellers", "plane"),
    ("iss", "Banks & card issuers", "landmark"),
    ("mer", "Merchants", "store"),
    ("part", "ID, key & crypto partners", "plug"),
]
USERS_DESC = ("Six kinds of user: Galaxy owners in 62 markets, 18.7 million Korean Wallet users, travellers, the banks "
              "and card issuers whose cards it holds, the merchants who take it, and the partners who put IDs, keys "
              "and stablecoins into it.")

WHO = {"gal": "A Galaxy user", "kr": "A Korean Wallet user", "trav": "A traveller", "iss": "A card issuer",
       "mer": "A merchant", "part": "A partner"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "pay", "who": "gal", "name": "Pay with my phone",
     "why": "The everyday loop: add a card, store it as a token, tap in store or from the watch.",
     "steps": [("5.1", "app", "Add a card to Samsung Wallet"), ("3.1", "tokens", "Stored as a network token"),
               ("2.1", "nfc", "Tap to pay in store"), ("5.2", "watch", "Or pay from the watch")]},
    {"id": "korea", "who": "kr", "name": "Pay and earn in Korea",
     "why": "MST and NFC with Korean cards, Samsung Wallet Money, Points and Pay Planner.",
     "steps": [("2.2", "korea", "Pay with a Korean card"), ("4.2", "walletmoney", "Top up Samsung Wallet Money"),
               ("3.4", "points", "Earn Wallet Points"), ("3.4", "payplanner", "Track spending in Pay Planner")]},
    {"id": "send", "who": "gal", "name": "Send money",
     "why": "Tap phones to send in the US or Korea, or send USDC abroad.",
     "steps": [("2.4", "taptransfer", "Tap to Transfer in the US"), ("2.4", "taptransferkr", "Tap transfer in Korea"),
               ("2.5", "stablecoin", "Send USDC abroad")]},
    {"id": "travel", "who": "trav", "name": "Travel abroad",
     "why": "Trips, a digital ID at the airport, cards and QR abroad, and transit by card.",
     "steps": [("3.3", "trips", "Plan in Trips"), ("3.2", "clear", "Show ID at the checkpoint"),
               ("2.2", "overseas", "Pay abroad with Mastercard, Visa or Amex"), ("2.1", "transit", "Ride transit with a card"),
               ("2.6", "gln", "Pay by QR with GLN")]},
    {"id": "card", "who": "gal", "name": "Get a Samsung credit card",
     "why": "The Galaxy Card, issued by Barclays on Visa and run inside the wallet.",
     "steps": [("5.3", "samsungcom", "Apply on Samsung.com"), ("4.1", "galaxycard", "Get the Galaxy Card"),
               ("2.1", "nfc", "Pay with Samsung Wallet for 3% back")]},
    {"id": "issuer", "who": "iss", "name": "Put our cards in Samsung Wallet",
     "why": "Join through Wallet Express or a direct deal, tokenise and push cards from the bank's app.",
     "steps": [("4.3", "walletexpress", "Join through Wallet Express"), ("3.1", "tokens", "Tokenise through the network"),
               ("5.3", "bankapps", "Push cards from the bank's app"), ("4.3", "dzbank", "Launch for a banking group")]},
    {"id": "merchant", "who": "mer", "name": "Take Samsung Wallet",
     "why": "Contactless and MST in store, QR in Asia and Samsung Pay online.",
     "steps": [("2.1", "nfc", "Accept contactless"), ("2.1", "mst", "Accept at a mag-stripe terminal"),
               ("2.6", "unionpay", "Take UnionPay QR in Hong Kong"), ("2.3", "online", "Offer Samsung Pay online")]},
    {"id": "life", "who": "part", "name": "Leave the wallet at home",
     "why": "Identity, car and home keys in the same app.",
     "steps": [("3.2", "koreaid", "Carry a Korean mobile ID"), ("3.3", "carkeys", "Unlock the car"),
               ("3.3", "homekey", "Open the front door")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Tokens for Mastercard cards since 2015, Wallet Express, Mastercard cards tapped in 62 markets and used abroad by Koreans, and Germany's cooperative banks.",
     "steps": [("3.1", "tokens", "MDES tokens since 2015"), ("4.3", "walletexpress", "Wallet Express in the UK"),
               ("2.1", "nfc", "Mastercard cards tapped in store"), ("2.2", "overseas", "Korean Mastercard cards abroad"),
               ("4.3", "dzbank", "Cooperative banks' Mastercards")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, transfers and a card could land",
     "why": "Where Samsung has needs and Mastercard is not yet in: agentic checkout with Galaxy AI, Click to Pay online, cross-border send next to USDC, P2P on Mastercard rails, a Galaxy card outside the US and offers in the Benefits tab.",
     "steps": [("3.5", "agentic", "Agent Pay for Galaxy AI checkout"), ("2.3", "online", "Click to Pay and passkeys online"),
               ("2.5", "stablecoin", "Mastercard Move beside USDC payouts"), ("2.4", "taptransfer", "Send on Mastercard rails"),
               ("4.2", "hanacard", "The Hana Card co-brand"), ("3.4", "points", "Card-linked offers in Benefits")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Samsung Wallet's map",
    "title": "Inside every Samsung Wallet, outside Samsung's own money",
    "lead": "Mastercard has tokenised Mastercard cards for Samsung Pay through MDES since 2015, and in 2023 Samsung joined Mastercard's Wallet Express to bring issuers in. But the products Samsung owns went elsewhere in 2025–26: Tap to Transfer runs on Visa Direct, the first Galaxy Card is a Barclays Visa, cross-border transfers use USDC with Coinbase, and Hong Kong QR uses UnionPay. In Korea, home to most of its users, domestic cards and bank rails carry the payments. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Samsung's own (Q3 2026 guidance, 8 October 2026; Q2 2026 results; Korean newsroom, August 2025) or from Visa, Mastercard and press. Samsung publishes no Wallet revenue or network split; US user numbers are an eMarketer estimate.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Tokens", "MDES", "Mastercard cards since 2015"],
        ["Issuer route", "Wallet Express", "Mastercard, UK, December 2023"],
        ["Galaxy Card", "Visa", "Barclays, July 2026"],
        ["P2P (US)", "Visa Direct", "Tap to Transfer, May 2025"],
        ["Cross-border", "USDC", "Coinbase, late October 2026"],
        ["Korea", "Domestic cards", "18.7m users, KRW 88.6tn in 2024"],
        ["Hong Kong QR", "UnionPay", "February 2026"],
        ["Samsung Money", "Mastercard debit", "SoFi, 2020 ⚠ status"],
    ],
    "sides": {
        "neo": {"dir": "Tokens for Mastercard cards in every market, Wallet Express for issuers, Mastercard cards tapped at home and abroad, and the 2020 Samsung Money debit card.",
                "deals": "What it does not do: the Galaxy Card, P2P, cross-border send, Korean domestic payments, QR or agentic checkout."},
        "snb": {"dir": "Visa's Galaxy Card and Tap to Transfer, USDC with Coinbase, UnionPay QR, Amex abroad, Korean card companies and bank rails, and Samsung's own Knox, IDs and keys.",
                "deals": "Where they meet: every card in the wallet, and the online and agentic checkout Samsung says it will automate."},
    },
    "tl": [
        ["Jul 2015", "MDES to deliver Samsung Pay in Europe"],
        ["Aug 2015", "Samsung Pay launches in Korea with NFC and MST"],
        ["May 2020", "Samsung Money by SoFi on Mastercard debit"],
        ["Dec 2023", "Samsung joins Mastercard Wallet Express"],
        ["May 2025", "Tap to Transfer on Visa Direct"],
        ["Feb 2026", "Amex abroad; UnionPay in Hong Kong"],
        ["Jul 2026", "Galaxy Card with Barclays on Visa"],
        ["Sep 2026", "Germany's cooperative banks join"],
        ["Oct 2026", "USDC stablecoin wallet in the US"],
    ],
    "l": {
        "U": {"d": 1, "s": "Users carry Mastercard among every network's cards.",
              "gap": "Galaxy users store Mastercard, Visa, Amex and UnionPay cards; Galaxy Card holders carry Visa; Koreans pay at home on domestic cards.",
              "neo": "Mastercard cardholders, issuers on Wallet Express.", "snb": "Galaxy Card holders, Korean domestic users, USDC senders."},
        "L5": {"d": 1, "s": "The app holds every network's cards.", "gap": "The app and watch carry Mastercard cards; Samsung.com sells a Visa card; Mastercard documents bank-app provisioning.",
               "neo": "Cards in the app and watch, provisioning guide.", "snb": "Galaxy Card applications, Samsung's own app."},
        "L4": {"d": 1, "s": "Wallet Express is Mastercard's; the Galaxy Card is Visa.", "gap": "Wallet Express and the old SoFi card are Mastercard; the Galaxy Card, Wallet Money and devices are not.",
               "neo": "Wallet Express, Samsung Money by SoFi ⚠, Mastercards from DZ BANK.", "snb": "Galaxy Card, Wallet Money, Hana Card, devices."},
        "L3": {"d": 1, "s": "MDES tokens for Mastercard cards; the rest is Samsung's.", "gap": "Tokens are Mastercard's for its cards; IDs, keys, Trips, Points and AI are Samsung's and partners'.",
               "neo": "MDES tokens.", "snb": "Knox, CLEAR, Korean IDs, car keys, Points, AI."},
        "L2": {"d": 1, "s": "Mastercard in tap-to-pay and abroad; Visa, USDC and local rails elsewhere.", "gap": "Contactless, MST and transit carry Mastercard cards; P2P is Visa Direct, cross-border is USDC, QR is UnionPay and local schemes.",
               "neo": "Contactless, transit, Korean cards abroad.", "snb": "Visa Direct, USDC, UnionPay, GLN, Korean domestic and bank rails."},
        "L1": {"d": 0, "s": "Samsung's own scale and security.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Group results, leadership, Knox, strategy."},
    },
    "t": area_lens(LAYERS),
}
