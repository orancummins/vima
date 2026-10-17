"""Crédit Agricole's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the Q2 and H1 2026 results (31 July 2026), the Q4 and
full-year 2025 results (4 February 2026) and the IKB release (12 October 2026). ``neo`` is the Mastercard lens:
[depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

PRQ2 = "https://www.credit-agricole.com/en/pdfPreview/211049"
SLQ2 = "https://www.credit-agricole.com/en/pdfPreview/211051"
PRFY = "https://www.credit-agricole.com/en/pdfPreview/208647"
SLFY = "https://www.credit-agricole.com/en/pdfPreview/208649"
IKB = "https://www.credit-agricole.com/en/pdfPreview/211487"
DEUT = "https://www.credit-agricole.com/en/news-channels/the-channels/newsflash/credit-agricole-announces-the-launch-of-credit-agricole-deutschland"
GOV = "https://www.credit-agricole.com/en/group/governance"
RAT = "https://www.credit-agricole.com/en/finance/debt-and-ratings"
GROUP = "https://www.credit-agricole.com/en/group/discover-the-credit-agricole-group"
HIST = "https://www.credit-agricole.com/en/group/history-of-the-credit-agricole-group"
ACTA = "https://www.credit-agricole.com/en/group/group-project-and-act-2028/act-2028/a-for-acceleration"
ACTT = "https://www.credit-agricole.com/en/group/group-project-and-act-2028/act-2028/t-for-transformation"
TARIFS = "https://www.credit-agricole.fr/content/dam/assetsca/cr895/npc/documents/tarifs/2026/Tarifs-2026-Particulier-V8.pdf"
GOLD = "https://www.moneyvox.fr/carte-bancaire/actualites/107763/quelle-banque-de-reseau-propose-la-gold-mastercard-la-moins-chere"
MEMO = "https://credit-agricole.fr/content/dam/assetsca/cr868/npc/documents/informations-reglementaires/memos/MEMO_MDP_Carte%20Mastercard_CACF.pdf"
LCL = "https://www.lcl.fr/cartes-bancaires"
PRO = "https://www.credit-agricole.fr/professionnel.html"
CAWL = "https://www.cawl.fr/"
WLCAWL = "https://worldline.com/fr-fr/home/top-navigation/media-relations/communique-de-presse/pr-2026_06_30_01"
WLAGENT = "https://worldline.com/fr-fr/home/top-navigation/media-relations/communique-de-presse/pr-2026_06_25_01"
CFIAGENT = "https://www.crowdfundinsider.com/2026/07/288572-credit-agricole-mastercard-worldline-complete-frances-first-production-agentic-payment/"
MAAP = "https://www.mastercard.com/us/en/news-and-trends/press/2025/april/mastercard-unveils-agent-pay-pioneering-agentic-payments-technology-to-power-commerce-in-the-age-of-ai.html"
IOS = "https://next.ink/244182/le-credit-agricole-lance-sa-propre-application-de-paiement-sur-iphone-quid-dapple-pay/"
WERO = "https://www.societegenerale.com/sites/default/files/documents/2025-09/cp-wero-1-an-vf.pdf"
BPCEWERO = "https://www.economiematin.fr/?p=219887"
CBSHARE = "https://www.moneyvox.fr/carte-bancaire/actualites/108113/le-reseau-francais-cb-reprend-du-terrain-a-visa-et-mastercard"
MCBIO = "https://www.mastercard.com/news/europe/en/newsroom/news-briefs/en/2019/june/mastercard-collaborates-with-credit-agricole-on-biometric-card-trial-in-france"
BIO = "https://www.moneyvox.fr/carte-bancaire/actualites/85394/credit-agricole-une-carte-bancaire-biometrique-arrive"
TOULOUSE = "https://www.credit-agricole.fr/content/dam/assetsca/cr831/npc/documents/espace-presse/2022-03-10.pdf"
AMEX = "https://www.creditagricole.info/app/uploads/2023/10/Credit-Agricole-signe-un-partenariat-national-avec-American-Express.pdf"
APPLEPAY = "https://consomac.fr/news-11875-apple-pay-enfin-disponible-au-credit-agricole.html"
ITCARDS = "https://www.credit-agricole.it/privati/carte"
ITVISA = "https://lepetitjournal.com/milan/actualites/credit-agricole-visa-partenariat-italie-innovation-317703"
PLCARDS = "https://www.credit-agricole.pl/klienci-indywidualni/karty-kredytowe"
EGVISA = "https://www.ca-egypt.com/en/news/credit-agricole-egypt-and-visa-renew-their-partnership"
CAPS = "https://presse.credit-agricole.com/section/ca-payment-services"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · heritage · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: €8.8 billion of group profit in 2025, CET1 of 17.2% at 30 June 2026, a cooperative owned by 12.3 million mutual shareholders since 1894, €500 million for AI and the ACT 2028 plan with a push into Germany.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & results", "blurb": "€8.8bn profit, 55m customers.", "div": "group", "rev": "cc", "products": [
            P("results", "Results & capital", "Group net income of €8,754 million in 2025 and €2,778 million in Q2 2026; Crédit Agricole S.A. earned €7,074 million in 2025 (RoTE 13.5%) and €2,051 million in Q2 2026 (RoTE 14.3%, cost/income 52.6%); CET1 of 17.2% for the group and 11.3% for Crédit Agricole S.A. at 30 June 2026.",
              s=["con", "corp"], neo=[0, ""], src=[["Q2 2026 results", PRQ2], ["FY2025 results", PRFY]]),
            P("customers", "Customers & reach", "55 million customers, 160,000 employees and 8,065 branches in 46 countries; ninth-largest bank in the world (The Banker 2026), first financier of the French economy and first retail bank in the EU by customers; 580,000 new retail customers in Q2 2026.",
              s=["con"], neo=[0, ""], src=[["Crédit Agricole Group", GROUP], ["IKB release, Oct 2026", IKB], ["Q2 2026 results", PRQ2]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Ownership & leadership", "blurb": "Regional Banks own 63.5%.", "div": "group", "rev": "cc", "products": [
            P("ownership", "Ownership & ratings", "The Regional Banks own 63.5% of the listed Crédit Agricole S.A. through SAS Rue La Boétie; shares at €15.72 in October 2026, a market value of about €47 billion ⚠ estimate; counterparty ratings AA- (S&P), Aa3 (Moody's) and AA- (Fitch), all stable.",
              s=["corp"], neo=[0, ""], src=[["Q2 2026 results", PRQ2], ["Debt and ratings", RAT]]),
            P("leadership", "Board & executive committee", "Chairman Eric Vial, CEO Olivier Gavalda (since May 2025), Deputy CEO Jérôme Grivet; deputy general managers Clotilde L'Angevin (finance), Gérald Grégoire (customers, development and innovation, including payments), Stéphane Priami (international and CAPFM) and Grégory Erphelin (transformation); Philippe Marquetty runs CA Payment Services.",
              s=["corp"], neo=[0, ""], src=[["Governance", GOV]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage", "blurb": "Local banks since 1894.", "div": "rb", "rev": "retail", "products": [
            P("heritage", "Heritage", "First local agricultural bank at Salins-les-Bains in 1885; Local Banks created by the Act of 5 November 1894 and Regional Banks in 1899; the central body (CNCA) bought by the Regional Banks in 1988 and listed as Crédit Agricole S.A. in 2001; LCL is the second French network.",
              s=["con"], o="I", neo=[0, ""], src=[["History", HIST]]),
        ]},
        {"id": "1.4", "ic": "brain", "name": "Technology & AI", "blurb": "€500m and an AI company.", "div": "group", "rev": "cc", "products": [
            P("aiplatform", "Crédit Agricole Artificial Intelligence", "€500 million over 2026–28 from the ACT 2028 IT budget, including €150 million of capital for a new AI company of 150 staff from September 2026, and an industrial agentic platform from the end of Q3 2026 with productivity and customer-facing agents, built on European technology where possible.",
              s=["con", "corp"], st="new", ay="Jul 2026", o="B", neo=[0, ""],
              mc="Customer-facing agents will need agentic payment credentials; the group used Agent Pay in June 2026.",
              src=[["Q2 2026 results", PRQ2], ["Q2 2026 slides", SLQ2]]),
            P("cagip", "CA-GIP & data marketplace", "Crédit Agricole Group Infrastructure Platform runs the group's IT production under Olivier Biton; ACT 2028 adds a group data marketplace, a shared KYC platform and a target to halve time-to-market.",
              s=["corp"], o="B", neo=[0, ""], src=[["Governance", GOV], ["ACT 2028: Transformation", ACTT], ["FY2025 results", PRFY]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "ACT 2028, Germany, IKB.", "div": "group", "rev": "cc", "products": [
            P("act2028", "ACT 2028", "Crédit Agricole S.A. targets for 2028: revenue above €30 billion, net income above €8.5 billion, cost/income below 55% and RoTE above 14%; 8 million new customers in France, 1 million more business customers and first bank for young people.",
              s=["corp"], neo=[0, ""], src=[["FY2025 slides", SLFY], ["FY2025 results", PRFY], ["ACT 2028: Acceleration", ACTA]]),
            P("deals", "Deals", "Banco BPM stake raised to 29.3% (2026), Santander's CACEIS minority bought (2025), Degroof Petercam, Merca Leasing, Banque Thaler, Milleis (integrated 30 April 2026), a BCC-Grupo Cajamar partnership (2026) and IKB Deutsche Industriebank from Lone Star (signed 12 October 2026, closing due by end Q2 2027).",
              s=["corp"], o="A", st="flux", neo=[0, ""], src=[["Q2 2026 results", PRQ2], ["FY2025 results", PRFY], ["IKB release, Oct 2026", IKB]]),
            P("germany", "Germany: CA Savings & CA Deutschland", "A European digital savings platform launched in Germany in 2026 and Crédit Agricole Deutschland, a universal retail bank launched on 9 October 2026 on about one million existing German customers, aiming for two million by end-2028.",
              s=["con", "saver"], st="new", ay="Oct 2026", o="B", neo=[None, "Card network not announced."],
              mc="A new retail bank still choosing its card and payment stack ⚠.",
              src=[["CA Deutschland, Oct 2026", DEUT], ["Q2 2026 slides", SLQ2]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Regional Bank cards on Cartes Bancaires with Mastercard or Visa, LCL's mixed Visa and Mastercard range, Mastercard business cards, Visa in Italy and both schemes in Poland, Wero and the group's own mobile wallet, CAWL and CAPS for acquiring and processing, and a euro stablecoin.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Regional Bank cards", "blurb": "CB with Mastercard or Visa.", "div": "rb", "rev": "retail", "products": [
            P("racards", "Crédit Agricole cards", "All co-badged with Cartes Bancaires: Mastercard (€37.50), EKO Mastercard (€39), Mastercard or Visa Classic (€49.50), Mastercard Globe Trotter, Gold Mastercard or Visa Premier (€132), World Elite Mastercard or Visa Infinite (€330) and Mastercard Mozaïc for 10–17s; sociétaire Mastercard cards fund a local mutual fund; cards up 2% a year, premium 21% of stock.", short="Regional Bank cards (Mastercard-led, Visa alongside)",
              s=["con", "young"], lc="everyday", o="P", at="Mastercard, Visa, Cartes Bancaires", neo=[1, "Mastercard-led, Visa alongside, CB co-badged."],
              mc="Mastercard's largest French home: several tiers are Mastercard-only.",
              src=[["CA tariffs 2026 (Centre Ouest)", TARIFS], ["CA Mastercard memo", MEMO], ["Q2 2026 results", PRQ2]]),
            P("biometric", "Biometric Mastercard", "A fingerprint-sensor Gold Mastercard (€162) and World Elite Mastercard (€368); trialled with Mastercard and CAPS among 200 customers in Touraine and Poitou in June 2019 and rolled out from 2021 in about half the Regional Banks.", short="Biometric (Mastercard)",
              s=["con"], lc="everyday", ay="Jun 2019", o="P", at="Mastercard", neo=[2, "Mastercard."],
              src=[["Mastercard: biometric trial, Jun 2019", MCBIO], ["MoneyVox: biometric card, 2021", BIO], ["CA Toulouse 31, Mar 2022", TOULOUSE], ["CA tariffs 2026 (Centre Ouest)", TARIFS]]),
            P("cartwin", "Cartwin", "A card tied to both a current account and a revolving credit: Mastercard Cartwin and Gold Mastercard Cartwin (€49.50 and €132) with immediate or deferred debit, and Visa and Visa Premier Cartwin with fewer options.", short="Cartwin (Mastercard and Visa)",
              s=["con", "borrower"], lc="borrow", o="P", at="Mastercard, Visa", neo=[1, "Mastercard and Visa."], src=[["CA tariffs 2026 (Centre Ouest)", TARIFS]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "LCL cards", "blurb": "Visa and Mastercard.", "div": "lcl", "rev": "retail", "products": [
            P("lclcards", "LCL cards", "Visa Premier (€12.20 a month), Mastercard Platinum+ (€19.50), Visa Infinite (€30), Inventive Mastercard, Visa Cléo, Mouv by LCL for 10–17s ⚠ network not stated, a virtual card and a Visa revolving-credit card.", short="LCL cards (Visa and Mastercard)",
              s=["con"], lc="everyday", o="P", at="Visa, Mastercard", neo=[1, "Mixed; Visa at the top tier."], src=[["LCL: cards", LCL]]),
        ]},
        {"id": "2.3", "ic": "briefcase", "name": "Business cards", "blurb": "Mastercard only.", "div": "rb", "rev": "retail", "products": [
            P("procards", "Professional & business cards", "Mastercard Professionnel, Mastercard Business and Mastercard Business World for professionals, farmers and companies, with Apple Pay Pro; no Visa business card listed.", short="Business cards (Mastercard)",
              s=["sme"], lc="move", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="A Mastercard-only book the group wants to grow by 1 million business customers.",
              src=[["CA professionals", PRO], ["FY2025 results", PRFY]]),
        ]},
        {"id": "2.4", "ic": "earth", "name": "Italy, Poland & Egypt cards", "blurb": "Visa in Italy, split in Poland.", "div": "italia", "rev": "retail", "products": [
            P("italiacards", "CA Italia cards", "Carta Crédit Agricole Visa debit and a Bancomat card, a recyclable digital Visa Debit from the July 2021 Visa partnership, credit cards issued with Nexi ⚠ scheme not stated, and American Express Platino and business cards.", short="CA Italia (Visa debit)",
              s=["con"], lc="everyday", ay="Jul 2021", o="P", at="Visa, Nexi, American Express", neo=[0, "Visa debit; Nexi credit scheme not stated."],
              src=[["CA Italia: cards", ITCARDS], ["Le Petit Journal: CA Italia and Visa, Jul 2021", ITVISA]]),
            P("polskacards", "CA Bank Polska cards", "Visa Standard, Mastercard Standard, Mastercard and Visa Silver (former Decathlon, Auchan and Leroy Merlin cards), Visa and Mastercard Gold, and Mastercard Maxima earning points in Bezcenne Chwile; Apple Pay, Google Pay, Garmin Pay and Xiaomi Pay.", div="intl", short="Poland (Visa and Mastercard)",
              s=["con"], lc="borrow", o="P", at="Visa, Mastercard", neo=[1, "Visa and Mastercard ⚠ debit not checked."], src=[["CA Polska: credit cards", PLCARDS]]),
            P("egyptcards", "CA Egypt cards", "A Visa partnership renewed for five years in 2021, extending 17 years of cooperation ⚠ Mastercard presence not checked.", div="intl",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["CA Egypt: Visa renewal, 2021", EGVISA]]),
        ]},
        {"id": "2.5", "ic": "smartphone", "name": "Wero & mobile payments", "blurb": "5m Wero users; own iPhone wallet.", "div": "caps", "rev": "retail", "products": [
            P("wero", "Wero", "EPI's account-to-account wallet, offered to all Crédit Agricole customers from October 2024; nearly 5 million customers of the Regional Banks and LCL used it each month by September 2025; free in Ma Banque; e-commerce expected in 2026 ⚠ launch date at Crédit Agricole not confirmed.",
              s=["con", "young"], lc="move", st="new", ay="Oct 2024", o="P", at="EPI", neo=[0, "EPI's own."],
              mc="The European wallet the group co-owns, aimed at e-commerce and shops.",
              src=[["EPI: Wero one year, Sep 2025", WERO], ["CA tariffs 2026 (Centre Ouest)", TARIFS], ["Économie Matin: Wero online, May 2026", BPCEWERO]]),
            P("paiementmobile", "Paiement Mobile", "The group's own contactless app, on Android and from 23 June 2026 on iPhone through the NFC access opened by the EU Digital Markets Act; the customer chooses CB, Mastercard or Visa per card; Apple Pay is kept alongside.", short="Paiement Mobile (CB, Mastercard, Visa)",
              s=["con"], lc="everyday", st="new", ay="Jun 2026", o="B", neo=[1, "Carries Mastercard among three schemes ⚠ token service not stated."],
              mc="A bank-owned wallet that still needs token and provisioning services.",
              src=[["Next.ink: iPhone app, Jun 2026", IOS], ["Q2 2026 slides", SLQ2]]),
            P("wallets", "Apple Pay & Google Pay", "Apple Pay opened to Crédit Agricole on 28 January 2020 on CB first, with Visa and Mastercard to follow; LCL lists Apple Pay, Google Pay, Wero and its own Android payment app.",
              s=["con"], lc="everyday", ay="Jan 2020", o="P", at="Apple, Google", neo=[None, "Token service not stated."], src=[["Consomac: Apple Pay, Jan 2020", APPLEPAY], ["LCL: cards", LCL]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Acquiring & processing", "blurb": "CAWL, Up2pay, CAPS.", "div": "caps", "rev": "retail", "products": [
            P("cawl", "CAWL", "Merchant terminals and e-commerce acceptance for clients of the Regional Banks and LCL, set up with Worldline in 2023; it won a significant number of large-merchant tenders, and Crédit Agricole became sole owner on 30 June 2026, with Worldline kept as a supplier.",
              s=["sme", "corp"], lc="move", st="flux", ay="Jun 2026", o="A", at="Worldline", neo=[None, "Schemes accepted not stated ⚠."],
              mc="A newly wholly owned acquirer choosing its own risk and checkout tools.",
              src=[["Worldline: CAWL, Jun 2026", WLCAWL], ["CAWL", CAWL]]),
            P("up2pay", "Up2pay", "Up2pay mobile and Up2pay caisse digitale for small merchants, alongside CAWL terminals.",
              s=["sme"], lc="move", o="B", neo=[None, "Nothing public."], src=[["CA professionals", PRO]]),
            P("caps", "CA Payment Services", "Runs the group's payment strategy, processing platforms, operations, transaction security and scheme representation, and holds an ACPR payment-institution licence ⚠ volumes not published.", short="CAPS processing",
              s=["corp"], lc="move", o="B", neo=[1, "Processes Mastercard among other schemes."], src=[["CA Payment Services", CAPS]]),
            P("amexaccept", "American Express acceptance", "A national partnership signed in October 2023 for Crédit Agricole merchants to accept American Express.",
              s=["sme"], lc="move", ay="Oct 2023", o="P", at="American Express", neo=[0, "American Express."], src=[["Crédit Agricole: Amex partnership, Oct 2023", AMEX]]),
        ]},
        {"id": "2.7", "ic": "coins", "name": "Digital money", "blurb": "Stablecoin and tokens.", "div": "large", "rev": "lc", "products": [
            P("stablecoin", "Euro stablecoin", "A euro-pegged stablecoin named EURXT (Euro eXchange Token), launched in 2026 ⚠ issuer and scale not stated.",
              s=["corp"], lc="move", st="new", o="B", neo=[0, ""], src=[["Q2 2026 slides", SLQ2]]),
            P("tokenised", "Tokenised finance", "Amundi's first tokenised fund with CACEIS, and support for a fund subscribing to a natively tokenised IPO on the LISE blockchain.",
              s=["corp", "saver"], lc="grow", st="new", o="B", neo=[0, ""], src=[["FY2025 results", PRFY], ["Q2 2026 slides", SLQ2]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: France's first agentic payment on Mastercard Agent Pay, a Digital Trust line and shared KYC, AI agents for customers, and premium card benefits with Priceless in Poland.",
    "tiles": [
        {"id": "3.1", "ic": "bot", "name": "Agentic commerce", "blurb": "First in France, on Agent Pay.", "div": "caps", "rev": "retail", "products": [
            P("agentpay", "Agentic payment", "On 25 June 2026 Crédit Agricole, Mastercard and Worldline ran France's first agentic payment in production: an AI agent bought festival tickets on Weezevent in a journey defined with Mastercard Agent Pay, with Crédit Agricole as issuer handling authentication and authorisation; named: Philippe Marquetty (CAPS) and Barbara Sessa (Mastercard France).", short="Agent Pay (Mastercard)",
              s=["con"], lc="move", st="new", ay="Jun 2026", o="P", at="Mastercard, Worldline", neo=[3, "Mastercard Agent Pay."],
              mc="The newest joint work, and the partners talk of a European roll-out.",
              src=[["Worldline: agentic payment, Jun 2026", WLAGENT], ["Crowdfund Insider, Jul 2026", CFIAGENT], ["Mastercard: Agent Pay, Apr 2025", MAAP]]),
            P("agents", "Customer-facing AI agents", "The industrial agentic platform includes agents that interact with customers and agents staff can build themselves.",
              s=["con"], lc="everyday", st="new", o="B", neo=[0, ""], src=[["Q2 2026 slides", SLQ2]]),
        ]},
        {"id": "3.2", "ic": "shield-check", "name": "Fraud & digital trust", "blurb": "CAPS security, shared KYC.", "div": "caps", "rev": "cc", "products": [
            P("fraud", "Transaction security", "CAPS guarantees the security of card and payment transactions for the group's banks; biometric cards remove PIN entry above the contactless limit ⚠ no Mastercard fraud product named in public sources.",
              s=["con", "sme"], lc="everyday", o="B", neo=[None, "Nothing public."],
              mc="Wero and instant payments need scam scoring the card rules do not give.",
              src=[["CA Payment Services", CAPS], ["MoneyVox: biometric card, 2021", BIO]]),
            P("digitaltrust", "Digital Trust & shared KYC", "ACT 2028 creates a shared KYC platform and a Digital Trust business line as new group activities.",
              s=["corp"], lc="open", st="new", o="B", neo=[0, ""], src=[["ACT 2028: Transformation", ACTT]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Card benefits & loyalty", "blurb": "Premium cards, Priceless.", "div": "rb", "rev": "retail", "products": [
            P("premium", "Premium cards", "Gold Mastercard, Visa Premier, World Elite Mastercard and Visa Infinite rose to 21% of Regional Bank cards by June 2026 (19.2% at end-2025), sold in Premium and Prestige packages.", short="Premium (Mastercard and Visa)",
              s=["con"], lc="everyday", o="P", at="Mastercard, Visa", neo=[1, "World Elite and Gold beside Visa Premier and Infinite."],
              src=[["Q2 2026 results", PRQ2], ["FY2025 results", PRFY], ["CA tariffs 2026 (Centre Ouest)", TARIFS]]),
            P("priceless", "Bezcenne Chwile", "Mastercard's Priceless programme in Poland, where Mastercard Maxima credit cards earn points exchangeable for vouchers.", div="intl", short="Priceless (Poland)",
              s=["con"], lc="grow", o="P", at="Mastercard", neo=[3, "Mastercard Priceless."], src=[["CA Polska: credit cards", PLCARDS]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: the Regional Banks' €665 billion of loans, LCL, BforBank, CA Italia and banks in Poland, Egypt and Ukraine, €124 billion of consumer and mobility finance, leasing, CACIB and CACEIS, and €3.3 trillion of savings and insurance assets.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Retail banking in France", "blurb": "22.9% of French credit.", "div": "rb", "rev": "retail", "products": [
            P("regional", "Regional Banks", "Loans of €665 billion and customer assets of €957 billion at 30 June 2026; 22.9% of French credit and 20.5% of deposits (Banque de France, April 2026); 300,000 new customers in Q2 2026; home loans up 11.7%.",
              s=["con", "sme", "farm"], lc="borrow", neo=[1, "Cards Mastercard-led with Visa."], src=[["Q2 2026 results", PRQ2]]),
            P("lclbank", "LCL", "Loans of €175 billion and customer assets of €277.5 billion, including €12 billion from Milleis; 76,000 new customers in Q2 2026; positioned as the bank for entrepreneurs, with L by LCL Pro digital banking.", div="lcl",
              s=["con", "sme"], lc="everyday", neo=[1, "Mixed Visa and Mastercard."], src=[["Q2 2026 results", PRQ2], ["FY2025 results", PRFY], ["ACT 2028: Acceleration", ACTA]]),
            P("bforbank", "BforBank", "The group's digital bank, positioned for digital savings, with a new chief executive from June 2026 ⚠ card scheme not checked.", div="group",
              s=["saver"], lc="open", neo=[None, "Not checked."], src=[["ACT 2028: Acceleration", ACTA], ["Governance", GOV]]),
        ]},
        {"id": "4.2", "ic": "flag", "name": "Italy & international", "blurb": "6m clients in Italy.", "div": "italia", "rev": "retail", "products": [
            P("caitalia", "Crédit Agricole Italia", "More than 6 million clients; loans of €63.6 billion and customer assets of €124.4 billion at 30 June 2026; 52,000 new customers in Q2 2026, 38% online; a mid-corporate platform with CACIB.",
              s=["con", "sme"], lc="everyday", neo=[0, "Visa debit."], src=[["Q2 2026 results", PRQ2], ["IKB release, Oct 2026", IKB]]),
            P("intlretail", "Poland, Egypt & Ukraine", "Loans of €8.0 billion outside Italy; 61,000 new customers in Poland in Q2 2026; loans up 27% in Egypt and 33.8% in Ukraine.", div="intl",
              s=["con", "sme"], lc="borrow", neo=[1, "Poland split; Egypt Visa."], src=[["Q2 2026 results", PRQ2]]),
        ]},
        {"id": "4.3", "ic": "hand-coins", "name": "Consumer finance & mobility", "blurb": "€124bn managed.", "div": "capfm", "rev": "sfs", "products": [
            P("capfm", "CA Personal Finance & Mobility", "Sofinco, Agos, CA Auto Bank and Leasys ⚠ joint-venture partner not re-verified: production of €12.8 billion in Q2 2026 and €124.3 billion under management; used-car margins at Leasys weighed on results.",
              s=["borrower"], lc="borrow", neo=[None, "Card schemes not stated."],
              mc="Fleet and mobility payments at Leasys and CA Auto Bank are untested ground.",
              src=[["Q2 2026 results", PRQ2]]),
            P("leasing", "Leasing & factoring", "CA Leasing & Factoring: leasing production up 15.2% in Q2 2026 and €22.2 billion of leasing outstandings, with Merca Leasing in Germany.", div="group",
              s=["sme", "corp"], lc="borrow", neo=[0, ""], src=[["Q2 2026 results", PRQ2]]),
        ]},
        {"id": "4.4", "ic": "factory", "name": "Corporate & investment banking", "blurb": "CACIB and CACEIS.", "div": "large", "rev": "lc", "products": [
            P("cacib", "Crédit Agricole CIB", "Revenue of €1,780 million in Q2 2026 (+4.4%); second in euro green, social and sustainable bonds; with LCL, a programme for European mid-caps and, from 2027, IKB's German Mittelstand clients.",
              s=["corp"], lc="borrow", neo=[0, ""],
              mc="Commercial and virtual cards for mid-corporates are not in public view.",
              src=[["Q2 2026 results", PRQ2], ["IKB release, Oct 2026", IKB]]),
            P("caceis", "CACEIS", "Asset servicing with €6,190 billion under custody and €3,871 billion under administration at 30 June 2026.",
              s=["corp"], lc="grow", neo=[0, ""], src=[["Q2 2026 results", PRQ2]]),
        ]},
        {"id": "4.5", "ic": "gem", "name": "Savings, insurance & wealth", "blurb": "€3.3tn of assets.", "div": "large", "rev": "ag", "products": [
            P("amundi", "Amundi", "Europe's largest asset manager with €2,581 billion under management and €24 billion of net inflows in Q2 2026.",
              s=["saver"], lc="grow", neo=[0, ""], src=[["Q2 2026 results", PRQ2], ["Crédit Agricole Group", GROUP]]),
            P("assurances", "Crédit Agricole Assurances", "First insurer in France: record savings inflows of €6.1 billion net in Q2 2026 and 18.2 million property and casualty policies.", div="group",
              s=["saver", "con"], lc="beyond", neo=[0, ""], src=[["Q2 2026 results", PRQ2]]),
            P("indosuez", "Indosuez Wealth Management", "Private banking with Degroof Petercam and Banque Thaler; €317 billion of wealth assets.", div="group",
              s=["saver"], lc="grow", o="A", neo=[0, ""], src=[["Q2 2026 results", PRQ2]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: the Ma Banque and LCL apps, 8,065 branches, and partners from Worldline and Nexi to Banco BPM.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Apps", "blurb": "Ma Banque and LCL.", "div": "rb", "rev": "retail", "products": [
            P("apps", "Ma Banque & LCL apps", "Ma Banque and Crédit Agricole En Ligne for Regional Bank customers, with Wero and the Paiement Mobile wallet; LCL's app for its customers; 38% of new CA Italia customers join online ⚠ app user numbers not published.",
              s=["con", "young"], lc="everyday", neo=[0, ""], src=[["CA tariffs 2026 (Centre Ouest)", TARIFS], ["LCL: cards", LCL], ["Q2 2026 results", PRQ2]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches", "blurb": "8,065 branches.", "div": "rb", "rev": "retail", "products": [
            P("branches", "Branches & advisers", "8,065 branches worldwide, most of them in the Regional Banks and LCL in France, run with 27,165 elected administrators of local and regional banks.",
              s=["con", "farm"], lc="open", neo=[0, ""], src=[["Crédit Agricole Group", GROUP], ["IKB release, Oct 2026", IKB]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partners", "blurb": "Worldline, Nexi, Banco BPM.", "div": "group", "rev": "cc", "products": [
            P("partners", "Partners", "Worldline (acceptance for CAWL), Nexi (Italian credit cards), American Express, Apple, Banco BPM (29.3%), BCC-Grupo Cajamar and Crelan.",
              s=["sme", "con"], lc="open", o="P", neo=[1, "Mastercard in agentic payments and cards, not a named strategic partner."], src=[["Worldline: CAWL, Jun 2026", WLCAWL], ["CA Italia: cards", ITCARDS], ["Q2 2026 results", PRQ2], ["FY2025 results", PRFY]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Crédit Agricole", "blurb": "The lead scheme on the Regional Banks' cards.", "products": [
        P("mcatca", "Mastercard at Crédit Agricole", "Mastercard is the lead international scheme on the Regional Banks' cards, co-badged with Cartes Bancaires, with Mastercard-only tiers, biometric cards and business cards, and Visa offered alongside; LCL is mixed, CA Italia debit is Visa and Poland is split with Priceless. In June 2026 the group ran France's first agentic payment on Agent Pay. No group network contract is public.",
          s=["con"], div="group", rev="cc", mc="The relationship this map is drawn for.",
          src=[["CA tariffs 2026 (Centre Ouest)", TARIFS], ["CA professionals", PRO], ["Worldline: agentic payment, Jun 2026", WLAGENT]]),
    ]},
    {"id": "pillar-market", "name": "French payments", "blurb": "CB, Wero, the DMA.", "products": [
        P("market", "The market", "Cartes Bancaires carries most domestic card payments; its share in the Yavin index fell from 89.6% in H2 2021 to 61.4% in H1 2025, then rose to 63.6% in H2 2025; Wero had 43.5 million users in September 2025 and is moving into e-commerce; the EU Digital Markets Act opened iPhone NFC to banks.",
          s=["con"], div="group", rev="cc", src=[["MoneyVox: CB share, Mar 2026", CBSHARE], ["EPI: Wero one year, Sep 2025", WERO], ["Next.ink: iPhone app, Jun 2026", IOS]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
