"""National Commercial Bank Jamaica's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are NCB Financial Group's own unless a source says otherwise: the H1 FY2026 results (six months to
31 March 2026, released 7 May 2026) and the FY2025 results (year to 30 September 2025, released 13 November
2025), in Jamaican dollars. The Q3 FY2026 results were not found. ``neo`` is the Mastercard lens: [depth, note],
where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

H1 = "https://cdn.jamstockex.com/pd/2026/05/NCB-Financial-Group-Limited-NCBFG-Unaudited-Financial-Results-Six-Months-Ended-March-31-2026.pdf"
FY25 = "https://cdn.jamstockex.com/pd/2025/11/NCB-Financial-Group-Limited-NCBFG-Financial-Results-Year-Ended-September-30-2025.pdf"
GROUP = "https://www.ncbfinancialgrouplimited.com/about-us"
WHO = "https://www.jncb.com/about-us/who-we-are/"
MILESTONES = "https://www.jncb.com/about-us/milestones/"
MGMT = "https://www.jncb.com/about-us/management-team/"
BOARD = "https://www.jncb.com/about-us/board-of-directors/"
MARTIN = "https://www.jncb.com/about-us/news/ncbj-confirms-sheree-martin-as-chief-executive-officer/"
UPDATE = "https://www.jncb.com/about-us/news/ncb-update/"
LYNKCARD = "https://www.jncb.com/about-us/news/lynk-launches-virtual-card/"
CHEQUES = "https://www.jncb.com/about-us/news/ach-cheque-discontinuation-notice-for-ncb-website/"
REPO = "https://www.jncb.com/about-us/news/ncb-lists-2-billion-in-repossessed-properties-amid-post-melissa-loan-stress/"
SMEFUND = "https://www.jncb.com/about-us/news/ncb-returns-with-2-billion-sme-fund/"
CARDS = "https://www.jncb.com/personal/cards/all-cards/"
DEBIT = "https://www.jncb.com/personal/cards/ncb-visa-debit/"
PREPAID = "https://www.jncb.com/personal/cards/ncb-mastercard-prepaid/"
BIZCARDS = "https://www.jncb.com/business/cards/"
ACCEPT = "https://www.jncb.com/business/accept-payments/"
EPOS = "https://www.jncb.com/business/accept-payments/epos/"
PAYSMART = "https://www.jncb.com/business/accept-payments/paysmart/"
MOBILE = "https://www.jncb.com/personal/about-online-banking/mobile-banking/"
LOANS = "https://www.jncb.com/personal/loans/"
CORP = "https://www.jncb.com/business/financial-management/corporate-banking-solutions/"
LYNK = "https://lynk.us/"
DIGI25 = "https://www.jamaicaobserver.com/2025/05/25/ncb-pushing-ahead-digital-payment-initiatives/"
PAY23 = "https://jamaicaobserver.com/business/ncb-financial-expanding-payments-business"
MSME = "https://jamaicaobserver.com/2025/02/27/mastercard-partners-ncb-support-unbanked-msmes"
PREPAID21 = "https://jamaicaobserver.com/2021/04/20/ncb-launches-prepaid-mastercard"
KEYCARD = "https://www.jamaicaobserver.com/2020/11/12/ncb-commences-phasing-out-of-iconic-keycard"
MIDAS = "https://jamaicaobserver.com/2025/03/27/ncb-midas-cards-deactivated-monday"
MELISSA = "https://www.jamaicaobserver.com/2026/05/13/ncbfg-retools-storm-response-melissa/"
LEECHIN = "https://jamaica-gleaner.com/article/business/20250219/lee-chin-declares-commitment-ncb-ownership"
SAGICOR = "https://www.jamaicaobserver.com/2026/01/28/sagicor-bank-plans-apple-pay-introduction/"
CIBC = "https://www.jamaicaobserver.com/2026/06/09/cibc-caribbean-launches-google-pay-jamaica/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · owners · heritage", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: J$2.43 trillion of group assets and J$844 billion of deposits, Michael Lee-Chin's AIC as the largest owner, a bank dating from 1837, a turnaround strategy and the aftermath of Hurricane Melissa.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "J$2.43tn assets, ROE 7%.", "div": "ncbfg", "rev": "tw", "products": [
            P("balance", "Balance sheet & earnings", "Group assets of J$2.43 trillion, deposits of J$844 billion and loans of J$604.5 billion at 31 March 2026; net profit of J$10.3 billion in the half (annualised ROE 7.15%) and J$36.9 billion in FY2025, which included a J$15.1 billion disposal gain; NPL ratio 4.17%. Market cap and ratings not confirmed ⚠.",
              s=["inv"], neo=[0, ""], src=[["H1 FY2026 results", H1], ["FY2025 results", FY25]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Owners & leadership", "blurb": "Lee-Chin, Almeida, Martin.", "div": "ncbfg", "rev": "tw", "products": [
            P("owner", "Ownership & listing", "AIC (Barbados) owns 46.99% of NCB Financial Group (March 2026), with control through Michael Lee-Chin's Portland Holdings; listed in Kingston and Port of Spain. AIC's stake has fallen from 53% in 2019.",
              s=["inv"], neo=[0, ""], src=[["H1 FY2026 results", H1], ["Gleaner: Lee-Chin on ownership, Feb 2025", LEECHIN]]),
            P("leadership", "Board & executives", "Chairman Michael Lee-Chin, Group CEO Robert Almeida; Sheree Martin became NCBJ's CEO on 1 September 2026, the first woman in the role; Danielle Cameron Duncan runs Payments and Digital Channels.",
              s=["corp"], st="new", ay="Sep 2026", neo=[0, ""], src=[["NCBJ: Sheree Martin confirmed, Aug 2026", MARTIN], ["NCBJ: management team", MGMT], ["NCBJ: board", BOARD]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage", "blurb": "Since 1837.", "div": "ncbj", "rev": "csme", "products": [
            P("heritage", "Heritage", "The Colonial Bank opened in Kingston in 1837, later became Barclays' Jamaican bank and in 1977 National Commercial Bank Jamaica; NCB Financial Group became the holding company in 2016. 27 branches, 300+ ABMs and 2,000+ staff today.",
              s=["con"], o="I", neo=[0, ""], src=[["NCBJ: who we are", WHO], ["NCBJ: milestones", MILESTONES]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology", "blurb": "Cloud and a new website.", "div": "ncbfg", "rev": "tw", "products": [
            P("tech", "Cloud & digital platforms", "Cloud migration for resilience (FY2025), a rebuilt jncb.com with online card eligibility checks and pre-approved offers (2026), and digital loans paid out on approval. No public AI programme found ⚠.",
              s=["corp"], st="new", neo=[0, ""], src=[["FY2025 results", FY25], ["NCBJ: personal loans", LOANS]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & resilience", "blurb": "Turnaround after Melissa.", "div": "ncbfg", "rev": "tw", "products": [
            P("strategy", "Turnaround strategy", "Cost discipline (half-year expenses down 6%), centres of excellence across the group and growth in core banking, insurance and wealth; Almeida called FY2025 'a successful milestone' in the turnaround.",
              s=["corp"], neo=[0, ""], src=[["FY2025 results", FY25], ["H1 FY2026 results", H1]]),
            P("deals", "Deals & restructuring", "Sold the Netherlands insurance brokerage (J$15.1 billion gain, FY2025), issued US$225 million of senior secured notes (July 2025), and is moving NCB Cayman to Clarien and NCB Merchant Bank (Trinidad) to Guardian (2026, pending approval).",
              s=["inv"], st="flux", o="A", neo=[0, ""], src=[["FY2025 results", FY25], ["NCBJ: NCB update, May 2026", UPDATE]]),
            P("melissa", "Hurricane Melissa response", "Melissa crossed Jamaica on 28–31 October 2025. POS and online banking stayed up; NCB ran relief packages and took cash to customers; about US$129 million of group insurance claims were fully reinsured; about J$2 billion of repossessed property was listed in June 2026.",
              s=["con", "sme"], st="new", neo=[0, ""], src=[["Observer: storm response, May 2026", MELISSA], ["NCBJ: repossessed properties, Jun 2026", REPO], ["H1 FY2026 results", H1]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: Visa debit for every account since Midas closed, credit split between Mastercard and Visa, a Mastercard prepaid card, about 70% of the island's card terminals, the Lynk wallet and Jam-Dex, and clearing as cheques are phased out.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "All Visa since 2025.", "div": "ncbj", "rev": "pay", "products": [
            P("debit", "NCB Visa Debit", "Classic and Platinum EMV debit cards with NCB Miles, Visa Direct inbound transfers and Visa Concierge on Platinum. They replaced the Keycard (from 2020) and the Multilink Midas card, switched off on 31 March 2025.", short="Visa Debit",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."],
              mc="Mastercard has no debit at Jamaica's largest bank.",
              src=[["NCBJ: Visa Debit", DEBIT], ["Observer: Midas deactivated, Mar 2025", MIDAS], ["Observer: Keycard phase-out, Nov 2020", KEYCARD]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Mastercard travel, Visa cash back.", "div": "ncbj", "rev": "pay", "products": [
            P("mccredit", "NCB Mastercard credit cards", "Mastercard Standard in US dollars and Mastercard Platinum Travel in JMD and USD (NCB Miles, five lounge passes); a Mastercard Black in JMD and USD appears on NCB's card-interest form ⚠.", short="Mastercard credit",
              s=["con"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard holds NCB's travel and US-dollar cards.",
              src=[["NCBJ: credit and prepaid cards", CARDS], ["NCBJ: business cards", BIZCARDS]]),
            P("visacredit", "NCB Visa credit cards", "NCB Visa Classic (cash back, the starter card) and NCB Visa Platinum (up to 4% cash back, US$10,000 purchase protection).", short="Visa credit",
              s=["con"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["NCBJ: credit and prepaid cards", CARDS]]),
            P("bizcards", "Business credit cards", "NCB Business Elite and Executive Travel Business on Mastercard, NCB Visa Platinum Business on Visa, and NCB Business Edge (0.5% cash back; network not stated ⚠).",
              s=["sme", "corp"], lc="borrow", o="P", at="Mastercard, Visa", neo=[1, "Split Mastercard and Visa."], src=[["NCBJ: business cards", BIZCARDS]]),
            P("flexipay", "FlexiPay Biz", "Instalments on business credit cards: 0% for three months on purchases of J$100,000 or more, or 6 or 12 months at 15–20%.",
              s=["sme"], lc="borrow", neo=[1, "Rides on the card, Mastercard or other ⚠."], src=[["NCBJ: business cards", BIZCARDS]]),
        ]},
        {"id": "2.3", "ic": "wallet", "name": "Prepaid", "blurb": "Mastercard since 2021.", "div": "ncbj", "rev": "pay", "products": [
            P("prepaid", "NCB Mastercard Prepaid", "Launched in April 2021 for the underbanked: no fees, loaded at branches, online, by employers or through Mastercard Send and remittance providers, and usable at Cirrus ABMs worldwide.", short="Mastercard Prepaid",
              s=["con", "unb"], lc="open", ay="Apr 2021", o="P", at="Mastercard", neo=[2, "Mastercard."],
              src=[["NCBJ: Mastercard Prepaid", PREPAID], ["Observer: prepaid Mastercard, Apr 2021", PREPAID21]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Acquiring", "blurb": "About 70% of POS.", "div": "ncbj", "rev": "pay", "products": [
            P("acquiring", "NCB Merchant Services", "About 70% of Jamaica's POS terminals (February 2025), taking every major brand including Amex, with JMD and USD settlement and card payments at Highway 2000 tolls since March 2024. Payment Services earned revenue of J$39.0 billion in FY2025.",
              s=["mer", "sme"], lc="move", neo=[1, "Accepts every network."],
              src=[["Observer: digital payments, May 2025", DIGI25], ["NCBJ: accept payments", ACCEPT], ["FY2025 results", FY25]]),
            P("epos", "NCB ePOS (Tap on Phone)", "An Android phone becomes a contactless terminal ('Powered by Fasstap'), launched June 2024 at J$500 a month plus fees.",
              s=["mer", "sme"], lc="move", o="P", at="Fasstap", neo=[1, "Accepts every network."], src=[["NCBJ: ePOS", EPOS], ["Observer: digital payments, May 2025", DIGI25]]),
            P("mcmsme", "Mastercard MSME programme", "Mastercard supplies smartphones running NCB's payment platform to unbanked micro and small merchants, free to them, with settlement into NCB accounts; announced February 2025, NCB the only bank 'so far'.", short="Mastercard MSME phones",
              s=["mer"], lc="open", st="new", ay="Feb 2025", o="P", at="Mastercard", neo=[1, "Mastercard-backed; accepts every network."],
              mc="The one joint acceptance programme on record.",
              src=[["Observer: Mastercard and NCB, Feb 2025", MSME]]),
            P("ecom", "E-commerce, links & QR", "Website checkout, payment links and QR (vPOS) payments, with Fygaro for small-business e-commerce.",
              s=["mer", "sme"], lc="move", o="P", at="Fygaro", neo=[1, "Accepts every network."], src=[["NCBJ: accept payments", ACCEPT], ["Observer: digital payments, May 2025", DIGI25]]),
            P("paysmart", "PaySmart", "Bill-payment collection: customers pay a business from NCB accounts or credit cards through online banking, the app or IVR.",
              s=["mer", "corp"], lc="move", neo=[0, ""], src=[["NCBJ: PaySmart", PAYSMART]]),
        ]},
        {"id": "2.5", "ic": "smartphone", "name": "Wallets & Jam-Dex", "blurb": "Lynk, NCB Pay, CBDC.", "div": "lynk", "rev": "pay", "products": [
            P("lynk", "Lynk", "NCB's wallet company (TFOB), launched December 2021: transfers, 300+ billers, top-ups, Western Union and MoneyGram remittances and cardless cash at NCB ABMs, for close to 300,000 users (April 2026).",
              s=["unb", "mer"], lc="everyday", neo=[0, "Own wallet."], src=[["NCBJ: Lynk virtual card, Apr 2026", LYNKCARD], ["Lynk", LYNK]]),
            P("lynkcard", "Lynk Virtual Card", "A virtual card inside Lynk, 'Powered by Visa', for online, subscription and tap-to-pay spending without a bank account; soft launch February 2026, launched 9 April 2026.", short="Lynk card (Visa)",
              s=["unb"], lc="open", st="new", ay="Apr 2026", o="P", at="Visa", neo=[0, "Visa."],
              mc="The inclusion card went to Visa, not Mastercard.",
              src=[["NCBJ: Lynk virtual card, Apr 2026", LYNKCARD]]),
            P("ncbpay", "NCB Pay", "NCB's own phone wallet (March 2023) for contactless payment with NCB Visa credit, Mastercard credit and prepaid cards, on Android only ⚠ current status.",
              s=["con"], lc="everyday", ay="Mar 2023", neo=[1, "Visa and Mastercard cards."],
              mc="Rivals are bringing Apple Pay and Google Pay; tokenisation is open ground.",
              src=[["Observer: payments business, Feb 2023", PAY23], ["Observer: Sagicor and Apple Pay, Jan 2026", SAGICOR]]),
            P("jamdex", "Jam-Dex", "The Bank of Jamaica's CBDC (July 2022); Lynk was the first wallet for it and is one of two public ones. About J$260 million was in circulation in December 2025.",
              s=["unb", "mer"], lc="move", o="P", at="Bank of Jamaica", neo=[0, ""], src=[["Observer: Sagicor and Apple Pay, Jan 2026", SAGICOR], ["Observer: digital payments, May 2025", DIGI25]]),
        ]},
        {"id": "2.6", "ic": "arrow-left-right", "name": "Clearing & remittances", "blurb": "Cheques end in 2028.", "div": "ncbj", "rev": "ccb", "products": [
            P("clearing", "RTGS, ACH & cheques", "From 1 September 2026 NCB no longer clears cheques of J$1 million or more through the national system, and all cheque clearing ends on 1 March 2028; businesses are steered to RTGS, ACH credits and digital payments.",
              s=["sme", "corp"], lc="move", st="flux", ay="Sep 2026", neo=[0, ""],
              mc="Businesses leaving cheques need digital payables.",
              src=[["NCBJ: cheque discontinuation, Jul 2026", CHEQUES]]),
            P("remit", "Remittances & correspondent flows", "Visa Direct into Visa debit accounts, Western Union and MoneyGram into Lynk, and a US$250 million securitisation of inbound correspondent payments (2020, to 2030).",
              s=["con", "unb"], lc="move", neo=[0, "Visa Direct; Western Union, MoneyGram."], src=[["NCBJ: Visa Debit", DEBIT], ["H1 FY2026 results", H1]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every card and account: chip-and-PIN security and card self-service, NCB Miles rewards on Visa debit and Mastercard credit, and digital loans paid out in minutes.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "EMV and PCI.", "div": "ncbj", "rev": "pay", "products": [
            P("fraud", "Fraud & card security", "EMV chip and PIN on all cards, a security centre, a PCI DSS programme for merchants and online dispute and blocking tools. No network fraud tools are named in public ⚠.",
              s=["con", "mer"], lc="everyday", neo=[None, "Nothing public."],
              mc="Credit stress after Melissa and growing e-commerce make fraud scoring a fit.",
              src=[["NCBJ: accept payments", ACCEPT], ["NCBJ: Visa Debit", DEBIT]]),
        ]},
        {"id": "3.2", "ic": "gift", "name": "NCB Miles", "blurb": "Rewards on both networks.", "div": "ncbj", "rev": "pay", "products": [
            P("miles", "NCB Miles & rewards", "Points on Visa debit and Mastercard Platinum Travel credit, redeemed for flights, hotels and car rentals, plus a virtual rewards card for phone wallets ⚠ network not stated. Reward and loyalty costs rose in FY2025.",
              s=["con"], lc="grow", neo=[1, "Visa debit and Mastercard credit."],
              src=[["NCBJ: Visa Debit", DEBIT], ["NCBJ: credit and prepaid cards", CARDS], ["FY2025 results", FY25]]),
        ]},
        {"id": "3.3", "ic": "gauge", "name": "Digital lending", "blurb": "Paid out on approval.", "div": "ncbj", "rev": "csme", "products": [
            P("digiloans", "Digital loans & offers", "Unsecured digital loans from J$100,000 to J$5 million, some paid out instantly, with pre-approved offers online; changes to the digital loan range cut fee income in late 2025.",
              s=["con"], lc="borrow", st="new", neo=[0, ""], src=[["NCBJ: personal loans", LOANS], ["H1 FY2026 results", H1]]),
        ]},
        {"id": "3.4", "ic": "headset", "name": "Card servicing", "blurb": "Manage my card.", "div": "ncbj", "rev": "pay", "products": [
            P("servicing", "Card management", "Activation, disputes, lost-card reports and replacements at managemycard.jncb.com; online eligibility checks and application tracking.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["NCBJ: credit and prepaid cards", CARDS]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: consumer and SME banking, corporate and government banking, treasury and NCB Capital Markets, Guardian insurance and pensions, and Clarien in Bermuda.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Consumer & SME", "blurb": "J$66bn revenue.", "div": "ncbj", "rev": "csme", "products": [
            P("retail", "Accounts, mortgages & loans", "Savings and current accounts with Visa debit, mortgages, auto and refreshed EV loans; the Consumer & SME segment had revenue of J$66.1 billion in FY2025.",
              s=["con"], lc="everyday", neo=[0, "Visa debit."], src=[["FY2025 results", FY25]]),
            P("smefund", "SME Growth Fund II", "J$2 billion for small businesses, loans up to J$35 million from 9.75%, April to June 2026, doubled after the first fund ran out.",
              s=["sme"], lc="borrow", st="new", ay="Apr 2026", neo=[0, ""], src=[["NCBJ: SME fund, Apr 2026", SMEFUND]]),
        ]},
        {"id": "4.2", "ic": "building-2", "name": "Corporate & commercial", "blurb": "Structured finance, FX.", "div": "ncbj", "rev": "ccb", "products": [
            P("corporate", "Corporate banking", "Structured finance, deposits, FX, merchant services and credit cards for large companies and government; segment revenue J$23.9 billion in FY2025.",
              s=["corp"], lc="borrow", neo=[0, ""],
              mc="Commercial cards for corporates and government are open as cheques end.",
              src=[["NCBJ: corporate banking", CORP], ["FY2025 results", FY25]]),
        ]},
        {"id": "4.3", "ic": "chart-candlestick", "name": "Treasury & wealth", "blurb": "NCB Capital Markets.", "div": "ncbcm", "rev": "tw", "products": [
            P("treasury", "Treasury & correspondent banking", "Liquidity, investments and correspondent banking; investment securities of J$1.29 trillion at March 2026.",
              s=["corp"], lc="grow", neo=[0, ""], src=[["H1 FY2026 results", H1]]),
            P("wealth", "NCB Capital Markets", "Brokerage, asset management and corporate advisory, with group investment management centralised there in FY2025.",
              s=["inv"], lc="grow", neo=[0, ""], src=[["NCBFG: about us", GROUP], ["FY2025 results", FY25]]),
        ]},
        {"id": "4.4", "ic": "hand-coins", "name": "Insurance & pensions", "blurb": "Guardian, 21 markets.", "div": "guardian", "rev": "ins", "products": [
            P("insurance", "Guardian Group & pensions", "Life, health, property and casualty insurance and pensions across 21 Caribbean markets; insurance service result J$15.1 billion in the half, with Melissa claims fully reinsured.",
              s=["inv"], lc="grow", neo=[0, ""], src=[["NCBFG: about us", GROUP], ["H1 FY2026 results", H1]]),
        ]},
        {"id": "4.5", "ic": "globe", "name": "International", "blurb": "Clarien, Cayman.", "div": "clarien", "rev": "ccb", "products": [
            P("clarien", "Clarien & NCB Cayman", "Clarien in Bermuda (personal, commercial and private banking, wealth, trust) and NCB Cayman, which is moving under Clarien (pending approval).",
              s=["inv", "corp"], lc="grow", st="flux", neo=[None, "Card networks not checked."], src=[["NCBFG: about us", GROUP], ["NCBJ: NCB update, May 2026", UPDATE]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach NCB: the mobile app and online banking, 27 branches and 300-plus ABMs, and digital onboarding and the merchant portal.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "NCB Mobile app", "blurb": "No data charges.", "div": "ncbj", "rev": "csme", "products": [
            P("app", "NCB Mobile app", "Balances, transfers to any bank, bill and card payments, with soft tokens and no data charges.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["NCBJ: mobile banking", MOBILE]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Online banking", "blurb": "Personal and business.", "div": "ncbj", "rev": "csme", "products": [
            P("online", "NCB Online Banking", "Personal and business online banking, used for card loads, PaySmart bills and transfers.",
              s=["con", "sme", "corp"], lc="everyday", neo=[0, ""], src=[["NCBJ: PaySmart", PAYSMART], ["NCBJ: Mastercard Prepaid", PREPAID]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & ABMs", "blurb": "27 branches, 300+ ABMs.", "div": "ncbj", "rev": "csme", "products": [
            P("branches", "Branches & ABMs", "27 branches and more than 300 ABMs, about a third of the island's machines, with cardless cash for Lynk users.",
              s=["con", "unb"], lc="everyday", neo=[0, ""], src=[["NCBJ: who we are", WHO], ["Observer: digital payments, May 2025", DIGI25]]),
        ]},
        {"id": "5.4", "ic": "log-in", "name": "Onboarding & portals", "blurb": "Apply online.", "div": "ncbj", "rev": "pay", "products": [
            P("onboard", "Digital onboarding", "Online card eligibility checks, pre-approved card and loan offers and application tracking on jncb.com.",
              s=["con"], lc="open", st="new", neo=[0, ""], src=[["NCBJ: credit and prepaid cards", CARDS], ["NCBJ: personal loans", LOANS]]),
            P("merchantportal", "Merchant Portal", "Transaction tracking, reports and user control for ePOS and POS merchants.",
              s=["mer"], lc="move", neo=[0, ""], src=[["NCBJ: ePOS", EPOS]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at NCB", "blurb": "Credit and prepaid; debit is Visa.", "products": [
        P("mcatncb", "Mastercard at NCB", "Mastercard carries NCB's prepaid card (2021), the travel and US-dollar credit cards and two business cards, and backs a 2025 acceptance programme for unbanked merchants. Visa carries all debit since Midas closed in March 2025, the cash-back credit cards, Visa Direct and, from 2026, the Lynk virtual card.",
          s=["con"], div="ncbj", rev="pay", mc="The relationship this map is drawn for.",
          src=[["NCBJ: credit and prepaid cards", CARDS], ["Observer: Mastercard and NCB, Feb 2025", MSME], ["NCBJ: Lynk virtual card, Apr 2026", LYNKCARD]]),
    ]},
    {"id": "pillar-market", "name": "Jamaican payments", "blurb": "Cash, CBDC, wallets.", "products": [
        P("market", "The Jamaican market", "Nearly four-fifths of transactions were still cash in 2025; 3.8 million JMD debit cards and about 437,000 JMD credit cards (May 2025); Jam-Dex since 2022; cheques phased out by 2028; CIBC launched Google Pay in June 2026 and Scotia and Sagicor plan Apple Pay.",
          s=["con"], div="ncbfg", rev="pay", src=[["Observer: Sagicor and Apple Pay, Jan 2026", SAGICOR], ["Observer: CIBC Google Pay, Jun 2026", CIBC], ["Observer: digital payments, May 2025", DIGI25]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
