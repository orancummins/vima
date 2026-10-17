"""BCEL's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the 2025 Annual Report (uploaded 5 May 2026)
and the H1 2026 business-performance summary (31 August 2026). English sources are thin; BCEL publishes
no card counts by network. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own
product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

AR25 = "https://www.bcel.com.la/bcel/bcelweb-datas/financial-info/annual-rpt/en/bcel_web_file_41_c6bc8ffc9660865511b263b8fa4f3acd.pdf"
H126 = "https://www.bcel.com.la/bcel/bcelweb-datas/financial-info/half-year-rpt/en/bcel_web_file_25_5bf6102883ed8d6cc5f5c8c464901038.pdf"
HIST = "https://www.bcel.com.la/bcel/history.html?lang=en"
SHARE = "https://www.bcel.com.la/bcel/share-structure.html?lang=en"
CARDS = "https://www.bcel.com.la/bcel/product.html?prid=cards&lang=en"
WMC = "https://www.bcel.com.la/bcel/product-review.html?prd=cards&id=mastercard&lang=en"
VPMC = "https://www.bcel.com.la/bcel/product-review.html?prd=cards&id=Virtual&lang=en"
VPC = "https://www.bcel.com.la/bcel/product-review.html?prd=cards&id=VISA_Platinum2&lang=en"
VPD = "https://www.bcel.com.la/bcel/product-review.html?prd=cards&id=PlatinumDebit&lang=en"
VCORP = "https://www.bcel.com.la/bcel/product-review.html?prd=cards&id=visacorp&lang=en"
UPCARD = "https://www.bcel.com.la/bcel/product-review.html?prd=cards&id=unionpay&lang=en"
PAYCARD = "https://www.bcel.com.la/bcel/product-review.html?prd=cards&id=paycard&lang=en"
XBORDER = "https://www.bcel.com.la/bcel/product-review.html?prd=e-banking&id=crossborder&lang=en"
WECHAT = "https://www.bcel.com.la/bcel/product-review.html?prd=e-banking&id=wechat&lang=en"
IBANK = "https://www.bcel.com.la/bcel/product-review.html?prd=e-banking&id=ibank&lang=en"
ONECARE = "https://www.bcel.com.la/bcel/product-review.html?prd=e-banking&id=OneCare&lang=en"
FASTTRACK = "https://www.bcel.com.la/bcel/product-review.html?prd=e-banking&id=Fast_tract&lang=en"
ONEPROOF = "https://www.bcel.com.la/bcel/product-review.html?prd=e-banking&id=BCEL%20OneProof&lang=en"
LAPNETATM = "https://www.bcel.com.la/bcel/product-review.html?prd=atm&id=bconnex&lang=en"
INTLATM = "https://www.bcel.com.la/bcel/product-review.html?prd=atm&id=ATM%20service&lang=en"
ATM = "https://www.bcel.com.la/bcel/product-review.html?prd=atm&id=atm&lang=en"
BCOME = "https://www.bcel.com.la/bcel/product-review.html?prd=ft&id=bcome&lang=en"
MG = "https://www.bcel.com.la/bcel/product-review.html?prd=ft&id=mg&lang=en"
GLN = "https://www.bcel.com.la/bcel/product-review.html?prd=ft&id=GLN&lang=en"
FT = "https://www.bcel.com.la/bcel/product.html?prid=ft&lang=en"
PROMO = "https://www.bcel.com.la/bcel/promotion-review-card.html?pmt=cards&id=bcel-card&type=all&lang=en"
SME3 = "https://www.bcel.com.la/bcel/product-review.html?prd=credits&id=SME3percent&lang=en"
OCEANBASE = "https://www.bcel.com.la/bcel/bcel-news-details.html?fid=1480&fType=bcel-news&type=news&lang=en"
AGM26 = "https://www.bcel.com.la/bcel/bcel-news-details.html?fid=1432&fType=bcel-news&type=news&lang=en"
EDL = "https://www.bcel.com.la/bcel/bcel-news-details.html?fid=1425&fType=bcel-news&type=news&lang=en"
VISAPLAT = "https://www.bcel.com.la/bcel/bcelweb-datas/file-path/bcel-news/en/bcel_web_file_321_c06a2c9d0f5ee5791e1a653cd694b93f.pdf"
WECHATPR = "https://www.bcel.com.la/bcel/bcelweb-datas/file-path/bcel-news/en/bcel_web_file_151_e823b68c1b596a81c26e2a8c5148e14d.pdf"
UPQRPR = "https://www.bcel.com.la/bcel/bcelweb-datas/file-path/bcel-news/en/bcel_web_file_145_801ddbf026414af73f58eb70669ad8b6.pdf"
THANACHART = "https://www.bcel.com.la/bcel/bcelweb-datas/file-path/bcel-news/en/bcel_web_file_109_57d98e937c697ac3118f768ab35c8643.pdf"
WMC19 = "https://laos.opendevelopmentmekong.net/news/bcel-launches-world-mastercard-credit-card-prepaid-mastercard/"
UPI19 = "https://unionpayintl.com/en/mediaCenter/newsCenter/companyNews/5474.shtml"
UPI24 = "https://www.unionpayintl.com/lao/mediaCenter/newsCenter/companyNews/3015950.shtml"
UPLAPNET = "https://www.tourismlaos.org/2025/01/17/laos-china-launch-qr-payment-system-for-cashless-tourism/"
NAPAS = "https://vietnamnews.vn/economy/1690482/seven-banks-allow-customers-to-pay-by-qr-codes-in-laos.html"
MMONEYLAPNET = "https://www.vientianetimes.org.la/freefreenews/freecontent_125_Mmoney_y25.php"
MMONEYVISA = "https://vientianetimes.org.la/freefreenews/freecontent_65_Mmoney_y26.php"
JCB15 = "https://en.vietstock.vn/2015/05/bcel-jcb-launch-joint-credit-card-58-203222.htm"
UP11 = "https://en.vietstock.vn/2011/08/bcellaunches-latest-product-1148-112051.htm"
CARDS17 = "https://en.vietstock.vn/2017/04/bcel-takes-lions-share-of-electronic-card-products-143-258207.htm"
EZYKIP = "https://www.tourismlaos.org/2024/02/16/bcel-launches-new-payment-app-for-tourists-during-visit-laos-year-2024/"
GLN22 = "https://www.tourismlaos.org/2022/12/27/laos-south-korea-allow-qr-payments-for-travelers/"
SBV25 = "https://tapchinganhang.gov.vn/hien-dai-hoa-dich-vu-giao-dich-ngoai-te-tai-ngan-hang-ngoai-thuong-lao-trong-boi-canh-chuyen-doi-so-16643.html"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · state · listing", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: LAK 161 trillion of assets and record 2025 profit, the state's 60% and BRED's 10%, roots in 1975 as Laos's foreign-trade bank, a stake in the national switch, and a 2025–29 plan to become a full digital bank.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "Profit doubled in 2025.", "div": "bcel", "rev": "group", "products": [
            P("balance", "Balance sheet & earnings", "Total assets of LAK 160.8 trillion, deposits of LAK 150.8 trillion and loans of LAK 69.5 trillion at the end of 2025; net profit of LAK 932.5 billion (2024: LAK 449.6 billion), ROE 20.3%, NPL 2.76%, CAR 10.2%. In H1 2026, assets reached LAK 166.4 trillion and net profit LAK 625 billion, up 97%. No credit rating found ⚠.",
              s=["corp"], neo=[0, ""], src=[["Annual Report 2025", AR25], ["H1 2026 business performance", H126]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Ownership & leadership", "blurb": "State 60%, BRED 10%.", "div": "bcel", "rev": "group", "products": [
            P("owners", "Ownership & listing", "The first company on the Lao Securities Exchange (2010–11). Ministry of Finance 60%, COFIBRED (BRED Banque Populaire) 10% since July 2011, other investors 30%. A 1:5 share split (February 2025) and a LAK 841.9 billion share offering (October 2025) took the share count to 1.545 billion; at the 2025 average price that is about LAK 1.9 trillion of market value ⚠ (estimate).",
              s=["corp"], ay="Jan 2011", o="I", neo=[0, ""], src=[["BCEL: share structure", SHARE], ["Annual Report 2025", AR25]]),
            P("leadership", "Board & management", "Chairman Soulivath Souvannachoumkham (Ministry of Finance), Vice Chairman Bounta Daravy; Managing Director Saysamone Chanthachack since August 2022, with six deputy MDs, among them Nanthalath Keopaseuth, a former head of BCEL's card centre who signs most payments deals.",
              s=["corp"], neo=[0, ""], src=[["H1 2026 business performance", H126], ["Annual Report 2025", AR25]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & group", "blurb": "Since 1975; seven JVs.", "div": "jv", "rev": "group", "products": [
            P("heritage", "Heritage", "Began in 1975 as the State Bank's international-settlement arm and Laos's only foreign-trade bank until 1989, when it became a state-owned commercial bank. Brand colours red, blue and the yellow Cassia flower; slogan Modern Quick Reliable.",
              s=["con"], ay="1975", o="I", neo=[0, ""], src=[["BCEL: about BCEL", HIST], ["Annual Report 2025", AR25]]),
            P("jvs", "Associates & joint ventures", "Lao-Viet Bank (25%, with BIDV), Lao-Viet Insurance (35%), Banque Franco-Lao (30%, sale approved ⚠ not confirmed complete), BCEL-KT Securities (70%), Lao China Bank (39.9%), Lao Foreign Exchange (10%) and 20% of LAPNet, the national payment switch, alongside the Bank of the Lao PDR (25%) and UnionPay International (15%).",
              s=["corp"], st="flux", o="P", at="BIDV, BRED, Fudian, UnionPay", neo=[0, ""],
              mc="UnionPay owns 15% of the national switch; Mastercard has no stake.",
              src=[["Annual Report 2025", AR25], ["BCEL AGM, 30 Apr 2026", AGM26]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Technology & strategy", "blurb": "A digital bank by 2029.", "div": "bcel", "rev": "group", "products": [
            P("strategy", "Strategic Development Plan 2025–2029", "Fifteen work plans and 50 projects: eight to move to full digital banking, six on IT, four on data, Basel II, IFRS and ISO 9001. 2026 targets: net profit up 10% and NPLs no higher than 3%, with more aggressive marketing and products with domestic and international connectivity.",
              s=["corp"], st="new", ay="2025", neo=[0, ""], src=[["Annual Report 2025", AR25]]),
            P("core", "Core banking on OceanBase", "A memorandum with OceanBase (20 August 2026) to move the core onto a distributed database after a 2026 proof of concept with OceanBase and HiSun, for faster end-of-day runs and round-the-clock service. AI: nothing public ⚠.",
              s=["corp"], st="new", ay="Aug 2026", o="P", at="OceanBase, HiSun", neo=[0, ""], src=[["BCEL: OceanBase MoU, Aug 2026", OCEANBASE]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Nine ways money moves: UnionPay debit for the mass market, Visa for premium and corporate cards, a World Mastercard and a virtual prepaid Mastercard, JCB credit, acquiring for every network, OnePay QR, LAPNet and LAO QR, cross-border QR and remittances, and the EZyKip tourist wallet.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "UnionPay debit", "blurb": "The mass-market card.", "div": "cards", "rev": "retail", "products": [
            P("updebit", "BCEL UnionPay cards", "BCEL's ATM and debit cards (Standard, Carbon, Gold), on UnionPay since July 2011, linking LAK, THB and USD accounts. UnionPay said eight in ten Lao bank cards carried its brand in 2019; BCEL had 499,245 debit cardholders at the end of 2016.", short="UnionPay debit",
              s=["con", "rural"], lc="everyday", ay="Jul 2011", o="P", at="UnionPay", neo=[0, "UnionPay."],
              mc="The biggest card base at BCEL sits on UnionPay.",
              src=[["BCEL: UnionPay cards", UPCARD], ["Vietstock: UnionPay card, Aug 2011", UP11], ["UnionPay: QR in Laos, Jul 2019", UPI19], ["Vietstock: BCEL cards, Apr 2017", CARDS17]]),
            P("upvirtual", "ATM UnionPay Virtual Card", "A virtual UnionPay card in BCEL One, launched in 2025.",
              s=["con"], lc="everyday", st="new", ay="2025", o="P", at="UnionPay", neo=[0, "UnionPay."], src=[["Annual Report 2025", AR25]]),
            P("govcards", "Student, payroll & tax cards", "Chip ATM cards for students, civil servants and payroll (Pay Card for workers without a fixed address), plus Smart Tax and Smart VAT cards ⚠ network assumed UnionPay from the catalogue.",
              s=["con", "corp"], lc="everyday", o="P", at="UnionPay", neo=[0, "UnionPay ⚠."], src=[["BCEL: cards", CARDS], ["BCEL: Pay Card", PAYCARD]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Visa cards", "blurb": "Premium and corporate.", "div": "cards", "rev": "retail", "products": [
            P("visacredit", "BCEL Visa credit & Visa Platinum Credit", "Visa credit since 2010, with BCEL calling itself Laos's leading Visa issuer; Visa Platinum Credit (November 2021) has limits up to US$100,000, 45 days interest-free, contactless and lounge access. 11,574 Visa cards at the end of 2016.", short="Visa credit",
              s=["con", "trav"], lc="borrow", ay="Nov 2021", o="P", at="Visa", neo=[0, "Visa."],
              src=[["BCEL: Visa Platinum launch, Nov 2021", VISAPLAT], ["BCEL: Visa Platinum Credit", VPC], ["Vietstock: BCEL cards, Apr 2017", CARDS17]]),
            P("visadebit", "BCEL Visa Platinum Debit", "An international contactless debit card (November 2021) for up to US$5,000 a day at home and US$10,000 abroad; the only non-UnionPay debit card in the catalogue.",
              s=["con", "trav"], lc="everyday", ay="Nov 2021", o="P", at="Visa", neo=[0, "Visa."], src=[["BCEL: Visa Platinum Debit", VPD], ["BCEL: Visa Platinum launch, Nov 2021", VISAPLAT]]),
            P("visacorp", "BCEL Visa Corporate Card", "Billed as the first corporate credit card in Laos: limits of US$50,000 or more, 3-D Secure and lounge access ⚠ launch date not published.",
              s=["corp"], lc="move", o="P", at="Visa", neo=[0, "Visa."],
              mc="The only commercial card at BCEL is Visa's.",
              src=[["BCEL: Visa Corporate Card", VCORP]]),
        ]},
        {"id": "2.3", "ic": "gem", "name": "Mastercard cards", "blurb": "World and virtual prepaid.", "div": "cards", "rev": "retail", "products": [
            P("wmc", "BCEL World Mastercard", "A travel credit card with free overseas travel insurance (medical cover to US$100,000) and two free LoungeKey visits a year through the Mastercard Airport Experience app; launched in April 2019 with a prepaid Mastercard. Can share a credit limit with BCEL's Visa and JCB cards.", short="World Mastercard",
              s=["con", "trav"], lc="borrow", ay="Apr 2019", o="P", at="Mastercard", neo=[2, "Mastercard credit."],
              mc="Mastercard's one premium card at BCEL.",
              src=[["BCEL: World Mastercard", WMC], ["Vientiane Times via Open Development Laos, Apr 2019", WMC19], ["BCEL: Visa Platinum Credit", VPC]]),
            P("vpmc", "BCEL Virtual Prepaid Mastercard", "A top-up virtual card applied for online and shown in BCEL One, with US$10–5,000 a day of top-ups, no annual fee and online spending up to US$5,000 a day abroad ⚠ date of the virtual version unknown.", short="Virtual Prepaid Mastercard",
              s=["con", "trav"], lc="move", o="P", at="Mastercard", neo=[2, "Mastercard prepaid."],
              src=[["BCEL: Virtual Prepaid Mastercard", VPMC]]),
        ]},
        {"id": "2.4", "ic": "credit-card", "name": "JCB & co-brand credit", "blurb": "JCB since 2015.", "div": "cards", "rev": "retail", "products": [
            P("jcb", "BCEL-JCB & co-brand credit", "The BCEL-JCB credit card (May 2015; BCEL the second JCB issuer in Laos) and a UnionPay co-brand credit card ⚠ current status of both not confirmed; both can share a limit with Visa Platinum.",
              s=["con"], lc="borrow", ay="May 2015", o="P", at="JCB, UnionPay", neo=[0, "JCB and UnionPay."], src=[["Vietstock: BCEL-JCB card, May 2015", JCB15], ["BCEL: UnionPay QR launch, Sep 2019", UPQRPR], ["BCEL: Visa Platinum Credit", VPC]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acquiring & acceptance", "blurb": "Every network accepted.", "div": "cards", "rev": "retail", "products": [
            P("acquiring", "Card acquiring, ATMs & payment gateway", "Visa acquirer since 2010 and the first Lao bank allowed to take e-commerce payments; EDC terminals (1,790 at the end of 2016), UnionPay POS nationwide; BCEL ATMs take Visa, Mastercard, Maestro, Cirrus, Diners Club, JCB and UnionPay ⚠ Mastercard POS acquiring implied, not stated.", short="Acquiring",
              s=["merch", "trav"], lc="move", o="P", at="Visa, Mastercard, UnionPay, JCB", neo=[1, "Takes Mastercard at ATMs ⚠ POS."],
              src=[["BCEL: Visa Platinum launch, Nov 2021", VISAPLAT], ["BCEL: international cards at ATMs", INTLATM], ["Vietstock: BCEL cards, Apr 2017", CARDS17], ["BCEL: UnionPay QR launch, Sep 2019", UPQRPR]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "OnePay QR", "blurb": "Laos's first QR payments.", "div": "onepay", "rev": "retail", "products": [
            P("onepay", "BCEL OnePay & OnePay Shop", "QR payment inside BCEL One, which BCEL says brought QR payments to Laos; more than 10,000 OnePay merchants by October 2019 ⚠ no later count; OnePay Shop added in 2025.", short="OnePay",
              s=["con", "merch"], lc="move", o="B", neo=[0, "BCEL's own QR."],
              mc="QR, not cards, is how most Lao merchants get paid.",
              src=[["BCEL: WeChat Pay and Alipay, Oct 2019", WECHATPR], ["Annual Report 2025", AR25]]),
            P("chinaqr", "UnionPay QR, WeChat Pay & Alipay acceptance", "The first UnionPay QR acceptance in Laos (13 September 2019) and WeChat Pay and Alipay at OnePay merchants with Swift Pass and NTT Data (11 October 2019; 2.5% fee).",
              s=["merch", "trav"], lc="move", ay="Sep 2019", o="P", at="UnionPay, Swift Pass, NTT Data", neo=[0, "UnionPay and Chinese wallets."],
              src=[["BCEL: UnionPay QR launch, Sep 2019", UPQRPR], ["BCEL: WeChat Pay and Alipay, Oct 2019", WECHATPR], ["BCEL: WeChat Pay & Alipay", WECHAT]]),
        ]},
        {"id": "2.7", "ic": "network", "name": "LAPNet & LAO QR", "blurb": "BCEL owns 20%.", "div": "lapnet", "rev": "group", "products": [
            P("lapnet", "LAPNet switch", "The national payment network built by the Bank of the Lao PDR, 20% owned by BCEL and 15% by UnionPay International: shared ATMs across 14 member banks and interbank transfers; M moneyX became the first e-wallet member in July 2025; BCEL won LAPNet's service-quality award for 2025.", short="LAPNet",
              s=["con", "rural"], lc="move", o="P", at="Bank of the Lao PDR, UnionPay", neo=[0, "Domestic switch; UnionPay a shareholder."],
              src=[["Annual Report 2025", AR25], ["BCEL: LAPNet", LAPNETATM], ["Vientiane Times: M moneyX joins LAPNet, Jul 2025", MMONEYLAPNET]]),
            P("laoqr", "LAO QR", "The national QR standard run through LAPNet and accepted in stores across Laos; OnePay merchants are part of it ⚠ inferred from LAPNet's cross-border links.", short="LAO QR",
              s=["con", "merch"], lc="move", o="P", at="LAPNet", neo=[0, "National QR."], src=[["Vientiane Times: M moneyX joins LAPNet, Jul 2025", MMONEYLAPNET], ["Tourism Laos: Laos-China QR, Jan 2025", UPLAPNET]]),
        ]},
        {"id": "2.8", "ic": "earth", "name": "Cross-border & remittances", "blurb": "QR links to four neighbours.", "div": "bcelone", "rev": "treasury", "products": [
            P("thqr", "OnePay in Thailand", "BCEL One users scan Thai PromptPay QR codes at merchants of Bangkok Bank, Krungsri, Kasikorn and Krungthai; first agreed with Thanachart in March 2018.",
              s=["con", "trav"], lc="move", ay="Mar 2018", o="P", at="PromptPay banks", neo=[0, "QR link."], src=[["BCEL: cross-border payment", XBORDER], ["BCEL: Thanachart QR, Mar 2018", THANACHART]]),
            P("xqr", "LAPNet QR links: China, Vietnam, Cambodia", "UnionPay app users pay at LAO QR merchants of eight banks including BCEL (December 2024); Vietnamese customers of seven banks pay at 14 Lao banks through NAPAS (January 2025); a Cambodia link since August 2023 ⚠.",
              s=["trav", "merch"], lc="move", st="new", ay="Dec 2024", o="P", at="UnionPay, NAPAS", neo=[0, "UnionPay and national QR."],
              mc="Cross-border QR is being built without the card schemes, except UnionPay.",
              src=[["Tourism Laos: Laos-China QR, Jan 2025", UPLAPNET], ["UnionPay: LAPNet and PayNet, Nov 2024", UPI24], ["Vietnam News: Laos QR, Jan 2025", NAPAS]]),
            P("gln", "GLN Korea link", "GLN wallet users pay at OnePay merchants and withdraw at BCEL ATMs (December 2022); Koreans can send up to US$5,000 a time into BCEL One for about US$4.",
              s=["remit", "trav"], lc="move", ay="Dec 2022", o="P", at="GLN International", neo=[0, ""], src=[["Tourism Laos: GLN QR, Dec 2022", GLN22], ["BCEL: GLN remittance", GLN]]),
            P("moneygram", "MoneyGram & international transfers", "MoneyGram in BCEL One to and from 200+ countries, 23 more MoneyGram agents in 2025, SWIFT transfers with a JPMorgan straight-through-processing award (2025) and CNY transfers through the Border Trade E-Bank.", short="MoneyGram & SWIFT",
              s=["remit"], lc="move", o="P", at="MoneyGram", neo=[0, ""],
              mc="Remittances run on MoneyGram and SWIFT; no Mastercard Move.",
              src=[["BCEL: MoneyGram", MG], ["Annual Report 2025", AR25], ["BCEL: fund transfers", FT]]),
        ]},
        {"id": "2.9", "ic": "wallet", "name": "Tourist wallet", "blurb": "EZyKip for visitors.", "div": "bcelone", "rev": "retail", "products": [
            P("ezykip", "EZyKip", "A wallet for foreign visitors without a Lao account (late January 2024): QR cash withdrawals at BCEL ATMs with no fee and payment at OnePay and LAO QR stores, with card top-ups from UnionPay, Visa, Mastercard, JCB, Amex, Alipay and WeChat Pay planned ⚠ status unknown.",
              s=["trav"], lc="move", ay="Jan 2024", o="B", neo=[None, "Mastercard top-ups planned ⚠."],
              mc="A ready-made place for Mastercard tourist top-ups.",
              src=[["Tourism Laos: EZyKip, Feb 2024", EZYKIP]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: an app to spot fake payment slips and a PCI DSS project, remote onboarding and OneCare, billers and partners plugged into BCEL One, and card discounts, a Mastercard campaign and a donations platform.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "Fake slips, PCI DSS.", "div": "bcel", "rev": "retail", "products": [
            P("oneproof", "BCEL OneProof", "An app that scans the QR on an e-slip to show whether a OnePay payment really happened, against fake transfer slips.",
              s=["merch"], lc="everyday", o="B", neo=[0, "BCEL's own."], src=[["BCEL: OneProof", ONEPROOF]]),
            P("pci", "Card security & PCI DSS", "A PCI DSS compliance project in the 2025–29 plan, 3-D Secure on cards and cybersecurity to international standards; no network fraud tools disclosed ⚠.",
              s=["con", "corp"], lc="everyday", st="new", neo=[None, "Nothing public."],
              mc="Tokenisation and scheme risk scoring are untouched ground.",
              src=[["Annual Report 2025", AR25], ["BCEL: Visa Corporate Card", VCORP]]),
        ]},
        {"id": "3.2", "ic": "fingerprint", "name": "Onboarding & care", "blurb": "Open an account in the app.", "div": "bcelone", "rev": "retail", "products": [
            P("onboard", "Online account opening", "Self-service opening of deposit accounts in BCEL One, launched in H1 2026, with face and document checks.",
              s=["con"], lc="open", st="new", ay="2026", o="B", neo=[0, ""], src=[["H1 2026 business performance", H126], ["BCEL: OneCare", ONECARE]]),
            P("onecare", "BCEL OneCare & 1555", "In-app help that blocks and unblocks cards, resets PINs, links accounts and issues new cards without a branch visit, plus the 1555 call centre.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["BCEL: OneCare", ONECARE]]),
        ]},
        {"id": "3.3", "ic": "plug", "name": "Partners & billers", "blurb": "EDL, gold, insurance.", "div": "bcelone", "rev": "retail", "products": [
            P("edl", "EDL auto-debit", "An agreement with Électricité du Laos (April 2026) to pay electricity bills by automatic debit from BCEL One.",
              s=["con"], lc="everyday", st="new", ay="Apr 2026", o="P", at="EDL", neo=[0, ""], src=[["BCEL: EDL agreement, Apr 2026", EDL], ["H1 2026 business performance", H126]]),
            P("partners", "Gold, insurance & government links", "Gold trading and settlement with Lao Bullion Bank, insurance sales with AGL Laos, the Ministry of Finance's Finlink (Smart Cash) and the Bank of the Lao PDR's CMS, all wired up in 2025.",
              s=["con", "corp"], lc="grow", st="new", ay="2025", o="P", at="Lao Bullion Bank, AGL", neo=[0, ""], src=[["Annual Report 2025", AR25]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Loyalty & community", "blurb": "Discounts, campaigns, giving.", "div": "cards", "rev": "retail", "products": [
            P("offers", "BCEL Card discounts", "5–10% off at restaurants, hotels, clinics and stores for any BCEL card, some also for QR; a BCEL Exclusive Shopping Experience with Siam Piwat in Thailand (Q2 2026).",
              s=["con"], lc="beyond", o="B", neo=[1, "All BCEL cards, Mastercard among them."],
              mc="Merchant offers are BCEL's own; card-linked offers could scale them.",
              src=[["BCEL: card promotions", PROMO], ["H1 2026 business performance", H126]]),
            P("mccampaign", "Mastercard Campaign 2025", "A Mastercard cardholder campaign with a live lucky draw for its winners in Q2 2026.",
              s=["con"], lc="beyond", st="new", ay="2025", o="P", at="Mastercard", neo=[2, "Mastercard card campaign."], src=[["H1 2026 business performance", H126]]),
            P("oneheart", "BCEL One Heart", "A donations platform in the app: LAK 472 million from more than 4,900 donations to 26 projects in H1 2026, after LAK 300.6 million in 2025.",
              s=["con"], lc="beyond", o="B", neo=[0, ""], src=[["H1 2026 business performance", H126], ["Annual Report 2025", AR25]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: LAK 151 trillion of deposits, mostly savings; loans that go 61% to industry, plus 3% SME credit; FX, trade finance and securities; and payroll and tax payments for the state.",
    "tiles": [
        {"id": "4.1", "ic": "coins", "name": "Deposits", "blurb": "LAK 151 trillion.", "div": "bcel", "rev": "retail", "products": [
            P("deposits", "Savings, current & term deposits", "LAK 150.8 trillion at the end of 2025 (savings 59%, term 24%, current 13%) in kip, dollars and baht, including OneBank and OneBank Kid accounts (2025); LAK 155.4 trillion at 30 June 2026.",
              s=["con", "rural"], lc="grow", o="B", neo=[0, "UnionPay debit."], src=[["Annual Report 2025", AR25], ["H1 2026 business performance", H126]]),
        ]},
        {"id": "4.2", "ic": "building-2", "name": "Lending", "blurb": "Industry 61%; SMEs at 3%.", "div": "bcel", "rev": "corporate", "products": [
            P("corplend", "Corporate lending", "Loans of LAK 69.5 trillion at the end of 2025: industry 61%, trade 14%, construction 11%; credit-loss charges of LAK 2.9 trillion in 2025; LAK 67.7 trillion and NPL 2.06% at 30 June 2026.",
              s=["corp"], lc="borrow", o="B", neo=[0, ""], src=[["Annual Report 2025", AR25], ["H1 2026 business performance", H126]]),
            P("sme3", "SME, home & consumer loans", "SME loans at 3% a year for up to 10 years and LAK 5 billion, for manufacturers, agricultural exporters and tourism, alongside home and consumer loans.",
              s=["merch", "con"], lc="borrow", o="B", neo=[0, ""], src=[["BCEL: SME 3% loans", SME3]]),
        ]},
        {"id": "4.3", "ic": "chart-candlestick", "name": "Treasury, FX & securities", "blurb": "FX, trade, BCEL-KT.", "div": "jv", "rev": "treasury", "products": [
            P("tradefx", "FX, trade finance & money changers", "Letters of credit, guarantees, FX (LAK 356.7 billion of FX income in 2025) and nine money changers at airports and Thai border bridges; digital FX customers grew from 45,000 in 2020 to 160,000 in 2024 ⚠ (State Bank of Vietnam journal).",
              s=["corp", "trav"], lc="move", o="B", neo=[0, ""], src=[["Annual Report 2025", AR25], ["SBV journal: BCEL FX, Oct 2025", SBV25]]),
            P("securities", "BCEL-KT Securities & share trading", "BCEL-KT Securities (70%, with KTZMICO) and share trading in BCEL One from 2025; BCEL won seven Lao Securities Exchange awards for 2025.",
              s=["con", "corp"], lc="grow", st="new", o="P", at="KTZMICO", neo=[0, ""], src=[["Annual Report 2025", AR25]]),
        ]},
        {"id": "4.4", "ic": "receipt-text", "name": "Government & payroll", "blurb": "Payroll, tax, bills.", "div": "bcel", "rev": "corporate", "products": [
            P("payroll", "Payroll & cash management", "Self-service payroll in i-Bank, pay cards for workers without accounts and civil-servant cards.",
              s=["corp"], lc="everyday", o="B", neo=[0, "UnionPay pay cards ⚠."], src=[["BCEL: i-Bank", IBANK], ["BCEL: Pay Card", PAYCARD]]),
            P("taxpay", "Tax & bill payments", "Smart Tax, Smart VAT and road-tax payments, and water, electricity, telecom and TV bills through the app, i-Bank, ATMs and BCOME.",
              s=["con", "corp"], lc="everyday", o="B", neo=[0, ""], src=[["BCEL: cards", CARDS], ["BCEL: i-Bank", IBANK], ["BCEL: BCOME", BCOME]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: BCEL One for about 1.4 million users and i-Bank, 21 branches and 101 service units with ATMs, and 734 BCOME agents in villages.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "BCEL One & i-Bank", "blurb": "About 1.4m app users.", "div": "bcelone", "rev": "retail", "products": [
            P("bcelone", "BCEL One", "The app for payments, OnePay, card controls, the virtual prepaid Mastercard, MoneyGram, share and gold trading, and FastTrack pre-ordered cash; over 1.4 million users and 2.5 million e-banking users at the end of 2024, with digital channels above 73% of transactions ⚠ (State Bank of Vietnam journal).", short="BCEL One",
              s=["con", "remit", "merch"], lc="everyday", o="B", neo=[1, "Hosts the Virtual Prepaid Mastercard."],
              mc="The channel any new Mastercard product would ride.",
              src=[["SBV journal: BCEL FX, Oct 2025", SBV25], ["BCEL: FastTrack", FASTTRACK], ["BCEL: Virtual Prepaid Mastercard", VPMC]]),
            P("ibank", "BCEL i-Bank", "Internet banking for companies and individuals: payroll, bill and tax payments, transfers to banks at home and abroad, OTP tokens; now on version 3.",
              s=["corp"], lc="everyday", o="B", neo=[0, ""], src=[["BCEL: i-Bank", IBANK]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "21 branches, 101 units.", "div": "bcel", "rev": "retail", "products": [
            P("branches", "Branches, service units & van", "21 branches, 101 service units and 9 money changers across all provinces (31 March 2026), and a mobile banking van.",
              s=["con", "corp"], lc="open", o="B", neo=[0, ""], src=[["H1 2026 business performance", H126], ["Annual Report 2025", AR25]]),
            P("atms", "ATMs & deposit machines", "287 ATMs on BCEL's ATM page against more than 400 cited at the EZyKip launch ⚠, deposit machines, and multi-currency ATMs paying yuan and baht (2025); they accept Mastercard, Maestro and Cirrus among seven networks.",
              s=["con", "trav"], lc="everyday", o="B", neo=[1, "Accept Mastercard cards."], src=[["BCEL: ATMs", ATM], ["Tourism Laos: EZyKip, Feb 2024", EZYKIP], ["BCEL: international cards at ATMs", INTLATM]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "BCOME agents", "blurb": "734 village agents.", "div": "bcome", "rev": "retail", "products": [
            P("bcome", "BCEL Community Money Express (BCOME)", "Agent banking at 734 shops (end-2025, 176 added in 2025, two super agents): open an ATM card, deposit, withdraw, send cash and pay bills and road tax.",
              s=["rural", "remit"], lc="open", o="B", neo=[0, ""], src=[["Annual Report 2025", AR25], ["BCEL: BCOME", BCOME]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at BCEL", "blurb": "One premium card, a prepaid one.", "products": [
        P("mcatbcel", "Mastercard at BCEL", "UnionPay carries BCEL's mass debit cards and owns 15% of LAPNet; Visa carries the premium, debit and corporate cards and BCEL's acquiring since 2010. Mastercard has the World Mastercard credit card and a prepaid Mastercard (both April 2019), the virtual prepaid card in BCEL One, ATM acceptance and a 2025 cardholder campaign.",
          s=["con"], div="cards", rev="retail", mc="The relationship this map is drawn for.",
          src=[["BCEL: World Mastercard", WMC], ["BCEL: Visa Platinum launch, Nov 2021", VISAPLAT], ["UnionPay: QR in Laos, Jul 2019", UPI19]]),
    ]},
    {"id": "pillar-market", "name": "Lao banking", "blurb": "QR, kip, state banks.", "products": [
        P("market", "The Lao market", "36 commercial banks, with state-owned banks holding about 32% of assets and 37% of deposits (December 2025); inflation of 7.4% in June 2026 and a weak kip; LAO QR linked to Thailand, Cambodia, Vietnam and China; Visa backing a prepaid card from the M moneyX wallet (April 2026).",
          s=["con"], div="bcel", rev="group", src=[["Annual Report 2025", AR25], ["H1 2026 business performance", H126], ["Vientiane Times: M moneyX Visa card, Apr 2026", MMONEYVISA]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
