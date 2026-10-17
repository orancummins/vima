"""Shinhan Card's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the company's own, as Shinhan Financial Group reports them, unless a source says otherwise:
the 2Q 2026 results (23 July 2026) and the FY2025 results. Press releases are Shinhan Card's own, in
Korean. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it,
2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

SFG2Q26 = "https://shinhangroup.com/en/ir/finance/investorPresentations/detail/33172"
SFGFY25 = "https://shinhangroup.com/en/ir/finance/investorPresentations/detail/32336"
GURU = "https://www.theguru.co.kr/news/article.html?no=105078"
MTOVS = "https://www.mt.co.kr/en/finance/2026/08/18/2026081414034446086"
YAHOO = "https://finance.yahoo.com/markets/crypto/articles/south-koreas-largest-card-issuer-165911022.html"
HIST = "https://www.shinhancard.com/pconts/company/html/intro/history/yearSh/shc{}.html"
H26, H25, H24, H23, H22, H21, H20, H15, H07, H08 = (HIST.format(y) for y in (2026, 2025, 2024, 2023, 2022, 2021, 2020, 2015, 2007, 2008))
PRESS = "https://www.shinhancard.com/pconts/company/html/promotion/press/{}_3999.html"
AGENT = "https://shinhangroup.com/kr/archive/press/detail/692"
MCAGENT = "https://www.mastercard.com/news/ap/en/newsroom/press-releases/en/2026/mastercard-completes-korea-s-first-live-agentic-transactions-unlocking-trusted-ai-powered-commerce/"
FFN = "https://ffnews.com/newsarticle/paytech/mastercard-completes-koreas-first-live-agentic-transactions-unlocking-trusted-ai-powered-commerce/"
ALLIANCE = "https://shinhangroup.com/kr/archive/press/detail/742"
POC = PRESS.format(1238732)
SOLANA = PRESS.format(1238976)
SOLT300 = PRESS.format(1238381)
SOLT150 = PRESS.format(1233575)
SOLTJ = PRESS.format(1233252)
SIMPLE = PRESS.format(1237936)
BENZ = PRESS.format(1238733)
BESTX = PRESS.format(1234354)
BESTXO = PRESS.format(1236254)
CNEO = PRESS.format(1236751)
CAIR = "https://biz.sbs.co.kr/amp/article/20000332490"
HARU = PRESS.format(1234731)
UPI = PRESS.format(1234848)
E9 = PRESS.format(1234358)
TRIP = PRESS.format(1233247)
LINEUP = "https://www.shinhancard.com/pconts/html/landing/bestCardB.html"
AIRONE = "https://www.shinhancard.com/pconts/html/card/micro/air_one_micro.html"
FAME = PRESS.format(1236269)
SOLFDS = PRESS.format(1235068)
MYDATA = PRESS.format(1234620)
AINA = PRESS.format(1235070)
AISOLA = PRESS.format(1233240)
PLAN = PRESS.format(1235927)
TEEN = PRESS.format(1234621)
ORG = PRESS.format(1234622)
STRAT = PRESS.format(1235066)
ABS25 = PRESS.format(1236007)
LOAN25 = PRESS.format(1234624)
ABS26 = PRESS.format(1237937)
LEAK = "https://www.shinhancard.com/pconts/html/helpdesk/dataRoom/MOBFM164/1237028_1118.html"
SVFC = "https://shinhanfinance.com.vn/en/news/post/92695/shinhan-finance-cooperates-comprehensively-with-strategic-partners"
MWG = PRESS.format(1233576)
APIN = "https://www.insight.co.kr/news/505863"
APDAUM = "https://v.daum.net/v/20260123081204682"
BCWIKI = "https://ko.wikipedia.org/wiki/%EB%B9%84%EC%94%A8%EC%B9%B4%EB%93%9C"
MERCH = "https://sateconomy.co.kr/news/view/1065574609764746"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · heritage · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: ₩44 trillion of assets and ₩253 billion of profit in the half, LG Card's franchise inside Shinhan Financial Group since 2007, funding raised in Seoul and abroad, and a strategy built on the Plan cards, AI agents and digital assets.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & earnings", "blurb": "₩253bn in H1, second in Korea.", "div": "shc", "rev": "card", "products": [
            P("balance", "Balance sheet & earnings", "Net income of ₩253.4 billion in H1 2026 (up 2.8%) and ₩476.7 billion in 2025 (down 16.7%); total assets of ₩44.1 trillion, ROE 6.07%; delinquency 1.21% at June 2026, down from a 1.61% peak in March 2025. Second to Samsung Card on half-year profit.",
              s=["con"], neo=[0, ""], src=[["SFG 2Q 2026 results", SFG2Q26], ["SFG FY2025 results", SFGFY25], ["The Guru: issuers' H1 2026", GURU]]),
            P("volume", "Customers & volume", "About 28 million cardholders ⚠ and ₩235.7 trillion of transactions in 2025; ₩123.4 trillion in H1 2026 (up 7.6%), of which ₩16.1 trillion on check (debit) cards.",
              s=["con"], neo=[0, ""], src=[["SFG 2Q 2026 results", SFG2Q26], ["Yahoo Finance: Shinhan Card and Solana", YAHOO]]),
        ]},
        {"id": "1.2", "ic": "badge-check", "name": "Heritage & ownership", "blurb": "LG Card inside Shinhan since 2007.", "div": "sfg", "rev": "card", "products": [
            P("heritage", "Shinhan Financial Group & LG Card", "Wholly owned by Shinhan Financial Group (KRX and NYSE listed); the integrated Shinhan Card launched on 1 October 2007 from the old Shinhan Card and LG Card, with IT merged in August 2008.",
              s=["con"], o="I", neo=[0, ""], src=[["Shinhan Card history 2007", H07], ["Shinhan Card history 2008", H08], ["SFG 2Q 2026 results", SFG2Q26]]),
        ]},
        {"id": "1.3", "ic": "scale", "name": "Leadership & controls", "blurb": "Park Chang-hoon since 2025.", "div": "shc", "rev": "card", "products": [
            P("leadership", "Leadership", "CEO Park Chang-hoon since January 2025 (term after 2026 not confirmed ⚠); Executive Vice President Kim Young-il led the Solana deal. The organisation was cut to 4 groups, 20 divisions and 58 departments in June 2025.",
              s=["corp"], neo=[0, ""], src=[["Shinhan Card history 2025", H25], ["Solana MOU, Apr 2026", SOLANA], ["Reorganisation, Jun 2025", ORG]]),
            P("controls", "Data protection & consumer protection", "In December 2025 Shinhan disclosed that staff leaked 192,088 merchant owners' phone numbers, and some names and birth dates, to sell cards; CEO Park apologised and promised compensation.",
              s=["merch"], st="flux", neo=[0, ""], src=[["Shinhan Card: leak notice, Dec 2025", LEAK]]),
        ]},
        {"id": "1.4", "ic": "coins", "name": "Funding", "blurb": "Bonds, ABS and dollar loans.", "div": "shc", "rev": "finance", "products": [
            P("funding", "Funding", "₩29.4 trillion of funding, 71% debentures; US$700 million raised abroad in 2025 (HSBC-led US$300 million loan, US$400 million social ABS rated Aaa by Moody's), a US$250 million ABS with Société Générale (February 2026) and a US$400 million Formosa bond (June 2026).",
              s=["corp"], neo=[0, ""], src=[["SFG 2Q 2026 results", SFG2Q26], ["Social ABS, Sep 2025", ABS25], ["Syndicated loan, Jun 2025", LOAN25], ["ABS, Feb 2026", ABS26], ["Shinhan Card history 2026", H26]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & AI", "blurb": "Plan cards, AI agents, tokens.", "div": "shc", "rev": "card", "products": [
            P("strategy", "Strategy", "One flagship card family (the Plan series), products built with Shinhan Bank, AI agents and stablecoin payments; the H2 2025 strategy meeting centred on AI agents.",
              s=["corp"], neo=[0, ""], src=[["Strategy meeting, Jul 2025", STRAT], ["Plan series 1 million, Sep 2025", PLAN]]),
            P("aina", "AINa & the Agentic AI Alliance", "AINa, an in-house generative-AI platform for staff (July 2025), and the only private financial firm in the science ministry's Agentic AI Alliance of about 250 organisations (April 2026).",
              s=["corp"], st="new", ay="Apr 2026", neo=[0, ""], src=[["AINa, Jul 2025", AINA], ["Agentic AI Alliance, Apr 2026", ALLIANCE]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Eight ways money moves: Plan cards and premium cards sold domestic-only or on Mastercard, Korean rails for every domestic purchase, the SOL Travel check card on Mastercard, Visa, Amex, JCB and UnionPay on other cards, wallets, Agent Pay with Mastercard, and stablecoin tests.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Plan series", "blurb": "1 million+ flagship cards.", "div": "shc", "rev": "card", "products": [
            P("plan", "Plan series", "Shinhan's flagship card family (Point, Discount, Edu, ECO, Hi-Point and SOL Plan), past 1 million cards in about 18 months to September 2025; sold domestic-only or with Mastercard for overseas use.", short="Plan series (domestic or Mastercard)",
              s=["con"], lc="everyday", o="B", neo=[1, "Mastercard on the international version."],
              mc="Mastercard is the brand on Shinhan's flagship line, but only when customers pay for overseas use.",
              src=[["Plan series 1 million, Sep 2025", PLAN], ["Shinhan Card history 2026", H26]]),
            P("simple", "Simple Plan & Simple Plan+", "1–1.5% off at home and 2% abroad with no conditions (February 2026); ₩15,000 a year domestic-only or ₩18,000 on Mastercard.", short="Simple Plan (domestic or Mastercard)",
              s=["con"], lc="everyday", st="new", ay="Feb 2026", neo=[1, "Domestic-only or Mastercard."], src=[["Simple Plan, Feb 2026", SIMPLE]]),
        ]},
        {"id": "2.2", "ic": "gem", "name": "Premium cards", "blurb": "Mastercard, Amex and Visa.", "div": "shc", "rev": "card", "products": [
            P("bestx", "The BEST-X & The BEST-XO", "Shinhan's first premium card in six years (February 2025, upgraded October 2025), about ₩300,000 a year; the Mastercard version adds valet parking at Incheon Airport and hotels.", short="The BEST-X (Mastercard)",
              s=["prem"], lc="everyday", st="new", ay="Feb 2025", neo=[1, "Domestic-only or Mastercard."], src=[["The BEST-X, Feb 2025", BESTX], ["The BEST-XO, Oct 2025", BESTXO]]),
            P("cneo", "The CLASSIC NEO", "Premium card where the customer picks the categories that earn up to 5% (November 2025); domestic-only or Mastercard Platinum.", short="The CLASSIC NEO (Mastercard)",
              s=["prem"], lc="everyday", st="new", ay="Nov 2025", neo=[1, "Domestic-only or Mastercard Platinum."], src=[["The CLASSIC NEO, Nov 2025", CNEO]]),
            P("benz", "Mercedes-Benz Shinhan Card", "Premium PLCC in three tiers, up to ₩700,000 a year, with metal plates (April 2026); domestic-only or Mastercard.", short="Mercedes-Benz (Mastercard)",
              s=["prem"], lc="everyday", st="new", ay="Apr 2026", o="P", at="Mercedes-Benz Korea", neo=[1, "Domestic-only or Mastercard."], src=[["Mercedes-Benz Shinhan Card, Apr 2026", BENZ]]),
            P("cair", "The CLASSIC Air", "Korean Air miles plus MyShinhan points (September 2026); ₩147,000 domestic-only or ₩150,000 on American Express.", short="The CLASSIC Air (Amex)",
              s=["prem", "trav"], lc="everyday", st="new", ay="Sep 2026", at="American Express", neo=[0, "American Express."],
              mc="A 2026 premium launch went to Amex, not Mastercard.", src=[["SBS Biz: The CLASSIC Air, Sep 2026", CAIR]]),
            P("bestf", "The BEST-F", "Premium mileage card; the mileage version is shown on Visa ⚠ undated page.", short="The BEST-F (Visa)",
              s=["prem", "trav"], lc="everyday", neo=[0, "Visa."], src=[["Shinhan Card: mileage cards", AIRONE]]),
        ]},
        {"id": "2.3", "ic": "network", "name": "Domestic rails", "blurb": "Domestic-only cards, S&, BC.", "div": "shc", "rev": "card", "products": [
            P("domestic", "Domestic-only cards & Korean processing", "Every flagship card comes in a cheaper domestic-only version, about ₩3,000 a year less; purchases in Korea are processed by Shinhan on Korean rails whatever the brand ⚠.", short="Domestic-only cards",
              s=["con", "merch"], lc="everyday", o="B", neo=[0, "Korean rails."],
              mc="Most of Shinhan's volume is domestic and never needs a scheme.", src=[["Simple Plan, Feb 2026", SIMPLE], ["Mercedes-Benz Shinhan Card, Apr 2026", BENZ]]),
            P("sand", "S& brand", "Shinhan's own brand offered as a cheaper option on older cards such as Deep Oil, Edu and Mr.Life ⚠ status unclear.",
              s=["con"], lc="everyday", st="unconf", neo=[0, "Shinhan's own brand."], src=[["Shinhan Card: card line-up", LINEUP]]),
            P("bc", "BC Card", "Shinhan took on Chohung Bank's BC card business and later issued BC cards through Jeju Bank; it now reportedly issues only one UnionPay home-shopping card under BC ⚠.",
              s=["con"], lc="everyday", st="retired", o="I", at="BC Card (KT)", neo=[0, "BC Card."], src=[["Wikipedia (ko): BC Card", BCWIKI]]),
        ]},
        {"id": "2.4", "ic": "plane", "name": "Travel check cards", "blurb": "SOL Travel: 3 million on Mastercard.", "div": "shc", "rev": "card", "products": [
            P("soltravel", "SOL Travel check card", "Travel debit card built with Shinhan Bank (February 2024): 42 currencies with no FX margin, no overseas fees, and Mastercard Travel Rewards cashback; 3 million cards and ₩5.4 trillion of spending by March 2026.", short="SOL Travel (Mastercard)",
              s=["trav", "con"], lc="move", ay="Feb 2024", o="P", at="Shinhan Bank, Mastercard", neo=[2, "Mastercard, with Travel Rewards."],
              mc="Shinhan's biggest Mastercard debit franchise.", src=[["SOL Travel 1.5 million, Nov 2024", SOLT150], ["SOL Travel 3 million, Mar 2026", SOLT300]]),
            P("soltj", "SOL Travel J check card", "Japan version (May 2025): 50% off at Don Quijote and Starbucks Japan, and Mastercard Travel Rewards in Japan until December 2026.", short="SOL Travel J (Mastercard)",
              s=["trav"], lc="move", st="new", ay="May 2025", neo=[2, "Mastercard Travel Rewards."], src=[["SOL Travel J, May 2025", SOLTJ]]),
        ]},
        {"id": "2.5", "ic": "earth", "name": "Visa, JCB & UnionPay", "blurb": "The other brands.", "div": "shc", "rev": "card", "products": [
            P("visamass", "Visa cards", "Older mass cards B.Big, YOLO, Mr.Life, RPM+ Platinum# and YaY carry Visa for overseas use ⚠ undated page.", short="Mass cards (Visa)",
              s=["con"], lc="everyday", neo=[0, "Visa."], src=[["Shinhan Card: card line-up", LINEUP]]),
            P("haru", "Haru (Hoshino Resorts)", "Japan travel credit card launched with JCB International's president (June 2025): 2% back abroad, 3.5% in Japan, up to 30% off at Hoshino Resorts; JCB (URS Platinum).", short="Haru (JCB)",
              s=["trav"], lc="everyday", st="new", ay="Jun 2025", o="P", at="JCB, Hoshino Resorts", neo=[0, "JCB."], src=[["Haru, Jun 2025", HARU]]),
            P("upi", "UnionPay cards & QR", "UnionPay versions of some cards; UnionPay QR in SOL Pay (September 2023), linked to WeChat Pay merchants in China (February 2025).", short="UnionPay & WeChat Pay",
              s=["trav"], lc="move", ay="Sep 2023", o="P", at="UnionPay, WeChat Pay", neo=[0, "UnionPay."], src=[["UnionPay QR and WeChat Pay, Feb 2025", UPI]]),
        ]},
        {"id": "2.6", "ic": "wallet", "name": "Wallets", "blurb": "SOL Pay NFC; Apple Pay pending.", "div": "solpay", "rev": "card", "products": [
            P("nfc", "SOL Pay overseas NFC", "Contactless payment abroad from SOL Pay for Visa, Mastercard and UnionPay Shinhan cards.",
              s=["trav"], lc="move", neo=[1, "Visa, Mastercard and UnionPay."], src=[["UnionPay QR and WeChat Pay, Feb 2025", UPI]]),
            P("applepay", "Apple Pay", "The regulator approved Shinhan's Apple Pay terms in June 2025 and a launch was expected in 2026; not confirmed live by October 2026 ⚠. Hyundai Card has been alone on Apple Pay in Korea since March 2023.",
              s=["con"], lc="move", st="unconf", o="P", at="Apple", neo=[None, "Network not announced."],
              mc="Wallet tokens would ride on whichever brand each card carries.", src=[["Insight: Apple Pay terms approved, Jun 2025", APIN], ["Daum: Hyundai alone on Apple Pay, Jan 2026", APDAUM]]),
        ]},
        {"id": "2.7", "ic": "bot", "name": "Agent Pay", "blurb": "Korea's first live AI payment.", "div": "shc", "rev": "card", "products": [
            P("agentpay", "AI Agent Pay with Mastercard", "Korea's first live agentic card payment (March 2026): an AI agent booked and paid for a car from Incheon Airport through hoppa on Mastercard Agent Pay. Shinhan says it co-designed authentication, the payment flow and merchant integration, and will extend it to travel and shopping.", short="Agent Pay (Mastercard)",
              s=["con", "trav"], lc="move", st="new", ay="Mar 2026", o="P", at="Mastercard", neo=[3, "Mastercard Agent Pay."],
              mc="The deepest joint work: Mastercard's own product, co-designed with Shinhan. Mastercard's release does not name the issuer ⚠.",
              src=[["SFG: Agent Pay with Mastercard, Mar 2026", AGENT], ["Mastercard: Korea's first agentic transactions", MCAGENT], ["FF News, Mar 2026", FFN]]),
        ]},
        {"id": "2.8", "ic": "coins", "name": "Digital money", "blurb": "Stablecoin tests, Solana.", "div": "shc", "rev": "other", "products": [
            P("stablepoc", "Stablecoin & blockchain proofs of concept", "Six tests completed (April 2026): a hybrid card spending stablecoin in check mode and using it as collateral in credit mode, with Fireblocks and Mastercard; stablecoin cross-border settlement with Visa; P2P payments, external wallets and a hardware-wallet IC card.", short="Stablecoin PoCs (Mastercard and Visa)",
              s=["con", "corp"], lc="move", st="new", ay="Apr 2026", o="P", at="Mastercard, Visa, Fireblocks, Solana", neo=[1, "Mastercard hybrid card; Visa settlement."],
              src=[["Stablecoin PoCs, Apr 2026", POC]]),
            P("solana", "Solana partnership", "MOU with the Solana Foundation (30 April 2026): a 2026 testnet pilot of customer-to-merchant stablecoin payments, non-custodial wallets and a hybrid TradFi and DeFi model.",
              s=["con"], lc="move", st="new", ay="Apr 2026", o="P", at="Solana Foundation", neo=[0, ""], src=[["Solana MOU, Apr 2026", SOLANA], ["Yahoo Finance: Shinhan Card and Solana", YAHOO]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every card: fraud checks fed by telecom data, a data business and MyData for 8 million users, MyShinhan points and partner cards, and AI in the contact centre.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & scams", "blurb": "Telecom data in the FDS.", "div": "shc", "rev": "card", "products": [
            P("fame", "FDS with SK Telecom FAME", "The card industry's first fraud system combining telecom and card data (October 2025): suspicious calls, URLs and malicious apps flagged by SK Telecom's FAME stop payments in real time.",
              s=["con"], lc="everyday", st="new", ay="Oct 2025", o="P", at="SK Telecom", neo=[0, "Shinhan's own, with SK Telecom."], src=[["FAME, Oct 2025", FAME]]),
            P("solfds", "SOL Pay scam guard", "Malicious-app detection in SOL Pay fed to the FDS stopped 218 voice-phishing cases worth ₩3.5 billion in a year (July 2025), with family phishing alerts for older customers.",
              s=["con"], lc="everyday", neo=[0, ""],
              mc="Voice phishing is the pressing problem; Mastercard scam and identity tools could add to Shinhan's own.", src=[["SOL Pay scam guard, Jul 2025", SOLFDS]]),
        ]},
        {"id": "3.2", "ic": "database", "name": "Data & MyData", "blurb": "8 million MyData users.", "div": "data", "rev": "other", "products": [
            P("databiz", "Data business", "Korea's first private data alliance, GranData (October 2021), the first personal-business credit bureau licence in finance (October 2021) and the Data Bada marketplace (August 2024).",
              s=["corp", "merch"], lc="beyond", o="B", neo=[0, ""], src=[["Shinhan Card history 2021", H21], ["Shinhan Card history 2024", H24]]),
            P("mydata", "MyData", "Personal asset and spending management for 8 million users; MyData 2.0 from June 2025, and a spending-log service from January 2026.",
              s=["con"], lc="grow", neo=[0, ""], src=[["MyData 2.0, Jun 2025", MYDATA], ["Shinhan Card history 2026", H26]]),
            P("visadata", "Visa data partnership", "A data-business MOU with Visa (September 2020).",
              s=["corp"], lc="beyond", ay="Sep 2020", o="P", at="Visa", neo=[0, "Visa."], src=[["Shinhan Card history 2020", H20]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards & partner cards", "blurb": "Points, miles, PLCCs.", "div": "shc", "rev": "card", "products": [
            P("points", "MyShinhan points & miles", "MyShinhan points across the Plan series, and Korean Air and Asiana mileage cards; automatic point use for customers over 65 (February 2026).",
              s=["con", "trav"], lc="grow", neo=[0, ""], src=[["The BEST-X, Feb 2025", BESTX], ["Shinhan Card: card line-up", LINEUP], ["Shinhan Card history 2026", H26]]),
            P("plcc", "Partner cards (PLCC)", "Co-brands with Kakao Bank, Toss, Naver Pay, GS Retail, Coway, LG Electronics, Shinsegae, E-mart, Baemin and Mercedes-Benz, among others.",
              s=["con"], lc="everyday", o="P", at="Kakao Bank, Toss, Naver Pay and others", neo=[None, "Networks vary by card."],
              src=[["Shinhan Card history 2025", H25], ["Shinhan Card history 2026", H26]]),
        ]},
        {"id": "3.4", "ic": "headset", "name": "AI in service", "blurb": "AI-SOLa for agents.", "div": "shc", "rev": "card", "products": [
            P("aisola", "AI-SOLa", "Generative-AI support for contact-centre staff (January 2025): speech to text and a small language model suggest answers in real time.",
              s=["con"], lc="everyday", st="new", ay="Jan 2025", neo=[0, ""], src=[["AI-SOLa, Jan 2025", AISOLA]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: card spending and card loans, auto finance and leasing, merchant and SME services, cards for foreigners in Korea, and consumer finance in Vietnam, Kazakhstan and Indonesia.",
    "tiles": [
        {"id": "4.1", "ic": "hand-coins", "name": "Consumer credit", "blurb": "Card loans ₩8.2tn.", "div": "shc", "rev": "finance", "products": [
            P("cardvol", "Card spending", "Credit purchases of ₩19.2 trillion on the balance sheet at June 2026; card business revenue ₩1.69 trillion in H1 2026 (up 3.5%).",
              s=["con"], lc="everyday", neo=[1, "International versions mostly Mastercard on new cards; domestic volume on Korean rails."], src=[["SFG 2Q 2026 results", SFG2Q26]]),
            P("loans", "Card loans & cash advances", "Card loans of ₩8.2 trillion and cash advances of ₩1.4 trillion at June 2026; new card-loan lending fell 5.2% in H1 2026.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["SFG 2Q 2026 results", SFG2Q26]]),
        ]},
        {"id": "4.2", "ic": "gauge", "name": "Auto & lease", "blurb": "Shinhan MyCar.", "div": "mycar", "rev": "auto", "products": [
            P("mycar", "Shinhan MyCar, lease & instalments", "Auto finance platform past ₩1 trillion of lending (February 2022); ₩4.0 trillion of lease assets and ₩3.4 trillion of instalment finance at June 2026.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Shinhan Card history 2022", H22], ["SFG 2Q 2026 results", SFG2Q26]]),
        ]},
        {"id": "4.3", "ic": "store", "name": "Merchants & SMEs", "blurb": "Biz cards, MySHOP.", "div": "shc", "rev": "card", "products": [
            P("biz", "Business cards", "Biz Plan (November 2024), Npay biz for sole traders with Naver Pay (October 2025) and the SOHO SOLution card (2025) ⚠ networks not stated.",
              s=["merch", "corp"], lc="everyday", neo=[None, "Networks not stated."],
              mc="Commercial cards are an open question for Mastercard.", src=[["Shinhan Card history 2024", H24], ["Shinhan Card history 2025", H25]]),
            P("myshop", "MySHOP Partner", "Tools for small merchants: MySHOP Together growth services (July 2023), a support-programme search (April 2024) and weekend loans against card receivables (June 2020), under merchant fees cut again from February 2025.",
              s=["merch"], lc="beyond", neo=[0, ""], src=[["Shinhan Card history 2023", H23], ["Shinhan Card history 2024", H24], ["Shinhan Card history 2020", H20], ["Sateconomy: merchant fees cut, Feb 2025", MERCH]]),
        ]},
        {"id": "4.4", "ic": "users-round", "name": "Foreigners in Korea", "blurb": "TripPASS, E9pay.", "div": "shc", "rev": "card", "products": [
            P("trippass", "TripPASS", "Mobile passport, payments and won transfers for inbound visitors (March 2025), with a prepaid card loaded at CU and GS25 or from Mastercard, Amex and JCB cards.",
              s=["foreign"], lc="open", st="new", ay="Mar 2025", o="P", at="Road System", neo=[None, "Prepaid card's network not stated."], src=[["TripPASS, Mar 2025", TRIP]]),
            P("e9pay", "E9pay Shinhan Card & SOL Global", "Credit card for foreign residents with remittance firm E9pay (May 2025), guidance in 16 languages; domestic-only or Mastercard. SOL Global check cards for residents (September 2024).", short="E9pay card (Mastercard)",
              s=["foreign"], lc="open", st="new", ay="May 2025", o="P", at="E9pay", neo=[1, "Domestic-only or Mastercard."], src=[["E9pay card, May 2025", E9], ["Shinhan Card history 2024", H24]]),
        ]},
        {"id": "4.5", "ic": "globe", "name": "Overseas", "blurb": "Vietnam leads.", "div": "overseas", "rev": "other", "products": [
            P("svfc", "Shinhan Vietnam Finance", "Consumer finance and THE FIRST credit card, launched with Mastercard in 2022; ₩10.7 billion profit in H1 2026 (up 175%); Mobile World MOU (December 2024).", short="Vietnam (Mastercard)",
              s=["con"], lc="borrow", ay="Aug 2022", o="A", at="Mastercard", neo=[2, "THE FIRST card on Mastercard."], src=[["Shinhan Finance: THE FIRST", SVFC], ["Money Today: overseas H1 2026", MTOVS], ["Mobile World MOU, Dec 2024", MWG]]),
            P("overseas", "Kazakhstan, Indonesia & Myanmar", "Shinhan Finance in Kazakhstan (2015; auto joint venture with Aster in 2024), Shinhan Indo Finance (2015) and Myanmar microfinance; ₩6.0 billion, ₩2.6 billion and a ₩0.5 billion loss in H1 2026.",
              s=["con"], lc="borrow", neo=[None, ""], src=[["Money Today: overseas H1 2026", MTOVS], ["Shinhan Card history 2015", H15], ["Shinhan Card history 2024", H24]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Shinhan Card: the SOL Pay app, the group's Super SOL app and bank-built products, and partners from Kakao Bank and Toss to car dealers.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "SOL Pay", "blurb": "About 9.8 million monthly users.", "div": "solpay", "rev": "card", "products": [
            P("solpay", "SOL Pay app", "Shinhan Card's app (earlier pLay and PayFAN ⚠): about 9.8 million monthly users in H1 2026 ⚠ read from a chart; QR, NFC, transit and MyData inside.",
              s=["con", "trav"], lc="everyday", neo=[0, ""], src=[["SFG 2Q 2026 results", SFG2Q26], ["Shinhan Card history 2024", H24]]),
            P("teen", "SOL Pay Cheoeum", "A teen-only app and prepaid card (June 2025), the card industry's first.",
              s=["con"], lc="open", st="new", ay="Jun 2025", neo=[None, ""], src=[["SOL Pay Cheoeum, Jun 2025", TEEN]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Shinhan group", "blurb": "Super SOL, SOL Plan+.", "div": "sfg", "rev": "card", "products": [
            P("supersol", "Super SOL & bank-built cards", "The group's all-in-one app passed 11 million monthly users after its mid-2026 relaunch; SOL Plan+ (June 2026) links card spending to bank savings, and SOL Travel is sold with Shinhan Bank.",
              s=["con"], lc="open", st="new", ay="Jun 2026", o="P", at="Shinhan Bank", neo=[0, ""], src=[["SFG 2Q 2026 results", SFG2Q26], ["Shinhan Card history 2026", H26]]),
        ]},
        {"id": "5.3", "ic": "plug", "name": "Partner channels", "blurb": "Kakao Bank, Toss, dealers.", "div": "shc", "rev": "card", "products": [
            P("partners", "Partner channels", "Cards sold through Kakao Bank (2025–26), Toss (July 2026), Naver Pay, E9pay's app and Mercedes-Benz's new-car links.",
              s=["con", "prem", "foreign"], lc="open", o="P", at="Kakao Bank, Toss, Naver Pay, E9pay", neo=[None, ""], src=[["Shinhan Card history 2026", H26], ["E9pay card, May 2025", E9], ["Mercedes-Benz Shinhan Card, Apr 2026", BENZ]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Shinhan Card", "blurb": "The default overseas brand, and Agent Pay.", "products": [
        P("mcatshinhan", "Mastercard at Shinhan Card", "Mastercard is the overseas brand on Shinhan's new flagship and premium cards from 2025–26 and on the SOL Travel check card, and its partner for Korea's first live Agent Pay transaction (March 2026). But domestic purchases run on Korean rails, older cards carry Visa, and Amex (The CLASSIC Air), JCB (Haru) and UnionPay have places too; no network agreement is public.",
          s=["con"], div="shc", rev="card", mc="The relationship this map is drawn for.",
          src=[["SFG: Agent Pay with Mastercard, Mar 2026", AGENT], ["Simple Plan, Feb 2026", SIMPLE], ["SOL Travel 3 million, Mar 2026", SOLT300]]),
    ]},
    {"id": "pillar-market", "name": "Korean cards", "blurb": "Fee cuts, wallets, stablecoins.", "products": [
        P("market", "The Korean market", "Six main issuers, with Samsung first and Shinhan second on H1 2026 profit; merchant fees cut again from February 2025; Hyundai alone on Apple Pay; card bonds at about 4.55%; and a proposed Digital Asset Basic Act for stablecoins.",
          s=["con"], div="shc", rev="card", src=[["The Guru: issuers' H1 2026", GURU], ["Sateconomy: merchant fees cut, Feb 2025", MERCH], ["Daum: Hyundai alone on Apple Pay, Jan 2026", APDAUM], ["Yahoo Finance: Shinhan Card and Solana", YAHOO]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
