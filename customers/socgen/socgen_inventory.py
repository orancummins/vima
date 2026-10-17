"""Société Générale's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the Q2 2026 results (30 July 2026), the Capital
Markets Day (21 September 2026) and the 2026 Universal Registration Document (13 March 2026). ``neo`` is the
Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard,
1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

PR2Q26 = "https://www.societegenerale.com/sites/default/files/resultats-publication/en/2026-07/q2-2026-press-release-en.pdf"
SL2Q26 = "https://www.societegenerale.com/sites/default/files/resultats-publication/en/2026-07/q2-2026-financial-results-presentation.pdf"
CMDPR = "https://www.societegenerale.com/sites/default/files/documents/2026-09/capital-markets-day-press-release.pdf"
CMD = "https://www.societegenerale.com/sites/default/files/documents/2026-09/capital-markets-day-presentation.pdf"
URD = "https://investors.societegenerale.com/sites/default/files/documents/2026-03/universal-registration-document-2026.pdf"
EXCO = "https://investors.societegenerale.com/en/strategy-governance/governance/executive-committee"
IR = "https://investors.societegenerale.com/en"
GRISONI = "https://www.societegenerale.com/en/news/press-release/appointment-benoit-grisoni"
PRLIST = "https://www.societegenerale.com/en/press-release"
SGCARDS = "https://particuliers.sg.fr/ouvrir-compte-bancaire-en-ligne/moyens-paiement"
CIRRUS = "https://particuliers.sg.fr/ouvrir-compte-bancaire-en-ligne/moyens-paiement/cartes-bancaires-mastercard/carte-retrait-cb-service-eclair-cirrus"
SGPRO = "https://professionnels.sg.fr/compte-banque-au-quotidien/simulateur-cartes"
SGCORP = "https://entreprises.sg.fr/au-quotidien/cartes-bancaires"
BANXUP = "https://particuliers.sg.fr/ouvrir-compte-bancaire-en-ligne/banxup"
MVOX25 = "https://www.moneyvox.fr/carte-bancaire/actualites/103690/societe-generale-ces-deux-cartes-bancaires-ont-disparu"
MVOXCB = "https://www.moneyvox.fr/carte-bancaire/actualites/108113/le-reseau-francais-cb-reprend-du-terrain-a-visa-et-mastercard"
BOURSO = "https://www.boursobank.com/banque/carte-bancaire-gratuite-ultim"
BOURSOMETAL = "https://www.boursobank.com/banque/carte-bancaire-premium-metal"
BOURSOPRO = "https://www.boursobank.com/professionnels/carte-bancaire-professionnelle"
BOURSOENC = "https://www.boursobank.com/professionnels/solutions-encaissement"
BOURSOWERO = "https://epicompany.eu/media-insights/boursobank-integrates-wero-into-its-payment-solutions"
WEROFR = "https://societegenerale.com/sites/default/files/documents/2024-09/cp-epi-lance-wero-en-france.pdf"
WERO1Y = "https://www.societegenerale.com/sites/default/files/documents/2025-09/cp-wero-1-an-vf.pdf"
LOL = "https://www.electronicpaymentsinternational.com/news/societe-generale-mastercard/"
TREEZOR = "https://www.treezor.com/shares-completes-the-acquisition-of-treezor/"
KBCARDS = "https://www.kb.cz/cs/obcane/karty"
KBWE = "https://www.kb.cz/cs/o-bance/tiskove-zpravy/tiskove-zpravy-2021/komercni-banka-rozsiruje-nabidku-karet-o-exkluzivni-mastercard-world-elite"
KBVIRT = "https://www.kb.cz/cs/o-bance/tiskove-zpravy/komercni-banka-nabizi-v-kb-virtualni-kartu-pro-jednotlivce-i-firmy"
BRDDEBIT = "https://www.brd.ro/persoane-fizice/carduri-si-conturi/carduri/carduri-de-debit"
BRDGOLD = "https://www.brd.ro/persoane-fizice/carduri-si-conturi/carduri/card-de-credit-gold"
BRDCC = "https://www.brd.ro/card-de-credit-brd"
HANSEATIC = "https://www.hanseaticbank.de/kreditkarte"
FIDITALIA = "https://www.fiditalia.it/carte/carta-bianca"
SGFORGE = "https://www.sgforge.com/"
PAYXPERT = "https://www.payxpert.com/"
MAAP = "https://www.mastercard.com/us/en/news-and-trends/press/2025/april/mastercard-unveils-agent-pay-pioneering-agentic-payments-technology-to-power-commerce-in-the-age-of-ai.html"
ROSHARE = "https://www.romania-insider.com/banca-transilvania-largest-market-share-assets-june-2026"
VISA23 = "https://www.finance.cz/aktuality/ceska-sporitelna-karty-visa/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · heritage · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: €476 billion of loans and CET1 of 13.2% at 30 June 2026, a bank founded in 1864, an AI agreement with Anthropic, and a 2029 roadmap presented on 21 September 2026.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "€27bn revenue, €6bn profit.", "div": "group", "rev": "corp", "products": [
            P("balance", "Balance sheet & earnings", "Revenues of €27.3 billion and Group net income of €6.0 billion in 2025 (ROTE 10.2%); a record €1.79 billion in Q2 2026 and €3.49 billion in the first half (ROTE 12.0%); loans of €476 billion, deposits of €626 billion and CET1 of 13.2% at 30 June 2026; rated A+ by Fitch, A1 by Moody's and A by S&P (outlook positive); market value €52.7 billion at end-2025 ⚠ no October 2026 figure.",
              s=["con", "corp"], neo=[0, ""], src=[["Q2 2026 results", PR2Q26], ["2026 URD", URD], ["SG investors", IR]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership & heritage", "blurb": "Krupa and Connelly; since 1864.", "div": "group", "rev": "corp", "products": [
            P("leadership", "Board & executive committee", "Chair William Connelly (from the May 2026 AGM), CEO Slawomir Krupa, Deputy CEO Pierre Palmieri, Alexis Kohler (investment banking, general secretariat), Lubomira Rochet (French retail, private banking, insurance and the Group's operations), CFO Leopoldo Alvear and Cécile Bartenieff (mobility and international retail); Benoit Grisoni of BoursoBank also runs individual and professional clients from 1 October 2026.",
              s=["corp"], neo=[0, ""], src=[["SG: Executive Committee", EXCO], ["Q2 2026 results", PR2Q26], ["SG: Grisoni appointment, Sep 2026", GRISONI]]),
            P("heritage", "Heritage", "Founded in 1864, nationalised in 1945 and privatised in June 1987; Boursorama and Crédit du Nord bought and later merged into the group's French model, Komerční banka a subsidiary since 2001 and BRD for about 25 years; about 110,000 staff serving 27 million clients in 58 countries.",
              s=["con"], o="I", neo=[0, ""], src=[["2026 URD", URD]]),
        ]},
        {"id": "1.3", "ic": "brain", "name": "Technology & AI", "blurb": "Anthropic, 12% IT intensity.", "div": "group", "rev": "corp", "products": [
            P("ai", "AI programme", "A strategic agreement with Anthropic announced at the Capital Markets Day: Claude models, coding tools and agentic capabilities rolled out across the group and tailored with SG; AI initiatives to save €500–600 million by 2029, about €350 million already identified; IT spending down about €0.5 billion to an IT intensity of 12%.",
              s=["corp"], st="new", ay="Sep 2026", o="P", at="Anthropic", neo=[0, ""],
              mc="Mastercard's Agent Pay (April 2025) has no SG mention; SG is now building agents with Anthropic.",
              src=[["SG: Capital Markets Day release", CMDPR], ["SG: Capital Markets Day slides", CMD], ["Mastercard: Agent Pay, Apr 2025", MAAP]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy 2029", "blurb": "ROTE 13–14% in 2029.", "div": "group", "rev": "corp", "products": [
            P("strategy", "2029 roadmap", "Costs about 2% below 2026 (under €16.3 billion in 2029), revenue growth about 3% a year, cost/income below 55% and ROTE of 13–14% in 2029 and above 15% from 2030, CET1 above 13%; growth in BoursoBank, wealth, selected investment-banking franchises, Eastern Europe and Ayvens; one integrated approach to French individual clients.",
              s=["corp"], st="new", ay="Sep 2026", neo=[0, ""], src=[["SG: Capital Markets Day release", CMDPR], ["Q2 2026 results", PR2Q26]]),
        ]},
        {"id": "1.5", "ic": "briefcase", "name": "Deals", "blurb": "15 disposals since 2023.", "div": "group", "rev": "corp", "products": [
            P("deals", "Deals 2022–26", "Rosbank sold (2022); LeasePlan bought to form Ayvens and a PayXpert stake (2023); Bernstein joint venture (2024); SG Equipment Finance to BPCE, private banks in London and Geneva to UBP and African subsidiaries sold (2025); an MoU with Crédit Mutuel Arkéa on the retail securities-services business (March 2026) and Treezor sold to Shares (completed 6 October 2026); 15 disposals since 2023.",
              s=["corp"], o="A", st="flux", neo=[0, ""], src=[["2026 URD", URD], ["SG press releases", PRLIST], ["Treezor: Shares completes acquisition, Oct 2026", TREEZOR], ["SG: Capital Markets Day slides", CMD]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Eight ways money moves: French retail cards on Cartes Bancaires and Visa, corporate cards split between Visa and Mastercard, BoursoBank on Visa, Mastercard-led cards at BRD and KB's premium credit, consumer-finance cards, Wero and instant transfers, acquiring, and transaction banking and stablecoins.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "France retail cards", "blurb": "CB and Visa.", "div": "sg", "rev": "frpb", "products": [
            P("sgcards", "SG retail cards", "CB Visa, CB Visa Premier, CB Visa Infinite and CB Visa Evolution, all co-badged with Cartes Bancaires; SG says its cards are of the Visa brand; more than 180 Collection designs and a dynamic-CVV option; Apple Pay on every CB Visa card and SG Pay on Android.", short="SG cards (CB and Visa)",
              s=["con"], lc="everyday", o="P", at="Visa, Cartes Bancaires", neo=[0, "Visa and CB."],
              mc="Visa holds SG's 8.5 million-client retail book.",
              src=[["SG: cards range", SGCARDS]]),
            P("sgmc", "CB Mastercard & CB Gold Mastercard", "No longer sold from June 2025; holders moved to the Visa equivalents in September and October 2025 without waiting for expiry. SG gave no reason.", short="SG Mastercard (withdrawn 2025)",
              s=["con"], lc="everyday", st="retired", ay="Jun 2025", neo=[0, "Mastercard, withdrawn 2025."],
              mc="SG's switch of its remaining retail Mastercard book to Visa.",
              src=[["MoneyVox: two SG cards gone, Jun 2025", MVOX25]]),
            P("cirrus", "CB Service Éclair Cirrus", "A withdrawal-only card on CB and Mastercard's Cirrus network, €30 a year; its assistance cover ended on 1 January 2026.", short="Cirrus withdrawal card",
              s=["con"], lc="everyday", o="P", at="Mastercard, Cartes Bancaires", neo=[1, "CB and Mastercard Cirrus."], src=[["SG: Cirrus card", CIRRUS]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Business & corporate cards", "blurb": "Visa, and Mastercard for corporates.", "div": "sg", "rev": "frpb", "products": [
            P("procards", "SG professional cards", "CB Visa Business and CB Visa Gold Business for professionals.", short="Pro cards (CB and Visa)",
              s=["sme"], lc="everyday", o="P", at="Visa, Cartes Bancaires", neo=[0, "Visa and CB."], src=[["SG professionnels: cards", SGPRO]]),
            P("corpvisa", "CB Visa Affaires", "CB Visa Affaires and CB Visa Gold Affaires in the Cartes Affaires Environnement range: recycled PVC, paperless statements and 5 cents to the French forestry office per payment; managed in Sogecarte Net.", short="Corporate Visa",
              s=["corp"], lc="everyday", o="P", at="Visa, Cartes Bancaires", neo=[0, "Visa and CB."], src=[["SG entreprises: Cartes Affaires", SGCORP]]),
            P("corpmc", "CB Corporate Mastercard", "CB Corporate Mastercard and CB Corporate Executive Mastercard for business travel, with negotiated travel benefits and higher limits, in the same range and Sogecarte Net.", short="Corporate Mastercard",
              s=["corp"], lc="everyday", o="P", at="Mastercard, Cartes Bancaires", neo=[2, "Mastercard, CB co-badged."],
              mc="Mastercard's last issuing foothold in SG France.",
              src=[["SG entreprises: Cartes Affaires", SGCORP]]),
        ]},
        {"id": "2.3", "ic": "smartphone", "name": "BoursoBank & teen cards", "blurb": "Visa; Banxup on Mastercard.", "div": "bourso", "rev": "frpb", "products": [
            P("boursocards", "BoursoBank cards", "Welcome (Visa Classic), Ultim and Metal (from €5.90 a month), and Visa Business at €9.99 a month for Bourso Business; free virtual cards; Apple Pay, Google Pay, Samsung Pay and Garmin Pay ⚠ CB co-badging not stated.", short="BoursoBank (Visa)",
              s=["con", "young"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."],
              mc="9.1 million clients aiming for 14 million by 2029, all on Visa.",
              src=[["BoursoBank: Ultim", BOURSO], ["BoursoBank: Metal", BOURSOMETAL], ["BoursoBank: business card", BOURSOPRO]]),
            P("banxup", "Banxup", "An app and Mastercard for 10–17 year-olds, with parent-set limits, issued by Treezor on an e-money account ⚠ Treezor left the group on 6 October 2026; Banxup's future not stated.", short="Banxup (Mastercard)",
              s=["young"], lc="open", st="flux", o="P", at="Mastercard, Treezor", neo=[2, "Mastercard via Treezor."], src=[["SG: Banxup", BANXUP], ["Treezor: Shares completes acquisition, Oct 2026", TREEZOR]]),
        ]},
        {"id": "2.4", "ic": "earth", "name": "Czech & Romanian cards", "blurb": "KB Visa debit; BRD Mastercard-led.", "div": "brd", "rev": "mibs", "products": [
            P("kbcards", "KB debit cards", "Platinum Visa debit with current accounts, Visa Infinite debit for KB Premium, and a virtual Visa issued in the KB+ app since 25 March 2026; MojeKarta designs carry both brands ⚠ 4U and A credit-card networks not verified.", div="kb", short="KB debit (Visa)",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["KB: cards", KBCARDS], ["KB: virtual Visa, Mar 2026", KBVIRT]]),
            P("kbwe", "KB Mastercard World Elite", "A credit card launched on 1 July 2021 to replace the Platinum card: travel insurance to CZK 10 million, concierge, four lounge visits a year and Mastercard Premium benefits; free for KB Premium clients (two cards).", div="kb", short="KB World Elite (Mastercard)",
              s=["saver"], lc="borrow", ay="Jul 2021", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["KB: World Elite, Jul 2021", KBWE], ["KB: cards", KBCARDS]]),
            P("brdcards", "BRD cards", "Debit cards on Mastercard or Visa, Mastercard Platinum and Noir (World Elite) debit, and Mastercard Gold and Platinum credit cards with airport lounges and Mastercard Priceless discounts; Apple Pay and Google Pay; about 2.2 million clients.", short="BRD (mostly Mastercard)",
              s=["con"], lc="everyday", o="P", at="Mastercard, Visa", neo=[1, "Mastercard-led, Visa alongside."],
              mc="Mastercard's strongest card book in the group.",
              src=[["BRD: debit cards", BRDDEBIT], ["BRD: Gold credit card", BRDGOLD], ["BRD: credit card", BRDCC]]),
        ]},
        {"id": "2.5", "ic": "hand-coins", "name": "Consumer-finance cards", "blurb": "Fiditalia Mastercard, Hanseatic Visa.", "div": "cf", "rev": "mibs", "products": [
            P("fiditalia", "Fiditalia Carta Bianca", "A revolving credit card in Italy on Mastercard, with Mastercard Identity Check and Click to Pay.", short="Fiditalia (Mastercard)",
              s=["borrower"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Fiditalia: Carta Bianca", FIDITALIA]]),
            P("hanseatic", "Hanseatic Bank credit cards", "Visa credit cards in Germany without a current account; Hanseatic passed one million customers in 2025 and won the Finanz Award for its card a sixth time.", short="Hanseatic (Visa)",
              s=["borrower"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Hanseatic Bank: credit cards", HANSEATIC], ["2026 URD", URD]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Wero & instant", "blurb": "Wero replaced Paylib.", "div": "group", "rev": "frpb", "products": [
            P("wero", "Wero", "EPI's account-to-account wallet, which SG co-owns: live at SG from 24 October 2024 in place of Paylib; SG plans to take it into e-commerce; BoursoBank to add it by the end of 2026, including for 10–17s; Wero has more than 55 million users, 72% in France, with point of sale due in 2027 ⚠.",
              s=["con", "young", "sme"], lc="move", st="new", ay="Oct 2024", o="P", at="EPI", neo=[0, "EPI's own."],
              mc="The European alternative to the card schemes, backed by SG.",
              src=[["EPI: Wero launches in France, Sep 2024", WEROFR], ["EPI: Wero after one year, Sep 2025", WERO1Y], ["EPI: BoursoBank and Wero, Jun 2026", BOURSOWERO]]),
            P("instant", "Instant transfers", "Free instant transfers at BoursoBank, credited in under ten seconds; instant payments across the SG network ⚠ volumes not published.",
              s=["con", "sme"], lc="move", neo=[0, ""], src=[["BoursoBank: Ultim", BOURSO], ["EPI: Wero launches in France, Sep 2024", WEROFR]]),
        ]},
        {"id": "2.7", "ic": "store", "name": "Acquiring", "blurb": "PayXpert and Stancer.", "div": "group", "rev": "frpb", "products": [
            P("payxpert", "PayXpert", "A payments fintech in which SG took a majority stake in 2023: e-commerce, POS terminals, multi-acquiring, Click to Pay and Asian payment methods ⚠ scheme mix not stated.",
              s=["sme"], lc="move", o="A", ay="2023", neo=[None, "Schemes not stated."], src=[["2026 URD", URD], ["PayXpert", PAYXPERT]]),
            P("boursoenc", "BoursoBank acceptance", "For Bourso Business clients, with Stancer: a mobile terminal, free from 150 transactions a month, and Tap to Pay on iPhone and Android.",
              s=["sme"], lc="move", o="P", at="Stancer", neo=[None, "Schemes not stated."], src=[["BoursoBank: acceptance", BOURSOENC]]),
        ]},
        {"id": "2.8", "ic": "coins", "name": "Transaction banking & digital money", "blurb": "GTPS and SG-Forge.", "div": "cib", "rev": "gbis", "products": [
            P("gtps", "Global Transaction & Payment Services", "Cash management, trade finance, correspondent banking, supply-chain finance and FX in more than 40 countries, running the group's euro payment platform; revenues up 6.7% in Q2 2026.",
              s=["corp"], lc="move", neo=[0, ""], mc="Virtual cards and Move could add to this franchise.", src=[["2026 URD", URD], ["Q2 2026 results", PR2Q26]]),
            P("forge", "SG-Forge stablecoins", "EUR CoinVertible (EURCV) and USD CoinVertible (USDCV, June 2025, BNY as reserve custodian) on public blockchains, and a first US digital bond on blockchain (November 2025).",
              s=["corp"], lc="move", o="B", neo=[0, ""], src=[["2026 URD", URD], ["SG-Forge", SGFORGE], ["SG press releases", PRLIST]]),
            P("treezor", "Treezor", "Banking-as-a-service for accounts and cards, which issued more than 8.5 million cards; Mastercard bought 5% in 2022 to reinforce an industrial partnership; sold 100% to Shares on 6 October 2026.", short="Treezor (sold)",
              s=["sme"], lc="move", st="retired", o="A", at="Mastercard", neo=[1, "Mastercard held 5%; sold."], src=[["2026 URD", URD], ["Treezor: Shares completes acquisition, Oct 2026", TREEZOR]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs underneath: card security and authentication, AI and automation, and card benefits from Mastercard Priceless at BRD to Visa Infinite in France.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "Dynamic CVV, Identity Check.", "div": "group", "rev": "frpb", "products": [
            P("security", "Card security", "A dynamic-CVV option for SG cards, in-app controls and instant limits at BoursoBank and KB, and Mastercard Identity Check at Fiditalia ⚠ no group fraud figures found.",
              s=["con"], lc="everyday", neo=[1, "Identity Check at Fiditalia."], src=[["SG: cards range", SGCARDS], ["BoursoBank: Ultim", BOURSO], ["Fiditalia: Carta Bianca", FIDITALIA]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI & automation", "blurb": "65% of Bourso contacts by AI.", "div": "bourso", "rev": "frpb", "products": [
            P("aiops", "AI in service", "BoursoBank's share of client interactions handled by AI rose from 39% in 2020 to 65% in 2025, with 0.6 contacts per client a year and about 1,000 staff; Anthropic's Claude to speed up support functions across the group.",
              s=["con", "young"], lc="beyond", st="new", o="P", at="Anthropic", neo=[0, ""], src=[["SG: Capital Markets Day slides", CMD]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Card benefits", "blurb": "Priceless at BRD and KB.", "div": "group", "rev": "mibs", "products": [
            P("priceless", "Mastercard Priceless & premium benefits", "BRD's Mastercard Gold, Platinum and Noir holders get Priceless discounts and lounge access; KB's World Elite carries Mastercard Premium benefits and concierge.", div="brd",
              s=["con", "saver"], lc="beyond", o="P", at="Mastercard", neo=[3, "Mastercard's own programme."], src=[["BRD: credit card", BRDCC], ["BRD: Gold credit card", BRDGOLD], ["KB: World Elite, Jul 2021", KBWE]]),
            P("visaperks", "Visa premium benefits", "Visa Infinite club and concierge for SG, and Visa SmartDelay with LoungeKey for BoursoBank Metal.",
              s=["saver"], lc="beyond", o="P", at="Visa", neo=[0, "Visa."], src=[["SG: cards range", SGCARDS], ["BoursoBank: Metal", BOURSOMETAL]]),
            P("lol", "League of Legends card", "France's first gaming card, launched with Mastercard in September 2019: up to 30% off gaming goods, coaching from SG-sponsored Gamers Origin and Priceless VIP access to the Worlds final ⚠ presumed ended with SG's retail Mastercard range in 2025.", short="Gaming card (Mastercard)",
              s=["young"], lc="beyond", st="retired", ay="Sep 2019", o="P", at="Mastercard", neo=[2, "Mastercard ⚠ presumed ended."], src=[["Electronic Payments International: gaming card, Sep 2019", LOL]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What it sells: the SG network and BoursoBank in France, private banking and insurance, global banking and markets, KB, BRD and Africa, and Ayvens with consumer finance.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "SG network", "blurb": "8.5m clients, 1,400 branches.", "div": "sg", "rev": "frpb", "products": [
            P("sgnetwork", "SG retail network", "France's fourth-largest national player after merging with Crédit du Nord: nearly 8.5 million individual, professional and corporate clients, about 1,400 branches under SG and ten regional brands, loans of €190 billion and deposits of €219 billion (Q2 2026).",
              s=["con", "sme"], lc="open", o="I", neo=[0, ""], src=[["2026 URD", URD], ["Q2 2026 results", PR2Q26], ["SG: Capital Markets Day release", CMDPR]]),
        ]},
        {"id": "4.2", "ic": "rocket", "name": "BoursoBank", "blurb": "9.1m clients.", "div": "bourso", "rev": "frpb", "products": [
            P("bourso", "BoursoBank", "France's leading online bank and broker: about 9.1 million clients at 30 June 2026 (280,000 added in the quarter), €84 billion under administration, €84 million of Q2 net income toward more than €300 million in 2026; aiming for more than 14 million clients by end-2029.",
              s=["con", "young", "saver"], lc="open", neo=[0, ""],
              mc="The group's growth engine, on Visa.",
              src=[["Q2 2026 results", PR2Q26], ["SG: Capital Markets Day release", CMDPR]]),
        ]},
        {"id": "4.3", "ic": "gem", "name": "Private banking & insurance", "blurb": "€145bn AuM, €167bn life.", "div": "group", "rev": "frpb", "products": [
            P("privbank", "SG Private Banking", "France's second-largest private bank, also in Luxembourg and Monaco: record assets under management of €145 billion in Q2 2026, aiming for about €180 billion in 2029.",
              s=["saver"], lc="grow", neo=[0, ""], src=[["Q2 2026 results", PR2Q26], ["SG: Capital Markets Day release", CMDPR]]),
            P("insurance", "SG Assurances", "Life insurance outstandings of a record €167 billion (43% unit-linked) in Q2 2026; €19.0 billion of gross premiums in 2025.",
              s=["saver"], lc="grow", neo=[0, ""], src=[["Q2 2026 results", PR2Q26], ["2026 URD", URD]]),
        ]},
        {"id": "4.4", "ic": "chart-candlestick", "name": "Global banking & markets", "blurb": "€2.7bn a quarter.", "div": "cib", "rev": "gbis", "products": [
            P("markets", "Global Markets", "Equities (€1,016 million in Q2 2026) and fixed income and currencies (€545 million), with the Bernstein research joint venture; 2029 revenue range €6.0–6.5 billion.",
              s=["corp"], lc="grow", neo=[0, ""], src=[["Q2 2026 results", PR2Q26], ["SG: Capital Markets Day release", CMDPR]]),
            P("financing", "Financing & Advisory", "Global Banking & Advisory and transaction banking: €975 million of revenues in Q2 2026, up 8.9%.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Q2 2026 results", PR2Q26]]),
            P("sgss", "Securities Services", "Custody, clearing and fund administration: €5,901 billion under custody; the retail securities business to go to Crédit Mutuel Arkéa under a March 2026 MoU.",
              s=["corp"], lc="grow", st="flux", neo=[0, ""], src=[["Q2 2026 results", PR2Q26], ["SG press releases", PRLIST]]),
        ]},
        {"id": "4.5", "ic": "globe", "name": "International retail", "blurb": "KB, BRD and Africa.", "div": "kb", "rev": "mibs", "products": [
            P("kb", "Komerční banka", "The Czech Republic's third-largest bank: loans of €38.1 billion and deposits of €44.9 billion at end-2025, close to 2.2 million clients and 185 branches; 1.5 million retail clients moved to its new digital bank by end-2025; voted Mastercard Bank of the Year 2025.",
              s=["con", "sme", "corp"], lc="open", o="A", neo=[1, "Visa debit, Mastercard premium credit."], src=[["2026 URD", URD], ["SG: Capital Markets Day slides", CMD]]),
            P("brd", "BRD Groupe Société Générale", "Romania's fifth bank by assets (about 10%): loans of €10.6 billion and deposits of €14.8 billion at end-2025, about 2.2 million clients, 347 branches; Romanian loans up 11.4% a year in Q2 2026.", div="brd",
              s=["con", "sme"], lc="open", o="A", neo=[1, "Mastercard-led cards."], src=[["2026 URD", URD], ["Q2 2026 results", PR2Q26], ["Romania Insider: market shares, Jun 2026", ROSHARE]]),
            P("africa", "Africa, Mediterranean & overseas", "Algeria, Tunisia, Côte d'Ivoire, Senegal and other markets plus the French overseas territories; €14 billion of loans in Q2 2026; Benin and Togo still being sold.", div="group",
              s=["con", "corp"], lc="open", st="flux", neo=[None, "Card networks not checked."], src=[["2026 URD", URD], ["Q2 2026 slides", SL2Q26]]),
        ]},
        {"id": "4.6", "ic": "plane", "name": "Mobility & consumer finance", "blurb": "Ayvens' 3.2m vehicles.", "div": "ayvens", "rev": "mibs", "products": [
            P("ayvens", "Ayvens", "The world's largest multi-brand vehicle lessor, formed from ALD and LeasePlan in 2023: about 3.2 million vehicles in 41 countries, €52.6 billion of earning assets and €755 million of Q2 2026 revenues; ROTE target 14–16% in 2029 ⚠ fleet-payment networks not found.",
              s=["driver", "corp"], lc="borrow", o="A", neo=[None, "No card network found."],
              mc="Fleet and fuel payments and carbon data are a possible opening.",
              src=[["2026 URD", URD], ["Q2 2026 results", PR2Q26], ["SG: Capital Markets Day release", CMDPR]]),
            P("consumer", "Consumer finance", "CGI (France, first), BDK (Germany, third), Hanseatic Bank and Fiditalia (Italy, fourth): €23 billion of loans, 61% in mobility, 22,000 partners; financing deals with BYD and Chery.", div="cf",
              s=["borrower", "driver"], lc="borrow", o="P", neo=[1, "Fiditalia Mastercard, Hanseatic Visa."], src=[["2026 URD", URD], ["Q2 2026 results", PR2Q26], ["SG: Capital Markets Day slides", CMD]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: L'Appli SG, the BoursoBank app and KB+, about 1,400 French branches plus KB's and BRD's, and partners and wallets.",
    "tiles": [
        {"id": "5.1", "ic": "monitor", "name": "Apps", "blurb": "L'Appli SG, BoursoBank, KB+.", "div": "group", "rev": "frpb", "products": [
            P("sgapp", "L'Appli SG", "SG's app for activating and running cards, with the Pass Sécurité, SG Pay on Android and Apple Pay.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["SG: cards range", SGCARDS]]),
            P("boursoapp", "BoursoBank app & boursorama.com", "Ranked the top banking app, with an NPS of +54; boursorama.com draws more than 130 million visits a month.", div="bourso",
              s=["con", "young", "saver"], lc="everyday", neo=[0, ""], src=[["SG: Capital Markets Day slides", CMD], ["2026 URD", URD]]),
            P("kbplus", "KB+", "KB's new digital-bank app, where clients open a virtual Visa and set limits in seconds.", div="kb",
              s=["con"], lc="everyday", st="new", neo=[0, ""], src=[["KB: virtual Visa, Mar 2026", KBVIRT]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches", "blurb": "About 1,400 in France.", "div": "sg", "rev": "frpb", "products": [
            P("branches", "Branches", "About 1,400 SG branches in France (to be streamlined), 185 at KB, 347 at BRD and 52 in the French overseas territories.",
              s=["con", "sme"], lc="open", neo=[0, ""], src=[["2026 URD", URD], ["SG: Capital Markets Day release", CMDPR]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partners & wallets", "blurb": "22,000 partners, four wallets.", "div": "group", "rev": "mibs", "products": [
            P("partners", "Partners", "22,000 consumer-finance partners (more than 80% of outstandings), car makers BYD and Chery, and Ayvens' leasing partners.", div="cf",
              s=["borrower", "driver"], lc="open", o="P", neo=[0, ""], src=[["2026 URD", URD]]),
            P("wallets", "Digital wallets", "Apple Pay, Google Pay, Samsung Pay and Garmin Pay at BoursoBank, Apple Pay and SG Pay at SG, and Apple Pay and Google Pay at BRD.",
              s=["con", "young"], lc="everyday", o="P", at="Apple, Google, Samsung", neo=[None, "Token services not stated."], src=[["BoursoBank: Ultim", BOURSO], ["SG: cards range", SGCARDS], ["BRD: debit cards", BRDDEBIT]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Société Générale", "blurb": "Corporates and the east, not French retail.", "products": [
        P("mcatsg", "Mastercard at Société Générale", "SG France and BoursoBank are Cartes Bancaires and Visa; SG stopped selling its last retail Mastercard cards in June 2025. Mastercard keeps SG's corporate cards, the Cirrus withdrawal card, BRD's Mastercard-led range with Priceless, KB's World Elite and Fiditalia; it held 5% of Treezor until the October 2026 sale. KB was voted Mastercard Bank of the Year 2025. No network contract is public.",
          s=["con"], div="group", rev="corp", mc="The relationship this map is drawn for.",
          src=[["MoneyVox: two SG cards gone, Jun 2025", MVOX25], ["SG entreprises: Cartes Affaires", SGCORP], ["BRD: credit card", BRDCC], ["2026 URD", URD]]),
    ]},
    {"id": "pillar-market", "name": "French and European payments", "blurb": "CB, Visa, Wero.", "products": [
        P("market", "The market", "Cartes Bancaires' share rose from 61.4% to 63.6% in the second half of 2025, after 89.6% in late 2021 (Yavin index), helped by CB in Apple Pay; 121 of 129 French banks offer Visa Classic; Wero moves into e-commerce; a digital euro is under negotiation; Česká spořitelna went Visa-only in 2023.",
          s=["con"], div="group", rev="corp", src=[["MoneyVox: CB regains share, Mar 2026", MVOXCB], ["MoneyVox: two SG cards gone, Jun 2025", MVOX25], ["2026 URD", URD], ["finance.cz: ČS goes Visa, Apr 2023", VISA23]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
