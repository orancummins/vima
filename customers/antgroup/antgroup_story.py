"""Ant International's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from antgroup_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("A cross-border wallet and payments group as five discs that stack into one, from 150 million merchants, "
       "2 billion accounts and a $1.2 billion Series A at the bottom to Antom's portal, the WorldFirst app and partner "
       "wallets at the top. Click the stack to open it. Choose who you are and what you want to do, and the areas that "
       "deliver it light up across the layers, joined in the order they act. Switch to the Mastercard lens to see how "
       "deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("trav", "Travellers", "plane"),
    ("wal", "Wallet partners", "wallet"),
    ("mer", "Merchants", "store"),
    ("sme", "Cross-border SMEs", "briefcase-business"),
    ("fi", "Banks & lenders", "landmark"),
    ("ai", "AI agents", "bot"),
]
USERS_DESC = ("Six kinds of user: travellers paying abroad with their home wallets, the 53 wallets and bank apps that "
              "join Alipay+, Antom's merchants, WorldFirst's 1.6 million SMEs, the banks and lenders that use its "
              "treasury and credit tools, and the AI agents that now pay on people's behalf.")

WHO = {"trav": "A traveller", "wal": "A wallet", "mer": "A merchant", "sme": "A cross-border SME",
       "fi": "A bank or lender", "ai": "An AI agent"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "travel", "who": "trav", "name": "Pay abroad with my home wallet",
     "why": "Scan a merchant's QR code with GCash or Kakao Pay, or tap where only cards are taken, with Alipay+ in between.",
     "steps": [("5.2", "walletapps", "Open my own wallet"), ("2.1", "aplusqr", "Scan to pay through Alipay+"),
               ("2.2", "aplusnfc", "Or tap at a Mastercard terminal"), ("3.6", "aplusrewards", "Get a merchant offer")]},
    {"id": "wallet", "who": "wal", "name": "Take my wallet global",
     "why": "One connection gives a domestic wallet 150 million merchants abroad, by QR and by NFC on Mastercard.",
     "steps": [("4.1", "walletpartners", "Join Alipay+"), ("2.1", "nationalqr", "Reach national QR schemes"),
               ("2.2", "aplusnfc", "Add tap-to-pay on Mastercard"), ("3.6", "genaicockpit", "Run the wallet with AI tools")]},
    {"id": "merchant", "who": "mer", "name": "Accept payments in 200 markets",
     "why": "Antom's core loop: integrate once, accept cards and wallets, recover declines, screen fraud, win disputes.",
     "steps": [("5.1", "antomportal", "Integrate through the portal"), ("2.3", "antomacq", "Accept cards and wallets"),
               ("3.3", "revbooster", "Recover declined cards"), ("3.1", "antomshield", "Screen for fraud"),
               ("3.2", "smartdispute", "Fight chargebacks")]},
    {"id": "sme", "who": "sme", "name": "Sell abroad and get paid",
     "why": "Collect from marketplaces, hold many currencies, hedge FX and spend on a card.",
     "steps": [("4.3", "wfsme", "Open a WorldFirst account"), ("2.4", "worldacct", "Collect and pay in many currencies"),
               ("3.5", "falcon", "Forecast and hedge FX"), ("2.4", "worldcard", "Spend on the World Card")]},
    {"id": "agent", "who": "ai", "name": "Let an AI agent pay",
     "why": "AMP for wallets, Agent Pay pilots for cards, and a shared way to know which agent is paying.",
     "steps": [("3.4", "amp", "Connect through AMP"), ("3.4", "kya", "Be verified under Know-Your-Agent"),
               ("3.4", "agentpay", "Pay by card through Agent Pay"), ("3.4", "antomagentic", "Check out with AgentSafePay")]},
    {"id": "treasury", "who": "fi", "name": "Move treasury in real time",
     "why": "Blockchain transfers between its own accounts and banks, with tokenised deposits and AI FX.",
     "steps": [("2.5", "whalertp", "Send on WhaleRTP"), ("2.5", "tokdep", "Settle in HSBC tokenised deposits"),
               ("3.5", "barclays", "Trade FX with Barclays")]},
    {"id": "credit", "who": "sme", "name": "Borrow as a small business",
     "why": "Credit built on alternative data, through partners or ANEXT Bank.",
     "steps": [("4.4", "bettrcredit", "Get a credit decision"), ("4.4", "anext", "Bank with ANEXT")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The only card network behind Alipay+ NFC, a partner with Visa in Know-Your-Agent, Agent Pay pilots through Antom, the UK World Card, and every Antom card payment.",
     "steps": [("2.2", "aplusnfc", "Alipay+ NFC on Mastercard"), ("3.4", "kya", "Know-Your-Agent"),
               ("3.4", "agentpay", "Agent Pay pilot"), ("2.4", "worldcard", "UK World Card"),
               ("2.3", "antomacq", "Card acceptance")]},
    {"id": "mcnext", "who": "mc", "name": "Where NFC, disputes and payouts could land",
     "why": "Where Ant International has needs and Mastercard is not yet in: NFC for more of 53 wallets and on iOS, live Agent Pay, Ethoca for Antom's disputes, Move for WorldFirst payouts, World Card beyond the UK, and tokens for Antom.",
     "steps": [("4.1", "walletpartners", "NFC for more wallets"), ("3.2", "smartdispute", "Ethoca and Consumer Clarity"),
               ("2.4", "worldacct", "Move for payouts"), ("2.4", "worldcard", "World Card beyond the UK"),
               ("3.3", "tokenpay", "Network tokens and Click to Pay")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Ant International's map",
    "title": "Mastercard's tap for Alipay+ wallets, on a network built to go around cards",
    "lead": "Mastercard is the only card network behind Alipay+ NFC, which lets GCash and Kakao Pay users tap at 150 million Mastercard terminals. It works with Ant International and Visa on Know-Your-Agent, is piloted by Antom through Agent Pay, and carries WorldFirst's UK World Card. But most of Ant International's volume moves wallet to merchant over its own QR rails, ten national QR schemes and blockchain treasury, outside every card network. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Ant International's own releases, its 2025 Sustainability Report, partner releases and press. Ant International is private and does not publish volumes by rail or network.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["NFC", "Mastercard only", "GCash (Aug 2025), Kakao Pay (Sep 2025)"],
        ["QR", "Own rails", "53 wallets, 10 national QR schemes"],
        ["Agents", "KYA with Mastercard and Visa", "Agent Pay pilot via Antom"],
        ["Acquiring", "Antom, every network", "300+ methods, 200+ markets"],
        ["SME card", "World Card", "Mastercard in the UK"],
        ["Disputes", "Own tools", "SmartDispute, Copilot"],
        ["Treasury", "Blockchain", "WhaleRTP, HSBC tokenised deposits"],
        ["China inbound", "Seven card brands", "Mastercard among them"],
    ],
    "sides": {
        "neo": {"dir": "Alipay+ NFC on Mastercard acceptance, Know-Your-Agent with Verifiable Intent, Agent Pay pilots, the UK World Card, and card acceptance through Antom.",
                "deals": "What it does not do: QR, national schemes, treasury, disputes, payouts or credit."},
        "snb": {"dir": "Alipay+ QR and national QR schemes, WhaleRTP and tokenised deposits, Swift bank-to-wallet, Visa in Know-Your-Agent and agentic pilots, and Ant International's own risk and dispute tools.",
                "deals": "Where they meet: travellers' payments abroad, and the rules for AI agents."},
    },
    "tl": [
        ["2019", "WorldFirst acquired"],
        ["2022", "2C2P acquired; ANEXT Bank"],
        ["May 2024", "Consumer Friendly Zones with Mastercard in Shanghai"],
        ["Aug 2025", "GCash Tap to Pay on Mastercard via Alipay+"],
        ["Sep 2025", "Antom pilots Agent Pay; Kakao Pay NFC"],
        ["Apr 2026", "Agentic Mobile Protocol launched"],
        ["Jul 2026", "$1.2bn Series A"],
        ["Sep 2026", "Brazil licence; Know-Your-Agent with Mastercard and Visa"],
        ["Oct 2026", "HSBC tokenised deposits in the Middle East"],
    ],
    "l": {
        "U": {"d": 1, "s": "Travellers tap on Mastercard; most still scan QR.",
              "gap": "Wallet users reach Mastercard only through Alipay+ NFC; merchants accept it through Antom; SMEs in the UK spend on it.",
              "neo": "NFC tappers, Antom card payers, UK World Card holders.", "snb": "QR scanners, treasury banks, borrowers."},
        "L5": {"d": 0, "s": "The front doors are Ant International's and its partners'.", "gap": "Portal, apps and wallets are not Mastercard's.",
               "neo": "None.", "snb": "Antom portal, WorldFirst app, partner wallets."},
        "L4": {"d": 1, "s": "Mastercard in merchants and China inbound.", "gap": "Merchants accept Mastercard; visitors to China can link it; wallets, SMEs and credit are off-card.",
               "neo": "Antom merchants, China inbound.", "snb": "Wallet partners, SMEs, credit."},
        "L3": {"d": 1, "s": "Agent Pay and KYA; the rest is in-house.",
               "gap": "Agentic work involves Mastercard; risk, disputes, FX and marketing are Ant International's own.",
               "neo": "Agent Pay, Know-Your-Agent.", "snb": "AI SHIELD, SmartDispute, Falcon, A+ Rewards."},
        "L2": {"d": 1, "s": "NFC rides on Mastercard; QR and treasury do not.",
               "gap": "Mastercard carries Alipay+ NFC and the UK World Card; QR, national schemes, WhaleRTP and Swift do not touch it.",
               "neo": "Alipay+ NFC, World Card, card acquiring.", "snb": "QR, national schemes, WhaleRTP, Swift."},
        "L1": {"d": 0, "s": "Ant International's own network, funding and models.", "gap": "Nothing in the foundation is Mastercard's.",
               "neo": "None.", "snb": "Network, funding, licences, AI models."},
    },
    "t": area_lens(LAYERS),
}
