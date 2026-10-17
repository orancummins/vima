"""MUFG's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the Q1 FY2026 highlights (3 August 2026), the FY2025
IR presentation (19 May 2026) and Investors Day 2026 (September 2026), with Mitsubishi UFJ NICOS, MUFG Bank and
ACOM product pages for card networks. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own
product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q1 = "https://www.mufg.jp/dam/ir/fs/2026/pdf/highlights2606_en.pdf"
CAP = "https://www.mufg.jp/dam/pressrelease/2026/pdf/news-20260814-001_en.pdf"
FY25 = "https://www.mufg.jp/dam/ir/presentation/2025/pdf/slides2603_en.pdf"
IDAY = "https://www.mufg.jp/dam/ir/presentation/2026/pdf/slides260901_en.pdf"
SPEECH = "https://www.mufg.jp/dam/ir/presentation/2026/pdf/speech260901_en.pdf"
ROE = "https://www.mufg.jp/dam/pressrelease/2026/pdf/news-20260515-003_en.pdf"
CEO = "https://www.mufg.jp/dam/pressrelease/2025/pdf/news-20251216-001_en.pdf"
BKBOARD = "https://www.mufg.jp/dam/pressrelease/2025/pdf/news-20251216-003_en.pdf"
EXECS = "https://www.mufg.jp/dam/pressrelease/2026/pdf/news-20260305-002_en.pdf"
RATINGS = "https://www.mufg.jp/english/ir/fixed_income/ratings/index.html"
MCAP = "https://finance.technews.tw/2026/07/13/mufg-becomes-japan-most-valuable-company/"
EMUTBANK = "https://www.mufg.jp/dam/pressrelease/2026/pdf/news-20260924-001_en.pdf"
EMUT = "https://www.mufg.jp/dam/pressrelease/2025/pdf/news-20250527-001_ja.pdf"
JCB = "https://www.mufg.jp/dam/pressrelease/2026/pdf/news-20260706-002_en.pdf"
SHRIRAM = "https://www.mufg.jp/dam/pressrelease/2026/pdf/news-20260408-001_en.pdf"
DANAMON = "https://www.mufg.jp/dam/pressrelease/2026/pdf/news-20261007-001_en.pdf"
SFIN = "https://www.mufg.jp/dam/pressrelease/2026/pdf/news-20261016-001_en.pdf"
JGB = "https://www.mufg.jp/dam/pressrelease/2026/pdf/news-20260813-002_en.pdf"
ST = "https://www.mufg.jp/dam/pressrelease/2025/pdf/news-20251009-001_en.pdf"
WNAVI = "https://www.mufg.jp/dam/pressrelease/2025/pdf/news-20250121-001_en.pdf"
JACCS = "https://www.bk.mufg.jp/news/news2025/pdf/news0314.pdf"
EUBANK = "https://www.mufg.jp/dam/pressrelease/2026/pdf/news-20260108-001_en.pdf"
UNIONSALE = "https://www.businesswire.com/news/home/20221019005507/en/MUFG-Bank-Ltd.-UK-Regulatory-Announcement-MUFG-Announces-December-1-Closing-Date-of-the-Sale-of-MUFG-Union-Bank-to-U.S.-Bancorp"
MUCARD = "https://www.cr.mufg.jp/apply/card/mucard/index.html"
GOLD = "https://www.cr.mufg.jp/apply/card/mucard_goldprestige/index.html"
TOUCH = "https://www.cr.mufg.jp/apply/card/touch_payment/index.html"
BIZCARD = "https://www.cr.mufg.jp/business/card/index.html"
JIGYO = "https://www.cr.mufg.jp/corporate/company/jigyo/index.html"
NICOSCO = "https://www.cr.mufg.jp/corporate/company/overview/index.html"
NICOSMSG = "https://www.cr.mufg.jp/corporate/company/greet/index.html"
NICOSFY = "https://www.cr.mufg.jp/corporate/company/financial_affairs/notification/pdf/202603.pdf"
GPW = "https://www.cr.mufg.jp/mufgcard/gpwallet/faq/index.html"
SYSMERGE = "https://www.watch.impress.co.jp/docs/news/2052847.html"
DEBIT = "https://www.bk.mufg.jp/tsukau/debit/index.html"
VDEBIT = "https://www.bk.mufg.jp/tsukau/debit/visa/index.html"
JDEBIT = "https://www.bk.mufg.jp/tsukau/debit/jcb/index.html"
ACMC = "https://www.acom.co.jp/lineup/credit/"
ACOMDB = "https://pdf.irpocket.com/C8572/xoA3/tx0r/qGU6/CeFh.pdf"
COTRA = "https://www.cotra.ne.jp/company/"
METI = "https://www.watch.impress.co.jp/docs/news/2099068.html"
FRAUD = "https://paymentnavi.com/?p=173293"
JFTC = "https://www.jftc.go.jp/houdou/pressrelease/2025/jul/250722_daisan.html"
PAYPAY = "https://about.paypay.ne.jp/en/pr/20260810/01/"
JCBWIKI = "https://ja.wikipedia.org/wiki/ジェーシービー"
UNIONMC = "https://www.businesstravelnews.com/Expense-Management/MUFG-Union-Bank-wholly-owned-by-the-Bank-of-Tokyo-Mitsubishi-UFJ-has-launched-a-commercial-card-program-with-MasterCard-"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · group · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Japan's largest bank group and, since July 2026, its most valuable company, record profits as rates rise, a new chief executive, the Morgan Stanley alliance, AI with OpenAI and Google, and a plan raised to 12% ROE.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "¥809bn in one quarter.", "div": "mufg", "rev": "global", "products": [
            P("balance", "Balance sheet & earnings", "Net profit of ¥2.43 trillion in the year to March 2026 (ROE 11.3%) and a record ¥809.4 billion in April–June 2026, 30% of the ¥2.7 trillion target; total assets ¥433.9 trillion, loans ¥135.7 trillion and deposits ¥236.9 trillion; CET1 12.95%; market value about ¥41.9 trillion (13 July 2026); rated A1 by Moody's.",
              s=["con", "corp"], neo=[0, ""], src=[["Q1 FY2026 highlights", Q1], ["FY2025 IR presentation", FY25], ["Basel III ratios, Aug 2026", CAP], ["TechNews: most valuable company, Jul 2026", MCAP], ["MUFG: credit ratings", RATINGS]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Hanzawa takes over.", "div": "mufg", "rev": "global", "products": [
            P("leadership", "Board & executives", "Junichi Hanzawa became President & Group CEO on 1 April 2026, with Hironori Kamezawa as Chairman; Masakazu Osawa runs MUFG Bank. Business groups: Tadashi Yamamoto (Retail & Digital), Takuya Tanaka (Commercial Banking & Wealth), Hideaki Takase (Japanese CIB) and Komoriya (Global Commercial Banking ⚠ first name not given).",
              s=["corp"], st="new", neo=[0, ""], src=[["MUFG: CEO change, Dec 2025", CEO], ["MUFG Bank: board change, Dec 2025", BKBOARD], ["MUFG: board and executives, Mar 2026", EXECS], ["Investors Day 2026 speech", SPEECH]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & group", "blurb": "Formed 2005; JCB's founders.", "div": "mufg", "rev": "global", "products": [
            P("heritage", "Heritage", "Formed in 2005 from Mitsubishi Tokyo Financial Group and UFJ Holdings, with more than 360 years of history; about 2,300 locations in 50+ countries and about 160,000 staff. Two predecessors, Sanwa Bank and Nippon Shinpan, founded JCB in 1961, and MUFG Bank is still a major JCB shareholder ⚠.",
              s=["con"], o="I", neo=[0, ""], mc="JCB is family: the domestic scheme was born inside today's MUFG.",
              src=[["MUFG Emut Bank release (boilerplate), Sep 2026", EMUTBANK], ["Japanese Wikipedia: JCB", JCBWIKI]]),
            P("morganstanley", "Morgan Stanley alliance", "MUFG's equity stake in Morgan Stanley contributed ¥222.2 billion of the April–June 2026 net income; the two run joint securities firms in Japan and a private-credit business set up in 2025.",
              s=["corp"], o="P", at="Morgan Stanley", neo=[0, ""], src=[["Q1 FY2026 highlights", Q1], ["Investors Day 2026", IDAY]]),
        ]},
        {"id": "1.4", "ic": "brain", "name": "Technology & AI", "blurb": "OpenAI, Google, Sakana.", "div": "mufg", "rev": "rd", "products": [
            P("tech", "AI & cloud", "AI with OpenAI (Moneytree data inside ChatGPT apps), a retail alliance with Google from May 2026 (AI agents, data-driven marketing), Sakana AI for credit work, AI agents for relationship managers, and the digital bank built on Google Cloud.",
              s=["con", "corp"], st="new", o="P", at="OpenAI, Google, Sakana AI", neo=[0, ""],
              mc="Agent-led retail journeys with no payment network named yet.",
              src=[["FY2025 IR presentation", FY25], ["Investors Day 2026 speech", SPEECH], ["MUFG: retail strategy, May 2025 (JA)", EMUT]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "ROE target 12%.", "div": "mufg", "rev": "global", "products": [
            P("strategy", "Medium-term plan FY2024–26", "The final year of the plan: the FY2026 ROE target was raised to about 12% from 9% in May 2026, with a net profit target of ¥2.7 trillion; Asia is the 'second home market' with $20 billion invested since 2013.",
              s=["corp"], neo=[0, ""], src=[["MUFG: ROE target revised, May 2026", ROE], ["Investors Day 2026", IDAY]]),
            P("deals", "Deals 2022–26", "MUFG Union Bank sold to U.S. Bancorp (December 2022); WealthNavi (January 2025); Jaccs stake raised to 40% of votes (March 2025); Moneytree (2025); 20% of Shriram Finance for about ¥682 billion (April 2026); an EU universal bank (2026).",
              s=["corp"], o="A", neo=[0, ""], src=[["WealthNavi tender result, Jan 2025", WNAVI], ["MUFG Bank and Jaccs, Mar 2025 (JA)", JACCS], ["Shriram Finance completed, Apr 2026", SHRIRAM], ["MUFG Union Bank sale, Oct 2022", UNIONSALE], ["EU universal bank, Jan 2026", EUBANK]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Mitsubishi UFJ Card on four networks, co-brands and card processing, Visa and JCB debit and a Visa prepaid wallet, ACOM's AC Mastercard, NICOS acquiring, bank transfers through Zengin and Cotra, and stablecoin and token pilots.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Credit cards", "blurb": "Four networks, one card.", "div": "nicos", "rev": "rd", "products": [
            P("mucard", "Mitsubishi UFJ Card", "NICOS's flagship card, issued on Mastercard, Visa, JCB or American Express at the customer's choice, with up to 20% points at selected stores under Emut and card-funded investing with eSmart Securities; card issuance up 1.8 times in FY2025. Card settlement earned ¥63.4 billion in April–June 2026.", short="Mitsubishi UFJ Card (4 networks)",
              s=["con"], lc="everyday", st="active", o="B", neo=[1, "Mastercard is one of four network choices; no split published."],
              mc="The group's main credit card leaves the network to the customer.",
              src=[["NICOS: Mitsubishi UFJ Card", MUCARD], ["Q1 FY2026 highlights", Q1], ["FY2025 IR presentation", FY25]]),
            P("gold", "Mitsubishi UFJ Card Gold Prestige", "The gold tier, on Mastercard, Visa, JCB or American Express, with up to 2.0% points on card-funded investing (from June 2026).",
              s=["con", "aff"], lc="everyday", o="B", neo=[1, "One of four networks."], src=[["NICOS: Gold Prestige", GOLD]]),
            P("platinum", "Mitsubishi UFJ Card Platinum American Express", "The top consumer card, issued only on American Express under licence.",
              s=["aff"], lc="everyday", o="P", at="American Express", neo=[0, "American Express."], src=[["NICOS: Mitsubishi UFJ Card", MUCARD]]),
            P("dcnicos", "DC Card & NICOS Card", "Legacy brands: the DC Card system was merged into the MUFG Card system on 9 December 2025, and NICOS Card is being folded in; integration costs of ¥31.1 billion left NICOS with an ordinary loss of ¥23.0 billion in the year to March 2026.",
              s=["con"], lc="everyday", st="flux", o="I", neo=[1, "Mixed networks ⚠."], src=[["Impress Watch: card systems merged, Oct 2025", SYSMERGE], ["NICOS: president's message, Jun 2026", NICOSMSG], ["NICOS: FY2025 accounts (JA)", NICOSFY]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Co-brands & processing", "blurb": "JAL Mastercard, au PAY.", "div": "nicos", "rev": "rd", "products": [
            P("cobrand", "Co-brand cards", "Partner cards such as JAL Mastercard CLUB-A Gold, the Mitsubishi Estate Group Card and JA Card.",
              s=["con"], lc="everyday", o="P", at="JAL, Mitsubishi Estate, JA", neo=[1, "JAL CLUB-A on Mastercard; others mixed."], src=[["NICOS: business lines", JIGYO]]),
            P("processing", "Issuing & franchise processing", "Runs issuing for au PAY Card and Lawson Ponta Plus, debit-card issuing for other banks, and a franchise with 15 regional banks and 40 affiliated card companies.",
              s=["sme"], lc="move", o="B", neo=[None, "Networks of the cards processed not stated."],
              mc="A processor for other issuers: a route to regional banks' card books.",
              src=[["NICOS: business lines", JIGYO]]),
        ]},
        {"id": "2.3", "ic": "wallet", "name": "Debit & prepaid", "blurb": "Visa and JCB only.", "div": "bank", "rev": "rd", "products": [
            P("debit", "Mitsubishi UFJ-Visa Debit & Mitsubishi UFJ-JCB Debit", "MUFG Bank's debit cards, free of annual fees, on Visa or JCB with touch payment; there is no Mastercard debit.", short="Debit (Visa, JCB)",
              s=["con"], lc="everyday", o="P", at="Visa, JCB", neo=[0, "Visa and JCB."],
              mc="Debit for 34 million bank customers runs on Visa and JCB.",
              src=[["MUFG Bank: debit", DEBIT], ["MUFG Bank: Visa Debit", VDEBIT], ["MUFG Bank: JCB Debit", JDEBIT]]),
            P("gpwallet", "Global Point Wallet", "A NICOS prepaid app that turns Global Points into a Visa virtual prepaid card for Apple Pay, Google Pay, QUICPay+ and online shopping.",
              s=["con"], lc="everyday", st="new", o="B", at="Visa", neo=[0, "Visa."], src=[["NICOS: Global Point Wallet FAQ", GPW]]),
        ]},
        {"id": "2.4", "ic": "hand-coins", "name": "Consumer-finance cards", "blurb": "AC Mastercard, 1m holders.", "div": "acom", "rev": "rd", "products": [
            P("acmc", "ACOM AC Mastercard", "ACOM's credit card, issued only on Mastercard, with instant issue at machines and a virtual card in the app: about 1.05 million cardholders and ¥158.4 billion of card receivables at June 2026.", short="AC Mastercard",
              s=["cf"], lc="borrow", o="B", at="Mastercard", neo=[2, "Mastercard only."],
              mc="The one MUFG card book that rides wholly on Mastercard.",
              src=[["ACOM: AC Mastercard", ACMC], ["ACOM: Q1 FY2026 data book", ACOMDB]]),
            P("jaccs", "Jaccs", "A shopping-credit and card company; MUFG Bank raised its stake to 37.7% (group voting 40%) in March 2025.",
              s=["cf"], lc="borrow", o="A", neo=[None, "Network mix not researched."], src=[["MUFG Bank and Jaccs, Mar 2025 (JA)", JACCS]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acceptance", "blurb": "NICOS and Airペイ.", "div": "nicos", "rev": "rd", "products": [
            P("acquiring", "Merchant acquiring", "NICOS signs merchants for card, e-money and foreign-currency payments, and runs acquiring for Recruit's Airペイ (AirPAY).",
              s=["sme"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["NICOS: business lines", JIGYO]]),
            P("contactless", "Contactless & wallets", "Mitsubishi UFJ Card supports Visa touch, Mastercard contactless and JCB touch; in-store Apple Pay runs through QUICPay ⚠, the domestic contactless scheme JCB operates.",
              s=["con"], lc="everyday", o="P", at="Visa, Mastercard, JCB", neo=[1, "Mastercard contactless is one of three; Apple Pay via QUICPay ⚠."],
              src=[["NICOS: touch payment", TOUCH], ["NICOS: Mitsubishi UFJ Card", MUCARD]]),
        ]},
        {"id": "2.6", "ic": "send", "name": "Transfers", "blurb": "Zengin and Cotra.", "div": "bank", "rev": "rd", "products": [
            P("transfers", "Bank transfers & Cotra", "Domestic transfers through the Zengin system, and Cotra, owned by MUFG Bank, Mizuho, SMBC and Resona, for low-cost small transfers and QR tax payments.",
              s=["con", "sme"], lc="move", o="P", at="Cotra", neo=[0, "Bank rails."], src=[["Cotra: company", COTRA]]),
        ]},
        {"id": "2.7", "ic": "coins", "name": "Digital money", "blurb": "Stablecoins, tokens.", "div": "trust", "rev": "global", "products": [
            P("stablecoin", "Stablecoins & tokenised deposits", "Joint stablecoin issuance and cross-border pilots by Japan's three megabanks with Mitsubishi Corporation and Mitsubishi UFJ Trust (adopted by the FSA's PoC hub, 7 November 2025), Project Agorá and a G-SIB digital-money consortium.",
              s=["corp"], lc="move", st="new", o="P", neo=[0, ""],
              mc="Megabank stablecoins could settle card-like flows off the networks.",
              src=[["FY2025 IR presentation", FY25]]),
            P("tokens", "Security tokens & on-chain repo", "Progmat security tokens, a digital subordinated bond (October 2025) and an on-chain JGB repo proof of concept (August 2026).",
              s=["corp"], lc="grow", st="new", o="B", neo=[0, ""], src=[["Security-token bond, Oct 2025", ST], ["On-chain JGB repo PoC, Aug 2026", JGB]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account and card: fraud screening against ¥51 billion of card fraud in Japan, AI advice with WealthNavi, OpenAI and Google, Moneytree's data links, and group points with a new premium club.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "AI plus people.", "div": "nicos", "rev": "rd", "products": [
            P("fraud", "Card fraud prevention", "NICOS combines AI and human review and says its fraud losses fell for three years to FY2025, against Japan-wide card fraud of ¥51.05 billion in 2025; EMV 3-D Secure has been mandatory for online merchants since March 2025.",
              s=["con"], lc="everyday", o="B", neo=[0, "NICOS's own ⚠."],
              mc="Tokens and network fraud scores are an open field.",
              src=[["NICOS: president's message, Jun 2026", NICOSMSG], ["Payment Navi: card fraud 2025", FRAUD]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI for customers", "blurb": "MAP AI and agents.", "div": "emut", "rev": "rd", "products": [
            P("mapai", "MAP AI advice", "The Money Advisory Platform built with WealthNavi, using data on about 60 million group customers, at the heart of the digital bank and the merged online broker.",
              s=["con", "aff"], lc="grow", st="new", o="B", neo=[0, ""], src=[["Investors Day 2026 speech", SPEECH], ["MUFG: retail strategy, May 2025 (JA)", EMUT]]),
            P("aiagents", "AI agents with OpenAI & Google", "GPT models inside MUFG services, Moneytree inside ChatGPT apps, and AI agents for customers under the May 2026 Google alliance.",
              s=["con"], lc="everyday", st="new", o="P", at="OpenAI, Google", neo=[0, ""],
              mc="Agents that will need a way to pay: Agent Pay is untested here.",
              src=[["FY2025 IR presentation", FY25]]),
        ]},
        {"id": "3.3", "ic": "plug", "name": "Open data", "blurb": "Moneytree LINK.", "div": "bank", "rev": "rd", "products": [
            P("moneytree", "Moneytree", "A financial-data platform connected to more than 2,500 institutions, with its Moneytree LINK API used by about 120 companies; MUFG agreed to buy it in May 2025 for the digital bank and SME credit models.",
              s=["con", "sme"], lc="open", st="new", o="A", neo=[0, ""], src=[["MUFG: retail strategy, May 2025 (JA)", EMUT]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Points & premium", "blurb": "Up to 20% back.", "div": "emut", "rev": "rd", "products": [
            P("points", "Global Points & Emut points", "Global Points on NICOS cards, with up to 20% back at selected stores (card points worth ¥5 each), and a common group ID, points and loyalty programme to come under Emut.",
              s=["con"], lc="everyday", st="new", o="B", neo=[0, "Group points on every network."],
              mc="Merchant offers could feed the 20% programme.",
              src=[["NICOS: Mitsubishi UFJ Card", MUCARD], ["Investors Day 2026 speech", SPEECH]]),
            P("excellent", "Emut Excellent Club", "A club for wealthy clients with what MUFG calls Japan's first platinum card linked to assets under management, and joint advice across bank, trust bank and securities.",
              s=["aff"], lc="grow", st="new", o="B", neo=[None, "Network of the new card not stated."],
              mc="A premium card yet to pick its network.",
              src=[["Investors Day 2026 speech", SPEECH]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: retail accounts and home loans for 34 million bank customers, consumer finance through ACOM, wealth and investing, corporate and global banking, and partner banks and digital lenders across Asia.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Retail banking", "blurb": "34 million customers.", "div": "bank", "rev": "rd", "products": [
            P("accounts", "Accounts & deposits", "About 34 million MUFG Bank retail customers, with more than 1 million new accounts in FY2025, the first rise in eight years; ¥94.8 trillion of individual deposits.",
              s=["con"], lc="everyday", neo=[0, "Visa and JCB debit."], src=[["Investors Day 2026 speech", SPEECH], ["Q1 FY2026 highlights", Q1]]),
            P("mortgages", "Home loans", "Housing loans of ¥14.4 trillion at June 2026.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Q1 FY2026 highlights", Q1]]),
        ]},
        {"id": "4.2", "ic": "hand-coins", "name": "Consumer finance", "blurb": "ACOM and card loans.", "div": "acom", "rev": "rd", "products": [
            P("consumerfin", "ACOM & card loans", "ACOM's loans, guarantees and AC Mastercard, and card loans across the group: consumer finance earned ¥83.1 billion in April–June 2026.",
              s=["cf"], lc="borrow", o="I", neo=[1, "The AC Mastercard is the card."], src=[["Q1 FY2026 highlights", Q1], ["ACOM: Q1 FY2026 data book", ACOMDB]]),
        ]},
        {"id": "4.3", "ic": "trending-up", "name": "Wealth & investing", "blurb": "Largest AuM of any bank.", "div": "trust", "rev": "cwm", "products": [
            P("wealth", "Wealth & online investing", "The largest assets under management of any Japanese bank; Mitsubishi UFJ eSmart Securities and WealthNavi (¥2.1 trillion) to merge in FY2027; card-funded investment plans on Mitsubishi UFJ Card.",
              s=["aff", "con"], lc="grow", st="flux", neo=[1, "Funded by multi-network cards."], src=[["Investors Day 2026 speech", SPEECH], ["NICOS: Mitsubishi UFJ Card", MUCARD]]),
            P("inheritance", "Emut Sozoku", "A digital inheritance platform from the second half of FY2026, with Mitsubishi UFJ Trust's expertise.",
              s=["aff"], lc="grow", st="new", neo=[0, ""], src=[["Investors Day 2026 speech", SPEECH]]),
        ]},
        {"id": "4.4", "ic": "building-2", "name": "Corporate & global banking", "blurb": "Corporate cards to come.", "div": "bank", "rev": "jcib", "products": [
            P("jcib", "Japanese Corporate & Investment Banking", "Japan's top main bank for corporates; JCIB earned ¥139.4 billion in April–June 2026 and targets an ROE of 14.5%.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Q1 FY2026 highlights", Q1], ["Investors Day 2026 speech", SPEECH]]),
            P("globalpay", "Global payments business", "JCIB plans to grow a global payments business through active investment in the next plan.",
              s=["corp"], lc="move", st="new", neo=[None, "Nothing announced."],
              mc="A stated plan to invest in corporate payments.",
              src=[["Investors Day 2026 speech", SPEECH]]),
            P("corpcard", "Business & corporate cards", "NICOS business cards on Visa and Mastercard, with corporate cashless products to be launched 'in earnest' (June 2026). In the US, MUFG Union Bank once ran a Mastercard commercial-card programme ⚠ date.",
              s=["sme", "corp"], lc="move", st="new", o="B", neo=[1, "Visa and Mastercard."],
              mc="Japan's corporate card push is starting, with Mastercard on the card.",
              src=[["NICOS: business cards", BIZCARD], ["NICOS: president's message, Jun 2026", NICOSMSG], ["Business Travel News: Union Bank commercial card", UNIONMC]]),
            P("gcib", "Global CIB & markets", "Project finance, Americas fee income and the Morgan Stanley alliance; an EU universal bank in Amsterdam.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["FY2025 IR presentation", FY25], ["EU universal bank, Jan 2026", EUBANK]]),
        ]},
        {"id": "4.5", "ic": "earth", "name": "Asia", "blurb": "Partner banks and wallets.", "div": "asia", "rev": "gcb", "products": [
            P("krungsri", "Krungsri", "Thailand's largest card issuer, about 76.9% owned; net income ¥35.6 billion in April–June 2026; took full ownership of SFinance in Vietnam in October 2026.",
              s=["asia"], lc="everyday", o="A", neo=[None, "Covered on the Krungsri page."], src=[["Krungsri and SFinance, Oct 2026", SFIN], ["Q1 FY2026 highlights", Q1]]),
            P("danamon", "Danamon & Adira", "About 92.5% owned; absorbing MUFG's Jakarta branch as Bank MUFG Danamon (name announced 7 October 2026).",
              s=["asia"], lc="everyday", st="flux", o="A", neo=[None, "Card networks not verified."], src=[["Bank MUFG Danamon, Oct 2026", DANAMON]]),
            P("partners", "VietinBank & Security Bank", "20% stakes in Vietnam's VietinBank and the Philippines' Security Bank.",
              s=["asia"], lc="everyday", o="A", neo=[None, "Card networks not verified."], src=[["Investors Day 2026", IDAY]]),
            P("digitalasia", "Digital finance investees", "Six investments of about $1.8 billion since 2022: Home Credit point-of-sale lending, Akulaku, DMI Finance, Thailand's largest e-wallet and Mynt, the Philippines' largest e-wallet (GCash).",
              s=["asia"], lc="move", o="A", neo=[None, "Nothing public."],
              mc="Wallets with tens of millions of users across ASEAN.",
              src=[["Investors Day 2026", IDAY]]),
            P("shriram", "Shriram Finance", "20% of one of India's largest non-bank lenders, completed 8 April 2026 for INR 396 billion.",
              s=["asia"], lc="borrow", st="new", o="A", neo=[0, ""], src=[["Shriram Finance completed, Apr 2026", SHRIRAM]]),
            P("jcbasean", "MUFG Bank × JCB in ASEAN", "A strategic alliance signed 6 July 2026: premium cards with partner banks, starting with JCB's highest-tier card outside Japan in Indonesia in FY2026, and JCB payments for MUFG's digital investees.",
              s=["asia", "aff"], lc="everyday", st="new", o="P", at="JCB", neo=[0, "JCB."],
              mc="The group's only new scheme alliance, and it is with JCB.",
              src=[["MUFG Bank and JCB, Jul 2026", JCB]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: the MUFG Bank and card apps, Emut and the digital bank opening early in 2027, and branches, advisers and partner companies.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Apps", "blurb": "Bank and card apps.", "div": "bank", "rev": "rd", "products": [
            P("bankapp", "MUFG Bank app", "Rebuilt in 2025 as an all-in-one asset hub showing the group's services in one place.",
              s=["con"], lc="everyday", st="new", neo=[0, ""], src=[["MUFG: retail strategy, May 2025 (JA)", EMUT]]),
            P("cardapps", "MDC app & NICOS card app", "Two NICOS apps for statements, points and card controls, one per card brand family.",
              s=["con", "cf"], lc="everyday", neo=[0, ""], src=[["NICOS: business lines", JIGYO]]),
        ]},
        {"id": "5.2", "ic": "rocket", "name": "Emut & Emut Bank", "blurb": "Digital bank in 2027.", "div": "emut", "rev": "rd", "products": [
            P("emut", "Emut", "The group retail brand launched in June 2025, tying bank, card, securities and trust services together with points and a common ID.",
              s=["con"], lc="open", st="new", o="B", neo=[1, "Bundles the multi-network Mitsubishi UFJ Card."], src=[["MUFG: retail strategy, May 2025 (JA)", EMUT], ["Investors Day 2026 speech", SPEECH]]),
            P("emutbank", "MUFG Emut Bank", "Licensed on 24 September 2026 with ¥47.45 billion of capital and CEO Kunihiro Yamashita; services start between January and March 2027, on Google Cloud with MAP AI.",
              s=["con"], lc="open", st="new", o="B", neo=[None, "Debit network not announced."],
              mc="A new bank that has not yet named a card network.",
              src=[["MUFG Emut Bank licensed, Sep 2026", EMUTBANK]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & partners", "blurb": "Advisers and alliances.", "div": "mufg", "rev": "cwm", "products": [
            P("branches", "Branches & advisers", "Bank branches, consolidated under the previous plan, with remote advice across bank, trust bank and securities for wealthy clients.",
              s=["aff", "sme"], lc="grow", neo=[0, ""], src=[["Investors Day 2026 speech", SPEECH]]),
            P("partnerco", "Regional banks & partner companies", "NICOS's franchise of regional banks and affiliated card companies, and Emut's tie-ups in shopping, healthcare and social media.",
              s=["con", "sme"], lc="open", o="P", neo=[None, "Mixed."], src=[["NICOS: business lines", JIGYO], ["Investors Day 2026", IDAY]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at MUFG", "blurb": "One of four, and AC Mastercard.", "products": [
        P("mcatmufg", "Mastercard at MUFG", "Mastercard is one of four network choices on NICOS's Mitsubishi UFJ Card range, the only network on ACOM's AC Mastercard (about 1.05 million holders) and JAL's CLUB-A card, and one of two on business cards. MUFG Bank's debit is Visa and JCB, the prepaid wallet is Visa, and the group's only scheme alliance of 2026 is with JCB in ASEAN. No MUFG–Mastercard agreement has been published.",
          s=["con"], div="mufg", rev="rd", mc="The relationship this map is drawn for.",
          src=[["NICOS: Mitsubishi UFJ Card", MUCARD], ["ACOM: AC Mastercard", ACMC], ["MUFG Bank and JCB, Jul 2026", JCB]]),
    ]},
    {"id": "pillar-market", "name": "Japan's cashless push", "blurb": "58% cashless, credit 83%.", "products": [
        P("market", "The Japanese market", "Cashless payments reached 58.0% of spending in 2025 (¥162.7 trillion), 82.7% of it on credit cards and 10.2% on code payments, against a 65% target for 2030; PayPay has 75 million users; JCB is Japan's own international brand; the JFTC accepted a Visa commitment plan on interchange in July 2025; card fraud was ¥51 billion.",
          s=["con"], div="mufg", rev="rd",
          src=[["Impress Watch: METI cashless ratio, Apr 2026", METI], ["PayPay: 75 million users, Aug 2026", PAYPAY], ["JFTC: Visa commitment plan, Jul 2025", JFTC], ["Payment Navi: card fraud 2025", FRAUD]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
