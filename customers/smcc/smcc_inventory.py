"""Sumitomo Mitsui Card's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are SMBC Group's own unless a source says otherwise: the FY3/26 results presentation and data book (May 2026)
and the 1Q FY3/27 overview (31 July 2026). SMCC's own website could not be read, so card brands per product rest partly
on Japanese Wikipedia and consumer sites (marked ⚠). ``neo`` is the Mastercard lens: [depth, note], where 3 =
Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

FYPPT = "https://www.smfg.co.jp/english/investor/financial/latest_statement/2026_3/2026_fy_e_pre.pdf"
DATABOOK = "https://www.smfg.co.jp/english/investor/financial/latest_statement/2026_3/2026_fy_e_databook.pdf"
Q1 = "https://www.smfg.co.jp/english/investor/financial/latest_statement/2027_3/2027_1q_e03.pdf"
WIKI = "https://ja.wikipedia.org/wiki/%E4%B8%89%E4%BA%95%E4%BD%8F%E5%8F%8B%E3%82%AB%E3%83%BC%E3%83%89"
PRES = "https://paymentnavi.com/?p=171773"
MYNAVI = "https://job.mynavi.jp/27/pc/search/corp2008/outline.html"
VPOINT = "https://www.ccc.co.jp/en/news/press/20260401_008677.html"
OLIVE = "https://www.smfg.co.jp/news/pdf/j20230301_02.pdf"
NANKAI = "https://www.nankai.co.jp/lib/groupinfo/news/pdf/260212.pdf"
SENDAI = "https://www.77card.co.jp/pdf/260304_news.pdf"
JRK = "https://dxmagazine.jp/news/2602ukre22/"
STERA = "https://paymentnavi.com/paymentnews/142949.html"
CLOVER = "https://mondovisione.com/media-and-resources/news/fiserv-and-sumitomo-mitsui-introduce-clover-suite-of-products-enabling-digital-2026121/"
PAYPAY = "https://www.softbank.jp/sbnews/entry/20250519_02"
EXPO = "https://www.smfg.co.jp/news/pdf/j20231023_01.pdf"
AMZ14 = "https://paymentnavi.com/?p=37622"
AMZ21 = "https://nlab.itmedia.co.jp/fav/articles/3916478/"
NLBI = "https://www.businessinsider.jp/article/2504-mitsui-sumitomo-card-nl-visa-or-mastercard-which-is-better/"
VAR = "https://paymentnavi.com/?p=174182"
MCAG = "https://paymentnavi.com/?p=174963"
CAMP = "https://paymentnavi.com/?p=178836"
CASHLESS = "https://www.watch.impress.co.jp/docs/news/2099068.html"
SCBRI = "https://www.scbri.jp/reports/.assets/newstopics_20260403.pdf"
FRAUD = "https://ecnomikata.com/ecnews/marketing/49820/"
PAYPAYU = "https://about.paypay.ne.jp/en/pr/20260810/01/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "volume · ownership · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: 43 million card holders and ¥42 trillion of shopping a year, a company wholly owned by SMBC Group that has absorbed the group's other card and loan firms, Japan's first Visa issuer since 1980, and a group plan built on Olive and Trunk.",
    "tiles": [
        {"id": "1.1", "ic": "chart-column", "name": "Scale & results", "blurb": "43.35 million card holders.", "div": "smcc", "rev": "card", "products": [
            P("scale", "Cards & volume", "43.35 million card holders at March 2026, up from 33.16 million in March 2023; shopping sales handled of ¥41.95 trillion in FY3/26, up from ¥30.18 trillion three years earlier, and ¥10.1 trillion in 1Q FY3/27.",
              s=["con"], neo=[0, ""], src=[["SMFG FY3/26 data book", DATABOOK], ["SMFG 1Q FY3/27 overview, Jul 2026", Q1]]),
            P("results", "Earnings", "With SMBC Consumer Finance: operating revenue ¥1,034.7 billion and net income ¥105.7 billion in FY3/26, after a ¥64.3 billion loss in FY3/25 caused by a ¥141.5 billion allowance for interest refunds; 1Q FY3/27 operating revenue ¥271.9 billion and net income ¥14.5 billion.",
              s=["corp"], neo=[0, ""], src=[["SMFG FY3/26 presentation", FYPPT], ["SMFG 1Q FY3/27 overview, Jul 2026", Q1]]),
            P("rank", "Market position", "Japanese credit card payments were ¥134.6 trillion in 2025, so SMCC's shopping volume is about 30% of the market ⚠ (different periods and definitions; this map's arithmetic). Rakuten Card also claims first place on its own basis ⚠.",
              s=["con"], neo=[0, ""], src=[["SCBRI: 2025 cashless mix", SCBRI], ["SMFG FY3/26 data book", DATABOOK]]),
        ]},
        {"id": "1.2", "ic": "building-2", "name": "Ownership & group", "blurb": "100% SMBC Group.", "div": "smfg", "rev": "card", "products": [
            P("smfgown", "SMBC Group ownership", "Wholly owned by Sumitomo Mitsui Financial Group; a direct subsidiary again from April 2019, when SMFG bought out NTT Docomo's 34% stake ⚠. Unlisted; registered head office in Osaka, Tokyo head office at SMBC Toyosu Building.",
              s=["corp"], o="I", neo=[0, ""], src=[["Japanese Wikipedia: SMCC ⚠", WIKI], ["Mynavi company profile", MYNAVI]]),
            P("consol", "Group consolidation", "Merged SMBC Mobit in July 2023, absorbed SMBC Finance Service (formerly Cedyna and OMC) in April 2024 and made SMBC Consumer Finance (Promise) a wholly owned subsidiary in October 2024.",
              s=["con"], o="A", ay="Apr 2024", neo=[0, ""], src=[["Japanese Wikipedia: SMCC ⚠", WIKI], ["SMFG FY3/26 presentation", FYPPT]]),
        ]},
        {"id": "1.3", "ic": "scale", "name": "Leadership", "blurb": "Sasaki president from June.", "div": "smcc", "rev": "card", "products": [
            P("leaders", "Board & management", "佐々木丈也 (Sasaki), deputy president and COO, became president on 30 June 2026 ⚠ (English reading unconfirmed); Yukihiko Onishi, president and CEO before him, became chairman. An April 2026 reorganisation strengthened SME and corporate business, AI and cloud. About 5,900 staff at March 2025 ⚠.",
              s=["corp"], st="new", ay="Jun 2026", neo=[0, ""], src=[["Payment Navi: new president, Mar 2026", PRES], ["Mynavi company profile", MYNAVI]]),
        ]},
        {"id": "1.4", "ic": "badge-check", "name": "Heritage", "blurb": "Japan's first Visa card, 1980.", "div": "smcc", "rev": "card", "products": [
            P("heritage", "Heritage", "Founded in December 1967 as Sumitomo Credit Service; BankAmericard with Bank of America from 1968; Japan's first Visa card in February 1980, and founder of Visa Japan (now VJA) that year; renamed Sumitomo Mitsui Card in April 2001 ⚠.",
              s=["con"], o="I", neo=[0, "Visa heritage."], src=[["Japanese Wikipedia: SMCC ⚠", WIKI]]),
            P("dual", "Visa and Mastercard dual issuing", "Mastercard cards issued since April 1989; Japan's first UnionPay card in December 2007 ⚠.",
              s=["con"], ay="Apr 1989", at="Mastercard", neo=[1, "Second brand since 1989."],
              mc="Mastercard has been part of the line-up for 37 years.",
              src=[["Japanese Wikipedia: SMCC ⚠", WIKI]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy", "blurb": "Olive to 15m accounts.", "div": "smfg", "rev": "card", "products": [
            P("mtp", "Group plan to FY3/29", "SMBC Group's plan makes Olive and Trunk Japan's leading digital platform: Olive from 7.5 million accounts (March 2026) to 15 million in FY3/29; card sales handled from ¥38 trillion to ¥55 trillion, excluding a large transaction; 'PayPay integration and AI-Olive' named as next steps.",
              s=["con", "olive"], st="new", neo=[0, ""], src=[["SMFG FY3/26 presentation", FYPPT], ["SMFG 1Q FY3/27 overview, Jul 2026", Q1]]),
            P("techai", "AI & blockchain", "SMBC Group plans ¥100 billion of AI investment and is preparing payment infrastructure for stablecoins and tokenised deposits.",
              s=["corp"], st="new", neo=[0, ""], src=[["SMFG FY3/26 presentation", FYPPT]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Eight ways money moves: numberless consumer cards on Visa or Mastercard, Olive on Visa, Visa-only premium tiers, co-brands led by Amazon on Mastercard, memberships of every scheme, stera acquiring, stera transit on 200-plus transport operators, and wallets.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Consumer cards", "blurb": "Visa or Mastercard, numberless.", "div": "smcc", "rev": "card", "products": [
            P("nl", "SMCC (NL) & Gold (NL)", "Numberless cards since February 2021, Visa or Mastercard by choice, with up to 7% back for smartphone touch at named convenience stores and restaurants.", short="NL cards (Visa, Mastercard)",
              s=["con"], lc="everyday", ay="Feb 2021", o="B", at="Visa, Mastercard", neo=[1, "Visa or Mastercard."],
              mc="The main mass-market card offers Mastercard as an equal choice.",
              src=[["Japanese Wikipedia: SMCC ⚠", WIKI], ["Business Insider Japan: NL Visa or Mastercard, Jun 2025", NLBI]]),
            P("mccards", "SMCC Mastercard line", "三井住友Mastercard mirrors the Visa line-up except Debut Plus, RevoStyle, Platinum Preferred and Tile, and is promoted less than Visa ⚠.", short="Mastercard line",
              s=["con"], lc="everyday", at="Mastercard", neo=[2, "Mastercard-branded cards."], src=[["Japanese Wikipedia: SMCC ⚠", WIKI]]),
            P("fsomc", "FS & OMC cards", "Cards inherited from SMBC Finance Service (Cedyna and OMC), renamed SMCC (FS) or (OMC) on Visa, Mastercard or JCB, with JCB treated as an open brand ⚠.", short="FS & OMC (V, M, JCB)",
              s=["con"], lc="everyday", ay="Apr 2024", o="I", at="Visa, Mastercard, JCB", neo=[1, "Visa, Mastercard or JCB ⚠."], src=[["Japanese Wikipedia: SMCC ⚠", WIKI]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Olive", "blurb": "8 million accounts, all Visa.", "div": "olive", "rev": "card", "products": [
            P("olive", "Olive Flexible Pay", "One card that switches between credit, debit and points payment in the app, the world's first use of Visa's flexible-credential feature, launched with SMBC on 1 March 2023; 8.0 million Olive accounts at June 2026.", short="Olive Flexible Pay (Visa)",
              s=["olive", "con"], lc="open", ay="Mar 2023", o="P", at="SMBC, Visa", neo=[0, "Visa."],
              mc="The group's flagship account and card runs only on Visa.",
              src=[["Olive launch release, Mar 2023", OLIVE], ["SMFG 1Q FY3/27 overview, Jul 2026", Q1]]),
        ]},
        {"id": "2.3", "ic": "gem", "name": "Premium cards", "blurb": "Visa Infinite at the top.", "div": "smcc", "rev": "card", "products": [
            P("platpref", "Platinum Preferred", "Points-focused platinum card, Visa only ⚠.", short="Platinum Preferred (Visa)",
              s=["prem"], lc="everyday", at="Visa", neo=[0, "Visa."], src=[["Japanese Wikipedia: SMCC ⚠", WIKI]]),
            P("infinite", "Visa Infinite & Olive Infinite", "SMCC Visa Infinite issued from 29 September 2025 ⚠; Olive Infinite, 'Visa's highest tier', serves wealthy customers in SMBC Wealth.", short="Visa Infinite",
              s=["prem", "olive"], lc="everyday", st="new", ay="Sep 2025", at="Visa", neo=[0, "Visa."],
              mc="The top tier went to Visa.",
              src=[["Japanese Wikipedia: SMCC ⚠", WIKI], ["SMFG FY3/26 presentation", FYPPT]]),
        ]},
        {"id": "2.4", "ic": "users-round", "name": "Co-brands & processing", "blurb": "Amazon on Mastercard.", "div": "partners", "rev": "card", "products": [
            P("amazon", "Amazon Mastercard", "Co-brand with Amazon Japan issued by SMCC since 3 February 2014; renewed on 1 November ⚠2021 as the no-fee Amazon Mastercard and Amazon Prime Mastercard, earning Amazon points.", short="Amazon (Mastercard)",
              s=["shop"], lc="everyday", ay="Feb 2014", o="P", at="Amazon", neo=[2, "Mastercard only."],
              mc="Mastercard's largest visible programme at SMCC.",
              src=[["Payment Navi: Amazon MasterCard, Feb 2014", AMZ14], ["Nlab: Amazon Mastercard renewal ⚠", AMZ21]]),
            P("ana", "ANA & transit co-brands", "ANA cards on Visa or Mastercard and transit co-brands with Suica, PASMO, PiTaPa and nimoca ⚠.", short="ANA & transit (V, M)",
              s=["prem", "shop"], lc="everyday", o="P", at="ANA, rail operators", neo=[1, "Visa or Mastercard ⚠."], src=[["Japanese Wikipedia: SMCC ⚠", WIKI]]),
            P("processing", "Issuer processing", "Credit decisions and processing for NTT Docomo's d card and Japan Post Bank's JP BANK card, both on Visa or Mastercard ⚠.", short="d card, JP BANK (V, M)",
              s=["con"], lc="everyday", o="P", at="NTT Docomo, Japan Post Bank", neo=[1, "Visa or Mastercard ⚠."], src=[["Japanese Wikipedia: SMCC ⚠", WIKI]]),
        ]},
        {"id": "2.5", "ic": "network", "name": "Network memberships", "blurb": "Visa first, Mastercard second.", "div": "smcc", "rev": "card", "products": [
            P("netvisa", "Visa", "The house brand: Japan's first Visa issuer, founder of VJA, co-builder of stera, first user of Visa's flexible credential, and a Visa Agentic Ready issuer from May 2026.", short="Visa (house brand)",
              s=["con"], lc="move", at="Visa", neo=[0, "Visa."],
              mc="Visa holds the flagships and the joint projects.",
              src=[["Japanese Wikipedia: SMCC ⚠", WIKI], ["Payment Navi: Visa Agentic Ready, May 2026", VAR], ["Airport bus stera transit release, Feb 2026", NANKAI]]),
            P("netmc", "Mastercard", "Issued since 1989 on the NL, Gold, Platinum, Amazon, ANA and FS/OMC cards; no card-count or volume split is published; no Mastercard–SMCC agreement found for 2015–26 ⚠.", short="Mastercard (second brand)",
              s=["con", "shop"], lc="move", at="Mastercard", neo=[2, "Mastercard-branded cards."],
              mc="A real but second-rank position, with no recent joint announcement.",
              src=[["Japanese Wikipedia: SMCC ⚠", WIKI], ["Payment Navi: Amazon MasterCard, Feb 2014", AMZ14]]),
            P("netother", "JCB, UnionPay & iD", "JCB on the inherited FS and OMC cards; UnionPay cards since 2007; Docomo's FeliCa-based iD on proper cards since 2005 ⚠.", short="JCB, UnionPay, iD",
              s=["con"], lc="move", at="JCB, UnionPay, NTT Docomo", neo=[0, "Other schemes."], src=[["Japanese Wikipedia: SMCC ⚠", WIKI]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Acquiring & stera", "blurb": "300,000+ stera terminals.", "div": "stera", "rev": "merchant", "products": [
            P("stera", "stera platform", "Merchant payment platform launched in October 2019, built with GMO Payment Gateway, GMO Financial Gate and Visa; 300,000 stera terminals passed more than a year early by March 2024, with a target of 1 million by 2030 ⚠.",
              s=["merch"], lc="move", ay="Oct 2019", o="P", at="GMO-PG, GMO-FG, Visa", neo=[1, "Acquires Mastercard among others."],
              mc="SMCC acquires Mastercard on a platform co-built with Visa.",
              src=[["Payment Navi: next stera, Mar 2024", STERA], ["Airport bus stera transit release, Feb 2026", NANKAI]]),
            P("clover", "Clover with Fiserv", "Partnership announced 21 January 2026 to bring Fiserv's Clover POS and business tools to Japanese small merchants, launching late 2026; networks not stated.",
              s=["merch", "sme"], lc="move", st="new", ay="Jan 2026", o="P", at="Fiserv", neo=[None, "Networks not stated."], src=[["Fiserv and SMCC: Clover, Jan 2026", CLOVER]]),
            P("expo", "Expo 2025 payments", "Cashless platinum partner of Expo 2025 Osaka with SMBC and NEC: all-in-one terminals, tablet POS and the Myakupe e-money.",
              s=["merch"], lc="move", ay="Apr 2025", o="P", at="NEC", neo=[None, "Nothing public."], src=[["Expo 2025 partner release, Oct 2023", EXPO]]),
        ]},
        {"id": "2.7", "ic": "arrow-left-right", "name": "Transit", "blurb": "200+ operators on stera transit.", "div": "stera", "rev": "merchant", "products": [
            P("transit", "stera transit", "Open-loop contactless fares since July 2020; over 200 operators in 45 prefectures announced by January 2026, including JR Kyushu (92 stations, April 2026), the Sendai Tozai line and Kansai airport buses (March 2026). SMCC handles Visa, Mastercard and UnionPay touch; JCB handles JCB, Amex, Diners and Discover.", short="stera transit",
              s=["merch", "con"], lc="move", ay="Jul 2020", o="B", at="JCB, QUADRAC", neo=[1, "Mastercard touch accepted."],
              mc="SMCC promotes Mastercard touch on transport alongside Visa.",
              src=[["Airport bus stera transit release, Feb 2026", NANKAI], ["Sendai Tozai line release, Mar 2026", SENDAI], ["DX Magazine: JR Kyushu, Jan 2026", JRK]]),
            P("passcase", "Pass Case app", "Transit app launched in March 2025 ⚠.",
              s=["con"], lc="move", st="new", ay="Mar 2025", o="B", neo=[None, "Nothing public."], src=[["Japanese Wikipedia: SMCC ⚠", WIKI]]),
        ]},
        {"id": "2.8", "ic": "smartphone", "name": "Wallets & contactless", "blurb": "Mastercard first on Apple Pay.", "div": "smcc", "rev": "card", "products": [
            P("wallets", "Apple Pay & Google Pay", "Apple Pay with Mastercard contactless from October 2016, Visa from May 2021 and Visa on Google Pay from March 2022 ⚠; Mastercard touch cannot be used in Google Pay or Samsung Pay (June 2025).", short="Apple Pay (M 2016), Google Pay (V)",
              s=["con"], lc="everyday", ay="Oct 2016", o="P", at="Apple, Google", neo=[1, "Mastercard on Apple Pay, not Google Pay."],
              mc="Android wallets lack Mastercard touch.",
              src=[["Japanese Wikipedia: SMCC ⚠", WIKI], ["Business Insider Japan: NL Visa or Mastercard, Jun 2025", NLBI]]),
            P("idfelica", "iD & e-money", "Docomo's iD built into proper cards since 2005, with WAON, Edy and PiTaPa links ⚠.", short="iD (FeliCa)",
              s=["con"], lc="everyday", ay="Dec 2005", o="P", at="NTT Docomo", neo=[0, "Docomo's iD."], src=[["Japanese Wikipedia: SMCC ⚠", WIKI]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every card: fraud control against Japan's ¥51 billion of card fraud, AI in Olive and the call centre, V Point as the group's points business, and the SoftBank and PayPay alliance.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & identity", "blurb": "¥51bn of fraud in Japan.", "div": "smcc", "rev": "card", "products": [
            P("fraud", "Fraud controls", "Japanese card fraud losses were ¥51.05 billion in 2025, mostly from stolen card numbers; SMCC's numberless cards keep the number off the plastic. Its own fraud tools are not described in the sources read ⚠.",
              s=["con", "merch"], lc="everyday", o="B", neo=[None, "Nothing public."],
              mc="Number theft is the problem tokens and passkeys address.",
              src=[["ECのミカタ: 2025 card fraud", FRAUD], ["Japanese Wikipedia: SMCC ⚠", WIKI]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI & agents", "blurb": "Visa Agentic Ready issuer.", "div": "smfg", "rev": "card", "products": [
            P("aiolive", "AI-Olive & AI call centre", "AI-Olive is named in SMBC Group's plan; the SoftBank alliance includes a 24-hour call centre run by autonomous AI.",
              s=["olive", "con"], lc="everyday", st="new", o="P", at="SoftBank", neo=[0, ""], src=[["SMFG FY3/26 presentation", FYPPT], ["SoftBank News: alliance, May 2025", PAYPAY]]),
            P("agentic", "Agentic payments", "SMCC is one of five Japanese issuers in Visa Agentic Ready (May 2026). Mastercard's first live agentic transaction in Japan (20 May 2026) used MUFG NICOS and other issuers' cards; SMCC is not named.",
              s=["con"], lc="move", st="new", ay="May 2026", at="Visa", neo=[0, "Visa."],
              mc="Agent Pay is live in Japan but SMCC has signed up with Visa.",
              src=[["Payment Navi: Visa Agentic Ready, May 2026", VAR], ["Payment Navi: Mastercard agentic transaction, May 2026", MCAG]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Points & offers", "blurb": "V Point, now a subsidiary.", "div": "vpoint", "rev": "card", "products": [
            P("vpoint", "V Point", "SMBC Group's V Point merged with CCC's T Point in April 2024; SMCC made V POINT MARKETING (formerly CCC MK Holdings) a subsidiary on 31 March 2026, aiming for the 'No. 1 point program'.",
              s=["con", "shop"], lc="grow", st="new", ay="Mar 2026", o="A", at="CCC", neo=[0, "Own points."],
              src=[["CCC: V POINT MARKETING, Apr 2026", VPOINT], ["Japanese Wikipedia: SMCC ⚠", WIKI]]),
            P("campaign", "Smartphone-touch rewards", "Up to 8% back in an August 2026 campaign for smartphone contactless and mobile order at participating convenience stores and restaurants; physical-card touch is excluded.",
              s=["con"], lc="everyday", st="new", ay="Aug 2026", neo=[1, "Visa and Mastercard touch."], src=[["Payment Navi: up to 8% back, Aug 2026", CAMP], ["Business Insider Japan: NL Visa or Mastercard, Jun 2025", NLBI]]),
        ]},
        {"id": "3.4", "ic": "database", "name": "Partners & data", "blurb": "SoftBank and PayPay alliance.", "div": "partners", "rev": "card", "products": [
            P("paypay", "SoftBank & PayPay alliance", "Comprehensive alliance of 15 May 2025: SMCC cards favoured in PayPay, PayPay favoured in Vpass and Olive, points exchange, and joint work on healthcare, digital insurance and AI. PayPay has 75 million users.",
              s=["con", "olive"], lc="move", st="new", ay="May 2025", o="P", at="SoftBank, PayPay", neo=[0, ""],
              src=[["SoftBank News: alliance, May 2025", PAYPAY], ["PayPay: 75 million users, Aug 2026", PAYPAYU]]),
            P("data", "Data & money management", "Custella data-analysis service for businesses (October 2019) and joint operation of Money Forward Home with Money Forward (December 2024) ⚠.",
              s=["merch", "con"], lc="beyond", o="P", at="Money Forward", neo=[0, ""], src=[["Japanese Wikipedia: SMCC ⚠", WIKI]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: consumer finance through Promise and Mobit, revolving and instalments, loan guarantees for banks, business and corporate cards with Trunk, and Visa debit and prepaid.",
    "tiles": [
        {"id": "4.1", "ic": "coins", "name": "Consumer finance", "blurb": "¥351bn of finance revenue.", "div": "smbccf", "rev": "finance", "products": [
            P("promise", "Promise & Mobit loans", "SMBC Consumer Finance (Promise), wholly owned since October 2024, and the SMBC Mobit loan brands; SMBCCF finance revenue ¥169.3 billion in FY3/26, NPL ratio 10.53%.",
              s=["con"], lc="borrow", o="A", ay="Oct 2024", neo=[0, ""], src=[["SMFG FY3/26 presentation", FYPPT], ["Japanese Wikipedia: SMCC ⚠", WIKI]]),
            P("revolve", "Revolving, instalments & cash advance", "Finance revenue of ¥350.7 billion in FY3/26 across the group, including card revolving and cash advances.",
              s=["con"], lc="borrow", neo=[1, "Rides on each card's brand."], src=[["SMFG FY3/26 presentation", FYPPT]]),
        ]},
        {"id": "4.2", "ic": "landmark", "name": "Loan guarantees", "blurb": "¥87bn of guarantee revenue.", "div": "smbccf", "rev": "guarantee", "products": [
            P("guarantee", "Loan guarantees", "Guarantees of other lenders' consumer loans: ¥87.4 billion of revenue in FY3/26 and ¥21.8 billion in 1Q FY3/27.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["SMFG FY3/26 presentation", FYPPT], ["SMFG 1Q FY3/27 overview, Jul 2026", Q1]]),
        ]},
        {"id": "4.3", "ic": "briefcase-business", "name": "Business & corporate", "blurb": "Trunk: 90,000 accounts.", "div": "smfg", "rev": "card", "products": [
            P("trunk", "Trunk", "Digital banking and payments for small companies from 26 May 2025, with SMBC: 90,000 accounts in July 2026, aiming for 300,000 in FY3/29 and a corporate card of about ¥3 trillion ⚠; finance and factoring planned in FY3/27. Card network not stated ⚠.",
              s=["sme"], lc="open", st="new", ay="May 2025", o="P", at="SMBC", neo=[None, "Network not stated."],
              mc="A new small-business card book still open on network.",
              src=[["SMFG FY3/26 presentation", FYPPT], ["SMFG 1Q FY3/27 overview, Jul 2026", Q1]]),
            P("corpcard", "Corporate cards", "Corporate cards for large companies since 1985 ⚠; the April 2026 reorganisation strengthened corporate business. Networks not confirmed ⚠.",
              s=["corp"], lc="everyday", o="B", neo=[None, "Networks not confirmed."],
              src=[["Japanese Wikipedia: SMCC ⚠", WIKI], ["Payment Navi: new president, Mar 2026", PRES]]),
            P("bizcard", "Business cards & prepaid", "Business Card for Owners for sole proprietors (2017) and Japan's first business prepaid card (2018) ⚠.",
              s=["sme"], lc="everyday", o="B", neo=[None, "Networks not confirmed."], src=[["Japanese Wikipedia: SMCC ⚠", WIKI]]),
        ]},
        {"id": "4.4", "ic": "wallet", "name": "Debit & prepaid", "blurb": "Visa debit with SMBC.", "div": "smfg", "rev": "card", "products": [
            P("smbcdebit", "SMBC Debit", "Visa debit card with SMBC from October 2016, now inside Olive ⚠.", short="SMBC Debit (Visa)",
              s=["olive"], lc="everyday", ay="Oct 2016", o="P", at="SMBC, Visa", neo=[0, "Visa."], src=[["Japanese Wikipedia: SMCC ⚠", WIKI]]),
            P("prepaid", "Prepaid & gift", "Visa prepaid cards (2015), the family prepaid Kazoku no Osaifu (2020) and VJA gift cards ⚠.", short="Prepaid (Visa)",
              s=["con"], lc="everyday", at="Visa", neo=[0, "Visa."], src=[["Japanese Wikipedia: SMCC ⚠", WIKI]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach SMCC: the Vpass app and the SMBC app that carries Olive, partner channels from Amazon to PayPay, and SMBC's branches.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Apps", "blurb": "Vpass and the SMBC app.", "div": "smcc", "rev": "card", "products": [
            P("vpass", "Vpass", "Card app and website since 1999; FS cards moved onto Vpass in December 2024 ⚠; PayPay is favoured inside it under the 2025 alliance.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["Japanese Wikipedia: SMCC ⚠", WIKI], ["SoftBank News: alliance, May 2025", PAYPAY]]),
            P("smbcapp", "SMBC app & Olive", "Olive is opened and run in the SMBC app and Vpass, with bank, card, securities and insurance in one view.",
              s=["olive"], lc="open", o="P", at="SMBC", neo=[0, ""], src=[["Olive launch release, Mar 2023", OLIVE]]),
        ]},
        {"id": "5.2", "ic": "users-round", "name": "Partner channels", "blurb": "Amazon, ANA, Docomo, PayPay.", "div": "partners", "rev": "card", "products": [
            P("partnerch", "Partner channels", "Amazon (the Amazon Mastercard), ANA, NTT Docomo, Japan Post Bank, PayPay and V Point stores bring customers to SMCC cards.",
              s=["shop", "con"], lc="open", o="P", at="Amazon, ANA, PayPay", neo=[0, ""],
              src=[["Payment Navi: Amazon MasterCard, Feb 2014", AMZ14], ["SoftBank News: alliance, May 2025", PAYPAY], ["Japanese Wikipedia: SMCC ⚠", WIKI]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "SMBC branches", "blurb": "Face-to-face through the bank.", "div": "smfg", "rev": "card", "products": [
            P("branches", "SMBC branches & consulting", "SMBC branches and Olive Consulting (from FY3/27) offer face-to-face, online and AI-chat advice, with extra points for card instalment investing.",
              s=["olive", "prem"], lc="grow", o="P", at="SMBC", neo=[0, ""], src=[["SMFG FY3/26 presentation", FYPPT]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at SMBC Card", "blurb": "A real second brand to Visa.", "products": [
        P("mcatsmcc", "Mastercard at SMBC Card", "SMCC has issued Mastercard since 1989, offers it as an equal choice on the NL, Gold and Platinum cards, runs the Mastercard-only Amazon co-brand, put Mastercard first on Apple Pay in 2016 and acquires Mastercard on stera and stera transit. Visa is the house brand and holds Olive, Platinum Preferred, Visa Infinite, stera's design and the agentic pilot. No network split is published ⚠.",
          s=["con"], div="smcc", rev="card", mc="The relationship this map is drawn for.",
          src=[["Japanese Wikipedia: SMCC ⚠", WIKI], ["Payment Navi: Amazon MasterCard, Feb 2014", AMZ14], ["Airport bus stera transit release, Feb 2026", NANKAI]]),
    ]},
    {"id": "pillar-market", "name": "Japanese payments", "blurb": "58% cashless, credit-led.", "products": [
        P("market", "The Japanese market", "Cashless payments were 58.0% of consumption in 2025, with credit cards 82.7% of cashless value and code payments 10.2%, led by PayPay; card fraud losses were ¥51 billion. The target is 65% by 2030.",
          s=["con"], div="smfg", rev="card", src=[["Impress Watch: METI cashless ratio, Apr 2026", CASHLESS], ["SCBRI: 2025 cashless mix", SCBRI], ["ECのミカタ: 2025 card fraud", FRAUD]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
