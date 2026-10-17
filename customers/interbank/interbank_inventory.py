"""Interbank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the IFS 2Q26 results (11 August 2026) and call
(12 August 2026), and Interbank's 2025 annual report (Memoria Anual, 24 February 2026). Amounts in soles (S/).
``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on
Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public. interbank.pe refused automated requests, so
several card networks rest on comparison sites and carry a ⚠.
"""
# ruff: noqa: E501

Q2R = "https://www.sec.gov/Archives/edgar/data/0001615903/000119312526344966/ifs-ex99_1.htm"
Q2T = "https://ifs.com.pe/documents/d/ifs/q2-2026-ifs-transcript"
Q4T = "https://www.fool.com/earnings/call-transcripts/2026/02/12/intercorp-financial-ifs-earnings-call-transcript/"
Q1H = "https://www.nasdaq.com/articles/intercorp-financial-services-q1-earnings-call-highlights"
MEM = "https://ifs.com.pe/documents/d/ifs/memoria-anual-ibk"
HIST = "https://ifs.com.pe/history"
TORI = "https://forbes.pe/negocios/2024-02-21/carlos-tori-asumira-como-nuevo-gerente-general-de-interbank-a-partir-del-1-de-mayo-de-este-ano/"
PMP = "https://thelatinamericanlawyer.com/ppu-assists-scotiabank-peru-in-sale-of-pmp-shares-to-intercorp/"
MULTI = "https://www.bbva.com/es/pe/innovacion/la-aceptacion-multimarca-de-las-tarjetas-en-peru/"
IZI24 = "https://forbes.pe/negocios/2024-10-22/izipay-aumentara-el-volumen-de-operaciones-hasta-en-12-este-ano-proyecta-su-ceo/"
IZILINK = "https://www.izipay.pe/link-de-pago/"
IZIYA = "https://www.peru-retail.com/interbank-lanza-izipayya-su-nueva-app-con-qr-que-acepta-todas-las-billeteras-digitales/"
TAP21 = "https://www.peru-retail.com/empresa-peruana-crea-software-que-convierte-el-celular-en-pos/"
RANKIA = "https://www.rankia.pe/blog/tarjetas-creditos-tarjetas-debito-peru/5141081-tarjeta-credito-interbank-como-solicitar-membresia-beneficios"
MCCL = "https://interbank.pe/web/guest/tarjetas/tarjetas-credito/mastercard-clasica"
MILLAS = "https://interbank.pe/tarjetas/tarjetas-credito/millas-benefit"
TPE = "https://tarjetas.pe/tarjeta-interbank"
AMEX = "https://www.global66.com/blog/american-express/"
RAPPI = "https://forbes.pe/negocios/2023-08-10/interbank-anuncia-el-fin-de-su-alianza-con-rappi-las-tarjetas-rappibank-dejaran-de-funcionar-en-peru"
ANTH = "https://forbes.pe/tecnologia/ia/2026-08-11/interbank-suscribio-acuerdo-con-anthropic-para-fortalecer-el-uso-de-inteligencia-artificial-en-el-banco"
PLINWA = "https://libero.pe/tecnologia/2025/11/03/plin-whatsapp-interbank-asi-puedes-transferir-hacer-pagos-sin-salir-de-whatsapp-aplicacion-yape-plin-video-266901"
ALERTS = "https://gestion.pe/tu-dinero/interbank-dispone-de-mas-alertas-en-su-banca-movil-que-esta-cambiando-para-sus-usuarios-noticia/"
VISAPE = "https://visa.com.tt/partner-with-us/info-for-partners/blog/visa-direct-revolutionizing-the-money-movement-in-peru.html"
PBRIEF = "https://paymentbrief.com/markets/peru"
INFOBAE = "https://www.infobae.com/peru/2025/05/03/billeteras-digitales-como-yape-y-plin-estan-desplazando-a-las-tarjetas-de-credito-por-que/"
INDECOPI = "https://www.peru-retail.com/indecopi-sanciono-a-interbank-por-entregar-tarjeta-de-credito-sin-autorizacion/"
RIQRA = "https://blog.riqra.com/posts/pasarelas-pago-online-peru"
IZIDIST = "https://gestion.pe/economia/empresas/izipay-tambien-sera-usado-como-red-para-distribuir-productos-de-interbank-noticia/"
APPLE = "https://www.mactech.com/2026/09/22/apple-enables-tap-to-pay-on-iphone-in-more-latin-american-countries/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · ownership · brand", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: S/52.6 billion of loans and a 15.6% ROE, 99% owned by Intercorp Financial Services, a bank founded in 1897 and privatised in 1994, an AI agreement with Anthropic and a target of ROE above 17%.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "S/52.6bn loans, ROE 15.6%.", "div": "interbank", "rev": "group", "products": [
            P("balance", "Balance sheet & earnings", "Gross loans of S/52.6 billion and deposits of S/57.0 billion at 30 June 2026; net income of S/402.5 million in 2Q26 (ROE 15.6%) and S/1,458.5 million in 2025 (ROE 16.2%); 13.7% of Peru's loans and 13.3% of deposits; total capital ratio 16.0% at end-2025; 6,742 staff.",
              s=["con"], neo=[0, ""], src=[["IFS 2Q26 results", Q2R], ["Interbank annual report 2025", MEM]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership & ownership", "blurb": "Tori, Rodríguez-Pastor, IFS.", "div": "ifs", "rev": "group", "products": [
            P("leadership", "Board & management", "Chair Carlos Rodríguez-Pastor (since 1995), CEO Carlos Tori (since May 2024, previously head of payments and chair of Izipay); Luis Felipe Castellanos runs IFS and Michela Casassa is CFO; Alexander Woodman leads retail and channels.",
              s=["corp"], neo=[0, ""], src=[["Interbank annual report 2025", MEM], ["Forbes Perú: Tori named CEO, Feb 2024", TORI], ["IFS 2Q26 call", Q2T]]),
            P("ownership", "Intercorp Financial Services", "IFS, listed in New York since 2019 and in Lima since 2007, owns about 99% of Interbank and also controls Interseguro, Inteligo and Izipay; it is part of the Rodríguez-Pastor family's Intercorp group. Market capitalisation not confirmed ⚠.",
              s=["corp"], o="I", neo=[0, ""], src=[["IFS: history", HIST], ["Interbank annual report 2025", MEM]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & brand", "blurb": "Founded 1897.", "div": "interbank", "rev": "retail", "products": [
            P("heritage", "Heritage & brand", "Banco Internacional del Perú, incorporated in Lima in 1897 and privatised in August 1994; investment grade since 2010; Euromoney's Bank of the Year in Peru in 2024; a co-branded Vea card with Supermercados Peruanos since 2004.",
              s=["con"], o="I", neo=[0, ""], src=[["IFS: history", HIST], ["Interbank annual report 2025", MEM]]),
        ]},
        {"id": "1.4", "ic": "brain", "name": "Technology & AI", "blurb": "Claude Enterprise, AWS, CyberSOC.", "div": "interbank", "rev": "group", "products": [
            P("tech", "Core technology & security", "Credit-decision engines run in AWS environments, an AI-driven cyber-security operations centre, and continued spending on digital channels, data, cybersecurity and GenAI.",
              s=["corp"], neo=[0, ""], src=[["Interbank annual report 2025", MEM], ["IFS 2Q26 call", Q2T]]),
            P("anthropic", "Anthropic agreement", "A direct enterprise agreement with Anthropic (August 2026), the first for a Peruvian bank as reported, rolling out Claude Enterprise to knowledge workers and technology teams first; led by Claudio Querol, VP Data, Analytics & AI.",
              s=["corp"], st="new", ay="Aug 2026", o="P", at="Anthropic", neo=[0, ""], src=[["Forbes Perú: Anthropic agreement, Aug 2026", ANTH]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "ROE above 17%.", "div": "ifs", "rev": "group", "products": [
            P("strategy", "Strategy", "ROE above 17% in 2026 and 18% or more in the medium term; grow consumer and small-business lending; deepen primary relationships (up 16% a year); cut funding costs through Izipay and Plin. Risks named: El Niño from the second half of 2026 and pension-fund withdrawals.",
              s=["corp"], neo=[0, ""], src=[["IFS 2Q26 call", Q2T], ["IFS 4Q25 call", Q4T]]),
            P("deals", "Deals", "Bought Scotiabank's 50% of Izipay (signed December 2021, closed April 2022); Rappibank with Rappi (2021, closed 2023); subordinated bonds of US$300 million (2024) and US$350 million (2025) and a US$500 million senior bond (January 2026).",
              s=["corp"], o="A", neo=[0, ""], src=[["Latin American Lawyer: PMP sale, 2022", PMP], ["Interbank annual report 2025", MEM], ["IFS 2Q26 results", Q2R]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Five ways money moves: credit cards mostly on Visa, with an American Express range and a small Mastercard one; Visa debit; Izipay, the acquirer that began as Mastercard's in Peru; Plin, the bank wallet with 2.8 million monthly users; and wallet interoperability set by the central bank.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Credit cards", "blurb": "Visa first, then Amex.", "div": "interbank", "rev": "retail", "products": [
            P("visacredit", "Visa credit cards", "The main range: Visa Clásica, Oro, Platinum, Signature and Infinite, plus Visa Cashback and Visa Premia; card turnover up 21% a year in 2Q26 and card fees of S/464.9 million in 2025.", short="Credit (Visa)",
              s=["con"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Rankia: Interbank cards, Aug 2026", RANKIA], ["tarjetas.pe: Interbank guide, Aug 2026", TPE], ["Interbank annual report 2025", MEM]]),
            P("amex", "American Express cards", "Blue, Green, Gold, Platinum, Black and The Platinum Card, earning Millas Benefit; Interbank and BCP are Peru's Amex issuers, a relationship of about 25 years ⚠.", short="Credit (Amex)",
              s=["con"], lc="borrow", o="P", at="American Express", neo=[0, "American Express."], src=[["Rankia: Interbank cards, Aug 2026", RANKIA], ["Global66: Amex in Peru", AMEX]]),
            P("mccredit", "Mastercard credit cards", "Mastercard Clásica (annual fee about S/60–75, waived with a monthly purchase), Oro and Platinum ⚠; one comparison site lists no Mastercard at all, so the range looks small.", short="Credit (Mastercard)",
              s=["con"], lc="borrow", st="unconf", o="P", at="Mastercard", neo=[2, "Mastercard ⚠ size unknown."],
              mc="Mastercard's only issuing foothold at Interbank, and a small one.",
              src=[["Interbank: Mastercard Clásica", MCCL], ["Rankia: Interbank cards, Aug 2026", RANKIA]]),
            P("vea", "Vea co-brand card", "Credit card with Supermercados Peruanos (Plaza Vea), in the Intercorp group, since 2004; on Visa ⚠.",
              s=["con"], lc="borrow", ay="2004", o="P", at="Supermercados Peruanos", neo=[0, "Visa ⚠."], src=[["Interbank annual report 2025", MEM], ["tarjetas.pe: Interbank guide, Aug 2026", TPE]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Debit", "blurb": "Visa Débito Benefit.", "div": "interbank", "rev": "retail", "products": [
            P("debit", "Visa Débito Benefit", "The debit card for Interbank accounts, earning miles in some categories; on Visa ⚠.",
              s=["con", "sme"], lc="everyday", o="P", at="Visa", neo=[0, "Visa ⚠."], src=[["tarjetas.pe: Interbank guide, Aug 2026", TPE]]),
        ]},
        {"id": "2.3", "ic": "store", "name": "Izipay acquiring", "blurb": "45%+ of acquiring.", "div": "izipay", "rev": "payments", "products": [
            P("izipay", "Izipay", "Procesos de Medios de Pago, historically Peru's Mastercard acquirer (from 1999 ⚠), licensed for Visa in 2020; 100% IFS since April 2022; accepts Visa, Mastercard, Amex, Diners and Plin QR; claimed above 45% of acquiring in 2024; its float in Interbank accounts up about 50% a year.", short="Izipay (every network)",
              s=["merch", "sme"], lc="move", o="A", neo=[1, "Every network; Mastercard's historic acquirer ⚠."],
              mc="The largest acquirer in Peru by its own claim, with Mastercard roots.",
              src=[["BBVA: multi-brand acceptance", MULTI], ["Forbes Perú: Izipay CEO, Oct 2024", IZI24], ["Izipay: payment links", IZILINK], ["IFS 2Q26 call", Q2T]]),
            P("izipayya", "IzipayYa", "An app for micro-merchants with a QR that accepts every wallet (May 2023).",
              s=["merch"], lc="move", ay="May 2023", o="B", neo=[0, "QR and wallets."], src=[["Peru Retail: IzipayYa launch", IZIYA], ["Interbank annual report 2025", MEM]]),
            P("tapphone", "Phone as POS", "Izipay's software turns a smartphone into a card terminal, built with SmartPesa (November 2021); Apple's Tap to Pay on iPhone came to Peru through SumUp in September 2026.",
              s=["merch"], lc="move", ay="Nov 2021", o="P", at="SmartPesa", neo=[1, "Accepts every network."], src=[["Peru Retail: Izipay tap to phone, Nov 2021", TAP21], ["MacTech: Tap to Pay in LatAm, Sep 2026", APPLE]]),
        ]},
        {"id": "2.4", "ic": "smartphone", "name": "Plin", "blurb": "2.8m monthly users.", "div": "plin", "rev": "retail", "products": [
            P("plin", "Plin", "The wallet inside the apps of Interbank, BBVA and Scotiabank, launched January 2020 using Visa and Mastercard rails for instant transfers ⚠ current rails; 2.8 million monthly active clients, 60% of payments to merchants, and 234 million Interbank Plin transactions in 2Q26 (+44%).",
              s=["con", "merch"], lc="move", ay="Jan 2020", o="P", at="BBVA, Scotiabank", neo=[1, "Card rails at launch ⚠."],
              src=[["Interbank annual report 2025", MEM], ["IFS 2Q26 call", Q2T]]),
            P("plincredit", "Plin with credit card", "Paying through Plin with an Interbank credit card (2026), the bank's answer to Yape.",
              s=["con"], lc="move", st="new", neo=[1, "Interbank cards, mostly Visa."],
              mc="Cards inside a wallet need tokens and card-on-file controls.",
              src=[["IFS 1Q26 call highlights", Q1H]]),
            P("plinwa", "Plin WhatsApp & Plin Corredores", "Transfers and payments of up to S/100 by chat or voice inside WhatsApp, using AI (2025), and Plin top-ups for Lima's Metropolitano buses.",
              s=["con"], lc="move", st="new", ay="2025", neo=[0, ""], src=[["Libero: Plin WhatsApp, Nov 2025", PLINWA], ["Interbank annual report 2025", MEM]]),
        ]},
        {"id": "2.5", "ic": "arrow-left-right", "name": "Interoperability", "blurb": "Yape and Plin joined.", "div": "plin", "rev": "retail", "products": [
            P("interop", "Wallet interoperability", "The central bank (BCRP) required all wallets to interoperate; Yape and Plin linked by phone number from 2023 and by QR later, so Interbank customers can pay anyone.",
              s=["con"], lc="move", ay="2023", o="P", at="BCRP", neo=[0, "Account to account."], src=[["Visa: Visa Direct in Peru", VISAPE], ["PaymentBrief: Peru", PBRIEF]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: fraud alerts and card blocking in the app, the AVI assistant and data science, Millas Benefit and cashback, and open-banking partnerships with no public detail.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "Alerts and card blocks.", "div": "interbank", "rev": "retail", "products": [
            P("fraud", "Fraud alerts & card controls", "Fraud alerts on the app's home screen and a pilot to block credit cards temporarily from the app ⚠ date; Indecopi fined the bank in 2026 for issuing a card a customer had not asked for.",
              s=["con"], lc="everyday", neo=[0, "Interbank's own."],
              mc="Scam and fraud tools are an open need.",
              src=[["Gestión: app alerts", ALERTS], ["Peru Retail: Indecopi sanction, 2026", INDECOPI]]),
            P("cyber", "Cyber-security", "An AI-driven security operations centre, continuous testing and staff training.",
              s=["corp"], lc="everyday", neo=[0, ""], src=[["Interbank annual report 2025", MEM]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "Assistant & data", "blurb": "AVI, data science.", "div": "interbank", "rev": "retail", "products": [
            P("avi", "AVI digital assistant", "The first digital contact for clients not yet on the app; it helped bring 16,000 clients onto digital in 2Q26.",
              s=["con"], lc="open", st="new", neo=[0, ""],
              mc="Agent Pay could give the assistant a way to pay.",
              src=[["IFS 2Q26 call", Q2T]]),
            P("analytics", "Data, analytics & GenAI", "Analytical and AI models across the credit cycle, and the GenAI programme now built on Claude Enterprise.",
              s=["con", "sme"], lc="borrow", neo=[0, ""], src=[["Interbank annual report 2025", MEM], ["Forbes Perú: Anthropic agreement, Aug 2026", ANTH]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Loyalty", "blurb": "Millas Benefit.", "div": "interbank", "rev": "retail", "products": [
            P("millas", "Millas Benefit", "Miles on Visa, Amex and Mastercard credit cards and on Benefit debit, up to 2 miles per US$1 on premium cards, for flights, goods and services.",
              s=["con"], lc="grow", neo=[0, "Interbank's own."],
              mc="Card-linked offers and Priceless experiences could feed it.",
              src=[["Interbank: Millas Benefit", MILLAS], ["tarjetas.pe: Interbank guide, Aug 2026", TPE]]),
            P("cashback", "Cashback & Premia", "Visa Cashback (5% back in chosen categories) and Visa Premia with merchant coupons.",
              s=["con"], lc="grow", o="P", at="Visa", neo=[0, "Visa."], src=[["tarjetas.pe: Interbank guide, Aug 2026", TPE], ["Rankia: Interbank cards, Aug 2026", RANKIA]]),
        ]},
        {"id": "3.4", "ic": "plug", "name": "Open banking", "blurb": "Alliances, little detail.", "div": "interbank", "rev": "retail", "products": [
            P("openbanking", "Open-banking alliances", "Part of the 2021 'two fronts' digital strategy, alongside a payments ecosystem and Rappibank; no current partners or Peruvian open-finance rules found ⚠.",
              s=["con", "sme"], lc="open", st="unconf", neo=[None, "Nothing public."], src=[["Interbank annual report 2025", MEM]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: consumer loans with an 18.1% share and payroll loans, mortgages with 16%, small-business banking growing 31% a year, commercial and corporate banking, and the group's insurance and wealth arms.",
    "tiles": [
        {"id": "4.1", "ic": "hand-coins", "name": "Consumer & payroll", "blurb": "18.1% of consumer loans.", "div": "interbank", "rev": "retail", "products": [
            P("consumer", "Consumer lending", "Cards and personal loans: S/9.3 billion in cards and other consumer loans at June 2026 and an 18.1% share; cash-loan disbursements up 37% a year.",
              s=["con"], lc="borrow", neo=[0, "Cards mostly Visa."], src=[["IFS 2Q26 results", Q2R], ["IFS 2Q26 call", Q2T]]),
            P("payroll", "Payroll-deduction loans", "Loans repaid from salary (convenios), S/5.6 billion at June 2026.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["IFS 2Q26 results", Q2R]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Mortgages", "blurb": "16% share.", "div": "interbank", "rev": "retail", "products": [
            P("mortgages", "Mortgages", "S/11.0 billion at end-2025 (+7.9%), including the state MiVivienda programme; a 16.0% share.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["Interbank annual report 2025", MEM], ["IFS 2Q26 results", Q2R]]),
        ]},
        {"id": "4.3", "ic": "briefcase", "name": "Small business", "blurb": "Loans up 31%.", "div": "interbank", "rev": "commercial", "products": [
            P("smallbiz", "Small-business banking", "Banking and Izipay acquiring sold together: loans up 31% and deposits up 32% a year to June 2026, now about 36% of low-cost wholesale deposits.",
              s=["sme"], lc="everyday", neo=[1, "Izipay acquires Mastercard."],
              mc="No business-card network is disclosed; commercial cards are open ground.",
              src=[["IFS 2Q26 call", Q2T]]),
        ]},
        {"id": "4.4", "ic": "building-2", "name": "Commercial & corporate", "blurb": "S/24.7bn of loans.", "div": "interbank", "rev": "commercial", "products": [
            P("commercial", "Commercial banking", "Corporate and mid-sized companies: S/24.7 billion of loans, an 11.3% share, in working capital, trade finance and leasing.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["IFS 2Q26 results", Q2R], ["Interbank annual report 2025", MEM]]),
            P("capmkts", "Capital markets & treasury", "Foreign exchange, derivatives and the bank's own funding in local and international bond markets.",
              s=["corp"], lc="grow", neo=[0, ""], src=[["Interbank annual report 2025", MEM]]),
        ]},
        {"id": "4.5", "ic": "gem", "name": "Insurance & wealth", "blurb": "Interseguro, Inteligo.", "div": "interseguro", "rev": "group", "products": [
            P("interseguro", "Interseguro", "The IFS insurer and annuities leader: net income S/118.8 million in 2Q26, premiums up 9% a year.",
              s=["aff"], lc="grow", neo=[0, ""], src=[["IFS 2Q26 results", Q2R], ["IFS 2Q26 call", Q2T]]),
            P("inteligo", "Inteligo & Interfondos", "Private banking and funds with assets under management of about US$10 billion (+14% a year).",
              s=["aff"], lc="grow", neo=[0, ""], src=[["IFS 2Q26 call", Q2T]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: the Interbank app for 86% of retail clients, One App Negocios for businesses, the branch network, and Intercorp's supermarkets and malls.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Interbank app", "blurb": "86% digital.", "div": "interbank", "rev": "retail", "products": [
            P("app", "Interbank app", "86% of retail customers are digital; NPS 61 in retail; Plin built in.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["IFS 2Q26 call", Q2T]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "One App Negocios", "blurb": "Volumes up 117%.", "div": "interbank", "rev": "commercial", "products": [
            P("oneapp", "One App Negocios", "One app for business banking and Izipay acquiring; transaction volumes up 117% from January to June 2026; 76% of commercial clients digital.",
              s=["sme", "merch"], lc="everyday", st="new", neo=[0, ""], src=[["IFS 2Q26 call", Q2T]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches", "blurb": "Tiendas across Peru.", "div": "interbank", "rev": "retail", "products": [
            P("branches", "Branches (tiendas)", "A national network of stores, including Money Market branches in supermarkets since 2005; current count not found ⚠.",
              s=["con"], lc="everyday", o="I", neo=[0, ""], src=[["Interbank annual report 2025", MEM]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Partners & ecosystem", "blurb": "Intercorp retail, Izipay.", "div": "ifs", "rev": "group", "products": [
            P("ecosystem", "Intercorp ecosystem & Izipay network", "Supermercados Peruanos, InRetail and Real Plaza in the Intercorp group, and Izipay's merchants as a channel to sell Interbank products.",
              s=["con", "merch"], lc="open", o="P", at="Intercorp", neo=[0, ""], src=[["Interbank annual report 2025", MEM], ["Gestión: Izipay as distribution", IZIDIST]]),
            P("rappibank", "Rappibank", "A joint venture with Rappi for cards and accounts (2021), wound down by October 2023; network not confirmed ⚠.",
              s=["con"], lc="open", st="retired", o="P", at="Rappi", neo=[None, "Network not confirmed."], src=[["Forbes Perú: Rappibank ends, Aug 2023", RAPPI]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Interbank", "blurb": "Izipay's roots, a small card range.", "products": [
        P("mcatinterbank", "Mastercard at Interbank", "Visa carries Interbank's main credit and debit cards and Amex the premium end. Mastercard has a small credit range ⚠, Izipay's history as its Peruvian acquirer, and Plin's use of card rails at launch ⚠. No joint announcements were found for 2020–2026.",
          s=["con"], div="interbank", rev="group", mc="The relationship this map is drawn for.",
          src=[["Rankia: Interbank cards, Aug 2026", RANKIA], ["BBVA: multi-brand acceptance", MULTI]]),
    ]},
    {"id": "pillar-market", "name": "Peruvian banking", "blurb": "Wallets, El Niño, a new government.", "products": [
        P("market", "The Peruvian market", "Wallets are taking share from cards: Yape (BCP) has about 14 million users and wallets were forecast to reach 28% of payments by 2027; wallet interoperability is mandated; El Niño and a new government (July 2026) shape 2026.",
          s=["con"], div="interbank", rev="group", src=[["Infobae: wallets and cards, May 2025", INFOBAE], ["IFS 2Q26 call", Q2T]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
