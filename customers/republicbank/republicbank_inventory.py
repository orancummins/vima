"""Republic Bank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the Republic Financial Holdings (RFHL) 2025 Annual
Report (year to 30 September 2025) and the FY2026 quarterly releases to 30 June 2026. Amounts are in Trinidad and
Tobago dollars. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it,
2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

AR25 = "https://www.republictt.com/pdfs/annual-reports/RFHL-ANNUAL-REPORT-2025.pdf"
FY25 = "https://guardian.co.tt/business/rfhl-profits-hit-22b-6.2.2446238.8dc62168b9"
Q1 = "https://www.republictt.com/news/rfhl-records-5957-million-first-quarter-profits"
Q3 = "https://www.republictt.com/news/rfhl-records-152-billion-third-quarter-profits"
ESG = "https://www.republictt.com/news/rfhl-expands-sustainable-finance-commitment-us750-million-2030"
COURT = "https://www.republictt.com/news/court-appeal-rules-republic-bank-exercised-reasonable-care"
MKT = "https://stockanalysis.com/quote/ttse/RFHL/"
SCOTIA = "https://republicguyana.com/node/899"
CARDS = "https://www.republictt.com/creditcardbenefits"
AAMC = "https://www.republictt.com/personal/aadvantage-mastercard"
AAVI = "https://www.republictt.com/personal/republicaadvantage-visa-infinite-credit-card"
PRICESMART = "https://www.republictt.com/personal/republic-bank-pricesmart-visa-platinum-credit-card"
PLATMC = "https://www.republictt.com/personal/republic-bank-platinum-mastercard-credit-card"
INTLMC = "https://www.republictt.com/personal/international-mastercard-republic"
CBCC = "https://www.central-bank.org.tt/cbtt_storage/2025/09/republic-bank-limited-credit-cards-sep2025.pdf"
CBEP = "https://www.central-bank.org.tt/cbtt_storage/2025/09/republic-bank-limited-electronic-payments-sep2025.pdf"
USLIMIT = "https://stabroeknews.com/?p=727871"
DEBIT = "https://www.republictt.com/personal/republicbankvisadebit"
GIFT = "https://www.republictt.com/personal/visa-gift-cards"
ENDCASH = "https://www.republictt.com/personal/endcash"
ENDLAUNCH = "https://www.guardian.co.tt/business/republic-launches-new-payment-system-6.2.1297801.82d24357e4"
ENDSUSP = "https://trinidadexpress.com/business/local/republic-temporarily-suspends-endcash-services/article_5a4f33fb-8136-4544-9071-82a1f35e1c9f.html"
YOOZ = "https://www.republictt.com/personal/yooz-top-upbill-pay"
POS = "https://www.republictt.com/commercial/point-sale-terminals"
AMEX = "https://www.republictt.com/commercial/american-express-terminals"
COMMERCIAL = "https://www.republictt.com/commercial"
ACH = "https://www.republictt.com/commercial/republicach"
UPI = "https://thefintechtimes.com/trinidad-and-tobago-preparing-for-payments-revolution/"
PCI = "https://republictt.com/news/republic-bank-attains-international-recognition-visa-global-registry-achieving-payment-card"
ONLINE = "https://www.republictt.com/personal/republiconline"
MOBILE = "https://www.republictt.com/personal/republicmobile"
ONBOARD = "https://www.republictt.com/republiconboard"
OFFERS = "https://www.republictt.com/personal/exclusive-offers"
PRICELESS = "https://www.republictt.com/node/1612"
BALANCE = "https://balancecover.rfhl.com/tt"
SMEPACK = "https://www.republictt.com/commercial/commercial-business-packages"
VISABIZ = "https://www.republictt.com/commercial/republic-international-visa-business-card"
CORPMC = "https://www.republictt.com/commercial/republic-bank-aadvantage-corporate-mastercard"
FUNDS = "https://www.republictt.com/personal/republic-mutual-funds"
BARBADOS = "https://www.republicbarbados.com/personal/republic-credit-cards"
GHANA = "https://www.republicghana.com/"
BVI = "https://www.virginislandsnewsonline.com/en/news/republic-bank-launches-new-exclusive-vertical-mastercard-black-credit-card"
ATMS = "https://www.republictt.com/personal/blue-machine"
THIS = "https://www.republictt.com/node/1643"
WAMNOW = "https://www.central-bank.org.tt/?p=38322"
CPAY = "https://www.central-bank.org.tt/cbtt_storage/2026/06/latest-news-central-bank-authorises-convenience-pay-technologies-limited-june-2026.pdf"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · footprint · transformation", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: a TT$134.6 billion group across 16 countries, T&T's biggest branch and ATM network, Nigel Baptiste's team, a cloud-first rebuild and a growing appetite for deals.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "TT$2.2bn profit, ROE 15%.", "div": "rfhl", "rev": "group", "products": [
            P("balance", "Balance sheet & earnings", "RFHL made a profit of TT$2.2 billion in the year to September 2025 (up 9.8%), with ROE of 15.0% and capital adequacy of 14.9% (Republic Bank 16.0%). At 30 June 2026 assets were TT$134.6 billion, loans TT$77.4 billion and deposits TT$105.3 billion; nine-month profit was TT$1.52 billion, up 1.6%. Market value about TT$18.4 billion on 16 October 2026.",
              s=["inv"], neo=[0, ""], src=[["RFHL 2025 Annual Report", AR25], ["RFHL nine-month results, Jul 2026", Q3], ["StockAnalysis: RFHL", MKT]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Baptiste and Karamath.", "div": "rfhl", "rev": "group", "products": [
            P("leadership", "Board & executive team", "Yashmid Karamath chairs RFHL (from early 2026, after Vincent Pereira). Nigel Baptiste is Group President and CEO and runs Republic Bank as President and Managing Director; Marsha Mc Leod-Marshall is CFO, Houston Ross Group Chief Information and Digital Transformation Officer, and Karen Tom Yew Chief Risk Officer.",
              s=["corp"], neo=[0, ""], src=[["RFHL 2025 Annual Report", AR25], ["RFHL first-quarter results, Jan 2026", Q1]]),
        ]},
        {"id": "1.3", "ic": "earth", "name": "Heritage & footprint", "blurb": "16 countries, 7,293 staff.", "div": "rfhl", "rev": "region", "products": [
            P("footprint", "Footprint", "Banks in Trinidad and Tobago, Barbados, Guyana, Grenada, the Eastern Caribbean, Suriname, the BVI, the Cayman Islands and Ghana: 16 countries and 7,293 staff, 3,631 of them at Republic Bank in T&T. The holding company was formed by vesting order in 2015 ⚠ heritage dates not confirmed.",
              s=["con"], o="I", neo=[0, ""], src=[["RFHL 2025 Annual Report", AR25]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology", "blurb": "Cloud-first, faster onboarding.", "div": "rfhl", "rev": "group", "products": [
            P("tech", "Digital transformation", "A cloud-first architecture, a Strategic Transformation Office and new data-governance unit, revamped biometric log-in for Endcash, the group's first digital card-in-wallet (in Guyana), and digital onboarding across most subsidiaries by July 2026. No public AI programme ⚠.",
              s=["corp"], st="new", neo=[0, ""],
              mc="The card-in-wallet in Guyana is the group's first tokenisation step; T&T has none public.",
              src=[["RFHL 2025 Annual Report", AR25], ["RFHL nine-month results, Jul 2026", Q3]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "M&A and US$750m green goal.", "div": "rfhl", "rev": "group", "products": [
            P("strategy", "Strategy", "Accelerate digital transformation, expand regional connectivity and keep mergers and acquisitions as a strategic pillar. Sustainable-finance commitment raised to US$750 million by 2030 (September 2026), after about US$243 million of climate finance was deployed.",
              s=["corp"], st="new", neo=[0, ""], src=[["RFHL 2025 Annual Report", AR25], ["RFHL sustainable finance, Sep 2026", ESG]]),
            P("deals", "Deals", "RBC Royal Bank (Suriname) in 2015; Scotiabank's operations in Guyana and the Eastern Caribbean (US$123 million, agreed November 2018); 74.99% of Cayman National in 2019, raised to 86.91% in August 2025.",
              s=["corp"], o="A", neo=[0, ""], src=[["Republic: Scotiabank deal, Nov 2018", SCOTIA], ["RFHL 2025 Annual Report", AR25]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: T&T's largest credit card book on Visa and Mastercard, American Airlines and PriceSmart co-brands, Visa/LINX debit and Visa prepaid, the Endcash QR wallet, card acceptance for Visa, Mastercard, LINX and Amex, and ACH and wires.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Credit cards", "blurb": "Visa and Mastercard side by side.", "div": "rbl", "rev": "retail", "products": [
            P("visacc", "Visa credit cards", "International Visa Classic, Gold, Platinum and Signature (US$25.75 to US$100 a year), with cash back of TT$0.40 per TT$50 spent and the Visa Benefits Portal. Republic is T&T's largest credit card operator; credit card fees earned the group TT$372 million in FY2025.", short="Visa credit",
              s=["con"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Republic: credit cards", CARDS], ["Central Bank: card fees, Jun 2025", CBCC], ["RFHL 2025 Annual Report", AR25]]),
            P("mccc", "Mastercard credit cards", "International Mastercard Classic and Platinum Mastercard (US$25.75 and US$75 a year), with the same cash back, Mastercard Global Service and Purchase Protection; contactless up to TT$300. US-dollar spend on all Republic credit cards was halved to US$5,000 a cycle in September 2023.", short="Mastercard credit",
              s=["con"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="About five of Republic's twelve T&T credit programmes are Mastercard.",
              src=[["Republic: Platinum Mastercard", PLATMC], ["Republic: International Mastercard", INTLMC], ["Stabroek News: US$ limit cut, Sep 2023", USLIMIT]]),
        ]},
        {"id": "2.2", "ic": "plane", "name": "Co-brand cards", "blurb": "AAdvantage and PriceSmart.", "div": "rbl", "rev": "retail", "products": [
            P("aadvantage", "Republic Bank/AAdvantage cards", "American Airlines co-brands on both networks: AAdvantage Mastercard and Mastercard Gold (US$50 and US$60), and the top-tier AAdvantage Visa Infinite (US$150, 7,500 bonus miles); one mile per US$1 spent.", short="AAdvantage (Mastercard and Visa)",
              s=["travel"], lc="borrow", o="P", at="American Airlines", neo=[1, "Standard and Gold on Mastercard; Infinite on Visa."],
              mc="Visa holds the top tier of the travel co-brand.",
              src=[["Republic: AAdvantage Mastercard", AAMC], ["Republic: AAdvantage Visa Infinite", AAVI]]),
            P("pricesmart", "PriceSmart Visa Platinum", "A co-brand for PriceSmart members: 4% cash back at PriceSmart clubs and 1% elsewhere, US$25 a year ⚠ launch year 2019.",
              s=["con"], lc="borrow", o="P", at="PriceSmart", neo=[0, "Visa."], src=[["Republic: PriceSmart Visa Platinum", PRICESMART]]),
        ]},
        {"id": "2.3", "ic": "wallet-cards", "name": "Debit & prepaid", "blurb": "Visa/LINX debit.", "div": "rbl", "rev": "retail", "products": [
            P("debit", "Republic Bank Visa Debit", "Chip-and-PIN, contactless debit co-badged with Visa and LINX, the domestic debit network: it works where LINX is shown (in-store, ATMs and local websites), replacing the magstripe OneCard; renewals run 2026–2028.", short="Debit (Visa/LINX)",
              s=["con", "sme"], lc="everyday", o="P", at="Visa, LINX", neo=[0, "Visa/LINX."],
              mc="Visa's brand sits on every Republic debit card even though LINX carries the transactions.",
              src=[["Republic: Visa Debit", DEBIT]]),
            P("prepaid", "Visa Gift Card & travel prepaid", "Visa gift cards from TT$100 to TT$5,000, valid six months, and a VTM travel prepaid card whose maximum balance was cut to US$3,000 in October 2023 ⚠ VTM network assumed Visa.",
              s=["con", "travel"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Republic: Visa gift cards", GIFT], ["Stabroek News: US$ limit cut, Sep 2023", USLIMIT]]),
        ]},
        {"id": "2.4", "ic": "smartphone", "name": "Wallets & mobile pay", "blurb": "Endcash QR wallet.", "div": "endcash", "rev": "retail", "products": [
            P("endcash", "Endcash", "Launched in March 2021 as T&T's first mobile wallet: QR payments between people and businesses, open to non-customers and loaded from any local Visa or Mastercard card. Biometric log-in revamped in FY2025; services were suspended for a time ⚠ date and current status unconfirmed.",
              s=["con", "sme"], lc="move", st="flux", ay="Mar 2021", o="B", neo=[1, "Loaded by Visa or Mastercard cards; own QR rails."],
              mc="A bank-owned QR wallet that tokenised cards could feed.",
              src=[["Republic: Endcash", ENDCASH], ["Guardian: Endcash launch, Mar 2021", ENDLAUNCH], ["Trinidad Express: Endcash suspended", ENDSUSP]]),
            P("yooz", "Yooz top-up & bill pay", "Phone top-ups and utility bills for bmobile and Digicel users, paid from a Republic account or any bank's credit card.",
              s=["con"], lc="everyday", o="P", at="bmobile, Digicel", neo=[1, "Any bank's credit card."], src=[["Republic: Yooz", YOOZ]]),
            P("cardinwallet", "Card-in-wallet", "The group's first digital card-in-wallet went live in Guyana (FY2025). No Apple Pay or Google Pay for Republic cards in T&T is confirmed ⚠.",
              s=["con"], lc="everyday", st="unconf", neo=[None, "Network not stated."],
              mc="Tokenised wallets for T&T cards are an open gap.",
              src=[["RFHL 2025 Annual Report", AR25]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Merchant acquiring", "blurb": "Visa, Mastercard, LINX, Amex.", "div": "rbl", "rev": "retail", "products": [
            P("pos", "Point-of-sale terminals", "Terminals that accept Republic debit, LINX, and local and international Visa and Mastercard cards, with electronic settlement and regional sales representatives across Trinidad and Tobago.",
              s=["sme"], lc="move", o="B", neo=[1, "Accepts Mastercard among others."], src=[["Republic: point-of-sale terminals", POS]]),
            P("amex", "American Express acceptance", "Republic signs merchants to accept American Express cards on its terminals and EPay.",
              s=["sme"], lc="move", o="P", at="American Express", neo=[0, "Amex."], src=[["Republic: American Express terminals", AMEX]]),
            P("epay", "Republic EPay", "Republic Bank's e-commerce payment gateway for businesses ⚠ scale not published.",
              s=["sme", "corp"], lc="move", o="B", neo=[1, "Accepts cards of every network ⚠."], src=[["Republic: commercial banking", COMMERCIAL]]),
        ]},
        {"id": "2.6", "ic": "arrow-left-right", "name": "Transfers & clearing", "blurb": "ACH, RTGS and instant.", "div": "rbl", "rev": "retail", "products": [
            P("ach", "RepublicACH", "Payroll, dividend, pension and supplier payments and direct debits over Transach, the national ACH run by TTIPS under Central Bank oversight; next business day.",
              s=["sme", "corp"], lc="move", o="P", at="TTIPS", neo=[0, ""], src=[["Republic: RepublicACH", ACH]]),
            P("wires", "Wires & RTGS", "International wires and RTGS transfers at TT$65 outgoing, and transfers to any local bank from RepublicOnline.",
              s=["corp", "con"], lc="move", neo=[0, ""], src=[["Central Bank: payment fees, Jun 2025", CBEP], ["Republic: RepublicOnline", ONLINE]]),
            P("instant", "National instant payments", "T&T is building a UPI-style instant-payment platform with NPCI International for person-to-person, merchant and government payments; Republic's role is not public ⚠.",
              s=["con", "sme"], lc="move", st="unconf", neo=[0, "Account-to-account."],
              mc="A national A2A rail could compete with cards for everyday payments.",
              src=[["Fintech Times: T&T payments, Sep 2026", UPI]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: chip-and-PIN first in the English-speaking Caribbean and PCI compliance, selfie onboarding, cash back, AAdvantage and Mastercard Priceless moments, and a new data-governance unit.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "Chip, PIN and PCI DSS.", "div": "rbl", "rev": "retail", "products": [
            P("security", "Card security", "Chip-and-PIN credit cards, the first in the English-speaking Caribbean, 24-hour monitoring, and PCI DSS compliance maintained in April 2025 and listed on Visa's Global Registry of Service Providers.",
              s=["con", "sme"], lc="everyday", o="B", neo=[0, "Own controls; Visa registry."],
              mc="No public use of Mastercard fraud or scam tools.",
              src=[["Republic: PCI DSS and Visa registry, May 2025", PCI], ["Republic: credit cards", CARDS]]),
            P("alerts", "RepublicAlerts & card controls", "Instant payment notifications and the ability to deactivate cards in RepublicOnline.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["Republic: RepublicOnline", ONLINE]]),
        ]},
        {"id": "3.2", "ic": "fingerprint", "name": "Onboarding & identity", "blurb": "Selfie and liveness.", "div": "rbl", "rev": "retail", "products": [
            P("onboard", "RepublicOnboard", "Open a deposit account online with a selfie, liveness check and document capture; digital onboarding live across most group banks by July 2026.",
              s=["con"], lc="open", st="new", o="B", neo=[0, ""],
              mc="Identity checks for digital onboarding are an opening.",
              src=[["Republic: RepublicOnboard", ONBOARD], ["RFHL nine-month results, Jul 2026", Q3]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards & offers", "blurb": "Cash back and Priceless.", "div": "rbl", "rev": "retail", "products": [
            P("cashback", "Cash back & offers", "TT$0.40 cash back per TT$50 spent on Republic credit cards, credited quarterly, and card discounts with insurers such as CG United and COLFIRE.",
              s=["con"], lc="grow", o="B", neo=[1, "On Visa and Mastercard cards."], src=[["Republic: credit cards", CARDS], ["Republic: exclusive offers", OFFERS]]),
            P("priceless", "Priceless Carnival", "In February 2024 Republic, Mastercard and Tribe ran a #Priceless Experience for Republic Mastercard holders: 27 won costume rebates of up to US$1,000 and VIP Carnival access (Danielle Dumas, Mastercard T&T).",
              s=["con"], lc="grow", ay="Feb 2024", o="P", at="Mastercard, Tribe", neo=[3, "Mastercard Priceless."],
              mc="Mastercard's clearest joint marketing with Republic.",
              src=[["Republic: Priceless Carnival, Feb 2024", PRICELESS]]),
        ]},
        {"id": "3.4", "ic": "chart-column", "name": "Data & operations", "blurb": "Data governance, shared services.", "div": "rfhl", "rev": "group", "products": [
            P("data", "Data & shared services", "A Data Governance and Management unit, group Shared Services and technology support divisions, and a personal finance tracker in RepublicOnline ⚠ no data or analytics products published.",
              s=["corp"], neo=[None, ""], src=[["RFHL 2025 Annual Report", AR25], ["Republic: RepublicOnline", ONLINE]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: accounts, loans and mortgages, small-business packages and cards, corporate and investment banking, funds, trust and digital life insurance, and sister banks across the Caribbean and Ghana.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Personal banking", "blurb": "Accounts, loans, mortgages.", "div": "rbl", "rev": "retail", "products": [
            P("accounts", "Accounts", "e-Free, Savings Plus, RightStart, chequing and foreign-currency accounts, with the Visa/LINX debit card. Group deposits were TT$105.3 billion at June 2026.",
              s=["con"], lc="everyday", neo=[0, "Visa/LINX debit."], src=[["Republic: Visa Debit", DEBIT], ["RFHL nine-month results, Jul 2026", Q3]]),
            P("loans", "Loans & mortgages", "Make It Happen personal loans, car loans, H.E.L.P. student loans and the Mortgage Centre; T&T advances were TT$37.1 billion at September 2025, up 8.6%.",
              s=["home", "con"], lc="borrow", neo=[0, ""], src=[["RFHL 2025 Annual Report", AR25]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "Small business", "blurb": "Packages, loans, cards.", "div": "rbl", "rev": "retail", "products": [
            P("sme", "Business packages & loans", "Current accounts with LINX/Visa point of sale, term loans, commercial mortgages, overdrafts, Side Hustle and agri-business loans, leasing and an SME toolkit; US$250 million of the new sustainable-finance goal is for women-led and farm SMEs.",
              s=["sme"], lc="borrow", neo=[0, ""], src=[["Republic: business packages", SMEPACK], ["RFHL sustainable finance, Sep 2026", ESG]]),
            P("bizcards", "Business & corporate cards", "International Visa Business card with cash back, and the Republic Bank/AAdvantage Corporate Mastercard with 5,000 enrolment miles.",
              s=["sme", "corp"], lc="borrow", o="P", at="Visa, Mastercard, American Airlines", neo=[1, "Visa Business; AAdvantage Corporate on Mastercard."],
              mc="One Mastercard commercial card; no virtual or fleet cards.",
              src=[["Republic: Visa Business", VISABIZ], ["Republic: AAdvantage Corporate Mastercard", CORPMC]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Corporate & investment", "blurb": "Lending, trade, bonds.", "div": "rbl", "rev": "retail", "products": [
            P("cib", "Corporate & investment banking", "Corporate lending, trade finance, bond arrangement and trustee services for companies and governments, led by Riah Dass-Mungal.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["RFHL 2025 Annual Report", AR25], ["Republic: commercial banking", COMMERCIAL]]),
        ]},
        {"id": "4.4", "ic": "coins", "name": "Wealth & insurance", "blurb": "Funds and digital life cover.", "div": "wealth", "rev": "ofs", "products": [
            P("funds", "Funds & retirement", "Republic Money Market, Caribbean Equity and US$ Fixed Income funds, retirement plans and tax-incentive savings plans; trust fees earned the group TT$345 million in FY2025.",
              s=["inv"], lc="grow", neo=[0, ""], src=[["Republic: mutual funds", FUNDS], ["RFHL 2025 Annual Report", AR25]]),
            P("life", "Republic Life & BalanceCover", "Republic Life Insurance's fully digital life platform (February 2024) added endowment and funeral cover in July 2025; BalanceCover repays a credit card balance on death or disability.",
              s=["inv", "con"], lc="grow", st="new", neo=[0, ""], src=[["RFHL 2025 Annual Report", AR25], ["Republic: BalanceCover", BALANCE]]),
        ]},
        {"id": "4.5", "ic": "globe", "name": "Regional banks", "blurb": "Caribbean and Ghana.", "div": "caribbean", "rev": "region", "products": [
            P("region", "Caribbean banks", "Banks in Barbados, Guyana, Grenada, the Eastern Caribbean, Suriname, the BVI and Cayman National; Barbados issues Visa credit cards.",
              s=["con", "corp"], lc="everyday", o="A", neo=[0, "Barbados on Visa."], src=[["RFHL 2025 Annual Report", AR25], ["Republic Barbados: credit cards", BARBADOS]]),
            P("bvi", "Mastercard Black (BVI)", "Republic Bank (BVI) launched a vertical Mastercard Black card with Mastercard in April 2024, with cash back, MasterAssist Black and luggage protection.",
              s=["travel"], lc="borrow", ay="Apr 2024", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Shows a group bank choosing Mastercard for its top tier.",
              src=[["Virgin Islands News: Mastercard Black, Apr 2024", BVI]]),
            P("ghana", "Republic Bank (Ghana)", "40 branches and 55 ATMs across Ghana, issuing Classic, Business, Infinite and Adeshie Visa credit cards.",
              s=["con"], div="ghana", lc="everyday", neo=[0, "Visa."], src=[["RFHL 2025 Annual Report", AR25], ["Republic Bank Ghana", GHANA]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Republic: RepublicOnline and the app, SMS banking, the country's largest branch and ATM network, and partners from American Airlines to the mobile operators.",
    "tiles": [
        {"id": "5.1", "ic": "monitor", "name": "RepublicOnline & app", "blurb": "P2P, wires, cardless cash.", "div": "rbl", "rev": "retail", "products": [
            P("online", "RepublicOnline & Republic Mobile", "Web and app banking with real-time registration, peer-to-peer payments, international wires, transfers to any local bank, cardless cash, card controls, a finance tracker and fingerprint log-in.",
              s=["con", "sme"], lc="everyday", o="B", neo=[0, ""], src=[["Republic: RepublicOnline", ONLINE]]),
            P("sms", "RepublicMobile SMS", "Balances, card payments and transfers by text to short code 8RBL on bmobile and Digicel.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["Republic: RepublicMobile", MOBILE]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "38 branches, 130 ATMs.", "div": "rbl", "rev": "retail", "products": [
            P("branches", "Branches & ATMs", "38 branches and 130 ATMs at 83 locations, the largest network in T&T; contactless ATMs from August 2023, cardless cash and EasiChange coin machines. ATMs take Visa and Mastercard credit cards.",
              s=["con"], lc="everyday", o="B", neo=[1, "ATMs accept Mastercard credit cards."], src=[["RFHL 2025 Annual Report", AR25], ["Republic: ATMs", ATMS]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partners", "blurb": "Airlines, retailers, telcos.", "div": "rbl", "rev": "retail", "products": [
            P("partners", "Partners & sponsorships", "American Airlines (AAdvantage), PriceSmart, insurers, bmobile and Digicel (Yooz), and title sponsor of AMCHAM T&T's Tech Hub Islands Summit (July 2024).",
              s=["con", "travel"], lc="beyond", o="P", neo=[0, ""], src=[["Republic: AAdvantage Mastercard", AAMC], ["Republic: Tech Hub Islands Summit, Jul 2024", THIS]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Republic", "blurb": "Half the credit range, no debit.", "products": [
        P("mcatrepublic", "Mastercard at Republic", "Mastercard carries about five of Republic's twelve T&T credit programmes, including the AAdvantage co-brand and Platinum, ran a Priceless Carnival campaign in 2024 and powers the BVI's Mastercard Black. Visa has every debit card (with LINX), the top tiers, prepaid, and the Barbados and Ghana books. Both networks paid incentives in FY2025.",
          s=["con"], div="rbl", rev="retail", mc="The relationship this map is drawn for.",
          src=[["Republic: credit cards", CARDS], ["RFHL 2025 Annual Report", AR25]]),
    ]},
    {"id": "pillar-market", "name": "T&T payments", "blurb": "LINX, UPI, e-money.", "products": [
        P("market", "The T&T market", "LINX carries domestic debit; cash is still widely used; a UPI-based instant-payment platform with NPCI International and a Payment Systems and Services Bill are coming; e-money issuers such as WamNow (2025) and Convenience Pay (2026) are being registered; US-dollar card spend is rationed.",
          s=["con"], div="rfhl", rev="group",
          src=[["Fintech Times: T&T payments, Sep 2026", UPI], ["Central Bank: WamNow, Nov 2025", WAMNOW], ["Central Bank: Convenience Pay, Jun 2026", CPAY]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
