"""Google's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from google_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Google as a payments player, as five discs that stack into one platform, from Alphabet's $402.8 billion of "
       "revenue at the bottom to Google Wallet, the Google Pay app in India, Chrome and Gemini at the top. Click the "
       "stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the "
       "layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("shop", "Shoppers & cardholders", "user-round"),
    ("india", "Google Pay users in India", "zap"),
    ("mer", "Merchants & PSPs", "store"),
    ("dev", "Developers & agent builders", "code-xml"),
    ("issuer", "Card issuers", "landmark"),
    ("biz", "Businesses paying Google", "briefcase-business"),
]
USERS_DESC = ("Six kinds of user: shoppers who keep cards in Google Wallet and Chrome, Google Pay's UPI users in India, "
              "merchants and the processors that add the Google Pay button, developers building agents that pay, the "
              "issuers whose cards Google tokenises, and the advertisers, cloud customers and Play buyers who pay Google.")

WHO = {"shop": "A shopper", "india": "A Google Pay user in India", "mer": "A merchant", "dev": "A developer",
       "issuer": "A card issuer", "biz": "A business paying Google"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "tap", "who": "shop", "name": "Pay with my phone",
     "why": "A card added to Google Wallet becomes a token for tap to pay and transit.",
     "steps": [("5.1", "walletapp", "Open Google Wallet"), ("2.3", "tokens", "Add a card as a token"),
               ("2.2", "tap", "Tap to pay"), ("2.2", "transit", "Tap through the gates")]},
    {"id": "online", "who": "shop", "name": "Check out online",
     "why": "Chrome autofill, a virtual card, Google Pay and BNPL if wanted.",
     "steps": [("5.3", "chrome", "Autofill in Chrome"), ("2.1", "chromevc", "Use a virtual card"), ("2.1", "gpay", "Pay with Google Pay"),
               ("2.4", "bnpl", "Or split it with BNPL")]},
    {"id": "agent", "who": "shop", "name": "Let an agent buy for me",
     "why": "Universal Cart watches prices; AP2 mandates prove what the shopper approved.",
     "steps": [("5.4", "aimode", "Ask Gemini or AI Mode"), ("3.4", "ucart", "Add to Universal Cart"), ("3.3", "benefits", "Pick the card with the best perks"),
               ("2.6", "ap2", "Approve a mandate")]},
    {"id": "india", "who": "india", "name": "Pay and borrow in India",
     "why": "UPI first, then RuPay credit on UPI and the Flex card.",
     "steps": [("5.2", "gpayapp", "Open Google Pay"), ("2.5", "upi", "Pay by UPI"), ("2.5", "rupaycredit", "Link a RuPay credit card"),
               ("4.4", "flex", "Get a Flex card"), ("2.3", "indiatokens", "Tap a tokenised card")]},
    {"id": "merchant", "who": "mer", "name": "Add Google to my checkout",
     "why": "The Google Pay button through a PSP, faster authentication and UCP checkout in AI Mode.",
     "steps": [("5.5", "psps", "Integrate through a PSP"), ("3.1", "directcheckout", "Offer direct checkout"), ("3.1", "spa", "Skip the passcode"),
               ("3.4", "ucp", "Sell through UCP")]},
    {"id": "dev", "who": "dev", "name": "Build an agent that pays",
     "why": "AP2 on Google Cloud, with cards, bank transfers or stablecoins.",
     "steps": [("4.3", "cloud", "Build on Google Cloud"), ("2.6", "ap2", "Use AP2 mandates"), ("2.6", "x402", "Or pay in stablecoins"),
               ("3.2", "dcapi", "Verify the user")]},
    {"id": "issuer", "who": "issuer", "name": "Get my card into Google Wallet",
     "why": "Tokens, perks shown at checkout and virtual cards in Chrome.",
     "steps": [("2.3", "tokens", "Provision tokens"), ("2.1", "chromevc", "Offer virtual cards"), ("3.3", "benefits", "Show card perks")]},
    {"id": "biz", "who": "biz", "name": "Pay Google",
     "why": "Advertisers, cloud customers and Play buyers pay Google by card, processed by PayPal among others.",
     "steps": [("4.1", "search", "Buy ads"), ("4.2", "play", "Buy on Play"), ("2.7", "billing", "Pay by card")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Mastercard cards tokenised in Google Wallet and Google Pay, MDES in India since 2021, a launch partner of AP2 and a backer of UCP.",
     "steps": [("2.3", "tokens", "Mastercard tokens in Wallet"), ("2.3", "indiatokens", "MDES in Google Pay India"),
               ("2.6", "ap2", "AP2 launch partner"), ("3.4", "ucp", "Backs UCP")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, authentication and BNPL could land",
     "why": "Where Google has needs and Mastercard is not yet in: Agent Pay tokens in Universal Cart and Gemini, authentication parity with Visa in Europe, a Mastercard rail for BNPL, card benefits at checkout, and services for Google's own billing.",
     "steps": [("3.4", "ucart", "Agent Pay tokens in Universal Cart"), ("3.1", "spa", "Authentication beside Visa"),
               ("2.4", "bnpl", "A Mastercard rail for BNPL"), ("3.3", "benefits", "Mastercard perks at checkout"),
               ("2.7", "billing", "Services for Google's billing")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Google's map",
    "title": "In every wallet and every protocol, but Visa gets the exclusives",
    "lead": "Google holds Mastercard cards as tokens in Google Wallet and Google Pay, used MDES in India from 2021, made Mastercard a launch partner of AP2 and counts it among UCP's backers. But Google issues almost nothing itself, and where it has chosen one network it has chosen Visa: BNPL in Google Pay settles on Visa virtual cards, Visa came first in India, and Europe's new Secure Payment Authentication launched with Visa. In India, UPI and RuPay carry Google's business and its first credit card. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Alphabet's own (Q2 2026 results, 22 July 2026; FY2025 10-K) or from Google's blogs and developer pages, Axis Bank, NPCI data via the press, the CFPB and PayPal. Google does not publish a network split or payments revenue. Mastercard's own January 2026 page could not be fetched ⚠.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Wallet tokens", "Every network", "Mastercard via MDES ⚠"],
        ["India tokens", "Visa then Mastercard", "Sep 2020; Dec 2021"],
        ["BNPL in Google Pay", "Visa", "Virtual cards for all four lenders"],
        ["Europe authentication", "Visa", "SPA, June 2026"],
        ["Flex card (India)", "RuPay", "Axis Bank, Dec 2025"],
        ["UPI", "32.7%", "May 2026, second to PhonePe"],
        ["AP2", "Mastercard a launch partner", "Sep 2025; Visa not named"],
        ["UCP", "Mastercard, Visa, Amex", "Jan 2026"],
    ],
    "sides": {
        "neo": {"dir": "Tokens for Mastercard cards in Google Wallet and Google Pay, MDES in India, a launch seat in AP2 and support for UCP.",
                "deals": "What it does not do: Google's BNPL rail, Europe's new authentication, Google's own card, or anything live inside Gemini or Universal Cart."},
        "snb": {"dir": "Visa for BNPL virtual cards, India's first tokens and Secure Payment Authentication; RuPay and UPI in India; PayPal processing Google's own billing; American Express in AP2, UCP and Chrome virtual cards; stablecoins through x402.",
                "deals": "Where they meet: every tokenised card in the wallet, and the agent-made purchases that AP2 and UCP will route."},
    },
    "tl": [
        ["Sep 2020", "Google Pay India tokens with Visa"],
        ["Dec 2021", "Mastercard MDES tokens in Google Pay India"],
        ["May 2022", "Virtual cards in Chrome and Android"],
        ["Jun 2024", "US Google Pay app closes"],
        ["May 2025", "CFPB withdraws its Google Payment order"],
        ["Sep 2025", "AP2 launched with Mastercard; PayPal partnership"],
        ["Dec 2025", "Flex card with Axis Bank on RuPay"],
        ["Jan 2026", "UCP at NRF; Mastercard joins"],
        ["May 2026", "Universal Cart; AP2 to Gemini Spark"],
        ["Jun 2026", "Secure Payment Authentication with Visa"],
    ],
    "l": {
        "U": {"d": 1, "s": "Shoppers carry Mastercard in the wallet; India runs on UPI.",
              "gap": "Mastercard holders pay through Google Wallet and Google Pay; Indian users mostly pay by UPI and RuPay; BNPL users pay on Visa.",
              "neo": "Mastercard holders using Wallet and Google Pay.", "snb": "UPI and RuPay users, BNPL users, PayPal-processed Google buyers."},
        "L5": {"d": 1, "s": "The doors hold every card.", "gap": "Wallet, Chrome and PSPs carry Mastercard among others; the India app is UPI-first; Gemini's network role is not public.",
               "neo": "Mastercard cards in Wallet, Chrome and PSP checkouts.", "snb": "UPI in the Google Pay app, Visa BNPL in Chrome."},
        "L4": {"d": 0, "s": "Google's own lines barely use Mastercard.", "gap": "Ads, Cloud and Play accept cards; Google's only co-brand card is on RuPay.",
               "neo": "Acceptance on Play and billing.", "snb": "Flex on RuPay, Google Cloud, Search and ads."},
        "L3": {"d": 1, "s": "UCP includes Mastercard; authentication started with Visa.", "gap": "Mastercard backs UCP but Secure Payment Authentication launched with Visa, and no Mastercard tie to Universal Cart is public.",
               "neo": "UCP support, card perks for any network.", "snb": "Visa in SPA, Airwallex and Adyen, Gemini, ID passes."},
        "L2": {"d": 1, "s": "Mastercard tokens everywhere; Visa for BNPL; UPI in India.", "gap": "Tokens and AP2 include Mastercard; BNPL is Visa; UPI and RuPay carry India; x402 carries stablecoins.",
               "neo": "Tokens, MDES in India, AP2 partner.", "snb": "Visa BNPL, UPI, RuPay, x402, PayPal processing."},
        "L1": {"d": 0, "s": "Alphabet's own scale and licences.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Results, leadership, licences, PayPal partnership."},
    },
    "t": area_lens(LAYERS),
}
