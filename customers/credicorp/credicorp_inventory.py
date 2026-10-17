"""Credicorp's layers, areas and products (BCP, Yape and Mibanco at the core), as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the 1Q26 results release (15 May 2026), the 4Q25 release
(13 February 2026) and a summary of the 2Q26 results (August 2026). BCP's 2025 figures come via Wikipedia, which cites
BCP's 2025 Memoria Integrada and the SBS. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own
product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

GCHOME = "https://grupocredicorp.com/en/home/"
GCQ4 = "https://grupocredicorp.com/economia-peruana-creceria-35-durante-2026-estima-credicorp/"
GCQ1 = "https://grupocredicorp.com/yape-alcanzo-16-4-millones-de-usuarios-activos-mensuales-consolidando-su-cobertura-a-nivel-nacional/"
GCHELM = "https://grupocredicorp.com/banco-de-credito-del-peru-adquirira-el-100-de-helm-bank-usa/"
GCSUST = "https://grupocredicorp.com/iniciativas-de-inclusion-beneficiaron-a-millones-de-personas-en-los-ultimos-cinco-anos/"
GCIIF = "https://grupocredicorp.com/dos-de-cada-tres-peruanos-ya-usan-billeteras-digitales-y-empujan-la-inclusion-financiera-a-su-maximo-historico/"
Q2 = "https://quartr.com/events/credicorp-ltd-bap-q2-2026_Fk4RVchn"
Q2MB = "https://www.marketbeat.com/instant-alerts/credicorp-q2-earnings-call-highlights-2026-08-14/"
WIKIBCP = "https://en.wikipedia.org/wiki/Banco_de_Cr%C3%A9dito_del_Per%C3%BA"
ESWIKI = "https://es.wikipedia.org/wiki/Credicorp"
CAVERO = "https://gestion.pe/g-de-gestion/reportaje/bcp-diego-cavero-busca-crecer-mas-alla-del-pbi-tenemos-250-casos-de-uso-de-ia-noticia/"
KINEXYS = "https://gestion.pe/tu-dinero/bcp-adopta-plataforma-kinexys-de-jp-morgan-para-pagos-internacionales-noticia/"
HELMSBS = "https://gestion.pe/tu-dinero/bcp-obtiene-autorizacion-para-comprar-banco-en-eeuu-noticia/"
MIAMI = "https://gestion.pe/economia/empresas/bcp-miami-opera-como-sucursal-bancaria-en-eeuu-y-podra-atender-a-empresas-locales-noticia/"
MIBCEO = "https://gestion.pe/economia/empresas/credicorp-renueva-gerencia-general-en-mibanco-y-liderazgo-en-area-de-microfinanzas-noticia/"
NEOBANK = "https://gestion.pe/tu-dinero/yape-cada-vez-mas-cerca-de-ser-neobanco-cual-es-la-nueva-estrategia-de-credicorp-noticia/"
WALLETS = "https://gestion.pe/tu-dinero/yape-apple-pay-y-google-pay-que-billetera-digital-lleva-la-delantera-en-peru-noticia/"
MCPE = "https://gestion.pe/economia/empresas/mastercard-peru-y-su-estrategia-de-soluciones-mas-alla-de-las-tarjetas-tradicionales-noticia/"
MCXB = "https://gestion.pe/economia/empresas/mastercard-proximo-a-desarrollar-el-yape-para-remesas-los-detalles-interoperabilidad-remesas-noticia/"
MCSME = "https://gestion.pe/g-de-gestion/reportaje/mastercard-sobre-pymes-en-peru-anuncia-nuevas-verticales-avances-con-cooperativas-bancos-y-bcrp-noticia/"
ALIAS = "https://gestion.pe/tu-dinero/peruanos-duplican-pagos-al-instante-con-celular-y-qr-que-pasara-con-tiendas-que-no-los-acepten-noticia/"
BCRPREG = "https://gestion.pe/tu-dinero/yape-y-bancos-seran-multados-por-fallos-en-pagos-inmediatos-que-pasara-con-quejas-de-clientes-noticia/"
NEQUI = "https://gestion.pe/tu-dinero/yape-habilita-envio-de-dinero-a-nequi-en-colombia-los-pasos-a-seguir-noticia/"
YBOL = "https://gestion.pe/tu-dinero/bolivianos-se-rinden-ante-yape-que-ya-domina-el-altiplano-que-perseguira-en-dos-anos-noticia/"
KREALO = "https://gestion.pe/g-de-gestion/reportaje/krealo-de-credicorp-cerraria-el-ano-con-ocho-transacciones-el-destino-de-tenpo-y-tyba-noticia/"
BLANCO = "https://gestion.pe/economia/empresas/krealo-invierte-en-fintech-de-whatsapp-que-ya-movio-us-250-millones-en-creditos-pyme-noticia/"
CULQICEO = "https://gestion.pe/economia/empresas/credicorp-peru-spencer-friedman-es-nombrado-nuevo-ceo-de-culqi-noticia/"
BLOQUEO = "https://gestion.pe/tu-dinero/bcp-habilita-bloqueo-inmediato-de-tarjetas-desde-agentes-como-funcionara-noticia/"
YELITE = "https://gestion.pe/tu-dinero/yape-ya-se-codea-con-la-elite-de-los-bancos-peruanos-en-que-dio-el-gran-salto-noticia/"
BODEGAS = "https://gestion.pe/economia/empresas/yape-y-plin-dominan-pagos-en-bodegas-de-lima-73-de-ventas-ya-se-realiza-con-billeteras-digitales-noticia/"
R2 = "https://gestion.pe/tu-dinero/bcp-que-alista-en-peru-su-aliado-que-presta-a-conductores-de-uber-noticia/"
MIBYAPE = "https://gestion.pe/economia/empresas/clientes-de-mibanco-podran-pagar-sus-prestamos-por-yape-noticia/"
MIBWA = "https://gestion.pe/tu-dinero/whatsapp-cuando-se-podra-tomar-creditos-y-pagar-por-mensaje-el-plan-de-mibanco-noticia/"
COCOS = "https://gestion.pe/tu-dinero/banco-grande-deja-de-operar-plataforma-especializada-de-cambio-de-moneda-de-quien-se-trata-noticia/"
WARDA = "https://gestion.pe/tu-dinero/bcp-estima-4-millones-de-clientes-con-cuentas-ocultas-al-2028-noticia/"
YBANK = "https://gestion.pe/economia/empresas/yape-cuando-sera-dificil-diferenciarlo-de-un-banco-noticia/"
Y5Y = "https://gestion.pe/tu-dinero/yape-los-planes-de-credicorp-para-la-billetera-digital-en-el-proximo-quinquenio-noticia/"
SHARE = "https://gestion.pe/tu-dinero/accion-de-credicorp-repunta-54-en-el-ano-oportunidad-o-rally-agotado-noticia/"
CRIPTO = "https://gestion.pe/tu-dinero/bitcoin-bcp-el-gran-dilema-en-2026-lo-masificara-o-no-noticia/"
CEOS = "https://forbes.pe/negocios/2025-07-15/anuncian-cambios-de-ceo-en-pacifico-seguros-credicorp-capital-y-prima-afp/"
TPE = "https://tarjetas.pe/tarjeta-bcp"
MIBDEB = "https://www.mibanco.com.pe/servicios/tarjeta-de-debito"
YAPE = "https://www.yape.com.pe/"
YREM = "https://www.yape.com.pe/productos/remesas"
YCRED = "https://www.yape.com.pe/productos/creditos-yape"
YPROMO = "https://www.yape.com.pe/productos/yape-promos"
TENPO = "https://www.tenpo.cl/"
TENPONEO = "https://www.tenpo.cl/primer-neobanco"
BCPBO = "https://www.bcp.com.bo/Personas/TarjetaDeCredito"
BCPBOPP = "https://www.bcp.com.bo/TarjetaPrepago"
CULQI = "https://culqi.com/"
APPLEPAY = "https://support.apple.com/en-us/109524"
MULTI = "https://www.bbva.com/es/pe/innovacion/la-aceptacion-multimarca-de-las-tarjetas-en-peru/"
MC2019 = "https://www.mastercard.com/news/latin-america/pt-br/noticias/comunicados-de-imprensa/pr-pt/2019/dezembro/soluciones-de-visanet-a-nivel-nacional-aceptaran-pagos-con-tarjetas-mastercard-desde-el-2020"
WU = "https://secure.businesswire.com/news/home/20250814951664/es"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · brands · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Peru's largest financial group, ROE above 20%, a bank founded in 1889, about 250 AI use cases, and a target of 10% of revenue from new businesses.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "ROE 20.3% in 2Q26.", "div": "credicorp", "rev": "universal", "products": [
            P("balance", "Balance sheet & earnings", "Net income of S/1,982 million in 2Q26 (ROE 20.3%) and S/6,925 million in 2025 (ROE 19.0%); loans up 13.1% and deposits up 17.7% in a year; BCP held 33% of Peru's loans and 36% of deposits at end-2025 ⚠; ratings not confirmed ⚠.",
              s=["con"], neo=[0, ""], src=[["Quartr: 2Q26 summary", Q2], ["Credicorp: 4Q25 results, Feb 2026", GCQ4], ["Wikipedia: BCP (2025 Memoria, SBS)", WIKIBCP]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Ferrari, Cavero, Morales.", "div": "credicorp", "rev": "universal", "products": [
            P("leadership", "Board & executives", "Gianfranco Ferrari (Credicorp CEO), Diego Cavero (BCP CEO since 2022), Raimundo Morales (neobank unit: Yape, iO, Tenpo), Alejandro Pérez-Reyes (Mibanco from 1 October 2026) and Ignacio Belaunde (CFO from 1 October 2026); chair Luis Enrique Romero ⚠.",
              s=["corp"], neo=[0, ""], src=[["Gestión: new Mibanco CEO and CFO, May 2026", MIBCEO], ["Gestión: Diego Cavero, Aug 2026", CAVERO], ["Gestión: neobank unit, May 2026", NEOBANK], ["Wikipedia (es): Credicorp", ESWIKI]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & brands", "blurb": "Banco Italiano, 1889.", "div": "bcp", "rev": "universal", "products": [
            P("brands", "Heritage & brands", "Founded in 1889 as Banco Italiano and renamed BCP in 1942; Edyficar (2010) and Mibanco (2014) added microfinance; Yape launched in 2017. Today: BCP, Yape, iO, Mibanco, BCP Bolivia, Tenpo, Culqi, Pacífico, Prima AFP and Credicorp Capital; more than 40,000 staff in six countries.",
              s=["con"], o="I", neo=[0, ""], src=[["Wikipedia: BCP", WIKIBCP], ["Credicorp: home", GCHOME]]),
        ]},
        {"id": "1.4", "ic": "brain", "name": "Technology & AI", "blurb": "250 gen-AI use cases.", "div": "bcp", "rev": "universal", "products": [
            P("tech", "Core technology & AI", "About 250 generative-AI use cases (sales, collections, chatbots, process automation) and about 10,000 Copilot licences; half of BCP's staff used AI tools daily in 2025 ⚠; BCP handles about 3.5 million monetary transactions a day.",
              s=["corp"], neo=[0, ""], src=[["Gestión: Diego Cavero, Aug 2026", CAVERO], ["Wikipedia: BCP", WIKIBCP]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & ventures", "blurb": "10% of revenue from new.", "div": "credicorp", "rev": "universal", "products": [
            P("strategy", "Strategy", "Innovation at 9.9% of risk-adjusted revenue in 2Q26 against a 10% target; ROE guidance about 19.5% for 2026 and about 22% medium term; a neobank unit since 1 April 2026; Yape to become the second-largest business within three to five years.",
              s=["corp"], st="new", neo=[0, ""], src=[["Quartr: 2Q26 summary", Q2], ["Gestión: neobank unit, May 2026", NEOBANK], ["Gestión: Yape plans, Aug 2025", Y5Y]]),
            P("krealo", "Krealo", "Credicorp's venture arm since 2018: 17 investments, including Remitee, Akua and Welli (2025) and Jelou and Blanco (2026); majority owner of Tenpo and Tyba (about US$1.5 billion under management).",
              s=["corp"], o="B", neo=[0, ""], src=[["Gestión: Krealo, Dec 2025", KREALO], ["Gestión: Krealo invests in Blanco, Jul 2026", BLANCO]]),
            P("sustain", "Inclusion & sustainability", "Sustainability Strategy 2025–2030: 7 million people brought into the financial system through Yape and BCP between 2020 and May 2026, 1.3 million first loans through Yape since 2022, 3 million covered by inclusive insurance.",
              s=["yaper", "micro"], neo=[0, ""], src=[["Credicorp: Sustainability Report 2025, Jul 2026", GCSUST]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: Visa and Amex credit cards, Visa debit, Yape's account-to-account payments, remittances and blockchain transfers, Culqi's acquiring, and Visa cards in Bolivia beside Tenpo's prepaid Mastercard in Chile.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Credit cards", "blurb": "Visa and Amex; no Mastercard.", "div": "bcp", "rev": "universal", "products": [
            P("visacredit", "BCP Visa credit cards", "Visa Light, Clásica, LATAM Pass (Clásica to Signature), Infinite Sapphire and Iridium, and the Qore points range; BCP leads Peru with 34% of revolving card balances (end-2025) ⚠ and says it handles about 36% of Visa card volume in Peru ⚠.", short="BCP credit (Visa)",
              s=["con", "saver"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."],
              mc="Peru's largest card book is Visa's.",
              src=[["tarjetas.pe: BCP cards, Oct 2026", TPE], ["Wikipedia: BCP", WIKIBCP]]),
            P("amex", "BCP American Express", "Amex LATAM Pass Clásica, Oro, Platinum and Black; BCP and Interbank are Peru's two Amex issuers.", short="BCP Amex",
              s=["saver"], lc="borrow", o="P", at="American Express", neo=[0, "Amex."], src=[["tarjetas.pe: BCP cards, Oct 2026", TPE]]),
            P("io", "iO", "BCP's digital, no-fee credit card with cashback on digital purchases; enabled for Apple Pay and moved into the neobank unit in April 2026.", short="iO (Visa)",
              s=["con", "yaper"], lc="borrow", st="new", o="B", at="Visa", neo=[0, "Visa iO."], src=[["tarjetas.pe: BCP cards, Oct 2026", TPE], ["Apple: Apple Pay banks", APPLEPAY], ["Gestión: neobank unit, May 2026", NEOBANK]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Debit", "blurb": "Visa at BCP and Mibanco.", "div": "bcp", "rev": "universal", "products": [
            P("bcpdebit", "BCP debit card", "Debit cards on BCP savings and current accounts, and the key to the 'Débito BCP' Yape account, where the Yape balance is the BCP account; network not confirmed on a BCP page ⚠.", short="BCP debit (Visa ⚠)",
              s=["con", "yaper"], lc="everyday", o="P", at="Visa ⚠", neo=[0, "Visa ⚠."], src=[["Yape: account types", "https://www.yape.com.pe/tipos-de-cuenta"]]),
            P("mibdebit", "Mibanco debit card", "A debit card for micro-entrepreneurs, usable 'in Visa shops in Peru and abroad' without extra fees.", short="Mibanco debit (Visa)",
              s=["micro"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Mibanco: debit card", MIBDEB]]),
        ]},
        {"id": "2.3", "ic": "zap", "name": "Yape payments", "blurb": "16.7m monthly users.", "div": "yape", "rev": "universal", "products": [
            P("yapepay", "Yape payments", "Phone-number and QR payments, QR/POS merchant payments, bills, top-ups, transport cards and passport fees: 16.7 million monthly users making about 69 payments each in 2Q26 ⚠; payments were 47% of Yape revenue in 1Q26 and revenue-generating volume grew 50% a year.", short="Yape (A2A)",
              s=["yaper", "micro"], lc="move", o="B", neo=[0, "Own closed loop and account-to-account."],
              mc="The wallet that is replacing cash and, at the counter, cards.",
              src=[["Credicorp: 1Q26 results, May 2026", GCQ1], ["Gestión: Yape fee income, Feb 2026", YELITE], ["MarketBeat: 2Q26 call ⚠", Q2MB]]),
            P("interop", "Interoperability & immediate transfers", "BCRP-mandated interoperability since 2023 links Yape, Plin and banks; alias payments averaged S/16.5 billion and 225 million operations a month in January–May 2026; the CCE's real-time hub was built with Mastercard's real-time payments infrastructure ⚠; a UPI-style BCRP system is planned.", short="Interoperability (CCE)",
              s=["yaper", "con"], lc="move", o="P", at="BCRP, CCE", neo=[1, "CCE hub on Mastercard real-time infrastructure ⚠."],
              mc="Mastercard's quiet foothold: the rails under interbank transfers ⚠.",
              src=[["Gestión: immediate payments, Sep 2026", ALIAS], ["Gestión: Mastercard Peru, Jul 2023", MCPE], ["Gestión: neobank unit, May 2026", NEOBANK]]),
        ]},
        {"id": "2.4", "ic": "send", "name": "Cross-border & digital assets", "blurb": "Remittances, Kinexys, crypto.", "div": "bcp", "rev": "universal", "products": [
            P("remit", "Yape remittances", "Receive money from abroad in soles or dollars through Western Union, Ria, Remitly, Xoom, MoneyGram, Tenpo and others, free of charge; send to Nequi and Bancolombia in Colombia (February 2026).",
              s=["yaper", "con"], lc="move", st="new", o="P", at="Western Union, Ria, Remitly", neo=[0, "Money-transfer operators."],
              mc="No Mastercard rail in Yape's remittance list; Cross Border Services was built for exactly this.",
              src=[["Yape: remittances", YREM], ["Gestión: Yape to Nequi, Feb 2026", NEQUI], ["Business Wire: Yape and Western Union ⚠", WU]]),
            P("kinexys", "Kinexys cross-border payments", "First Latin American bank on J.P. Morgan's Kinexys blockchain deposit accounts: near-real-time transfers abroad, 24/7, for Telecrédito clients (June 2026).",
              s=["corp"], lc="move", st="new", ay="Jun 2026", o="P", at="J.P. Morgan", neo=[0, "J.P. Morgan."], src=[["Gestión: BCP adopts Kinexys, Jun 2026", KINEXYS]]),
            P("cripto", "Criptococos", "An SBS-supervised pilot (October 2025) to buy bitcoin and USDC: up to 3,000 users and US$3,000 each, 2,000 sign-ups; a decision on a wider launch is due at the end of 2026.",
              s=["saver"], lc="grow", st="new", ay="Oct 2025", o="B", neo=[0, ""], src=[["Gestión: Criptococos, Dec 2025", CRIPTO]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acquiring", "blurb": "Culqi, and Niubiz.", "div": "culqi", "rev": "universal", "products": [
            P("culqi", "Culqi", "Credicorp's payments fintech: online checkout, payment links and POS that take cards, Yape and other wallets from 3.44% a transaction, working with Niubiz and Izipay; CEO Spencer Friedman since September 2025.",
              s=["sme"], lc="move", o="A", neo=[1, "Accepts every network."], src=[["Culqi", CULQI], ["Gestión: Culqi CEO, Sep 2025", CULQICEO]]),
            P("niubiz", "Niubiz (ex-VisaNet)", "Peru's largest acquirer and Visa's historic one; it has accepted Mastercard since 2020 under a December 2019 deal. BCP's shareholding is not confirmed ⚠. Wallets rose to 18.4% of its volume by April 2026.",
              s=["sme"], lc="move", st="unconf", o="P", at="Niubiz", neo=[1, "Multi-brand since 2020; ownership ⚠."],
              src=[["Mastercard: VisaNet to accept Mastercard, Dec 2019 ⚠", MC2019], ["BBVA: multi-brand acceptance, Feb 2020", MULTI], ["Gestión: wallets and Niubiz, Jun 2026", WALLETS]]),
        ]},
        {"id": "2.6", "ic": "globe", "name": "Bolivia & Chile", "blurb": "Visa, and a Mastercard neobank.", "div": "tenpo", "rev": "universal", "products": [
            P("tenpo", "Tenpo cards (Chile)", "Chile's first neobank (licence January 2026, about 2.5 million clients) issues the Tarjeta Prepago Tenpo Mastercard and a credit card whose network is not shown ⚠; part of Credicorp's neobank unit.", short="Tenpo (Mastercard prepaid)",
              s=["con"], lc="everyday", st="new", o="A", at="Mastercard", neo=[1, "Prepaid on Mastercard; credit network ⚠."],
              mc="The group's one Mastercard issuer.",
              src=[["Tenpo", TENPO], ["Tenpo: first neobank", TENPONEO], ["Gestión: Krealo and Tenpo, Dec 2025", KREALO]]),
            P("bcpbo", "BCP Bolivia & Yape Bolivia", "BCP Bolivia issues Visa credit (to Signature) and Visa prepaid cards; Yape Bolivia had about 4 million users at end-2025, aims for 5.5 million in 2026 and is starting to lend.", short="BCP Bolivia (Visa) & Yape",
              s=["con", "yaper"], lc="everyday", o="I", at="Visa", neo=[0, "Visa; Yape A2A."], src=[["BCP Bolivia: credit cards", BCPBO], ["BCP Bolivia: prepaid", BCPBOPP], ["Gestión: Yape in Bolivia, Nov 2025", YBOL]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: an emergency card block at 10,000 agents and new rules on payment complaints, AI and agents, and Yape Promos and LATAM Pass miles.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "Block cards at any agent.", "div": "bcp", "rev": "universal", "products": [
            P("bloqueo", "Bloqueo de Emergencia", "Since November 2025 customers whose phone is stolen can block all BCP debit and credit cards at any of more than 10,000 BCP Agents, in 86% of districts; more than 4,000 phones are stolen in Peru a day.",
              s=["con"], lc="everyday", st="new", ay="Nov 2025", o="B", neo=[0, "BCP's own."], src=[["Gestión: emergency block, Nov 2025", BLOQUEO]]),
            P("scams", "Scams & payment disputes", "Yape anti-scam guidance and reporting of extortion accounts; BCRP rules (July 2026) require answers to complaints on immediate payments within 15 working days or fines of up to 120 UIT.",
              s=["yaper"], lc="everyday", st="new", o="B", neo=[0, ""],
              mc="Account-to-account fraud is the risk; Mastercard sells scam scoring for it.",
              src=[["Yape", YAPE], ["Gestión: BCRP rules, Jul 2026", BCRPREG]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI & agents", "blurb": "Agents next, says Cavero.", "div": "bcp", "rev": "universal", "products": [
            P("agents", "AI for customers", "Chatbots and AI tools for sales and collections today; next, AI agents to which customers delegate decisions, such as moving a month-end surplus into the best deposit (Diego Cavero, August 2026).",
              s=["con"], lc="everyday", st="new", neo=[None, "Nothing public."],
              mc="Agent Pay has no announced partner here.",
              src=[["Gestión: Diego Cavero, Aug 2026", CAVERO]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Loyalty & offers", "blurb": "Yape Promos, LATAM Pass.", "div": "yape", "rev": "universal", "products": [
            P("promos", "Yape Promos & Yape Tienda", "Discounts paid with Yape at Cineplanet, KFC, Burger King, Tambo and others, bought in-app or in-store; Yape Tienda, its marketplace, is being relaunched; e-commerce was 3% of Yape revenue in 1Q26.",
              s=["yaper"], lc="grow", o="B", neo=[0, ""],
              mc="Merchant-funded offers without a card network behind them.",
              src=[["Yape Promos", YPROMO], ["Yape", YAPE], ["Credicorp: 1Q26 results, May 2026", GCQ1]]),
            P("latam", "LATAM Pass & Qore", "Miles on BCP's Visa and Amex LATAM Pass cards (up to 2 miles per US$1 on Infinite Iridium) and Qore points that pay the statement.",
              s=["saver"], lc="grow", o="P", at="LATAM", neo=[0, "Visa and Amex."], src=[["tarjetas.pe: BCP cards, Oct 2026", TPE]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: Peru's biggest retail bank and mortgage book, Yape loans for 4.1 million people, SME and wholesale banking reaching into the US, Mibanco's microfinance, and Pacífico, Prima and Credicorp Capital.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Retail banking", "blurb": "13.7m retail clients.", "div": "bcp", "rev": "universal", "products": [
            P("retail", "BCP retail banking", "Banca Consumo, Exclusiva and Enalta for 13.7 million retail clients, 89% of whose monetary transactions are digital; 44% of individuals' savings and demand deposits (end-2025) ⚠.",
              s=["con"], lc="everyday", neo=[0, "Visa cards."], src=[["Wikipedia: BCP", WIKIBCP]]),
            P("mortgages", "Mortgages & consumer loans", "Peru's largest mortgage lender with 32.7% of mortgages and 39.5% of MiVivienda loans; personal and vehicle loans (end-2025) ⚠.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Wikipedia: BCP", WIKIBCP]]),
            P("warda", "Wardaditos", "Hidden savings pots fed by fixed amounts, a share of income or round-ups: 1.3 million clients and 4.5 million operations a month (April 2026), 4 million clients targeted by 2028.",
              s=["con", "yaper"], lc="grow", st="new", o="B", neo=[0, ""], src=[["Gestión: wardaditos, Apr 2026", WARDA]]),
        ]},
        {"id": "4.2", "ic": "hand-coins", "name": "Yape lending", "blurb": "4.1m borrowers.", "div": "yape", "rev": "universal", "products": [
            P("yapeloan", "Crédito Yape", "Single- and multi-instalment loans in the app, backed by BCP: 16 million loans to 4.1 million people, about a third new to credit; a book of about S/1.8 billion and 28% of Yape's risk-adjusted revenue in 2Q26 ⚠; SME loans since June 2025.",
              s=["yaper", "micro"], lc="borrow", st="new", o="B", neo=[0, ""],
              src=[["Yape: Crédito Yape", YCRED], ["Gestión: Yape fee income, Feb 2026", YELITE], ["MarketBeat: 2Q26 call ⚠", Q2MB], ["Gestión: Yape plans, Aug 2025", Y5Y]]),
        ]},
        {"id": "4.3", "ic": "briefcase", "name": "Small business", "blurb": "2.4m SME clients.", "div": "bcp", "rev": "universal", "products": [
            P("smallbiz", "BCP Small Business Banking", "2.4 million SME clients; 327,600 with active loans (+49% in 2025) ⚠; working capital, Factura Negociable and the Mi Negocio platform.",
              s=["sme"], lc="borrow", neo=[0, ""],
              mc="No business card on Mastercard; Mastercard is pitching SME data models in Peru.",
              src=[["Wikipedia: BCP", WIKIBCP], ["Gestión: Mastercard on SMEs, Jun 2026", MCSME]]),
            P("r2", "R2 partnership", "R2, a fintech, lends to SMEs with BCP using merchants' transaction data, with tickets of about S/700 to S/1,200 in its Uber driver programme.",
              s=["sme"], lc="borrow", st="new", o="P", at="R2", neo=[0, ""], src=[["Gestión: R2 and BCP, Sep 2026", R2]]),
        ]},
        {"id": "4.4", "ic": "building-2", "name": "Wholesale & US", "blurb": "Helm Bank, BCP Miami.", "div": "bcp", "rev": "universal", "products": [
            P("wholesale", "Wholesale & transaction banking", "Loans, trade finance, leasing, cash management and FX for Peru's corporates; Euromoney's best transaction bank in Peru, 2025.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Wikipedia: BCP", WIKIBCP]]),
            P("usexp", "Helm Bank USA & BCP Miami", "Helm Bank USA (US$1.1 billion of assets) agreed for US$180 million in December 2025, approved by the SBS in May 2026, US approvals pending ⚠; BCP Miami became a full branch in July 2026, aiming for about 100 new corporate clients by 2027.",
              s=["corp"], lc="move", st="flux", ay="Dec 2025", o="A", neo=[0, ""],
              src=[["Credicorp: Helm Bank, Dec 2025", GCHELM], ["Gestión: SBS approval, May 2026", HELMSBS], ["Gestión: BCP Miami branch, Aug 2026", MIAMI]]),
        ]},
        {"id": "4.5", "ic": "users-round", "name": "Microfinance", "blurb": "880,000 small borrowers.", "div": "mibanco", "rev": "micro", "products": [
            P("mibanco", "Mibanco", "Loans to more than 880,000 micro and small businesses, S/16.3 billion disbursed in 2025, ROE 22.9% in 2Q26 ⚠; loans payable by Yape since 2023; Mibanco Colombia alongside; new CEO Alejandro Pérez-Reyes from 1 October 2026.",
              s=["micro"], lc="borrow", st="flux", o="A", neo=[0, "Visa debit."],
              src=[["Credicorp: 4Q25 results, Feb 2026", GCQ4], ["Gestión: Mibanco via Yape, Jun 2023", MIBYAPE], ["Gestión: new Mibanco CEO, May 2026", MIBCEO], ["MarketBeat: 2Q26 call ⚠", Q2MB]]),
        ]},
        {"id": "4.6", "ic": "gem", "name": "Insurance, pensions & wealth", "blurb": "Pacífico, Prima, Tyba.", "div": "pacifico", "rev": "insurance", "products": [
            P("pacifico", "Pacífico, Prima AFP & Credicorp Capital", "Pacífico (second in Peruvian premiums, own claim) with 3 million on inclusive insurance and Tsana telehealth (1.3 million sign-ups in 2025); Prima AFP (second in pensions); Credicorp Capital and Tyba in Peru, Chile and Colombia.",
              s=["saver"], lc="grow", neo=[0, ""], src=[["Credicorp: home", GCHOME], ["Credicorp: Sustainability Report 2025, Jul 2026", GCSUST], ["Forbes Perú: new CEOs, Jul 2025", CEOS]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: the BCP app with Apple Pay, the Yape app, 305 branches and about 10,400 agents, and WhatsApp and Telecrédito.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "BCP app & wallets", "blurb": "89% of transactions digital.", "div": "bcp", "rev": "universal", "products": [
            P("app", "BCP app & Banca por Internet", "Mobile and online banking carrying 89% of retail monetary transactions; FX moved into the app and Yape when Cocos y Lucas closed in February 2026.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Wikipedia: BCP", WIKIBCP], ["Gestión: Cocos y Lucas closed, Mar 2026", COCOS]]),
            P("applepay", "Apple Pay & Google Pay", "BCP and iO cards are listed for Apple Pay in Peru; contactless wallet payments grew 42% in a year against 82% for QR (Niubiz).",
              s=["con"], lc="everyday", o="P", at="Apple, Google", neo=[0, "Visa and Amex cards."], src=[["Apple: Apple Pay banks", APPLEPAY], ["Gestión: wallets, Jun 2026", WALLETS]]),
        ]},
        {"id": "5.2", "ic": "wallet", "name": "Yape app", "blurb": "19m+ yaperos.", "div": "yape", "rev": "universal", "products": [
            P("yapeapp", "Yape app", "More than 19 million registered users and 16.7 million monthly active (2Q26) ⚠, about 82% of the working-age population; opens with a BCP debit card, a national ID or another bank's card; 73% of Lima bodega sales are paid by wallet.",
              s=["yaper"], lc="open", o="B", neo=[0, ""], src=[["Yape", YAPE], ["Credicorp: 1Q26 results, May 2026", GCQ1], ["Gestión: bodegas, Mar 2026", BODEGAS]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & agents", "blurb": "305 branches, 10,400 agents.", "div": "bcp", "rev": "universal", "products": [
            P("branches", "Branches, agents & ATMs", "About 305 branches, 10,400 BCP Agents (bodegas, pharmacies) and 2,400 ATMs at end-2025 ⚠; agents also cash out Yape and block cards.",
              s=["con", "micro"], lc="everyday", neo=[0, ""], src=[["Wikipedia: BCP", WIKIBCP], ["Gestión: emergency block, Nov 2025", BLOQUEO]]),
        ]},
        {"id": "5.4", "ic": "headset", "name": "WhatsApp & portals", "blurb": "Mibanco chat, Telecrédito.", "div": "mibanco", "rev": "micro", "products": [
            P("mibwa", "Mibanco por WhatsApp", "Accounts, balances and product information by WhatsApp since November 2025, combining AI and human advisers, with credit and transfers to follow in 2026.",
              s=["micro"], lc="open", st="new", ay="Nov 2025", o="P", at="Meta (WhatsApp)", neo=[0, ""], src=[["Gestión: Mibanco on WhatsApp, Nov 2025", MIBWA], ["Credicorp: 4Q25 results, Feb 2026", GCQ4]]),
            P("telecredito", "Telecrédito", "BCP's corporate banking portal, now sending transfers abroad over Kinexys.",
              s=["corp"], lc="move", neo=[0, ""], src=[["Gestión: BCP adopts Kinexys, Jun 2026", KINEXYS]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Credicorp", "blurb": "Visa cards, Yape rails, Tenpo.", "products": [
        P("mcatcredicorp", "Mastercard at Credicorp", "BCP's credit cards, iO, Mibanco's debit card and BCP Bolivia's cards are Visa, and the premium LATAM Pass range is split with Amex; no BCP Mastercard programme or joint announcement was found. Mastercard's footholds are Tenpo's prepaid card in Chile, acceptance through Culqi and Niubiz, and the CCE real-time hub ⚠; Yape's account-to-account payments carry no network.",
          s=["con"], div="credicorp", rev="universal", mc="The relationship this map is drawn for.",
          src=[["tarjetas.pe: BCP cards, Oct 2026", TPE], ["Tenpo", TENPO], ["Gestión: Mastercard Peru, Jul 2023", MCPE]]),
    ]},
    {"id": "pillar-market", "name": "Peruvian payments", "blurb": "Wallets, interoperability, El Niño.", "products": [
        P("market", "The Peruvian market", "Wallet use rose from 19% of people in 2021 to 65% in 2025; wallets were 35.9% of Niubiz transactions by April 2026; BCRP interoperability since 2023, new immediate-payment rules in July 2026 and a UPI-style system planned; El Niño provisions of S/106 million in 2Q26.",
          s=["con"], div="credicorp", rev="universal", src=[["Credicorp: inclusion index, Apr 2026", GCIIF], ["Gestión: wallets, Jun 2026", WALLETS], ["Gestión: BCRP rules, Jul 2026", BCRPREG], ["Quartr: 2Q26 summary", Q2]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
