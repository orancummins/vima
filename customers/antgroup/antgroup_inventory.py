"""Ant International's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Ant International is private and publishes no financial statements: figures are its own releases (MoMents,
30 April 2026; VOYAGE, 18 September 2026), its 2025 Sustainability Report (May 2026) and press. Ant Group and
Alipay in mainland China are context only. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's
own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

NEWS = "https://www.ant-intl.com/en/news/detail/?id="
ABOUT = "https://www.ant-intl.com/en/about-us/"
HOME = "https://www.ant-intl.com/en/"
SR25 = "https://cdn.marmot-cloud.com/storage/intl_website/2026/05/11/HdZbV62/ant-intl_SR2025.pdf"
MOMENTS = "https://www.thailand-business-news.com/pr-news/expanding-infrastructure-for-the-age-of-ai-commerce-ant-international-connects-over-150-million-merchants-with-more-than-2-billion-consumers"
VOYAGE = NEWS + "ant-international-launches-full-stack-ai-native-solutions-for-payment-account-fx-treasury-and-growth-operations-for-global-businesses"
KYA = NEWS + "ant-international-mastercard-and-visa-initiate-collaboration-on-know-your-agent-interoperability-to-scale-agentic-commerce"
AMP = NEWS + "ant-internationals-agentic-mobile-protocol-rolls-out-globally-with-wallets-acquirers-initiating-collaboration-on-kya-interoperability-framework-with-mastercard-and-visa"
BRAZIL = NEWS + "ant-international-secures-payment-institution-licence-from-the-central-bank-of-brazil"
HSBC25 = NEWS + "hsbc-and-ant-international-celebrate-the-launch-of-the-banks-tokenised-deposit-service-in-singapore"
HSBCME = NEWS + "ant-international-and-hsbc-expand-real-time-treasury-management-services-to-the-middle-east"
BARC = NEWS + "ant-international-partners-with-barclays-on-global-treasury-management-with-proprietary-ai-powered-fx-model"
SERIESA = "https://www.theasianbanker.com/press-releases/ant-international-completes-1-2-billion-series-a-financing-round"
STANDARD = "https://www.thestandard.com.hk/finance/article/334298/Ant-International-raises-US1-billion-to-revive-Ant-Groups-Hong-Kong-IPO"
FNS = "https://fintechnews.sg/111459/fintech/ant-group-international-revenue/"
NFC = "https://www.alipayplus.com/nfc/"
KAKAO = "https://fxnewsgroup.com/forex-news/payments/alipay-mastercard-partner-to-bring-overseas-nfc-payments-to-kakao-pay-users/"
GCASH = "https://mynt.com.ph/newsroom/gcash-tap-to-pay-goes-global-in-partnership-with-alipay-and-powered-by-mastercard"
ANTOMAG = "https://thefintechtimes.com/antom-launches-agentic-payment-solution-partners-with-visa-and-mastercard-on-ai-pilots/"
ICFZ = "https://www.silicon.co.uk/press-release/ant-group-mastercard-e-wallets-launch-international-consumer-friendly-zones-program-in-shanghai-to-drive-inbound-tourism-to-china"
AMEX = "https://english.shanghai.gov.cn/en-Latest-WhatsNew/20250228/5af2c2cb1807459a84f5b49e6a1ebb06.html"
WFCARD = "https://www.worldfirst.com/uk/world-card/"
ANTOM = "https://www.antom.com/"
C2P = "https://www.2c2p.com/"
BETTR = "https://www.bettr.com/"
STABLE = "https://fintechnews.hk/34285/blockchain/ant-international-stablecoin-license-hk-singapore/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "network · funding · licences", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: a network of more than 150 million merchants and 2 billion accounts, about $3 billion of revenue in 2024, a $1.2 billion Series A in July 2026, licences from Singapore to Brazil, and its own AI models.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & revenue", "blurb": "150m merchants, 2bn accounts.", "div": "ai", "rev": "grp", "products": [
            P("scale", "Network scale", "More than 150 million merchants and more than 2 billion user accounts, over 300 payment methods in 220-plus markets (April 2026), and more than 25 million transactions a day (September 2026).",
              s=["mer", "wal"], neo=[0, ""], src=[["MoMents release, Apr 2026", MOMENTS], ["Ant International: VOYAGE, Sep 2026", VOYAGE]]),
            P("revenue", "Revenue & profit", "About $3 billion of revenue in 2024 and about 25% growth in 2025, with two years of adjusted profit, as reported by Bloomberg from unnamed people ⚠. No financial statements are published.",
              s=["mer"], st="unconf", neo=[0, ""], src=[["The Standard (Bloomberg), Jun 2026", STANDARD], ["Fintech News SG (Bloomberg), May 2025", FNS]]),
        ]},
        {"id": "1.2", "ic": "coins", "name": "Ownership & funding", "blurb": "$1.2bn Series A.", "div": "grp", "rev": "grp", "products": [
            P("ownership", "Ownership & Series A", "Part of Ant Group, with its own board since 2023 and independent operation since 2024; a Series A of about $1.2 billion closed on 21 July 2026 with Ant Group, Alibaba and unnamed institutions; a valuation of about $10 billion was reported ⚠, and the round is linked to a possible Hong Kong listing ⚠.",
              s=["mer"], st="new", ay="Jul 2026", neo=[0, ""], src=[["The Asian Banker: Series A, Jul 2026", SERIESA], ["The Standard (Bloomberg), Jun 2026", STANDARD], ["Fintech News SG, May 2025", FNS]]),
        ]},
        {"id": "1.3", "ic": "users-round", "name": "Leadership", "blurb": "Peng Yang, Douglas Feagin.", "div": "ai", "rev": "grp", "products": [
            P("leaders", "Leadership", "CEO Peng Yang; President Douglas Feagin; CFO Yi Zhou; Chief Innovation Officer Jiangming Yang; business CEOs Gary Liu (Antom), Clara Shi (WorldFirst), Huaisheng Chen (Bettr) and Kai Qiu (ANEXT Bank). Chairman Eric Jing, also Ant Group's chairman and CEO (2025) ⚠.",
              s=["mer"], neo=[0, ""], src=[["Ant International: about us", ABOUT], ["Fintech News SG, May 2025", FNS]]),
        ]},
        {"id": "1.4", "ic": "scale", "name": "Licences & trust", "blurb": "Singapore HQ, Brazil PI.", "div": "ai", "rev": "grp", "products": [
            P("licences", "Licences", "Financial licensees in many markets (no full list published ⚠), ANEXT Bank as a Singapore digital bank, and a Payment Institution licence from the Central Bank of Brazil (September 2026).",
              s=["mer", "fi"], st="new", ay="Sep 2026", neo=[0, ""], src=[["Ant International: Brazil licence, Sep 2026", BRAZIL], ["Ant International: about us", ABOUT], ["Sustainability Report 2025", SR25]]),
            P("guardian", "Regulatory work", "Leads the Payment FX workstream in MAS's Project Guardian on tokenisation, and works with MAS's BuildFin.ai on agentic finance.",
              s=["fi"], neo=[0, ""], src=[["Ant International: HSBC tokenised deposits, Jun 2025", HSBC25], ["Ant International: KYA, Sep 2026", KYA]]),
        ]},
        {"id": "1.5", "ic": "brain", "name": "AI platform", "blurb": "Three large in-house models.", "div": "ai", "rev": "grp", "products": [
            P("aimodels", "In-house AI models", "Antom's 3-in-1 Transformer (10 billion-plus parameters), the FalconTST FX model (8.5 billion-plus, 93% accuracy, open-sourced in 2025) and the AI SHIELD risk model (7 billion-plus); 81.4% of payment tasks completed or aided by AI.",
              s=["mer", "fi"], o="B", neo=[0, ""], src=[["Ant International: VOYAGE, Sep 2026", VOYAGE], ["MoMents release, Apr 2026", MOMENTS]]),
        ]},
        {"id": "1.6", "ic": "target", "name": "Strategy & deals", "blurb": "Four pillars, 100 products.", "div": "ai", "rev": "grp", "products": [
            P("strategy", "Four pillars as one", "Alipay+, Antom, WorldFirst and Bettr combined into one set of AI-led growth tools; close to 100 products launched at VOYAGE (September 2026) for roll-out in autumn and winter 2026.",
              s=["mer", "sme"], st="new", neo=[0, ""], src=[["Ant International: VOYAGE, Sep 2026", VOYAGE], ["MoMents release, Apr 2026", MOMENTS]]),
            P("deals", "Acquisitions & stakes", "WorldFirst (2019), 2C2P (2022), MultiSafepay (now wholly owned ⚠ date), ANEXT Bank (incorporated 2022) and a stake in R2, a Latin American SME lender (late 2025).",
              s=["mer", "sme"], o="A", neo=[0, ""], src=[["Ant International: about us", ABOUT], ["Sustainability Report 2025", SR25]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: the Alipay+ wallet gateway over its own QR rails and ten national QR schemes, Alipay+ NFC on Mastercard, Antom acquiring, WorldFirst accounts and cards, blockchain treasury, and bank-to-wallet transfers with Swift.",
    "tiles": [
        {"id": "2.1", "ic": "network", "name": "Wallet gateway", "blurb": "53 wallets, 10 QR schemes.", "div": "aplus", "rev": "wallet", "products": [
            P("aplusqr", "Alipay+ cross-border QR", "Lets users of 53 home wallets (AlipayHK, GCash, Kakao Pay, TNG eWallet, DANA, TrueMoney, Toss) pay at more than 150 million merchants abroad, including Alipay's network in China (since 2024).",
              s=["trav", "wal"], lc="move", o="B", neo=[0, "Own wallet and QR rails."],
              mc="Wallet-to-merchant payments that skip the card networks.",
              src=[["Ant International: VOYAGE, Sep 2026", VOYAGE], ["Ant International: about us", ABOUT]]),
            P("nationalqr", "National QR schemes", "Ten national QR systems connected, including SGQR, DuitNow, ZeroPay, PromptPay, QRIS, LankaPay and QR Ph; cross-border QR with NAPAS in Vietnam and with mada in the Gulf planned for 2026.",
              s=["wal", "trav"], lc="move", o="P", neo=[0, "Domestic schemes."], src=[["MoMents release, Apr 2026", MOMENTS]]),
        ]},
        {"id": "2.2", "ic": "smartphone", "name": "NFC on Mastercard", "blurb": "Tap at 150m Mastercard sites.", "div": "aplus", "rev": "wallet", "products": [
            P("aplusnfc", "Alipay+ NFC", "Wallets tap to pay at any Mastercard contactless terminal, more than 150 million locations, through a token linked to the wallet; GCash (August 2025) and Kakao Pay (September 2025) first; Android only, iOS coming.", short="Alipay+ NFC",
              s=["trav", "wal"], lc="move", st="new", ay="Aug 2025", o="P", at="Mastercard", neo=[2, "Rides wholly on Mastercard acceptance."],
              mc="The only card network behind Alipay+ NFC; 51 more wallets could follow.",
              src=[["Alipay+: NFC", NFC], ["GCash Tap to Pay, Aug 2025", GCASH], ["FX News Group: Kakao Pay NFC, Sep 2025", KAKAO]]),
        ]},
        {"id": "2.3", "ic": "store", "name": "Merchant acquiring", "blurb": "Antom, 2C2P, MultiSafepay.", "div": "antom", "rev": "merchant", "products": [
            P("antomacq", "Antom acquiring & checkout", "Accepts cards (Visa, Mastercard and others), wallets and bank transfers in more than 200 markets and 140 currencies, with 300-plus methods; Pix in Brazil.",
              s=["mer"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["Antom", ANTOM], ["Ant International: Brazil licence, Sep 2026", BRAZIL]]),
            P("c2pgw", "2C2P by Antom", "Payment gateway in six Southeast Asian markets (Lazada, AirAsia, Changi Airport), with issuing of wallets and cards, payouts, airline payments and 600,000 over-the-counter points; networks not named ⚠.",
              s=["mer"], lc="move", o="A", neo=[None, "Networks not published."], src=[["2C2P", C2P]]),
            P("msp", "MultiSafepay", "European payment provider, wholly owned, with more than 20,000 merchants, 40-plus methods, volume up 50% and 20% of volume in person (2025).",
              s=["mer"], lc="move", o="A", neo=[1, "Accepts every network."], src=[["Sustainability Report 2025", SR25]]),
        ]},
        {"id": "2.4", "ic": "wallet-cards", "name": "Accounts & cards", "blurb": "WorldFirst, 1.6m SMEs.", "div": "wf", "rev": "account", "products": [
            P("worldacct", "WorldFirst World Account", "Multi-currency business accounts, FX and global transfers for more than 1.6 million SMEs in 210-plus markets, collecting from 130-plus marketplaces; World Payout and Whale Pooling (same-day rate above 98%).",
              s=["sme"], lc="move", o="A", neo=[0, "Bank and own rails."], src=[["Sustainability Report 2025", SR25], ["Ant International: VOYAGE, Sep 2026", VOYAGE]]),
            P("worldcard", "WorldFirst World Card", "Business virtual and physical card; in the UK on Mastercard with up to 1.2% cashback, no FX fee in 15 currencies and Google Wallet; 17 currencies (2026). Other markets' network not confirmed ⚠.", short="World Card",
              s=["sme"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard in the UK."],
              src=[["WorldFirst UK: World Card", WFCARD], ["Ant International: VOYAGE, Sep 2026", VOYAGE]]),
        ]},
        {"id": "2.5", "ic": "coins", "name": "Blockchain treasury", "blurb": "WhaleRTP, tokenised deposits.", "div": "bettr", "rev": "credit", "products": [
            P("whalertp", "WhaleRTP", "Blockchain treasury platform with more than 20 banks and 17-plus currencies; carried 45% of Ant International's 2025 cross-border volume, and more than 53% of its own liquidity runs on blockchain.",
              s=["fi"], lc="move", o="B", neo=[0, "Off the card networks."],
              src=[["Ant International: VOYAGE, Sep 2026", VOYAGE], ["Ant International: HSBC Middle East, Oct 2026", HSBCME], ["Sustainability Report 2025", SR25]]),
            P("tokdep", "Tokenised deposits with HSBC", "HSBC's Tokenised Deposit Service for real-time treasury in Hong Kong and Singapore (2025) and the UAE (October 2026); work together since 2020.",
              s=["fi"], lc="move", st="new", o="P", at="HSBC", neo=[0, "Bank rails."],
              src=[["Ant International: HSBC Singapore, Jun 2025", HSBC25], ["Ant International: HSBC Middle East, Oct 2026", HSBCME]]),
            P("settletoken", "Bettr Settlement Token & stablecoins", "Tokenised e-money for wholesale settlement across Ant International; stablecoin issuer licences sought in Hong Kong, Singapore and Luxembourg (June 2025) ⚠ status unknown.",
              s=["fi"], lc="move", st="unconf", neo=[0, "Off the card networks."], src=[["Bettr", BETTR], ["Fintech News HK, Jun 2025", STABLE]]),
        ]},
        {"id": "2.6", "ic": "arrow-left-right", "name": "Bank-to-wallet", "blurb": "Swift and Standard Chartered.", "div": "aplus", "rev": "wallet", "products": [
            P("swiftb2w", "Bank-to-wallet on Swift", "Live trials with Standard Chartered and Swift of ISO 20022 transfers from 11,500 banks into 1.7 billion Alipay+ wallet accounts.",
              s=["wal", "fi"], lc="move", st="new", o="P", at="Swift", neo=[0, "Bank rails."], src=[["Sustainability Report 2025", SR25]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every payment: AI risk and dispute tools, payment optimisation, agentic commerce with Mastercard and Visa, FX forecasting, and marketing and AI tools for wallets.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Risk & fraud", "blurb": "AI SHIELD, Antom Shield.", "div": "antom", "rev": "merchant", "products": [
            P("antomshield", "AI SHIELD & Antom Shield", "A risk model of more than 7 billion parameters with over 95% precision and payment success up to 13.5% higher; fraud down 50% through its risk tools (2025).",
              s=["mer", "wal"], lc="everyday", o="B", neo=[0, "Own models."], src=[["MoMents release, Apr 2026", MOMENTS], ["Sustainability Report 2025", SR25]]),
        ]},
        {"id": "3.2", "ic": "receipt-text", "name": "Disputes", "blurb": "SmartDispute, Copilot.", "div": "antom", "rev": "merchant", "products": [
            P("smartdispute", "SmartDispute & Antom Copilot", "Dispute success up from 24.5% to 41.8% with SmartDispute; Copilot cuts chargeback handling time by up to 46%; chargebacks down up to 87% for leading AI clients.",
              s=["mer"], lc="everyday", st="new", o="B", neo=[0, "Own tools."],
              mc="Dispute pain that Ethoca and Consumer Clarity address.",
              src=[["Ant International: VOYAGE, Sep 2026", VOYAGE], ["MoMents release, Apr 2026", MOMENTS]]),
        ]},
        {"id": "3.3", "ic": "gauge", "name": "Optimisation", "blurb": "Revenue Booster, tokens.", "div": "antom", "rev": "merchant", "products": [
            P("revbooster", "Card Revenue Booster & orchestration", "Recovery of declined card payments and Antom Payment Orchestration; Autopilot cuts the first transaction from days to minutes.",
              s=["mer"], lc="grow", o="B", neo=[1, "Card payments on every network."], src=[["Antom", ANTOM], ["Ant International: VOYAGE, Sep 2026", VOYAGE]]),
            P("tokenpay", "Tokenised payment & billing", "Tokenised payments, auto-billing, subscriptions and usage-based billing; use of network tokens not stated ⚠.",
              s=["mer"], lc="grow", o="B", neo=[None, "Network tokens not stated."], src=[["Antom", ANTOM]]),
        ]},
        {"id": "3.4", "ic": "bot", "name": "Agentic commerce", "blurb": "AMP, KYA, Agent Pay.", "div": "aplus", "rev": "wallet", "products": [
            P("amp", "Agentic Mobile Protocol", "Open-source protocol for AI agents to pay from wallets (April 2026); Phase I with 10 wallets (1.5 billion accounts) and 7 acquirers including Adyen, Checkout.com, Fiserv and Worldline; co-developed Google's UCP.",
              s=["ai", "wal"], lc="move", st="new", ay="Apr 2026", o="B", neo=[0, "Wallet rails."], src=[["Ant International: AMP roll-out, Sep 2026", AMP], ["Sustainability Report 2025", SR25]]),
            P("kya", "Know-Your-Agent with Mastercard & Visa", "Interoperable agent identity across card and wallet networks (September 2026), through MAS's BuildFin.ai, joining AMP with Mastercard Verifiable Intent and Visa's Trusted Agent Protocol.", short="KYA",
              s=["ai"], lc="open", st="new", ay="Sep 2026", o="P", at="Mastercard, Visa", neo=[1, "Shared with Visa."],
              mc="Pablo Fourez for Mastercard; the standard for wallet-led agents.",
              src=[["Ant International: KYA, Sep 2026", KYA]]),
            P("agentpay", "Antom with Mastercard Agent Pay", "Among the first Asia Pacific partners piloting tokenised card payments by AI agents with Mastercard Agent Pay, alongside Visa Intelligent Commerce (September 2025).", short="Agent Pay pilot",
              s=["ai", "mer"], lc="move", st="new", ay="Sep 2025", o="P", at="Mastercard", neo=[3, "Mastercard Agent Pay."],
              mc="A pilot; no live volume published.",
              src=[["Fintech Times: Antom agentic, Sep 2025", ANTOMAG]]),
            P("antomagentic", "Antom agentic payments", "Agentic Payments, Agentic Commerce Hub, Shopping Agent and AgentSafePay, a full guarantee against agent-specific losses (2026).",
              s=["ai", "mer"], lc="move", st="new", o="B", neo=[1, "Cards and wallets."], src=[["Ant International: VOYAGE, Sep 2026", VOYAGE]]),
        ]},
        {"id": "3.5", "ic": "chart-candlestick", "name": "FX & treasury AI", "blurb": "FalconTST, Barclays.", "div": "wf", "rev": "account", "products": [
            P("falcon", "Falcon FX & forecasting", "FalconTST forecasts cash flow and FX exposure with 93% accuracy, cutting hedging costs by 30–60%; sold through WorldFirst as Falcon Forecast and Falcon FX.",
              s=["sme", "fi"], lc="everyday", o="B", neo=[0, ""], src=[["Ant International: VOYAGE, Sep 2026", VOYAGE]]),
            P("barclays", "Barclays FX partnership", "Barclays built the model into its BARX NetFX platform and ran Ant International's intra-group FX (May 2025).",
              s=["fi"], lc="everyday", ay="May 2025", o="P", at="Barclays", neo=[0, ""], src=[["Ant International: Barclays, May 2025", BARC]]),
        ]},
        {"id": "3.6", "ic": "gift", "name": "Marketing & wallet tech", "blurb": "A+ Rewards, GenAI Cockpit.", "div": "aplus", "rev": "wallet", "products": [
            P("aplusrewards", "A+ Rewards", "Connects merchants to wallet users and 30-plus AI and e-commerce platforms; Consumer Friendly Zones and campaigns for travellers.",
              s=["mer", "trav"], lc="grow", o="B", neo=[0, "Own network."], src=[["Ant International: VOYAGE, Sep 2026", VOYAGE]]),
            P("genaicockpit", "GenAI Cockpit & wallet tech", "AI-as-a-service for wallets (TNG eWallet, easypaisa) and wallet technology for 35 partners in 25 markets.",
              s=["wal"], lc="beyond", o="B", neo=[0, ""], src=[["MoMents release, Apr 2026", MOMENTS], ["Sustainability Report 2025", SR25]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "Who buys: 53 partner wallets, Antom's merchants from Airbnb to Google, 1.6 million cross-border SMEs, lenders and banks through Bettr, and visitors to China through Ant Group's Alipay.",
    "tiles": [
        {"id": "4.1", "ic": "wallet", "name": "Wallet partners", "blurb": "53 wallets and bank apps.", "div": "aplus", "rev": "wallet", "products": [
            P("walletpartners", "Alipay+ partners", "53 wallets and bank apps (September 2026), up from 47 in 2025; new in 2026 are iFAST Global Bank, KBank, SCB, barq and ShopeePay.",
              s=["wal"], lc="open", neo=[0, "Wallet rails."], src=[["Ant International: VOYAGE, Sep 2026", VOYAGE], ["MoMents release, Apr 2026", MOMENTS]]),
        ]},
        {"id": "4.2", "ic": "building-2", "name": "Merchants", "blurb": "Airbnb, Adobe, Delivery Hero.", "div": "antom", "rev": "merchant", "products": [
            P("antommerchants", "Antom merchants", "Enterprise and SME merchants including Airbnb, Adobe and Delivery Hero; 89.5% of clients use its AI tools.",
              s=["mer"], lc="everyday", neo=[1, "Accepts every network."], src=[["Sustainability Report 2025", SR25], ["Ant International: VOYAGE, Sep 2026", VOYAGE]]),
            P("epos", "EPOS360", "An AI device and app for small shops (late 2025), in Singapore and in Malaysia through TNG eWallet.",
              s=["mer"], lc="everyday", st="new", o="B", neo=[None, ""], src=[["MoMents release, Apr 2026", MOMENTS]]),
        ]},
        {"id": "4.3", "ic": "briefcase-business", "name": "Cross-border SMEs", "blurb": "1.6m on WorldFirst.", "div": "wf", "rev": "account", "products": [
            P("wfsme", "WorldFirst for SMEs & enterprises", "More than 1.6 million SMEs (end-2025), the most global business accounts of any provider by its own count ⚠, and an enterprise suite of treasury tools.",
              s=["sme"], lc="everyday", neo=[0, ""], src=[["Sustainability Report 2025", SR25], ["MoMents release, Apr 2026", MOMENTS]]),
        ]},
        {"id": "4.4", "ic": "hand-coins", "name": "Credit & banking", "blurb": "Bettr, ANEXT, R2.", "div": "bettr", "rev": "credit", "products": [
            P("bettrcredit", "Bettr credit tech", "AI Credit Engine used by 49 institutions in 28 markets reaching more than 100 million users; partners such as bKash; a stake in R2 in Latin America.",
              s=["fi", "sme"], lc="borrow", o="B", neo=[0, ""], src=[["Ant International: VOYAGE, Sep 2026", VOYAGE], ["Sustainability Report 2025", SR25]]),
            P("anext", "ANEXT Bank", "Singapore digital bank for regional small businesses (incorporated 2022); with Bettr, 980,000 users and 110,000 SME customers.",
              s=["sme"], lc="borrow", o="B", neo=[None, ""], src=[["Ant International: about us", ABOUT], ["Sustainability Report 2025", SR25]]),
        ]},
        {"id": "4.5", "ic": "plane", "name": "China inbound", "blurb": "Alipay for visitors.", "div": "grp", "rev": "wallet", "products": [
            P("chinainbound", "Visitors paying in China", "Ant Group's Alipay lets visitors link Visa, Mastercard, JCB, Discover, Diners and, since February 2025, Amex cards; Consumer Friendly Zones with Mastercard and wallets in Beijing, Shanghai and other cities (2024).",
              s=["trav"], lc="move", o="P", at="Ant Group", neo=[1, "One of seven card brands."],
              src=[["Consumer Friendly Zones, May 2024", ICFZ], ["Shanghai government: Amex on Alipay, Feb 2025", AMEX]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Ant International: Antom's portal and APIs, the WorldFirst app and its agent, partner wallets' own apps, and offices from Hangzhou to São Paulo.",
    "tiles": [
        {"id": "5.1", "ic": "code-xml", "name": "Portal & APIs", "blurb": "Antom portal, plugins.", "div": "antom", "rev": "merchant", "products": [
            P("antomportal", "Antom portal & APIs", "Merchant portal with Copilot, APIs and Shopify and WooCommerce plugins; 72% of new merchants integrated themselves within a year.",
              s=["mer"], lc="open", o="B", neo=[0, ""], src=[["Antom", ANTOM], ["MoMents release, Apr 2026", MOMENTS]]),
        ]},
        {"id": "5.2", "ic": "smartphone", "name": "Apps & agents", "blurb": "WorldFirst app, Wyn.", "div": "wf", "rev": "account", "products": [
            P("wfapp", "WorldFirst app & Wyn", "The WorldFirst app with Wyn, a natural-language agent for account management, and Account for Agent, a business account for AI agents (2026).",
              s=["sme", "ai"], lc="open", st="new", o="B", neo=[0, ""], src=[["Ant International: VOYAGE, Sep 2026", VOYAGE]]),
            P("walletapps", "Partner wallet apps", "Travellers reach Alipay+ through their own wallets (GCash, Kakao Pay, AlipayHK and others), not an Ant International app.",
              s=["trav", "wal"], lc="open", neo=[0, ""], src=[["Ant International: AMP roll-out, Sep 2026", AMP]]),
        ]},
        {"id": "5.3", "ic": "earth", "name": "Regions", "blurb": "Asia to Brazil and the Gulf.", "div": "ai", "rev": "grp", "products": [
            P("regions", "Regional presence", "Offices across China, Asia, EMEA, the Americas and Oceania; new in Brazil (2026), a treasury hub planned for the Middle East, and Vietnam's financial centre.",
              s=["mer"], lc="open", st="new", neo=[0, ""], src=[["Ant International", HOME], ["Ant International: HSBC Middle East, Oct 2026", HSBCME], ["MoMents release, Apr 2026", MOMENTS]]),
        ]},
        {"id": "5.4", "ic": "presentation", "name": "Partners & events", "blurb": "MoMents, VOYAGE.", "div": "ai", "rev": "grp", "products": [
            P("partners", "Partners & forums", "MoMents for wallets and banks (Kuala Lumpur, April 2026) and VOYAGE for merchants (Shanghai, September 2026, 1,100 executives); bank partners HSBC, Barclays and Standard Chartered.",
              s=["wal", "mer"], lc="open", neo=[0, ""], src=[["MoMents release, Apr 2026", MOMENTS], ["Ant International: VOYAGE, Sep 2026", VOYAGE]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Ant International", "blurb": "NFC, KYA, Agent Pay.", "products": [
        P("mcatant", "Mastercard at Ant International", "Mastercard is the only card network behind Alipay+ NFC (GCash, Kakao Pay), sits with Visa in Know-Your-Agent work, is piloted by Antom through Agent Pay, and carries WorldFirst's UK World Card. Most of Ant International's volume moves on its own wallet and QR rails, national schemes and blockchain treasury.",
          s=["wal"], div="ai", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Alipay+: NFC", NFC], ["Ant International: KYA, Sep 2026", KYA]]),
    ]},
    {"id": "pillar-market", "name": "Cross-border wallets", "blurb": "QR, cards, agents.", "products": [
        P("market", "The market", "Wallet interoperability against card networks for travel payments, national QR schemes as partners, Adyen and Checkout.com as both peers and AMP acquirers, and regulators shaping agentic finance and stablecoins.",
          s=["wal"], div="ai", rev="grp", src=[["Ant International: AMP roll-out, Sep 2026", AMP], ["Ant International: KYA, Sep 2026", KYA]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
