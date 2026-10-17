"""UOB's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the 2Q26 results (7 August 2026), the FY25 results
(24 February 2026) and the Annual Report 2025. Card networks were read from UOB's card pages on 17 October 2026.
``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on
Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

NR2Q26 = "https://www.uobgroup.com/investor-relations/assets/pdfs/investor/financial/2026/news-release-2q-2026.pdf"
CFO2Q26 = "https://links.sgx.com/1.0.0/corporate-announcements/PJL323UFL9E3U2E8/899002_2Q26%20-%20CFO%20slides.pdf"
DECK = "https://www.uobgroup.com/investor-relations/assets/pdfs/investor/presentations/citi-asean-summit-2026.pdf"
FY25 = "https://www.uobgroup.com/investor-relations/assets/pdfs/investor/financial/2025/news-release-4q-2025.pdf"
AR25 = "https://links.sgx.com/1.0.0/corporate-announcements/CJ5LTSEV6VGWLF37/878788_UOB%20AR2025.pdf"
FS = "https://www.uobgroup.com/investor-relations/assets/pdfs/investor/financial/2026/corp-factsheet-2q-2026.pdf"
GMC = "https://www.uobgroup.com/uobgroup/about/management/group-management-committee.page"
VISA26 = "https://www.uobgroup.com/assets/web-resources/uobgroup/pdf/newsroom/news-releases/2026/visa-infinite-tiers-launch.pdf"
MCAGENT = "https://www.mastercard.com/news/ap/en/newsroom/press-releases/en/2026/mastercard-delivers-its-first-live-agentic-transaction-in-singapore-with-dbs-and-uob/"
MCASEAN = "https://newsroom.mastercard.com/news/ap/en/newsroom/press-releases/en/2026/mastercard-powering-asean-s-ai-ambitions-in-the-future-of-payments/"
REGAL19 = "https://www.uob.com.sg/web-resources/uobgroup/pdf/newsroom/2019/UOB-Regal-card.pdf"
WOORI24 = "https://www.uob.com.sg/uobgroup/newsroom/news-releases/2024/uob-woori-card-pioneer-reciprocal-card-partnership.page"
CITIDEAL = "https://www.uob.com.my/about/news/2022/news-release-jan14-2022.page"
CITIPRICE = "https://www.thesundaily.my/home/singapore-s-uob-to-buy-citi-retail-arms-in-4-southeast-asia-markets-for-365-bln-AY8760406"
AR23 = "https://www.uobgroup.com/AR2023/investor-highlights.html"
THAI = "https://www.theasianbanker.com/updates-and-articles/uob-thailand-sharpens-retail-banking-focus-after-citibank-integration"
AWS = "https://www.uobgroup.com/uobgroup/newsroom/news-releases/2026/uob-aws-mou.page"
SWIFTHSBC = "https://www.uobgroup.com/uobgroup/newsroom/news-releases/2026/uob-cross-border-transactions-on-swift.page"
SWIFTSG = "https://www.uobgroup.com/uobgroup/newsroom/news-releases/2026/singapore-banks-on-swift-ledger.page"
HEADASEAN = "https://www.uobgroup.com/uobgroup/newsroom/news-releases/2026/uob-new-head-of-asean-and-greater-china.page"
UOBAM = "https://www.thestar.com.my/business/business-news/2026/08/05/singapore039s-uob-to-sell-asset-management-business-to-allianz-unit-for-us434mil"
PAYNOWGEN2 = "https://www.crowdfundinsider.com/2026/06/287873-singapores-paynow-system-set-for-significant-enhancements-following-mas-and-abs-review/"
NEXUS = "https://www.mas.gov.sg/publications/annual-report/2026/annual-report-2025-2026/innovative-and-inclusive-financial-centre/payment-innovation"
VTS15 = "https://www.digitalnewsasia.com/uob-offer-visa-tokenisation-its-app"
PRVI = "https://www.uob.com.sg/personal/cards/travel/prvi-miles-card.page"
LADYS = "https://www.uob.com.sg/personal/cards/rewards/ladys-card/index.page"
ONEDEBIT = "https://www.uob.com.sg/personal/cards/cashback/one-debit-card.page"
KRISDEBIT = "https://www.uob.com.sg/personal/cards/travel/krisflyer-debit-card.page"
ABSOLUTE = "https://www.uob.com.sg/personal/cards/cashback/absolute-cashback-card.page"
RESERVE = "https://www.uob.com.sg/personal/cards/privilege/reserve-card.page"
VIMETAL = "https://www.uob.com.sg/personal/cards/privilege/visa-infinite-metal-card.page"
SINGTEL = "https://www.uob.com.sg/personal/cards/cashback/singtel-card.page"
ONECARD = "https://www.uob.com.sg/personal/cards/cashback/one-card.page"
FXPLUS = "https://www.uob.com.sg/personal/save/foreign-currency-accounts/fxplus.page"
BIZCARDS = "https://www.uob.com.sg/business/transact/cards/business-credit-cards.page"
APPLEPAY = "https://www.uob.com.sg/applepay"
PAYNOW = "https://www.uob.com.sg/personal/digital-banking/paynow.page"
NETS = "https://www.uob.com.sg/personal/digital-banking/nets-contactless.page"
TMRW = "https://www.uob.com.sg/personal/digital-banking/index.page"
MYCARDS = "https://www.uob.com.my/personal/cards/all-cards.page"
MYDEBIT = "https://www.uob.com.my/personal/cards/debit-cards/uob-debit-card.page"
MYBIZ = "https://www.uob.com.my/web-resources/business/pdf/platinum-business-mastercard-acquisition-campaign.pdf"
THDEBIT = "https://www.uob.co.th/personal/deposits/debit-cards.page"
THPAYLATER = "https://www.uob.co.th/personal/cards/credit/uob-paylater.page"
IDCARDS = "https://www.uob.co.id/personal/cards/index.page"
VNCARDS = "https://www.uob.com.vn/personal/cards/index.page"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · footprint · family", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: S$572 billion of assets and Aa1 ratings, a bank founded in 1935 and built by acquisition, the Wee family as strategic shareholders, Citi's four ASEAN consumer businesses absorbed, and an AI and cloud programme.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "S$1.5bn a quarter, ROE 11.8%.", "div": "uob", "rev": "oth", "products": [
            P("balance", "Balance sheet & earnings", "Net profit S$1.48 billion in 2Q26 (+10%) and S$2.92 billion in 1H26; ROE 11.6%, CET1 15.4%, NPL 1.6%; loans S$361 billion and deposits S$437 billion at 30 June 2026. FY2025 net profit S$4.68 billion (−23% after a pre-emptive allowance), total assets S$572 billion, market cap S$57.9 billion at end-2025; rated Aa1/AA-/AA-.",
              s=["corp"], neo=[0, ""], src=[["UOB 2Q26 news release", NR2Q26], ["UOB investor deck, Aug 2026", DECK], ["UOB Annual Report 2025", AR25]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Wee Ee Cheong, Wong Kan Seng.", "div": "uob", "rev": "oth", "products": [
            P("leadership", "Board & management", "Chairman Wong Kan Seng; Deputy Chairman and CEO Wee Ee Cheong; CFO Leong Yung Chee; Susan Hwee runs Group Retail, Frederick Chin Wholesale Banking and Markets, Lawrence Goh Technology and Operations; Tan Choon Hin became Head of ASEAN and Greater China on 1 September 2026. Pratik Bhattacharjee heads Group Cards and Payment Products.",
              s=["corp"], st="flux", neo=[0, ""], src=[["UOB: Group Management Committee", GMC], ["UOB: new Head of ASEAN and Greater China, Aug 2026", HEADASEAN]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & ownership", "blurb": "Founded 1935, built by deals.", "div": "uob", "rev": "oth", "products": [
            P("heritage", "Heritage & shareholders", "Founded in August 1935 by Datuk Wee Kheng Chiang and partners; grew through Chung Khiaw (1971), Far Eastern (1984), Overseas Union Bank (2001), Bank of Asia (2004) and Bank Buana (2005). Listed on SGX (U11); strategic shareholders, including the Wee family, hold 28%. Group headcount 31,222 at end-2025.",
              s=["corp"], o="I", neo=[0, ""], src=[["UOB investor deck, Aug 2026", DECK], ["UOB corporate factsheet 2Q26", FS], ["UOB Annual Report 2025", AR25]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "AWS cloud, agentic AI.", "div": "uob", "rev": "oth", "products": [
            P("tech", "AI programme", "More than 20,000 staff trained in generative AI and Copilot for over 35,000; Program AURA builds agentic AI for AML/KYC, credit, collections and relationship managers; GenAI in the contact centre and private-bank advice.",
              s=["corp"], st="new", neo=[0, ""], src=[["UOB investor deck, Aug 2026", DECK]]),
            P("aws", "AWS hybrid cloud", "An MoU with AWS (9 October 2026) for a dedicated cloud environment in Singapore, a hybrid model serving UOB's five ASEAN markets, starting with data, analytics and AI customer engagement.",
              s=["corp"], st="new", ay="Oct 2026", o="P", at="AWS", neo=[0, ""], src=[["UOB and AWS MoU, Oct 2026", AWS]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "One bank for ASEAN.", "div": "uob", "rev": "oth", "products": [
            P("strategy", "ASEAN strategy & 2026 guidance", "Be the leading bank in ASEAN: connect customers across the regional network, grow wealth and capture trade flows. 2026 guidance: low single-digit loan and fee growth, NIM 1.75–1.80%, credit costs 25–30bp; a S$3 billion capital return including a S$2 billion buyback.",
              s=["corp"], neo=[0, ""], src=[["UOB 2Q26 CFO slides", CFO2Q26], ["UOB 2Q26 news release", NR2Q26]]),
            P("citideal", "Citi ASEAN consumer acquisition", "Agreed 14 January 2022 for Citi's net assets (about S$4 billion) plus a S$915 million premium, about S$4.9 billion ⚠ in all; about 2.4 million customers. Completed Malaysia and Thailand 1 November 2022, Vietnam 1 March 2023, Indonesia 20 November 2023.",
              s=["citi"], o="A", ay="Jan 2022", neo=[0, ""], src=[["UOB: Citi acquisition, Jan 2022", CITIDEAL], ["The Sun: deal value", CITIPRICE], ["UOB corporate factsheet 2Q26", FS]]),
            P("uobam", "UOB Asset Management sale", "Sale of UOBAM (about S$42 billion of client assets) to Allianz Global Investors for about S$555 million with a 10-year distribution agreement, agreed 5 August 2026; pre-tax gain about S$330 million; closing expected in 2027.",
              s=["aff"], st="flux", ay="Aug 2026", o="P", at="Allianz Global Investors", neo=[0, ""], src=[["The Star: UOBAM sale, Aug 2026", UOBAM], ["UOB 2Q26 CFO slides", CFO2Q26]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: ASEAN's biggest consumer credit card book by billings, premium on Visa and the Lady's and PRVI cards on Mastercard; Mastercard debit across Malaysia, Thailand and Vietnam; SME metal and business cards; instalments; PayNow, NETS and QR; and tokenised deposits on Swift's ledger.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Singapore credit cards", "blurb": "Visa leads, Lady's on Mastercard.", "div": "sg", "rev": "retail", "products": [
            P("sgvisa", "Visa cards: Visa Infinite Metal, Reserve, Singtel-UOB, One ⚠", "The premium and everyday Visa range: UOB Visa Infinite Metal, Reserve (Visa Infinite), Privilege Banking Visa Infinite, Singtel-UOB (Visa Signature), EVOL and Lazada-UOB ⚠, and UOB One Card ⚠ (network not stated on its page). UOB is top in billings for Visa consumer cards in Singapore.", short="Singapore Visa cards",
              s=["con", "aff"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["UOB: Visa Infinite Metal Card", VIMETAL], ["UOB: Reserve Card", RESERVE], ["UOB: Singtel-UOB Card", SINGTEL], ["UOB: One Card", ONECARD], ["UOB Annual Report 2025", AR25]]),
            P("sgmc", "Mastercard cards: Lady's & PRVI Miles", "UOB Lady's Card on World Mastercard, with Lady's Solitaire ⚠ and Lady's Debit, and the PRVI Miles Mastercard, one of three PRVI Miles versions (Visa, Mastercard, Amex).", short="Lady's & PRVI (Mastercard)",
              s=["con", "trav"], lc="borrow", o="P", at="Mastercard", neo=[2, "World Mastercard."],
              mc="Mastercard's main consumer credit franchise at UOB Singapore.",
              src=[["UOB: Lady's Card", LADYS], ["UOB: PRVI Miles Card", PRVI]]),
            P("sgamex", "American Express cards", "UOB Absolute Cashback (American Express) and the PRVI Miles American Express; Amex cards cannot be added to mobile wallets at UOB.",
              s=["con"], lc="borrow", o="P", at="American Express", neo=[0, "Amex."], src=[["UOB: Absolute Cashback Card", ABSOLUTE], ["UOB: Apple Pay", APPLEPAY]]),
        ]},
        {"id": "2.2", "ic": "earth", "name": "Regional credit cards", "blurb": "Visa's largest ASEAN issuer.", "div": "uob", "rev": "retail", "products": [
            P("visainf", "Visa Infinite Privilege & Private relaunch", "More than 300,000 Visa Infinite cardholders in Singapore, Malaysia, Thailand, Indonesia and Vietnam moved to Visa's new Visa Infinite Privilege and Private tiers (22 July 2026); UOB calls itself Visa's largest card issuer in ASEAN by billings. Affluent card billings grew more than 25% in 2025.", short="Visa Infinite tiers (Visa)",
              s=["aff"], lc="borrow", st="new", ay="Jul 2026", o="P", at="Visa", neo=[0, "Visa."],
              mc="The premium book across five markets went deeper with Visa in July 2026.",
              src=[["UOB and Visa: Visa Infinite tiers, Jul 2026", VISA26]]),
            P("mycards", "Malaysia credit cards", "Visa Infinite Metal, Visa Infinite, Zenith, PRVI Miles Elite, Lady's, ONE, EVOL, Simple and Lazada UOB cards, and the UOB World Card ⚠ (Mastercard World tier); fee waivers tied to spend from January 2026.",
              s=["con", "citi"], lc="borrow", o="P", at="Visa, Mastercard", neo=[1, "Visa premium; Mastercard on World and Lady's ⚠."], src=[["UOB Malaysia: all cards", MYCARDS]]),
            P("idcards", "Indonesia credit cards", "UOB Zenith Visa and PRVIMiles Visa, both upgraded in 2026; about 500,000 former Citi customers migrated in November 2023.",
              s=["con", "citi"], lc="borrow", o="P", at="Visa", neo=[0, "Visa ⚠ (only Visa cards seen)."], src=[["UOB Indonesia: cards", IDCARDS], ["UOB AR2023 investor highlights", AR23]]),
            P("thcards", "Thailand credit cards", "A retail base grown from 1.5 million to 2.5 million by Citi; 92% of Citi's Thai retail customers migrated and re-carded; more than 40% of migrated cardholders also opened deposit accounts. Network split not readable ⚠.",
              s=["citi"], lc="borrow", o="A", neo=[None, "Network split not public ⚠."], src=[["Asian Banker: UOB Thailand, Jul 2025", THAI]]),
        ]},
        {"id": "2.3", "ic": "wallet-cards", "name": "Debit & travel cards", "blurb": "Mastercard across the region.", "div": "uob", "rev": "retail", "products": [
            P("sgdebit", "UOB One Debit", "Up to 4% cashback, issued on both Visa and Mastercard; only the Visa version taps for NETS, Singapore's domestic scheme.", short="One Debit (Visa & Mastercard)",
              s=["con"], lc="everyday", o="P", at="Visa, Mastercard, NETS", neo=[1, "Visa and Mastercard versions."], src=[["UOB: One Debit Card", ONEDEBIT], ["UOB: NETS contactless", NETS]]),
            P("krisdebit", "KrisFlyer UOB Debit", "Earns KrisFlyer miles on spend and savings, with Mastercard Contactless and e-Commerce Protection.", short="KrisFlyer debit (Mastercard)",
              s=["trav"], lc="everyday", o="P", at="Singapore Airlines, Mastercard", neo=[2, "Mastercard."], src=[["UOB: KrisFlyer UOB Debit Card", KRISDEBIT]]),
            P("fxplus", "FX+ debit", "A multi-currency account with a travel debit card charging 0% FX fees, no cap; Grab offers tied to Mastercard World and World Elite cards ⚠ network inferred.", short="FX+ (Mastercard ⚠)",
              s=["trav"], lc="move", st="new", o="B", neo=[2, "Mastercard ⚠."],
              mc="Cross-border spend is UOB's growth line: billings +10%, volumes +35% in 2025.",
              src=[["UOB: FX+", FXPLUS], ["UOB Annual Report 2025", AR25]]),
            P("regdebit", "Malaysia, Thailand & Vietnam debit", "UOB Debit in Malaysia and Vietnam on Mastercard (Vietnam's Privilege Banking debit carries Mastercard Travel Pass); Thai debit on Mastercard with PromptCard for domestic use.", short="Regional debit (Mastercard)",
              s=["con", "citi"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard; Thai cards also carry PromptCard."], src=[["UOB Malaysia: debit card", MYDEBIT], ["UOB Thailand: debit cards", THDEBIT], ["UOB Vietnam: cards", VNCARDS]]),
        ]},
        {"id": "2.4", "ic": "briefcase-business", "name": "Business cards", "blurb": "Regal metal on World Elite.", "div": "uob", "rev": "gwb", "products": [
            P("regal", "UOB Regal Business Metal Card", "Asia Pacific's first World Elite Mastercard Business metal card for SMEs, launched with Mastercard on 28 May 2019 from joint SME research; lounges, golf and Accor Plus.", short="Regal Business Metal (Mastercard)",
              s=["sme"], lc="borrow", ay="May 2019", o="P", at="Mastercard", neo=[2, "World Elite Mastercard."], src=[["UOB and Mastercard: Regal card, May 2019", REGAL19]]),
            P("commercial", "Corporate & commercial cards", "UOB Corporate and Commercial Cards, the Business World Debit ⚠ and the Zuellig Pharma Infinite Business Card, promoted with both Visa Commercial Offers and Mastercard Easy Savings.",
              s=["sme", "corp"], lc="move", o="P", at="Visa, Mastercard", neo=[1, "Visa and Mastercard."],
              mc="UOB Infinity runs in 10 markets; virtual and controlled cards are open ground.",
              src=[["UOB: business credit cards", BIZCARDS]]),
            P("mybiz", "Malaysia Platinum Business Mastercard", "The SME card in Malaysia, with RM288 cashback for new cardholders (17 June–31 August 2026).",
              s=["sme"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["UOB Malaysia: Platinum Business campaign", MYBIZ]]),
        ]},
        {"id": "2.5", "ic": "hand-coins", "name": "Instalments", "blurb": "SmartPay, PayLater.", "div": "uob", "rev": "retail", "products": [
            P("smartpay", "UOB SmartPay", "Instalment conversion of card purchases in Singapore, alongside recurring bill payment on cards.",
              s=["con"], lc="borrow", o="B", neo=[1, "Runs on UOB's cards of every network."], src=[["UOB: SmartPay", "https://www.uob.com.sg/personal/cards/services/smart-pay.page"]]),
            P("paylater", "UOB PayLater & PayAnything (Thailand)", "Instalments and pay-anything services on UOB Thailand credit cards.",
              s=["citi"], lc="borrow", o="B", neo=[None, "Network split not public."], src=[["UOB Thailand: PayLater", THPAYLATER]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "PayNow, NETS & QR", "blurb": "Account-to-account across ASEAN.", "div": "tmrw", "rev": "retail", "products": [
            P("paynow", "PayNow & cross-border transfers", "PayNow on TMRW up to S$200,000 a day, to e-wallets (Grab, Singtel Dash, Liquid Pay) and instantly to Malaysia via DuitNow and Thailand via PromptPay. PayNow had about 11 million registrations and carried about S$300 billion in 2025.",
              s=["con", "trav"], lc="move", o="P", at="PayNow, DuitNow, PromptPay", neo=[0, "Account-to-account."], src=[["UOB: PayNow", PAYNOW], ["Crowdfund Insider: PayNow review, Jun 2026", PAYNOWGEN2]]),
            P("nets", "NETS contactless", "NETS tap-and-pay on the One Debit Visa and ATM cards, and SimplyGo transit on the ATM contactless card.",
              s=["con"], lc="everyday", o="P", at="NETS", neo=[0, "Domestic scheme."], src=[["UOB: NETS contactless", NETS]]),
            P("scantopay", "TMRW Scan to Pay (ASEAN QR)", "QR payments in TMRW across more than 40 million touchpoints in Indonesia, Malaysia and Thailand; scan-to-pay and P2P volumes +35% in 2025. Project Nexus, linking ASEAN instant-payment systems, is targeted for 2027.",
              s=["trav"], lc="move", o="P", at="National QR schemes", neo=[0, "National QR rails."],
              mc="Cross-border QR competes directly with card spend abroad.",
              src=[["UOB Annual Report 2025", AR25], ["MAS Annual Report 2025/26", NEXUS]]),
        ]},
        {"id": "2.7", "ic": "coins", "name": "Digital money", "blurb": "Tokenised deposits on Swift.", "div": "infinity", "rev": "gwb", "products": [
            P("swift", "Tokenised deposits on Swift's ledger", "The first Singapore-headquartered bank to transact live on Swift's blockchain ledger (HKD with HSBC, 26 August 2026), then the first live SGD tokenised-deposit interbank payments with DBS and OCBC (10 September 2026).",
              s=["corp"], lc="move", st="new", ay="Aug 2026", o="P", at="Swift, HSBC, DBS, OCBC", neo=[0, ""], src=[["UOB and HSBC on Swift's ledger, Aug 2026", SWIFTHSBC], ["DBS, OCBC and UOB on Swift's ledger, Sep 2026", SWIFTSG]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: scam controls and tokens, Mastercard Agent Pay live since March 2026, AI insights served 530 million times, and rewards that travel across borders.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud, scams & tokens", "blurb": "S$15.6m of losses prevented.", "div": "uob", "rev": "retail", "products": [
            P("fraud", "Fraud & scam controls", "Real-time fraud surveillance, an industry-first block on unauthorised remote-device access, and SMS one-time passwords replaced by digital tokens; S$15.6 million of fraud losses prevented for Singapore customers in 2025.",
              s=["con"], lc="everyday", o="B", neo=[0, "UOB's own."],
              mc="Scams are UOB's 'pressing concern'; network scam scores and passkeys could add a layer.",
              src=[["UOB Annual Report 2025", AR25]]),
            P("tokens", "Wallet tokens", "Apple Pay for UOB Mastercard and Visa cards, provisioned through TMRW digital-token authentication since July 2025 (Amex and UnionPay not supported); UOB was an early Visa Token Service bank in 2015 ⚠.",
              s=["con"], lc="everyday", o="P", at="Mastercard, Visa", neo=[1, "Mastercard and Visa tokens."], src=[["UOB: Apple Pay", APPLEPAY], ["Digital News Asia: Visa tokenisation", VTS15]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "Agentic payments", "blurb": "Agent Pay, live March 2026.", "div": "sg", "rev": "retail", "products": [
            P("agentpay", "Mastercard Agent Pay", "Mastercard's first live authenticated agentic transaction in Singapore, with DBS and UOB (6 March 2026): an AI agent booked a Changi airport ride using an Agentic Token and Payment Passkeys. UOB is Mastercard's partner for region-wide testing, Singapore and Malaysia first (6 April 2026).", short="Agent Pay (Mastercard)",
              s=["con"], lc="beyond", st="new", ay="Mar 2026", o="P", at="Mastercard", neo=[3, "Mastercard Agent Pay."],
              mc="The clearest joint work: Mastercard's own product, live at UOB.",
              src=[["Mastercard: first live agentic transaction, Mar 2026", MCAGENT], ["Mastercard: ASEAN AI, Apr 2026", MCASEAN]]),
        ]},
        {"id": "3.3", "ic": "brain", "name": "AI insights", "blurb": "530m insight cards.", "div": "tmrw", "rev": "retail", "products": [
            P("insights", "TMRW insights & GenAI", "530 million personalised insight cards served to 5 million customers; one in two customers acts on them; GenAI advisory for private-bank clients and a GenAI chatbot for bankers.",
              s=["con", "aff"], lc="everyday", o="B", neo=[0, "UOB's own."],
              mc="Agentic tokens could let TMRW's AI act, not just advise.",
              src=[["UOB Annual Report 2025", AR25], ["UOB investor deck, Aug 2026", DECK]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Rewards & lifestyle", "blurb": "UNI$, Rewards+, Michelin.", "div": "uob", "rev": "retail", "products": [
            P("rewards", "UNI$, UOB$ & Rewards+", "UNI$ points and UOB$ cashback; Rewards+ on TMRW with more than 1,000 deals and over a million users; UNI$ redeemable in Johor (volumes +29% in Q4 2025); MICHELIN Guide Hotels global partner and Asia's Finest Tables.",
              s=["con", "aff", "trav"], lc="beyond", o="B", neo=[1, "Across every network."],
              mc="Card-linked offers and merchant data could extend Rewards+.",
              src=[["UOB Annual Report 2025", AR25]]),
            P("woori", "Woori Card reciprocal privileges", "A first between an ASEAN bank and a Korean card company (MoU 17 July 2024): UOB cardholders get Woori merchant privileges in Korea, Woori's 12 million cardholders get UOB's in five ASEAN markets; Mastercard holders first, Visa to follow.",
              s=["trav"], lc="beyond", ay="Jul 2024", o="P", at="Woori Card", neo=[1, "Mastercard first, then Visa."], src=[["UOB and Woori Card, Jul 2024", WOORI24]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: personal banking for 8.5 million across ASEAN, wealth with S$204 billion of high-net-worth assets, the absorbed Citi franchise, and wholesale, SME and markets business.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Personal banking", "blurb": "8.5 million customers.", "div": "uob", "rev": "retail", "products": [
            P("personal", "Accounts, loans & cards", "More than 8.5 million retail customers; Group Retail income S$2.57 billion in 1H26, credit card income +13%; CASA S$120 billion; about S$15 billion of card billings a quarter; gross card fees S$572 million in 1H26.",
              s=["con"], lc="everyday", neo=[1, "Cards on Visa, Mastercard and Amex."], src=[["UOB 2Q26 CFO slides", CFO2Q26], ["UOB Annual Report 2025", AR25]]),
        ]},
        {"id": "4.2", "ic": "gem", "name": "Wealth & private bank", "blurb": "S$204bn of AUM.", "div": "uob", "rev": "retail", "products": [
            P("wealth", "Privilege Banking & Private Bank", "High-net-worth AUM of S$204 billion (+7%); wealth income +16% in 1H26 and +30% in Malaysia, Indonesia, Thailand and Vietnam; S$4 billion of net new money.",
              s=["aff"], lc="grow", neo=[0, "Premium cards on Visa."], src=[["UOB 2Q26 news release", NR2Q26], ["UOB 2Q26 CFO slides", CFO2Q26]]),
        ]},
        {"id": "4.3", "ic": "refresh-cw", "name": "ASEAN-4 & the Citi book", "blurb": "Four markets absorbed.", "div": "uob", "rev": "retail", "products": [
            P("citi", "Former Citi customers", "About 700,000 customers migrated in Malaysia (July 2023), 500,000 in Indonesia (November 2023), 92% in Thailand, and Vietnam completed in 2025; UOB is now a top-five card issuer in Indonesia, Malaysia and Thailand.",
              s=["citi"], lc="open", o="A", neo=[None, "Networks of re-carded Citi cards not disclosed ⚠."],
              mc="The largest recent card migration in ASEAN; the network outcome is not public.",
              src=[["UOB AR2023 investor highlights", AR23], ["Asian Banker: UOB Thailand, Jul 2025", THAI], ["UOB Annual Report 2025", AR25]]),
        ]},
        {"id": "4.4", "ic": "building-2", "name": "Wholesale, SME & markets", "blurb": "Trade loans +33%.", "div": "infinity", "rev": "gwb", "products": [
            P("gwb", "Wholesale & transaction banking", "Wholesale income S$2.91 billion in 1H26, close to half from transaction banking; trade loans +33%; cross-border income 28%; about 24% of SGD loans.",
              s=["corp"], lc="move", neo=[0, ""], src=[["UOB 2Q26 CFO slides", CFO2Q26], ["UOB investor deck, Aug 2026", DECK]]),
            P("sme", "SME banking", "Named Best SME Bank globally and in Singapore; AI Ready 2.0 for SME AI adoption (September 2026); SME cards on Mastercard (Regal, Platinum Business).",
              s=["sme"], lc="borrow", neo=[1, "SME cards on Mastercard."], src=[["UOB Annual Report 2025", AR25]]),
            P("gm", "Global Markets", "Income S$1.24 billion in 1H26 (+15%), with record customer treasury income.",
              s=["corp"], lc="grow", neo=[0, ""], src=[["UOB 2Q26 CFO slides", CFO2Q26]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach UOB: the TMRW app ranked first in five ASEAN markets, UOB Infinity for companies in 10 markets, about 400 branches and centres, and partner brands from Lazada to KrisFlyer.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "UOB TMRW", "blurb": "#1 app in five markets.", "div": "tmrw", "rev": "retail", "products": [
            P("tmrw", "UOB TMRW app", "Ranked first on Google Play in Indonesia, Malaysia, Singapore, Thailand and Vietnam (December 2025), launched in Vietnam in 2025; 82% of customers are digitally enabled, and digitally engaged customers spend 2.5 times more on card.",
              s=["con", "trav"], lc="everyday", o="B", neo=[0, ""], src=[["UOB Annual Report 2025", AR25], ["UOB: TMRW", TMRW]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "UOB Infinity & APIs", "blurb": "Ten markets for companies.", "div": "infinity", "rev": "gwb", "products": [
            P("infinity", "UOB Infinity, SME app & APIs", "UOB Infinity for corporates in 10 markets (usage +20% in 2025, two-thirds from ASEAN companies), the UOB SME app, host-to-host and UOB API Services.",
              s=["sme", "corp"], lc="move", o="B", neo=[0, ""], src=[["UOB Annual Report 2025", AR25], ["UOB: business credit cards", BIZCARDS]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches", "blurb": "About 400 across ASEAN.", "div": "uob", "rev": "retail", "products": [
            P("branches", "Branches & wealth centres", "About 400 branches, wealth and private-banking centres and ATMs across ASEAN: Thailand 139, Indonesia 82, Malaysia 55, Singapore 42, Vietnam 5.",
              s=["con", "aff"], lc="open", neo=[0, ""], src=[["UOB investor deck, Aug 2026", DECK], ["UOB Annual Report 2025", AR25]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Partner brands", "blurb": "Lazada, Singtel, KrisFlyer.", "div": "sg", "rev": "retail", "products": [
            P("partners", "Co-brand & lifestyle partners", "Lazada-UOB and Singtel-UOB cards (Visa), KrisFlyer UOB Debit (Mastercard), Zuellig Pharma, Michelin and live entertainment presales.",
              s=["con"], lc="beyond", o="P", at="Lazada, Singtel, Singapore Airlines", neo=[1, "Visa and Mastercard co-brands."], src=[["UOB: Singtel-UOB Card", SINGTEL], ["UOB: KrisFlyer UOB Debit Card", KRISDEBIT], ["UOB Annual Report 2025", AR25]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at UOB", "blurb": "Debit, SME cards, Agent Pay.", "products": [
        P("mcatuob", "Mastercard at UOB", "UOB is ASEAN's top consumer credit card issuer by billings across Visa and Mastercard, and Visa's largest issuer in the region, with the premium tier on Visa. Mastercard carries regional debit in Malaysia, Thailand and Vietnam, the Lady's and PRVI Mastercard cards, the Regal and Platinum Business SME cards, and UOB's agentic payments, live since March 2026.",
          s=["con"], div="uob", rev="retail", mc="The relationship this map is drawn for.",
          src=[["UOB Annual Report 2025", AR25], ["UOB and Visa: Visa Infinite tiers, Jul 2026", VISA26], ["Mastercard: first live agentic transaction, Mar 2026", MCAGENT]]),
    ]},
    {"id": "pillar-market", "name": "Singapore & ASEAN", "blurb": "PayNow, QR links, Nexus.", "products": [
        P("market", "The market", "Three local banks lead Singapore; PayNow (about 11 million registrations) and NETS dominate domestic account payments, PayNow links to DuitNow and PromptPay, national QR schemes connect across ASEAN, and Project Nexus is targeted for 2027.",
          s=["con"], div="uob", rev="retail", src=[["Crowdfund Insider: PayNow review, Jun 2026", PAYNOWGEN2], ["MAS Annual Report 2025/26", NEXUS]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
