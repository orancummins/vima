"""Commonwealth Bank of Australia's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from cba_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Australia's largest bank as five discs that stack into one platform, from $1.45 trillion of assets and a 14% "
       "return at the bottom to the CommBank app, branches and brokers at the top. Click the stack to open it. Choose who "
       "you are and what you want to do, and the areas that deliver it light up across the layers, joined in the order "
       "they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("home", "Homebuyers", "house"),
    ("inv", "Investors", "trending-up"),
    ("sme", "Businesses & merchants", "briefcase"),
    ("corp", "Corporates & institutions", "factory"),
    ("kiwi", "ASB customers", "earth"),
]
USERS_DESC = ("Six kinds of customer: everyday customers (CBA is the main bank for one in three Australians), homebuyers, "
              "CommSec investors, businesses and the merchants on CommBank terminals, corporates and institutions, and ASB's "
              "customers in New Zealand.")

WHO = {"con": "A CommBank customer", "home": "A homebuyer", "inv": "An investor", "sme": "A business owner",
       "corp": "A corporate treasurer", "kiwi": "An ASB customer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a Debit Mastercard, the app, warnings and fraud checks.",
     "steps": [("4.2", "accounts", "Open a Smart Access account"), ("2.1", "debit", "Pay with Debit Mastercard"), ("5.1", "app", "Run it in the app"),
               ("3.1", "warnings", "Get a warning before a risky payment"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "card", "who": "con", "name": "Borrow and earn on a card",
     "why": "A Mastercard credit card, Yello points and Velocity, or StepPay for a one-off.",
     "steps": [("2.2", "credit", "Take a Smart or Ultimate Mastercard"), ("3.3", "yello", "Earn Yello points"),
               ("3.3", "velocity", "Convert to Velocity Points"), ("2.2", "steppay", "Split a purchase with StepPay")]},
    {"id": "online", "who": "con", "name": "Shop online and with an agent",
     "why": "Click to Pay and wallets today, and an AI agent paying with a CBA debit card in January 2026's Agent Pay trial.",
     "steps": [("2.6", "wallets", "Add a card to a wallet"), ("2.6", "ctp", "Check out with Click to Pay"), ("3.4", "agentpay", "Let an agent buy the tickets")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "A quarter of Australia's home loans, decided fast and settled digitally.",
     "steps": [("5.3", "brokers", "Apply direct or through a broker"), ("3.1", "identity", "Verify with an ePassport"), ("4.1", "homeloans", "Take a home loan"),
               ("5.1", "app", "Manage it in the app")]},
    {"id": "invest", "who": "inv", "name": "Start investing",
     "why": "CommSec, Everyday Investing from $2, and Yello points for trading.",
     "steps": [("4.5", "commsec", "Open a CommSec account"), ("3.3", "yello", "Earn Yello points on trades"), ("3.2", "insights", "Track goals in the app")]},
    {"id": "sme", "who": "sme", "name": "Run a business and take payments",
     "why": "A business account, Visa debit and Mastercard credit, CommBank terminals at 0.99%, PayTo and Companion.",
     "steps": [("4.3", "business", "Open a business account"), ("2.3", "bizdebit", "Spend with Business Visa Debit"), ("2.3", "bizcredit", "Use a business credit card"),
               ("2.4", "acquiring", "Take cards on a Smart terminal"), ("2.5", "payto", "Collect by PayTo"), ("3.2", "companion", "Borrow through Companion")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "Institutional transaction banking, CommBiz and NPP payments.",
     "steps": [("4.4", "ibm", "Bank with IB&M"), ("5.1", "netbank", "Run it in CommBiz"), ("2.5", "fastpay", "Pay in real time over the NPP")]},
    {"id": "nz", "who": "kiwi", "name": "Bank in New Zealand",
     "why": "ASB, CBA's New Zealand bank.",
     "steps": [("4.6", "asb", "Bank with ASB")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Consumer debit and credit, Bankwest and business credit cards, Click to Pay, Mastercard tickets in Yello and Australia's first Agent Pay purchase.",
     "steps": [("2.1", "debit", "Debit Mastercard"), ("2.1", "worlddebit", "World Debit Mastercard"), ("2.2", "credit", "Mastercard credit cards"),
               ("2.3", "bizcredit", "Business credit on Mastercard"), ("2.6", "ctp", "Click to Pay"), ("3.4", "agentpay", "Agent Pay trial")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, scam scores and offers could land",
     "why": "Where CBA has needs and Mastercard is not yet in: Agent Pay for Companion, scam scoring on account-to-account payments, offers to fund rewards under the 0.3% cap, acquirer tools, and business debit.",
     "steps": [("3.2", "companion", "Agent Pay inside Companion"), ("3.1", "fraud", "Scam scores on NPP and PayTo"),
               ("3.3", "yello", "Merchant-funded offers in Yello"), ("2.4", "acquiring", "Risk and merchant data for acquiring"),
               ("2.3", "bizdebit", "Win back business debit")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Commonwealth Bank's map",
    "title": "Australia's biggest card book on Mastercard, with eftpos in the same wallet",
    "lead": "CBA's consumer debit cards and every consumer credit card run on Mastercard, and CBA holds 29.3% of Australia's card balances. Bankwest's cards and business credit cards are Mastercard too, Click to Pay is live, and a CBA debit card made Australia's first Agent Pay purchase in January 2026. But eftpos sits on the same debit cards, Visa has business debit, and payments between accounts run on AP+'s rails. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are CBA's own (FY26 results, 12 August 2026) or from CommBank's product pages as read on 17 October 2026, Mastercard, the RBA and AP+. No public CBA–Mastercard agreement was found; ASB's card network and eftpos on the debit card are not confirmed from a primary page.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Consumer debit", "Mastercard", "Debit and World Debit Mastercard; eftpos on the card ⚠"],
        ["Consumer credit", "Mastercard", "29.3% of Australian card balances"],
        ["Business debit", "Visa", "Business Visa Debit Card"],
        ["Business credit", "Mastercard", "Business and corporate cards ⚠"],
        ["Agentic", "Agent Pay", "Australia's first, January 2026"],
        ["Online checkout", "Click to Pay", "All CBA Mastercard cards"],
        ["Account-to-account", "PayTo, NPP", "AP+ rails"],
        ["Regulation", "RBA caps", "0.3% credit, 8c debit, 1 Oct 2026"],
    ],
    "sides": {
        "neo": {"dir": "Consumer debit and credit, Bankwest, business credit and StepPay cards, Click to Pay, Mastercard tickets in Yello, Agent Pay, and acceptance on CommBank terminals.",
                "deals": "What it does not do: business debit, the eftpos half of debit, PayTo and NPP, fraud and scam models, AI or ASB."},
        "snb": {"dir": "eftpos on the debit card and Keycard, Visa business debit and (⚠) ASB, AP+'s NPP and PayTo, CBA's own fraud, identity and AI, Velocity and Klarna.",
                "deals": "Where they meet: debit routing, where every tap can go to Mastercard or eftpos."},
    },
    "tl": [
        ["1984", "First CBA Mastercard credit cards"],
        ["2008", "Bankwest, a Mastercard issuer, joins"],
        ["Nov 2023", "CommBank Yello launches"],
        ["2025 ⚠", "Click to Pay on CBA Mastercard cards"],
        ["Jan 2026", "First Agent Pay purchase in Australia, on a CBA debit card"],
        ["Mar 2026", "RBA bans surcharges and cuts caps"],
        ["Aug 2026", "FY26 results; Velocity joins Yello"],
        ["Oct 2026", "Surcharge ban and 0.3% credit cap in force"],
        ["Apr 2027", "1.0% cap on foreign cards"],
    ],
    "l": {
        "U": {"d": 1, "s": "Most personal cardholders carry Mastercard.",
              "gap": "Consumer debit and credit cardholders carry Mastercard; business debit holders carry Visa and ASB's customers carry Visa ⚠.",
              "neo": "Personal debit and credit cardholders, Bankwest cardholders.", "snb": "Business debit holders, ASB customers, Keycard holders."},
        "L5": {"d": 0, "s": "The front doors are CBA's.", "gap": "App, NetBank, CommBiz, branches and brokers are the bank's own.", "neo": "None.", "snb": "App, NetBank, branches, brokers."},
        "L4": {"d": 1, "s": "Accounts come with Debit Mastercard.", "gap": "Everyday accounts carry Debit Mastercard and business accounts Visa debit; loans, CommSec, IB&M and ASB have no Mastercard role.",
               "neo": "Personal accounts through Debit Mastercard.", "snb": "Home loans, business accounts, CommSec, IB&M, ASB."},
        "L3": {"d": 1, "s": "Agent Pay and Yello tickets are Mastercard's; the rest is CBA's.", "gap": "Fraud, identity and AI are built in-house; Mastercard runs the Agent Pay trial and presale tickets in Yello.",
               "neo": "Agent Pay, Mastercard Presale tickets.", "snb": "Fraud models, warnings, Companion, Velocity."},
        "L2": {"d": 1, "s": "Cards on Mastercard; eftpos, Visa and NPP alongside.", "gap": "Mastercard has consumer debit and all credit; eftpos shares the debit card, Visa has business debit, and NPP and PayTo are AP+'s.",
               "neo": "Debit, credit, Bankwest, business credit, StepPay, Click to Pay.", "snb": "eftpos, Visa business debit, PayTo, NPP."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, brands, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
