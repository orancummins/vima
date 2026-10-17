"""ICBC's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the 2026 Interim Report (24 September 2026) and the
2025 Annual Report (April 2026). ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own
product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

IR26 = "https://v.icbc.com.cn/userfiles/resources/icbcltd/download/2026/InterimReport20260924.pdf"
AR25 = "https://v.icbc.com.cn/userfiles/resources/icbcltd/download/2026/2025AnnualReport.pdf"
BOARD = "https://www.icbc-ltd.com/en/column/1438058343720960006.html"
SENIOR = "https://www.icbc-ltd.com/en/column/1438058326864052336.html"
RATINGS = "https://www.icbc-ltd.com/en/column/1438058343720960011.html"
CDH1 = "https://english.sse.com.cn/news/newsrelease/voice/c/c_20260902_10831069.shtml"
CDFY = "https://english.sse.com.cn/news/newsrelease/voice/c/c_20260330_10813469.shtml"
FILING = "https://filingreader.com/news-wire/hongkong/2026-08-29/icbc-posts-45-profit-rise-in-first-half"
MCAP = "https://companiesmarketcap.com/icbc/marketcap/"
ETC = "https://etc-corporate.org/news/enabling-seamless-journeys-the-european-travel-commission-and-mastercard-launch-new-european-travel-co-branded-card-for-chinese-visitors/"
MCETC = "https://www.mastercard.com/news/europe/en/newsroom/press-releases/en/2026/enabling-seamless-journeys-the-european-travel-commission-and-mastercard-launch-new-european-travel-co-branded-card-for-chinese-visitors/"
BBT = "https://www.bbtnews.com.cn/2026/0203/584065.shtml"
SINA24 = "https://finance.sina.cn/2024-05-12/detail-inauyvkv5963643.d.html"
NUCC23 = "https://www.paymentsdive.com/news/mastercard-joint-venture-china-credit-card-processing/700312/"
PEONY = "https://v.icbc.com.cn/userfiles/resources/icbc/zygg/download/2026/mdxjjk_zc_202604.pdf"
SANDS = "https://en.prnasia.com/releases/apac/ICBC_Sands_Lifestyle_Mastercard_Launch-170523.shtml"
LANGPING = "https://www.icbc.com.cn/icbc/en/newsupdates/icbc%20news/LangPingEndorsesICBCMasterCardCreditCard.htm"
SHANGRI = "https://nz.icbc.com.cn/icbc/en/newsupdates/icbc%20news/ICBCLaunchesCo-brandedCreditCardwithShangriLaHotel.htm"
ASIACARDS = "https://www.icbcasia.com/hk/en/personal/credit-cards/type-of-cards/default.html"
ASIAVIRT = "https://www.icbcasia.com/hk/en/personal/credit-cards/virtual-digital-credit-card/default.html"
ASIAMOB = "https://www.icbcasia.com/hk/en/personal/credit-cards/mobile-payment/default.html"
ASIACORP = "https://www.icbcasia.com/hk/en/commercial/sme-financing/corporate-card/default.html"
ASIADEBIT = "https://www.icbcasia.com/hk/en/personal/banking/others/debit-card/default.html"
MACAU = "https://www.icbc.com.mo/icbc/%E6%B5%B7%E5%A4%96%E5%88%86%E8%A1%8C/%E5%B7%A5%E9%93%B6%E6%BE%B3%E9%97%A8/en/icbc_card/icbc_card/icbc_co_brandedcreditcard/icbc_marts_mastercard"
ARG = "https://www.icbc.com.ar/personas"
USA16 = "https://www.electronicpaymentsinternational.com/news/icbc-rolls-out-its-first-us-credit-cards-280416-4877251/"
BJVISA = "https://english.beijing.gov.cn/specials/paymentservices/news/202503/t20250304_4024575.html"
UPI24 = "https://www.aap.com.au/aapreleases/cision20241105ae48592"
CARDSEN = "https://www.icbc.com.cn/en/column/1438058327061184654.html"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · state · AI", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: the world's largest bank with RMB57 trillion of assets, two-thirds owned by the Chinese state, a G-SIB in Bucket 3, AI-ICBC and 398 institutions in 49 countries.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "RMB57trn, ROE 8.6%.", "div": "icbc", "rev": "other", "products": [
            P("balance", "Balance sheet & earnings", "Total assets of RMB57.07 trillion, loans of RMB31.99 trillion and deposits of RMB39.17 trillion at 30 June 2026; net profit of RMB176.5 billion in the half (+4.5%) and RMB370.8 billion in 2025; NIM 1.29%, ROE 8.63%, NPL ratio 1.29%, CET1 13.21%.",
              s=["con", "corp"], neo=[0, ""], src=[["2026 Interim Report", IR26], ["2025 Annual Report", AR25], ["FilingReader: H1 2026, Aug 2026", FILING]]),
        ]},
        {"id": "1.2", "ic": "building-2", "name": "State ownership & ratings", "blurb": "Huijin and MOF own two-thirds.", "div": "icbc", "rev": "other", "products": [
            P("owners", "Ownership, listing & ratings", "Founded 1984 and listed in Shanghai and Hong Kong in October 2006. Central Huijin holds 34.79% and the Ministry of Finance about 31%. Market value is about US$345 billion ⚠ third-party figure. Rated A by S&P and A1 by Moody's. First in The Banker's Top 1000 World Banks for 13 years, and moved up to G-SIB Bucket 3.",
              s=["corp"], o="I", neo=[0, ""], src=[["2026 Interim Report", IR26], ["ICBC: credit ratings", RATINGS], ["CompaniesMarketCap: ICBC, Oct 2026", MCAP], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "1.3", "ic": "scale", "name": "Leadership", "blurb": "Liao Lin and Liu Jun.", "div": "icbc", "rev": "other", "products": [
            P("leadership", "Board & senior management", "Chairman Liao Lin. Liu Jun is Vice Chairman, President and Chief Compliance Officer. Wang Jingwu is Chief Risk Officer and Yao Mingde is CFO. Zhang Weiwu, Zhang Shouchuan and Zhao Guide are senior EVPs. The board has 13 directors, 6 of them independent. 402,548 employees.",
              s=["corp"], neo=[0, ""], src=[["ICBC: board of directors", BOARD], ["ICBC: senior management", SENIOR], ["2026 Interim Report", IR26]]),
        ]},
        {"id": "1.4", "ic": "brain", "name": "Technology & AI", "blurb": "LLMs in 600+ scenarios.", "div": "icbc", "rev": "other", "products": [
            P("tech", "FinTech & core systems", "RMB28.6 billion invested in FinTech in 2025. The ECOS 2.0 technology ecosystem and core-system rebuild, on domestically developed computing power. First bank certified at the top level of China's digital-transformation maturity model.",
              s=["corp"], neo=[0, ""], src=[["2025 Annual Report", AR25], ["2026 Interim Report", IR26]]),
            P("ai", "AI-ICBC & the AI+ Action Plan", "Large models in more than 600 scenarios. Two 'super agents', one for customers and one for staff, with four kinds of front-line agents in pilot (H1 2026). AI digital employees did the work of about 55,000 people in 2025. ICBC Zhiyong is an in-house financial model with more than 100 billion parameters.",
              s=["con", "corp"], lc="everyday", st="new", neo=[0, ""],
              mc="An agent-first bank with no agentic card payments yet.",
              src=[["2026 Interim Report", IR26], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & reach", "blurb": "398 institutions, 49 countries.", "div": "icbc", "rev": "other", "products": [
            P("strategy", "Five transformations & the new five-year plan", "The 14th Five-Year Plan closed in 2025. ICBC is pursuing 'five transformations' towards a 'modern bank'. In August 2026 Liu Jun said growth would shift from credit towards integration, internationalisation and digitalisation.",
              s=["corp"], st="new", neo=[0, ""], src=[["China Daily: H1 2026 results, Aug 2026", CDH1], ["2025 Annual Report", AR25]]),
            P("intl", "International network", "398 overseas institutions in 49 countries and regions, with US$511 billion of assets (6.1% of the group) and 9.8% of pre-tax profit in H1 2026. ICBC holds 19.74% of Standard Bank Group, in 21 African countries.",
              s=["corp", "abroad"], neo=[0, ""], src=[["2026 Interim Report", IR26], ["China Daily: H1 2026 results, Aug 2026", CDH1], ["2025 Annual Report", AR25]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: 1.3 billion cards, mostly on UnionPay at home; RMB-capable Mastercard cards since 2024; international Peony cards on Visa and Mastercard; acceptance for visitors; cross-border RMB and IGPS; and e-CNY and mBridge.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Domestic cards", "blurb": "1.34 billion cards.", "div": "cards", "rev": "personal", "products": [
            P("debit", "ICBC debit cards", "1,196 million debit cards at 30 June 2026, with RMB9.26 trillion of spending in the half and RMB18.51 trillion in 2025. Domestic use runs through UnionPay ⚠ (inferred from card rules; no split disclosed).",
              s=["con", "sme"], lc="everyday", o="B", at="UnionPay", neo=[0, "UnionPay at home ⚠."], src=[["2026 Interim Report", IR26], ["Peony International Debit Card rules, Apr 2026", PEONY]]),
            P("credit", "Peony credit cards & co-brands", "143 million credit cards and RMB597 billion of balances at 30 June 2026, down from RMB698 billion at end-2025. RMB0.79 trillion of spending in the half. Peony, Easy Loan instalments, and Air China PhoenixMiles, PICC and Tuniu co-brands. Mostly UnionPay ⚠; network split not disclosed.", short="Credit cards (mostly UnionPay ⚠)",
              s=["con"], lc="borrow", st="flux", o="B", at="UnionPay, Mastercard, Visa", neo=[1, "Mostly UnionPay; some Mastercard and Visa ⚠."],
              mc="A shrinking credit book where Mastercard holds a small share.",
              src=[["2026 Interim Report", IR26], ["2025 Annual Report", AR25], ["ICBC: bank cards", CARDSEN]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Mastercard RMB cards", "blurb": "Since NUCC opened, May 2024.", "div": "cards", "rev": "personal", "products": [
            P("mcrmb", "China Mastercard credit card", "Launched when Mastercard NUCC opened on 9 May 2024, alongside about eight other banks. RMB and US-dollar accounts for use at home and abroad, with 10 foreign currencies at ICBC. Links to WeChat Pay, Alipay, Meituan and JD.", short="China Mastercard (RMB)",
              s=["con", "traveller"], lc="everyday", st="new", ay="May 2024", o="P", at="Mastercard NUCC", neo=[2, "Mastercard, domestic and abroad ⚠ routing inferred."],
              mc="Mastercard's first domestic RMB issuing at China's largest bank.",
              src=[["China Securities Journal via Sina, May 2024", SINA24], ["Payments Dive: Mastercard NUCC approval, Nov 2023", NUCC23]]),
            P("mc101", "Mastercard '10+1' multi-currency debit card", "Launched in 2025 for domestic use and described by ICBC as the first of its kind. RMB plus 10 foreign currencies ⚠ (our reading of '10+1').",
              s=["con", "traveller"], lc="everyday", st="new", ay="2025", o="P", at="Mastercard", neo=[2, "Mastercard."],
              src=[["2025 Annual Report", AR25]]),
            P("etc", "ICBC European Travel co-branded credit card", "Launched on 3 February 2026 with the European Travel Commission and Mastercard for Chinese travellers to Europe. Four series and 10 foreign currencies, including euro, sterling and Swiss franc. No FX fee, plus cashback, ATM subsidies and a travel concierge ⚠ (press summary).", short="European Travel card (Mastercard)",
              s=["traveller"], lc="everyday", st="new", ay="Feb 2026", o="P", at="Mastercard, European Travel Commission", neo=[2, "Mastercard."],
              mc="Ailish Campbell (Mastercard) and Eduardo Santander (ETC) launched it; the clearest joint product.",
              src=[["ETC and Mastercard: European travel card, Feb 2026", ETC], ["Mastercard newsroom, Feb 2026", MCETC], ["Beijing Business Today, Feb 2026 ⚠", BBT], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "2.3", "ic": "earth", "name": "International cards", "blurb": "Peony Visa and Mastercard.", "div": "cards", "rev": "personal", "products": [
            P("peonyintl", "Peony International Debit Card", "RMB and foreign-currency accounts, issued as Peony Visa or Peony Mastercard (rules, April 2026 edition). At home it is used at UnionPay-marked points; abroad, wherever the scheme is accepted.", short="Peony International (Visa, Mastercard)",
              s=["traveller"], lc="everyday", o="B", at="Visa, Mastercard", neo=[1, "Split between Visa and Mastercard."],
              src=[["Peony International Debit Card rules, Apr 2026", PEONY]]),
            P("cobrand", "Mastercard co-brand heritage", "In 1995 ICBC was the first Chinese issuer to do a co-branded card with Mastercard, according to Mastercard's Ling Hai in 2017. Later cards include the ICBC MasterCard Lang Ping card (no annual fee or currency conversion fee) ⚠ undated, and a Shangri-La co-brand (2016) on Mastercard, Visa and UnionPay ⚠.",
              s=["traveller"], lc="everyday", ay="1995", o="P", at="Mastercard", neo=[1, "Mastercard and other networks."],
              src=[["PR Newswire: ICBC Sands Lifestyle Mastercard, Feb 2017", SANDS], ["ICBC: Lang Ping MasterCard card", LANGPING], ["ICBC: Shangri-La co-brand ⚠", SHANGRI]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Acceptance & visitors", "blurb": "Instant Refund for visitors.", "div": "icbc", "rev": "corporate", "products": [
            P("acquiring", "Merchant acquiring & Instant Refund", "Merchant services under GBC+, more than 180 consumer promotions in H1 2026, and 'Instant Refund' departure tax refunds for foreign visitors. Acquiring volumes are not disclosed.",
              s=["sme", "visitor"], lc="move", o="B", neo=[1, "Accepts every network ⚠."], src=[["2026 Interim Report", IR26], ["2025 Annual Report", AR25]]),
            P("inbound", "Foreign-card acceptance", "In March 2025 Visa planned low-cost card-and-QR terminals for the Visa–UnionPay Beijing Central Axis zone with ICBC, Bank of Beijing, Bank of Communications and Lakala ⚠ (a plan).",
              s=["visitor", "sme"], lc="move", st="new", ay="Mar 2025", o="P", at="Visa, UnionPay", neo=[0, "Visa and UnionPay led it."],
              mc="Visa, not Mastercard, put its name to ICBC's inbound terminals in Beijing.",
              src=[["Beijing: Visa–UnionPay zone, Mar 2025", BJVISA]]),
            P("weixin", "Weixin Pay for overseas UnionPay cards", "Since November 2024 visitors can link UnionPay cards issued outside the mainland to Weixin Pay, with ICBC providing the support.",
              s=["visitor"], lc="move", st="new", ay="Nov 2024", o="P", at="UnionPay International, Weixin Pay", neo=[0, "UnionPay."], src=[["UnionPay International, Nov 2024", UPI24]]),
        ]},
        {"id": "2.5", "ic": "globe", "name": "Cross-border & settlement", "blurb": "RMB5.5trn cross-border.", "div": "icbc", "rev": "corporate", "products": [
            P("igps", "ICBC Global Payment Services & cash management", "IGPS gives direct local payments in 44 countries or regions. More than 14,000 global cash-management customers. 17.82 million corporate settlement accounts, with RMB1,253 trillion of settlement in H1 2026.",
              s=["corp"], lc="move", o="B", neo=[0, ""], src=[["2025 Annual Report", AR25], ["2026 Interim Report", IR26]]),
            P("rmbclear", "Cross-border RMB & clearing", "RMB5.5 trillion of cross-border RMB in H1 2026 (+9%), and more than RMB10 trillion in 2025. RMB clearing bank in 12 countries, plus joint clearing for Africa with Standard Bank from June 2026. Early link to PBC's Cross-border Payment Connect.",
              s=["corp", "abroad"], lc="move", st="new", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26], ["China Daily: H1 2026 results, Aug 2026", CDH1], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "2.6", "ic": "coins", "name": "Digital money", "blurb": "e-CNY, mBridge, CBETS.", "div": "icbc", "rev": "treasury", "products": [
            P("ecny", "e-CNY", "e-CNY for fiscal funds, migrant-worker payroll and prepaid platforms. In 2025 ICBC made the first transaction on PBC's digital-asset platform and was named 'Best Digital RMB Service Provider in China'.",
              s=["con", "corp"], lc="move", o="P", at="People's Bank of China", neo=[0, "Central-bank rails."], src=[["2026 Interim Report", IR26], ["2025 Annual Report", AR25]]),
            P("mbridge", "mBridge & e-CNY cross-border", "Six overseas institutions, including ICBC (Asia), joined CBETS as direct participants. ICBC launched an 'e-CNY Cross-Border e-Commerce Payment Solution' (H1 2026) and has made e-CNY payments for China–Singapore trade.",
              s=["corp"], lc="move", st="new", o="P", at="PBC, m-CBDC Bridge", neo=[0, ""],
              mc="State-built cross-border rails that compete with card and A2A routes.",
              src=[["2026 Interim Report", IR26], ["2025 Annual Report", AR25]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: anti-telecom-fraud models and an enterprise risk platform, AI agents and a credit-card approval assistant, iBonus rewards and the e-Life platform, and open banking for small businesses.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & risk", "blurb": "Anti-telecom-fraud models.", "div": "icbc", "rev": "personal", "products": [
            P("fraud", "Anti-telecom-fraud controls", "Online anti-telecom-fraud risk control built on knowledge graphs, machine learning and LLMs, working with the police (H1 2026). Named 'China Best Anti-Fraud Technology Practice' by The Asian Banker.",
              s=["con"], lc="everyday", o="B", neo=[0, "ICBC's own."],
              mc="Telecom fraud is the stated priority; cross-border card traffic could use Mastercard's scoring.",
              src=[["2026 Interim Report", IR26]]),
            P("riskplat", "Enterprise intelligent risk platform", "Used in every domestic branch, moving risk control from manual to technology-led work (2025).",
              s=["corp"], lc="borrow", o="B", neo=[0, ""], src=[["2025 Annual Report", AR25]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI agents", "blurb": "2.8m card reviews by AI.", "div": "icbc", "rev": "personal", "products": [
            P("agents", "Customer & staff agents", "Two super agents, the 'Gong Xiao Cai' marketing agent and 'TianShu' agents for corporate account managers (2025–26).",
              s=["con", "corp"], lc="everyday", st="new", o="B", neo=[0, ""],
              mc="Agent Pay is untouched ground at a bank already building agents.",
              src=[["2026 Interim Report", IR26], ["2025 Annual Report", AR25]]),
            P("cardai", "Credit-card approval assistant", "A large model reviews applications, builds a full customer view and suggests decisions and limits. It was used more than 2.82 million times in H1 2026. AI also supports merchant review and instalment marketing.",
              s=["con"], lc="borrow", st="new", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards & lifestyle", "blurb": "iBonus and e-Life.", "div": "cards", "rev": "personal", "products": [
            P("ibonus", "ICBC iBonus Point & Member Benefits", "A single rewards platform. Points can be earned on spending through third-party payment platforms, Alipay points redeemed, and iBonus used for cash rebates on JD.com.",
              s=["con"], lc="grow", o="B", neo=[0, ""],
              mc="Card-linked offers could feed a rewards platform that already joins Alipay and JD.",
              src=[["2025 Annual Report", AR25], ["2026 Interim Report", IR26]]),
            P("elife", "ICBC e-Life & ICBC Travel", "A lifestyle platform for dining, delivery, travel, ride-hailing and trade-ins. The 'ICBC Travel' section (H1 2026) brings together credit-card benefits and merchants, and local governments use it for consumption vouchers.",
              s=["con", "traveller"], lc="beyond", st="new", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "3.4", "ic": "plug", "name": "Open banking & data", "blurb": "GBC+ and Operation+.", "div": "icbc", "rev": "corporate", "products": [
            P("openbank", "Open banking (GBC+)", "Open banking for tax, industrial internet, freight, agriculture and education. The data base includes the CIDA customer assembly and more than 1,200 credit-card customer tags and models.",
              s=["sme", "corp"], lc="open", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26], ["2025 Annual Report", AR25]]),
            P("operation", "Operation+ for small businesses", "A platform inside corporate mobile banking for finance and tax, payroll, office work, risk control and contracts (H1 2026).",
              s=["sme"], lc="everyday", st="new", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: deposits and wealth for 780 million people, RMB20 trillion of corporate loans, treasury and bond underwriting, leasing, asset management and insurance, and banks abroad that issue Mastercard alongside Visa and UnionPay.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Personal banking", "blurb": "RMB26.5trn of assets.", "div": "icbc", "rev": "personal", "products": [
            P("deposits", "Personal deposits & wealth", "RMB21.06 trillion of personal deposits and RMB26.5 trillion of personal financial assets at 30 June 2026. Private banking was named China's best by Euromoney. Pension finance and 'ICBC Wealth' run alongside.",
              s=["con"], lc="grow", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26]]),
            P("loans", "Personal loans & consumer finance", "RMB9.00 trillion of personal loans, covering mortgages, consumer, business and car finance. Interest subsidies applied to more than 100 million consumer transactions in H1 2026.",
              s=["con"], lc="borrow", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26]]),
        ]},
        {"id": "4.2", "ic": "factory", "name": "Corporate banking", "blurb": "48.6% of income.", "div": "icbc", "rev": "corporate", "products": [
            P("corporate", "Corporate loans & services", "RMB20.09 trillion of corporate loans at 30 June 2026, for more than 15 million corporate customers. Green loans exceed RMB7 trillion and digital-economy loans total RMB1.26 trillion.",
              s=["corp"], lc="borrow", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26], ["China Daily: H1 2026 results, Aug 2026", CDH1]]),
            P("inclusive", "Inclusive & small-business finance", "Inclusive loans grew 22.8% in 2025, with 'Sci-Tech Innovation e Loan', 'Merchant e Loan' and the 'Gong Xiao Hui' assistant.",
              s=["sme"], lc="borrow", o="B", neo=[0, ""],
              mc="Small-business and commercial cards are thin at home.",
              src=[["2025 Annual Report", AR25], ["2026 Interim Report", IR26]]),
        ]},
        {"id": "4.3", "ic": "chart-candlestick", "name": "Treasury & markets", "blurb": "14.3% of income.", "div": "icbc", "rev": "treasury", "products": [
            P("markets", "Treasury, bonds & FX", "Treasury operations brought in RMB64.0 billion in H1 2026. ICBC lead-underwrote 1,407 bond issues worth RMB1.04 trillion, and RMB24.7 billion of panda bonds. Offshore RMB FX market-making rose 36%.",
              s=["corp"], lc="grow", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26], ["China Daily: H1 2026 results, Aug 2026", CDH1]]),
        ]},
        {"id": "4.4", "ic": "briefcase-business", "name": "Subsidiaries", "blurb": "Leasing, wealth, insurance.", "div": "subs", "rev": "other", "products": [
            P("leasing", "ICBC Financial Leasing", "Aircraft, ship and equipment leasing; green ships make up 42.1% of the shipping book.",
              s=["corp"], lc="borrow", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26]]),
            P("assetmgmt", "ICBC Wealth Management & ICBCUBS", "ICBC Wealth Management runs RMB1.99 trillion of wealth products. ICBCUBS is a fully licensed fund house ⚠ (the former ICBC Credit Suisse; renaming date not confirmed).",
              s=["con"], lc="grow", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26]]),
            P("insurance", "ICBC-AXA Assurance", "A joint-venture life insurer covering protection, pensions and health.",
              s=["con"], lc="grow", o="P", at="AXA", neo=[0, ""], src=[["2026 Interim Report", IR26]]),
        ]},
        {"id": "4.5", "ic": "flag", "name": "Banks abroad", "blurb": "Mastercard beside Visa, UnionPay.", "div": "asia", "rev": "other", "products": [
            P("asia", "ICBC (Asia), Hong Kong", "Credit cards on Platinum Mastercard, Visa Signature, Visa Platinum and UnionPay dual-currency. A Mastercard Corporate Card, virtual cards on all three networks, Apple Pay, Huawei Pay and Click to Pay. Debit cards are UnionPay. Issued the Sands Lifestyle Mastercard (2017), which brought Pay with Rewards to Asia Pacific.", short="ICBC (Asia) (Mastercard, Visa, UnionPay)",
              s=["abroad"], lc="everyday", o="B", at="Mastercard, Visa, UnionPay", neo=[1, "Shared with Visa and UnionPay."],
              mc="Mastercard's deepest ICBC card relationship sits in Hong Kong.",
              src=[["ICBC (Asia): credit cards", ASIACARDS], ["ICBC (Asia): corporate cards", ASIACORP], ["ICBC (Asia): virtual cards", ASIAVIRT], ["ICBC (Asia): mobile payment", ASIAMOB], ["ICBC (Asia): debit card", ASIADEBIT], ["PR Newswire: Sands Lifestyle Mastercard, Feb 2017", SANDS]]),
            P("macau", "ICBC (Macau)", "Issues the MARTS Mastercard co-brand (no annual fee) and Visa co-brands such as New Yaohan.",
              s=["abroad"], lc="everyday", o="B", at="Mastercard, Visa", neo=[1, "Mastercard and Visa."], src=[["ICBC (Macau): MARTS Mastercard", MACAU]]),
            P("argentina", "ICBC (Argentina)", "Visa and Mastercard credit cards, including ICBC Visa Signature and ICBC Mastercard Black.",
              s=["abroad"], lc="everyday", at="Visa, Mastercard", neo=[1, "Visa and Mastercard."], src=[["ICBC (Argentina): personal banking", ARG]]),
            P("standard", "Standard Bank stake & other banks abroad", "Holds 19.74% of Standard Bank Group. Also owns ICBC Standard Bank in London and banks in Europe, the US, Canada, Thailand and Turkey. ICBC USA's 2016 credit cards ran on UnionPay and Visa.",
              s=["abroad", "corp"], lc="everyday", neo=[0, "UnionPay and Visa in the US."], src=[["2025 Annual Report", AR25], ["2026 Interim Report", IR26], ["Electronic Payments International: ICBC USA cards, Apr 2016", USA16]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach ICBC: the mobile bank with more than 300 million monthly users, corporate online banking, more than 15,000 outlets and 46,000 ATMs, and the wallets its cards link to.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Mobile banking", "blurb": "300m+ monthly users.", "div": "icbc", "rev": "personal", "products": [
            P("app", "ICBC mobile banking", "649 million personal mobile-banking customers and more than 300 million monthly active users at 30 June 2026, first in the industry. 'SmartEnjoy+ 1.0' launched in H1 2026. 99% of business is digital.",
              s=["con", "traveller"], lc="everyday", st="new", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Corporate online banking", "blurb": "19.9m firms.", "div": "icbc", "rev": "corporate", "products": [
            P("corpapp", "Corporate internet & mobile banking", "19.93 million corporate customers and 9.53 million monthly users at 30 June 2026.",
              s=["sme", "corp"], lc="everyday", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Outlets & ATMs", "blurb": "15,426 outlets.", "div": "icbc", "rev": "personal", "products": [
            P("outlets", "Outlets, self-service & ATMs", "15,426 outlets, 18,985 self-service banks, 70,672 intelligent devices and 45,923 ATMs at 30 June 2026, covering 87.6% of counties.",
              s=["con", "visitor"], lc="open", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26]]),
        ]},
        {"id": "5.4", "ic": "wallet", "name": "Wallets & platforms", "blurb": "WeChat Pay, Alipay, JD.", "div": "cards", "rev": "personal", "products": [
            P("wallets", "Third-party wallets", "ICBC cards, including the China Mastercard, link to WeChat Pay, Alipay, Meituan and JD. Rewards connect to Alipay points and JD.com.",
              s=["con"], lc="everyday", o="P", at="WeChat Pay, Alipay, JD", neo=[1, "Mastercard cards can sit inside the wallets."], src=[["China Securities Journal via Sina, May 2024", SINA24], ["2025 Annual Report", AR25]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at ICBC", "blurb": "Travel cards and banks abroad.", "products": [
        P("mcaticbc", "Mastercard at ICBC", "UnionPay carries most of ICBC's 1.3 billion domestic cards ⚠. Mastercard's links go back to the first co-brand in 1995. Since Mastercard NUCC opened in May 2024, ICBC has issued a China Mastercard RMB card, a '10+1' multi-currency debit card (2025) and the European Travel co-brand (February 2026). Peony international debit comes on Visa and Mastercard. ICBC (Asia), ICBC (Macau) and ICBC (Argentina) issue Mastercard alongside Visa and UnionPay.",
          s=["traveller"], div="icbc", rev="personal", mc="The relationship this map is drawn for.",
          src=[["China Securities Journal via Sina, May 2024", SINA24], ["ETC and Mastercard: European travel card, Feb 2026", ETC], ["2025 Annual Report", AR25]]),
    ]},
    {"id": "pillar-market", "name": "China's payments", "blurb": "UnionPay, wallets, e-CNY.", "products": [
        P("market", "The Chinese market", "UnionPay is the domestic scheme, and Alipay and WeChat Pay lead everyday payments ⚠ (no share figures gathered). Foreign schemes clear RMB only through licensed ventures: Mastercard NUCC (2023) and American Express's (2020). The state is pushing e-CNY, mBridge and easier payments for inbound visitors.",
          s=["con"], div="icbc", rev="other", src=[["Payments Dive: Mastercard NUCC approval, Nov 2023", NUCC23], ["UnionPay International, Nov 2024", UPI24], ["Beijing: Visa–UnionPay zone, Mar 2025", BJVISA]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
