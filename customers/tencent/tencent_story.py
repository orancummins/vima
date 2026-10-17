"""Tencent's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from tencent_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Tencent as a payments player, as five discs that stack into one platform, from RMB751.8 billion of revenue "
       "and Tenpay's licence at the bottom to Weixin's 1.44 billion users, WeChat Pay HK and TenPay Global's partners at "
       "the top. Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it "
       "light up across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep "
       "Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Weixin users in China", "user-round"),
    ("visitor", "Visitors to China", "plane"),
    ("hk", "Hong Kong users", "arrow-left-right"),
    ("mer", "Merchants", "store"),
    ("sender", "Senders abroad", "send"),
    ("partner", "Wallets, acquirers & remitters", "network"),
    ("dev", "Developers & agent builders", "code-xml"),
]
USERS_DESC = ("Seven kinds of user: Weixin's users on the mainland, visitors who bind a foreign card or bring a home "
              "wallet, Hong Kong residents on WeChat Pay HK, the merchants that take Weixin Pay, people abroad sending "
              "money home, the wallets, acquirers and remittance firms that plug into TenPay Global, and developers "
              "building Mini Programs and agents.")

WHO = {"con": "A Weixin user", "visitor": "A visitor to China", "hk": "A Hong Kong resident", "mer": "A merchant",
       "sender": "A sender abroad", "partner": "A wallet or remittance partner", "dev": "A developer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Pay for everything in Weixin",
     "why": "The everyday loop: the app, the wallet on domestic rails, red packets, Mini Programs and a credit line.",
     "steps": [("5.1", "weixin", "Open Weixin"), ("2.1", "wxpay", "Pay by QR with Weixin Pay"), ("2.1", "redpackets", "Send a red packet"),
               ("3.1", "miniprog", "Order in a Mini Program"), ("4.3", "loans", "Borrow on Fenfu or Weilidai")]},
    {"id": "save", "who": "con", "name": "Grow my savings",
     "why": "Licaitong funds and WeSure cover inside the wallet.",
     "steps": [("5.1", "weixin", "Open the wallet"), ("4.2", "licaitong", "Invest through Licaitong"), ("4.2", "wesure", "Buy cover through WeSure")]},
    {"id": "visit", "who": "visitor", "name": "Pay like a local on a visit",
     "why": "Bind a Visa, Mastercard or other card, verify, and pay any Weixin Pay merchant; get tax back on the way out.",
     "steps": [("3.5", "visitorhelp", "Get help in my language"), ("2.3", "foreigncard", "Bind my foreign card"), ("2.3", "feewaiver", "Pay no fee for 90 days"),
               ("3.4", "realname", "Verify with my passport"), ("2.1", "wxpay", "Scan to pay"), ("3.5", "taxrefund", "Get my tax refund")]},
    {"id": "homewallet", "who": "visitor", "name": "Pay with my home wallet",
     "why": "Overseas wallets and PayPal scan Weixin Pay codes through the national gateway.",
     "steps": [("2.4", "cpg", "Scan with my home e-wallet"), ("2.4", "paypal", "Or pay with PayPal"), ("3.1", "miniprog", "Book in a Mini Program")]},
    {"id": "abroad", "who": "con", "name": "Pay with Weixin abroad",
     "why": "Weixin Pay at shops, transport and Mini Programs in other countries.",
     "steps": [("2.5", "outbound", "Pay abroad with Weixin Pay"), ("3.1", "miniprog", "Ride and eat via Mini Programs")]},
    {"id": "hk", "who": "hk", "name": "Spend and send across the border",
     "why": "WeChat Pay HK pays mainland merchants in HKD and sends money instantly over Payment Connect.",
     "steps": [("5.2", "wphkapp", "Open WeChat Pay HK"), ("2.7", "wphk", "Pay in HKD on the mainland"), ("2.7", "payconnect", "Send to a mainland bank account")]},
    {"id": "remit", "who": "sender", "name": "Send money to family in China",
     "why": "Remittances land in a Weixin Pay balance or linked bank card through Visa Direct or Mastercard Move.",
     "steps": [("5.3", "partners", "Use a remittance provider"), ("2.6", "mcmove", "Send via Mastercard Move"), ("2.6", "visadirect", "Or via Visa Direct")]},
    {"id": "merchant", "who": "mer", "name": "Sell through Weixin",
     "why": "Open a merchant account, take Weixin Pay and every interoperable QR, and market in the same app.",
     "steps": [("3.1", "merchantplat", "Sign up as a merchant"), ("2.2", "qrinterop", "Accept every QR"), ("4.1", "commpay", "Pay the processing fee"),
               ("3.2", "marketing", "Advertise with AIM+")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Visitor card binding since 2023, Mastercard Move remittances since December 2025, partner status at TenPay Global, and linked cards in WeChat Pay HK.",
     "steps": [("2.3", "foreigncard", "Mastercard cards bound by visitors"), ("2.6", "mcmove", "Mastercard Move into Weixin Pay"),
               ("5.3", "partners", "A TenPay Global partner"), ("2.7", "wphk", "Linked HK cards ⚠")]},
    {"id": "mcnext", "who": "mc", "name": "Where visitor cards, agents and remittances could land",
     "why": "Where Tencent has needs and Mastercard is thin: risk tools for card binding, agentic payments in Xiaowei and WorkBuddy, more Move volume, refunds to cards and outbound acceptance.",
     "steps": [("3.4", "realname", "Tokens and risk scores for bound cards"), ("3.3", "xiaowei", "Agent Pay for Xiaowei"),
               ("2.6", "mcmove", "Grow Move volume against Visa Direct"), ("3.5", "taxrefund", "Tax refunds to cards"), ("2.5", "outbound", "Acquirer links abroad")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Tencent's payments map",
    "title": "A wallet for 1.4 billion that runs off the card rails, with Mastercard at the border",
    "lead": "Weixin Pay is China's second-largest wallet and runs on domestic rails: wallet balances and bound mainland bank cards, which are UnionPay. Tencent issues no cards. Mastercard enters at the edges: visitors have been able to bind Mastercard cards since 2023, alongside Visa and five other networks, and since December 2025 Mastercard Move pays remittances into Weixin Pay, two years after Visa Direct. Most of the cross-border growth runs on wallet links, PayPal and Payment Connect. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Tencent's own (Q2 2026 results, 12 August 2026) or from Tencent's newsroom, Mastercard, Visa and the press. Tencent does not report payment volumes or Weixin Pay users, and the list of networks visitors can bind comes from a travel guide ⚠.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Domestic wallet", "UnionPay and balances", "Weixin Pay since 2013"],
        ["Visitor cards", "Visa, Mastercard and five more", "Since July–August 2023"],
        ["Remittances", "Mastercard Move", "December 2025"],
        ["Remittances", "Visa Direct", "November 2023"],
        ["Home wallets", "CPG gateway", "40+ wallets, 2025–26"],
        ["PayPal", "PayPal World", "May 2026"],
        ["Hong Kong", "WeChat Pay HK", "Payment Connect, March 2026"],
        ["Agents", "Xiaowei, SkillPay", "Prototype, 2026"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard cards bound by visitors, Mastercard Move remittances, and linked Hong Kong cards ⚠.",
                "deals": "What it does not do: domestic wallet funding, QR rails, home-wallet links, outbound acceptance, loans or agents."},
        "snb": {"dir": "UnionPay cards and balances at home, Visa for cards and Visa Direct, Alipay and UnionPay QR interoperability, CPG wallets, PayPal and Payment Connect.",
                "deals": "Where they meet: visitors' cards and remittances, where Visa arrived first."},
    },
    "tl": [
        ["Aug 2013", "WeChat Pay launched"],
        ["2019", "Mastercard partnership with Weixin Pay ⚠"],
        ["Jul 2023", "PBOC fines Tenpay; global cards allowed into Weixin Pay"],
        ["Aug 2023", "Mastercard cardholders can bind cards"],
        ["Nov 2023", "Visa Direct to Weixin; Mastercard China clearing licence"],
        ["Sep 2025", "Home e-wallets via the CPG"],
        ["Dec 2025", "Mastercard Move to Weixin Pay"],
        ["Mar 2026", "WeChat Pay HK on Payment Connect"],
        ["May 2026", "PayPal World and the visitor fee waiver"],
        ["Aug 2026", "Xiaowei agent prototype"],
    ],
    "l": {
        "U": {"d": 1, "s": "Visitors and senders abroad can use Mastercard; Weixin's own users do not.",
              "gap": "1.44 billion users fund the wallet with domestic cards and balances; Mastercard reaches visitors who bind cards and people sending money in.",
              "neo": "Visitors with Mastercard cards, Mastercard Move senders.", "snb": "Mainland users, merchants, home-wallet visitors, Visa Direct senders."},
        "L5": {"d": 1, "s": "Mastercard is one TenPay Global partner among many.", "gap": "Weixin, WeChat Pay HK and QQ Wallet are Tencent's; Mastercard sits among the partners.",
               "neo": "Partner network.", "snb": "Weixin, QQ Wallet, WeChat Pay HK, wallets and acquirers."},
        "L4": {"d": 0, "s": "The business lines carry no card network.", "gap": "Merchant fees, Licaitong, loans, WeSure and Cloud run without a card product.",
               "neo": "None.", "snb": "Commercial payments, wealth, loans, insurance, cloud."},
        "L3": {"d": 0, "s": "Services are Tencent's own.", "gap": "Mini Programs, marketing, Xiaowei, risk checks and tax refunds involve no Mastercard service.",
               "neo": "None.", "snb": "Mini Programs, AIM+, Xiaowei, real-name checks, tax refunds."},
        "L2": {"d": 1, "s": "Mastercard in visitor cards and remittances; the rest is domestic or A2A.", "gap": "Visa, Amex and others share visitor cards; Visa Direct came first; QR, CPG, PayPal and Payment Connect run without cards.",
               "neo": "Visitor cards, Mastercard Move.", "snb": "Weixin Pay rails, QR interoperability, CPG, PayPal, Visa Direct, Payment Connect."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, licences, AI, WeBank."},
    },
    "t": area_lens(LAYERS),
}
