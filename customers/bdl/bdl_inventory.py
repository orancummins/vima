"""Banque de Développement Local's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the H1 2026 COSOB report (October 2026), the
2025 annual report (June 2026) and BDL's product pages, in French. ``neo`` is the Mastercard lens:
[depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

AR25 = "https://www.bdl.dz/wp-content/uploads/2026/06/rapport-annuel-2025.pdf"
H126 = "https://www.bdl.dz/wp-content/uploads/2026/10/Rapport-semestriel-COSOB-Juin-2026-FR.pdf"
CAPITAL = "https://www.bdl.dz/ouverture-du-capital/"
AGO26 = "https://www.bdl.dz/wp-content/uploads/2026/07/Resolution-AGO-2026-Fr.pdf"
AGEX = "https://www.bdl.dz/wp-content/uploads/2026/08/Resolutions-AGEX.pdf"
HOME = "https://www.bdl.dz/"
MC = "https://www.bdl.dz/mastercard/"
VISA = "https://www.bdl.dz/carte-visa/"
CIB = "https://www.bdl.dz/carte-cib/"
CORP = "https://www.bdl.dz/carte-corporate/"
ECOMINT = "https://www.bdl.dz/ecommerce-international/"
CNAS = "https://www.bdl.dz/ecommerce-international-cnas/"
PROMO = "https://www.bdl.dz/promo-cartes-internationales/"
ALLOC = "https://www.bdl.dz/allocation-touristique/"
WIMPAY = "https://www.bdl.dz/wimpay/"
DIGIT = "https://www.bdl.dz/digitbdl/"
TPE = "https://www.bdl.dz/tpe/"
EPAY = "https://www.bdl.dz/e-paiement/"
WEBM = "https://www.bdl.dz/webmarchand/"
EBANK = "https://www.bdl.dz/ebanking/"
ONLINE = "https://www.bdl.dz/banque-en-ligne/"
ISLAMIC = "https://www.bdl.dz/finance-islamique/"
PSG = "https://www.bdl.dz/psg/"
BDC = "https://www.bdl.dz/bdc/"
VFS = "https://www.bdl.dz/vfs-global/"
PHARMA = "https://www.bdl.dz/pharmaciens/"
CONFORT = "https://www.bdl.dz/credit-confort/"
ASSUR = "https://www.bdl.dz/assurance/"
SATIMPOST = "https://www.bdl.dz/partenariat/"
SATIMECO = "https://algerie-eco.com/?p=182690"
IPO = "https://www.bdl.dz/la-banque-de-developpement-local-bdl-entre-en-bourse-une-nouvelle-ere-pour-leconomie-algerienne/"
IPOLAUNCH = "https://www.bdl.dz/lancement-de-la-vente-des-actions/"
ECOMLAUNCH = "https://www.bdl.dz/la-bdl-lance-un-nouveau-service-inedit-e-commerce-a-linternational/"
CNASCONV = "https://www.bdl.dz/signature-de-la-convention-entre-la-bdl-et-la-cnas-un-service-innovant-pour-la-diaspora-algerienne/"
RASSEMBLEMENT = "https://www.bdl.dz/rassemblement-national-2025-une-mobilisation-strategique-de-toutes-les-forces-du-reseau-bdl/"
MC2018 = "https://www.algerie360.com/avec-sa-mastercard-et-le-compte-el-amane-la-bdl-elargit-sa-panoplie-de-produits/"
MCINBOUND = "https://news.radioalgerie.dz/fr/node/75683"
TSAVISA = "https://www.tsa-algerie.com/?p=270580"
TSAPROMO = "https://www.tsa-algerie.com/allocation-touristique-la-bdl-casse-les-prix-de-ses-cartes-visa-et-mastercard/"
PLANS26 = "https://algerie-eco.com/2025/12/25/bdl-prevoit-de-renforcer-ses-services-numeriques-et-son-reseau-commercial-en-2026/"
PDG = "https://algerie-eco.com/?p=321152"
AGOECO = "https://algerie-eco.com/?p=326967"
WAIT = "https://maghrebemergent.news/fr/carte-visa-ou-mastercard-en-algerie-la-longue-attente-des-clients-se-poursuit/"
GIE = "https://giemonetique.dz/qui-sommes-nous/chiffres/"
GIEABOUT = "https://giemonetique.dz/qui-sommes-nous/gie-monetique/"
EPAY25 = "https://algerie-eco.com/?p=236056"
DZMOB = "https://algerie-eco.com/?p=231514"
CASHLESS = "https://algerie-eco.com/2025/10/17/gouverneur-de-la-banque-dalgerie-lobjectif-est-darriver-a-des-transactions-sans-argent-liquide-a-lhorizon-2028/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · listing · state", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: DA 2.4 trillion of assets and a record half-year profit, a 2025 listing that put 30% of the bank on the Algiers Stock Exchange, a new chairman and CEO, stakes in SATIM and 26 other bodies, and a new core system.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "DA 22bn profit in H1 2026.", "div": "bdl", "rev": "central", "products": [
            P("balance", "Balance sheet & earnings", "Total assets of DA 2,380.7 billion, customer deposits of DA 1,900.2 billion and net customer loans of DA 1,127.6 billion at 30 June 2026; net banking income DA 45.2 billion (+49.7%) and net profit DA 22.3 billion (+66.3%) in the half; capital adequacy 15.2%, cost-income 19.9%. 2025: net profit DA 27.3 billion. No public credit rating ⚠.",
              s=["inv"], neo=[0, ""], src=[["BDL: H1 2026 COSOB report", H126], ["BDL: annual report 2025", AR25]]),
            P("commitments", "Loans & commitments", "Customer commitments of DA 2,481 billion (+17%), including signature commitments, of which investment credit DA 1,019 billion; cost of funds down to 1.79%; revenue split 48% private sector, 46% public sector, 6% households ⚠ headline credit figures include off-balance-sheet items.",
              s=["corp"], neo=[0, ""], src=[["BDL: H1 2026 COSOB report", H126], ["BDL: capital page", CAPITAL]]),
        ]},
        {"id": "1.2", "ic": "chart-candlestick", "name": "Listing & owners", "blurb": "30% floated in March 2025.", "div": "bdl", "rev": "central", "products": [
            P("ipo", "Initial public offering", "44.2 million new shares at DA 1,400, sold from 20 January to 20 February 2025, 21.7% oversubscribed and raising DA 61.88 billion; 79% of demand from individuals. Listed on the main market on 13 March 2025, the second public bank after CPA.",
              s=["inv"], ay="Mar 2025", o="B", neo=[0, ""], src=[["BDL: IPO, Mar 2025", IPO], ["BDL: share sale launched, Jan 2025", IPOLAUNCH]]),
            P("owners", "Ownership & dividends", "The Treasury holds 70% and the market 30%; 11,583 registered shareholders; market value DA 207.8 billion at DA 1,410 a share (30 June 2026). Dividend of DA 15.77 billion on 2025 profits, and a share buy-back authorised in June 2026.",
              s=["inv"], neo=[0, ""], src=[["BDL: annual report 2025", AR25], ["BDL: AGM resolutions, Jun 2026", AGO26]]),
        ]},
        {"id": "1.3", "ic": "scale", "name": "Leadership", "blurb": "Ferfera, chairman and CEO.", "div": "bdl", "rev": "central", "products": [
            P("leadership", "Chairman & CEO and board", "Mustapha Ferfera was named chairman and CEO by the board on 23 July 2026; Mohamed Mebarek, previously acting director general, is deputy director general. The board includes State, independent, staff and two newly elected minority-shareholder directors.",
              s=["inv"], ay="Jul 2026", st="new", neo=[0, ""], src=[["Algérie Eco: new chairman and CEO, Aug 2026", PDG], ["BDL: AGM resolutions, Jun 2026", AGO26]]),
            P("governance", "Single-head governance", "A meeting on 7 September 2026 replaced the separate chair and director general with one chairman and CEO, named Ferfera to the board for the Ministry of Finance, and appointed a new auditor after a banking-commission objection.",
              s=["inv"], st="flux", ay="Sep 2026", neo=[0, ""], src=[["BDL: AGEX resolutions, 2026", AGEX], ["Algérie Eco: AGM, Sep 2026", AGOECO]]),
        ]},
        {"id": "1.4", "ic": "network", "name": "Heritage & stakes", "blurb": "Since 1985; 14.7% of SATIM.", "div": "satim", "rev": "central", "products": [
            P("heritage", "Heritage & capital", "Created on 30 April 1985 as a public bank; capital raised in steps from DA 500 million (1989) to DA 147.4 billion (2025); 4,685 staff at end-2025.",
              s=["inv"], o="I", neo=[0, ""], src=[["BDL: annual report 2025", AR25]]),
            P("stakes", "Subsidiaries & stakes", "One subsidiary and 27 stakes worth DA 10.7 billion: FINALEP (66%), the national leasing company SNL (50%), SATIM, the interbank card processor (14.7%), the clearing centre CPI (5.75%), the stock exchange operator (16.3%), insurers SAPS and El Djazair Takaful, and state guarantee funds.",
              s=["corp"], o="I", neo=[0, ""], src=[["BDL: H1 2026 COSOB report", H126], ["BDL: annual report 2025", AR25]]),
        ]},
        {"id": "1.5", "ic": "database", "name": "Technology & strategy", "blurb": "A new core system.", "div": "bdl", "rev": "central", "products": [
            P("tech", "Core system & payment standards", "A contract with EADN for a new information system (SI-NASR) signed in H1 2026 ⚠, ISO 20022 started on the ARTS real-time gross settlement system, and Microsoft Teams cleared by the data-protection authority. No public AI work ⚠.",
              s=["corp"], st="new", o="P", at="EADN", neo=[0, ""], src=[["BDL: H1 2026 COSOB report", H126], ["BDL: annual report 2025", AR25]]),
            P("strategy", "Strategy", "Seven axes: branches and digital relationship, deposits and own funds, more lending to private companies, bancassurance, service, digital transformation and cyber-security, and value for shareholders. Revenue growth of about 8% a year projected for 2026–27; more branches in the far south in 2026.",
              s=["inv"], neo=[0, ""], src=[["BDL: annual report 2025", AR25], ["Algérie Eco: 2026 plans, Dec 2025", PLANS26]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: CIB debit and corporate cards at home, Mastercard and Visa cards on foreign-currency accounts that now carry the €750 travel allowance, 17,000 terminals and web merchants on CIB, cross-border e-commerce acquiring on Visa and Mastercard, WIMPAY on the DZ Mob Pay network, and SATIM's local processing of Mastercard.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "CIB cards", "blurb": "The everyday card is domestic.", "div": "bdl", "rev": "menages", "products": [
            P("cib", "CIB Classique & Gold", "Interbank debit cards for payments at bank and Algérie Poste terminals, online payments and ATMs across Algeria; weekly limits of DA 150,000 (Classique) and DA 300,000 (Gold); free, valid four years; special online ceilings for AADL 3 housing instalments and Hajj fees.", short="CIB debit (domestic)",
              s=["con", "trav"], lc="everyday", o="P", at="GIE Monétique", neo=[0, "CIB, the domestic scheme."],
              mc="The card most BDL customers carry has no Mastercard role.",
              src=[["BDL: CIB card", CIB]]),
            P("corpcard", "Carte Corporate Silver & Gold", "A CIB-standard company card for staff expenses, payments and withdrawals in Algeria, with monthly payment ceilings of DA 500,000 (Silver) and DA 20 million (Gold).", short="Corporate card (CIB)",
              s=["pro", "corp"], lc="everyday", o="P", at="GIE Monétique", neo=[0, "CIB, the domestic scheme."],
              mc="No international commercial card: room for a Mastercard corporate or travel card.",
              src=[["BDL: Corporate card", CORP]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "International cards", "blurb": "Mastercard since 2018, Visa too.", "div": "bdl", "rev": "menages", "products": [
            P("mastercard", "Mastercard Titanium & Platinum", "International cards on a foreign-currency account since July 2018: contactless and 3-D Secure, weekly payment ceilings of €5,000 (Titanium) and €8,000 (Platinum), DA 8,000 and DA 14,000 for three years under an August 2026 offer.", short="Mastercard (international)",
              s=["trav"], lc="move", ay="Jul 2018", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="BDL's own Mastercard programme, one of two international ranges.",
              src=[["BDL: Mastercard", MC], ["Algérie360: BDL Mastercard launch, Jul 2018", MC2018], ["BDL: cards at -50%", PROMO]]),
            P("visa", "Visa Classique & Gold", "International cards on a foreign-currency account: weekly ceilings of €500 (Classique) and €5,000 (Gold), DA 3,000 and DA 5,000; launched about 2024 ⚠ date unconfirmed.", short="Visa (international)",
              s=["trav"], lc="move", ay="2024 ⚠", o="P", at="Visa", neo=[0, "Visa."],
              src=[["BDL: Visa card", VISA], ["BDL: Rassemblement National, Jun 2025", RASSEMBLEMENT]]),
            P("allowance", "Travel allowance on a card", "From 19 July 2026 the yearly €750 allowance (€300 for ages 12–18) is paid only onto a named international card; BDL loads it onto its Visa or Mastercard and cut card fees by half. Across banks, customers report waits of months for a card.", short="€750 allowance (Visa or Mastercard)",
              s=["trav"], lc="move", st="new", ay="Jul 2026", neo=[1, "Visa or Mastercard, the customer's choice."],
              mc="A regulatory push that sends every Algerian traveller to an international card.",
              src=[["BDL: droit de change", ALLOC], ["TSA: BDL cuts card prices, Aug 2026", TSAPROMO], ["Maghreb Émergent: card waits, Oct 2026", WAIT]]),
        ]},
        {"id": "2.3", "ic": "store", "name": "Acceptance at home", "blurb": "17,000 terminals on CIB.", "div": "bdl", "rev": "prive", "products": [
            P("tpe", "Card terminals (TPE)", "17,246 terminals at 30 June 2026 (+73%), about 15% of Algeria's 116,315; they accept CIB and Algérie Poste's EDAHABIA cards; management moved to branches in 2026. Foreign-card acceptance is not stated ⚠.", short="TPE (CIB, EDAHABIA)",
              s=["pro"], lc="move", o="P", at="GIE Monétique", neo=[0, "CIB and EDAHABIA."],
              mc="No Mastercard acceptance at BDL's terminals is public: visitors cannot pay there by card.",
              src=[["BDL: H1 2026 COSOB report", H126], ["BDL: TPE", TPE], ["GIE Monétique: figures", GIE]]),
            P("webmarchand", "Webmarchand", "Online acquiring for Algerian merchants of any bank's CIB card and EDAHABIA, through the interbank e-payment platform.", short="Web merchants (CIB)",
              s=["pro"], lc="move", o="P", at="GIE Monétique", neo=[0, "CIB and EDAHABIA."], src=[["BDL: Webmarchand", WEBM]]),
            P("epay", "e-Paiement", "CIB cardholders pay bills and buy online from Algérie Telecom, Air Algérie, Sonelgaz, Mobilis, Djezzy and others, confirmed by SMS one-time code; free.", short="CIB online payments",
              s=["con"], lc="everyday", neo=[0, "CIB."], src=[["BDL: e-Paiement", EPAY]]),
        ]},
        {"id": "2.4", "ic": "earth", "name": "Cross-border e-commerce", "blurb": "Visa, then Mastercard.", "div": "bdl", "rev": "prive", "products": [
            P("ecomint", "E-commerce international", "Algerian e-merchants take Visa (May 2025, a first in Algeria; over €1 million by December 2025) and Mastercard (December 2025) payments from abroad: 5% per transaction, a DA 65,000 monthly pack with anti-fraud, DA 70,000 to join.", short="Cross-border acquiring (Visa, Mastercard)",
              s=["pro", "corp", "dias"], lc="move", st="new", ay="May 2025", o="P", at="Visa, Mastercard", neo=[1, "Visa and Mastercard."],
              mc="BDL acquires Mastercard online for exporters, the only Algerian bank to say so.",
              src=[["BDL: E-commerce international", ECOMINT], ["APS: Mastercard payments into Algeria, Dec 2025", MCINBOUND], ["TSA: Visa e-commerce, Jun 2025", TSAVISA]]),
            P("cnas", "CNAS contributions from abroad", "Under a May 2025 convention, Algerians abroad pay social-security contributions on the CNAS platform built by BDL, by Visa only so far; Mastercard is announced as coming soon.", short="CNAS (Visa; Mastercard planned)",
              s=["dias"], lc="move", st="new", ay="May 2025", o="P", at="CNAS, Visa", neo=[0, "Visa; Mastercard planned."],
              mc="A diaspora flow that still runs only on Visa.",
              src=[["BDL: CNAS payments", CNAS], ["BDL: CNAS convention, May 2025", CNASCONV]]),
        ]},
        {"id": "2.5", "ic": "smartphone", "name": "Mobile & transfers", "blurb": "WIMPAY on DZ Mob Pay.", "div": "wimpay", "rev": "menages", "products": [
            P("wimpay", "WIMPAY BDL", "QR payments and person-to-person transfers on the interbank DZ Mob Pay network (BDL among seven launch banks, January 2025), with payer and merchant apps; DA 20 to DA 1 million per payment, DA 5 a transaction for merchants.", short="WIMPAY (DZ Mob Pay)",
              s=["con", "pro"], lc="move", st="new", ay="Jan 2025", o="P", at="DZ Mob Pay, SATIM", neo=[0, "Domestic QR network."],
              src=[["BDL: WIMPAY", WIMPAY], ["Algérie Eco: DZ Mob Pay, Nov 2025", DZMOB]]),
            P("transfers", "Transfers", "Internal and interbank transfers in DigitBDL (external below DA 1 million), standing orders and bulk transfers; ISO 20022 on ARTS from 2026.",
              s=["con", "corp"], lc="move", neo=[0, "Domestic clearing."], src=[["BDL: DigitBDL", DIGIT], ["BDL: H1 2026 COSOB report", H126]]),
        ]},
        {"id": "2.6", "ic": "plug", "name": "Processing", "blurb": "Mastercard processed in Algeria.", "div": "satim", "rev": "central", "products": [
            P("satim", "Local Mastercard processing at SATIM", "A convention of 13 December 2023, signed by director general Youcef Lalmas and SATIM's Madjid Messaouden, backs SATIM's plan to process Algerian banks' Mastercard transactions in Algeria; BDL calls itself Mastercard principal member and sponsor of the project. Go-live not published ⚠.", short="SATIM processing (Mastercard)",
              s=["corp"], lc="move", ay="Dec 2023", o="P", at="SATIM, Mastercard", neo=[2, "Mastercard ⚠ status."],
              mc="BDL is Mastercard's sponsor bank for domestic processing in Algeria.",
              src=[["BDL: BDL–Mastercard partnership, Dec 2023", SATIMPOST], ["Algérie Eco: BDL–SATIM convention, Dec 2023", SATIMECO]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: 3-D Secure and one-time codes, a risk map with 160 fixes in 2025, online account opening, and travel insurance, visa-fee collection and stakes in insurers. Nothing public on data, AI or open banking.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Security & risk", "blurb": "3-D Secure and OTP.", "div": "bdl", "rev": "central", "products": [
            P("secure", "3-D Secure & one-time codes", "3-D Secure on the Visa and Mastercard cards and on cross-border e-commerce; SMS one-time codes on CIB online payments; a one-time code as second factor in DigitBDL.", short="3-D Secure & OTP",
              s=["con", "trav"], lc="everyday", neo=[1, "3-D Secure on the international cards."],
              mc="Authentication and fraud tools for exporters are an opening.",
              src=[["BDL: Mastercard", MC], ["BDL: e-Paiement", EPAY], ["BDL: DigitBDL", DIGIT]]),
            P("risk", "Risk map & controls", "A risk map since 2022, revised in 2025 with payments and Islamic finance among focus areas; 160 action plans closed and 71 opened; COBIT and Basel alignment.",
              s=["inv"], neo=[0, ""], src=[["BDL: annual report 2025", AR25]]),
        ]},
        {"id": "3.2", "ic": "fingerprint", "name": "Onboarding", "blurb": "Accounts opened online.", "div": "bdl", "rev": "menages", "products": [
            P("onlineacct", "Online account opening", "Cheque, savings and foreign-currency accounts opened online with documents uploaded and a branch appointment, for anyone 19 or over; 79,918 accounts opened in 2025.",
              s=["con", "trav"], lc="open", neo=[0, ""], src=[["BDL: open an account online", ONLINE], ["BDL: annual report 2025", AR25]]),
        ]},
        {"id": "3.3", "ic": "plane", "name": "Travel services", "blurb": "Insurance and visa fees.", "div": "bdl", "rev": "menages", "products": [
            P("travelins", "Travel insurance", "Travel insurance sold in branches, with free travel cover cited for Mastercard holders.",
              s=["trav"], lc="beyond", neo=[0, ""], src=[["BDL: travel insurance", ASSUR], ["Algérie360: BDL Mastercard, Dec 2025", "https://www.algerie360.com/la-bdl-devoile-toutes-les-specificites-de-sa-carte-mastercard-internationale/"]]),
            P("vfs", "VFS Global fees", "79 branches collect France visa-appointment fees for VFS Global, since 2 September 2019.",
              s=["trav"], lc="beyond", ay="Sep 2019", o="P", at="VFS Global", neo=[0, ""], src=[["BDL: VFS Global", VFS]]),
        ]},
        {"id": "3.4", "ic": "hand-coins", "name": "Bancassurance", "blurb": "SAPS and Takaful stakes.", "div": "bdl", "rev": "menages", "products": [
            P("bancassur", "Bancassurance", "Stakes in the health and life insurer SAPS (15%) and El Djazair Takaful (6.67%); bancassurance and placements are a stated growth axis.",
              s=["con"], lc="grow", o="P", at="SAPS, El Djazair Takaful", neo=[0, ""], src=[["BDL: H1 2026 COSOB report", H126], ["BDL: annual report 2025", AR25]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: pawn loans, home and consumer credit, an Islamic window, loans for professionals and start-ups, DA 1 trillion of investment credit for companies and the public sector, trade finance, savings, and leasing through SNL.",
    "tiles": [
        {"id": "4.1", "ic": "coins", "name": "Household lending", "blurb": "Pawn loans and home loans.", "div": "bdl", "rev": "menages", "products": [
            P("psg", "Pawn loans (prêt sur gages)", "Loans against gold of up to DA 3 million at DA 15,000 a gram, for six to 36 months; relaunched in 2025, with revenue of DA 2.7 billion in 2025 and up 67% in H1 2026.",
              s=["con"], lc="borrow", o="I", neo=[0, ""], src=[["BDL: pawn loans", PSG], ["BDL: H1 2026 COSOB report", H126]]),
            P("homeloans", "Home loans", "Mortgage lending for households, with revenue of DA 3.45 billion in 2025; household credit reached DA 116.5 billion at 30 June 2026.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["BDL: annual report 2025", AR25], ["BDL: capital page", CAPITAL]]),
            P("confort", "Crédit Confort", "Consumer credit from DA 50,000 to DA 1.5 million over up to 60 months, only for goods made or assembled in Algeria.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["BDL: Crédit Confort", CONFORT]]),
        ]},
        {"id": "4.2", "ic": "gem", "name": "Islamic finance", "blurb": "Mourabaha and Ijara.", "div": "islamic", "rev": "menages", "products": [
            P("islamic", "BDL Finance Islamique", "Mourabaha for cars, household goods, investment and working capital, Ijara for homes and Moudaraba, overseen by a Sharia committee; Islamic credit revenue of DA 66 million in H1 2026.",
              s=["con", "pro"], lc="borrow", st="new", neo=[0, ""], src=[["BDL: Islamic finance", ISLAMIC], ["BDL: H1 2026 COSOB report", H126]]),
        ]},
        {"id": "4.3", "ic": "briefcase", "name": "Professionals & start-ups", "blurb": "State-backed micro loans.", "div": "bdl", "rev": "prive", "products": [
            P("pros", "Professional & start-up lending", "Loans backed by the ANADE, ANGEM and CNAC schemes, investment and working-capital credit, a bus-replacement loan and start-up finance.",
              s=["pro"], lc="borrow", neo=[0, ""], src=[["BDL: home page", HOME], ["BDL: annual report 2025", AR25]]),
            P("pharma", "Offer for pharmacists", "Financing, CIB terminals, preferential prices agreed with the pharmacists' union SNAPO and instant social-security reimbursements.",
              s=["pro"], lc="everyday", o="P", at="SNAPO", neo=[0, "CIB terminals."], src=[["BDL: pharmacists", PHARMA]]),
        ]},
        {"id": "4.4", "ic": "factory", "name": "Companies & public sector", "blurb": "DA 1trn investment credit.", "div": "bdl", "rev": "public", "products": [
            P("corplending", "Corporate & public lending", "Investment credit of DA 1,019 billion at 30 June 2026, real-estate and tourism promoters, and public companies, which brought 46% of H1 2026 revenue.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["BDL: capital page", CAPITAL], ["BDL: H1 2026 COSOB report", H126]]),
            P("trade", "Trade finance", "Imports, exports and pre-domiciliation; trade revenue of DA 1.3 billion in H1 2026, up 48%.",
              s=["corp"], lc="move", neo=[0, ""], src=[["BDL: H1 2026 COSOB report", H126]]),
        ]},
        {"id": "4.5", "ic": "trending-up", "name": "Savings & leasing", "blurb": "Bons de caisse, SNL.", "div": "snl", "rev": "central", "products": [
            P("savings", "Savings & placements", "Savings accounts with and without interest, bons de caisse paying 2% to 5%, term deposits and the El Amane package account with a CIB card.",
              s=["con", "inv"], lc="grow", neo=[0, ""], src=[["BDL: bons de caisse", BDC], ["Algérie360: El Amane, Jul 2018", MC2018]]),
            P("leasing", "Leasing & investment companies", "The national leasing company SNL (50%) and the investment company FINALEP (66%).",
              s=["corp"], lc="borrow", o="I", neo=[0, ""], src=[["BDL: H1 2026 COSOB report", H126]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach BDL: DigitBDL for 153,000 subscribers, an e-banking portal for companies, 185 branches, and public platforms from CNAS to Hajj fees.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "DigitBDL", "blurb": "153,000 subscribers.", "div": "digit", "rev": "menages", "products": [
            P("digit", "DigitBDL app", "152,754 subscribers at 30 June 2026 (+25%): balances, transfers, cheque tracking, card spending and salary-file signing for companies.",
              s=["con", "corp"], lc="everyday", neo=[0, ""], src=[["BDL: DigitBDL", DIGIT], ["BDL: H1 2026 COSOB report", H126]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "E-banking", "blurb": "Bulk transfers for firms.", "div": "bdl", "rev": "prive", "products": [
            P("ebank", "E-banking portal", "Accounts, single and bulk transfers, statements, SWIFT copies and cheque-book orders for individuals, professionals and companies.",
              s=["corp", "pro"], lc="everyday", neo=[0, ""], src=[["BDL: e-banking", EBANK]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches", "blurb": "185 branches.", "div": "bdl", "rev": "menages", "products": [
            P("branches", "Branches", "185 branches (August 2026), five opened and 11 self-service spaces added in 2025, with more planned in the far south in 2026.",
              s=["con", "pro"], lc="open", neo=[0, ""], src=[["TSA: BDL card prices, Aug 2026", TSAPROMO], ["BDL: annual report 2025", AR25]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Public platforms", "blurb": "CNAS, Djezzy, Hajj.", "div": "bdl", "rev": "public", "products": [
            P("partners", "Partner & public platforms", "CNAS for the diaspora, Djezzy for card payments from abroad, VFS Global, Hajj fees with the pilgrimage office, AADL 3 housing instalments and the Algiers Stock Exchange.",
              s=["dias", "con"], lc="open", o="P", at="CNAS, Djezzy, VFS Global", neo=[0, ""],
              src=[["BDL: CNAS payments", CNAS], ["TSA: Visa e-commerce, Jun 2025", TSAVISA], ["BDL: CIB card", CIB]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at BDL", "blurb": "Sponsor bank, small card book.", "products": [
        P("mcatbdl", "Mastercard at BDL", "BDL issues Mastercard Titanium and Platinum since 2018, acquires Mastercard for Algerian e-merchants selling abroad since December 2025, and sponsored SATIM's project to process Mastercard in Algeria (2023, status ⚠). Visa sits alongside on international cards and came first in cross-border acquiring and CNAS; everyday cards and terminals run on CIB.",
          s=["trav"], div="bdl", rev="central", mc="The relationship this map is drawn for.",
          src=[["BDL: BDL–Mastercard partnership, Dec 2023", SATIMPOST], ["APS: Mastercard payments into Algeria, Dec 2025", MCINBOUND]]),
    ]},
    {"id": "pillar-market", "name": "Algerian payments", "blurb": "CIB, EDAHABIA, cashless by 2028.", "products": [
        P("market", "The Algerian market", "23.3 million CIB and EDAHABIA cards, 116,315 terminals and 4,960 ATMs (July 2026) under GIE Monétique; DA 939 billion of e-payments in 2025 (+46%); DZ Mob Pay for interbank QR; a cashless target for 2028; and the €750 travel allowance moved onto international cards in July 2026.",
          s=["con"], div="bdl", rev="central",
          src=[["GIE Monétique: figures", GIE], ["GIE Monétique: about", GIEABOUT], ["Algérie Eco: e-payments 2025", EPAY25], ["Algérie Eco: cashless by 2028", CASHLESS]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
