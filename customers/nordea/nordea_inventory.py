"""Nordea's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the Q3 2026 report (15 October 2026), the 2025
results (29 January 2026) and the 2030 strategy (5 November 2025). ``neo`` is the Mastercard lens: [depth, note],
where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

Q3 = "https://mb.cision.com/Public/434/4409162/bcaca891ce13b532.pdf"
Q3REL = "https://www.finanznachrichten.de/nachrichten-2026-10/69842506-nordea-bank-abp-third-quarter-results-2026-008.htm"
FY25 = "https://www.nordea.com/en/press/2026-01-29/fourth-quarter-and-full-year-results-2025"
STRAT = "https://www.nordea.com/en/press/2025-11-05/inside-information-nordea-announces-updated-strategy-and-new-financial-targets-for-2030"
RESTR = "https://www.nordea.com/en/press/2026-03-17/nordea-to-book-restructuring-costs-to-execute-its-2030-strategy-implementation"
GLT = "https://www.nordea.com/en/about-us/our-leadership"
GLTCHG = "https://www.nordea.com/en/press/2026-08-19/changes-in-nordeas-group-leadership-team"
BOARD = "https://www.nordea.com/en/about-us/corporate-governance/board-of-directors/members-of-the-board"
ABOUT = "https://www.nordea.com/en/about-us"
HIST = "https://www.nordea.com/en/about-us/who-are-we/our-history"
ORG = "https://www.nordea.com/en/about-us/our-organisation"
MARKETS = "https://www.nordea.com/en/about-us/who-are-we/our-markets"
RATINGS = "https://www.nordea.com/en/investors/debt-and-rating/current-rating"
EUROMONEY = "https://www.euromoney.com/article/bvjay01zwv4kc84skcwwsws0o/banking/nordics-and-baltics-best-digital-bank-2026-nordea/"
AGENT = "https://www.nordea.com/en/news/first-ever-finnish-ai-agent-payment-mastercard-and-nordea-completes-live-agentic-transaction"
DANSKE = "https://www.nordea.com/en/press/2024-11-18/nordea-completes-the-acquisition-of-danske-banks-personal-customer-and-private-banking-business-in-norway"
NETS15 = "https://www.nordea.com/en/press-and-news/news-and-press-releases/press-releases/2015/2015-06-15-nordea-to-divest-its-merchant-acquiring-business-to-nets.html"
NETS21 = "https://www.nets.eu/Media-and-press/news/Pages/Nordea-and-Nets-prolong-their-long-term-partnership-in-Denmark-and-Finland.aspx"
TIETO = "https://tietoevry.com/en/newsroom/all-news-and-releases/press-releases/2020/12/tietoevry-partners-with-nordea-to-deliver-card-services"
SE_DEBIT = "https://www.nordea.se/privat/produkter/kreditkort-bankkort/nordea-debit.html"
SE_GOLD = "https://www.nordea.se/privat/produkter/kreditkort-bankkort/nordea-gold.html"
SE_PREM = "https://www.nordea.se/privat/produkter/kreditkort-bankkort/nordea-premium.html"
DK_CARDS = "https://www.nordea.dk/privat/produkter/kort/"
NO_DEBIT = "https://www.nordea.no/privat/vare-produkter/bankkort/nordea-bankkort.html"
NO_GOLD = "https://www.nordea.no/privat/vare-produkter/kredittkort/kredittkortet-nordea-gold-mastercard.html"
FI_DEBIT = "https://www.nordea.fi/en/personal/our-services/credit-payment-cards/debit-cards.html"
FI_COMBI = "https://www.nordea.fi/en/personal/our-services/credit-payment-cards/credit-or-debit.html"
FI_CARDS = "https://www.nordea.fi/en/personal/our-services/credit-payment-cards/"
FI_TERMS = "https://www.nordea.fi/en/personal/our-services/amendments.html"
FI_C2P = "https://www.nordea.fi/en/personal/our-services/credit-payment-cards/click-to-pay.html"
FI_BIZCARDS = "https://www.nordea.fi/sv/foretag/vanliga-fragor/vanliga-fragor-om-foretagskort.html"
FI_BIZDEBIT = "https://www.nordea.fi/en/business/our-services/corporate-cards/business-visa-debit.html"
FI_USAGE = "https://www.nordea.fi/en/business/our-services/corporate-cards/card-usage-areas.html"
STOCKMANN = "https://www.analist.nl/corporatenieuws/persberichten/1210177-nordea-and-stockmann-to-start-card-cooperation-in-finland"
P27 = "https://www.mastercard.com/news/europe/en/newsroom/press-releases/en/2019/june/mastercard-and-p27-nordic-payments-platform-to-build-a-world-first-real-time-payments-system-across-the-region/"
RIKSBANK = "https://www.riksbank.se/en-gb/payments--cash/payments-in-sweden/payments-report-2026/developments-in-the-payments-market/modernising-the-payments-market/"
MOBILEPAY = "https://www.realtid.se/bors-finans/nordea-och-mobilepay-ingar-samarbete/"
OPENB = "https://www.fintechfutures.com/open-banking/nordea-flies-higher-with-open-banking-pilots"
MCOB = "https://www.mastercard.com/europe/en/business/open-finance/help-articles/nordics-dk-se-no-fi-nordea.html"
WERO = "https://en.wikipedia.org/wiki/Wero_(payment)"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · four countries · one platform", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: EUR 400 billion of loans and ROE of 15%, banks dating from 1820, a head office in Helsinki since 2018, one digital platform for four countries, and a 2030 plan built on Nordic scale.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "EUR 400bn of loans, ROE 15%.", "div": "group", "rev": "other", "products": [
            P("balance", "Balance sheet & earnings", "Loans of EUR 399.6 billion, deposits of EUR 259.0 billion and record assets under management of EUR 509 billion at 30 September 2026; Q3 2026 net profit EUR 1.18 billion, ROE 15.1%, CET1 15.8%; 2025 net profit EUR 4.84 billion; rated Aa3 (Moody's, October 2026), AA- (S&P) and AA (Fitch, May 2026); 28,376 staff.",
              s=["con"], neo=[0, ""], src=[["Q3 2026 report", Q3], ["Q3 2026 release", Q3REL], ["2025 results", FY25], ["Nordea: credit ratings", RATINGS]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Hester and Vang-Jensen.", "div": "group", "rev": "other", "products": [
            P("leadership", "Board & Group Leadership Team", "Chair Sir Stephen Hester, CEO Frank Vang-Jensen (since 2019), CFO Ian Smith; Per Långsved takes over Personal Banking from Sara Mella on 1 November 2026; Nina Arkilahti runs Business Banking, Petteri Änkilä LC&I and Martin A Persson Asset & Wealth Management; risk and compliance merge on 1 January 2027.",
              s=["corp"], st="flux", neo=[0, ""], src=[["Nordea: leadership", GLT], ["Nordea: leadership changes, Aug 2026", GLTCHG], ["Nordea: board", BOARD]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & home", "blurb": "From 1820; Helsinki since 2018.", "div": "group", "rev": "other", "products": [
            P("heritage", "Heritage & the move to Finland", "Roots in a Copenhagen savings bank of 1820 and banks in Sweden, Norway and Finland; four Nordic banks merged in the 1990s under one Nordea brand from 2001; re-domiciled to Helsinki on 1 October 2018, bringing ECB supervision; listed in Helsinki, Stockholm and Copenhagen with about 580,000 private shareholders.",
              s=["con"], o="I", neo=[0, ""], src=[["Nordea: history", HIST], ["Nordea: about us", ABOUT]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & processing", "blurb": "One platform, two processors.", "div": "group", "rev": "other", "products": [
            P("platform", "One Nordic digital platform", "A three-year consolidation replaced 22 codebases and 42 front ends with one platform for Nordea Mobile, Nordea Business and the netbanks in four countries; more than 70% of new features launch in every market at once.",
              s=["con", "sme"], neo=[0, ""], src=[["Euromoney: best digital bank, Jul 2026", EUROMONEY]]),
            P("processing", "Card issuing & processing", "Card processing is outsourced: TietoEVRY for Norway and Sweden (five-year deal, December 2020 ⚠) and Nets for Denmark and Finland (issuing, processing, fraud and disputes, renewed June 2021).",
              s=["con", "sme"], lc="everyday", o="P", at="TietoEVRY, Nets", neo=[0, "Processors, not networks."],
              mc="Two outsourced processors; payments is a Nordic scale area for 2030.",
              src=[["Nets: Nordea partnership, Jun 2021", NETS21], ["Tietoevry: Nordea card services, Dec 2020", TIETO]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "2030 strategy", "blurb": "EPS of about EUR 2 in 2030.", "div": "group", "rev": "other", "products": [
            P("strategy", "2030 strategy", "Be the best-performing financial services group in the Nordics: ROE above 15% every year, cost-to-income of 40–42% in 2030, EPS of about EUR 2 and more than EUR 20 billion of distributions; growth in Norway, Sweden, pensions, private banking and small businesses; Nordic scale in mortgages, corporate lending, savings and payments.",
              s=["corp"], st="new", ay="Nov 2025", neo=[0, ""], src=[["Nordea: 2030 strategy, Nov 2025", STRAT]]),
            P("restructure", "Restructuring", "EUR 190 million booked in Q1 2026 for at least EUR 150 million of annual savings from 2028; about 1,500 employees affected in 2026–27.",
              s=["corp"], st="new", ay="Mar 2026", neo=[0, ""], src=[["Nordea: restructuring, Mar 2026", RESTR]]),
            P("deals", "Deals", "Danske Bank's Norwegian personal-customer and private-banking business (completed 18 November 2024; 235,000 customers, EUR 9 billion of loans), Gjensidige Bank (2019); merchant acquiring sold to Nets for about EUR 230 million (2015).",
              s=["con"], o="A", neo=[0, ""], src=[["Nordea: Danske Norway completed, Nov 2024", DANSKE], ["Nordea: history", HIST], ["Nordea: acquiring sold to Nets, Jun 2015", NETS15]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Visa debit in every country (with Dankort and BankAxept), Mastercard on every credit and combination card, Mastercard and First Card for companies, wallets and Click to Pay, Swish and MobilePay, acceptance through Nets, and transaction banking.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "Visa in all four countries.", "div": "group", "rev": "pb", "products": [
            P("debitse", "Nordea Debit (Sweden)", "\"Our most common bank card\": Visa debit linked to the account, with travel insurance, Apple Pay, Google Pay and Samsung Pay, and FX at Visa's reference rate plus 1.65%.", short="Debit Sweden (Visa)",
              s=["con", "fam"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Nordea Sweden: Nordea Debit", SE_DEBIT]]),
            P("debitfi", "Nordea Debit (Finland)", "Debit card accepted where the Visa symbol shows, also a first card for minors; repriced into new service packages from 1 May 2026.", short="Debit Finland (Visa)",
              s=["con", "fam"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Nordea Finland: debit cards", FI_DEBIT]]),
            P("dankort", "Visa/Dankort & Nordea Pay (Denmark)", "Visa/Dankort co-badged debit (DKK 25,000 a week) and Nordea Pay, a Visa debit card with balance control from age 7 and Visa Cashback.", short="Debit Denmark (Dankort, Visa)",
              s=["con", "fam"], lc="everyday", o="P", at="Dankort, Visa", neo=[0, "Dankort and Visa."], src=[["Nordea Denmark: cards", DK_CARDS]]),
            P("bankaxept", "Nordea bankkort (Norway)", "BankAxept domestic debit co-badged with an international scheme for travel and online; the fee table lists Visa cash withdrawals ⚠.", short="Debit Norway (BankAxept, Visa ⚠)",
              s=["con", "fam"], lc="everyday", o="P", at="BankAxept, Visa", neo=[0, "BankAxept and Visa ⚠."], src=[["Nordea Norway: bankkort", NO_DEBIT]]),
            P("bizdebit", "Business Visa Debit", "SME debit card in the Nordea Digital package, with Apple Pay and Google Pay.", short="Business debit (Visa)",
              s=["sme"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Nordea Finland: Business Visa Debit", FI_BIZDEBIT]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit & combination cards", "blurb": "Mastercard in all four countries.", "div": "group", "rev": "pb", "products": [
            P("gold", "Nordea Gold", "Payment and credit card on Mastercard in all four countries: up to SEK 100,000 of credit with family travel insurance in Sweden, DKK 5,000–150,000 in Denmark, open to every Norwegian customer, and Finland's combination card with debit and credit sides.", short="Nordea Gold (Mastercard)",
              s=["con"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard's core at Nordea: the credit and combination book in four countries.",
              src=[["Nordea Sweden: Nordea Gold", SE_GOLD], ["Nordea Denmark: cards", DK_CARDS], ["Nordea Norway: Nordea Gold", NO_GOLD], ["Nordea Finland: credit or debit", FI_COMBI]]),
            P("premium", "Nordea Premium & Platinum", "Premium credit cards on Mastercard: LoungeKey access to more than 1,000 lounges and Mastercard Airport Experiences in Sweden; Platinum in Denmark (DKK 20,000–250,000) and Finland.", short="Premium (Mastercard)",
              s=["con", "saver"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Nordea Sweden: Nordea Premium", SE_PREM], ["Nordea Denmark: cards", DK_CARDS], ["Nordea Finland: cards", FI_CARDS]]),
            P("credit", "Nordea Credit", "Entry credit card on Mastercard (DKK 10,000–30,000 in Denmark); Finland's Mastercard Credit Account terms were updated in June 2026.", short="Nordea Credit (Mastercard)",
              s=["con"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Nordea Denmark: cards", DK_CARDS], ["Nordea Finland: amended terms", FI_TERMS]]),
            P("stockmann", "Stockmann Mastercard", "Co-branded credit card with the Finnish department store Stockmann since 2008, with no annual fee; still offered.",
              s=["con"], lc="borrow", ay="2008", o="P", at="Stockmann, Mastercard", neo=[2, "Mastercard."], src=[["Nordea and Stockmann, 2008", STOCKMANN], ["Nordea Finland: cards", FI_CARDS]]),
        ]},
        {"id": "2.3", "ic": "briefcase", "name": "Company cards", "blurb": "Business Mastercard, First Card.", "div": "finance", "rev": "bb", "products": [
            P("bizmc", "Nordea Business Mastercard", "Company credit card with an invoice per card and an online service for tracking transactions.", short="Business Mastercard",
              s=["sme", "corp"], lc="move", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Nordea Finland: company cards", FI_BIZCARDS]]),
            P("firstcard", "First Card", "Corporate charge card settled on one monthly invoice (about 30 days' credit), with a travel account, travel insurance and usage limits by region set in the First Card app; network not stated ⚠.",
              s=["sme", "corp"], lc="move", neo=[None, "Network not stated."], src=[["Nordea Finland: company cards", FI_BIZCARDS], ["Nordea Finland: card usage areas", FI_USAGE]]),
        ]},
        {"id": "2.4", "ic": "wallet", "name": "Wallets & Click to Pay", "blurb": "Both networks, Nordea ID.", "div": "group", "rev": "pb", "products": [
            P("wallets", "Apple Pay, Google Pay & Samsung Pay", "Nordea's Visa and Mastercard cards work in the main phone wallets in every country.",
              s=["con"], lc="everyday", o="P", at="Apple, Google, Samsung", neo=[1, "Both networks."], src=[["Nordea Sweden: Nordea Debit", SE_DEBIT], ["Nordea Finland: Business Visa Debit", FI_BIZDEBIT]]),
            P("c2p", "Click to Pay", "Online checkout without typing card details, offered \"in cooperation with Visa and Mastercard\": cards are enrolled in Nordea Mobile and confirmed in the Nordea ID app.",
              s=["con"], lc="everyday", o="P", at="Visa, Mastercard", neo=[1, "Mastercard and Visa."], src=[["Nordea Finland: Click to Pay", FI_C2P]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Mobile & instant payments", "blurb": "Swish, MobilePay, instant.", "div": "group", "rev": "pb", "products": [
            P("swish", "Swish", "Sweden's account-to-account mobile payment, developed with ten banks including Nordea and settled between bank accounts in the Riksbank's system.",
              s=["con", "sme"], lc="move", o="P", at="Swish banks", neo=[0, "Account-to-account."], src=[["Riksbank: Payments Report 2026", RIKSBANK]]),
            P("mobilepay", "MobilePay & Vipps", "Nordea joined Danske Bank's MobilePay as a partner bank ⚠ date; Vipps MobilePay is due to drop the MobilePay name in Denmark and Finland on 12 January 2027 ⚠.",
              s=["con"], lc="move", o="P", at="Vipps MobilePay", neo=[0, "Bank account and card-funded."], src=[["Realtid: Nordea and MobilePay", MOBILEPAY]]),
            P("instant", "Instant payments", "EU rules require instant euro transfers with payee verification; P27, the Nordic real-time platform Nordea co-owned, picked Mastercard as its technology partner in June 2019 but was later abandoned ⚠. Nordea's stance on Wero is not public ⚠.",
              s=["con", "corp"], lc="move", st="flux", ay="Jun 2019", o="P", at="P27 banks", neo=[0, "Mastercard's P27 role lapsed ⚠."], src=[["Mastercard: P27, Jun 2019", P27], ["Riksbank: Payments Report 2026", RIKSBANK], ["Wikipedia: Wero", WERO]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Acceptance", "blurb": "Sold to Nets in 2015.", "div": "group", "rev": "bb", "products": [
            P("acquiring", "Merchant acquiring with Nets", "Nordea sold its merchant acquiring business to Nets (now part of Nexi) for about EUR 230 million in 2015 and refers merchants to it under a partnership.",
              s=["sme"], lc="move", st="retired", ay="Jun 2015", o="P", at="Nets (Nexi)", neo=[1, "Nets accepts every network."], src=[["Nordea: acquiring sold to Nets, Jun 2015", NETS15]]),
        ]},
        {"id": "2.7", "ic": "arrow-left-right", "name": "Transaction banking", "blurb": "Cash management, ERP links.", "div": "group", "rev": "bb", "products": [
            P("txb", "Transaction Banking & Corporate Access", "Payment and cash-management services run inside Business Banking; Corporate Access Lite gives real-time file exchange with Sweden's largest ERP vendor, with a Nordic roll-out from 2026.",
              s=["sme", "corp"], lc="move", st="new", neo=[0, ""], src=[["Q3 2026 report", Q3], ["Euromoney: best digital bank, Jul 2026", EUROMONEY]]),
            P("paytab", "Payments tab", "A dedicated payments tab in Nordea's apps and netbanks puts all payment services and flows in one view (Q3 2026); payments and card fees were EUR 163 million in the quarter, up 4%.",
              s=["con"], lc="move", st="new", ay="Q3 2026", neo=[0, ""], src=[["Q3 2026 report", Q3]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: fraud handled with Nets and confirmed in Nordea ID, 1.6 billion in-app insights and the first Finnish agent payment on Mastercard, open banking since 2017, and card benefits split between Visa cashback and Mastercard travel.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & identity", "blurb": "Nordea ID, Nets fraud tools.", "div": "group", "rev": "pb", "products": [
            P("fraud", "Card fraud & disputes", "Nets handles card fraud prevention, detection and disputes for Nordea in Denmark and Finland (renewed 2021); the tools used in Norway and Sweden are not public ⚠.",
              s=["con", "sme"], lc="everyday", o="P", at="Nets", neo=[0, "Nets."],
              mc="No Mastercard fraud or scam tool is publicly in use.",
              src=[["Nets: Nordea partnership, Jun 2021", NETS21]]),
            P("nordeaid", "Nordea ID", "Nordea's authentication app, used to log in, confirm payments and enrol cards in Click to Pay.",
              s=["con"], lc="open", neo=[0, ""], src=[["Nordea Finland: Click to Pay", FI_C2P]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI & agents", "blurb": "First Finnish agent payment.", "div": "group", "rev": "pb", "products": [
            P("insights", "In-app insights & automated credit", "1.6 billion context-aware machine-learning nudges in 2025 for payments, savings and risk checks; instant KYC and automated risk scoring cut manual work on Norwegian credit-card applications by 80%.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Euromoney: best digital bank, Jul 2026", EUROMONEY]]),
            P("agentpay", "Agent Pay pilot", "Finland's first live agentic payment (5 June 2026): an AI agent bought a coffee-tasting package on Priceless.com with a Nordea Mastercard, using Mastercard Agent Pay and agentic tokens; led by Kirsi Wiitala, Nordea's Head of Transaction Banking, and Erik Gutwasser of Mastercard.", short="Agent Pay (Mastercard)",
              s=["con"], lc="move", st="new", ay="Jun 2026", o="P", at="Mastercard", neo=[3, "Mastercard Agent Pay."],
              mc="Mastercard's newest and clearest joint first with Nordea.",
              src=[["Nordea: first Finnish agent payment, Jun 2026", AGENT]]),
        ]},
        {"id": "3.3", "ic": "code-xml", "name": "Open banking", "blurb": "Portal since 2017.", "div": "group", "rev": "bb", "products": [
            P("openbanking", "Nordea Open Banking", "Developer portal and APIs launched in Finland at the end of 2017 and in Sweden in 2018.",
              s=["sme", "corp"], lc="open", ay="2017", neo=[0, "Nordea's own."], src=[["Fintech Futures: Nordea open banking", OPENB]]),
            P("mcob", "Mastercard Open Banking connection", "Mastercard's open-banking service connects to Nordea personal and corporate accounts in all four countries; corporate administrators can grant access, and payments always need user confirmation.",
              s=["sme"], lc="open", o="P", at="Mastercard", neo=[1, "Mastercard connects; not a Nordea programme."], src=[["Mastercard: Nordea connection guide", MCOB]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Card benefits", "blurb": "Visa cashback, Mastercard lounges.", "div": "group", "rev": "pb", "products": [
            P("cashback", "Cashback & card offers", "Visa Cashback on Nordea Pay in Denmark and card cashback offers in Sweden.",
              s=["con", "fam"], lc="grow", o="P", at="Visa", neo=[0, "Visa Cashback."],
              mc="Card-linked offers on the Mastercard credit book are open ground.",
              src=[["Nordea Denmark: cards", DK_CARDS], ["Nordea Sweden: Nordea Debit", SE_DEBIT]]),
            P("travel", "Travel benefits", "Mastercard LoungeKey and Mastercard Airport Experiences (Fast Track in Helsinki) on Nordea Premium; travel insurance on Gold and Debit.",
              s=["con", "saver"], lc="beyond", o="P", at="Mastercard", neo=[3, "Mastercard's travel programme."], src=[["Nordea Sweden: Nordea Premium", SE_PREM]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: mortgages and everyday banking for households and families, a digital bank for small businesses with Nordea Finance, lending and markets for large corporates, and EUR 509 billion of savings, pensions and private banking.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Homes & families", "blurb": "21% of Swedish mortgage growth.", "div": "group", "rev": "pb", "products": [
            P("mortgages", "Mortgages & everyday banking", "Personal Banking income of EUR 1.17 billion in Q3 2026; mortgage lending up 2% and deposits up 4%; Sweden took 21% of mortgage-market growth to August 2026; Norwegian mortgage share about 15% after the Danske deal.",
              s=["home", "con"], lc="borrow", neo=[0, ""], src=[["Q3 2026 report", Q3], ["Nordea: Danske Norway completed, Nov 2024", DANSKE]]),
            P("family", "Nordea Family", "A package for children with a debit card, a payment wristband and the Gimi money app at no cost; opening it takes under three minutes, down from 35.",
              s=["fam"], lc="open", st="new", neo=[0, "Visa debit."], src=[["Euromoney: best digital bank, Jul 2026", EUROMONEY]]),
        ]},
        {"id": "4.2", "ic": "briefcase-business", "name": "Business Banking", "blurb": "50,000 new SMEs by 2030.", "div": "finance", "rev": "bb", "products": [
            P("sme", "Business Banking", "Income of EUR 835 million in Q3 2026; lending up 6% and 58% more new small-business customers than a year earlier, towards more than 50,000 new small-business customers by 2030; Nordea Business Insights and e-invoicing.",
              s=["sme"], lc="everyday", st="new", neo=[1, "Visa debit, Mastercard credit."],
              mc="Spend controls and virtual cards for a fast-growing SME base.",
              src=[["Q3 2026 report", Q3], ["Euromoney: best digital bank, Jul 2026", EUROMONEY]]),
            P("nfinance", "Nordea Finance", "Asset-based lending, leasing and receivables finance inside Business Banking.",
              s=["sme"], lc="borrow", neo=[0, ""], src=[["Q3 2026 report", Q3]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Large Corporates & Institutions", "blurb": "Lending up 13%.", "div": "group", "rev": "lci", "products": [
            P("lci", "Large Corporates & Institutions", "Income of EUR 547 million in Q3 2026, lending and deposits each up 13%; Markets, investment banking and branches in London, New York and Shanghai.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Q3 2026 report", Q3], ["Nordea: organisation", ORG]]),
        ]},
        {"id": "4.4", "ic": "trending-up", "name": "Wealth & pensions", "blurb": "EUR 509bn under management.", "div": "nam", "rev": "awm", "products": [
            P("pb", "Private Banking", "Net flows of EUR 0.9 billion in Q3 2026 and a large intake of new private-banking customers.",
              s=["saver"], lc="grow", neo=[0, ""], src=[["Q3 2026 release", Q3REL]]),
            P("lp", "Nordea Life & Pension", "Assets under management of EUR 116 billion, up 20% in a year.",
              s=["saver"], lc="grow", neo=[0, ""], src=[["Q3 2026 report", Q3]]),
            P("nam", "Nordea Asset Management", "Part of record group AuM of EUR 509 billion; the BetaPlus index range passed EUR 100 billion.",
              s=["saver"], lc="grow", neo=[0, ""], src=[["Q3 2026 release", Q3REL]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Nordea: Nordea Mobile with 5 million digitally active users, Nordea Business for companies, branches and advisers, and property portals that carry its loan promise.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Nordea Mobile", "blurb": "5 million digital users.", "div": "group", "rev": "pb", "products": [
            P("mobile", "Nordea Mobile & Netbank", "5 million digitally active users and 135 million log-ins a month at the end of 2025; 99% of retail interactions and 70% of personal-banking sales are digital; Euromoney's best digital bank in the Nordics, 2026.",
              s=["con", "fam", "saver"], lc="everyday", neo=[0, ""], src=[["Euromoney: best digital bank, Jul 2026", EUROMONEY], ["Q3 2026 report", Q3]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Nordea Business", "blurb": "Best corporate digital bank.", "div": "group", "rev": "bb", "products": [
            P("nbiz", "Nordea Business & Business Mobile", "Online bank and app for companies, named best corporate digital bank and best mobile banking app in all four countries for a fourth year (Global Finance, 2026); 44% of SME sales are digital.",
              s=["sme"], lc="everyday", neo=[0, ""], src=[["Q3 2026 report", Q3], ["Euromoney: best digital bank, Jul 2026", EUROMONEY]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & advisers", "blurb": "1,000 meetings a day in Sweden.", "div": "group", "rev": "pb", "products": [
            P("branches", "Branches & advisory", "Advice in person and online in four countries, with about 1,000 customer meetings a day in Sweden.",
              s=["con", "home", "saver"], lc="grow", neo=[0, ""], src=[["Nordea: our markets", MARKETS]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Partners & portals", "blurb": "Loan promise on property sites.", "div": "dk", "rev": "pb", "products": [
            P("portals", "Property portals & partners", "Nordea's Danish loan promise appears on the property portals Boliga, Boligsiden and Danbolig.",
              s=["home"], lc="borrow", o="P", at="Boliga, Boligsiden, Danbolig", neo=[0, ""], src=[["Euromoney: best digital bank, Jul 2026", EUROMONEY]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Nordea", "blurb": "Credit cards, and the first agent payment.", "products": [
        P("mcatnordea", "Mastercard at Nordea", "Visa carries Nordea's debit cards in every country, alongside Dankort in Denmark and BankAxept in Norway. Mastercard carries the credit and combination cards (Gold, Credit, Premium and Platinum), the Stockmann co-brand and Business Mastercard, and the premium travel benefits. In June 2026 the two ran Finland's first live Agent Pay transaction. No network deal or switch has been announced since 2015 ⚠.",
          s=["con"], div="group", rev="other", mc="The relationship this map is drawn for.",
          src=[["Nordea Sweden: Nordea Debit", SE_DEBIT], ["Nordea Sweden: Nordea Gold", SE_GOLD], ["Nordea: first Finnish agent payment, Jun 2026", AGENT]]),
    ]},
    {"id": "pillar-market", "name": "Nordic payments", "blurb": "Domestic schemes, A2A, instant.", "products": [
        P("market", "The Nordic market", "Domestic debit schemes (Dankort, BankAxept), account-to-account apps (Swish, Vipps MobilePay), EU instant-payment and payee-verification rules, Wero's spread in Europe, and Norwegian rules that delay rate changes and squeeze margins.",
          s=["con"], div="group", rev="other", src=[["Riksbank: Payments Report 2026", RIKSBANK], ["Wikipedia: Wero", WERO], ["Q3 2026 report", Q3]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
