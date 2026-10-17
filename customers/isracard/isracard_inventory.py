"""Isracard's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are Isracard's own where its site gives them (the About page: 4.8 million active cards, NIS 13.1 billion
of credit at the end of Q2 2026) and otherwise from Globes; 2025 and Q2 2026 results come from third-party summaries
and are marked ⚠. Card networks are read from the card art on Isracard's product pages (17 October 2026).
``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on
Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

ABOUT = "https://www.isracard.co.il/pages/about-isracard/private"
HOME = "https://www.isracard.co.il/"
FLYCARD = "https://www.isracard.co.il/flycard/private"
TOP = "https://www.isracard.co.il/credit-cards/isracardtop"
BASIC = "https://www.isracard.co.il/credit-cards/basic"
WCARD = "https://www.isracard.co.il/credit-cards/w"
SUPERFLY = "https://www.isracard.co.il/credit-cards/superfly"
LIFESTYLE = "https://www.isracard.co.il/credit-cards/lifestyle"
MAMI = "https://www.isracard.co.il/credit-cards/mami"
CASHBACK = "https://www.isracard.co.il/credit-cards/cashbackplus"
LOBBY = "https://www.isracard.co.il/lobby-credit-cards/private"
CORPORATE = "https://www.isracard.co.il/credit-cards/corporate"
PREPAID = "https://www.isracard.co.il/credit-cards/prepaidcard"
CLEARING = "https://www.isracard.co.il/lobby-clearance/business"
LOAN = "https://www.isracard.co.il/loans/non-bank-loan"
SAVING = "https://www.isracard.co.il/investments/saving/private"
G_IPO = "https://en.globes.co.il/en/article-hapoalim-holding-huge-isracard-tase-ipo-today-1001280792"
G_DIV = "https://en.globes.co.il/en/article-hapoalim-to-distribute-isracard-holding-as-dividend-1001317090"
G_DIGITAL = "https://en.globes.co.il/en/article-israels-digital-bank-to-issue-isracard-mastercard-cards-1001329214"
G_LAYOFF = "https://en.globes.co.il/en/article-isracard-to-lay-off-250-1001432061"
G_HAREL = "https://en.globes.co.il/en/article-harel-gives-up-on-acquiring-isracard-1001468947"
G_VOTE = "https://en.globes.co.il/en/article-isracard-shareholders-approve-acquisition-by-delek-1001502791"
G_BOI = "https://en.globes.co.il/en/article-boi-grants-tshuva-permit-to-control-isracard-1001515351"
G_ESH = "https://en.globes.co.il/en/article-isracard-to-buy-digital-bank-esh-1001537843"
G_FLY = "https://en.globes.co.il/en/article-isracard-hijacks-el-al-fly-card-from-icc-cal-1001538579"
G_FLYALL = "https://en.globes.co.il/en/article-el-al-claims-icc-cals-new-flyall-card-is-consumer-fraud-1001545346"
G_ESHOFF = "https://en.globes.co.il/en/article-Isracard-cancels-acquisition-of-Nir-Zuks-Esh-Bank-1001549848"
G_CAL = "https://en.globes.co.il/en/article-cal-sale-likely-to-be-postponed-after-horesh-harel-cancel-deal-1001557413"
BAKSHI = "https://bakshi-finance.co.il/stocks/iscd.en.html"
SWS = "https://www.webull.com/news/15404467647366144"
WIKI = "https://en.wikipedia.org/wiki/Isracard"
MC_AGENT = "https://newsroom.mastercard.com/news/press/2025/april/mastercard-unveils-agent-pay-pioneering-agentic-payments-technology-to-power-commerce-in-the-age-of-ai"
ASSAEL = "https://il.linkedin.com/in/assael"
BOI_R2P = "https://boi.org.il/en/communication-and-publications/press-releases/the-bank-of-israel-is-continuing-to-advance-instant-payments-in-israel-and-has-instructed-participants-to-prepare-for-receiving-payment-requests-r2p-by-the-end-of-2023/"
HAMICHLOL = "https://www.hamichlol.org.il/PAY"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "cards · credit · control", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: 4.8 million active cards and NIS 13.1 billion of credit, a 2025 loss after a one-off provision, control by Delek Group since July 2025, and a franchise that began with Eurocard in 1975.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & results", "blurb": "4.8m cards, NIS 13.1bn credit.", "div": "isracard", "rev": "group", "products": [
            P("scale", "Cards, credit & results", "More than 4.8 million active cards and about NIS 13.1 billion of business and private credit at the end of Q2 2026. 2025 revenue NIS 3.52 billion and a reported net loss of NIS 40 million after a one-off provision of about NIS 345 million ⚠; Q2 2026 net income NIS 80 million on revenue of NIS 871 million ⚠.",
              s=["con", "sme"], neo=[0, ""], src=[["Isracard: About", ABOUT], ["Bakshi Finance: FY2025 summary ⚠", BAKSHI], ["Simply Wall St: Q2 2026 ⚠", SWS]]),
            P("ratings", "Capital & ratings", "CET1 10.7% at end-2025; Moody's Baa1, S&P A, Fitch A and Midroog Aa2.il, all stable (February 2026) ⚠; Maala ESG rating Platinum Plus AA.",
              s=["partner"], neo=[0, ""], src=[["Bakshi Finance: ratings ⚠", BAKSHI], ["Isracard: About", ABOUT]]),
        ]},
        {"id": "1.2", "ic": "building-2", "name": "Ownership & deals", "blurb": "Delek in control since 2025.", "div": "delek", "rev": "group", "products": [
            P("delek", "Delek Group control", "Yitzhak Tshuva's Delek Group won control at a NIS 3.56 billion valuation (shareholder vote February 2025); the Bank of Israel granted the permit on 9 July 2025. Delek paid about NIS 1.3 billion for 37%, reaching about 40% ⚠.",
              s=["partner"], st="new", ay="Jul 2025", o="A", neo=[0, ""], src=[["Globes: BoI permit, Jul 2025", G_BOI], ["Globes: shareholders approve Delek, Feb 2025", G_VOTE]]),
            P("separation", "Separation from Bank Hapoalim", "Floated on the TASE in April 2019 (65.2% for NIS 1.76 billion); Hapoalim distributed its last 33% in March 2020. Harel's 2023 takeover was dropped in January 2024 after the Competition Authority opposed it.",
              s=["partner"], o="I", ay="Apr 2019", neo=[0, ""], src=[["Globes: Hapoalim distributes stake, Feb 2020", G_DIV], ["Globes: IPO, Apr 2019", G_IPO], ["Globes: Harel drops bid, Jan 2024", G_HAREL]]),
            P("esh", "Esh Bank MOU", "A March 2026 MOU to buy digital bank Esh for up to NIS 500 million, to prepare for Israel's lean-bank reform, expired without agreement in July 2026.",
              s=["con"], st="retired", ay="Mar 2026", neo=[0, ""],
              mc="Isracard wants a route into banking; account and open-finance tools would follow it.",
              src=[["Globes: Esh MOU, Mar 2026", G_ESH], ["Globes: Esh cancelled, Jul 2026", G_ESHOFF]]),
        ]},
        {"id": "1.3", "ic": "users-round", "name": "Leadership & people", "blurb": "Furman CEO, Yassur chair.", "div": "isracard", "rev": "group", "products": [
            P("leadership", "Management", "CEO Itamar Furman (named in 2026), chair Tamar Yassur ⚠; predecessors Ran Oz (2022–25) and Ron Wexler (2020).",
              s=["partner"], neo=[0, ""], src=[["Globes: FLY CARD, Mar 2026", G_FLY], ["Globes: shareholders approve Delek, Feb 2025", G_VOTE]]),
            P("people", "Workforce", "About 2,000 staff in late 2022, when 250 jobs (12%) were cut ⚠ no current figure.",
              s=["partner"], neo=[0, ""], src=[["Globes: 250 job cuts, Dec 2022", G_LAYOFF]]),
        ]},
        {"id": "1.4", "ic": "badge-check", "name": "Heritage & licences", "blurb": "Eurocard 1975, Amex 1995.", "div": "europay", "rev": "group", "products": [
            P("heritage", "Heritage", "Began in 1975 when Bank Hapoalim bought Eurocard Israel, now Europay (Eurocard) Israel; won the American Express licence in 1995 and bought out Aminit, its Visa arm ⚠.",
              s=["partner"], o="I", neo=[0, ""], src=[["Wikipedia: Isracard ⚠", WIKI]]),
            P("licences", "Network licences", "Four brands on its cards: Isracard, Mastercard (issued through Europay; agreement renewed 2013 ⚠), Visa under licence, and American Express, exclusive in Israel.",
              s=["partner"], o="I", neo=[1, "Mastercard one of four brands."],
              mc="Mastercard's link runs back to Eurocard; it is the brand on most Isracard credit cards.",
              src=[["Isracard: About", ABOUT], ["Wikipedia: Isracard ⚠", WIKI]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Eight ways money moves: Mastercard on most own-brand cards, Visa on a few, an exclusive American Express licence, El Al's FLY CARD won in 2026, bank-issued cards, acquiring for 100,000 businesses, wallets beside Bit and PayBox, and a first agentic purchase.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Mastercard cards", "blurb": "TOP, BASIC, World Elite.", "div": "europay", "rev": "private", "products": [
            P("top", "Isracard TOP & BASIC", "TOP gives vouchers and discounts at selected chains; BASIC charges no FX fees. Both carry Mastercard.", short="TOP & BASIC (Mastercard)",
              s=["con"], lc="everyday", o="B", at="Mastercard", neo=[2, "Mastercard."], src=[["Isracard: TOP", TOP], ["Isracard: BASIC", BASIC]]),
            P("cashback", "CashBack+ & World Elite", "CashBack+ pays up to 1% back in its first year, managed in the app; World Elite Mastercard adds extended free travel insurance.", short="CashBack+ & World Elite (Mastercard)",
              s=["con", "prem"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Isracard: CashBack+", CASHBACK], ["Isracard: card catalogue", LOBBY]]),
            P("prepaid", "Nateanchik prepaid", "A reloadable prepaid card topped up in the app, usable wherever Mastercard is accepted, with a PIN above NIS 300.", short="Nateanchik (Mastercard)",
              s=["con"], lc="everyday", at="Mastercard", neo=[2, "Mastercard."], src=[["Isracard: Nateanchik", PREPAID]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Visa cards", "blurb": "W and Mami.", "div": "isracard", "rev": "private", "products": [
            P("visa", "W & Mami Card", "The W card and Mami Card (up to 20% back as Mami Money, no card fee, 1% FX) carry Visa; Isracard has issued Visa on a small scale since 2001, mainly for Hapoalim customers ⚠.", short="W & Mami (Visa)",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Isracard: W", WCARD], ["Isracard: Mami", MAMI], ["Wikipedia: Isracard ⚠", WIKI]]),
        ]},
        {"id": "2.3", "ic": "gem", "name": "American Express", "blurb": "Exclusive in Israel.", "div": "amex", "rev": "private", "products": [
            P("amex", "American Express cards", "Platinum, Gold and CashBack Premium (up to NIS 500 a month back), issued by Isracard and Premium Express under the exclusive Israeli licence held since 1995.", short="Amex (exclusive licence)",
              s=["prem"], lc="everyday", o="P", at="American Express", neo=[0, "American Express."], src=[["Isracard: card catalogue", LOBBY], ["Isracard: About", ABOUT]]),
        ]},
        {"id": "2.4", "ic": "plane", "name": "FLY CARD", "blurb": "El Al's club, won from CAL.", "div": "flycard", "rev": "private", "products": [
            P("flycard", "FLY CARD by El Al (Isracard)", "A ten-year deal (March 2026) to run El Al's club cards, taken from ICC CAL; about 3.6 million club members and 500,000 cards; NIS 120–160 million a year of pre-tax profit expected. Premium and Premium Select carry Mastercard; base card network not shown ⚠.", short="FLY CARD (Mastercard tiers)",
              s=["trav", "prem"], lc="everyday", st="new", ay="Mar 2026", o="P", at="El Al", neo=[1, "Premium tiers on Mastercard; Amex tier too."],
              mc="Hundreds of thousands of cards to move by the end of 2026, on Mastercard where Isracard issues them.",
              src=[["Globes: FLY CARD deal, Mar 2026", G_FLY], ["Globes: CAL settlement, Jun 2026", G_FLYALL], ["Isracard: FLY CARD", FLYCARD]]),
            P("flyamex", "FLY CARD American Express Premium", "The club's Amex premium tier (NIS 40 a month, 1 point per NIS 4); Amex stays a strategic partner of the club.",
              s=["prem"], lc="everyday", o="P", at="American Express, El Al", neo=[0, "American Express."], src=[["Isracard: FLY CARD", FLYCARD]]),
        ]},
        {"id": "2.5", "ic": "landmark", "name": "Bank & partner issuing", "blurb": "Hapoalim, digital bank.", "div": "isracard", "rev": "private", "products": [
            P("bankcards", "Bank cards", "Cards issued with banks for their account holders; a November 2022 operating agreement raised Hapoalim's share of income by about NIS 50 million a quarter for eight years. Network varies by card ⚠.",
              s=["con", "partner"], lc="everyday", o="P", at="Bank Hapoalim", neo=[1, "Mastercard and Visa ⚠."], src=[["Globes: Hapoalim agreement, Dec 2022", G_LAYOFF], ["Isracard: FLY CARD", FLYCARD]]),
            P("digitalbank", "First Digital Bank cards", "May 2020 agreement for Isracard to issue and manage the new digital bank's cards under Mastercard ⚠ current status.",
              s=["partner"], lc="open", ay="May 2020", o="P", at="First Digital Bank", neo=[2, "Mastercard."], src=[["Globes: digital bank, May 2020", G_DIGITAL]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Acquiring", "blurb": "100,000+ businesses.", "div": "isracard", "rev": "business", "products": [
            P("acquiring", "Isracard acquiring", "Clears Isracard, Mastercard, Visa, American Express and JCB ⚠ for more than 100,000 SMEs; 2.9–3.25% for cards issued abroad and an Amex surcharge of 0.4–0.7%; payment links and AI-built-site integration.",
              s=["sme"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["Isracard: acquiring", CLEARING], ["Isracard: About", ABOUT]]),
            P("bizaccount", "Business payment account", "A payment account for the self-employed with card and bank-transfer collection, digital invoices and a non-bank credit line: 0.95% acquiring and no fees for 24 months for joiners to 31 December 2026.",
              s=["sme"], lc="open", st="new", o="B", neo=[0, ""], src=[["Isracard: acquiring", CLEARING]]),
        ]},
        {"id": "2.7", "ic": "zap", "name": "Wallets & instant", "blurb": "Apple Pay beside Bit.", "div": "isracard", "rev": "private", "products": [
            P("wallets", "Apple Pay, Google Pay & payment ring", "Cards in Apple Pay and Google Pay, a payment ring and in-app wallet payment; network tokens follow the card's brand ⚠.",
              s=["con"], lc="move", o="P", at="Apple, Google", neo=[1, "Tokens on each card's network ⚠."], src=[["Isracard: home page", HOME]]),
            P("a2a", "Bit, PayBox & instant payments", "Bank-run apps lead person-to-person payments (Bit about 80% in 2022, PayBox 1.6 million users in 2021) ⚠, and the Bank of Israel has pushed instant payments and request-to-pay since 2020 ⚠. Isracard excludes bit and PayBox transfers from FLY CARD offers.",
              s=["con"], lc="move", neo=[0, "Bank rails."], src=[["Hamichlol: payment apps ⚠", HAMICHLOL], ["Bank of Israel: instant payments ⚠", BOI_R2P], ["Isracard: FLY CARD", FLYCARD]]),
        ]},
        {"id": "2.8", "ic": "bot", "name": "Agentic payments", "blurb": "A first Agent Pay purchase.", "div": "isracard", "rev": "private", "products": [
            P("agentpay", "Agent Pay purchase", "A purchase made entirely by an AI agent through PayOS on Mastercard Agent Pay, with passkeys and agentic tokens, reported as Israel's first with Bank Hapoalim and Isracard ⚠ undated, unconfirmed by either.",
              s=["con"], lc="move", st="unconf", o="P", at="Mastercard, PayOS", neo=[3, "Mastercard Agent Pay ⚠."],
              mc="The opening for Agent Pay at scale in Israel.",
              src=[["LinkedIn: Israel's first agentic purchase ⚠", ASSAEL], ["Mastercard: Agent Pay, Apr 2025", MC_AGENT]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every card: self-service blocking and disputes, data-led credit and services to other issuers, dozens of clubs and benefit sites, and service through WhatsApp, phone and the app.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & disputes", "blurb": "Block, dispute, chargeback.", "div": "isracard", "rev": "private", "products": [
            P("fraud", "Card controls & disputes", "Online blocking and unblocking, transaction disputes and chargebacks through the acquirer, and PINs on larger prepaid purchases. No public fraud-scoring programme ⚠.",
              s=["con", "sme"], lc="everyday", o="B", neo=[None, "Nothing public."], src=[["Isracard: home page", HOME], ["Isracard: acquiring", CLEARING]]),
        ]},
        {"id": "3.2", "ic": "brain", "name": "Data & issuer services", "blurb": "Credit on data.", "div": "isracard", "rev": "group", "products": [
            P("data", "Data, credit models & issuer services", "Credit offered through a digital platform with marketing and data-analysis capabilities, and services to other issuers ⚠ details not public.",
              s=["partner"], lc="borrow", o="B", neo=[0, ""], src=[["Isracard: About", ABOUT]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Clubs & benefits", "blurb": "Dozens of clubs.", "div": "isracard", "rev": "private", "products": [
            P("clubs", "Consumer clubs", "Runs dozens of Israel's largest consumer clubs, from FLY CARD to Hot and Tov, with card-linked discounts.",
              s=["con", "partner"], lc="beyond", o="P", neo=[1, "Club cards mostly Mastercard ⚠."],
              mc="Card-linked offers and benefits eligibility fit the club model.",
              src=[["Isracard: About", ABOUT], ["Isracard: card catalogue", LOBBY]]),
            P("benefits", "Benefits, TopCash & Time-Off", "A benefits site (cinema, attractions, lounges), Isracard Fun, TopCash online cashback and Time-Off travel deals.",
              s=["con", "trav"], lc="beyond", o="B", neo=[0, ""], src=[["Isracard: home page", HOME]]),
            P("igul", "Igul LeTova", "Round-up giving: purchases are rounded up and the change goes to charity.",
              s=["con"], lc="beyond", o="P", neo=[0, ""], src=[["Isracard: home page", HOME]]),
        ]},
        {"id": "3.4", "ic": "headset", "name": "Service", "blurb": "WhatsApp, phone, app.", "div": "isracard", "rev": "private", "products": [
            P("service", "Customer service", "Service through WhatsApp, the *6272 phone line and the app, with self-service for card replacement, charge dates and credit limits.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["Isracard: home page", HOME]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: non-bank loans and revolving credit, credit and purchasing cards for businesses, employer and affinity cards, insurance and savings, and co-brand cards with Rami Levy and Super-Pharm.",
    "tiles": [
        {"id": "4.1", "ic": "hand-coins", "name": "Consumer credit", "blurb": "Loans for any bank's customers.", "div": "finance", "rev": "private", "products": [
            P("loans", "Non-bank loans", "Loans from Isracard Finance for card-holding customers of any bank aged 21 and over, money next day, 0.5% off the rate online and up to three months' grace.",
              s=["con"], lc="borrow", o="B", neo=[0, ""], src=[["Isracard: non-bank loan", LOAN]]),
            P("revolving", "Revolving & instalment credit", "Revolving credit, instant credit, a fixed monthly payment and spreading of charges on the card.",
              s=["con"], lc="borrow", o="B", neo=[1, "Rides on the card's network."], src=[["Isracard: home page", HOME]]),
        ]},
        {"id": "4.2", "ic": "briefcase-business", "name": "Business finance & cards", "blurb": "Purchasing and B2B cards.", "div": "isracard", "rev": "business", "products": [
            P("bizfinance", "Business credit", "Finance for SMEs alongside acquiring: cash-flow management, discounting of card receipts and vouchers, and insured credit.",
              s=["sme"], lc="borrow", o="B", neo=[0, ""], src=[["Isracard: acquiring", CLEARING]]),
            P("b2b", "Purchasing, B2B & business cards", "Isracard and American Express purchasing cards, a B2B card, a business credit card, a business FLY CARD and gift cards ⚠ networks not stated.",
              s=["sme", "corp"], lc="move", o="B", neo=[None, "Networks not stated."],
              mc="Commercial cards with spend controls are open ground.",
              src=[["Isracard: acquiring", CLEARING]]),
        ]},
        {"id": "4.3", "ic": "building", "name": "Employer & affinity cards", "blurb": "Corporate club.", "div": "isracard", "rev": "private", "products": [
            P("corporate", "Corporate club card", "An employee-benefit card with no card fee, 0% FX and a MyCorporate benefits site; employees choose Mastercard, Visa or American Express.",
              s=["corp", "con"], lc="everyday", o="P", neo=[1, "Mastercard, Visa or Amex."], src=[["Isracard: Corporate", CORPORATE]]),
            P("affinity", "Organisation & community cards", "Eleven cards for organisations and communities (such as Amdocs, Mezer, Meshekard) and four for the Haredi sector ⚠ networks vary.",
              s=["con"], lc="everyday", o="P", neo=[None, "Networks vary."], src=[["Isracard: card catalogue", LOBBY]]),
        ]},
        {"id": "4.4", "ic": "trending-up", "name": "Insurance & savings", "blurb": "Agency and BEST INVEST.", "div": "insurance", "rev": "private", "products": [
            P("insurance", "Isracard Insurance Agency", "Car, travel, flight-cancellation and pet insurance through Isracard Insurance Agency (2020).",
              s=["con", "trav"], lc="grow", o="B", neo=[0, ""], src=[["Isracard: Corporate", CORPORATE], ["Isracard: home page", HOME]]),
            P("saving", "BEST INVEST savings", "A savings policy from Hachshara Insurance with six investment managers, sold to Isracard customers from NIS 180 a month.",
              s=["con"], lc="grow", o="P", at="Hachshara Insurance", neo=[0, ""], src=[["Isracard: savings", SAVING]]),
        ]},
        {"id": "4.5", "ic": "store", "name": "Retail co-brands", "blurb": "Rami Levy, Super-Pharm.", "div": "isracard", "rev": "private", "products": [
            P("superfly", "Superfly (Rami Levy)", "Superfly and Superfly Premium co-brand cards with the Rami Levy chain, on Mastercard.", short="Superfly (Mastercard)",
              s=["con"], lc="everyday", o="P", at="Rami Levy", neo=[2, "Mastercard."], src=[["Isracard: Superfly", SUPERFLY]]),
            P("lifestyle", "LifeStyle (Super-Pharm)", "LifeStyle Gold with exclusive Super-Pharm discounts, up to NIS 500 joining gift and 0% FX, on Mastercard.", short="LifeStyle (Mastercard)",
              s=["con"], lc="everyday", o="P", at="Super-Pharm", neo=[2, "Mastercard."], src=[["Isracard: LifeStyle", LIFESTYLE]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Isracard: the app and website, bank branches for bank cards, and the business site for merchants.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "App & website", "blurb": "Cards, cashback, top-ups.", "div": "isracard", "rev": "private", "products": [
            P("app", "Isracard app & personal area", "Card management, CashBack balances, prepaid top-ups, digital card issuance and loan applications in the app and website.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["Isracard: home page", HOME], ["Isracard: Nateanchik", PREPAID]]),
        ]},
        {"id": "5.2", "ic": "landmark", "name": "Bank branches", "blurb": "Bank cards through banks.", "div": "isracard", "rev": "private", "products": [
            P("branches", "Bank branches", "Bank-account cards, including American Express and soon FLY CARD Premium bank cards, are ordered at the customer's bank branch.",
              s=["con", "partner"], lc="open", o="P", neo=[1, "Bank cards on several networks ⚠."], src=[["Isracard: FLY CARD", FLYCARD]]),
        ]},
        {"id": "5.3", "ic": "briefcase", "name": "Business site", "blurb": "For merchants.", "div": "isracard", "rev": "business", "products": [
            P("bizportal", "Isracard for business", "The business site for acquiring, the payment account, reports and business cards.",
              s=["sme"], lc="open", o="B", neo=[0, ""], src=[["Isracard: acquiring", CLEARING]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Isracard", "blurb": "The brand on most own cards.", "products": [
        P("mcatisracard", "Mastercard at Isracard", "Mastercard carries most of Isracard's own and co-brand credit cards (TOP, BASIC, CashBack+, World Elite, LifeStyle, Superfly, FLY CARD Premium tiers) and the Nateanchik prepaid card, a link dating from Eurocard in 1975. Visa carries W and Mami; American Express is licensed exclusively to Isracard. A first Agent Pay purchase is reported ⚠.",
          s=["con"], div="isracard", rev="group", mc="The relationship this map is drawn for.",
          src=[["Isracard: About", ABOUT], ["Isracard: FLY CARD", FLYCARD], ["Isracard: TOP", TOP]]),
    ]},
    {"id": "pillar-market", "name": "Israeli cards", "blurb": "Three groups, club wars.", "products": [
        P("market", "The Israeli market", "Three card groups after the Strum law: Isracard (Delek), Max (Clal) and CAL (Discount, its sale collapsed in September 2026). Isracard had about 47% of the market in 2020 ⚠; Bit and PayBox lead mobile transfers ⚠.",
          s=["con"], div="isracard", rev="group", src=[["Globes: CAL sale, Sep 2026", G_CAL], ["Globes: Hapoalim distributes stake, Feb 2020", G_DIV]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
