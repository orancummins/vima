"""Samsung's layers, areas and products, read through Samsung Wallet, as at 17 October 2026 (see page_data.py for the format).

Figures are Samsung's own unless a source says otherwise: the Q3 2026 guidance (8 October 2026), the Q2 2026
results (30 July 2026), the FY2025 results (29 January 2026), and the global, US, Korean, UK, German, Malaysian
and Hong Kong newsrooms for Samsung Wallet. Samsung does not report Wallet revenue or a network split.
``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on
Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q3 = "https://news.samsung.com/global/samsung-electronics-announces-earnings-guidance-for-third-quarter-2026"
Q2 = "https://news.samsung.com/global/samsung-electronics-announces-second-quarter-2026-results"
Q1 = "https://news.samsung.com/global/samsung-electronics-announces-first-quarter-2026-results"
FY25 = "https://news.samsung.com/global/samsung-electronics-announces-fourth-quarter-and-fy-2025-results"
BOARD = "https://www.samsung.com/global/ir/governance-csr/board-of-directors.html"
MCAP = "https://companiesmarketcap.com/samsung/marketcap/"
HERALD = "https://www.koreaherald.com/article/10621169"
KR10 = "https://news.samsung.com/kr/삼성월렛-출시-10주년-결제를-넘어-일상-속-디지털-지갑"
ESSAY = "https://news.samsung.com/kr/%ea%b8%b0%ea%b3%a0%eb%ac%b8-%ec%82%bc%ec%84%b1%ec%9b%94%eb%a0%9b-10%ec%a3%bc%eb%85%84-%ea%b0%a4%eb%9f%ad%ec%8b%9c%ec%9d%98-%eb%9d%bc%ec%9d%b4%ed%94%84-%ed%97%88%eb%b8%8c%eb%a1%9c-%ed%96%a5%ed%95%98"
CARD = "https://news.samsung.com/global/introducing-samsung-galaxy-card"
PAYPERS = "https://thepaypers.com/payments/news/samsung-launches-us-co-branded-credit-card-with-barclays"
STABLE = "https://news.samsung.com/us/samsung-wallet-bring-stablecoin-access-eligible-galaxy-users-us/"
VISAT2T = "https://corporate.visa.com/en/sites/visa-perspectives/innovation/visa-samsung-launch-tap-to-transfer-samsung-wallet.html"
T2T = "https://news.samsung.com/us/samsung-introduces-new-tap-to-transfer-feature-for-samsung-wallet/"
WEX = "https://news.samsung.com/uk/samsung-joins-mastercard-for-payments-with-wallet-express"
MDES15 = "https://news.samsung.com/global/mastercard-extends-partnership-with-samsung-to-deliver-samsung-pay-in-europe"
PYMNTS15 = "https://www.pymnts.com/company-profile/2015/mastercard-backs-samsung-pay/"
SA18 = "https://www.mastercard.com/news/eemea/en/newsroom/press-releases/en/2018/august/mastercard-continues-to-make-mobile-payments-in-sa-safer-simpler-and-more-convenient-with-samsung-pay"
SOFI = "https://www.mastercard.com/news/press/2020/may/introducing-samsung-money-by-sofi-do-more-with-your-money"
AMEX = "https://news.samsung.com/kr/%ec%82%bc%ec%84%b1%ec%a0%84%ec%9e%90-%ec%82%bc%ec%84%b1-%ec%9b%94%eb%a0%9b%ec%97%90%ec%84%9c-%ec%95%84%eb%a9%95%ec%8a%a4-%ec%b9%b4%eb%93%9c-%ed%95%b4%ec%99%b8-%ea%b2%b0%ec%a0%9c-%ec%a7%80%ec%9b%90"
TAPKR = "https://news.samsung.com/kr/%ea%b0%a4%eb%9f%ad%ec%8b%9c-%ec%8a%a4%eb%a7%88%ed%8a%b8%ed%8f%b0%eb%81%bc%eb%a6%ac-%eb%a7%9e%eb%8c%80%eb%a9%b4-%ea%b3%84%ec%a2%8c%ec%9d%b4%ec%b2%b4-%ec%82%bc%ec%84%b1%ec%9b%94%eb%a0%9b-%ed%83%ad"
CASH = "https://news.samsung.com/kr/삼성전자-한국은행-삼성월렛-모바일현금카드-mou체"
MONEY = "https://news.samsung.com/kr/삼성전자-삼성월렛-머니·포인트-서비스-가입자"
HANA = "https://news.samsung.com/kr/삼성전자-하나카드와-삼성월렛-서비스-제휴-업무협"
HK = "https://www.samsung.com/hk_en/news/product/samsung-wallet-elevates-the-digital-wallet-experience-with-unionpay-international-partnership/"
MAYBANK = "https://news.samsung.com/my/samsung-malaysia-and-maybank-sign-strategic-partnership-to-introduce-malaysias-first-samsung-wallet-qr-payment-experience"
DZ = "https://news.samsung.com/de/samsung-schliest-neue-partnerschaft-mobiles-bezahlen-mit-der-genossenschaftlichen-finanzgruppe"
CLEAR = "https://news.samsung.com/us/samsung-partners-clear-samsung-id-clear-samsung-wallet/"
TRIPS = "https://news.samsung.com/global/samsung-wallets-new-trips-feature-enables-seamless-journeys-for-global-travelers"
MOBEE = "https://news.samsung.com/global/samsung-and-mobeewave-partner-to-deploy-mpos-payments-worldwide"
LOOP = "https://news.samsung.com/global/samsung-pay-is-safe-secure-and-works-almost-anywhere-you-can-swipe-or-tap-a-card-today"
KED = "https://www.kedglobal.com/newsView/ked202302210005"
ANN = "https://asianews.network/samsung-pay-boosts-ties-with-naver-kakao-to-cement-payment-leadership"
MCDEV = "https://developer.mastercard.com/mastercard-processing-digital/documentation/use-cases/enable-card-samsung-pay-issuer-mobile-app/"
WALMART = "https://www.sammyfans.com/2026/08/24/walmart-will-finally-let-customers-pay-with-samsung-pay/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "scale · security · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What Samsung Wallet stands on: a group heading for about KRW 195 trillion of quarterly sales on AI memory, a wallet in 62 markets with 18.7 million Korean users, Knox security, and a plan to turn the wallet into a 'life hub'.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & results", "blurb": "KRW 195tn in Q3 2026.", "div": "grp", "rev": "grp", "products": [
            P("results", "Group results", "Q3 2026 guidance of about KRW 195 trillion of sales and KRW 107.4 trillion of operating profit (8 October 2026). Q2 2026 revenue was KRW 171.5 trillion with KRW 89.5 trillion of operating profit, KRW 89.2 trillion of it from chips; MX and Networks made KRW 33.2 trillion of revenue and a KRW 0.7 trillion loss. FY2025 revenue KRW 333.6 trillion. Market value about US$1.05 trillion ⚠ third-party.",
              s=["gal"], neo=[0, ""], src=[["Samsung: Q3 2026 guidance", Q3], ["Samsung: Q2 2026 results", Q2], ["Samsung: Q4 and FY2025 results", FY25], ["CompaniesMarketCap: Samsung, Oct 2026", MCAP]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Jun, Roh, Chai.", "div": "grp", "rev": "grp", "products": [
            P("leadership", "Co-CEOs & wallet head", "Co-CEOs Young-Hyun Jun (Vice Chairman, chips) and TaeMoon Roh (DX and mobile, co-CEO since 21 November 2025); board chaired by independent director Je-Yoon Shin. Samsung Wallet is run by Woncheol Chai, EVP and Head of the Digital Wallet Team in MX.",
              s=["gal"], neo=[0, ""], src=[["Samsung: Board of Directors", BOARD], ["Korea Herald: Roh named co-CEO, Nov 2025", HERALD], ["Samsung: Galaxy Card, Jul 2026", CARD]]),
        ]},
        {"id": "1.3", "ic": "chart-column", "name": "Wallet scale", "blurb": "62 markets, 18.7m in Korea.", "div": "wallet", "rev": "mx", "products": [
            P("walletscale", "Samsung Wallet reach", "62 markets (February 2026). In Korea 18.66 million users in 2025, up from 1.6 million in 2015, about one in three people; payments of KRW 88.6 trillion in 2024 against KRW 3.6 trillion in 2016, and about KRW 430 trillion in ten years. In the US, 82 million compatible Galaxy devices; about 15 million users against Apple Pay's 71.6 million ⚠ eMarketer estimate.",
              short="Wallet reach", s=["gal", "kr"], neo=[1, "Holds cards on every network, Mastercard among them."],
              src=[["Samsung Korea: Wallet at 10, Aug 2025", KR10], ["Samsung HK: UnionPay, Feb 2026", HK], ["Samsung US: stablecoin, Oct 2026", STABLE], ["The Paypers: Galaxy Card, Jul 2026", PAYPERS]]),
        ]},
        {"id": "1.4", "ic": "shield-check", "name": "Security platform", "blurb": "Knox, eSE, biometrics.", "div": "knox", "rev": "mx", "products": [
            P("knox", "Samsung Knox & eSE", "Galaxy's security platform under every Wallet item, with a hardware secure element (eSE) for payments, keys and IDs and end-to-end encryption to partners' servers.",
              s=["gal", "iss"], lc="everyday", o="B", neo=[0, ""], src=[["Samsung: Wallet at 10 essay, Aug 2025", ESSAY]]),
            P("samsungpass", "Samsung Pass", "Biometric sign-in and authentication, merged with Samsung Pay in 2022 so that payment and authentication run under one security scheme.",
              s=["gal"], lc="open", ay="2022", o="B", neo=[0, ""], src=[["Samsung: Wallet at 10 essay, Aug 2025", ESSAY]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "A 'life hub'.", "div": "wallet", "rev": "mx", "products": [
            P("strategy", "Wallet strategy", "Replace the physical wallet, then become a 'life hub': automate and personalise online payment with Galaxy AI, and add digital assets. The 2026 moves monetise the wallet: an own-brand credit card, Korean stored value and stablecoin transfers. No public targets ⚠.",
              s=["gal"], st="new", neo=[0, ""], src=[["Samsung: Wallet at 10 essay, Aug 2025", ESSAY], ["Samsung Korea: Wallet at 10, Aug 2025", KR10]]),
            P("deals", "Wallet partnerships 2023–26", "Mastercard Wallet Express (UK, December 2023), Visa Tap to Transfer (May 2025), Coinbase (October 2025), Hana Card (November 2025), UnionPay and Bank of China (Hong Kong) and Amex (February 2026), CLEAR (May 2026), Barclays and Visa (July 2026), Maybank (July 2026), DZ BANK (September 2026).",
              s=["iss"], o="P", neo=[1, "Wallet Express is Mastercard's; most 2025–26 deals are with others."],
              src=[["Samsung UK: Wallet Express, Dec 2023", WEX], ["Samsung: Galaxy Card, Jul 2026", CARD], ["Samsung Germany: DZ BANK, Sep 2026", DZ]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: tap to pay by NFC and MST on every network, Korean cards at home and abroad, online checkout, phone-to-phone transfers on Visa Direct and Korean bank rails, USDC for cross-border, and QR with UnionPay, Maybank and GLN.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Tap to pay", "blurb": "NFC, MST, transit.", "div": "wallet", "rev": "mx", "products": [
            P("nfc", "Samsung Wallet contactless", "Card tokens on Galaxy phones and watches, paid by NFC wherever contactless is taken, in 62 markets, with Mastercard, Visa, Amex and UnionPay cards; Walmart began taking it at selected US stores in August 2026 ⚠ secondary source.", short="Tap to pay (all networks)",
              s=["gal", "mer"], lc="move", ay="2015", o="B", neo=[1, "Every network; Mastercard cards through MDES."],
              mc="Most Mastercard volume in the wallet runs here.",
              src=[["Samsung HK: UnionPay, Feb 2026", HK], ["Samsung Germany: DZ BANK, Sep 2026", DZ], ["Sammy Fans: Walmart, Aug 2026", WALMART]]),
            P("mst", "MST (magnetic secure transmission)", "Samsung Pay's 2015 launch feature: it pays at mag-stripe terminals, which let it work at every card merchant in Korea without new hardware. LoopPay, its inventor, was part of Samsung by 2015. ⚠ Dropped from recent US models (not verified).",
              s=["kr", "mer"], lc="move", ay="Aug 2015", o="A", at="LoopPay", neo=[1, "Carries whichever card is stored."],
              src=[["Samsung Korea: Wallet at 10, Aug 2025", KR10], ["Samsung: LoopPay statement, Oct 2015", LOOP]]),
            P("transit", "Open-loop transit", "Ride metros and buses with a stored credit card in 85 cities in 12 countries, plus Korean transit cards.",
              s=["trav", "gal"], lc="move", neo=[1, "Any contactless card."],
              mc="Mastercard is a large open-loop transit network.",
              src=[["Samsung Korea: Wallet at 10, Aug 2025", KR10]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Korean cards", "blurb": "Home and abroad.", "div": "kr", "rev": "mx", "products": [
            P("korea", "Korean card payments", "Korean credit and debit cards paid by MST and NFC at home; Samsung Card was the only financial partner until Naver Pay joined in February 2023. Samsung Pay held about 80% of offline digital payments in H1 2022 ⚠ 2022 data.", short="Korea domestic",
              s=["kr"], lc="move", ay="Aug 2015", o="P", at="Korean card companies", neo=[0, "Korean domestic processing ⚠."],
              src=[["KED Global: Samsung–Naver, Feb 2023", KED], ["Korea Herald via ANN, Mar 2023", ANN]]),
            P("overseas", "Paying abroad", "Korean users pay abroad by NFC with Mastercard and Visa cards; Amex cards issued by Samsung Card were added on 4 February 2026.", short="Abroad (Mastercard, Visa, Amex)",
              s=["kr", "trav"], lc="move", o="P", at="Samsung Card, Amex", neo=[1, "Mastercard and Visa, now Amex too."],
              src=[["Samsung Korea: Amex abroad, Feb 2026", AMEX]]),
            P("cashcard", "Mobile cash card & ATMs", "A mobile cash card agreed with the Bank of Korea and KFTC on 26 September 2024, for ATM cash at 17 banks by NFC or QR and for payment from a bank account; 10 banks were linked before.",
              s=["kr"], lc="everyday", ay="Sep 2024", o="P", at="Bank of Korea, KFTC", neo=[0, "Korean bank rails."],
              src=[["Samsung Korea: mobile cash card MOU, Sep 2024", CASH]]),
        ]},
        {"id": "2.3", "ic": "receipt-text", "name": "Online checkout", "blurb": "In apps and on the web.", "div": "wallet", "rev": "mx", "products": [
            P("online", "Online & in-app payments", "Samsung Pay at checkout online and in apps, including in the Coinbase app (October 2025); Samsung plans to automate online payment with AI.",
              s=["gal", "mer"], lc="move", o="B", neo=[1, "Stored cards on every network."],
              mc="Click to Pay, passkeys and agentic tokens fit here.",
              src=[["Samsung Korea: Wallet at 10, Aug 2025", KR10], ["Samsung US: stablecoin, Oct 2026", STABLE]]),
        ]},
        {"id": "2.4", "ic": "send", "name": "Transfers", "blurb": "Tap to send money.", "div": "us", "rev": "mx", "products": [
            P("taptransfer", "Tap to Transfer (US)", "Send money to a bank account by tapping phones or a friend's contactless debit card, in about a minute; live 21 May 2025 on Visa's Tap to P2P and Visa Direct, with Green Dot. Samsung says Visa or Mastercard debit cards can be used.", short="Tap to Transfer (Visa Direct)",
              s=["gal"], lc="move", ay="May 2025", o="P", at="Visa, Green Dot", neo=[1, "Visa Direct rail; Mastercard debit cards accepted."],
              mc="Samsung was Visa's first Tap to P2P partner.",
              src=[["Visa: Tap to Transfer, May 2025", VISAT2T], ["Samsung US: Tap to Transfer, 2025", T2T]]),
            P("taptransferkr", "Tap transfer (Korea)", "Bank transfers between two Galaxy phones held back to back, launched with Woori Bank on 10 October 2024.",
              s=["kr"], lc="move", ay="Oct 2024", o="P", at="Woori Bank", neo=[0, "Bank transfer."],
              src=[["Samsung Korea: tap transfer, Oct 2024", TAPKR]]),
        ]},
        {"id": "2.5", "ic": "coins", "name": "Cross-border & stablecoin", "blurb": "USDC to 60+ countries.", "div": "us", "rev": "mx", "products": [
            P("stablecoin", "USDC stablecoin wallet", "From the last week of October 2026 in the US: USDC transfers to compatible wallets with no transfer fee, and payouts to bank accounts in more than 60 countries in local currency, with Coinbase, on 82 million Galaxy devices.", short="USDC (Coinbase)",
              s=["gal", "part"], lc="move", st="new", ay="Oct 2026", o="P", at="Coinbase", neo=[0, "USDC."],
              mc="Cross-border send in the wallet is going to a stablecoin, not a card network.",
              src=[["Samsung US: stablecoin, Oct 2026", STABLE]]),
            P("fx", "Currency exchange", "Order foreign currency in Samsung Wallet and collect it the same day (Korea). Provider not stated ⚠.",
              s=["kr", "trav"], lc="beyond", neo=[None, ""], src=[["Samsung Korea: Wallet at 10, Aug 2025", KR10]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "QR & local rails", "blurb": "UnionPay, Maybank, GLN.", "div": "asia", "rev": "mx", "products": [
            P("unionpay", "UnionPay NFC and QR (Hong Kong)", "NFC and QR payments in one card through UnionPay International and Bank of China (Hong Kong), first for BOC credit card holders, 27 February 2026.",
              s=["gal"], lc="move", st="new", ay="Feb 2026", o="P", at="UnionPay, BOCHK", neo=[0, "UnionPay."],
              src=[["Samsung HK: UnionPay, Feb 2026", HK]]),
            P("maybankqr", "Maybank QR (Malaysia)", "Malaysia's first Samsung Wallet QR payments, under a collaboration agreement signed with Maybank on 24 July 2026. QR scheme not stated ⚠.",
              s=["gal"], lc="move", st="new", ay="Jul 2026", o="P", at="Maybank", neo=[0, "Local QR ⚠."],
              src=[["Samsung Malaysia: Maybank, Jul 2026", MAYBANK]]),
            P("gln", "GLN QR abroad", "Korean users scan merchants' QR codes abroad and pay from a GLN account in Samsung Wallet, in GLN partner countries.",
              s=["kr", "trav"], lc="move", o="P", at="GLN", neo=[0, "GLN QR."],
              src=[["Samsung Korea: Wallet at 10, Aug 2025", KR10]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around each payment: network tokens and device security, digital IDs from Korean resident cards to US passports, car and home keys and Trips, Wallet Points and Pay Planner, and the AI that is meant to automate checkout.",
    "tiles": [
        {"id": "3.1", "ic": "key-round", "name": "Tokens & risk", "blurb": "MDES since 2015.", "div": "wallet", "rev": "mx", "products": [
            P("tokens", "Network tokens", "Card numbers replaced by tokens from launch in 2015. Mastercard's MDES has tokenised Mastercard cards for Samsung Pay since 2015 (Europe from July 2015; South Africa 2018); other networks use their own token services ⚠.", short="Tokens (MDES for Mastercard)",
              s=["iss", "gal"], lc="everyday", ay="2015", o="P", at="Mastercard, other networks", neo=[1, "MDES for Mastercard cards."],
              mc="Mastercard's deepest technical role in Samsung Wallet.",
              src=[["Samsung: Mastercard extends partnership, Jul 2015", MDES15], ["PYMNTS: Mastercard backs Samsung Pay, 2015", PYMNTS15], ["Mastercard: Samsung Pay in South Africa, Aug 2018", SA18]]),
            P("fraud", "Device fraud controls", "Biometrics, Knox and eSE guard payments; no named Samsung fraud-scoring product was found ⚠.",
              s=["gal"], lc="everyday", o="B", neo=[0, ""], src=[["Samsung: Wallet at 10 essay, Aug 2025", ESSAY]]),
        ]},
        {"id": "3.2", "ic": "fingerprint", "name": "Digital ID", "blurb": "Korean IDs, CLEAR.", "div": "wallet", "rev": "mx", "products": [
            P("koreaid", "Korean mobile IDs", "Mobile resident registration card (first private app, April 2025 ⚠ date), driving licence, veterans' card, student IDs, e-certificates and the Milipass military ID (January 2026).",
              s=["kr", "part"], lc="open", o="P", at="Korean government", neo=[0, ""],
              src=[["Samsung Korea: Wallet at 10, Aug 2025", KR10], ["Samsung Korea: Amex abroad, Feb 2026", AMEX]]),
            P("clear", "Samsung ID with CLEAR (US)", "A free digital ID backed by a US passport and verified by CLEAR, accepted at more than 250 TSA checkpoints, launched 26 May 2026; mobile driving licences for Arizona and Iowa.",
              s=["trav", "part"], lc="open", st="new", ay="May 2026", o="P", at="CLEAR", neo=[0, ""],
              src=[["Samsung US: CLEAR, May 2026", CLEAR], ["Samsung: Galaxy Card, Jul 2026", CARD]]),
        ]},
        {"id": "3.3", "ic": "plane", "name": "Keys, tickets & trips", "blurb": "Cars, homes, journeys.", "div": "wallet", "rev": "mx", "products": [
            P("carkeys", "Digital car keys", "UWB and NFC keys for Mercedes-Benz (June 2025), Porsche, Audi, Toyota, Volvo and Polestar, and GM vehicles.",
              s=["gal", "part"], lc="beyond", o="P", at="Carmakers", neo=[0, ""], src=[["Samsung Korea: Wallet at 10, Aug 2025", KR10], ["Samsung: Trips, Apr 2026", TRIPS]]),
            P("homekey", "Digital home keys", "Keys for selected SmartThings-compatible smart door locks.",
              s=["gal"], lc="beyond", o="P", neo=[0, ""], src=[["Samsung: Galaxy Card, Jul 2026", CARD]]),
            P("trips", "Trips", "Travel tickets, event tickets, boarding passes and bookings in one timeline, launched 27 April 2026.",
              s=["trav"], lc="beyond", st="new", ay="Apr 2026", o="B", neo=[0, ""],
              src=[["Samsung: Trips, Apr 2026", TRIPS]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Rewards & insights", "blurb": "Points, Pay Planner.", "div": "kr", "rev": "mx", "products": [
            P("points", "Samsung Wallet Points & Benefits", "Points on every Samsung Wallet Money payment, spendable like cash, with promotions up to 10% (December 2025) and points on gifts bought in the Benefits tab.",
              s=["kr"], lc="grow", st="new", ay="Oct 2025", o="B", neo=[0, ""],
              mc="Card-linked offers could feed the Benefits tab.",
              src=[["Samsung Korea: Money and Points at 1m, Dec 2025", MONEY]]),
            P("payplanner", "Pay Planner", "Spending management inside Samsung Wallet in Korea.",
              s=["kr"], lc="everyday", o="B", neo=[0, ""], src=[["Samsung: Wallet at 10 essay, Aug 2025", ESSAY]]),
        ]},
        {"id": "3.5", "ic": "bot", "name": "AI & agentic checkout", "blurb": "Planned with Galaxy AI.", "div": "wallet", "rev": "mx", "products": [
            P("agentic", "AI-automated payments", "Samsung plans to make online payment 'automated and intelligent' with Galaxy AI; MX promised 'Agentic AI experiences' with the Galaxy S26. No agentic payment product or network partner has been announced ⚠.",
              s=["gal"], lc="move", st="new", o="B", neo=[None, "No network named."],
              mc="Agent Pay could carry Galaxy AI's purchases on Mastercard tokens already in the wallet.",
              src=[["Samsung Korea: Wallet at 10, Aug 2025", KR10], ["Samsung: Q4 and FY2025 results", FY25]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What Samsung sells around the wallet: the US Galaxy Card on Visa, Korean stored value and a Hana Card co-brand, issuer enablement through Wallet Express and Germany's cooperative banks, earlier money products, and the Galaxy phones that carry it all.",
    "tiles": [
        {"id": "4.1", "ic": "credit-card", "name": "Galaxy Card", "blurb": "Barclays, Visa.", "div": "us", "rev": "mx", "products": [
            P("galaxycard", "Samsung Galaxy Card (US)", "Samsung's first credit card, issued by Barclays US Consumer Bank on Visa, applications from 22 July 2026: 5% back on Samsung, 3% on Samsung Wallet payments, 2% on streaming, 1% elsewhere, $200 after $2,000 in 90 days; virtual and metal; run inside Samsung Wallet.", short="Galaxy Card (Visa)",
              s=["gal"], lc="borrow", st="new", ay="Jul 2026", o="P", at="Barclays, Visa", neo=[0, "Visa."],
              mc="Samsung's one ownable card programme went to Visa.",
              src=[["Samsung: Galaxy Card, Jul 2026", CARD], ["The Paypers: Galaxy Card, Jul 2026", PAYPERS]]),
        ]},
        {"id": "4.2", "ic": "wallet", "name": "Korean money", "blurb": "Wallet Money, Hana.", "div": "kr", "rev": "mx", "products": [
            P("walletmoney", "Samsung Wallet Money", "Stored value linked to a bank account, usable at every offline card merchant, launched in October 2025; with Points it passed 1 million subscribers by 15 December 2025; a Woori Bank account variant.",
              s=["kr"], lc="everyday", st="new", ay="Oct 2025", o="P", at="Woori Bank", neo=[0, "Bank-linked stored value."],
              src=[["Samsung Korea: Money and Points at 1m, Dec 2025", MONEY]]),
            P("hanacard", "Hana Card travel co-brand", "A Samsung Wallet travel card and university IDs planned under an MOU with Hana Card signed on 18 November 2025. Network not stated ⚠.",
              s=["kr", "trav"], lc="borrow", st="new", ay="Nov 2025", o="P", at="Hana Card", neo=[None, "Network not stated ⚠."],
              mc="A Korean co-brand with an open network choice.",
              src=[["Samsung Korea: Hana Card MOU, Nov 2025", HANA]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Issuer enablement", "blurb": "Wallet Express, DZ BANK.", "div": "eu", "rev": "mx", "products": [
            P("walletexpress", "Mastercard Wallet Express", "A Mastercard programme Samsung joined on 6 December 2023 in the UK, giving banks and issuers a quick, low-cost way to offer Samsung Wallet, including Galaxy Watch payments.", short="Wallet Express (Mastercard)",
              s=["iss"], lc="open", ay="Dec 2023", o="P", at="Mastercard", neo=[3, "Mastercard's own programme."],
              mc="Mastercard's own route for issuers into Samsung Wallet.",
              src=[["Samsung UK: Wallet Express, Dec 2023", WEX]]),
            P("dzbank", "DZ BANK & Germany's cooperative banks", "From 21 September 2026 customers of more than 600 Volksbanken Raiffeisenbanken, Sparda and PSD banks can add their Mastercard and Visa credit and debit cards to Samsung Wallet.",
              s=["iss", "gal"], lc="open", st="new", ay="Sep 2026", o="P", at="DZ BANK", neo=[1, "Mastercard and Visa cards."],
              src=[["Samsung Germany: DZ BANK, Sep 2026", DZ]]),
        ]},
        {"id": "4.4", "ic": "hand-coins", "name": "Earlier money products", "blurb": "SoFi, Samsung POS.", "div": "us", "rev": "mx", "products": [
            P("sofi", "Samsung Money by SoFi", "A cash management account with a Mastercard debit card, inside Samsung Pay, for Galaxy users; announced 27 May 2020 and opened 23 July 2020. Current status not confirmed ⚠.", short="Samsung Money (Mastercard)",
              s=["gal"], lc="everyday", st="unconf", ay="2020", o="P", at="SoFi, Mastercard", neo=[2, "Mastercard debit."],
              mc="The only Samsung-branded Mastercard programme found.",
              src=[["Mastercard: Samsung Money by SoFi, May 2020", SOFI]]),
            P("samsungpos", "Samsung POS", "Phones as contactless terminals with Mobeewave, taking cards and Samsung Pay, Apple Pay and Google Pay, worldwide from 15 October 2019 after a Canadian pilot. Current status not confirmed ⚠.",
              s=["mer"], lc="move", st="unconf", ay="Oct 2019", o="P", at="Mobeewave", neo=[1, "Accepts every network."],
              src=[["Samsung: Mobeewave, Oct 2019", MOBEE]]),
        ]},
        {"id": "4.5", "ic": "smartphone", "name": "Galaxy devices", "blurb": "KRW 33.2tn in Q2.", "div": "grp", "rev": "mx", "products": [
            P("devices", "Galaxy phones, watches & tablets", "The MX business: KRW 33.2 trillion of revenue with Networks in Q2 2026 on the Galaxy S26 and A series, and a Galaxy Z8 launch in July 2026. Wallet users rebuy Galaxy phones at more than twice the rate of non-users.",
              s=["gal"], lc="beyond", neo=[0, ""],
              src=[["Samsung: Q2 2026 results", Q2], ["Samsung: Wallet at 10 essay, Aug 2025", ESSAY]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How people reach Samsung Wallet: the app on Galaxy phones, Galaxy Watch, Samsung.com and stores, and banks' own apps that push cards into the wallet.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Wallet app", "blurb": "16.6m launches a day in Korea.", "div": "wallet", "rev": "mx", "products": [
            P("app", "Samsung Wallet app", "On Galaxy phones with Android 9 or later and a Samsung account; 16.6 million launches a day in Korea (2025).",
              s=["gal", "kr"], lc="open", o="B", neo=[1, "Holds every network's cards."],
              src=[["Samsung Korea: Wallet at 10, Aug 2025", KR10], ["Samsung: Galaxy Card, Jul 2026", CARD]]),
        ]},
        {"id": "5.2", "ic": "gauge", "name": "Galaxy Watch", "blurb": "Pay from the wrist.", "div": "wallet", "rev": "mx", "products": [
            P("watch", "Galaxy Watch payments", "Contactless payment from Galaxy Watch, offered by Wallet Express issuers in the UK and by Germany's cooperative banks.",
              s=["gal"], lc="move", o="B", neo=[1, "Every network."],
              src=[["Samsung UK: Wallet Express, Dec 2023", WEX], ["Samsung Germany: DZ BANK, Sep 2026", DZ]]),
        ]},
        {"id": "5.3", "ic": "plug", "name": "Partners & stores", "blurb": "Samsung.com, bank apps.", "div": "us", "rev": "mx", "products": [
            P("samsungcom", "Samsung.com & Samsung stores", "Where US customers apply for the Galaxy Card, online or in Samsung stores, and earn 5% on Samsung purchases.",
              s=["gal"], lc="open", st="new", neo=[0, "Visa card."], src=[["Samsung: Galaxy Card, Jul 2026", CARD]]),
            P("bankapps", "Banks' apps (push provisioning)", "Issuers add cards to Samsung Wallet from their own apps; Mastercard documents the flow for Samsung Pay through Mastercard Processing.",
              s=["iss"], lc="open", o="P", neo=[1, "Mastercard documents its flow; others have their own."],
              src=[["Mastercard Developers: Samsung Pay provisioning", MCDEV]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Samsung", "blurb": "Tokens yes, Samsung's money no.", "products": [
        P("mcatsamsung", "Mastercard at Samsung", "Mastercard has tokenised Mastercard cards for Samsung Pay since 2015 through MDES, brought issuers in through Wallet Express (UK, 2023) and carried Samsung Money by SoFi (2020). Samsung's own money products of 2025–26 went elsewhere: the Galaxy Card and Tap to Transfer to Visa, cross-border to USDC with Coinbase, Hong Kong QR to UnionPay. No Agent Pay, Click to Pay or Move work with Samsung was found.",
          s=["iss"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Samsung: Mastercard extends partnership, Jul 2015", MDES15], ["Samsung UK: Wallet Express, Dec 2023", WEX], ["Samsung: Galaxy Card, Jul 2026", CARD]]),
    ]},
    {"id": "pillar-market", "name": "Wallet market", "blurb": "Apple, Google, Naver, Kakao.", "products": [
        P("market", "The market", "In the US Apple Pay has about 71.6 million users, Google Pay 42 million and Samsung Wallet 15 million (eMarketer 2026 ⚠). In Korea Samsung leads offline mobile payment; Naver Pay (31.5 million members in 2023) leads online, Kakao Pay competes, and Apple Pay arrived with Hyundai Card in March 2023. Korea's easy-payment market reached about KRW 350 trillion in 2024.",
          s=["gal"], div="grp", rev="grp",
          src=[["The Paypers: Galaxy Card, Jul 2026", PAYPERS], ["Korea Herald via ANN, Mar 2023", ANN], ["Samsung Korea: Wallet at 10, Aug 2025", KR10]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
