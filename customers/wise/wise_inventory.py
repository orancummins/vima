"""Wise's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Wise Group plc reports in US dollars under US GAAP from FY26 (year to 31 March 2026): figures are its FY26 results
and Form 20-F (25 June 2026), its Q1 FY27 trading update (17 July 2026) and its own pages. ``neo`` is the Mastercard
lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

FY26 = "https://www.investegate.co.uk/announcement/rns/wise-class-a--wise/wise-fy26-results/9637901"
F20 = "https://www.sec.gov/Archives/edgar/data/2099039/000119312526282911/d17323d20f.htm"
Q1 = "https://fxnewsgroup.com/forex-news/payments/wise-group-registers-26-y-y-growth-in-cross-border-volume-in-q1-fy27/"
FXCQ1 = "https://www.fxcintel.com/research/analysis/wise-q1-2027-earnings"
PLAT = "https://wise.com/platform/"
NEWS = "https://newsroom.wise.com/en-NAM/"
MC2020 = "https://newsroom.mastercard.com/news/press/2020/august/transferwise-and-mastercard-expand-their-global-partnership/"
VISA2021 = "https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.17606.html"
VISADIRECT = "https://www.finextra.com/pressarticle/80900/visa-partners-transferwise-on-cross-border-payments"
UKCARD = "https://wise.com/gb/card/"
USCARD = "https://wise.com/us/card"
USBLOG = "https://wise.com/us/blog/transferwise-debit-mastercard-launch-us"
HELP = "https://wise.com/help/articles/2935771/where-will-my-wise-card-work"
FR = "https://www.comparateurbanque.com/transferwise/nouvelle-carte-visa/"
FIFA = "https://wise.com/gb/blog/how-to-order-wise-visa-fifa-world-cup-2026-card"
BIZCARD = "https://wise.com/gb/business/card"
AUCARD = "https://wise.com/au/card-supplement-agreement"
SGCARD = "https://wise.com/sg/card-supplement-agreement"
OCC = "https://investegate.co.uk/announcement/rns/wise-class-a--wise/wise-us-national-trust-bank-charter-application/9685426"
NASDAQ = "https://fstech.co.uk/fst/Wise_debuts_on_Nasdaq_completing_primary_listing_move_to_US.php"
VOTE = "https://www.uktech.news/fintech/wise-votes-in-favour-of-us-listing-despite-share-class-controversy-20250729"
SWIFT = "https://www.fxcintel.com/research/analysis/swift-partnership-wise-visa"
THAI = "https://newsroom.wise.com/en-CAS/271897-wise-launches-multi-currency-account-and-card-for-thai-locals-expats-and-digital-nomads/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "scale · licences · control", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $2.5 billion of net revenue and 18.9 million active customers in FY26, more than 80 licences, a Nasdaq primary listing since May 2026 under founder control, one in-house stack, and $41 billion of customer money.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & profit", "blurb": "$2.5bn revenue, 26% margin.", "div": "grp", "rev": "grp", "products": [
            P("scale", "FY26 results", "Year to 31 March 2026, first in US GAAP and dollars: net revenue $2,502.8 million (+19%), income before tax $660.4 million (26% margin), 18.9 million active customers (+21%), cross-border volume $243.5 billion (+31%) and card spend $43.6 billion (+37%).",
              s=["pers", "biz"], neo=[0, ""], src=[["Wise: FY26 results, Jun 2026", FY26]]),
            P("q1fy27", "Q1 FY27", "Quarter to 30 June 2026: 11.9 million active customers (+21%), $69.3 billion cross-border volume (+26%), net revenue $714.0 million (+25%), customer holdings $41.2 billion; FY27 guidance of net revenue growth around the middle of 15–20% and a margin near the top of 20–25%.", short="Q1 FY27",
              s=["pers", "biz"], st="new", neo=[0, ""], src=[["Wise Q1 FY27, Jul 2026 (FX News Group)", Q1], ["FXC Intelligence: Wise Q1 FY27", FXCQ1]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Licences & charter", "blurb": "80+ licences, no US bank.", "div": "grp", "rev": "grp", "products": [
            P("licences", "Licence stack", "More than 80 licences: FCA e-money (Wise Payments Ltd), National Bank of Belgium payment institution (Wise Europe SA), money transmitter licences in 48 US states and four territories, MAS major payment institution, an Australian AFSL; new approvals in South Africa, the UAE and Thailand in FY26.",
              s=["pers", "biz", "bank"], neo=[0, ""], src=[["Wise: Form 20-F, Jun 2026", F20], ["Wise: FY26 results, Jun 2026", FY26], ["Wise: Australian card terms", AUCARD], ["Wise: Singapore card terms", SGCARD]]),
            P("charter", "US trust bank charter", "Applied to the OCC for Wise National Trust (16 June 2025); denied in July 2026, citing anti-money-laundering weaknesses and a July 2025 multistate consent order ($4.2 million penalty). Wise will reapply under the GENIUS Act framework.", short="Trust bank charter",
              s=["pers", "biz"], st="flux", ay="Jun 2025", div="us", neo=[0, ""],
              mc="Without a charter Wise cannot join US card networks and relies on sponsor banks.",
              src=[["Wise: trust bank charter, Jul 2026", OCC], ["Wise: Form 20-F, Jun 2026", F20]]),
        ]},
        {"id": "1.3", "ic": "chart-candlestick", "name": "Listing & control", "blurb": "Nasdaq WSE, founder-led.", "div": "grp", "rev": "grp", "products": [
            P("nasdaq", "Nasdaq primary listing", "Wise Group plc (Jersey) became the holding company on 8 May 2026 and listed on Nasdaq as WSE on 11 May 2026, keeping a secondary London listing; London-listed since July 2021. Shares closed about $15.40 on the first day ⚠.", short="Nasdaq listing",
              s=["pers"], st="new", ay="May 2026", neo=[0, ""], src=[["FStech: Nasdaq debut, May 2026", NASDAQ], ["Wise: FY26 results, Jun 2026", FY26]]),
            P("control", "Dual-class control and leadership", "Class B shares hold about 58% of votes (May 2026), including co-founder and CEO Kristo Käärmann's; a 10-year extension passed in July 2025 (90.58% of Class A votes) over co-founder Taavet Hinrikus's objection. CFO Emmanuel Thomassin, CPO Nilan Peiris, CTO Harsh Sinha, Chair David Wells.", short="Control & leadership",
              s=["pers"], neo=[0, ""], src=[["UKTN: shareholder vote, Jul 2025", VOTE], ["Wise: Form 20-F, Jun 2026", F20]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology", "blurb": "One stack, 4.7m payments a day.", "div": "grp", "rev": "grp", "products": [
            P("stack", "In-house global stack", "One in-house technology stack with more than 1,000 engineers, over 4.7 million transactions a day and more than 99% straight-through processing on Platform transfers; over 8,000 staff in 11 key locations.",
              s=["pers", "bank"], o="B", neo=[0, ""], src=[["Wise: Form 20-F, Jun 2026", F20], ["Wise Platform", PLAT]]),
        ]},
        {"id": "1.5", "ic": "coins", "name": "Float & funding", "blurb": "$41bn held for customers.", "div": "grp", "rev": "interest", "products": [
            P("float", "Customer holdings", "$41.2 billion of customer holdings (June 2026); interest income on customer balances of $806.1 million in FY26, of which $196.9 million was paid back to customers.",
              s=["pers", "save"], lc="borrow", neo=[0, ""], src=[["Wise: FY26 results, Jun 2026", FY26], ["Wise Q1 FY27, Jul 2026 (FX News Group)", Q1]]),
            P("funding", "Debt funding", "A £330 million revolving credit facility (December 2024, undrawn at March 2026) and a £2 billion EMTN programme (November 2025) with £250 million of 5.1% notes due 2030.",
              s=["pers"], neo=[0, ""], src=[["Wise: Form 20-F, Jun 2026", F20]]),
        ]},
        {"id": "1.6", "ic": "target", "name": "Strategy", "blurb": "\"The\" network for money.", "div": "grp", "rev": "grp", "products": [
            P("strategy", "Strategy and targets", "Build \"the\" network for the world's money: more licences and direct rail connections, Wise Platform above 50% of cross-border volume in the long run (about 6% now), and lower prices; net revenue growth of 15–20% a year from FY24 and a 20–25% pre-tax margin while rates stay high.",
              s=["pers", "bank"], neo=[0, ""], src=[["Wise: FY26 results, Jun 2026", FY26], ["Wise: Form 20-F, Jun 2026", F20], ["FXC Intelligence: Wise Q1 FY27", FXCQ1]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "How money moves: cross-border transfers at a 0.50% take rate, direct links to domestic payment systems in eight markets, a debit card now issued mainly on Visa after starting on Mastercard, business cards, local account details, and push-to-card payouts.",
    "tiles": [
        {"id": "2.1", "ic": "send", "name": "Cross-border transfers", "blurb": "$243bn at 0.52%.", "div": "wise", "rev": "xb", "products": [
            P("xborder", "International transfers", "$243.5 billion sent in FY26 in 40+ currencies to 160+ countries, at the mid-market rate; cross-border revenue $1,257.0 million; 77% of transfers instant in Q1 FY27.",
              s=["pers", "biz"], lc="move", o="B", neo=[0, "Account to account."], src=[["Wise: FY26 results, Jun 2026", FY26], ["Wise Q1 FY27, Jul 2026 (FX News Group)", Q1], ["Wise Platform", PLAT]]),
            P("pricing", "Falling take rate", "Average cross-border fee 0.58% in FY25, 0.52% in FY26 and 0.50% in Q1 FY27, the lowest Wise has charged, with a further 1–2 basis points of cuts expected.",
              s=["pers", "biz"], lc="move", neo=[0, ""], src=[["Wise: FY26 results, Jun 2026", FY26], ["Wise Q1 FY27, Jul 2026 (FX News Group)", Q1]]),
        ]},
        {"id": "2.2", "ic": "network", "name": "Direct access", "blurb": "Eight domestic systems.", "div": "grp", "rev": "xb", "products": [
            P("fps", "UK Faster Payments", "The first non-bank to be a directly connected settling participant in UK Faster Payments (2018).",
              s=["pers", "biz"], lc="move", ay="2018", o="B", neo=[0, "Domestic rail."], src=[["Wise: Form 20-F, Jun 2026", F20]]),
            P("direct", "Direct links in eight markets", "Direct access to domestic payment systems in the UK, Europe, Hungary, Australia, Singapore, the Philippines, Japan and Brazil (Japan and Brazil added in FY26); more than half of FY26 transactions used a direct link.", short="Direct links",
              s=["pers", "biz", "bank"], lc="move", st="new", o="B", neo=[0, "Domestic rails."],
              mc="Each new direct link is volume that skips both card networks' money-movement products.",
              src=[["Wise Platform", PLAT], ["Wise: FY26 results, Jun 2026", FY26], ["Wise: Form 20-F, Jun 2026", F20]]),
        ]},
        {"id": "2.3", "ic": "credit-card", "name": "Wise Card", "blurb": "$43.6bn spend, mostly Visa.", "div": "wise", "rev": "card", "products": [
            P("card", "Wise debit card", "A multi-currency debit card spending in 40+ currencies, with free ATM withdrawals up to £250 or $250 a month; $43.6 billion card spend and $391.6 million card revenue in FY26. Current UK and US cards are Visa; earlier Mastercard cards are still in use ⚠ (no public split).", short="Wise Card",
              s=["pers", "trav"], lc="everyday", o="P", at="Visa; Mastercard (legacy)", neo=[1, "Mostly Visa now; a Mastercard tail."],
              mc="The single biggest win-back: a 37%-growth debit portfolio Mastercard launched.",
              src=[["Wise: UK card", UKCARD], ["Wise: US card", USCARD], ["Wise: where will my card work", HELP], ["Wise: FY26 results, Jun 2026", FY26]]),
            P("mccard", "Mastercard debit, 2018–2020", "The first Wise card launched in Europe on Mastercard in 2018 and in the US in June 2019 (Community Federal Savings Bank); by August 2020 more than 1 million Mastercard cards, and a deal to issue wherever Mastercard is accepted and Wise is licensed.", short="Mastercard debit (legacy)",
              s=["pers", "trav"], lc="everyday", st="flux", ay="2018", o="P", at="Mastercard", neo=[2, "Wholly Mastercard, now being replaced."],
              src=[["Mastercard: TransferWise partnership, Aug 2020", MC2020], ["Wise: US Mastercard launch, Jun 2019", USBLOG]]),
            P("visacard", "Visa global card deal", "A global Visa partnership (27 January 2021), the first on Visa Cloud Connect, to take the card into APAC, Europe, Latin America, the Middle East, the UK and the US; new cards move to Visa at renewal ⚠ (no Wise announcement found).", short="Visa card deal",
              s=["pers", "trav"], lc="everyday", ay="Jan 2021", o="P", at="Visa", neo=[0, "Visa."],
              src=[["Visa: TransferWise partnership, Jan 2021", VISA2021], ["Comparateur Banque: switch to Visa, 2024", FR]]),
            P("digital", "Digital cards and wallets", "Virtual cards with refreshable details, Apple Pay and Google Pay (and Samsung Pay in the US), freeze and unfreeze, and a notification for every payment.",
              s=["pers", "trav"], lc="everyday", neo=[1, "Tokens on the card's network, mostly Visa."], src=[["Wise: UK card", UKCARD], ["Wise: US card", USCARD]]),
            P("fifa", "Wise Visa FIFA World Cup 26 card", "A free, limited-edition digital Visa card in 17 countries for the 2026 World Cup (June 2026), with Visa as the tournament sponsor.", short="FIFA World Cup card",
              s=["pers", "trav"], lc="grow", st="new", ay="Jun 2026", o="P", at="Visa", neo=[0, "Visa."], src=[["Wise: FIFA World Cup card, Jun 2026", FIFA]]),
        ]},
        {"id": "2.4", "ic": "briefcase-business", "name": "Business cards", "blurb": "Team cards, 0.5% cashback.", "div": "biz", "rev": "card", "products": [
            P("bizcard", "Wise Business card", "Physical and digital team cards (£3 each after a £50 set-up fee) with limits by person, card or group, and 0.5% cashback for UK businesses; business card spend in North America drove Q1 FY27 card growth. Network not stated ⚠.", short="Business card",
              s=["biz"], lc="everyday", neo=[None, "Network not stated."],
              mc="The fastest-growing card line, with no named network.",
              src=[["Wise: Business card", BIZCARD], ["FXC Intelligence: Wise Q1 FY27", FXCQ1]]),
        ]},
        {"id": "2.5", "ic": "arrow-left-right", "name": "Receive & pay in", "blurb": "Local details, 22 currencies.", "div": "wise", "rev": "other", "products": [
            P("receive", "Local account details", "Local account details to receive money in 22 currencies, with local instant pay-ins (Chile from July 2026) and, in Canada, Interac e-Transfer on the Chequing Account.",
              s=["pers", "biz"], lc="move", neo=[0, "Domestic rails."], src=[["Wise: UK card", UKCARD], ["Wise Q1 FY27, Jul 2026 (FX News Group)", Q1], ["Wise newsroom", NEWS]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Push to card", "blurb": "Mastercard Send, Visa Direct.", "div": "wise", "rev": "xb", "products": [
            P("mcsend", "Mastercard Send", "Near-real-time transfers to Mastercard cards in Spain, Romania, Bulgaria, the Czech Republic, Hungary, Poland, Ukraine, Georgia, Croatia and Russia (August 2020); current use not confirmed ⚠.", short="Mastercard Send",
              s=["pers"], lc="move", st="unconf", ay="Aug 2020", o="P", at="Mastercard", neo=[3, "Mastercard Send."],
              mc="The one Mastercard money-movement product Wise has used; now part of Mastercard Move.",
              src=[["Mastercard: TransferWise partnership, Aug 2020", MC2020]]),
            P("visadirect", "Visa Direct", "Push-to-card transfers on Visa Direct, starting in Spain with Romania, Hungary, the Czech Republic and Bulgaria planned (about 2019 ⚠); current use not confirmed.",
              s=["pers"], lc="move", st="unconf", o="P", at="Visa", neo=[0, "Visa."], src=[["Finextra: Visa and TransferWise", VISADIRECT]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every transfer: machine-learning financial-crime checks and KYC, AI copilots for staff, the Wise Platform API, Swift correspondent services for banks, interest and investments on balances, and tools for business accounting and cashback.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Financial crime & KYC", "blurb": "99% of checks in under a second.", "div": "grp", "rev": "grp", "products": [
            P("fincrime", "Financial-crime models", "Machine-learning models for financial crime and fraud, with 99% of compliance checks finished in under a second; the OCC still cited anti-money-laundering weaknesses in July 2026.", short="Financial crime",
              s=["pers", "biz", "bank"], lc="everyday", o="B", neo=[0, "Own models."],
              mc="AML and fraud tooling is a live need after the OCC decision.",
              src=[["Wise: Form 20-F, Jun 2026", F20], ["Wise: trust bank charter, Jul 2026", OCC]]),
            P("kyc", "Onboarding and KYC", "Wise's onboarding and compliance checks, which Platform partners can embed in their own products.",
              s=["bank", "ent"], lc="open", o="B", neo=[0, "Own."], src=[["Wise Platform", PLAT]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI", "blurb": "Copilots for crime and support.", "div": "grp", "rev": "grp", "products": [
            P("ai", "AI copilots and document AI", "Large-language-model copilots for Financial Crime and Customer Support teams, AI document processing, and machine learning for currency-flow prediction and risk; no customer AI product announced.", short="AI copilots",
              s=["pers"], lc="everyday", st="new", o="B", neo=[0, "Own."], src=[["Wise: Form 20-F, Jun 2026", F20]]),
        ]},
        {"id": "3.3", "ic": "code-xml", "name": "Platform API", "blurb": "Send, receive, accounts, cards.", "div": "plat", "rev": "xb", "products": [
            P("api", "Wise Platform API", "One API for partners to send, receive, hold multi-currency accounts and issue cards, with more than 99% straight-through processing and 77% of instant payments arriving in under 20 seconds.",
              s=["bank", "ent"], lc="open", o="B", neo=[0, "Own."], src=[["Wise Platform", PLAT]]),
        ]},
        {"id": "3.4", "ic": "globe", "name": "Correspondent Services", "blurb": "Swift into Wise.", "div": "plat", "rev": "xb", "products": [
            P("swiftcs", "Correspondent Services", "Banks send ordinary Swift MT or MX messages and Wise delivers the payment (Swift partnership, September 2023); 57% instant at launch.",
              s=["bank"], lc="move", ay="Sep 2023", o="P", at="Swift", neo=[0, "Swift and Wise rails."],
              mc="A direct rival to Mastercard Move for bank cross-border flows.",
              src=[["FXC Intelligence: Swift and Wise, Sep 2023", SWIFT], ["Wise Platform", PLAT]]),
        ]},
        {"id": "3.5", "ic": "trending-up", "name": "Interest & Assets", "blurb": "$9bn invested.", "div": "assets", "rev": "interest", "products": [
            P("assets", "Wise Assets", "Balances invested in funds through Wise Assets: $9.0 billion under custody (March 2026), rolled out to Brazil in FY26.",
              s=["save"], lc="beyond", o="B", neo=[0, ""], src=[["Wise: Form 20-F, Jun 2026", F20], ["Wise: FY26 results, Jun 2026", FY26]]),
            P("interest", "Interest on balances", "Interest on held balances: 3.40% APY on US dollars in the US (September 2026), and a multi-currency Interest feature in Canada (May 2026).",
              s=["save", "pers"], lc="beyond", st="new", neo=[0, ""], src=[["Wise: US card", USCARD], ["Wise newsroom", NEWS]]),
        ]},
        {"id": "3.6", "ic": "receipt-text", "name": "Business tools", "blurb": "Receipts, Xero, cashback.", "div": "biz", "rev": "other", "products": [
            P("accounting", "Receipts and accounting sync", "Receipt capture in the app and sync with Xero and QuickBooks; cardholders grouped by team, project or location.",
              s=["biz"], lc="everyday", neo=[0, ""], src=[["Wise: Business card", BIZCARD]]),
            P("cashback", "Business cashback", "0.5% cashback on eligible card spend for UK-registered businesses.",
              s=["biz"], lc="grow", neo=[None, "Card network not stated."], src=[["Wise: Business card", BIZCARD]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "Who buys: 11.3 million active personal customers, about 850,000 businesses in 79 countries, and banks and enterprises on Wise Platform, from Morgan Stanley to Capitec.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Wise Account", "blurb": "11.3m active people.", "div": "wise", "rev": "xb", "products": [
            P("account", "Wise Account", "A multi-currency account in 40 currencies; 11.26 million active personal customers and $48 billion of personal cross-border volume in Q1 FY27.",
              s=["pers", "trav"], lc="open", o="B", neo=[0, ""], src=[["Wise Q1 FY27, Jul 2026 (FX News Group)", Q1], ["FXC Intelligence: Wise Q1 FY27", FXCQ1], ["Wise: Form 20-F, Jun 2026", F20]]),
            P("chequing", "Canada Chequing Account", "A chequing account for Canadians with no monthly fee, Interac e-Transfer, CDIC eligibility and Group Spend (September 2026), after Wise joined Payments Canada (January 2026).", short="Canada Chequing",
              s=["pers"], lc="open", st="new", ay="Sep 2026", neo=[0, ""], src=[["Wise newsroom", NEWS]]),
            P("markets", "New markets", "Launches in Mexico (January 2025) and Chile (July 2026), an account and card in Thailand, and new licences in South Africa and the UAE.",
              s=["pers"], lc="open", st="new", neo=[None, "Card network by market not public."], src=[["Wise newsroom", NEWS], ["Wise: Thailand launch", THAI], ["Wise: FY26 results, Jun 2026", FY26]]),
            P("youth", "Young Explorer card", "A card for 6 to 17 year olds in the UK.",
              s=["pers"], lc="open", neo=[0, "UK cards are Visa ⚠."], src=[["Wise: UK card", UKCARD]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "Wise Business", "blurb": "850k firms, 31% of volume.", "div": "biz", "rev": "xb", "products": [
            P("business", "Wise Business", "About 850,000 active business customers in 79 countries (FY26); 608,000 active in Q1 FY27 (+28%), 5% of customers but 31% of cross-border volume ($21 billion, +39%).",
              s=["biz"], lc="everyday", o="B", neo=[None, "Card network not stated."],
              mc="Commercial-card and spend-control territory, growing fastest.",
              src=[["Wise: Form 20-F, Jun 2026", F20], ["FXC Intelligence: Wise Q1 FY27", FXCQ1]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Wise Platform", "blurb": "Banks on Wise's rails.", "div": "plat", "rev": "xb", "products": [
            P("platform", "Wise Platform", "Cross-border infrastructure for banks and enterprises, about 6% of cross-border volume (Q1 FY27) and under 10% of transaction revenue; partners include Morgan Stanley, Standard Chartered, Nubank, Bank Mandiri, Monzo, N26, Google Pay, Bolt and Itaú.",
              s=["bank", "ent"], lc="move", o="B", neo=[0, "Wise's own network."],
              mc="Banks that might use Mastercard Move use Wise instead.",
              src=[["Wise Platform", PLAT], ["FXC Intelligence: Wise Q1 FY27", FXCQ1], ["Wise: Form 20-F, Jun 2026", F20]]),
            P("newpartners", "New Platform banks", "UniCredit, Raiffeisen Bank and MBSB Bank in FY26 and Capitec in South Africa (April 2026); Itaú's instant foreign-currency payments (March 2025).", short="New partner banks",
              s=["bank"], lc="move", st="new", o="P", at="UniCredit, Raiffeisen, MBSB, Capitec", neo=[0, ""], src=[["Wise: FY26 results, Jun 2026", FY26], ["Wise newsroom", NEWS]]),
            P("platcards", "Platform card issuing", "Partners can issue cards and multi-currency accounts on Wise; Nubank uses Wise for an international account ⚠. The network behind partner cards is not public.", short="Platform cards",
              s=["bank"], lc="everyday", o="B", neo=[None, "Network not public."],
              mc="An open network choice inside partner banks.",
              src=[["Wise Platform", PLAT]]),
        ]},
        {"id": "4.4", "ic": "store", "name": "Enterprises & fintechs", "blurb": "Upwork, Wealthsimple.", "div": "plat", "rev": "xb", "products": [
            P("payouts", "Enterprise payouts", "Upwork pays freelancers through Wise Platform (September 2025); Wealthsimple offers Canadians transfers to 30 countries (November 2025).", short="Enterprise payouts",
              s=["ent"], lc="move", st="new", o="P", at="Upwork, Wealthsimple", neo=[0, "Wise rails."],
              mc="Payout use cases Mastercard Move also targets.",
              src=[["Wise newsroom", NEWS]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Wise: its own app and website with 24/7 support, partner banks' apps and Swift, and 11 key offices from London to Austin.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "App & web", "blurb": "Wise's own front door.", "div": "wise", "rev": "grp", "products": [
            P("app", "Wise app and website", "Account opening in minutes, a digital card at once, and 24/7 support; rated 4.3 out of 5 on more than 200,000 Trustpilot reviews.",
              s=["pers", "biz", "trav"], lc="open", o="B", neo=[0, ""], src=[["Wise: UK card", UKCARD], ["Wise: US card", USCARD]]),
        ]},
        {"id": "5.2", "ic": "plug", "name": "Partner channels", "blurb": "Inside other banks' apps.", "div": "plat", "rev": "grp", "products": [
            P("partnerapps", "Embedded in partner apps", "Wise transfers sold under partner brands: Itaú, Nubank, Monzo, Google Pay and others; Swift members reach Wise through Correspondent Services.",
              s=["bank", "ent"], lc="open", o="P", neo=[0, ""], src=[["Wise Platform", PLAT], ["Wise newsroom", NEWS], ["FXC Intelligence: Swift and Wise, Sep 2023", SWIFT]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Offices", "blurb": "11 key locations.", "div": "grp", "rev": "grp", "products": [
            P("offices", "Offices and hubs", "Over 8,000 staff of 130 nationalities in 11 key locations and about 53 subsidiaries in 24 countries; the Austin hub grew by 200% (September 2025).",
              s=["pers"], lc="open", neo=[0, ""], src=[["Wise: Form 20-F, Jun 2026", F20], ["Wise newsroom", NEWS]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Wise", "blurb": "First card, now a tail.", "products": [
        P("mcatwise", "Mastercard at Wise", "Mastercard carried the first Wise card (Europe 2018, US 2019), more than 1 million cards by August 2020, and Mastercard Send payouts in ten European markets. Visa signed a global deal in January 2021 and current UK and US cards are Visa. No Mastercard–Wise announcement found since 2020.",
          s=["pers"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Mastercard: TransferWise partnership, Aug 2020", MC2020], ["Visa: TransferWise partnership, Jan 2021", VISA2021]]),
    ]},
    {"id": "pillar-market", "name": "Cross-border money", "blurb": "Banks, Revolut, remitters.", "products": [
        P("market", "The market", "Wise names Airwallex, Block, Chime, Flywire, Payoneer, PayPal, Revolut, MoneyGram, Western Union, Remitly, Mastercard and Visa as competitors, along with banks not yet on Wise Platform; US rules are shifting with the GENIUS Act and a Fed proposal on master accounts.",
          s=["pers"], div="grp", rev="grp", src=[["Wise: Form 20-F, Jun 2026", F20], ["Wise: trust bank charter, Jul 2026", OCC]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
