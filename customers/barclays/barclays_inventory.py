"""Barclays' layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the H1 2026 results (28 July 2026) and the
2025 annual report (February 2026). ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's
own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

IR = "https://home.barclays/content/dam/home-barclays/documents/investor-relations/"
H1 = IR + "ResultAnnouncements/H12026Results/Q226-BPLC-Results-RA.pdf"
H1P = IR + "ResultAnnouncements/H12026Results/Q226-Results-Presentation.pdf"
FY25 = IR + "ResultAnnouncements/FullYear2025Results/FY25-BPLC-Results-RA.pdf"
FY25P = IR + "ResultAnnouncements/FullYear2025Results/FY25-Results-and-Targets-Update-Presentation.pdf"
AR25 = IR + "reports-and-events/annual-reports/2025/Barclays-PLC-Annual-Report-2025.pdf"
HIST = "https://home.barclays/who-we-are/our-history/"
LEAD = "https://home.barclays/who-we-are/structure-and-leadership/leadership/"
NEWS = "https://home.barclays/news/press-releases/"
VISA20 = NEWS + "2020/02/barclays-extends-long-standing-visa-partnership-with-new-europea"
TESCO = NEWS + "2024/11/completion-of-the-acquisition-of-tesco-s-retail-banking-business"
JETBLUE = NEWS + "2025/01/jetblue-and-barclays-launch-premier-credit-card-packed-with-prem"
BCUK = "https://www.barclaycard.co.uk/personal/credit-cards"
BCP = "https://www.barclaycard.co.uk/business"
DEBIT = "https://www.barclays.co.uk/current-accounts/debit-cards/"
USC = "https://cards.barclaycardus.com/banking/cards/"
USN = "https://cards.barclaycardus.com/banking/about-us/newsroom/"
FRONTIER = "https://www.chartmill.com/news/external/61871/prnews-2026-6-30-frontier-airlines-and-barclays-extend-long-term-partnership-to-deliver-more-value-for-frontier-airlines-world-mastercard-cardmembers"
GM = "https://www.paymentsdive.com/news/barclays-replaces-goldman-sachs-as-gm-card-issuer/729730/"
AA = "https://frequentmiler.com/barlcays-aviator-to-citi-transition-april-2026-what-we-know-and-what-we-dont"
POINTS = "https://www.thepointcalculator.com/us/credit-cards/issuers/barclays/"
BROOK = "https://www.fintechfutures.com/m-a/barclays-partners-brookfield-to-spin-out-payments-business"
UBYX = "https://www.paymentsjournal.com/barclays-takes-stake-in-u-s-stablecoin-settlement-platform-ubyx"
CFR = "https://www.pymnts.com/fraud-prevention/2024/mastercard-taps-ai-to-tackle-uk-app-fraud-epidemic"
PSR = "https://www.psr.org.uk/information-for-consumers/app-scams-reimbursement-dashboard"
GOH = "https://fintechfutures.com/m-a/barclays-to-buy-uk-money-app-gohenry"
SAMSUNG = "https://news.bloomberglaw.com/mergers-and-acquisitions/barclays-partners-with-samsung-to-launch-us-credit-card"
AVIOS = "https://www.headforpoints.com/2022/07/02/two-weeks-50000-avios-bonus-barclaycard"
WHICH = "https://www.which.co.uk/news/article/tesco-bank-to-be-sold-to-barclays-what-customers-need-to-know-aMUR11N67StQ"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · ring-fence · heritage", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: a £1.7 trillion balance sheet split by the ring-fence, three centuries since Lombard Street, the first credit card and cash machine in Britain, a near-total move to the cloud, and a 2028 plan to grow in the UK.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & capital", "blurb": "£1.7 trillion, RoTE 14.8%.", "div": "grp", "rev": "grp", "products": [
            P("balance", "Balance sheet", "Total assets of £1,730 billion, customer loans of £359 billion and deposits of £594 billion at 30 June 2026; more than 20 million UK and 25 million US customers.",
              s=["corp"], neo=[0, ""], src=[["H1 2026 results", H1], ["Annual report 2025", AR25]]),
            P("earnings", "Earnings & capital", "Income of £29.1 billion and RoTE of 11.3% in 2025; £16.5 billion and 14.8% in the first half of 2026; CET1 14.3%; 2026 income guidance raised to about £31.5 billion; market value about £58 billion in mid-October 2026.",
              s=["corp"], neo=[0, ""], src=[["H1 2026 results", H1], ["FY2025 results", FY25]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Entities & leadership", "blurb": "Ring-fenced and not.", "div": "grp", "rev": "grp", "products": [
            P("entities", "The ring-fence", "Barclays Bank UK PLC holds UK retail and small-business deposits; Barclays Bank PLC the Investment Bank and international; Barclays Bank Delaware the US cards; Barclays Execution Services runs technology and operations. Rated A1, A+ and AA- at bank level.",
              s=["corp"], neo=[0, ""], src=[["Annual report 2025", AR25], ["Barclays: credit ratings", "https://home.barclays/investor-relations/fixed-income-investors/credit-ratings/"]]),
            P("leadership", "Board & leadership", "Chair Nigel Higgins, Group CEO C.S. Venkatakrishnan, Group Finance Director Anna Cross; Vim Maru runs Barclays UK, Matt Hammerstein the UK Corporate Bank, Denny Nealon the US Consumer Bank.",
              s=["corp"], neo=[0, ""], src=[["Barclays: leadership", LEAD]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage", "blurb": "Lombard Street, 1690.", "div": "barclays", "rev": "grp", "products": [
            P("heritage", "Firsts", "Goldsmith bankers on Lombard Street from 1690; Barclaycard, Britain's first credit card, in 1966 (with BankAmericard, now Visa); the first cash machine at Enfield in 1967; Connect, the first UK debit card, in 1987.",
              s=["con", "corp"], o="I", neo=[0, ""], src=[["Barclays: our history", HIST]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "Nine-tenths in the cloud.", "div": "grp", "rev": "grp", "products": [
            P("tech", "Cloud, AI platform & Copilot", "Almost 90% of the estate in the cloud; Barclays' own AI platform with more than 250 tools and models; about 100,000 Microsoft 365 Copilot licences; AI coding tools for 19,000 developers; partners AWS, Microsoft, GitLab and Databricks.",
              s=["corp"], o="P", at="Microsoft, AWS", neo=[0, ""], src=[["Annual report 2025", AR25], ["FY2025 presentation", FY25P]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "Simpler, better, more balanced.", "div": "grp", "rev": "grp", "products": [
            P("strategy", "2028 targets", "Shift capital to the UK, grow UK lending more than 5% a year, RoTE above 14% and more than £15 billion returned over 2026–28, with the Investment Bank held to about half of group capital.",
              s=["corp"], neo=[0, ""], src=[["H1 2026 results", H1], ["FY2025 presentation", FY25P]]),
            P("deals", "In and out", "Kensington Mortgages (2023), Tesco Bank (November 2024), the GM card book (2025), Best Egg (May 2026) and GoHenry (agreed June 2026) in; German consumer finance, Entercard and the American Airlines cards (to Citi, April 2026) out.",
              s=["con", "corp"], o="A", st="new", neo=[0, ""], src=[["H1 2026 results", H1], ["FY2025 results", FY25]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: Visa debit for UK current accounts, Barclaycard (mostly Visa, with Avios and Tesco on Mastercard), US partner cards (mostly Mastercard), Barclaycard Payments with Brookfield, commercial cards and transaction banking, and a first step into stablecoin settlement.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "UK debit", "blurb": "Visa.", "div": "uk", "rev": "uk", "products": [
            P("debit", "Barclays Visa debit", "Debit cards for every UK current account, on Visa under the multi-year European partnership renewed in 2020; Barclays then processed nearly half of UK card transactions.",
              s=["con", "sme"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."],
              mc="The biggest prize if the 2020 Visa agreement, of undisclosed term, comes up for renewal.",
              src=[["Barclays: debit cards", DEBIT], ["Barclays and Visa, Feb 2020", VISA20]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Barclaycard UK", "blurb": "About £16 billion of balances.", "div": "barclaycard", "rev": "uk", "products": [
            P("barclaycard", "Barclaycard Platinum, Rewards, Forward & Amazon", "1.4 million new card customers in 2025 and about £16 billion of balances with Tesco; Rewards is Visa, and the Platinum, Forward and Amazon cards ⚠ most likely Visa too.", short="Barclaycard (Visa)",
              s=["con"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Barclaycard: credit cards", BCUK], ["FY2025 presentation", FY25P]]),
            P("avios", "Barclaycard Avios & Avios Plus", "Mastercard credit cards with IAG Loyalty since 2022; Avios Plus costs £20 a month.", short="Avios (Mastercard)",
              s=["con", "aff"], lc="grow", o="P", at="IAG Loyalty, Mastercard", ay="2022", neo=[2, "Mastercard."],
              src=[["Barclaycard: credit cards", BCUK], ["Head for Points, Jul 2022", AVIOS]]),
            P("tesco", "Tesco Bank Clubcard cards", "Tesco Bank's credit cards, historically Mastercard ⚠, came with the purchase in November 2024 and a ten-year exclusive Tesco partnership; Tesco Bank is now a trading name of Barclays Bank UK.", short="Tesco Bank (Mastercard)",
              s=["con"], lc="borrow", st="new", ay="Nov 2024", o="A", neo=[2, "Mastercard ⚠ current network unconfirmed."],
              mc="If Barclays moves Tesco onto Barclaycard's platform, the network is in play.",
              src=[["Barclays: Tesco Bank completion, Nov 2024", TESCO], ["Which?: Tesco Bank to Barclays, Feb 2024", WHICH]]),
        ]},
        {"id": "2.3", "ic": "plane", "name": "US partner cards", "blurb": "20 partners, mostly Mastercard.", "div": "us", "rev": "us", "products": [
            P("usmc", "US co-brands on Mastercard", "JetBlue (Premier, World Elite Mastercard, 2025), Emirates Skywards, Miles & More, Frontier (renewed June 2026), GM Rewards (won from Goldman Sachs), AARP, Carnival (new September 2026), Gap and Barnes & Noble (renewed June 2026).", short="Mastercard co-brands",
              s=["us"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard's real home at Barclays; renewals bring loyalty and data opportunities.",
              src=[["Barclays: JetBlue Premier, Jan 2025", JETBLUE], ["Frontier and Barclays, Jun 2026", FRONTIER], ["Payments Dive: GM cards, Oct 2024", GM]]),
            P("usvisa", "Wyndham, Holland America & Samsung (Visa)", "The Wyndham Rewards and Holland America cards are Visa, and so is the new Samsung Galaxy Card (July 2026, 5% back on Samsung, in Samsung Wallet).", short="Visa co-brands",
              s=["us"], lc="everyday", st="new", o="P", at="Visa", neo=[0, "Visa."],
              src=[["Point Calculator: Barclays cards, Jun 2026", POINTS], ["Bloomberg Law: Barclays and Samsung, Jul 2026", SAMSUNG]]),
            P("aadvantage", "AAdvantage Aviator (to Citi)", "The American Airlines cards, World Elite Mastercard, left for Citi on 24 April 2026, releasing £3.6 billion of capital; the volume stays on Mastercard but not at Barclays. Hawaiian's cards are closed to new applicants.", short="AAdvantage (exited)",
              s=["us"], lc="everyday", st="retired", neo=[2, "Mastercard, now at Citi."],
              src=[["Frequent Miler: Aviator to Citi, 2026", AA], ["H1 2026 results", H1]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Barclaycard Payments", "blurb": "160,000 businesses, with Brookfield.", "div": "pay", "rev": "ukcb", "products": [
            P("bcpayments", "Barclaycard Payments", "Acquiring for more than 160,000 UK businesses: card readers, gateway, currency conversion and cash advance. Since April 2025 a partnership with Brookfield (Barclays invests about £400 million; Brookfield may buy about 70% from year three), staying Barclays' acceptance provider for at least ten years.",
              s=["merch", "sme"], lc="move", neo=[1, "Accepts every network."],
              mc="A business being rebuilt with outside capital, and a home for Ethoca, Click to Pay and merchant risk tools.",
              src=[["Barclaycard Payments", BCP], ["FinTech Futures: Barclays and Brookfield, Apr 2025", BROOK]]),
        ]},
        {"id": "2.5", "ic": "arrow-left-right", "name": "Commercial cards & transaction banking", "blurb": "iPortal for every client.", "div": "barclays", "rev": "ukcb", "products": [
            P("commcards", "Commercial cards", "Select Cashback and Premium Plus business cards, a charge card, corporate, purchasing and fuel cards, and virtual payments.",
              s=["sme", "corp"], lc="move", neo=[None, "Network not stated."], src=[["Barclaycard: business", BCP]]),
            P("txbanking", "Transaction banking", "Cash management, trade and working capital and international payments for UK and international corporates, through iPortal for every corporate client in 2026.",
              s=["corp"], lc="move", neo=[0, ""], src=[["Annual report 2025", AR25]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Tokenised money", "blurb": "A stake in Ubyx.", "div": "barclays", "rev": "ib", "products": [
            P("ubyx", "Ubyx", "Barclays' first stablecoin investment (January 2026): a clearing network for stablecoins and tokenised deposits.",
              s=["corp"], lc="move", st="new", ay="Jan 2026", neo=[0, "Off the card networks."], src=[["PaymentsJournal: Barclays and Ubyx, Jan 2026", UBYX]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account and payment: machine learning on 450 million payments a month, AI across the bank, loyalty with Avios and Clubcard, and the open questions of agentic payments and scam scoring.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & scams", "blurb": "450 million payments a month.", "div": "uk", "rev": "uk", "products": [
            P("fraud", "Fraud & scam prevention", "Machine-learning models screen more than 450 million UK payments a month in under a second; App ID verifies Barclays callers; a founder of Stop Scams UK; external fraud losses of £180 million in 2025.",
              s=["con", "sme"], lc="everyday", neo=[0, "Barclays' own."],
              mc="Mandatory APP-scam reimbursement splits costs 50:50; Barclays is not named among Consumer Fraud Risk's banks.",
              src=[["Annual report 2025", AR25], ["PSR: APP reimbursement dashboard", PSR], ["PYMNTS: Consumer Fraud Risk, Sep 2024", CFR]]),
        ]},
        {"id": "3.2", "ic": "brain", "name": "AI in the bank", "blurb": "Copilot, BARXBot, call summaries.", "div": "grp", "rev": "grp", "products": [
            P("ai", "AI at work and for customers", "More than a million colleague hours saved in 2025; the Help Hub Assistant; BARXBot for FX quotes; generative-AI call summaries in US contact centres (8 million calls); a US 'Customer Assist' due in 2026.",
              s=["corp", "us"], lc="beyond", st="new", neo=[0, ""], src=[["Annual report 2025", AR25], ["Barclays US newsroom", USN]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Loyalty", "blurb": "Avios, Clubcard, Experiences.", "div": "barclaycard", "rev": "uk", "products": [
            P("loyalty", "Avios, Clubcard & Barclays Experiences", "Avios with IAG, Clubcard benefits with Tesco, Amazon rewards, Barclaycard Rewards cashback, and Barclays Experiences for Premier customers; in the US, partners' own programmes.",
              s=["con", "aff", "us"], lc="grow", neo=[1, "Avios and Tesco cards on Mastercard."],
              mc="Card-linked offers and Priceless for the Mastercard cards.",
              src=[["Barclaycard: credit cards", BCUK], ["Annual report 2025", AR25]]),
        ]},
        {"id": "3.4", "ic": "bot", "name": "Agentic & open banking", "blurb": "No network chosen.", "div": "barclays", "rev": "uk", "products": [
            P("agentic", "Agentic payments & open banking", "Barclays has not announced Mastercard Agent Pay or Visa Intelligent Commerce, and publishes little on its open-banking APIs.",
              s=["con", "merch"], lc="move", neo=[0, "Nothing announced."],
              mc="White space: Agent Pay for the Avios, Tesco and US Mastercard portfolios.",
              src=[["Digital Commerce 360: Visa and Mastercard in agentic commerce, Apr 2026", "https://www.digitalcommerce360.com/2026/04/02/visa-mastercard-in-agentic-commerce/"]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "Five divisions opened out into what customers buy: Barclays UK's current accounts and mortgages, business banking, the UK Corporate Bank, Private Bank & Wealth, the Investment Bank, and the US Consumer Bank with Best Egg.",
    "tiles": [
        {"id": "4.1", "ic": "wallet", "name": "UK retail", "blurb": "20 million customers.", "div": "uk", "rev": "uk", "products": [
            P("accounts", "Current accounts, savings & Premier", "Current accounts, the Savings Hub and ISAs for more than 20 million UK customers; about 1.1 million Premier customers.",
              s=["con", "aff"], lc="everyday", neo=[0, "Visa debit."], src=[["Annual report 2025", AR25], ["H1 2026 results", H1]]),
            P("mortgages", "Mortgages & Kensington", "A £177 billion mortgage book, Kensington for specialist lending, and a broker platform used by 26,000 brokers.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["H1 2026 results", H1], ["Annual report 2025", AR25]]),
            P("gohenry", "GoHenry", "A money app and card for children, 500,000 users, agreed in June 2026 and due to complete in the fourth quarter ⚠.",
              s=["con"], lc="open", st="new", o="A", neo=[None, "Card network not verified."], src=[["FinTech Futures: Barclays to buy GoHenry, Jun 2026", GOH]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "Business banking", "blurb": "Up to £6.5 million turnover.", "div": "uk", "rev": "uk", "products": [
            P("bizbank", "Business banking", "Banking for firms up to £6.5 million turnover: £17.7 billion of loans and £51.1 billion of deposits.",
              s=["sme"], lc="everyday", neo=[0, "Visa debit."], src=[["H1 2026 results", H1]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "UK Corporate Bank", "blurb": "A quarter of UK corporates.", "div": "barclays", "rev": "ukcb", "products": [
            P("ukcb", "UK Corporate Bank", "Lending and transaction banking for firms from £6.5 million turnover to the FTSE 350, with relationships with more than a quarter of UK corporates; RoTE 20.6%.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["H1 2026 results", H1], ["Annual report 2025", AR25]]),
        ]},
        {"id": "4.4", "ic": "gem", "name": "Private Bank & Wealth", "blurb": "£142 billion invested.", "div": "barclays", "rev": "pbwm", "products": [
            P("pbwm", "Private Bank, Premier Wealth & Direct Investing", "Private banking for clients with £5 million and more, Premier Wealth Management, Planning & Advice, and Barclays Direct Investing (formerly Smart Investor, custody fees dropped May 2026): £142.5 billion invested.",
              s=["aff"], lc="grow", neo=[0, ""], src=[["H1 2026 results", H1], ["H1 2026 presentation", H1P]]),
        ]},
        {"id": "4.5", "ic": "chart-candlestick", "name": "Investment Bank", "blurb": "Sixth worldwide.", "div": "ib", "rev": "ib", "products": [
            P("ib", "Markets & banking", "Equities, credit, rates, FX and prime; advisory and capital markets; the International Corporate Bank: sixth globally in markets and banking in 2025, income of £13.1 billion.",
              s=["corp"], lc="grow", neo=[0, ""], src=[["FY2025 results", FY25], ["H1 2026 presentation", H1P]]),
        ]},
        {"id": "4.6", "ic": "flag", "name": "US Consumer Bank", "blurb": "Cards, Best Egg, savings.", "div": "us", "rev": "us", "products": [
            P("usbank", "US Consumer Bank & Best Egg", "About $30 billion of card receivables after the AAdvantage sale, Best Egg personal loans (May 2026, $40 billion originated since 2013), and online savings of about $26.6 billion.",
              s=["us"], lc="borrow", st="new", neo=[1, "Most cards Mastercard."], src=[["H1 2026 results", H1], ["H1 2026 presentation", H1P]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Barclays: the app (14 million digitally active), 206 branches, partners from Tesco to JetBlue, and portals for brokers and corporates.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Apps", "blurb": "14.1 million digitally active.", "div": "uk", "rev": "uk", "products": [
            P("app", "Barclays & Barclaycard apps", "14.1 million digitally active UK customers, 99.98% availability, Siri payments and an app relaunch planned for 2026; the US app's use rose in 2025.",
              s=["con", "us"], lc="everyday", neo=[0, ""], src=[["H1 2026 results", H1], ["FY2025 presentation", FY25P]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches", "blurb": "206 in the UK.", "div": "uk", "rev": "uk", "products": [
            P("branches", "Branches", "206 branches at mid-2026, down from 221 at the end of 2024, 86 with extended hours.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["H1 2026 results", H1]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partners", "blurb": "Tesco, Amazon, IAG, JetBlue.", "div": "barclaycard", "rev": "us", "products": [
            P("partners", "Partner channels", "Tesco, Amazon and IAG in the UK; 20 US brands, AARP and Samsung Wallet in the US.",
              s=["con", "us"], lc="open", neo=[1, "Several partner cards on Mastercard."], src=[["Annual report 2025", AR25], ["Barclays US cards", USC]]),
        ]},
        {"id": "5.4", "ic": "monitor", "name": "Brokers & iPortal", "blurb": "26,000 brokers.", "div": "barclays", "rev": "ukcb", "products": [
            P("portals", "Broker platform & iPortal", "The digital mortgage-broker platform (45 minutes cut to 15) and iPortal, the single channel for corporate clients.",
              s=["home", "corp"], lc="open", neo=[0, ""], src=[["Annual report 2025", AR25]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Barclays", "blurb": "US co-brands, Avios, Tesco.", "products": [
        P("mcatbarclays", "Mastercard at Barclays", "No group agreement with Mastercard is public; Visa has been Barclays' UK scheme partner since 1966 and renewed in 2020. Mastercard carries most US co-brands (JetBlue, Emirates, Frontier, GM, AARP, Carnival, Barnes & Noble), the UK Avios cards and, historically, Tesco Bank's cards; American Airlines' Mastercard book left for Citi in 2026.",
          s=["corp"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Barclays and Visa, Feb 2020", VISA20], ["Barclays: JetBlue Premier, Jan 2025", JETBLUE]]),
    ]},
    {"id": "pillar-market", "name": "UK & US cards", "blurb": "Scams, Brookfield, co-brands.", "products": [
        P("market", "The market", "Mandatory APP-scam reimbursement in the UK, Barclaycard leading UK credit cards, acquiring under pressure, and US co-brand contracts moving between issuers (AAdvantage to Citi, GM from Goldman).",
          s=["con"], div="grp", rev="grp", src=[["PSR: APP reimbursement dashboard", PSR], ["FinTech Futures: Barclays and Brookfield, Apr 2025", BROOK]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
