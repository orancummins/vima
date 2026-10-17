"""Banco República (BROU)'s layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the Financial Synthesis for June 2026 and December 2025,
the 2024 Annual Report and the card and service pages on brou.com.uy. Amounts are in US dollars, as BROU reports
them. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on
Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

SF26 = "https://www.brou.com.uy/documents/20182/459463/Web%2BSintesis%2BFinanciera%2BJunio%2B2026%2BIngles.pdf/6421c715-a0ee-4c5a-9265-53d546dcb0d7"
SF25 = "https://www.brou.com.uy/documents/20182/422537/Web%2BSintesis%2BFinanciera%2BDiciembre%2B2025%2BIngles.pdf/f3577ab1-1342-4ae4-860e-5e21c3944a54"
AR24 = "https://www.brou.com.uy/documents/20182/378974/memoria-2024-ing.pdf/d22805c4-c95f-455b-9f78-d4018cdd228b"
MOODYS = "https://www.brou.com.uy/documents/20182/30431/BROU_Calificacion_Moodys_Dic_2025_global.pdf/ef2f22b7-b95f-42a3-90ef-d94f2b47de8c"
STAFF = "https://www.brou.com.uy/documents/d/guest/personal-superior-editable-pdf"
INST = "https://www.brou.com.uy/web-institucional"
GROUP = "https://www.brou.com.uy/institucional/grupo-banco-republica"
PRES = "https://www.gub.uy/presidencia/politicas-y-gestion/se-comunica-designacion-presidente-directorio-del-banco-republica-oriental-del"
CARVE = "https://radiocarve.uy/brou-cerro-2025-con-ganancias-por-475-millones-de-dolares-y-busca-ampliar-el-credito/"
MC19 = "https://www.brou.com.uy/institucional/noticias/brou-y-mastercard-potenciaran-su-oferta-de-medios-de-pago"
MAESTRO = "https://www.brou.com.uy/web/guest/personas/tarjetas/redbrou-maestro"
BLOOM = "https://www.bloomberglinea.com/latinoamerica/uruguay/que-hacer-si-tenes-una-tarjeta-maestro-del-brou-que-dejara-de-funcionar-en-noviembre/"
MCDEB = "https://www.brou.com.uy/web/guest/personas/tarjetas/debito-mastercard/brou-mastercard-debito"
RECDEB = "https://www.brou.com.uy/web/guest/personas/tarjetas/debito-mastercard/brou-recompensa-mastercard-debito"
VISADEB = "https://www.brou.com.uy/web/guest/personas/tarjetas/redbrou-visa/visa-institucional"
MIBROU = "https://www.brou.com.uy/web/guest/personas/tarjetas/redbrou-visa/mi-brou"
RECCRED = "https://www.brou.com.uy/web/guest/personas/tarjetas/mastercard/brou-recompensa"
MCPROD = "https://www.brou.com.uy/web/guest/personas/tarjetas/master/productos"
MCBLACK = "https://www.brou.com.uy/web/guest/personas/tarjetas/mastercard-black"
VISAPROD = "https://www.brou.com.uy/web/guest/personas/tarjetas/visa/productos"
VISAPLAT = "https://www.brou.com.uy/web/guest/personas/tarjetas/visa-platinum"
VISAINF = "https://www.brou.com.uy/web/guest/personas/tarjetas/visa/tarjeta-brou-visa-infinite-credito"
ALFA = "https://www.brou.com.uy/web/guest/personas/tarjetas/prepaga-alfabrou"
GPAY = "https://www.brou.com.uy/personas/tarjetas/google-pay"
BAM = "https://www.brou.com.uy/personas/app-ebrou/app-movil/brou-a-mano"
BAMCOM = "https://www.brou.com.uy/clientes-empresa/empresas/servicios/bam-comercios"
SPI = "https://www.brou.com.uy/personas/servicios/spi"
ALIAS = "https://www.brou.com.uy/personas/servicios-ebrou/transferencias-a-celulares"
TUAPP = "https://www.brou.com.uy/personas/servicios/billeteras-electronicas/tuapp"
NOTIF = "https://www.brou.com.uy/personas/tarjetas/notificacion-de-transacciones"
RECPROG = "https://www.brou.com.uy/personas/recompensa/programa-brou-recompensa"
TIT = "https://www.brou.com.uy/personas/tarjetas/tit"
PYME = "https://www.elobservador.com.uy/cafe-y-negocios/brou-lanza-una-nueva-tarjeta-credito-pymes-como-solicitarla-y-cuales-son-sus-principales-beneficios-n6046937"
PYMECARD = "https://www.brou.com.uy/clientes-empresa/pyme-y-profesionales/emprendedor/tarjeta-de-credito-brou-pyme-mastercard"
EMPCARDS = "https://www.brou.com.uy/clientes-empresa/empresas/tarjetas/tarjeta-de-credito"
BCU26 = "https://www.montevideo.com.uy/Noticias/BCU-presento-su-hoja-de-ruta-para-el-sistema-de-pagos-2026-2030-cuales-son-los-cambios-uc956879"
AMBITO = "https://www.ambito.com/uruguay/las-transferencias-instantaneas-baten-record-mientras-el-efectivo-y-los-cheques-pierden-terreno-n6260972"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "state ownership · balance sheet · 130 years", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Uruguay's state bank since 1896, with 41% of the system's assets and 45% of its deposits, USD 475 million of profit in 2025, a Moody's Baa1 rating, and its own card processor, Sistarbanc.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "41% of system assets.", "div": "brou", "rev": "central", "products": [
            P("balance", "Balance sheet & earnings", "Assets of USD 25.9 billion, 41% of Uruguay's financial system, and USD 22.2 billion of non-financial deposits (a 45% share) at 30 June 2026. Net income was USD 375 million in the half and USD 475 million in 2025 (USD 774 million in 2024), with ROE of 22.4% in H1 2026. Moody's rates deposits Baa1/P-2 and raised the standalone assessment to baa1 in April 2026.",
              s=["con"], neo=[0, ""], src=[["BROU: Financial Synthesis, Jun 2026", SF26], ["BROU: Financial Synthesis, Dec 2025", SF25], ["Moody's rating report, Apr 2026", MOODYS]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "García and Espino.", "div": "brou", "rev": "central", "products": [
            P("leadership", "Board & management", "A five-member board named by the executive: President Álvaro García (from March 2025, a former economy minister), Vice-Presidents Adriana Rodríguez and Leandro Francolino, Directors Ignacio Fessler and Elbio Fernández. General Manager Mariela Espino; Diego Neira runs Digital Banking, Gustavo Galli retail and Juan Llosa cards and digital business.",
              s=["corp"], neo=[0, ""], src=[["BROU: senior staff, Sep 2026", STAFF], ["Presidencia: García named, Mar 2025", PRES]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & ownership", "blurb": "Banco País since 1896.", "div": "brou", "rev": "central", "products": [
            P("heritage", "State ownership & group", "Founded in 1896 and wholly owned by the Uruguayan state, a commercial and development bank in one, supervised by the central bank. It owns República AFISA and República Microfinanzas outright, 51% of República AFAP and about 64% of Sistarbanc.",
              s=["con"], o="I", neo=[0, ""], src=[["BROU: the bank", INST], ["BROU: group companies", GROUP], ["BROU: 2024 Annual Report", AR24]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & processing", "blurb": "Sistarbanc runs the cards.", "div": "sistarbanc", "rev": "central", "products": [
            P("tech", "Digital platform & security", "eBROU upgraded, 100% digital onboarding, a digital key, an online anti-fraud module and AI-based threat-intelligence tools (2024), and a data-analytics executive area.",
              s=["corp"], neo=[0, ""], src=[["BROU: 2024 Annual Report", AR24], ["BROU: senior staff, Sep 2026", STAFF]]),
            P("sistarbanc", "Sistarbanc", "A card processor set up in 1981 and about 64% BROU-owned, processing Visa and Mastercard cards, the state's social-plan cards and the electronic payment system. In 2024 it built the Maestro-to-Mastercard Debit migration and Apple Pay and Google Pay support, and earned about USD 2.8 million.",
              s=["corp"], o="I", neo=[0, "Processes both networks."], src=[["BROU: 2024 Annual Report", AR24]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy", "blurb": "Credit, cards, digital.", "div": "brou", "rev": "central", "products": [
            P("strategy", "Banco País strategy", "Grow credit, keep the credit-card position won back through BROU Recompensa, replace Maestro, push instant payments and wallets, and serve SMEs better. The Strategic Plan itself is not public ⚠.",
              s=["corp"], neo=[0, ""], src=[["BROU: 2024 Annual Report", AR24], ["Radio Carve: García, Jul 2026", CARVE]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: 1.78 million debit cards moving from Maestro to Debit Mastercard by 1 November 2026 beside Visa debit, credit cards on both networks led by BROU Recompensa Mastercard, AlfaBROU prepaid, the BROU a Mano wallet and Google Pay, phone-as-POS acceptance, instant SPI transfers and Toke QR, and tuapp for social programmes.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "Maestro off on 1 November.", "div": "brou", "rev": "personas", "products": [
            P("mcdebit", "BROU Mastercard Débito", "Chip-and-contactless debit replacing RedBROU Maestro, launched publicly in 2024 with online application in eBROU. It works for Uruguayan e-commerce and seven foreign sites (Uber, Netflix, Spotify, HBO Max, Disney+, Booking, Airbnb). By December 2024 it made up 60% of debit purchases.", short="Debit Mastercard",
              s=["con", "social"], lc="everyday", st="new", ay="2024", o="P", at="Mastercard", neo=[2, "Debit Mastercard."],
              mc="The mass-market debit base of Uruguay's largest bank lands on Debit Mastercard.",
              src=[["BROU: Mastercard Débito", MCDEB], ["BROU: 2024 Annual Report", AR24]]),
            P("recdebit", "BROU Recompensa Mastercard Débito", "Debit card inside the Recompensa points programme, with travel assistance and a 2% fee on purchases abroad.",
              s=["con"], lc="everyday", o="P", at="Mastercard", neo=[2, "Debit Mastercard."], src=[["BROU: Recompensa Mastercard Débito", RECDEB]]),
            P("maestro", "RedBROU Maestro", "The legacy magnetic-stripe card, which BROU calls the most widely used debit card in Uruguay. It stops working for residents on 1 November 2026; the migration had reached more than 50% of customers by December 2024.", short="Maestro (switching off)",
              s=["con"], lc="everyday", st="flux", ay="1 Nov 2026", o="I", at="Mastercard", neo=[2, "Maestro, a Mastercard brand."],
              src=[["BROU: RedBROU Maestro", MAESTRO], ["Bloomberg Línea: Maestro ends, Sep 2026", BLOOM]]),
            P("visadebit", "Visa Débito & MI BROU", "Chip-and-contactless Visa debit with travel insurance, sold also by WhatsApp, and MI BROU, a Visa debit card for young people under an agreement with INJU and MIDES.",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["BROU: Visa Débito", VISADEB], ["BROU: MI BROU", MIBROU]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Recompensa on Mastercard.", "div": "recompensa", "rev": "personas", "products": [
            P("reccredit", "BROU Recompensa Mastercard Crédito", "The flagship card from the December 2019 Mastercard agreement, launched in 2020: one point per UYU 100, 10% off at supermarkets and pharmacies, 5% at ANCAP fuel, and no fee in the first year. The Recompensa portfolio grew 6% in 2024.", short="Recompensa (Mastercard)",
              s=["con"], lc="borrow", ay="2020", o="P", at="Mastercard", neo=[2, "Mastercard credit."],
              mc="The card BROU credits with winning back credit-card leadership.",
              src=[["BROU: Recompensa Mastercard Crédito", RECCRED], ["BROU and Mastercard agreement, Dec 2019", MC19], ["BROU: 2024 Annual Report", AR24]]),
            P("mccredit", "Mastercard Internacional, Oro, Platinum & Black", "Mastercard credit tiers; Black carries Mastercard Airport Experiences lounge access.",
              s=["con"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["BROU: Mastercard products", MCPROD], ["BROU: Mastercard Black", MCBLACK]]),
            P("visacredit", "Visa Internacional, Oro, Platinum & Infinite", "Visa credit tiers: Platinum earns ANCAPuntos for fuel and has Priority Pass from August 2025, and BROU Recompensa Visa Infinite now sits at the top of the range.", short="Visa credit",
              s=["con"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."],
              mc="Visa holds BROU's top-tier card, even inside Recompensa.",
              src=[["BROU: Visa products", VISAPROD], ["BROU: Visa Platinum", VISAPLAT], ["BROU: Recompensa Visa Infinite", VISAINF]]),
        ]},
        {"id": "2.3", "ic": "wallet", "name": "Prepaid", "blurb": "AlfaBROU.", "div": "brou", "rev": "personas", "products": [
            P("alfabrou", "Prepaga AlfaBROU", "An international prepaid card for travel and online shopping, controlled in eBROU, with a two-point VAT reduction on local purchases. Prepaid cards are listed under both Visa and Mastercard ⚠.",
              s=["con"], lc="everyday", o="B", neo=[1, "Both networks ⚠."], src=[["BROU: AlfaBROU", ALFA], ["BROU: Mastercard products", MCPROD]]),
        ]},
        {"id": "2.4", "ic": "smartphone", "name": "Wallets & tokens", "blurb": "BROU a Mano, Google Pay.", "div": "bam", "rev": "personas", "products": [
            P("bam", "BROU a Mano", "BROU's own wallet in the eBROU app (from February 2025): tap to pay with tokenised credit and prepaid cards on Android, QR payment from the account, parking, top-ups and bills, with biometric checks. Debit cards are not tokenised.",
              s=["con"], lc="move", st="new", ay="Feb 2025", o="B", neo=[1, "Tokenises both networks."],
              mc="Debit tokens and Apple Pay are the missing pieces.",
              src=[["BROU: BROU a Mano", BAM], ["BROU: 2024 Annual Report", AR24]]),
            P("gpay", "Google Pay", "BROU credit and prepaid cards in Google Wallet, for any merchant taking Visa or Mastercard.",
              s=["con"], lc="move", o="P", at="Google", neo=[1, "Both networks."], src=[["BROU: Google Pay", GPAY]]),
            P("applepay", "Apple Pay", "Sistarbanc built Apple Pay support in 2024; whether BROU cardholders can use it is not confirmed ⚠.",
              s=["con"], lc="move", st="unconf", o="P", at="Apple", neo=[None, "Not confirmed."], src=[["BROU: 2024 Annual Report", AR24]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acceptance", "blurb": "The phone as a POS.", "div": "bam", "rev": "corporativa", "products": [
            P("bamcom", "BROU a Mano Comercios", "An Android phone becomes a POS for cards and Toke QR, run with Sistarbanc: no terminal rent, card sales credited in 24 business hours, QR at once, plus payment links. Part of the June 2026 SME package.",
              s=["sme"], lc="move", st="new", o="P", at="Sistarbanc", neo=[1, "Accepts every network."],
              mc="Tap on Phone acceptance for Uruguay's smallest merchants.",
              src=[["BROU: BROU a Mano Comercios", BAMCOM], ["El Observador: Paquete Pyme, Jun 2026", PYME]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Instant payments", "blurb": "SPI 24/7, Toke QR.", "div": "brou", "rev": "personas", "products": [
            P("spi", "SPI instant transfers", "Transfers to other Uruguayan banks 24 hours a day under the central bank's interbank system, free to receive. Uruguay made a record 34 million instant transfers in the second half of 2025, double a year earlier.",
              s=["con", "sme"], lc="move", o="P", at="BCU", neo=[0, "Domestic account-to-account."],
              mc="Account-to-account payments are growing faster than cards.",
              src=[["BROU: SPI", SPI], ["Ámbito: instant transfers record, Mar 2026", AMBITO]]),
            P("alias", "Transfers to mobile numbers", "Send money using a phone number instead of an account number, to BROU or other banks (from late 2023); more than 120,000 users had linked a number by end-2024.",
              s=["con"], lc="move", ay="2023", o="B", neo=[0, ""], src=[["BROU: transfers to mobiles", ALIAS], ["BROU: 2024 Annual Report", AR24]]),
            P("toke", "PCT-Toke QR payments", "Pay in shops by scanning a QR code from the eBROU app, settled straight into the merchant's account (from September 2024). Uptake is low so far: 46,062 sign-ups but 657 payments in 2024.",
              s=["con", "sme"], lc="move", ay="Sep 2024", o="P", at="Sistarbanc", neo=[0, "Domestic QR."], src=[["BROU: 2024 Annual Report", AR24]]),
        ]},
        {"id": "2.7", "ic": "coins", "name": "E-money & social payments", "blurb": "tuapp, social cards.", "div": "brou", "rev": "personas", "products": [
            P("tuapp", "tuapp & Multipagos", "tuapp, a 50% joint venture, is a phone wallet for bills, parking, top-ups and payments at more than 3,000 shops, including TATA supermarkets. With Multipagos and the STM transport wallet it is one of the most-used payment methods in Uruguay.",
              s=["con", "social"], lc="move", o="P", neo=[0, "Own e-money and transfers."], src=[["BROU: tuapp", TUAPP], ["BROU: 2024 Annual Report", AR24]]),
            P("social", "Social-programme cards", "Payment of the AFAM-PE family allowance and the Tarjeta Uruguay Social to more than 100,000 beneficiaries, plus the MIDES gas-canister subsidy through tuapp.",
              s=["social"], lc="beyond", o="P", at="MIDES", neo=[None, "Network not stated."], src=[["BROU: 2024 Annual Report", AR24]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: Mastercard Identity Check and transaction alerts, BROU's own anti-fraud module, the BROU Recompensa points programme and ANCAPuntos, seasonal discounts on both networks, and a new data-analytics area.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & authentication", "blurb": "Identity Check since 2024.", "div": "brou", "rev": "personas", "products": [
            P("idcheck", "Mastercard Identity Check", "Implemented in 2024 to secure e-commerce purchases on BROU's Mastercard cards.",
              s=["con"], lc="everyday", ay="2024", o="P", at="Mastercard", neo=[3, "Mastercard's own."], src=[["BROU: 2024 Annual Report", AR24]]),
            P("notif", "Transaction notifications", "Free alerts in the eBROU inbox for Visa and Mastercard purchases made without a second authentication factor.",
              s=["con"], lc="everyday", o="B", neo=[1, "Both networks."], src=[["BROU: transaction notifications", NOTIF]]),
            P("fraud", "Fraud prevention", "A fraud-prevention unit, an online anti-fraud module (2024), the digital key, warnings on one-time codes and AI threat intelligence. The central bank's 2026–2030 roadmap calls fraud a growing risk.",
              s=["con", "sme"], lc="everyday", o="B", neo=[0, "BROU's own."],
              mc="Scam and fraud scoring for instant transfers is open ground.",
              src=[["BROU: 2024 Annual Report", AR24], ["Montevideo Portal: BCU roadmap, Mar 2026", BCU26]]),
        ]},
        {"id": "3.2", "ic": "gift", "name": "Loyalty & benefits", "blurb": "Recompensa points.", "div": "recompensa", "rev": "personas", "products": [
            P("recompensa", "BROU Recompensa programme", "Points worth one peso each on Recompensa Mastercard credit, debit and prepaid cards, redeemed in eBROU; Recompensa Visa Infinite has joined. BROU credits the programme, with the national football team sponsorship, for regaining credit-card leadership ⚠.", short="Recompensa",
              s=["con"], lc="grow", ay="2020", o="P", at="Mastercard", neo=[1, "Mostly Mastercard; Visa Infinite too."],
              mc="Card-linked offers could extend the programme beyond fixed discounts.",
              src=[["BROU: Recompensa programme", RECPROG], ["BROU: 2024 Annual Report", AR24]]),
            P("ancap", "BROU–ANCAPuntos", "Fuel points with the state oil company ANCAP, offered on Visa and Mastercard cards.",
              s=["con"], lc="grow", o="P", at="ANCAP", neo=[1, "Both networks."], src=[["BROU: Visa Platinum", VISAPLAT]]),
            P("benefits", "Seasonal discounts", "Discounts of up to 30% for summer and winter tourism, back to school and Mother's and Father's months, on Visa debit and credit and on Recompensa Mastercard cards.",
              s=["con"], lc="grow", o="B", neo=[1, "Both networks."], src=[["BROU: 2024 Annual Report", AR24]]),
        ]},
        {"id": "3.3", "ic": "brain", "name": "Data & AI", "blurb": "A data-analytics area.", "div": "brou", "rev": "central", "products": [
            P("data", "Data analytics & AI", "An executive area for data analytics (2026), with AI used so far in security tools. No public generative-AI or customer-assistant programme was found ⚠.",
              s=["corp"], neo=[None, "Nothing public."], src=[["BROU: senior staff, Sep 2026", STAFF], ["BROU: 2024 Annual Report", AR24]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: accounts and consumer loans for 2.1 million depositors, the June 2026 SME package with a Pyme Mastercard, corporate and farm credit of about USD 5 billion, trusts, pensions and microcredit through group companies, and treasury and the New York branch.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Accounts & personal loans", "blurb": "2.1 million depositors.", "div": "brou", "rev": "personas", "products": [
            P("accounts", "Accounts & payroll", "Peso and dollar accounts for 2.14 million deposit customers (June 2026), payroll accounts opened in eBROU, term deposits and payroll saving in the app.",
              s=["con", "saver"], lc="open", o="B", neo=[1, "Comes with Mastercard or Visa debit."], src=[["BROU: Financial Synthesis, Jun 2026", SF26], ["BROU: 2024 Annual Report", AR24]]),
            P("loans", "Consumer & payroll-deduction loans", "Retail loans of USD 3.87 billion at June 2026, including salary-deduction loans through 136 employer agreements (2024) and instant credit for new digital customers.",
              s=["con"], lc="borrow", o="B", neo=[0, ""], src=[["BROU: Financial Synthesis, Jun 2026", SF26], ["BROU: 2024 Annual Report", AR24]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "SMEs & professionals", "blurb": "Paquete Pyme, June 2026.", "div": "brou", "rev": "corporativa", "products": [
            P("pyme", "Paquete Pyme", "A package for micro, small and medium firms launched in June 2026: an account, Mastercard debit, credit card, POS, BROU a Mano Comercios, Crédito Express and training.",
              s=["sme"], lc="open", st="new", ay="Jun 2026", o="B", neo=[1, "Mastercard cards inside."], src=[["El Observador: Paquete Pyme, Jun 2026", PYME]]),
            P("pymecard", "BROU Pyme Mastercard & Pyme Platinum", "Business credit cards with Mastercard Global Service, 5% off ANCAP fuel, 10% at supermarkets and pharmacies, and cyber cover; BROU says it is Uruguay's first Mastercard credit card with SME-only benefits.", short="Pyme Mastercard",
              s=["sme"], lc="borrow", st="new", ay="Jun 2026", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard's newest programme at BROU.",
              src=[["BROU: Pyme Mastercard", PYMECARD], ["El Observador: Paquete Pyme, Jun 2026", PYME]]),
        ]},
        {"id": "4.3", "ic": "factory", "name": "Corporate & agro", "blurb": "About USD 5bn of loans.", "div": "brou", "rev": "corporativa", "products": [
            P("corporate", "Corporate & state lending", "Corporate loans of USD 5.05 billion (June 2026), foreign trade, guarantees, payroll and supplier payments, and finance for roads and local-government projects.",
              s=["corp"], lc="borrow", o="B", neo=[0, ""], src=[["BROU: Financial Synthesis, Jun 2026", SF26], ["BROU: 2024 Annual Report", AR24]]),
            P("agro", "Agribusiness", "Harvest and irrigation credit, a livestock trust, rural auctions and more than USD 150 million of emergency credit to farm SMEs.",
              s=["agro"], lc="borrow", o="B", neo=[0, ""], src=[["BROU: 2024 Annual Report", AR24]]),
            P("corpcards", "Agro & corporate cards", "BROU Agro Visa for farmers, corporate credit cards on Visa or Mastercard, and a named Mastercard corporate debit card.",
              s=["agro", "corp"], lc="everyday", o="P", neo=[1, "Agro on Visa; corporate split."],
              mc="Commercial and virtual cards for the state's own suppliers are untested.",
              src=[["BROU: business credit cards", EMPCARDS], ["BROU: card printing terminals", TIT]]),
        ]},
        {"id": "4.4", "ic": "hand-coins", "name": "Trusts, pensions & microcredit", "blurb": "AFISA, AFAP, Microfinanzas.", "div": "afap", "rev": "central", "products": [
            P("afisa", "República AFISA", "BROU's wholly owned trust company (2003), the market leader in financial trusts for rural electrification, vehicle-revenue collection, public works and wind farms.",
              s=["corp"], lc="grow", o="B", neo=[0, ""], src=[["BROU: group companies", GROUP]]),
            P("afap", "República AFAP", "Uruguay's leading pension-fund manager (1996), 51% BROU with the social-security bank (37%) and the state insurer (12%).",
              s=["saver"], lc="grow", o="B", neo=[0, ""], src=[["BROU: group companies", GROUP]]),
            P("micro", "República Microfinanzas", "Microcredit for small and low-income entrepreneurs, wholly owned since 2008.",
              s=["sme", "social"], lc="borrow", o="B", neo=[0, ""], src=[["BROU: group companies", GROUP]]),
        ]},
        {"id": "4.5", "ic": "globe", "name": "Treasury & international", "blurb": "USD 15.9bn placed.", "div": "ny", "rev": "finanzas", "products": [
            P("treasury", "Treasury & placements", "Financial placements of USD 15.9 billion at June 2026, mostly in foreign currency, and liquid assets above USD 15 billion.",
              s=["corp"], lc="grow", o="B", neo=[0, ""], src=[["BROU: Financial Synthesis, Jun 2026", SF26], ["Radio Carve: García, Jul 2026", CARVE]]),
            P("ny", "New York branch", "One of two foreign branches, managing a portfolio of more than USD 2 billion.",
              s=["corp"], lc="move", o="B", neo=[0, ""], mc="A route for cross-border flows that Mastercard Move could serve.",
              src=[["Radio Carve: García, Jul 2026", CARVE], ["BROU: senior staff, Sep 2026", STAFF]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: the eBROU app for 1.6 million, 129 branches and 8,592 self-service terminals, card-printing kiosks, WhatsApp, and employers and social programmes.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "eBROU app", "blurb": "1.6 million users.", "div": "brou", "rev": "personas", "products": [
            P("app", "eBROU & App eBROU", "1.61 million e-banking customers at June 2026 (1.43 million at end-2024), with BROU a Mano, transfers, card requests and PIN changes inside the app.",
              s=["con", "sme"], lc="everyday", o="B", neo=[0, ""], src=[["BROU: Financial Synthesis, Jun 2026", SF26]]),
            P("onboard", "Digital onboarding", "Become a customer from the app with a chip ID card, get a peso account, debit card and digital key; 34,000 joined this way in 2024.",
              s=["con"], lc="open", o="B", neo=[0, ""], src=[["BROU: 2024 Annual Report", AR24]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "129 branches.", "div": "brou", "rev": "personas", "products": [
            P("branches", "Branches, ATMs & correspondents", "129 branches and two abroad, 481 ATMs and 7,872 small cash machines and POS (June 2026), and 1,447 financial correspondents in 337 places (2024).",
              s=["con", "agro", "social"], lc="everyday", o="B", neo=[0, ""], src=[["BROU: Financial Synthesis, Jun 2026", SF26], ["BROU: 2024 Annual Report", AR24]]),
            P("tit", "Card-printing terminals", "Self-service and staffed printers in branches that issue Mastercard and Visa debit cards on the spot, 48 hours after the request.",
              s=["con"], lc="open", o="B", neo=[1, "Prints both networks."], src=[["BROU: card printing terminals", TIT]]),
        ]},
        {"id": "5.3", "ic": "headset", "name": "WhatsApp & assistance", "blurb": "1.8m messages a year.", "div": "brou", "rev": "personas", "products": [
            P("whatsapp", "WhatsApp, calls & help site", "1.79 million WhatsApp messages with staff or a bot, 405,000 calls and 557,000 emails in 2024; card applications and account opening by WhatsApp.",
              s=["con", "sme"], lc="open", o="B", neo=[0, ""], src=[["BROU: 2024 Annual Report", AR24]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Employers & programmes", "blurb": "Payroll and social plans.", "div": "brou", "rev": "corporativa", "products": [
            P("partners", "Employers, ministries & merchants", "Payroll and salary-deduction agreements with employers, social programmes with MIDES and INJU, and merchant partners such as ANCAP and TATA.",
              s=["corp", "social"], lc="open", o="P", neo=[0, ""], src=[["BROU: 2024 Annual Report", AR24], ["BROU: tuapp", TUAPP]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at BROU", "blurb": "Debit and Recompensa on Mastercard.", "products": [
        P("mcatbrou", "Mastercard at BROU", "Mastercard has carried BROU's mass debit base for years, first on Maestro and now on Debit Mastercard, which takes over fully when Maestro switches off on 1 November 2026. A December 2019 agreement renewed the alliance and produced BROU Recompensa, the flagship credit card. Identity Check (2024) and the Pyme Mastercard (June 2026) followed. Visa keeps a real second place: Visa debit, the top-tier Visa Infinite, ANCAPuntos Platinum, agro cards and part of corporate.",
          s=["con"], div="brou", rev="central", mc="The relationship this map is drawn for.",
          src=[["BROU and Mastercard agreement, Dec 2019", MC19], ["BROU: 2024 Annual Report", AR24], ["Bloomberg Línea: Maestro ends, Sep 2026", BLOOM]]),
    ]},
    {"id": "pillar-market", "name": "Uruguayan banking", "blurb": "Transfers, open finance, one state bank.", "products": [
        P("market", "The Uruguayan market", "Ten commercial banks, with BROU holding 41% of assets and 45% of deposits. Instant transfers set a record of 34 million in the second half of 2025 and carried 88% of retail payment value against 4% for cards, although cards still lead by count. The central bank's 2026–2030 roadmap adds open finance, more interoperability and local-currency cross-border payments.",
          s=["con"], div="brou", rev="central",
          src=[["BROU: Financial Synthesis, Jun 2026", SF26], ["Ámbito: instant transfers record, Mar 2026", AMBITO], ["Montevideo Portal: BCU roadmap, Mar 2026", BCU26]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
