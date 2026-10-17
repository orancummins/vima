"""BBVA's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the January–June 2026 report (30 July 2026),
BBVA in 2025 and the 2025 annual report, and BBVA México's 2T26 quarterly report. Garanti BBVA (Turkey) is a
separate customer. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it,
2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1R = "https://shareholdersandinvestors.bbva.com/wp-content/uploads/2026/07/January-June-Report-2026.pdf"
Q2P = "https://shareholdersandinvestors.bbva.com/wp-content/uploads/2026/07/2Q26-ENG-Earnings-Presentation_Analysts.pdf"
B25 = "https://shareholdersandinvestors.bbva.com/wp-content/uploads/2026/03/BBVA-in-2025_ENG.pdf"
AR25 = "https://shareholdersandinvestors.bbva.com/wp-content/uploads/2026/03/Annual-Report-BBVA-2025_ENG.pdf"
URD = "https://shareholdersandinvestors.bbva.com/wp-content/uploads/2026/03/URD-BBVA-2025_ENG.pdf"
MX2T = "https://investors.bbva.mx/wp-content/uploads/2026/08/Reporte-Trimestral-BBVA-México-2T26.pdf"
MXPLAN = "https://www.bbva.com/es/economia-y-finanzas/bbva-detalla-su-hoja-de-ruta-para-mexico-hasta-2029-con-foco-en-el-crecimiento-y-la-transformacion/"
WIKI = "https://en.wikipedia.org/wiki/BBVA"
ELECH = "https://expansion.mx/economia/2026/07/29/bbva-mexico-nombra-jose-luis-elechiguerra-country-manager"
SAB = "https://thecorner.eu/news-spain/bbva-gives-up-after-failure-of-its-takeover-bid-opa-for-banco-sabadell-accepted-by-only-25-33-of-the-capital/122490/"
CARDHIST = "https://www.estrategiasdeinversion.com/actualidad/noticias/empresas/bbva-40-anos-de-innovacion-en-tarjetas-n-139536"
OPENAI = "https://www.fstech.co.uk/fst/BBVA_To_Roll_Out_ChatGPT_Across_120000_Strong_Global_Workforce.php"
QIV = "https://www.fstech.co.uk/fst/BBVA_Joins_European_Stablecoin_Coalition.php"
MXCC = "https://www.bbva.mx/personas/productos/tarjetas-de-credito.html"
MXPLAT = "https://www.bbva.mx/personas/productos/tarjetas-de-credito/tarjeta-de-credito-platinum.html"
MXAZUL = "https://www.bbva.mx/personas/productos/tarjetas-de-credito/tarjeta-de-credito-azul.html"
MXLIB = "https://www.bbva.mx/personas/productos/cuentas/cuenta-libreton-basico.html"
MXVISA = "https://www.bbva.com/es/mx/gracias-a-visa-los-tarjetahabientes-de-bbva-podran-vivir-la-copa-mundial-de-la-fifa-2026/"
AQUA = "https://www.helpmycash.com/tarjetas/bbva/tarjeta-aqua-debito"
OCU = "https://www.ocu.org/dinero/tarjetas/noticias/tarjeta-aqua-bbva"
VPREM = "https://forbes.es/economia/890631/bbva-y-visa-lanzan-una-nueva-gama-de-tarjetas-en-espana-para-clientes-de-alto-valor/"
RENFE = "https://www.estrategiasdeinversion.com/actualidad/noticias/otras/bbva-y-renfe-lanzan-una-tarjeta-de-credito-vinculada-n-533741"
ITCC = "https://www.aziendabanca.it/notizie/banche/carta-di-credito-bbva"
DECC = "https://www.bbva.com/en/innovation/bbva-launches-a-credit-card-in-germany-and-expands-its-financial-products-offering/"
DE6 = "https://www.bbva.com/en/innovation/bbva-reaches-six-figure-customer-base-in-germany-with-23-of-customers-holding-over-100000-e/"
DELAUNCH = "https://thepaypers.com/fintech/news/bbva-launches-its-digital-bank-in-germany"
SABRE = "https://www.bbva.com/en/innovation/bbva-partners-with-mastercard-and-sabre-direct-pay-to-transform-travel-agency-payments-in-mexico/"
VAGENT = "https://www.bbva.com/en/innovation/bbva-completes-its-first-ai-agent-initiated-transaction-together-with-visa/"
BIZUM = "https://www.infobae.com/espana/agencias/2026/01/19/el-volumen-de-operaciones-con-bizum-crecio-un-53-en-2025-y-se-situo-en-67751-millones/"
BIZUMNFC = "https://www.mobileworldlive.com/spanish/bizum-acelera-su-despliegue-en-el-pago-presencial-ya-llega-a-20-millones-de-usuarios/"
WERO = "https://www.eldiario.es/sociedad/plataforma-paneuropea-bizums-avanza-finales-2026-podran-operar-particulares_1_12879881.html"
SPEI = "https://expansion.mx/economia/2026/08/11/transferencias-spei-superan-pago-tarjetas-mexico"
SPEIX = "https://www.veritas.org.mx/Economia-y-finanzas/Fintech/SPEI-CoDi-DiMo-y-la-evolucion-de-los-pagos-digitales-en-Mexico"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · governance · plan", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: €965 billion of assets and a ROTE of 22%, a bank dating from 1857 that issued Spain's first card, AI at the centre of the 2025–2029 plan, and a failed bid for Sabadell.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "€6.1bn profit in H1, ROTE 22%.", "div": "group", "rev": "cc", "products": [
            P("balance", "Balance sheet & earnings", "Net attributable profit of €6,051 million in H1 2026 (+11.1%), ROTE 22.2%, efficiency 37.8% and CET1 12.90%; total assets €965 billion, loans €522.5 billion, deposits €533 billion; 82.8 million active customers and 126,994 employees at 30 June 2026; market value €122 billion.",
              s=["con"], neo=[0, ""], src=[["BBVA: January–June 2026 report", H1R]]),
            P("fy25", "2025 and the franchises", "Record 2025 profit of €10.5 billion (ROTE 19.3%): Mexico €5.26 billion and Spain €4.18 billion, then Turkey, South America and Rest of Business; 11.5 million new customers, 66% through digital channels. Rated A+ (S&P), A2 (Moody's) and A (Fitch) after upgrades in late 2025.",
              s=["con"], neo=[0, ""], src=[["BBVA in 2025", B25], ["BBVA annual report 2025", AR25]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Heritage & governance", "blurb": "1857; Torres and Genç.", "div": "group", "rev": "cc", "products": [
            P("leadership", "Board & senior management", "Chair Carlos Torres Vila, CEO Onur Genç, Finance María Luisa Gómez Bravo; Peio Belausteguigoitia runs Spain, and José Luis Elechiguerra became Director General of BBVA México on 1 September 2026, with Eduardo Osuna proposed as chairman ⚠.",
              s=["corp"], st="flux", neo=[0, ""], src=[["BBVA: URD 2025", URD], ["Expansión: Elechiguerra, Jul 2026", ELECH]]),
            P("heritage", "Heritage & listing", "Banco de Bilbao (1857), Vizcaya (1901) and Argentaria merged by 1999; listed in Madrid, New York and Mexico. Banco de Bilbao issued Spain's first bank card in April 1971 with BankAmericard, the forerunner of Visa, and Europe's first Visa Oro in 1982.",
              s=["con"], o="I", neo=[0, "Its card history is Visa's."], src=[["Wikipedia: BBVA", WIKI], ["Estrategias de Inversión: 40 years of cards, 2011", CARDHIST]]),
        ]},
        {"id": "1.3", "ic": "brain", "name": "AI & technology", "blurb": "ChatGPT for 120,000.", "div": "group", "rev": "cc", "products": [
            P("ai", "AI strategy & OpenAI", "Eight AI initiatives ('The 8'): the Blue assistant, an AI banker, risk, operations, software, an 'alter ego' for every employee, data and agent architecture. ChatGPT Enterprise for all 120,000 employees (December 2025, up from 11,000), and a new AI Transformation unit in 2026.",
              s=["corp"], lc="beyond", st="new", ay="Dec 2025", o="P", at="OpenAI", neo=[0, ""],
              mc="An AI-first bank with no Mastercard agentic work in public.",
              src=[["FStech: ChatGPT for 120,000, Dec 2025", OPENAI], ["BBVA annual report 2025", AR25], ["BBVA: January–June 2026 report", H1R]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy & deals", "blurb": "ROTE c.22%; Sabadell failed.", "div": "group", "rev": "cc", "products": [
            P("strategy", "2025–2029 Strategic Plan", "Six priorities, among them a radical customer perspective, enterprise segments and AI; goals for 2025–28 of ROTE about 22%, cost:income about 35% and about €48 billion of cumulative profit (€16.6 billion by June 2026); €700 billion of sustainable business by 2029.",
              s=["corp"], st="new", neo=[0, ""], src=[["BBVA: January–June 2026 report", H1R], ["BBVA in 2025", B25]]),
            P("deals", "Deals", "BBVA USA sold to PNC for US$11.6 billion (2020–21), Garanti raised to about 86% (2022), a bid for Banco Sabadell that failed with 25.33% acceptance (16 October 2025), Garanti BBVA Romania sold to Raiffeisen for about €591 million (March 2026), and buybacks of almost €4 billion.",
              s=["corp"], o="A", neo=[0, ""], src=[["The Corner: Sabadell bid fails, Oct 2025", SAB], ["Wikipedia: BBVA", WIKI], ["BBVA: January–June 2026 report", H1R]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Visa cards for 34.5 million Mexicans, Visa debit and premium credit in Spain beside a Renfe Mastercard, Mastercard credit at the Italian and German digital banks, Mastercard virtual cards for Mexican travel agencies, 411,000 terminals, Bizum and SPEI, and a euro stablecoin.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Mexico cards", "blurb": "Visa, 31% of credit cards.", "div": "mexico", "rev": "mexico", "products": [
            P("mxcredit", "BBVA México credit cards", "Eleven cards from Mi Primera Tarjeta and Start to Azul, Oro and Platinum, plus IPN, UNAM and Rayados affinity cards: a Ps 232 billion book (+12.2%), 31.4% of the market, more than 10 million active cardholders and 1.5 million new cards in H1 2026. Benefits are Visa's (Concierge, Luxury Hotel Collection, insurance).", short="Mexico credit (Visa)",
              s=["con", "newc"], lc="borrow", o="P", at="Visa", neo=[0, "Visa; one page still says 'Visa / Mastercard' ⚠."],
              mc="The largest card franchise in Mexico, and it is Visa's.",
              src=[["BBVA México: credit cards", MXCC], ["BBVA México: Platinum", MXPLAT], ["BBVA México: Azul", MXAZUL], ["BBVA México 2T26 report", MX2T], ["BBVA: Mexico roadmap, Mar 2026", MXPLAN]]),
            P("mxdebit", "BBVA México debit cards", "Physical and digital debit cards on Libretón and other accounts; BBVA México and Visa ran a 2025 World Cup programme for 'any Visa card issued by BBVA México', credit or debit.", short="Mexico debit (Visa)",
              s=["con"], lc="everyday", ay="Jun 2025", o="P", at="Visa", neo=[0, "Visa."],
              src=[["BBVA México: Libretón", MXLIB], ["BBVA: Visa World Cup alliance, Jun 2025", MXVISA]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Spain cards", "blurb": "Visa debit; a Renfe Mastercard.", "div": "spain", "rev": "spain", "products": [
            P("esdebit", "Aqua debit", "Numberless debit card with a dynamic CVV that changes every five minutes (Aqua range launched 2020); free for linked customers, otherwise €35 a year. Listed as Visa by a comparison site ⚠.", short="Aqua debit (Visa ⚠)",
              s=["con"], lc="everyday", o="B", at="Visa", neo=[0, "Visa ⚠ third-party source."],
              src=[["HelpMyCash: Aqua Débito, Sep 2026", AQUA], ["OCU: Aqua, Nov 2020", OCU]]),
            P("escredit", "Aqua credit range", "Aqua Más and Aqua Máxima numberless credit cards with dynamic CVV and deferred payment; the contracts refer to 'Visa/MasterCard' without saying which ⚠.", short="Aqua credit (network ⚠)",
              s=["con"], lc="borrow", st="unconf", neo=[None, "Network not confirmed ⚠."],
              mc="If any of the range is open to a choice, it is the largest Spanish book Mastercard could contest.",
              src=[["OCU: Aqua, Nov 2020", OCU]]),
            P("espremium", "Visa Infinite, Platinum & Aqua Oro", "A premium range for Patrimonios, Banca Privada and Banca Personal clients, launched with Visa on 16 March 2026: no FX fees, lounges and fast-track on Infinite, travel cover on Platinum.", short="Premium (Visa)",
              s=["prem"], lc="borrow", st="new", ay="Mar 2026", o="P", at="Visa", neo=[0, "Visa."],
              src=[["Forbes España: BBVA and Visa premium range, Mar 2026", VPREM]]),
            P("renfe", "Renfe Mastercard", "Co-branded credit card with the Más Renfe loyalty programme, issued by BBVA Consumer Finance in three tiers (Clásica, Viaja, Descubre) from June 2022; points for AVE and long-distance tickets.", short="Renfe Mastercard",
              s=["con"], lc="borrow", ay="Jun 2022", o="P", at="Renfe, Mastercard", neo=[2, "Mastercard."],
              src=[["Estrategias de Inversión: Renfe Mastercard, Jun 2022", RENFE]]),
        ]},
        {"id": "2.3", "ic": "rocket", "name": "Digital-bank cards", "blurb": "Mastercard credit in Italy, Germany.", "div": "digital", "rev": "rest", "products": [
            P("itcredit", "BBVA Italy credit card", "Numberless credit card with a dynamic CVV and limits of €600–6,000, launched through a 'strategic agreement with Mastercard' (November 2024); Pay&Plan instalments.", short="Italy credit (Mastercard)",
              s=["saver"], lc="borrow", ay="Nov 2024", o="P", at="Mastercard", neo=[2, "Mastercard."],
              src=[["AziendaBanca: BBVA credit card in Italy, Nov 2024", ITCC]]),
            P("decredit", "BBVA Germany credit card", "BBVA Germany's first credit card, launched 17 June 2026 in partnership with Mastercard: no FX fees, 13.99% APR, a dynamic CVV that changes every seven minutes and 5% cashback on travel and online for six months.", short="Germany credit (Mastercard)",
              s=["saver"], lc="borrow", st="new", ay="Jun 2026", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard's newest BBVA programme, with Mastercard Germany's country manager at the launch.",
              src=[["BBVA: credit card in Germany, Jun 2026", DECC]]),
            P("dedebit", "Digital-bank debit cards", "Debit cards on the free German current account (3% cashback for the first year at the June 2025 launch) and the Italian account ⚠ network not confirmed.",
              s=["saver"], lc="everyday", neo=[None, "Network not confirmed ⚠."],
              src=[["The Paypers: BBVA digital bank in Germany, Jul 2025", DELAUNCH]]),
        ]},
        {"id": "2.4", "ic": "briefcase-business", "name": "Commercial & virtual cards", "blurb": "Mastercard VCNs with Sabre.", "div": "mexico", "rev": "mexico", "products": [
            P("vcn", "Travel-agency virtual cards", "Single-use virtual card numbers for Mexican travel agencies to pay airlines and hotels, with a credit line and reconciliation on Sabre Direct Pay; launched 30 September 2025, with South America and Europe planned.", short="Virtual cards (Mastercard)",
              s=["corp"], lc="move", st="new", ay="Sep 2025", o="P", at="Mastercard, Sabre", neo=[3, "Mastercard virtual card technology."],
              mc="The one BBVA México programme on Mastercard, and it is meant to travel.",
              src=[["BBVA: Mastercard and Sabre Direct Pay, Sep 2025", SABRE]]),
            P("mxbizcards", "Business cards & Anticipo TPV", "Business cards, digital credit lines and advances on terminal sales for 1.1 million SME clients ⚠ card network not stated.",
              s=["sme"], lc="borrow", neo=[None, "Network not stated ⚠."], src=[["BBVA México 2T26 report", MX2T]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acceptance", "blurb": "411,000 terminals in Mexico.", "div": "mexico", "rev": "mexico", "products": [
            P("barrio", "Banco de Barrio terminals", "BBVA México's financial-inclusion programme has signed more than 590,000 clients, installed 411,000 point-of-sale terminals and opened 1.2 million payroll accounts.",
              s=["sme"], lc="move", o="B", neo=[1, "Accepts every network."],
              mc="Merchant data from 411,000 small-business terminals.",
              src=[["BBVA México 2T26 report", MX2T]]),
            P("openpay", "Openpay", "BBVA's online payment gateways in Mexico, Colombia, Peru and Argentina; BBVA Peru also holds an affiliate stake in VisaNet Peru ⚠ volumes not published.",
              s=["sme"], lc="move", o="A", neo=[1, "Accepts every network."], src=[["BBVA annual report 2025", AR25]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Bizum & SPEI", "blurb": "Account-to-account at home.", "div": "group", "rev": "spain", "products": [
            P("bizum", "Bizum (Spain)", "Spain's bank-owned mobile payments: 30.6 million users and 1,237 million operations worth €67.8 billion in 2025; the second e-commerce method; in-store NFC opened in 2026 ⚠ figures differ; interlinking with Wero agreed in February 2026.",
              s=["con"], lc="move", st="flux", o="P", at="Bizum", neo=[0, "Bizum; not Mastercard."],
              mc="Bizum at the till competes with BBVA's own cards.",
              src=[["Infobae: Bizum 2025, Jan 2026", BIZUM], ["Mobile World Live: Bizum in store", BIZUMNFC], ["elDiario.es: Bizum and Wero", WERO]]),
            P("spei", "SPEI, CoDi & DiMo (Mexico)", "Banxico's real-time rail: more than 7,300 million transfers in 2025 (+36.8%), used by about 73.5 million adults; Banxico expects it to overtake card payments by the end of 2026. CoDi (QR, 2019) and DiMo (phone number, 2023) have not reached mass use ⚠.",
              s=["con", "sme"], lc="move", st="flux", o="P", at="Banxico", neo=[0, "Banxico; not Mastercard."],
              mc="Most of BBVA México's 2,421 million H1 transactions run on its own app and transfers, not cards ⚠.",
              src=[["Expansión: SPEI overtakes cards, Aug 2026", SPEI], ["Veritas: SPEI, CoDi and DiMo", SPEIX]]),
        ]},
        {"id": "2.7", "ic": "coins", "name": "Digital money", "blurb": "Qivalis euro stablecoin.", "div": "cib", "rev": "rest", "products": [
            P("qivalis", "Qivalis euro stablecoin", "BBVA joined the Amsterdam-based consortium of about a dozen European banks in February 2026; a MiCA euro stablecoin for payments and tokenised-asset settlement, launch planned for H2 2026 pending a Dutch e-money licence.",
              s=["corp"], lc="move", st="new", ay="Feb 2026", o="P", at="Qivalis", neo=[0, "Banks' own token."],
              src=[["FStech: BBVA joins Qivalis, Feb 2026", QIV]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: numberless cards with dynamic CVVs, BBVA's first AI-agent payment on Visa, the Blue assistant on OpenAI models, and Puntos BBVA rewards.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Card security", "blurb": "Numberless, dynamic CVV.", "div": "group", "rev": "spain", "products": [
            P("dyncvv", "Numberless cards & dynamic CVV", "No printed number or CVV on Aqua cards in Spain, on Mexican digital cards and on the Italian and German credit cards; the app shows a CVV that changes every five to seven minutes.",
              s=["con", "saver"], lc="everyday", o="B", neo=[1, "BBVA's own; Mastercard's network on the Italian and German cards."],
              src=[["OCU: Aqua, Nov 2020", OCU], ["BBVA: credit card in Germany, Jun 2026", DECC]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "Agentic commerce", "blurb": "First agent payment, on Visa.", "div": "spain", "rev": "spain", "products": [
            P("agentic", "AI-agent payments", "BBVA completed its first payment initiated by an AI agent with real card credentials, through Visa Intelligent Commerce and Visa Payment Passkeys in Visa's Agentic Ready programme (2 July 2026); Roberto Pagán, Head of Consumer Payments, BBVA Spain.",
              s=["con"], lc="everyday", st="new", ay="Jul 2026", o="P", at="Visa", neo=[0, "Visa."],
              mc="Agent Pay has no BBVA pilot in public; Visa is first.",
              src=[["BBVA: first agent-initiated payment with Visa, Jul 2026", VAGENT]]),
        ]},
        {"id": "3.3", "ic": "sparkles", "name": "Blue & AI for customers", "blurb": "An assistant on OpenAI.", "div": "group", "rev": "mexico", "products": [
            P("blue", "Blue", "BBVA's digital assistant, built on OpenAI models and moving to conversational, multimodal advice that can execute transactions, with voice in Mexico; BBVA is exploring banking inside ChatGPT, and Germany lists ChatGPT Apps integration.",
              s=["con"], lc="everyday", st="new", o="P", at="OpenAI", neo=[0, ""],
              src=[["BBVA annual report 2025", AR25], ["FStech: ChatGPT for 120,000, Dec 2025", OPENAI], ["BBVA: Germany six figures, Apr 2026", DE6]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Rewards", "blurb": "Puntos BBVA, Visa benefits.", "div": "mexico", "rev": "mexico", "products": [
            P("puntos", "Puntos BBVA & card benefits", "Mexican credit cards return 5–15% of purchases as Puntos BBVA, and premium cards add Visa Concierge, hotel and airport benefits; in Europe, cashback on the German cards and Más Renfe points.",
              s=["con", "prem"], lc="grow", o="B", neo=[0, "Visa benefits in Mexico."],
              mc="Card-linked offers and Priceless benefits are untested at BBVA.",
              src=[["BBVA México: credit cards", MXCC], ["BBVA México: Platinum", MXPLAT]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: Spanish retail and wealth, Mexico's biggest bank with a quarter of mortgages, a million SMEs, corporate and investment banking, digital banks in Italy and Germany, and South America.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Spain", "blurb": "€4.2bn profit in 2025.", "div": "spain", "rev": "spain", "products": [
            P("esretail", "BBVA Spain", "Loans of €201 billion and deposits of €240 billion, H1 2026 profit €2,172 million and efficiency 33.6%; loan share up to about 14% and consumer about 16.7% ⚠ read from a chart; 1,865 branches.",
              s=["con", "sme"], lc="everyday", neo=[0, "Visa debit."], src=[["BBVA: January–June 2026 report", H1R], ["BBVA 2Q26 presentation", Q2P]]),
            P("eswealth", "Wealth, pensions & insurance", "€126.5 billion of mutual and pension funds and portfolios in Spain (+5.9% in the half), private and personal banking, and insurance sold under the Allianz bancassurance agreement.",
              s=["prem"], lc="grow", neo=[0, ""], src=[["BBVA: January–June 2026 report", H1R]]),
        ]},
        {"id": "4.2", "ic": "flag", "name": "Mexico", "blurb": "26% of loans, 34.5m customers.", "div": "mexico", "rev": "mexico", "products": [
            P("mxretail", "BBVA México", "Mexico's largest bank: 34.5 million customers (82% digital), 26.2% of loans and 24.2% of deposits, efficiency 30.8% and H1 2026 profit of €2,979 million; personal and payroll loans Ps 257 billion, auto Ps 83 billion.",
              s=["con", "newc"], lc="everyday", neo=[0, "Visa cards."], src=[["BBVA México 2T26 report", MX2T], ["BBVA: January–June 2026 report", H1R]]),
            P("mxmortgage", "Mortgages", "A Ps 401 billion book (+7.4%) and more than a quarter of new Mexican mortgages (CNBV, May 2026).",
              s=["con"], lc="borrow", neo=[0, ""], src=[["BBVA México 2T26 report", MX2T]]),
        ]},
        {"id": "4.3", "ic": "briefcase", "name": "SMEs & companies", "blurb": "1.1 million SMEs in Mexico.", "div": "mexico", "rev": "mexico", "products": [
            P("smes", "SME & commercial banking", "1.1 million SME clients in Mexico and Crédito Digital Pyme (2026); penetration of medium-sized companies up to 28.3% and 21.8% of corporate credit; in Spain, lending to larger and mid-size companies grew about 2–3% in Q2 2026.",
              s=["sme"], lc="borrow", st="new", neo=[None, "Card network not stated ⚠."], src=[["BBVA México 2T26 report", MX2T], ["BBVA: Mexico roadmap, Mar 2026", MXPLAN], ["BBVA: January–June 2026 report", H1R]]),
        ]},
        {"id": "4.4", "ic": "building-2", "name": "Corporate & investment banking", "blurb": "Global markets, project finance.", "div": "cib", "rev": "rest", "products": [
            P("cib", "Corporate & Investment Banking", "Wholesale banking across the group, with Rest of Business (CIB in Europe, the US and Asia plus the digital banks) earning €508 million in H1 2026; project finance, corporate lending, Global Markets and transaction banking. 73,000 large corporates borrowed from BBVA in 2025.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["BBVA: January–June 2026 report", H1R], ["BBVA in 2025", B25]]),
        ]},
        {"id": "4.5", "ic": "globe", "name": "Digital banks", "blurb": "Italy and Germany.", "div": "digital", "rev": "rest", "products": [
            P("itbank", "BBVA Italy", "Fully digital bank launched in late 2021: more than 580,000 customers by November 2024 and a target of one million in 2026; accounts, Pay&Plan, loans and a Mastercard credit card.",
              s=["saver"], lc="everyday", neo=[1, "Mastercard credit; debit ⚠."], src=[["AziendaBanca: BBVA credit card in Italy, Nov 2024", ITCC], ["BBVA: Germany six figures, Apr 2026", DE6]]),
            P("debank", "BBVA Germany", "Launched June 2025 with a free interest-paying account; six-figure customer base by April 2026, 23% holding more than €100,000; One Click Loan, deposits up to 3.2% and a Mastercard credit card. Murat Kalkan is Global Head of Digital Banks.",
              s=["saver"], lc="grow", st="new", ay="Jun 2025", neo=[1, "Mastercard credit; debit ⚠."], src=[["BBVA: Germany six figures, Apr 2026", DE6], ["BBVA: credit card in Germany, Jun 2026", DECC]]),
        ]},
        {"id": "4.6", "ic": "earth", "name": "South America", "blurb": "Peru, Colombia, Argentina.", "div": "samerica", "rev": "samerica", "products": [
            P("samerica", "BBVA South America", "Banks in Argentina, Colombia, Peru, Uruguay and Venezuela: H1 2026 profit of €556 million, and €726 million in 2025 with lending up 13.9% ⚠ card networks not researched.",
              s=["con"], lc="everyday", neo=[None, "Not researched ⚠."], src=[["BBVA: January–June 2026 report", H1R], ["BBVA annual report 2025", AR25]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach BBVA: an app that sells about four in five products, 5,555 branches and 30,794 ATMs, and Banco de Barrio, co-brand partners and carmakers.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "BBVA app", "blurb": "79% of units sold digitally.", "div": "group", "rev": "mexico", "products": [
            P("app", "BBVA app", "About 79% of product units sold and 66% of new customers came through digital channels in 2025; 28.3 million digital customers in Mexico, where 76% of 2,421 million H1 2026 transactions were digital.",
              s=["con", "saver"], lc="open", neo=[0, ""], src=[["BBVA annual report 2025", AR25], ["BBVA México 2T26 report", MX2T]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "5,555 branches.", "div": "group", "rev": "spain", "products": [
            P("branches", "Branches & ATMs", "5,555 branches and 30,794 ATMs at 30 June 2026: Spain 1,865 branches and 4,602 ATMs; Mexico 1,604 branches and 14,434 ATMs.",
              s=["con", "prem"], lc="everyday", neo=[0, ""], src=[["BBVA: January–June 2026 report", H1R], ["BBVA México 2T26 report", MX2T]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partners & Banco de Barrio", "blurb": "Co-brands, carmakers, barrios.", "div": "mexico", "rev": "mexico", "products": [
            P("partners", "Partners & correspondents", "Banco de Barrio in Mexican neighbourhoods; affinity cards with IPN, UNAM and Rayados; carmaker alliances for auto finance; Renfe in Spain; Sabre Direct Pay for travel agencies.",
              s=["newc", "sme"], lc="open", o="P", neo=[1, "Renfe and Sabre on Mastercard; Mexican co-brands on Visa."],
              src=[["BBVA México 2T26 report", MX2T], ["BBVA México: credit cards", MXCC], ["Estrategias de Inversión: Renfe Mastercard, Jun 2022", RENFE]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at BBVA", "blurb": "Digital-bank credit, Renfe, virtual cards.", "products": [
        P("mcatbbva", "Mastercard at BBVA", "BBVA México's credit and debit cards and Spain's debit and premium credit run on Visa, and BBVA's first AI-agent payment (July 2026) ran on Visa Intelligent Commerce. Mastercard carries the Italian (2024) and German (2026) digital-bank credit cards, the Renfe co-brand in Spain (2022) and travel-agency virtual cards in Mexico with Sabre (2025). No group network agreement is public ⚠.",
          s=["con"], div="group", rev="cc", mc="The relationship this map is drawn for.",
          src=[["BBVA: credit card in Germany, Jun 2026", DECC], ["BBVA: Mastercard and Sabre Direct Pay, Sep 2025", SABRE], ["BBVA: Visa World Cup alliance, Jun 2025", MXVISA]]),
    ]},
    {"id": "pillar-market", "name": "Spain & Mexico", "blurb": "Bizum, SPEI, no Sabadell.", "products": [
        P("market", "The two home markets", "Spain: a tax on bank income, a failed Sabadell bid and Bizum moving into shops. Mexico: BBVA holds a quarter of loans, Banxico expects SPEI to overtake cards in 2026, and a new country manager from September 2026.",
          s=["con"], div="group", rev="cc", src=[["Expansión: SPEI overtakes cards, Aug 2026", SPEI], ["Infobae: Bizum 2025, Jan 2026", BIZUM], ["The Corner: Sabadell bid fails, Oct 2025", SAB]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
