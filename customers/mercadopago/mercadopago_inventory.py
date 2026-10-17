"""Mercado Pago's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Mercado Pago is the fintech business of MercadoLibre, Inc. (NASDAQ: MELI): figures are the group's own
releases (FY2025, 24 February 2026; Q2 2026, 5 August 2026), its IR newsletters and its country sites,
with press where marked. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product
runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

CMS = "https://http2.mlstatic.com/storage/ml-cms-backend/cms-documents-prod/5dbba919-721c-4916-bb91-c76a8713f7f0/"
Q2 = CMS + "bd60a342-c523-41b8-af7a-da2818fef5ff/MELI_Q2_2026_Press_Release.pdf"
NLJUN = CMS + "8baec7a6-1199-4b09-a82d-645ff576be32/MELI_IR_Newsletter_June2026.pdf"
NLMAR = CMS + "bd4f2906-167d-4612-8fa0-6d911201b556/Meli_Investor_Newsletter_March_2026.pdf"
BOND = CMS + "5b693125-1530-4caa-b06f-3cc16f933044/MELI_-_Sept_2026_Bond_-_Pricing_Press_Release_Exhibit_to_Pricing_8-K.pdf"
BEYOND = CMS + "573fff76-34d5-4fc4-9281-46701a7f10ba/Beyond_Banking_Investment_through_Mercado_Pago_June_2026.pdf"
FY25 = "https://mexicobusiness.news/ecommerce/news/mercado-libre-delivers-record-2025-sales-45-4q25-growth"
FY25BW = "https://www.businesswire.com/news/home/20260224265595/en/Mercado-Libre-Caps-Stellar-2025-Performance-with-45-YoY-Revenue-Growth-in-Q4-as-Strategic-Investments-Accelerate-Market-Share-Gains"
ABOUT = "https://investor.mercadolibre.com/about-meli"
BRHOME = "https://www.mercadopago.com.br"
BRCONTA = "https://www.mercadopago.com.br/conta"
BRCC = "https://www.mercadopago.com.br/conta/cartao-de-credito"
BRCCBLOG = "https://www.mercadopago.com.br/blog/vantagens-do-cartao-mercado-pago"
BRDEBIT = "https://www.mercadopago.com.br/blog/cartao-debito-mercado-pago-como-usar-vantagens"
BRCRYPTO = "https://www.mercadopago.com.br/criptomoedas"
BRPOINT = "https://www.mercadopago.com.br/ferramentas-para-vender/maquininhas-point"
BRTAP = "https://www.mercadopago.com.br/ferramentas-para-vender/tap-to-pay-no-iphone"
MXHOME = "https://www.mercadopago.com.mx"
MXCUENTA = "https://www.mercadopago.com.mx/cuenta"
MXCC = "https://www.mercadopago.com.mx/tarjeta-de-credito"
ARCC = "https://www.mercadopago.com.ar/tarjeta-de-credito"
ARCUENTA = "https://www.mercadopago.com.ar/cuenta"
ARPREPAID = "https://www.mercadopago.com.ar/tarjeta-prepaga"
MT2021 = "https://www.moneytimes.com.br/mercado-pago-lanca-cartao-de-credito/"
LR2023 = "https://www.larepublica.co/globoeconomia/mercado-pago-y-visa-buscan-acelerar-la-bancarizacion-de-mas-poblacion-en-mexico-3668598"
BNA2018 = "https://bnamericas.com/en/news/brief-mercado-pago-mastercard-launch-prepaid-card"
ITS2016 = "https://www.itsitio.com/noticias/acuerdo-entre-mastercard-mercado-pago-y-first-data-para-mejorar-la-experiencia-de-compra/"
IPROUP = "https://www.iproup.com/finanzas/4351-mercado-pago-banco-banco-digital-Mercado-Libre-y-Mastercard-dan-otro-paso-en-su-alianza-estrategica"
DF2022 = "https://www.df.cl/mercados/banca-fintech/mercado-libre-entra-al-negocio-de-tarjetas-de-prepago-fisicas-y-virtuales"
CHILE = "https://www.latamfintech.co/articles/mercado-pago-planea-lanzar-su-tarjeta-de-credito-en-chile-en-2026-para-competir-con-la-banca-tradicional"
FINS = "https://finsidersbrasil.com.br/bancos-digitais/mercado-pago-diz-que-licenca-bancaria-no-brasil-nao-e-prioridade/"
BLAR = "https://www.bloomberglinea.com/latinoamerica/argentina/mercado-pago-y-revolut-obtendran-licencia-bancaria-antes-de-2027-dice-director-del-bcra/"
DHAR = "https://dolarhoy.com/economia/hito-financiero-el-banco-central-aprobo-la-licencia-bancaria-para-mercado-pago-y-se-reconfigura-el-sistema-financiero-argentino-202610111380"
MXSEP = "https://www.descubre.vc/noticia/mercado-pago-avanza-hacia-licencia-bancaria-en-m-xico-y-apunta-al-mercado-de-n-mina-2026-09-10"
MXMAR = "https://www.descubre.vc/noticia/mercado-pago-proyecta-obtener-su-licencia-bancaria-en-m-xico-para-2026-2026-03-10"
MODO = "https://dolarhoy.com/empresas/guerra-de-billeteras-virtuales-mercado-pago-llego-a-un-acuerdo-con-modo-que-paso-ahora--20241151480"
PRISMA = "https://www.letrap.com.ar/visa-se-expande-argentina-compro-la-operacion-banelco-y-pagomiscuentas-prisma-n5421981/amp"
BAT = "https://www.batimes.com.ar/news/economy/mercadolibre-ceo-steps-aside-after-25-years-for-chairman-job.phtml"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "scale · licences · platform", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $12.6 billion of revenue in 2025 and $101 billion of payments in the second quarter of 2026, payment and credit licences in each country with bank licences pending in Mexico and Argentina, an investment-grade Nasdaq parent, and one in-house technology platform.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & growth", "blurb": "$12.6bn revenue, 88m users.", "div": "mp", "rev": "grp", "products": [
            P("scale", "Revenue & volume", "Net revenue of $12.6 billion in 2025 (+46%), up from $5.0 billion in 2022; $4.4 billion in the second quarter of 2026 (+49%), with total payment volume of $101 billion (+56%) and 5.2 billion transactions.",
              s=["cons", "sme"], neo=[0, ""], src=[["MELI: Q2 2026, Aug 2026", Q2], ["MELI IR newsletter, Jun 2026", NLJUN]]),
            P("users", "Users", "88 million monthly active users in the second quarter of 2026 (+30%), growing 38% in Brazil and 45% in Mexico; about 69 million customers in Brazil on Central Bank data (February 2026).",
              s=["cons"], neo=[0, ""], src=[["MELI: Q2 2026, Aug 2026", Q2], ["Finsiders, Feb 2026", FINS]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Licences", "blurb": "Payments and credit; banks pending.", "div": "mp", "rev": "grp", "products": [
            P("brlic", "Brazil licences", "A payment institution (Mercado Pago Instituição de Pagamento Ltda.), a financial institution (Mercado Crédito) and a securities distributor since 2024. No bank licence, which it says is not a priority for now (February 2026).",
              s=["cons", "sme"], neo=[0, ""], div="br", src=[["Finsiders, Feb 2026", FINS], ["Mercado Pago Brazil", BRHOME]]),
            P("mxlic", "Mexico licences and bank application", "Run by MP Agregador, with credit from Mercado Lending; regulated by the CNBV, Banxico and Condusef. Applying to be a multiple-banking institution since 2024, about halfway through the process in September 2026, with payroll accounts as the target.",
              s=["cons", "sme"], st="flux", neo=[0, ""], div="mx",
              mc="A bank licence brings payroll and deposit accounts, and a new debit programme to place.",
              src=[["Mercado Pago Mexico: account", MXCUENTA], ["descubre.vc, Sep 2026", MXSEP], ["descubre.vc, Mar 2026", MXMAR]]),
            P("arlic", "Argentina licences and bank application", "A payment-service provider, not authorised as a financial institution, per its own site in October 2026. It applied for a bank licence in May 2025, and the BCRA's superintendent said on 23 September 2026 that it would have one before the end of the year; one outlet reports it already granted ⚠.",
              s=["cons", "sme"], st="flux", neo=[0, ""], div="ar",
              mc="Salary accounts and deposits would follow, and with them new card programmes.",
              src=[["Bloomberg Línea, Sep 2026", BLAR], ["DolarHoy, Oct 2026", DHAR], ["Mercado Pago Argentina: account", ARCUENTA]]),
            P("cllic", "Chile prepaid-issuer licence", "A prepaid-card issuer, with more than 9 million cards issued and 2.8 million in use; it asked the CMF in 2025 to extend the licence to credit cards.",
              s=["cons"], neo=[0, ""], div="cl", src=[["La Tercera via LatamFintech, Dec 2025", CHILE]]),
        ]},
        {"id": "1.3", "ic": "users-round", "name": "Ownership & leadership", "blurb": "Nasdaq parent, BBB-.", "div": "grp", "rev": "grp", "products": [
            P("owner", "Parent, ratings & leadership", "MercadoLibre, Inc. (NASDAQ: MELI), rated BBB- by S&P, Baa3 by Moody's and BBB- by Fitch, issued $1 billion of 2036 notes in September 2026. Leaders: Executive Chairman Marcos Galperin, CEO Ariel Szarfsztejn (since 1 January 2026), CFO Martín de los Santos and Fintech President Osvaldo Giménez (since 2020; he has run Mercado Pago since 2004).",
              s=["cons"], neo=[0, ""], div="grp", src=[["MELI: about and management", ABOUT], ["MELI: 2036 notes, Sep 2026", BOND], ["Buenos Aires Times", BAT]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "40,000 apps, agents writing code.", "div": "grp", "rev": "grp", "products": [
            P("tech", "In-house platform", "More than 40,000 applications and 20,000 developers on a multi-cloud platform; an in-house AI platform above 99.99% uptime. Human-written code is now 'the exception', and agents have reviewed more than half a million code submissions and migrated about 9,000 services.",
              s=["cons", "sme"], o="B", neo=[0, ""], src=[["MELI IR newsletter, Jun 2026", NLJUN], ["MELI: Q2 2026, Aug 2026", Q2]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy", "blurb": "Latin America's largest digital bank.", "div": "grp", "rev": "grp", "products": [
            P("strategy", "Ecosystem and digital bank", "To be 'the largest digital bank in Latin America', tied to the marketplace: free shipping, the credit card and Meli+ as 'interlocking pieces'. Users active on both sides grew 37% in the second quarter of 2026 and move almost 90% more payment volume than fintech-only users.",
              s=["cons", "seller"], neo=[0, ""], src=[["MELI: Q2 2026, Aug 2026", Q2], ["Bloomberg Línea, Sep 2026", BLAR]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: acquiring at $64 billion a quarter, online checkout, credit cards on Visa in Brazil and Mexico and on Mastercard in Argentina, debit and prepaid cards on Visa in Brazil and on Mastercard elsewhere, Pix, QR and transfers, and crypto.",
    "tiles": [
        {"id": "2.1", "ic": "store", "name": "Acquiring", "blurb": "$64bn a quarter, every network.", "div": "mp", "rev": "acq", "products": [
            P("acquiring", "Merchant acquiring", "Acquiring volume of $64 billion in the second quarter of 2026 (+44% in USD; +42% FX-neutral), with market share up in every market. In Argentina it competes with Fiserv and Prisma's Payway.",
              s=["sme", "ent"], lc="move", neo=[1, "Accepts every network."],
              mc="One of the region's largest acquirers, growing faster than the market.",
              src=[["MELI: Q2 2026, Aug 2026", Q2], ["Letra P, Feb 2026", PRISMA]]),
            P("point", "Point card machines", "Point terminals that take credit, debit, QR and Pix, with 'the same rate for every network' and up to 18 instalments in Brazil; 1.4 million active devices in Mexico, 'equal to all of the country's incumbent banks combined'.",
              s=["sme"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["Mercado Pago: Point", BRPOINT], ["MELI: Q2 2026, Aug 2026", Q2]]),
            P("taptopay", "Point Tap & Tap to Pay", "Phones as card terminals: Point Tap, and Tap to Pay on iPhone in Brazil, launched in Mexico in early 2026.",
              s=["sme"], lc="move", st="new", ay="2026", neo=[1, "Accepts every network."], src=[["Mercado Pago: Tap to Pay on iPhone", BRTAP], ["MELI IR newsletter, Mar 2026", NLMAR]]),
            P("payfac", "Mastercard payment facilitator, Argentina", "In September 2016 Mercado Pago became a Mastercard payment facilitator in Argentina, signing up merchants to accept Mastercard and Maestro on First Data's network. Its current status is not public ⚠.",
              s=["sme"], lc="move", st="unconf", ay="Sep 2016", o="P", at="Mastercard, First Data", div="ar", neo=[2, "A Mastercard programme with First Data."],
              src=[["ITSitio, Sep 2016", ITS2016]]),
        ]},
        {"id": "2.2", "ic": "zap", "name": "Online checkout", "blurb": "Checkout, links, subscriptions.", "div": "mp", "rev": "acq", "products": [
            P("checkout", "Checkout, payment links & subscriptions", "Online checkout for stores, payment links for social media and WhatsApp, subscription plans and developer APIs; the checkout of Mercado Libre's own marketplace.",
              s=["ent", "seller"], lc="move", o="B", neo=[1, "Accepts every network."],
              mc="Tokens and Click to Pay on the region's largest checkout are not public.",
              src=[["Mercado Pago Brazil", BRHOME]]),
        ]},
        {"id": "2.3", "ic": "credit-card", "name": "Credit cards", "blurb": "$7.7bn book, 2.6m cards a quarter.", "div": "credito", "rev": "credit", "products": [
            P("brcc", "Credit card, Brazil (Visa)", "Launched on Visa in March 2021, now Visa Gold with Vai de Visa benefits, up to 18 interest-free instalments, cashback with Meli+ and no annual fee. The card book was $7.7 billion across markets in the second quarter of 2026 (+91%), with 2.6 million cards issued in the quarter.",
              s=["cons"], lc="borrow", ay="Mar 2021", o="P", at="Visa", div="br", neo=[0, "Visa."],
              mc="The largest and fastest-growing card programme, on Visa.",
              src=[["Mercado Pago blog, Mar 2026", BRCCBLOG], ["Money Times, Mar 2021", MT2021], ["MELI: Q2 2026, Aug 2026", Q2]]),
            P("mxcc", "Credit card, Mexico (Visa)", "Launched on Visa in 2023, with 150,000 cards in its first three months and Visa Token Service. Today: up to 24 interest-free months, no annual fee, credit from Mercado Lending.",
              s=["cons"], lc="borrow", ay="2023", o="P", at="Visa", div="mx", neo=[0, "Visa."],
              src=[["Mercado Pago Mexico: credit card", MXCC], ["La República, Jul 2023", LR2023]]),
            P("arcc", "Credit card, Argentina (Mastercard)", "A 'Tarjeta Mastercard' credit card managed in the app, with no maintenance, renewal or delivery charges, rolled out gradually from a waiting list. Launch date not confirmed ⚠.",
              s=["cons"], lc="borrow", o="P", at="Mastercard", div="ar", neo=[2, "Mastercard."],
              src=[["Mercado Pago Argentina: credit card", ARCC], ["La Tercera via LatamFintech, Dec 2025", CHILE]]),
            P("clcc", "Credit card, Chile (planned)", "Planned for 2026 as the fourth credit-card market, subject to the CMF extending the prepaid-issuer licence. Network not stated; launch not confirmed ⚠.",
              s=["cons"], lc="borrow", st="unconf", div="cl", neo=[None, "Network not public."],
              mc="An open network decision.",
              src=[["La Tercera via LatamFintech, Dec 2025", CHILE]]),
        ]},
        {"id": "2.4", "ic": "wallet-cards", "name": "Debit & prepaid cards", "blurb": "Visa in Brazil, Mastercard elsewhere.", "div": "mp", "rev": "svc", "products": [
            P("brdebit", "Debit card, Brazil (Visa)", "The account's debit card 'works like any Visa debit card' (September 2026). Brazil started on Mastercard prepaid in 2018 and was on Visa by 2021 ⚠.",
              s=["cons"], lc="everyday", o="P", at="Visa", div="br", neo=[0, "Visa."],
              src=[["Mercado Pago blog, Sep 2026", BRDEBIT], ["Money Times, Mar 2021", MT2021]]),
            P("mxdebit", "Debit card, Mexico (Mastercard)", "A free 'Debit Mastercard' on the Mercado Pago account, with ATM withdrawals of up to MXN 9,000 a day.",
              s=["cons", "unb"], lc="everyday", o="P", at="Mastercard", div="mx", neo=[2, "Mastercard."],
              src=[["Mercado Pago Mexico", MXHOME], ["Mercado Pago Mexico: account", MXCUENTA]]),
            P("arprepaid", "Prepaid card, Argentina (Mastercard)", "A prepaid card launched with Mastercard in February 2018 for Mercado Libre users without a bank account, in Argentina, Brazil and Mexico; Argentina's card is still Mastercard ⚠.",
              s=["cons", "unb"], lc="everyday", ay="Feb 2018", o="P", at="Mastercard", div="ar", neo=[2, "Mastercard."],
              src=[["BNamericas, Feb 2018", BNA2018], ["Mercado Pago Argentina: prepaid card", ARPREPAID]]),
            P("clprepaid", "Prepaid card, Chile (Mastercard)", "Physical and virtual prepaid cards with Mastercard from November 2022; more than 9 million issued, and about 7 in 10 Chileans with a prepaid card use Mercado Pago's.",
              s=["cons", "unb"], lc="everyday", ay="Nov 2022", o="P", at="Mastercard", div="cl", neo=[2, "Mastercard."],
              src=[["Diario Financiero, Nov 2022", DF2022], ["La Tercera via LatamFintech, Dec 2025", CHILE]]),
        ]},
        {"id": "2.5", "ic": "arrow-left-right", "name": "Pix, QR & transfers", "blurb": "Off the card networks.", "div": "mp", "rev": "svc", "products": [
            P("pix", "Pix (Brazil)", "Free Pix payments and transfers, Pix on Point machines and online, and eight free Pix withdrawals a month.",
              s=["cons", "sme"], lc="move", div="br", neo=[0, "Off the card networks."], src=[["Mercado Pago Brazil: account", BRCONTA]]),
            P("qr", "QR payments (Argentina)", "Argentina's first large QR network and account-to-account payments. In November 2024 it blocked Visa credit payments by Modo users on its QR codes, citing Visa's tokenisation rules, then restored them; the BCRA enforces interoperability.",
              s=["cons", "sme"], lc="move", div="ar", neo=[1, "Cards can fund QR payments."], src=[["Beyond Banking study, Jun 2026", BEYOND], ["DolarHoy, Nov 2024", MODO]]),
            P("spei", "CLABE transfers (Mexico)", "Free SPEI transfers to and from a CLABE account number.",
              s=["cons"], lc="move", div="mx", neo=[0, "Off the card networks."], src=[["Mercado Pago Mexico: account", MXCUENTA]]),
        ]},
        {"id": "2.6", "ic": "coins", "name": "Crypto", "blurb": "Meli Dólar, via Paxos.", "div": "br", "rev": "svc", "products": [
            P("crypto", "Crypto & Meli Dólar", "More than 15 cryptoassets in Brazil, including Bitcoin and Mercado Libre's own dollar stablecoin, Meli Dólar, at a 0.2% fee; Paxos executes and holds them.",
              s=["invest"], lc="grow", o="P", at="Paxos", neo=[0, "Off the card networks."], src=[["Mercado Pago: crypto", BRCRYPTO]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every payment: a credit book of more than $16 billion and its underwriting, tokens and authentication, security, AI assistants, Meli+ loyalty, and savings and investments.",
    "tiles": [
        {"id": "3.1", "ic": "gauge", "name": "Credit & underwriting", "blurb": "$16bn+, 7.0% NPL.", "div": "credito", "rev": "credit", "products": [
            P("credit", "Credit book", "More than $16 billion in the second quarter of 2026 (+75%), with the card book $7.7 billion; the 15–90-day NPL ratio was 4.6% for cards and 7.0% overall, near historic lows after a shift upmarket. At the end of 2025 the mix was about 45% cards, 36% consumer, 16% merchant ⚠.",
              s=["cons", "sme"], lc="borrow", o="B", neo=[1, "Card loans partly on Mastercard."],
              src=[["MELI: Q2 2026, Aug 2026", Q2], ["MELI: FY2025, Feb 2026", FY25BW]]),
            P("bnpl", "Credit without a card", "Instalment credit without a card ('Linha de crédito' in Brazil, 'Meses sin Tarjeta' in Mexico) and personal loans; in Mexico, 40% of personal-loan users in 2025 had never had credit before.",
              s=["cons", "unb"], lc="borrow", o="B", neo=[0, "Off the card networks."],
              src=[["Mercado Pago Brazil: account", BRCONTA], ["Mercado Pago Mexico: account", MXCUENTA], ["descubre.vc, Sep 2026", MXSEP]]),
        ]},
        {"id": "3.2", "ic": "fingerprint", "name": "Tokens & authentication", "blurb": "Visa tokens; Mastercard from 2019 ⚠.", "div": "mp", "rev": "svc", "products": [
            P("tokens", "Tokens & biometrics", "Visa Token Service on the Mexican credit card (2023). Mastercard agreed to supply user authentication and to bring biometrics and tokenisation from 2019 ⚠.",
              s=["cons"], lc="open", neo=[1, "Visa on the Mexican credit card; Mastercard earlier ⚠."],
              mc="Mastercard tokens and Click to Pay on the Mastercard programmes are not public.",
              src=[["La República, Jul 2023", LR2023], ["IProUP", IPROUP]]),
        ]},
        {"id": "3.3", "ic": "shield-check", "name": "Security & insurance", "blurb": "Phone theft, R$4.99 cover.", "div": "br", "rev": "svc", "products": [
            P("security", "Account security & insurance", "Help for stolen phones and hijacked accounts, and insurance from R$4.99 a month; 61% of Brazilians surveyed avoid finance apps or add security away from home. Fraud models are its own; no Mastercard fraud tools are public.",
              s=["cons"], lc="everyday", o="B", neo=[0, "Its own models."],
              mc="Account takeover and phone theft are where identity and fraud services fit.",
              src=[["Finsiders, Feb 2026", FINS], ["Mercado Pago Brazil", BRHOME]]),
        ]},
        {"id": "3.4", "ic": "bot", "name": "AI assistants", "blurb": "9m conversations a quarter.", "div": "mp", "rev": "svc", "products": [
            P("assistant", "AI assistant & Mago", "An AI assistant launched in October 2025 handled more than 9 million conversations in the fourth quarter, 87% without a person; 'Mago' manages money in the Brazilian app, and the internal Maxwell platform runs support agents.",
              s=["cons", "sme"], lc="everyday", st="new", ay="Oct 2025", o="B", neo=[0, ""],
              src=[["Mexico Business News, Feb 2026", FY25], ["MELI IR newsletter, Jun 2026", NLJUN]]),
        ]},
        {"id": "3.5", "ic": "gift", "name": "Loyalty", "blurb": "Meli+ cashback; Vai de Visa.", "div": "grp", "rev": "svc", "products": [
            P("meliplus", "Meli+", "Mercado Libre's subscription: cashback on the Mercado Pago credit card and higher yields on savings; the Meli+ Mega plan reached Mexico from MXN 249 a month.",
              s=["cons"], lc="grow", neo=[0, ""],
              mc="Card-linked offers for Mastercard cardholders in Mexico and Argentina are not public.",
              src=[["MELI IR newsletter, Mar 2026", NLMAR], ["Mercado Pago Brazil: credit card", BRCC]]),
            P("vaidevisa", "Vai de Visa benefits", "Discounts on cinemas, restaurants, shops and travel through Visa's programme on the Brazilian card.",
              s=["cons"], lc="grow", o="P", at="Visa", div="br", neo=[0, "Visa."], src=[["Mercado Pago blog, Mar 2026", BRCCBLOG]]),
        ]},
        {"id": "3.6", "ic": "trending-up", "name": "Savings & investment", "blurb": "$23bn under management.", "div": "mp", "rev": "svc", "products": [
            P("savings", "Savings & investments", "$23 billion under management (+68%). Brazil: Cofrinhos savings pots paying up to 140% of CDI. Mexico: up to 12% a year through GBM's fund. Argentina: Mercado Fondo, with more than 20 million accounts by 2024, over half of adults. Chile: 2.2 million investors with Banco BICE.",
              s=["invest", "cons"], lc="grow", neo=[0, "Off the card networks."],
              src=[["MELI: Q2 2026, Aug 2026", Q2], ["Beyond Banking study, Jun 2026", BEYOND], ["Mercado Pago Mexico: account", MXCUENTA], ["La Tercera via LatamFintech, Dec 2025", CHILE]]),
            P("insurance", "Insurance", "Phone, purchase and personal insurance sold in the app.",
              s=["cons"], lc="beyond", neo=[0, ""], src=[["Mercado Pago Brazil", BRHOME]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "Who buys: consumers with a free digital account, small merchants who take payments and borrow, sellers on Mercado Libre, and people who receive their pay or social benefits into Mercado Pago.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Consumers", "blurb": "A free digital account.", "div": "mp", "rev": "svc", "products": [
            P("account", "Digital account", "A free account with a card, transfers, bill payments, top-ups and transport cards, and savings and credit on top; 88 million monthly active users.",
              s=["cons"], lc="everyday", neo=[1, "Mastercard in Mexico and Argentina; Visa in Brazil."],
              src=[["Mercado Pago Brazil: account", BRCONTA], ["Mercado Pago Mexico: account", MXCUENTA], ["MELI: Q2 2026, Aug 2026", Q2]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "Merchants & SMEs", "blurb": "Accept, borrow, manage.", "div": "mp", "rev": "acq", "products": [
            P("merchants", "Business account", "Card machines, payment links, Pix and Tap to Pay, with business loans and a card whose limit grows with use; in Mexico, 80% of business credit in 2025 went to SMEs.",
              s=["sme"], lc="everyday", neo=[1, "Accepts every network."],
              src=[["Mercado Pago Brazil", BRHOME], ["descubre.vc, Sep 2026", MXSEP]]),
        ]},
        {"id": "4.3", "ic": "users-round", "name": "Marketplace", "blurb": "Paying for Mercado Libre.", "div": "grp", "rev": "acq", "products": [
            P("marketplace", "Marketplace payments", "The checkout and seller account for Mercado Libre: users active on both generate 70% more GMV than marketplace-only users, and the card offers up to 18 or 24 interest-free months on Mercado Libre.",
              s=["seller", "cons"], lc="move", neo=[1, "Every network accepted."],
              src=[["MELI: Q2 2026, Aug 2026", Q2], ["Mercado Pago Mexico: credit card", MXCC]]),
        ]},
        {"id": "4.4", "ic": "hand-coins", "name": "Salaries & benefits", "blurb": "Payroll and social transfers.", "div": "mp", "rev": "svc", "products": [
            P("benefits", "Social benefits", "About 1.8 million Argentine benefit recipients, 14.1% of the total, have chosen Mercado Pago to receive their transfers.",
              s=["unb"], lc="open", div="ar", neo=[0, ""], src=[["Beyond Banking study, Jun 2026", BEYOND]]),
            P("payroll", "Salary portability", "Brazilians can bring their salary to unlock the credit card and Meli+; payroll accounts are the main aim of the Mexican bank licence.",
              s=["cons"], lc="open", st="new", neo=[0, ""],
              mc="Payroll accounts mean debit cards and open-finance identity.",
              src=[["Mercado Pago Brazil", BRHOME], ["descubre.vc, Sep 2026", MXSEP]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How people reach Mercado Pago: the app in 18 countries, Point resellers and the Mercado Libre programmes, and developers and partners from GBM to Paxos.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "App", "blurb": "One app, 18 countries.", "div": "mp", "rev": "grp", "products": [
            P("app", "Mercado Pago app", "The account, cards, credit, savings and the assistant in one app, across Brazil, Mexico, Argentina, Chile, Colombia and the rest of Mercado Libre's 18 countries.",
              s=["cons", "sme"], lc="open", o="B", neo=[0, ""], src=[["MELI: Q2 2026, Aug 2026", Q2], ["Mercado Pago Brazil", BRHOME]]),
        ]},
        {"id": "5.2", "ic": "store", "name": "Resellers", "blurb": "Point resellers.", "div": "br", "rev": "acq", "products": [
            P("resellers", "Point resellers & Mercado Livre Negócios", "Independent resellers of Point machines and a programme for Mercado Livre business sellers.",
              s=["sme"], lc="open", neo=[0, ""], src=[["Mercado Pago Brazil", BRHOME]]),
        ]},
        {"id": "5.3", "ic": "plug", "name": "Developers & partners", "blurb": "APIs; GBM, BICE, Paxos.", "div": "mp", "rev": "grp", "products": [
            P("developers", "Developers & partner programme", "Payment APIs and a partner programme for integrators and platforms.",
              s=["ent"], lc="open", neo=[0, ""], src=[["Mercado Pago Brazil", BRHOME]]),
            P("partners", "Financial partners", "GBM runs the Mexican investment fund, Banco BICE the Chilean one, Banco Industrial is depositary for Mercado Fondo, and Paxos handles crypto.",
              s=["invest"], lc="grow", o="P", at="GBM, Banco BICE, Paxos", neo=[0, ""],
              src=[["Mercado Pago Mexico: account", MXCUENTA], ["Mercado Pago Argentina: account", ARCUENTA], ["Mercado Pago: crypto", BRCRYPTO]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Mercado Pago", "blurb": "Debit in Mexico, cards in Argentina.", "products": [
        P("mcatmp", "Mastercard at Mercado Pago", "Mastercard runs the Mexican debit card, the Argentine credit and prepaid cards and the Chilean prepaid card, and goes back to a 2016 payment-facilitator deal and the 2018 prepaid launch in three countries. Visa holds the Brazilian debit and credit cards and the Mexican credit card, the largest and fastest-growing programmes.",
          s=["cons"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Mercado Pago Mexico", MXHOME], ["Mercado Pago Argentina: credit card", ARCC], ["Mercado Pago blog, Sep 2026", BRDEBIT]]),
    ]},
    {"id": "pillar-market", "name": "Latin American fintech", "blurb": "Pix, Visa, Nubank, licences.", "products": [
        P("market", "The market", "Pix, SPEI and interoperable QR take payments off the cards; Visa agreed to buy Argentina's Prisma and Newpay (February 2026); Nubank, Revolut and Ualá chase bank licences; Brazil restricts 'bank' to licensed banks (November 2025).",
          s=["cons"], div="grp", rev="grp", src=[["Letra P, Feb 2026", PRISMA], ["Finsiders, Feb 2026", FINS]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
