"""Bank of China's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the 2026 Interim Report (28 August 2026), the 2025
Annual Report (30 March 2026) and BOCHK's 2026 interim results (28 August 2026). ``neo`` is the Mastercard lens:
[depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

IR26 = "https://pic.bankofchina.com/bocappd/report/202608/P020260828601670971259.pdf"
AR25 = "https://pic.bankofchina.com/bocappd/report/202603/P020260330594078083473.pdf"
HKIR26 = "https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0828/2026082800459.pdf"
FR = "https://filingreader.com/news-wire/hongkong/2026-08-29/bank-of-china-reports-first-half-profit-growth"
GALLERY = "https://www.boc.cn/en/aboutboc/ab5/200811/t20081117_1602013.html"
HIST = "https://www.boc.cn/en/aboutboc/ab7/200809/t20080926_1601852.html"
BCEN = "https://www.boc.cn/en/bcservice/"
SINA24 = "https://finance.sina.cn/2024-05-12/detail-inauyvkv5963643.d.html"
ITH24 = "https://www.ithome.com/0/766/714.htm"
ITH23 = "https://www.ithome.com/0/733/632.htm"
EPI24 = "https://www.electronicpaymentsinternational.com/news/mastercard-jv-switches-first-domestic-transaction-in-china"
ITH25 = "https://www.ithome.com/0/844/397.htm"
HKLIST = "https://www.bochk.com/dam/boccreditcard/cardproductlisting/eng/index.html"
CHILL = "https://www.bochk.com/dam/boccreditcard/chillcard/eng/index.html"
CHEERS = "https://www.bochk.com/dam/boccreditcard/cheerscard/eng/index.html"
GO = "https://www.bochk.com/dam/boccreditcard/gocard/eng/index.html"
BLISS = "https://www.bochk.com/dam/boccreditcard/blisscard/eng/index.html"
HKCC = "https://www.bochk.com/en/creditcard.html"
MCCHILL = "https://newsroom.mastercard.com/news/ap/en-hk/newsroom/press-releases/en-hk/2022/june/bochk-partners-with-mastercard-to-launch-boc-chill-card"
MIVISA = "https://www.marketing-interactive.com/bochk-and-visa-unveil-new-card-to-cope-with-change-in-consumption-patterns"
OLY = "https://ikkyinchina.com/2021/09/13/digital-payments-beijing-olympics"
VISAPR = "https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.22846.html"
BDAY = "https://www.businessday.co.za/business-times/business/2026-10-13-visa-receives-approval-to-prepare-for-domestic-business-in-china/"
AMEX11 = "https://www.privatebankerinternational.com/news/bank-of-china-to-issue-american-express-branded-credit-cards-for-wealthy-customers-271011/"
MCAP = "https://marketcapof.com/stocks/bachf.us/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · state · reach", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: RMB40 trillion of assets, a bank founded in 1912 and now owned mainly by the Chinese state, a G-SIB since 2011, the BOCAI model platform and 532 institutions in 64 countries outside the mainland.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "RMB40.2trn, ROE 8.7%.", "div": "boc", "rev": "other", "products": [
            P("balance", "Balance sheet & earnings", "Total assets of RMB40.19 trillion, gross loans of RMB24.74 trillion and customer deposits of RMB26.83 trillion at 30 June 2026. Operating income of RMB357.1 billion (+8.41%) and profit of RMB132.0 billion (+4.67%) in the half; RMB257.9 billion of profit in 2025. NIM 1.27%, ROE 8.66%, NPL ratio 1.22%, CET1 12.04%.",
              s=["con", "corp"], neo=[0, ""], src=[["2026 Interim Report", IR26], ["2025 Annual Report", AR25], ["FilingReader: H1 2026, Aug 2026", FR]]),
        ]},
        {"id": "1.2", "ic": "building-2", "name": "Heritage, owners & ratings", "blurb": "Since 1912; Huijin 58.6%.", "div": "boc", "rev": "other", "products": [
            P("owners", "Ownership, listing & ratings", "Founded in February 1912 and once China's central bank, then its foreign-exchange bank. Listed in Hong Kong and Shanghai in 2006. Central Huijin holds 58.59% and the Ministry of Finance 8.64% after a RMB165 billion share placement in 2025. Rated A by S&P and Fitch and A1 by Moody's. The first G-SIB from an emerging economy (2011). Market value about US$209 billion ⚠ (third-party, July 2026).",
              s=["corp"], o="I", neo=[0, ""], src=[["2025 Annual Report", AR25], ["MarketCapOf: BACHF, Jul 2026 ⚠", MCAP]]),
        ]},
        {"id": "1.3", "ic": "scale", "name": "Leadership", "blurb": "Ge Haijiao and Zhang Hui.", "div": "boc", "rev": "other", "products": [
            P("leadership", "Board & senior management", "Chairman Ge Haijiao, who also chairs BOCHK. Zhang Hui is Vice Chairman and President, and Chief Compliance Officer from February 2026. Executive Vice Presidents: Cai Zhao, Wu Jian, Yang Jun, Liu Chenggang and Huang Xueling (from March 2026). The Chief Risk Officer left in January 2026 ⚠ (no successor named). 310,898 employees. BOCHK's Chief Executive is Sun Yu.",
              s=["corp"], neo=[0, ""], src=[["2026 Interim Report", IR26], ["BOCHK 2026 interim results", HKIR26]]),
        ]},
        {"id": "1.4", "ic": "brain", "name": "Technology & AI", "blurb": "2,200 AI assistants.", "div": "boc", "rev": "other", "products": [
            P("ai", "BOCAI & the AI+ plan", "An 'AI + Finance' implementation plan and a '326' AI framework. The BOCAI large-model platform has agent capabilities, more than 32,000 users and runs on a group cloud of 55,000 servers, and more than 2,200 intelligent assistants across credit, marketing, operations, risk and customer service (H1 2026).",
              s=["con", "corp"], lc="everyday", st="new", neo=[0, ""],
              mc="A bank building agents with no agentic card payments yet.",
              src=[["2026 Interim Report", IR26]]),
        ]},
        {"id": "1.5", "ic": "earth", "name": "Global reach & strategy", "blurb": "532 institutions, 64 countries.", "div": "overseas", "rev": "other", "products": [
            P("intl", "Global network", "532 overseas institutions in 64 countries and regions, including 45 Belt and Road countries, and the only Chinese bank in all 21 APEC economies. Outside the mainland, Hong Kong, Macao and Taiwan brought 17.0% of H1 2026 income and other countries 4.4%.",
              s=["corp", "hk"], neo=[0, ""], src=[["2026 Interim Report", IR26]]),
            P("strategy", "Globalisation & the 15th Five-Year Plan", "2026 is the first year of the 15th Five-Year Plan. BOC calls globalisation its core strategy and works on the state's 'five major tasks': technology, green, inclusive, pension and digital finance. Technology loans are more than a third of corporate loans.",
              s=["corp"], st="new", neo=[0, ""], src=[["2026 Interim Report", IR26]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: 750 million debit and 152 million credit cards, mostly UnionPay at home; Great Wall Mastercard RMB cards since 2024; Visa and Mastercard for travel; the leading foreign-card acquirer for visitors; CIPS, RMB clearing, e-CNY and mBridge; and BOCHK's cards on Visa, Mastercard and UnionPay.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Domestic cards", "blurb": "750m debit, 152m credit.", "div": "cards", "rev": "personal", "products": [
            P("debit", "BOC debit cards", "More than 750.5 million debit cards issued in total by 30 June 2026, including more than 130 million social security cards and 10.5 million rural revitalisation cards. Domestic use runs on UnionPay ⚠ (inferred; BOC does not split by network).",
              s=["con"], lc="everyday", o="B", at="UnionPay", neo=[0, "UnionPay at home ⚠."], src=[["2026 Interim Report", IR26], ["2025 Annual Report", AR25]]),
            P("credit", "Great Wall credit cards", "151.9 million credit cards issued in total. RMB535.3 billion of spending in H1 2026 and RMB1,103.7 billion in 2025. Card loans fell from RMB486.0 billion to RMB449.2 billion in the half; card NPL ratio 2.37%. Great Wall premium cards for private and wealth clients, a YOU Card for young people, and new-energy-vehicle instalments. Mostly UnionPay ⚠; network split not disclosed.", short="Great Wall credit (mostly UnionPay ⚠)",
              s=["con"], lc="borrow", st="flux", o="B", at="UnionPay, Mastercard, Visa", neo=[1, "Mostly UnionPay; some Mastercard, Visa, JCB, Amex ⚠."],
              mc="A shrinking credit book where Mastercard holds a small share.",
              src=[["2026 Interim Report", IR26], ["2025 Annual Report", AR25]]),
            P("quickpay", "Quick payments & BOC Travel Benefits", "Debit-card quick payments passed RMB4 trillion in H1 2026 (RMB8 trillion in 2025). The 'BOC Travel Benefits' brand runs payment promotions in more than 100 cities. Mobile banking joined the UnionPay cloud network in 2025.",
              s=["con"], lc="everyday", st="new", o="B", at="UnionPay", neo=[0, ""], src=[["2026 Interim Report", IR26], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Mastercard RMB cards", "blurb": "Great Wall Mastercard since 2024.", "div": "cards", "rev": "personal", "products": [
            P("gwmc", "Great Wall Mastercard series (RMB)", "Issued when Mastercard NetsUnion opened on 9 May 2024; BOC was among the first banks named. Unlike BOC's older Mastercard, which worked only abroad, it can be used in China and overseas, and linked to WeChat Pay and Alipay.", short="Great Wall Mastercard (RMB)",
              s=["con", "traveller"], lc="everyday", st="new", ay="May 2024", o="P", at="Mastercard NetsUnion", neo=[2, "Mastercard, at home and abroad."],
              mc="Mastercard's first domestic RMB issuing at China's oldest bank.",
              src=[["Sina Finance, May 2024", SINA24], ["IT Home, May 2024", ITH24], ["Electronic Payments International, May 2024", EPI24]]),
            P("mcdual", "Mastercard dual-application credit cards", "In 2025 BOC launched a 'Mastercard dual-application credit card product system' for online and offline use at home and abroad, and switched on domestic use for its single-branded Mastercard cards: one card for both.",
              s=["traveller"], lc="everyday", st="new", ay="2025", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["2025 Annual Report", AR25]]),
            P("mcdebit", "Mastercard RMB debit cards", "Issued on the spot at BOC's smart counters in H1 2026, alongside social security cards and e-CNY wallets.",
              s=["con", "traveller"], lc="everyday", st="new", ay="2026", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["2026 Interim Report", IR26]]),
        ]},
        {"id": "2.3", "ic": "plane", "name": "International cards", "blurb": "Visa and Mastercard for travel.", "div": "cards", "rev": "personal", "products": [
            P("heritage", "Great Wall International Card", "In 1987 BOC was the first Chinese bank to join Mastercard and Visa. In 1988 it issued the Great Wall International Card, a Mastercard and China's first international credit card. From 1992 its card centre acquired and settled Mastercard and Visa cards in China.",
              s=["traveller"], lc="everyday", st="retired", ay="1988", o="B", at="Mastercard, Visa", neo=[2, "Mastercard."],
              src=[["BOC: Bank Card Gallery", GALLERY], ["BOC: credit card history", HIST]]),
            P("visaup", "Visa–UnionPay dual-brand credit cards", "Existing dual-brand cards moved from magnetic stripe to chip in batches from 25 May 2025, to make overseas use safer.",
              s=["traveller"], lc="everyday", st="flux", ay="May 2025", o="P", at="Visa, UnionPay", neo=[0, "Visa."],
              src=[["IT Home, Apr 2025", ITH25], ["2025 Annual Report", AR25]]),
            P("applepay", "Apple Pay for Visa and Mastercard cards", "Launched in H1 2026 for BOC's Visa and Mastercard cards, for customers travelling abroad.",
              s=["traveller"], lc="everyday", st="new", ay="2026", o="P", at="Apple, Visa, Mastercard", neo=[1, "Visa and Mastercard."],
              mc="Tokenised cards at a bank that does not disclose other token work.",
              src=[["2026 Interim Report", IR26]]),
            P("xborder", "Cross-border cards & Global Wonderful", "The Zhuojun Credit Card and Cross-Border Debit Card for students and travellers, the 'Global Wonderful' campaign and 'BOC Benefits for Overseas Study'. Networks are not stated ⚠.",
              s=["traveller"], lc="everyday", st="new", o="B", neo=[None, "Networks not disclosed ⚠."],
              mc="Students and travellers are where Mastercard benefits could be packaged.",
              src=[["2026 Interim Report", IR26], ["2025 Annual Report", AR25]]),
            P("legacy", "Overseas Great Wall, JCB & Amex cards", "BOC's English card pages list a Great Wall International Credit Card issued in the UK, a Great Wall Maestro debit card and a BOC JCB credit card ⚠ (pages may be dated). In 2011 BOC and American Express launched the BOC Private Bank American Express Card.",
              s=["traveller", "con"], lc="everyday", o="P", at="Mastercard, JCB, Amex", neo=[1, "Mastercard and Maestro beside JCB and Amex ⚠."],
              src=[["BOC: bank cards", BCEN], ["Private Banker International, Oct 2011", AMEX11]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Acceptance & visitors", "blurb": "Foreign-card volume +64%.", "div": "boc", "rev": "corporate", "products": [
            P("foreigncard", "Foreign-card acquiring", "BOC says it leads the foreign-card acquiring market and covers all of the PBOC's key merchants. Foreign-card volume rose by 75.73% in 2025 and by 64.35% in H1 2026. 24/7 ATM withdrawals for major international cards, and card acceptance for the Canton Fair, CIIE and other events.",
              s=["visitor", "sme"], lc="move", st="new", o="B", at="Visa, Mastercard, others ⚠", neo=[1, "Accepts every network ⚠."],
              mc="The leading acquirer of Mastercard-branded visitor spending in China ⚠.",
              src=[["2026 Interim Report", IR26], ["2025 Annual Report", AR25]]),
            P("taxrefund", "Departure tax refund", "Tax-refund agency services for visitors in 25 provinces (H1 2026), with self-service refund terminals in Shenzhen that take under three minutes.",
              s=["visitor"], lc="move", st="new", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26]]),
            P("olympics", "Olympic payments with Visa", "Official banking partner of Beijing 2008 and Beijing 2022. For 2022 BOC worked with Visa, the Games' payment partner, on acceptance at venues and Olympic Visa cards.",
              s=["visitor"], lc="move", st="retired", ay="2021", o="P", at="Visa", neo=[0, "Visa."],
              src=[["2025 Annual Report", AR25], ["Ikky in China, Sep 2021", OLY]]),
        ]},
        {"id": "2.5", "ic": "globe", "name": "Cross-border & digital money", "blurb": "CIPS, e-CNY, mBridge.", "div": "boc", "rev": "corporate", "products": [
            P("cips", "International settlement & RMB clearing", "USD2.61 trillion of international settlement in H1 2026 (+23%). First in CIPS participant relationships and holds 19 RMB clearing-bank seats, adding the UK, Sri Lanka and Indonesia in 2026.",
              s=["corp"], lc="move", st="new", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26]]),
            P("remit", "BOC Instant Remittance", "The first new-generation cross-border remittance product in the Chinese mainland (H1 2026). Rails not described ⚠.",
              s=["con", "traveller"], lc="move", st="new", ay="2026", o="B", neo=[None, "Rails not disclosed ⚠."],
              mc="Cross-border person-to-person flows that Mastercard Move competes for.",
              src=[["2026 Interim Report", IR26]]),
            P("ecny", "e-CNY", "31.5 million e-CNY consumer payments worth RMB10.8 billion in H1 2026, plus RMB11.2 billion of tax payments; BOC says it leads the market.",
              s=["con", "corp"], lc="move", o="P", at="People's Bank of China", neo=[0, "Central-bank rails."], src=[["2026 Interim Report", IR26]]),
            P("mbridge", "mBridge & cross-border e-CNY", "More than RMB600 billion of mBridge transactions in total by June 2026, the first in Macao, and direct participation in the PBOC's cross-border e-CNY transfer platform.",
              s=["corp"], lc="move", st="new", o="P", at="PBOC, mBridge", neo=[0, ""],
              mc="State-built cross-border rails beside card and account routes.",
              src=[["2026 Interim Report", IR26], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "2.6", "ic": "gem", "name": "Hong Kong cards", "blurb": "Visa, Mastercard, UnionPay.", "div": "hkcards", "rev": "personal", "products": [
            P("cheers", "BOC Cheers Card", "BOCHK's flagship rewards card, on Visa Infinite and Visa Signature, relaunched with Visa in July 2023. The renamed BOC Bliss Card (formerly the Travel Visa Signature) is also on Visa.", short="BOC Cheers (Visa)",
              s=["hk"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."],
              src=[["BOCHK: Cheers Card", CHEERS], ["BOCHK: Bliss Card", BLISS], ["Marketing-Interactive, Jul 2023", MIVISA]]),
            P("chill", "BOC Chill Card", "Launched with Mastercard on 28 June 2022 as BOCHK's first eco-friendly card, now as World and Platinum Mastercard. Cash rebates of up to 10% at Chill merchants and 5% overseas and online, Pay Later instalments, e-commerce protection and Mastercard Travel Rewards.", short="BOC Chill (Mastercard)",
              s=["hk"], lc="everyday", ay="Jun 2022", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Launched by Huang Jinyue (BOC Credit Card) and Helena Chen (Mastercard).",
              src=[["Mastercard: BOC Chill Card, Jun 2022", MCCHILL], ["BOCHK: Chill Card", CHILL]]),
            P("gocard", "BOC Go Card", "A UnionPay dual-currency card for Greater Bay Area and cross-border spending, with UnionPay privileges and QuickPass.", short="BOC Go (UnionPay)",
              s=["hk", "traveller"], lc="everyday", o="P", at="UnionPay International", neo=[0, "UnionPay."],
              src=[["BOCHK: Go Card", GO], ["BOCHK 2026 interim results", HKIR26]]),
            P("hkcobrand", "Co-brand & affinity cards", "Taobao and Esso World Mastercards; SOGO, Henderson Club and Hong Kong Airlines Visa cards; SaSa and CMHK UnionPay dual-currency cards; and university and association cards. Card fee income rose 12.2% to HK$1,474 million in H1 2026.",
              s=["hk"], lc="everyday", o="P", at="Mastercard, Visa, UnionPay", neo=[1, "Split three ways."],
              src=[["BOCHK: credit card listing", HKLIST], ["BOCHK 2026 interim results", HKIR26]]),
            P("hkbiz", "Business & commercial cards", "BOC Visa Infinite and Visa Platinum Business Cards and a UnionPay dual-currency commercial card.",
              s=["sme", "hk"], lc="everyday", o="P", at="Visa, UnionPay", neo=[0, "Visa and UnionPay."],
              mc="No Mastercard commercial card in BOCHK's line-up.",
              src=[["BOCHK: credit card listing", HKLIST]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: the Cyber Defence risk system that watched 9.2 billion online transactions, AI and automation, BOC Benefits and BOCHK's rewards, and open-banking platforms for firms.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & risk", "blurb": "9.2bn transactions watched.", "div": "boc", "rev": "personal", "products": [
            P("fraud", "Cyber Defence & anti-phishing", "The 'Cyber Defence' smart risk-control system monitored 9.217 billion online transactions in 2025, and BOC shut down 9,396 phishing sites and app links. BOCHK runs anti-fraud education with its 'Trusty' ambassador.",
              s=["con", "hk"], lc="everyday", o="B", neo=[0, "BOC's own."],
              mc="Cross-border card fraud could use Mastercard scoring.",
              src=[["2025 Annual Report", AR25], ["BOCHK 2026 interim results", HKIR26]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI & automation", "blurb": "3,800 automated scenarios.", "div": "boc", "rev": "other", "products": [
            P("automation", "Automation & AI DocuAssist", "Robotic process automation in more than 3,800 scenarios, with about 300,000 tasks a month. AI recognises 305 types of document, and BOC AI DocuAssist extracts data from documents.",
              s=["corp"], lc="everyday", st="new", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26]]),
            P("bonnie", "Bonnie & BOCHK iService", "BOCHK's virtual assistant 'Bonnie' and remote service platform 'iService', with facial recognition in mobile banking.",
              s=["hk"], lc="everyday", o="B", neo=[0, ""],
              mc="Assistants that could one day pay on a customer's behalf.",
              src=[["BOCHK 2026 interim results", HKIR26]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards & benefits", "blurb": "BOC Benefits, Amazing Rewards.", "div": "cards", "rev": "personal", "products": [
            P("benefits", "BOC Benefits", "Seasonal 'BOC Benefits' campaigns for culture, tourism, hotels and supermarkets, run with payment institutions and card networks, plus government trade-in subsidies and instalment offers on e-commerce platforms.",
              s=["con"], lc="beyond", st="new", o="P", at="Card networks, payment institutions", neo=[1, "Run with several networks ⚠."],
              mc="Card-linked offers could feed campaigns BOC already runs with networks.",
              src=[["2026 Interim Report", IR26], ["2025 Annual Report", AR25]]),
            P("hkrewards", "Amazing Local & Global Rewards", "BOCHK's campaigns for local online and overseas spending, priority concert tickets now open to mainland and Macao cardholders, and the Gift Point programme.",
              s=["hk"], lc="beyond", st="new", o="B", neo=[0, ""], src=[["BOCHK 2026 interim results", HKIR26], ["BOCHK: credit cards", HKCC]]),
        ]},
        {"id": "3.4", "ic": "plug", "name": "Open banking & data", "blurb": "e-Manager, Fortune.", "div": "boc", "rev": "corporate", "products": [
            P("openbank", "Scenario finance & open banking", "BOC Corporate e-Manager, and a 'Fortune' community of 44 partner institutions in funds, insurance and securities inside mobile banking (June 2026).",
              s=["sme", "corp"], lc="open", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: deposits, wealth and loans for about 554 million people, corporate and inclusive lending, treasury and bonds, investment banking, insurance and aircraft leasing, and BOCHK in Hong Kong and Southeast Asia.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Personal banking", "blurb": "39.1% of income.", "div": "boc", "rev": "personal", "products": [
            P("wealth", "Deposits, wealth & pensions", "Personal AUM of more than RMB18 trillion and RMB1.51 trillion of distributed wealth products at 30 June 2026. About 554 million domestic personal customers at end-2025. BOC Pension Finance and private banking.",
              s=["con"], lc="grow", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26], ["2025 Annual Report", AR25]]),
            P("loans", "Personal & consumer loans", "RMB6.02 trillion of personal loans in the mainland at 30 June 2026. Interest subsidies on consumer loans reached more than 1.66 million customers.",
              s=["con"], lc="borrow", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26]]),
        ]},
        {"id": "4.2", "ic": "factory", "name": "Corporate banking", "blurb": "38.0% of income.", "div": "boc", "rev": "corporate", "products": [
            P("corporate", "Corporate loans & trade", "Corporate banking brought in RMB135.6 billion in H1 2026. Corporate customers grew 7.54% in the half, from more than 8.4 million. Cross-border e-commerce volume rose 24.5%.",
              s=["corp"], lc="borrow", o="B", neo=[0, ""],
              mc="Exporters and cross-border sellers with no commercial-card offer found.",
              src=[["2026 Interim Report", IR26], ["2025 Annual Report", AR25]]),
            P("inclusive", "Inclusive & small-business finance", "Inclusive loans of more than RMB3.06 trillion to about 1.99 million borrowers at 30 June 2026.",
              s=["sme"], lc="borrow", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26]]),
        ]},
        {"id": "4.3", "ic": "chart-candlestick", "name": "Treasury & markets", "blurb": "14.0% of income.", "div": "boc", "rev": "treasury", "products": [
            P("markets", "Treasury, bonds & FX", "Treasury operations brought in RMB50.1 billion in H1 2026. Top in Panda, free-trade-zone and offshore RMB bond underwriting.",
              s=["corp"], lc="grow", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26]]),
        ]},
        {"id": "4.4", "ic": "briefcase-business", "name": "Investment banking & insurance", "blurb": "BOCI, BOC Life, BOC Aviation.", "div": "boci", "rev": "ibins", "products": [
            P("boci", "BOC International", "Investment banking through BOCI, with HK$1.35 billion of profit in H1 2026, BOCI China (listed in Shanghai) and BOCI-Prudential, fifth in Hong Kong's MPF market.",
              s=["corp"], lc="grow", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26]]),
            P("insurance", "BOC Life & BOCG Insurance", "BOC Life's standard new premiums rose 27.9% to HK$18.96 billion in H1 2026. BOCG Insurance writes general insurance.",
              s=["con", "hk"], lc="grow", o="B", neo=[0, ""], src=[["BOCHK 2026 interim results", HKIR26], ["2026 Interim Report", IR26]]),
            P("aviation", "BOC Aviation, leasing & consumer finance", "Aircraft leasing through BOC Aviation, plus BOC Financial Leasing and BOC Consumer Finance.",
              s=["corp", "con"], lc="borrow", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26]]),
        ]},
        {"id": "4.5", "ic": "flag", "name": "BOCHK & Southeast Asia", "blurb": "HK$4.8trn, ROE 13.2%.", "div": "bochk", "rev": "other", "products": [
            P("bochk", "BOC Hong Kong (Holdings)", "Hong Kong-listed and controlled by BOC. HK$4.77 trillion of assets and HK$24.36 billion of profit in H1 2026, ROE 13.18%. Leads new residential mortgages and IPO receiving-bank business in Hong Kong. Its card arm issues on Visa, Mastercard and UnionPay.", short="BOCHK (Visa, Mastercard, UnionPay)",
              s=["hk"], lc="everyday", o="B", at="Visa, Mastercard, UnionPay", neo=[1, "Cards split three ways."],
              mc="Mastercard's clearest branded card at the group is BOCHK's Chill Card.",
              src=[["BOCHK 2026 interim results", HKIR26], ["BOCHK: credit card listing", HKLIST]]),
            P("seasia", "Southeast Asia entities", "BOCHK runs BOC's entities in Southeast Asia: RMB acquiring in Cambodia (a first), RMB clearing in Indonesia, CIPS links, and digital-channel volume up more than 30% in H1 2026 with UnionPay and WeChat QR codes.",
              s=["hk", "corp"], lc="move", st="new", o="B", at="UnionPay, WeChat", neo=[0, ""], src=[["2026 Interim Report", IR26], ["BOCHK 2026 interim results", HKIR26]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach BOC: mobile banking with 105 million monthly users and an international version in 31 countries, corporate online banking in 56, more than 10,000 outlets and 42,000 smart counters, and the wallets its cards link to, including BOCHK's BoC Pay+.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Mobile banking", "blurb": "105m monthly users.", "div": "boc", "rev": "personal", "products": [
            P("app", "BOC Mobile Banking", "313 million registered and 105 million monthly active customers at end-2025, its most active channel. Monthly users rose 6.86% in H1 2026. A 'Beautiful Countryside' version serves rural customers.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["2025 Annual Report", AR25], ["2026 Interim Report", IR26]]),
            P("intlapp", "BOC Mobile Banking (International)", "Available in 31 countries and regions in 12 languages (June 2026), with local features such as NAPAS transfers in Vietnam and e-wallet QR payments in Thailand.",
              s=["traveller", "hk"], lc="everyday", st="new", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Corporate online banking", "blurb": "56 countries, 15 languages.", "div": "boc", "rev": "corporate", "products": [
            P("corpapp", "Corporate online banking & iGTB", "Overseas corporate online banking in 56 countries and regions and 15 languages, with CIPS settlement and local interbank payments. RMB248.8 trillion of e-channel transactions in H1 2026.",
              s=["corp", "sme"], lc="everyday", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Outlets & ATMs", "blurb": "10,249 outlets.", "div": "boc", "rev": "personal", "products": [
            P("outlets", "Outlets, smart counters & ATMs", "10,249 commercial banking institutions in the mainland, 42,142 smart counters and 21,920 ATMs at 30 June 2026, with RMB758 billion of ATM transactions in the half.",
              s=["con", "visitor"], lc="open", o="B", neo=[0, ""], src=[["2026 Interim Report", IR26]]),
        ]},
        {"id": "5.4", "ic": "wallet", "name": "Wallets & platforms", "blurb": "WeChat Pay, Alipay, BoC Pay+.", "div": "boc", "rev": "personal", "products": [
            P("wallets", "Third-party wallets", "BOC cards, including the Great Wall Mastercard, link to WeChat Pay and Alipay, and BOC works with both on rewards for card binding.",
              s=["con"], lc="everyday", o="P", at="WeChat Pay, Alipay", neo=[1, "Mastercard cards can sit inside the wallets."],
              src=[["2025 Annual Report", AR25], ["Sina Finance, May 2024", SINA24]]),
            P("bocpay", "BoC Pay+ & BoC Bill", "BOCHK's wallet: users up 8.1% and RMB volume up 15.5% in H1 2026, with UnionPay's real-time FX and mainland UnionPay payments, and use on 12306, Ctrip and DiDi. BoC Bill acquiring volume rose 17.6%. An NFC-and-QR service for BOC UnionPay cards in Samsung Wallet was a first in Hong Kong.", short="BoC Pay+ (UnionPay)",
              s=["hk", "sme"], lc="move", st="new", o="B", at="UnionPay International", neo=[0, "UnionPay."],
              src=[["BOCHK 2026 interim results", HKIR26], ["2026 Interim Report", IR26]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at BOC", "blurb": "The first member, a small RMB line.", "products": [
        P("mcatboc", "Mastercard at Bank of China", "BOC was the first Chinese member of Mastercard (1987), and its 1988 Great Wall International Card, a Mastercard, was China's first international credit card. Today UnionPay carries most of its 750 million debit and 152 million credit cards ⚠. Since May 2024 BOC has issued Great Wall Mastercard RMB cards through Mastercard NetsUnion, added dual-application credit cards in 2025 and Mastercard RMB debit and Apple Pay in 2026. At BOCHK the Chill Card is Mastercard, while Visa holds the flagship Cheers and business cards.",
          s=["traveller"], div="boc", rev="personal", mc="The relationship this map is drawn for.",
          src=[["BOC: Bank Card Gallery", GALLERY], ["Sina Finance, May 2024", SINA24], ["2025 Annual Report", AR25], ["Mastercard: BOC Chill Card, Jun 2022", MCCHILL]]),
    ]},
    {"id": "pillar-market", "name": "China's payments", "blurb": "UnionPay, wallets, Visa arriving.", "products": [
        P("market", "The Chinese market", "State-controlled UnionPay dominates bank cards; bank cards handled 4.6 trillion transactions worth RMB963.6 trillion in 2025. WeChat Pay and Alipay lead everyday payments ⚠ (no share figures gathered). American Express (2020) and Mastercard NetsUnion (November 2023) hold clearing licences; on 13 October 2026 Visa won approval to prepare one.",
          s=["con"], div="boc", rev="other", src=[["BusinessDay (Reuters), Oct 2026", BDAY], ["Visa press release, Oct 2026", VISAPR], ["IT Home, Nov 2023", ITH23]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
