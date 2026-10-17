"""BNP Paribas' layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the 2Q26 results (23 July 2026), the 4Q25 results
(5 February 2026) and the 2025 Universal Registration Document (19 March 2026). ``neo`` is the Mastercard lens:
[depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

PR2Q26 = "https://invest.bnpparibas/en/document/2q26-pr"
SL2Q26 = "https://invest.bnpparibas/document/2q26-slides"
TR2Q26 = "https://invest.bnpparibas/en/document/second-quarter-2026-results-transcript"
PR4Q25 = "https://invest.bnpparibas/en/document/4q25-pr"
URD25 = "https://invest.bnpparibas/en/document/universal-registration-document-annual-financial-report-2025-pdf"
GLANCE = "https://invest.bnpparibas/en/document/2026-at-a-glance"
RAT = "https://invest.bnpparibas/en/debt-and-ratings"
PIERRI = "https://www.bnpparibas-am.com/press/mediaroom-en-bnp-paribas-sandro-pierri-joins-the-executive-committee-of-the-bnp-paribas-group/"
TARIFS = "https://www.moneyvox.fr/tarif-bancaire/bnp-paribas/pdf/tarifs-2026.pdf"
TA21 = "https://www.test-achats.be/argent/payer/news/carte-visa-debit-bnppf"
NICKEL = "https://nickel.eu/fr"
NICKELABOUT = "https://nickel.eu/fr/qui-sommes-nous"
FLOA = "https://floa.com/"
BNL = "https://bnl.it/it/Individui-e-Famiglie/Carte"
BGL = "https://www.bgl.lu/fr/particuliers/cartes-de-paiement.html"
BGLPAY = "https://www.bgl.lu/fr/particuliers/paiements-mobiles.html"
PL = "https://www.bnpparibas.pl/klienci-indywidualni/karty"
CONSORS = "https://www.consorsfinanz.de/mastercard"
TEB = "https://www.teb.com.tr/kartlar/"
PAYPERS = "https://thepaypers.com/payments/news/bnp-paribas-accelerates-wero-rollout-for-merchants-in-europe"
FORTISWERO = "https://newsroom.bnpparibasfortis.be/easy-banking-app-integrates-wero-for-instant-european-e-commerce-payments"
FORTISH1 = "https://newsroom.bnpparibasfortis.be/bnp-paribas-fortis-reported-a-net-profit-of-eur-15-billion-for-the-first-half-of-2026"
FORTISSURVEY = "https://newsroom.bnpparibasfortis.be/belgians-have-little-confidence-in-ai-driven-payments-the-bank-card-remains-king"
ESTREEM = "https://www.qorusglobal.com/content/29415-bnp-paribas-and-bpce-launch-estreem-a-new-payments-processing-leader"
CPAY = "https://www.mastercard.com/news/europe/en-uk/newsroom/press-releases/en-gb/2019/june/bnp-paribas-personal-finance-partners-with-mastercard-to-launch-its-cpay-card-in-france"
ECN = "https://www.ecommerce-nation.fr/wero-depasse-435-millions-dutilisateurs-et-vise-le-commerce-pour-2026/"
MAAP = "https://www.mastercard.com/us/en/news-and-trends/press/2025/april/mastercard-unveils-agent-pay-pioneering-agentic-payments-technology-to-power-commerce-in-the-age-of-ai.html"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · heritage · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: €939 billion of loans and CET1 of 13% at 30 June 2026, a group formed in 2000 from BNP and Paribas, 2,068 APIs and Mistral AI, and a 2027–30 plan due on 2 February 2027.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "€51bn revenue, €12bn profit.", "div": "group", "rev": "corp", "products": [
            P("balance", "Balance sheet & earnings", "Revenue of €51.2 billion and net income of €12.2 billion in 2025; €4.3 billion of net income in 2Q26 (RoTE 13.3%, CET1 13.0%); loans of €939.4 billion and deposits of €1,161 billion at 30 June 2026; rated A+/A1/AA- by S&P, Moody's and Fitch; market value €90.2 billion at end-2025; more than 180,000 staff in 64 countries.",
              s=["con", "corp"], neo=[0, ""], src=[["2Q26 results", PR2Q26], ["4Q25 results", PR4Q25], ["BNP Paribas: debt and ratings", RAT], ["2026 at a glance", GLANCE]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Lemierre and Bonnafé.", "div": "group", "rev": "corp", "products": [
            P("leadership", "Board & executive committee", "Chair Jean Lemierre, CEO Jean-Laurent Bonnafé, COOs Yann Gérardin (CIB) and Thierry Laborde (CPBS, and a director of EPI), CFO Lars Machenil, CIO Marc Camus; Sandro Pierri of the asset manager joined the committee in March 2026 ⚠ later changes not verified.",
              s=["corp"], neo=[0, ""], src=[["2025 URD", URD25], ["BNPP AM: Pierri, Apr 2026", PIERRI]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage", "blurb": "BNP and Paribas, 2000.", "div": "group", "rev": "corp", "products": [
            P("heritage", "Heritage", "BNP formed in 1966 and Paribas privatised in 1987; BNP Paribas created on 23 May 2000; BNL bought in 2006, Fortis Bank and BGL in 2009, Hello bank! launched in 2012, Nickel bought in 2017 and Bank of the West sold to BMO in 2023.",
              s=["con"], o="I", neo=[0, ""], src=[["2025 URD", URD25]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "Mistral AI, 2,068 APIs.", "div": "group", "rev": "corp", "products": [
            P("ai", "AI platforms", "Ranked first eurozone bank in the Evident AI index; more than 7,500 developers on generative AI, Mistral AI as partner since 2024, an LLM-as-a-service platform and 'My companion' for 100,000 staff, aiming at 'the agentic era'.",
              s=["corp"], st="new", o="P", at="Mistral AI", neo=[0, ""],
              mc="Agent Pay launched in April 2025 with no BNP Paribas mention; the group says it is heading for agents.",
              src=[["4Q25 results", PR4Q25], ["2Q26 slides", SL2Q26], ["Mastercard: Agent Pay, Apr 2025", MAAP]]),
            P("apis", "Group API platform", "2,068 APIs carrying more than 3.76 billion transactions a month.",
              s=["corp"], neo=[0, ""], src=[["2026 at a glance", GLANCE]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "A 2030 plan in February.", "div": "group", "rev": "corp", "products": [
            P("strategy", "Targets & plan", "RoTE of 12% in 2026 and above 13% in 2028, cost:income below 56% by 2028, CET1 of 13% and a payout of at least 60% from 2027; payments named one of three cross-cutting growth areas; the 2027–30 plan is due with 4Q26 results on 2 February 2027.",
              s=["corp"], neo=[0, ""], src=[["4Q25 results", PR4Q25], ["2Q26 transcript", TR2Q26], ["2026 at a glance", GLANCE]]),
            P("deals", "Deals", "AXA IM bought (July 2025), HSBC's German private bank (October 2025), the AG Insurance stake sold to Ageas (April 2026, an €858 million gain), Athlon to join Arval ⚠ completion not confirmed, and BMCI Morocco to be sold in 4Q26.",
              s=["corp"], o="A", st="flux", neo=[0, ""], src=[["2025 URD", URD25], ["2Q26 results", PR2Q26], ["2Q26 transcript", TR2Q26]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Eight ways money moves: French cards on Cartes Bancaires and Visa, Belgian debit on Bancontact and Visa, Mastercard at BNL and in Poland, Mastercard on Nickel, Cetelem, Consors Finanz and Floa, Wero, acquiring and the Estreem processor, and tokens and a euro stablecoin.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "France cards", "blurb": "CB and Visa.", "div": "france", "rev": "cpbs", "products": [
            P("frcards", "BNP Paribas France cards", "Origin, Visa Classic, Visa Premier (€144 a year), Visa Infinite, Visa Plus and BNP Net, all co-badged with Cartes Bancaires; the biometric Visa Premier is withdrawn on 31 December 2026; 7.7 million clients.", short="France cards (CB and Visa)",
              s=["con"], lc="everyday", o="P", at="Visa, Cartes Bancaires", neo=[0, "Visa and CB."],
              mc="Visa holds the group's largest debit franchise.",
              src=[["BNP Paribas France fees 2026", TARIFS]]),
            P("cirrus", "Mastercard Cirrus card", "A cash-withdrawal card, the last Mastercard product in the French retail range, discontinued on 12 December 2025.", short="Cirrus (withdrawn)",
              s=["con"], lc="everyday", st="retired", ay="Dec 2025", neo=[0, "Mastercard, withdrawn December 2025."], src=[["BNP Paribas France fees 2026", TARIFS]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Belgium cards", "blurb": "Bancontact and Visa.", "div": "fortis", "rev": "cpbs", "products": [
            P("fortisdebit", "Bancontact/Visa Debit", "BNP Paribas Fortis, Fintro and Hello bank! Belgium debit cards, co-badged Bancontact and Visa Debit since 2021 in place of Maestro; more than 4 million clients.", short="Belgium debit (Visa)",
              s=["con"], lc="everyday", ay="Sep 2021", o="P", at="Visa, Bancontact", neo=[0, "Visa and Bancontact."], src=[["Test Achats: Visa Debit, Sep 2021", TA21]]),
            P("fortiscredit", "BNP Paribas Fortis credit cards", "Credit cards for Fortis clients ⚠ network not verified.",
              s=["con"], lc="borrow", neo=[None, "Network not verified."], src=[["BNP Paribas Fortis H1 2026", FORTISH1]]),
        ]},
        {"id": "2.3", "ic": "credit-card", "name": "Italy cards", "blurb": "BNL on Mastercard.", "div": "bnl", "rev": "cpbs", "products": [
            P("bnlmc", "BNL debit & credit", "Debit and prepaid cards and Classic and Gold World credit cards on Mastercard, and World Elite ⚠ scheme not stated; about 2.4 million clients.", short="BNL cards (Mastercard)",
              s=["con"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["BNL: cards", BNL]]),
            P("bnlamex", "BNL American Express", "Amex Oro and Platino alongside the Mastercard range.",
              s=["con"], lc="borrow", o="P", at="American Express", neo=[0, "American Express."], src=[["BNL: cards", BNL]]),
        ]},
        {"id": "2.4", "ic": "earth", "name": "Luxembourg, Poland & Türkiye", "blurb": "Split, Mastercard-led in Poland.", "div": "polska", "rev": "cpbs", "products": [
            P("plcards", "BNP Paribas Bank Polska cards", "Mastercard Standard, Gold and Multicurrency debit, with Visa Platinum and Visa Filmowa alongside.", short="Poland cards (mostly Mastercard)",
              s=["con"], lc="everyday", o="P", at="Mastercard, Visa", neo=[1, "Mastercard-led, Visa alongside."], src=[["BNP Paribas Bank Polska: cards", PL]]),
            P("bglcards", "BGL BNP Paribas cards", "Visa Debit and Visa Classic, with Mastercard Gold, Platinum and Elite for premium credit; about 185,000 clients.", div="group", short="BGL cards (Visa and Mastercard)",
              s=["con"], lc="everyday", o="P", at="Visa, Mastercard", neo=[1, "Visa debit, Mastercard premium credit."], src=[["BGL: payment cards", BGL]]),
            P("teb", "TEB Bonus cards", "TEB's Bonus credit cards in Türkiye show Visa Signature and Infinite benefits, and a TEB Özel World Elite card ⚠ probably Mastercard.", div="group",
              s=["con"], lc="borrow", o="P", at="Visa", neo=[1, "Visa, and a World Elite card ⚠."], src=[["TEB: cards", TEB]]),
        ]},
        {"id": "2.5", "ic": "wallet", "name": "Challenger & credit cards", "blurb": "Nickel, Cpay, Consors, Floa.", "div": "pf", "rev": "cpbs", "products": [
            P("nickelcard", "Nickel card", "A Mastercard with every Nickel account since launch in February 2014: Classic at €25 a year, Chrome €30, Metal €80, and limited-edition UEFA Champions League designs; 4.94 million accounts opened by end-2025.", div="nickel", short="Nickel (Mastercard)",
              s=["con"], lc="open", ay="Feb 2014", o="A", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard's clearest home in the group, with its football sponsorship on the card.",
              src=[["Nickel", NICKEL], ["Nickel: about us", NICKELABOUT], ["2025 URD", URD25]]),
            P("cpay", "Cetelem Cpay", "Personal Finance's Cpay Mastercard, which replaced the Cetelem card in France from March 2019 with in-app controls ⚠ detail from a search snippet.", short="Cpay (Mastercard)",
              s=["borrower"], lc="borrow", ay="Mar 2019", o="P", at="Mastercard", neo=[2, "Mastercard ⚠."], src=[["Mastercard: Cpay, Jun 2019 ⚠", CPAY]]),
            P("consors", "Consors Finanz Mastercard", "A no-fee Mastercard in Germany: pay now, in instalments or up to 90 days later, with Apple Pay and Google Pay.", short="Consors Finanz (Mastercard)",
              s=["borrower"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Consors Finanz: Mastercard", CONSORS]]),
            P("floacard", "Floa cards", "Carte Cdiscount (€1.25 a month) and Carte Gold (€4.50 a month), both Mastercard with cashback.", div="floa", short="Floa (Mastercard)",
              s=["borrower"], lc="borrow", o="A", at="Mastercard", neo=[2, "Mastercard."], src=[["Floa", FLOA]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Wero & instant", "blurb": "57 million Wero users.", "div": "group", "rev": "cpbs", "products": [
            P("wero", "Wero", "EPI's account-to-account wallet, which BNP Paribas co-owns: live at BNP Paribas France, Fortis (e-commerce from February 2026), BGL (Payconiq switched off 30 September 2026) and Nickel; e-commerce for every French customer from September 2026, 57 million users, point of sale next.",
              s=["con", "sme"], lc="move", st="new", ay="Sep 2026", o="P", at="EPI", neo=[0, "EPI's own."],
              mc="The most direct challenge to the card schemes; Laborde sits on EPI's board.",
              src=[["The Paypers: Wero rollout, Sep 2026", PAYPERS], ["Fortis: Wero in Easy Banking, Feb 2026", FORTISWERO], ["BGL: mobile payments", BGLPAY], ["Ecommerce Nation: Wero, Sep 2025", ECN]]),
            P("instant", "Instant transfers", "Free instant transfers for French customers through Wero; instant payments among Fortis business clients up 75% in the first half of 2026.",
              s=["con", "sme"], lc="move", neo=[0, ""], src=[["BNP Paribas France fees 2026", TARIFS], ["BNP Paribas Fortis H1 2026", FORTISH1]]),
        ]},
        {"id": "2.7", "ic": "store", "name": "Acquiring & processing", "blurb": "Axepta and Estreem.", "div": "group", "rev": "cpbs", "products": [
            P("axepta", "Axepta BNP Paribas", "The group's acquiring and gateway business, to serve merchants for Wero in all five EPI countries by 2026; BNL lost its influence over Worldline Merchant Services Italia in September 2025.",
              s=["sme"], lc="move", neo=[None, "Card schemes not stated."], src=[["The Paypers: Wero rollout, Sep 2026", PAYPERS], ["2025 URD", URD25]]),
            P("estreem", "Estreem", "A card processor owned 50:50 with BPCE (February 2025), handling 17 billion transactions a year across Visa, Mastercard and CB, about 30% of French card payments; platform built in 2026, clients migrated by 2028.",
              s=["sme", "corp"], lc="move", st="new", ay="Feb 2025", o="P", at="BPCE", neo=[1, "Processes Mastercard among other schemes."],
              mc="A platform still being built, where tokens and fraud tools could be designed in ⚠.",
              src=[["Qorus: Estreem, Feb 2025", ESTREEM]]),
            P("onepointsix", "1Point6", "A payment solution for platforms that began its growth in 2Q26.",
              s=["corp"], lc="move", st="new", neo=[None, "Nothing public."], src=[["2Q26 results", PR2Q26]]),
        ]},
        {"id": "2.8", "ic": "coins", "name": "Digital money", "blurb": "Stablecoin, tokens, Lyf.", "div": "group", "rev": "cib", "products": [
            P("stablecoin", "Euro stablecoin consortium", "One of ten banks behind a MiCAR euro stablecoin (2025) ⚠ name and launch date not verified.",
              s=["corp"], lc="move", st="new", o="P", neo=[0, ""], src=[["2025 URD", URD25]]),
            P("dtc", "Securities tokenisation", "Securities Services helped build the DTC tokenisation service alongside 50 firms in 2Q26.",
              s=["corp"], lc="grow", st="new", neo=[0, ""], src=[["2Q26 results", PR2Q26]]),
            P("lyf", "Lyf", "A mobile payments app, equity-accounted at 46.3% to 50%.",
              s=["con"], lc="move", neo=[None, "Nothing public."], src=[["2025 URD", URD25]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: AI screening for money laundering and sanctions, the Samy and Eva assistants, and card benefits and payment protection from Priceless in Poland to Cardif.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & compliance", "blurb": "AI screening.", "div": "group", "rev": "corp", "products": [
            P("screening", "Screening & transaction filtering", "AI-based customer screening and transaction filtering for money laundering and sanctions; AI spending aimed at efficiency, cost of risk and cybersecurity.",
              s=["con", "corp"], lc="everyday", neo=[0, "The group's own."],
              mc="Personal Finance's cost of risk is 153bps; instant payments need fraud scoring.",
              src=[["2025 URD", URD25], ["4Q25 results", PR4Q25], ["2Q26 results", PR2Q26]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "Assistants", "blurb": "Samy and Eva.", "div": "fortis", "rev": "cpbs", "products": [
            P("assistants", "Samy & Eva", "Samy, Fortis' digital assistant, resolves 77% of about 800,000 conversations; Floa runs the Eva AI assistant.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["BNP Paribas Fortis H1 2026", FORTISH1], ["Floa", FLOA]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Card benefits & protection", "blurb": "Priceless, Cardif.", "div": "polska", "rev": "cpbs", "products": [
            P("priceless", "Bezcenne Chwile", "Mastercard's Priceless programme, run by BNP Paribas Bank Polska on its Mastercard debit and credit cards.", short="Priceless (Poland)",
              s=["con"], lc="grow", o="P", at="Mastercard", neo=[3, "Mastercard Priceless."], src=[["BNP Paribas Bank Polska: cards", PL]]),
            P("retourcolis", "Assurance retour colis", "Mastercard's return-postage refund on BGL cards.", div="group",
              s=["con"], lc="grow", o="P", at="Mastercard", neo=[3, "Mastercard's benefit."], src=[["BGL: payment cards", BGL]]),
            P("protection", "Payment & credit protection", "Cardif payment-protection, credit and warranty insurance (the Stellantis warranty partnership reached Italy in 2Q26), and Floa's insurance on payment methods.", div="group",
              s=["borrower", "driver"], lc="beyond", neo=[0, ""], src=[["2Q26 results", PR2Q26], ["Floa", FLOA]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: consumer credit for 25 million through Cetelem, Findomestic and Consors Finanz, Floa's instalments, Arval's 1.9 million vehicles, retail banking in four home markets and Nickel Pro, Europe's top cash-management franchise, and €2.6 trillion of assets under management.",
    "tiles": [
        {"id": "4.1", "ic": "hand-coins", "name": "Consumer credit & BNPL", "blurb": "25 million customers.", "div": "pf", "rev": "cpbs", "products": [
            P("pf", "Personal Finance", "Cetelem, Findomestic, AlphaCredit and Consors Finanz for 25 million customers, with retail partners Apple (UK launch 2Q26), Orange and Currys and car makers Stellantis, Chery and Lynk & Co; mobility production up 16.4% in 2Q26.",
              s=["borrower", "driver"], lc="borrow", neo=[1, "Cpay and Consors Finanz on Mastercard."], src=[["2Q26 results", PR2Q26], ["4Q25 results", PR4Q25]]),
            P("floabnpl", "Floa instalments", "Pay in 3, 4, 10 or 12 instalments or later, at more than 20,000 merchants including Cdiscount, Veepee and SFR; 4 million customers.", div="floa",
              s=["borrower"], lc="borrow", o="A", neo=[0, "Floa's own credit."],
              mc="Competes with Mastercard Installments; could run on Mastercard credentials.",
              src=[["Floa", FLOA], ["4Q25 results", PR4Q25]]),
        ]},
        {"id": "4.2", "ic": "target", "name": "Arval & leasing", "blurb": "1.9 million vehicles.", "div": "group", "rev": "cpbs", "products": [
            P("arval", "Arval & Leasing Solutions", "Full-service leasing of 1.9 million vehicles, about 2.3 million with Athlon ⚠ completion not confirmed; equipment finance through Leasing Solutions; revenue down 21.1% in 2Q26 on used-car prices.",
              s=["driver"], lc="borrow", neo=[None, "Fleet card scheme not public."],
              mc="Fleet, fuel and virtual cards for one of Europe's largest fleets are untested ground.",
              src=[["2Q26 results", PR2Q26], ["2Q26 transcript", TR2Q26]]),
        ]},
        {"id": "4.3", "ic": "house", "name": "Retail banking", "blurb": "Four home markets.", "div": "france", "rev": "cpbs", "products": [
            P("retail", "Commercial & personal banking", "More than 7.7 million clients in France, more than 4 million in Belgium, about 2.4 million in Italy and 185,000 in Luxembourg, and more than 17 million in Europe-Mediterranean.",
              s=["con", "sme"], lc="everyday", neo=[1, "Visa at home, Mastercard in Italy and Poland."], src=[["2026 at a glance", GLANCE], ["2025 URD", URD25]]),
            P("nickelpro", "Nickel Compte Pro", "A €50-a-year account for sole traders, launched in 2Q26; Nickel opens about 600,000 accounts a year.", div="nickel",
              s=["sme"], lc="open", st="new", neo=[2, "Mastercard, like every Nickel card ⚠."],
              mc="Room for Mastercard Business debit and acceptance.",
              src=[["2Q26 results", PR2Q26], ["Nickel", NICKEL]]),
        ]},
        {"id": "4.4", "ic": "factory", "name": "Corporate & institutional", "blurb": "Number one in Europe.", "div": "group", "rev": "cib", "products": [
            P("cib", "Corporate & Institutional Banking", "Global Banking, Global Markets and Securities Services: revenue of €5.3 billion and pre-tax income of €2.4 billion in 2Q26; third in EMEA M&A in the half.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["2Q26 results", PR2Q26]]),
            P("cashmgmt", "Cash management & trade", "First in Europe for large-corporate cash management and trade finance, with factoring, and Kantox's FX automation (bought July 2023).",
              s=["corp"], lc="move", neo=[0, ""],
              mc="Move, Track and virtual cards could serve this franchise.",
              src=[["2026 at a glance", GLANCE], ["2025 URD", URD25]]),
        ]},
        {"id": "4.5", "ic": "gem", "name": "Wealth & insurance", "blurb": "€2.6tn under management.", "div": "group", "rev": "ips", "products": [
            P("wealth", "Asset management & wealth", "BNP Paribas Asset Management with AXA IM (€1,732 billion), private banking in France (€140 billion), and Consorsbank and DAB for more than 2 million investors; IPS manages €2,590 billion.",
              s=["saver"], lc="grow", neo=[0, ""], src=[["2Q26 results", PR2Q26], ["2025 URD", URD25]]),
            P("cardif", "Cardif savings & protection", "Savings and protection insurance with €8.5 billion of net inflows in 2Q26.",
              s=["saver"], lc="grow", neo=[0, ""], src=[["2Q26 results", PR2Q26]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: Mes Comptes and Easy Banking, Hello bank!, branches, tobacconists and ATMs, and wallets and retail partners.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Apps & Hello bank!", "blurb": "408m connections a month.", "div": "group", "rev": "cpbs", "products": [
            P("apps", "Mes Comptes & Easy Banking", "Mes Comptes, ranked France's best network-bank app three years running, and Fortis' Easy Banking App with 2.77 million active users; 408 million app connections a month across the group in 2Q26.",
              s=["con", "saver"], lc="everyday", neo=[0, ""], src=[["2025 URD", URD25], ["BNP Paribas Fortis H1 2026", FORTISH1], ["2Q26 results", PR2Q26]]),
            P("hello", "Hello bank!", "The digital bank in France, Belgium, Germany and Italy, with 3.9 million customers ⚠ French cards believed Visa.",
              s=["con"], lc="open", neo=[None, "Believed Visa ⚠."], src=[["2026 at a glance", GLANCE], ["2Q26 results", PR2Q26]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "1,474 branches in France.", "div": "france", "rev": "cpbs", "products": [
            P("branches", "Branches, tobacconists & ATMs", "1,474 branches in France and more than 1,200 in Europe-Mediterranean, 13,370 Nickel points of sale, more than 6,700 ATMs shared with Crédit Mutuel, CIC and Société Générale, and BGL replacing its ATMs.",
              s=["con"], lc="open", neo=[0, ""], src=[["2025 URD", URD25], ["BGL: payment cards", BGL]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partners & wallets", "blurb": "Retailers, bpost, Apple Pay.", "div": "group", "rev": "cpbs", "products": [
            P("partners", "Partners", "Personal Finance's retail and car-maker partners, Floa through Lydia and Bankin', and Nickel through bpost (1,100 points in Belgium), tobacconists and an Amazon offer.",
              s=["borrower", "con"], lc="open", o="P", neo=[0, ""], src=[["2025 URD", URD25], ["Floa", FLOA], ["2Q26 results", PR2Q26]]),
            P("wallets", "Digital wallets", "Apple Pay and Google Pay at Nickel, BGL, Consors Finanz and Bank Polska; Samsung Pay and Google Pay at BNL.",
              s=["con"], lc="everyday", o="P", at="Apple, Google, Samsung", neo=[None, "Token service not stated."], src=[["BGL: mobile payments", BGLPAY], ["BNL: cards", BNL], ["Consors Finanz: Mastercard", CONSORS]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at BNP Paribas", "blurb": "The challengers, not the home banks.", "products": [
        P("mcatbnp", "Mastercard at BNP Paribas", "Mastercard carries Nickel, Cpay, Consors Finanz and Floa, BNL in Italy, most of Bank Polska with Priceless, and BGL's premium credit. Cartes Bancaires and Visa hold BNP Paribas France, where the last Mastercard card went in December 2025, and Bancontact and Visa hold Fortis. No group network contract is public.",
          s=["con"], div="group", rev="corp", mc="The relationship this map is drawn for.",
          src=[["Nickel", NICKEL], ["BNP Paribas France fees 2026", TARIFS], ["Test Achats: Visa Debit, Sep 2021", TA21]]),
    ]},
    {"id": "pillar-market", "name": "European banking", "blurb": "Wero, CB, Bancontact.", "products": [
        P("market", "The market", "Wero pushing into e-commerce and shops, domestic schemes (Cartes Bancaires, Bancontact, Bancomat, BLIK ⚠), EU instant-payment rules and MiCAR; only 23% of Belgians trust AI-driven payments and 97% hold a debit card.",
          s=["con"], div="group", rev="corp", src=[["The Paypers: Wero rollout, Sep 2026", PAYPERS], ["Fortis: payments survey, Aug 2026", FORTISSURVEY], ["2025 URD", URD25]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
