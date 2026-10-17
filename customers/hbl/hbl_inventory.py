"""HBL's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the H1 2026 results release (August 2026), the 2025
results (18 February 2026), the 2025 annual report and the December 2025 investor presentation. ``neo`` is the
Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard,
1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H126 = "https://www.hbl.com/news-and-media/hbl-declares-h126-profit-before-tax-of-rs-73.1-billion-reflecting-continued-client-focus-and-disciplined-execution-of-strategy"
FY25 = "https://www.hbl.com/news-and-media/hbl-posts-2025-profit-before-tax-of-rs-148.1-billion-up-23-yoy-while-continuing-to-scale-with-profitability"
AR25 = "https://www.hbl.com/assets/documents/HBL_Annual_Report_2025.pdf"
IP25 = "https://www.hbl.com/assets/documents/Investor_Presentation_-_Dec_25.pdf"
MGMT = "https://www.hbl.com/about-us/management"
BOARD = "https://www.hbl.com/about-us/board-of-directors"
HIST = "https://www.hbl.com/about-us/history"
CORP = "https://www.hbl.com/about-us/corporate-information"
SHARE = "https://www.hbl.com/assets/documents/Categories_of_Shareholders_2025.pdf"
MCBDC = "https://www.mastercard.com/news/eemea/en/newsroom/press-releases/en/2025-1/august/hbl-in-partnership-with-mastercard-launches-business-debit-cards-to-empower-pakistan-s-smes"
HBLBDC = "https://www.hbl.com/news-and-media/hbl-in-partnership-with-mastercard-launches-business-debit-cards-to-empower-pakistans-smes"
BIZDC = "https://www.hbl.com/personal/cards/debit-cards/hbl-business-debitcard"
WORLDDC = "https://www.hbl.com/personal/cards/debit-cards/hbl-world-debitcard"
DCOV = "https://www.hbl.com/personal/cards/debit-cards/debit-cards-overview"
CCOV = "https://www.hbl.com/personal/cards/credit-cards/credit-cards-overview"
PLAT = "https://www.hbl.com/personal/cards/credit-cards/platinum-credit-card"
KFS = "https://www.hbl.com/assets/documents/Jan_2024_English_KFS.pdf"
FUEL = "https://www.hbl.com/personal/cards/credit-cards/fuel-saver-credit-card"
PAYDC = "https://www.hbl.com/personal/cards/debit-cards/hbl-pay-debitcard"
GPAY = "https://www.hbl.com/personal/cards/google-pay"
PAYPAKDC = "https://www.hbl.com/personal/cards/debit-cards/hbl-paypak-debit-card"
USDDC = "https://www.hbl.com/personal/cards/debit-cards/hbl-visa-usd-debitcard"
COBADGE = "https://www.hbl.com/news-and-media/hbl-unveils-hbl-paypak-unionpay-co-badge-card-empowering-domestic-payment-schemes-with-global-connectivity"
COSIGN = "https://www.hbl.com/news-and-media/hbl-to-launch-unionpay-paypak-co-badge-debit-card"
UPIMOU = "https://www.hbl.com/news-and-media/hbl-and-unionpay-international-sign-mou-on-strategic-cooperation-to-strengthen-digital-payments"
MPOS = "https://www.thefridaytimes.com/31-Mar-2022/hbl-partners-with-visa-to-enable-mobile-pos-services-for-its-clients-in-pakistan"
PITB = "https://pitb.gov.pk/node/10116"
SHESNEXT = "https://www.hbl.com/news-and-media/the-shes-next-program-returns-to-pakistan-to-empower-women-led-businesses-drive-economic-growth"
KQR = "https://www.hbl.com/personal/konnect/konnect-account/konnect-qr-payments"
KCARD = "https://www.hbl.com/personal/konnect/konnect-account/konnect-debit-card"
KG2P = "https://www.hbl.com/personal/konnect/g2p/about-g2p"
RAAST = "https://www.hbl.com/personal/digital-banking/raast"
SBPRAAST = "https://www.sbp.org.pk/DFS/Raast-P2P.html"
APS26 = "https://www.sbp.org.pk/assets/document/publications/Annual-Payment-Systems-Review-FY26.pdf"
MFBCC = "https://www.app.com.pk/?p=1283751"
AKDNMFB = "https://the.akdn/en/where-we-work/south-asia/pakistan/microfinance-pakistan"
APPLEPAY = "https://www.techjuice.pk/apple-pay-pakistan-ios-27-beta-paypak-code-integration-evidence/"
EASYPAISA = "https://propakistani.pk/2025/01/28/easypaisa-becomes-pakistans-first-digital-bank-to-receive-commercial-approval-for-regular-operations/amp/"
BOPMC = "https://en.dailypakistan.com.pk/13-Jul-2026/mastercard-bank-of-punjab-expand-strategic-partnership-to-boost-pakistans-digital-economy"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · owners · heritage", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Pakistan's largest lender and customer base, an Rs 8 trillion balance sheet, AKFED as majority owner since 2004, a bank founded in 1941, a Temenos core being rolled out, and the 'Scale with Profitability' strategy.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "40 million customers, Rs 8tn.", "div": "hbl", "rev": "treasury", "products": [
            P("balance", "Balance sheet & earnings", "40 million customers; balance sheet Rs 8.0 trillion, deposits Rs 5.9 trillion and advances Rs 2.1 trillion at 30 June 2026; profit after tax Rs 34.5 billion in the half and Rs 66.8 billion in 2025 (profit before tax Rs 148.1 billion, up 23%); total CAR 17.2%; rated AAA / A-1+ by VIS; domestic deposit share 12.65% at December 2025.",
              s=["con"], neo=[0, ""], src=[["HBL: H1 2026 results", H126], ["HBL: 2025 results, Feb 2026", FY25], ["HBL annual report 2025", AR25]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Owners & leadership", "blurb": "AKFED 56.6%; Nassir Salim CEO.", "div": "hbl", "rev": "treasury", "products": [
            P("owners", "Ownership & listing", "Listed on the Pakistan Stock Exchange (HBL); the Aga Khan Fund for Economic Development owns 56.58% and took control at privatisation in February 2004; the government sold its last 41.5% in April 2015. Market value about US$1.5 billion in March 2026.",
              s=["corp"], o="I", neo=[0, ""], src=[["HBL: shareholders 2025", SHARE], ["HBL: history", HIST], ["HBL investor presentation, Dec 2025", IP25]]),
            P("leadership", "Board & management", "Chairman Sultan Ali Allana (since 2004) and President & CEO Muhammad Nassir Salim (since March 2024); CFO Irfan Ahmed Meer, Head Retail Aalishaan Zaidi, CTO Muhammad Faisal Anwar, Chief Strategy & Transformation Officer Abrar Ahmed Mir; Aamir Kureshi has fronted the card-scheme launches. About 21,800 staff.",
              s=["corp"], neo=[0, ""], src=[["HBL: board", BOARD], ["HBL: management", MGMT], ["HBL annual report 2025", AR25]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & brand", "blurb": "Founded 1941; new look 2026.", "div": "hbl", "rev": "retail", "products": [
            P("brand", "Heritage & brand", "Founded in 1941 and moved to Pakistan in 1947 at Jinnah's request as the country's first commercial bank; nationalised in 1974 and privatised in 2004. A refreshed identity with a 'Momentum' device rolled out from February 2026; title sponsor of the Pakistan Super League through 2027.",
              s=["con"], o="I", st="flux", neo=[0, ""], src=[["HBL: history", HIST], ["HBL: 2025 results, Feb 2026", FY25]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & data", "blurb": "Temenos core in 480+ branches.", "div": "hbl", "rev": "treasury", "products": [
            P("tech", "Core, data & AI", "Moving to Temenos Transact: 24 branches by end-2025 and more than 480 by June 2026. A data lake for KYC and faster app loan approvals, cloud upgrades, a 24x7 security operations centre, and generative AI used in marketing and recruitment; no AI targets published ⚠.",
              s=["corp"], st="flux", o="P", at="Temenos", neo=[0, ""], src=[["HBL: H1 2026 results", H126], ["HBL annual report 2025", AR25]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "Scale with Profitability.", "div": "hbl", "rev": "treasury", "products": [
            P("strategy", "Scale with Profitability", "A client-first plan built on current accounts, Islamic branches (35% of the network), SME, agriculture and digital payments; 2025–26 deals include Mastercard business debit, a PayPak–UnionPay co-badge card, a UnionPay strategic MoU, exits from Belgium, Oman and Mauritius, and the HBL Microfinance stake raised to 90.83%.",
              s=["corp"], st="new", neo=[0, ""], src=[["HBL: 2025 results, Feb 2026", FY25], ["HBL annual report 2025", AR25], ["HBL–UnionPay MoU, Sep 2026", UPIMOU]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: Pakistan's largest debit issuer on Mastercard, Visa, UnionPay and PayPak; a third of the country's credit-card spend, mostly on Visa; the largest POS network; Raast instant payments; phone tokens; and remittances and the China corridor.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit cards", "blurb": "6.4 million, four networks.", "div": "hbl", "rev": "retail", "products": [
            P("debit", "HBL DebitCards", "Pakistan's largest debit issuer: 6.4 million cards issued, one in five in the country, and Rs 270 billion of spend in 2025 (about 15% of the market). Classic and Gold come on Mastercard or Visa; the range also includes UnionPay, PayPak and a Visa USD card for freelancers. The split by network is not published ⚠.", short="Debit (four networks)",
              s=["con", "aff"], lc="everyday", o="P", at="Mastercard, Visa, UnionPay, 1LINK", neo=[1, "One of four networks ⚠ split unknown."],
              mc="The largest debit book in Pakistan, shared four ways.",
              src=[["HBL: debit cards", DCOV], ["HBL annual report 2025", AR25], ["HBL: Visa USD debit", USDDC]]),
            P("world", "HBL World DebitCard", "Described as Pakistan's most premium debit card, for high-net-worth customers: Mastercard World, with lounge access through Mastercard Airport Pass and Priceless experiences. Launch date not published ⚠.", short="World debit (Mastercard)",
              s=["aff"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard World."], src=[["HBL: World DebitCard", WORLDDC]]),
            P("bizdebit", "HBL Business DebitCard", "Classic and World Business debit cards for SMEs and sole proprietors, launched with Mastercard on 27 August 2025 (Mastercard's J.K. Khalil and HBL's Muhammad Nassir Salim), with Easy Savings Specials and Travel Pass; World Business costs PKR 22,000 a year from year two.", short="Business debit (Mastercard)",
              s=["sme"], lc="everyday", st="new", ay="Aug 2025", o="P", at="Mastercard", neo=[2, "Mastercard Business."],
              mc="The newest joint launch, and a base for commercial cards.",
              src=[["Mastercard: HBL business debit, Aug 2025", MCBDC], ["HBL: business debit launch", HBLBDC], ["HBL: Business DebitCard", BIZDC]]),
            P("unionpay", "UnionPay debit & PayPak co-badge", "UnionPay debit since 2013 with more than 1.8 million cards issued, and a PayPak–UnionPay co-badge debit card signed in November 2025 and launched on 15 July 2026 with the SBP Governor present; a strategic MoU with UnionPay International followed in Shanghai on 17 September 2026.", short="UnionPay & co-badge",
              s=["con", "corp"], lc="everyday", st="new", ay="Jul 2026", o="P", at="UnionPay, 1LINK", neo=[0, "UnionPay and PayPak."],
              mc="UnionPay is HBL's fastest-moving scheme partner in 2025–26.",
              src=[["HBL: co-badge launch, Jul 2026", COBADGE], ["HBL: co-badge agreement, Nov 2025", COSIGN], ["HBL–UnionPay MoU, Sep 2026", UPIMOU]]),
            P("paypak", "HBL PayPak DebitCard", "A domestic-only card on 1LINK's PayPak scheme at a lower annual fee, for use at ATMs and merchants within Pakistan.",
              s=["con", "unb"], lc="everyday", o="P", at="1LINK", neo=[0, "PayPak."], src=[["HBL: PayPak debit", PAYPAKDC]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "One rupee in three.", "div": "hbl", "rev": "retail", "products": [
            P("credit", "HBL CreditCards", "Green, Gold and FuelSaver cards: one rupee in every three spent on credit cards in Pakistan is on an HBL card (39% share); Rs 418 billion of spend (up 27%), a Rs 54 billion book and 90,000 new cards in 2025, more than half booked in HBL Mobile. The fact sheet lists Visa and Mastercard; current card art is Visa ⚠.", short="Credit (mostly Visa ⚠)",
              s=["con"], lc="borrow", o="P", at="Visa, Mastercard", neo=[1, "Visa and Mastercard ⚠ mostly Visa."],
              mc="Pakistan's biggest credit book, where Mastercard looks thin.",
              src=[["HBL annual report 2025", AR25], ["HBL: credit card fact sheet, Jan 2024", KFS], ["HBL: FuelSaver", FUEL]]),
            P("platinum", "HBL Platinum CreditCard", "Visa Platinum with Visa Airport Companion lounge access, three times reward points abroad and Visa offers.",
              s=["aff"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["HBL: Platinum CreditCard", PLAT], ["HBL: credit cards", CCOV]]),
        ]},
        {"id": "2.3", "ic": "store", "name": "Merchant acquiring", "blurb": "26% of Pakistan's POS spend.", "div": "hbl", "rev": "retail", "products": [
            P("acquiring", "HBL merchant acquiring & SmartPOS", "Pakistan's largest POS network: about 40,000 devices in more than 250 cities; throughput Rs 604 billion in 2025 (up 32%), more than 26% of the country's POS volume; smaller towns make up 16% of spend.",
              s=["sme"], lc="move", o="B", neo=[1, "Accepts every network."],
              mc="Acquirer risk and merchant data for the country's biggest POS estate.",
              src=[["HBL annual report 2025", AR25], ["HBL investor presentation, Dec 2025", IP25]]),
            P("mpos", "mPOS & PayZen gateway", "Phone-based card acceptance built with Visa (signed April 2021, launched March 2022) for couriers and e-commerce, and merchant processing for the Punjab government's PayZen on Visa's gateway (June 2024).",
              s=["sme", "corp"], lc="move", ay="Mar 2022", o="P", at="Visa, PITB", neo=[0, "Visa."],
              src=[["Friday Times: HBL mPOS with Visa, Mar 2022", MPOS], ["PITB: PITB, HBL and Visa, Jun 2024", PITB]]),
        ]},
        {"id": "2.4", "ic": "zap", "name": "Raast instant payments", "blurb": "Free, by mobile number.", "div": "hbl", "rev": "retail", "products": [
            P("raast", "Raast on HBL Mobile & Konnect", "SBP's instant-payment system through HBL Mobile and the Konnect app: a Raast ID on the mobile number, up to PKR 200,000 a day, free. Nationally Raast carried 2,755 million payments worth PKR 80 trillion in the year to June 2026, with merchant payments up from 4.9 million to 182.5 million.",
              s=["con", "unb"], lc="move", o="P", at="State Bank of Pakistan", neo=[0, "SBP's Raast."],
              mc="Account-to-account payments growing far faster than cards.",
              src=[["HBL: Raast", RAAST], ["SBP: Raast P2P partners", SBPRAAST], ["SBP: payment systems review FY26", APS26]]),
        ]},
        {"id": "2.5", "ic": "smartphone", "name": "Tokens & wallets", "blurb": "HBL Pay, Google Pay.", "div": "hbl", "rev": "retail", "products": [
            P("hblpay", "HBL Pay", "Tap-to-pay inside HBL Mobile on Android, tokenising HBL Visa and Mastercard debit and credit cards to the standards of both networks.",
              s=["con"], lc="everyday", o="B", neo=[1, "Visa and Mastercard tokens."], src=[["HBL: HBL Pay", PAYDC]]),
            P("gpay", "Google Pay & Apple Pay", "HBL cards can be added to Google Wallet. Apple Pay is not live in Pakistan; an activation option in the HBL app and PayPak code in iOS 27 have been reported ⚠.",
              s=["con"], lc="everyday", st="new", o="P", at="Google", neo=[1, "Tokens on each card's network."], src=[["HBL: Google Pay", GPAY], ["TechJuice: iOS 27 PayPak code, Sep 2026", APPLEPAY]]),
        ]},
        {"id": "2.6", "ic": "earth", "name": "Remittances & China", "blurb": "RMB corridor, FX platform.", "div": "intl", "rev": "intl", "products": [
            P("remit", "Remittances, RMB & FX", "Home remittances and G2P are 'healthy contributors' to income (H1 2026); branches in Beijing (2021) and Urumqi make HBL one of three RMB intermediaries in MENA and South Asia; HBL Infinity FX volumes US$2.6 billion in 2025; adviser on Pakistan's first Panda bond.",
              s=["corp", "con"], lc="move", o="B", neo=[0, ""],
              mc="Inbound remittances are untested ground for Mastercard Move.",
              src=[["HBL: H1 2026 results", H126], ["HBL annual report 2025", AR25]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: 3D Secure on each scheme and card controls in the app, offers from Mastercard, Visa and HBL's own merchants, and a WhatsApp and API layer serving 6,500 billers, with 14 million service contacts a year.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "3D Secure on every scheme.", "div": "hbl", "rev": "retail", "products": [
            P("security", "Card security & controls", "3D Secure on each scheme (Mastercard Identity Check, Visa Secure, UnionPay SecurePay, 1LINK for PayPak), chip and PIN, SMS alerts, and switches in HBL Mobile for e-commerce, international, ATM and contactless use; 466,062 complaints handled in 2025. No Mastercard fraud product named ⚠.",
              s=["con", "sme"], lc="everyday", o="B", neo=[1, "Identity Check on Mastercard cards only."],
              mc="No scam or account-to-account fraud scoring in public view.",
              src=[["HBL: Business DebitCard", BIZDC], ["HBL: debit cards", DCOV], ["HBL annual report 2025", AR25]]),
        ]},
        {"id": "3.2", "ic": "gift", "name": "Rewards & offers", "blurb": "Easy Savings, Visa Offers.", "div": "hbl", "rev": "retail", "products": [
            P("offers", "Deals, rewards & scheme offers", "HBL Deals & Discounts and credit-card reward points; Mastercard Easy Savings Specials and Priceless on business and World debit cards; Visa Offers and Visa Airport Companion on credit cards.",
              s=["con", "aff", "sme"], lc="grow", o="P", at="Mastercard, Visa", neo=[1, "Mastercard on debit, Visa on credit."],
              src=[["HBL: Business DebitCard", BIZDC], ["HBL: World DebitCard", WORLDDC], ["HBL: Platinum CreditCard", PLAT]]),
        ]},
        {"id": "3.3", "ic": "code-xml", "name": "APIs, billers & service", "blurb": "6,500 billers on WhatsApp.", "div": "hbl", "rev": "retail", "products": [
            P("apis", "Billers, APIs & service", "WhatsApp banking aggregates more than 6,500 billers; a 'Best Digital API' award; a digital customer-experience centre handling 14.4 million interactions in 2025; no open-banking programme published ⚠.",
              s=["con", "corp"], lc="everyday", neo=[0, ""], src=[["HBL annual report 2025", AR25], ["HBL investor presentation, Dec 2025", IP25]]),
            P("data", "Data & AI", "A data lake used for centralised KYC and quicker app loan approvals, generative AI in the HBLPSL 'FanTunes' campaign (144 million views) and an AI recruitment chatbot.",
              s=["con"], lc="everyday", st="new", neo=[0, ""], src=[["HBL annual report 2025", AR25]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: retail, Prestige and Islamic banking, Pakistan's leading consumer-loan book, SME and farm lending, corporate and transaction banking, Konnect's branchless banking and government payments, HBL Microfinance Bank, and an international network being trimmed.",
    "tiles": [
        {"id": "4.1", "ic": "users-round", "name": "Retail, Prestige & Islamic", "blurb": "608 Islamic branches.", "div": "hbl", "rev": "retail", "products": [
            P("retail", "Retail & Islamic banking", "Current accounts at the centre of strategy: domestic deposits a record Rs 5.1 trillion in June 2026 with a 42.5% current-account mix; 608 Islamic branches (35% of the network) after 143 conversions in 2025; HBL Nisa serves 1.1 million of 5.3 million women customers.",
              s=["con"], lc="open", neo=[1, "Debit on four networks."], src=[["HBL: H1 2026 results", H126], ["HBL annual report 2025", AR25]]),
            P("prestige", "Prestige & Premium", "Prestige for the wealthiest, through 56 lounges and 850 branches, and Premium (launched 2025) with 133,000 clients and Rs 386 billion of deposits; World debit on Mastercard, Platinum credit on Visa.",
              s=["aff"], lc="grow", st="new", neo=[1, "World debit Mastercard; Platinum Visa."], src=[["HBL annual report 2025", AR25]]),
        ]},
        {"id": "4.2", "ic": "hand-coins", "name": "Consumer lending", "blurb": "Rs 187bn book.", "div": "hbl", "rev": "retail", "products": [
            P("loans", "Personal loans & Ready Cash", "The largest consumer book among banks, Rs 187 billion in June 2026; personal loans and Ready Cash hold a 39% share (Rs 55 billion), with more than half of Ready Cash drawn in HBL Mobile.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["HBL: H1 2026 results", H126], ["HBL annual report 2025", AR25]]),
            P("auto", "Car & home finance", "Auto finance of Rs 47 billion with a 16.5% share and home finance of Rs 23 billion in 2025.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["HBL annual report 2025", AR25]]),
        ]},
        {"id": "4.3", "ic": "briefcase", "name": "SME & agriculture", "blurb": "Rs 152bn SME, Rs 110bn+ farm.", "div": "hbl", "rev": "retail", "products": [
            P("sme", "SME banking", "SME advances of Rs 152 billion and 6,000 new SME clients in 2025; 17 SME Trade Centres; Asaan Finance collateral-free loans; first bank past Rs 100 billion of SME lending; business debit cards with Mastercard.",
              s=["sme"], lc="borrow", neo=[1, "Business debit on Mastercard."],
              mc="Business debit opens the door to business credit and payment controls.",
              src=[["HBL annual report 2025", AR25], ["HBL: business debit launch", HBLBDC]]),
            P("agri", "Agriculture & HBL Zarai", "With HBL Microfinance, the largest lender to farmers: more than Rs 110 billion in June 2026; HBL Zarai Services served 9,175 farmers on 374,479 acres in 2025.",
              s=["farm"], lc="borrow", neo=[0, ""], src=[["HBL: H1 2026 results", H126], ["HBL annual report 2025", AR25]]),
        ]},
        {"id": "4.4", "ic": "building-2", "name": "Corporate & transaction banking", "blurb": "Rs 23.8tn cash throughput.", "div": "hbl", "rev": "corp", "products": [
            P("corporate", "Corporate & investment banking", "Average corporate advances of about Rs 900 billion; 23 investment-banking deals in 2025 including the Rs 1.23 trillion power-sector syndication; HBL Symphony fixed-income portal Rs 3.94 trillion.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["HBL annual report 2025", AR25]]),
            P("cashmgmt", "Cash management & HBL Pay Business", "Throughput of Rs 23.8 trillion in 2025 (up 23%) through the HBL Pay Business Banking platform and a new business app; transaction banking started in the Maldives.",
              s=["corp", "sme"], lc="move", o="B", neo=[0, ""],
              mc="Commercial cards and virtual cards are absent from the corporate offer.",
              src=[["HBL annual report 2025", AR25]]),
            P("payroll", "Employee banking", "2.5 million payroll accounts; 28 million salary payments worth Rs 1.8 trillion in 2025, with 97% of withdrawals made digitally.",
              s=["corp", "con"], lc="move", neo=[0, ""], src=[["HBL annual report 2025", AR25]]),
        ]},
        {"id": "4.5", "ic": "network", "name": "Konnect by HBL", "blurb": "54,000 agents; G2P.", "div": "konnect", "rev": "incl", "products": [
            P("konnect", "Konnect branchless banking", "Accounts and cash services through 54,364 neighbourhood agents; Rs 969 billion of Konnect volume and Rs 2 trillion of on-the-go collections to date; the branchless segment lost Rs 2.8 billion before tax in 2025.",
              s=["unb"], lc="open", neo=[0, ""], src=[["HBL annual report 2025", AR25], ["HBL investor presentation, Dec 2025", IP25]]),
            P("g2p", "G2P disbursements", "Rs 156 billion paid under the Benazir Income Support Programme in 2025 to 3.3 million women, work for 66 government bodies, and provincial farm subsidies with debit cards (300,000 in a three-year deal); the cards' network is not stated ⚠.",
              s=["unb", "farm"], lc="move", o="P", at="BISP, provincial governments", neo=[None, "Card network not stated ⚠."],
              mc="Social and subsidy cards are where Mastercard serves the Bank of Punjab.",
              src=[["HBL annual report 2025", AR25], ["HBL: Konnect G2P", KG2P], ["Konnect debit card", KCARD]]),
            P("kqr", "Konnect Visa QR", "Scan-to-pay from a Konnect account at Visa QR merchants and Konnect shops.",
              s=["unb", "con"], lc="move", o="P", at="Visa", neo=[0, "Visa QR."], src=[["HBL: Konnect QR", KQR]]),
        ]},
        {"id": "4.6", "ic": "coins", "name": "HBL Microfinance Bank", "blurb": "Rs 100bn+ loans; PayPak credit.", "div": "mfb", "rev": "incl", "products": [
            P("mfb", "HBL Microfinance Bank", "Formerly First MicroFinance Bank (AKFED, 2002), 90.83% owned; a loan book above Rs 100 billion, the largest microfinance housing lender (Rs 28 billion), back in profit in 2025, with a US$80 million IFC risk-sharing deal; about 4.5 million customers and 2.6 million wallet users ⚠.",
              s=["farm", "unb"], lc="borrow", o="A", neo=[0, ""], src=[["HBL annual report 2025", AR25], ["AKDN: microfinance in Pakistan", AKDNMFB]]),
            P("mfbcc", "PayPak credit card", "Signed on 29 September 2026 with 1LINK and Euronet to issue Pakistan's first PayPak credit card, in Green, Standard, Pink and Edge variants, conventional and Islamic.", short="PayPak credit (MfB)",
              s=["unb", "farm"], lc="borrow", st="new", ay="Sep 2026", o="P", at="1LINK, Euronet", neo=[0, "PayPak."],
              mc="The domestic scheme's first credit card comes from inside the HBL group.",
              src=[["APP: first PayPak credit card, Sep 2026", MFBCC]]),
        ]},
        {"id": "4.7", "ic": "globe", "name": "International & wealth", "blurb": "25 branches abroad; AMC.", "div": "intl", "rev": "intl", "products": [
            P("intl", "International network", "25 international branches, all profitable in 2025: UAE, Bahrain, Singapore, the UK (Prestige launched 2025), China, Bangladesh, Sri Lanka and the Maldives; exits from Belgium, Oman and Mauritius, and Türkiye winding down.",
              s=["corp"], lc="move", st="flux", neo=[0, ""], src=[["HBL annual report 2025", AR25], ["HBL investor presentation, Dec 2025", IP25]]),
            P("wealth", "Asset management & bancassurance", "HBL Asset Management with Rs 355 billion of funds; bancassurance with a 37% market share and Rs 6.75 billion of premiums in 2025; Jubilee insurance associates.",
              s=["aff"], lc="grow", neo=[0, ""], src=[["HBL annual report 2025", AR25], ["HBL: corporate information", CORP]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach HBL: HBL Mobile for 5 million users and WhatsApp for a million, about 2,000 branches with Prestige lounges and SME Trade Centres, and 2,300 ATMs and 54,000 Konnect agents.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "HBL Mobile & WhatsApp", "blurb": "5 million app users.", "div": "hbl", "rev": "retail", "products": [
            P("app", "HBL Mobile", "More than 5 million users, 45% of the bank's digital transactions and Rs 11 trillion of payments in 2025; digital onboarding for credit cards and loans; card controls and HBL Pay.",
              s=["con", "aff"], lc="everyday", o="B", neo=[0, ""], src=[["HBL annual report 2025", AR25], ["HBL investor presentation, Dec 2025", IP25]]),
            P("whatsapp", "WhatsApp banking", "One million users and 110 million transactions, with bill payments for 6,500 billers.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["HBL annual report 2025", AR25]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & lounges", "blurb": "About 2,000 branches.", "div": "hbl", "rev": "retail", "products": [
            P("branches", "Branches, Prestige lounges & Trade Centres", "About 2,000 branches including HBL Microfinance, 56 Prestige lounges, 17 SME Trade Centres and more than 500 SME and farm branches; 75 new branches in 2025.",
              s=["con", "aff", "sme", "farm"], lc="open", neo=[0, ""], src=[["HBL: H1 2026 results", H126], ["HBL annual report 2025", AR25]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "ATMs & agents", "blurb": "140,000 touchpoints.", "div": "konnect", "rev": "incl", "products": [
            P("agents", "ATMs, agents & POS", "More than 140,000 touchpoints: 2,318 ATMs, 54,364 Konnect agents, 40,009 POS terminals and 42,113 QR locations at end-2025.",
              s=["unb", "con"], lc="open", neo=[0, ""], src=[["HBL annual report 2025", AR25], ["HBL: H1 2026 results", H126]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at HBL", "blurb": "Premium and business debit.", "products": [
        P("mcathbl", "Mastercard at HBL", "Partners since 2013, Mastercard is one of four networks on HBL's debit cards and holds the World debit card and, since August 2025, Classic and World Business debit. Visa holds Platinum credit, most credit card art, Konnect QR, the mPOS and PayZen tie-ups and She's Next grants; UnionPay signed a strategic MoU in September 2026; PayPak and Raast are the state-backed rails.",
          s=["con"], div="hbl", rev="retail", mc="The relationship this map is drawn for.",
          src=[["Mastercard: HBL business debit, Aug 2025", MCBDC], ["HBL: debit cards", DCOV], ["HBL: Platinum CreditCard", PLAT], ["HBL: Visa She's Next, Nov 2025", SHESNEXT]]),
    ]},
    {"id": "pillar-market", "name": "Pakistan payments", "blurb": "PayPak, Raast, QR.", "products": [
        P("market", "The Pakistani market", "69.9 million payment cards in June 2026 (3.3 million credit); Raast at 2,755 million payments a year; QR merchants up from 1.1 million to 3.8 million under the Cashless Pakistan subsidy; 1LINK designated a payment system in August 2025; Easypaisa the first digital bank (2025); Mastercard expanding with the Bank of Punjab (July 2026).",
          s=["con"], div="hbl", rev="retail",
          src=[["SBP: payment systems review FY26", APS26], ["ProPakistani: Easypaisa digital bank, Jan 2025", EASYPAISA], ["Daily Pakistan: Mastercard and BOP, Jul 2026", BOPMC]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
