"""GCB Bank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from gcb_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Ghana's largest bank as five discs that stack into one platform, from GH¢67 billion of assets and a 1953 "
       "state charter at the bottom to 184 branches, the GCB app and G-Money agents at the top. Click the stack to open "
       "it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined "
       "in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("hnw", "Private-banking clients", "gem"),
    ("dia", "Ghanaians abroad & their families", "earth"),
    ("wal", "G-Money users & agents", "smartphone"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates, SOEs & government", "building-2"),
    ("trade", "Importers & exporters", "globe"),
]
USERS_DESC = ("Seven kinds of customer: everyday account holders, private-banking clients, Ghanaians abroad and the "
              "families they send to, G-Money users and agents, small businesses, the corporates and state enterprises "
              "that make GCB Ghana's largest lender, and traders on the Africa and China corridors.")

WHO = {"con": "A GCB customer", "hnw": "A private-banking client", "dia": "A Ghanaian abroad", "wal": "A G-Money user",
       "sme": "A small business", "corp": "A corporate treasurer", "trade": "A trader"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a ReadyCash or Visa or Mastercard card, the app, instant transfers and card security.",
     "steps": [("4.1", "accounts", "Open an account"), ("2.1", "readycash", "Get a free ReadyCash card"), ("2.1", "debit", "Upgrade to Visa or Mastercard debit"),
               ("5.2", "app", "Run it in the app"), ("2.5", "gip", "Send money instantly"), ("3.1", "security", "Protected by chip and 3-D Secure")]},
    {"id": "wallet", "who": "wal", "name": "Live on a mobile wallet",
     "why": "G-Money: a telco-agnostic wallet with agents, GhQR, savings and loans.",
     "steps": [("5.3", "agents", "Cash in with an agent"), ("2.6", "gmoney", "Pay and send with G-Money"),
               ("2.6", "gmoneybiz", "Receive wages by bulk payment"), ("3.2", "amber", "Earn loyalty points")]},
    {"id": "premium", "who": "hnw", "name": "Bank privately",
     "why": "Amber Club, Visa Signature and Infinite, and GCB Capital.",
     "steps": [("3.2", "amber", "Join Amber Club"), ("2.2", "hnw", "Carry Visa Infinite"), ("4.5", "capital", "Invest with GCB Capital")]},
    {"id": "diaspora", "who": "dia", "name": "Send money home",
     "why": "Remittances through money-transfer operators into Link2Home accounts and wallets.",
     "steps": [("2.7", "remit", "Send through a transfer operator"), ("4.1", "accounts", "Save in a Link2Home account"),
               ("5.2", "ebank", "Manage it online"), ("2.6", "gmoney", "Family receive it in G-Money")]},
    {"id": "borrow", "who": "con", "name": "Borrow to buy",
     "why": "Salary Advance, 24-hour loans and buy now pay later.",
     "steps": [("4.1", "loans", "Take a Salary Advance"), ("4.1", "bnpl", "Buy now, pay later"), ("5.2", "app", "Repay in the app")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "An SME account, Visa business cards, Lite Pay acceptance and collections.",
     "steps": [("4.2", "sme", "Open an SME account"), ("2.3", "visabiz", "Spend on a Visa business card"),
               ("2.4", "litepay", "Take cards with Lite Pay"), ("3.3", "gcbpay", "Collect with GCB-Pay")]},
    {"id": "corp", "who": "corp", "name": "Run a corporate or state enterprise",
     "why": "Ghana's largest loan book, the Corporate Mastercard and collection platforms.",
     "steps": [("4.3", "corporate", "Borrow from Ghana's largest lender"), ("2.3", "corpmc", "Pay with the Corporate Mastercard"),
               ("5.3", "portals", "Manage cards in the portal"), ("3.3", "fees", "Collect fees through branches")]},
    {"id": "trade", "who": "trade", "name": "Trade across Africa and with China",
     "why": "Trade finance, the Afro-Asia desk, PAPSS and a planned RMB route.",
     "steps": [("4.4", "trade", "Open a letter of credit"), ("4.4", "afroasia", "Find buyers through the Afro-Asia desk"),
               ("2.7", "papss", "Pay Nigeria in naira over PAPSS"), ("2.7", "rmb", "Settle in RMB (planned)")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Ghana's first Mastercard principal: debit alongside Visa, the Corporate Mastercard, acceptance, and the MD on Mastercard's Africa council.",
     "steps": [("2.1", "debit", "Mastercard debit, Standard to Platinum"), ("2.3", "corpmc", "Corporate Mastercard since 2008"),
               ("2.4", "litepay", "Accepted on Lite Pay and POS"), ("1.2", "leadership", "MD on the Africa Leadership Council")]},
    {"id": "mcnext", "who": "mc", "name": "Where premium, wallets and remittances could land",
     "why": "Where GCB has needs and Mastercard is not yet in: a top tier against Visa Infinite, a companion card for G-Money, Move for diaspora money, Tap on Phone, fraud tools and offers.",
     "steps": [("2.2", "hnw", "World Elite against Visa Infinite"), ("2.6", "gmoney", "A Mastercard companion card for G-Money"),
               ("2.7", "remit", "Mastercard Move for diaspora inflows"), ("2.4", "litepay", "Tap on Phone for Lite Pay merchants"),
               ("3.1", "security", "Fraud scoring and tokens"), ("3.2", "amber", "Priceless and card-linked offers")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across GCB Bank's map",
    "title": "Ghana's first Mastercard bank, where Visa took the top tier and mobile money moves the cash",
    "lead": "GCB became Ghana's first Mastercard principal in 2008 and still issues Mastercard debit and the Corporate Mastercard. But it offers Visa debit tier for tier, gave its premium Signature and Infinite cards to Visa in 2024 and widened that work in June 2026. Its default ReadyCash card runs on gh-link, and most money in Ghana moves on mobile money and GhIPSS. Its MD joined Mastercard's Africa Leadership Council in March 2026. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own as reported in the Ghanaian press (H1 2026 statement, 29 July 2026; FY2025 results, 25 March 2026). GCB's live site is behind a bot check, so product pages come from archived snapshots; the split of cards by network is not published.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Default card", "ReadyCash", "gh-link, free with every account"],
        ["Debit", "Visa and Mastercard", "Tier for tier; split not published ⚠"],
        ["Premium", "Visa", "Signature and Infinite, Dec 2024"],
        ["Corporate card", "Mastercard", "Since 2008"],
        ["Business cards", "Visa", "Debit and prepaid, about 2022 ⚠"],
        ["Wallet", "G-Money", "Mobile money; no card"],
        ["Cross-border", "PAPSS, MTOs", "Gateway bank for PAPSS"],
        ["Relationship", "Mastercard council", "MD nominated Mar 2026"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard debit and the Corporate Mastercard, acceptance on Lite Pay and ATMs, and a seat for the MD on its Africa council.",
                "deals": "What it does not do: premium cards, business prepaid, the wallet, instant transfers, remittances or data."},
        "snb": {"dir": "Visa's premium and business cards and its data offer, gh-link's ReadyCash, GhIPSS Instant Pay, G-Money, PAPSS and money-transfer operators.",
                "deals": "Where they meet: everyday debit, where GCB offers both networks side by side."},
    },
    "tl": [
        ["Oct 2008", "First Mastercard principal in Ghana"],
        ["Mar 2016", "Lite Pay accepts Visa, Mastercard and gh-link"],
        ["Jan 2020", "G-Money launched"],
        ["Jul 2020", "Instant Visa and Mastercard issuance in branches"],
        ["Mar 2023", "First PAPSS client payment ⚠"],
        ["Jan 2024", "GhIPSS to process Visa's domestic transactions"],
        ["Dec 2024", "Visa Signature and Infinite launched"],
        ["Jan 2025", "Mastercard opens Accra office; new MD"],
        ["Mar 2026", "MD joins Mastercard's Africa council"],
        ["Jun 2026", "GCB and Visa widen collaboration"],
        ["Jul 2026", "H1 profit up 46%"],
    ],
    "l": {
        "U": {"d": 1, "s": "Some cardholders carry Mastercard; most money moves elsewhere.",
              "gap": "Debit holders may hold Mastercard or Visa; premium and business holders carry Visa; ReadyCash and G-Money users carry neither.",
              "neo": "Mastercard debit and corporate cardholders.", "snb": "Visa premium and business holders, ReadyCash and G-Money users, traders."},
        "L5": {"d": 1, "s": "The front doors are GCB's; portals serve Mastercard corporate cards.", "gap": "Branches, ATMs, app and agents are the bank's; the corporate card portal serves the Corporate Mastercard ⚠.",
               "neo": "Corporate card portal ⚠.", "snb": "Branches, app, G-Money agents."},
        "L4": {"d": 1, "s": "Corporate banking carries the Corporate Mastercard.", "gap": "Accounts default to gh-link ReadyCash; SME cards are Visa; loans, BNPL and trade have no network role.",
               "neo": "Corporate Mastercard.", "snb": "Accounts, SME, BNPL, trade, GCB Capital."},
        "L3": {"d": 1, "s": "Card security uses both schemes; the rest is GCB's or Visa's.", "gap": "3-D Secure on both networks; Ghana Card onboarding is GCB's; Visa offers data and premium benefits.",
               "neo": "3-D Secure on Mastercard cards.", "snb": "Visa benefits and data offer, Ghana Card, collections."},
        "L2": {"d": 1, "s": "Mastercard debit and corporate cards; Visa, gh-link, GhIPSS and PAPSS carry the rest.", "gap": "Mastercard shares debit with Visa and owns the corporate card; premium, business, wallet, instant and cross-border rails are not Mastercard's.",
               "neo": "Mastercard debit, Corporate Mastercard, acceptance.", "snb": "Visa premium and business, ReadyCash, GIP, G-Money, PAPSS."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's, though the MD sits on its Africa council.", "neo": "None.", "snb": "Capital, ownership, strategy, technology."},
    },
    "t": area_lens(LAYERS),
}
