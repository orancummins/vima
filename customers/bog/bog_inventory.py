"""Bank of Georgia's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are Lion Finance Group's own unless a source says otherwise: the 2Q26 and 1H26 results
(11 August 2026) and the 4Q25 and FY25 results (25 February 2026). Bank of Georgia's own website could
not be read (bot wall), so card details lean on press and guides, marked ⚠. ``neo`` is the Mastercard
lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard,
1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H126 = "https://data.fca.org.uk/artefacts/NSM/RNS/de38e4d0-f536-4530-91c8-a704d19349cc.html"
FY25 = "https://data.fca.org.uk/artefacts/NSM/RNS/a746d49f-ea50-4c6d-a5b0-9dd0f6bfca90.html"
AIBANK = "https://www.investegate.co.uk/announcement/rns/lion-finance-group-plc--bgeo/bank-of-georgia-named-world-s-best-ai-bank-2026/9824883"
IFC = "https://www.investegate.co.uk/announcement/rns/lion-finance-group-plc--bgeo/jsc-bank-of-georgia-signs-loan-agreements-with-ifc/9812153"
EXEC26 = "https://www.investegate.co.uk/announcement/rns/lion-finance-group-plc--bgeo/executive-management-changes/9354465"
PAYHEAD = "https://www.investegate.co.uk/announcement/rns/lion-finance-group-plc--bgeo/bank-of-georgia-executive-management-updates/9323525"
PREMIUM = "https://www.investegate.co.uk/announcement/rns/lion-finance-group-plc--bgeo/bank-of-georgia-executive-management-updates/9574254"
NOTES = "https://www.investegate.co.uk/announcement/rns/lion-finance-group-plc--bgeo/bank-of-georgia-priced-usd-300-000-000-6-50-notes/9590536"
ORUJYAN = "https://www.investegate.co.uk/announcement/rns/lion-finance-group-plc--bgeo/directorate-change/9465618"
MALTA = "https://www.investegate.co.uk/announcement/rns/lion-finance-group-plc--bgeo/statement-re-press-comment/9015453"
NAME = "https://www.investegate.co.uk/announcement/rns/lion-finance-group-plc--bgeo/change-of-name-to-lion-finance-group-plc/8725823"
APPLEPAY = "https://www.investegate.co.uk/announcement/rns/lion-finance-group-plc--bgeo/bog-launches-apple-pay-service-for-its-customers/49015"
WIKI_LFG = "https://en.wikipedia.org/wiki/Lion_Finance_Group"
WIKI_BOG = "https://en.wikipedia.org/wiki/Bank_of_Georgia"
AMEX08 = "https://georgiacapital.ge/news/company-news/430-bank-of-georgia-becomes-exclusive-partner-of-american-express-for-credit-card-acquiring-and-issuing-in-georgia"
MCBIZ = "https://cbw.ge/banking/bank-of-georgia-and-mastercard-unveil-exclusive-offers-for-business-cardholders"
MC2025 = "https://georgiatoday.ge/georgia-as-a-financial-innovation-hub-mastercard-summarizes-2025"
MCCORP = "https://gbc.ge/en/news/finanse/bank-of-georgia-offers-mastercard-corporate-card"
NBGVISA = "https://nbg.gov.ge/en/media/news/natia-turnava-meets-with-visa-senior-vice-president"
NBGOB = "https://nbg.gov.ge/en/page/open-banking"
NBGCARD = "https://nbg.gov.ge/en/page/card-payment-systems"
JAM = "https://jam-news.net/georgias-national-bank-on-new-payment-system/"
MONTRAN = "https://persportaal.anp.nl/artikel/CSN-030626022/national-bank-of-georgia-launches-modernized-rtgs-payment-system-with-montran"
SOLO = "https://pbservices.ge/blog/solo-bank-bogs-premium-branch/"
EXPAT = "https://expathub.ge/georgian-banks-for-expats/"
DIGCARD = "https://cbw.ge/banking/bank-of-georgia-introduces-digital-card"
AMERIA = "https://ameriabank.am/en/personal/cards"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · governance · heritage", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: about 40% of Georgian banking assets and a group return on equity of 27%, a London listing renamed Lion Finance Group in 2025, roots back to 1903, generative AI since 2025, and a target of about 15% loan growth a year.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "GEL 1.2bn profit in the half.", "div": "lfg", "rev": "other", "products": [
            P("balance", "Group balance sheet & earnings", "Profit of GEL 1,203.8 million in 1H26 (up 17.3%; ROAE 27.2%), of which Georgia GEL 925.1 million and Armenia GEL 272.5 million; loans of GEL 44.4 billion and deposits of GEL 43.7 billion at 30 June 2026; total assets GEL 65.8 billion. Profit before one-offs was GEL 2.19 billion in 2025 (ROAE 28.4%).",
              s=["con"], neo=[0, ""], src=[["1H26 results, Aug 2026", H126], ["FY25 results, Feb 2026", FY25]]),
            P("systemic", "Bank of Georgia's place in the system", "Around 40% of Georgian banking assets and a systemically important bank with a 3.0% buffer for 2026; Wikipedia ranks it second by assets after TBC ⚠. About 8,600 staff at the bank and 13,300 across the group.",
              s=["con"], neo=[0, ""], src=[["Wikipedia: Bank of Georgia", WIKI_BOG], ["1H26 results, Aug 2026", H126]]),
            P("funding", "Bonds & development-bank lines", "USD 300 million of 6.50% senior notes due 2031, rated Ba2 by Moody's (May 2026), a GEL 450 million 11.50% local-currency Eurobond (2025) and USD 118 million from IFC for small businesses, 30% of it rural (October 2026).",
              s=["corp"], st="new", o="P", at="IFC", neo=[0, ""], src=[["USD 300m notes, May 2026", NOTES], ["IFC loans, Oct 2026", IFC], ["FY25 results, Feb 2026", FY25]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership & board", "blurb": "Gachechiladze and Carvill.", "div": "lfg", "rev": "other", "products": [
            P("board", "Lion Finance Group board", "Chair Mel Carvill and CEO Archil Gachechiladze; independent directors include Andrew McIntyre (audit), Maria Gordon (remuneration, from June 2026) and Armen Orujyan (from March 2026).",
              s=["corp"], neo=[0, ""], src=[["Board appointment, Mar 2026", ORUJYAN], ["Wikipedia: Lion Finance Group", WIKI_LFG]]),
            P("exco", "Bank of Georgia executives", "Archil Gachechiladze runs both group and bank; Giorgi Shagidze, ex-CEO of Moldova's maib, became group CFO in March 2026; Giorgi Gureshidze is deputy CEO for mass retail; Levan Kobakhidze has led the payments business since 1 January 2026; Valerian Gabunia has led premium banking since 1 July 2026.",
              s=["corp"], neo=[0, ""], src=[["Management changes, Jan 2026", EXEC26], ["Head of Payments, Dec 2025", PAYHEAD], ["Premium banking, May 2026", PREMIUM]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & listing", "blurb": "Roots in 1903, London since 2007.", "div": "lfg", "rev": "other", "products": [
            P("heritage", "Heritage & listing", "Roots in 1903; privatised and renamed Bank of Georgia in 1994; the first international IPO from Georgia in London in 2007; Georgia Capital demerged in 2018; the parent renamed Lion Finance Group PLC on 6 February 2025, keeping the bank brands. LSE ticker BGEO, a FTSE 100 member in 2026.",
              s=["corp"], o="I", neo=[0, ""], src=[["Wikipedia: Bank of Georgia", WIKI_BOG], ["Change of name, Feb 2025", NAME], ["1H26 results, Aug 2026", H126]]),
        ]},
        {"id": "1.4", "ic": "brain", "name": "Technology & AI", "blurb": "World's Best AI Bank 2026.", "div": "bog", "rev": "other", "products": [
            P("tech", "AI, models & security", "Generative AI and large language models in use since 2025 under the bank's model-risk rules; named World's Best AI Bank 2026 by Global Finance (15 October 2026), after World's Best Digital Bank in 2024 and 2025; ISO 27001 certified in 2025.",
              s=["corp"], st="new", o="B", neo=[0, ""], src=[["World's Best AI Bank, Oct 2026", AIBANK], ["1H26 results, Aug 2026", H126]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "15% growth, 20%+ ROAE.", "div": "lfg", "rev": "other", "products": [
            P("strategy", "Medium-term targets", "About 15% loan growth a year, return on equity above 20% and a 30–50% payout; Georgia growing loans 17% and Armenia 37% in the year to June 2026.",
              s=["corp"], neo=[0, ""], src=[["1H26 results, Aug 2026", H126]]),
            P("deals", "Deals", "Ameriabank in Armenia (about USD 303.6 million, consolidated from 2024), a bid for HSBC Malta confirmed in July 2025 with no deal announced since ⚠, and Digital Area's purchase of the Fina ERP platform (2025).",
              s=["corp"], o="A", neo=[0, ""], src=[["Wikipedia: Lion Finance Group", WIKI_LFG], ["HSBC Malta statement, Jul 2025", MALTA], ["FY25 results, Feb 2026", FY25]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "How money moves: Visa and Mastercard cards side by side for 1.7 million paying customers, American Express on an exclusive deal, a Mastercard Corporate Card, Apple Pay, more than half of Georgia's card acquiring, and the central bank's instant payments and open banking coming alongside.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Everyday cards & wallets", "blurb": "Visa or Mastercard, customer's choice.", "div": "bog", "rev": "retail", "products": [
            P("debit", "Debit & gold cards", "Cards for 1.71 million customers who paid with a Bank of Georgia card in June 2026 (up 11.9%), offered on Visa or Mastercard in standard and gold tiers ⚠; the split by network is not public.", short="Debit (Visa & Mastercard)",
              s=["con"], lc="everyday", o="P", at="Visa, Mastercard", neo=[1, "Visa and Mastercard side by side."],
              src=[["1H26 results, Aug 2026", H126], ["Expat Hub: Georgian banks", EXPAT]]),
            P("digicard", "Digital Card", "A virtual card ordered in internet or mobile banking in seconds, on Visa or Mastercard at the customer's choice (about 2020 ⚠).",
              s=["con"], lc="open", o="P", at="Visa, Mastercard", neo=[1, "Visa or Mastercard."], src=[["CBW: Digital Card", DIGCARD]]),
            P("credit", "Credit cards & overdrafts", "Retail Banking's credit cards and overdrafts within a GEL 6.8 billion consumer-loan book growing 23% a year; networks by card not public ⚠.",
              s=["con"], lc="borrow", neo=[None, "Network split not public."], src=[["1H26 results, Aug 2026", H126]]),
            P("wallets", "Apple Pay & mobile wallets", "Apple Pay launched in September 2019 for Visa and Mastercard debit and credit cards; Google Pay status at the bank not confirmed ⚠.",
              s=["con"], lc="everyday", ay="Sep 2019", o="P", at="Apple", neo=[1, "Tokens on Visa and Mastercard."], src=[["Apple Pay launch, Sep 2019", APPLEPAY]]),
        ]},
        {"id": "2.2", "ic": "gem", "name": "Premium & Amex", "blurb": "World Elite, Visa Platinum, Amex.", "div": "solo", "rev": "retail", "products": [
            P("solocards", "SOLO cards", "SOLO Premium (about USD 105 a year) and SOLO International (about USD 260) each include both a Visa Platinum and a Mastercard World Elite card, with LoungeKey visits and a personal banker (February 2025).", short="SOLO (World Elite & Visa Platinum)",
              s=["aff"], lc="everyday", o="P", at="Visa, Mastercard", neo=[1, "World Elite alongside Visa Platinum."],
              mc="Mastercard's top tier sits in every SOLO wallet, but beside Visa.",
              src=[["PB Services: SOLO, Feb 2025", SOLO]]),
            P("amex", "American Express", "Exclusive Amex issuing and acquiring partner in Georgia since December 2008 (Green, Gold, Blue and later Platinum cards); an Amex Reward card is still listed ⚠ current exclusivity unconfirmed.",
              s=["con", "aff"], lc="everyday", o="P", at="American Express", ay="Dec 2008", neo=[0, "Amex."], src=[["Georgia Capital: Amex exclusive, Dec 2008", AMEX08], ["Expat Hub: Georgian banks", EXPAT]]),
        ]},
        {"id": "2.3", "ic": "credit-card", "name": "Business & corporate cards", "blurb": "The region's first Corporate Card.", "div": "bog", "rev": "sme", "products": [
            P("corpcard", "Mastercard Corporate Card", "Launched with Bank of Georgia in 2025 as the region's first premium business card: multi-currency account, expense management, travel insurance and access to more than 1,200 airport lounges, free for the first year ⚠ launch date.", short="Corporate Card (Mastercard)",
              s=["corp", "sme"], lc="move", st="new", ay="2025", o="P", at="Mastercard", neo=[2, "Mastercard Corporate Card."],
              mc="Mastercard's clearest standalone win at the bank.",
              src=[["Georgia Today: Mastercard 2025, Dec 2025", MC2025], ["GBC: Mastercard Corporate Card", MCCORP]]),
            P("bizcard", "Business cards", "Business cards on Visa or Mastercard ⚠, with a Mastercard offer programme of more than 20 software brands for business Mastercard holders that ran to the end of 2025.",
              s=["sme"], lc="everyday", o="P", at="Mastercard, Visa", neo=[1, "Mastercard offers; Visa also issued ⚠."], src=[["CBW: business Mastercard offers", MCBIZ], ["Expat Hub: Georgian banks", EXPAT]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Merchant acquiring", "blurb": "56.7% of Georgia's volume.", "div": "bog", "rev": "sme", "products": [
            P("pos", "POS acquiring", "56.7% of Georgian acquiring volume and 28,800 active merchants (up 13.3%) at June 2026; POS volume GEL 4.17 billion in 2Q26, up 20.9%. Accepts every network, with Amex under the 2008 exclusive ⚠.", short="POS acquiring",
              s=["merch"], lc="move", o="B", neo=[1, "Accepts every network."],
              mc="The country's largest acceptance book: Mastercard's merchant data and fraud tools fit here.",
              src=[["1H26 results, Aug 2026", H126], ["Georgia Capital: Amex exclusive, Dec 2008", AMEX08]]),
            P("ecom", "E-commerce acquiring", "GEL 2.35 billion of online card payments in 2Q26, up 18.8%, after card-to-card transfers were taken out of the figures.",
              s=["merch"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["1H26 results, Aug 2026", H126]]),
        ]},
        {"id": "2.5", "ic": "arrow-left-right", "name": "Transfers & processing", "blurb": "P2P on cards, Georgian Card.", "div": "bog", "rev": "retail", "products": [
            P("p2p", "Card-to-card transfers & settlement", "Instant card-to-card transfers, now reported apart from acquiring, and settlement operations that drove most of the 22% growth in fee income in 2Q26; inbound money transfers to Georgia rose 8.4% in the quarter.",
              s=["con"], lc="move", neo=[None, "Network split not public."], src=[["1H26 results, Aug 2026", H126]]),
            P("gcard", "Georgian Card", "The card processor Bank of Georgia bought in 2004, one of two registered processing operators that handle most card transactions in Georgia, with UFC ⚠ current ownership.",
              s=["merch"], lc="move", o="A", ay="2004", neo=[0, ""], src=[["Wikipedia: Bank of Georgia", WIKI_BOG], ["NBG: card payment systems", NBGCARD]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Instant payments & open banking", "blurb": "National rails due end-2026.", "div": "bog", "rev": "retail", "products": [
            P("ips", "NBG instant payments", "A cardless, SEPA-compatible instant payment system the National Bank is building with the World Bank and Montran, due by the end of 2026; the RTGS upgrade went live in June 2026. Not yet live.", short="Instant payments (NBG)",
              s=["con", "sme"], lc="move", st="unconf", o="P", at="National Bank of Georgia", neo=[0, "National rails."],
              mc="Built partly to cut card-scheme costs on domestic lari payments.",
              src=[["NBG RTGS with Montran, Jun 2026", MONTRAN], ["JAMnews: new payment system, Mar 2025", JAM]]),
            P("openbanking", "Open banking", "The NBG framework (2020) requires banks to offer account-information and payment-initiation APIs; Bank of Georgia's own API offer is not public ⚠.",
              s=["sme"], lc="move", neo=[None, "Not public."], src=[["NBG: open banking", NBGOB]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: an AI assistant that settles 80% of queries, loans decided in 15 seconds, sanctions and fraud controls, and Mastercard's Priceless, cashback and business offers.",
    "tiles": [
        {"id": "3.1", "ic": "bot", "name": "AI for customers", "blurb": "80% of queries, 15-second loans.", "div": "bog", "rev": "retail", "products": [
            P("assistant", "AI assistant", "Resolves more than 80% of customer queries on its own with a 91% satisfaction score (October 2026).",
              s=["con"], lc="everyday", st="new", o="B", neo=[0, ""],
              mc="An 'AI bank' with no public agentic-payments partner yet.",
              src=[["World's Best AI Bank, Oct 2026", AIBANK]]),
            P("instantloan", "15-second lending", "99% of unsecured loans approved and paid out in under 15 seconds, on automated, model-driven decisions.",
              s=["con"], lc="borrow", st="new", o="B", neo=[0, ""], src=[["World's Best AI Bank, Oct 2026", AIBANK], ["1H26 results, Aug 2026", H126]]),
        ]},
        {"id": "3.2", "ic": "shield-check", "name": "Fraud, AML & sanctions", "blurb": "Screening near Russia.", "div": "bog", "rev": "other", "products": [
            P("fincrime", "Financial crime & security", "Transaction monitoring, sanctions screening and enhanced due diligence given Georgia's proximity to Russia; ISO 27001 since 2025. No Mastercard fraud tool is publicly named ⚠.",
              s=["con", "corp"], lc="everyday", o="B", neo=[None, "No network tool named."], src=[["1H26 results, Aug 2026", H126]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Offers & Priceless", "blurb": "Cashback with Mastercard.", "div": "bog", "rev": "retail", "products": [
            P("offers", "Mastercard promotions & Priceless", "Bank of Georgia was a Mastercard promotion and cashback partner in 2025; SOLO ran a St George's Day event with Mastercard, and Georgia joined Mastercard's Priceless platform.",
              s=["con", "aff"], lc="grow", st="new", o="P", at="Mastercard", neo=[2, "Mastercard campaigns."], src=[["Georgia Today: Mastercard 2025, Dec 2025", MC2025]]),
            P("bizoffers", "Business software perks", "Discounts and free services from Google Workspace, Notion, HubSpot and 20 other brands for business Mastercard holders, through the business mobile and internet bank (to end-2025).",
              s=["sme"], lc="grow", o="P", at="Mastercard", neo=[3, "Mastercard's offers programme."], src=[["CBW: business Mastercard offers", MCBIZ]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: consumer loans and mortgages for 2.3 million active retail customers, SOLO for the mass affluent, small-business and corporate banking with Galt & Taggart, Digital Area's commerce tools, and Ameriabank and BNB outside Georgia.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Mass retail", "blurb": "2.3 million active customers.", "div": "bog", "rev": "retail", "products": [
            P("retail", "Retail accounts & consumer loans", "2.28 million monthly active retail customers (up 9.5%) and consumer loans of GEL 6.8 billion, up 23% in the year to June 2026.",
              s=["con"], lc="everyday", neo=[1, "Cards on Visa and Mastercard."], src=[["1H26 results, Aug 2026", H126]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Mortgages", "blurb": "GEL 5.5bn, in lari.", "div": "bog", "rev": "retail", "products": [
            P("mortgages", "Mortgages", "GEL 5.5 billion, up 16.6%, 41% of retail loans; from July 2026 loans up to GEL 1 million must be in lari where income is in lari.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["1H26 results, Aug 2026", H126]]),
        ]},
        {"id": "4.3", "ic": "gem", "name": "SOLO premium", "blurb": "The mass-affluent franchise.", "div": "solo", "rev": "retail", "products": [
            P("solo", "SOLO premium banking", "Described by the bank as the nation's leading mass-affluent franchise: personal bankers, concierge on SOLO International, and premium cards; new head from July 2026.",
              s=["aff"], lc="grow", neo=[1, "World Elite and Visa Platinum."], src=[["Premium banking, May 2026", PREMIUM], ["PB Services: SOLO, Feb 2025", SOLO]]),
        ]},
        {"id": "4.4", "ic": "briefcase", "name": "SME banking", "blurb": "136,000 active businesses.", "div": "bog", "rev": "sme", "products": [
            P("sme", "SME & micro banking", "136,400 monthly active business customers, SME loans of GEL 5.7 billion, and IFC funding of USD 118 million for MSMEs (October 2026).",
              s=["sme"], lc="borrow", neo=[1, "Business cards partly Mastercard."], src=[["1H26 results, Aug 2026", H126], ["IFC loans, Oct 2026", IFC]]),
        ]},
        {"id": "4.5", "ic": "building-2", "name": "Corporate & investment", "blurb": "GEL 10.3bn of loans.", "div": "gt", "rev": "cib", "products": [
            P("cib", "Corporate & Investment Banking", "Corporate loans of GEL 10.3 billion and deposits of GEL 7.8 billion, trade finance and documentary business.",
              s=["corp"], lc="borrow", neo=[1, "Corporate Card on Mastercard."], src=[["1H26 results, Aug 2026", H126]]),
            P("galt", "Galt & Taggart", "The group's investment bank: brokerage, research and debt capital markets, joint lead manager on the bank's 2026 notes.",
              s=["corp"], lc="grow", neo=[0, ""], src=[["USD 300m notes, May 2026", NOTES], ["1H26 results, Aug 2026", H126]]),
        ]},
        {"id": "4.6", "ic": "store", "name": "Digital Area", "blurb": "Commerce and SaaS.", "div": "da", "rev": "other", "products": [
            P("digitalarea", "Digital Area", "A Georgian digital ecosystem of e-commerce, ticketing and inventory software, which bought the Fina ERP platform in 2025 and wrote down an e-commerce delivery unit in 2026.",
              s=["merch"], lc="beyond", o="A", neo=[None, "Not public."], src=[["1H26 results, Aug 2026", H126], ["FY25 results, Feb 2026", FY25]]),
        ]},
        {"id": "4.7", "ic": "globe", "name": "Beyond Georgia", "blurb": "Ameriabank and BNB.", "div": "ameria", "rev": "afs", "products": [
            P("ameria", "Ameriabank (Armenia)", "Armenia's largest lender by loans (22.9% share), 521,500 active retail customers and digital users up 47%; issues Visa and Mastercard cards.",
              s=["con", "corp"], lc="everyday", o="A", ay="2024", neo=[1, "Visa and Mastercard."], src=[["1H26 results, Aug 2026", H126], ["Ameriabank: cards", AMERIA]]),
            P("bnb", "BNB (Belarus)", "Belarusky Narodny Bank serves retail and SME clients in Belarus; Tier 1 ratio 10.1%.",
              s=["con"], lc="everyday", neo=[None, "Not public."], src=[["1H26 results, Aug 2026", H126]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: a mobile bank opened by a million people a day, business internet and mobile banking, 206 branches and SOLO lounges, and self-service terminals.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Mobile bank", "blurb": "A million users a day.", "div": "bog", "rev": "retail", "products": [
            P("app", "Mobile & internet bank", "1.92 million monthly and 1.05 million daily digital users at June 2026 (up from 355,000 monthly in 2019); 73% of retail products sold digitally; NPS reached 76 in late 2025.",
              s=["con", "aff"], lc="open", o="B", neo=[0, ""], src=[["1H26 results, Aug 2026", H126], ["FY25 results, Feb 2026", FY25]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Business banking online", "blurb": "115,000 digital businesses.", "div": "bog", "rev": "sme", "products": [
            P("bizapp", "Business mobile & internet bank", "114,800 businesses using digital channels each month (up 14.7%), with online account opening and card applications.",
              s=["sme"], lc="open", o="B", neo=[0, ""], src=[["1H26 results, Aug 2026", H126], ["CBW: business Mastercard offers", MCBIZ]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & self-service", "blurb": "206 branches, ATMs, terminals.", "div": "bog", "rev": "retail", "products": [
            P("branches", "Branches & SOLO lounges", "206 branches at June 2026, 115 full-scale and 91 transactional, plus SOLO premium branches.",
              s=["con", "aff"], lc="open", neo=[0, ""], src=[["1H26 results, Aug 2026", H126], ["PB Services: SOLO, Feb 2025", SOLO]]),
            P("terminals", "ATMs & self-service terminals", "About 989 ATMs and 3,134 self-service payment terminals ⚠ date of count unclear.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Wikipedia: Bank of Georgia", WIKI_BOG]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Bank of Georgia", "blurb": "Side by side with Visa.", "products": [
        P("mcatbog", "Mastercard at Bank of Georgia", "Bank of Georgia issues Visa and Mastercard side by side, with Amex on an exclusive deal from 2008. Mastercard has the Corporate Card (2025), World Elite in every SOLO package, business offers and Priceless campaigns, and is accepted at the 56.7% of Georgian card volume the bank acquires. In 2025 the bank renegotiated terms with the international payment systems, cutting its scheme fees.",
          s=["con"], div="bog", rev="other", mc="The relationship this map is drawn for.",
          src=[["FY25 results, Feb 2026", FY25], ["Georgia Today: Mastercard 2025, Dec 2025", MC2025], ["PB Services: SOLO, Feb 2025", SOLO]]),
    ]},
    {"id": "pillar-market", "name": "Georgian payments", "blurb": "Instant payments, a national switch.", "products": [
        P("market", "The Georgian market", "Visa has 1.9 million active cards in Georgia (June 2026); the National Bank is building cardless instant payments for end-2026 and a National Switch to reduce the card schemes' role in lari transfers, after political attacks on scheme fees in March 2025.",
          s=["con"], div="bog", rev="other", src=[["NBG: Visa meeting, Jul 2026", NBGVISA], ["JAMnews: new payment system, Mar 2025", JAM], ["NBG RTGS with Montran, Jun 2026", MONTRAN]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
