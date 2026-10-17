"""PayPal Holdings' kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from paypal_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("The digital wallet as five discs that stack into one platform, from 439 million accounts and $1.79 trillion of "
       "volume at the bottom to the PayPal and Venmo apps and partners at the top. Click the stack to open it. Choose who "
       "you are and what you want to do, and the areas that deliver it light up across the layers, joined in the order "
       "they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "PayPal users", "user-round"),
    ("venmo", "Venmo users", "users-round"),
    ("send", "Senders abroad", "send"),
    ("crypto", "Crypto holders", "coins"),
    ("smb", "Small businesses", "briefcase"),
    ("ent", "Enterprises & platforms", "building-2"),
]
USERS_DESC = ("Six kinds of user across 439 million accounts: PayPal users, Venmo's 67 million monthly actives, people "
              "sending money abroad, crypto holders, small businesses, and the enterprises and platforms on Braintree.")

WHO = {"con": "A PayPal user", "venmo": "A Venmo user", "send": "A sender", "crypto": "A crypto holder",
       "smb": "A small business", "ent": "An enterprise"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "pay", "who": "con", "name": "Pay online with PayPal",
     "why": "The core loop: the app, the PayPal button, Pay Later and buyer protection.",
     "steps": [("5.1", "apps", "Open the app"), ("2.1", "checkout", "Pay with the PayPal button"),
               ("2.6", "paylater", "Split it with Pay Later"), ("3.1", "fraud", "Covered by buyer protection")]},
    {"id": "instore", "who": "con", "name": "Pay in a shop",
     "why": "PayPal's debit and credit cards on Mastercard, and phone tap in Germany.",
     "steps": [("2.4", "ppdebit", "Tap the PayPal Debit Mastercard"), ("2.4", "detap", "Or tap the phone in Germany"),
               ("2.5", "ppcredit", "Finance it on PayPal Credit"), ("3.5", "rewards", "Earn cashback and points")]},
    {"id": "venmo", "who": "venmo", "name": "Split and pay with Venmo",
     "why": "Venmo P2P, checkout, the Mastercard debit card and the Visa credit card.",
     "steps": [("2.3", "venmop2p", "Pay friends"), ("2.1", "venmocheckout", "Pay with Venmo at checkout"),
               ("2.4", "venmodebit", "Spend with Venmo Debit"), ("2.5", "venmocredit", "Earn 4% on the Venmo Credit Card")]},
    {"id": "send", "who": "send", "name": "Send money abroad",
     "why": "PayPal P2P, Xoom, PayPal World and cash-out to a card.",
     "steps": [("2.3", "p2p", "Send to a PayPal user"), ("2.3", "xoom", "Send to a bank or cash pickup"),
               ("2.3", "world", "Reach UPI or Weixin Pay"), ("2.3", "cashout", "Cash out to a card")]},
    {"id": "smb", "who": "smb", "name": "Run a small business",
     "why": "Sign up through a partner, take payments online and in store, and borrow.",
     "steps": [("5.2", "isv", "Sign up through Wix or BigCommerce"), ("2.2", "open", "Take payments with PayPal Open"),
               ("2.2", "pos", "Sell in person"), ("4.4", "workingcapital", "Borrow with Working Capital")]},
    {"id": "ent", "who": "ent", "name": "Process payments at scale",
     "why": "Braintree, Fastlane, tokens and payouts.",
     "steps": [("2.2", "braintree", "Process with Braintree"), ("2.1", "fastlane", "Recognise guests with Fastlane"),
               ("3.2", "tokens", "Lift approvals with tokens"), ("2.2", "hyperwallet", "Pay out with Hyperwallet")]},
    {"id": "agent", "who": "smb", "name": "Sell through AI assistants",
     "why": "Agent Ready, Store Sync and the PayPal wallet in ChatGPT, Gemini and Copilot.",
     "steps": [("3.3", "agentready", "Get agent ready"), ("3.3", "aichannels", "Sell in ChatGPT and Copilot"),
               ("3.3", "agentpay", "Accept Agent Pay")]},
    {"id": "crypto", "who": "crypto", "name": "Hold and spend crypto",
     "why": "PYUSD, crypto in the wallet and Pay with Crypto.",
     "steps": [("2.7", "pyusd", "Hold PYUSD"), ("2.7", "crypto", "Buy, send or pay with crypto")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Every debit card, the PayPal Credit and Cashback cards, tokens in the wallet, Agent Pay and One Credential.",
     "steps": [("2.4", "ppdebit", "PayPal and Venmo debit on Mastercard"), ("2.5", "ppcredit", "PayPal Credit and Cashback on Mastercard"),
               ("3.2", "tokens", "Mastercard tokens in the wallet"), ("3.3", "agentpay", "Agent Pay in the PayPal wallet"),
               ("3.2", "onecredential", "One Credential in co-development")]},
    {"id": "mcnext", "who": "mc", "name": "Where Move, One Credential and agents could land",
     "why": "Where PayPal has needs and Mastercard is not yet in: payouts for Xoom and PayPal World, instalments on debit, Agent Pay across every assistant, fraud and identity, issuer services for PayPal Bank, and stablecoin settlement.",
     "steps": [("2.3", "xoom", "Mastercard Move for Xoom and PayPal World"), ("2.6", "paylater", "One Credential instalments on debit"),
               ("3.3", "aichannels", "Agent Pay across ChatGPT, Gemini and Copilot"), ("3.1", "fraud", "Fraud and identity services"),
               ("1.3", "paypalbank", "Issuer services for PayPal Bank"), ("2.7", "pyusd", "Stablecoin settlement for PYUSD")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across PayPal's map",
    "title": "Mastercard's debit partner, with Visa in Venmo credit and cash-out",
    "lead": "Every PayPal and Venmo debit card in the US and UK runs on Mastercard, as do the PayPal Credit and Cashback cards. Agreements in 2016–17 put tokenised Mastercard cards in the wallet without a wallet fee, Agent Pay went into the wallet in October 2025, and One Credential is being built together. Visa carries the Venmo Credit Card and Visa Direct cash-out, and has had wallet parity since 2016; Pay Later, PYUSD and account-to-account rails run off the networks. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are PayPal's own (Q2 2026 results, 28 July 2026; FY2025 10-K) or from its newsroom, Mastercard and press. Mastercard's own pages could not be fetched. PayPal does not publish its network split.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Mastercard", "PayPal US and UK, Venmo, Business"],
        ["Credit", "Mostly Mastercard", "Venmo Credit Card on Visa"],
        ["Wallet", "2016–17 agreements", "No wallet fee; Visa parity"],
        ["Cash-out", "Both networks", "Mastercard debit and Visa Direct"],
        ["Agentic", "Agent Pay", "In the PayPal wallet, October 2025"],
        ["Instalments", "One Credential", "Co-development, June 2025 ⚠"],
        ["Stablecoins", "PYUSD", "Paxos, 70 markets"],
        ["Ownership", "Stripe and Advent bid", "$60.50 a share, July 2026 ⚠"],
    ],
    "sides": {
        "neo": {"dir": "Every debit card, PayPal Credit and Cashback cards, tokens in the wallet, cash-out to debit, Agent Pay and One Credential.",
                "deals": "What it does not do: Venmo credit, Visa Direct cash-out, Xoom, Pay Later, PYUSD or fraud."},
        "snb": {"dir": "The Venmo Credit Card and Visa Direct, PayPal's own Pay Later and fraud models, PYUSD with Paxos, and PayPal World with UPI and Weixin Pay.",
                "deals": "Where they meet: the cards in the wallet, and agent-made payments."},
    },
    "tl": [
        ["Jul 2016", "Visa agreement: wallet parity and Visa Direct"],
        ["Sep 2016", "Mastercard agreement in the US; wallet fee dropped"],
        ["Oct 2017", "Mastercard agreement goes global"],
        ["Jun 2025", "PayPal Credit Mastercard; One Credential"],
        ["Oct 2025", "Agent Pay in the PayPal wallet"],
        ["Nov 2025", "UK relaunch on Mastercard debit and credit"],
        ["Dec 2025", "PayPal Bank applications"],
        ["Jul 2026", "Stripe and Advent bid reported"],
        ["Oct 2026", "Venmo Visa credit card upgraded"],
    ],
    "l": {
        "U": {"d": 1, "s": "Debit and PayPal credit holders carry Mastercard; Venmo credit holders carry Visa.",
              "gap": "PayPal and Venmo debit holders carry Mastercard; Venmo credit holders carry Visa; Pay Later and PYUSD users use neither.",
              "neo": "Debit holders, PayPal Credit and Cashback holders.", "snb": "Venmo credit holders, Pay Later and crypto users."},
        "L5": {"d": 0, "s": "The front doors are PayPal's.", "gap": "Apps, partners and bank ties are PayPal's.", "neo": "None.", "snb": "Apps, software partners, sports, banks."},
        "L4": {"d": 1, "s": "Venmo and merchant services carry Mastercard in part.", "gap": "Venmo's debit and merchants' acceptance involve Mastercard; balances and lending do not.",
               "neo": "Venmo debit, merchant acceptance.", "snb": "Balances, Working Capital, KKR and Blue Owl funding."},
        "L3": {"d": 1, "s": "Agent Pay and One Credential are Mastercard's; fraud is PayPal's.", "gap": "Agent Pay and One Credential are Mastercard products; fraud, ads and Honey are PayPal's own.",
               "neo": "Agent Pay, One Credential ⚠, tokens.", "snb": "Fraud models, ads, Honey, Visa tokens."},
        "L2": {"d": 1, "s": "Debit on Mastercard; Venmo credit and cash-out on Visa.", "gap": "Mastercard has every debit card and most credit; Visa has Venmo credit and Visa Direct; Pay Later, PYUSD and PayPal World use neither.",
               "neo": "Debit, PayPal Credit, Cashback, cash-out.", "snb": "Venmo Credit, Visa Direct, Pay Later, PYUSD, UPI, Pix."},
        "L1": {"d": 0, "s": "PayPal's own scale and licences.", "gap": "Nothing in the foundation is Mastercard's; PayPal Bank would choose its networks directly.", "neo": "None.", "snb": "Licences, PayPal Bank, strategy, the bid."},
    },
    "t": area_lens(LAYERS),
}
