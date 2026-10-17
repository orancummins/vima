"""Deutsche Bank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the Q2 2026 results (29 July 2026), the FY2025
results (29 January 2026) and the November 2025 investor deep dive. ``neo`` is the Mastercard lens:
[depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q2 = "https://investor-relations.db.com/files/documents/quarterly-results/2026/Q2-2026-Media-Release.pdf"
Q2DECK = "https://investor-relations.db.com/files/documents/quarterly-results/2026/Deutsche-Bank-Q2-2026-Presentation.pdf"
Q2CALL = "https://investor-relations.db.com/files/documents/quarterly-results/2026/Q2-2026-Analyst-Call-Transcript-For-Upload.pdf"
FY25 = "https://investor-relations.db.com/files/documents/quarterly-results/2025/Q4-2025-Media-Release.pdf"
IDD = "https://investor-relations.db.com/files/documents/other-presentations-and-events/2025/Media-Release-IDD-2025.pdf"
IDDCB = "https://investor-relations.db.com/files/documents/other-presentations-and-events/2025/IDD-2025-Presentation-Corporate-Bank-Fabrizio-Campelli.pdf"
IDDPB = "https://investor-relations.db.com/files/documents/other-presentations-and-events/2025/IDD-2025-Presentation-Private-Bank-Claudio-de-Sanctis.pdf"
AKRAM = "https://investor-relations.db.com/files/documents/other-presentations-and-events/2026/Raja-Akram-at-BofA-31st-Annual-Financials-CEO-Conference-Transcript-For-Upload.pdf"
IR = "https://investor-relations.db.com/"
RATINGS = "https://investor-relations.db.com/creditors/ratings"
MCAP = "https://companiesmarketcap.com/deutsche-bank/marketcap/"
WHO = "https://www.db.com/who-we-are"
BOARD = "https://www.db.com/who-we-are/boards-and-committees/management-board"
SUPBOARD = "https://investor-relations.db.com/corporate-governance/organizational-structure/supervisory-board?language_id=1"
ACCOUNTS = "https://www.deutsche-bank.de/pk/konto-und-karte/konten-im-ueberblick/konten-im-vergleich.html"
CARDS = "https://www.deutsche-bank.de/pk/konto-und-karte/karten-im-ueberblick/karten-im-vergleich.html"
MOBILE = "https://www.deutsche-bank.de/pk/konto-und-karte/services/mobiles-zahlen.html"
DBWERO = "https://www.deutsche-bank.de/pk/konto-und-karte/services/wero.html"
PBCREDIT = "https://www.postbank.de/privatkunden/produkte/konten-karten/kreditkarten.html"
PBAPPLE = "https://www.postbank.de/privatkunden/services/online-banking/apple-pay.html"
PBWERO = "https://www.postbank.de/privatkunden/services/online-banking/wero.html"
MMCARD = "https://www.miles-and-more-kreditkarte.com/"
MM2025 = "https://www.db.com/news/detail/20250917-neue-partnerschaft-bringt-bessere-leistungen-lufthansa-miles-and-more-credit-card-wechselt-zur-deutschen-bank"
MM2023 = "https://www.db.com/news/detail/20230710-lufthansa-group-and-miles-und-more-enter-into-new-partnership-with-deutsche-bank-and-mastercard"
MERCHANT = "https://corporates.db.com/solutions/corporate-bank-solutions/cash-management/merchant-solutions/"
FISERV = "https://www.db.com/news/detail/20210621-deutsche-bank-and-fiserv-announce-joint-venture-for-payment-acceptance-in-germany"
VERTLAUNCH = "https://db.com/news/detail/20221012-deutsche-bank-and-fiserv-launch-vert-germany-s-newest-payments-company"
VERT = "https://www.vert.de/"
CYBERSOURCE = "https://www.db.com/news/detail/20220922-deutsche-bank-partners-with-visa-to-prevent-fraud-in-online-retail"
APAC = "https://www.db.com/news/detail/20241203-deutsche-bank-launches-merchant-solutions-in-asia-pacific-empowering-ecommerce-growth"
RTP = "https://www.mastercard.com/us/en/news-and-trends/press/2025/june/deutsche-bank-and-mastercard-partner-to-power-merchant-solutions-with-open-banking-payments.html"
MC2021 = "https://www.db.com/news/detail/20210224-deutsche-bank-and-mastercard-intensify-their-collaboration-in-the-payments-space"
CASH = "https://corporates.db.com/solutions/corporate-bank-solutions/cash-management"
VOP = "https://corporates.db.com/in-focus/Focus-topics/instant-payments-vop/index"
DIGITALASSETS = "https://digitalassets.db.com/?kid=digitalassets.tn"
CUSTODY = "https://unchainedcrypto.com/deutsche-bank-confirms-bitcoin-and-ether-custody-launch-still-subject-to-regulators/"
FLOWTSS = "https://flow.db.com/Topics/trust-and-securities-services/custody-the-bridge-between-digital-assets-and-mainstream-finance"
FLOWCASH = "https://flow.db.com/Topics/cash-management/europe-has-a-window-of-opportunity-but-it-will-not-be-open-forever"
ALLUNITY = "https://allunity.com/"
GEMINI = "https://forkast.news/google-bets-deutsche-bank-can-make-ai-agents-work-inside-a-global-banks-compliance-framework/"
SURVEIL = "https://news.bgov.com/artificial-intelligence/deutsche-bank-goldman-look-to-ai-to-flag-trader-misconduct"
EPI = "https://www.epicompany.eu/"
GIROCARD = "https://tuenews.de/en/changes-to-ec-cards/"
BIZCARDS = "https://www.deutsche-bank.de/ub/unsere-loesungen/konto-zahlungsverkehr/kreditkarten.html"
ACCEPT = "https://www.deutsche-bank.de/ub/unsere-loesungen/konto-zahlungsverkehr/karten-akzeptanzloesungen.html"
BETTER = "https://www.db.com/news/detail/20210920-deutsche-bank-acquires-berlin-based-payment-service-provider-better-payment"
DATAMESH = "https://www.db.com/news/detail/20230222-deutsche-bank-invests-in-australian-paytech-datamesh"
PBCO = "https://www.postbank.de/unternehmen.html"
PBPK = "https://www.postbank.de/privatkunden.html"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · brands · plan", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: €491 billion of loans and €698 billion of deposits, a record second quarter in 2026, a bank founded in 1870 with Postbank as a branch of it, Google Cloud and AI, and the Global Hausbank plan to 2028.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "Record Q2, RoTE 11%.", "div": "dbg", "rev": "group", "products": [
            P("balance", "Balance sheet & earnings", "Net revenues of €8.5 billion and a record second-quarter net profit of €1.9 billion in Q2 2026 (RoTE 11.0%, CET1 13.9%); loans of €491 billion, deposits of €698 billion and €1,922 billion under management. 2025: revenues €32.1 billion, net profit €7.1 billion. Rated A1/A/A+; market value about US$61 billion (16 October 2026).",
              s=["corp"], neo=[0, ""], src=[["Q2 2026 results", Q2], ["Q2 2026 presentation", Q2DECK], ["FY2025 results", FY25], ["Deutsche Bank: ratings", RATINGS], ["companiesmarketcap: Deutsche Bank", MCAP]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Sewing and Wynaendts.", "div": "dbg", "rev": "group", "products": [
            P("leadership", "Management board", "CEO Christian Sewing (since April 2018), President Fabrizio Campelli (Corporate Bank and Investment Bank), CFO Raja Akram (since 15 March 2026), Chief Technology, Data & Innovation Officer Marie-Jeanne Deverdun, Private Bank head Claudio de Sanctis; supervisory board chaired by Alexander Wynaendts. In payments: Gerald Podobnik (Co-Head Corporate Bank), Ole Matthiessen (Cash Management), Kilian Thalhammer (Merchant Solutions).",
              s=["corp"], neo=[0, ""], src=[["Deutsche Bank: management board", BOARD], ["Deutsche Bank: supervisory board", SUPBOARD]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & brands", "blurb": "Since 1870; Postbank a branch.", "div": "dbg", "rev": "group", "products": [
            P("brands", "Heritage & brands", "Founded in 1870 'to support German companies abroad'; 89,879 staff (FTE) at the end of 2025 and revenue 39% from Germany. Brands: Deutsche Bank, Postbank (now 'a branch of Deutsche Bank AG'), BHW, DWS and Fyrst ⚠ (2026 status unverified).",
              s=["con"], o="I", neo=[0, ""], src=[["Deutsche Bank: who we are", WHO], ["Postbank: company", PBCO], ["FY2025 results", FY25]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "Google's design partner.", "div": "dbg", "rev": "group", "products": [
            P("tech", "Technology & AI", "Design partner for Google's Gemini Enterprise for Financial Services and its Financial Research Agent (August 2026), an LLM for trade surveillance built with Google Cloud ⚠, and the Private Bank's core platforms cut from 15 to two. The CFO names transaction monitoring and credit underwriting as the main back-office AI uses.",
              s=["corp"], st="new", o="P", at="Google Cloud", neo=[0, ""], src=[["Forkast: Google and Deutsche Bank, Aug 2026", GEMINI], ["Bloomberg Government: AI surveillance", SURVEIL], ["Raja Akram, Sep 2026", AKRAM], ["IDD 2025: Private Bank", IDDPB]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Global Hausbank 2028", "blurb": "RoTE above 13%.", "div": "dbg", "rev": "group", "products": [
            P("strategy", "Scaling the Global Hausbank", "2026–28 targets (17 November 2025): RoTE above 13%, cost/income below 60%, revenue about €37 billion, about €5 billion of extra revenue from asset gathering, payments and servicing, and advisory, and a 60% payout from 2026. All 2025 targets were met.",
              s=["corp"], st="new", neo=[0, ""], src=[["IDD 2025 media release", IDD], ["FY2025 results", FY25]]),
            P("deals", "Deals", "The Vert joint venture with Fiserv (announced June 2021, launched October 2022), Better Payment bought (September 2021), a stake in DataMesh (February 2023), and the Private Bank India franchise sold (agreed Q2 2026).",
              s=["merch", "corp"], o="A", neo=[0, ""], src=[["Deutsche Bank and Fiserv, Jun 2021", FISERV], ["Better Payment, Sep 2021", BETTER], ["DataMesh, Feb 2023", DATAMESH], ["Q2 2026 results", Q2]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "How money moves: girocards co-badged with Debit Mastercard, Mastercard credit and the Miles & More card, Amex for corporates, Merchant Solutions and Vert for acceptance, the leading euro clearer, Wero, and digital-asset custody and stablecoins.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "girocard with Debit Mastercard.", "div": "db", "rev": "pb", "products": [
            P("dbcard", "Deutsche Bank Card", "A girocard 'with Mastercard function' (Debit Mastercard co-badge), included in the AktivKonto (€6.90 a month) and BestKonto (€13.90); a free virtual Mastercard debit card for Apple Pay; DB Card Plus at €18 a year, network not stated ⚠. The date Maestro gave way to Debit Mastercard is not public.", short="DB Card (girocard + Mastercard)",
              s=["con"], lc="everyday", o="P", at="girocard, Mastercard", neo=[1, "girocard at home, Debit Mastercard abroad and online."],
              mc="Mastercard is the co-badge on every card; girocard keeps domestic spend.",
              src=[["Deutsche Bank: accounts", ACCOUNTS], ["Deutsche Bank: cards", CARDS], ["tünews: changes to EC cards, Jun 2023", GIROCARD]]),
            P("pbcard", "Postbank Card, Card plus & virtual", "Postbank Card with girocard and Debit Mastercard; Card plus, a Debit Mastercard from age 12 at €18 a year; and a free virtual card ordered in the app for wallets.", short="Postbank Card (girocard + Mastercard)",
              s=["con"], lc="everyday", o="P", at="girocard, Mastercard", neo=[1, "girocard and Debit Mastercard."], src=[["Postbank: Apple Pay", PBAPPLE], ["Postbank: credit cards", PBCREDIT]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Mastercard throughout.", "div": "db", "rev": "pb", "products": [
            P("dbcredit", "Deutsche Bank Mastercard", "Standard (€39 a year), Gold (€82, free in BestKonto, 6% travel cashback), Travel (€94, no foreign-transaction fee) and Platin.", short="DB Mastercard credit",
              s=["con", "aff"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Deutsche Bank: cards", CARDS], ["Deutsche Bank: accounts", ACCOUNTS]]),
            P("pbcredit", "Postbank Mastercard, Gold & Platinum", "Classic at €29 a year (February 2025 ⚠), Gold and Platinum with Priority Pass. Postbank says a Visa card cannot be used for Apple Pay, so some legacy Visa cards appear to remain ⚠.", short="Postbank Mastercard (some legacy Visa ⚠)",
              s=["con"], lc="borrow", o="P", at="Mastercard", neo=[1, "Mastercard; some legacy Visa ⚠."], src=[["Postbank: credit cards", PBCREDIT], ["Postbank: Apple Pay", PBAPPLE]]),
        ]},
        {"id": "2.3", "ic": "plane", "name": "Miles & More", "blurb": "Issued by DB since Oct 2025.", "div": "mm", "rev": "pb", "products": [
            P("milesmore", "Miles & More credit cards", "Blue (€5.50 a month), Gold (€11.50), MyFlex (no fee, instalments) and status cards, plus Business Blue and Gold; won with Mastercard in a July 2023 tender and issued by Deutsche Bank from 1 October 2025, with cards moved from DKB by spring 2026. Miles & More has more than 36 million members.", short="Miles & More (Mastercard)",
              s=["trav", "sme"], lc="borrow", st="new", ay="Oct 2025", o="P", at="Lufthansa, Mastercard", neo=[2, "Mastercard, won jointly in 2023."],
              mc="One of Europe's largest loyalty programmes, won together.",
              src=[["Miles & More with Deutsche Bank and Mastercard, Jul 2023", MM2023], ["Miles & More moves to Deutsche Bank, Sep 2025", MM2025], ["Miles & More credit card", MMCARD]]),
        ]},
        {"id": "2.4", "ic": "briefcase", "name": "Business & corporate cards", "blurb": "Mastercard, and Amex for T&E.", "div": "db", "rev": "cb", "products": [
            P("bizcard", "BusinessCard Direct & BusinessCard", "BusinessCard Direct, a business Mastercard debit card (free in year one, then €24), and BusinessCard credit cards at about €29 and €79 ⚠, with Mastercard Business Bonus.", short="BusinessCard (Mastercard)",
              s=["sme"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Deutsche Bank: business cards", BIZCARDS]]),
            P("amex", "American Express corporate cards", "Amex Business Platinum, Business Gold and Corporate Card sold by Deutsche Bank, with a virtual TAN-based payment solution.", short="Amex corporate cards",
              s=["corp", "sme"], lc="everyday", o="P", at="American Express", neo=[0, "American Express."],
              mc="Amex holds the corporate travel-and-expense shelf.",
              src=[["Deutsche Bank: business cards", BIZCARDS]]),
            P("b2b2c", "Card issuing with the Private Bank", "The Corporate Bank plans 'B2B2C solutions on card issuance with PB' and 'B2C Commerce Solutions' by 2028; details not public.",
              s=["corp"], lc="move", st="unconf", neo=[None, "Not announced."],
              mc="Commercial and virtual cards are the clearest opening.",
              src=[["IDD 2025: Corporate Bank", IDDCB]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Merchant Solutions", "blurb": "Acquiring in four continents.", "div": "ms", "rev": "cb", "products": [
            P("ms", "Merchant Solutions acquiring", "Omnichannel acquiring for '10+ international credit cards and local EU debit cards', more than 30 alternative methods and Deutsche Bank's own gateway; live in Australia, India, Indonesia and South Korea since 3 December 2024 through DataMesh. Volumes not public.",
              s=["merch"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["Deutsche Bank: Merchant Solutions", MERCHANT], ["Merchant Solutions in APAC, Dec 2024", APAC]]),
            P("rtp", "Request to Pay with Mastercard open banking", "Account-to-account payments inside Merchant Solutions on Mastercard's open-banking rails, announced at Money20/20 Amsterdam in June 2025 ⚠ (detail from a search summary).", short="Request to Pay (Mastercard open banking)",
              s=["merch"], lc="move", st="new", ay="Jun 2025", o="P", at="Mastercard", neo=[3, "Mastercard Open Banking ⚠."], src=[["Mastercard: Deutsche Bank open banking, Jun 2025", RTP]]),
            P("msextras", "Marketplaces, currency conversion & BNPL", "Marketplace payments, dynamic currency conversion and multi-currency pricing, and buy-now-pay-later financing from an unnamed provider.",
              s=["merch"], lc="grow", neo=[None, "Providers not named."], src=[["Deutsche Bank: Merchant Solutions", MERCHANT]]),
        ]},
        {"id": "2.6", "ic": "receipt-text", "name": "Vert", "blurb": "Clover terminals with Fiserv.", "div": "vert", "rev": "cb", "products": [
            P("vert", "Vert", "The Deutsche Bank–Fiserv joint venture (launched 12 October 2022) selling Clover terminals from €9.90 a month to about 800,000 small businesses at Deutsche Bank, Postbank and Fyrst; First Data acquires; accepts girocard, Mastercard, Visa, Maestro, V PAY and Apple Pay.",
              s=["sme", "merch"], lc="move", o="P", at="Fiserv", neo=[1, "Accepts every network."], src=[["Vert launch, Oct 2022", VERTLAUNCH], ["Vert", VERT], ["Deutsche Bank: card acceptance", ACCEPT]]),
        ]},
        {"id": "2.7", "ic": "arrow-left-right", "name": "Cash management & clearing", "blurb": "The #1 euro clearer.", "div": "db", "rev": "cb", "products": [
            P("cash", "Cash management & clearing", "Offered in 34 countries; describes itself as the first euro clearer and first US-dollar clearer among eurozone banks, with more than €250 trillion of cross-border payments a year and 140+ correspondent countries; FX4Cash and payment tracking. Aim to double US-dollar clearing share by 2028.",
              s=["corp"], lc="move", neo=[0, ""],
              mc="The cross-border push is where Mastercard Move could fit.",
              src=[["Deutsche Bank: cash management", CASH], ["IDD 2025: Corporate Bank", IDDCB]]),
            P("instant", "SEPA Instant & Verification of Payee", "Free verification of payee, mandatory from 9 October 2025, by API, host-to-host and EBICS.",
              s=["corp", "sme"], lc="move", neo=[0, "SEPA instant."], src=[["Deutsche Bank: instant payments and VoP", VOP]]),
            P("dbx", "dbX platforms & APIs", "Modular treasury platforms for corporates, non-banks, fintechs and institutions, ISO 20022 messaging and a target of 100% API access by 2028.",
              s=["corp"], lc="open", neo=[0, ""], src=[["Deutsche Bank: cash management", CASH], ["IDD 2025: Corporate Bank", IDDCB]]),
        ]},
        {"id": "2.8", "ic": "send", "name": "Wero & wallets", "blurb": "EPI shareholder.", "div": "dbg", "rev": "pb", "products": [
            P("wero", "Wero", "Phone-number payments between people in about 10 seconds for Deutsche Bank and Postbank customers, with growing online acceptance; Deutsche Bank is an EPI shareholder and giropay closed on 31 December 2024.",
              s=["con"], lc="move", st="new", o="P", at="EPI", neo=[0, "Wero, the European scheme."],
              mc="Wero competes with cards online and, later, in shops.",
              src=[["Deutsche Bank: Wero", DBWERO], ["Postbank: Wero", PBWERO], ["EPI", EPI]]),
            P("wallets", "Apple Pay, Google Pay & Samsung Wallet", "Phone wallets for Deutsche Bank cards; Postbank supports Mastercard cards only; Click to Pay on Deutsche Bank and Postbank Mastercards.", short="Wallets (Mastercard tokens)",
              s=["con"], lc="everyday", o="P", at="Apple, Google, Samsung", neo=[2, "Mastercard cards tokenised."], src=[["Deutsche Bank: mobile payments", MOBILE], ["Postbank: Apple Pay", PBAPPLE]]),
        ]},
        {"id": "2.9", "ic": "coins", "name": "Digital assets", "blurb": "Custody, EURAU, Agorá.", "div": "dbg", "rev": "cb", "products": [
            P("custody", "Digital asset custody", "Custody of bitcoin, ether, USDC, EURC and EURAU for Corporate Bank clients via Autobahn, with Taurus (since September 2023); first clients targeted for 2026 but subject to regulators ⚠ not confirmed live.",
              s=["corp"], lc="grow", st="unconf", o="P", at="Taurus", neo=[0, ""], src=[["Deutsche Bank: digital assets", DIGITALASSETS], ["Unchained: custody, Sep 2026", CUSTODY]]),
            P("allunity", "AllUnity stablecoins", "A euro e-money token from DWS, Galaxy and Flow Traders (July 2025, BaFin licence); EURAU, CHFAU and SEKAU on the Arc mainnet from 22 September 2026 and USDAU from 30 September.",
              s=["corp"], lc="move", st="new", o="P", at="Galaxy, Flow Traders", neo=[0, ""],
              mc="Stablecoin settlement links are open ground for the Multi-Token Network.",
              src=[["AllUnity", ALLUNITY]]),
            P("agora", "Project Agorá & tokenised money", "A live real-value test in Project Agorá (July 2026), a May 2026 white paper on digital money, and tokenised money-market funds as a 2028 lever; no live tokenised-deposit product found ⚠.",
              s=["corp"], lc="move", st="new", neo=[0, ""], src=[["Deutsche Bank flow: Europe's window, Sep 2026", FLOWCASH], ["Deutsche Bank flow: custody, Sep 2026", FLOWTSS]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: BestSign and Click to Pay, Visa's Cybersource screening for merchants, an AI client tool at Postbank and Google's research agent for corporates, and loyalty through Miles & More.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Security & fraud", "blurb": "BestSign, Click to Pay, Cybersource.", "div": "dbg", "rev": "pb", "products": [
            P("bestsign", "BestSign, 3-D Secure & alerts", "App-based authentication for Deutsche Bank and Postbank (also needed for Wero), 3-D Secure, SMS fraud alerts and a card-security package.",
              s=["con"], lc="everyday", o="B", neo=[0, "Deutsche Bank's own."], src=[["Deutsche Bank: Wero", DBWERO], ["Deutsche Bank: cards", CARDS]]),
            P("c2p", "Click to Pay", "Deutsche Bank Mastercards can be registered for Click to Pay; Postbank uses virtual card numbers through it.", short="Click to Pay (Mastercard)",
              s=["con"], lc="everyday", o="P", at="Mastercard", neo=[3, "Mastercard's own."], src=[["Deutsche Bank: cards", CARDS], ["Postbank: credit cards", PBCREDIT]]),
            P("cybersource", "Cybersource Decision Manager", "AI fraud screening from Visa for Deutsche Bank's e-commerce merchants (September 2022).", short="Cybersource (Visa)",
              s=["merch"], lc="move", ay="Sep 2022", o="P", at="Visa", neo=[0, "Visa."],
              mc="Visa holds merchant fraud tooling; Mastercard's risk services are the alternative.",
              src=[["Deutsche Bank and Visa, Sep 2022", CYBERSOURCE]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI for clients", "blurb": "Postbank AI, research agent.", "div": "dbg", "rev": "pb", "products": [
            P("aiclient", "AI client tools", "An AI client-interaction tool live at Postbank and moving to the Deutsche Bank brand; a goal of more than 80% of inbound queries assisted by conversational AI and voice agents that 'execute daily banking transactions' by 2028.",
              s=["con"], lc="everyday", st="new", neo=[0, ""],
              mc="Agents that execute payments are where Agent Pay could fit.",
              src=[["Raja Akram, Sep 2026", AKRAM], ["IDD 2025: Private Bank", IDDPB]]),
            P("aicb", "AI for corporates", "Google's Financial Research Agent for German mid-sized corporates (August 2026), AI-led onboarding more than 95% faster for SMEs and mid-caps, and AI portfolio monitoring.",
              s=["corp", "sme"], lc="open", st="new", o="P", at="Google Cloud", neo=[0, ""], src=[["Forkast: Google and Deutsche Bank, Aug 2026", GEMINI], ["IDD 2025: Corporate Bank", IDDCB]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Loyalty", "blurb": "MilesPay, Business Bonus.", "div": "mm", "rev": "pb", "products": [
            P("milespay", "MilesPay & Mastercard Business Bonus", "Pay with miles at the till on the Miles & More Mastercard, and Mastercard Business Bonus on business cards.", short="MilesPay & Business Bonus (Mastercard)",
              s=["trav", "sme"], lc="grow", o="P", at="Mastercard, Lufthansa", neo=[2, "On Mastercard."], src=[["Miles & More credit card", MMCARD], ["Deutsche Bank: business cards", BIZCARDS]]),
            P("urlaubsplus", "Postbank Urlaubsplus", "A 5% travel bonus for Postbank cardholders.",
              s=["con"], lc="grow", neo=[0, "Postbank's own."], src=[["Postbank: credit cards", PBCREDIT]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: the Private Bank for about 19 million clients in Germany and wealth clients worldwide, the Corporate Bank for 800,000 SMEs and 13,000 large corporates, the Investment Bank, and DWS with €1.19 trillion.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Private Bank", "blurb": "19m clients in Germany.", "div": "db", "rev": "pb", "products": [
            P("pbanking", "Personal Banking", "About 19 million clients in Germany across Deutsche Bank and Postbank, with accounts, cards, BHW building-society loans and mortgages; revenue of €5.3 billion in 2025. Ambition: more than 70% of new business through digital or remote channels.",
              s=["con"], lc="everyday", neo=[1, "girocard with Debit Mastercard."], src=[["IDD 2025: Private Bank", IDDPB], ["FY2025 results", FY25], ["Postbank: private customers", PBPK]]),
            P("wealth", "Wealth Management", "Revenue of €4.4 billion in 2025; Private Bank client assets of €846 billion at Q2 2026 and a €1 trillion goal by 2028; Q2 2026 RoTE 11.3%.",
              s=["aff"], lc="grow", neo=[0, ""], src=[["Q2 2026 results", Q2], ["IDD 2025: Private Bank", IDDPB]]),
        ]},
        {"id": "4.2", "ic": "building-2", "name": "Corporate Bank", "blurb": "€7.4bn revenue, RoTE 16%.", "div": "db", "rev": "cb", "products": [
            P("cb", "Corporate Treasury & Business Banking", "Revenue of €7.4 billion in 2025 (Corporate Treasury Services €4.2 billion, Business Banking €1.3 billion) and Q2 2026 RoTE of 16.4%; about 800,000 SMEs, 19,000 mid-caps and 13,000 large corporates; 200,000 more Business Banking clients targeted by 2028.",
              s=["sme", "corp"], lc="everyday", neo=[1, "Business cards on Mastercard."], src=[["FY2025 results", FY25], ["Q2 2026 results", Q2], ["IDD 2025: Corporate Bank", IDDCB]]),
            P("trade", "Trade & supply-chain finance", "Drove 7% Corporate Bank loan growth in Q2 2026.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Q2 2026 results", Q2]]),
            P("tss", "Trust & Securities Services", "About €4.0 trillion under custody in 30 markets.",
              s=["corp"], lc="grow", neo=[0, ""], src=[["IDD 2025: Corporate Bank", IDDCB]]),
        ]},
        {"id": "4.3", "ic": "chart-candlestick", "name": "Investment Bank", "blurb": "€11.5bn revenue.", "div": "db", "rev": "ib", "products": [
            P("ib", "Investment Bank", "Revenue of €11.5 billion in 2025; Q2 2026 revenue of €3.2 billion with record fixed income and currencies (€2.6 billion) and origination and advisory up 36%.",
              s=["corp"], lc="grow", neo=[0, ""], src=[["FY2025 results", FY25], ["Q2 2026 results", Q2]]),
        ]},
        {"id": "4.4", "ic": "trending-up", "name": "Asset Management", "blurb": "DWS, €1.19tn.", "div": "dws", "rev": "am", "products": [
            P("dws", "DWS", "€1,190 billion under management and record net inflows of €25 billion in Q2 2026; co-owner of AllUnity.",
              s=["aff", "corp"], lc="grow", neo=[0, ""], src=[["Q2 2026 results", Q2], ["AllUnity", ALLUNITY]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: the Deutsche Bank and Postbank apps, Autobahn and the corporate portal, fewer branches after 100 closures, and partners from Fiserv to Lufthansa.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Apps", "blurb": "Deutsche Bank and Postbank.", "div": "dbg", "rev": "pb", "products": [
            P("apps", "Deutsche Bank & Postbank apps", "Banking apps for both brands; Postbank's virtual Debit Mastercard is ordered in the app.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Postbank: Apple Pay", PBAPPLE]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Corporate portals", "blurb": "Autobahn, CashManager.", "div": "db", "rev": "cb", "products": [
            P("autobahn", "Autobahn & Corporate Bank Portal", "Autobahn and the Corporate Bank Portal (the route to digital-asset custody), CashManager, db direct internet and EBICS.",
              s=["corp"], lc="open", neo=[0, ""], src=[["Deutsche Bank: digital assets", DIGITALASSETS], ["Deutsche Bank: instant payments and VoP", VOP]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & cash", "blurb": "100 closures done.", "div": "postbank", "rev": "pb", "products": [
            P("branches", "Branches & Bargeld-Code", "100 Private Bank branch closures completed in H1 2026, and Bargeld-Code cardless cash withdrawal for Deutsche Bank and Postbank.",
              s=["con"], lc="everyday", st="flux", neo=[0, ""], src=[["Q2 2026 analyst call", Q2CALL], ["Postbank: private customers", PBPK]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Partners", "blurb": "Fiserv, Lufthansa, Google.", "div": "dbg", "rev": "cb", "products": [
            P("partners", "Partner channels", "Vert with Fiserv, Lufthansa Miles & More, DataMesh in Asia-Pacific, Google Cloud, Taurus for custody and American Express.",
              s=["merch", "trav"], lc="open", o="P", at="Fiserv, Lufthansa, Google", neo=[1, "Miles & More on Mastercard."], src=[["Vert launch, Oct 2022", VERTLAUNCH], ["Miles & More moves to Deutsche Bank, Sep 2025", MM2025]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Deutsche Bank", "blurb": "On every card, behind girocard.", "products": [
        P("mcatdb", "Mastercard at Deutsche Bank", "Every Deutsche Bank and Postbank issuing programme found runs on Mastercard: Debit Mastercard co-badged on the girocards, all consumer and business credit, and the Miles & More card won jointly in 2023 and issued from October 2025. A 2021 partnership covered business payments, and Mastercard open banking powers Request to Pay (June 2025 ⚠). Amex holds corporate cards, Visa screens merchant fraud and girocard keeps domestic debit.",
          s=["con"], div="dbg", rev="group", mc="The relationship this map is drawn for.",
          src=[["Deutsche Bank and Mastercard, Feb 2021", MC2021], ["Miles & More with Deutsche Bank and Mastercard, Jul 2023", MM2023]]),
    ]},
    {"id": "pillar-market", "name": "German banking", "blurb": "girocard, Wero, instant.", "products": [
        P("market", "The German market", "Maestro and V PAY leaving new girocards between July 2023 and the end of 2027, with some banks choosing Visa Debit; Wero replacing giropay; instant payments with verification of payee from October 2025; MiCA for stablecoins; and the ECB's Pontes settlement live (September 2026).",
          s=["con"], div="dbg", rev="group", src=[["tünews: changes to EC cards, Jun 2023", GIROCARD], ["Deutsche Bank flow: Europe's window, Sep 2026", FLOWCASH]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
