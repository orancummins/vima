"""Attijariwafa bank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the H1 2026 results (27 July 2026), the 2025 results
(23 February 2026), the Financial Report 2025 and the September 2026 investor presentation. The bank's own card pages
could not be read, so card networks come from press and one independent guide (marked ⚠). ``neo`` is the Mastercard
lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1 = "https://ir.attijariwafabank.com/static-files/cbba8fbc-6f4e-40c1-8413-4dd5dff2c7bd"
H1EN = "https://ir.attijariwafabank.com/static-files/53d607a8-26fe-49a1-95f7-0bfa41530e80"
FY25 = "https://ir.attijariwafabank.com/static-files/237262e0-db19-4ae5-ad23-5666a1d4faa3"
AR25 = "https://ir.attijariwafabank.com/static-files/a416ccce-c175-4c8c-9459-421c61011f10"
PRES = "https://ir.attijariwafabank.com/static-files/a5c71469-d5ff-4048-8ca8-8c7311300ca4"
KEYFIG = "https://ir.attijariwafabank.com/key-figures"
GOV = "https://ir.attijariwafabank.com/corporate-governance"
KETTANI = "https://www.infomediaire.net/?p=182984"
SIMPLE = "https://lematin.ma/economie/attijariwafa-bank-lance-sa-neobanque-simple/347733"
SIMPLEWF = "https://wafir.ma/fr/guide/simple-neobanque-attijariwafa-avis-30-jours-tarifs-frais-2026"
CARDS = "https://wafir.ma/fr/guide/comparatif-cartes-bancaires-maroc-2026-visa-mastercard-gold-platinum"
AP = "https://fr.hespress.com/432204-attijari-payment-lance-officiellement-son-activite-dacquisition-commercants.html"
HESPEN = "https://en.hespress.com/115317-moroccos-digital-payments-market-opens-as-four-banks-break-monopoly.html"
CC = "https://conseil-concurrence.ma/wp-content/uploads/2025/05/Communique-du-Conseil-de-la-concurrence-CMI-Fr.pdf"
BAMCC = "https://fr.hespress.com/480898-paiement-electronique-bam-et-le-conseil-de-la-concurrence-saluent-louverture-du-marche.html"
IFEE = "https://fnh.ma/article/actualite-economique/bank-al-maghrib-plafonne-les-frais-dinterchange-des-paiements-par-carte"
IFEE2 = "https://www.financialafrik.com/2026/10/09/maroc-bank-al-maghrib-abaisse-a-050-le-plafond-des-frais-dinterchange-sur-les-paiements-par-carte/"
CMI = "https://fnh.ma/article/actualite-economique/paiements-electroniques-cmi-transformation"
INST = "https://telquel.ma/instant-t/2023/05/31/le-virement-interbancaire-instantane-operationnel-au-maroc-a-partir-du-1er-juin_1814743/"
INST2 = "https://telquel.ma/instant-t/2024/02/29/8-mois-apres-leurs-lancement-les-virements-instantanes-avoisinent-les-31-000-operations-par-jour_1859415/"
MOB = "https://fr.hespress.com/370361-paiement-numerique-au-maroc-seulement-10-adoptent-le-mobile.html"
UCL = "https://boursenews.ma/article/actualite/cartes-de-paiements-attijariwafa-bank-lance-une-premiere-en-afrique-et-au-moyen-orient"
VISA24 = "https://www.infomediaire.net/?p=175649"
RAM = "https://snrtnews.com/fr/article/royal-air-maroc-et-visa-revelent-les-premieres-cartes-bancaires-co-brandees-avec-des"
APAY = "https://www.financialafrik.com/2023/08/10/attijariwafa-bank-lance-son-apple-pay/"
APAY2 = "https://telquel.ma/instant-t/2024/11/19/paiement-mobile-voici-les-banques-marocaines-qui-ont-integre-apple-pay_1905063/"
JCB = "https://fnh.ma/article/actualites-marocaines/monetique-attijariwafa-bank-prete-a-accepter-les-cartes-du-reseau-japonais-jcb-sur-ses-gab"
LANA = "https://telquel.ma/2026/04/10/cih-bank-lana-cash-signe-un-partenariat-strategique-avec-mastercard_1983718"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · owners · plan", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Morocco's largest bank with MAD 825 billion of assets and a 22.9% return on tangible equity, owned 46.5% by Al Mada, dating from 1904 and 1911, rated BB+, and starting its GOAL 2030 plan with data and AI at its heart.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "MAD 825bn, RoaTE 22.9%.", "div": "awb", "rev": "bmeo", "products": [
            P("balance", "Balance sheet & earnings", "Total assets of MAD 825.3 billion and equity of MAD 81.1 billion at 30 June 2026; net banking income of MAD 18.4 billion (+4.0%) and net income group share of MAD 5.9 billion (+1.1%) in the half, RoaTE 22.9%, cost:income 36.8%. In 2025: net banking income MAD 34.9 billion and group share MAD 10.6 billion (+16.2%). More than 12 million customers and 22,052 employees in 27 countries.",
              s=["corp"], neo=[0, ""], src=[["H1 2026 results", H1EN], ["2025 results", FY25], ["IR: key figures", KEYFIG]]),
        ]},
        {"id": "1.2", "ic": "users-round", "name": "Owners & leadership", "blurb": "Al Mada 46.5%; El Kettani.", "div": "awb", "rev": "bmeo", "products": [
            P("owners", "Shareholders", "Listed in Casablanca with a market value of about USD 17 billion at end-2025; Al Mada holds 46.5% and Grupo Santander (Santusa) 5.1%, with local institutions and free float the rest ⚠ split read from a chart.",
              s=["corp"], neo=[0, ""], src=[["Financial Report 2025", AR25]]),
            P("leadership", "Board & management", "Chairman and CEO Mohamed El Kettani; deputy CEOs include Rachid Kettani (retail banking, since September 2025) and Hassan El Bedraoui; Mohammed Hamlili runs finance; Ghyzlaine Alami Marrouni leads the retail and professional market.",
              s=["corp"], neo=[0, ""], src=[["IR: governance", GOV], ["Infomédiaire: Rachid Kettani, Sep 2025", KETTANI], ["Le Matin: Simple, May 2026", SIMPLE]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & ratings", "blurb": "1904, 1911, 2004; BB+.", "div": "awb", "rev": "bmeo", "products": [
            P("heritage", "Heritage", "Formed in 2004 from Banque Commerciale du Maroc (1911) and Wafabank (1904); Africa's fifth-largest bank by assets (African Business, October 2025).",
              s=["con"], o="I", neo=[0, ""], src=[["Financial Report 2025", AR25]]),
            P("ratings", "Credit ratings", "Fitch BB+ (upgraded December 2025), S&P BB+ and Moody's Ba1, all stable; Moody's includes two notches of state support.",
              s=["corp"], neo=[0, ""], src=[["Financial Report 2025", AR25]]),
        ]},
        {"id": "1.4", "ic": "brain", "name": "Data & AI", "blurb": "AI agents, \"AI for All\".", "div": "awb", "rev": "bmeo", "products": [
            P("ai", "Data & AI programme", "Machine learning in pilot or production for next-best-offer, personal finance, real-time fraud detection and scoring; a generative-AI wave with assistants for branches, the contact centre and clients, and AI-written credit memos.",
              s=["con", "corp"], st="new", neo=[0, "The bank's own."],
              mc="An AI agenda with no payments partner named: room for Decision Intelligence and agentic payments.",
              src=[["Investor presentation, Sep 2026", PRES]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "GOAL 2030", "blurb": "Payments, Africa, AI.", "div": "awb", "rev": "bmeo", "products": [
            P("goal2030", "GOAL 2030", "The plan that replaced @mbitions 2025 in 2026: pioneer the future of banking (digital payments and embedded finance), sustain pan-African leadership, human-centric banking powered by AI, and one integrated group. Morocco retail is to accelerate payments and digital journeys.",
              s=["corp"], st="new", neo=[0, ""], src=[["H1 2026 results", H1], ["Investor presentation, Sep 2026", PRES]]),
            P("ventures", "Attijariwafa Ventures", "A USD 30 million corporate venture fund set up in 2023 with Wafa Assurance, with five investments so far; the group is a founding member of the Morocco Fintech Center led by Bank Al-Maghrib.",
              s=["corp"], ay="2023", o="B", neo=[0, ""], src=[["Investor presentation, Sep 2026", PRES]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: a Visa core card range with Mastercard at the top, Simple's cards mostly on Mastercard, Apple Pay and QR payments, a new acquirer in Attijari Payment, CMI as the domestic switch, instant transfers since 2023, and Wafacash for cash and remittances.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Wafa cards & co-brands", "blurb": "Visa core, Mastercard top.", "div": "awb", "rev": "bmeo", "products": [
            P("wafavisa", "Wafa Visa cards", "The core debit and credit range: Wafa Visa Classic (MAD 150 a year), Gold (MAD 400, with an e-shopping virtual card) and Platinum (MAD 1,200) ⚠ independent guide, May 2026; Visa signed a strategic partnership with the bank in December 2024.",
              short="Wafa Visa (Visa)", s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa ⚠."],
              src=[["Wafir: card comparison, May 2026", CARDS], ["Infomédiaire: Visa partnership, Dec 2024", VISA24]]),
            P("awbblack", "AWB Black", "An invitation-only card for clients with more than MAD 1 million of wealth, on Mastercard World Elite, at MAD 2,500 a year ⚠ independent guide.",
              short="AWB Black (Mastercard)", s=["con"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard World Elite ⚠."],
              src=[["Wafir: card comparison, May 2026", CARDS]]),
            P("ucl", "UEFA Champions League Mastercard", "An international contactless affinity card launched on 13 September 2019, billed as the first of its kind in Africa and the Middle East, with Priceless Mascots for cardholders' children ⚠ current status unknown.",
              short="UEFA card (Mastercard)", s=["con", "young"], lc="everyday", st="unconf", ay="Sep 2019", o="P", at="Mastercard", neo=[2, "Mastercard."],
              src=[["Boursenews: UEFA Mastercard, Sep 2019", UCL]]),
            P("ram", "Royal Air Maroc co-brand", "Safar Flyer miles cards with Royal Air Maroc and Visa, issued by Attijariwafa bank and Bank of Africa, unveiled in February 2024 ⚠.",
              short="Royal Air Maroc (Visa)", s=["con", "mre"], lc="everyday", ay="Feb 2024", o="P", at="Visa, Royal Air Maroc", neo=[0, "Visa."],
              src=[["SNRT News: RAM and Visa cards, Feb 2024", RAM]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Simple cards", "blurb": "Three tiers on Mastercard.", "div": "simple", "rev": "bmeo", "products": [
            P("simplecards", "Simple cards", "Launched 25 May 2026: SimpleGo (free) with a Standard Mastercard, SimplePlus (MAD 19 a month) Mastercard Gold, SimplePrime (MAD 59) Mastercard World ⚠ Le Matin says Gold, and SimpleMetal (MAD 159) a metal card whose network is not stated ⚠. Cards are collected at Marjane, by Glovo or at about 4,000 Wafacash points.",
              short="Simple (mostly Mastercard)", s=["young", "mre", "con"], lc="everyday", st="new", ay="May 2026", o="B", at="Mastercard", neo=[1, "Three of four tiers on Mastercard; Metal not stated."],
              mc="The newest and most visible Mastercard programme in the group.",
              src=[["Le Matin: Simple launch, May 2026", SIMPLE], ["Wafir: Simple review, Jun 2026", SIMPLEWF]]),
            P("virtual", "Virtual & single-use cards", "Multi-use or single-use cards generated instantly to secure e-commerce and international payments, free in every Simple tier.",
              s=["young", "con"], lc="move", st="new", neo=[None, "Network not stated."], src=[["H1 2026 results", H1], ["Wafir: Simple review, Jun 2026", SIMPLEWF]]),
        ]},
        {"id": "2.3", "ic": "smartphone", "name": "Wallets & QR", "blurb": "Apple Pay 2023; Simple Pay.", "div": "awb", "rev": "bmeo", "products": [
            P("tokenwallets", "Apple Pay & Google Pay", "Apple Pay launched on 9 August 2023, first for L'bankalik customers, followed by Google Pay ⚠ date; for Simple, Le Matin lists both in SimpleGo while Wafir said they were due in Q3 2026 ⚠.",
              s=["con", "young"], lc="move", ay="Aug 2023", o="P", at="Apple, Google", neo=[1, "Tokenises Visa and Mastercard cards alike."],
              src=[["Financial Afrik: Apple Pay, Aug 2023", APAY], ["TelQuel: banks on Apple Pay, Nov 2024", APAY2]]),
            P("simplepay", "Simple Pay & QR payments", "Free instant QR-code payments between people and to merchants, open to the bank's 6 million mobile customers (May 2026); Moroccan mobile payment is used by only about 10% (May 2024).",
              s=["con", "vse"], lc="move", st="new", ay="May 2026", o="B", neo=[0, "Domestic QR, not a card scheme."],
              src=[["Le Matin: Simple launch, May 2026", SIMPLE], ["Hespress: mobile payment at 10%, May 2024", MOB]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Attijari Payment", "blurb": "Acquiring since May 2025.", "div": "apay", "rev": "bmeo", "products": [
            P("attpay", "Attijari Payment (merchant acquiring)", "Licensed as a payment institution on 13 March 2025 and acquiring since 1 May 2025, when CMI's monopoly ended: standard, till-integrated and multi-site terminals and online payments. Schemes accepted and merchant numbers not published ⚠.",
              short="Attijari Payment", s=["vse", "corp"], lc="move", st="new", ay="May 2025", o="B", neo=[1, "Accepts the international schemes ⚠."],
              mc="A new acquirer taking over CMI's merchants as interchange falls to 0.50%.",
              src=[["Hespress: Attijari Payment, Jul 2025", AP], ["Hespress EN: four banks break the monopoly, Jul 2025", HESPEN]]),
            P("processing", "Attijari Payment Processing", "The group's card processor, led by Fahd Bettache: it added UnionPay acceptance on the bank's ATMs in 2018 and JCB in March 2021, with partner M2M.",
              s=["con", "corp"], lc="move", ay="2021", o="B", at="M2M", neo=[1, "Processes every scheme."],
              src=[["FNH: JCB on ATMs, Mar 2021", JCB], ["Hespress: Attijari Payment, Jul 2025", AP]]),
        ]},
        {"id": "2.5", "ic": "network", "name": "CMI, the domestic switch", "blurb": "Monopoly ended 2024–25.", "div": "awb", "rev": "bmeo", "products": [
            P("cmi", "Centre Monétique Interbancaire (CMI)", "The interbank processor founded by nine banks (2001, live 2004), Attijariwafa among them ⚠: once the sole acquirer, now a technical platform for every acquirer after the Competition Council decision of 31 October 2024. In 2025 it handled about 240 million card transactions and nearly MAD 100 billion for merchants.",
              short="CMI", s=["con", "vse"], lc="move", st="flux", o="P", at="CMI", neo=[0, "Domestic switch and processor."],
              src=[["Competition Council on CMI, May 2025", CC], ["FNH: CMI's transformation, Jan 2026", CMI]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Instant transfers", "blurb": "Live since June 2023.", "div": "awb", "rev": "bmeo", "products": [
            P("instant", "Instant interbank transfers", "Morocco's instant transfer, run by GSIMT on ISO 20022, in under 20 seconds, 24/7, since 1 June 2023; about 31,000 a day after eight months. The bank also offers instant transfers into Wafabourse brokerage accounts (December 2025).",
              s=["con", "vse"], lc="move", ay="Jun 2023", o="P", at="GSIMT", neo=[0, "Account-to-account."],
              src=[["TelQuel: instant transfer live, May 2023", INST], ["TelQuel: 31,000 a day, Feb 2024", INST2], ["Financial Report 2025", AR25]]),
        ]},
        {"id": "2.7", "ic": "send", "name": "Cash & remittances", "blurb": "Wafacash, economic banking.", "div": "wafacash", "rev": "sfs", "products": [
            P("wafacash", "Wafacash", "Cash and international money transfer through about 4,000 points, reaching 245 rural localities (June 2026); MAD 66.2 billion of volume in 2025, but net banking income fell 7% as transfers slowed; bought Express Tel in 2025.",
              s=["unb", "mre"], lc="move", o="B", neo=[0, "Own and partner rails ⚠."],
              mc="A slowing remittance business is a case for cross-border send.",
              src=[["Financial Report 2025", AR25], ["H1 2026 results", H1]]),
            P("hissab", "Economic banking accounts & wallet", "Hissab Bikhir and Taamine Iktissadi accounts and a mobile wallet for the unbanked: 337,000 new customers in 2025 and 200,000 in the first half of 2026.",
              s=["unb"], lc="open", o="B", neo=[0, ""], src=[["2025 results", FY25], ["H1 2026 results", H1]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: the bank's own real-time fraud models, AI assistants for clients and staff, onboarding in minutes, Simple's deals and travel booking, and free support for more than a million very small businesses.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & risk", "blurb": "Real-time models.", "div": "awb", "rev": "bmeo", "products": [
            P("fraud", "Fraud detection & scoring", "Real-time machine-learning detection of atypical transactions learned from payment behaviour, and behavioural scoring for credit, in pilot or production.",
              s=["con", "vse"], lc="everyday", neo=[0, "The bank's own."],
              mc="No Mastercard fraud or scam tool is public here.",
              src=[["Investor presentation, Sep 2026", PRES]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI & onboarding", "blurb": "Simple AI; minutes to open.", "div": "simple", "rev": "bmeo", "products": [
            P("simpleai", "Simple AI & client assistant", "A conversational assistant in Simple, with voice commands planned, and a 24/7 client assistant for product questions, complaints and transactions.",
              s=["young", "con"], lc="everyday", st="new", neo=[0, ""],
              mc="Agentic payments are untouched ground.",
              src=[["Le Matin: Simple launch, May 2026", SIMPLE], ["Investor presentation, Sep 2026", PRES]]),
            P("staffai", "AI for advisers", "A generative-AI assistant for branches and the contact centre with a 360-degree client view, and AI agents that help analysts read corporate data.",
              s=["corp"], lc="borrow", st="new", neo=[0, ""], src=[["Investor presentation, Sep 2026", PRES]]),
            P("onboarding", "Digital onboarding", "An account opened in minutes with an ID-card scan, biometrics and e-signature, with no branch visit.",
              s=["young", "mre"], lc="open", st="new", neo=[0, ""], src=[["Le Matin: Simple launch, May 2026", SIMPLE]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Deals & travel", "blurb": "Simple Deals, Simple Trip.", "div": "simple", "rev": "bmeo", "products": [
            P("deals", "Simple Deals & Share", "Discounts, promo codes, lounge access and exclusive offers, plus a referral programme that rewards members.",
              s=["young", "con"], lc="grow", st="new", neo=[0, ""],
              mc="Card-linked offers and Priceless could feed Simple Deals before the 2030 World Cup.",
              src=[["H1 2026 results", H1]]),
            P("trip", "Simple Trip", "Search, book and pay for a trip inside the app.",
              s=["young", "mre"], lc="beyond", st="new", neo=[0, ""], src=[["H1 2026 results", H1]]),
        ]},
        {"id": "3.4", "ic": "briefcase", "name": "Small-business support", "blurb": "1 million since 2016.", "div": "awb", "rev": "bmeo", "products": [
            P("darmoukawil", "Dar Al Moukawil", "Free support for very small businesses: 162,607 helped in the first half of 2026 and more than a million since 2016, through 25 centres and Daralmoukawil.com.",
              s=["vse"], lc="open", o="B", neo=[0, ""], src=[["H1 2026 results", H1], ["2025 results", FY25]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: Morocco's largest retail and corporate bank, consumer credit, leasing and Islamic finance, Wafa Assurance, and banks in 14 African countries and across Europe.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Retail & professional", "blurb": "26.6% of deposits.", "div": "awb", "rev": "bmeo", "products": [
            P("retail", "Retail & professional banking", "A 26.6% share of Moroccan deposits at end-2025 and MAD 382 billion of deposits in Morocco in June 2026 (+12%); MAD 5.5 billion of household loans in the half.",
              s=["con", "vse"], lc="everyday", neo=[1, "Visa core cards, Mastercard premium and Simple ⚠."], src=[["H1 2026 results", H1], ["Financial Report 2025", AR25]]),
        ]},
        {"id": "4.2", "ic": "building-2", "name": "Corporate & investment", "blurb": "30% of corporate loans.", "div": "awb", "rev": "bmeo", "products": [
            P("cib", "Corporate banking", "Corporate loans of MAD 227 billion (+14%) and equipment loans of MAD 142 billion (+36%) in June 2026; a 30% share of corporate loans and 27% of Treasury securities trading in 2025.",
              s=["corp"], lc="borrow", neo=[0, ""],
              mc="No commercial-card programme is public; Citi launched Mastercard commercial cards in Morocco in 2024.",
              src=[["H1 2026 results", H1], ["2025 results", FY25]]),
            P("markets", "Investment banking & asset management", "Attijari Finances Corp. (M&A), Wafa Gestion (24.3% of fund assets), Attijari Intermédiation (48.2% of online trading via Wafabourse) and Attijari Titrisation.",
              s=["corp", "con"], lc="grow", neo=[0, ""], src=[["Financial Report 2025", AR25]]),
        ]},
        {"id": "4.3", "ic": "hand-coins", "name": "Specialised finance", "blurb": "Wafasalaf 28.8% share.", "div": "wafasalaf", "rev": "sfs", "products": [
            P("wafasalaf", "Wafasalaf", "Morocco's consumer-credit leader with a 28.8% share (September 2025); net banking income MAD 1.44 billion in 2025; 50.91% owned. Simple sends its users to Wafasalaf for credit.",
              s=["con"], lc="borrow", neo=[0, ""],
              mc="Simple plans instalments and instant credit: Mastercard Installments could serve them.",
              src=[["Financial Report 2025", AR25], ["Wafir: Simple review, Jun 2026", SIMPLEWF]]),
            P("leasing", "Leasing, mortgages & factoring", "Wafabail (MAD 4.8 billion of new leases in 2025), Wafa Immobilier, Attijari Factoring and Wafa LLD long-term car rental.",
              s=["vse", "corp", "con"], lc="borrow", neo=[0, ""], src=[["Financial Report 2025", AR25]]),
            P("assafa", "Bank Assafa", "The group's participative (Islamic) bank, mainly home finance: assets of about MAD 9 billion and net banking income of MAD 241 million in 2025.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Financial Report 2025", AR25]]),
        ]},
        {"id": "4.4", "ic": "gem", "name": "Insurance", "blurb": "Wafa Assurance.", "div": "wafaass", "rev": "ins", "products": [
            P("wafaassurance", "Wafa Assurance", "Premiums of MAD 12.7 billion in 2025 (+8.4%), with subsidiaries in Tunisia, Côte d'Ivoire, Senegal, Cameroon and Egypt; group interest 39.64%.",
              s=["con", "corp"], lc="grow", neo=[0, ""], src=[["Financial Report 2025", AR25], ["H1 2026 results", H1]]),
        ]},
        {"id": "4.5", "ic": "earth", "name": "Africa & Europe", "blurb": "14 African countries.", "div": "africa", "rev": "irb", "products": [
            P("northafrica", "North Africa", "Attijari bank Tunisie (57.21%), Attijariwafa bank Egypt (bought from Barclays in May 2017) and Attijari bank Mauritanie: about MAD 3.8 billion of net banking income in 2025.",
              s=["con", "corp"], lc="everyday", o="A", neo=[None, "Networks not researched."], src=[["Financial Report 2025", AR25]]),
            P("westafrica", "West Africa (WAEMU)", "CBAO in Senegal with branches in Burkina Faso, Benin and Niger, Crédit du Sénégal, SIB in Côte d'Ivoire, BIM in Mali and BIA Togo: 1,251 branches in the region.",
              s=["con", "corp"], lc="everyday", o="A", neo=[None, "Networks not researched."], src=[["Financial Report 2025", AR25]]),
            P("centralafrica", "Central Africa (CEMAC)", "Union Gabonaise de Banque, Crédit du Congo and SCB Cameroun, with Chad also listed: 716 branches.",
              s=["con", "corp"], lc="everyday", o="A", neo=[None, "Networks not researched."], src=[["Financial Report 2025", AR25]]),
            P("europe", "Attijariwafa bank Europe", "A French bank (99.82%) serving Moroccans abroad in France, Belgium, Germany, Italy, Spain and Switzerland; international retail as a whole was 32.8% of group net banking income in 2025.",
              s=["mre"], lc="move", neo=[0, ""], src=[["Financial Report 2025", AR25], ["H1 2026 results", H1]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: Attijariwafa Mobile for 6 million, the Simple app, and the densest network in Africa, with more than 8,000 branches, Wafacash points and retail partners.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Attijariwafa Mobile", "blurb": "94.9% of transactions digital.", "div": "awb", "rev": "bmeo", "products": [
            P("mobile", "Attijariwafa Mobile & web", "About 6 million mobile customers; 181.5 million digital log-ons and 94.9% of eligible transactions on digital channels in the first half of 2026.",
              s=["con", "vse"], lc="everyday", neo=[0, ""], src=[["H1 2026 results", H1EN], ["Le Matin: Simple launch, May 2026", SIMPLE]]),
        ]},
        {"id": "5.2", "ic": "sparkles", "name": "Simple app", "blurb": "A super app, May 2026.", "div": "simple", "rev": "bmeo", "products": [
            P("simpleapp", "Simple", "Morocco's first neobank by its own account, launched 25 May 2026 as a super app: freemium tiers, savings and investing (Simple Invest), a teen account (Simple ONE, ages 12–17), aimed at young people and Moroccans abroad; it follows L'bankalik (2016).",
              s=["young", "mre"], lc="open", st="new", ay="May 2026", o="B", neo=[1, "Carries Mastercard cards."],
              src=[["Le Matin: Simple launch, May 2026", SIMPLE], ["Investor presentation, Sep 2026", PRES], ["Wafir: Simple review, Jun 2026", SIMPLEWF]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & partners", "blurb": "8,000+ branches.", "div": "awb", "rev": "bmeo", "products": [
            P("branches", "Branches & Wafacash points", "5,593 points in Morocco and more than 8,000 across the group at end-2025; about 7,000 contact points including ATMs and Wafacash for Simple.",
              s=["con", "unb"], lc="everyday", neo=[0, ""], src=[["Financial Report 2025", AR25], ["Le Matin: Simple launch, May 2026", SIMPLE]]),
            P("partners", "Retail & delivery partners", "Simple cards sold or delivered through Marjane, Glovo and selected Bim and Aswak Assalam stores ⚠.",
              s=["young"], lc="open", st="new", o="P", at="Marjane, Glovo", neo=[0, ""], src=[["Wafir: Simple review, Jun 2026", SIMPLEWF]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Attijariwafa", "blurb": "Simple and the top cards.", "products": [
        P("mcatawb", "Mastercard at Attijariwafa bank", "Mastercard carries three of Simple's four tiers (May 2026), AWB Black World Elite ⚠ and the 2019 UEFA Champions League card. Visa carries the core Wafa Visa range ⚠, the Royal Air Maroc co-brand and a strategic partnership signed in December 2024. Domestic payments are switched and processed by CMI and the group's own processor, and the bank now acquires merchants itself.",
          s=["con"], div="awb", rev="bmeo", mc="The relationship this map is drawn for.",
          src=[["Le Matin: Simple launch, May 2026", SIMPLE], ["Infomédiaire: Visa partnership, Dec 2024", VISA24], ["Boursenews: UEFA Mastercard, Sep 2019", UCL]]),
    ]},
    {"id": "pillar-market", "name": "Moroccan payments", "blurb": "CMI opened, interchange cut.", "products": [
        P("market", "The Moroccan market", "CMI's acquiring monopoly ended (decision of 31 October 2024; multi-acquirer from 1 May 2025); domestic interchange capped at 0.65% in October 2024 and 0.50% from 1 October 2026 (0.15% for government and neighbourhood shops); instant transfers since 2023; Mastercard has signed with CIH's Lana Cash (April 2026), Crédit du Maroc and Crédit Agricole du Maroc.",
          s=["con"], div="awb", rev="bmeo",
          src=[["Hespress: BAM and the Competition Council, Jul 2026", BAMCC], ["FNH: interchange cap, 2026", IFEE], ["Financial Afrik: 0.50% in force, Oct 2026", IFEE2], ["TelQuel: Lana Cash and Mastercard, Apr 2026", LANA]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
