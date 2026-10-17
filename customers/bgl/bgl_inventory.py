"""BGL BNP Paribas's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the 2025 results (2 April 2026), the tariff guide in
force from 1 October 2026 and bgl.lu product pages; the BNP Paribas group's Luxembourg line (CPBL) gives the latest
quarter. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides
wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

RES25 = "https://www.bgl.lu/content/dam/publicsite/a-propos/communiqu%C3%A9s-de-presse/2026/resultats_annuels/FR_20260402%20R%C3%A9sultats%20au%2031%20d%C3%A9cembre%202025_BGL%20BNP%20Paribas.pdf"
PJ25 = "https://paperjam.lu/article/bgl-bnp-paribas-affiche-un-benefice-de-515-millions-deuros"
CPBL = "https://chronicle.lu/category/surveys-reports/62553-bnp-paribas-cpbl-net-banking-income-reaches-eur187m-in-q2-up-12"
KNOW = "https://www.bgl.lu/fr/qui-sommes-nous/nous-connaitre.html"
GOV = "https://www.bgl.lu/fr/qui-sommes-nous/gouvernance-bgl-bnp-paribas.html"
HIST = "https://www.bgl.lu/fr/qui-sommes-nous/histoire-de-la-banque.html"
PRESS = "https://www.bgl.lu/fr/qui-sommes-nous/communiques-de-presse.html"
OTTON = "https://www.bgl.lu/content/dam/publicsite/a-propos/communiqu%C3%A9s-de-presse/2025/nomination/CommuniquePresse_Luxembourg_FINAL.pdf"
NOM26 = "https://www.bgl.lu/content/dam/publicsite/a-propos/communiqu%C3%A9s-de-presse/2026/20260327%20BGL%20BNP%20Paribas%20Nominations.pdf"
WERO25 = "https://www.bgl.lu/content/dam/publicsite/a-propos/communiqu%C3%A9s-de-presse/2025/epi-wero/20250616_Wero_FR.pdf"
BANCOMAT = "https://www.bgl.lu/content/dam/publicsite/a-propos/communiqu%C3%A9s-de-presse/2023/bancomat/FR_20231121_Bancomat.pdf"
ING = "https://www.bgl.lu/content/dam/publicsite/a-propos/communiqu%C3%A9s-de-presse/2024/021224/PressRelease_FR_0212.pdf"
AI24 = "https://www.bgl.lu/content/dam/publicsite/a-propos/communiqu%C3%A9s-de-presse/2024/intelligence-artificielle/240125%20-%20Communiqu%C3%A9%20BGL%20BNP%20Paribas%20AI.pdf"
INNOV = "https://www.bgl.lu/fr/solutions-innovantes.html"
CARDS = "https://www.bgl.lu/fr/particuliers/cartes-de-paiement.html"
VDEBIT = "https://www.bgl.lu/fr/particuliers/cartes-de-paiement/visa-debit.html"
ELITE = "https://www.bgl.lu/fr/particuliers/cartes-de-paiement/mastercard-elite.html"
RETOUR = "https://www.bgl.lu/fr/particuliers/cartes-de-paiement/assurance-retour-mastercard.html"
PLA = "https://www.bgl.lu/fr/particuliers/cartes-de-paiement/cartes-bancaires-pla.html"
MOBILE = "https://www.bgl.lu/fr/particuliers/paiements-mobiles.html"
TARIF = "https://www.bgl.lu/content/dam/publicsite/pdf/documents-officiels/tarif/guide-des-tarifs/guide-tarifaire.pdf"
ENT = "https://www.bgl.lu/fr/entreprises.html"
VBIZ = "https://www.bgl.lu/fr/entreprises/solutions-de-paiement/visa-business.html"
TPE = "https://www.bgl.lu/fr/entreprises/solutions-de-paiement/terminal-paiement.html"
WEROPRO = "https://www.bgl.lu/fr/entreprises/solutions-de-paiement/wero.html"
LIFE = "https://www.bgl.lu/fr/particuliers/assurances-vie.html"
VD20 = "https://www.bnpparibas.lu/en/bgl-bnp-paribas-and-visa-are-launching-a-new-card-in-luxembourg-the-visa-debit-card/"
AP19 = "https://www.bnpparibas.lu/en/apple-pay-coming-bgl-bnp-paribas-customers/"
VPAY13 = "https://mabanqueprivee.bnpparibas/rsc/contrib/document/particuliers/produits/comptes-cartes-services/PDF_frontaliersluxembour_20130617060422.pdf"
LEASE12 = "https://paperjam.lu/article/communique-resultats-financiers-au-31-decembre-2012-de-bgl-bnp-paribas"
GIRAFFY = "https://giraffy.com/lu/en/banking/credit-cards"
PR2Q26 = "https://invest.bnpparibas/en/document/2q26-pr"
URD25 = "https://invest.bnpparibas/en/document/universal-registration-document-annual-financial-report-2025-pdf"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · owners · plan", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: €2 billion of revenue and €514.5 million of profit in 2025, BNP Paribas and the Luxembourg State as owners, a bank dating from 1919, core banking in the group cloud and the GTS plan giving way to 2027–30.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & results", "blurb": "€514.5m profit, CET1 20.6%.", "div": "bgl", "rev": "cc", "products": [
            P("results", "2025 results", "Revenue of €2,008.5 million (+4%), costs of €921.8 million, cost of risk of €175.4 million and net income of €514.5 million (+8%) in 2025; balance sheet €64.6 billion and CET1 20.6% at 31 December 2025; 2,083 staff.",
              s=["con"], neo=[0, ""], src=[["BGL: 2025 results, Apr 2026", RES25], ["Paperjam: €515m profit", PJ25]]),
            P("cpbl", "Latest quarter (group's Luxembourg line)", "BNP Paribas' Commercial & Personal Banking in Luxembourg: revenue €187 million in Q2 2026 (+12.0%), gross operating income €104 million, cost of risk 8 bp, pre-tax income €100 million. BGL publishes no quarterly accounts of its own.",
              s=["con"], st="new", neo=[0, ""], src=[["Chronicle.lu: CPBL Q2 2026", CPBL], ["BNP Paribas 2Q26 results", PR2Q26]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Owners & leadership", "blurb": "BNP Paribas 66%, State 34%.", "div": "group", "rev": "cc", "products": [
            P("owners", "Ownership & ratings", "BNP Paribas 65.96% and the Luxembourg State 34% since May 2009, with BNP Paribas Fortis also named as a main shareholder; rated A2 (Moody's), A+ (S&P) and AA- (Fitch) on a page last updated October 2022 ⚠; about 185,000 clients ⚠.",
              s=["corp"], o="I", neo=[0, ""], src=[["BGL: history", HIST], ["BGL: governance", GOV], ["BGL: the bank", KNOW], ["BNP Paribas URD 2025", URD25]]),
            P("leadership", "Board & executive committee", "Chair Bob Kieffer; CEO and BNP Paribas country head Nicolas Otton since 1 January 2026, succeeding Béatrice Belorgey; COO Fernand Lepage and Chief Compliance Officer Séverine Campagne from 1 April 2026; Markus Stegmann heads retail banking.",
              s=["corp"], st="new", ay="Jan 2026", neo=[0, ""], src=[["BGL: Otton appointed, Nov 2025", OTTON], ["BGL: appointments, Mar 2026", NOM26], ["BGL: governance", GOV]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage", "blurb": "Since 1919.", "div": "bgl", "rev": "rcb", "products": [
            P("heritage", "From Banque Générale to BGL BNP Paribas", "Founded in 1919 as Banque Générale du Luxembourg; Fortis-owned from 1999, rescued with the Luxembourg State in 2008, BGL BNP Paribas from September 2009; merged with BNP Paribas Luxembourg in 2010 and absorbed ABN AMRO Bank (Luxembourg) in 2018.",
              s=["con"], o="I", neo=[0, ""], src=[["BGL: history", HIST]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "Core banking in the group cloud.", "div": "bgl", "rev": "cc", "products": [
            P("cloud", "Core banking in the group cloud", "Migration of core banking to the BNP Paribas group cloud finished in 2025, giving the computing power the bank needs for AI.",
              s=["corp"], st="new", o="P", at="BNP Paribas group", neo=[0, ""], src=[["BGL: 2025 results, Apr 2026", RES25]]),
            P("ai", "AI programme", "A €7.4 million, three-year R&D project with the University of Luxembourg's SnT to monitor AI models, up to €2.95 million co-financed by the state (January 2024); LuxemBERT, a Luxembourgish language model (2022); AI used in risk, payments, e-mail and credit processing.",
              s=["corp"], ay="Jan 2024", o="P", at="University of Luxembourg (SnT)", neo=[0, ""],
              mc="An AI-minded bank with no agentic-payments partner yet.",
              src=[["BGL: AI metamodel, Jan 2024", AI24], ["BGL: innovative solutions", INNOV]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy", "blurb": "GTS ends; 2027–30 next.", "div": "bgl", "rev": "cc", "products": [
            P("gts", "GTS plan & 2027–30", "GTS (Growth, Technology, Sustainability), launched in 2022, is in its final phase: mobile as the main channel, most retail products online, My Business Banking, the cloud move and shared utilities. Work on the 2027–30 plan has begun.",
              s=["corp"], st="flux", neo=[0, ""], src=[["BGL: 2025 results, Apr 2026", RES25]]),
            P("sekoia", "seKoia head office", "New Kirchberg head office opened 18 September 2025: 18,500 m², 1,100 workstations and 70% less energy than the old building; private banking moved into Royal Roosevelt House in June 2026.",
              s=["corp"], st="new", ay="Sep 2025", neo=[0, ""], src=[["BGL: 2025 results, Apr 2026", RES25], ["BGL: press releases", PRESS]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Visa Debit in every pack, credit cards split between Visa Classic and Mastercard Gold, Platinum and Elite, Visa Business, Apple Pay and watches, Wero replacing Payconiq, Axepta terminals, and the shared Bancomat ATMs.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "Visa Debit since 2020.", "div": "retail", "rev": "rcb", "products": [
            P("visadebit", "Visa Debit", "The debit card in every pack (one in Essentiel and Confort, two in Exclusif; €2 a month on its own), launched with Visa on 24 November 2020 for online and foreign use; it took over from V PAY ⚠.",
              short="Visa Debit (Visa)", s=["con", "xb"], lc="everyday", ay="Nov 2020", o="P", at="Visa", neo=[0, "Visa."],
              mc="Every BGL pack carries a Visa debit card; no renewal date is public.",
              src=[["BGL and Visa: Visa Debit, Nov 2020", VD20], ["BGL: Visa Debit", VDEBIT], ["BGL: tariffs from Oct 2026", TARIF], ["BNP Paribas: cards for cross-border workers, 2013 ⚠", VPAY13]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Visa entry, Mastercard premium.", "div": "retail", "rev": "rcb", "products": [
            P("visaclassic", "Visa Classic", "The entry credit card, €2 a month and included in the Essentiel pack, with purchase protection; made of corn-based PLA with five-year validity.",
              short="Visa Classic (Visa)", s=["con"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."],
              src=[["BGL: payment cards", CARDS], ["BGL: tariffs from Oct 2026", TARIF], ["BGL: PLA cards", PLA]]),
            P("mcgold", "Mastercard Gold", "The mid-tier credit card, €5.50 a month, offered against Visa Classic in the Confort and Exclusif packs; purchase protection and Mastercard's return-postage cover.",
              short="Mastercard Gold", s=["con", "xb"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard card."],
              mc="Where Mastercard competes card by card with Visa Classic inside the packs.",
              src=[["BGL: payment cards", CARDS], ["BGL: tariffs from Oct 2026", TARIF]]),
            P("mcpremium", "Mastercard Platinum & Elite", "Platinum (€17 a month, half price in Exclusif) with travel insurance and Priority Pass; Elite (€28 a month) with a 24/7 concierge, Priority Pass to 1,300+ lounges and a 24-month extended warranty; Elite terms from July 2022. Not branded World Elite on the site ⚠.",
              short="Platinum & Elite (Mastercard)", s=["hnw"], lc="borrow", ay="Jul 2022", o="P", at="Mastercard, Europ Assistance", neo=[2, "Mastercard cards."],
              mc="Mastercard owns BGL's premium tier.",
              src=[["BGL: Mastercard Elite", ELITE], ["BGL: payment cards", CARDS], ["BGL: tariffs from Oct 2026", TARIF]]),
        ]},
        {"id": "2.3", "ic": "briefcase", "name": "Business cards", "blurb": "Visa Business only.", "div": "ent", "rev": "rcb", "products": [
            P("visabusiness", "Visa Business", "A deferred-debit card for professionals and companies of every size, with a default €2,500 monthly limit, employee cards for costs such as fuel and travel insurance; terms from April 2022. No Mastercard business card is offered on the site.",
              short="Visa Business (Visa)", s=["pro", "corp"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."],
              mc="The commercial-card gap: one Visa product and no virtual cards.",
              src=[["BGL: Visa Business", VBIZ]]),
        ]},
        {"id": "2.4", "ic": "smartphone", "name": "Wallets", "blurb": "Apple Pay first, 2019.", "div": "retail", "rev": "rcb", "products": [
            P("applepay", "Apple Pay", "Launched 21 May 2019 for V PAY, Visa and Mastercard cards, the first in Luxembourg; Spuerkeess followed that November.",
              s=["con", "xb"], lc="everyday", ay="May 2019", o="P", at="Apple", neo=[1, "Visa and Mastercard cards."],
              src=[["BGL: Apple Pay, May 2019", AP19]]),
            P("wearables", "Garmin Pay & Fitbit Pay", "Payment by watch for BGL cards; Google Pay is not listed on BGL's consumer pages ⚠.",
              s=["con"], lc="everyday", o="P", at="Garmin, Fitbit", neo=[1, "Visa and Mastercard cards."],
              src=[["BGL: mobile payments", MOBILE], ["BGL: Visa Debit", VDEBIT]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Wero & instant", "blurb": "Payconiq off 30 Sep 2026.", "div": "retail", "rev": "rcb", "products": [
            P("wero", "Wero", "BGL joined EPI with Spuerkeess, BIL, POST and Raiffeisen on 16 June 2025, with LUXHUB as technical partner; payments by phone number, e-mail or QR in under 10 seconds, across Luxembourg, Belgium, France and Germany.",
              s=["con", "xb"], lc="move", st="new", ay="Jun 2025", o="P", at="EPI, LUXHUB", neo=[0, "EPI account-to-account."],
              mc="Wero plans in-store and online payments next, where cards compete.",
              src=[["BGL/EPI: Wero in Luxembourg, Jun 2025", WERO25], ["BGL: mobile payments", MOBILE]]),
            P("payconiq", "Payconiq", "Switched off at BGL on 30 September 2026 in favour of Wero (EPI bought Payconiq in 2023); business QR codes stay valid until the end of 2026.",
              s=["con"], lc="move", st="retired", o="P", at="EPI", neo=[0, "Account-to-account."],
              src=[["BGL: mobile payments", MOBILE], ["BGL: Wero for business", WEROPRO]]),
            P("instant", "Instant transfers", "Transfers in seconds from the app, including to other banks.",
              s=["con", "pro"], lc="move", neo=[0, "SEPA Instant."], src=[["BGL: innovative solutions", INNOV]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Acceptance", "blurb": "Axepta and Wero for merchants.", "div": "ent", "rev": "rcb", "products": [
            P("axepta", "Axepta terminals & e-commerce", "Terminals and online checkout from the group's Axepta BNP Paribas, accepting Bancontact, Visa, Mastercard, Amex, Apple Pay and Google Pay; three plans, next-day settlement and 5–15% off for professional packs.",
              s=["pro"], lc="move", o="P", at="Axepta BNP Paribas", neo=[1, "Accepts every network."],
              src=[["BGL: payment terminals", TPE]]),
            P("weropro", "Wero for business", "Payment requests and QR codes with no terminal, and an e-commerce module, replacing Payconiq.",
              s=["pro"], lc="move", st="new", o="P", at="EPI", neo=[0, "Account-to-account."],
              src=[["BGL: Wero for business", WEROPRO]]),
        ]},
        {"id": "2.7", "ic": "building", "name": "Cash", "blurb": "Bancomat, shared by six.", "div": "bgl", "rev": "rcb", "products": [
            P("bancomat", "Bancomat shared ATMs", "A common ATM network with Spuerkeess, BIL, Raiffeisen, POST and ING Luxembourg, announced November 2023: recycling machines and 30% less energy; still being rolled out in 2025.",
              s=["con"], lc="everyday", st="flux", ay="Nov 2023", o="P", at="Bancomat", neo=[0, ""],
              src=[["BGL et al: Bancomat, Nov 2023", BANCOMAT], ["BGL: 2025 results, Apr 2026", RES25]]),
            P("globalnet", "Group ATM network", "Free euro withdrawals in the BNP Paribas Global Network and Global Alliance, Deutsche Bank among them.",
              s=["xb"], lc="everyday", o="P", at="BNP Paribas Global Network", neo=[0, ""],
              src=[["BGL: Visa Debit", VDEBIT], ["BGL: tariffs from Oct 2026", TARIF]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: 3D Secure and card controls, card benefits including Mastercard's return-postage cover, the Genius assistant and account aggregation, and a shared KYC utility.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Security", "blurb": "3D Secure, card lock.", "div": "bgl", "rev": "rcb", "products": [
            P("threeds", "3D Secure", "Online card payments secured by 3D Secure on every BGL debit and credit card.",
              s=["con"], lc="everyday", neo=[1, "Visa and Mastercard schemes."], src=[["BGL: mobile payments", MOBILE]]),
            P("cardcontrol", "Card lock & PIN in the app", "Lock and unlock a card instantly, view the PIN in Web Banking; fraud and cyber-attack guidance for businesses.",
              s=["con", "pro"], lc="everyday", neo=[0, ""], src=[["BGL: innovative solutions", INNOV], ["BGL: Visa Debit", VDEBIT], ["BGL: businesses", ENT]]),
        ]},
        {"id": "3.2", "ic": "gift", "name": "Card benefits", "blurb": "Mastercard's return cover.", "div": "retail", "rev": "rcb", "products": [
            P("retour", "Mastercard return-postage cover", "Return shipping refunded up to €30 a claim, three claims a year, for Gold, Platinum and Elite holders in Belgium and Luxembourg; terms set by Mastercard.",
              s=["con", "hnw"], lc="everyday", o="P", at="Mastercard", neo=[3, "Mastercard's own benefit."],
              mc="Mastercard's own service, already live at BGL.",
              src=[["BGL: Mastercard return cover", RETOUR]]),
            P("cardinsurance", "Card insurance & assistance", "Purchase protection on credit cards, online-purchase cover on Visa Debit, travel cover on Platinum, Elite and Visa Business; claims via SPB and Europ Assistance.",
              s=["con", "hnw"], lc="everyday", o="P", at="SPB, Europ Assistance", neo=[1, "On Visa and Mastercard cards."],
              src=[["BGL: payment cards", CARDS], ["BGL: Mastercard Elite", ELITE], ["BGL: Visa Business", VBIZ]]),
        ]},
        {"id": "3.3", "ic": "bot", "name": "Assistant & data", "blurb": "Genius chatbot.", "div": "retail", "rev": "rcb", "products": [
            P("genius", "Genius", "A digital assistant with budget advice, alerts and recommendations; a conversational chatbot was added in 2025.",
              s=["con"], lc="everyday", st="new", neo=[0, ""],
              mc="An assistant that could one day pay: Agent Pay is untouched ground.",
              src=[["BGL: innovative solutions", INNOV], ["BGL: 2025 results, Apr 2026", RES25]]),
            P("aggregator", "Account aggregator", "Balances and transactions from other banks shown in the BGL app.",
              s=["con"], lc="everyday", neo=[None, "Provider not named."], src=[["BGL: innovative solutions", INNOV]]),
        ]},
        {"id": "3.4", "ic": "fingerprint", "name": "KYC utility", "blurb": "i-Hub, shared.", "div": "bgl", "rev": "cc", "products": [
            P("ihub", "i-Hub KYC platform", "A shared Know Your Customer platform for the Luxembourg financial centre, operational for BGL in 2025.",
              s=["corp"], lc="open", st="new", o="P", at="i-Hub", neo=[0, ""], src=[["BGL: 2025 results, Apr 2026", RES25]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: current-account packs and home loans, private banking, corporate and professional banking, international leasing, and Cardif life insurance.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Retail banking", "blurb": "Four packs, home loans.", "div": "retail", "rev": "rcb", "products": [
            P("packs", "Current-account packs", "Jeunes (free), Essentiel (€4 a month), Confort (€9) and Exclusif (€12) from 1 October 2026, each with Visa Debit and a choice of Visa or Mastercard credit card above Essentiel.",
              s=["con", "xb"], lc="open", neo=[1, "Visa debit; Visa or Mastercard credit."],
              src=[["BGL: tariffs from Oct 2026", TARIF]]),
            P("homeloans", "Home & renovation loans", "Mortgages (fixed €250 fee with Exclusif or under 30), renovation loans and co-ownership energy-renovation loans.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["BGL: tariffs from Oct 2026", TARIF], ["BGL: businesses", ENT]]),
            P("loans", "Personal, car & student loans", "Consumer loans, with student loans applied for entirely in the app.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["BGL: innovative solutions", INNOV]]),
        ]},
        {"id": "4.2", "ic": "gem", "name": "Private banking", "blurb": "AuM +8% in 2025.", "div": "private", "rev": "wm", "products": [
            P("privatebank", "Banque Privée", "Assets under management of target clients up 8% and loans up 12% in 2025; Euromoney's Best Bank for UHNW in Luxembourg 2026; Royal Roosevelt House opened June 2026.",
              s=["hnw"], lc="grow", st="new", neo=[0, ""],
              mc="Premium Mastercard cards and benefits fit this client base.",
              src=[["BGL: 2025 results, Apr 2026", RES25], ["BGL: press releases", PRESS]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Corporate & professional", "blurb": "Revenue +7% with retail.", "div": "ent", "rev": "rcb", "products": [
            P("corporates", "Corporate & professional banking", "Accounts, investment loans, credit lines, cash management, trade finance and asset finance for start-ups, SMEs, large companies, the public sector and associations; retail and corporate revenue up 7% in 2025, deposits up 6%.",
              s=["pro", "corp"], lc="everyday", neo=[0, "Visa Business."], src=[["BGL: businesses", ENT], ["BGL: 2025 results, Apr 2026", RES25]]),
        ]},
        {"id": "4.4", "ic": "factory", "name": "Leasing International", "blurb": "Revenue +8%.", "div": "leasing", "rev": "lease", "products": [
            P("leasing", "BNP Paribas Leasing Solutions", "Equipment leasing across Europe and Türkiye, in which BGL took 50% plus one share in 2012 ⚠ current stake; revenue up 8% in 2025, cost of risk 62 bp.",
              s=["corp"], lc="borrow", o="A", neo=[0, ""], src=[["BGL: 2025 results, Apr 2026", RES25], ["Paperjam: 2012 results", LEASE12]]),
        ]},
        {"id": "4.5", "ic": "coins", "name": "Insurance & investing", "blurb": "Cardif Lux Vie.", "div": "cardif", "rev": "rcb", "products": [
            P("lifeins", "Life insurance", "OptiPension+, OptiSave+, OptiLib and OptiLife², designed by Cardif Lux Vie and sold by BGL's insurance agency.",
              s=["con", "hnw"], lc="grow", o="P", at="Cardif Lux Vie", neo=[0, ""], src=[["BGL: life insurance", LIFE]]),
            P("directinvest", "Direct Invest Clic", "Programmed regular investing from the Web Banking app.",
              s=["con"], lc="grow", st="new", neo=[0, ""], src=[["BGL: innovative solutions", INNOV]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: the Web Banking app, now the only channel for two-thirds of its users, 22 branches, My Business Banking, and clients referred by ING.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Web Banking app", "blurb": "Two-thirds mobile only.", "div": "retail", "rev": "rcb", "products": [
            P("app", "Web Banking app", "Usage up 12 points in 2025, with more than two-thirds of users on mobile only and most retail products available online.",
              s=["con", "xb"], lc="everyday", neo=[0, ""], src=[["BGL: 2025 results, Apr 2026", RES25]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches", "blurb": "22 branches.", "div": "retail", "rev": "rcb", "products": [
            P("branches", "Branches", "22 branches across Luxembourg, with a remote-advice model that raised reachability in 2025.",
              s=["con", "home"], lc="open", neo=[0, ""], src=[["BGL: the bank", KNOW], ["BGL: 2025 results, Apr 2026", RES25]]),
        ]},
        {"id": "5.3", "ic": "monitor", "name": "My Business Banking", "blurb": "For legal entities.", "div": "ent", "rev": "rcb", "products": [
            P("mbb", "My Business Banking", "A digital platform for companies to manage payments, direct debits, contracts and documents; its scope is being widened.",
              s=["pro", "corp"], lc="everyday", st="new", neo=[0, ""],
              mc="Where spend controls and virtual cards could sit.",
              src=[["BGL: businesses", ENT], ["BGL: 2025 results, Apr 2026", RES25]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Partners", "blurb": "18,000 from ING.", "div": "bgl", "rev": "rcb", "products": [
            P("ingref", "ING referral", "About 18,000 ING Luxembourg everyday-banking clients referred to BGL from December 2024 to summer 2025, as ING left mass retail.",
              s=["con"], lc="open", ay="Dec 2024", o="P", at="ING Luxembourg", neo=[0, ""], src=[["ING and BGL: referral, Dec 2024", ING]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at BGL", "blurb": "Premium credit; Visa debit.", "products": [
        P("mcatbgl", "Mastercard at BGL", "Visa carries BGL's debit (Visa Debit since November 2020), entry credit and business cards. Mastercard carries the Gold, Platinum and Elite credit cards, its return-postage cover, and Mastercard credentials in Apple Pay since 2019. No network agreement or joint Mastercard initiative has been announced.",
          s=["con"], div="bgl", rev="cc", mc="The relationship this map is drawn for.",
          src=[["BGL: payment cards", CARDS], ["BGL and Visa: Visa Debit, Nov 2020", VD20], ["BGL: Mastercard return cover", RETOUR]]),
    ]},
    {"id": "pillar-market", "name": "Luxembourg banking", "blurb": "Wero, Bancomat, cross-border.", "products": [
        P("market", "The Luxembourg market", "Spuerkeess, BIL, Raiffeisen and POST are the main domestic rivals; ING left mass retail in 2024–25. Banks share ATMs (Bancomat) and moved from Payconiq to Wero in 2025–26. Nearly half the workforce crosses a border each day. Spuerkeess and POST also issue Mastercard credit cards ⚠.",
          s=["con"], div="bgl", rev="cc", src=[["BGL/EPI: Wero in Luxembourg, Jun 2025", WERO25], ["BGL et al: Bancomat, Nov 2023", BANCOMAT], ["Giraffy: Luxembourg credit cards ⚠", GIRAFFY]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
