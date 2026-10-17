"""CaixaBank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the H1 2026 results (29 July 2026) and the 2025 results
(30 January 2026). ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it,
2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1 = "https://www.caixabank.com/en/headlines/news/caixabank-profit-3203-million-euros-june-2026-commercial-growth"
H1R = "https://www.caixabank.com/StaticFiles/pdfs/260729_OIR_Informe_Financiero_1S26_en.pdf"
H1PR = "https://www.caixabank.com/docs/comunicacion/92242.pdf"
CEO = "https://www.caixabank.com/docs/comunicacion/92243.pdf"
FY25 = "https://www.caixabank.com/en/headlines/news/caixabank-posts-a-net-profit-of-5-89-billion-in-2025-up-1-8-driven-by-strong-business-growth"
FY25R = "https://www.caixabank.com/StaticFiles/pdfs/260130_OIR_Informe_Financiero_2025_en.pdf"
EXCO = "https://www.caixabank.com/en/shareholders-investors/corporate-governance/management-committee.html"
BOARD = "https://www.caixabank.com/en/shareholders-investors/corporate-governance/board-directors.html"
SHARE = "https://www.caixabank.com/en/shareholders-investors/caixabanks-share/capital-distribution.html"
PLAN = "https://valenciaplaza.com/caixabank-espera-duplicar-crecimiento-hasta-2027-rentabilidad-supere-15"
WIKI = "https://en.wikipedia.org/wiki/CaixaBank"
MCVIRT = "https://www.caixabank.com/es/actualidad/noticias/caixabank-lanza-un-nuevo-servicio-de-pago-virtual-entre-empresas-para-digitalizar-el-pago-a-proveedores"
MCVIRT2 = "https://www.mastercard.com/news/europe/es-es/noticias/notas-de-prensa/es-es/2026/mastercard-y-caixabank-lanzan-un-nuevo-servicio-de-pago-virtual-entre-empresas-para-digitalizar-el-pago-a-proveedores/"
VAGENT = "https://www.caixabank.com/en/headlines/news/caixabank-completes-its-first-transaction-initiated-by-an-artificial-intelligence-agent-in-collaboration-with-visa"
FTF = "https://www.fintechfutures.com/ai-in-fintech/caixabank-ai-agent-payment-visa"
IMAGINMC = "https://www.caixabank.com/en/headlines/news/imagin-introduces-marc-marquez-as-the-ambassador-for-its-new-travel-card"
APPLEPAY = "https://www.caixabank.com/en/headlines/news/caixabank-customers-in-spain-can-now-pay-with-installments-when-checking-out-with-apple-pay"
TAP = "https://www.caixabank.com/en/headlines/news/caixabank-launches-tap-to-pay-on-iphone-for-businesses-to-accept-contactless-payments"
TRAVEL = "https://www.caixabank.com/en/headlines/news/caixabank-strengthens-its-travel-card-offering-with-imagin-and-moneytotravel"
CPCCARDS = "https://www.caixabankpc.com/en/particular/cards"
VUELING = "https://www.caixabank.com/en/headlines/news/vueling-and-caixabank-present-its-new-loyalty-card"
BRAILLE = "https://www.caixabank.com/en/headlines/news/caixabank-launches-spains-first-credit-card-with-braille-system?id=43462"
MASTERPASS = "https://forbes.es/?p=10090"
DEBIT = "https://www.caixabank.cat/deployedfiles/particulares/Estaticos/pdf/Cuentas/Precontrato-de-la-Tarjeta-de-debito_ES.pdf"
CORP = "https://caixabank.cat/empresa/tarjetas/mastercard-corporate.html"
BIZUMEU = "https://aebanca.es/en/actualidad/notas-de-prensa/banking-associations-aeb-ceca-and-unacc-welcome-the-launch-of-bizums-interconnection-with-13-european-countries/"
BIZUMSHOP = "https://www.hola.com/al-dia/20260429898615/bizum-pago-tiendas-fisicas-18-mayo-sin-tarjeta-como-funciona/"
EMPSA = "https://empsa.org/news/bancomat-epi-and-sibs-mb-way-successfully-demonstrate-cross-border-central-interoperability-for-retail-payment/"
ECBEPI = "https://www.ecb.europa.eu/press/pr/date/2020/html/ecb.pr200702~214c52c76b.en.html"
BPICARDS = "https://www.bancobpi.pt/particulares/cartoes"
IPR = "https://eur-lex.europa.eu/eli/reg/2024/886/oj"
IFR = "https://eur-lex.europa.eu/eli/reg/2015/751/oj"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · owners · plan", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: 20.9 million customers and €693 billion of assets, the 'la Caixa' Foundation and the Spanish state as anchor owners, a bank built from 'la Caixa', Bankia and BPI, and a 2025–2027 plan with more than €5 billion for technology.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "€3.2bn in the half, ROTE 18%.", "div": "group", "rev": "bank", "products": [
            P("balance", "Balance sheet & earnings", "Attributable profit of €3,203 million in H1 2026 (+8.5%; Q2 €1,631 million) and €5.89 billion in 2025; ROTE 18.0%, cost-to-income 39.6%, CET1 12.5%, NPL ratio 1.78%; total assets €693.4 billion, loans €406.2 billion and customer funds €771.9 billion at 30 June 2026.",
              s=["con"], neo=[0, ""], src=[["H1 2026 financial report", H1R], ["2025 results", FY25]]),
            P("ratings", "Credit ratings", "S&P A+ (stable), Moody's A2 (stable), Fitch A– (positive outlook) and Morningstar DBRS A (high), with Moody's and S&P upgrades in 2025.",
              s=["corp"], neo=[0, ""], src=[["2025 financial report", FY25R]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Owners & leadership", "blurb": "Foundation 31%, state 18%.", "div": "group", "rev": "centre", "products": [
            P("owners", "Ownership & listing", "Listed in Madrid (IBEX 35), market value €86.2 billion at 30 June 2026; the 'la Caixa' Foundation holds 31.0% through CriteriaCaixa and the Spanish state's FROB 18.0% through BFA; 506,856 shareholders.",
              s=["saver"], neo=[0, ""], src=[["CaixaBank: capital distribution", SHARE], ["H1 2026 financial report", H1R]]),
            P("leadership", "Board & management committee", "Chair Tomás Muniesa (since January 2025), CEO Gonzalo Gortázar (since 2014), COO Luis Javier Blas, CFO Javier Pano, Jordi Mondéjar for retail, private and business banking, Iñaki Badiola for CIB and Mariona Vicens for digital transformation and advanced analytics.",
              s=["corp"], neo=[0, ""], src=[["CaixaBank: board", BOARD], ["CaixaBank: management committee", EXCO]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & brands", "blurb": "'la Caixa', Bankia, BPI.", "div": "group", "rev": "bank", "products": [
            P("heritage", "Heritage & brands", "Roots in the Barcelona savings bank 'la Caixa' ⚠ founding year not in sources; Criteria CaixaCorp listed in 2007 and renamed CaixaBank in 2011; Banca Cívica and Banco de Valencia in 2012; registered office moved to Valencia in October 2017; Bankia merged in March 2021; BPI fully owned.",
              s=["con"], o="I", neo=[0, ""], src=[["Wikipedia: CaixaBank", WIKI]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "€5bn+ for tech to 2027.", "div": "group", "rev": "bank", "products": [
            P("tech", "Technology, data & AI", "More than €5 billion of technology investment over 2025–2027 with generative AI across channels; CaixaBank Tech as the technology subsidiary; a management-committee head of digital transformation and advanced analytics.",
              s=["corp"], neo=[0, ""], src=[["Valencia Plaza: Strategic Plan, Nov 2024", PLAN], ["CaixaBank: management committee", EXCO]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategic Plan 2025–27", "blurb": "ROTE above 16%, beaten early.", "div": "group", "rev": "bank", "products": [
            P("strategy", "Strategic Plan 2025–2027", "Business volume +4% a year, consumer credit above 6% and business credit above 5% a year, ROTE above 16% by 2027, efficiency slightly above 40%, payout of 50–60% plus capital above 12.5% CET1; targets beaten in 2025 and raised.",
              s=["corp"], neo=[0, ""], src=[["Valencia Plaza: Strategic Plan, Nov 2024", PLAN], ["2025 results", FY25], ["CEO transcript, H1 2026", CEO]]),
            P("deals", "Deals", "Bankia merger completed in March 2021; the BFA (Angola) stake cut from 48.1% to 33.4% after its 2025 IPO; eight €500 million buybacks; Comercia absorbs UniversalPay's POS business ⚠ date unconfirmed.",
              s=["corp"], o="A", neo=[0, ""], src=[["Wikipedia: CaixaBank", WIKI], ["2025 financial report", FY25R], ["H1 2026 financial report", H1R]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Eight ways money moves: Spain's biggest card issuer with 34 million cards and a Visa-led credit range, debit on both networks, travel and B2B virtual cards on Mastercard, wallets and instalments, Comercia's 805,000 terminals, Bizum in shops and linked to Wero, and BPI's cards and MB WAY in Portugal.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Credit cards", "blurb": "MyCard and co-brands on Visa.", "div": "cpc", "rev": "bank", "products": [
            P("mycard", "MyCard, Visa Classic & Visa&Go", "Credit cards issued by CaixaBank Payments & Consumer, paid at month end or in instalments; the issuer has more than 34 million cards and 31% of invoiced card purchases in Iberia (August 2025). The named consumer range is Visa.", short="MyCard (Visa)",
              s=["con"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."],
              mc="Spain's biggest credit book sits on Visa; card turnover share is 31.0%.",
              src=[["CaixaBank Payments & Consumer: cards", CPCCARDS], ["Apple Pay instalments, Aug 2025", APPLEPAY], ["Braille card, May 2022", BRAILLE]]),
            P("cobrands", "Co-brand cards", "Vueling Visa (Avios; launched September 2021 with Visa), IKEA Visa, MediaMarkt Visa, Visa FNAC, Repsol Más, RACC and Miles & More. A RACC Mastercard appeared on a 2022 fee schedule ⚠.",
              s=["con"], lc="borrow", ay="Sep 2021", o="P", at="Visa, Vueling, IKEA", neo=[0, "Visa."], src=[["CaixaBank Payments & Consumer: cards", CPCCARDS], ["Vueling Visa, Sep 2021", VUELING]]),
            P("clubs", "Football club cards", "Club-branded Visa contactless cards tied to sponsorships of Villarreal, Cádiz, Granada, Almería, Mallorca and others, renewed in late 2025; 190,000 Villarreal cards sold ⚠ (club releases not fetched).",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa ⚠."], src=[["CaixaBank Payments & Consumer: cards", CPCCARDS]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Debit & prepaid", "blurb": "Visa or Mastercard.", "div": "caixabank", "rev": "bank", "products": [
            P("debit", "Debit cards", "Debit cards issued by CaixaBank Payments & Consumer with CaixaBank as agent; the pre-contract prices foreign spending at the rate 'published by the card brand, VISA, MASTERCARD', so both networks are used. The split is not public ⚠.", short="Debit (Visa & Mastercard)",
              s=["con", "young"], lc="everyday", o="P", at="Visa, Mastercard", neo=[1, "Visa or Mastercard; split not public."], src=[["CaixaBank: debit card pre-contract", DEBIT]]),
            P("prepaid", "Prepaid & benefit cards", "Business, travel, virtual (CyberBusiness), meal and transport prepaid cards issued by Global Payments MoneyToPay, a company of CaixaBank and Global Payments ⚠ networks not stated.",
              s=["sme"], lc="move", o="P", at="Global Payments", neo=[None, "Network not stated ⚠."], src=[["imagin and MoneyToTravel, Jun 2026", TRAVEL]]),
        ]},
        {"id": "2.3", "ic": "plane", "name": "Travel cards", "blurb": "imagin and MoneyToTravel.", "div": "imagin", "rev": "bank", "products": [
            P("imagintravel", "imagin travel card", "A fee-free digital and physical debit card for paying in any currency and withdrawing abroad, supported by Mastercard and fronted by Marc Márquez (February 2025); since June 2026 every imagin card carries no FX or ATM fees abroad.", short="imagin travel (Mastercard)",
              s=["young"], lc="everyday", st="new", ay="Feb 2025", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard's newest consumer foothold, with the group's youngest customers.",
              src=[["imagin travel card, Feb 2025", IMAGINMC], ["imagin and MoneyToTravel, Jun 2026", TRAVEL]]),
            P("moneytotravel", "MoneyToTravel", "A prepaid travel card from MoneyToPay with no FX fees, two free ATM withdrawals a month abroad, an eSIM, lounge access on delays and travel insurance, priced at the Mastercard exchange rate ⚠ network inferred (June 2026).",
              s=["young", "con"], lc="everyday", st="new", ay="Jun 2026", o="P", at="Global Payments", neo=[2, "Mastercard exchange rate ⚠."], src=[["imagin and MoneyToTravel, Jun 2026", TRAVEL]]),
        ]},
        {"id": "2.4", "ic": "briefcase-business", "name": "Commercial & B2B cards", "blurb": "Virtual cards with Mastercard.", "div": "cpc", "rev": "bank", "products": [
            P("virtualb2b", "B2B virtual payment service", "Launched 1 June 2026 with Mastercard: companies create a virtual card per supplier payment with limits, expiry and geographic controls, tags and approval rules; more than 60 ERPs reconcile automatically; suppliers are paid at once and the buyer is charged at the end of the cycle.", short="B2B virtual cards (Mastercard)",
              s=["corp", "sme"], lc="move", st="new", ay="Jun 2026", o="P", at="Mastercard", neo=[3, "Mastercard's virtual card technology."],
              mc="The first joint Mastercard launch in a decade, aimed at a business book growing 10.6%.",
              src=[["CaixaBank: B2B virtual payments, Jun 2026", MCVIRT], ["Mastercard Spain newsroom, Jun 2026", MCVIRT2]]),
            P("corporate", "Mastercard Corporate", "Corporate credit cards for business travel with rewards ⚠ (page title only; not fetched).",
              s=["corp"], lc="move", o="P", at="Mastercard", neo=[2, "Mastercard ⚠."], src=[["CaixaBank: Mastercard Corporate", CORP]]),
            P("bizcards", "Business & fleet cards", "MyCard Negocios for the self-employed, Solred fuel cards and the Via-T Bip&Drive toll device, issued by CaixaBank Payments & Consumer ⚠ networks not stated.",
              s=["sme"], lc="move", o="P", at="Repsol", neo=[None, "Network not stated."], src=[["CaixaBank Payments & Consumer: cards", CPCCARDS]]),
        ]},
        {"id": "2.5", "ic": "smartphone", "name": "Wallets & instalments", "blurb": "Apple Pay Pay Later first.", "div": "cpc", "rev": "bank", "products": [
            P("wallets", "Mobile wallets", "Cards in Apple Pay, Google Pay and Samsung Pay ⚠ and wearables such as Garmin Pay ⚠, from the CaixaBank Pay app.",
              s=["con", "young"], lc="everyday", o="P", at="Apple, Google, Samsung", neo=[1, "Tokens on both networks."], src=[["Apple Pay instalments, Aug 2025", APPLEPAY]]),
            P("paylater", "Instalments in Apple Pay", "The first Spanish bank to let customers split online and in-app Apple Pay purchases over 2 to 12 months, for MyCard and eligible Visa or Mastercard credit cards (29 August 2025).",
              s=["con"], lc="borrow", st="new", ay="Aug 2025", o="P", at="Apple", neo=[1, "Visa or Mastercard credit."], src=[["Apple Pay instalments, Aug 2025", APPLEPAY]]),
            P("masterpass", "Masterpass in CaixaBank Pay", "CaixaBank was the first Spanish bank to launch Masterpass, inside CaixaBank Pay, in December 2016, with Mastercard Spain's Ovidio Egido; Masterpass has since given way to Click to Pay ⚠.",
              s=["con"], lc="everyday", st="retired", ay="Dec 2016", o="P", at="Mastercard", neo=[3, "Mastercard's own, now retired ⚠."], src=[["Forbes España: Masterpass, Dec 2016", MASTERPASS]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Acquiring", "blurb": "Comercia: 805,000 POS.", "div": "comercia", "rev": "bank", "products": [
            P("comercia", "Comercia Global Payments", "Spain's largest merchant acquirer, a joint venture in which CaixaBank holds 20% and Global Payments the rest, with more than 805,000 POS terminals and a 30.5% market share (June 2025).", short="Comercia (all networks)",
              s=["sme"], lc="move", o="P", at="Global Payments", neo=[1, "Accepts every network."], src=[["Tap to Pay on iPhone, Jun 2025", TAP], ["2025 financial report", FY25R]]),
            P("taptopay", "Tap to Pay on iPhone & Smartphone TPV", "The first Spanish bank to let merchants take contactless cards and wallets on an iPhone through the Smartphone TPV app, with no extra hardware (26 June 2025).",
              s=["sme"], lc="move", st="new", ay="Jun 2025", o="P", at="Apple", neo=[1, "Accepts every network."], src=[["Tap to Pay on iPhone, Jun 2025", TAP]]),
        ]},
        {"id": "2.7", "ic": "zap", "name": "Bizum & instant", "blurb": "In shops from May 2026.", "div": "caixabank", "rev": "bank", "products": [
            P("bizum", "Bizum", "Spain's bank-owned account-to-account mobile payment scheme: more than 30.6 million users, 39 banks, 111,000 merchants and more than 105 million online payments a year; 3.4 million payments a day and more than €67 billion in 2025.",
              s=["con", "young"], lc="move", o="P", at="Bizum", neo=[0, "Account-to-account."],
              mc="The main domestic substitute for card payments.",
              src=[["¡HOLA!: Bizum in shops, Apr 2026", BIZUMSHOP], ["AEB: Bizum interconnection, Feb 2026", BIZUMEU]]),
            P("bizumshop", "Bizum in shops", "NFC payments at the till straight from account to account, live from 18 May 2026 with CaixaBank, Sabadell and Bankinter as the first three banks; merchant fees expected below card fees.",
              s=["con", "sme"], lc="move", st="new", ay="May 2026", o="P", at="Bizum", neo=[0, "Account-to-account."],
              mc="Competes with debit cards at the point of sale.",
              src=[["¡HOLA!: Bizum in shops, Apr 2026", BIZUMSHOP]]),
            P("europa", "Bizum–Wero interconnection", "Bizum, MB WAY, Bancomat and Vipps MobilePay (the EuroPA alliance) and EPI's Wero began building a central hub on 2 February 2026 across 13 countries and 330 million people: person-to-person first, shop and online payments later. Bizum already links to Italy, Portugal and Andorra (March 2025).",
              s=["con"], lc="move", st="new", ay="Feb 2026", o="P", at="EPI, EuroPA", neo=[0, "Bizum, Wero and EuroPA."],
              mc="A European account-to-account network for cross-border spending that bypasses the card schemes.",
              src=[["AEB: Bizum interconnection, Feb 2026", BIZUMEU], ["EMPSA: cross-border pilot, Apr 2026 ⚠", EMPSA], ["ECB: EPI launch, Jul 2020", ECBEPI]]),
            P("instant", "SEPA Instant transfers", "Instant euro transfers with Verification of Payee, required of all euro-area banks under the Instant Payments Regulation.",
              s=["con", "sme"], lc="move", neo=[0, ""], src=[["Instant Payments Regulation", IPR]]),
        ]},
        {"id": "2.8", "ic": "flag", "name": "Portugal rails", "blurb": "BPI cards and MB WAY.", "div": "bpi", "rev": "bpi", "products": [
            P("bpicards", "BPI cards", "BPI Electron debit, credit and prepaid cards and MBNet virtual cards for online shopping; the networks are not named on BPI's page ⚠ (Electron suggests Visa).",
              s=["port"], lc="everyday", o="A", neo=[None, "Networks not stated ⚠."], src=[["Banco BPI: cards", BPICARDS]]),
            P("mbway", "MB WAY in the BPI app", "SIBS's mobile payments, free in the BPI app; MB WAY is part of the EuroPA link-up with Bizum and Wero.",
              s=["port"], lc="move", o="P", at="SIBS", neo=[0, "SIBS."], src=[["Banco BPI: cards", BPICARDS], ["AEB: Bizum interconnection, Feb 2026", BIZUMEU]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: fraud controls and tokens, a first agentic payment with Visa, and loyalty, co-brand and accessibility programmes that are mostly built on Visa.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "Tokens, identity, monitoring.", "div": "group", "rev": "bank", "products": [
            P("fraud", "Fraud & payment security", "Tokenisation, identity verification and real-time fraud monitoring used in card payments, and anti-fraud services on travel cards; no Mastercard fraud or scam-scoring product found ⚠.",
              s=["con", "sme"], lc="everyday", neo=[None, "No Mastercard tool found ⚠."],
              mc="Bizum in shops and the Wero link will move more money account to account, where card fraud tools do not reach.",
              src=[["Visa agentic transaction, Jul 2026", VAGENT], ["imagin and MoneyToTravel, Jun 2026", TRAVEL]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI & agentic commerce", "blurb": "First agent payment, with Visa.", "div": "group", "rev": "bank", "products": [
            P("agentic", "Agentic payments", "CaixaBank completed its first transaction started by an AI agent on 2 July 2026, with real card data on standard merchant systems, through Visa Intelligent Commerce and Visa's Agentic Ready programme.",
              s=["con"], lc="everyday", st="new", ay="Jul 2026", o="P", at="Visa", neo=[0, "Visa Intelligent Commerce."],
              mc="Visa got there first; Mastercard Agent Pay is untouched here.",
              src=[["CaixaBank: agentic transaction, Jul 2026", VAGENT], ["FinTech Futures, Jul 2026", FTF]]),
            P("analytics", "Data & advanced analytics", "A management-committee lead for digital transformation and advanced analytics and generative AI across channels under the €5 billion technology plan.",
              s=["corp"], lc="everyday", neo=[0, ""], src=[["CaixaBank: management committee", EXCO], ["Valencia Plaza: Strategic Plan, Nov 2024", PLAN]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Loyalty & inclusion", "blurb": "Avios, clubs, Braille.", "div": "cpc", "rev": "bank", "products": [
            P("loyalty", "Loyalty & rewards", "Loyalty programmes that cut recurring banking fees by 2.4% in H1 2026, Avios on the Vueling Visa, and football club cards.",
              s=["con"], lc="grow", neo=[0, "Mostly Visa co-brands."],
              mc="Card-linked offers could fund rewards that are eating into fees.",
              src=[["H1 2026 results", H1], ["Vueling Visa, Sep 2021", VUELING]]),
            P("braille", "Braille card", "Spain's first card with Braille, developed with ONCE and Visa and launched on MyCard Visa (May 2022).",
              s=["con"], lc="everyday", ay="May 2022", o="P", at="Visa, ONCE", neo=[0, "Visa."], src=[["Braille card, May 2022", BRAILLE]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: Spain's leading retail bank with a 24.7% deposit share, consumer finance through CaixaBank Payments & Consumer, business and corporate banking, wealth and insurance, the imagin neobank and BPI in Portugal.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Retail & mortgages", "blurb": "6.4m payrolls, 24.7% of deposits.", "div": "caixabank", "rev": "bank", "products": [
            P("retail", "Retail banking", "20.9 million customers in Spain and Portugal, more than 1.1 million added in Spain in a year, 6.4 million payroll customers, 24.7% of Spanish deposits and 23.3% of loans.",
              s=["con"], lc="everyday", neo=[1, "Debit on Visa or Mastercard."], src=[["H1 2026 results", H1], ["H1 2026 financial report", H1R]]),
            P("mortgages", "Mortgages", "Home-purchase lending up 6.7% (€9.05 billion) in the year to June 2026.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["H1 2026 results", H1]]),
            P("microbank", "MicroBank", "The group's social bank: 282,288 microcredits worth €2.52 billion in the twelve months to June 2026.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["H1 2026 results", H1]]),
        ]},
        {"id": "4.2", "ic": "hand-coins", "name": "Consumer finance", "blurb": "€12.9bn book, +11.5%.", "div": "cpc", "rev": "bank", "products": [
            P("consumer", "CaixaBank Payments & Consumer", "The group's card and consumer-finance company: more than 34 million cards, 16 million customers and a €12.9 billion book (August 2025); group consumer lending up 11.5% to June 2026 and a 17.7% share.",
              s=["con"], lc="borrow", neo=[0, "Credit range on Visa."], src=[["Apple Pay instalments, Aug 2025", APPLEPAY], ["H1 2026 results", H1], ["H1 2026 financial report", H1R]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Business & corporate", "blurb": "Business loans +10.6%.", "div": "caixabank", "rev": "bank", "products": [
            P("business", "Business banking", "Loans to businesses up 10.6% (€18.03 billion) in the year to June 2026, with merchant services through Comercia and cards through CaixaBank Payments & Consumer.",
              s=["sme"], lc="borrow", neo=[1, "B2B and corporate cards on Mastercard; others not stated."], src=[["H1 2026 results", H1]]),
            P("cib", "Corporate & Investment Banking", "Lending, markets and transaction banking for large companies, led by Iñaki Badiola.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["CaixaBank: management committee", EXCO]]),
        ]},
        {"id": "4.4", "ic": "coins", "name": "Wealth & insurance", "blurb": "€217bn under management.", "div": "vida", "rev": "bank", "products": [
            P("wealth", "Wealth, pensions & insurance", "Assets under management of €216.7 billion, wealth fees up 12.1% and protection insurance up 14.5% in H1 2026; 34.4% of pension plans and 38.8% of savings insurance in Spain; VidaCaixa and SegurCaixa Adeslas (49.9%).",
              s=["saver"], lc="grow", neo=[0, ""], src=[["H1 2026 results", H1], ["H1 2026 financial report", H1R], ["2025 financial report", FY25R]]),
        ]},
        {"id": "4.5", "ic": "rocket", "name": "imagin", "blurb": "4.2m customers, half of new.", "div": "imagin", "rev": "bank", "products": [
            P("imaginbank", "imagin neobank", "4.2 million customers, mostly under 35, about €24 billion of loans and deposits (+20%), about half of the group's new customers in Spain and 9% of payroll accounts.",
              s=["young"], lc="open", neo=[1, "Travel card on Mastercard."], src=[["H1 2026 results", H1], ["2025 results", FY25]]),
        ]},
        {"id": "4.6", "ic": "flag", "name": "BPI in Portugal", "blurb": "€218m profit in the half.", "div": "bpi", "rev": "bpi", "products": [
            P("bpi", "Banco BPI", "Portugal's bank in the group: €218 million of H1 2026 profit, 11.7% of lending and 11.1% of customer funds, 4,630 employees and an NPL ratio of 1.55%.",
              s=["port"], lc="everyday", o="A", neo=[None, "Card networks not stated ⚠."], src=[["H1 2026 results", H1], ["H1 2026 financial report", H1R]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: 12 million digital customers, the largest base in Spain, more than 4,500 branches and 12,000 ATMs, and partners from airlines to football clubs.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Apps", "blurb": "12m+ digital customers.", "div": "caixabank", "rev": "bank", "products": [
            P("app", "CaixaBank app & digital banking", "12.4 million digital banking users (August 2025), the largest base in Spain's financial sector, with CaixaBank Pay for cards and wallets.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["Apple Pay instalments, Aug 2025", APPLEPAY], ["CaixaBank: agentic transaction, Jul 2026", VAGENT]]),
            P("imaginapp", "imagin & BPI apps", "The imagin app for under-35s and the BPI app with MB WAY in Portugal.",
              s=["young", "port"], lc="open", neo=[0, ""], src=[["H1 2026 results", H1], ["Banco BPI: cards", BPICARDS]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & partners", "blurb": "4,543 branches, 12,233 ATMs.", "div": "group", "rev": "bank", "products": [
            P("branches", "Branches & ATMs", "4,543 branches (4,235 in Spain) and 12,233 ATMs at 30 June 2026, in more than 3,700 municipalities.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["H1 2026 financial report", H1R], ["H1 2026 results", H1]]),
            P("partners", "Co-brand & club partners", "Vueling, IKEA, MediaMarkt, FNAC, Repsol, RACC and Miles & More, and the football clubs whose cards CaixaBank issues.",
              s=["con"], lc="open", o="P", at="Vueling, IKEA, Repsol", neo=[0, "Visa co-brands."], src=[["CaixaBank Payments & Consumer: cards", CPCCARDS]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at CaixaBank", "blurb": "Visa-led, Mastercard in the corners.", "products": [
        P("mcatcaixa", "Mastercard at CaixaBank", "Spain's largest card issuer (34 million cards, 31.0% of card turnover) runs a consumer credit range that is visibly Visa, and Visa took its first agentic payment in July 2026. Mastercard carries part of debit, the imagin travel card (February 2025), prepaid travel ⚠, Mastercard Corporate ⚠ and, since June 2026, the B2B virtual card platform; it also gave CaixaBank Spain's first Masterpass in 2016.",
          s=["con"], div="group", rev="bank", mc="The relationship this map is drawn for.",
          src=[["CaixaBank: B2B virtual payments, Jun 2026", MCVIRT], ["imagin travel card, Feb 2025", IMAGINMC], ["CaixaBank Payments & Consumer: cards", CPCCARDS]]),
    ]},
    {"id": "pillar-market", "name": "Spanish payments", "blurb": "Bizum, Wero, instant.", "products": [
        P("market", "The Spanish and Portuguese market", "Bizum with 30.6 million users moving into shops, its 2026 link with Wero and the EuroPA wallets, mandatory SEPA Instant with Verification of Payee, EU interchange caps of 0.2% on debit and 0.3% on credit, and Spain's tax on interest and fee income (€304 million in H1 2026).",
          s=["con"], div="group", rev="bank", src=[["AEB: Bizum interconnection, Feb 2026", BIZUMEU], ["Interchange Fee Regulation", IFR], ["Instant Payments Regulation", IPR], ["H1 2026 results", H1]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
