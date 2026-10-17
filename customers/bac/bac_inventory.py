"""BAC's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are BAC's own unless a source says otherwise: the IIQ 2026 corporate presentation (results to
30 June 2026, published September 2026) and BAC's country websites for Costa Rica, Panama, Guatemala,
Honduras, El Salvador and Nicaragua. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's
own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

PRES = "https://www.baccredomatic.com/sites/default/files/2026-09/BAC%20Corporate%20presentation%20IIQ%202026.pdf"
IQ26 = "https://www.baccredomatic.com/sites/default/files/2026-06/PPT%20Resultados%20financieros%20IQ2026_0.pdf"
FITCH = "https://www.baccredomatic.com/sites/default/files/2026-09/BAC%20ALCANZA%20GRADO%20DE%20INVERSION%20CON%20CALIFICACION%20FITCH%20RATINGS_0.pdf"
MBK_PA = "https://www.baccredomatic.com/es-pa/acerca-de-bac/noticia/bac-se-consolida-como-el-segundo-banco-de-panama-tras-integrar-multibank"
MBK_EYN = "https://www.revistaeyn.com/finanzas/bac-culmina-compra-de-multibank-y-refuerza-presencia-en-panama-DD29808029"
MBK_PL = "https://www.prensalibre.com/economia/vida-empresarial/refuerza-su-liderazgo-para-ofrecer-mas-valor-mas-soluciones-y-mas-oportunidades/"
ICBAC = "https://www.baccredomatic.com/sites/default/files/2026-08/IC%20BAC%200626_0.pdf"
OPA = "https://www.larepublica.co/finanzas/banco-de-bogota-acepto-vender-su-25-en-bhi-y-recibiria-alrededor-de-3-1-billones-3504071"
DF = "https://www.larepublica.net/noticia/bac-credomatic-es-el-primer-banco-centroamericano-en-certificarse-digital-first"
UNL = "https://www.tvn-2.com/economia/empresas/publirreportajes/bac-credomatic-lanza-nueva-tarjeta_1_2017981.html"
GPAY = "https://www.revistaeyn.com/empresasymanagement/centroamericanos-integran-tarjetas-de-credito-y-debito-a-la-billetera-digital-de-google-EE20061423"
APAY = "https://delfino.cr/2024/07/bac-impulsa-pagos-electronicos-con-la-integracion-de-apple-pay"
CARDS_CR = "https://www.baccredomatic.com/es-cr/personas/tarjetas"
AMEX_CR = "https://www.baccredomatic.com/es-cr/personas/tarjetas/amex"
AMEXMETAL = "https://www.larepublica.net/noticia/bac-credomatic-y-american-express-lanzan-tarjeta-metalica-en-costa-rica"
WALLET = "https://www.baccredomatic.com/es-cr/personas/landing/billetera-digital"
TASA = "https://www.baccredomatic.com/es-cr/personas/tasa-cero"
CCLICK = "https://www.baccredomatic.com/es-cr/pymes/compra-click"
HIT = "https://www.baccredomatic.com/es-gt/pymes/puntos-de-ventas?nombre=hit&id=281831"
TCD = "https://www.baccredomatic.com/empresas/tesoreria-corporativa-digital"
APP = "https://www.baccredomatic.com/es-cr/personas/nueva-app-movil"
SINPE = "https://www.baccredomatic.com/es-cr/personas/landing/sinpe-movil"
GT = "https://www.baccredomatic.com/es-gt"
PA = "https://www.baccredomatic.com/es-pa"
SV = "https://www.baccredomatic.com/es-sv"
HN = "https://www.baccredomatic.com/es-hn"
NI = "https://www.baccredomatic.com/es-ni"
REMESA = "https://www.baccredomatic.com/es-gt/personas/landing/remesas-bac"
PA_XPRESS = "https://www.baccredomatic.com/es-pa/personas/landing/bac-xpress"
NI_MCDEBIT = "https://www.baccredomatic.com/es-ni/personas/tarjetas/debito/bac-debito-mastercard-internacional/mastercard/debito"
GT_WALMART = "https://www.baccredomatic.com/es-gt/personas/tarjetas/supermercados-y-clubes/walmart-clasica-mastercard/mastercard/clasica"
DISCOVER = "https://investorrelations.discover.com/newsroom/press-releases/press-release-details/2006/Discover-Financial-Services-Partners-With-Credomatic-To-Promote-Merchant-Acceptance-Of-Discover-Network-Cards-In-Central-America/default.aspx"
MEXICO = "https://www.elfinancierocr.com/finanzas/bac-credomatic-vende-cartera-de-tarjetas-de-credito-en-mexico-a-banco-invex/WKNADAGQJNA5LFUHVZDV5HT5GA/story/"
AVAL = "https://accounter.co/noticias/actualidad/titulares/banco-de-bogota-compro-el-bac-por-us1920-millones"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · six markets · owners", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: US$46.9 billion of assets across six Central American banks, investment grade from S&P and Fitch, a payments flow worth 55% of the region's GDP, and Multibank folded into BAC Panamá in June 2026.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "US$46.9bn, ROAE 18%.", "div": "bac", "rev": "central", "products": [
            P("balance", "Balance sheet & earnings", "Assets of US$46.9 billion, gross loans of US$33.2 billion and deposits of US$35.1 billion at 30 June 2026, each up about 20% with Multibank; net income of US$357 million in the half (down 8.2% on a colón FX loss; underlying up 11.6%) and US$789 million in 2025; ROAE 18.0%, total capital 12.5%. Rated BBB- by S&P and Fitch (upgraded to investment grade in September 2026) and Ba1 by Moody's.",
              s=["con"], neo=[0, ""], src=[["BAC IIQ 2026 presentation", PRES], ["BAC: Fitch investment grade, Sep 2026", FITCH]]),
        ]},
        {"id": "1.2", "ic": "earth", "name": "Six markets", "blurb": "No country over 30% of loans.", "div": "bac", "rev": "central", "products": [
            P("mkt_pa", "BAC Panamá", "The largest market since Multibank: US$10.3 billion of loans, US$13.9 billion of assets and US$64 million of net income in H1 2026; second in Panama by loans and third or second by assets ⚠ (sources differ). Mastercard SmartCash, Destiny Black and Unlimited alongside Amex and Visa.",
              s=["con", "corp"], div="pa", rev="corporate", neo=[1, "Mastercard, Visa and Amex."], src=[["BAC IIQ 2026 presentation", PRES], ["BAC Panamá: Multibank merger, Jun 2026", MBK_PA], ["BAC Panamá home page", PA]]),
            P("mkt_cr", "BAC Costa Rica", "US$8.9 billion of loans, US$13.6 billion of assets and US$90 million of net income in H1 2026, the highest fee ratio in the group (45.4%). The card catalogue lists 63 credit products: 27 Amex, 20 Visa and 16 Mastercard.",
              s=["con", "prem"], div="cr", rev="consumer", neo=[1, "Amex leads the catalogue; Mastercard 16 of 63."], src=[["BAC IIQ 2026 presentation", PRES], ["BAC Costa Rica: cards", CARDS_CR]]),
            P("mkt_gt", "BAC Guatemala", "US$5.1 billion of loans, US$7.1 billion of assets and US$63 million of net income in H1 2026 (ROAE 16.7%). Visa and Mastercard debit, the Walmart Clásica Mastercard, Amex Blue and Business, HIT Tap on Phone and Mi Remesa BAC.",
              s=["con", "remit"], div="gt", rev="consumer", neo=[1, "Visa and Mastercard debit; Walmart on Mastercard."], src=[["BAC IIQ 2026 presentation", PRES], ["BAC Guatemala home page", GT]]),
            P("mkt_hn", "BAC Honduras", "US$4.1 billion of loans, US$5.7 billion of assets and US$86 million of net income in H1 2026, with a 9.3% NIM and ROAE of 20.3%; 50 years in Honduras. Mastercard Clásica and Preferente debit, Conecta Mastercard, Visa Millas Plus and Amex.",
              s=["con", "remit"], div="hn", rev="consumer", neo=[1, "Mastercard and Visa debit; Amex premium."], src=[["BAC IIQ 2026 presentation", PRES], ["BAC Honduras home page", HN]]),
            P("mkt_sv", "BAC El Salvador", "US$3.1 billion of loans, US$4.1 billion of assets and US$27 million of net income in H1 2026 in a dollarised economy. Mastercard Clásica debit, Platinum and Walmart Mastercard, Visa Platino and Infinite, and Amex.",
              s=["con", "remit"], div="sv", rev="consumer", neo=[1, "Three networks."], src=[["BAC IIQ 2026 presentation", PRES], ["BAC El Salvador home page", SV]]),
            P("mkt_ni", "BAC Nicaragua", "US$2.0 billion of loans, US$3.0 billion of assets and US$56 million of net income in H1 2026, with the group's best ROAA (4.0%). The most Mastercard-led market: Mastercard Clásica, La Colonia Mastercard and Débito Mastercard Internacional, plus GasCard Visa and Amex.",
              s=["con", "remit"], div="ni", rev="consumer", neo=[1, "Mostly Mastercard among BAC's own cards ⚠."], src=[["BAC IIQ 2026 presentation", PRES], ["BAC Nicaragua home page", NI], ["BAC Nicaragua: Débito Mastercard Internacional", NI_MCDEBIT]]),
        ]},
        {"id": "1.3", "ic": "scale", "name": "Owners, leaders & heritage", "blurb": "Sarmiento family, Tabash.", "div": "bac", "rev": "central", "products": [
            P("owners", "Ownership & listing", "BAC Holding International (Panama), listed in Bogotá and Panama, owns BAC International Bank through BAC International Corp. It was spun off from Grupo Aval and Banco de Bogotá in 2022; Sarmiento Angulo family companies bought Banco de Bogotá's 25% in December 2022 and hold well over 70% ⚠ (current percentages not found).",
              s=["corp"], neo=[0, ""], src=[["BAC IIQ 2026 presentation", PRES], ["La República: Banco de Bogotá sells 25%, Dec 2022", OPA]]),
            P("leadership", "Leadership", "Rodolfo Tabash Espinach is President and CEO; Ramón Chiari Brin runs BAC Panamá; Laura Moreno heads corporate relations. More than 21,000 staff; management tenure averages 17 years. Other executive names not found ⚠.",
              s=["corp"], neo=[0, ""], src=[["BAC: Fitch investment grade, Sep 2026", FITCH], ["BAC Panamá: Multibank merger, Jun 2026", MBK_PA], ["Delfino: Apple Pay, Jul 2024", APAY]]),
            P("heritage", "Heritage", "Banco de América and Credomatic, the card business, grew into a regional group ⚠ (founding dates not verified); Banco de Bogotá bought BAC for about US$1.92 billion (2010 ⚠), and BAC sold its Mexican card book to Banco Invex in December 2016 to focus on Central America.",
              s=["con"], o="I", neo=[0, ""], src=[["Accounter: Banco de Bogotá buys BAC", AVAL], ["El Financiero: Mexico card sale, Dec 2016", MEXICO]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy & deals", "blurb": "Multibank and the payments moat.", "div": "bac", "rev": "central", "products": [
            P("strategy", "Strategy", "'Reimagine banking to generate prosperity': scale across six markets, digital sales (52% of core products sold digitally), the payments ecosystem as low-cost funding and data, a 'triple value' sustainability agenda, and rebuilding capital after the Multibank dividend.",
              s=["corp"], neo=[0, ""], src=[["BAC IIQ 2026 presentation", PRES], ["BAC: Fitch investment grade, Sep 2026", FITCH]]),
            P("multibank", "Multibank", "BAC International Corp. bought 99.57% of Multi Financial Group at US$26.8611 a share on 18 March 2026 (about US$5 billion of assets, 0.1 million clients) and merged Multibank into BAC Panamá on 9 June 2026, lifting Panama to about 31% of group loans and deposits.",
              short="Multibank (2026)", s=["con", "corp"], div="pa", rev="corporate", st="new", ay="Mar 2026", o="A", neo=[None, "Multibank's card networks not found."],
              mc="About 100,000 clients moving onto BAC cards: a reissue window in Panama.",
              src=[["E&N: Multibank purchase, Mar 2026", MBK_EYN], ["BAC Panamá: Multibank merger, Jun 2026", MBK_PA], ["Prensa Libre: Multibank figures, Apr 2026", MBK_PL]]),
            P("ecosystem", "Payments ecosystem", "About US$226 billion of payments ran through BAC in 2025, about 55% of Central American GDP (13.8% a year since 2021), and US$122 billion in H1 2026: supplier payments, acquiring, payroll, Ameritransfer and international ⚠ (split not legible).",
              s=["sme", "corp"], lc="move", neo=[1, "Card flows on every network; transfers BAC's own."],
              mc="BAC calls this flow its barrier to entry: the prize for any network.",
              src=[["BAC IIQ 2026 presentation", PRES]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Nine ways money moves: the region's largest card issuer on Visa, Mastercard and American Express, Tasa Cero instalments, a 54% acquiring share with softPOS and payment links, wallets, SINPE Móvil and ACH transfers, and remittances into the northern markets.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Credit cards", "blurb": "41% issuer share, three networks.", "div": "bac", "rev": "consumer", "products": [
            P("credit", "BAC credit cards", "Central America's largest credit-card issuer, about 41% of issuing volume (+140bps a year to IIQ 2026 ⚠), under long-term agreements with Visa, Mastercard and American Express. Families include CashBack, Gane Premios, Millas Plus, EconoMía and Óptima; Costa Rica lists 20 Visa and 16 Mastercard credit products.",
              short="Credit (Visa, Mastercard, Amex)", s=["con", "prem"], lc="borrow", o="P", at="Visa, Mastercard, American Express", neo=[1, "Split across Visa, Mastercard and Amex."],
              mc="A three-network issuer: share is won product by product.",
              src=[["BAC IIQ 2026 presentation", PRES], ["BAC Costa Rica: cards", CARDS_CR]]),
            P("amex", "American Express cards", "Amex is the largest brand in BAC Costa Rica's catalogue (27 credit products, from Blue to The Platinum Card) and BAC issues Amex in all six markets, including Centurion in Panama and Business Link corporate lines ⚠ (exclusivity not confirmed).",
              s=["prem", "sme"], lc="borrow", o="P", at="American Express", neo=[0, "Amex."], src=[["BAC Costa Rica: Amex cards", AMEX_CR], ["BAC Panamá home page", PA]]),
        ]},
        {"id": "2.2", "ic": "gem", "name": "Premium & co-brands", "blurb": "Black, Infinite, Platinum.", "div": "bac", "rev": "consumer", "products": [
            P("premium", "Premium cards", "Mastercard Black (Millas Plus, CashBack Premium, AAdvantage) and the Unlimited Mastercard launched in Panama in November 2022; Visa Infinite for Millas Plus, ConnectMiles and LifeMiles; and Amex Platinum, a metal Platinum card (Costa Rica ⚠ date) and Centurion.",
              s=["prem"], lc="everyday", ay="Nov 2022", o="P", at="Mastercard, Visa, American Express", neo=[1, "Mastercard Black and Unlimited among three."],
              src=[["TVN: Unlimited Mastercard, Nov 2022", UNL], ["BAC Costa Rica: cards", CARDS_CR], ["La República: Amex metal card", AMEXMETAL]]),
            P("cobrand", "Co-brand cards", "Walmart (Amex in Costa Rica, Mastercard in Guatemala and El Salvador), PriceSmart (mostly Visa), AAdvantage (all three networks), Avianca LifeMiles (Amex and Visa), Copa ConnectMiles, Auto Mercado, La Colonia Mastercard in Nicaragua and Comisariato Los Andes in Honduras.",
              s=["con", "prem"], lc="everyday", o="P", at="Walmart, PriceSmart, American Airlines, Avianca, Copa", neo=[1, "Split by partner and country."],
              src=[["BAC Costa Rica: cards", CARDS_CR], ["BAC Guatemala: Walmart Mastercard", GT_WALMART], ["BAC Nicaragua home page", NI]]),
        ]},
        {"id": "2.3", "ic": "wallet-cards", "name": "Debit", "blurb": "43% debit share ⚠.", "div": "bac", "rev": "consumer", "products": [
            P("debit", "La Roja & BAC debit", "About 43% of debit issuing volume ⚠. La Roja debit on Visa and Mastercard in Costa Rica and Panama, Mastercard Clásica and Preferente in Honduras, Mastercard Clásica in El Salvador, Débito Mastercard Internacional in Nicaragua, and Visa and Mastercard Clásica and Gold in Guatemala.",
              short="Debit (Visa & Mastercard)", s=["con", "remit"], lc="everyday", o="P", at="Visa, Mastercard", neo=[1, "Visa and Mastercard, varying by market."],
              src=[["BAC IIQ 2026 presentation", PRES], ["BAC Costa Rica: cards", CARDS_CR], ["BAC Nicaragua: Débito Mastercard Internacional", NI_MCDEBIT]]),
            P("digitalfirst", "Mastercard Digital First", "In December 2021 BAC became the first financial group in the region certified under Mastercard's Digital First programme, giving Mastercard cardholders immediate digital access and payment; Guatemala now issues a digital credit card from the app.",
              s=["con"], lc="open", ay="Dec 2021", o="P", at="Mastercard", neo=[3, "Mastercard's programme ⚠ current scope."],
              mc="Mastercard's clearest joint programme with BAC.",
              src=[["La República: Digital First, Dec 2021", DF], ["BAC Guatemala home page", GT]]),
        ]},
        {"id": "2.4", "ic": "hand-coins", "name": "Instalments", "blurb": "Tasa Cero to 24 months.", "div": "cr", "rev": "consumer", "products": [
            P("tasacero", "Tasa Cero & Minicuotas", "Interest-free instalments of 3 to 24 months at affiliated merchants on all BAC credit cards in Costa Rica (bar a few business cards), and in Panama (3–18 months for travel), Honduras and Nicaragua; Minicuotas and Extrafinanciamiento sit alongside. BAC runs both the card and the merchant side.",
              s=["con", "sme"], lc="borrow", o="B", neo=[1, "BAC-run on every network's cards."],
              mc="Mastercard Installments would compete with BAC's own scheme.",
              src=[["BAC Costa Rica: Tasa Cero", TASA], ["BAC Panamá home page", PA], ["BAC Honduras home page", HN]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acquiring", "blurb": "54% acquiring share.", "div": "bac", "rev": "corporate", "products": [
            P("acquiring", "Merchant acquiring", "About 54% of Central American acquiring volume (+59bps to IIQ 2026 ⚠); BAC says it is the only company in the region that both acquires and issues across all major brands. POS terminals and MiPOS in all six markets; Discover acceptance since 2006.",
              s=["sme"], lc="move", o="B", neo=[1, "Accepts every network."],
              mc="The region's dominant acquirer: Mastercard acceptance runs through BAC.",
              src=[["BAC IIQ 2026 presentation", PRES], ["Discover and Credomatic, Feb 2006", DISCOVER]]),
            P("hit", "HIT Tap on Phone", "Contactless acceptance on an Android phone with no extra hardware, for Mastercard, Visa, Amex and wallets, with automatic daily closings; offered to small businesses in Guatemala, Panama, El Salvador and Honduras.",
              s=["sme"], lc="move", st="new", o="B", neo=[1, "Accepts every network."], src=[["BAC Guatemala: HIT", HIT], ["BAC Panamá home page", PA]]),
        ]},
        {"id": "2.6", "ic": "receipt-text", "name": "E-commerce", "blurb": "Compra Click links.", "div": "bac", "rev": "corporate", "products": [
            P("compraclick", "Compra Click & e-commerce", "Payment links for businesses selling on WhatsApp and social media (Costa Rica: US$50 set-up, US$25 a month, US$0.11 a transaction), with 3-D Secure for Visa and Mastercard, Tasa Cero and Minicuotas; Pyme Store and an e-commerce gateway sit alongside. Apple Pay was added in July 2024 for Visa and Amex cards.",
              s=["sme"], lc="move", ay="Jul 2024", o="B", neo=[1, "Visa and Mastercard 3-D Secure; Apple Pay launched without Mastercard."],
              mc="Click to Pay and passkeys are open ground at the region's largest acquirer.",
              src=[["BAC Costa Rica: Compra Click", CCLICK], ["Delfino: Apple Pay, Jul 2024", APAY]]),
        ]},
        {"id": "2.7", "ic": "wallet", "name": "Wallets", "blurb": "Apple, Google, Garmin.", "div": "bac", "rev": "consumer", "products": [
            P("wallets", "Digital wallets", "Apple Pay, Google Pay, Garmin and Fitbit for Visa, Mastercard and Amex cards in Costa Rica; Google Wallet came to Visa and Mastercard cards across Central America in June 2024, with Mastercard's country manager Francisco Milian at the launch.",
              s=["con"], lc="everyday", ay="Jun 2024", o="P", at="Apple, Google", neo=[1, "Tokens on all three networks."],
              src=[["BAC Costa Rica: digital wallet", WALLET], ["E&N: Google Wallet, Jun 2024", GPAY]]),
        ]},
        {"id": "2.8", "ic": "zap", "name": "Instant payments", "blurb": "SINPE Móvil, ACH Xpress.", "div": "cr", "rev": "consumer", "products": [
            P("sinpe", "SINPE Móvil", "Costa Rica's central-bank phone-number transfers inside the BAC app: free up to ₡100,000 a day, and usable to pay in Kash up to ₡600,000.",
              s=["con", "sme"], lc="move", o="P", at="Banco Central de Costa Rica", neo=[0, "Central-bank rail."], src=[["BAC Costa Rica: SINPE Móvil", SINPE]]),
            P("xpress", "Xpress, ACH & local transfers", "Xpress and ACH Xpress transfers in Panama, and local ACH transfers in Honduras and Nicaragua, for people and businesses.",
              s=["con", "sme"], div="pa", lc="move", neo=[0, "Local ACH."], src=[["BAC Panamá: Xpress", PA_XPRESS], ["BAC Honduras home page", HN]]),
        ]},
        {"id": "2.9", "ic": "send", "name": "Remittances & cross-border", "blurb": "Mi Remesa, Ameritransfer.", "div": "gt", "rev": "consumer", "products": [
            P("remesa", "Mi Remesa BAC", "Receives money from abroad in Guatemala, Honduras and El Salvador (Remesa Familiar in Nicaragua), the four remittance-dependent markets.",
              s=["remit"], lc="move", neo=[None, "Remittance partners not disclosed."],
              mc="Mastercard Move could add card and wallet payouts ⚠.",
              src=[["BAC Guatemala: Mi Remesa", REMESA], ["BAC Nicaragua home page", NI]]),
            P("ameritransfer", "Ameritransfer & international", "Ameritransfer ⚠ and international wires for businesses in every market; Ameritransfer and international flows are reported lines in BAC's payments volume.",
              s=["sme", "corp"], div="bac", rev="corporate", lc="move", neo=[None, "Rails not disclosed."], src=[["BAC IIQ 2026 presentation", PRES], ["BAC Guatemala home page", GT]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: 3-D Secure and card insurance, a monthly consumer-spending index built from BAC's own transactions, points and miles, and APIs and host-to-host links for corporate treasurers.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "3-D Secure, Orión.", "div": "bac", "rev": "consumer", "products": [
            P("security", "Fraud & security", "3-D Secure on e-commerce for Visa and Mastercard, card theft and fraud insurance (Seguro PRF), BAC Código security device, and the Orión cybersecurity community. BAC's fraud-scoring vendors are not public ⚠.",
              s=["con", "sme"], lc="everyday", neo=[None, "Vendors not public."],
              mc="96% of transactions are digital: room for scam and identity tools.",
              src=[["BAC Costa Rica: Compra Click", CCLICK], ["BAC Nicaragua home page", NI], ["BAC Tesorería Corporativa Digital", TCD]]),
        ]},
        {"id": "3.2", "ic": "chart-column", "name": "Data & insights", "blurb": "Índice de Consumo BAC.", "div": "bac", "rev": "central", "products": [
            P("icbac", "Índice de Consumo BAC", "A monthly consumer-spending index built from real, anonymised transactions in six countries; June 2026 put Honduras at 104.2 and Panama at 96.3, with inbound tourism up 15.5%.",
              s=["corp"], lc="beyond", st="new", o="B", neo=[0, "BAC's own data."],
              mc="Mastercard's spending and merchant data could deepen it.",
              src=[["Índice de Consumo BAC, Jun 2026", ICBAC]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Loyalty", "blurb": "Points, cashback, miles.", "div": "bac", "rev": "consumer", "products": [
            P("loyalty", "Puntos BAC, CashBack & Millas Plus", "Points, cashback (up to 7% on some Honduran cards) and Millas Plus miles, redeemed through BAC's Mi Viaje travel site, plus campaigns such as La Regalona in Nicaragua (September 2026 to January 2027).",
              s=["con", "prem"], lc="grow", o="B", neo=[0, "BAC's own, across networks."],
              mc="Card-linked offers could reach BAC's 6 million clients.",
              src=[["BAC Nicaragua home page", NI], ["BAC Honduras home page", HN], ["BAC Panamá home page", PA]]),
        ]},
        {"id": "3.4", "ic": "code-xml", "name": "APIs & treasury", "blurb": "BAC API, host-to-host.", "div": "bac", "rev": "corporate", "products": [
            P("treasury", "Tesorería Corporativa Digital", "Payments, statements and automatic reconciliation across countries from one point, connected by BAC API, host-to-host links to a company's ERP, or corporate SWIFT (terms dated May 2026).",
              s=["corp"], lc="move", st="new", o="B", neo=[0, ""], src=[["BAC Tesorería Corporativa Digital", TCD]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: consumer accounts and loans (36% of the book), mortgages (16%), corporate and SME banking (49%) for more than 300,000 businesses, and pensions, brokerage and insurance.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Consumer banking", "blurb": "US$11.9bn of consumer loans.", "div": "bac", "rev": "consumer", "products": [
            P("accounts", "Accounts", "Digital accounts opened in the app (71% of accounts are opened end to end digitally), Alcanza savings paying up to 5% in Guatemala, and BAC Objetivos savings goals.",
              s=["con"], lc="open", neo=[1, "Debit on Visa and Mastercard."], src=[["BAC IIQ 2026 presentation", PRES], ["BAC Guatemala home page", GT], ["BAC Costa Rica: new app", APP]]),
            P("loans", "Personal loans", "Consumer loans of about US$11.9 billion including cards; 56% of instant personal loans are digital end to end, and Guatemala's Préstamo fácil pays out within 24 business hours.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["BAC IIQ 2026 presentation", PRES], ["BAC Guatemala home page", GT]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Mortgages", "blurb": "16% of loans.", "div": "bac", "rev": "mortgage", "products": [
            P("mortgages", "Mortgages", "Mortgages are about 16% of BAC's US$33.2 billion loan book at June 2026 ⚠ (amount read from a chart).",
              s=["home"], lc="borrow", neo=[0, ""], src=[["BAC IIQ 2026 presentation", PRES]]),
        ]},
        {"id": "4.3", "ic": "briefcase-business", "name": "Corporate & SME", "blurb": "300,000+ businesses.", "div": "bac", "rev": "corporate", "products": [
            P("corporate", "Corporate banking", "Corporate and commercial lending is about 49% of the book (about US$16 billion), with payroll, supplier payments, manager's cheques and trade; supplier payments are the largest single flow in BAC's payments volume.",
              s=["corp"], lc="borrow", neo=[0, ""],
              mc="Commercial and virtual cards could ride the supplier-payment flow.",
              src=[["BAC IIQ 2026 presentation", PRES], ["BAC Panamá home page", PA]]),
            P("sme", "SME banking", "More than 300,000 businesses served; women-led firms are 36% of the SME portfolio; business cards include Amex Business, LifeMiles Empresarial and Corporate Millas Plus ⚠ (networks vary).",
              s=["sme"], lc="everyday", neo=[None, "Business-card networks not public."], src=[["BAC IIQ 2026 presentation", PRES], ["BAC Guatemala home page", GT], ["BAC Panamá: Multibank merger, Jun 2026", MBK_PA]]),
        ]},
        {"id": "4.4", "ic": "coins", "name": "Pensions & insurance", "blurb": "Funds, brokers, insurance.", "div": "bac", "rev": "central", "products": [
            P("wealth", "Pensions, brokerage & insurance", "Pension funds, brokerages, insurance brokers and a reinsurance captive held under BAC International Bank, and private banking in Costa Rica ⚠.",
              s=["con", "corp"], lc="grow", neo=[0, ""], src=[["BAC IIQ 2026 presentation", PRES]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach BAC: the app for more than 4 million users, branches and ATMs in six countries, Rapibac points, and the airlines, retailers and merchants behind its cards.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "BAC app", "blurb": "4 million digital clients.", "div": "bac", "rev": "consumer", "products": [
            P("app", "BAC app & online banking", "4.1 million digital clients (65% of clients) and 96% of monetary transactions digital; a new app rolling out in Costa Rica in 2026 with privacy mode, quick actions and savings goals, and no AI assistant yet.",
              s=["con", "sme"], lc="everyday", st="new", neo=[0, ""],
              mc="No AI assistant yet: agentic payments are open ground.",
              src=[["BAC IIQ 2026 presentation", PRES], ["BAC Costa Rica: new app", APP]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "Six countries.", "div": "bac", "rev": "consumer", "products": [
            P("branches", "Branches & ATMs", "Branches in every market, now in nine of Panama's ten provinces after Multibank, and ATMs with cardless withdrawal and cash deposit; group totals not found ⚠.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["BAC Panamá: Multibank merger, Jun 2026", MBK_PA]]),
            P("rapibac", "Rapibac", "Rapibac service points in El Salvador, Honduras and Nicaragua ⚠ (described only by name).",
              s=["con", "remit"], div="hn", lc="everyday", neo=[0, ""], src=[["BAC Honduras home page", HN], ["BAC El Salvador home page", SV]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partners", "blurb": "Airlines, retailers.", "div": "bac", "rev": "consumer", "products": [
            P("partners", "Airlines, retailers & merchants", "American Airlines, Avianca and Copa miles cards, Walmart, PriceSmart, La Colonia and Auto Mercado co-brands, and the merchants that take BAC's terminals and links.",
              s=["prem", "sme"], lc="open", o="P", neo=[1, "Co-brands split across networks."], src=[["BAC Costa Rica: cards", CARDS_CR], ["BAC Panamá home page", PA]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at BAC", "blurb": "One of three networks.", "products": [
        P("mcatbac", "Mastercard at BAC", "BAC has long-term agreements with Visa, Mastercard and American Express. Mastercard carries part of its credit and debit in all six markets, most in Nicaragua, plus Black and Unlimited cards, the Walmart co-brand in Guatemala and El Salvador, and the 2021 Digital First certification. Amex leads the Costa Rica catalogue and the premium tier; Visa holds Infinite travel cards and was first on Apple Pay checkout.",
          s=["con"], div="bac", rev="central", mc="The relationship this map is drawn for.",
          src=[["BAC IIQ 2026 presentation", PRES], ["La República: Digital First, Dec 2021", DF]]),
    ]},
    {"id": "pillar-market", "name": "Central American banking", "blurb": "Six markets, one leader.", "products": [
        P("market", "The regional market", "Six economies growing about 3.6% in 2026, with remittance-heavy northern markets, dollarised El Salvador and Panama, Costa Rica's SINPE Móvil, and Panama's capital buffers phasing in to 2032. BAC is number one by assets, loans and deposits.",
          s=["con"], div="bac", rev="central", src=[["BAC IIQ 2026 presentation", PRES], ["BAC Costa Rica: SINPE Móvil", SINPE]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
