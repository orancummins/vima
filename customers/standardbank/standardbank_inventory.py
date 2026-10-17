"""Standard Bank Group's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the 2026 interim results (13 August 2026) and the
Capital Markets Day (26 March 2026). Card networks for South African personal products are read from the card
art on Standard Bank's own product pages on 17 October 2026. ``neo`` is the Mastercard lens: [depth, note],
where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

HY26 = "https://www.standardbank.com/file_source/Investor%20Relations/Documents/Financial-results/Interim-Results/SBG-2026-Interim-Results-Booklet.pdf"
SENS26 = "https://careers.standardbank.com/file_source/Investor%20Relations/Documents/Financial-results/Interim-Results/SBG-2026-Interim-Results-SENS-Short-Form-and-Dividend-Declaration.pdf"
CMD = "https://www.standardbank.com/static_file/Investor%20Relations/CMD_2026/downloadable%20files/Capital%20Markets%20Day%20Script%20consolidated.pdf"
LEAD = "https://www.standardbank.com/sbg/standard-bank-group/our-group/about-us/leadership"
CARDS = "https://www.standardbank.co.za/southafrica/personal/products-and-services/bank-with-us/credit-cards/compare-cards"
ACCTS = "https://www.standardbank.co.za/southafrica/personal/products-and-services/bank-with-us/bank-accounts/our-accounts"
MYMO = "https://www.standardbank.co.za/southafrica/personal/products-and-services/bank-with-us/bank-accounts/our-accounts/mymo-account"
PRESTIGE = "https://www.standardbank.co.za/southafrica/personal/products-and-services/bank-with-us/bank-accounts/our-accounts/prestige-banking-account"
CORP = "https://www.standardbank.co.za/southafrica/business/products-and-services/bank-with-us/company-cards/our-cards"
FLEET = "https://www.standardbank.co.za/southafrica/business/products-and-services/business-solutions/fleet-management/visa-fleet-card"
PAYCARD = "https://www.standardbank.co.za/southafrica/business/products-and-services/business-solutions/workplace-solutions/paycard"
TAP = "https://www.standardbank.co.za/southafrica/personal/learn/different-ways-to-tap-and-pay"
APPLE = "https://www.standardbank.co.za/southafrica/personal/products-and-services/ways-to-bank/innovative-payment-solutions/apple-pay"
MPASS = "https://www.standardbank.co.za/southafrica/personal/products-and-services/ways-to-bank/innovative-payment-solutions/masterpass"
SNAP = "https://www.standardbank.co.za/southafrica/personal/products-and-services/ways-to-bank/innovative-payment-solutions/snapscan"
WALLETS = "https://www.standardbank.co.za/southafrica/personal/products-and-services/bank-with-us/digital-wallets"
SHYFT = "https://www.shyft.co.za/cards"
VISASHYFT = "https://usa.visa.com/content/dam/VCOM/global/solutions/documents/standard-bank-case-study.pdf"
MC2013 = "https://www.retailbankerinternational.com/news/standard-bank-signs-five-year-deal-with-mastercard/"
MCSME = "https://newsroom.mastercard.com/news/eemea/en/newsroom/press-releases/en/2020/october/standard-bank-mastercard-and-google-collaborate-to-help-smes-open-their-digital-doors-and-reach-more-customers/"
MCGW = "https://www.mastercard.com/gateway/expertise/case-studies/standard-bank.html"
MCZAP = "https://www.mastercard.com/news/eemea/en/newsroom/press-releases/en/2018/august/mastercard-and-zapper-collaborate-to-drive-digital-payments-interoperability/"
SAMSUNG = "https://news.samsung.com/za/samsung-pay-now-available-to-standard-bank-mastercard-debit-customers"
VCARD = "https://businesstech.co.za/news/banking/262777/standard-bank-launches-new-virtual-card-system-and-samsung-pay-support/"
UPI25 = "https://prnewswire.co.uk/news-releases/standard-bank-and-unionpay-strengthen-long-standing-partnership-to-drive-digital-payment-innovations-in-africa-302424465.html"
UPI26 = "https://www.engineeringnews.co.za/article/standard-bank-and-unionpay-unlock-cross-border-e-commerce-opportunities-for-merchants-across-nine-african-markets-2026-08-19"
UPI24 = "https://itweb.co.za/article/standard-bank-unionpay-international-ink-partnership-deal/GxwQDq1AXZyqlPVo"
PSSB = "https://standardbank.co.za/southafrica/news-and-media/newsroom/standard-bank-sees-tenfold-surge-in-payshap-id-transactions-as-instant-payments-gain-traction"
STITCH = "https://stitch.money/blog/real-time-payments-in-south-africa-the-state-of-payshap-in-2026"
NPS = "https://www.resbank.co.za/content/dam/sarb/publications/media-releases/2026/nps-transition.pdf"
PASA = "https://thecondia.com/south-africa-dissolves-pasa-payinc-sarb/"
DCS = "https://www.resbank.co.za/content/dam/sarb/what-we-do/payments-and-settlements/regulation-oversight-and-supervision/document-for-comments/Domestic%20scheme%20feasibility%20paper%20-%20version%20sent%20to%20stakeholders%20-%201%20March%202021.pdf"
SABRIC = "https://www.sabric.co.za/?p=4450"
SABRICBT = "https://businesstech.co.za/news/banking/872745/alarm-bells-for-anyone-with-banking-apps-on-their-phones-in-south-africa/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · ownership · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Africa's largest bank, with R3.8 trillion of assets, 19.5 million active clients in 21 African countries, ICBC as its biggest shareholder, a cloud and AI platform, and 2028 targets set in March 2026.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "R26.1bn earned in H1, ROE 19.8%.", "div": "sbg", "rev": "group", "products": [
            P("balance", "Balance sheet & earnings", "Headline earnings of R26.1 billion in the six months to 30 June 2026 (up 10%), ROE 19.8%, CET1 13.6%, total assets R3.81 trillion and deposits R2.5 trillion; R49.2 billion and ROE 19.3% in 2025. South Africa made 51% of earnings, Africa Regions 40%. Market value about R532 billion (US$32 billion).",
              s=["corp"], neo=[0, ""], src=[["2026 interim results booklet", HY26], ["2026 interim results announcement", SENS26]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership & ownership", "blurb": "Tshabalala; ICBC holds 19.7%.", "div": "sbg", "rev": "group", "products": [
            P("leadership", "Board & leadership council", "Chairman Nonkululeko Nyembezi, Group CEO Sim Tshabalala, CFO Arno Daehnke, SBSA CEO David Hodnett, COO Margaret Nienaber (technology, AI and payments), Funeka Montjane (PPB), Bill Blackie (BCB), Luvuyo Masinda (CIB), Lungisa Fuzile (Africa Regions and Offshore) and Yuresh Maharaj (Insurance & Asset Management).",
              s=["corp"], neo=[0, ""], src=[["Standard Bank: leadership", LEAD], ["2026 interim results booklet", HY26]]),
            P("owners", "Ownership, heritage & ICBC", "Listed on the JSE (SBK). ICBC holds 19.7% and the Government Employees Pension Fund 14.3%; the group owns 40% of ICBC Standard Bank in London. A 163-year heritage, starting with wool-trade finance in the Eastern Cape (founded 1862 ⚠); 51,200 employees.",
              s=["corp"], o="I", neo=[0, ""], src=[["2026 interim results booklet", HY26], ["Capital Markets Day, Mar 2026", CMD]]),
        ]},
        {"id": "1.3", "ic": "database", "name": "Technology & AI", "blurb": "R23.5bn tech spend; 72% use GenAI.", "div": "sbg", "rev": "group", "products": [
            P("tech", "Cloud, card modernisation & AI", "R23.5 billion of technology spend in 2025 (27.7% of costs), 78% of migratable compute in the cloud, and card modernisation among the current programmes. 72% of staff use generative AI, with 87 approved use cases; first in Africa in the Evident AI Index (June 2026).",
              s=["corp"], st="new", neo=[0, ""],
              mc="Card modernisation is a re-platforming window for issuing and tokens.",
              src=[["Capital Markets Day, Mar 2026", CMD], ["2026 interim results booklet", HY26]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "2028 strategy & deals", "blurb": "HEPS +8–12% a year to 2028.", "div": "sbg", "rev": "group", "products": [
            P("strategy", "2028 targets", "Set at the Capital Markets Day on 26 March 2026: HEPS growth of 8–12% a year, ROE of 18–22%, CET1 above 12.5% and a 45–60% payout, with technology, AI and payments as the three investment pillars.",
              s=["corp"], st="new", ay="Mar 2026", neo=[0, ""], src=[["Capital Markets Day, Mar 2026", CMD], ["2026 interim results announcement", SENS26]]),
            P("deals", "Deals", "Bought out Liberty's minorities in 2022 (about R16 billion upstreamed since); more capital into Standard Bank Tanzania (July 2026), a larger stake in Standard Bank Angola due in the second half of 2026, and a Cairo office ahead of Egypt.",
              s=["corp", "afr"], o="A", st="flux", neo=[0, ""], src=[["Capital Markets Day, Mar 2026", CMD], ["2026 interim results announcement", SENS26]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Eight ways money moves: Mastercard credit and mass-market debit cards, Visa for Private Banking and fleet, Diners Club of its own, R129 billion of card acquiring in a half, PayShap and Instant Money, Shyft and SWIFT cross-border, and a first stablecoin.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Credit & charge cards", "blurb": "Mastercard, plus its own Diners Club.", "div": "sbsa", "rev": "ppb", "products": [
            P("credit", "Blue, Gold, Titanium & Platinum credit cards", "Every personal credit card on Standard Bank's site carries Mastercard (October 2026): Blue, Gold (with Priceless car-rental offers), Titanium and Private Banking Platinum. The PPB card book was R33.3 billion at June 2026, and card turnover grew 16%. Up to 55 days interest-free; virtual card linked.", short="Credit cards (Mastercard)",
              s=["con", "priv"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard on current card art ⚠."],
              mc="The core of Mastercard's place at Standard Bank.",
              src=[["Standard Bank: compare credit cards", CARDS], ["2026 interim results booklet", HY26], ["Capital Markets Day, Mar 2026", CMD]]),
            P("worldcitizen", "World Citizen credit card", "The top personal card, a World Mastercard: unlimited lounge access, up to 40% off flights with Standard Bank Travel, travel insurance, and Mastercard Medical Tourism Services discounts.", short="World Citizen (World Mastercard)",
              s=["priv", "glob"], lc="borrow", o="P", at="Mastercard", neo=[2, "World Mastercard."],
              src=[["Standard Bank: compare credit cards", CARDS]]),
            P("diners", "Diners Club South Africa", "A wholly owned SBSA subsidiary that issues and acquires Diners Club cards under a franchise from Diners Club International: Diners Club Platinum, Beyond credit cards and a Shari'ah charge card with ClubMiles rewards.", short="Diners Club (own scheme)",
              s=["priv"], lc="borrow", at="Diners Club International", neo=[0, "Diners Club."], src=[["SARB: domestic card scheme paper, Mar 2021", DCS], ["Standard Bank: compare credit cards", CARDS]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Debit & cheque cards", "blurb": "MyMo on Mastercard, Private on Visa.", "div": "sbsa", "rev": "ppb", "products": [
            P("debit", "MyMo, Achieva & Consolidator cards", "The mass and middle-market cards for about 12 million active South African clients carry Mastercard on current card art; MyMo was voted Product of the Year 2025. Samsung Pay has been available for Mastercard debit since August 2019.", short="Debit (Mastercard)",
              s=["con"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard on current card art ⚠."],
              src=[["Standard Bank: bank accounts", ACCTS], ["Standard Bank: MyMo account", MYMO], ["Samsung: Pay for Standard Bank Mastercard debit, Aug 2019", SAMSUNG]]),
            P("privdebit", "Private & Professional banking cards", "Private Banking and Professional banking account cards carry Visa; the Prestige account comes with Titanium Mastercard credit.", short="Private debit (Visa)",
              s=["priv"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."],
              mc="Visa holds the top of the transactional franchise.",
              src=[["Standard Bank: bank accounts", ACCTS], ["Standard Bank: Prestige Banking", PRESTIGE]]),
        ]},
        {"id": "2.3", "ic": "briefcase-business", "name": "Commercial & prepaid cards", "blurb": "Clients choose Mastercard or Visa.", "div": "sbsa", "rev": "bcb", "products": [
            P("corpcards", "Corporate, travel & procurement cards", "Corporate credit, charge, travel, procurement and aviation cards, where clients choose between Mastercard and Visa.",
              s=["sme", "corp"], lc="move", o="P", at="Mastercard, Visa", neo=[1, "Mastercard or Visa."], src=[["Standard Bank: business cards", CORP]]),
            P("fleet", "Fleet & garage cards", "A Visa Fleet Card with chip and PIN for fuel and vehicle costs ⚠.",
              s=["sme", "corp"], lc="move", o="P", at="Visa", neo=[0, "Visa."],
              mc="Fleet sits with Visa.",
              src=[["Standard Bank: Visa Fleet Card", FLEET]]),
            P("paycard", "PayCard prepaid payroll", "Mastercard or Visa prepaid cards for paying staff, usable only in South Africa ⚠.",
              s=["sme", "cash"], lc="move", o="P", at="Mastercard, Visa", neo=[1, "Mastercard or Visa."], src=[["Standard Bank: PayCard", PAYCARD]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Merchant acquiring", "blurb": "R129bn of card turnover in a half.", "div": "sbsa", "rev": "bcb", "products": [
            P("acquiring", "Card acquiring", "Card acquiring turnover of R129 billion in the first half of 2026 (R98 billion in South Africa, up 5%, with new merchants up 28%; R30 billion in Africa Regions). A growth priority to 2028.",
              s=["sme"], lc="move", st="active", neo=[1, "Accepts every network."],
              mc="Acquirer risk and acceptance tools have a growing book to work on.",
              src=[["2026 interim results booklet", HY26], ["Capital Markets Day, Mar 2026", CMD]]),
            P("simplyblu", "SimplyBlu", "An e-commerce store builder and checkout for small businesses, launched in June 2019 on Mastercard Payment Gateway Services; Mastercard and Google added free access and Google Ads in October 2020. New merchant sales grew 19% in 2025.", short="SimplyBlu (Mastercard Gateway)",
              s=["sme"], lc="move", ay="Jun 2019", o="P", at="Mastercard", neo=[3, "Mastercard Gateway runs it."],
              src=[["Mastercard: Standard Bank, Mastercard and Google, Oct 2020", MCSME], ["Mastercard Gateway: SimplyBlu case study", MCGW], ["Capital Markets Day, Mar 2026", CMD]]),
            P("snapscan", "SnapScan", "QR payments and a wallet at more than 50,000 merchants, earning UCount points, working with most bank cards.",
              s=["con", "sme"], lc="move", neo=[1, "Card-agnostic."], src=[["Standard Bank: SnapScan", SNAP], ["Standard Bank: digital wallets", WALLETS]]),
            P("unionpay", "UnionPay acceptance & issuing", "UnionPay cards accepted at all South African ATMs and POS. The partnership dates from about 2010 and was renewed in Shanghai in April 2025; UnionPay e-commerce acceptance followed in nine more African markets in August 2026 ⚠.",
              s=["sme", "afr"], lc="move", st="new", ay="Apr 2025", o="P", at="UnionPay International", neo=[0, "UnionPay."],
              mc="The network with the fresh announcements is UnionPay.",
              src=[["PR Newswire: Standard Bank and UnionPay, Apr 2025", UPI25], ["Engineering News: nine markets, Aug 2026", UPI26], ["ITWeb: UnionPay deal, Jan 2024", UPI24]]),
        ]},
        {"id": "2.5", "ic": "smartphone", "name": "Wallets & tokens", "blurb": "Apple Pay, Samsung Pay, Masterpass.", "div": "sbsa", "rev": "ppb", "products": [
            P("tokens", "Phone & wearable payments", "Apple Pay, Samsung Pay, Garmin Pay, and tap-to-pay in the Android banking app, which is open only to Standard Bank Mastercard cheque and credit cardholders.",
              s=["con"], lc="everyday", o="P", at="Apple, Samsung, Garmin", neo=[1, "In-app tap is Mastercard-only."],
              src=[["Standard Bank: ways to tap and pay", TAP], ["Standard Bank: Apple Pay", APPLE]]),
            P("masterpass", "Masterpass", "Still offered as Standard Bank's online checkout wallet in 2026: register any South African bank card and pay by QR or in-app.", short="Masterpass (Mastercard)",
              s=["con"], lc="everyday", ay="2018", o="P", at="Mastercard", neo=[3, "Mastercard's own."],
              mc="An older Mastercard wallet; Click to Pay is its successor.",
              src=[["Standard Bank: Masterpass", MPASS], ["Mastercard: Masterpass interoperability, Aug 2018", MCZAP]]),
            P("virtualcard", "Virtual cards", "A virtual card created and topped up in the app since 2018, which can be co-branded with Takealot, Zando and Travelstart, and a virtual credit card linked to each credit card.",
              s=["con"], lc="everyday", ay="2018", neo=[None, "Network not stated."], src=[["BusinessTech: virtual card, 2018", VCARD], ["Standard Bank: compare credit cards", CARDS]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Instant & account payments", "blurb": "PayShap, Instant Money, FlexiPay.", "div": "sbsa", "rev": "ppb", "products": [
            P("payshap", "PayShap", "A launch bank for South Africa's real-time rail (March 2023, run by PayInc, formerly BankservAfrica). ShapID use rose 817% in a year to October 2024, and PayShap Request followed in December 2024. In 2026 Standard Bank began routing low-value payments to PayShap automatically. Industry: about 45 million payments a month, R50,000 cap.",
              s=["con", "sme"], lc="move", st="new", ay="Mar 2023", o="P", at="PayInc", neo=[0, "Account-to-account."],
              mc="Low-value everyday payments are moving off cards and onto PayShap.",
              src=[["Standard Bank: PayShap ID surge, Oct 2024", PSSB], ["2026 interim results booklet", HY26], ["Stitch: PayShap in 2026", STITCH]]),
            P("instantmoney", "Instant Money", "Cash-send to people without a bank account, through the app, USSD and retail partners: R23.4 billion in the first half of 2026, with 2.5 million platform clients.",
              s=["cash"], lc="move", o="B", neo=[0, "Bank's own rail."], src=[["2026 interim results booklet", HY26]]),
            P("debicheck", "Debit orders & DebiCheck", "Collections on PayInc's authenticated-collections rail; DebiCheck volumes fell in the first half of 2026.",
              s=["sme"], lc="move", o="P", at="PayInc", neo=[0, ""], src=[["2026 interim results booklet", HY26], ["SARB: NPS transition, Aug 2026", NPS]]),
            P("flexipay", "FlexiPay & mobile money", "Mobile money in Africa Regions: FlexiPay in Uganda (transactions up 99% to R7 billion), with PayPulse and @Ease elsewhere.",
              s=["afr"], lc="move", o="B", neo=[0, ""], src=[["Capital Markets Day, Mar 2026", CMD], ["2026 interim results booklet", HY26]]),
        ]},
        {"id": "2.7", "ic": "earth", "name": "Cross-border & FX", "blurb": "30% of SA cross-border; Shyft.", "div": "shyft", "rev": "cib", "products": [
            P("shyft", "Shyft", "A global money app for South Africa and Botswana: ZAR, USD, GBP, EUR and AUD wallets, US shares, physical cards (Mastercard in app imagery ⚠, plus a UnionPay card) and virtual cards. FX and payments are built on Visa Cross-Border Solutions (Currencycloud).", short="Shyft (Visa rails)",
              s=["glob"], lc="move", o="P", at="Visa Cross-Border Solutions", neo=[1, "Mastercard cards ⚠ on Visa's cross-border rails."],
              mc="Visa's plumbing sits under the group's consumer FX app.",
              src=[["Shyft: cards", SHYFT], ["Visa: Shyft case study, 2023", VISASHYFT]]),
            P("crossborder", "Cross-border payments", "Shares of 30% of South Africa's cross-border payments and 19% across Africa. It was the first African bank on China's CIPS (R9.5 billion since late 2025), launched a global remittances platform in 2025, and plans Blue-to-Blue real-time settlement across the network for 2026.",
              s=["corp", "afr"], lc="move", st="new", neo=[0, "SWIFT and CIPS."],
              mc="Remittances and intra-network settlement are open ground for Mastercard Move.",
              src=[["2026 interim results booklet", HY26], ["Capital Markets Day, Mar 2026", CMD]]),
        ]},
        {"id": "2.8", "ic": "coins", "name": "Digital assets", "blurb": "ZARU stablecoin, Aroko rails.", "div": "sbg", "rev": "cib", "products": [
            P("digitalassets", "Stablecoins & tokenised deposits", "Supported the launch of ZARU, a rand stablecoin; builds regulated on- and off-ramps, custody and tokenised deposits. CIB's Aroko blockchain rails have carried more than R1 trillion.",
              s=["corp"], lc="move", st="new", neo=[0, ""],
              mc="Stablecoin on-ramps could link to card spending and settlement.",
              src=[["Capital Markets Day, Mar 2026", CMD]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: fraud defences against rising app and card fraud, AI that made 10 million personalised interactions in a half, UCount Rewards and fast-growing value-added services, and APIs for corporates.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "Card fraud up 18% in SA.", "div": "sbsa", "rev": "ppb", "products": [
            P("fraud", "Fraud detection & monitoring", "PPB is investing in fraud detection and monitoring. Across South Africa in 2025, digital banking fraud reached about R2.4 billion (up 29%) and gross card fraud about R1.75 billion (up 18%), led by card-not-present fraud. No Mastercard fraud tool is public at Standard Bank ⚠.",
              s=["con", "sme"], lc="everyday", neo=[None, "No Mastercard tool public."],
              mc="Rising card-not-present and app fraud is the clearest need.",
              src=[["2026 interim results booklet", HY26], ["SABRIC: 2025 crime statistics", SABRIC], ["BusinessTech: SABRIC card fraud", SABRICBT]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI & personalisation", "blurb": "10 million tailored interactions.", "div": "sbg", "rev": "ppb", "products": [
            P("personalisation", "Personalisation & agentic AI", "More than 10 million AI-driven personalised client interactions and 3.1 million tailored app offers in the first half of 2026. Conversational AI answers 65% of app queries; agentic AI cut asset-finance paperwork from about an hour to a minute, and PPB names agentic e-commerce as a future opportunity.",
              s=["con", "sme"], lc="everyday", st="new", neo=[0, ""],
              mc="Agentic e-commerce on the Mastercard card book is untouched ground for Agent Pay.",
              src=[["2026 interim results booklet", HY26], ["Capital Markets Day, Mar 2026", CMD]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards & value-added services", "blurb": "UCount; VAS income up 50%.", "div": "sbsa", "rev": "ppb", "products": [
            P("ucount", "UCount Rewards", "1.64 million members (June 2026), who earn points on credit, cheque and debit cards and on SnapScan, with offers such as up to 40% back at Checkers, Shoprite and Sixty60.",
              s=["con", "priv"], lc="grow", neo=[1, "Earned mostly on Mastercard cards."],
              mc="Card-linked offers and Priceless could deepen UCount.",
              src=[["2026 interim results booklet", HY26], ["Standard Bank: compare credit cards", CARDS]]),
            P("vas", "Value-added services", "Airtime, data, electricity, lotto and vouchers in the app; PPB value-added services revenue rose 50% in the first half of 2026.",
              s=["con", "cash"], lc="beyond", neo=[0, ""], src=[["2026 interim results booklet", HY26], ["Capital Markets Day, Mar 2026", CMD]]),
        ]},
        {"id": "3.4", "ic": "code-xml", "name": "APIs & connectivity", "blurb": "29 CIB APIs, OneHub.", "div": "sbg", "rev": "cib", "products": [
            P("apis", "OneHub & corporate APIs", "CIB has 29 APIs available and is rolling out OneHub API solutions for its payments business.",
              s=["corp"], lc="open", st="new", neo=[0, ""], src=[["Capital Markets Day, Mar 2026", CMD]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What clients buy: transactional accounts for 12 million South Africans, nearly half the mortgage profit pool, business banking for half a million SA clients, Africa's leading CIB, and Liberty insurance and STANLIB funds.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Everyday accounts", "blurb": "12 million active in SA.", "div": "sbsa", "rev": "ppb", "products": [
            P("accounts", "MyMo, Achieva, Prestige & Private Banking", "Transactional accounts for 11.96 million active South African clients (4.95 million digitally active) and 4.45 million in Africa Regions. One in two South African Private Banking clients bank here.",
              s=["con", "priv"], lc="open", neo=[1, "Mastercard mass-market cards, Visa Private."], src=[["2026 interim results booklet", HY26], ["Capital Markets Day, Mar 2026", CMD]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Home & vehicle finance", "blurb": "Half the mortgage profit pool.", "div": "sbsa", "rev": "ppb", "products": [
            P("homeloans", "Home Services", "Mortgages with nearly half the South African profit pool; disbursements up 17% in the first half of 2026.",
              s=["con", "priv"], lc="borrow", neo=[0, ""], src=[["Capital Markets Day, Mar 2026", CMD], ["2026 interim results booklet", HY26]]),
            P("vaf", "Vehicle & Asset Finance and personal loans", "Retail vehicle finance up 10%, and a 21% share of South African personal unsecured lending and overdrafts.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["2026 interim results booklet", HY26], ["Capital Markets Day, Mar 2026", CMD]]),
        ]},
        {"id": "4.3", "ic": "briefcase", "name": "Business & commercial", "blurb": "10,000 new clients a month.", "div": "sbsa", "rev": "bcb", "products": [
            P("bcb", "Business & Commercial Banking", "About 536,000 active South African clients ⚠, adding about 10,000 a month; 15-minute digital account opening; BizFlex pay-as-you-earn loans; Business Lending disbursements up 27% in South Africa. ROE 36.3%.",
              s=["sme"], lc="open", neo=[1, "Business cards Mastercard or Visa."], src=[["2026 interim results booklet", HY26], ["Capital Markets Day, Mar 2026", CMD]]),
        ]},
        {"id": "4.4", "ic": "building-2", "name": "Corporate & Investment Banking", "blurb": "R13.8bn earned, ROE 24.8%.", "div": "sbg", "rev": "cib", "products": [
            P("cib", "Corporate & Investment Banking", "Transaction banking, markets and investment banking across Africa: earnings R13.8 billion in the first half of 2026 (up 15%), ROE 24.8%, and R100 billion of revenue targeted by 2028.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["2026 interim results booklet", HY26], ["Capital Markets Day, Mar 2026", CMD]]),
        ]},
        {"id": "4.5", "ic": "gem", "name": "Insurance, wealth & offshore", "blurb": "Liberty, STANLIB, Offshore.", "div": "liberty", "rev": "iam", "products": [
            P("liberty", "Liberty & STANLIB", "Insurance and asset management (ROE 21.1%), with R10 billion of insurance premiums sold through PPB and R28 billion of claims paid in 2025.",
              s=["priv", "con"], lc="grow", neo=[0, ""], src=[["2026 interim results booklet", HY26], ["Capital Markets Day, Mar 2026", CMD]]),
            P("offshore", "Standard Bank Offshore", "Accounts in Jersey and the Isle of Man with a Visa debit card; earnings of R548 million in the first half of 2026 (down 23%).",
              s=["glob", "priv"], lc="grow", o="P", at="Visa", neo=[0, "Visa."], src=[["Standard Bank: Prestige Banking", PRESTIGE], ["2026 interim results booklet", HY26]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How clients reach the group: a banking app with a billion log-ins a half, about 1,000 branches and 5,600 ATMs across Africa, and retailers, advisers and agents.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Banking app & online", "blurb": "A billion log-ins in a half.", "div": "sbsa", "rev": "ppb", "products": [
            P("app", "Banking app, USSD & Online Banking for Business", "1.03 billion log-ins in the first half of 2026 (up 22%), with 69% of transactional clients digitally active; the South African app is reused across Africa Regions. USSD carries PayShap and Instant Money.",
              s=["con", "sme", "afr"], lc="everyday", neo=[1, "In-app tap for Mastercard cards."], src=[["2026 interim results booklet", HY26], ["Capital Markets Day, Mar 2026", CMD], ["Standard Bank: PayShap ID surge, Oct 2024", PSSB]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "1,037 branches, 5,646 ATMs.", "div": "sbg", "rev": "ppb", "products": [
            P("branches", "Branches, kiosks & ATMs", "516 branches, 170 in-store kiosks and 3,496 ATMs in South Africa, plus 521 branches and 2,150 ATMs in Africa Regions (June 2026); ATM use in South Africa fell 22%.",
              s=["con", "cash", "afr"], lc="everyday", neo=[0, ""], src=[["2026 interim results booklet", HY26]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partners & advisers", "blurb": "Retailers, Liberty advisers.", "div": "sbg", "rev": "ppb", "products": [
            P("partners", "Retailers, advisers & agents", "Retail partners for Instant Money, Liberty tied advisers and the largest bank-based advice force, and agency banking that is being deepened across the continent.",
              s=["cash", "priv", "afr"], lc="open", neo=[0, ""], src=[["Capital Markets Day, Mar 2026", CMD], ["2026 interim results booklet", HY26]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Standard Bank", "blurb": "The retail cards, not the new rails.", "products": [
        P("mcatsb", "Mastercard at Standard Bank", "Standard Bank's South African personal credit cards and mass-market debit cards carry Mastercard, World Citizen is a World Mastercard, in-app tap-to-pay is Mastercard-only, and SimplyBlu runs on Mastercard Gateway. The last public network deal was a five-year Africa agreement in August 2013. Visa holds Private Banking, offshore and fleet cards and Shyft's FX rails; UnionPay has the recent announcements; Diners Club is the bank's own.",
          s=["con"], div="sbg", rev="group", mc="The relationship this map is drawn for.",
          src=[["Standard Bank: compare credit cards", CARDS], ["Retail Banker International: Mastercard deal, Aug 2013", MC2013], ["Visa: Shyft case study, 2023", VISASHYFT]]),
    ]},
    {"id": "pillar-market", "name": "South African payments", "blurb": "PayShap, PayInc, the SARB.", "products": [
        P("market", "The South African market", "No domestic card scheme: Visa and Mastercard dominate and settle in SAMOS, while PayInc (formerly BankservAfrica, now 50% owned by the SARB) runs EFT, DebiCheck, real-time clearing and PayShap. The SARB studied a domestic card scheme in 2021, citing offshore processing of domestic card payments, and took card interoperability under its own management in August 2026. No current rule routes card debit payments domestically ⚠.",
          s=["con"], div="sbg", rev="group",
          src=[["SARB: domestic card scheme paper, Mar 2021", DCS], ["SARB: NPS transition, Aug 2026", NPS], ["The Condia: PASA and PayInc, Jun 2026", PASA], ["Stitch: PayShap in 2026", STITCH]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
