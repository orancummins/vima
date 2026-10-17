"""Worldline's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the H1 2026 results (30 July 2026), the FY2025
results (25 February 2026) and the 2025 Universal Registration Document (filed 6 March 2026). Where a Worldline
release has no full link in the research, the source points at Worldline's press-release index. ``neo`` is the
Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard,
1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1PR = "https://investors.worldline.com/content/dam/investors-worldline-com/assets/documents/press-releases/2026/20260730-worldline-h1-2026-results-press-release.pdf"
H1P = "https://investors.worldline.com/content/dam/investors-worldline-com/assets/documents/presentations/2026/20260730-worldline-h1-2026-results-presentation.pdf"
FY25 = "https://investors.worldline.com/content/dam/investors-worldline-com/assets/documents/press-releases/20260225-worldline-fy-2025-results-press-release-en.pdf"
URD = "https://investors.worldline.com/content/dam/worldline-shared/documents/legal/universal-registration-document/worldline-urd-2025-en.pdf"
IRH = "https://investors.worldline.com/en/home.html"
IRPR = "https://investors.worldline.com/en/home/news-events/financial-press-releases/"
WLPR = "https://worldline.com/en/home/top-navigation/media-relations/press-release/"
RSS = "https://www.globenewswire.com/news-release/2026/04/29/3283439/0/en/worldline-reverse-stock-split-press-release.html"
INGMC = "https://www.mastercard.com/news/europe/en/newsroom/press-releases/en/2026/worldline-ing-and-mastercard-complete-a-live-end-to-end-european-agentic-payment-in-production/"
CAMC = "https://www.optionfinance.fr/info-financiere-en-continu/d/2026-06-25-worldline-inaugure-le-paiement-agentique-en-france-avec-credit-agricole-et-mastercard.html"
MCAS = "https://www.mastercard.com/us/en/news-and-trends/press/2026/september/mastercard-gives-merchants-a-simpler-way-to-build--connect-and-s.html"
MC25 = "https://www.mastercard.com/news/press/2025/june/one-year-in-mastercard-s-checkout-transformation-gains-ground-across-europe-1/"
MC20 = "https://www.mastercard.com/news/ap/en/newsroom/press-releases/en/2020/june/mastercard-axis-bank-and-worldline-launch-soft-pos-to-enable-smartphones-to-be-used-as-pos-devices/"
MC13 = "https://www.fintechfutures.com/m-a/mastercard-inks-broad-masterpass-distribution-deal-with-worldline-oct-21-2013-"
EIC1 = "https://www.capitalbrief.com/briefing/worldline-shares-drop-over-20-on-media-allegations-of-fraud-cover-up-6098b195-286f-4f07-8b04-392141b4b66d/"
EIC3 = "https://www.crowdfundinsider.com/2025/06/243664-belgian-prosecutors-investigate-worldlines-local-unit-amid-money-laundering-allegations/"
AGENTIC = "https://worldline.com/en/home/top-navigation/about-worldline/innovation/agentic-commerce"
ISSUING = "https://worldline.com/en/home/main-navigation/solutions/financial-institutions/card-issuing"
WEROACQ = "https://worldline.com/en/home/main-navigation/solutions/financial-institutions/open-banking-solutions/wero-acquiring-processing"
FRAUD = "https://worldline.com/en/home/main-navigation/solutions/financial-institutions/authentication-and-security/payment-fraud-management"
EXCO = "https://worldline.com/en/home/top-navigation/about-worldline/strategic-executive-board"
BOARD = "https://worldline.com/en/home/top-navigation/about-worldline/board-of-directors"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "results · capital · licences", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: €4.0 billion of revenue and a €5.2 billion loss in 2025, a €500 million capital raise with French banks as new anchors, payment licences across Europe, a business pruned back to its European core, and the remediation after the 2025 press investigation.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & results", "blurb": "€4.0bn revenue, 14% of Europe.", "div": "grp", "rev": "grp", "products": [
            P("scale", "Revenue & earnings", "FY2025 revenue of €4,030 million (−2.7% organic), adjusted EBITDA of €737 million and a net loss of €5,157 million after about €4.7 billion of goodwill impairment; H1 2026 revenue of €1,897 million (−1.3%) and adjusted EBITDA of €328 million. On the fully pruned scope: H1 2026 revenue €1,736 million, acquiring volume €245 billion (+4.3%) and 8.3 billion acceptance transactions.",
              s=["ent"], neo=[0, ""], src=[["H1 2026 results", H1PR], ["FY2025 results", FY25]]),
            P("footprint", "Footprint", "About 1.2 million merchants, 320+ banks, 156 million cards and a 14% share of European acquiring volume, present in 38 countries (pre-pruning figures, end-2025).",
              s=["smb", "bank"], neo=[0, ""], src=[["Universal Registration Document 2025", URD]]),
        ]},
        {"id": "1.2", "ic": "coins", "name": "Ownership & capital", "blurb": "French banks step in.", "div": "grp", "rev": "grp", "products": [
            P("capital", "Shareholders & the 2026 raise", "About €500 million raised in March 2026 (a reserved issue and a rights issue 121% subscribed), taken up by Bpifrance, Crédit Agricole, Crédit Mutuel and BNP Paribas; SIX did not take part. A 1-for-40 reverse split followed (June 2026). Market cap about €0.67 billion at €11.86 a share (16 October 2026) ⚠ own estimate; S&P BB, negative outlook since March 2025.",
              s=["ent"], st="flux", neo=[0, ""], src=[["Worldline: financial press releases", IRPR], ["Reverse stock split, Apr 2026", RSS], ["Worldline investors", IRH], ["Universal Registration Document 2025", URD]]),
        ]},
        {"id": "1.3", "ic": "users-round", "name": "Leadership", "blurb": "Vacheron since 2025.", "div": "grp", "rev": "grp", "products": [
            P("leadership", "Board & executive committee", "Chair Wilfried Verstraete; CEO Pierre-Antoine Vacheron (since March 2025, formerly head of payments at Groupe BPCE); CFO Srikanth Seshadri; Madalena Cascais Tomé, former CEO of SIBS, runs Financial Institutions and Processing; Stefaan D'Hoore, a former Visa regional risk officer, became Chief Risk & Compliance Officer in April 2026.",
              s=["ent"], neo=[0, ""], src=[["Worldline: executive board", EXCO], ["Worldline: board of directors", BOARD]]),
        ]},
        {"id": "1.4", "ic": "badge-check", "name": "Licences & heritage", "blurb": "From Sligos to Ingenico.", "div": "grp", "rev": "grp", "products": [
            P("licences", "Licences & heritage", "Payment institutions in Belgium, Luxembourg, Sweden, the Netherlands, Greece and Italy, PAYONE an e-money institution under BaFin, equensWorldline a processor under DNB, and an FCA licence in the UK. Built from Sligos (1972) and Atos, listed in 2014, and grown through Equens (2016), SIX Payment Services (2018) and Ingenico (2020).",
              s=["bank"], o="I", neo=[0, ""], src=[["Universal Registration Document 2025", URD]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "North Star 2030", "blurb": "Pruned to Europe.", "div": "grp", "rev": "grp", "products": [
            P("strategy", "North Star 2030", "Simplify, Converge, Integrate, Grow (Capital Markets Day, November 2025): about 4% organic growth a year from 2027, adjusted EBITDA above €900 million and free cash flow of €300–350 million by 2030. The 2026 revenue outlook was cut to flat to slightly positive in July.",
              s=["ent"], st="new", neo=[0, ""], src=[["H1 2026 results", H1PR], ["FY2025 results", FY25]]),
            P("pruning", "Divestments", "Mobility & e-Transactional Services to Magellan (€400 million), North America to Shift4, PaymentIQ, New Zealand, the ANZ joint venture, India to BillDesk and its CAWL stake to Crédit Agricole, all closed by 3 August 2026.",
              s=["ent"], o="B", st="retired", neo=[0, ""], src=[["H1 2026 results", H1PR], ["Worldline: financial press releases", IRPR]]),
            P("tech", "Platform convergence & AI", "Ogone merchants 80% moved to GoPay, 55% of issuing volume on the target issuing platform, four legacy platforms closed in 2025; 83% of developers use AI coding tools, with Claude, Google, Mistral and open models.",
              s=["ent", "bank"], st="flux", neo=[0, ""], src=[["H1 2026 presentation", H1P]]),
        ]},
        {"id": "1.6", "ic": "scale", "name": "Risk & remediation", "blurb": "After 'Dirty Payments'.", "div": "wl", "rev": "ms", "products": [
            P("remediation", "Press investigation & remediation", "The 'Dirty Payments' investigation (24 June 2025) said Worldline kept processing for high-risk merchants; shares fell more than 40% in a day and Brussels prosecutors opened a money-laundering probe. A €10 million guarantee was posted in Belgium (March 2026), a BaFin monitor sits at PAYONE, and €30–40 million of remediation is planned for 2026.",
              s=["smb", "ent"], st="flux", neo=[0, ""],
              mc="A buyer for merchant-monitoring and anti-money-laundering tools; Visa's fraud tools are already in.",
              src=[["Capital Brief: shares fall, Jun 2025", EIC1], ["Crowdfund Insider: Belgian probe, Jun 2025", EIC3], ["Universal Registration Document 2025", URD]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: acquiring €245 billion in half a year, domestic schemes from Bancontact to TWINT, processing for 156 million cards, Wero and instant payments, Global Collect for cross-border commerce, and stablecoins and the digital euro.",
    "tiles": [
        {"id": "2.1", "ic": "store", "name": "Acquiring", "blurb": "€245bn in H1 2026.", "div": "wl", "rev": "ms", "products": [
            P("acquiring", "Commercial acquiring", "Card acquiring under Worldline, PAYONE, Bambora, Axepta and Worldline Greece (fully owned since May 2026): €245 billion of volume in H1 2026, growing in Germany, Italy, Greece, the Nordics and Central Europe while Benelux turns round.",
              s=["smb", "ent"], lc="move", neo=[1, "Acquires every network, with domestic schemes."], src=[["H1 2026 presentation", H1P], ["H1 2026 results", H1PR]]),
            P("hub", "Acquiring Hub", "Connects Worldline's Axis, GoPay and Tap on Mobile to several acquirers, including third parties.",
              s=["ent"], lc="move", neo=[1, "Carries every network."], src=[["Universal Registration Document 2025", URD]]),
        ]},
        {"id": "2.2", "ic": "flag", "name": "Domestic schemes", "blurb": "Bancontact, CB, Girocard, TWINT.", "div": "wl", "rev": "ms", "products": [
            P("domestic", "Domestic schemes", "Bancontact (Worldline's Banksys heritage), Cartes Bancaires (its gateways carry more than half of French in-store commerce transactions), Girocard through PAYONE and the Sparkassen, TWINT, BLIK, Bizum and iDEAL.",
              s=["smb", "shop"], lc="move", o="I", neo=[0, "Domestic schemes."],
              mc="Where Worldline is strongest, a card payment often never touches Mastercard.",
              src=[["Universal Registration Document 2025", URD], ["H1 2026 presentation", H1P]]),
        ]},
        {"id": "2.3", "ic": "credit-card", "name": "Issuing processing", "blurb": "156 million cards.", "div": "equens", "rev": "fs", "products": [
            P("issuing", "Card issuing processing", "Issuer processing from Essential to Card as a Service and commercial cards for about 156 million cards: KBC, OP Financial Group (12-year renewal), ING Germany and the Netherlands, ABN AMRO (renewed March 2026) and Banca Sammarinese di Investimento (September 2026). Financial Services revenue fell 7.1% in H1 2026.",
              s=["bank"], lc="move", neo=[1, "Processes every network."],
              mc="Issuer value-added services could help a shrinking Financial Services arm.",
              src=[["Worldline: card issuing", ISSUING], ["H1 2026 results", H1PR], ["Worldline: press releases", WLPR]]),
            P("ics", "ABN AMRO / ICS credit-card outsourcing", "Credit-card processing outsourced by ABN AMRO's ICS, signed early July 2026.",
              s=["bank"], lc="borrow", st="new", ay="Jul 2026", neo=[None, "Card-brand mix not verified ⚠."], src=[["H1 2026 results", H1PR]]),
        ]},
        {"id": "2.4", "ic": "arrow-left-right", "name": "Wero & instant", "blurb": "EPI shareholder since 2020.", "div": "equens", "rev": "fs", "products": [
            P("wero", "Wero acceptance & processing", "An EPI shareholder since November 2020 and Wero member since June 2025: Wero e-commerce live in Germany (PAYONE, Q4 2025) and Belgium (March 2026), Wero for issuers and acquiring processing, and BNP Paribas Netherlands moved onto Wero before the iDEAL switch ⚠ timing 2027 or 2028.",
              s=["bank", "smb"], lc="move", st="new", neo=[0, "Off the card networks."],
              mc="Worldline's own filing frames Wero as a way round card-network fees.",
              src=[["Worldline: Wero acquiring processing", WEROACQ], ["H1 2026 results", H1PR], ["Universal Registration Document 2025", URD]]),
            P("instant", "Instant payments & clearing", "equensWorldline clearing, IP BOP Cloud (live January 2025), Nimbus instant-payments SaaS, Swift connectivity to the ECB's TIPS, and account-to-account connectivity for French banks.",
              s=["bank"], lc="move", neo=[0, ""], src=[["Universal Registration Document 2025", URD], ["H1 2026 presentation", H1P]]),
        ]},
        {"id": "2.5", "ic": "globe", "name": "Cross-border", "blurb": "Global Collect, 150+ markets.", "div": "gc", "rev": "ms", "products": [
            P("globalcollect", "Global Collect", "Cross-border acceptance in 150+ markets for 800+ global enterprises, back to growth in H1 2026, with YeePay for Chinese airlines (October 2025) and EcoFlow (May 2026).",
              s=["glob"], lc="move", neo=[1, "Acquires every network."], src=[["H1 2026 presentation", H1P]]),
            P("klarna", "Klarna", "Klarna's pay-later on Global Collect first, then GoPay and Worldline's terminals (May 2026).",
              s=["glob", "shop"], lc="borrow", st="new", ay="May 2026", o="P", at="Klarna", neo=[0, "Klarna."],
              mc="A bank-led instalment option is the alternative at the counter.",
              src=[["Worldline: press releases", WLPR]]),
        ]},
        {"id": "2.6", "ic": "coins", "name": "Digital money", "blurb": "Stablecoins, digital euro.", "div": "grp", "rev": "ms", "products": [
            P("stablecoins", "Stablecoin settlement", "Stablecoin settlement with Fipto (November 2025), Circle Payments Network managed payments (April 2026) and an 'Open USD' partnership.",
              s=["glob"], lc="move", st="new", o="P", at="Fipto, Circle", neo=[0, "Off the card networks."], src=[["Worldline: press releases", WLPR], ["H1 2026 results", H1PR]]),
            P("deuro", "Digital euro pilot", "Chosen for the ECB's digital-euro pilot as acquiring PSP and technical service provider (July 2026); the pilot starts in the second half of 2027.",
              s=["bank"], lc="move", st="new", ay="Jul 2026", neo=[0, ""], src=[["Worldline: press releases", WLPR]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every payment: 3-D Secure and Worldline's own token service, fraud scoring and Visa's Decision Manager, Click to Pay, Europe's first live agentic payments on Mastercard Agent Pay, and open banking and smart routing.",
    "tiles": [
        {"id": "3.1", "ic": "fingerprint", "name": "Authentication & tokens", "blurb": "ACS and its own token service.", "div": "equens", "rev": "fs", "products": [
            P("acs", "Access Control Server (3-D Secure)", "Trusted authentication for issuers, growing in Q2 2026 and already handling agentic transactions.",
              s=["bank", "shop"], lc="open", neo=[1, "3-D Secure for every network."], src=[["H1 2026 results", H1PR]]),
            P("tokens", "Token management", "An EMVCo-compliant issuer token service, and network tokens on Global Collect, where Mastercard named Worldline a tokenisation partner (June 2025) ⚠ from a search summary.",
              s=["bank", "glob"], lc="open", neo=[1, "Own token service; Mastercard tokens on Global Collect ⚠."],
              mc="Worldline's own token service can stand in for Mastercard's.",
              src=[["Worldline: card issuing", ISSUING], ["Mastercard: checkout in Europe, Jun 2025", MC25]]),
        ]},
        {"id": "3.2", "ic": "shield-check", "name": "Fraud & risk", "blurb": "Watcher, Decision Manager.", "div": "equens", "rev": "fs", "products": [
            P("fraud", "Payment Fraud Management", "Watcher, Instant Score and case management for banks, which Worldline calls Europe's number one fraud processor.",
              s=["bank"], lc="everyday", neo=[0, "Worldline's own."], src=[["Worldline: payment fraud management", FRAUD]]),
            P("visadm", "Visa Decision Manager", "Visa Acceptance Solutions' Decision Manager built into Worldline's merchant fraud tools (October 2024).",
              s=["ent", "glob"], lc="everyday", ay="Oct 2024", o="P", at="Visa", neo=[0, "Visa."], src=[["Worldline: press releases", WLPR]]),
            P("vop", "Verification of Payee", "Verification of Payee for the EU Instant Payments Regulation, and a domestic scheme for the central banks of Aruba and of Curaçao and Sint Maarten (Q2 2026).",
              s=["bank"], lc="move", neo=[0, ""], src=[["H1 2026 results", H1PR], ["Universal Registration Document 2025", URD]]),
        ]},
        {"id": "3.3", "ic": "zap", "name": "Click to Pay", "blurb": "Recurring, a European first.", "div": "gc", "rev": "ms", "products": [
            P("c2p", "Click to Pay", "Ogone and Saferpay named Click to Pay partners in Mastercard's European checkout update (June 2025) ⚠ from a search summary, and Click to Pay for recurring payments on Global Collect, generally available from 30 July 2026.",
              s=["glob", "shop"], lc="grow", st="new", neo=[1, "EMVCo standard; Mastercard named Worldline a partner ⚠."],
              mc="Carrying Click to Pay through the GoPay migration keeps it in front of every Ogone and SIPS merchant.",
              src=[["Mastercard: checkout in Europe, Jun 2025", MC25], ["Worldline: press releases", WLPR]]),
        ]},
        {"id": "3.4", "ic": "bot", "name": "Agentic commerce", "blurb": "Europe's first on Agent Pay.", "div": "wl", "rev": "ms", "products": [
            P("agentpay", "Mastercard Agent Pay", "Europe's first live end-to-end agentic payment in production, an ING cardholder and a Dutch merchant on Agent Pay (2 June 2026), then France's first with Crédit Agricole and Weezevent (25 June 2026); Worldline did acceptance, acquiring, authentication and issuer processing. Named with Fiserv and Nexi as a planned user of Mastercard's Agent Suite for merchants (September 2026).", short="Agent Pay",
              s=["bank", "ent"], lc="move", st="new", ay="Jun 2026", o="P", at="Mastercard", neo=[3, "Mastercard Agent Pay."],
              mc="Mastercard's clearest lead at Worldline, and Visa followed within a month.",
              src=[["Mastercard: Worldline, ING and Mastercard, Jun 2026", INGMC], ["Option Finance: Crédit Agricole, Jun 2026", CAMC], ["Mastercard: Agent Suite, Sep 2026", MCAS]]),
            P("agentic", "Agentic stack", "A Worldline MCP server, the ConnectAI developer hub supporting Google's AP2 and OpenAI's ACP, and a UCP payment handler on Global Collect (September 2026); Visa ran a live agentic payment with ING in Germany (July 2026). Worldline calls itself protocol-agnostic.",
              s=["ent", "glob"], lc="move", st="new", neo=[1, "Protocol-agnostic; Visa too."], src=[["Worldline: agentic commerce", AGENTIC], ["H1 2026 presentation", H1P]]),
        ]},
        {"id": "3.5", "ic": "plug", "name": "Open banking & routing", "blurb": "3,500 banks, AI routing.", "div": "wl", "rev": "fs", "products": [
            P("openbanking", "Open banking APIs", "Access to about 3,500 banks in 19 countries, with UniCredit renewed in 2025.",
              s=["bank", "ent"], lc="open", neo=[0, ""], src=[["Universal Registration Document 2025", URD]]),
            P("routing", "AI smart routing & DCC", "AI smart routing (July 2025), credited with 3% more cross-border approvals, alongside currency conversion, loyalty and promotions, and a multi-country portal.",
              s=["ent", "glob"], lc="grow", neo=[1, "Routes across networks."], src=[["H1 2026 presentation", H1P], ["Universal Registration Document 2025", URD]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "Who buys: small merchants (half of Merchant Services revenue), enterprises with €600 billion processed, banks that outsource processing, and public bodies and specialist verticals.",
    "tiles": [
        {"id": "4.1", "ic": "briefcase", "name": "Small merchants", "blurb": "Half of Merchant Services.", "div": "payone", "rev": "ms", "products": [
            P("smb", "SMB acquiring", "Half of Merchant Services revenue, sold directly, through partner banks and through ISVs, with PAYONE's 'Germany pays digitally' fee-free card acceptance for savings-bank customers.",
              s=["smb"], lc="everyday", neo=[1, "Accepts every network."], src=[["Universal Registration Document 2025", URD]]),
            P("tapmobile", "Tap on Mobile", "SoftPOS in 23 markets: €760 million of volume in 2025 (three times 2024), Tap to Pay on iPhone and BLIK in Poland. Worldline launched SoftPOS with Mastercard and Axis Bank in India in 2020 ⚠ India since sold.",
              s=["smb"], lc="move", neo=[1, "Accepts every network."], src=[["FY2025 results", FY25], ["Mastercard: SoftPOS in India, Jun 2020", MC20]]),
            P("smartpos", "SmartPOS & terminals", "Android SmartPOS in 16 markets and the S-Cube terminal with the Sparkassen (October 2025). Worldline was the first payment provider certified for Mastercard's Enhanced Contactless (March 2021).",
              s=["smb"], lc="move", neo=[1, "Accepts every network."], src=[["FY2025 results", FY25], ["Worldline: press releases", WLPR]]),
            P("financing", "Merchant cash advance", "Cash advances with YouLend in Belgium and the Netherlands, Lemonero in the Czech Republic and POS Fast Cash with Eurobank in Greece.",
              s=["smb"], lc="borrow", o="P", at="YouLend, Lemonero, Eurobank", neo=[0, ""], src=[["Universal Registration Document 2025", URD]]),
        ]},
        {"id": "4.2", "ic": "building-2", "name": "Enterprise", "blurb": "€600bn processed.", "div": "wl", "rev": "ms", "products": [
            P("enterprise", "Enterprise acceptance", "€600 billion processed for large merchants, about €200 billion of it acquired by Worldline, with FreedomPay for hospitality, Deliverect kiosks, commercetools, Gr4vy and a Salesforce Commerce Cloud connector (Q2 2026).",
              s=["ent"], lc="everyday", neo=[1, "Accepts every network."], src=[["Universal Registration Document 2025", URD], ["H1 2026 results", H1PR]]),
            P("onecommerce", "One Commerce", "An omnichannel platform, live in the UK on 7 January 2026 and shown at EuroShop in February.",
              s=["ent"], lc="everyday", st="new", ay="Jan 2026", neo=[1, "Accepts every network."], src=[["Worldline: press releases", WLPR]]),
        ]},
        {"id": "4.3", "ic": "landmark", "name": "Banks & processors", "blurb": "Financial Services, €792m.", "div": "equens", "rev": "fs", "products": [
            P("fi", "Processing for banks", "Financial Services, €792 million of revenue in 2025: issuing and acquiring processing for banks, a backup acquiring-processing service, and next-generation processing for PSA in Austria on Worldline's sovereign cloud (January 2026).",
              s=["bank"], lc="everyday", neo=[1, "Every network and domestic scheme."], src=[["FY2025 results", FY25], ["H1 2026 presentation", H1P], ["Worldline: press releases", WLPR]]),
        ]},
        {"id": "4.4", "ic": "scroll-text", "name": "Public sector & verticals", "blurb": "Greece, insurance, Switzerland.", "div": "greece", "rev": "ms", "products": [
            P("verticals", "Public sector & verticals", "Clearing non-domestic cards for Greece's Independent Authority for Public Revenue through DIAS (Q2 2026), Paycloud Hub for insurance in Italy, the Secure EFTPOS Network in Switzerland and IRIS account-to-account QR payments in Greece.",
              s=["ent"], lc="beyond", neo=[0, ""], src=[["H1 2026 results", H1PR], ["Universal Registration Document 2025", URD]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Worldline: a thousand sales staff and 23,000 partner-bank branches, 400 ISVs and platforms, and the Axis and GoPay gateways that legacy Ogone, SIPS and Saferpay merchants are moving onto.",
    "tiles": [
        {"id": "5.1", "ic": "users-round", "name": "Sales & bank partners", "blurb": "23,000 branches.", "div": "payone", "rev": "ms", "products": [
            P("channels", "Direct sales & partner banks", "More than 1,000 direct sales and support staff, digital self-service onboarding, and partner banks carrying about 30% of SMB flows through 23,000 branches, from the Sparkassen to KB SmartPay in the Czech Republic.",
              s=["smb", "bank"], lc="open", neo=[0, ""], src=[["Universal Registration Document 2025", URD]]),
        ]},
        {"id": "5.2", "ic": "code-xml", "name": "ISVs & platforms", "blurb": "400 partners, Launchpad.", "div": "wl", "rev": "ms", "products": [
            P("isv", "Worldline for Platforms by OPP", "Payments for 400+ ISVs and ISOs, and for platforms through OPP, and Worldline Web powered by Wix for small merchants (Switzerland first).",
              s=["isv"], lc="open", neo=[0, ""], src=[["Universal Registration Document 2025", URD]]),
            P("launchpad", "Launchpad", "AI self-service onboarding, in pilot in H1 2026.",
              s=["smb", "isv"], lc="open", st="new", neo=[0, ""], src=[["H1 2026 results", H1PR]]),
        ]},
        {"id": "5.3", "ic": "monitor", "name": "Gateways", "blurb": "Axis and GoPay.", "div": "wl", "rev": "ms", "products": [
            P("gateways", "Axis, GoPay & legacy gateways", "Axis in-store (more than 10 billion transactions a year, December 2025) and GoPay online, with Saferpay, Ogone and SIPS being moved across. Mastercard's MasterPass was distributed to Worldline merchants from 2013.",
              s=["ent", "smb"], lc="open", st="flux", neo=[1, "Carries every network."], src=[["FY2025 results", FY25], ["H1 2026 results", H1PR], ["FinTech Futures: MasterPass deal, Oct 2013", MC13]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Worldline", "blurb": "Agent Pay firsts, domestic schemes.", "products": [
        P("mcatwl", "Mastercard at Worldline", "Worldline acquires and processes Mastercard across Europe, ran Europe's first live Agent Pay payments with ING (June 2026) and Crédit Agricole, is a planned Agent Suite user, and carries Click to Pay and tokens on Global Collect, Ogone and Saferpay. No framework agreement is public. Domestic schemes, Wero, Klarna and Visa's fraud tools sit beside it, and the new risk chief came from Visa.",
          s=["bank"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Mastercard: Worldline, ING and Mastercard, Jun 2026", INGMC], ["Mastercard: checkout in Europe, Jun 2025", MC25]]),
    ]},
    {"id": "pillar-market", "name": "European acquiring", "blurb": "Wero, the digital euro, AML.", "products": [
        P("market", "The market", "Wero and the digital euro as account-based rivals to cards, domestic schemes in every core market, the EU's new anti-money-laundering authority, the Instant Payments Regulation and PSD3. Peers such as Adyen, Nexi and Stripe ⚠ are inference, not sourced.",
          s=["bank"], div="grp", rev="grp", src=[["Universal Registration Document 2025", URD]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
