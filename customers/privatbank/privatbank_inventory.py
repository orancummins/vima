"""PrivatBank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the H1 2026 results (27 July 2026), the Q1 2026 results
(29 April 2026) and the 2025 financial statements and management report. ``neo`` is the Mastercard lens: [depth, note],
where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

H1 = "https://privatbank.ua/en/news/2026/7/27/privatbank-reports-results-for-the-first-half-of-2026-strong-financial-performance-and-uah-24-6-billion-in-net-profit"
Q1 = "https://privatbank.ua/en/news/2026/4/29/privatbank-in-q1-2026-largest-tax-payment-and-stable-financial-results"
FY25 = "https://static.privatbank.ua/files//finzvit2025-eng.pdf"
MGMT = "https://privatbank.ua/en/about/management/corp"
ABOUT = "https://privatbank.ua/en/about"
NILSON = "https://privatbank.ua/en/news/2025/7/25/privatbank-stav-naybilshim-emitentom-kartok-visa-ta-mastercard-u-yevropi-the-nilson-report"
AGENT = "https://www.mastercard.com/news/eemea/en/newsroom/press-releases/en/2026/mastercard-and-privatbank-complete-ukraine-s-first-payment-executed-by-an-ai-agent/"
AGENTPB = "https://privatbank.ua/en/news/2026/6/23/mastercard-and-privatbank-complete-ukraine-s-first-payment-executed-by-an-ai-agent"
PSYS = "https://privatbank.ua/handbook/elektronni-platizhni-sistemi"
MCX2 = "https://privatbank.ua/en/news/2025/11/12/ukrajinci-mozhut-otrimati-v-privatbanku-keshbeki-do-15-000-grn-za-mizhnarodni-perekazi-z-kartkami-mastercard"
MCX3 = "https://babel.ua/en/news/123874-ukrainians-can-receive-up-to-uah-100-000-in-cashback-for-international-transfers-with-mastercard-cards-from-privatbank"
MCDEL = "https://babel.ua/en/news/121468-privatbank-and-mastercard-deliver-cards-free-of-charge-across-ukraine-and-to-over-60-countries-around-the-world-the-conditions"
KATKA = "https://privatbank.ua/en/news/2026/4/14/privatbank-ta-visa-zapuskayut-katka24-razom-iz-navi-keshbek-znizhki-ta-promokodi-dlya-geymeriv"
NAVI = "https://privatbank.ua/en/news/2025/12/9/privatbank-visa-ta-navi-ogolosili-pro-start-spivpraci-ta-stvorennya-pershoji-v-ukrajini-finansovoji-geymerskoji-ekosistemi"
DAF = "https://epravda.com.ua/rus/news/2023/08/03/702879/"
FACEPAY = "https://www.unian.net/economics/finance/10683147-v-ukraine-poyavilas-tehnologiya-oplaty-licom.html"
APPLEPAY = "https://www.nfcw.com/2018/05/17/357061/privatbank-brings-apple-pay-to-ukraine/"
GARMIN = "https://privatbank.ua/en/news/2018/7/24/v-ukrajini-zapustili-platizhniy-servis-dlya-aktivnih-lyudey-garmin-pay"
PREMIUM = "https://privatbank.ua/premium-banking/compare-premium-cards"
DIIA = "https://privatbank.ua/diiacard"
PAYOUT = "https://finance.ua/ua/cards/kartka-dlya-vyplat-mc-world-visa-rewards-12498-privatbank-p"
NBUCARDS = "https://interfax.com.ua/news/economic/1075078.html"
ACQ24 = "https://privatbank.ua/en/news/2025/2/17/za-2024-cherez-ekosistemu-ekvayringu-privatbanku-ukrajinci-oplatili-kartkami-pokupok-na-bilshe-nizh-1-trln-grn"
ACQ25 = "https://privatbank.ua/en/news/2026/2/10/ukrajinskiy-biznes-perehodit-v-smartfoni-ta-onlayn"
PARTS = "https://mind.ua/news/20278390-privatbank-znizhue-tarifi-dlya-biznesu-na-poslugu-oplata-chastinami"
PRYVIT = "https://privatbank.ua/en/news/2025/5/29/ukrajinci-otrimali-ponad-735-milyoniv-propoziciy-ta-keshbekiv-vid-programi-loyalnosti-privatbanku-privit"
SUBS = "https://privatbank.ua/en/news/2026/9/11/customer-needs-above-all-how-privatbank-turned-ukrainians-daily-expenses-into-benefits-of-up-to-uah-1-000-per-month-in-a-new-subscription-format"
CRIMEA = "https://privatbank.ua/en/news/2026/10/6/privatbank-wins-final-award-against-russia-in-pca-arbitration-over-unlawful-expropriation-of-its-assets-in-crimea"
FRAUDMIA = "https://privatbank.ua/en/news/2026/9/21/privatbank-ministry-of-internal-affairs-and-state-migration-service-strengthen-countermeasures-against-fraud-involving-counterfeit-documents"
SIGN = "https://privatbank.ua/en/news/2026/9/23/barrier-free-banking-privatbank-introduced-sign-language-video-verification-for-new-clients"
INCOME = "https://privatbank.ua/en/news/2026/9/8/no-complex-spreadsheets-privatbank-launched-automatic-income-limit-control-for-sole-proprietors-in-privat24-for-business"
SMEAWARD = "https://privatbank.ua/en/news/2026/9/1/privatbank-recognized-as-one-of-the-best-banks-for-business-in-eastern-europe-sme-banking-agency-study"
IPO = "https://finance.liga.net/en/bank/news/nbu-announces-plans-for-privatbank-ipo-possibly-in-warsaw"
TOP10 = "https://komersant.ua/en/na-14-zris-dokhid-top-10-bankiv-ukrainy-khto-zarobyv-naybilshe"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · state owner · recovery", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: UAH 925 billion of assets and Ukraine's biggest tax bill, a state owner since 2016 with an IPO under study, court wins against the former owners and Russia, and a bank rebuilding its core around AI.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & earnings", "blurb": "UAH 24.6bn profit in H1.", "div": "pb", "rev": "central", "products": [
            P("balance", "Balance sheet & earnings", "Total assets of UAH 924.7 billion, net loans of UAH 188.5 billion (+45%) and customer funds of UAH 785 billion at 30 June 2026; net profit of UAH 24.6 billion in the half after UAH 24.9 billion of income tax. 2025 profit before tax UAH 88 billion, after tax UAH 29.1 billion; UAH 59 billion paid to the state budget.",
              s=["con"], neo=[0, ""], src=[["H1 2026 results", H1], ["2025 financial statements", FY25], ["Komersant: top-10 banks, 2025", TOP10]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "State owner & leadership", "blurb": "100% state; Björknert CEO.", "div": "pb", "rev": "central", "products": [
            P("owner", "State ownership & listing plans", "Nationalised in December 2016; 100% owned by the state through the Cabinet of Ministers. In June 2026 the NBU said it was weighing an IPO, possibly in Warsaw, with 2027 mentioned in press ⚠. Ratings are capped by the sovereign (Fitch IDR CCC, Moody's deposits Caa3).",
              s=["corp"], st="flux", neo=[0, ""], src=[["2025 financial statements", FY25], ["LIGA: NBU on a PrivatBank IPO, Jun 2026", IPO]]),
            P("leadership", "Management & supervisory boards", "CEO Mikael Björknert (since January 2025), CFO Larysa Chernyshova, retail chief Dmytro Musiienko, corporate and SME chief Yevhen Zaihraiev, digital chief Marc Krabbenborg, risk chief Oleksii Filipov; supervisory board chaired by Nils Melngailis, with an independent majority.",
              s=["corp"], neo=[0, ""], src=[["PrivatBank: management", MGMT]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & recovery", "blurb": "Since 1992; courts in London and The Hague.", "div": "pb", "rev": "legacy", "products": [
            P("recovery", "Former-owner and Crimea recovery", "Operating since 1992. In 2025 the High Court of England ordered the former owners to compensate the bank, and derecognising their zero-value assets cut the NPL ratio from 59.4% to 10% (3.3% on the post-nationalisation book). On 6 October 2026 a PCA tribunal awarded more than USD 327 million plus interest against Russia for Crimean assets.",
              s=["corp"], o="I", neo=[0, ""], src=[["2025 financial statements", FY25], ["PrivatBank: PCA award, Oct 2026", CRIMEA], ["PrivatBank: about", ABOUT]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology, AI & strategy", "blurb": "AI as the base for growth.", "div": "pb", "rev": "central", "products": [
            P("tech", "Core, payments tech & AI", "Full SWIFT ISO 20022 migration and SEP 4.1 instant 24/7 transfers in 2025; AI named the foundation for future growth, with an award for its AI programme (Frontrunner Awards 2025). About 17,000 employees.",
              s=["corp"], neo=[0, ""], src=[["2025 financial statements", FY25]]),
            P("strategy", "Strategy", "A universal bank focused on retail and small business, growing its corporate share and a high-quality loan book while acting as a systemic state bank in wartime. The public strategy document runs to 2024 ⚠.",
              s=["corp"], neo=[0, ""], src=[["2025 financial statements", FY25], ["PrivatBank: about", ABOUT]]),
            P("ifi", "IFI partnerships", "The largest risk-sharing deal on the Ukrainian market with the EBRD (EUR 625 million of financing) plus IFC and EIB agreements in 2025; 12,100 small firms got UAH 24.5 billion of loans under international programmes.",
              s=["sme", "corp"], lc="borrow", o="P", at="EBRD, IFC, EIB", neo=[0, ""], src=[["2025 financial statements", FY25]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: about 32 million active cards on Visa and Mastercard, credit and premium cards led by Visa Infinite and a Visa gamer card, phone wallets, 350,000 POS terminals with LiqPay and Terminal, the bank's own instalments, and transfers from Mastercard-only cross-border P2P to PrivatMoney and instant SEP.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit & payout cards", "blurb": "32m active cards, both networks.", "div": "pb", "rev": "retail", "products": [
            P("debit", "Payment & payout cards", "Free everyday and payout cards issued on Visa or Mastercard at the customer's choice (Mastercard World and Visa Rewards tiers ⚠): 31.97 million active cards at 1 April 2025, about 54% of Ukraine's active cards. Nilson ranked PrivatBank Europe's largest Visa and Mastercard issuer for 2024.", short="Debit (Visa & Mastercard)",
              s=["con", "abroad", "benef"], lc="everyday", o="P", at="Visa, Mastercard", neo=[1, "Split between Visa and Mastercard; no split published ⚠."],
              mc="The country's largest card base, with no published network split.",
              src=[["Interfax: NBU card data, May 2025", NBUCARDS], ["PrivatBank: Nilson ranking, Jul 2025", NILSON], ["Finance.ua: payout card", PAYOUT]]),
            P("domestic", "PROSTIR & UnionPay", "Connected to the NBU's domestic scheme PROSTIR since December 2017 (about 0.3% of Ukraine's active cards) and a UnionPay participant since November 2019.",
              s=["benef"], lc="everyday", o="P", at="NBU, UnionPay", neo=[0, "PROSTIR and UnionPay."], src=[["PrivatBank: payment systems", PSYS], ["Interfax: NBU card data, May 2025", NBUCARDS]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit & premium cards", "blurb": "Visa Infinite on top.", "div": "pb", "rev": "retail", "products": [
            P("universal", "Universal credit card", "The main credit card, with a grace period of up to 55 days and free delivery in Ukraine and abroad; issued on Visa or Mastercard ⚠ (network choice inferred from the bank's pages).", short="Universal (Visa & Mastercard ⚠)",
              s=["con"], lc="borrow", o="B", neo=[1, "Both networks ⚠."], src=[["PrivatBank: premium cards", PREMIUM], ["Babel: free delivery with Mastercard, Sep 2025", MCDEL]]),
            P("premium", "Premium packages & Visa Infinite", "Premium, Premium PLUS and Premium MAX packages (free or UAH 200–600 a month, credit up to UAH 800,000); the flagship is Visa Infinite, with Visa Signature services, Visa's hotel and restaurant collections, DragonPass and LoungeKey. Package networks are not stated ⚠.",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa Infinite flagship; Mastercard premium tiers not named ⚠."],
              mc="No Mastercard premium tier is visible at Ukraine's biggest issuer.",
              src=[["PrivatBank: premium cards", PREMIUM]]),
            P("katka", "Katka24 gamer card", "Co-branded with Visa and NAVI, launched 14 April 2026 after a December 2025 ecosystem launch: up to 15% gaming cashback on credit funds, a 62-day grace period and interest-free instalments at Comfy, MOYO and Foxtrot.", short="Katka24 (Visa)",
              s=["young"], lc="borrow", st="new", ay="Apr 2026", o="P", at="Visa, NAVI", neo=[0, "Visa."], src=[["PrivatBank: Katka24, Apr 2026", KATKA], ["PrivatBank: Visa and NAVI, Dec 2025", NAVI]]),
        ]},
        {"id": "2.3", "ic": "smartphone", "name": "Phone & watch wallets", "blurb": "First with Apple Pay in Ukraine.", "div": "p24", "rev": "retail", "products": [
            P("wallets", "Apple Pay, Google Pay & Garmin Pay", "Ukraine's first Apple Pay bank (May 2018) and first with Android Pay (November 2017), both for Mastercard and Visa; Garmin Pay from July 2018, launched with Mastercard's Ukraine head quoted.",
              s=["con", "young"], lc="everyday", ay="May 2018", o="P", at="Apple, Google, Garmin", neo=[1, "Tokens on both networks."], src=[["NFCW: Apple Pay, May 2018", APPLEPAY], ["PrivatBank: Garmin Pay, Jul 2018", GARMIN]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Card acceptance", "blurb": "UAH 1 trillion a year.", "div": "liqpay", "rev": "corporate", "products": [
            P("pos", "POS acquiring", "More than 345,000 POS terminals and UAH 1.06 trillion of card payments in 2024 (+24%); UAH 15.8 billion of acquiring commission in 2025; Euromoney's best acquiring bank in Ukraine and a Nilson top-40 global acquirer. The competition authority closed its review of the model in 2025.",
              s=["sme", "corp"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["PrivatBank: acquiring 2024", ACQ24], ["2025 financial statements", FY25]]),
            P("terminal", "Terminal (phone as POS)", "A smartphone acceptance app: UAH 15 billion of turnover in 2025, 78,000+ merchants and 40,000+ active terminals, rolled out at Foxtrot and with a voice readout for blind shoppers.",
              s=["sme"], lc="move", st="new", o="B", neo=[1, "Accepts every network."],
              mc="A home-grown tap-on-phone base Mastercard's acceptance tools could serve.",
              src=[["PrivatBank: business goes mobile, Feb 2026", ACQ25], ["2025 financial statements", FY25]]),
            P("liqpay", "LiqPay & Kasa", "Internet acquiring that processed about UAH 103 billion in 2025 for 25,000+ merchants; 63,984 Kasa virtual tills with UAH 87.6 billion of turnover.",
              s=["sme"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["PrivatBank: business goes mobile, Feb 2026", ACQ25]]),
        ]},
        {"id": "2.5", "ic": "hand-coins", "name": "Instalments", "blurb": "Payment in Parts.", "div": "pb", "rev": "retail", "products": [
            P("parts", "Payment in Parts", "Point-of-sale instalments at partner merchants, funded on the bank's own credit; merchant tariffs cut from October 2024 until the end of 2026. Volumes are not disclosed ⚠.",
              s=["con", "young"], lc="borrow", o="B", neo=[0, "The bank's own instalments."],
              mc="Mastercard Installments has no visible role.",
              src=[["Mind.ua: Payment in Parts tariffs, Oct 2024", PARTS]]),
            P("instbiz", "Instant Instalments for Business", "Instalments for sole proprietors, launched in 2025 and described by the bank as new to the Ukrainian market.",
              s=["sme"], lc="borrow", st="new", o="B", neo=[0, ""], src=[["2025 financial statements", FY25]]),
        ]},
        {"id": "2.6", "ic": "send", "name": "Transfers & instant payments", "blurb": "Cross-border on Mastercard.", "div": "pmoney", "rev": "retail", "products": [
            P("p2pintl", "International card transfers", "International P2P transfers sent only from a PrivatBank Mastercard currency card, at a reduced 1% fee; cashback campaigns with Mastercard for sending and receiving ran from March 2025 to April 2026 (up to UAH 100,000).", short="Cross-border P2P (Mastercard)",
              s=["abroad"], lc="move", o="P", at="Mastercard", neo=[2, "Sending is Mastercard-only; product name not stated ⚠."],
              mc="Mastercard's clearest exclusive at PrivatBank, serving millions of Ukrainians abroad.",
              src=[["Babel: transfer cashback, Dec 2025", MCX3], ["PrivatBank: transfer cashback, Nov 2025", MCX2]]),
            P("pmoney", "PrivatMoney", "The bank's own money-transfer system since 2010, confirmed as a significant payment system in 2025, with new partners in Canada (Ukrainian Credit Union) and Ukraine (Raiffeisen Bank).",
              s=["abroad"], lc="move", o="B", neo=[0, "The bank's own system."], src=[["2025 financial statements", FY25], ["PrivatBank: payment systems", PSYS]]),
            P("remit", "Remittance networks", "A direct participant in Ria, Western Union, MoneyGram, MEEST and Intelexpress.",
              s=["abroad"], lc="move", o="P", at="Ria, Western Union, MoneyGram", neo=[0, ""], src=[["PrivatBank: payment systems", PSYS]]),
            P("sep", "Instant SEP transfers", "Instant 24/7 account transfers through the NBU's SEP 4.1 since 2025, and an AI-driven P2P limit system under the NBU transfer memorandum.",
              s=["con", "sme"], lc="move", st="new", o="P", at="NBU", neo=[0, "Account-to-account."], src=[["2025 financial statements", FY25]]),
            P("rtp", "Request to Pay", "Split-the-bill payment requests built with Visa, a first in Ukraine (2025).",
              s=["con", "young"], lc="move", st="new", o="P", at="Visa", neo=[0, "Visa."], src=[["2025 financial statements", FY25]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: AI transfer limits, Visa's authentication framework and a document-fraud link to the Interior Ministry, Ukraine's first agentic payment on Mastercard Agent Pay, AI tools for business, the Pryvit loyalty programme and paid subscriptions, and charity tools.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & identity", "blurb": "AI limits, Visa DAF.", "div": "pb", "rev": "retail", "products": [
            P("p2pai", "AI transfer limits", "A flexible P2P limit system built on AI, the first under the NBU's memorandum on individual transfers (2025).",
              s=["con"], lc="move", st="new", o="B", neo=[0, "The bank's own."], src=[["2025 financial statements", FY25]]),
            P("daf", "Visa Digital Authentication Framework", "Lighter online-payment authentication on EMV 3-D Secure and Visa tokens, launched with Visa in August 2023 as a world first.",
              s=["con"], lc="move", ay="Aug 2023", o="P", at="Visa", neo=[0, "Visa."], src=[["Ekonomichna Pravda: Visa DAF, Aug 2023", DAF]]),
            P("docfraud", "Document fraud & verification", "A September 2026 agreement with the Interior Ministry and State Migration Service to check passports via the Trembita data exchange before accounts open, and sign-language video verification for new clients.",
              s=["con"], lc="open", st="new", ay="Sep 2026", o="P", at="Interior Ministry", neo=[0, ""],
              mc="Identity and scam scoring are needs with no Mastercard tool in sight.",
              src=[["PrivatBank: document fraud, Sep 2026", FRAUDMIA], ["PrivatBank: sign-language verification, Sep 2026", SIGN]]),
            P("facepay", "FacePay24", "Pay by face with a linked Visa card, launched with Visa and AWS in September 2019 ⚠ current status unknown.",
              s=["con"], lc="everyday", ay="Sep 2019", o="P", at="Visa, AWS", neo=[0, "Visa."], src=[["UNIAN: FacePay24, Sep 2019", FACEPAY]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI & agentic commerce", "blurb": "Ukraine's first agent payment.", "div": "p24", "rev": "retail", "products": [
            P("agentpay", "Mastercard Agent Pay", "Ukraine's first payment made by an AI agent, completed with Mastercard Agent Pay and announced on 23 June 2026 (possibly in a test environment ⚠); both sides plan more use cases. Named: Inga Andreieva (Mastercard) and Dmytro Musiienko (PrivatBank).", short="Agent Pay (Mastercard)",
              s=["con"], lc="everyday", st="new", ay="Jun 2026", o="P", at="Mastercard", neo=[3, "Mastercard's own product."],
              mc="The newest and most strategic Mastercard first at the bank.",
              src=[["Mastercard: Agent Pay with PrivatBank, Jun 2026", AGENT], ["PrivatBank: Agent Pay, Jun 2026", AGENTPB]]),
            P("aibiz", "AI tools for business", "Payments built from a photo or text, AI checks on a partner's reputation, an AI assistant for foreign-trade contracts, and automatic income-limit control for sole proprietors (September 2026).",
              s=["sme"], lc="everyday", st="new", o="B", neo=[0, ""], src=[["2025 financial statements", FY25], ["PrivatBank: income-limit control, Sep 2026", INCOME]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Loyalty & subscriptions", "blurb": "Pryvit and Privat PRO.", "div": "pryvit", "rev": "retail", "products": [
            P("pryvit", "Pryvit", "AI-personalised cashback and discounts in Privat24 since May 2024: 735 million offers in the first year and more than 1,500 partners; cited in Euromoney's 2025 Best Bank award.",
              s=["con", "young"], lc="grow", ay="May 2024", o="B", neo=[0, "Network-neutral."],
              mc="Card-linked offers and merchant data could feed Pryvit.",
              src=[["PrivatBank: Pryvit's first year, May 2025", PRYVIT], ["2025 financial statements", FY25]]),
            P("subs", "Subscriptions", "Basic (free), Privat PRO (UAH 129 a month) and Joint PRO (UAH 297 for five people), opened in September 2026: up to UAH 1,000 a month of benefits with Nova Poshta, Silpo, WOG, Netflix, Spotify and others, and up to 7% on Envelopes.",
              s=["con"], lc="everyday", st="new", ay="Sep 2026", o="B", neo=[0, ""],
              mc="Recurring-payment and benefit tools fit a new paid tier.",
              src=[["PrivatBank: Subscriptions, Sep 2026", SUBS]]),
        ]},
        {"id": "3.4", "ic": "users-round", "name": "Charity & community", "blurb": "Envelopes, Dobro, Superhumans.", "div": "p24", "rev": "retail", "products": [
            P("envelopes", "Envelopes & Dobro", "Envelopes for savings and fundraising (680+ opened by foundations in 2025) and Dobro, listing 5,500+ verified fundraisers; UAH 246 million of the bank's own charity in 2025.",
              s=["con"], lc="grow", o="B", neo=[0, ""], src=[["2025 financial statements", FY25]]),
            P("community", "Programmes with Mastercard", "A second Superhumans fundraiser with Mastercard (UAH 4.3 million for facial reconstruction) and business, export and startup schools for veterans and entrepreneurs with OLX, the EBA and Mastercard (12,000+ users).",
              s=["sme"], lc="beyond", o="P", at="Mastercard, OLX, EBA", neo=[1, "Mastercard a named partner."], src=[["2025 financial statements", FY25]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: retail deposits above UAH 500 billion and consumer credit, banking for 950,000 businesses, a corporate book that quadrupled in 2025, government bonds in the app, and state and humanitarian payments through Diia.Card and UNHCR.",
    "tiles": [
        {"id": "4.1", "ic": "wallet", "name": "Retail accounts & lending", "blurb": "UAH 500bn+ of retail deposits.", "div": "pb", "rev": "retail", "products": [
            P("deposits", "Accounts & deposits", "Retail deposits above UAH 500 billion at end-2025, a record, with a full deposit guarantee under martial law; 18 million individual customers.",
              s=["con", "benef"], lc="grow", neo=[1, "Cards on Visa or Mastercard."], src=[["2025 financial statements", FY25], ["H1 2026 results", H1]]),
            P("consumer", "Consumer credit", "Credit cards are the main retail credit book, alongside consumer loans with retail chains and mortgages; the retail segment earned UAH 40 billion after tax in 2025.",
              s=["con"], lc="borrow", neo=[1, "Credit cards on both networks ⚠."], src=[["2025 financial statements", FY25]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "Small business", "blurb": "950,000 business customers.", "div": "p24b", "rev": "corporate", "products": [
            P("sme", "SME banking", "950,000 business customers, international-programme loans, foreign-exchange trading almost round the clock, and recognition among the best banks for business in Eastern Europe (September 2026).",
              s=["sme"], lc="everyday", neo=[None, "Business-card network not stated ⚠."],
              mc="Commercial and virtual cards for small firms are open ground.",
              src=[["H1 2026 results", H1], ["PrivatBank: SME study, Sep 2026", SMEAWARD], ["2025 financial statements", FY25]]),
        ]},
        {"id": "4.3", "ic": "factory", "name": "Corporate banking", "blurb": "Book up fourfold in 2025.", "div": "pb", "rev": "corporate", "products": [
            P("corp", "Corporate banking", "Large-corporate loans up fourfold in 2025 (+UAH 11.3 billion), financing energy, defence, manufacturing, agriculture and logistics, with project finance, factoring and trade finance added in 2026.",
              s=["corp"], lc="borrow", st="new", neo=[0, ""],
              mc="Commercial cards and payment controls could follow the lending.",
              src=[["2025 financial statements", FY25], ["Q1 2026 results", Q1]]),
        ]},
        {"id": "4.4", "ic": "chart-candlestick", "name": "Investments", "blurb": "Bonds in the app.", "div": "p24", "rev": "markets", "products": [
            P("bonds", "Government bonds & investments", "Domestic government bonds bought and sold in the Privat24 app and a 24/7 investment platform on the web (2025).",
              s=["con"], lc="grow", st="new", neo=[0, ""], src=[["2025 financial statements", FY25]]),
        ]},
        {"id": "4.5", "ic": "hand-coins", "name": "State & humanitarian payments", "blurb": "Diia.Card, UNHCR.", "div": "pb", "rev": "retail", "products": [
            P("diia", "Diia.Card", "A free digital card in Privat24 for all state payments (school pack UAH 5,000, Winter 6500, veterans' sport, health screening), launched in 2025. Network not stated ⚠.",
              s=["benef"], lc="everyday", st="new", o="P", at="Government of Ukraine", neo=[None, "Network not stated ⚠."], src=[["PrivatBank: Diia.Card", DIIA], ["2025 financial statements", FY25]]),
            P("unhcr", "Humanitarian payments", "A UNHCR partnership that processed 4.1 million charitable aid payments worth UAH 10 billion in 2025, plus pension and social-payment cards.",
              s=["benef"], lc="everyday", o="P", at="UNHCR", neo=[None, ""], src=[["2025 financial statements", FY25]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: Privat24 for 13.7 million, Privat24 for Business, 1,000+ branches with 7,500 ATMs and 10,000 self-service terminals, cards posted free to 60+ countries, and payment partners.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Privat24", "blurb": "13.7 million users.", "div": "p24", "rev": "retail", "products": [
            P("p24app", "Privat24", "13.7 million users (H1 2026), with zero-rated data on Vodafone and lifecell, eSIM sales, rail tickets in Germany, Austria and Czechia, and sign-language consultations.",
              s=["con", "young", "abroad", "benef"], lc="everyday", neo=[0, ""], src=[["H1 2026 results", H1], ["2025 financial statements", FY25]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Privat24 for Business", "blurb": "Online accounts for firms.", "div": "p24b", "rev": "corporate", "products": [
            P("p24biz", "Privat24 for Business", "Online account opening for legal entities (2025), electronic documents, AI tools and foreign-exchange trading.",
              s=["sme", "corp"], lc="open", neo=[0, ""], src=[["2025 financial statements", FY25]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & self-service", "blurb": "1,000+ branches.", "div": "pb", "rev": "retail", "products": [
            P("branches", "Branches, ATMs & terminals", "More than 1,000 branches (1,059 registered units at end-2025), about 7,500 ATMs and nearly 10,000 self-service terminals; branches served as Invincibility Points in winter blackouts.",
              s=["con", "benef"], lc="everyday", neo=[0, ""], src=[["PrivatBank: Subscriptions, Sep 2026", SUBS], ["2025 financial statements", FY25], ["Q1 2026 results", Q1]]),
        ]},
        {"id": "5.4", "ic": "earth", "name": "Cards abroad", "blurb": "Free delivery to 60+ countries.", "div": "pb", "rev": "retail", "products": [
            P("delivery", "Free card delivery abroad", "Cards ordered in Privat24 and posted free to more than 60 countries, mostly Poland, Germany and Czechia, in a programme with Mastercard (September 2025, reported extended to end-2026 ⚠); Visa runs a similar programme ⚠.",
              s=["abroad"], lc="open", o="P", at="Mastercard, Visa", neo=[1, "Joint with Mastercard; Visa too ⚠."], src=[["Babel: free delivery with Mastercard, Sep 2025", MCDEL]]),
        ]},
        {"id": "5.5", "ic": "plug", "name": "Payment partners", "blurb": "iPay, Portmone, RozetkaPay.", "div": "liqpay", "rev": "corporate", "products": [
            P("partners", "Payment partners", "Payment providers working through the bank as indirect participants, including iPay, Portmone, WayForPay, RozetkaPay and KastaPay.",
              s=["sme"], lc="move", o="P", at="iPay, Portmone, WayForPay", neo=[1, "Visa, Mastercard and PROSTIR."], src=[["PrivatBank: payment systems", PSYS]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at PrivatBank", "blurb": "Half the cards, cross-border, Agent Pay.", "products": [
        P("mcatpb", "Mastercard at PrivatBank", "PrivatBank issues Visa and Mastercard side by side and publishes no split; Ukraine's cards are about evenly divided, with Visa ahead on cards in circulation since 2025 and Mastercard ahead on active cards. Mastercard has international P2P sending, free card delivery abroad, transfer campaigns, community programmes and, since June 2026, the country's first Agent Pay transaction. Visa has the premium flagship, the gamer card, DAF, FacePay24 and Request to Pay.",
          s=["con"], div="pb", rev="retail", mc="The relationship this map is drawn for.",
          src=[["Interfax: NBU card data, May 2025", NBUCARDS], ["Mastercard: Agent Pay with PrivatBank, Jun 2026", AGENT]]),
    ]},
    {"id": "pillar-market", "name": "Ukrainian banking", "blurb": "War, state banks, an IPO.", "products": [
        P("market", "The Ukrainian market", "War, blackouts and a shrinking population; state banks hold most sector assets ⚠; Visa and Mastercard level on cards with PROSTIR at 0.3%; monobank the fastest-growing rival; privatisation of state banks under way, with a PrivatBank IPO under study for 2027 ⚠.",
          s=["con"], div="pb", rev="central", src=[["Interfax: NBU card data, May 2025", NBUCARDS], ["LIGA: NBU on a PrivatBank IPO, Jun 2026", IPO], ["Komersant: top-10 banks, 2025", TOP10]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
