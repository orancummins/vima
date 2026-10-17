"""KB Kookmin Card's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the company's own, as KB Financial Group discloses them and the Korean business press reports
them, unless a source says otherwise: the H1 2026 results (July 2026). KB Card's own site loads its press
and history pages by script, so most product facts come from press reports of its releases, translated.
``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it,
2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

SAT0724 = "https://sateconomy.co.kr/news/view/1065612369517799"
SAT0807 = "https://sateconomy.co.kr/news/view/1065599055785653"
BIZW = "https://news.bizwatch.co.kr/article/finance/2026/07/27/0019"
NEWSIS = "https://mobile.newsis.com/view/NISX20260731_0003732291"
MTN = "https://news.mtn.co.kr/news-detail/2026092815530779050"
MYDAILY = "https://www.mydaily.co.kr/page/view/2026081116291911306"
M1208 = "https://www.metroseoul.co.kr/article/20241208500088"
M0224 = "https://www.metroseoul.co.kr/article/20250224500124"
M0119 = "https://www.metroseoul.co.kr/article/20260119500127"
M1201 = "https://www.metroseoul.co.kr/article/20241201500014"
M1027 = "https://www.metroseoul.co.kr/article/20241027500005"
YOUPRIME = "https://www.metroseoul.co.kr/article/20260201500071"
HCLASSIC = "https://www.dailian.co.kr/news/view/1437877/%EA%B5%AD%EB%AF%BC%EC%B9%B4%EB%93%9C-%ED%97%A4%EB%A6%AC%ED%8B%B0%EC%A7%80-%ED%81%B4%EB%9E%98%EC%8B%9D-%EC%B6%9C%EC%8B%9C%EC%8B%A4%EC%86%8D-%EC%B1%99-2024"
HSMART = "https://www.insight.co.kr/news/425738"
AYN = "https://www.heraldk.com/article/2026012616093011256"
KBALL = "https://www.heraldk.com/article/2026012717063511965"
NEEDPAY = "https://www.heraldk.com/article/2026050517191558250"
TRAVEV = "https://www.heraldk.com/article/2025110320500936635"
AJD = "https://www.ajd.co.kr/card/detail/1057"
FNTRAV = "https://www.fnnews.com/news/202607131817212578"
MACAO = "https://www.gcs.gov.mo/detail/en/N25JbcFcLv"
CPP = "https://en.bloomingbit.io/feed/news/120718"
AGENTPOC = "https://sateconomy.co.kr/news/view/1065599958703855"
SBI = "https://biz.sbs.co.kr/amp/article/20000339628"
AIINT = "https://v.daum.net/v/20260603170022221"
VISAEV = "https://view.asiae.co.kr/article/2026051816303649667"
APTF = "https://news.tf.co.kr/read/economy/2333589.htm"
AP2023 = "https://www.insight.co.kr/news/440927"
KBPAY25 = "https://sateconomy.co.kr/news/view/1065580164796269"
MAU26 = "https://news.dealsitetv.com/articles/172487"
OVS = "https://dealsite.co.kr/articles/163546"
MYANMAR = "https://stockhub.kr/en/news/news_12dd3267e36b"
KWORLD = "https://www.sidae.com/article/2014101613448054456"
WIKI = "https://ko.wikipedia.org/wiki/KB%EA%B5%AD%EB%AF%BC%EC%B9%B4%EB%93%9C"
KBFGH1 = "https://sateconomy.co.kr/news/view/1065594872737182"
KBHOME = "https://card.kbcard.com/CXPRIMAZZC0001.cms"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · heritage · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: ₩31 trillion of assets and ₩219 billion of profit in the half, a card business that began inside Kookmin Bank in 1980 and has stood alone since 2011, funding from bonds and ABS, and a 2026 strategy of execution, corporate sales, AI and digital assets.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & earnings", "blurb": "₩219bn in H1, third in Korea.", "div": "kbc", "rev": "card", "products": [
            P("balance", "Balance sheet & earnings", "Net income of ₩218.9 billion in H1 2026, up 20.7% (Q2 ₩111.4 billion); operating revenue ₩2.76 trillion (+0.6%); ROE 7.86%; total assets ₩31.3 trillion. Delinquency 1.07% at June 2026, from 1.40% a year earlier. Third on half-year profit, behind Samsung Card and Shinhan Card, ahead of Hyundai Card.",
              s=["corp"], neo=[0, ""], src=[["Toyo Economy: H1 2026 results, Jul 2026", SAT0724], ["Toyo Economy: H1 2026 analysis, Aug 2026", SAT0807], ["Bizwatch: six issuers' H1 2026", BIZW]]),
            P("volume", "Customers & volume", "About 12.95 million members at end-April 2026 (Shinhan 14.55 million) and about ₩93.5 trillion of card usage in H1 2026, up 5.3%; card revenue ₩2.21 trillion.",
              s=["con"], neo=[0, ""], src=[["The Fact: members, Jun 2026", APTF], ["Toyo Economy: H1 2026 analysis, Aug 2026", SAT0807], ["Newsis: card CEOs, Aug 2026", NEWSIS]]),
            P("funding", "Funding", "Funded mainly by card bonds, with Kimchi bonds and overseas ABS added to cut interest costs; AA+ three-year card bonds yielded about 4.55% in July 2026, up from the low 3% range in January.",
              s=["corp"], neo=[0, ""], src=[["Toyo Economy: H1 2026 results, Jul 2026", SAT0724], ["Bizwatch: six issuers' H1 2026", BIZW]]),
        ]},
        {"id": "1.2", "ic": "badge-check", "name": "Heritage & ownership", "blurb": "Kookmin Bank's card since 1980.", "div": "kbfg", "rev": "card", "products": [
            P("heritage", "KB Financial Group & Kookmin heritage", "Wholly owned by KB Financial Group (KRX and NYSE listed; H1 2026 net income ₩3.88 trillion ⚠). Kookmin Bank began card business in 1980; Kookmin Credit Card (1987) was merged back into the bank in 2003 and KB Kookmin Card was spun off on 2 March 2011 ⚠.",
              s=["corp"], o="I", neo=[0, ""], src=[["Wikipedia (ko): KB Kookmin Card", WIKI], ["Toyo Economy: KB Financial H1 2026", KBFGH1]]),
        ]},
        {"id": "1.3", "ic": "scale", "name": "Leadership & controls", "blurb": "Kim Jae-kwan since 2025.", "div": "kbc", "rev": "card", "products": [
            P("leadership", "Leadership", "CEO Kim Jae-kwan, former KB Financial CFO, since January 2025; his term ends in December 2026 and KB Financial's subsidiary CEO committee was due to meet from end-September ⚠ outcome not known. KB Financial is moving to chairman-elect Lee Jae-geun ⚠.",
              s=["corp"], st="flux", neo=[0, ""], src=[["Metro: next CEO named, Dec 2024", M1208], ["Newsis: card CEOs, Aug 2026", NEWSIS], ["MTN: KB CEO process, Sep 2026", MTN]]),
            P("aml", "Anti-money-laundering & consumer protection", "Financial Services Commission chairman's award on Anti-Money Laundering Day (December 2024), for training, high-risk-country checks and periodic risk ratings.",
              s=["con"], neo=[0, ""], src=[["Metro: AML award, Dec 2024", M1201]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy & AI", "blurb": "Execution, corporate sales, AI.", "div": "kbc", "rev": "card", "products": [
            P("strategy", "Strategy 2026", "Kim's 2026 theme is execution: a reorganisation adds a Corporate Sales Division with 18 sales departments, and digital, AI and data units are rearranged. Growth in H1 2026 came mostly from card spending and lower costs, not new businesses.",
              s=["corp"], neo=[0, ""], src=[["Metro: 2026 strategy, Jan 2026", M0119], ["Toyo Economy: H1 2026 analysis, Aug 2026", SAT0807]]),
            P("aicenter", "AI Center & AI transformation", "An AI Center (head Lee Cheong-jae) and an AI Data Business Group; a copilot rollout and AI in decisions (2026); AI agents presented to about 20 foreign bank executives at a Visa event at KB's head office (May 2026).",
              s=["corp"], st="new", ay="2026", neo=[0, ""], src=[["Aju: AI Center head interview, Jun 2026", AIINT], ["Asia Economy: Visa event, May 2026", VISAEV], ["Toyo Economy: H1 2026 results, Jul 2026", SAT0724]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Eight ways money moves: the ALL·YOU·NEED cards and the HERITAGE premium cards, sold domestic-only or with an international brand; KB's own K-World brand on JCB and UnionPay; the Travelers check card on Mastercard; Visa, UnionPay and others; wallets; agent payments; and stablecoin tests.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "ALL·YOU·NEED cards", "blurb": "New product brands, 2026.", "div": "kbc", "rev": "card", "products": [
            P("kball", "KB ALL card", "The ALL line's lead card (January 2026), renamed from WE:SH All: 1% off at home with no spending condition or cap, 2% abroad up to ₩40,000 a month; ₩20,000 a year, ₩14,000 mobile-only. Network not stated ⚠.",
              s=["con"], lc="everyday", st="new", ay="Jan 2026", o="B", neo=[None, "Network not stated."], src=[["Herald: KB ALL card, Jan 2026", KBALL], ["Herald: ALL·YOU·NEED, Jan 2026", AYN]]),
            P("youprime", "KB YOU Prime", "Card for customers in their 30s and 40s (February 2026): up to ₩60,000 a month off through a Daily or Family pack; ₩30,000 a year; no international brand or overseas service fees; Mastercard or K-World (JCB), both with lounges and valet.", short="KB YOU Prime (Mastercard or JCB)",
              s=["con"], lc="everyday", st="new", ay="Feb 2026", o="B", neo=[1, "Mastercard or K-World (JCB)."],
              mc="KB's newest card offers Mastercard, but JCB through its own K-World brand sits beside it.", src=[["Metro: KB YOU Prime, Feb 2026", YOUPRIME]]),
            P("needpay", "KB NEED Pay", "Card for wallet users (May 2026): 15% off through KB Pay or 10% through Naver Pay, Kakao Pay or Toss Pay, up to ₩30,000 a month; 2% off abroad; ₩19,000 domestic-only or international. Network not stated ⚠.",
              s=["con", "young"], lc="everyday", st="new", ay="May 2026", o="B", neo=[None, "Network not stated."], src=[["Herald: KB NEED Pay, May 2026", NEEDPAY]]),
            P("wesh", "WE:SH series", "The 2022–25 credit-card line (My WE:SH, Our WE:SH, WE:SH All), past 1 million cards in about two years; folded into ALL·YOU·NEED in 2026.",
              s=["con"], lc="everyday", st="retired", ay="2022", o="B", neo=[None, ""], src=[["Metro: next CEO named, Dec 2024", M1208], ["Herald: KB ALL card, Jan 2026", KBALL]]),
        ]},
        {"id": "2.2", "ic": "gem", "name": "HERITAGE premium", "blurb": "Mastercard, JCB and Visa.", "div": "kbc", "rev": "card", "products": [
            P("hsmart", "HERITAGE Smart", "KB's first premium card in five years (January 2023): 1% off at home and 3% abroad without limits, or Korean Air miles; Mastercard World services (valet, lounges) on the Mastercard version.", short="HERITAGE Smart (Mastercard)",
              s=["prem"], lc="everyday", ay="Jan 2023", o="B", neo=[1, "Mastercard World services on Mastercard versions."], src=[["Insight: HERITAGE Smart, Jan 2023", HSMART]]),
            P("hclassic", "HERITAGE Classic", "Premium card (December 2024): a discount version on Mastercard Platinum or JCB Platinum (₩127,000) and a SkyPass mileage version on Mastercard World or Visa Signature (₩157,000); lounges, valet and contactless on all four brands.", short="HERITAGE Classic (Mastercard, JCB, Visa)",
              s=["prem", "trav"], lc="everyday", ay="Dec 2024", o="B", neo=[1, "Mastercard, JCB or Visa."], src=[["Dailian: HERITAGE Classic, Dec 2024", HCLASSIC]]),
        ]},
        {"id": "2.3", "ic": "network", "name": "Domestic rails & K-World", "blurb": "Own brand on JCB and UnionPay.", "div": "kworld", "rev": "card", "products": [
            P("domestic", "Domestic-only cards & Korean processing", "Cards come domestic-only or with an international brand, often at the same fee; purchases in Korea are processed on Korean rails whatever the brand ⚠ inferred.", short="Domestic-only cards",
              s=["con", "biz"], lc="everyday", o="B", neo=[0, "Korean rails."],
              mc="Most of KB's volume is domestic and never needs a scheme ⚠.", src=[["Herald: KB NEED Pay, May 2026", NEEDPAY], ["Wikipedia (ko): KB Kookmin Card", WIKI]]),
            P("kworld", "K-World", "KB's own brand (July 2014) for use abroad at the domestic-only fee: JCB acceptance first, UnionPay from September 2014, with a lower overseas service fee; built so KB pays no scheme fees on domestic spending. Still the alternative to Mastercard on KB YOU Prime.", short="K-World (JCB, UnionPay)",
              s=["con", "trav"], lc="move", ay="Jul 2014", o="P", at="JCB, UnionPay", neo=[0, "KB's own brand on JCB and UnionPay."],
              mc="A deliberate move away from global scheme fees, and still on new cards.", src=[["Sidae: K-World, Oct 2014", KWORLD], ["Metro: KB YOU Prime, Feb 2026", YOUPRIME]]),
            P("bc", "BC Card co-brands", "KT co-brand credit cards are issued under BC Card, with Visa, Mastercard or UnionPay ⚠.",
              s=["con"], lc="everyday", st="unconf", o="P", at="BC Card (KT)", neo=[0, "BC Card."], src=[["Wikipedia (ko): KB Kookmin Card", WIKI]]),
            P("processing", "Card processing for others", "KB's card system runs Kakao Bank's Friends check cards, NH Chaeum cards, KB Securities cards and Jeonbuk Bank cards (from 2022), and iM Bank's teen prepaid product (June 2024) ⚠.",
              s=["corp"], lc="beyond", o="B", neo=[0, ""], src=[["Wikipedia (ko): KB Kookmin Card", WIKI]]),
        ]},
        {"id": "2.4", "ic": "plane", "name": "Travelers check card", "blurb": "Travel debit on Mastercard.", "div": "kbc", "rev": "card", "products": [
            P("travelers", "KB Travelers check card", "Travel debit card on Mastercard: no 1% brand fee or 0.25% overseas fee, 10% off abroad from July 2026, issue age down to 7, and a foreign-currency account in 11 currencies; KB has 11.4% of personal overseas check-card spend, against Hana's 42.3% and Shinhan's 31.0%.", short="Travelers check card (Mastercard)",
              s=["trav", "young"], lc="move", o="B", neo=[2, "Mastercard, with Travel Rewards."],
              mc="KB's main Mastercard debit franchise, but third in travel debit.", src=[["AJD: Travelers check card ⚠ undated", AJD], ["Financial News: travel cards, Jul 2026", FNTRAV], ["Herald: travel offers, Nov 2025", TRAVEV]]),
            P("macao", "Travelers check card – Macao Edition", "Unveiled with Mastercard Korea and the Macao Government Tourism Office (October 2025): discounts on Macao flights, hotels, dining and shows, and cards showing Macao heritage buildings.", short="Macao Edition (Mastercard)",
              s=["trav"], lc="move", st="new", ay="Oct 2025", o="P", at="Mastercard Korea, MGTO", neo=[2, "Mastercard."], src=[["Macao Government Information Bureau, Oct 2025", MACAO]]),
        ]},
        {"id": "2.5", "ic": "earth", "name": "Visa, UnionPay & others", "blurb": "The other brands.", "div": "kbc", "rev": "card", "products": [
            P("visa", "Visa cards", "Visa on the HERITAGE Classic SkyPass option (Visa Signature) and on KT co-brands; 50% cashback on contactless transit abroad with KB Visa cards (October 2024).", short="Visa cards",
              s=["con", "trav"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Dailian: HERITAGE Classic, Dec 2024", HCLASSIC], ["Metro: autumn travel offers, Oct 2024", M1027], ["Sidae: K-World, Oct 2014", KWORLD]]),
            P("upi", "UnionPay cards", "KB UnionPay credit and check cards, with a 10% instant discount in nine markets including China, Japan and the US (to December 2025); UnionPay also through K-World.", short="UnionPay cards",
              s=["trav"], lc="move", o="P", at="UnionPay", neo=[0, "UnionPay."], src=[["Herald: travel offers, Nov 2025", TRAVEV]]),
            P("amex", "American Express & JCB", "Amex and JCB are listed among KB's brands ⚠ no current Amex product found; JCB on HERITAGE Classic and through K-World.",
              s=["con"], lc="everyday", st="unconf", o="P", at="American Express, JCB", neo=[0, "American Express, JCB."], src=[["Wikipedia (ko): KB Kookmin Card", WIKI], ["Dailian: HERITAGE Classic, Dec 2024", HCLASSIC]]),
        ]},
        {"id": "2.6", "ic": "wallet", "name": "Wallets", "blurb": "KB Pay app card; Apple Pay pending.", "div": "kbpay", "rev": "card", "products": [
            P("appcard", "KB Pay app card & ISP", "Online payments through the KB Pay app card or ISP, with a six-digit ISP password since August 2020; the same system serves Kakao Bank check cards ⚠.",
              s=["con"], lc="move", o="B", neo=[0, ""], src=[["Wikipedia (ko): KB Kookmin Card", WIKI]]),
            P("applepay", "Apple Pay", "KB, Shinhan and BC sent Apple letters of intent in June 2023; KB cards could briefly be added to Apple Pay in June 2026 during Visa's testing, but KB says no date is set. Not live at October 2026 ⚠.",
              s=["con"], lc="move", st="unconf", o="P", at="Apple, Visa", neo=[None, "Visa ran the test; launch networks not announced."],
              mc="Wallet tokens would ride on each card's brand; Visa is the one named so far.", src=[["The Fact: Apple Pay test, Jun 2026", APTF], ["Insight: Apple Pay letters of intent, Jun 2023", AP2023]]),
        ]},
        {"id": "2.7", "ic": "bot", "name": "Agent payments", "blurb": "Visa programme, K-AP test.", "div": "kbc", "rev": "card", "products": [
            P("agentpoc", "AI-agent payment tests", "MOU and joint test with SY Polaris (29 September 2026) using its K-AP standard to run agent, shop, payment-module and card-system flows; KB also takes part in Visa's Agentic Commerce Ready Program abroad.", short="Agent payments (Visa, K-AP)",
              s=["con"], lc="move", st="new", ay="Sep 2026", o="P", at="SY Polaris, Visa", neo=[0, "Visa programme and K-AP."],
              mc="Mastercard ran Korea's first Agent Pay with Shinhan; KB has chosen Visa's programme so far.", src=[["Toyo Economy: agent payment test, Sep 2026", AGENTPOC], ["Aju: AI Center head interview, Jun 2026", AIINT]]),
        ]},
        {"id": "2.8", "ic": "coins", "name": "Digital money", "blurb": "Stablecoin tests.", "div": "kbc", "rev": "other", "products": [
            P("cpp", "Mastercard Crypto Partner Program", "KB joined Mastercard's programme (September 2026) to test stablecoin payments in KB Pay with a Coinbase wallet, covering authorisation, settlement, cancellations and refunds ahead of new Korean rules.", short="Stablecoin test (Mastercard)",
              s=["con", "corp"], lc="move", st="new", ay="Sep 2026", o="P", at="Mastercard, Coinbase", neo=[2, "Within Mastercard's Crypto Partner Program."],
              mc="KB's one live strategic project with Mastercard.", src=[["Bloomingbit (ETNews): Mastercard CPP, Sep 2026", CPP]]),
            P("hybrid", "Hybrid stablecoin card patent", "A patent linking a blockchain wallet address to a credit card: stablecoin balance is spent first, with the credit card covering any shortfall (January 2026).",
              s=["con"], lc="move", st="new", ay="Jan 2026", o="B", neo=[None, "Network not stated."], src=[["Metro: 2026 strategy, Jan 2026", M0119]]),
            P("sbi", "SBI stablecoin & agent-identity MOU", "MOU with SBI Holdings, SBI Evers Spin and Evers Spin (13 October 2026): KYA identity and permissions for Japanese AI agents using Korean services, and stablecoins held by Japanese tourists paying at Korean merchants, possibly through KB Pay.",
              s=["trav", "corp"], lc="move", st="new", ay="Oct 2026", o="P", at="SBI Holdings, Evers Spin", neo=[0, ""], src=[["SBS Biz: SBI MOU, Oct 2026", SBI]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every card: overseas payment controls and AML checks, a data business for small merchants and local government, points, miles and Mastercard Travel Rewards, and AI in operations.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Security & controls", "blurb": "Overseas blocks, safe payment.", "div": "kbc", "rev": "card", "products": [
            P("overseassafe", "Overseas payment controls", "Overseas safe payment, overseas transaction blocking and DCC blocking for cardholders; KB was first in the industry with an overseas online safe-payment service (2014). No public detail on its fraud-detection system ⚠.",
              s=["con", "trav"], lc="everyday", o="B", neo=[0, "KB's own."],
              mc="No public fraud or scam tool from a scheme; room for Mastercard's.", src=[["KB Card homepage", KBHOME], ["Sidae: K-World, Oct 2014", KWORLD]]),
        ]},
        {"id": "3.2", "ic": "database", "name": "Data", "blurb": "Data lake for small merchants.", "div": "kbc", "rev": "other", "products": [
            P("datalake", "Data business", "A data lake for small merchants (2024) and a data partnership with Korea University, combining KB Card and KB Kookmin Bank data for consulting; platform and data income is not reported separately.",
              s=["biz", "corp"], lc="beyond", o="B", neo=[0, ""], src=[["Metro: 2025 strategy, Feb 2025", M0224], ["Toyo Economy: H1 2026 analysis, Aug 2026", SAT0807]]),
            P("tourism", "Regional tourism data", "Data on visitors' spending for Icheon city's festivals and shops, and Jeju village discounts (2024).",
              s=["corp"], lc="beyond", o="P", at="Icheon city", neo=[0, ""], src=[["Metro: 2025 strategy, Feb 2025", M0224]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards & offers", "blurb": "Pointree, miles, Travel Rewards.", "div": "kbc", "rev": "card", "products": [
            P("points", "Pointree points & miles", "Pointree points, Korean Air SkyPass mileage cards and Star Shop merchant discounts and points.",
              s=["con", "prem"], lc="grow", o="B", neo=[0, ""], src=[["Dailian: HERITAGE Classic, Dec 2024", HCLASSIC], ["KB Card homepage", KBHOME]]),
            P("mtr", "Mastercard Travel Rewards", "Travelers check card holders register in KB Pay for up to 10% cashback at Japanese department stores, Alipay merchants in China and European shopping sites (to December 2025); a Westin Chosun Seoul perk for KB Mastercard spending abroad.", short="Travel Rewards (Mastercard)",
              s=["trav"], lc="move", o="P", at="Mastercard", neo=[3, "Mastercard Travel Rewards."], src=[["Herald: travel offers, Nov 2025", TRAVEV]]),
        ]},
        {"id": "3.4", "ic": "brain", "name": "AI in operations", "blurb": "Copilot, AI agents.", "div": "kbc", "rev": "card", "products": [
            P("copilot", "Copilot & AI agents", "AI in operations and decisions, a copilot rollout, data restructuring, IT projects reviewed by return and leaner cloud spend (2026).",
              s=["corp"], lc="beyond", st="new", ay="2026", neo=[0, ""], src=[["Toyo Economy: H1 2026 results, Jul 2026", SAT0724], ["Asia Economy: Visa event, May 2026", VISAEV]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: card spending, card loans and cash advances, instalment finance and leasing, Korea's largest corporate card business, merchant services, and consumer finance in Thailand, Cambodia and Indonesia.",
    "tiles": [
        {"id": "4.1", "ic": "hand-coins", "name": "Consumers & youth", "blurb": "₩93.5tn of card usage in H1.", "div": "kbc", "rev": "finance", "products": [
            P("cardvol", "Card spending", "About ₩93.5 trillion of card usage in H1 2026, up 5.3%; card revenue ₩2.21 trillion (+0.2%).",
              s=["con"], lc="everyday", neo=[1, "Mastercard on many international versions; domestic volume on Korean rails."], src=[["Toyo Economy: H1 2026 analysis, Aug 2026", SAT0807]]),
            P("loans", "Card loans & cash advances", "Average new card-loan rates of about 13.8% and cash-advance rates of about 18.3% at June 2026, against a 4.33% funding rate; balances not disclosed in sources read ⚠.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Toyo Economy: H1 2026 analysis, Aug 2026", SAT0807]]),
            P("youth", "KB Youth Club & Star Teens", "KB Youth Club check card for 18–29s passed 200,000 accounts in about eight months from December 2025; Catch! Teenieping designs on the Travelers and Star Teens cards (July 2026). Networks not stated ⚠.",
              s=["young"], lc="open", st="new", ay="Dec 2025", o="B", neo=[None, "Networks not stated."], src=[["My Daily: youth strategy, Aug 2026", MYDAILY]]),
        ]},
        {"id": "4.2", "ic": "gauge", "name": "Instalment & lease", "blurb": "₩157bn revenue in H1.", "div": "kbc", "rev": "auto", "products": [
            P("lease", "Instalment finance & leasing", "Revenue of ₩157.3 billion in H1 2026, up 15.2%, about 5.7% of operating revenue.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Toyo Economy: H1 2026 analysis, Aug 2026", SAT0807]]),
        ]},
        {"id": "4.3", "ic": "briefcase-business", "name": "Corporate & SME cards", "blurb": "Korea's largest corporate base.", "div": "corp", "rev": "card", "products": [
            P("corpcard", "Corporate cards", "The most corporate card members in Korea: 456,000 at November 2024, with ₩15.8 trillion of approvals; product design and sales being rebuilt in 2026 under a new Corporate Sales Division. Networks not stated ⚠.",
              s=["biz"], lc="everyday", st="flux", o="B", neo=[None, "Networks not stated."],
              mc="Korea's biggest corporate card book, with no public scheme partner.", src=[["Metro: 2025 strategy, Feb 2025", M0224], ["Metro: 2026 strategy, Jan 2026", M0119], ["Toyo Economy: H1 2026 results, Jul 2026", SAT0724]]),
        ]},
        {"id": "4.4", "ic": "store", "name": "Merchants", "blurb": "3.1m on preferential fees.", "div": "kbc", "rev": "card", "products": [
            P("merchant", "Merchant services", "Acquiring for card payments in Korea with an online merchant portal and sales analysis; 3.087 million merchants (95.7%) paid preferential fees of 0.4–1.45% in H1 2026 after cuts from February 2025.",
              s=["biz"], lc="beyond", o="B", neo=[0, "Korean acquiring."], src=[["Toyo Economy: H1 2026 analysis, Aug 2026", SAT0807], ["KB Card homepage", KBHOME]]),
        ]},
        {"id": "4.5", "ic": "globe", "name": "Overseas", "blurb": "Thailand leads.", "div": "overseas", "rev": "other", "products": [
            P("kbj", "KB J Capital (Thailand)", "77.4%-owned consumer finance: personal, auto and mortgage loans and appliance instalments; net income ₩11.3 billion in Q1 2026, up 58.8%.",
              s=["con"], lc="borrow", o="A", neo=[None, ""], src=[["Dealsite: overseas Q1 2026, Jun 2026", OVS]]),
            P("sea", "Cambodia & Indonesia", "KB Daehan Specialized Bank (Cambodia, 97.5%, merged with i-Finance Leasing late 2025) made ₩1.7 billion in Q1 2026; KB Finansia Multi Finance (Indonesia, since 2020) lost ₩3.6 billion, held back by BNPL. Overseas profit ₩18.8 billion in H1 2026. The Myanmar office is being closed (approved December 2025).",
              s=["con"], lc="borrow", o="A", neo=[None, ""], src=[["Dealsite: overseas Q1 2026, Jun 2026", OVS], ["MTN: KB CEO process, Sep 2026", MTN], ["Yonhap Infomax: Myanmar exit, Mar 2026", MYANMAR]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach KB Card: the KB Pay app with 9 million monthly users, KB Kookmin Bank's branches and apps, and partners from Naver Pay and Toss to Korean Air and Macao's tourism office.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "KB Pay", "blurb": "9.1 million monthly users.", "div": "kbpay", "rev": "card", "products": [
            P("kbpay", "KB Pay app", "KB Card's all-in-one finance app (October 2020): 14 million sign-ups by February 2025 and 9.10 million monthly users in Q1 2026, beside KB Star Banking's 14.07 million in a group total of 33.84 million.",
              s=["con", "young"], lc="everyday", ay="Oct 2020", o="B", neo=[0, ""], src=[["Toyo Economy: KB Pay 14 million, Feb 2025", KBPAY25], ["Dealsite TV: group MAU, Jul 2026", MAU26]]),
            P("shoptravel", "KB Pay Shopping & Travel", "Non-financial shopping and travel inside KB Pay, with 5.78 million sign-ups about 15 months after launch (February 2025).",
              s=["con", "trav"], lc="beyond", o="B", neo=[0, ""], src=[["Toyo Economy: KB Pay 14 million, Feb 2025", KBPAY25]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "KB group", "blurb": "Bank branches, Star Banking.", "div": "kbfg", "rev": "card", "products": [
            P("branches", "KB Kookmin Bank channels", "Cards sold through KB Card's site, app, call centre and branches and KB Kookmin Bank branches; KB Financial runs a hub model with KB Star Banking and separate apps rather than one super-app.",
              s=["con"], lc="open", o="P", at="KB Kookmin Bank", neo=[0, ""], src=[["Insight: HERITAGE Smart, Jan 2023", HSMART], ["Dealsite TV: group MAU, Jul 2026", MAU26]]),
        ]},
        {"id": "5.3", "ic": "plug", "name": "Partners", "blurb": "Wallets, airlines, tourism.", "div": "kbc", "rev": "card", "products": [
            P("partners", "Partner channels", "Naver Pay, Kakao Pay and Toss Pay as linked wallets on NEED Pay; Korean Air SkyPass; the Macao Government Tourism Office and Mastercard Korea; KT co-brands.",
              s=["con", "trav", "corp"], lc="open", o="P", at="Naver Pay, Kakao Pay, Toss, Korean Air, MGTO", neo=[None, ""], src=[["Herald: KB NEED Pay, May 2026", NEEDPAY], ["Macao Government Information Bureau, Oct 2025", MACAO], ["Dailian: HERITAGE Classic, Dec 2024", HCLASSIC]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at KB Card", "blurb": "Premium, travel debit, stablecoins.", "products": [
        P("mcatkb", "Mastercard at KB Card", "Mastercard is the international brand on KB's premium and lifestyle cards (HERITAGE, KB YOU Prime), its Travelers check card with Travel Rewards and a Macao edition, and the network for its 2026 stablecoin test. But KB built K-World on JCB and UnionPay to avoid scheme fees, offers JCB beside Mastercard on new cards, and is working with Visa on agent payments and Apple Pay. No network agreement is public.",
          s=["con"], div="kbc", rev="card", mc="The relationship this map is drawn for.",
          src=[["Metro: KB YOU Prime, Feb 2026", YOUPRIME], ["Herald: travel offers, Nov 2025", TRAVEV], ["Bloomingbit (ETNews): Mastercard CPP, Sep 2026", CPP]]),
    ]},
    {"id": "pillar-market", "name": "Korean cards", "blurb": "Fee cuts, funding costs, agents.", "products": [
        P("market", "The Korean market", "Six main issuers made ₩1.19 trillion in H1 2026 (+6.5%), with Samsung, Shinhan and KB first to third; merchant fees cut again from February 2025; card bond yields up to about 4.55%; Hyundai still alone on Apple Pay; and stablecoin rules pending.",
          s=["con"], div="kbc", rev="card", src=[["Bizwatch: six issuers' H1 2026", BIZW], ["Toyo Economy: H1 2026 analysis, Aug 2026", SAT0807], ["The Fact: Apple Pay test, Jun 2026", APTF]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
