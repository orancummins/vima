"""UniCredit's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the 2Q26 results (23 July 2026), the FY25 results
(9 February 2026) and the 2025 Annual Report. ``neo`` is the Mastercard lens: [depth, note], where
3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

Q2PR = "https://www.unicreditgroup.eu/content/dam/unicreditgroup-eu/documents/en/investors/group-results/2026/2Q26/2Q26_UniCredit_PR_ENG.pdf"
Q2 = "https://www.unicreditgroup.eu/content/dam/unicreditgroup-eu/documents/en/investors/group-results/2026/2Q26/2Q26_Results.pdf"
FY25 = "https://www.emarketstorage.it/sites/default/files/comunicati/2026-02/20260209_177268.pdf"
AR25 = "https://www.unicreditgroup.eu/content/dam/unicreditgroup-eu/documents/en/investors/financial-reports/2025/4q25/2025-Annual-Reports-and-Accounts.pdf"
CBKOFFER = "https://www.unicreditgroup.eu/content/dam/unicreditgroup-eu/documents/en/investors/unicredit-unlimited-next-phase/PR_UniCredit-exchange-offer-Commerzbank-_16032026.pdf"
CBKRESULT = "https://www.unicreditgroup.eu/content/dam/unicreditgroup-eu/documents/en/investors/unicredit-unlimited-next-phase/Announcement-pursuant-to-Section-23-para.-1-sentence-1-no.-3-of-the-German-Securities-Acquisition-and-Takeover-Act-(WpUeG)-dated-8-July-2026.pdf"
CBKCOND = "https://www.unicreditgroup.eu/content/dam/unicreditgroup-eu/documents/en/investors/unicredit-unlimited-next-phase/Announcement-regarding-the-fulfilment-of-offer-conditions-dated-16-October-2026.pdf"
CBKPR = "https://www.commerzbank.de/group/newsroom/press-releases/result-tender-offer-unicredit.html"
EXCO = "https://www.unicreditgroup.eu/en/governance/management.html"
BOARD = "https://www.unicreditgroup.eu/en/governance/governance-bodies/board-of-directors.html"
RATINGS = "https://www.unicreditgroup.eu/content/unicreditgroup-eu/en/investors/debt-investors/credit-ratings.html"
MCDEAL = "https://insurancenewsnet.com/oarticle/unicredit-and-mastercard-expand-payments-partnership-10"
CARDS = "https://www.unicredit.it/it/privati/carte.html"
HVBCARD = "https://www.hypovereinsbank.de/hvb/privatkunden/banking-im-alltag/karten/debitkarte-unicredit-card"
HVBPAY = "https://www.hypovereinsbank.de/hvb/services/digitales-banking/apple-pay"
BUDDY = "https://www.unicredit.it/it/privati/buddy/modello-buddy.html"
DIGITAL = "https://www.unicredit.it/it/privati/servizi-digitali/tutti-i-servizi.html"
SOLUTIONS = "https://www.unicreditgroup.eu/content/unicreditgroup-eu/en/strategy/business/client-solutions.html"
QUOTE = "https://www.borsaitaliana.it/borsa/azioni/scheda/IT0005239360.html?lang=en"
SIA = "https://www.aziendabanca.it/notizie/unicredit-sia-rinnovo-processing"
BUDDYBANK = "https://www.fintechfutures.com/baas/buddybank-finally-opens-for-business"
ALPHA = "https://news.bloomberglaw.com/banking-law/unicredit-converts-alpha-bank-stake-to-direct-holding-of-29-8"
JCB = "https://www.electronicpaymentsinternational.com/news/jcb-partners-with-unicredit-for-merchant-acquiring-business-in-italy-070316-4830344"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · banks · plan", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: €443 billion of loans and a 21.7% return in the second quarter of 2026, 13 banks across Europe, a Google Cloud and Vodeno technology base, the UniCredit Unlimited plan and a 49.65% position in Commerzbank.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "RoTE 21.7% in 2Q26.", "div": "ucg", "rev": "group", "products": [
            P("balance", "Balance sheet & earnings", "Customer loans of €442.6 billion and deposits of €503.8 billion at 30 June 2026; net profit of €2.91 billion in 2Q26 (RoTE 21.7%) and €10.6 billion in 2025; CET1 14.3%; cost/income 35.2%; rated A-/A3/A-; share price €76.19 on 16 October 2026, a market value of about €115 billion ⚠ (estimate).",
              s=["con"], neo=[0, ""], src=[["2Q26 results release", Q2PR], ["FY25 results release", FY25], ["UniCredit: credit ratings", RATINGS], ["Borsa Italiana: UCG", QUOTE]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Orcel and Padoan.", "div": "ucg", "rev": "group", "products": [
            P("leadership", "Board & executive committee", "Chair Pietro Carlo Padoan and a 15-member board; CEO Andrea Orcel, who also heads Italy; Richard Burton runs Group Client Solutions, where payments, acquiring and issuing sit; Ali Khan Digital & Information; Marion Höllinger Germany; Teodora Petkova CEE. 67,118 staff (FTE) at the end of 2025.",
              s=["corp"], neo=[0, ""], src=[["UniCredit: executive committee", EXCO], ["UniCredit: board", BOARD], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Banks & brands", "blurb": "13 banks, one group.", "div": "ucg", "rev": "group", "products": [
            P("brands", "Banks & brands", "13 banks: UniCredit in Italy and CEE, HypoVereinsbank (UniCredit Bank GmbH) in Germany, UniCredit Bank Austria, UniCredit Bulbank ⚠, UniCredit Bank Romania (merged with Alpha Bank Romania in August 2025), buddy, onemarkets and UniCredit NV/SA; 2025 marked 20 years of UniCredit and HypoVereinsbank. Roots in Credito Italiano (1870) ⚠.",
              s=["con"], o="I", neo=[0, ""], src=[["2025 Annual Report", AR25]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Cloud, core & AI", "blurb": "Google Cloud for 13 banks.", "div": "ucg", "rev": "group", "products": [
            P("cloud", "Cloud & infrastructure", "A Google Cloud partnership (May 2025) moving all 13 banks, with Vertex AI and Gemini as the main AI platform; a stronger IBM partnership and a new infrastructure model with Accenture; trading centralised on Murex.",
              s=["corp"], o="P", at="Google Cloud, IBM, Accenture", neo=[0, ""], src=[["2Q26 results presentation", Q2], ["2025 Annual Report", AR25]]),
            P("vodeno", "Vodeno core banking", "A cloud-native core bought with Aion Bank for €376 million (closed 6 March 2025), for embedded finance and banking-as-a-service and the base for re-entering Poland.",
              s=["corp", "sme"], lc="open", st="new", ay="Mar 2025", o="A", neo=[0, ""], src=[["2025 Annual Report", AR25]]),
            P("aiplatform", "AI platform & governance", "More than 35 AI applications in production in 2025 and a move to agentic AI, about 1,100 data and AI staff, and responsible-AI governance aligned with the EU AI Act.",
              s=["corp"], st="new", neo=[0, ""], src=[["2025 Annual Report", AR25]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Unlimited & Commerzbank", "blurb": "49.65% of Commerzbank.", "div": "ucg", "rev": "group", "products": [
            P("strategy", "UniCredit Unlimited", "The 2026–28 plan, building to 2030 (9 February 2026): net revenue about €27.5 billion and cost/income about 33% in 2028, RoTE above 23%, and about €30 billion of distributions over three years. 2026 net profit guided to about €11.5 billion before integration costs.",
              s=["corp"], st="new", neo=[0, ""], src=[["FY25 results release", FY25], ["2Q26 results release", Q2PR]]),
            P("cbk", "Commerzbank", "An exchange offer at 0.485 UniCredit shares per Commerzbank share (16 March 2026) brought in 17.60% on top of a 26.77% holding; an overall position of 49.65% with swaps. ECB and BaFin cleared entities including EURO Kartensysteme (girocard) and Commerz Globalpay (acquiring) on 15–16 October 2026; some approvals remain, possibly as early as 4Q26. Commerzbank says it stays 'open to constructive dialogue'.",
              s=["con", "sme", "corp"], st="flux", ay="Mar 2026", o="A", neo=[None, "Commerzbank's card networks not public here ⚠."],
              mc="The largest card-network decision ahead: about 17 million more retail customers in Germany and Poland.",
              src=[["Commerzbank offer, Mar 2026", CBKOFFER], ["Acceptance result, Jul 2026", CBKRESULT], ["Offer conditions, Oct 2026", CBKCOND], ["Commerzbank: tender result", CBKPR]]),
            P("deals", "Other deals", "Alpha Bank Romania (90.1%, November 2024), the Italian life joint ventures (June 2025), Bank Austria's 50.1% of card complete sold (September 2025), Alpha Bank in Greece at about 29.8% (January 2026), 2,500 Austrian merchants bought from First Data (2026); the Banco BPM offer was withdrawn in July 2025 ⚠ and a Generali stake built and cut ⚠.",
              s=["corp"], o="A", neo=[0, ""], src=[["2025 Annual Report", AR25], ["Bloomberg Law: Alpha Bank 29.8%", ALPHA], ["2Q26 results presentation", Q2]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "How money moves: a 2023 Mastercard deal for about 20 million cards across 13 banks, Mastercard debit at HVB and on most Italian credit and prepaid cards, girocard and some Visa debit alongside, in-house acquiring in Austria, instant and account-to-account payments, and the Qivalis euro stablecoin.",
    "tiles": [
        {"id": "2.1", "ic": "network", "name": "Group card deal", "blurb": "Mastercard for 13 banks.", "div": "ucg", "rev": "group", "products": [
            P("mcdeal", "Mastercard multi-market agreement", "One agreement (26 May 2023) covering 13 banks in 12 markets, about 20 million cards and 'all card products', with Priceless, sponsorship and ESG work; since then new products in 12 markets, card transactions up 20% and a 2:3 card-to-cash ratio. The end date is not public.", short="Mastercard group deal",
              s=["con", "sme"], lc="everyday", ay="May 2023", o="P", at="Mastercard", neo=[2, "Group-wide issuing partner since 2023."],
              mc="Billed as the first strategy of this scale by a large European commercial bank.",
              src=[["UniCredit and Mastercard, May 2023", MCDEAL], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Italy debit & prepaid", "blurb": "MyOne and Genius Pay.", "div": "italy", "rev": "italy", "products": [
            P("myone", "MyOne debit", "The international debit card in Genius and buddy accounts, issued 'on the Mastercard or VISA network', with a custom PIN; the split between the two is not disclosed.", short="MyOne (Mastercard or Visa)",
              s=["con"], lc="everyday", o="P", at="Mastercard, Visa", neo=[1, "Mastercard or Visa; split not disclosed."],
              mc="The remaining Visa share of Italian debit is open ground.",
              src=[["UniCredit: cards", CARDS]]),
            P("geniuspay", "Genius Pay & Genius Pay buddy", "IBAN-linked prepaid cards 'issued on the Mastercard network', digital-first in the app, including a version for 11–17-year-olds.", short="Genius Pay (Mastercard)",
              s=["young", "con"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["UniCredit: cards", CARDS]]),
            P("geniuscard", "Genius Card & Card Click", "IBAN-linked Genius Card (and a WWF version) and Card Click, an e-commerce prepaid card that needs no account; network not stated on the pages ⚠.",
              s=["con", "young"], lc="everyday", o="B", neo=[None, "Network not stated ⚠."], src=[["UniCredit: cards", CARDS]]),
        ]},
        {"id": "2.3", "ic": "credit-card", "name": "Italy credit", "blurb": "Flexia and Ferrari.", "div": "italy", "rev": "italy", "products": [
            P("flexia", "Flexia Classic, Etica, WWF & Giovani", "Credit cards with optional repayment and 3–20 instalments in the app; €43 a year, limits of €1,500–5,000; the Etica and WWF versions donate 2‰ and 3‰ of spending. Network not stated on the page ⚠.",
              s=["con"], lc="borrow", o="B", neo=[None, "Network not stated ⚠."],
              mc="Instalments are UniCredit's own; no Mastercard Installments link was found.",
              src=[["UniCredit: cards", CARDS]]),
            P("flexiagold", "Flexia Gold & Miles & More", "Gold credit cards with Mastercard Travel Rewards cashback and a Miles & More co-brand; €100 a year, revolving APR 19.39%.", short="Flexia Gold (Mastercard)",
              s=["con", "inv"], lc="borrow", o="P", at="Mastercard, Miles & More", neo=[2, "Mastercard, with Travel Rewards."], src=[["UniCredit: cards", CARDS]]),
            P("ferrari", "UniCredit Scuderia Ferrari Metal Card", "A premium Mastercard credit card (2025) with Priceless, Reserved and Travel Rewards benefits and more than 1,700 lounges, launched with Lewis Hamilton and Charles Leclerc.", short="Ferrari Metal (Mastercard)",
              s=["inv"], lc="borrow", st="new", ay="2025", o="P", at="Mastercard, Scuderia Ferrari", neo=[2, "Mastercard premium credit."], src=[["2025 Annual Report", AR25]]),
        ]},
        {"id": "2.4", "ic": "wallet-cards", "name": "HVB cards (Germany)", "blurb": "Visa and Maestro out, Mastercard in.", "div": "hvb", "rev": "germany", "products": [
            P("ucard", "UniCredit Card (Mastercard debit)", "'The modern debit card from Mastercard', for private and business customers and free with the PlusKonto; activating it switches off the old HVB girocard with Maestro and the HVB Visa Debit Card. The switch date is not stated ⚠.", short="UniCredit Card (Mastercard)",
              s=["con", "sme"], lc="everyday", st="flux", o="P", at="Mastercard", neo=[2, "Mastercard debit, replacing Visa Debit and Maestro."],
              mc="A clear switch from Visa to Mastercard debit in Germany.",
              src=[["HVB: UniCredit Card", HVBCARD]]),
            P("girocard", "HVB girocard", "Still issued at €12 a year for domestic use, alongside the Mastercard debit card.",
              s=["con"], lc="everyday", o="I", neo=[0, "girocard, Germany's domestic scheme."], src=[["HVB: UniCredit Card", HVBCARD]]),
            P("hvbmc", "HVB Mastercard & Mastercard Gold", "Credit cards at €15 and €60–80 a year.", short="HVB Mastercard",
              s=["con"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["HVB: UniCredit Card", HVBCARD]]),
        ]},
        {"id": "2.5", "ic": "credit-card", "name": "Bank Austria cards", "blurb": "In-house since card complete.", "div": "ba", "rev": "austria", "products": [
            P("bacredit", "Bank Austria credit card", "A next-generation credit card issued in-house from March 2025, after Bank Austria sold its 50.1% of card complete in September 2025; network not stated ⚠.",
              s=["con"], lc="borrow", st="new", ay="Mar 2025", o="B", neo=[None, "Network not stated ⚠."], src=[["2025 Annual Report", AR25]]),
            P("touch", "Touch Card", "A tactile card for blind and partially sighted customers, launched with Mastercard in February 2025.", short="Touch Card (Mastercard)",
              s=["con"], lc="everyday", st="new", ay="Feb 2025", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["2025 Annual Report", AR25]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Acquiring", "blurb": "Austria in-house, Italy via Nexi.", "div": "ucg", "rev": "austria", "products": [
            P("baacq", "Bank Austria acquiring", "A POS and e-commerce platform built in-house (July 2025) with 'direct access to card schemes and digital wallets', plus 2,500 merchants, about 4,000 terminals and €750 million of volume bought from First Data (Fiserv).",
              s=["merch", "sme"], lc="move", st="new", ay="Jul 2025", o="B", neo=[1, "Accepts every network."],
              mc="An in-house acquirer that could take Mastercard's gateway, tokens and merchant Click to Pay.",
              src=[["2Q26 results presentation", Q2], ["2025 Annual Report", AR25]]),
            P("itacq", "Acquiring in Italy", "Accepts Mastercard, Visa, UnionPay and JCB (JCB from about 2016 ⚠); processing outsourced to SIA, now Nexi, in 2016, with talks in October 2020 to renew to 2036 across Italy, Austria and Germany ⚠.",
              s=["merch"], lc="move", o="P", at="Nexi (SIA)", neo=[1, "Accepts every network."], src=[["AziendaBanca: SIA renewal, Oct 2020", SIA], ["Electronic Payments International: JCB", JCB]]),
        ]},
        {"id": "2.7", "ic": "smartphone", "name": "Wallets & tokens", "blurb": "Apple, Google, BANCOMAT Pay.", "div": "ucg", "rev": "italy", "products": [
            P("wallets", "Digital wallets & Click to Pay", "Apple Pay, Google Pay and Samsung Pay in Italy, Germany and Austria, Apple Pay in Bosnia and Herzegovina (2025), BANCOMAT Pay in Italy, and Click to Pay with harmonised e-commerce across 12 markets (2023–25).",
              s=["con", "young"], lc="everyday", o="P", at="Apple, Google, Samsung, BANCOMAT", neo=[1, "Click to Pay and card tokens; BANCOMAT Pay is domestic."], src=[["HVB: Apple Pay", HVBPAY], ["UniCredit: digital services", DIGITAL], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "2.8", "ic": "arrow-left-right", "name": "Payments & cash management", "blurb": "100+ currencies, instant.", "div": "ucg", "rev": "group", "products": [
            P("gps", "Group Payments Solutions", "Cash management and payments in more than 100 currencies and UC PayFX; FAST international payments at 52% adoption in Italy; Payments Solutions revenue of €1.3 billion in 1H26 (+1.2%).",
              s=["corp", "sme"], lc="move", neo=[0, ""],
              mc="Correspondent and FAST flows are where Mastercard Move could fit.",
              src=[["UniCredit: Client Solutions", SOLUTIONS], ["2Q26 results presentation", Q2]]),
            P("instant", "Instant payments", "Live in the Czech Republic, Slovakia and Slovenia, a high-value platform in Hungary (2025) and revised Italian fees, under the EU Instant Payments Regulation with verification of payee.",
              s=["con", "sme"], lc="move", st="new", neo=[0, "SEPA instant."], src=[["2025 Annual Report", AR25]]),
            P("a2a", "AccountToPay, MyBank, CBILL & PagoPA", "Account-to-account and bill payments in Italy. Whether HVB, UniCredit Italy or Bank Austria have joined Wero is not known ⚠.",
              s=["con", "merch"], lc="move", neo=[0, "Domestic account-to-account."], src=[["UniCredit: digital services", DIGITAL]]),
        ]},
        {"id": "2.9", "ic": "coins", "name": "Digital money", "blurb": "Qivalis and the digital euro.", "div": "ucg", "rev": "group", "products": [
            P("qivalis", "Qivalis euro stablecoin", "A founder (September 2025) with ING, BNP Paribas, KBC, Danske, SEB, CaixaBank, RBI, DekaBank and Banca Sella; a Dutch e-money licence applied for and first issue targeted for 2H26. UniCredit calls it a 'European alternative' to US stablecoins.",
              s=["corp"], lc="move", st="new", ay="Sep 2025", o="P", at="Qivalis consortium", neo=[0, "Bank consortium."],
              mc="Mastercard's Multi-Token Network and stablecoin cards could link to it.",
              src=[["2025 Annual Report", AR25]]),
            P("deuro", "Digital euro, tokens & crypto", "'Actively contributing' to the digital euro pilot, tokenisation proofs of concept, and a crypto-linked certificate for retail customers in Austria and Croatia (1H26).",
              s=["con", "corp"], lc="grow", st="new", neo=[0, ""], src=[["2Q26 results presentation", Q2]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: HVB's new AI fraud platform and AI for KYC, more than 360 AI agents in Austria, and rewards from Mastercard's Priceless to HVB valyou.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & financial crime", "blurb": "AI fraud platform at HVB.", "div": "hvb", "rev": "germany", "products": [
            P("fraud", "Advanced Fraud Prevention & AI for KYC", "An AI-based fraud-prevention platform at HVB (1H26) and AI for KYC, corporate lending and transaction monitoring across the group; vendor not disclosed.",
              s=["con", "sme"], lc="everyday", st="new", neo=[None, "Vendor not disclosed."],
              mc="Instant payments raise push-payment scam risk; Mastercard's scam scoring could sit beside HVB's platform.",
              src=[["2Q26 results presentation", Q2]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI agents & assistants", "blurb": "360+ agents in Austria.", "div": "ucg", "rev": "group", "products": [
            P("aiagents", "AI agents & assistants", "More than 360 AI agents in use in Austria, an AI Fee Booster and Connect AI pilot in Hungary, a real-time assistant in the Bulgarian app, and generative-AI adviser support in Italy.",
              s=["con", "corp"], lc="everyday", st="new", neo=[0, ""],
              mc="No agentic payments use case is disclosed yet; Agent Pay is open ground.",
              src=[["2Q26 results presentation", Q2]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards & benefits", "blurb": "Priceless and valyou.", "div": "ucg", "rev": "italy", "products": [
            P("priceless", "Priceless per UniCredit & Travel Rewards", "Mastercard's Priceless experiences for UniCredit Mastercard holders, and Travel Rewards cashback on Flexia Gold and Miles & More cards.", short="Priceless (Mastercard)",
              s=["con", "inv"], lc="grow", o="P", at="Mastercard", neo=[3, "Mastercard's own programme."], src=[["UniCredit: cards", CARDS], ["UniCredit and Mastercard, May 2023", MCDEAL]]),
            P("valyou", "HVB valyou", "A tiered benefits programme for HVB customers; it still lists the HVB Visa Debit Card as a qualifying product.",
              s=["con"], lc="grow", neo=[0, "HVB's own."], src=[["HVB: UniCredit Card", HVBCARD]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy, by country: Italy (€2.32 billion of 1H26 profit), Germany through HVB, Austria and eight CEE markets, corporate and investment banking with trade finance, and onemarkets funds and insurance.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Italy", "blurb": "€2.32bn 1H26 profit.", "div": "italy", "rev": "italy", "products": [
            P("italy", "Banking in Italy", "1H26 net profit of €2.32 billion (RoAC 31.0%), €149.0 billion of loans and €185.8 billion of deposits; 1,941 branches; Valore Energia Più energy-efficiency loans.",
              s=["con", "sme"], lc="everyday", neo=[1, "Mastercard credit and prepaid; debit Mastercard or Visa."], src=[["2Q26 results release", Q2PR], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "4.2", "ic": "building-2", "name": "Germany (HVB)", "blurb": "#1 bank for SMEs.", "div": "hvb", "rev": "germany", "products": [
            P("hvb", "HypoVereinsbank", "1H26 net profit of €1.16 billion (RoAC 23.2%), €110.2 billion of loans; named best bank for SMEs in Germany (Euromoney, July 2026); the PlusKonto comes with the Mastercard debit card.",
              s=["con", "sme", "corp"], lc="everyday", neo=[2, "Mastercard debit."], src=[["2Q26 results presentation", Q2], ["HVB: UniCredit Card", HVBCARD]]),
            P("banxware", "Embedded SME lending with Banxware", "Instant loans of up to €250,000 inside partners' platforms, and FlexFinanzierung up to €5 million.",
              s=["sme"], lc="borrow", st="new", o="P", at="Banxware", neo=[0, ""], src=[["2025 Annual Report", AR25]]),
        ]},
        {"id": "4.3", "ic": "earth", "name": "Austria & CEE", "blurb": "Nine markets, 27% RoAC.", "div": "cee", "rev": "cee", "products": [
            P("austria", "Bank Austria", "1H26 net profit of €0.74 billion (RoAC 26.8%); issuing and acquiring brought in-house after card complete; micro and small businesses targeted.",
              s=["con", "sme"], lc="everyday", st="flux", neo=[1, "Touch Card on Mastercard; credit network not stated ⚠."], src=[["2Q26 results release", Q2PR], ["2025 Annual Report", AR25]]),
            P("cee", "Central & Eastern Europe", "1H26 net profit of €1.12 billion (RoAC 27.4%), €84.1 billion of loans, banks in Bulgaria, Croatia, the Czech Republic and Slovakia, Hungary, Romania (11% of assets), Serbia, Slovenia and Bosnia; a PRIME affluent model; Poland re-entered on the Vodeno platform. Network splits by country not public ⚠.",
              s=["con", "inv"], lc="everyday", neo=[None, "Mastercard likely primary under the 2023 deal ⚠."], src=[["2Q26 results release", Q2PR], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "4.4", "ic": "chart-candlestick", "name": "Corporate & investment banking", "blurb": "#1 in Italy, trade finance.", "div": "ucg", "rev": "group", "products": [
            P("cib", "Corporate & investment banking", "First in Italy in equity capital markets, M&A, bonds and loans (1H26 league tables), with correspondent banking in the top three in each country.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["2Q26 results presentation", Q2]]),
            P("trade", "Trade finance & risk management", "First in trade finance in Germany and Western Europe (awards), with UC Hedge and UCTrader FX for client risk management.",
              s=["corp", "sme"], lc="move", neo=[0, ""],
              mc="Mittelstand and trade clients are untested ground for commercial and virtual cards.",
              src=[["2Q26 results presentation", Q2], ["UniCredit: Client Solutions", SOLUTIONS]]),
        ]},
        {"id": "4.5", "ic": "coins", "name": "Investments & insurance", "blurb": "onemarkets, €41bn.", "div": "onemarkets", "rev": "group", "products": [
            P("onemarkets", "onemarkets funds", "Group funds with more than €41 billion under management, sold in 13 countries.",
              s=["inv"], lc="grow", o="B", neo=[0, ""], src=[["2Q26 results presentation", Q2], ["UniCredit: Client Solutions", SOLUTIONS]]),
            P("insurance", "Bancassurance", "An 18% bancassurance share in Italy and more than 40% in unit-linked, with UniCredit Life Insurance and UniCredit Vita Assicurazioni wholly owned since June 2025.",
              s=["inv", "con"], lc="grow", o="A", neo=[0, ""], src=[["2Q26 results presentation", Q2], ["2025 Annual Report", AR25]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: buddy, Italy's digital branch, apps in every country, 3,075 branches and the ATM networks in Italy and Germany.",
    "tiles": [
        {"id": "5.1", "ic": "headset", "name": "buddy", "blurb": "Italy's digital branch.", "div": "buddy", "rev": "italy", "products": [
            P("buddy", "buddy", "A 24/7 digital branch in Italy by chat, phone and video, with 'buddy@you' home visits and the €0 Genius buddy account; it grew out of buddybank (2018 ⚠), which used Mastercard for processing ⚠.",
              s=["con", "young"], lc="open", o="B", neo=[None, "Mastercard processing at launch ⚠."], src=[["UniCredit: buddy", BUDDY], ["FinTech Futures: buddybank, Feb 2018", BUDDYBANK]]),
        ]},
        {"id": "5.2", "ic": "smartphone", "name": "Apps & portals", "blurb": "Mobile, open banking, portals.", "div": "ucg", "rev": "group", "products": [
            P("apps", "Mobile banking apps", "Apps in Italy, Germany (HVB), Austria and Bosnia (m_bank), with prepaid cards managed digital-first.",
              s=["con", "young"], lc="everyday", neo=[0, ""], src=[["2025 Annual Report", AR25], ["UniCredit: digital services", DIGITAL]]),
            P("openbank", "Open-banking aggregation", "Accounts at other banks shown in UniCredit's internet banking and app in Italy; provider not disclosed.",
              s=["con"], lc="everyday", neo=[None, "Provider not disclosed."], src=[["UniCredit: digital services", DIGITAL]]),
            P("portals", "Corporate portals & onemarkets platform", "Corporate banking portals in Italy and Germany and the onemarkets investment platform.",
              s=["corp", "inv"], lc="open", neo=[0, ""], src=[["UniCredit: Client Solutions", SOLUTIONS]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & ATMs", "blurb": "3,075 branches.", "div": "ucg", "rev": "italy", "products": [
            P("branches", "Branches", "3,075 retail branches at the end of 2025: 1,941 in Italy and 1,134 abroad.",
              s=["con", "inv"], lc="open", neo=[0, ""], src=[["2025 Annual Report", AR25]]),
            P("atms", "ATMs & cash", "BancoSmart ATMs, Cassa Veloce and cardless Prelievo Smart in Italy; the Cash Group network in Germany and free withdrawals at UniCredit banks across Europe.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["UniCredit: digital services", DIGITAL], ["HVB: UniCredit Card", HVBCARD]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at UniCredit", "blurb": "One deal for 13 banks.", "products": [
        P("mcatucg", "Mastercard at UniCredit", "A single 2023 agreement makes Mastercard the issuing partner for 13 banks and about 20 million cards. HVB is swapping Visa Debit and Maestro girocards for Mastercard debit; Italian credit and prepaid cards are Mastercard and Priceless runs on them. Visa keeps part of Italian MyOne debit, girocard stays in Germany, and Commerzbank's card estate is the open question.",
          s=["con"], div="ucg", rev="group", mc="The relationship this map is drawn for.",
          src=[["UniCredit and Mastercard, May 2023", MCDEAL], ["HVB: UniCredit Card", HVBCARD]]),
    ]},
    {"id": "pillar-market", "name": "European banking", "blurb": "Instant, stablecoins, consolidation.", "products": [
        P("market", "The market", "The EU Instant Payments Regulation with verification of payee, the digital euro moving to its next phase (November 2025), MiCAR for stablecoins, Italian golden-power rules and German takeover law; rivals include Intesa Sanpaolo, Deutsche Bank, the Sparkassen and Erste ⚠.",
          s=["con"], div="ucg", rev="group", src=[["2025 Annual Report", AR25], ["Commerzbank offer, Mar 2026", CBKOFFER]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
