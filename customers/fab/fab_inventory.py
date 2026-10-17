"""First Abu Dhabi Bank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the H1 2026 results (23 July 2026) and the FY 2025
results (28 January 2026). Card networks are read from the bank's own card pages and from Mastercard and Visa
releases. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides
wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1 = "https://www.bankfab.com/en-ae/about-fab/group/in-the-media/fab-delivers-strong-h1-2026-results"
GNH1 = "https://gulfnews.com/business/banking/fab-h1-net-profit-rises-to-dh1073-billion-lending-grows-7-1.500617173"
FY25 = "https://www.bankfab.com/-/media/fab-uds/about-fab/group/media/in-the-media/2026/fab-q4-fy25-pr-en.pdf?view=1"
BOARD = "https://www.bankfab.com/en-ae/about-fab/group/board-of-directors"
EXCO = "https://www.bankfab.com/en-ae/about-fab/group/senior-management"
FORBES = "https://www.forbesmiddleeast.com/lists/100-most-valuable-companies-2026/first-abu-dhabi-bank-fab/"
WIKI = "https://en.wikipedia.org/wiki/First_Abu_Dhabi_Bank"
SUBS = "https://www.bankfab.com/en-ae/subsidiaries"
MCEXCL = "https://www.gccbusinessnews.com/mastercard-fab-exclusive-partnership/"
MC5 = "https://www.zawya.com/en/press-release/companies-news/mastercard-and-first-abu-dhabi-bank-hit-major-milestone-five-credit-cards-launched-in-six-months-mdickzh2"
LEGEND = "https://www.zawya.com/en/press-release/first-abu-dhabi-bank-and-mastercard-unveil-uaes-first-world-legend-exclusive-card-pairing-bespoke-design-with-luxury-lifestyle-benefits-521775"
ACTIVE = "https://www.bankfab.com/en-ae/about-fab/group/in-the-media/fab-launches-world-first-rewards-active-credit-card"
ADNOC = "https://gulfnews.com/business/banking/new-adnoc-credit-card-offers-15-return-on-fuel-transport-spending-1.500376487"
ADNOCW = "https://www.wam.ae/en/article/bn5rrg6-adnoc-distribution-fab-mastercard-launch-adnoc"
SMESUITE = "https://www.albawaba.com/business/pr/first-abu-dhabi-bank-and-mastercard-1626894"
MCLAREN = "https://www.bankfab.com/en-ae/personal/credit-cards/offers/mclaren-racing-mastercard-rewards"
ACCESSPASS = "https://gulfnews.com/business/gear-up-uae-mastercard-debuts-access-pass-as-abu-dhabi-grand-prix-fever-peaks-1.500370234"
SLICE = "https://www.zawya.com/en/business/banking-and-insurance/first-abu-dhabi-bank-introduces-slicepay-bnpl-card-in-uae-mhdvjqaf"
MCCOMM = "https://www.bankfab.com/en-ae/about-fab/group/in-the-media/20210210-fab-partners-with-mastercard"
WDEBIT = "https://www.bankfab.com/en-ae/about-fab/group/in-the-media/fab-launches-the-first-world-debit-card-for-smes-in-the-uae"
PAYITMC = "https://www.bankfab.com/en-ae/about-fab/group/in-the-media/fabs-payit-wallet-partners-with-mastercard"
PAYITVISA = "https://www.bankfab.com/en-ae/about-fab/group/in-the-media/payit-launches-digital-card-for-hassle-free-local-and-international-payments"
PAYITUA = "https://www.bankfab.com/en-ae/about-fab/group/in-the-media/fab-launches-payit-universal-account-financial-inclusion-2026"
SNPL = "https://www.bankfab.com/en-ae/about-fab/group/in-the-media/payit-send-now-pay-later-international-transfers"
VISATAP = "https://www.bankfab.com/en-ae/about-fab/group/in-the-media/20201104fabvisa"
VISAVPA = "https://www.bankfab.com/en-ae/about-fab/group/in-the-media/20201214fabvisa"
MAGNATI = "https://www.bankfab.com/en-ae/about-fab/group/in-the-media/20210404-magnati"
MAGSALE = "https://www.bankfab.com/en-ae/about-fab/group/in-the-media/20220228-fab-announces-the-sale-of-60-percent-in-magnati"
MAGVISA = "https://www.bankfab.com/en-ae/about-fab/group/in-the-media/20220406-magnati-and-visa-offer-to-accept-payments-through-smartphones"
GEIDEA = "https://www.bankfab.com/en-ae/about-fab/group/in-the-media/fab-magnati-strengthen-digital-foothold-in-ksa-through-strategic-alliance-with-geidea"
NIBROOK = "https://enterpriseam.com/uae/2024/09/19/fab-brookfield-take-over-network/"
NIMAG = "https://enterpriseam.com/uae/2025/10/02/network-international-magnati-finalize-merger/"
MAGNI = "https://www.bankfab.com/en-ae/about-fab/group/in-the-media/magnati-and-network-international-merger"
JAYWAN = "https://www.bankfab.com/en-ae/about-fab/group/in-the-media/fab-launches-jaywan-debit-card-uae-national-card-scheme"
JAYPAGE = "https://www.bankfab.com/en-ae/personal/jaywan-debit-card"
JAYKT = "https://www.khaleejtimes.com/business/finance/uae-jaywan-card-benefits-banks-travel-perks-how-to-apply?amp=1"
AANI = "https://www.centralbank.ae/media/eccjvuib/al-etihad-payments-launches-aani-a-instant-payments-platform-for-digital-transactions-in-the-uae-en.pdf"
APIP = "https://www.bankfab.com/en-ae/about-fab/group/in-the-media/fab-launches-api-developer-portal-to-accelerate-client-integration-and-digital-adoption"
SWIFT = "https://www.bankfab.com/en-ae/about-fab/group/in-the-media/completes-tokenized-deposit-milestone-with-citi-swift-ledger"
ONYX = "https://www.bankfab.com/en-ae/about-fab/group/in-the-media/fab-successfully-pilots-programmable-payments-through-onyx-by-jp-morgan"
CIPS = "https://www.bankfab.com/en-ae/about-fab/group/in-the-media/fab-becomes-first-mena-bank-to-join-cips"
AIHUB = "https://www.bankfab.com/en-ae/about-fab/group/in-the-media/fab-accelerates-enterprise-ai-adoption"
AIPORT = "https://www.bankfab.com/en-ae/about-fab/group/in-the-media/fab-launches-ai-analytics"
KHOBAR = "https://www.bankfab.com/en-ae/about-fab/group/in-the-media/fab-alkobar-ksa"
KSAINV = "https://www.bankfab.com/en-ae/about-fab/group/in-the-media/fab-to-expand-and-grow-investment-services-in-saudi-arabia"
CC = "https://www.bankfab.com/en-ae/personal/credit-cards"
ACCTS = "https://www.bankfab.com/en-ae/personal/accounts"
SHARE = "https://www.bankfab.com/en-ae/personal/credit-cards/fab-share-cards"
ETIHADP = "https://www.bankfab.com/en-ae/personal/promotions/etihad-guest-credit-cards"
ETIHAD = "https://www.tradearabia.com/News/294579/Etihad-Guest-extends-key-partnership-with-First-Abu-Dhabi-Bank"
BLUE = "https://www.bankfab.com/en-ae/personal/promotions/blue-fab-credit-cards"
TRAVEL = "https://www.bankfab.com/en-ae/personal/credit-cards/fab-travel-credit-card"
ISLAMIC = "https://www.bankfab.com/en-ae/islamic-banking"
MOBILE = "https://www.bankfab.com/en-ae/personal/help-and-support/digital-banking/mobile-banking"
DISC = "https://www.bankfab.com/en-ae/personal/credit-cards/services/discontinued-cards"
MISRH1 = "https://fabmisr.com.eg/en/press-room/2026/H1-2026"
MISRPOS = "https://www.fabmisr.com.eg/en/press-room/2026/FABMISR-POS"
MISRCC = "https://www.fabmisr.com.eg/en/personal-banking/credit-cards"
ENBDH1 = "https://www.emiratesnbd.com/en/media-center/emirates-nbd-h1-2026-results-announcement"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · Abu Dhabi · reach", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: the UAE's largest bank at AED 1.41 trillion, a record AED 21 billion profit in 2025, Abu Dhabi's ruling family in the chair, the 2017 merger that made it, 20-plus markets, agentic AI and tokenised deposits.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "AED 1.41 trillion, RoTE 18.5%.", "div": "group", "rev": "ibm", "products": [
            P("balance", "Balance sheet & earnings", "Operating income AED 19.50 billion (up 7%) and net profit AED 10.73 billion in H1 2026, RoTE 18.5%; total assets AED 1.41 trillion (USD 384 billion), net loans AED 661 billion, deposits AED 853 billion, CET1 13.7%, NPL ratio 2.2% at 30 June 2026. FY 2025 net profit a record AED 21.11 billion (up 24%) on income of AED 36.68 billion; a record AED 8.84 billion dividend.",
              s=["corp"], neo=[0, ""], src=[["FAB: H1 2026 results", H1], ["FAB: FY 2025 results", FY25], ["Gulf News: H1 2026", GNH1]]),
            P("ratings", "Ratings & market value", "Rated Aa3/AA-/AA- with stable outlooks, reaffirmed in H1 2026 and the highest-rated banking group in MENA; market value about USD 56 billion; more than 4 million customers.",
              s=["corp"], neo=[0, ""], src=[["FAB: H1 2026 results", H1], ["Forbes Middle East 2026", FORBES]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Ownership & leadership", "blurb": "Sheikh Tahnoon and Hana Al Rostamani.", "div": "group", "rev": "ibm", "products": [
            P("leadership", "Board & Group EXCO", "Chairman H.H. Sheikh Tahnoon bin Zayed Al Nahyan, Deputy Ruler of Abu Dhabi; Group CEO Hana Al Rostamani; CFO Lars Kramer; Futoon Al Mazrouei runs Personal, Business, Wealth and Privileged Client Banking, Linos Lekkas Investment Banking & Markets, Martin Tricaud Wholesale Banking, Omar Hafeez International and Divyesh Vithlani technology and transformation.",
              s=["corp"], neo=[0, ""], src=[["FAB: board", BOARD], ["FAB: senior management", EXCO]]),
        ]},
        {"id": "1.3", "ic": "earth", "name": "Heritage & reach", "blurb": "NBAD plus FGB, 20+ markets.", "div": "group", "rev": "intl", "products": [
            P("heritage", "The 2017 merger", "Formed by the merger of National Bank of Abu Dhabi and First Gulf Bank, effective 2017, and listed on the Abu Dhabi Securities Exchange; headquartered in Abu Dhabi.",
              s=["con"], o="I", neo=[0, ""], src=[["Wikipedia: First Abu Dhabi Bank", WIKI], ["FAB: board", BOARD]]),
            P("intlnet", "International network", "More than 20 markets and 140-plus branches; international assets AED 437 billion (31% of the group) and international revenue up 35% to 22% of the total in H1 2026; the only UAE bank with a licensed branch in mainland China, and live in Turkey and GIFT City.",
              s=["corp"], neo=[0, ""], src=[["FAB: H1 2026 results", H1], ["FAB: FY 2025 results", FY25], ["Forbes Middle East 2026", FORBES]]),
        ]},
        {"id": "1.4", "ic": "brain", "name": "Technology & AI", "blurb": "30+ agentic AI uses.", "div": "group", "rev": "ibm", "products": [
            P("ai", "AI Innovation Hub", "Copilot for every employee with 1,000-plus agents, more than 30 agentic AI use cases in trade, payments, operations and compliance, 90% of structured data on one platform; more than 20% productivity uplift in H1 2026 and top three in the 2026 Evident AI index for the Middle East and Africa.",
              s=["corp"], st="new", neo=[0, "FAB's own."], src=[["FAB: enterprise AI, Feb 2026", AIHUB], ["FAB: FY 2025 results", FY25], ["FAB: H1 2026 results", H1]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "The UAE's global bank.", "div": "group", "rev": "intl", "products": [
            P("strategy", "Strategy", "\"The UAE's global bank\": grow international corridors, embed AI at scale and lead in sustainable finance (AED 395 billion of AED 500 billion targeted for 2030); RoTE kept above medium-term guidance ⚠ figure not captured.",
              s=["corp"], neo=[0, ""], src=[["FAB: H1 2026 results", H1]]),
            P("deals", "Deals", "Bank Audi Egypt bought (2021) and renamed FABMISR; Magnati carved out (2021) and 60% sold to Brookfield (2022); co-investor in the Network International take-private (2024) and Magnati's merger into it (2025); Amundi and T. Rowe Price wealth partnerships (2025–26).",
              s=["corp"], o="A", neo=[0, ""], src=[["FAB: Magnati sale, Feb 2022", MAGSALE], ["Enterprise AM: Network takeover, Sep 2024", NIBROOK], ["FAB: FY 2025 results", FY25]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Eight ways money moves: Mastercard debit and a new Jaywan card, Mastercard credit after the 2024 exclusive deal, Visa co-brands with Etihad, Majid Al Futtaim and Al-Futtaim, Mastercard commercial cards, the Payit wallet, acquiring through Network International, and tokenised deposits on Swift Ledger.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "Platinum Mastercard debit.", "div": "fab", "rev": "pbwpc", "products": [
            P("debit", "FAB debit cards", "Personal accounts come with a free Platinum Mastercard debit card; offers are run for 'FAB Mastercard Debit or Credit' cardholders.",
              s=["con", "work"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard debit."], src=[["FAB: accounts", ACCTS], ["FAB: credit cards and offers", CC]]),
            P("smedebit", "World Business Debit", "The first 'World' debit card for SMEs in the UAE, launched with Mastercard in May 2019 with higher limits and partner discounts.",
              s=["sme"], lc="everyday", ay="May 2019", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["FAB: World Business Debit, May 2019", WDEBIT]]),
        ]},
        {"id": "2.2", "ic": "flag", "name": "Jaywan & Aani", "blurb": "The UAE's own rails.", "div": "fab", "rev": "pbwpc", "products": [
            P("jaywan", "Jaywan debit card", "A mono-badged domestic debit card on the UAE's national scheme, run by Al Etihad Payments for the Central Bank, launched 20 July 2026: domestic use only, 3D Secure, chip and PIN and tokenised wallets; no loyalty accrual. Credit cards are planned on the scheme.", short="Jaywan debit",
              s=["con"], lc="everyday", st="new", ay="Jul 2026", o="P", at="Al Etihad Payments", neo=[0, "Jaywan."],
              mc="Jaywan allows co-badging with global networks; FAB's choice is open.",
              src=[["FAB: Jaywan debit card, Jul 2026", JAYWAN], ["FAB: Jaywan FAQ", JAYPAGE], ["Khaleej Times: Jaywan, Jul 2026", JAYKT]]),
            P("aani", "Aani instant payments", "FAB was one of eight launch institutions on Aani, the Central Bank's instant-payments platform with phone-number transfers and merchant QR, in October 2023.",
              s=["con", "sme"], lc="move", ay="Oct 2023", o="P", at="Al Etihad Payments", neo=[0, "Account-to-account."], src=[["CBUAE: Aani launch, Oct 2023", AANI]]),
        ]},
        {"id": "2.3", "ic": "credit-card", "name": "Credit cards", "blurb": "Mastercard, up to World Legend.", "div": "fab", "rev": "pbwpc", "products": [
            P("credit", "FAB credit cards", "The own-brand range is Mastercard: Z Card for Gen Z, Cashback, Rewards Indulge, Elite, Travel (World Elite concierge) and the Sharia-compliant Emirati Islamic card; five of them launched in six months to August 2025 under the 2024 exclusive deal.", short="Credit (Mastercard)",
              s=["con", "aff"], lc="borrow", st="new", ay="Aug 2025", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="The core of the 2024 portfolio consolidation onto Mastercard.",
              src=[["Mastercard and FAB: five cards, Aug 2025", MC5], ["FAB: credit cards", CC], ["FAB: Travel card", TRAVEL]]),
            P("active", "Rewards Active card & ring", "A Mastercard credit card with a free tokenised fitness and payment ring that earns 25 FAB Rewards per 1,000 steps, with Lionel Messi card art; billed as a world first in January 2026.",
              s=["con"], lc="everyday", st="new", ay="Jan 2026", o="P", at="Mastercard, Steppi", neo=[2, "Mastercard tokens."], src=[["FAB: Rewards Active, Jan 2026", ACTIVE]]),
            P("slicepay", "SlicePay (Dubai First)", "A digital buy-now-pay-later card under the Dubai First name that splits purchases into four interest-free payments; the first Mastercard Installments programme in EEMEA (November 2023) ⚠ current status unconfirmed.",
              s=["con"], lc="borrow", ay="Nov 2023", o="P", at="Mastercard", div="dubaifirst", neo=[3, "Mastercard Installments."], src=[["Zawya: SlicePay, Nov 2023", SLICE]]),
            P("royale", "FAB Royale World Legend Exclusive", "The UAE's first World Legend Exclusive Mastercard, invitation-only, with Royale Lifestyle Concierge, the Mastercard Premium Lifestyle Program and meet-and-greet in 60 destinations (10 September 2026).",
              s=["aff"], lc="everyday", st="new", ay="Sep 2026", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Zawya: World Legend Exclusive, Sep 2026", LEGEND]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Co-brand cards", "blurb": "ADNOC on Mastercard; Etihad on Visa.", "div": "fab", "rev": "pbwpc", "products": [
            P("adnoc", "ADNOC Rewards World Mastercard", "With ADNOC Distribution (11 December 2025): 15% back on fuel, car care and Oasis spend, 3% on parking and tolls, for a programme of 2.5 million members; also the du and GEMS World Mastercards.",
              s=["con"], lc="everyday", st="new", ay="Dec 2025", o="P", at="ADNOC Distribution", neo=[2, "Mastercard."], src=[["Gulf News: ADNOC card, Dec 2025", ADNOC], ["WAM: ADNOC card, Dec 2025", ADNOCW]]),
            P("etihad", "Etihad Guest cards", "Etihad Guest Visa Infinite, Signature and Platinum since 2017; the partnership was extended to 2027 ⚠ date of the extension not confirmed.",
              s=["con", "aff"], lc="everyday", o="P", at="Etihad, Visa", neo=[0, "Visa."],
              mc="The biggest Visa co-brand left; renewal due by 2027.",
              src=[["FAB: Etihad Guest cards", ETIHADP], ["TradeArabia: Etihad Guest extension", ETIHAD]]),
            P("retailcobrand", "SHARE & Blue FAB cards", "SHARE cards with Majid Al Futtaim (Visa Signature and Infinite) and Blue FAB cards with Al-Futtaim (Visa Infinite and Signature), plus discontinued Visa lines still serviced.",
              s=["con"], lc="everyday", o="P", at="Majid Al Futtaim, Al-Futtaim, Visa", neo=[0, "Visa."], src=[["FAB: SHARE cards", SHARE], ["FAB: Blue FAB cards", BLUE], ["FAB: discontinued cards", DISC]]),
        ]},
        {"id": "2.5", "ic": "briefcase-business", "name": "Commercial cards", "blurb": "Mastercard since 2021.", "div": "fab", "rev": "wb", "products": [
            P("commcards", "Commercial cards", "A five-year Mastercard deal (February 2021) brought In Control, the Mastercard Purchase Card and travel and entertainment cards; a three-tier SME suite (ONYX World Elite, SILVER commercial credit, World Debit) followed in May 2026 ⚠.",
              s=["sme", "corp"], lc="move", ay="Feb 2021", o="P", at="Mastercard", neo=[3, "Mastercard In Control."], src=[["FAB: Mastercard commercial deal, Feb 2021", MCCOMM], ["Albawaba: SME cards suite, May 2026", SMESUITE]]),
            P("visavirtual", "Visa virtual cards & CTA", "The UAE's first Visa virtual corporate cards with Visa Payables Automation and a Visa Central Travel Account (December 2020) ⚠ current status unknown.",
              s=["corp"], lc="move", ay="Dec 2020", o="P", at="Visa", neo=[0, "Visa."], src=[["FAB: Visa virtual cards, Dec 2020", VISAVPA]]),
        ]},
        {"id": "2.6", "ic": "smartphone", "name": "Payit", "blurb": "Wallet, account, remittances.", "div": "payit", "rev": "pbwpc", "products": [
            P("payit", "Payit wallet & remittances", "The UAE's first fully featured wallet (2018), with Mastercard cross-border push payments to more than 100 corridors since March 2020 and Send Now Pay Later remittances repaid within 30 days (August 2026).", short="Payit",
              s=["work"], lc="move", st="new", ay="Mar 2020", o="B", neo=[1, "Mastercard cross-border ⚠ still in use."],
              mc="Remittance corridors and salary flows suit Mastercard Move.",
              src=[["FAB: payit and Mastercard, Mar 2020", PAYITMC], ["FAB: Send Now Pay Later, Aug 2026", SNPL]]),
            P("payitua", "Payit Universal Account & card", "A Central Bank Universal Account for people earning up to AED 5,000 and for WPS salaries (May 2026), with the Letsgo Payit Visa Platinum card (March 2023).",
              s=["work"], lc="open", st="new", ay="May 2026", o="B", at="Visa", neo=[0, "Visa card."], src=[["FAB: Payit Universal Account, May 2026", PAYITUA], ["FAB: Payit Visa card, Mar 2023", PAYITVISA]]),
        ]},
        {"id": "2.7", "ic": "network", "name": "Acquiring", "blurb": "Magnati, now Network International.", "div": "network", "rev": "pbwpc", "products": [
            P("acquiring", "Magnati & Network International", "FAB's payments arm, carved out as Magnati in 2021 (30,000+ merchants, 2 million prepaid cards, about USD 18 billion processed in 2020), 60% sold to Brookfield in 2022 and merged into Network International in 2025, which FAB co-owns ⚠ stake undisclosed.", short="Acquiring (Network)",
              s=["sme"], lc="move", st="flux", ay="Oct 2025", o="A", at="Brookfield", neo=[1, "Accepts every network."],
              src=[["FAB: Magnati carve-out, Apr 2021", MAGNATI], ["FAB: Magnati sale, Feb 2022", MAGSALE], ["Enterprise AM: merger, Oct 2025", NIMAG], ["FAB: merger notice", MAGNI]]),
            P("misrpos", "FABMISR acquiring", "FABMISR in Egypt launched POS acquiring in January 2026 after its 'Access by FABMISR' e-commerce gateway.",
              s=["sme"], lc="move", st="new", ay="Jan 2026", div="misr", rev="intl", o="B", neo=[1, "Accepts Visa and Mastercard."], src=[["FABMISR: POS launch, Jan 2026", MISRPOS]]),
        ]},
        {"id": "2.8", "ic": "coins", "name": "Cross-border & digital money", "blurb": "Swift Ledger, CIPS, JPM Coin.", "div": "group", "rev": "wb", "products": [
            P("digitalmoney", "Tokenised deposits & clearing", "Live USD tokenised-deposit transactions with Citi on Swift Ledger, first in the Middle East and Africa (September 2026); programmable payments with JPM Coin (2024); first MENA direct participant in China's CIPS (June 2025).",
              s=["corp"], lc="move", st="new", ay="Sep 2026", o="P", at="Swift, Citi, J.P. Morgan", neo=[0, ""],
              mc="Tokenised settlement is live without Mastercard.",
              src=[["FAB: Swift Ledger, Sep 2026", SWIFT], ["FAB: Onyx pilot, Sep 2024", ONYX], ["FAB: CIPS, Jun 2025", CIPS]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: fraud and security, agentic AI and merchant analytics, an API portal with 65 APIs, and FAB Rewards with Mastercard's McLaren pass and Priceless benefits.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "No vendor named.", "div": "fab", "rev": "pbwpc", "products": [
            P("fraud", "Fraud & security", "Fraud-and-security guidance, 3D Secure and chip and PIN; the 2024 Mastercard deal named Mastercard's UAE Global Center for Advanced AI and Cyber Technology ⚠ no live Mastercard fraud product found.",
              s=["con"], lc="everyday", neo=[None, "Nothing public."],
              mc="Aani and wallets raise scam risk; fraud scoring is open ground.",
              src=[["GCC Business News: exclusive deal, Mar 2024", MCEXCL], ["FAB: Jaywan debit card, Jul 2026", JAYWAN]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI, data & APIs", "blurb": "Agents, analytics, 65 APIs.", "div": "group", "rev": "ibm", "products": [
            P("agents", "Agentic AI in operations", "More than 30 agentic AI use cases across trade, payments, client operations and compliance, with 70–80% less manual effort in key workflows (H1 2026).",
              s=["corp"], st="new", neo=[0, ""],
              mc="Agentic commerce for cardholders has not been announced.",
              src=[["FAB: enterprise AI, Feb 2026", AIHUB], ["FAB: H1 2026 results", H1]]),
            P("merchantai", "Merchant analytics portal", "AI and machine-learning analytics for merchants (spend forecasting, segmentation, loyalty), piloted with Al-Futtaim in November 2018.",
              s=["sme"], lc="grow", ay="Nov 2018", o="B", neo=[0, ""], src=[["FAB: AI analytics portal, Nov 2018", AIPORT]]),
            P("apis", "API Developer Portal", "Launched 13 October 2026 with 65 APIs for payments, trade finance and cash management, for clients to build banking into their own systems.",
              s=["corp", "sme"], lc="move", st="new", ay="Oct 2026", o="B", neo=[0, ""], src=[["FAB: API portal, Oct 2026", APIP]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards & experiences", "blurb": "FAB Rewards, McLaren pass.", "div": "fab", "rev": "pbwpc", "products": [
            P("rewards", "FAB Rewards", "FAB Rewards and FAB Islamic Rewards across cards and accounts, step rewards with Steppi, and Mastercard Priceless and Travel Pass benefits on the Mastercard cards.",
              s=["con", "aff"], lc="grow", neo=[1, "Priceless on the Mastercard cards."], src=[["FAB: credit cards", CC], ["FAB: Rewards Active, Jan 2026", ACTIVE]]),
            P("mclaren", "McLaren Racing Mastercard Pass", "FAB cardholders were first on Mastercard's Access Pass: McLaren card art, McLaren Plus membership and prizes, from 24 November 2025.",
              s=["con", "aff"], lc="grow", st="new", ay="Nov 2025", o="P", at="Mastercard", neo=[3, "Mastercard Access Pass."], src=[["FAB: McLaren Racing Mastercard Pass", MCLAREN], ["Gulf News: Access Pass, Nov 2025", ACCESSPASS]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: personal banking for 4 million customers, Elite, Royale and private banking, business banking with 85% more new SMEs, wholesale and investment banking that lead MENA's league tables, Islamic banking, and banks in Egypt and Saudi Arabia.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Personal banking", "blurb": "Accounts, loans, mortgages.", "div": "fab", "rev": "pbwpc", "products": [
            P("accounts", "Accounts, loans & mortgages", "Current and savings accounts opened in minutes with an Emirates ID, personal loans, mortgages and insurance; retail CASA up AED 25 billion in 2025.",
              s=["con"], lc="everyday", neo=[1, "Mastercard debit; Jaywan too."], src=[["FAB: accounts", ACCTS], ["FAB: FY 2025 results", FY25]]),
        ]},
        {"id": "4.2", "ic": "gem", "name": "Wealth & privileged clients", "blurb": "AUM up 20%.", "div": "fab", "rev": "pbwpc", "products": [
            P("wealth", "Elite, Royale & private banking", "Wealth and privileged-client banking with retail AUM up 20% in H1 2026, and Amundi and T. Rowe Price partnerships.",
              s=["aff"], lc="grow", neo=[0, ""], src=[["FAB: H1 2026 results", H1], ["FAB: FY 2025 results", FY25]]),
        ]},
        {"id": "4.3", "ic": "briefcase", "name": "Business banking", "blurb": "85% more new SMEs.", "div": "fab", "rev": "pbwpc", "products": [
            P("sme", "Business banking", "SME accounts, cards and finance; new-to-bank SME clients up 85% in H1 2026.",
              s=["sme"], lc="everyday", st="new", neo=[1, "Mastercard cards; Network acquiring."], src=[["FAB: H1 2026 results", H1]]),
        ]},
        {"id": "4.4", "ic": "factory", "name": "Wholesale & investment banking", "blurb": "Top of MENA's tables.", "div": "group", "rev": "wb", "products": [
            P("wholesale", "Wholesale Banking", "Sector coverage and transaction banking; H1 2026 revenue AED 3.41 billion, up 16%.",
              s=["corp"], lc="move", neo=[0, ""], src=[["FAB: H1 2026 results", H1]]),
            P("ibm", "Investment Banking & Markets", "Top MENA league-table positions, AED 330 billion raised for clients in 2025, DCM volumes up 58% in H1 2026; revenue AED 6.42 billion in the half.",
              s=["corp"], lc="grow", rev="ibm", neo=[0, ""], src=[["FAB: H1 2026 results", H1], ["FAB: FY 2025 results", FY25]]),
        ]},
        {"id": "4.5", "ic": "landmark", "name": "Islamic banking", "blurb": "FAB Islamic.", "div": "islamic", "rev": "pbwpc", "products": [
            P("islamic", "FAB Islamic", "Islamic accounts, finance and cards in 'both Visa and Mastercard options', FAB Islamic Rewards and subsidised home finance with the Abu Dhabi Housing Authority.",
              s=["con"], lc="everyday", neo=[1, "Visa and Mastercard."], src=[["FAB: Islamic banking", ISLAMIC]]),
        ]},
        {"id": "4.6", "ic": "globe", "name": "Egypt & Saudi Arabia", "blurb": "FABMISR and three branches.", "div": "misr", "rev": "intl", "products": [
            P("misr", "FABMISR (Egypt)", "Ex-Bank Audi Egypt: net profit EGP 7.9 billion in H1 2026, total assets EGP 420 billion; credit cards on Mastercard including World Elite and World Business.",
              s=["con", "sme"], lc="everyday", o="A", neo=[1, "Mastercard credit; debit not checked."], src=[["FABMISR: H1 2026", MISRH1], ["FABMISR: credit cards", MISRCC]]),
            P("ksa", "FAB in Saudi Arabia", "A full-service bank licensed in 2018 with branches in three cities, and FAB Capital, cleared for wider investment business in March 2024; named in the 2024 Mastercard deal.",
              s=["corp"], lc="grow", div="ksa", o="B", neo=[None, "Covered by the 2024 deal ⚠."], src=[["FAB: Saudi branch, Oct 2019", KHOBAR], ["FAB: investment services, Mar 2024", KSAINV], ["GCC Business News: exclusive deal, Mar 2024", MCEXCL]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: FAB Mobile with Apple Pay, the Payit app in four languages, 140-plus branches, corporate portals and co-brand partners from ADNOC to Etihad.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "FAB Mobile", "blurb": "Accounts in minutes.", "div": "fab", "rev": "pbwpc", "products": [
            P("app", "FAB Mobile app", "Instant account opening with an Emirates ID, card controls, instant international transfers, Apple Pay and Jaywan applications.",
              s=["con", "aff"], lc="open", neo=[1, "Carries Mastercard and Visa cards."], src=[["FAB: mobile banking", MOBILE], ["FAB: accounts", ACCTS]]),
            P("payitapp", "Payit app", "Payit in English, Arabic, Hindi and Urdu for wallet, Universal Account and remittances.",
              s=["work"], lc="open", div="payit", neo=[1, "Mastercard remittances; Visa card."], src=[["FAB: Payit Universal Account, May 2026", PAYITUA]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & portals", "blurb": "140+ branches, FABeAccess.", "div": "group", "rev": "intl", "products": [
            P("branches", "Branches & network", "More than 140 branches across more than 20 markets.",
              s=["con", "corp"], lc="everyday", neo=[0, ""], src=[["Forbes Middle East 2026", FORBES]]),
            P("portals", "Corporate channels", "FABeAccess and iBanking corporate online banking, trade online and FAB Securities services, now joined by the API portal.",
              s=["corp"], lc="move", neo=[0, ""], src=[["FAB: subsidiaries and channels", SUBS], ["FAB: API portal, Oct 2026", APIP]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partners", "blurb": "ADNOC, Etihad, Al-Futtaim.", "div": "fab", "rev": "pbwpc", "products": [
            P("partners", "Co-brand & loyalty partners", "ADNOC Distribution, du and GEMS on Mastercard; Etihad Guest, Majid Al Futtaim (SHARE) and Al-Futtaim (Blue) on Visa.",
              s=["con"], lc="beyond", neo=[1, "Split between networks."], src=[["FAB: credit cards", CC], ["Gulf News: ADNOC card, Dec 2025", ADNOC]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at FAB", "blurb": "Exclusive since 2024.", "products": [
        P("mcatfab", "Mastercard at FAB", "An exclusive long-term global partnership signed in March 2024 across the UAE, Saudi Arabia, Oman and Egypt, under which FAB consolidated its portfolios on Mastercard: debit, own-brand credit, commercial cards and a run of firsts (five cards in six months, McLaren Access Pass, ADNOC, the Rewards Active ring, World Legend Exclusive). Visa keeps the Etihad, SHARE and Blue co-brands and Payit's card.",
          s=["con"], div="group", rev="pbwpc", mc="The relationship this map is drawn for.",
          src=[["GCC Business News: exclusive deal, Mar 2024", MCEXCL], ["Mastercard and FAB: five cards, Aug 2025", MC5]]),
    ]},
    {"id": "pillar-market", "name": "UAE payments", "blurb": "Jaywan, Aani, Network.", "products": [
        P("market", "The UAE market", "FAB (AED 1.41 trillion) and Emirates NBD (above AED 1.3 trillion, 36% of UAE card spend) are the two giants; the Central Bank's programme adds Aani instant payments (2023) and the Jaywan card scheme (2025–26); Network International, with Magnati inside it, is the main acquirer ⚠ network shares not public.",
          s=["con"], div="group", rev="pbwpc", src=[["FAB: H1 2026 results", H1], ["Emirates NBD: H1 2026", ENBDH1], ["CBUAE: Aani launch, Oct 2023", AANI], ["Khaleej Times: Jaywan, Jul 2026", JAYKT]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
