"""Tencent's layers, areas and products, read through payments, as at 17 October 2026 (see page_data.py for the format).

Figures are Tencent's own unless a source says otherwise: the Q2 2026 results and presentation (12 August 2026)
and the 2025 annual results (18 March 2026), with Tencent's newsroom, Mastercard, Visa and the press for the
payments products. Tencent does not report payments revenue, volume or Weixin Pay users separately. Q3 2026
results are due on 18 November 2026. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own
product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q2 = "https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0812/2026081200296.pdf"
Q2PPT = "https://static.www.tencent.com/website-2026-upload/2Q26-earnings-PPT_20260812_1800-88b183.pdf"
FY25 = "https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0318/2026031800388.pdf"
IR = "https://www.tencent.com/en-us/investors.html"
TEAM = "https://www.tencent.com/who-we-are/our-team/"
ABOUT = "https://www.tencent.com/en-us/about.html"
MCMOVE = "http://www.tencent.com/tenpay-global-and-mastercard-collaborate-to-enable-fast-and-secure-remittances-to-weixin-pay/"
MC23 = "https://marketech-apac.com/mastercard-enables-wechat-pay-for-international-travelers-in-china"
VISA23 = "https://www.visa.com.sg/about-visa/newsroom/press-releases/visa-and-tencent-financial-technology-extend-global-partnership-to-facilitate-remittances-to-digital-wallets-utilising-visa-direct.html"
STD23 = "https://www.thestandard.com.hk/market/article/53720/WeChat-Pay-to-accept-global-cards"
APEC = "https://www.utusan.com.my/pr-newswire-en/2026/05/tencent-announces-three-initiatives-to-make-inbound-payments-for-international-visitors-easier-than-ever-during-apec-2026/"
EPI = "https://www.electronicpaymentsinternational.com/news/tencent-rolls-out-inbound-payments-upgrades/"
ELDIK = "https://www.thailand-business-news.com/pr-news/tencent-partners-with-kyrgyzstans-eldik-bank-to-further-expand-cross-border-payment-network-in-central-asia"
GOLDEN = "https://technode.global/2025/10/09/sea-sees-strong-growth-in-weixin-pay-usage-as-chinese-tourists-travel-abroad-over-golden-week/"
SUMMER = "https://vir.com.vn/weixin-cross-border-spend-jumps-34-percent-135538.html"
CONNECT = "https://fintechnews.hk/37756/payments/wechat-pay-hk-instant-transfers-mainland/"
SVF = "https://thepaypers.com/payments/news/green-lights-for-ant-financial-and-tencent-in-hong-kong"
GUIDE = "https://chinafortravelers.com/guides/wechat-pay-for-foreigners/"
FINE = "https://techcrunch.com/2023/07/07/china-wraps-up-fintech-crackdown-with-big-fines-on-tencent-and-alibaba/"
NUCC = "https://www.centralbanking.com/central-banks/payments/7960251/chinese-regulators-grant-mastercard-bank-card-licence"
MCAP = "https://companiesmarketcap.com/tencent/marketcap/"
WIKIPAY = "https://en.wikipedia.org/wiki/WeChat_Pay"
WIKITC = "https://en.wikipedia.org/wiki/Tencent"
WEBANK = "https://en.wikipedia.org/wiki/WeBank_(China)"
LCT = "https://www.caixinglobal.com/2018-03-22/tencent-money-market-fund-triples-in-three-years-101224888.html"
MERCH = "https://pay.weixin.qq.com/index.php/public/wechatpay_hk"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "scale · licences · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: RMB751.8 billion of revenue in 2025, a FinTech and Business Services segment of RMB229.4 billion, Tenpay's payment licence and the 2023 fine, and a group now spending heavily on AI.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & results", "blurb": "RMB204.8bn in Q2 2026.", "div": "grp", "rev": "grp", "products": [
            P("results", "Revenue & segments", "Revenue of RMB751.8 billion in 2025 (+14%); Q2 2026 revenue of RMB204.8 billion (+11%) and non-IFRS net profit of RMB68.4 billion (+9%). FinTech and Business Services was RMB60.3 billion in Q2 2026 (+9%), 30% of revenue, at a 52% gross margin. Market value about US$476 billion in October 2026 ⚠; 115,927 staff at 30 June 2026.",
              s=["mer"], neo=[0, ""], src=[["Tencent: Q2 2026 results", Q2], ["Tencent: 2025 results", FY25], ["CompaniesMarketCap: Tencent, Oct 2026", MCAP]]),
            P("fintechseg", "FinTech Services revenue", "Payments revenue is not reported on its own. FinTech Services grew at a high single-digit rate in 2025 on wealth management, consumer loans and commercial payments, and again in Q2 2026; commercial payment transactions grew while the fall in value per transaction narrowed.",
              s=["mer"], neo=[0, ""], src=[["Tencent: Q2 2026 presentation", Q2PPT], ["Tencent: 2025 results", FY25]]),
        ]},
        {"id": "1.2", "ic": "users-round", "name": "Leadership & ownership", "blurb": "Pony Ma; Prosus about 25%.", "div": "grp", "rev": "grp", "products": [
            P("leadership", "Executives in payments", "Pony Ma (co-founder, Chairman and CEO), Martin Lau (President), John Lo (CFO), Allen Zhang (President, Weixin Group) and Davis Lin (SVP; head of FiT ⚠). Royal Chen and Daniel Hong are vice presidents of Tencent Financial Technology; Wenhui Yang runs TenPay Global from Singapore.",
              s=["mer"], neo=[0, ""], src=[["Tencent: management team", TEAM], ["Tencent: TenPay Global and Mastercard, Dec 2025", MCMOVE], ["Tencent inbound initiative, May 2026", APEC]]),
            P("ownership", "Listing & ownership", "Founded in Shenzhen in November 1998 and listed in Hong Kong (0700) since June 2004. Prosus holds about 25–26% ⚠ and Pony Ma about 8% ⚠. Added to a US Defense Department list of companies allegedly linked to China's military in January 2025 ⚠.",
              s=["mer"], o="I", neo=[0, ""], src=[["Wikipedia: Tencent", WIKITC], ["Tencent IR", IR]]),
        ]},
        {"id": "1.3", "ic": "scale", "name": "Licences & regulation", "blurb": "Tenpay fined RMB2.99bn, 2023.", "div": "wxpay", "rev": "fbs", "products": [
            P("licences", "Payment licences", "Tenpay holds a mainland non-bank payment licence, among the first under the People's Bank of China's 2010 rules; WeChat Pay HK was in the first batch of Hong Kong stored-value licences (August 2016); TenPay Global is a network of licensed entities ⚠ list not public.",
              s=["con", "mer"], o="B", neo=[0, ""], src=[["Wikipedia: Tencent", WIKITC], ["The Paypers: Hong Kong SVF licences, Aug 2016", SVF]]),
            P("pbocfine", "PBOC fine & normalised supervision", "The People's Bank of China fined Tenpay about RMB2.99 billion in July 2023 for past breaches in mainland payment services; Tencent said rectification was complete. Ant was fined RMB7.12 billion the same day.",
              s=["con", "mer"], st="retired", ay="Jul 2023", neo=[0, ""], src=[["TechCrunch: fines on Tencent and Ant, Jul 2023", FINE]]),
        ]},
        {"id": "1.4", "ic": "brain", "name": "AI strategy", "blurb": "Hy3, WorkBuddy, compute.", "div": "grp", "rev": "grp", "products": [
            P("aistrategy", "An AI-empowered Tencent", "Hy3 model in production from July 2026, WorkBuddy and CodeBuddy leading AI office agents in China, and capital spending of RMB84.7 billion in H1 2026, mostly on compute.",
              s=["dev"], st="new", ay="Jul 2026", neo=[0, ""], src=[["Tencent: Q2 2026 results", Q2], ["Tencent: Q2 2026 presentation", Q2PPT]]),
        ]},
        {"id": "1.5", "ic": "building-2", "name": "Fintech stakes", "blurb": "WeBank, about 30%.", "div": "fit", "rev": "fbs", "products": [
            P("webank", "WeBank", "China's first online-only bank, approved in December 2014; Tencent is the largest shareholder with about 30% ⚠. Its Weilidai micro-loans are reached through Weixin and QQ.",
              s=["con"], lc="borrow", o="P", at="WeBank", neo=[0, ""], src=[["Wikipedia: WeBank", WEBANK]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Weixin Pay on domestic bank cards and balances, interoperable QR codes, foreign cards bound by visitors, overseas wallets through the national QR gateway, Weixin Pay for Chinese tourists abroad, remittances in on Visa Direct and Mastercard Move, and WeChat Pay HK across the border.",
    "tiles": [
        {"id": "2.1", "ic": "wallet", "name": "Weixin Pay", "blurb": "Number one by MAU in China.", "div": "wxpay", "rev": "fbs", "products": [
            P("wxpay", "Weixin Pay (WeChat Pay)", "Launched in August 2013 inside Weixin: QR codes, payment codes, in-app, Mini Program and quick pay, funded by wallet balance or bound mainland bank cards (UnionPay ⚠). Tencent calls it China's number one mobile payment by MAU and DAU; about 42% of mobile payments to Alipay's 53% ⚠.", short="Weixin Pay (domestic rails)",
              s=["con", "mer"], lc="move", ay="Aug 2013", o="B", neo=[0, "Domestic rails; bound cards are UnionPay."],
              mc="China's second-largest wallet runs almost entirely off the card networks Mastercard leads.",
              src=[["Wikipedia: WeChat Pay", WIKIPAY], ["Tencent: Q2 2026 presentation", Q2PPT]]),
            P("redpackets", "Red packets & transfers", "Digital red packets from January 2014 took users from 30 million to 100 million in a month; peer-to-peer transfers are free, with a 0.1% fee on withdrawals above RMB1,000 since March 2016.",
              s=["con"], lc="move", ay="Jan 2014", o="B", neo=[0, ""], src=[["Wikipedia: WeChat Pay", WIKIPAY]]),
        ]},
        {"id": "2.2", "ic": "refresh-cw", "name": "QR interoperability", "blurb": "Open to Alipay and UnionPay.", "div": "wxpay", "rev": "fbs", "products": [
            P("qrinterop", "Interoperable QR codes", "From 2021 a government mandate made payment QR codes interoperable across WeChat Pay, Alipay and UnionPay Cloud QuickPass; Taobao and Tmall added WeChat Pay at checkout.",
              s=["mer"], lc="move", ay="2021", o="P", at="Alipay, UnionPay", neo=[0, "UnionPay QR, not Mastercard."], src=[["Wikipedia: WeChat Pay", WIKIPAY]]),
        ]},
        {"id": "2.3", "ic": "credit-card", "name": "Foreign cards for visitors", "blurb": "Up 80% in early 2026.", "div": "wxpay", "rev": "fbs", "products": [
            P("foreigncard", "International card binding", "Opened to global card networks in July 2023, with Visa named first; Mastercard said in August 2023 its cardholders could link cards and use Weixin Pay's whole merchant network, building on a 2019 partnership. Visa, Mastercard, Amex, JCB, Discover, Diners and overseas UnionPay are accepted ⚠; limits about US$5,000 a payment and US$50,000 a year ⚠. Transactions up nearly 80% in January–April 2026.", short="Foreign cards (Mastercard among several)",
              s=["visitor"], lc="move", ay="Jul 2023", o="P", at="Visa, Mastercard, Amex, JCB", neo=[1, "One of several networks visitors can bind."],
              mc="The one place Mastercard cards run inside Weixin Pay, shared with Visa and the rest.",
              src=[["The Standard: global cards, Jun 2023", STD23], ["Marketech APAC: Mastercard and WeChat Pay, Aug 2023", MC23], ["Tencent inbound initiative, May 2026", APEC], ["China for Travelers: card guide, Aug 2026", GUIDE]]),
            P("feewaiver", "90-day fee waiver", "First-time users who link an international card get the 3% processing fee waived for 90 days on up to RMB1,000 a day, announced on 27 May 2026 ahead of APEC 2026 in Shenzhen.",
              s=["visitor"], lc="open", st="new", ay="May 2026", o="B", neo=[1, "Applies to every network's cards."], src=[["Tencent inbound initiative, May 2026", APEC], ["EPI: inbound upgrades, May 2026", EPI]]),
        ]},
        {"id": "2.4", "ic": "earth", "name": "Home e-wallets", "blurb": "40+ wallets via the CPG.", "div": "global", "rev": "fbs", "products": [
            P("cpg", "Pay with Your Home E-Wallet", "Through the People's Bank of China's Cross-Border Interconnection Payment Gateway (CPG, launched September 2025), Weixin Pay merchants accept over 40 overseas wallets, 36 live in 13 countries and regions by May 2026: LiquidPay, Zalopay, MoMo, BCEL One, Hipay, WeChat Pay HK and others. Eldik Bank (Kyrgyzstan) and HUMO Pay (Uzbekistan) followed in 2026.", short="Home e-wallets (CPG)",
              s=["visitor", "partner"], lc="move", st="new", ay="Sep 2025", o="P", at="PBOC gateway, overseas wallets", neo=[0, "Wallet-to-QR, not cards."],
              mc="Account-to-account wallet links that bypass card networks for visitors.",
              src=[["TenPay Global and Eldik Bank, May 2026", ELDIK], ["Tencent inbound initiative, May 2026", APEC]]),
            P("paypal", "PayPal World", "US PayPal users can scan Weixin Pay QR codes at tens of millions of merchants, through TenPay Global and PayPal World (May 2026); more markets to follow.",
              s=["visitor"], lc="move", st="new", ay="May 2026", o="P", at="PayPal", neo=[0, "PayPal wallet ⚠ funding may be a card."], src=[["Tencent inbound initiative, May 2026", APEC], ["EPI: inbound upgrades, May 2026", EPI]]),
        ]},
        {"id": "2.5", "ic": "plane", "name": "Outbound acceptance", "blurb": "Golden Week +21%.", "div": "global", "rev": "fbs", "products": [
            P("outbound", "Weixin Pay abroad", "Chinese tourists pay abroad through local acquirers and wallet links: Golden Week 2025 cross-border transactions up 21%, Korea up 46%, Singapore up 32%, Malaysia over three times via PayNet, Japan via PayPay, au PAY and merpay; overseas accepting merchants up 64% in H1 2025.",
              s=["con", "partner"], lc="move", o="P", at="Local acquirers, PayNet, PayPay", neo=[0, "Tencent's QR rails abroad."],
              mc="Outbound Chinese spend that could otherwise go on cards.",
              src=[["Technode: Golden Week 2025", GOLDEN], ["VIR: summer 2025 cross-border", SUMMER]]),
        ]},
        {"id": "2.6", "ic": "send", "name": "Remittances in", "blurb": "Visa Direct, Mastercard Move.", "div": "global", "rev": "fbs", "products": [
            P("mcmove", "Mastercard Move to Weixin Pay", "From 8 December 2025 senders can pay salaries and family support into a Weixin Pay balance or linked bank cards through Mastercard Move, reaching over 1.4 billion Weixin and WeChat users; China received about US$31.4 billion of remittances in 2024. Announced by Anouska Ladds (Mastercard) and Wenhui Yang (TenPay Global).", short="Mastercard Move",
              s=["sender", "partner"], lc="move", st="new", ay="Dec 2025", o="P", at="Mastercard", neo=[3, "Mastercard Move runs it."],
              mc="Mastercard's newest and deepest product link with Tencent.",
              src=[["Tencent: TenPay Global and Mastercard, Dec 2025", MCMOVE]]),
            P("visadirect", "Visa Direct to Weixin", "Visa Direct remittances into Weixin wallet balances using only a wallet ID or phone number, announced on 16 November 2023 by Shirley Yu (Visa Greater China) and Royal Chen; TenPay Global then had 30+ remittance partners in 60+ countries.",
              s=["sender", "partner"], lc="move", ay="Nov 2023", o="P", at="Visa", neo=[0, "Visa."], src=[["Visa: Visa Direct with Tencent, Nov 2023", VISA23]]),
        ]},
        {"id": "2.7", "ic": "arrow-left-right", "name": "WeChat Pay HK", "blurb": "HKD wallet, Payment Connect.", "div": "hk", "rev": "fbs", "products": [
            P("wphk", "WeChat Pay HK", "A Hong Kong-dollar wallet (2017) under a 2016 stored-value licence; Hong Kong users pay mainland merchants in HKD (use up more than 120% in Golden Week 2025) and link Hong Kong bank accounts and credit cards ⚠ networks not published. User numbers are not public.",
              s=["hk"], lc="move", o="B", neo=[1, "Linked HK credit cards include Mastercard ⚠."], src=[["The Paypers: Hong Kong SVF licences, Aug 2016", SVF], ["Technode: Golden Week 2025", GOLDEN]]),
            P("payconnect", "Payment Connect transfers", "The first e-wallet on Payment Connect, which links the mainland's IBPS to Hong Kong's FPS: free, instant transfers to mainland bank accounts, settled with HSBC (March 2026).",
              s=["hk"], lc="move", st="new", ay="Mar 2026", o="P", at="HSBC, HKMA, PBOC", neo=[0, "A2A rails."], src=[["Fintech News HK: Payment Connect, Mar 2026", CONNECT]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every payment: Mini Programs and the merchant platform, marketing that closes the loop inside Weixin, an agent called Xiaowei, real-name checks, and tax refunds and help desks for visitors.",
    "tiles": [
        {"id": "3.1", "ic": "store", "name": "Mini Programs & merchant tools", "blurb": "Mini Programs in 92 markets.", "div": "weixin", "rev": "fbs", "products": [
            P("miniprog", "Mini Programs", "Apps inside Weixin where most commerce happens; Mini Programs reach 92 countries and regions, and inbound visitors using them rose more than 60% in Golden Week 2025.",
              s=["mer", "visitor"], lc="everyday", o="B", neo=[0, ""], src=[["Technode: Golden Week 2025", GOLDEN]]),
            P("merchantplat", "Weixin Pay merchant platform", "Merchants submit business and bank details, sign up and bind a merchant ID or use no-code collection, with payment, marketing, fund management and developer tools and industry solutions for retail, dining, travel, health and government.",
              s=["mer"], lc="open", o="B", neo=[0, ""], src=[["Weixin Pay merchant platform", MERCH]]),
        ]},
        {"id": "3.2", "ic": "target", "name": "Marketing", "blurb": "RMB43.6bn, +22%.", "div": "weixin", "rev": "mkt", "products": [
            P("marketing", "Closed-loop marketing & AIM+", "Marketing Services revenue of RMB43.6 billion in Q2 2026 (+22%), with AI ad ranking, AIM+ automated campaigns and closed-loop marketing for Mini Shops and Mini Games inside Weixin.",
              s=["mer"], lc="grow", st="new", o="B", neo=[0, ""],
              mc="Merchant offers and spend data are fields Mastercard sells into elsewhere.",
              src=[["Tencent: Q2 2026 results", Q2]]),
        ]},
        {"id": "3.3", "ic": "bot", "name": "AI agents", "blurb": "Xiaowei and SkillPay.", "div": "weixin", "rev": "fbs", "products": [
            P("xiaowei", "Xiaowei", "An agentic AI inside Weixin on the WeLM model, in small-scale prototype testing from mid-2026; it uses Mini Programs to find products and place orders, 'laying groundwork for agent-to-agent transaction loop', and for now asks users to confirm each step.",
              s=["con"], lc="beyond", st="new", ay="2026", o="B", neo=[0, ""],
              mc="Agentic checkout on Weixin Pay with no card network involved yet.",
              src=[["Tencent: Q2 2026 presentation", Q2PPT], ["Tencent: Q2 2026 results", Q2]]),
            P("skillpay", "SkillPay in WorkBuddy", "WorkBuddy, the AI office agent, can execute transactions by embedding SkillPay and Weixin Pay inside the task flow.",
              s=["dev"], lc="move", st="new", ay="2026", o="B", neo=[0, ""], src=[["Tencent: Q2 2026 presentation", Q2PPT]]),
        ]},
        {"id": "3.4", "ic": "fingerprint", "name": "Identity & risk", "blurb": "Passport real-name checks.", "div": "wxpay", "rev": "fbs", "products": [
            P("realname", "Real-name verification & risk", "Visitors verify with a passport before the full card limits apply; Tenpay finished self-inspection and rectification after the 2023 fine. Tencent publishes little on its fraud models ⚠.",
              s=["visitor", "con"], lc="open", o="B", neo=[None, "Nothing public."],
              mc="Card-binding by visitors is a natural home for token and risk-scoring tools.",
              src=[["China for Travelers: card guide, Aug 2026", GUIDE], ["TechCrunch: fines on Tencent and Ant, Jul 2023", FINE]]),
        ]},
        {"id": "3.5", "ic": "receipt-text", "name": "Visitor services", "blurb": "Tax refunds, 16 languages.", "div": "global", "rev": "fbs", "products": [
            P("taxrefund", "Departure tax refunds", "TenPay Global works with tax-refund agents, starting with WeChat Pay HK in Shenzhen and then Shaanxi: refunds land in a Weixin Pay balance or an overseas e-wallet within minutes (2026).",
              s=["visitor"], lc="move", st="new", ay="May 2026", o="P", at="Tax-refund agents", neo=[0, "To wallets, not cards."], src=[["Tencent inbound initiative, May 2026", APEC], ["TenPay Global and Eldik Bank, May 2026", ELDIK]]),
            P("visitorhelp", "Multilingual help", "In-app payment guidance in 16 languages, offline desks at airports, ports of entry and hotels, and 24/7 online support, rolled out in Shenzhen ahead of APEC 2026.",
              s=["visitor"], lc="open", st="new", ay="May 2026", o="B", neo=[0, ""], src=[["Tencent inbound initiative, May 2026", APEC]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What earns the money: merchant fees on commercial payments, Licaitong wealth management, consumer loans with licensed partners, WeSure insurance, and Tencent Cloud in the same reported segment.",
    "tiles": [
        {"id": "4.1", "ic": "hand-coins", "name": "Commercial payments", "blurb": "More payments, smaller tickets.", "div": "wxpay", "rev": "fbs", "products": [
            P("commpay", "Commercial payment services", "Fees on merchant payments through Weixin Pay. In Q2 2026 transaction numbers grew year on year while the decline in value per transaction narrowed; revenue was seasonally lower than in Q1.",
              s=["mer"], lc="everyday", o="B", neo=[0, ""], src=[["Tencent: Q2 2026 presentation", Q2PPT], ["Tencent: Q2 2026 results", Q2]]),
        ]},
        {"id": "4.2", "ic": "trending-up", "name": "Wealth & insurance", "blurb": "Licaitong and WeSure.", "div": "fit", "rev": "fbs", "products": [
            P("licaitong", "Licaitong", "Wealth management in the Weixin wallet since 2014, selling partners' money-market and index funds; assets passed RMB300 billion in January 2018 and grew again in Q2 2026 on automated strategies and thematic index funds ⚠ current total not disclosed.",
              s=["con"], lc="grow", o="P", at="Fund managers", neo=[0, ""], src=[["Caixin: Licaitong, Mar 2018", LCT], ["Tencent: Q2 2026 presentation", Q2PPT]]),
            P("wesure", "WeSure", "An insurance agency platform in Weixin selling cover from insurers such as Ping An ⚠ figures not public.",
              s=["con"], lc="grow", o="P", at="Ping An and others", neo=[0, ""], src=[["Wikipedia: Tencent", WIKITC]]),
        ]},
        {"id": "4.3", "ic": "coins", "name": "Consumer loans", "blurb": "With licensed partners.", "div": "fit", "rev": "fbs", "products": [
            P("loans", "Consumer loans & Fenfu", "Revenue from consumer loan services through licensed institutions, including WeBank's Weilidai and Fenfu, a credit line inside Weixin Pay ⚠; Tencent cites 'prudent risk management'.",
              s=["con"], lc="borrow", o="P", at="WeBank and other lenders", neo=[0, "No card product."],
              mc="Instalments and credit that sit outside the card networks.",
              src=[["Tencent: 2025 results", FY25], ["Wikipedia: WeBank", WEBANK]]),
        ]},
        {"id": "4.4", "ic": "database", "name": "Tencent Cloud", "blurb": "Low-20s% growth.", "div": "cloud", "rev": "fbs", "products": [
            P("cloud", "Tencent Cloud", "Cloud revenue growth accelerated to the low twenties per cent in Q2 2026 on AI demand (GPU rental, Model-as-a-Service) and international expansion; profitable at scale since 2025.",
              s=["dev", "mer"], lc="beyond", o="B", neo=[0, ""], src=[["Tencent: Q2 2026 presentation", Q2PPT], ["Tencent: 2025 results", FY25]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How people reach it: Weixin and WeChat for 1.44 billion, the WeChat Pay HK app, QQ Wallet, and the acquirers, wallets and remittance firms that connect TenPay Global abroad.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Weixin & WeChat", "blurb": "1.439bn monthly users.", "div": "weixin", "rev": "vas", "products": [
            P("weixin", "Weixin and WeChat", "Combined monthly active users of 1,439 million at 30 June 2026 (+2%); the wallet, Mini Programs and red packets all live inside it.",
              s=["con", "visitor"], lc="everyday", o="B", neo=[0, ""], src=[["Tencent: Q2 2026 results", Q2]]),
            P("qqwallet", "QQ Wallet", "A second consumer wallet on Tenpay inside QQ, which had 520 million mobile users in Q2 2026 ⚠ wallet figures not published.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["Tencent: Q2 2026 results", Q2]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "WeChat Pay HK app", "blurb": "Hong Kong's HKD wallet.", "div": "hk", "rev": "fbs", "products": [
            P("wphkapp", "WeChat Pay HK wallet", "The Hong Kong wallet inside WeChat, with 'Transfer to Chinese Mainland' for Payment Connect and HKD payments at mainland merchants down to Shenzhen taxis.",
              s=["hk"], lc="everyday", o="B", neo=[0, ""], src=[["Fintech News HK: Payment Connect, Mar 2026", CONNECT]]),
        ]},
        {"id": "5.3", "ic": "network", "name": "TenPay Global partners", "blurb": "Acquirers, wallets, remitters.", "div": "global", "rev": "fbs", "products": [
            P("partners", "Acquirers, wallets & remittance firms", "Local acquirers abroad, over 40 overseas wallets through the CPG, 30+ remittance institutions in 60+ countries (2023), and Visa, Mastercard and PayPal as network partners.",
              s=["partner"], lc="open", o="P", at="Visa, Mastercard, PayPal, wallets", neo=[1, "Mastercard is one partner among many."], src=[["Visa: Visa Direct with Tencent, Nov 2023", VISA23], ["TenPay Global and Eldik Bank, May 2026", ELDIK]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Tencent", "blurb": "Visitor cards and Move.", "products": [
        P("mcattencent", "Mastercard at Tencent", "Weixin Pay runs on domestic rails and issues no cards. Mastercard is one of several networks visitors can bind (since August 2023, from a 2019 partnership) and, since December 2025, Mastercard Move pays remittances into Weixin Pay, two years after Visa Direct. Mastercard's China clearing venture has held a licence since November 2023 ⚠ live scale unknown.",
          s=["visitor"], div="global", rev="fbs", mc="The relationship this map is drawn for.",
          src=[["Marketech APAC: Mastercard and WeChat Pay, Aug 2023", MC23], ["Tencent: TenPay Global and Mastercard, Dec 2025", MCMOVE], ["Central Banking: Mastercard licence, Nov 2023", NUCC]]),
    ]},
    {"id": "pillar-market", "name": "China payments", "blurb": "Two wallets, UnionPay, the PBOC.", "products": [
        P("market", "The Chinese market", "Alipay about 53% and WeChat Pay about 42% of mobile payments ⚠; UnionPay as the domestic card scheme; interoperable QR codes since 2021; normalised supervision after the 2023 fines; and a state push since 2023 to make payments easy for visitors.",
          s=["con"], div="wxpay", rev="fbs", src=[["Wikipedia: WeChat Pay", WIKIPAY], ["TechCrunch: fines on Tencent and Ant, Jul 2023", FINE]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
