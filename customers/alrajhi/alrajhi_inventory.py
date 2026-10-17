"""Al Rajhi Bank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the H1 2026 earnings release (21 July 2026), the
2Q 2026 investor presentation and call, the 2025 results (27 January 2026) and the Integrated Annual Report
2025. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides
wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

IRB = "https://www.alrajhibank.com.sa/-/media/Project/AlRajhi/ARBRevamp/Investor-Relation/Financial-Materials"
H1 = f"{IRB}/2026/Q2/ARB-2Q2026-Earnings-Release.pdf"
PRES = f"{IRB}/2026/Q2/ARB-Investor-Presentation-2Q2026.pdf"
CALL = f"{IRB}/2026/Q2/2Q-2026-Earnings-Call-Transcript.pdf"
FY25 = f"{IRB}/2025/ARB-4Q2025-Earnings-Release.pdf"
CALL4Q = f"{IRB}/2025/Q4/4Q-2025-Earnings-Call-Transcript---final.pdf"
IR25 = "https://www.alrajhibank.com.sa/ir25"
ABOUT = f"{IR25}/overview/this_is_alrajhi_bank.html"
DRIVERS = f"{IR25}/overview/value_drivers_2025.html"
EXCO = f"{IR25}/corporate_governance/executive_management.html"
SUBCEO = f"{IR25}/corporate_governance/chief_executive_officers_of_subsidiaries_and_international_network.html"
RETAIL = f"{IR25}/business_in_perspective/business_portfolio_review/retail_banking_group.html"
SHARED = f"{IR25}/business_in_perspective/shared_services_group.html"
DIGITAL = f"{IR25}/customer_engagement_and_responsible_banking/digitalisation_and_automation.html"
INNOV = f"{IR25}/customer_engagement_and_responsible_banking/innovation_and_product_development.html"
NEOLEAP = f"{IR25}/business_in_perspective/subsidiaries/neoleap.html"
EMKAN = f"{IR25}/business_in_perspective/subsidiaries/emkan_finance.html"
DRAHIM = f"{IR25}/business_in_perspective/subsidiaries/drahim.html"
CAPITAL = f"{IR25}/business_in_perspective/subsidiaries/alrajhi_capital.html"
CORP = f"{IR25}/business_in_perspective/business_portfolio_review/corporate_banking_group.html"
MSME = f"{IR25}/business_in_perspective/business_portfolio_review/msme_business.html"
STRAT = f"{IR25}/context/strategic_direction.html"
WEB = "https://www.alrajhibank.com.sa/en"
CURRENT = f"{WEB}/Personal/Accounts/Current-Account"
HOME = f"{WEB}/personal"
RING = f"{WEB}/Personal/Cards/Ring/Ring"
INFINITE = f"{WEB}/Personal/Cards/Credit-Cards/Infinite-Credit-Card"
CHARGE = f"{WEB}/Personal/Cards/Charge-Credit-Card/Infinite-Charge-Credit-Card"
CASHBACK = f"{WEB}/Personal/Cards/Cashback-Cards/Signature-Cashback-Plus-Card"
FURSAN = f"{WEB}/Personal/Cards/Miles-Card/AlFursan-infinite-credit-card"
FLYNAS = f"{WEB}/Personal/Cards/Miles-Card/Flynas-signature-credit-card"
MARRIOTT = f"{WEB}/Personal/Cards/Credit-Cards/Marriott-Bonvoy"
MARRIOTTNEWS = "https://intellinews.com/al-rajhi-bank-launches-marriott-bonvoy-credit-card-in-saudi-arabia-359146"
TRAVEL = f"{WEB}/Personal/Cards/Prepaid-Cards/Travel-Plus-Card"
GAMERS = f"{WEB}/Personal/Cards/Prepaid-Cards/Gamers-Card"
BIZSIG = f"{WEB}/Business/Cards/Business-Cards/Business-Signature-Credit-Card"
BIZDEBIT = f"{WEB}/Business/Cards/Business-Cards/Business-Debit-Card"
PURCH = f"{WEB}/Business/Cards/Corporate-Cards/Corporate-Purchasing-Card"
POS = f"{WEB}/Business/Cash-Management/POS"
ECOM = f"{WEB}/Business/Cash-Management/E-Commerce"
MADAPAY = f"{WEB}/Personal/Cards/Mada-Pay"
BNPL = f"{WEB}/Personal/Finance/Personal-Finance/Buy-Now-Pay-Later"
VISADIRECT = f"{WEB}/About-alrajhi-bank/Media-Center/2025/Visa-and-alrajhi-bank"
MOVE = f"{WEB}/About-alrajhi-bank/Media-Center/2024/urpay"
AFC = "https://www.alrajhibank.com.sa/About-alrajhi-bank/Media-Center/2026/alrajhi-bank-Sports-Presence-Partnership-with-the-AFC-Asian-with-Visa"
MONEY2020 = f"{WEB}/About-alrajhi-bank/Media-Center/2026/alrajhi-bank-Participates-as-a-Founding-Partner-of-Money2020"
KANTAR = f"{WEB}/About-alrajhi-bank/Media-Center/2026/Kantar-BrandZ"
ZID = "https://www.alrajhibank.com.sa/About-alrajhi-bank/Media-Center/2024/ZID"
AMEX = "https://intlbm.com/2024/01/02/american-express-saudi-arabia-partners-with-alrajhi-bank/"
URPAYAPP = "https://apps.apple.com/app/id1585778338"
MALAYSIA = "https://www.therakyatpost.com/living/2026/07/15/new-alrajhi-bank-visa-cards-are-built-around-how-malaysians-actually-spend/"
JORDAN = "https://alrajhibank.com.jo/en/visa-infinite-3"
SAMA = "https://sama.gov.sa/en-US/MediaCenter/News/Pages/news-1139.aspx"
SARIEPRESS = "https://www.arabnews.com/node/2648051"
MCMADA = "https://www.mastercard.com/news/eemea/en/newsroom/press-releases/en/2019/february/mastercard-and-mada-team-up-to-offer-apple-pay-in-the-kingdom"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · Shariah · ecosystem", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: the world's largest Islamic bank, SAR 1,055 billion of assets and a 23% return on equity, an exchange house from 1957, a cloud-ready core, and the Harmonize the Group strategy in its final year.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "SAR 1.06 trillion, ROE 23%.", "div": "arb", "rev": "other", "products": [
            P("balance", "Balance sheet & earnings", "Net income after zakat of SAR 13.8 billion in H1 2026, up 14%, and a record SAR 24.8 billion in 2025; assets of SAR 1,055 billion, financing SAR 762 billion and deposits SAR 688 billion at 30 June 2026; ROE 23.3%, cost to income 22.7%, total capital 23.5%.",
              s=["con"], neo=[0, ""], src=[["H1 2026 earnings release", H1], ["2025 earnings release", FY25]]),
            P("listing", "Listing, ratings & brand", "Listed on Tadawul (1120); market value SAR 395 billion at 30 June 2026, 39% of the sector's; rated Aa3/A/A by Moody's, S&P and Fitch; the Kingdom's most valuable brand at about USD 20.3 billion (Kantar BrandZ, September 2026).",
              s=["corp"], neo=[0, ""], src=[["2Q 2026 investor presentation", PRES], ["Kantar BrandZ, Sep 2026", KANTAR]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Al Rajhi and Al-Mogbel.", "div": "arb", "rev": "other", "products": [
            P("leadership", "Board & executive management", "Chairman Abdullah bin Sulaiman Al Rajhi, Managing Director and CEO Waleed Al-Mogbel, CFO Abdulrahman Al-Fadda, retail head Majed Al-Rajhi, corporate head Hussein Bayari and Chief Digital Officer Abdullah Al-Furaiji; neoleap is run by Abdullah Alibrahim.",
              s=["corp"], neo=[0, ""], src=[["Annual report 2025: executive management", EXCO], ["Annual report 2025: subsidiary CEOs", SUBCEO]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & Islamic model", "blurb": "Since 1957, fully Islamic.", "div": "bank", "rev": "other", "products": [
            P("heritage", "Heritage & Shariah model", "An exchange house from 1957, a bank since 1988 and Al Rajhi Bank since 2006; 100% Shariah-compliant, with Murabaha-based cards and finance; about 22 million customers and more than 25,000 staff, 98% of them Saudi.",
              s=["con"], o="I", neo=[0, ""], src=[["Annual report 2025: this is alrajhi bank", ABOUT], ["Annual report 2025: value drivers", DRIVERS]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & cloud", "blurb": "100% cloud-ready.", "div": "arb", "rev": "other", "products": [
            P("tech", "DigiCore, cloud & APIs", "A new core (DigiCore) carrying personal finance, auto lease, cards and mortgages, with 2.5 million contracts on it; every application cloud-ready by mid-2026; the first GPU environment for AI; group and open-banking APIs up from 218 to 409 in 2025; 1.2 billion transactions a month.",
              s=["corp"], neo=[0, ""], src=[["Annual report 2025: shared services", SHARED], ["2Q 2026 call", CALL]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "Harmonize the Group.", "div": "arb", "rev": "other", "products": [
            P("strategy", "Harmonize the Group", "The 2024–26 strategy joins the bank and eight subsidiaries: cross-sell (44% of customers hold two or more products), main bank for corporates, SME growth, automation and data; a new strategy goes to the Board by the end of 2026.",
              s=["corp"], st="flux", neo=[0, ""], src=[["2Q 2026 call", CALL], ["4Q 2025 call", CALL4Q]]),
            P("deals", "Subsidiaries & deals", "neoleap for payments (2021), Ejada bought in full (2022), neotek for open banking and 65% of Drahim (2024), a SAR 10 billion mortgage originate-to-distribute deal (2025) and a USD 1 billion AT1 sustainable sukuk (January 2026).",
              s=["corp"], o="A", neo=[0, ""], src=[["Annual report 2025: this is alrajhi bank", ABOUT], ["Annual report 2025: value drivers", DRIVERS]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: mada debit on every account, a Visa Islamic card range with 38% of the Kingdom's credit cards, business cards, almost a million POS terminals, sarie instant payments, the region's biggest remittance network, and the urpay wallet.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit & prepaid", "blurb": "mada on every account.", "div": "bank", "rev": "retail", "products": [
            P("madadebit", "mada debit card", "Every current account comes with a mada debit card, contactless through mada Atheer, for POS, ATMs and online on the Saudi Payments Network; fees apply outside mada.", short="mada debit",
              s=["con", "expat"], lc="everyday", o="P", at="Saudi Payments (mada)", neo=[0, "mada."], src=[["Al Rajhi: current account", CURRENT]]),
            P("wearables", "alrajhi bank Ring & SWAR Pro", "A payment ring and a bracelet linked to the customer's mada account, with an annual fee of SAR 150 for the ring.",
              s=["con"], lc="everyday", st="new", neo=[0, "mada."], src=[["Al Rajhi: Ring", RING]]),
            P("premiumdebit", "Signature & Infinite debit", "Premium debit cards for affluent (Signature) and private banking (Mada Infinite) customers, carrying mada with Visa ⚠.",
              s=["aff"], lc="everyday", o="P", at="Visa, mada", neo=[0, "Visa and mada ⚠."], src=[["Al Rajhi: personal banking", HOME]]),
            P("prepaid", "Prepaid cards", "Travel Plus multi-currency card, Digital Cashback (0.6% at home, 1% abroad), Gamers card (2024, 10% gaming cashback), Lite and Tasawaq cards; Visa Checkout online, Gamers and Lite network not stated ⚠.",
              s=["con", "expat"], lc="move", o="P", at="Visa", neo=[0, "Visa."], src=[["Al Rajhi: Travel Plus card", TRAVEL], ["Al Rajhi: Gamers card", GAMERS]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Islamic credit cards", "blurb": "38% share, all Visa.", "div": "bank", "rev": "retail", "products": [
            P("credit", "Platinum, Signature, SELECTIVE & Infinite credit", "Murabaha-based, Shariah-compliant credit cards with Visa Airport Companion lounges (1,200+ for Infinite), Visa Luxury Hotel Collection and Visa travel insurance; Al Rajhi's credit-card market share rose from 35.4% in 2024 to 38.4% in 2025 and card spend is up 84% since 2023.", short="Credit cards (Visa)",
              s=["con", "aff"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."],
              mc="The Kingdom's largest credit-card franchise is single-network Visa.",
              src=[["Al Rajhi: Infinite credit card", INFINITE], ["Annual report 2025: retail banking", RETAIL]]),
            P("charge", "Charge cards", "Classic, Platinum and Infinite charge cards with a 0% monthly profit margin, settled in full each month.",
              s=["con", "aff"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Al Rajhi: Infinite charge card", CHARGE]]),
            P("cobrand", "Co-brand cards: AlFursan, flynas & Marriott Bonvoy", "AlFursan Platinum and Infinite with Saudia, flynas Signature with nasmiles, and a Marriott Bonvoy Visa Infinite card launched in December 2024 with automatic Gold Elite status.",
              s=["aff"], lc="borrow", ay="Dec 2024", o="P", at="Saudia, flynas, Marriott, Visa", neo=[0, "Visa."],
              src=[["Al Rajhi: AlFursan Infinite", FURSAN], ["Al Rajhi: flynas Signature", FLYNAS], ["bne IntelliNews: Marriott Bonvoy card, Dec 2024", MARRIOTTNEWS]]),
            P("cashback", "Cashback Plus cards", "Platinum and Signature Cashback Plus cards, with up to 15% back on HungerStation and 10% on other food-delivery apps.",
              s=["con"], lc="everyday", o="P", at="Visa, HungerStation", neo=[0, "Visa."], src=[["Al Rajhi: Signature Cashback Plus", CASHBACK]]),
        ]},
        {"id": "2.3", "ic": "briefcase-business", "name": "Business & corporate cards", "blurb": "Visa for firms.", "div": "bank", "rev": "corporate", "products": [
            P("bizcards", "Business debit & credit cards", "Business Debit (with mada), Business Platinum and Signature credit cards with 1–3% cashback on digital ads, travel and marketplaces, Visa Signature purchase protection and Visa Golf.",
              s=["sme"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Al Rajhi: Business Signature card", BIZSIG], ["Al Rajhi: Business Debit card", BIZDEBIT]]),
            P("corpcards", "Corporate cards", "Travel & Expense Platinum and Signature cards, a purchasing card, a Corporate Prepaid Mada-Visa card and a virtual Corporate Travel Account; the purchasing card's network is not stated ⚠.",
              s=["corp"], lc="move", o="P", at="Visa", neo=[0, "Visa ⚠."],
              mc="Commercial cards for a 47%-growing SME book are open ground.",
              src=[["Al Rajhi: Corporate purchasing card", PURCH]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Acquiring & gateways", "blurb": "43.5% of POS terminals.", "div": "neoleap", "rev": "corporate", "products": [
            P("pos", "POS acquiring", "Nearly one million POS terminals and 43.5% of the Kingdom's physical terminals, licensed by mada, Visa and Mastercard and accepting mada, Visa, Mastercard and Apple Pay; Amex is accepted under an earlier agreement.", short="POS (all networks)",
              s=["sme"], lc="move", o="B", neo=[1, "Accepts Mastercard alongside mada, Visa and Amex."],
              src=[["Al Rajhi: POS", POS], ["Annual report 2025: MSME", MSME], ["International Banker: Amex, Jan 2024", AMEX]]),
            P("ecom", "E-commerce acquiring & MPGS", "Online acceptance of mada, Visa, Mastercard and UnionPay, with merchants able to plug into four gateways: neoleap's own, Mastercard Payment Gateway Services, Cybersource and Moyasar.", short="E-commerce (MPGS one of four)",
              s=["sme"], lc="move", o="P", at="Mastercard, Cybersource, Moyasar", neo=[1, "MPGS is one of four gateways."],
              mc="Mastercard's gateway already sits in the bank's merchant offer.",
              src=[["Al Rajhi: e-commerce", ECOM]]),
            P("neoleappay", "neoleap merchant services", "neoleap's POS devices hold a 36.6% share, its gateway 29.7% by value; Tashaeel instalments on the terminal, mokafaa as a payment method, Pay-by-Link, and the payments bundle for the Qiddiya giga-project.",
              s=["sme"], lc="move", st="new", o="B", neo=[1, "Accepts every network ⚠."], src=[["Annual report 2025: neoleap", NEOLEAP]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Instant payments", "blurb": "sarie: 22.6m a month.", "div": "bank", "rev": "retail", "products": [
            P("sarie", "sarie instant transfers", "22.6 million instant payments a month through the bank in 2025, on the national sarie rail; nationally about 784 million in 2025, up 32% ⚠.", short="sarie",
              s=["con", "sme"], lc="move", o="P", at="Saudi Payments (sarie)", neo=[0, "sarie."],
              mc="Account-to-account rails compete with cards for everyday payments.",
              src=[["Annual report 2025: shared services", SHARED], ["Arab News: cashless economy", SARIEPRESS]]),
            P("sadad", "SADAD bill payments", "Bill payments through SADAD, up 20% by value through Al Rajhi in 2025; e-payments reached 85% of the Kingdom's retail payments in 2025.",
              s=["con"], lc="everyday", o="P", at="SADAD", neo=[0, ""], src=[["Annual report 2025: digitalisation", DIGITAL], ["SAMA: e-payments 85%, Apr 2026", SAMA]]),
        ]},
        {"id": "2.6", "ic": "send", "name": "Remittances", "blurb": "Number one in the region.", "div": "bank", "rev": "retail", "products": [
            P("tahweel", "Tahweel Al Rajhi", "The Middle East's largest remittance bank by value, through 135 remittance centres and the app; 1.1 million expatriate customers added in 2025 through remittance-led campaigns.",
              s=["expat"], lc="move", o="B", neo=[0, ""], src=[["2Q 2026 investor presentation", PRES], ["Annual report 2025: retail banking", RETAIL]]),
            P("visadirect", "Visa Direct transfers", "Near real-time transfers to Visa cards since 2023, widened by a multi-year deal (dated January 2025 ⚠) to bank accounts in more than 30 countries, including India, Pakistan and Egypt.", short="Visa Direct",
              s=["expat"], lc="move", o="P", at="Visa", neo=[0, "Visa."], src=[["Al Rajhi: Visa partnership", VISADIRECT]]),
            P("move", "urpay on Mastercard Move", "Signed in June 2024 by neoleap's Abdullah Alibrahim and Mastercard's Adam Jones: cash pick-up, bank deposits and wallet transfers to more than 180 countries from the urpay wallet.", short="Mastercard Move (urpay)",
              s=["expat"], lc="move", ay="Jun 2024", o="P", at="Mastercard", div="neoleap", neo=[3, "Mastercard Move."],
              mc="Mastercard's one named partnership in the group.",
              src=[["Al Rajhi: urpay and Mastercard Move, Jun 2024", MOVE]]),
        ]},
        {"id": "2.7", "ic": "smartphone", "name": "urpay & wallets", "blurb": "8m+ urpay users.", "div": "neoleap", "rev": "retail", "products": [
            P("urpay", "urpay wallet", "neoleap's wallet with more than 8 million users at end-2025: transfers (Mastercard Move, Western Union, MoneyGram, Transfast), Musaned household salaries, SADAD bills, a marketplace and a planned visitor wallet.",
              s=["expat", "con"], lc="move", o="B", neo=[1, "Mastercard Move for transfers."], src=[["Annual report 2025: neoleap", NEOLEAP]]),
            P("urpaycards", "urpay cards", "Cards issued in the wallet, second in the market for card services in 2025, with cashback and premium tiers; issued as Visa and mada ⚠.",
              s=["expat", "con"], lc="everyday", o="P", at="Visa ⚠", neo=[0, "Visa ⚠."],
              mc="An open card programme for a fast-growing wallet.",
              src=[["Annual report 2025: neoleap", NEOLEAP], ["urpay app listing", URPAYAPP]]),
            P("wallets", "Apple Pay, Google Pay, Samsung Pay & mada Pay", "Every Al Rajhi debit, credit and prepaid card can be added to the phone wallets and to mada Pay; Mastercard and mada brought Apple Pay to the Kingdom in 2019, but which token service carries Al Rajhi's cards is not public ⚠.",
              s=["con"], lc="everyday", o="P", at="Apple, Google, Samsung, Saudi Payments", neo=[None, "Token service not public ⚠."],
              src=[["Al Rajhi: mada Pay", MADAPAY], ["Mastercard: mada and Apple Pay, Feb 2019", MCMADA]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: fraud controls, a real-time engine that has sold six million contracts, Drahim and neotek for data and open banking, mokafaa points, and 0% Tasaheal instalments.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "SAS and global limits.", "div": "bank", "rev": "other", "products": [
            P("fraud", "Fraud & security", "A group fraud-management system on SAS, extended to the eBusiness portal, a global limit for critical transactions, AI-based KYC for digital onboarding and ISO 27001 certification; fraudulent cases fell 'significantly' in 2025.",
              s=["con", "sme"], lc="everyday", o="B", neo=[0, "Al Rajhi's own."],
              mc="22.6 million instant payments a month need scam and account-to-account risk scoring.",
              src=[["Annual report 2025: shared services", SHARED], ["Annual report 2025: retail banking", RETAIL]]),
        ]},
        {"id": "3.2", "ic": "brain", "name": "Data, AI & open banking", "blurb": "6m contracts from real-time offers.", "div": "neotek", "rev": "other", "products": [
            P("ai", "Real-time engine & AI", "360-degree customer profiles and a real-time event engine that fires offers, such as limit increases and merchant rewards, at the moment of need: over 6 million contracts and SAR 20 billion of revenue attributed; data-driven marketing revenue up 570% since 2023.",
              s=["con"], lc="grow", o="B", div="bank", neo=[0, ""],
              mc="Spend insights and enrichment could feed the engine.",
              src=[["Annual report 2025: innovation", INNOV], ["2Q 2026 call", CALL]]),
            P("drahim", "Drahim", "A personal-finance and robo-investment app, 65% owned since 2024, whose engine categorised 9.5 billion transactions in 2025.",
              s=["con"], lc="grow", o="A", neo=[0, ""], src=[["Annual report 2025: Drahim", DRAHIM]]),
            P("neotek", "neotek open banking", "The group's open-banking and Banking-as-a-Service provider, holding the Kingdom's first final Open Banking licence from SAMA (2026); the bank runs 59 open-banking information services.",
              s=["sme", "corp"], lc="open", st="new", o="B", neo=[0, ""],
              mc="Open-finance services could sit alongside the first licensed provider.",
              src=[["Al Rajhi: Money20/20, Sep 2026", MONEY2020], ["Annual report 2025: shared services", SHARED]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "mokafaa loyalty", "blurb": "Points at Zid, Chalhoub, Alshaya.", "div": "bank", "rev": "retail", "products": [
            P("mokafaa", "mokafaa", "The bank's points programme, earned on cards and accounts and redeemed with partners such as Zid's online stores, Chalhoub and Alshaya brands, and as a payment method on neoleap terminals.",
              s=["con"], lc="grow", o="B", neo=[0, ""],
              mc="Card-linked offers could extend mokafaa to merchants.",
              src=[["Al Rajhi: Zid partnership, Sep 2024", ZID], ["Annual report 2025: neoleap", NEOLEAP]]),
        ]},
        {"id": "3.4", "ic": "hand-coins", "name": "Instalments & BNPL", "blurb": "Tasaheal at 0%.", "div": "bank", "rev": "retail", "products": [
            P("tasaheal", "Tasaheal instalments", "Card purchases at partner merchants converted into equal monthly instalments at a 0% profit margin and no processing fee; Tashaeel does the same on neoleap terminals.",
              s=["con"], lc="borrow", o="B", neo=[0, "Runs on Visa cards."], src=[["Al Rajhi: Infinite credit card", INFINITE], ["Annual report 2025: neoleap", NEOLEAP]]),
            P("bnpl", "Buy now, pay later", "A bank BNPL product with merchant sign-up, Emkan's POS finance and BNPL (2025), and the Kingdom's first fully digital business-to-business BNPL.",
              s=["con", "sme"], lc="borrow", st="new", o="B", neo=[0, ""], src=[["Al Rajhi: Buy Now, Pay Later", BNPL], ["Annual report 2025: corporate banking", CORP], ["Annual report 2025: Emkan", EMKAN]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: number one in personal finance, mortgages and auto leasing, accounts and Takaful, a corporate and SME book growing fast, Al Rajhi Capital, and banks in Malaysia, Jordan and Kuwait.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Personal & home finance", "blurb": "No. 1 in mortgages.", "div": "bank", "rev": "retail", "products": [
            P("mortgages", "Home finance", "37.7% of the Kingdom's mortgages and a SAR 277 billion residential book at end-2025, including Tharwa rent-backed finance, with SAR 4.9 billion securitised in H1 2026.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["Annual report 2025: retail banking", RETAIL], ["H1 2026 earnings release", H1]]),
            P("personalfin", "Personal & auto finance", "38.5% of personal finance and 34.4% of auto leasing (2025), with Watani Extra and Sahlha; retail financing fell 2.6% in the year to June 2026 as the bank chose value over volume.",
              s=["con", "home"], lc="borrow", neo=[0, ""], src=[["Annual report 2025: retail banking", RETAIL], ["H1 2026 earnings release", H1]]),
            P("emkan", "Emkan Finance", "The group's microfinance arm: personal finance, POS finance, BNPL and an SME credit card launched in 2025, with customers up 23%; the SME card's network is not public.",
              s=["con", "sme"], lc="borrow", st="new", div="emkan", neo=[None, "Card network not public."], src=[["Annual report 2025: Emkan", EMKAN]]),
        ]},
        {"id": "4.2", "ic": "coins", "name": "Accounts, savings & Takaful", "blurb": "64% current accounts.", "div": "bank", "rev": "retail", "products": [
            P("accounts", "Accounts & savings", "Current, Hassad, Awaeed, family and dependent accounts, Jamyah money circles and gold and silver wallets; 64% of deposits are current accounts, and 97% of new retail accounts opened digitally in 2025.",
              s=["con", "expat"], lc="open", neo=[0, "mada debit."], src=[["H1 2026 earnings release", H1], ["Annual report 2025: digitalisation", DIGITAL]]),
            P("takaful", "Takaful & protection", "Shariah-compliant motor, health, travel, cyber and savings cover with Al Rajhi Takaful: SAR 4.91 billion of sales in 2025.",
              s=["con"], lc="grow", o="P", at="Al Rajhi Takaful", neo=[0, ""], src=[["Annual report 2025: retail banking", RETAIL]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Corporate & SME", "blurb": "SME book up 47%.", "div": "bank", "rev": "corporate", "products": [
            P("corporate", "Corporate & private banking", "A corporate book of about SAR 285 billion, up 13%, a 14.5% share of corporate lending, investment-banking revenue up 328% since 2023, and Private Banking with Black Card privileges.",
              s=["corp", "aff"], lc="borrow", neo=[0, ""], src=[["2Q 2026 call", CALL], ["Annual report 2025: corporate banking", CORP]]),
            P("sme", "SME banking", "SME financing up 46.7% in the year to June 2026, now 9% of the book, with POS financing against card takings and digital accounts.",
              s=["sme"], lc="borrow", neo=[0, "Visa business cards."],
              mc="Fast SME growth with no Mastercard commercial-card offer.",
              src=[["H1 2026 earnings release", H1], ["Annual report 2025: MSME", MSME]]),
            P("cashmgmt", "Cash management & trade", "Payroll, virtual accounts, escrow, direct debit, SWIFT, liquidity management, letters of credit and guarantees, Etimad and supply-chain finance.",
              s=["corp", "sme"], lc="move", neo=[0, ""], src=[["Annual report 2025: corporate banking", CORP]]),
        ]},
        {"id": "4.4", "ic": "chart-candlestick", "name": "Al Rajhi Capital", "blurb": "No. 1 broker on Tadawul.", "div": "capital", "rev": "invest", "products": [
            P("capital", "Al Rajhi Capital", "The leading broker by value traded on Tadawul (15.5%), second in assets under management, and third in public offerings.",
              s=["aff"], lc="grow", neo=[0, ""], src=[["Annual report 2025: strategic direction", STRAT], ["Annual report 2025: Al Rajhi Capital", CAPITAL]]),
        ]},
        {"id": "4.5", "ic": "earth", "name": "International", "blurb": "Malaysia, Jordan, Kuwait.", "div": "intl", "rev": "other", "products": [
            P("intl", "Malaysia, Jordan & Kuwait", "28 branches abroad: a Malaysian subsidiary, which launched its first credit cards, Visa Platinum and Signature Credit Card-i, in July 2026, and branches in Jordan (with a Visa Infinite card) and Kuwait.",
              s=["con"], lc="everyday", st="new", ay="Jul 2026", o="P", at="Visa", neo=[0, "Visa."],
              src=[["The Rakyat Post: Malaysia Visa cards, Jul 2026", MALAYSIA], ["Al Rajhi Jordan: Visa Infinite", JORDAN]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: a 96% digital app, the region's largest branch and ATM network, business channels, and sponsors and partners.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "alrajhi app", "blurb": "96% digital.", "div": "bank", "rev": "retail", "products": [
            P("app", "alrajhi mobile app", "A 'Dynamic App' with 440 million log-ins a month, card design, an in-app marketplace with instalments, and online card and finance applications; digital-to-manual ratio 96:4.",
              s=["con", "expat"], lc="everyday", neo=[0, ""],
              mc="An AI-led app with no agentic payments partner yet.",
              src=[["Annual report 2025: digitalisation", DIGITAL], ["Annual report 2025: shared services", SHARED]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "513 branches, 4,273 ATMs.", "div": "bank", "rev": "retail", "products": [
            P("branches", "Branches, ATMs & remittance centres", "The largest network in the Middle East: 513 branches, 4,273 ATMs and 135 remittance centres at 30 June 2026; Amex cardmembers can use more than 4,500 Al Rajhi ATMs (2024).",
              s=["con", "expat"], lc="everyday", neo=[0, ""], src=[["2Q 2026 investor presentation", PRES], ["International Banker: Amex, Jan 2024", AMEX]]),
        ]},
        {"id": "5.3", "ic": "monitor", "name": "Business channels", "blurb": "Business app, BFM+.", "div": "bank", "rev": "corporate", "products": [
            P("bizapp", "alrajhi Business app & eBusiness", "Digital account opening, Business Financial Manager (BFM+) dashboards, an eBusiness marketing engine for paid push campaigns, and instant digital letters of guarantee.",
              s=["sme", "corp"], lc="everyday", st="new", neo=[0, ""], src=[["Annual report 2025: innovation", INNOV], ["Annual report 2025: corporate banking", CORP]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Sponsorships & partners", "blurb": "Asian Cup with Visa.", "div": "arb", "rev": "other", "products": [
            P("partners", "Sponsorships & ecosystem partners", "Official regional retail banking partner of the AFC Asian Cup 2027, through Visa (June 2026), and founding partner of Money20/20 Middle East (September 2026), where the group set out to sign agreements with partners not yet named ⚠.",
              s=["con", "corp"], lc="beyond", st="new", ay="Jun 2026", o="P", at="Visa, AFC", neo=[0, "Visa sponsorship."],
              src=[["Al Rajhi: AFC Asian Cup with Visa, Jun 2026", AFC], ["Al Rajhi: Money20/20, Sep 2026", MONEY2020]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Al Rajhi", "blurb": "Acceptance, MPGS, urpay transfers.", "products": [
        P("mcatarb", "Mastercard at Al Rajhi", "Every Al Rajhi card checked is mada or Visa, and Visa also carries its remittances and its Asian Cup sponsorship. Mastercard is at the edges: acceptance on 43.5% of the Kingdom's POS terminals and online, Mastercard Payment Gateway Services as one of four merchant gateways, and Mastercard Move in the urpay wallet since June 2024.",
          s=["con"], div="arb", rev="other", mc="The relationship this map is drawn for.",
          src=[["Al Rajhi: e-commerce", ECOM], ["Al Rajhi: urpay and Mastercard Move, Jun 2024", MOVE], ["Al Rajhi: Infinite credit card", INFINITE]]),
    ]},
    {"id": "pillar-market", "name": "Payments in the Kingdom", "blurb": "mada, sarie, 85% electronic.", "products": [
        P("market", "The market", "E-payments were 85% of retail payments in 2025 (14.6 billion transactions), led by mada at POS and online; sarie instant payments grew about 32% ⚠; SAMA capped card and retail fees in 2025–26; open-banking licences are now final.",
          s=["con"], div="arb", rev="other", src=[["SAMA: e-payments 85%, Apr 2026", SAMA], ["4Q 2025 call", CALL4Q]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
