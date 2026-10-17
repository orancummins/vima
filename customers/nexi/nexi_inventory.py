"""Nexi Group's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the 1H 2026 results (29 July 2026), the FY2025
results and Capital Markets Day (5 March 2026) and Nexi's press releases. ``neo`` is the Mastercard lens:
[depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

DL = "https://www.nexigroup.com/content/dam/corp/downloads/"
PR = DL + "media/press-release/"
H1 = DL + "investors/financial-press-releases/2026/26-07-29-nexi-1H2026-PR-financial-results.pdf"
CALL = DL + "investors/financial-results/2026/jul-29/1H26%20Results_Transcript.pdf"
FY25 = "https://www.emarketstorage.it/sites/default/files/comunicati/2026-03/20260305_178185.pdf"
CMD = DL + "investors/capital-market-day/2026/2026-03-05-pr-Nexi-Capital-Markets-Day.pdf"
NINEM = DL + "investors/financial-results/2025/11-05/2025-11-05-nexi-9M2025-financial-results-presentation.pdf"
CEO = "https://www.emarketstorage.it/sites/default/files/comunicati/2026-03/20260325_179985.pdf"
CFO = DL + "investors/financial-press-releases/2026/2026-01-23-pr-press-release.pdf"
TPGNO = DL + "investors/financial-press-releases/2025/2025-12-18-pr-nexi.pdf"
CVC = "https://www.electronicpaymentsinternational.com/news/cvc-weighs-e9bn-bid-nexi/"
CDP = "https://www.milanofinanza.it/news/focus-su-nexi-202605250920309943"
BORSA = "https://www.borsaitaliana.it/borsa/azioni/scheda/IT0005366767.html?lang=en"
GROUP = "https://www.nexigroup.com/en/group/"
MGMT = "https://www.nexigroup.com/en/group/governance/management/"
WIKI = "https://en.wikipedia.org/wiki/Nexi"
ARCHIVE = "https://www.nexigroup.com/en/media-relations/press-releases/"
MCOB = "https://www.mastercard.com/news/europe/en/newsroom/press-releases/en/2024/mastercard-and-nexi-team-up-to-advance-open-banking-payments-across-europe/"
MOVE = PR + "2025/2025-10-29-pr-Nexi.pdf"
NETSA2A = "https://investor.mastercard.com/investor-news/investor-news-details/2021/Mastercard-Completes-Acquisition-of-Nets-Account-to-Account-Payment-Business/default.aspx"
AGENTCONNECT = "https://pulse2.com/mastercard-launches-agent-connect-and-expands-agent-suite-for-merchants-to-support-ai-powered-shopping/"
MCP = PR + "2026/2026-03-04-pr-nexi-launches-new-agentic-commerce-capabilities.pdf"
GOOGLE = PR + "2026/2026-03-03-pr-nexi_google.pdf"
REFIBUY = PR + "2026/2026-09-17-pr-Nexi_ReFiBuy-ENG.pdf"
READY = PR + "2026/2026-02-18-pr-nexi-ready.pdf"
VISAREADY = PR + "2026/2026-04-23-pr-nexi-and-visa-enters-partnership-in-germany-final2.pdf"
WERO26 = PR + "2026/2026-04-28-pr-nexi-implements-Wero-for-ecommerce-in-germany.pdf"
WERO25 = PR + "2025/24-02-25-pr-nexi-becomes-wero-acquirer.pdf"
STATION = PR + "2026/2026-02-11-pr-nexi-group-smart-station.pdf"
DEURO = PR + "2026/2026-07-14-pr-DigitalEuro-Nexi-ENG.pdf"
YOUNITED = PR + "2026/2026-06-18-pr-Nexi-Younited.pdf"
ZIPPAY = PR + "2026/2026-03-09-pr-nexi-bpfi.pdf"
PAYPAL = PR + "2026/2026-03-31-pr-nexi-paypal-en.pdf"
BANCOMAT = PR + "2024/2024-04-03-pr-nexi-bancomat.pdf"
LUNAROSSA = PR + "2026/2026-09-pr-Nexi-Visa-LunaRossa-ENG.pdf"
SOFTPOS = PR + "2024/2024-05-29-pr-Nexi-Apple.pdf"
SOFTPOSSHOP = "https://www.nexi.it/shop/it/softpos"
SMARTPA = PR + "2026/2026-03-02-pr-smartPA-nexi.pdf"
INSTORE = "https://www.nexigroup.com/en/business/retailers-and-merchants/in-store-payments/"
ECOM = "https://www.nexigroup.com/en/business/retailers-and-merchants/e-commerce/"
ISSUINGPG = "https://www.nexigroup.com/en/business/banks-and-financial-institutions/cards-issuing-and-mobile-payments/"
DIGPAY = "https://www.nexigroup.com/en/business/banks-and-financial-institutions/digital-payments/"
DANKORT = "https://www.dankort.dk/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "results · owners · heritage", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: €3.6 billion of revenue at a 53% EBITDA margin, private-equity and Italian-state owners with bidders circling, a new chief executive, the ICBPI, Nets and SIA mergers, and a 2026 transition year.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & results", "blurb": "€3.6bn, 53% margin.", "div": "grp", "rev": "grp", "products": [
            P("scale", "Revenue & earnings", "FY2025 revenue of €3,585 million (+2.1%), EBITDA of €1,904 million (53.1% margin) and normalised net profit of €783 million, but a reported loss of €3,377 million after a €3.7 billion goodwill impairment; 1H 2026 revenue of €1,736 million (+1.0%) and EBITDA of €870 million; net debt €5.1 billion (2.7x).",
              s=["bank"], neo=[0, ""], src=[["1H 2026 results", H1], ["FY2025 results", FY25]]),
            P("volumes", "Volumes & footprint", "In 2025, 20.1 billion merchant transactions worth €837 billion and 22.0 billion issuing transactions worth €952 billion; about 9,600 staff in 25+ countries, about 3 million terminals and 140 million cards for about 250 banks and corporates.",
              s=["sme", "bank"], neo=[0, ""], src=[["FY2025 results", FY25], ["Nexi: group", GROUP]]),
        ]},
        {"id": "1.2", "ic": "coins", "name": "Owners & bidders", "blurb": "H&F, CDP, CVC circling.", "div": "grp", "rev": "grp", "products": [
            P("ownership", "Shareholders, ratings & bids", "Hellman & Friedman 22.2% and CDP Equity 19.1% (May 2026), with CDP cleared to go to 29.9% ⚠ not verified; investment-grade at Fitch and S&P. The board rejected TPG's offer for Digital Banking Solutions (December 2025) and CVC was reported weighing a €9 billion bid (April 2026); Italy's golden power applies. Market cap about €5.1–5.2 billion at €4.41 ⚠ derived.",
              s=["bank"], st="flux", neo=[0, ""], src=[["Milano Finanza: CDP, May 2026", CDP], ["EPI: CVC weighs bid, Apr 2026", CVC], ["Nexi: TPG offer rejected, Dec 2025", TPGNO], ["Borsa Italiana: NEXI", BORSA]]),
        ]},
        {"id": "1.3", "ic": "users-round", "name": "Leadership", "blurb": "Mingrone since March 2026.", "div": "grp", "rev": "grp", "products": [
            P("leadership", "Board & management", "Chair Marcello Sala; CEO Bernardo Mingrone (March 2026, after Paolo Bertoluzzo's ten years; CFO since 2016); CFO Piergiorgio Pedron (April 2026); regional heads for the Nordics, DACH and CSEE. The roles of business heads Roberto Catanzaro and Christian Segersven are unclear after a July 2026 simplification ⚠.",
              s=["bank"], st="flux", neo=[0, ""], src=[["Nexi: CEO appointment, Mar 2026", CEO], ["Nexi: CFO appointment, Jan 2026", CFO], ["Nexi: management", MGMT]]),
        ]},
        {"id": "1.4", "ic": "badge-check", "name": "Heritage", "blurb": "ICBPI, Nets, SIA.", "div": "grp", "rev": "grp", "products": [
            P("heritage", "Heritage & mergers", "ICBPI (1939) and CartaSi, renamed Nexi in 2017 and listed in 2019; Intesa's acquiring book (2020), Nets (2021) and SIA (2022). Before the merger Nets sold its account-to-account business, including Betalingsservice, to Mastercard for €2.85 billion (March 2021).",
              s=["bank"], o="I", neo=[0, "Nets' A2A arm went to Mastercard."], src=[["Wikipedia: Nexi", WIKI], ["Mastercard: Nets A2A acquisition, Mar 2021", NETSA2A]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy 2026–28", "blurb": "A transition year.", "div": "grp", "rev": "grp", "products": [
            P("strategy", "Capital Markets Day plan", "2026 a transition year with revenue growth in line with 2025 and EBITDA broadly flat; mid-single-digit growth and margin expansion in 2028; about €2.4 billion of excess cash over 2026–28 and a dividend growing at least 5% a year. Levers: SmartPay, more than 600 extra salespeople, Nexi Checkout, issuing services and AI.",
              s=["sme", "bank"], st="new", neo=[0, ""], src=[["Nexi: Capital Markets Day, Mar 2026", CMD]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: card acquiring worth €837 billion a year, e-commerce gateways from Computop to Przelewy24, issuer processing for 140 million cards, the Bancomat and Dankort domestic schemes, instant payments, Wero and the digital euro, and payouts and alternative methods.",
    "tiles": [
        {"id": "2.1", "ic": "store", "name": "Card acquiring", "blurb": "€837bn in 2025.", "div": "nexi", "rev": "ms", "products": [
            P("acquiring", "Merchant acquiring", "Multi-scheme acquiring, Merchant Solutions €2,038 million of revenue (57%) in 2025, accepting Mastercard, Maestro, Visa, V-PAY, UnionPay, JCB, Bancomat Pay, Amex and Diners; Italy is 59% of group revenue, with the Nordics, CSEE and DACH behind it.",
              s=["sme", "mid"], lc="move", neo=[1, "Accepts every network, with domestic schemes."], src=[["FY2025 results", FY25], ["Nexi: e-commerce", ECOM], ["9M 2025 presentation", NINEM]]),
        ]},
        {"id": "2.2", "ic": "monitor", "name": "E-commerce gateways", "blurb": "Computop, P24, XPay.", "div": "computop", "rev": "ms", "products": [
            P("ecom", "Nexi e-commerce gateway", "Plug-ins, SDKs, 3-D Secure, real-time fraud tools, currency conversion and recurring payments for online merchants; the Italian 'XPay' name is not confirmed ⚠.",
              s=["mid"], lc="move", neo=[1, "Accepts every network."], src=[["Nexi: e-commerce", ECOM]]),
            P("computop", "Computop Paygate", "The DACH e-commerce gateway, fully owned since 2025 and a technical service provider for Wero.",
              s=["mid"], lc="move", o="A", neo=[1, "Accepts every network."], src=[["FY2025 results", FY25], ["Nexi: Wero e-commerce in Germany, Apr 2026", WERO26]]),
            P("p24", "Przelewy24", "The Polish e-commerce payment provider, under pricing pressure in 1H 2026.",
              s=["mid"], lc="move", o="A", neo=[None, "Method mix not stated."], src=[["1H 2026 results call", CALL]]),
        ]},
        {"id": "2.3", "ic": "credit-card", "name": "Issuer processing", "blurb": "140m cards, 250 banks.", "div": "sia", "rev": "iss", "products": [
            P("issuing", "Issuer processing", "Issuing Solutions, €1,157 million of revenue in 2025: 22 billion transactions for about 250 banks and corporates, with 'international debit in Italy' a named growth driver. A large Nordic issuing client migrated away at the end of 2025.",
              s=["bank"], lc="move", neo=[1, "Every scheme; split not disclosed ⚠."],
              mc="Italy's move from Bancomat-only cards to scheme debit is open to both networks.",
              src=[["FY2025 results", FY25], ["1H 2026 results", H1], ["1H 2026 results call", CALL]]),
            P("wallets", "Mobile & wearable wallets", "Tokenised cards in Apple, Google and Samsung wallets and on Fitbit, Garmin and Swatch wearables for issuing banks.",
              s=["bank", "con"], lc="everyday", neo=[1, "Every scheme."], src=[["Nexi: cards issuing", ISSUINGPG]]),
        ]},
        {"id": "2.4", "ic": "flag", "name": "Domestic schemes", "blurb": "Bancomat, Dankort.", "div": "nexi", "rev": "iss", "products": [
            P("bancomat", "Bancomat processing hub", "Builds and runs Bancomat's processing hub under a contract signed April 2024: about 2 billion transactions, €160 billion and 34 million cards a year, ramping up in 2026 and lifting national-scheme volumes.",
              s=["bank", "con"], lc="move", ay="Apr 2024", neo=[0, "Domestic scheme."],
              mc="Nexi is building the domestic scheme's engine in Italy.",
              src=[["Nexi: Bancomat, Apr 2024", BANCOMAT], ["1H 2026 results", H1]]),
            P("dankort", "Dankort", "Denmark's debit scheme, linked to Nets, usable in Apple Pay at more than 40 banks ⚠ Nexi's operator role not stated.",
              s=["con"], lc="move", o="I", neo=[0, "Domestic scheme."], src=[["Dankort", DANKORT]]),
        ]},
        {"id": "2.5", "ic": "arrow-left-right", "name": "A2A, instant & digital money", "blurb": "Wero, Zippay, digital euro.", "div": "sia", "rev": "dbs", "products": [
            P("dph", "Digital Payment Hub & clearing", "Instant, SEPA credit-transfer and direct-debit processing with fraud and sanctions screening, ACH and SEPA clearing, SEPA direct debits for Danish banks (March 2026) and the Reserve Bank of New Zealand's RTGS upgrade (October 2025).",
              s=["bank"], lc="move", neo=[0, ""], src=[["Nexi: digital payments", DIGPAY], ["Nexi: press releases", ARCHIVE]]),
            P("zippay", "Zippay, Jiffy & Request to Pay", "Zippay mobile-number payments for AIB, Bank of Ireland and PTSB (March 2026, 5 million potential customers), Jiffy and Bancomat Pay rails, MyBank, and Request to Pay with CBI and EBA Clearing (2025–26).",
              s=["bank", "con"], lc="move", st="new", neo=[0, ""], src=[["Nexi: Zippay, Mar 2026", ZIPPAY], ["Nexi: digital payments", DIGPAY]]),
            P("wero", "Wero", "A founding EPI member and shareholder, a licensed Wero acquirer in Germany since February 2025, and live in German e-commerce with BAUR, Quelle and Bünting (April 2026), with point of sale planned.",
              s=["mid", "bank"], lc="move", st="new", neo=[0, "Off the card networks."],
              mc="Wero could take German and Italian debit volume away from cards.",
              src=[["Nexi: Wero acquirer, Feb 2025", WERO25], ["Nexi: Wero e-commerce in Germany, Apr 2026", WERO26]]),
            P("deuro", "Digital euro", "Part of the G+D consortium for the ECB's offline digital euro (October 2025) and a pilot PSP from the second half of 2027, planning to sell the infrastructure to other banks.",
              s=["bank"], lc="move", st="new", neo=[0, ""], src=[["Nexi: digital euro pilot, Jul 2026", DEURO], ["1H 2026 results call", CALL]]),
        ]},
        {"id": "2.6", "ic": "send", "name": "Payouts & methods", "blurb": "Move, Visa Direct, PayPal.", "div": "nexi", "rev": "ms", "products": [
            P("move", "Mastercard Move", "Payouts for Italian businesses on Mastercard Move, piloted from October 2025 and fully integrated during 2026.", short="Mastercard Move",
              s=["mid"], lc="move", st="new", ay="Oct 2025", o="P", at="Mastercard", neo=[3, "Mastercard Move."],
              mc="Live only in Italy; the Nordic, DACH and Polish merchants are next in line.",
              src=[["Nexi: Visa Direct and Mastercard Move, Oct 2025", MOVE]]),
            P("visadirect", "Visa Direct", "Visa Direct payouts, announced in the same release as Move (October 2025).",
              s=["mid"], lc="move", st="new", ay="Oct 2025", o="P", at="Visa", neo=[0, "Visa."], src=[["Nexi: Visa Direct and Mastercard Move, Oct 2025", MOVE]]),
            P("apms", "Wallets, methods & pay-later", "PayPal as a collecting PSP in Italy, the Nordics and Poland (March 2026), Klarna, WeChat Pay in Switzerland, JCB and UnionPay, Compass BNPL (2024), PayPal Pay Later and Younited Pay from 2027.",
              s=["mid", "con"], lc="borrow", o="P", at="PayPal, Klarna, Younited", neo=[0, "Off the card networks."],
              mc="Nexi relies on third parties for instalments; 78% of Italians bought in instalments in 1H 2026, per Younited.",
              src=[["Nexi: PayPal, Mar 2026", PAYPAL], ["Nexi: Younited, Jun 2026", YOUNITED], ["Nexi: press releases", ARCHIVE]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every payment: open banking on Mastercard's rails, 3-D Secure, Ethoca and Verification of Payee, an agentic MCP server and a Google Cloud pact, Nexi Ready managed issuing launched with Visa in Germany, and loyalty and value-added services.",
    "tiles": [
        {"id": "3.1", "ic": "plug", "name": "Open banking", "blurb": "On Mastercard since 2024.", "div": "nexi", "rev": "ms", "products": [
            P("mcob", "Mastercard Open Banking in Nexi gateways", "Account-to-account payments in Nexi's European gateways powered by Mastercard Open Banking (March 2024).", short="Mastercard Open Banking",
              s=["mid"], lc="move", ay="Mar 2024", o="P", at="Mastercard", neo=[3, "Mastercard Open Banking."], src=[["Mastercard and Nexi: open banking, Mar 2024", MCOB]]),
            P("obplatform", "Open banking platform for banks", "Nexi's own open banking, compliance and IBAN-check services for banks and corporates.",
              s=["bank"], lc="open", neo=[0, ""], src=[["Nexi: digital payments", DIGPAY]]),
        ]},
        {"id": "3.2", "ic": "shield-check", "name": "Fraud & disputes", "blurb": "3DS, Ethoca, VoP.", "div": "nexi", "rev": "ms", "products": [
            P("fraud", "3-D Secure & fraud prevention", "3-D Secure and real-time fraud tools for merchants, and fraud and notification services for issuers.",
              s=["mid", "bank"], lc="everyday", neo=[1, "3-D Secure for every network; own fraud tools."], src=[["Nexi: e-commerce", ECOM], ["Nexi: cards issuing", ISSUINGPG]]),
            P("ethoca", "Ethoca", "Nets partnered with Mastercard's Ethoca on chargebacks and friendly fraud (December 2021).",
              s=["mid"], lc="everyday", ay="Dec 2021", o="P", at="Mastercard", neo=[3, "Mastercard's Ethoca, through Nets."],
              mc="Only through Nets so far; Italian and DACH acquiring are untouched.",
              src=[["Nexi: press releases", ARCHIVE]]),
            P("vop", "Verification of Payee", "Verification of Payee for EBA Clearing and CBI under the EU instant-payments rules (2025).",
              s=["bank"], lc="move", neo=[0, ""], src=[["9M 2025 presentation", NINEM]]),
        ]},
        {"id": "3.3", "ic": "bot", "name": "AI & agentic", "blurb": "MCP server, Google Cloud.", "div": "nexi", "rev": "ms", "products": [
            P("agentic", "Agentic commerce", "A Nexi MCP server for agent-initiated payments (March 2026), piloting in the Nordics and Italy and built 'with Google, Visa and Mastercard'; Agentic Commerce Alliance member (January 2026); ReFiBuy optimisation (September 2026); named as exploring Mastercard Agent Connect (September 2026) ⚠ secondary.",
              s=["mid"], lc="grow", st="new", neo=[1, "With Google, Visa and Mastercard."],
              mc="Agent Pay and agentic tokens are not yet in Nexi's gateways.",
              src=[["Nexi: agentic commerce, Mar 2026", MCP], ["Nexi: ReFiBuy, Sep 2026", REFIBUY], ["Pulse 2.0: Agent Connect, Sep 2026", AGENTCONNECT]]),
            P("google", "Google Cloud", "A memorandum with Google Cloud (March 2026) on real-time fraud detection, onboarding, AP2 and UCP.",
              s=["mid", "bank"], lc="everyday", st="new", o="P", at="Google Cloud", neo=[0, ""], src=[["Nexi: Google Cloud, Mar 2026", GOOGLE]]),
        ]},
        {"id": "3.4", "ic": "rocket", "name": "Managed issuing", "blurb": "Nexi Ready, with Visa.", "div": "nexi", "rev": "iss", "products": [
            P("nexiready", "Nexi Ready", "Managed card issuing for banks, launched February 2026 (first customer live in Germany in October 2025), serving more than 100 banks, with Visa as network partner in Germany (April 2026) and wider geographies to follow.",
              s=["bank"], lc="open", st="new", ay="Feb 2026", o="P", at="Visa", neo=[0, "Visa in Germany."],
              mc="The clearest open slot: a Mastercard partner for Nexi Ready outside Germany.",
              src=[["Nexi: Nexi Ready, Feb 2026", READY], ["Nexi and Visa in Germany, Apr 2026", VISAREADY]]),
        ]},
        {"id": "3.5", "ic": "gift", "name": "Loyalty & VAS", "blurb": "Cashback, Nexi Club.", "div": "nexi", "rev": "iss", "products": [
            P("vas", "Issuer value-added services", "Customer value management, loyalty and cashback for issuers, the Digital Factory (Bridge, SDK) and currency conversion for merchants.",
              s=["bank"], lc="grow", neo=[0, ""], src=[["Nexi: cards issuing", ISSUINGPG], ["9M 2025 presentation", NINEM]]),
            P("nexiclub", "Nexi Club & Nexi Business app", "Rewards and a business app for Nexi's own merchants.",
              s=["sme"], lc="grow", neo=[0, ""], src=[["Nexi: SoftPOS shop", SOFTPOSSHOP]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "Who buys: Italian small merchants on SmartPay, mid-market and national merchants, banks and corporates that issue cards, banks that buy Digital Banking Solutions, and Italy's public administration.",
    "tiles": [
        {"id": "4.1", "ic": "briefcase", "name": "Small merchants", "blurb": "SmartPay.", "div": "nexi", "rev": "ms", "products": [
            P("smartpay", "SmartPay", "A hyper-local, all-channel acceptance offer for small merchants, sold by more than 600 extra salespeople under the 2026–28 plan.",
              s=["sme"], lc="everyday", st="new", neo=[1, "Accepts every network."], src=[["Nexi: Capital Markets Day, Mar 2026", CMD]]),
        ]},
        {"id": "4.2", "ic": "building-2", "name": "Mid-market & e-commerce", "blurb": "Nexi Unified, Checkout.", "div": "nexi", "rev": "ms", "products": [
            P("unified", "Nexi Unified", "An omnichannel offer for national mid-corporates in retail, hospitality and mobility.",
              s=["mid"], lc="everyday", st="new", neo=[1, "Accepts every network."], src=[["Nexi: Capital Markets Day, Mar 2026", CMD]]),
            P("checkout", "Nexi Checkout", "A collecting checkout for mid-market e-commerce, one of the 2026–28 growth levers.",
              s=["mid"], lc="move", st="new", neo=[1, "Accepts every network."],
              mc="No public sign of Click to Pay or Mastercard tokens here ⚠.",
              src=[["Nexi: Capital Markets Day, Mar 2026", CMD]]),
        ]},
        {"id": "4.3", "ic": "credit-card", "name": "Cards for banks & corporates", "blurb": "Credit, debit, fleet.", "div": "nexi", "rev": "iss", "products": [
            P("cards", "Cards for banks", "Credit, debit, prepaid, commercial and virtual cards issued by banks on Nexi's platforms; Nexi says Italian in-store mobile spending grew 61% in 2024.",
              s=["bank", "con"], lc="everyday", neo=[1, "Every scheme."], src=[["Nexi: cards issuing", ISSUINGPG], ["Nexi: press releases", ARCHIVE]]),
            P("eurowag", "Eurowag fleet cards", "Fleet and prepaid cards with Eurowag on Visa (February 2025).",
              s=["mid"], lc="everyday", ay="Feb 2025", o="P", at="Visa", neo=[0, "Visa."], src=[["Nexi: press releases", ARCHIVE]]),
        ]},
        {"id": "4.4", "ic": "database", "name": "Digital Banking Solutions", "blurb": "€391m, kept from TPG.", "div": "sia", "rev": "dbs", "products": [
            P("dbs", "Digital Banking Solutions", "€391 million of revenue in 2025 (+4.5% in 1H 2026): the NOVA digital-banking platform with Engineering (2024), clearing and instant payments, and compliance services. The board turned down TPG's offer for it in December 2025.",
              s=["bank"], lc="everyday", neo=[0, ""], src=[["FY2025 results", FY25], ["Nexi: TPG offer rejected, Dec 2025", TPGNO]]),
        ]},
        {"id": "4.5", "ic": "scroll-text", "name": "Public sector", "blurb": "pagoPA.", "div": "nexi", "rev": "dbs", "products": [
            P("pagopa", "pagoPA & Smart PA", "PSP and technology partner for pagoPA, Italy's public-payments system (about 450 million transactions in 2025), and Nexi Smart PA for pagoPA payments on SmartPOS (summer 2026).",
              s=["pa"], lc="beyond", st="new", neo=[None, "Network not stated."], src=[["Nexi: Smart PA, Mar 2026", SMARTPA], ["Nexi: digital payments", DIGPAY]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Nexi: the partner banks whose books it bought, about 3 million terminals and SoftPOS phones, and ISVs and direct sales.",
    "tiles": [
        {"id": "5.1", "ic": "users-round", "name": "Bank partners", "blurb": "Intesa, Crédit Agricole Italia.", "div": "nexi", "rev": "ms", "products": [
            P("banks", "Bank partnerships", "Merchant books bought from Intesa (2020), Banca di Credito Popolare (2025) and Banca Popolare di Sondrio (2Q 2026), and Crédit Agricole Italia renewed to 2029; contract renegotiations are the main 2025–26 headwind.",
              s=["sme", "bank"], lc="open", o="A", st="flux", neo=[0, ""], src=[["FY2025 results", FY25], ["1H 2026 results", H1], ["Nexi: press releases", ARCHIVE]]),
        ]},
        {"id": "5.2", "ic": "smartphone", "name": "Devices", "blurb": "SmartPOS, SoftPOS.", "div": "nexi", "rev": "ms", "products": [
            P("smartpos", "SmartPOS & SmartStation", "Android SmartPOS with an app store, SmartPOS Cashier with a tax-compliant till, and SmartStation, a dual-screen device for ISVs (February 2026).",
              s=["sme", "isv"], lc="everyday", neo=[1, "Accepts every network."], src=[["Nexi: in-store payments", INSTORE], ["Nexi: SmartStation, Feb 2026", STATION]]),
            P("softpos", "Nexi SoftPOS", "Phone-as-terminal on Android and Tap to Pay on iPhone (Italy May 2024, Germany, Switzerland and Finland since); in Italy a flat 1.89% for PagoBANCOMAT, Visa and Mastercard.",
              s=["sme"], lc="move", ay="May 2024", neo=[1, "Mastercard priced the same as Visa and PagoBANCOMAT."], src=[["Nexi: Tap to Pay on iPhone, May 2024", SOFTPOS], ["Nexi: SoftPOS shop", SOFTPOSSHOP]]),
        ]},
        {"id": "5.3", "ic": "code-xml", "name": "ISVs & direct sales", "blurb": "50+ new ISVs.", "div": "nexi", "rev": "ms", "products": [
            P("isv", "Nexi Integrated & direct sales", "Nexi Integrated, Partner Hub and Alliance for software partners, with more than 50 new ISV partnerships in 9M 2025 and Zucchetti expanded; direct sales made about 26% of new Italian SME sales.",
              s=["isv", "sme"], lc="open", neo=[0, ""], src=[["9M 2025 presentation", NINEM], ["Nexi: Capital Markets Day, Mar 2026", CMD]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Nexi", "blurb": "Open banking, Move, Ethoca.", "products": [
        P("mcatnexi", "Mastercard at Nexi", "Nexi accepts and processes Mastercard everywhere, runs open banking on Mastercard's rails (2024), pays out on Mastercard Move in Italy (2025–26) and used Ethoca through Nets; Mastercard owns Nets' old account-to-account business. Visa won the Nexi Ready launch in Germany, Visa Direct and Eurowag, and co-sponsors Luna Rossa with Nexi. The network split is not disclosed.",
          s=["bank"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Mastercard and Nexi: open banking, Mar 2024", MCOB], ["Nexi and Visa in Germany, Apr 2026", VISAREADY], ["Nexi and Visa: Luna Rossa, Sep 2026", LUNAROSSA]]),
    ]},
    {"id": "pillar-market", "name": "European processing", "blurb": "Bidders, Wero, debit.", "products": [
        P("market", "The market", "Private-equity and state ownership in play, Italian banks consolidating and renegotiating, Wero and the digital euro as account-based rivals to cards, Bancomat volumes rising, and German consumer weakness; peers such as Worldline, Adyen and Stripe ⚠ are inference, not sourced.",
          s=["bank"], div="grp", rev="grp", src=[["1H 2026 results call", CALL], ["EPI: CVC weighs bid, Apr 2026", CVC]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
