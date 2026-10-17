"""Lloyds Banking Group's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the H1 2026 results and Accelerate 2030 strategy
(30 July 2026) and the 2025 results (29 January 2026). ``neo`` is the Mastercard lens: [depth, note], where
3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

H1 = "https://www.investegate.co.uk/announcement/rns/lloyds-banking-group--lloy/2026-half-year-results/9694683"
FY25 = "https://www.investegate.co.uk/announcement/rns/lloyds-banking-group--lloy/2025-results-/9392603"
A2030 = "https://www.lloydsbankinggroup.com/assets/pdfs/who-we-are/accelerate-2030/2026-lbg-hy-strategy-presentation.pdf"
EXCO = "https://www.lloydsbankinggroup.com/who-we-are/group-overview/group-executive-committee.html"
CURVE = "https://www.investegate.co.uk/announcement/rns/lloyds-banking-group--lloy/curve-acquisition/9242567"
CURVEBLOG = "https://www.curve.com/blog/curve-is-joining-lloyds-banking-group/"
VISA24 = "https://www.bankingexchange.com/news-feed/item/10023-lloyds-to-transfer-10-million-cards-to-visa"
STABLE = "https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds-banking-group/lloyds-and-visa-test-round-the-clock-cross-border-settlement-using-stablecoins.html"
AUTO = "https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds-banking-group/lloyds-banking-group-launches-lloyds-auto.html"
HALIFAX = "https://www.marketingweek.com/lloyds-retire-halifax-173-years/"
PAYFROM = "https://www.openbankingexpo.com/news/mastercard-and-lloyds-enter-payment-partnership/"
CFR = "https://thefintechtimes.com/mastercard-takes-the-fight-to-app-fraud-with-ai-powered-consumer-risk-tool"
AGENTIC = "https://www.fstech.co.uk/fst/Lloyds_Pilots_Agentic_AI_Assistant_For_Mobile_Customers.php"
TOKEN = "https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds/tokenisation-set-to-transform-financial-services.html"
FRAUD = "https://www.ukfinance.org.uk/policy-and-guidance/reports-and-publications/annual-fraud-report-2026"
RATINGS = "https://www.lloydsbankinggroup.com/investors/fixed-income-investors/credit-ratings.html"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · ring-fence · brands", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: half of UK adults as customers, £491 billion of loans and RoTE back above 17%, banks dating from 1695, Halifax being folded into Lloyds, and Accelerate 2030.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "28 million customers, RoTE 17%.", "div": "lbg", "rev": "eic", "products": [
            P("balance", "Balance sheet & earnings", "About 28 million customers, half of UK adults; loans of £491.5 billion and deposits of £500.9 billion at 30 June 2026; statutory profit after tax of £3.1 billion in the half (RoTE 17.1%) and £4.8 billion in 2025; CET1 13.6%; rated A3/A-/A+ at group level.",
              s=["con"], neo=[0, ""], src=[["H1 2026 results", H1], ["2025 results", FY25], ["Lloyds: credit ratings", RATINGS]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Nunn and Budenberg.", "div": "lbg", "rev": "eic", "products": [
            P("leadership", "Board & executive committee", "Chair Sir Robin Budenberg, CEO Charlie Nunn, CFO William Chalmers; Jas Singh runs Consumer, Nick Williams Connected Finance, Amanda Murphy business banking and John Langley corporate and institutional banking.",
              s=["corp"], neo=[0, ""], src=[["Lloyds: executive committee", EXCO]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & brands", "blurb": "Halifax becomes Lloyds.", "div": "lbg", "rev": "retail", "products": [
            P("brands", "Brands", "Bank of Scotland (1695), Lloyds (1765) and Scottish Widows (1815), with HBOS joined in 2009; Halifax is being retired into Lloyds in England, Wales and Northern Ireland (announced July 2026), while Bank of Scotland stays in Scotland.",
              s=["con"], o="I", st="flux", neo=[0, ""], src=[["Marketing Week: Halifax retired, Jul 2026", HALIFAX]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "£100m+ from AI in 2026.", "div": "lbg", "rev": "eic", "products": [
            P("tech", "Core, cloud & AI", "A new core banking engine, two strategic data centres, Copilot for every colleague and GitHub Copilot for 11,000 engineers, about 50 generative-AI uses worth £50 million in 2025 and more than £100 million targeted in 2026, and a group digital-asset platform.",
              s=["corp"], neo=[0, ""], src=[["Accelerate 2030 presentation", A2030], ["2025 results", FY25]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Accelerate 2030", "blurb": "RoTE c.20% by 2030.", "div": "lbg", "rev": "eic", "products": [
            P("strategy", "Accelerate 2030", "Grow the core, innovate (new wallet and payments products) and simplify: RoTE above 18% in 2028 and about 20% in 2030, cost:income below 45%.",
              s=["corp"], st="new", neo=[0, ""], src=[["Accelerate 2030 presentation", A2030]]),
            P("deals", "Deals", "Curve (completed May 2026, about £120 million ⚠), Schroders Personal Wealth bought in full and renamed Lloyds Wealth (2025), Embark and Tusker earlier.",
              s=["con", "aff"], o="A", neo=[0, ""], src=[["Curve acquisition, Nov 2025", CURVE], ["H1 2026 results", H1]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: Visa debit for 30 million accounts, credit cards moving from Mastercard to Visa, Curve on Mastercard and a new Smart Wallet, card acceptance with Stripe, open-banking payments built with Mastercard, and tokenised deposits and stablecoins.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "Visa for 40 years.", "div": "lloyds", "rev": "retail", "products": [
            P("debit", "Lloyds, Halifax & Bank of Scotland debit", "Debit cards for more than 30 million personal and business accounts, on Visa for about 40 years.",
              s=["con", "sme"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Banking Exchange: Lloyds to Visa, Jun 2024", VISA24]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "10 million moving to Visa.", "div": "mbna", "rev": "retail", "products": [
            P("credit", "Credit cards: Lloyds, Halifax, Bank of Scotland & MBNA", "About 10 million consumer and commercial credit cards moving from Mastercard to Visa by the end of 2026 under a renewed Visa deal (June 2024); £18.2 billion of balances; Lloyds Ultra and Advance launched in 2025.", short="Credit (Mastercard to Visa)",
              s=["con", "sme"], lc="borrow", st="flux", ay="Jun 2024", o="P", at="Visa", neo=[1, "Mastercard until reissued, then Visa."],
              mc="The defining loss: the group's credit book leaves Mastercard by the end of 2026.",
              src=[["Banking Exchange: Lloyds to Visa, Jun 2024", VISA24], ["H1 2026 results", H1]]),
        ]},
        {"id": "2.3", "ic": "wallet", "name": "Curve & Smart Wallet", "blurb": "6 million on Curve.", "div": "curve", "rev": "retail", "products": [
            P("curve", "Curve", "A wallet that puts all of a customer's cards behind one Curve Mastercard, with FX savings, rewards, Pay Later and 'go back in time', for more than 6 million customers in the UK and EEA; Lloyds completed the purchase in May 2026.", short="Curve (Mastercard)",
              s=["con"], lc="everyday", st="new", ay="May 2026", o="A", neo=[2, "Curve is a Mastercard issuer."],
              mc="Mastercard's main way back into the group.",
              src=[["Curve: joining Lloyds", CURVEBLOG], ["H1 2026 results", H1]]),
            P("smartwallet", "Lloyds Smart Wallet", "Launching in the second half of 2026: spending rules, rewinding payments, point-of-sale finance and a document vault ⚠ built on Curve.",
              s=["con"], lc="everyday", st="new", neo=[None, "Network not announced."], src=[["Accelerate 2030 presentation", A2030]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Acceptance", "blurb": "Lloyds Accept with Stripe.", "div": "lloyds", "rev": "commercial", "products": [
            P("accept", "Lloyds Accept & Cardnet", "Tap to Pay and payment links inside the business account, built with Stripe (June 2026), alongside Cardnet merchant acquiring ⚠.",
              s=["sme"], lc="move", st="new", o="P", at="Stripe", neo=[1, "Accepts every network."], src=[["H1 2026 results", H1]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Open-banking payments", "blurb": "PayFrom Bank.", "div": "lloyds", "rev": "commercial", "products": [
            P("payfrom", "PayFrom Bank", "Open-banking checkout for commercial clients built on Mastercard's Open Banking Connect (July 2021), covering 95% of UK accounts ⚠ current status unknown.",
              s=["sme", "corp"], lc="move", ay="Jul 2021", o="P", at="Mastercard", neo=[3, "Mastercard Open Banking ⚠ status."], src=[["Open Banking Expo: PayFrom Bank, Jul 2021", PAYFROM]]),
        ]},
        {"id": "2.6", "ic": "coins", "name": "Digital money", "blurb": "Tokenised deposits, stablecoins.", "div": "lbg", "rev": "commercial", "products": [
            P("digitalmoney", "Tokenised deposits & stablecoins", "Co-chair of the UK tokenised-deposits project, live Project Agorá transactions (July 2026), the UK's first tokenised-gilt purchase, and a seven-day USDC cross-border settlement pilot with Visa (September 2026).",
              s=["corp"], lc="move", st="new", o="P", at="Visa, Archax", neo=[0, "Visa pilot; own tokens."],
              mc="Stablecoin international payments are planned for 2026–27; Visa ran the first pilot.",
              src=[["Lloyds and Visa stablecoin pilot, Sep 2026", STABLE], ["Lloyds: tokenisation survey, Oct 2026", TOKEN]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: fraud models that catch 90% of digital fraud and Mastercard's scam scores, an agentic AI assistant and spending insights, and rewards that join 28 million customers to a million businesses.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & scams", "blurb": "90% caught digitally.", "div": "lbg", "rev": "retail", "products": [
            P("fraud", "Fraud detection", "About 90% of digital fraud value detected and AI-led resolution, against UK payment fraud of £1.28 billion in 2025.",
              s=["con", "sme"], lc="everyday", neo=[0, "Lloyds' own."], src=[["Accelerate 2030 presentation", A2030], ["UK Finance: fraud report 2026", FRAUD]]),
            P("cfr", "Consumer Fraud Risk", "Lloyds Bank, Halifax and Bank of Scotland were among the nine UK launch banks for Mastercard's scam scoring in July 2023 ⚠ current use unconfirmed.",
              s=["con"], lc="everyday", ay="Jul 2023", o="P", at="Mastercard", neo=[3, "Mastercard's own ⚠."], src=[["Fintech Times: Consumer Fraud Risk, Jul 2023", CFR]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI for customers", "blurb": "An agentic assistant.", "div": "lloyds", "rev": "retail", "products": [
            P("assistant", "AI financial assistant & Explore Your Spending", "Billed as the UK's first agentic AI financial assistant (staff pilot November 2025, launch 2026), and spending insights for more than 11 million customers.",
              s=["con"], lc="everyday", st="new", neo=[0, ""],
              mc="Lloyds is hiring for agentic payments; Agent Pay is untouched ground.",
              src=[["FStech: agentic AI assistant, Nov 2025", AGENTIC], ["H1 2026 results", H1]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards", "blurb": "Connected Commerce.", "div": "lloyds", "rev": "retail", "products": [
            P("rewards", "Rewards & Connected Commerce", "Lloyds Rewards (8 million visitors in 2026), Club Lloyds and Premier, and Connected Commerce, merchant cashback linking 28 million retail customers to a million business clients (pilot H2 2026).",
              s=["con", "sme"], lc="grow", st="new", neo=[0, ""],
              mc="Card-linked offers and merchant data could power Connected Commerce.",
              src=[["Accelerate 2030 presentation", A2030]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: the UK's biggest mortgage book and a quarter of current accounts, Lloyds Auto (Black Horse, Lex Autolease, Tusker), business and corporate banking, and Scottish Widows pensions and Lloyds Wealth.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Mortgages & accounts", "blurb": "£325bn, number one.", "div": "lloyds", "rev": "retail", "products": [
            P("mortgages", "Mortgages", "£325 billion, a 19% share and the UK's largest lender, with offers in under three days targeted.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["Accelerate 2030 presentation", A2030]]),
            P("accounts", "Current accounts & loans", "More than 24% of UK current-account balances, 70% of them main-bank relationships, and the leading unsecured-loan book.",
              s=["con"], lc="everyday", neo=[0, "Visa debit."], src=[["Accelerate 2030 presentation", A2030]]),
        ]},
        {"id": "4.2", "ic": "target", "name": "Lloyds Auto", "blurb": "1 in 8 UK EVs.", "div": "auto", "rev": "retail", "products": [
            P("auto", "Lloyds Auto", "Black Horse, Lex Autolease and Tusker under one brand (October 2026): number one in UK vehicle finance and leasing, financing one in eight EVs, with a £1.95 billion motor-finance redress provision.",
              s=["driver"], lc="borrow", st="new", ay="Oct 2026", neo=[0, ""],
              mc="Fleet and fuel cards for the UK's largest leasing fleet are untested ground.",
              src=[["Lloyds Auto launch, Oct 2026", AUTO], ["H1 2026 results", H1]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Business & corporate", "blurb": "A million relationships.", "div": "lbg", "rev": "commercial", "products": [
            P("business", "Business & Commercial Banking", "A million business relationships and a 21% share of small-business deposits.",
              s=["sme"], lc="everyday", neo=[0, "Visa debit; credit moving to Visa."], src=[["Accelerate 2030 presentation", A2030]]),
            P("cib", "Corporate & Institutional Banking", "Infrastructure finance, debt capital markets and transaction banking, income up 70% since 2021 and expanding in the US and Europe.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Accelerate 2030 presentation", A2030]]),
        ]},
        {"id": "4.4", "ic": "coins", "name": "Pensions & wealth", "blurb": "Scottish Widows, Lloyds Wealth.", "div": "widows", "rev": "ipi", "products": [
            P("widows", "Scottish Widows & Lloyds Wealth", "Workplace pensions with £140 billion under administration, a record £1.3 billion of ISA subscriptions, insurance, and Lloyds Wealth (£17 billion).",
              s=["aff"], lc="grow", neo=[0, ""], src=[["H1 2026 results", H1]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: the Lloyds app for 22 million, branches being rebranded, and brokers and dealers.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Lloyds app", "blurb": "22 million users.", "div": "lloyds", "rev": "retail", "products": [
            P("app", "Lloyds app", "About 22 million app users and 7 billion digital log-ons a year; Halifax customers moving onto it.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["H1 2026 results", H1]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches", "blurb": "Halifax becomes Lloyds in 2027.", "div": "halifax", "rev": "retail", "products": [
            P("branches", "Branches & communities", "Branch presence in about 1,000 communities, Halifax branches becoming Lloyds in 2027.",
              s=["con"], lc="everyday", st="flux", neo=[0, ""], src=[["Marketing Week: Halifax retired, Jul 2026", HALIFAX]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Brokers & dealers", "blurb": "Intermediaries, motor dealers.", "div": "lbg", "rev": "retail", "products": [
            P("brokers", "Brokers, dealers & partners", "Mortgage intermediaries (Halifax Intermediaries becomes Lloyds Intermediaries in 2027), motor dealers and manufacturers, and embedded finance in third-party SME tools.",
              s=["home", "driver"], lc="open", neo=[0, ""], src=[["Accelerate 2030 presentation", A2030]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Lloyds", "blurb": "Curve, and a credit book leaving.", "products": [
        P("mcatlloyds", "Mastercard at Lloyds", "Visa has carried Lloyds' debit for about 40 years and, under a June 2024 deal, takes the group's 10 million credit cards from Mastercard by the end of 2026. Mastercard keeps Curve, now owned by Lloyds, PayFrom Bank's open-banking rails and scam scoring from 2023 ⚠; Visa also ran Lloyds' first stablecoin pilot.",
          s=["con"], div="lbg", rev="eic", mc="The relationship this map is drawn for.",
          src=[["Banking Exchange: Lloyds to Visa, Jun 2024", VISA24], ["Curve: joining Lloyds", CURVEBLOG]]),
    ]},
    {"id": "pillar-market", "name": "UK banking", "blurb": "Scams, motor finance, tokens.", "products": [
        P("market", "The UK market", "Mandatory APP-scam reimbursement, the FCA's motor-finance redress scheme (£9.1 billion industry-wide), tokenised deposits and stablecoin pilots, and a possible bank tax at the 28 October Budget ⚠.",
          s=["con"], div="lbg", rev="eic", src=[["UK Finance: fraud report 2026", FRAUD]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
