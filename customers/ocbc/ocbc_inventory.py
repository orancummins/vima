"""OCBC's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the 1H26 results (7 August 2026), the FY2025
results (25 February 2026) and the 2025 Annual Report. Card networks were read from OCBC's card pages and
card-face images in Singapore, Malaysia and Indonesia on 17 October 2026. ``neo`` is the Mastercard lens:
[depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

NR = "https://www.ocbc.com/group/media/release/"
H126 = NR + "2026/ocbc-group-first-half-2026-net-profit-grew-13percent.page"
FY25 = NR + "2025/ocbc-group-full-year-2025.page"
AR25 = "https://www.ocbc.com/iwov-resources/sg/ocbc/gbc/pdf/investors/annual-reports/2025/2025-annual-report-en.pdf"
FY25CEO = "https://www.ocbc.com/iwov-resources/sg/ocbc/gbc/pdf/investors/quarterly-results/2025/ocbc%20fy25%20ceo%20presentation.pdf"
GROUP = "https://www.ocbc.com/group/about-us/group-business"
MGMT = "https://www.ocbc.com/group/about-us/our-leadership/management-team"
CEO = NR + "2025/ocbc-appoints-tan-teck-long-as-group-chief-executive-officer-succeeding-helen-wong.page"
LOW = NR + "2025/ocbc-appoints-melvyn-low-as-group-chief-strategy-and-transformation-officer.page"
GWB = NR + "2025/ocbc-refreshes-global-wholesale-leadership-for-next-growth-chapter.page"
MCAP = "https://companiesmarketcap.com/ocbc-bank/marketcap/"
CARDS = "https://www.ocbc.com/personal-banking/cards/credit-card"
DEBIT = "https://www.ocbc.com/personal-banking/cards/debit-card"
ODEBIT = "https://www.ocbc.com/personal-banking/cards/ocbc-debit-card.page"
N90 = "https://www.ocbc.com/personal-banking/cards/90-degrees-travel-credit-card.page"
INF = "https://www.ocbc.com/personal-banking/cards/infinity-unlimited-cashback-card"
REW = "https://www.ocbc.com/personal-banking/cards/rewards-card"
NXT = "https://www.ocbc.com/personal-banking/cards/bnpl-nxt-card.page"
FRANKCC = "https://www.ocbc.com/personal-banking/cards/ocbc-frank-credit-card.page"
VOYAGE = "https://www.ocbc.com/personal-banking/cards/voyage-credit-card.page"
C365 = NR + "2026/ocbc-card-6-percent-cashback-groceries-transport.page"
LIGHTUP = NR + "2026/ocbc-launches-stars-wars-and-winnie-the-pooh-themed-cards.page"
DISNEY = NR + "2024/ocbc-and-disney-embark-on-regional-five-year-collaboration.page"
N90L = NR + "2019/ocbc-bank-targets-annual-card-billings-of-1-billion-in-three-years.page"
JCB = "https://www.acnnewswire.com/press-release/english/54751/ocbc-bank-to-commence-jcb-cards-acceptance-in-singapore"
BIZDEBIT = "https://www.ocbc.com/assets/pdf/Media/2010/nov/OCBC%20Bank%20Launches%20First%20Customisable%20Platinum%20Debit%20Card%20for%20Businesses.pdf"
MYCARDS = "https://www.ocbc.com.my/personal-banking/cards/credit-cards"
ID1ST = "https://cdn1.ocbc.id/en/tentang-ocbc/informasi/siaran-pers/2026/02/09/kartu-kredit-ocbc-1st"
IDMICKEY = "https://www.ocbc.id/en/tentang-ocbc/informasi/siaran-pers/2026/09/21/ocbc-luncurkan-kartu-kredit-bertema-mickey-mouse"
HSBCID = NR + "2026/ocbc-acquires-hsbc-international-wealth-and-premier-banking-indonesia.page"
PTBC = NR + "2024/ocbc-deepens-indonesia-presences-with-pt-bank-commonwealth-acquisition.page"
GE24 = NR + "2024/ocbc-makes-1point4-billion-offer-for-great-eastern.page"
GE25 = NR + "2025/ocbc-statement-on-the-approval-of-great-eastern-holdings-resolutions-b-and-c.page"
VDIRECT24 = NR + "2024/ocbc-is-first-bank-in-asia-pacific-to-enable-near-instant-peer-to-peer-transfers-to-both-weixin-pay-wechat-pay-and-alipay.page"
WALLETS25 = NR + "2025/ocbc-adds-eight-major-digital-wallets-across-southeast-asia-to-ocbc-app"
QR24 = NR + "2024/ocbc-aims-to-quadruple-number-of-cross-border-qr-payments-in-2k24.page"
CHINAQR25 = NR + "2025/ocbc-app-first-can-scan-and-pay-all-merchants-qr-codes-in-china.page"
WEIXIN26 = NR + "2026/ocbc-customers-can-scan-weixin-pay-qr-in-china.page"
SENIORS26 = NR + "2026/ocbc-sees-more-seniors-turn-to-digital-payments.page"
MONEYLOCK = NR + "2024/ocbc-extends-money-lock-anti-scam-feature-to-time-deposits.page"
INAPP = NR + "2025/ocbc-rolls-out-in-app-calls-for-business-and-retail-banking-customers.page"
HELIOS = NR + "2026/ocbc-harnesses-agentic-ai-to-quicken-onboarding-customers.page"
WOW = NR + "2026/ocbc-unveils-avatar-banking.page"
SWIFT = NR + "2026/dbs-ocbc-uob-complete-first-live-blockchain-enabled-sgd-transactions.page"
ANT26 = NR + "2026/ocbc-tokenised-deposit-ant-international-treasury.page"
GOLDX = NR + "2026/ocbc-lion-global-investors-and-digifit-launches-southeast-asia-first-onchain-tokenised-gold-fund.page"
SINGPASS = NR + "2026/ocbc-enables-singpass-msia-business-acc-opening.page"
NINGBO = NR + "2026/ocbc-extends-bank-of-ningbo-alliance.page"
SME26 = NR + "2026/ocbc-aims-to-support-12000-smes-across-its-core-markets.page"
ONECOLLECT = "https://www.ocbc.com/business-banking/smes/business-tools/onecollect"
MCAGENT = "https://newsroom.mastercard.com/news/ap/en/newsroom/press-releases/en/2026/mastercard-delivers-its-first-live-agentic-transaction-in-singapore-with-dbs-and-uob/"
PAYNOW = "https://www.abs.org.sg/consumer-banking/pay-now"
CARDMKT = "https://www.crowdfundinsider.com/?p=256061"
PAYMIX = "https://2c2p.com/blog/singapore-payment-methods"
NETSWIKI = "https://en.wikipedia.org/wiki/NETS_(company)"
SRF = "https://www.reedsmith.com/articles/singapore-to-implement-shared-responsibility-framework-for-phishing-scams/"
PHISH = "https://fintechnews.sg/61497/fintech/ocbc-hit-with-s330-million-additional-cap-requirement-after-phishing-scam/"
UPQR = "https://eastandpartners.com/news/ocbc-expands-unionpay-qr-digital-payments-partnership/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · ratings · group", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: a record S$4.19 billion half-year profit, Aa1 and AA- ratings, the oldest Singapore bank with banks in Malaysia, Indonesia, Hong Kong and China, a new CEO, and The Next Frontier strategy.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "Record S$4.19bn half.", "div": "group", "rev": "others", "products": [
            P("balance", "Balance sheet & earnings", "1H26 net profit a record S$4.19 billion (+13%), with S$2.22 billion in 2Q26 (+22%); loans S$364 billion, deposits S$459 billion, ROE 13.7%, CET1 15.7%, at 30 June 2026. FY2025 net profit S$7.42 billion, income a record S$14.6 billion; credit card fees S$414 million in 2025. Market cap about US$106 billion ⚠.",
              s=["con"], neo=[0, ""], src=[["1H26 results, Aug 2026", H126], ["FY2025 results, Feb 2026", FY25], ["Annual Report 2025", AR25], ["companiesmarketcap.com", MCAP]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Tan Teck Long since January.", "div": "group", "rev": "others", "products": [
            P("leadership", "Board & management", "Chairman Andrew Lee; Group CEO Tan Teck Long from 1 January 2026, succeeding Helen Wong; CFO Goh Chin Yee; Sunny Quek runs Global Consumer Financial Services, Regina Lim card payments, and Melvyn Low strategy and transaction banking (he also sits on the NETS board).",
              s=["corp"], st="new", ay="Jan 2026", neo=[0, ""], src=[["OCBC: management team", MGMT], ["OCBC: Tan Teck Long named CEO, Jul 2025", CEO], ["OCBC: Melvyn Low appointed, Nov 2025", LOW]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Group & markets", "blurb": "Since 1932; 19 markets.", "div": "group", "rev": "others", "products": [
            P("heritage", "Heritage, ratings & reach", "Singapore's longest-established bank, formed in 1932; second-largest financial group in Southeast Asia by assets (S$625 billion, end-2024); rated Aa1 by Moody's and AA- by Fitch and S&P; close to 400 branches and offices in 19 countries and regions; 33,323 staff at end-2025.",
              s=["con"], o="I", neo=[0, ""], src=[["OCBC: group business", GROUP], ["Annual Report 2025", AR25]]),
            P("regional", "OCBC Malaysia, Indonesia, Hong Kong & China", "OCBC Malaysia and OCBC Al-Amin; OCBC Indonesia (PT Bank OCBC NISP, about 85% owned, 199 offices); OCBC Hong Kong (formerly Wing Hang, bought 2014) and OCBC China (16 branches); about 20% of Bank of Ningbo, with a 10-year agreement renewed in September 2026.",
              s=["con", "corp"], o="A", neo=[0, ""], src=[["OCBC: group business", GROUP], ["OCBC: Bank of Ningbo, Sep 2026", NINGBO]]),
        ]},
        {"id": "1.4", "ic": "brain", "name": "AI, digital & data", "blurb": "ADD at the core.", "div": "group", "rev": "others", "products": [
            P("tech", "AI, Digital, Data (ADD)", "In-house generative-AI tools, AI training for every employee, agentic AI that cut Bank of Singapore source-of-wealth reports from 10 days to 1 hour, and quantum research with NUS, NTU and SMU.",
              s=["corp"], neo=[0, ""], src=[["Annual Report 2025", AR25]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "The Next Frontier", "blurb": "Four shifts from 2026.", "div": "group", "rev": "others", "products": [
            P("strategy", "The Next Frontier", "Launched February 2026: Asia, Tech, Net-Zero and Franchise shifts, with stable to improving ROE and cost-to-income in the low to mid 40s; S$2.5 billion capital return due by FY26.",
              s=["corp"], st="new", ay="Feb 2026", neo=[0, ""], src=[["FY25 CEO presentation", FY25CEO], ["1H26 results, Aug 2026", H126]]),
            P("deals", "Deals", "PT Bank Commonwealth (Indonesia, May 2024, 1.2 million customers), Great Eastern raised to 93.72% (2024–25), and HSBC's wealth and premier business in Indonesia (agreed May 2026: 336,000 customers, S$6.6 billion AUM, completion 2Q27).",
              s=["wealth", "con"], o="A", neo=[0, ""], src=[["OCBC: PT Bank Commonwealth, May 2024", PTBC], ["OCBC: Great Eastern statement, Jul 2025", GE25], ["OCBC: HSBC Indonesia, May 2026", HSBCID]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Singapore credit cards split between Visa and Mastercard, Visa debit with NETS and Mastercard World Elite debit, Mastercard-led cards in Malaysia, PayNow and QR in 57 destinations, Visa Direct transfers to 10 wallets, card and QR acceptance, and tokenised deposits.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Singapore credit cards", "blurb": "Visa flagship, Mastercard range.", "div": "sg", "rev": "consumer", "products": [
            P("c365", "OCBC 365 Credit Card", "The flagship cashback card since 2014, on Visa Signature: from 1 November 2026, 6% on dining, groceries, transport and petrol above S$800 a month, capped at S$160. Three in five OCBC credit cardholders hold one; almost one in four of its overseas transactions are in Malaysia.", short="365 Credit (Visa)",
              s=["card", "con"], lc="everyday", st="new", ay="Nov 2026", o="B", at="Visa", neo=[0, "Visa."],
              mc="OCBC's most-held card is a Visa.",
              src=[["OCBC: 365 refresh, Oct 2026", C365], ["OCBC: credit cards", CARDS]]),
            P("n90", "OCBC 90°N Card", "Travel miles card launched as a Mastercard in August 2019 (target S$1 billion of billings in three years); now issued as both a Mastercard, with Mastercard Travel Rewards and lounges, and a Visa, with DragonPass; 1.3 miles per S$1 locally and 2.1 abroad.", short="90°N (Mastercard and Visa)",
              s=["card"], lc="everyday", ay="Aug 2019", o="P", at="Mastercard, Visa", neo=[1, "Mastercard and Visa versions."],
              src=[["OCBC: 90°N card", N90], ["OCBC: 90°N Mastercard launch, Aug 2019", N90L]]),
            P("infinity", "OCBC INFINITY Cashback Card", "Unlimited 1.6% cashback with no minimum spend, on Mastercard, with Priceless experiences and Mastercard merchant offers ⚠ launch date not found.", short="INFINITY (Mastercard)",
              s=["card", "con"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."],
              src=[["OCBC: INFINITY Cashback Card", INF]]),
            P("rewards", "OCBC Rewards Card", "10X OCBC$ (4 miles per S$1) on shopping and 15X at Watsons, Lazada, Shopee, Taobao and TikTok Shop to March 2027, on Mastercard with Priceless benefits.", short="Rewards (Mastercard)",
              s=["card"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."],
              src=[["OCBC: Rewards Card", REW], ["OCBC: credit cards", CARDS]]),
            P("nxt", "OCBC NXT Credit Card", "A buy-now-pay-later card that splits purchases over 3 or 6 months interest-free, with 1% cash rebate, on Mastercard; the older Cashflo cards also carry in-built instalments ⚠ network not shown.", short="NXT instalments (Mastercard)",
              s=["card"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard; Cashflo not shown."],
              mc="Card instalments already sit on Mastercard rails here.",
              src=[["OCBC: NXT Credit Card", NXT]]),
            P("voyage", "OCBC VOYAGE & Premier Visa Infinite", "Wealth-segment travel cards for Premier, Premier Private Client and Bank of Singapore clients, on Visa Infinite; FRANK Credit, the youth cashback card, is also on Visa ⚠.", short="VOYAGE & FRANK (Visa)",
              s=["wealth", "card"], lc="grow", o="P", at="Visa", neo=[0, "Visa."],
              src=[["OCBC: VOYAGE Card", VOYAGE], ["OCBC: FRANK Credit Card", FRANKCC], ["OCBC: credit cards", CARDS]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Debit", "blurb": "Visa and NETS; World Elite.", "div": "sg", "rev": "consumer", "products": [
            P("debit", "OCBC Debit Card", "The everyday debit card on Visa Platinum, also working on NETS at local terminals, with 1% cashback on Visa spend in selected categories above S$500 a month; Disney, Star Wars and light-up designs since 2024.", short="Debit (Visa + NETS)",
              s=["con", "senior"], lc="everyday", o="P", at="Visa, NETS", neo=[0, "Visa; NETS locally."],
              src=[["OCBC: Debit Card", ODEBIT], ["OCBC: light-up cards, May 2026", LIGHTUP]]),
            P("worldelite", "Premier World Elite Debit", "OCBC Premier and Premier Private Client World Elite Mastercard debit cards: 1% rebate on transport, fast food and overseas spend, and up to seven currencies with no conversion fee.", short="World Elite debit (Mastercard)",
              s=["wealth"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard World Elite."],
              src=[["OCBC: debit cards", DEBIT]]),
            P("bizdebit", "Business debit & virtual cards", "The OCBC Business Debit, launched in 2010 as Singapore's first customisable Platinum debit Mastercard ⚠ current status, and a virtual purchasing card that corporates can put into mobile wallets ⚠ network not found.",
              s=["sme"], lc="move", o="P", at="Mastercard", neo=[1, "Business debit on Mastercard ⚠; virtual card unknown."],
              mc="One in two Singapore SMEs bank with OCBC.",
              src=[["OCBC: Business Debit Mastercard, Nov 2010", BIZDEBIT], ["OCBC: Melvyn Low appointed, Nov 2025", LOW]]),
        ]},
        {"id": "2.3", "ic": "earth", "name": "Cards beyond Singapore", "blurb": "Malaysia on Mastercard.", "div": "my", "rev": "consumer", "products": [
            P("mycards", "OCBC Malaysia cards", "Six of seven credit cards on Mastercard (World, Premier Voyage, 365, Great Eastern Platinum, Titanium, Cashflo), with only 90°N on Visa; an OCBC Mastercard online and overseas spend campaign ran in October 2026.", short="Malaysia (mostly Mastercard)",
              s=["card"], lc="everyday", o="P", at="Mastercard", neo=[1, "Mastercard on six of seven cards."],
              mc="Mastercard's strongest OCBC franchise.",
              src=[["OCBC Malaysia: credit cards", MYCARDS]]),
            P("idcards", "OCBC Indonesia cards", "OCBC 1st Card for young adults launched with Mastercard (February 2026); Nyala Platinum cards, including a Mickey Mouse edition (September 2026), on Visa. Hong Kong and China lineups not found ⚠.", short="Indonesia (Visa and Mastercard)",
              s=["card"], lc="everyday", st="new", ay="Feb 2026", o="P", at="Mastercard, Visa", neo=[1, "Split by card."],
              src=[["OCBC Indonesia: 1st Card, Feb 2026", ID1ST], ["OCBC Indonesia: Mickey Mouse card, Sep 2026", IDMICKEY]]),
            P("hsbccards", "HSBC Indonesia card book", "Buying HSBC's wealth and premier business in Indonesia will grow OCBC Indonesia's credit-card balances by more than 150% on completion, expected in 2Q27 ⚠ network of the cards not checked.",
              s=["card", "wealth"], lc="everyday", st="flux", ay="May 2026", o="A", at="HSBC", neo=[None, "Network not checked."],
              mc="A card book changing hands in 2027.",
              src=[["OCBC: HSBC Indonesia, May 2026", HSBCID]]),
        ]},
        {"id": "2.4", "ic": "zap", "name": "PayNow & QR", "blurb": "57 destinations.", "div": "sg", "rev": "consumer", "products": [
            P("paynow", "PayNow in the OCBC app", "Free 24/7 transfers by mobile number, NRIC or virtual address since July 2017; seniors' PayNow payments to Shopee and TikTok Shop were 1.5 times higher in the year to June 2026.",
              s=["con", "senior"], lc="move", o="P", at="ABS, FAST", neo=[0, "Account to account."],
              src=[["ABS: PayNow", PAYNOW], ["OCBC: seniors and digital payments, Sep 2026", SENIORS26]]),
            P("scanpay", "Scan & Pay abroad", "QR payments from the account in 57 destinations over Alipay+ (first Singapore bank, 2023), UnionPay, PromptPay, DuitNow, QRIS and Weixin Pay (February 2026, via UnionPay on NETS infrastructure); cross-border use up 60% in 2025, with one in five transactions in China.",
              s=["con", "senior"], lc="move", st="new", ay="Feb 2026", o="P", at="UnionPay, Alipay+, NETS", neo=[0, "QR networks."],
              mc="QR is replacing the travel card in China.",
              src=[["OCBC: Weixin Pay scan, Feb 2026", WEIXIN26], ["OCBC: China QR, Dec 2025", CHINAQR25], ["OCBC: cross-border QR, Mar 2024", QR24], ["East & Partners: UnionPay QR, 2023", UPQR], ["Annual Report 2025", AR25]]),
        ]},
        {"id": "2.5", "ic": "send", "name": "Cross-border transfers", "blurb": "Visa Direct to 10 wallets.", "div": "sg", "rev": "consumer", "products": [
            P("paytowallet", "Pay-to-wallet", "Near-instant, fee-free transfers from the OCBC app to Weixin Pay and Alipay (November 2024) and eight Southeast Asian wallets including GCash, GoPay and Touch 'n Go (November 2025), powered by Visa Direct under a strategic partnership since 2024; more than S$60 million sent in the first year; 50 wallets targeted.", short="Pay-to-wallet (Visa Direct)",
              s=["remit", "con"], lc="move", st="new", ay="Nov 2024", o="P", at="Visa", neo=[0, "Visa Direct."],
              mc="Visa's deepest strategic tie at OCBC.",
              src=[["OCBC: eight wallets, Nov 2025", WALLETS25], ["OCBC: Weixin Pay and Alipay transfers, Nov 2024", VDIRECT24]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Acceptance", "blurb": "Cards, JCB and QR.", "div": "sg", "rev": "wholesale", "products": [
            P("acquiring", "Card acquiring", "\"One of the leading acquirers\" in Singapore, accepting Visa and Mastercard and, since October 2019, JCB, for supermarkets, department stores and dining ⚠ current volumes not published.",
              s=["sme"], lc="move", ay="Oct 2019", o="B", at="JCB", neo=[1, "Accepts every network."],
              src=[["JCB: OCBC acceptance, Oct 2019", JCB]]),
            P("onecollect", "OCBC OneCollect", "An app for SMEs to collect QR payments through PayNow, Alipay+, WeChat Pay, UnionPay, ShopeePay and DuitNow QR into an OCBC business account.",
              s=["sme"], lc="move", o="B", neo=[0, "QR only."],
              src=[["OCBC: OneCollect", ONECOLLECT]]),
        ]},
        {"id": "2.7", "ic": "coins", "name": "Digital money", "blurb": "Tokenised deposits live.", "div": "group", "rev": "wholesale", "products": [
            P("tokdeposits", "Tokenised deposits", "Live tokenised SGD interbank payments on Swift's ledger with DBS and UOB (September 2026), a cross-border USD transaction with Citi, 24/7 SGD and USD deposits for Ant International on its WhaleRTP platform (October 2026), and blockchain commercial paper and bonds.",
              s=["corp"], lc="move", st="new", ay="Sep 2026", o="P", at="Swift, Ant International", neo=[0, ""],
              mc="Treasury flows are moving to bank tokens, not cards.",
              src=[["OCBC: Swift's ledger, Sep 2026", SWIFT], ["OCBC: Ant International, Oct 2026", ANT26]]),
            P("goldx", "GOLDX token", "Southeast Asia's first tokenised physical gold fund on public blockchains (Ethereum and Solana), with Lion Global Investors and DigiFT, bought with stablecoins or fiat (April 2026).",
              s=["wealth"], lc="grow", st="new", ay="Apr 2026", o="P", at="DigiFT", neo=[0, ""],
              src=[["OCBC: GOLDX, Apr 2026", GOLDX]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: Money Lock and in-app calls after the 2021 phishing losses, Singpass and agentic-AI onboarding, AI avatars for wealth, and OCBC$, miles and Disney rewards.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & scams", "blurb": "Money Lock, in-app calls.", "div": "sg", "rev": "consumer", "products": [
            P("moneylock", "OCBC Money Lock", "Lets customers lock savings and time deposits against digital transfers, unlocked only at a branch or ATM with a card and PIN; S$3.3 billion locked within two months of the November 2023 launch.",
              s=["con", "senior"], lc="everyday", ay="Nov 2023", o="B", neo=[0, "OCBC's own."],
              src=[["OCBC: Money Lock, Jan 2024", MONEYLOCK]]),
            P("inappcalls", "In-app calls", "Calls to and from the bank inside the authenticated OCBC and OCBC Business apps (2025–26), to cut impersonation scams and reliance on SMS one-time passwords.",
              s=["con", "sme"], lc="everyday", st="new", ay="Nov 2025", o="B", neo=[0, "OCBC's own."],
              mc="Authentication and scam scoring are open ground.",
              src=[["OCBC: in-app calls, Nov 2025", INAPP]]),
            P("phishing", "Phishing losses & the shared-responsibility rules", "A December 2021 SMS phishing wave cost customers S$13.7 million, all repaid; MAS imposed about S$330 million of extra capital in May 2022 ⚠ current status. Since 16 December 2024 banks bear phishing losses first if they breach their duties.",
              s=["con"], lc="everyday", o="I", neo=[0, ""],
              src=[["Fintech News: MAS capital add-on, May 2022", PHISH], ["Reed Smith: Shared Responsibility Framework", SRF]]),
        ]},
        {"id": "3.2", "ic": "fingerprint", "name": "Identity & onboarding", "blurb": "Singpass, HELIOS.", "div": "group", "rev": "wholesale", "products": [
            P("singpass", "Singpass across the Causeway", "Singaporeans can open OCBC Malaysia business accounts with Singpass, cutting the wait from about three weeks to five working days; the first use of Singpass outside Singapore (June 2026).",
              s=["sme"], lc="open", st="new", ay="Jun 2026", o="P", at="Singpass", neo=[0, ""],
              src=[["OCBC: Singpass for Malaysia, Jun 2026", SINGPASS]]),
            P("helios", "HELIOS agentic KYC", "An agentic-AI platform that does most customer due diligence before a relationship manager calls, opening private-bank accounts in 15 business days; live at Bank of Singapore, extending to Premier Private Client by end-2026.",
              s=["wealth"], lc="open", st="new", ay="Jul 2026", o="B", neo=[0, "OCBC's own."],
              src=[["OCBC: HELIOS, Jul 2026", HELIOS]]),
        ]},
        {"id": "3.3", "ic": "bot", "name": "AI for customers", "blurb": "Avatar banking.", "div": "sg", "rev": "consumer", "products": [
            P("wow", "OCBC WoW", "Billed as the region's first AI-native bank app (July 2026): avatars Wendy and Wayne give portfolio analysis, market news and investment ideas by voice or text, 24/7.",
              s=["wealth"], lc="grow", st="new", ay="Jul 2026", o="B", neo=[0, ""],
              mc="An AI-native app with no agentic payments yet.",
              src=[["OCBC: avatar banking, Jul 2026", WOW]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Rewards", "blurb": "OCBC$, miles, Disney.", "div": "sg", "rev": "consumer", "products": [
            P("ocbcdollars", "OCBC$, 90°N Miles & 360 bonus", "OCBC$ and 90°N Miles that never expire, redeemable in the app for miles, hotel points and cash; OCBC 360 Account bonus interest for spending S$500 a month on the 365 card; Mastercard Travel Rewards on Mastercard cards.",
              s=["card"], lc="grow", o="B", neo=[1, "Mastercard Travel Rewards on Mastercard cards."],
              src=[["OCBC: Rewards Card", REW], ["OCBC: 90°N card", N90], ["OCBC: 365 refresh, Oct 2026", C365]]),
            P("disney", "Disney collaboration", "A five-year deal from October 2024 across Singapore, Malaysia and Indonesia: Disney card designs, Disney+ rewards and financial-literacy comics, aiming to quadruple new-to-bank customers in Southeast Asia by 2029.",
              s=["con"], lc="open", st="new", ay="Oct 2024", o="P", at="Disney", neo=[0, "On Visa cards in Singapore."],
              src=[["OCBC: Disney, Oct 2024", DISNEY], ["OCBC: light-up cards, May 2026", LIGHTUP]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: the 360 Account and home loans, S$350 billion of wealth assets with Bank of Singapore, Great Eastern insurance, SME and commercial banking, and corporate, transaction and markets business across ASEAN and Greater China.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Consumer banking", "blurb": "360 Account, home loans.", "div": "sg", "rev": "consumer", "products": [
            P("accounts", "Accounts, loans & seniors", "The OCBC 360 Account, home and car loans and personal credit, with OCBC SeniorCare reaching more than 150,000 seniors since 2022 and smart text resizing in the app.",
              s=["con", "senior"], lc="everyday", neo=[0, "Visa debit."],
              src=[["Annual Report 2025", AR25], ["OCBC: seniors and digital payments, Sep 2026", SENIORS26]]),
        ]},
        {"id": "4.2", "ic": "gem", "name": "Wealth & private banking", "blurb": "S$350bn of AUM.", "div": "bos", "rev": "consumer", "products": [
            P("wealth", "Premier, Premier Private Client & Bank of Singapore", "Group wealth income a record S$3.29 billion in 1H26 (41% of income); banking wealth AUM S$350 billion; Bank of Singapore in Singapore, Hong Kong and Dubai.",
              s=["wealth"], lc="grow", neo=[0, "Visa Infinite and World Elite cards."], src=[["1H26 results, Aug 2026", H126], ["OCBC: group business", GROUP]]),
        ]},
        {"id": "4.3", "ic": "hand-coins", "name": "Insurance", "blurb": "Great Eastern.", "div": "ge", "rev": "insurance", "products": [
            P("greateastern", "Great Eastern", "Singapore's and Malaysia's oldest life insurer, 93.72% owned economically; insurance profit before tax S$1.49 billion in 2025 and insurance income S$791 million in 1H26 (+49%).",
              s=["wealth", "con"], lc="grow", o="A", neo=[0, ""], src=[["Annual Report 2025", AR25], ["OCBC: Great Eastern offer, May 2024", GE24], ["1H26 results, Aug 2026", H126]]),
        ]},
        {"id": "4.4", "ic": "briefcase", "name": "SME & commercial", "blurb": "One in two SMEs.", "div": "sg", "rev": "wholesale", "products": [
            P("sme", "SME & commercial banking", "Serves one in two Singapore SMEs; aims to back 12,000 SMEs with S$25 billion of sustainable finance by 2028; Women Unlimited and serial-entrepreneur programmes across four markets.",
              s=["sme"], lc="borrow", neo=[None, "Card networks for SMEs not found."],
              src=[["OCBC: wholesale leadership, May 2025", GWB], ["OCBC: 12,000 SMEs, Apr 2026", SME26]]),
        ]},
        {"id": "4.5", "ic": "building-2", "name": "Corporate & markets", "blurb": "ASEAN–Greater China flows.", "div": "group", "rev": "wholesale", "products": [
            P("gtb", "Corporate & transaction banking", "Global Wholesale Banking made S$3.59 billion before tax in 2025; transaction banking doubled income in five years under Melvyn Low, with close to 600 Greater China mandates and blockchain conditional payments.",
              s=["corp"], lc="move", neo=[None, "Commercial-card network not found."],
              src=[["Annual Report 2025", AR25], ["OCBC: Melvyn Low appointed, Nov 2025", LOW]]),
            P("markets", "Global Markets", "Treasury, FX and hedging; profit before tax up 67% to S$948 million in 2025, with record customer-flow income.",
              s=["corp", "wealth"], lc="grow", neo=[0, ""], src=[["Annual Report 2025", AR25]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach OCBC: the OCBC app with PayNow, Scan & Pay and wealth, OCBC WoW, OCBC Business and Velocity, and close to 400 branches and offices across 19 markets.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "OCBC app", "blurb": "Pay, scan, invest.", "div": "sg", "rev": "consumer", "products": [
            P("app", "OCBC app", "Payments, Scan & Pay, pay-to-wallet, structured deposits and a wide range of investments; digital wealth revenue up more than 80% in 2025; seniors' digital payments up nearly 60% in a year.",
              s=["con", "senior", "remit"], lc="everyday", neo=[0, ""], src=[["Annual Report 2025", AR25], ["OCBC: seniors and digital payments, Sep 2026", SENIORS26]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Business channels", "blurb": "OCBC Business, Velocity.", "div": "sg", "rev": "wholesale", "products": [
            P("bizapp", "OCBC Business app & Velocity", "The OCBC Business app (in-app calls from June 2025), OCBC Velocity online banking and OneCollect for SMEs and corporates.",
              s=["sme", "corp"], lc="everyday", neo=[0, ""], src=[["OCBC: in-app calls, Nov 2025", INAPP], ["OCBC: OneCollect", ONECOLLECT]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & partners", "blurb": "Close to 400 sites.", "div": "group", "rev": "consumer", "products": [
            P("branches", "Branches, partners & ecosystems", "Close to 400 branches and offices in 19 markets, the Wisma Atria lifestyle branch, CARE Ambassadors for seniors, and partners from Disney and Ant International to Bank of Ningbo.",
              s=["con", "senior"], lc="open", neo=[0, ""], src=[["OCBC: group business", GROUP], ["OCBC: credit cards", CARDS]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at OCBC", "blurb": "Newer cards and Malaysia.", "products": [
        P("mcatocbc", "Mastercard at OCBC", "In Singapore Visa carries the flagship 365 card, the main debit card and the Visa Infinite wealth cards, and powers cross-border transfers through Visa Direct since 2024. Mastercard has the INFINITY, Rewards and NXT cards, half of 90°N and World Elite debit, six of seven cards in Malaysia and a new youth card in Indonesia. No network contracts were found, and OCBC was not in Mastercard's first Singapore Agent Pay transaction (March 2026).",
          s=["card"], div="group", rev="consumer", mc="The relationship this map is drawn for.",
          src=[["OCBC: credit cards", CARDS], ["OCBC Malaysia: credit cards", MYCARDS], ["OCBC: eight wallets, Nov 2025", WALLETS25], ["Mastercard: Singapore agentic transaction, Mar 2026", MCAGENT]]),
    ]},
    {"id": "pillar-market", "name": "Singapore & ASEAN", "blurb": "PayNow, NETS, QR, scams.", "products": [
        P("market", "The market", "Card payments of about S$158 billion in 2025, two-thirds on credit; PayNow used by 80% of consumers and businesses; NETS, owned by DBS, OCBC and UOB, with more than 130,000 acceptance points; QR links across ASEAN; and banks bearing phishing losses first under the shared-responsibility rules.",
          s=["con"], div="group", rev="others",
          src=[["Crowdfund Insider: card market, Dec 2025", CARDMKT], ["2C2P: Singapore payments, Jun 2026", PAYMIX], ["NETS (Wikipedia)", NETSWIKI], ["Reed Smith: Shared Responsibility Framework", SRF]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
