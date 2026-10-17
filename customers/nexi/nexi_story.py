"""Nexi Group's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from nexi_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Europe's self-styled PayTech as five discs that stack into one platform, from €3.6 billion of revenue and the "
       "ICBPI, Nets and SIA mergers at the bottom to partner banks, 3 million terminals and ISVs at the top. Click the "
       "stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up across "
       "the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in "
       "every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("sme", "Small merchants", "store"),
    ("mid", "Mid-market & e-commerce", "building-2"),
    ("isv", "ISVs & partners", "code-xml"),
    ("bank", "Banks & issuers", "landmark"),
    ("pa", "Public administration", "building"),
    ("con", "Cardholders", "user-round"),
]
USERS_DESC = ("Six kinds of user: small merchants on about 3 million terminals, mid-market and online merchants, software "
              "partners, about 250 banks and corporates that issue through Nexi, Italy's public administration, and "
              "the 140 million cardholders behind them.")

WHO = {"sme": "A small merchant", "mid": "A mid-market merchant", "isv": "A software partner", "bank": "A bank",
       "pa": "A public body", "con": "A cardholder"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "shop", "who": "sme", "name": "Take payments in a shop",
     "why": "The everyday loop for an Italian small merchant: a bank partner, a terminal or phone, cards and Bancomat.",
     "steps": [("5.1", "banks", "Sign up through a partner bank"), ("4.1", "smartpay", "Choose SmartPay"),
               ("5.2", "softpos", "Take cards on a phone or SmartPOS"), ("2.4", "bancomat", "Accept PagoBANCOMAT"),
               ("2.1", "acquiring", "Settled by Nexi")]},
    {"id": "online", "who": "mid", "name": "Sell online across Europe",
     "why": "Nexi Checkout and Computop, open-banking payments, wallets and Wero.",
     "steps": [("4.2", "checkout", "Integrate Nexi Checkout"), ("2.2", "computop", "Or Computop in DACH"),
               ("3.1", "mcob", "Offer pay-by-bank"), ("2.6", "apms", "Offer PayPal and Klarna"), ("2.5", "wero", "Accept Wero in Germany")]},
    {"id": "payout", "who": "mid", "name": "Pay out to people",
     "why": "Mastercard Move and Visa Direct for Italian businesses.",
     "steps": [("2.6", "move", "Pay out on Mastercard Move"), ("2.6", "visadirect", "Or on Visa Direct")]},
    {"id": "agent", "who": "mid", "name": "Sell to AI agents",
     "why": "Nexi's MCP server and Google Cloud work, with Visa and Mastercard.",
     "steps": [("3.3", "agentic", "Connect through Nexi's MCP server"), ("3.3", "google", "Use Google's AP2 and UCP"),
               ("3.2", "fraud", "Authenticate the payment")]},
    {"id": "issue", "who": "bank", "name": "Launch a card programme",
     "why": "Nexi Ready managed issuing, processing, wallets and loyalty for a bank.",
     "steps": [("3.4", "nexiready", "Launch with Nexi Ready"), ("2.3", "issuing", "Process on Nexi"),
               ("2.3", "wallets", "Put cards in wallets"), ("3.5", "vas", "Add cashback and loyalty")]},
    {"id": "a2a", "who": "bank", "name": "Run instant payments",
     "why": "Digital Banking Solutions: clearing, instant payments, Verification of Payee, Zippay and the digital euro.",
     "steps": [("4.4", "dbs", "Buy Digital Banking Solutions"), ("2.5", "dph", "Clear instant payments"),
               ("3.2", "vop", "Verify the payee"), ("2.5", "zippay", "Offer mobile-number payments"), ("2.5", "deuro", "Pilot the digital euro")]},
    {"id": "isv", "who": "isv", "name": "Embed payments in a till",
     "why": "Nexi Integrated and SmartStation for software partners.",
     "steps": [("5.3", "isv", "Join Nexi Integrated"), ("5.2", "smartpos", "Run on SmartStation"), ("2.1", "acquiring", "Acquire through Nexi")]},
    {"id": "pa", "who": "pa", "name": "Collect public payments",
     "why": "pagoPA and Smart PA.",
     "steps": [("4.5", "pagopa", "Collect through pagoPA"), ("5.2", "smartpos", "Take payment at a SmartPOS")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Open banking in the gateways, Move payouts in Italy, Ethoca through Nets, and Mastercard cards everywhere Nexi acquires and processes.",
     "steps": [("3.1", "mcob", "Mastercard Open Banking"), ("2.6", "move", "Mastercard Move"), ("3.2", "ethoca", "Ethoca, through Nets"),
               ("2.1", "acquiring", "Acquiring Mastercard"), ("2.3", "issuing", "Processing Mastercard issuers")]},
    {"id": "mcnext", "who": "mc", "name": "Where Nexi Ready, agents and Italian debit could land",
     "why": "Where Nexi has needs and Mastercard is not yet in: a Nexi Ready partner outside Germany, Agent Pay in the MCP gateways, Ethoca across the group, Italy's debit migration, Move beyond Italy, and tokens and Click to Pay in Nexi Checkout.",
     "steps": [("3.4", "nexiready", "Nexi Ready beyond Germany"), ("3.3", "agentic", "Agent Pay and agentic tokens"),
               ("3.2", "ethoca", "Ethoca for Italy and DACH"), ("2.3", "issuing", "Mastercard Debit in Italy"),
               ("2.6", "move", "Move in the Nordics and DACH"), ("4.2", "checkout", "Click to Pay in Nexi Checkout")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Nexi's map",
    "title": "Mastercard owns Nets' old rails; Visa won Nexi Ready",
    "lead": "Nexi accepts and processes Mastercard across 25 countries, runs pay-by-bank in its gateways on Mastercard Open Banking (2024), pays out on Mastercard Move in Italy and used Ethoca through Nets; Mastercard also bought Nets' account-to-account business in 2021. But Visa is the network partner for Nexi Ready in Germany, launched Visa Direct alongside Move, and co-sponsors Luna Rossa with Nexi, while Nexi builds Bancomat's hub, pushes Wero and pilots the digital euro. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Nexi's own (1H 2026 results, 29 July 2026; FY2025 results and Capital Markets Day, 5 March 2026) or from Mastercard and press. Mastercard's newsroom was blocked. Nexi does not disclose its network split.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Acquiring", "Every network", "€837bn in 2025"],
        ["Issuing", "Every network", "140m cards; split not disclosed ⚠"],
        ["Open banking", "Mastercard Open Banking", "In the gateways since March 2024"],
        ["Payouts", "Move and Visa Direct", "Italy, October 2025"],
        ["Managed issuing", "Visa", "Nexi Ready in Germany, April 2026"],
        ["Domestic", "Bancomat hub", "Contract April 2024"],
        ["A2A", "Wero, Zippay, digital euro", "EPI founder"],
        ["Agentic", "Agent Connect", "Exploring, September 2026 ⚠"],
    ],
    "sides": {
        "neo": {"dir": "Card acceptance and issuer processing, Mastercard Open Banking in the gateways, Move payouts, Ethoca through Nets, SoftPOS at parity with Visa, and the old Nets account-to-account rails Mastercard now owns.",
                "deals": "What it does not do: Nexi Ready, the Bancomat hub, Wero, instant payments, pay-later or Google's agentic work."},
        "snb": {"dir": "Visa's Nexi Ready partnership in Germany, Visa Direct, Eurowag fleet cards and Luna Rossa; Bancomat and Dankort; Wero, Zippay and the digital euro; PayPal, Klarna, Compass and Younited.",
                "deals": "Where they meet: payouts, where Move and Visa Direct launched together, and agentic commerce, where Nexi builds with both."},
    },
    "tl": [
        ["Mar 2021", "Mastercard completes the Nets A2A purchase"],
        ["Dec 2021", "Nets partners with Ethoca"],
        ["Mar 2024", "Mastercard Open Banking in Nexi gateways"],
        ["Apr 2024", "Bancomat hub contract"],
        ["Feb 2025", "Wero acquirer in Germany; Eurowag Visa cards"],
        ["Oct 2025", "Mastercard Move and Visa Direct"],
        ["Mar 2026", "Agentic MCP server; Mingrone becomes CEO"],
        ["Apr 2026", "Visa partner for Nexi Ready in Germany"],
        ["Sep 2026", "Named as exploring Agent Connect ⚠; Visa and Nexi sponsor Luna Rossa"],
    ],
    "l": {
        "U": {"d": 1, "s": "Every merchant takes Mastercard; many cardholders carry Bancomat or Dankort.",
              "gap": "Merchants accept every network; banks issue on both networks and the domestic schemes; Nexi does not say which dominates.",
              "neo": "Merchants on Mastercard Open Banking and Move, Mastercard cardholders.", "snb": "Bancomat and Dankort users, Nexi Ready banks in Germany, Wero users."},
        "L5": {"d": 1, "s": "The terminals take Mastercard; the channels are Nexi's.", "gap": "Bank partners and ISVs are Nexi's; SoftPOS prices Mastercard the same as Visa and PagoBANCOMAT.",
               "neo": "Card acceptance on SmartPOS and SoftPOS.", "snb": "Bank partners, ISVs, direct sales."},
        "L4": {"d": 1, "s": "Every line carries Mastercard; none depends on it.", "gap": "Merchant and issuing lines carry Mastercard among other schemes; Digital Banking Solutions and pagoPA do not, and Eurowag cards are Visa.",
               "neo": "Card acceptance and bank cards.", "snb": "Eurowag Visa cards, Digital Banking Solutions, pagoPA."},
        "L3": {"d": 1, "s": "Open banking and Ethoca are Mastercard's; Nexi Ready went to Visa.", "gap": "Mastercard Open Banking and Ethoca run here; Nexi Ready, Google Cloud and Nexi's own fraud and loyalty tools do not.",
               "neo": "Open Banking, Ethoca, agentic exploration.", "snb": "Nexi Ready with Visa, Google Cloud, own open banking and loyalty."},
        "L2": {"d": 1, "s": "Mastercard in cards and Move; domestic schemes and A2A beside it.", "gap": "Acquiring, issuing and Move carry Mastercard; Bancomat, Dankort, Wero, instant payments and pay-later do not.",
               "neo": "Acquiring, issuing, wallets, Move.", "snb": "Bancomat, Dankort, Wero, Zippay, digital euro, Visa Direct, PayPal."},
        "L1": {"d": 0, "s": "Nexi's own capital and history.", "gap": "Nothing in the foundation is Mastercard's; Mastercard bought Nets' A2A arm before the merger.", "neo": "None.", "snb": "Owners, results, leadership, strategy."},
    },
    "t": area_lens(LAYERS),
}
