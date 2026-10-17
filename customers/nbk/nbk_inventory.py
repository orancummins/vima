"""National Bank of Kuwait's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the H1 2026 results (20 July 2026), the 2Q 2026
investor presentation and call, the 2025 Annual Report and NBK's card and payments pages (read 17 October 2026).
``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on
Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1 = "https://kuwaittimes.com/article/46764/business/nbk-posts-kd-3248-million-in-net-profit-for-first-half-of-2026/"
IP = "https://www.nbk.com/dam/jcr:4f54b9f6-9062-4525-8bc4-76db32bf9911/nbk-investor-presentation-2q-2026.pdf"
CALL = "https://www.nbk.com/dam/jcr:096de482-d56e-4967-aca2-ecededfa009a/2Q2026%20Full%20script-English.pdf"
AR25 = "https://www.nbk.com/dam/jcr:73b1509e-5280-4ef3-a29a-392c1b565299/nbk-annual-report-2025-e.pdf"
FY25 = "https://kuwaittimes.com/article/39203/business/nbks-2025-results-reinforce-its-sustainable-growth-trajectory-says-shaikha-al-bahar/"
ABOUT = "https://www.nbk.com/kuwait/About.html"
NETWORK = "https://www.nbk.com/about-nbk-group/our-network.html"
NEWS = "https://www.nbk.com/kuwait/news-and-insights/media-relations/news.html"
CREDIT = "https://www.nbk.com/kuwait/personal/cards/credit-cards.html"
MILES = "https://www.nbk.com/kuwait/personal/cards/credit-cards/miles-credit-card.html"
DEBIT = "https://www.nbk.com/kuwait/personal/cards/debit-cards.html"
DEBITCARD = "https://www.nbk.com/kuwait/personal/cards/debit-cards/debit-card.html"
PRIVILEGE = "https://www.nbk.com/kuwait/personal/cards/debit-cards/privilege.html"
PREPAID = "https://www.nbk.com/kuwait/personal/cards/prepaid-cards.html"
CARDSERV = "https://www.nbk.com/kuwait/personal/cards/card-services.html"
COMM = "https://www.nbk.com/kuwait/business/cards/commercial-cards.html"
PAYSERV = "https://www.nbk.com/kuwait/business/Business-Solutions/Payment-Services.html"
UPAY = "https://www.nbk.com/kuwait/business/Business-Solutions/upayments-solutions.html"
UPAYZ = "https://www.zawya.com/en/press-release/companies-news/nbk-acquires-51-of-the-capital-of-the-leading-payment-service-provider-upayments-tagbxfzz"
CDB = "https://kuwaittimes.com/article/37490/business/nbk-further-strengthens-its-leadership-in-consumer-and-digital-banking/"
VISA22 = "https://www.gccbusinessnews.com/kuwaits-nbk-extends-its-partnership-agreement-with-visa/"
AURAKT = "https://kuwaittimes.com/article/49240/business/nbk-elevates-aura-card-shopping-with-premium-benefits/"
MC25 = "https://kuwaittimes.com/article/29114/business/special-offer-for-nbk-mastercard-holders/"
MCUCL = "https://www.mastercard.com/news/eemea/en/newsroom/press-releases/en/2021/march/mastercard-and-nbk-partner-to-launch-action-packed-uefa-champions-league-mastercard-cards"
MCBIO = "https://mobileidworld.com/mastercard-national-bank-kuwai-biometric-payment-card-trial-gcc-905172/"
MCBIO2 = "https://mastercard.com/news/eemea/en/newsroom/press-releases/en/2018/may/national-bank-of-kuwait-and-mastercard-make-gcc-debut-of-pioneering-biometric-solutions"
WAMDNBK = "https://kuwaittimes.com/article/16052/business/nbk-launches-instant-payment-service-wamd-on-its-mobile-banking-app/amp"
WAMD1M = "https://www.businesswire.com/news/home/20250527732725/en/Kuwait%E2%80%99s-Real-Time-Payment-Scheme-WAMD-Surpasses-1-Million-Accounts-in-First-Year"
APPLEPAY = "https://www.cbk.gov.kw/en/cbk-news/announcements-and-press-releases/press-releases/2022/12/202212080902-launching-apple-pay-service-having-met-all-the-legal-and-regulatory-requirements"
KNETAP = "https://www.checkout.com/docs/payments/add-payment-methods/apple-pay/apple-pay-via-knet"
WEYAY = "https://www.weyaybank.com/"
WEYAYPRE = "https://www.weyaybank.com/cards/Prepaid-cards.html"
JEEL = "https://www.weyaybank.com/cards/Jeel.html"
BAH = "https://www.gdnonline.com/Details/1403801"
EGY = "https://kuwaittimes.com/article/48752/business/nbk--egypt-delivers-a-net-profit-of-kd-261-million-in-first-half-of-2026/amp"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · heritage · network", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: KD 46 billion of assets and more than 30% of Kuwait's banking assets, a bank founded by merchants in 1952, a 13-country network, a core and card-switch modernisation, and a strategy to defend Kuwait while growing wealth, Islamic banking and the region.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "KD 46bn of assets, A1/A+.", "div": "group", "rev": "consumer", "products": [
            P("balance", "Balance sheet & earnings", "Net profit of KD 324.8 million in H1 2026, up 3%, and KD 576 million in 2025, down 5% after Kuwait's new 15% tax; assets KD 46.2 billion, loans KD 27.8 billion and deposits KD 27.0 billion at 30 June 2026; CET1 13.0%, NPL ratio 1.22%; rated A1/A+/A+; market value KD 7.4 billion.",
              s=["corp"], neo=[0, ""], src=[["H1 2026 results, Jul 2026", H1], ["2Q 2026 investor presentation", IP], ["FY2025 results, Jan 2026", FY25]]),
        ]},
        {"id": "1.2", "ic": "badge-check", "name": "Heritage & leadership", "blurb": "Kuwait's first bank, 1952.", "div": "group", "rev": "consumer", "products": [
            P("heritage", "Heritage & ownership", "Opened on 15 November 1952 as Kuwait's first indigenous bank and the Gulf's first shareholding company, founded by nine merchants; listed since 1984 with the same core shareholders, and only PIFSS above 5% (6.19%).",
              s=["con"], o="I", neo=[0, ""], src=[["NBK: About", ABOUT], ["2Q 2026 investor presentation", IP]]),
            P("leadership", "Board & executive team", "Chairman Hamad Al-Bahar; Vice-Chairman and Group CEO Isam Al-Sager; Deputy Group CEO Shaikha Al-Bahar; Salah Al-Fulaij runs NBK Kuwait and Mohammed Al-Othman Consumer and Digital Banking; Group CFO Sujit Ronghe. 8,418 employees.",
              s=["corp"], neo=[0, ""], src=[["NBK: About", ABOUT], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "1.3", "ic": "earth", "name": "Network", "blurb": "13 countries, 138 locations.", "div": "intl", "rev": "intl", "products": [
            P("network", "Regional & international network", "138 branches, subsidiaries and offices in 13 countries: 70 branches in Kuwait, 53 in Egypt, three each in Saudi Arabia, the UAE and Iraq, two each in Bahrain and Lebanon, and London, Paris, Geneva, New York, Singapore and Shanghai; a DIFC branch opened in November 2025. International banking earns about 25% of group profit.",
              s=["corp", "hnw"], neo=[0, ""], src=[["NBK: our network", NETWORK], ["2Q 2026 investor presentation", IP], ["NBK newsroom", NEWS]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "Core, card switch, Copilot.", "div": "group", "rev": "consumer", "products": [
            P("tech", "Core & payments modernisation", "TCS BaNCS core upgrades, Red Hat OpenShift, a BASE24 card-switch upgrade to meet scheme mandates, ISO 20022, a cards system enhanced for tokenisation, 3-D Secure and new wallets, and an API layer for open-banking rules in Kuwait and the GCC (2025).",
              s=["con", "corp"], neo=[0, "Scheme-neutral."], src=[["2025 Annual Report", AR25]]),
            P("ai", "AI programme", "Aims to be Kuwait's leading AI-driven bank: Microsoft Copilot across the bank, machine learning for lead targeting, call centres and fraud, a roadmap for generative AI in customer journeys, and an AI Mindset programme for staff in 2026.",
              s=["con"], st="new", neo=[0, ""],
              mc="No agentic-payments work found; Agent Pay is open ground.",
              src=[["2025 Annual Report", AR25], ["NBK newsroom", NEWS]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "Defend Kuwait, grow the region.", "div": "group", "rev": "consumer", "products": [
            P("strategy", "Strategy & 2026 guidance", "Defend leadership in Kuwait, build a regional wealth business, expand in the region and grow Islamic banking through Boubyan, with a dual-track digital plan and a US$10 billion sustainable-finance target for 2030 (about 60% reached). 2026 loan growth guided to mid-to-high single digits; a regional conflict and the Strait of Hormuz closure weighed on activity.",
              s=["corp"], neo=[0, ""], src=[["2Q 2026 investor presentation", IP], ["2Q 2026 call script", CALL]]),
            P("deals", "Deals", "51% of the payment service provider UPayments (2025 ⚠ date), Boubyan Bank consolidated in 2012 (now 60.4%), a fourth UAE branch in DIFC (November 2025) and NBK France mortgages in Spain, Germany and Portugal.",
              s=["sme", "corp"], o="A", neo=[0, ""], src=[["Zawya: UPayments stake", UPAYZ], ["2Q 2026 investor presentation", IP]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: Visa flagship credit cards under a seven-year deal from 2022, a Mastercard set led by the Aura co-brand, KNET debit with Visa premium cards, Visa commercial cards, merchant acquiring with UPayments, and KNET's WAMD and the GCC's AFAQ for instant transfers.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Visa credit", "blurb": "KWT, Harrods, Kuwait Airways.", "div": "nbk", "rev": "consumer", "products": [
            P("kwt", "NBK KWT Visa Infinite", "The flagship cashback card, launched in early 2022, paying up to KD 1,000 a month ('Kuwait's highest cashback'), issued in the app and activated by tapping it on the phone; fee KD 125.", short="KWT Visa Infinite",
              s=["con", "aff"], lc="everyday", ay="2022", o="P", at="Visa", neo=[0, "Visa."], src=[["NBK: credit cards", CREDIT], ["GCC Business News: Visa renewal, Dec 2022", VISA22]]),
            P("harrods", "NBK-Harrods Visa Infinite", "Launched in 2025 with Harrods: Harrods Points, Visa Airport Companion and NBK Rewards.",
              s=["aff", "hnw"], lc="grow", st="new", ay="2025", o="P", at="Harrods, Visa", neo=[0, "Visa."], src=[["2025 Annual Report", AR25], ["NBK: credit cards", CREDIT]]),
            P("kac", "NBK-Kuwait Airways & NBK-KPC Visa cards", "Oasis Club Visa Infinite and Visa Signature cards earning Kuwait Airways miles, and a Visa Infinite for oil-sector employees with KPC; the 2026 summer campaign with Visa paid up to KD 500 on flights.",
              s=["aff"], lc="everyday", o="P", at="Kuwait Airways, KPC, Visa", neo=[0, "Visa."], src=[["NBK: credit cards", CREDIT], ["NBK newsroom: summer campaign, Jul 2026", NEWS]]),
            P("visacredit", "Visa Infinite, Signature & Platinum", "Visa Infinite, Visa Signature, Visa Platinum and a 0%-interest Visa Platinum, with NBK Miles, Visa Airport Companion and SmartDelay; APR 12% on all NBK credit cards.",
              s=["con", "aff"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["NBK: credit cards", CREDIT], ["NBK: card services", CARDSERV]]),
            P("diners", "Diners Club Credit Card", "A travel card with worldwide lounge access, free for the first year.",
              s=["aff"], lc="everyday", o="P", at="Diners Club", neo=[0, "Diners Club."], src=[["NBK: credit cards", CREDIT]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Mastercard credit", "blurb": "Aura, Miles, World.", "div": "nbk", "rev": "consumer", "products": [
            P("aura", "NBK-Aura World Mastercard", "A co-brand with Alshaya Group's Aura loyalty: up to 8% back in points at more than 50 Aura brands, 4% at The Avenues and 1% elsewhere, with Mastercard Travel Pass, Priceless offers and travel cover; a Platinum Mastercard prepaid version pays up to 6% (2025 ⚠ launch year).", short="Aura (Mastercard)",
              s=["con", "aff"], lc="everyday", st="new", ay="2025", o="P", at="Alshaya Group", neo=[2, "World Mastercard."],
              mc="Mastercard's anchor at NBK: the retail co-brand the bank says customers adopted quickly.",
              src=[["NBK: credit cards", CREDIT], ["Kuwait Times: Aura cards, Sep 2026", AURAKT], ["2025 Annual Report", AR25]]),
            P("miles", "NBK Miles World Mastercard", "A travel card earning NBK Miles, with LoungeKey through Mastercard Travel Pass, Priceless Specials and up to US$500,000 travel accident cover.",
              s=["aff"], lc="everyday", o="P", at="Mastercard", neo=[2, "World Mastercard."], src=[["NBK: Miles World Mastercard", MILES]]),
            P("worldmc", "World, Platinum, UEFA & Titanium Mastercards", "World Mastercard, Platinum Mastercard with Purchase Protection, the UEFA Champions League World Mastercard (March 2021 ⚠) and Titanium and Laki Titanium cards; a June 2025 campaign gave 115 travel vouchers to top foreign spenders on NBK Mastercards.",
              s=["con", "youth"], lc="borrow", ay="Mar 2021", o="P", at="Mastercard", neo=[2, "Mastercard."],
              src=[["NBK: credit cards", CREDIT], ["Kuwait Times: Mastercard campaign, Jun 2025", MC25], ["Mastercard: UEFA cards, Mar 2021 ⚠", MCUCL]]),
        ]},
        {"id": "2.3", "ic": "wallet", "name": "Debit, prepaid & wallets", "blurb": "KNET at home, Apple Pay.", "div": "nbk", "rev": "consumer", "products": [
            P("debit", "Debit cards", "Standard, Plus, Al Shabab (youth) and Zeina (children) debit cards working on KNET at home and at ATMs with the Cirrus sign abroad ⚠ scheme brand not stated.", short="Debit (KNET, Cirrus ⚠)",
              s=["con", "youth"], lc="everyday", o="B", at="KNET", neo=[1, "KNET at home; Cirrus abroad ⚠."], src=[["NBK: debit card", DEBITCARD], ["NBK: debit cards", DEBIT]]),
            P("premdebit", "Privilege & Thahabi Visa Platinum Debit", "Premium debit for Privilege and Thahabi clients, with up to KD 3,000 cash a day and KD 20,000 local spend.",
              s=["aff"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["NBK: Privilege debit", PRIVILEGE]]),
            P("prepaid", "Prepaid cards", "Aura and UEFA Platinum Mastercard prepaid; 247 Cashback, Avios Visa Signature, Oasis Club and Al Shabab Visa prepaid; KWD, foreign-currency, 15-currency and gift cards (networks not stated ⚠).",
              s=["con", "youth"], lc="everyday", o="P", at="Mastercard, Visa", neo=[1, "Split: Mastercard and Visa."], src=[["NBK: prepaid cards", PREPAID]]),
            P("wallets", "Apple Pay, Google Pay & Samsung Wallet", "All three wallets on NBK cards; Apple Pay went live in Kuwait on 6 December 2022 after tests with KNET, and acquirers route Kuwaiti Apple Pay through KNET.",
              s=["con", "youth"], lc="everyday", ay="Dec 2022", o="P", at="Apple, Google, Samsung, KNET", neo=[1, "Tokens on every network."],
              src=[["NBK: card services", CARDSERV], ["CBK: Apple Pay, Dec 2022", APPLEPAY], ["Checkout.com: Apple Pay via KNET", KNETAP]]),
        ]},
        {"id": "2.4", "ic": "briefcase-business", "name": "Commercial cards", "blurb": "Visa, virtual cards.", "div": "nbk", "rev": "corporate", "products": [
            P("commercial", "Commercial credit & prepaid cards", "Free-for-life commercial credit (1.5% cashback) and prepaid (1%) cards, virtual cards, real-time alerts, dashboards and accounting integration, with statements through Visa Spend Clarity for Business; corporate credit and debit cards too.", short="Commercial cards (Visa)",
              s=["sme", "corp"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."],
              mc="Virtual cards and spend controls are where Mastercard's commercial tools would compete.",
              src=[["NBK: commercial cards", COMM]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acceptance", "blurb": "POS, gateway, UPayments.", "div": "upay", "rev": "corporate", "products": [
            P("acquiring", "POS, Soft POS & payment gateway", "Merchant acquiring with five kinds of POS terminal, Soft POS on Android phones up to KD 250, and an online gateway taking KNET, Visa, Mastercard, Diners Club, Apple Pay, Samsung Pay and Google Pay.",
              s=["sme"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["NBK: payment services", PAYSERV]]),
            P("upayments", "UPayments", "A Kuwaiti payment service provider and e-commerce platform, 51% owned since 2025 ⚠: URent rent collection and UStore online shops with a built-in gateway, for NBK customers only.",
              s=["sme"], lc="move", st="new", ay="2025", o="A", neo=[None, "Networks not stated."],
              mc="Merchant tools and checkout for a fintech NBK now controls.",
              src=[["NBK: UPayments", UPAY], ["Zawya: UPayments stake", UPAYZ]]),
            P("posfin", "POS Financing", "Kuwait's first point-of-sale financing for SMEs: up to KD 30,000 against card sales through NBK terminals (2025).",
              s=["sme"], lc="borrow", st="new", ay="2025", neo=[0, ""], src=[["2025 Annual Report", AR25], ["Kuwait Times: consumer and digital, Dec 2025", CDB]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Instant & cross-border", "blurb": "WAMD, AFAQ.", "div": "nbk", "rev": "consumer", "products": [
            P("wamd", "WAMD instant payments", "KNET's account-to-account scheme under the Central Bank of Kuwait, in the NBK app since 30 June 2024: send, receive and request money by mobile number. WAMD passed a million accounts in its first year ⚠.", short="WAMD (KNET)",
              s=["con", "youth"], lc="move", ay="Jun 2024", o="P", at="KNET", neo=[0, "KNET's rail."],
              mc="Phone-number transfers on WAMD compete with card-based person-to-person payments.",
              src=[["Kuwait Times: NBK launches WAMD, Jun 2024", WAMDNBK], ["Business Wire: WAMD one million, May 2025 ⚠", WAMD1M]]),
            P("afaq", "AFAQ & cross-border payments", "Roll-out of AFAQ, the GCC's cross-border instant payment system, and upgraded cross-border payment processors in Kuwait and abroad, as part of an ISO 20022 programme (2025).",
              s=["con", "corp"], lc="move", st="new", ay="2025", o="P", at="GCC central banks", neo=[0, ""],
              mc="Cross-border flows across 13 countries are open ground for Mastercard Move.",
              src=[["2025 Annual Report", AR25]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: a real-time fraud platform and a 2018 Mastercard biometrics first, Face-tech onboarding with Kuwait Mobile ID, data and AI, banking-as-a-service for fintechs, and points programmes with Aura, Avios, Harrods and Kuwait Airways.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & identity", "blurb": "Real-time fraud, e-KYC.", "div": "group", "rev": "consumer", "products": [
            P("fraud", "Real-time fraud platform", "A new enterprise fraud platform with cross-channel correlation, instant scoring and real-time blocking (2025); Global Finance's best information security and fraud management in the Middle East, 2026.",
              s=["con", "sme"], lc="everyday", st="new", o="B", neo=[0, "NBK's own."],
              mc="Network-level fraud scores would add to an in-house platform.",
              src=[["2025 Annual Report", AR25], ["NBK: About", ABOUT]]),
            P("idcheck", "Biometric card & Identity Check", "In May 2018 NBK and Mastercard ran the GCC's first fingerprint-sensor card trial, and NBK became the first bank in the Middle East and Africa to offer Mastercard Identity Check for online purchases ⚠ current use not confirmed.",
              s=["con"], lc="everyday", ay="May 2018", o="P", at="Mastercard", neo=[3, "Mastercard's own ⚠ status."],
              src=[["Mobile ID World: biometric trial, May 2018", MCBIO], ["Mastercard: biometric solutions, May 2018 ⚠", MCBIO2]]),
            P("ekyc", "Digital onboarding & e-KYC", "Account opening entirely in the app with Kuwait Mobile ID (2025), Face-tech liveness and facial recognition, and digital KYC updates for retail and corporate customers.",
              s=["con", "youth"], lc="open", st="new", ay="2025", o="B", neo=[0, ""], src=[["2025 Annual Report", AR25]]),
        ]},
        {"id": "3.2", "ic": "brain", "name": "Data & AI", "blurb": "Customer 360, next best action.", "div": "group", "rev": "consumer", "products": [
            P("data", "Data, analytics & personalisation", "Customer 360 analytics, predictive models and Next Best Action to pick the customer, time, offer and channel, and a notification engine across push, SMS, WhatsApp and Apple Business Chat.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["2025 Annual Report", AR25]]),
        ]},
        {"id": "3.3", "ic": "code-xml", "name": "APIs & fintech", "blurb": "Virtual IBANs, BaaS.", "div": "nbk", "rev": "corporate", "products": [
            P("baas", "Banking-as-a-service", "Virtual IBANs, APIs and QR cardless 'ATM as a service' for fintechs, starting with AZ eWallet; an API layer built for open-banking rules in Kuwait and the GCC.",
              s=["sme"], lc="open", st="new", o="B", neo=[0, ""],
              mc="Card issuing and payouts for fintech partners are not yet part of the offer.",
              src=[["NBK newsroom: fintech, Jul 2026", NEWS], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Rewards & instalments", "blurb": "Aura, Avios, FlexiPay.", "div": "nbk", "rev": "consumer", "products": [
            P("rewards", "Rewards & partner points", "NBK Rewards and NBK Miles, KWT points, Kuwait Airways Oasis Club miles, Avios, Harrods Points and Aura points, with partner offers at IKEA, Xcite and The Bicester Collection.",
              s=["con", "aff"], lc="grow", o="P", at="Alshaya, Avios, Harrods, Kuwait Airways", neo=[1, "Aura and Miles on Mastercard; the rest on Visa."],
              mc="Mastercard offers could deepen the Aura programme it already carries.",
              src=[["NBK: credit cards", CREDIT], ["2025 Annual Report", AR25]]),
            P("flexipay", "NBK FlexiPay", "Pay card purchases over 12 months at 0% interest through online banking, on eligible Visa and Mastercard credit cards.",
              s=["con"], lc="borrow", o="B", neo=[1, "Works on both networks."], src=[["NBK: card services", CARDSERV]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: Kuwait's largest retail bank, Weyay for the young, corporate and transaction banking with over 30% of trade finance, Boubyan for Islamic banking, NBK Wealth, and banks in Egypt and the Gulf.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Consumer banking", "blurb": "Largest share in Kuwait.", "div": "nbk", "rev": "consumer", "products": [
            P("accounts", "Accounts & segments", "The largest retail market share and highest customer penetration in Kuwait: Al Jawhara prize savings, the eSavings account with round-ups, and Privilege, Thahabi, Plus, Shabab and Retiree segments.",
              s=["con", "aff"], lc="everyday", neo=[1, "KNET and Visa debit; Cirrus abroad ⚠."], src=[["2025 Annual Report", AR25], ["NBK newsroom", NEWS]]),
            P("homefin", "Consumer, housing & Al Manzel loans", "Consumer, auto and housing loans and Al Manzel home-renovation finance with more than 40 partners; a mortgage law is awaited.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Kuwait Times: consumer and digital, Dec 2025", CDB], ["2Q 2026 call script", CALL]]),
        ]},
        {"id": "4.2", "ic": "rocket", "name": "Weyay Bank", "blurb": "Kuwait's first digital bank.", "div": "weyay", "rev": "consumer", "products": [
            P("weyay", "Weyay Bank", "Kuwait's first fully digital bank, by NBK, for customers from 15: SELECT student prepaid card, Weyay Aura prepaid with Alshaya, a multicurrency card and Kuwait's first end-to-end digital loan (February 2025); customers aged 15–23 more than doubled.",
              s=["youth"], lc="open", st="new", ay="2022 ⚠", o="B", neo=[None, "Card networks not stated."],
              mc="A young, card-first franchise whose networks are not public.",
              src=[["Weyay Bank", WEYAY], ["Weyay: prepaid cards", WEYAYPRE], ["2025 Annual Report", AR25]]),
            P("jeel", "Jeel by Weyay", "A debit card and app for children aged 8 to 14 under parental control, named most innovative product in MENA.",
              s=["youth"], lc="open", st="new", o="B", neo=[None, "Network not stated."], src=[["Weyay: Jeel", JEEL], ["Kuwait Times: consumer and digital, Dec 2025", CDB]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Corporate & transaction banking", "blurb": "Over 30% of trade finance.", "div": "nbk", "rev": "corporate", "products": [
            P("corporate", "Corporate & transactional banking", "Primary banker to Kuwait's blue chips and at least 75% of foreign companies there, more than 30% of trade finance, project finance for Vision 2035, and cash management named Kuwait's best for a fourth year in 2026.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["2Q 2026 investor presentation", IP], ["NBK newsroom", NEWS]]),
        ]},
        {"id": "4.4", "ic": "landmark", "name": "Islamic banking", "blurb": "Boubyan, 60.4%.", "div": "boubyan", "rev": "islamic", "products": [
            P("boubyan", "Boubyan Bank", "NBK's Islamic bank, consolidated in 2012 and 60.4% owned, focused on affluent and high-net-worth clients and large and mid-sized companies; about 11.5% of Kuwait's banking assets in 2025 ⚠ chart reading.",
              s=["con", "corp"], lc="everyday", o="A", neo=[None, "Not covered here."], src=[["2Q 2026 investor presentation", IP]]),
        ]},
        {"id": "4.5", "ic": "gem", "name": "NBK Wealth", "blurb": "KD 63m profit in 2025.", "div": "wealth", "rev": "wealth", "products": [
            P("wealth", "NBK Wealth", "Private banking and asset management under one brand, with booking centres across the network and credit cards for high-net-worth clients; net profit KD 63 million and assets KD 1.4 billion in 2025.",
              s=["hnw"], lc="grow", neo=[0, ""], src=[["2Q 2026 investor presentation", IP]]),
        ]},
        {"id": "4.6", "ic": "globe", "name": "International", "blurb": "Egypt and the Gulf.", "div": "intl", "rev": "intl", "products": [
            P("egypt", "NBK-Egypt", "53 branches, with a retail digital transformation under way; net profit EGP 4.2 billion (about KD 26.1 million) in H1 2026.",
              s=["con", "corp"], lc="everyday", neo=[None, "Nothing public on networks."], src=[["Kuwait Times: NBK-Egypt H1 2026", EGY], ["2Q 2026 investor presentation", IP]]),
            P("gulf", "Gulf, Europe & beyond", "Branches in Bahrain (H1 2026 profit BD 60.5 million), the UAE, Saudi Arabia, Iraq and Lebanon, NBK France mortgages and Swiss private banking, serving GCC clients active abroad.",
              s=["corp", "hnw"], lc="beyond", neo=[0, ""], src=[["GDN: NBK-Bahrain H1 2026", BAH], ["2Q 2026 investor presentation", IP]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach NBK: the mobile app carrying about 90% of transactions, 70 Kuwaiti branches with ITMs and ATMs, and the partners whose brands sit on its cards.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Mobile & online", "blurb": "90% of transactions.", "div": "nbk", "rev": "consumer", "products": [
            P("app", "NBK Mobile Banking & Online Banking", "About 90% of transactions, more than 200 services (50 added in 2025), a 4.7 rating, in-app card issuance and 'Tap to Add Card + PIN'; online banking redesigned in 2025.",
              s=["con", "aff", "youth"], lc="everyday", neo=[0, ""], src=[["Kuwait Times: consumer and digital, Dec 2025", CDB], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "70 branches in Kuwait.", "div": "nbk", "rev": "consumer", "products": [
            P("branches", "Branches, ITMs & ATMs", "70 branches in Kuwait being redesigned, interactive teller machines (the first in London in 2026), digital safe-deposit boxes and ATMs moving to NCR CX for cardless journeys; call centre 1801801.",
              s=["con", "aff"], lc="everyday", neo=[0, ""], src=[["NBK newsroom", NEWS], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partners", "blurb": "Alshaya, Harrods, Kuwait Airways.", "div": "nbk", "rev": "consumer", "products": [
            P("partners", "Co-brand & ecosystem partners", "Alshaya's Aura, Harrods, Kuwait Airways, KPC, Avios, IKEA and Xcite on the card side, and fintechs such as AZ eWallet on the banking-as-a-service side.",
              s=["con", "aff"], lc="beyond", o="P", neo=[1, "Aura on Mastercard; the others on Visa."], src=[["NBK: credit cards", CREDIT], ["NBK newsroom", NEWS]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at NBK", "blurb": "A strong second to Visa.", "products": [
        P("mcatnbk", "Mastercard at NBK", "Visa is NBK's lead scheme: a seven-year renewal from December 2022, the KWT, Harrods, Kuwait Airways and KPC cards, premium debit and commercial cards. KNET runs domestic debit and WAMD. Mastercard holds the Aura co-brand with Alshaya, the Miles, World, Platinum and UEFA cards, Cirrus on standard debit ⚠, and a 2018 biometrics first.",
          s=["con"], div="group", rev="consumer", mc="The relationship this map is drawn for.",
          src=[["GCC Business News: Visa renewal, Dec 2022", VISA22], ["NBK: credit cards", CREDIT], ["Kuwait Times: Mastercard campaign, Jun 2025", MC25]]),
    ]},
    {"id": "pillar-market", "name": "Kuwaiti banking", "blurb": "KNET, WAMD, a new tax.", "products": [
        P("market", "The Kuwaiti market", "NBK holds more than 30% of banking assets; Kuwait Finance House leads Islamic banking. KNET switches domestic cards and runs WAMD, Apple Pay is routed through it, a 15% tax applies from 2025, a mortgage law is pending, and a 2026 regional conflict slowed projects and travel spending.",
          s=["con"], div="group", rev="consumer", src=[["2Q 2026 investor presentation", IP], ["2Q 2026 call script", CALL], ["CBK: Apple Pay, Dec 2022", APPLEPAY]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
