"""HSBC Holdings' layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the 2026 interim results (4 August 2026), the 2025
results and Annual Report (25 February 2026). ``neo`` is the Mastercard lens: [depth, note], where
3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

FY25 = "https://www.hsbc.com/-/files/hsbc/investors/hsbc-results/2025/annual/pdfs/hsbc-holdings-plc/260225-annual-results-2025-media-release.pdf"
ARA25 = "https://www.hsbc.com/-/files/hsbc/investors/hsbc-results/2025/annual/pdfs/hsbc-holdings-plc/260225-annual-report-and-accounts-2025.pdf"
H1 = "https://www.hsbc.com/-/files/hsbc/investors/hsbc-results/2026/interim/pdfs/hsbc-holdings-plc/260804-hsbc-holdings-plc-interim-results-2026-media-release.pdf"
GLANCE = "https://www.hsbc.com/who-we-are/hsbc-at-a-glance"
RATINGS = "https://www.hsbc.com/investors/fixed-income-investors/credit-ratings"
MCAP = "https://companiesmarketcap.com/hsbc/marketcap/"
EXCO = "https://www.hsbc.com/who-we-are/our-people/senior-management"
HANGSENG = "https://www.hsbc.com/investors/hsbc-proposal-to-privatise-hang-seng-bank"
REDCOIN = "https://www.about.hsbc.com.hk/news-and-media/hsbc-names-stablecoin-hsbc-redcoin"
LICENCE = "https://www.theasianbanker.com/press-releases/hsbc-to-launch-hkd-denominated-stablecoin-in-second-half-of-2026"
SWIFT = "https://www.about.hsbc.com.hk/news-and-media/hsbc-and-standard-chartered-execute-first-live-tokenised-deposit-transaction-on-swifts-blockchain"
NIO = "https://www.hsbc.com/news-and-views/news/hsbc-news-archive/hsbc-launches-hsbcnio-digital-banking-solution-for-businesses"
GOOGLE = "https://www.hsbc.com/news-and-views/news/hsbc-news-archive/hsbc-and-google-cloud-announce-transformative-ai-banking-partnership"
AICOE = "https://www.hsbc.com/news-and-views/news/hsbc-news-archive/hsbc-to-establish-global-ai-centre-of-excellence-in-singapore"
VISAAI = "https://www.about.hsbc.co.uk/news-and-media/hsbc-uk-leading-the-next-step-in-ai-powered-shopping-with-visa"
UKNEWS = "https://www.about.hsbc.co.uk/news-and-media"
PWE = "https://about.hsbc.co.uk/news-and-media/hsbc-uk-unveils-new-best-in-class-premier-world-elite-credit-card"
FLEXIPAY = "https://www.about.hsbc.co.uk/news-and-media/hsbc-uk-enters-point-of-sale-finance-market-with-flexipay"
RECYCLE = "https://www.about.hsbc.co.uk/news-and-media/hsbc-uk-and-mastercard-launch-payment-card-recycling-pilot"
PWEPAGE = "https://www.hsbc.co.uk/credit-cards/products/premier-world-elite/"
REWARDS = "https://www.hsbc.co.uk/credit-cards/products/rewards/"
GLOBALMONEY = "https://www.hsbc.co.uk/current-accounts/products/global-money/"
UKACCOUNTS = "https://www.hsbc.co.uk/current-accounts/"
UKCARDS = "https://www.hsbc.co.uk/credit-cards/"
FIRSTDIRECT = "https://www.firstdirect.com/banking/current-account/"
HKCARDS = "https://www.hsbc.com.hk/credit-cards/"
EVERYMILE = "https://www.hsbc.com.hk/credit-cards/products/everymile/"
MXCARDS = "https://www.hsbc.com.mx/tarjetas-de-credito/"
MXVIVA = "https://www.about.hsbc.com.mx/-/media/mexico/es/news-and-media/220912-comunicado-hsbc-viva-aerobus.pdf"
MXONE = "https://mx.linkedin.com/in/asalazarp/en"
LEGEND = "https://newsroom.mastercard.com/news/ap/en/newsroom/press-releases/en/2026/hsbc-hong-kong-introduces-asia-pacific-s-first-world-legend-mastercard/"
UAEVIRTUAL = "https://newsroom.mastercard.com/news/eemea/en/newsroom/press-releases/en/2026/june-2026/hsbc-and-mastercard-accelerate-growth-of-digital-b2b-payments-with-launch-of-mobile-virtual-card-solution/"
HKVIRTUAL = "https://newsroom.mastercard.com/news/ap/en-hk/newsroom/press-releases/en-hk/2025/mastercard-and-hsbc-unveil-first-mobile-virtual-corporate-card-in-hong-kong/"
LIVENATION = "https://www.mastercard.com/news/ap/en-hk/newsroom/press-releases/en-hk/2025/mastercard-and-hsbc-hong-kong-partner-to-offer-cardholders-privileged-access-to-live-nation-events/"
HSBIZ = "https://newsroom.mastercard.com/news/ap/en-hk/newsroom/press-releases/en-hk/2025/hang-seng-bank-and-mastercard-join-hands-to-advance-electronic-payments-for-enterprises/"
MCHK = "https://newsroom.mastercard.com/news/ap/en-hk/newsroom/press-releases/"
TRACK = "https://newsroom.mastercard.com/news/europe/en-uk/newsroom/press-releases/en-gb/2022/march/mastercard-track-card-to-account-transfer-launches-in-the-uk-with-hsbc/"
WHOLESALE = "https://newsroom.mastercard.com/news/eemea/en/newsroom/press-releases/en/2024/may/mastercard-and-hsbc-middle-east-accelerate-travel-payment-innovation-through-bank-s-first-wholesale-travel-program/"
CITYPOSSIBLE = "https://investor.mastercard.com/investor-news/investor-news-details/2020/Mastercard-Launches-Partnership-with-HSBC-to-Promote-More-Sustainable-and-Inclusive-Communities/default.aspx"
MC2010 = "https://www.electronicpaymentsinternational.com/news/hsbc-and-mastercard-renews-partnership/"
VISAMENA = "https://www.electronicpaymentsinternational.com/news/hsbc-signs-five-year-deal-with-visa"
VISAAPAC = "https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.7861.html"
ZING = "https://www.bankingdive.com/news/hsbc-sunsets-year-old-app-zing/738675/"
MCUK = "https://newsroom.mastercard.com/news/europe/en-uk/newsroom/press-releases/"
MCAPAC = "https://newsroom.mastercard.com/news/ap/en/newsroom/press-releases/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · entities · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $3.4 trillion of assets and RoTE of 18.2% in the first half of 2026, banks founded in Hong Kong and Shanghai in 1865, a Google Cloud AI deal, and a simpler group after Hang Seng was taken private and a dozen markets were sold.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "$3.4tn of assets, RoTE 18.2%.", "div": "hsbc", "rev": "cc", "products": [
            P("balance", "Balance sheet & earnings", "Total assets of $3.438 trillion, loans of $1.022 trillion and customer accounts of $1.828 trillion at 30 June 2026; profit before tax of $19.5 billion in the half (RoTE 18.2%, CET1 14.1%) and $29.9 billion in 2025; about 41 million customers in 56 markets; market value about $323 billion on 16 October 2026 ⚠.",
              s=["con", "corp"], neo=[0, ""], src=[["2026 interim results", H1], ["2025 results", FY25], ["HSBC at a glance", GLANCE], ["Market cap ⚠", MCAP]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Nelson and Elhedery.", "div": "hsbc", "rev": "cc", "products": [
            P("leadership", "Board & executive committee", "Chairman Brendan Nelson (since October 2025), CEO Georges Elhedery (since September 2024), CFO Pam Kaur, CIO Stuart Riley; Michael Roberts runs CIB, Barry O'Byrne IWPB, David Lindberg HSBC UK (from December 2025) and Maggie Ng Hong Kong.",
              s=["corp"], neo=[0, ""], src=[["HSBC: senior management", EXCO], ["HSBC UK newsroom", UKNEWS]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & entities", "blurb": "Hong Kong and Shanghai, 1865.", "div": "hsbc", "rev": "cc", "products": [
            P("entities", "Licensed banks & brands", "Founded in Hong Kong and Shanghai in 1865 to finance trade; HSBC UK Bank (ring-fenced), HSBC Bank plc, The Hongkong and Shanghai Banking Corporation, Hang Seng Bank, HSBC Bank USA, HSBC Continental Europe, HSBC Bank Middle East, HSBC Bank Australia and HSBC Innovation Bank; group rated A+/A3/A- by Fitch, Moody's and S&P.",
              s=["corp"], o="I", neo=[0, ""], src=[["Annual Report 2025", ARA25], ["HSBC: credit ratings", RATINGS]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "Google Cloud, 31,000 engineers.", "div": "hsbc", "rev": "cc", "products": [
            P("tech", "Cloud & AI", "More than 100 generative-AI uses and an AI coding assistant for 31,000 engineers; a multi-year Google Cloud partnership (June 2026) putting Gemini and agentic AI into wealth, financial-crime monitoring and a relationship-manager assistant, and a Global AI Centre of Excellence in Singapore (July 2026).",
              s=["corp"], st="new", o="P", at="Google Cloud", neo=[0, ""], src=[["Google Cloud partnership, Jun 2026", GOOGLE], ["AI Centre of Excellence, Jul 2026", AICOE], ["2025 results", FY25]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & reshaping", "blurb": "Four businesses, fewer markets.", "div": "hsbc", "rev": "cc", "products": [
            P("strategy", "2026–28 targets", "Four businesses since January 2025; RoTE of at least 17% excluding notable items each year to 2028, revenue growth rising to 5% in 2028, CET1 of 14–14.5%, $1.5 billion of cost savings actioned by June 2026, and Hong Kong as the world's leading cross-border wealth hub by 2029.",
              s=["corp"], neo=[0, ""], src=[["2025 results", FY25], ["2026 interim results", H1]]),
            P("exits", "Exits", "Canada sold to RBC, Argentina to Galicia, French retail and home loans, UK life insurance to Chesnara (January 2026), Uruguay (July 2026), and in summer 2026 Australian home and personal loans to Virgo BidCo, Egypt retail to Emirates NBD and Singapore life insurance to Allianz.",
              s=["con"], st="flux", neo=[0, ""], src=[["Annual Report 2025", ARA25], ["2026 interim results", H1]]),
            P("hangsengdeal", "Hang Seng privatisation", "Hang Seng Bank taken private for HK$106 billion ($13.7 billion): effective 26 January 2026 and delisted the next day, costing about 110bps of CET1, with $0.5 billion of synergies expected by 2028; the brand stays.",
              s=["con"], o="A", st="new", ay="Jan 2026", neo=[0, ""], src=[["HSBC: Hang Seng proposal", HANGSENG], ["2025 results", FY25]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Eight ways money moves: UK credit on Mastercard and debit on Visa, Global Money on Visa, Hong Kong cards split three ways, Hang Seng on Mastercard, Mexico split and the Gulf on Visa, commercial and virtual cards on Mastercard, Global Payments Solutions, and PayMe, tokenised deposits and a Hong Kong dollar stablecoin.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "UK cards", "blurb": "Mastercard credit, Visa debit.", "div": "uk", "rev": "uk", "products": [
            P("ukcredit", "HSBC UK credit cards", "Premier World Elite (launched October 2024, £290 a year) and the Rewards card on Mastercard; Balance Transfer, Purchase Plus and Classic do not name a scheme ⚠ assumed Mastercard; UK card balances of $8.3 billion at end-2025.", short="UK credit (Mastercard)",
              s=["con", "premier"], lc="borrow", ay="Oct 2024", o="P", at="Mastercard", neo=[2, "Mastercard ⚠ for the non-premium cards."],
              mc="Mastercard's anchor in the UK, and the base for any agentic or scam work.",
              src=[["Premier World Elite launch, Oct 2024", PWE], ["Premier World Elite", PWEPAGE], ["HSBC UK: Rewards card", REWARDS], ["HSBC UK: credit cards", UKCARDS]]),
            P("ukdebit", "HSBC UK debit", "The main current-account debit card ⚠ Visa, inferred from a page asset rather than stated in text.", short="UK debit (Visa ⚠)",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa ⚠."], src=[["HSBC UK: current accounts", UKACCOUNTS]]),
            P("fddebit", "first direct debit", "A virtual card on opening, with Apple Pay, Google Pay and Samsung Pay and a £210 switching offer ⚠ network not stated.", div="fd",
              s=["con"], lc="everyday", neo=[None, "Network not stated."], src=[["first direct: current account", FIRSTDIRECT]]),
        ]},
        {"id": "2.2", "ic": "globe", "name": "Global Money", "blurb": "18 currencies on Visa.", "div": "uk", "rev": "uk", "products": [
            P("globalmoney", "Global Money Account", "Holds 18 currencies and sends to about 200 countries, with no HSBC FX fee on card spending; the card is a Visa debit.", short="Global Money (Visa)",
              s=["con", "intl"], lc="move", o="B", at="Visa", neo=[0, "Visa."],
              mc="Cross-border consumer money is a Visa card today; Mastercard would have to displace it.",
              src=[["HSBC UK: Global Money", GLOBALMONEY]]),
            P("zing", "Zing", "A cross-border money app launched in January 2024 and closed on 22 May 2025, its customers moved to Global Money.",
              s=["intl"], lc="move", st="retired", neo=[None, "Network not in sources."], src=[["Banking Dive: Zing closure, Jan 2025", ZING]]),
        ]},
        {"id": "2.3", "ic": "wallet-cards", "name": "Hong Kong cards", "blurb": "Three networks.", "div": "hk", "rev": "hk", "products": [
            P("hkmc", "Premier & Privé World Legend Mastercard", "The HSBC Premier Mastercard and the Privé World Legend Mastercard (May 2026), Asia-Pacific's first World Legend card, in The Mastercard Collection.", short="HK premium credit (Mastercard)",
              s=["premier"], lc="borrow", st="new", ay="May 2026", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard holds the top of HSBC's Hong Kong card range.",
              src=[["Mastercard: World Legend, May 2026", LEGEND], ["HSBC HK: credit cards", HKCARDS]]),
            P("hkvisa", "Visa Signature, Gold, easy & EveryMile", "Visa Signature, Visa Gold and the easy card, earning up to 3.6% RewardCash, and EveryMile at HK$2 a mile ⚠ Visa inferred from its concierge.", short="HK credit (Visa)",
              s=["con"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["HSBC HK: credit cards", HKCARDS], ["HSBC HK: EveryMile", EVERYMILE]]),
            P("hkup", "Pulse & UnionPay Dual Currency", "UnionPay credit cards for spending in mainland China and Hong Kong.", short="HK credit (UnionPay)",
              s=["con"], lc="borrow", o="P", at="UnionPay", neo=[0, "UnionPay."], src=[["HSBC HK: credit cards", HKCARDS]]),
            P("hkred", "HSBC Red", "Up to 8% back at selected merchants and 4% online ⚠ network not stated.",
              s=["con"], lc="borrow", neo=[None, "Network not stated."], src=[["HSBC HK: credit cards", HKCARDS]]),
            P("hkdebit", "HSBC Hong Kong debit", "A Mastercard debit range, with supplementary Mastercard debit cards from February 2022; Hong Kong card balances of $9.7 billion at end-2025.", short="HK debit (Mastercard)",
              s=["con"], lc="everyday", ay="Feb 2022", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Mastercard HK newsroom", MCHK], ["Annual Report 2025", ARA25]]),
        ]},
        {"id": "2.4", "ic": "credit-card", "name": "Hang Seng cards", "blurb": "MMPOWER on Mastercard.", "div": "hangseng", "rev": "hk", "products": [
            P("mmpower", "MMPOWER World Mastercard", "Hang Seng's World Mastercard, launched 31 May 2023 ⚠ networks of other Hang Seng cards not confirmed.", short="MMPOWER (Mastercard)",
              s=["con"], lc="borrow", ay="May 2023", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Mastercard HK newsroom", MCHK]]),
            P("hsbizdebit", "Commercial Multi-Currency Debit Mastercard", "Hong Kong's first business World debit card, launched 15 April 2025.", short="Hang Seng business debit (Mastercard)",
              s=["sme"], lc="everyday", st="new", ay="Apr 2025", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Mastercard: Hang Seng commercial debit, Apr 2025", HSBIZ]]),
        ]},
        {"id": "2.5", "ic": "earth", "name": "Mexico & the Gulf", "blurb": "Split, and Visa.", "div": "mx", "rev": "iwpb", "products": [
            P("mxcards", "HSBC Mexico cards", "Premier World Elite and the Viva Aerobus VIVA cards (September 2022) on Mastercard ⚠, the 2026 One+ card on Visa ⚠ tied to the FIFA World Cup, and 2Now, Zero and AIR with no scheme stated; $2.3 billion of balances.", short="Mexico cards (split)",
              s=["con", "premier"], lc="borrow", o="P", at="Mastercard, Visa", neo=[1, "Split: Mastercard premium and VIVA, Visa One+ ⚠."],
              src=[["HSBC Mexico: credit cards", MXCARDS], ["HSBC Mexico: VIVA, Sep 2022 ⚠", MXVIVA], ["One+ Visa ⚠", MXONE]]),
            P("menacards", "Middle East debit & credit", "Visa debit and credit across the region, 10 million cards under a five-year exclusive debit renewal in July 2013; current terms not public ⚠.", div="me", short="Gulf cards (Visa)",
              s=["con"], lc="everyday", ay="Jul 2013", o="P", at="Visa", neo=[0, "Visa."], src=[["EPI: Visa MENA deal, Jul 2013", VISAMENA]]),
        ]},
        {"id": "2.6", "ic": "briefcase-business", "name": "Commercial & virtual cards", "blurb": "Mastercard in four markets.", "div": "hsbc", "rev": "cib", "products": [
            P("trackc2a", "Track Card-to-Account", "HSBC was the first UK issuer of Mastercard Track Card-to-Account Transfer, letting commercial cards pay suppliers' bank accounts (March 2022).",
              s=["sme", "corp"], lc="move", ay="Mar 2022", o="P", at="Mastercard", neo=[3, "Mastercard Track."], src=[["Mastercard: Track C2A with HSBC, Mar 2022", TRACK]]),
            P("hkvirtual", "Virtual Mastercard Programme", "Hong Kong's first mobile virtual corporate card, tokenised and run on Mastercard In Control Pay (June 2025).",
              s=["corp"], lc="move", st="new", ay="Jun 2025", o="P", at="Mastercard", neo=[3, "Mastercard In Control."], div="hk",
              mc="A proven template for virtual cards across Global Payments Solutions.",
              src=[["Mastercard: HK virtual corporate card, Jun 2025", HKVIRTUAL]]),
            P("uaevirtual", "UAE mobile virtual cards", "Mobile virtual cards for business clients on Mastercard In Control for Mobile Payments (June 2026).",
              s=["corp"], lc="move", st="new", ay="Jun 2026", o="P", at="Mastercard", neo=[3, "Mastercard In Control."], div="me",
              src=[["Mastercard: UAE mobile virtual card, Jun 2026", UAEVIRTUAL]]),
            P("wholesale", "Mastercard Wholesale Program", "Virtual cards for travel companies paying hotels and airlines, HSBC Middle East's first wholesale travel programme (May 2024).",
              s=["corp"], lc="move", ay="May 2024", o="P", at="Mastercard", neo=[3, "Mastercard Wholesale."], div="me",
              src=[["Mastercard: Wholesale Program, May 2024", WHOLESALE]]),
            P("bizdebit", "Twelve-currency business debit", "A Hong Kong business debit Mastercard holding twelve currencies, launched November 2021.",
              s=["sme"], lc="everyday", ay="Nov 2021", o="P", at="Mastercard", neo=[2, "Mastercard."], div="hk", src=[["Mastercard HK newsroom", MCHK]]),
        ]},
        {"id": "2.7", "ic": "send", "name": "Payments & collections", "blurb": "$500tn a year.", "div": "hsbc", "rev": "cib", "products": [
            P("gps", "Global Payments Solutions", "About $500 trillion of payments a year in 130 currencies; $2.29 billion of fee and other income in 2025, within $10.9 billion of wholesale transaction banking; ranked first for cash management by Euromoney.",
              s=["corp", "sme"], lc="move", neo=[0, ""], src=[["Annual Report 2025", ARA25], ["2025 results", FY25]]),
            P("dms", "Digital Merchant Services", "Omnichannel and wallet collections for corporate merchants in Hong Kong, India and Singapore, with six more markets due in 2026 ⚠ acquiring partners not disclosed.",
              s=["corp"], lc="move", st="new", neo=[None, "Acquirer and networks not disclosed."],
              mc="Six new markets need gateway, tokenisation and Click to Pay.",
              src=[["2025 results", FY25]]),
        ]},
        {"id": "2.8", "ic": "coins", "name": "Wallets & digital money", "blurb": "PayMe, RedCoin, tokens.", "div": "hk", "rev": "cib", "products": [
            P("payme", "PayMe", "Hong Kong's person-to-person and merchant wallet, with more than 3.3 million users (April 2026).",
              s=["con"], lc="move", neo=[None, "Card links not public."], src=[["Asian Banker: stablecoin licence, Apr 2026", LICENCE]]),
            P("redcoin", "HSBC RedCoin", "A Hong Kong dollar stablecoin, licensed on 10 April 2026 and named on 30 September 2026, due in the second half of 2026 for person-to-person and merchant payments through PayMe and the HK app.", short="RedCoin (stablecoin)",
              s=["con"], lc="move", st="new", ay="Sep 2026", neo=[0, "HSBC's own."],
              mc="A direct substitute for cards at Hong Kong merchants.",
              src=[["HSBC: RedCoin, Sep 2026", REDCOIN], ["Asian Banker: stablecoin licence, Apr 2026", LICENCE]]),
            P("tds", "Tokenised Deposit Service", "Round-the-clock cross-border transfers in seven currencies across Hong Kong, Singapore, the UK, Luxembourg, the US and the UAE; first live interbank transaction on Swift's ledger with Standard Chartered (20 August 2026).", div="hsbc",
              s=["corp"], lc="move", st="new", neo=[0, "HSBC's own."], src=[["HSBC: Swift tokenised deposit, Aug 2026", SWIFT]]),
            P("orion", "HSBC Orion & Gold Token", "Digital bonds, tokenised gold, and the technology behind the UK's first digital gilt.", div="hsbc",
              s=["corp", "premier"], lc="grow", neo=[0, ""], src=[["Asian Banker: stablecoin licence, Apr 2026", LICENCE], ["2026 interim results", H1]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: AI watching about a billion transactions a month, an agentic shopping trial with Visa, rewards from RewardCash to Mastercard's Pay with Rewards, and card recycling with Mastercard.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & financial crime", "blurb": "A billion transactions a month.", "div": "hsbc", "rev": "cc", "products": [
            P("fincrime", "Financial-crime monitoring", "Agentic AI with Google Cloud monitoring about a billion transactions a month and aiming to respond twice as fast; a $0.4 billion fraud-related UK securitisation charge in the first half of 2026.",
              s=["con", "corp"], lc="everyday", st="new", o="P", at="Google Cloud", neo=[0, "HSBC's own, with Google."],
              mc="No Mastercard scam or fraud tool is in public view, against UK appetite shown by NatWest.",
              src=[["Google Cloud partnership, Jun 2026", GOOGLE], ["2026 interim results", H1], ["Mastercard UK newsroom", MCUK]]),
        ]},
        {"id": "3.2", "ic": "fingerprint", "name": "Agentic payments", "blurb": "First live trial, with Visa.", "div": "uk", "rev": "uk", "products": [
            P("agentic", "AI-powered shopping", "HSBC UK and Visa completed what they called an industry-first agentic transaction on a live merchant site, with biometric authentication (14 July 2026).",
              s=["con"], lc="everyday", st="new", ay="Jul 2026", o="P", at="Visa", neo=[0, "Visa."],
              mc="Visa got there first, but Mastercard holds the UK credit book.",
              src=[["HSBC UK and Visa: AI shopping, Jul 2026", VISAAI]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards", "blurb": "RewardCash and Priceless.", "div": "hk", "rev": "hk", "products": [
            P("hkrewards", "RewardCash & Live Nation", "RewardCash and Red Hot Offers on Hong Kong cards, and Priceless access to Live Nation events for HSBC Hong Kong cardholders (June 2025).",
              s=["con", "premier"], lc="grow", o="P", at="Mastercard", neo=[1, "Priceless and Live Nation with Mastercard; RewardCash is HSBC's."],
              src=[["HSBC HK: credit cards", HKCARDS], ["Mastercard: Live Nation, Jun 2025", LIVENATION]]),
            P("ukrewards", "Pay with Rewards & Priceless", "HSBC UK Rewards cardholders redeem points through Mastercard Pay with Rewards and Priceless.", div="uk",
              s=["con"], lc="grow", o="P", at="Mastercard", neo=[3, "Mastercard Pay with Rewards."], src=[["HSBC UK: Rewards card", REWARDS]]),
        ]},
        {"id": "3.4", "ic": "refresh-cw", "name": "Sustainability", "blurb": "Recycled cards.", "div": "uk", "rev": "uk", "products": [
            P("sustain", "Card recycling & City Possible", "A card-recycling pilot with Mastercard in eight UK branches (June 2023), cards to be 85% recycled plastic by 2026, and the City Possible partnership for sustainable communities (September 2020).",
              s=["con"], lc="beyond", ay="Jun 2023", o="P", at="Mastercard", neo=[2, "Joint with Mastercard."],
              src=[["HSBC UK and Mastercard: recycling pilot, Jun 2023", RECYCLE], ["Mastercard: City Possible, Sep 2020", CITYPOSSIBLE]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: Hong Kong's leading bank with a quarter of deposits, HSBC UK with first direct, M&S Bank and the Innovation Bank, corporate and institutional banking for about half the Fortune Global 500, and wealth and Premier banking abroad.",
    "tiles": [
        {"id": "4.1", "ic": "building-2", "name": "Hong Kong", "blurb": "25% of deposits.", "div": "hk", "rev": "hk", "products": [
            P("hkbank", "HSBC Hong Kong & Hang Seng", "Retail, wealth and commercial banking at HSBC and Hang Seng: about 25% of deposits and ranked first; revenue of $8.1 billion and profit before tax of $5.1 billion in the first half of 2026, RoTE 35.5% in 2025.",
              s=["con", "sme"], lc="everyday", neo=[1, "Mastercard debit; credit split three ways."], src=[["2026 interim results", H1], ["2025 results", FY25]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "UK", "blurb": "HSBC UK, first direct, M&S Bank.", "div": "uk", "rev": "uk", "products": [
            P("ukretail", "UK Retail & Wealth", "HSBC UK, first direct and M&S Bank: $306 billion of loans and $348 billion of deposits at 30 June 2026, and Premier switching offers of up to £790 in 2026.",
              s=["con", "premier"], lc="everyday", neo=[1, "Mastercard credit, Visa debit ⚠."], src=[["2026 interim results", H1], ["HSBC UK newsroom", UKNEWS]]),
            P("flexipay", "Flexipay", "Point-of-sale instalments managed in the HSBC UK app, launched with OVO on 26 November 2024 and lent from HSBC's own balance sheet.",
              s=["con"], lc="borrow", ay="Nov 2024", o="P", at="OVO", neo=[0, "HSBC's own."],
              mc="Competes with card-network instalment products.",
              src=[["HSBC UK: Flexipay, Nov 2024", FLEXIPAY]]),
            P("ukcomm", "UK Commercial Banking & HSBC Innovation Bank", "Business banking in the UK, including HSBC Innovation Bank, formerly Silicon Valley Bank UK ⚠ acquired March 2023.", div="innov",
              s=["sme"], lc="everyday", o="A", neo=[1, "Mastercard commercial cards ⚠."], src=[["Annual Report 2025", ARA25]]),
        ]},
        {"id": "4.3", "ic": "factory", "name": "Corporate & institutional", "blurb": "Half the Fortune Global 500.", "div": "hsbc", "rev": "cib", "products": [
            P("cib", "Corporate & Institutional Banking", "Commercial banking outside the UK and Hong Kong plus global banking and markets: FX, payments, trade (about $900 billion a year) and securities services; profit before tax of $7.3 billion in the first half of 2026; about half of the Fortune Global 500 as clients.",
              s=["corp"], lc="move", neo=[1, "Mastercard virtual cards; payments are HSBC's."], src=[["2026 interim results", H1], ["Annual Report 2025", ARA25]]),
        ]},
        {"id": "4.4", "ic": "gem", "name": "Wealth & Premier", "blurb": "$2.1tn of wealth balances.", "div": "hsbc", "rev": "iwpb", "products": [
            P("iwpb", "International Wealth & Premier Banking", "Premier outside the UK and Hong Kong, the Private Bank, asset management and insurance; wealth balances of $2.1 trillion, Premier 3.0 live in seven markets and 29 Wealth Centres opened in 2025; priority markets mainland China, India, Singapore and the UAE.",
              s=["premier"], lc="grow", neo=[1, "Premier cards Mastercard in some markets."], src=[["Annual Report 2025", ARA25], ["2025 results", FY25]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: the UK and Hong Kong apps, HSBCnet and HSBCnio for companies, branches and Wealth Centres, and partners such as Sage and OVO.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Apps", "blurb": "8 million UK app users.", "div": "uk", "rev": "uk", "products": [
            P("ukapp", "HSBC UK app", "Relaunched in March 2025 with about 8 million active users, 30 releases planned for 2026.",
              s=["con", "intl"], lc="everyday", neo=[0, ""], src=[["Annual Report 2025", ARA25]]),
            P("hkapp", "HSBC HK app", "Active users up 20% a year; the planned channel for RedCoin with PayMe.", div="hk",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Asian Banker: stablecoin licence, Apr 2026", LICENCE]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "HSBCnet & HSBCnio", "blurb": "Clients' AI plugged in.", "div": "hsbc", "rev": "cib", "products": [
            P("hsbcnet", "HSBCnet & HSBC Access", "Corporate portals, and HSBC Access joining the Private Bank, Innovation Banking and CIB for eligible clients.",
              s=["corp"], lc="open", neo=[0, ""], src=[["HSBC: HSBCnio, Sep 2026", NIO], ["2026 interim results", H1]]),
            P("hsbcnio", "HSBCnio", "A transaction-banking platform launched at Sibos (29 September 2026) with AI tools; clients' own AI agents reach their HSBC data through the Model Context Protocol, with 'Ask HSBC' planned.",
              s=["corp"], lc="open", st="new", ay="Sep 2026", neo=[0, ""],
              mc="Clients' agents work straight against HSBC's rails.",
              src=[["HSBC: HSBCnio, Sep 2026", NIO]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & partners", "blurb": "Wealth Centres, Sage, OVO.", "div": "hsbc", "rev": "iwpb", "products": [
            P("branches", "Branches & Wealth Centres", "HSBC UK pledged £55 million for branches in 2026; 29 Wealth Centres opened in 2025.",
              s=["con", "premier"], lc="open", neo=[0, ""], src=[["HSBC UK newsroom", UKNEWS], ["Annual Report 2025", ARA25]]),
            P("partners", "Partners", "Sage for Making Tax Digital (January 2026), OVO for Flexipay and Live Nation for Hong Kong cardholders.",
              s=["sme", "con"], lc="open", o="P", at="Sage, OVO, Live Nation", neo=[0, ""], src=[["HSBC UK newsroom", UKNEWS], ["HSBC UK: Flexipay, Nov 2024", FLEXIPAY]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at HSBC", "blurb": "Premium credit and B2B cards.", "products": [
        P("mcathsbc", "Mastercard at HSBC", "Mastercard carries HSBC UK credit, including Premier World Elite, Hong Kong debit and premium credit, Hang Seng's MMPOWER and business debit, and HSBC's virtual and commercial cards in the UK, Hong Kong and the Gulf. Visa holds UK debit ⚠, Global Money, Gulf cards and the first live agentic payment; UnionPay shares Hong Kong credit. No group-wide network deal since the 2010 Premier renewal is public.",
          s=["con"], div="hsbc", rev="cc", mc="The relationship this map is drawn for.",
          src=[["Mastercard: World Legend, May 2026", LEGEND], ["EPI: Mastercard renewal, May 2010", MC2010], ["HSBC UK and Visa: AI shopping, Jul 2026", VISAAI]]),
    ]},
    {"id": "pillar-market", "name": "HSBC's markets", "blurb": "Stablecoins, agents, scams.", "products": [
        P("market", "The market", "Hong Kong's Stablecoins Ordinance (August 2025) and the first two licences (April 2026), Visa's earlier exclusive debit deals in Asia-Pacific (2008) and the Gulf (2013), and UK scam pressure; agentic pilots by Mastercard with DBS and UOB, not HSBC.",
          s=["con"], div="hsbc", rev="cc", src=[["Asian Banker: stablecoin licence, Apr 2026", LICENCE], ["Visa: APAC debit deal, Oct 2008", VISAAPAC], ["Mastercard APAC newsroom", MCAPAC]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
