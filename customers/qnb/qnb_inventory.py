"""QNB Group's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own as reported by Qatar News Agency, Gulf Times and The Peninsula: the nine-month
2026 results (8 October 2026), the H1 2026 results (8 July 2026) and the 2025 results (13 January 2026).
QNB's own site was not reachable; product pages were read from 2025 archive copies and are cited at their
qnb.com address. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it,
2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q9M26 = "https://www.gulf-times.com/article/735421/business/qnb-group-9-month-net-profit-surges-4-to-qr133bn"
Q9M26QNA = "https://qna.org.qa/en/News-Area/News/2026-10/8/qnb-group-net-profit-rises-4-percent-in-first-nine-months-of-2026"
H126 = "https://www.gulf-times.com/article/728855/business/qnb-group-h1-net-profit-surges-3-y-o-y-to-qr87bn"
AGBI = "https://www.agbi.com/banking-finance/2026/07/risk-management-helps-qnb-net-profit-rise-in-second-quarter/"
FY25 = "https://thepeninsulaqatar.com/article/13/01/2026/qnb-group-profits-rise-17-in-2025"
FY25AB = "https://www.theasianbanker.com/press-releases/qnb-group-reports-5-1-billion-net-profit-before-pillar-two-taxes-for-2025"
RATINGS = "https://www.qnb.com/sites/qnb/qnbqatar/page/en/encreditrating.html"
EXCO = "https://www.qnb.com/sites/qnb/qnbqatar/page/en/enexecutivemanagement.html"
AGM25 = "https://www.bankygate.com/58523/QNB-General-Assembly-approves-financial-statements-and-cash-dividend-for-shareholders"
MILKEN = "https://milkeninstitute.org/events/global-conference-2026/speakers/ali-al-kuwari"
COBRAND = "https://www.qnb.com/sites/qnb/qnbqatar/page/en/encobrandedcreditcards.html"
KSA17 = "https://www.argaam.com/en/article/articledetail/id/484720"
JEDDAH = "https://qnb.com/sites/qnb/qnbglobal/en/en23aug2023news"
VISAAWARD = "https://www.gulf-times.com/article/680084/business/qnb-group-wins-fastest-growing-credit-card-portfolio-in-qatar-accolade-from-visa"
QRAIRWAYS = "https://jobs.qnb.com/sites/qnb/qnbglobal/en/en29feb2024news"
HARRODS = "https://thepeninsulaqatar.com/article/07/04/2025/qnb-joins-hands-with-harrods-and-visa-to-provide-unrivalled-payment-experience"
WEE = "https://www.qatar-tribune.com/article/205971/BUSINESS/QNB-Mastercard-launch-exclusive-card-for-elite--customers-in-Qatar"
DIAMOND = "https://gulf-times.com/story/357167/qnb-launches-diamond-embedded-credit-card-for-vip-customers"
MCDEBIT = "https://thepeninsulaqatar.com/article/24/04/2025/qnb-and-mastercard-launch-debit-cards-campaign-to-reward-customers"
HIMYANDEBIT = "https://www.qnb.com/sites/qnb/qnbqatar/page/en/enhimyandebitcard.html"
HIMYANPP = "https://www.qnb.com/sites/qnb/qnbqatar/page/en/enhimyanprepaidcard.html"
HIMYANQCB = "https://gulf-times.com/story/728227/QCB-issues-first-national-payment-card-Himyan"
MCCOMM = "https://thepeninsulaqatar.com/article/18/04/2023/qnb-mastercard-sign-commercial-credit-cards-agreement"
MCCOMM2 = "https://www.gccbusinessnews.com/qnb-mastercard-sign-long-term-agreement-for-commercial-credit-cards/"
CORPCARD = "https://www.qnb.com/sites/qnb/qnbqatar/page/en/encorporatecreditcard.html"
HOTEL = "https://www.qnb.com/sites/qnb/qnbqatar/page/en/enintegratedpayment.html"
MCMYPOS = "https://www.mastercard.com/news/eemea/en/newsroom/press-releases/en/2023/march/mastercard-and-qnb-launch-mypos-tap-on-phone-service-for-small-businesses-in-qatar"
MYPOS = "https://www.qnb.com/sites/qnb/qnbqatar/page/en/enmypos.html"
ECOM = "https://www.qnb.com/sites/qnb/qnbqatar/page/en/enecommercepayment.html"
SIMPLIFY = "https://www.qnb.com/sites/qnb/qnbqatar/page/en/enqnbsimplify.html"
FAWRANQCB = "https://www.financemiddleeast.com/?p=3706"
FAWRANQNB = "https://ibsintelligence.com/ibsi-news/qnb-introduces-fawran-for-instant-payments-within-qatar"
QCBDEC25 = "https://www.gulf-times.com/article/718801/business/qatar-witnesses-6619mn-payment-system-transactions-valued-at-qr2009bn-in-december-2025-qcb"
MCSUDAN = "https://www.mastercard.com/news/eemea/en/newsroom/press-releases/en/2020/june/qnb-group-and-mastercard-undertake-first-successful-international-mastercard-transaction-in-sudan"
APPLEPAY = "https://www.qnb.com/sites/qnb/qnbqatar/page/en/enapplepay.html"
APPLEPAY21 = "https://dohanews.co/?p=89220"
GPAY = "https://www.qnb.com/sites/qnb/qnbglobal/en/en24aug2022news"
TRABOUT = "https://www.qnb.com.tr/en/about-qnb/about-us"
EGYPT9M = "https://www.zawya.com/en/capital-markets/banking-and-insurance/qnb-egypts-consolidated-profits-up-26.3-yoy-in-9-month-1588952"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · state anchor · reach", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: QR1.46 trillion of assets, a cost-to-income ratio near 24%, Aa2/A+ ratings, a board chaired by Qatar's Finance Minister, and a network across more than 28 countries.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & ratings", "blurb": "QR1.46tn assets, Aa2/A+.", "div": "qnb", "rev": "corp", "products": [
            P("balance", "Balance sheet & earnings", "Net profit of QR13.3 billion in the nine months to September 2026 (up 4%; QR16.4 billion before hyperinflation accounting in Türkiye); assets QR1.46 trillion, loans QR1.06 trillion, deposits QR979 billion; cost-to-income 24.3%, NPL ratio 2.7%, CAR 19.7%. 2025 profit was QR17.0 billion.",
              s=["corp"], neo=[0, ""], src=[["Gulf Times: 9M 2026 results, Oct 2026", Q9M26], ["QNA: 9M 2026 results", Q9M26QNA], ["The Peninsula: 2025 results, Jan 2026", FY25]]),
            P("ratings", "Ratings & capital", "Moody's Aa2, S&P A+ and Fitch A+ (2025 reports), the highest-rated bank in Qatar by its own account; CAR 19.7% and LCR 145% at September 2026. 2026 rating actions not checked ⚠.",
              s=["corp"], neo=[0, ""], src=[["QNB: credit ratings", RATINGS], ["Gulf Times: 9M 2026 results", Q9M26]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Ownership & leadership", "blurb": "QIA-anchored; Al-Khalifa CEO.", "div": "qnb", "rev": "corp", "products": [
            P("owners", "Ownership & board", "Listed on the Qatar Stock Exchange with the Qatar Investment Authority as anchor shareholder (stake ⚠). Ali Ahmed Al-Kuwari, Qatar's Minister of Finance, was elected chair for 2025–2027; shares closed at QR17.40 in July 2026, a market value of about QR160 billion ⚠ (computed).",
              s=["corp"], neo=[0, ""], src=[["Bankygate: 2025 general assembly", AGM25], ["Milken Institute: Ali Al-Kuwari, 2026", MILKEN], ["AGBI: H1 2026", AGBI]]),
            P("leadership", "Executive management", "Group CEO Abdulla Mubarak Al-Khalifa; Group Chief Business Officer Yousef Mahmoud Al-Neama; Adel Ali Al-Malki runs Group Retail Banking and the cards; CFO Ramzi Mari; Ömür Tan heads QNB Türkiye and Mohamed Bedeir QNB Egypt (2025 list ⚠).",
              s=["corp"], neo=[0, ""], src=[["QNB: executive management", EXCO], ["QNA: 9M 2026 results", Q9M26QNA]]),
        ]},
        {"id": "1.3", "ic": "earth", "name": "International network", "blurb": "28+ countries, two Saudi branches.", "div": "branches", "rev": "intl", "products": [
            P("network", "Group network", "More than 28 countries on three continents and more than 31,000 staff (April 2025): branches in Kuwait, Oman, the UK, France, Singapore, Hong Kong, India and elsewhere; subsidiaries in Türkiye, Egypt, Indonesia, Tunisia, Syria and Switzerland; associates in the UAE, Jordan, Iraq and Togo.",
              s=["intl", "corp"], neo=[0, ""], src=[["QNB: international network (co-branded cards page)", COBRAND], ["The Peninsula: debit campaign, Apr 2025", MCDEBIT]]),
            P("saudi", "QNB in Saudi Arabia", "QNB's first branch in Saudi Arabia opened in May 2017 and a second, in Jeddah, in August 2023, serving individuals, businesses and government; Abdulaziz Khalid Jokhdar is CEO for the Kingdom.",
              s=["corp", "intl"], ay="May 2017", neo=[0, ""],
              mc="Commercial cards for Qatari groups trading into Saudi Arabia are a natural extension of the 2023 deal.",
              src=[["Argaam: first Saudi branch, May 2017", KSA17], ["QNB: Jeddah branch, Aug 2023", JEDDAH], ["QNB: executive management", EXCO]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy & deals", "blurb": "Growth abroad, low costs.", "div": "qnb", "rev": "intl", "products": [
            P("strategy", "Strategy", "No numbered public plan was found ⚠; results stress growth outside Qatar, a cost-to-income ratio near 24%, capital near 20% and buybacks (QR2.5 billion since launch). Branches were shut for about a month after a regional conflict began in late February 2026 ⚠, and profit still rose.",
              s=["corp"], neo=[0, ""], src=[["Gulf Times: 9M 2026 results", Q9M26], ["AGBI: H1 2026", AGBI]]),
            P("deals", "Deals & funding", "Finansbank bought from National Bank of Greece in 2016 (QNB Türkiye since October 2024); Enpara separated into its own bank in August 2025; a QR1.0 billion bond in H1 2026, the largest local-currency issue by a Qatari financial institution to international investors.",
              s=["corp", "intl"], o="A", neo=[0, ""], src=[["QNB Türkiye: about us", TRABOUT], ["Gulf Times: H1 2026 results", H126]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Eight ways money moves: Visa consumer credit and the big co-brands, Mastercard for private-banking cards, debit and corporate cards, Himyan on QCB's NAPS switch, acquiring for every network with Mastercard's tap on phone, Fawran instant payments, and remittances.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Consumer credit", "blurb": "Visa, fastest-growing in Qatar.", "div": "qatar", "rev": "retail", "products": [
            P("liferewards", "QNB Life Rewards credit cards", "Visa Platinum for the Essential segment and Visa Infinite for First and First Plus clients, with Life Rewards points, up to 45 days' free credit and fee waivers; Visa named QNB's the fastest-growing credit card portfolio in Qatar in April 2024.", short="Credit (Visa)",
              s=["con", "first"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."],
              mc="The core consumer credit book is Visa's.",
              src=[["QNB: credit cards by segment", COBRAND], ["Gulf Times: Visa award, Apr 2024", VISAAWARD]]),
            P("nojoom", "QNB Ooredoo Nojoom card", "A co-branded Visa Platinum (and Platinum Retail Plus) earning Ooredoo Nojoom points.",
              s=["con"], lc="borrow", o="P", at="Ooredoo, Visa", neo=[0, "Visa."], src=[["QNB: credit cards by segment", COBRAND]]),
        ]},
        {"id": "2.2", "ic": "plane", "name": "Co-brands", "blurb": "Qatar Airways and Harrods.", "div": "qatar", "rev": "retail", "products": [
            P("qrairways", "QNB Qatar Airways cards", "Launched in February 2024 to earn Avios with Privilege Club: Visa Signature and Visa Infinite First Plus, with a Mastercard Platinum listed for the Essential segment ⚠ in 2025.", short="Qatar Airways (Visa)",
              s=["con", "first"], lc="borrow", ay="Feb 2024", o="P", at="Qatar Airways, Visa", neo=[1, "Visa; one Mastercard tier ⚠."],
              src=[["QNB: Qatar Airways card, Feb 2024", QRAIRWAYS], ["QNB: credit cards by segment", COBRAND]]),
            P("harrods", "QNB Harrods Visa", "Visa Platinum and Visa Infinite cards earning Harrods points, signed in London on 7 April 2025 and launched in Doha in May 2025, for Qatar only; Visa's Shashank Singh and QNB's Adel Al-Malki fronted it.", short="Harrods (Visa)",
              s=["first"], lc="borrow", st="new", ay="Apr 2025", o="P", at="Harrods, Visa", neo=[0, "Visa."],
              src=[["The Peninsula: QNB, Harrods and Visa, Apr 2025", HARRODS]]),
        ]},
        {"id": "2.3", "ic": "gem", "name": "Private cards", "blurb": "World Elite and an invite-only Visa.", "div": "qatar", "rev": "awm", "products": [
            P("worldelite", "QNB Private World Elite Mastercard", "An invitation-only metal-hybrid World Elite Exclusive card for QNB Private, launched in January 2021 with Louis Fourteen concierge, after an earlier diamond-embedded Private World Elite card ⚠ undated.", short="World Elite (Mastercard)",
              s=["first"], lc="borrow", ay="Jan 2021", o="P", at="Mastercard", neo=[2, "Mastercard World Elite."],
              src=[["Qatar Tribune: World Elite Exclusive, Jan 2021", WEE], ["Gulf Times: diamond card", DIAMOND]]),
            P("visainvite", "Invite-only Visa card", "An invitation-only Visa card for ultra-high-net-worth private-banking clients, cited in Visa's April 2024 award.",
              s=["first"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Gulf Times: Visa award, Apr 2024", VISAAWARD]]),
        ]},
        {"id": "2.4", "ic": "wallet-cards", "name": "Debit & Himyan", "blurb": "Mastercard debit, NAPS at home.", "div": "qatar", "rev": "retail", "products": [
            P("mcdebit", "QNB Mastercard debit cards", "QNB and Mastercard ran a spend campaign for QNB Mastercard Debit Card holders from 24 April to 24 June 2025 (20 travel vouchers of QR25,000). Whether all QNB debit is Mastercard is ⚠ not confirmed; local transactions route through NAPS.", short="Debit (Mastercard)",
              s=["con", "expat"], lc="everyday", o="P", at="Mastercard", neo=[1, "Mastercard abroad; NAPS at home ⚠."],
              mc="Mastercard's consumer foothold at QNB.",
              src=[["The Peninsula: QNB and Mastercard debit campaign, Apr 2025", MCDEBIT]]),
            P("himyan", "QNB Himyan debit & prepaid", "QCB's national card (announced November 2022, launched March 2023) on the NAPS switch, valid only in Qatar and in riyals; QNB prints it instantly with no fees, the prepaid card needs no account, and it can be added to Apple Pay.", short="Himyan (NAPS)",
              s=["con", "expat"], lc="everyday", ay="Mar 2023", o="P", at="Qatar Central Bank", neo=[0, "NAPS, Qatar's domestic switch."],
              mc="The domestic scheme Mastercard competes with for local debit spend.",
              src=[["QNB: Himyan debit card", HIMYANDEBIT], ["QNB: Himyan prepaid card", HIMYANPP], ["Gulf Times: QCB Himyan", HIMYANQCB]]),
        ]},
        {"id": "2.5", "ic": "briefcase-business", "name": "Commercial cards", "blurb": "Mastercard World, virtual cards.", "div": "qatar", "rev": "corp", "products": [
            P("corpcards", "QNB corporate & SME cards", "A long-term agreement with Mastercard (18 April 2023, Yousef Al-Neama and J.K. Khalil) for corporate and SME credit cards: QNB Mastercard World corporate cards with up to 55 days' credit, per-card limits, Corporate Liability Waiver and Mastercard Airport Pass lounges.", short="Corporate cards (Mastercard)",
              s=["corp", "sme"], lc="move", ay="Apr 2023", o="P", at="Mastercard", neo=[2, "Mastercard World."],
              mc="The deepest Mastercard relationship at QNB.",
              src=[["The Peninsula: commercial card deal, Apr 2023", MCCOMM], ["GCC Business News: commercial card deal", MCCOMM2], ["QNB: corporate credit cards", CORPCARD]]),
            P("virtualcards", "Virtual cards", "Single- and multi-use virtual cards issued online with custom spend controls tied to approval workflows.",
              s=["corp"], lc="move", o="P", at="Mastercard", neo=[2, "On the Mastercard corporate programme ⚠."], src=[["QNB: corporate credit cards", CORPCARD]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Acquiring", "blurb": "Every network; tap on phone.", "div": "qatar", "rev": "corp", "products": [
            P("acquiring", "Merchant acquiring", "POS terminals, cash-register and hotel-system integration and unattended kiosks accepting Visa, Mastercard, American Express, UnionPay and JCB, with dynamic currency conversion and FlexiPlan instalments.",
              s=["sme", "corp"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["QNB: integrated payments for hotels", HOTEL]]),
            P("mypos", "QNB myPOS", "Tap on phone for micro and small merchants, launched with Mastercard in March 2023: an Android app that takes contactless cards and wallets, with receipts by SMS, email or QR.", short="myPOS (with Mastercard)",
              s=["sme"], lc="move", ay="Mar 2023", o="P", at="Mastercard", neo=[1, "Launched with Mastercard; accepts all cards."],
              src=[["Mastercard: myPOS launch, Mar 2023", MCMYPOS], ["QNB: myPOS", MYPOS]]),
            P("gateway", "E-commerce gateway", "Hosted payment page with 3-D Secure, tokenisation, recurring payments, fraud screening and Apple Pay online acceptance.",
              s=["sme", "corp"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["QNB: e-commerce gateway", ECOM]]),
            P("simplify", "QNB Simplify", "A webstore and e-invoicing payment-link service for SMEs at qnb.simplify.com, which appears to run on Mastercard's Simplify Commerce ⚠ (inferred from the domain).",
              s=["sme"], lc="move", o="P", at="Mastercard ⚠", neo=[3, "Mastercard Simplify Commerce ⚠."], src=[["QNB: QNB Simplify", SIMPLIFY]]),
        ]},
        {"id": "2.7", "ic": "zap", "name": "Instant payments", "blurb": "Fawran: 3.6m accounts.", "div": "qatar", "rev": "retail", "products": [
            P("fawran", "Fawran", "Qatar Central Bank's instant payment service, live from March 2024: pay by mobile number or alias, 24/7, in QNB's app. Nationally it carried 3.19 million payments worth QR5.09 billion in December 2025, a quarter of all transactions, with 3.61 million registered accounts.", short="Fawran (QCB)",
              s=["con", "expat", "sme"], lc="move", ay="Mar 2024", o="P", at="Qatar Central Bank", neo=[0, "QCB's account-to-account rail."],
              mc="The fastest-growing rail in Qatar; card spend's main competitor.",
              src=[["Finance Middle East: Fawran, Feb 2024", FAWRANQCB], ["IBS Intelligence: QNB Fawran ⚠", FAWRANQNB], ["Gulf Times: QCB payments, Dec 2025", QCBDEC25]]),
            P("qmp", "QMP wallets", "Qatar Mobile Payments wallet-to-wallet transfers: 1.27 million wallets and 521,567 payments nationally in December 2025; QNB's role ⚠.",
              s=["con", "expat"], lc="move", o="P", at="Qatar Central Bank", neo=[0, ""], src=[["Gulf Times: QCB payments, Dec 2025", QCBDEC25]]),
        ]},
        {"id": "2.8", "ic": "arrow-left-right", "name": "Cross-border", "blurb": "Remittances; Sudan first.", "div": "branches", "rev": "intl", "products": [
            P("remit", "Direct transfers", "Direct transfer services to QNB Türkiye, India, Jordan and the Philippines for Qatar's expatriate workforce ⚠ (details not read).",
              s=["expat"], lc="move", neo=[None, "Network not public."],
              mc="A corridor book that Mastercard Move could serve.",
              src=[["QNB: international network", COBRAND]]),
            P("sudan", "Mastercard in Sudan", "QNB made the first international Mastercard transaction in Sudan in June 2020, on a virtual prepaid card, as the first bank there with a Mastercard issuing licence.",
              s=["intl"], lc="move", ay="Jun 2020", o="P", at="Mastercard", neo=[2, "Mastercard issuing licence."],
              src=[["Mastercard: first transaction in Sudan, Jun 2020", MCSUDAN]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every card and account: 3-D Secure and alerts, an open-banking API portal, Life Rewards points with airline, telecom and retail partners, and Mastercard Smart Data for corporate spend.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "3-D Secure, alerts.", "div": "qatar", "rev": "retail", "products": [
            P("security", "Card security", "3-D Secure online, an SMS alert on every transaction, chip and PIN and pre-authorisation fraud screening on the gateway; no Mastercard fraud product is named publicly ⚠.",
              s=["con", "sme"], lc="everyday", o="B", neo=[None, "Not disclosed."],
              mc="Fawran's growth makes real-time scam scoring a live need.",
              src=[["QNB: e-commerce gateway", ECOM], ["QNB: credit cards by segment", COBRAND]]),
        ]},
        {"id": "3.2", "ic": "code-xml", "name": "Open banking", "blurb": "API sandbox and portal.", "div": "qatar", "rev": "corp", "products": [
            P("openbanking", "Open-banking APIs", "An open-banking API sandbox and portal linked from qnb.com in 2025 ⚠ (scope not read).",
              s=["corp", "sme"], lc="open", o="B", neo=[0, ""], src=[["QNB: Himyan debit card page (site menu)", HIMYANDEBIT]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Loyalty", "blurb": "Life Rewards, Avios, lounges.", "div": "qatar", "rev": "retail", "products": [
            P("rewards", "QNB Life Rewards", "Points on every card, redeemable against bills and with partners, alongside Qatar Airways Avios, Ooredoo Nojoom and Harrods points, and QNB First lifestyle privileges.",
              s=["con", "first"], lc="grow", o="B", neo=[0, ""],
              mc="Card-linked offers could add merchant-funded value across partners.",
              src=[["QNB: credit cards by segment", COBRAND]]),
            P("airportpass", "Mastercard Airport Pass", "Lounge access at more than 1,000 airports through Mastercard's DragonPass app for QNB Mastercard World cardholders.",
              s=["corp", "first"], lc="beyond", o="P", at="Mastercard, DragonPass", neo=[3, "Mastercard's own programme."], src=[["QNB: corporate credit cards", CORPCARD]]),
        ]},
        {"id": "3.4", "ic": "database", "name": "Spend data", "blurb": "Mastercard Smart Data.", "div": "qatar", "rev": "corp", "products": [
            P("smartdata", "Smart Data reconciliation", "Mastercard Smart Data gives corporate clients online reporting and reconciliation of card spend, part of the 2023 commercial-card agreement.",
              s=["corp"], lc="move", ay="Apr 2023", o="P", at="Mastercard", neo=[3, "Mastercard Smart Data."],
              src=[["QNB: corporate credit cards", CORPCARD], ["The Peninsula: commercial card deal, Apr 2023", MCCOMM]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: retail banking for Qatar's citizens and expatriates, QNB First and Private, corporate and government banking with payroll, SME banking, and banks in Türkiye and Egypt.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Retail banking", "blurb": "Accounts, loans, cards.", "div": "qatar", "rev": "retail", "products": [
            P("retailbank", "Retail banking in Qatar", "Salary and current accounts, personal and car loans, deposits and cards for citizens and expatriates, segmented by salary into Essential, Select, First and First Plus.",
              s=["con", "expat"], lc="everyday", neo=[1, "Visa credit; Mastercard debit ⚠."], src=[["QNB: credit cards by segment", COBRAND]]),
        ]},
        {"id": "4.2", "ic": "coins", "name": "First, Private & wealth", "blurb": "QNB First and QNB Private.", "div": "qatar", "rev": "awm", "products": [
            P("first", "QNB First", "For clients earning at least QR35,000 a month or holding QR350,000; First Plus from QR100,000 a month or QR2 million, with Visa Infinite cards and lifestyle privileges.",
              s=["first"], lc="grow", neo=[0, "Visa Infinite."], src=[["QNB: credit cards by segment", COBRAND]]),
            P("wealth", "QNB Private & asset management", "Private banking, QNB Switzerland, funds, QNB Capital and QNB Financial Services brokerage.",
              s=["first"], lc="grow", neo=[1, "World Elite Mastercard for Private."], src=[["QNB: executive management", EXCO], ["Qatar Tribune: World Elite Exclusive, Jan 2021", WEE]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Corporate & government", "blurb": "Lending, trade, payroll.", "div": "qatar", "rev": "corp", "products": [
            P("cib", "Corporate & Institutional Banking", "Lending, project and structured finance, global transaction banking and the QNB Trade Portal for corporates, government and institutions.",
              s=["corp"], lc="borrow", neo=[1, "Mastercard corporate cards."], src=[["QNB: executive management", EXCO], ["QNB: corporate credit cards", CORPCARD]]),
            P("wps", "Wages Protection System", "Payroll through Qatar's Wages Protection System portal for employers paying a largely expatriate workforce ⚠ (details not read).",
              s=["corp", "expat"], lc="move", neo=[None, "Payroll cards not public."],
              mc="Payroll and prepaid for workers is open ground beyond Himyan.",
              src=[["QNB: international network (site menu)", COBRAND]]),
        ]},
        {"id": "4.4", "ic": "briefcase", "name": "SME banking", "blurb": "Accounts, cards, acceptance.", "div": "qatar", "rev": "corp", "products": [
            P("smebank", "SME banking", "SME accounts and packages, credit facilities, SME credit cards under the Mastercard deal, and merchant acceptance from myPOS to the gateway.",
              s=["sme"], lc="everyday", neo=[1, "Mastercard SME cards."], src=[["The Peninsula: commercial card deal, Apr 2023", MCCOMM], ["QNB: myPOS", MYPOS]]),
        ]},
        {"id": "4.5", "ic": "globe", "name": "Türkiye & Egypt", "blurb": "The two big subsidiaries.", "div": "turkiye", "rev": "intl", "products": [
            P("turkiye", "QNB Türkiye", "QNB Bank A.Ş., formerly Finansbank: 417 branches, 10,370 staff, TRY2.14 trillion of assets and TRY29.3 billion of Q2 2026 profit; card networks not confirmed ⚠.",
              s=["intl"], lc="everyday", o="A", ay="Jun 2016", neo=[None, "Networks not confirmed."], src=[["QNB Türkiye: about us", TRABOUT]]),
            P("enpara", "Enpara Bank", "Türkiye's branchless bank, separated from QNB Türkiye into its own licence on 28 August 2025.",
              s=["intl"], lc="everyday", st="new", ay="Aug 2025", o="B", div="enpara", neo=[None, "Networks not confirmed."], src=[["QNB Türkiye: about us", TRABOUT]]),
            P("egypt", "QNB Egypt", "Founded 1978; consolidated profit of EGP28.1 billion in the nine months to September 2026, up 26.3%; card networks not confirmed ⚠.",
              s=["intl"], lc="everyday", o="A", div="egypt", neo=[None, "Networks not confirmed."], src=[["Zawya: QNB Egypt 9M 2026, Oct 2026", EGYPT9M]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach QNB: QNB Mobile with Apple Pay and Google Pay, branches with instant card printing and cash-deposit ATMs, and corporate portals and partners.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Mobile & wallets", "blurb": "Apple Pay since 2021.", "div": "qatar", "rev": "retail", "products": [
            P("mobile", "QNB Mobile & internet banking", "The app for accounts, cards, Fawran and digital onboarding.",
              s=["con", "expat", "first"], lc="everyday", o="B", neo=[0, ""], src=[["QNB: Apple Pay", APPLEPAY]]),
            P("wallets", "Apple Pay, Google Pay & wearables", "Apple Pay from 2021 (the first bank in Qatar ⚠), Google Pay from August 2022, Garmin Pay and Fitbit Pay; credit, debit, prepaid and Himyan cards can be added.",
              s=["con", "expat"], lc="everyday", ay="2021", o="P", at="Apple, Google", neo=[1, "Tokens on Visa and Mastercard cards."],
              src=[["QNB: Apple Pay", APPLEPAY], ["Doha News: Apple Pay, 2021 ⚠", APPLEPAY21], ["QNB: Google Pay, Aug 2022", GPAY]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "4,800+ ATMs group-wide.", "div": "qatar", "rev": "retail", "products": [
            P("branches", "Branches & ATMs", "About 900 locations and more than 4,800 ATMs group-wide (2023); in Qatar, branches print cards on the spot and more than 300 ATMs take cash deposits.",
              s=["con", "expat"], lc="open", neo=[0, ""], src=[["GCC Business News: QNB footprint, Apr 2023", MCCOMM2], ["QNB: Himyan prepaid card", HIMYANPP]]),
        ]},
        {"id": "5.3", "ic": "monitor", "name": "Portals & partners", "blurb": "E-Business, airline, telecom.", "div": "qatar", "rev": "corp", "products": [
            P("portals", "Corporate portals", "E-Business internet banking, the QNB Trade Portal and the WPS portal for corporate and government clients.",
              s=["corp"], lc="move", o="B", neo=[0, ""], src=[["QNB: corporate credit cards (site menu)", CORPCARD]]),
            P("partners", "Brand partners", "Qatar Airways, Ooredoo and Harrods co-brands and QNB First merchant privileges.",
              s=["con", "first"], lc="beyond", o="P", at="Qatar Airways, Ooredoo, Harrods", neo=[0, "Mostly Visa co-brands."], src=[["QNB: credit cards by segment", COBRAND], ["The Peninsula: QNB, Harrods and Visa", HARRODS]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at QNB", "blurb": "Business cards; Visa for consumers.", "products": [
        P("mcatqnb", "Mastercard at QNB", "Mastercard carries QNB's corporate and SME cards under a 2023 long-term deal, with Smart Data and virtual cards, launched myPOS tap on phone with it, issues the Private World Elite cards and ran a debit campaign in 2025. Visa holds consumer credit and the Qatar Airways, Harrods and Ooredoo co-brands; NAPS carries Himyan.",
          s=["corp"], div="qnb", rev="corp", mc="The relationship this map is drawn for.",
          src=[["The Peninsula: commercial card deal, Apr 2023", MCCOMM], ["Gulf Times: Visa award, Apr 2024", VISAAWARD]]),
    ]},
    {"id": "pillar-market", "name": "Qatar payments", "blurb": "NAPS, Himyan, Fawran.", "products": [
        P("market", "The Qatari market", "Qatar's payment system handled 66.19 million transactions worth QR20.09 billion in December 2025: point of sale 49%, Fawran 25%, e-commerce 24% and QMP 2%. QCB runs NAPS, the Himyan national card, Fawran and QMP.",
          s=["con"], div="qnb", rev="retail", src=[["Gulf Times: QCB payments, Dec 2025", QCBDEC25], ["Gulf Times: QCB Himyan", HIMYANQCB]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
