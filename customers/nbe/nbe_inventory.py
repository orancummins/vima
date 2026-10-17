"""National Bank of Egypt's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own as reported in the Egyptian press unless a source says otherwise: the 2025 results
(reported 5 October 2026, with figures to end-August 2026) and executive interviews. NBE's own site could not be
read directly. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it,
2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

FY25 = "https://www.dailynewsegypt.com/2026/10/05/national-bank-of-egypt-2025-net-profit-rises-to-egp-175-5bn/"
FY25Z = "https://www.zawya.com/en/special-coverage/equities/national-bank-of-egypt-2025-net-profit-rises-to-3.34bln-1510685"
FORBES26 = "https://www.forbesmiddleeast.com/lists/top-100-ceos-2026/mohamed-el-etreby/"
BOARD24 = "https://enterpriseam.com/egypt/?p=644168"
WIKI = "https://en.wikipedia.org/wiki/National_Bank_of_Egypt"
FOTOUH = "https://www.bankygate.com/66615"
KSA = "https://en.sharikatmubasher.com/media-hub/news/21511811/national-bank-of-egypt-opens-1st-branch-in-saudi-arabia?lang=en"
KSA2 = "https://meobserver.news/business-economix/market-updates-finance/2025/10/19/nbe-sets-foot-in-saudi-market-with-high-tech-riyadh-branch-aiming-at-bilateral-business-growth/"
UEFA24 = "https://www.mastercard.com/news/eemea/en/newsroom/press-releases/en/2024/february/mastercard-and-the-national-bank-of-egypt-announce-the-launch-of-a-uefa-champions-league-mastercard-credit-card"
UEFA26 = "https://financialit.net/news/infrastructure/mastercard-brings-uefa-champions-league-trophy-egypt-together-national-bank"
UEFAOFF = "https://www.banker.news/129840"
USDDC = "https://www.albawabhnews.com/5390830"
FXLIM = "https://enterpriseam.com/egypt/2024/05/15/nbe-raises-limits-on-fx-transactions/"
FXLIM2 = "https://en.amwalalghad.com/?p=153858"
VISAUSD = "https://techbuild.africa/national-bank-of-egypt-us-dollar-credit-card/"
VISADC = "https://www.elwatannews.com/news/details/8212251"
MEEZADC = "https://www.bnok24.com/?p=10420"
PHONECASH = "https://www.bnok24.com/?p=8600"
APPLEPAY = "https://www.businesstodayegypt.com/amp/1/5671/Apple-Pay-initially-launches-in-partnership-with-3-Egyptian-banks"
MPGS = "https://nbe.gateway.mastercard.com/static/checkout/checkout.min.js"
HOME = "https://www.nbe.com.eg/NBE/E/"
APP22 = "https://www.albawabhnews.com/4635595"
IPN26 = "https://arabfinance.com/en/news/newdetails/egypt-instant-payment-network-transactions-by-end-of-q2-2026"
IPNFEE = "https://egyptianstreets.com/2025/04/03/instapay-now-charging-transfer-fees"
IPNWAIVE = "https://en.amwalalghad.com/?p=187926"
GULF = "https://www.sharikatmubasher.com/media-hub/news/21451621/egypt-to-enable-gulf-remittances-via-instapay-in-2-months"
MOMKEN = "https://enterpriseam.com/egypt/2021/03/10/nbe-pushing-into-non-bank-financial-services/"
NBEUK = "https://www.nbeuk.com/"
MEEZA = "https://meeza-eg.com/"
FITCH = "https://arabfinance.com/en/news/newdetails/fitch-affirms-egypt-b-rating-with-stable-outlook"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · owners · heritage", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Egypt's largest bank, with an EGP 9.2 trillion balance sheet at end-2025, wholly owned by the state, founded in 1898, run since September 2024 by Mohamed El-Etreby, and set on digital transformation and regional growth.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "EGP 9.2tn; EGP 175.5bn profit.", "div": "nbe", "rev": "treasury", "products": [
            P("balance", "Balance sheet & earnings", "Net profit EGP 175.5 billion in 2025 (EGP 133.3 billion in 2024) on pre-tax profit of EGP 312.5 billion; total assets EGP 9.2 trillion (up 13%), deposits EGP 5.7 trillion, loans EGP 4.8 trillion, equity EGP 690 billion and an NPL ratio of 0.8%. By end-August 2026 assets were about EGP 10.6 trillion.",
              s=["corp"], neo=[0, ""], src=[["Daily News Egypt: 2025 results, Oct 2026", FY25], ["Zawya: 2025 results", FY25Z]]),
            P("ratings", "Ratings & market share", "Ratings move with the sovereign, which Fitch holds at B with a stable outlook ⚠; Moody's has the bank's deposits at Caa1 ⚠ undated. The bank says it holds about 44% of Egypt's banking market ⚠ measure not defined.",
              s=["corp"], neo=[0, ""], src=[["Arab Finance: Fitch affirms Egypt at B", FITCH], ["Banky: Abou El Fotouh interview, Nov 2025", FOTOUH]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Owners & leadership", "blurb": "State-owned; El-Etreby CEO.", "div": "nbe", "rev": "treasury", "products": [
            P("owners", "State ownership", "Wholly owned by the Egyptian state since nationalisation in 1960 and not listed, so it has no market value; boards are named by the government for three-year terms.",
              s=["corp"], o="I", neo=[0, ""], src=[["Wikipedia: National Bank of Egypt", WIKI], ["Enterprise: new boards, Sep 2024", BOARD24]]),
            P("leadership", "Board & management", "CEO Mohamed El-Etreby since September 2024, after a swap with Hisham Okasha, who went to Banque Misr; non-executive chairman Mohamed Barakat ⚠ Wikipedia names Mohamed Kamal Al Din; deputy CEO Soha El-Turky, a former EBRD vice president; executive deputy chairman Yehia Abou El Fotouh. Staff 29,162 in 2024; Forbes says more than 35,000 ⚠.",
              s=["corp"], neo=[0, ""], src=[["Enterprise: new boards, Sep 2024", BOARD24], ["Forbes Middle East: El-Etreby, 2026", FORBES26], ["Banky: Abou El Fotouh interview, Nov 2025", FOTOUH]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage", "blurb": "Founded 1898.", "div": "nbe", "rev": "retail", "products": [
            P("brand", "Heritage", "Founded on 25 June 1898 with Sir Ernest Cassel among the founders; acted as Egypt's central bank until 1960; took over Lloyds Bank's Cairo and Alexandria branches (1925) and Citibank's Egyptian business (1961); co-founded CIB with Chase Manhattan (1975); bought Mohandes Bank and the Bank of Commerce and Development (2005).",
              s=["con"], o="I", neo=[0, ""], src=[["Wikipedia: National Bank of Egypt", WIKI]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "AI across channels.", "div": "nbe", "rev": "treasury", "products": [
            P("tech", "Digital platform & AI", "AI used across electronic channels; a standalone digital bank has been proposed, but the stated focus is improving existing services (November 2025). A web chatbot is linked from the homepage. Core banking vendor and AI targets not published ⚠.",
              s=["corp"], st="flux", neo=[0, ""], src=[["Banky: Abou El Fotouh interview, Nov 2025", FOTOUH], ["NBE website", HOME]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "Digital and regional growth.", "div": "nbe", "rev": "treasury", "products": [
            P("strategy", "Digital transformation & regional expansion", "Priorities named in November 2025: digital transformation, the first Egyptian bank branch in Saudi Arabia, a larger DIFC centre in Dubai and a study of Iraq; about 85% of new financing requests come from the private sector. No numerical targets published ⚠.",
              s=["corp"], st="new", neo=[0, ""], src=[["Banky: Abou El Fotouh interview, Nov 2025", FOTOUH], ["Mubasher: Saudi branch, Oct 2025", KSA]]),
            P("ebrd", "EBRD MSME facility", "A US$100 million EBRD financing agreement for micro, small and medium-sized enterprises, signed in December 2025.",
              s=["sme"], st="new", ay="Dec 2025", o="P", at="EBRD", neo=[0, ""], src=[["Forbes Middle East: El-Etreby, 2026", FORBES26]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: 8.4 million debit cards on Meeza, Visa and Mastercard; 1.9 million credit cards in parallel Visa and Mastercard ranges; a large POS estate and a Mastercard Gateway for online sales; 717 million InstaPay transfers in 2025; the Phone Cash wallet and Apple Pay; and an overseas network for trade and remittances.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit & prepaid cards", "blurb": "8.4 million, mostly Meeza ⚠.", "div": "nbe", "rev": "retail", "products": [
            P("meezadebit", "Meeza debit card", "The domestic-only debit card on Egypt's national scheme: EGP 30 to issue, EGP 12,000 a day in cash, EGP 100,000 a day in purchases, contactless without a PIN up to EGP 600 (2021 terms). NBE had 8.4 million debit cards in 2025; the split by network is not published ⚠.", short="Meeza debit",
              s=["con", "unb"], lc="everyday", o="P", at="Meeza", neo=[0, "Meeza."],
              mc="The mass debit base sits on the national scheme.",
              src=[["Bnok24: NBE Meeza debit card, Nov 2021", MEEZADC], ["Daily News Egypt: 2025 results, Oct 2026", FY25]]),
            P("visadebit", "Visa debit cards", "International debit cards on Visa, from EGP 150 to issue or free under CBE inclusion schemes, contactless and able to be added to phone wallets; several accounts can be linked to one card.", short="Visa debit",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Elwatan: NBE Visa debit, Jan 2026", VISADC]]),
            P("mcdebit", "Mastercard debit", "NBE issues Mastercard cards alongside Visa and Meeza; its Phone Cash wallet accepts 'Ahly Mastercard, Visa or Meeza' cards. No consumer Mastercard debit product page was found ⚠.", short="Mastercard debit ⚠",
              s=["con"], lc="everyday", st="unconf", o="P", at="Mastercard", neo=[1, "One of three debit networks ⚠ split unknown."],
              src=[["Bnok24: Phone Cash, Nov 2021", PHONECASH]]),
            P("usddebit", "USD corporate debit card", "A US dollar debit card for large corporates and SMEs to pay foreign suppliers, service providers and digital platforms, launched with Mastercard on 27 July 2026 by deputy CEO Soha El-Turky and Mastercard's Mohamed Assem; available at all branches.", short="USD corporate debit (Mastercard)",
              s=["corp", "sme"], lc="move", st="new", ay="Jul 2026", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="The newest joint launch, and a base for commercial cards.",
              src=[["Al Bawaba: USD corporate debit, Jul 2026", USDDC]]),
            P("prepaid", "Prepaid cards", "NBE prepaid cards can be linked to the Phone Cash wallet; the network behind them is not stated ⚠.",
              s=["unb"], lc="everyday", o="P", neo=[None, "Network not stated ⚠."], src=[["Bnok24: Phone Cash, Nov 2021", PHONECASH]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "1.9 million; Visa and Mastercard.", "div": "nbe", "rev": "retail", "products": [
            P("credit", "NBE credit cards", "1.9 million credit cards in 2025, in parallel ranges: Visa Classic, Gold and Platinum, and Mastercard Standard, Titanium and Platinum. Monthly FX limits were raised in March and May 2024 after the pound floated. The split by network is not published ⚠.", short="Credit (Visa and Mastercard)",
              s=["con"], lc="borrow", o="P", at="Visa, Mastercard", neo=[1, "Visa and Mastercard ⚠ split unknown."],
              mc="The country's largest bank, with Mastercard on an even footing in credit.",
              src=[["Daily News Egypt: 2025 results, Oct 2026", FY25], ["Enterprise: FX limits, May 2024", FXLIM], ["Amwal Al Ghad: card limits, Mar 2024", FXLIM2]]),
            P("mcprem", "Mastercard World & World Elite", "The top Mastercard tier, with the highest FX limit of the equivalent of EGP 60,000 a month since May 2024.", short="World Elite (Mastercard)",
              s=["aff"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard World and World Elite."],
              src=[["Enterprise: FX limits, May 2024", FXLIM], ["Amwal Al Ghad: card limits, Mar 2024", FXLIM2]]),
            P("visaprem", "Visa Signature & Infinite", "The top Visa tier, in the same EGP 60,000 FX band as World and World Elite.", short="Infinite (Visa)",
              s=["aff"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Enterprise: FX limits, May 2024", FXLIM]]),
            P("uefa", "UEFA Champions League Mastercard", "Egypt's first UEFA Champions League co-branded credit card, launched with Mastercard in February 2024 for customers from 18; the trophy toured Egypt with NBE in February 2026, and spend draws offered travel vouchers up to EGP 10,000 in March 2026.", short="UCL card (Mastercard)",
              s=["con"], lc="borrow", ay="Feb 2024", o="P", at="Mastercard, UEFA", neo=[2, "Mastercard co-brand."],
              mc="Mastercard's flagship sponsorship turned into a card.",
              src=[["Mastercard: UCL card launch, Feb 2024", UEFA24], ["Financial IT: UCL trophy in Egypt, Feb 2026", UEFA26], ["Banker: UCL card draw, Mar 2026", UEFAOFF]]),
            P("egyptair", "EgyptAir Mastercard", "A co-branded credit card with the national airline, in the entry FX tier. Loyalty terms not found ⚠.", short="EgyptAir (Mastercard)",
              s=["con", "aff"], lc="borrow", o="P", at="Mastercard, EgyptAir", neo=[2, "Mastercard co-brand."],
              src=[["Enterprise: FX limits, May 2024", FXLIM]]),
            P("usdcredit", "Visa US dollar credit card", "A dollar credit card for holders of dollar certificates, with limits from USD 2,000 to USD 50,000, launched with Visa ⚠ date not given, about 2024.", short="USD credit (Visa)",
              s=["aff"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["TechBuild Africa: Visa USD credit card", VISAUSD]]),
        ]},
        {"id": "2.3", "ic": "store", "name": "Acquiring & e-commerce", "blurb": "758,000 POS ⚠; Mastercard Gateway.", "div": "nbe", "rev": "retail", "products": [
            P("pos", "POS acquiring", "758,000 POS terminals in 2025, as the bank reports them ⚠ large against the market and may include group terminals. Accepts Meeza, Visa and Mastercard ⚠ inferred.",
              s=["sme"], lc="move", o="B", neo=[1, "Accepts every network ⚠."],
              mc="Acquirer risk and merchant data for one of Egypt's biggest estates.",
              src=[["Daily News Egypt: 2025 results, Oct 2026", FY25]]),
            P("mpgs", "Online payment gateway", "NBE's e-commerce acceptance runs on its own Mastercard Gateway instance, live at nbe.gateway.mastercard.com in October 2026. Start date not published ⚠.", short="Mastercard Gateway",
              s=["sme", "corp"], lc="move", o="P", at="Mastercard", neo=[3, "Mastercard Gateway."],
              mc="Mastercard's own product already runs NBE's online acceptance.",
              src=[["NBE Mastercard Gateway checkout", MPGS]]),
        ]},
        {"id": "2.4", "ic": "zap", "name": "InstaPay transfers", "blurb": "717 million in 2025.", "div": "nbe", "rev": "retail", "products": [
            P("instapay", "InstaPay through NBE", "About 717 million InstaPay transfers worth EGP 2.87 trillion in 2025, up 91% in value from 333 million worth EGP 1.5 trillion in 2024. InstaPay has charged 0.1% a transfer (EGP 0.50 to EGP 20) since 1 April 2025.",
              s=["con", "sme"], lc="move", o="P", at="Central Bank of Egypt", neo=[0, "CBE's Instant Payment Network."],
              mc="Account-to-account payments far outnumber card payments.",
              src=[["Daily News Egypt: 2025 results, Oct 2026", FY25], ["Egyptian Streets: InstaPay fees, Apr 2025", IPNFEE]]),
        ]},
        {"id": "2.5", "ic": "smartphone", "name": "Wallets & tokens", "blurb": "Phone Cash, Apple Pay.", "div": "nbe", "rev": "retail", "products": [
            P("phonecash", "Al Ahly Phone Cash", "A mobile wallet on a phone number, open to customers and non-customers from 16: wallet transfers, Fawry bills, QR payments, cash in and out at branches, ATMs and Fawry, and 24-hour single-use virtual cards for online purchases at home and abroad (2021 terms). Virtual card network not stated ⚠.", short="Phone Cash wallet",
              s=["con", "unb"], lc="everyday", o="B", at="Fawry", neo=[None, "Virtual card network not stated ⚠."],
              src=[["Bnok24: Phone Cash, Nov 2021", PHONECASH]]),
            P("applepay", "Apple Pay", "Live from 10 December 2024, with NBE among the first three banks; Meeza cards can be added to Apple Wallet. Which NBE networks are tokenised is not confirmed ⚠; Google Pay not confirmed in Egypt ⚠.",
              s=["con"], lc="everyday", ay="Dec 2024", o="P", at="Apple", neo=[1, "Tokens on each card's network ⚠."],
              src=[["Business Today Egypt: Apple Pay, Dec 2024", APPLEPAY], ["Meeza", MEEZA]]),
        ]},
        {"id": "2.6", "ic": "earth", "name": "Cross-border & remittances", "blurb": "Gulf inflows, trade.", "div": "intl", "rev": "intl", "products": [
            P("remit", "Remittances & trade flows", "Branches in New York, Shanghai and, since October 2025, Saudi Arabia, with offices in Dubai, Johannesburg and Addis Ababa; the CBE approved inbound Gulf remittances through InstaPay in November 2024. NBE's remittance volumes are not published ⚠.",
              s=["exp", "corp"], lc="move", o="B", neo=[0, ""],
              mc="Inbound remittances from the Gulf are untested ground for Mastercard Move.",
              src=[["Daily News Egypt: 2025 results, Oct 2026", FY25], ["Mubasher: Gulf remittances via InstaPay, Nov 2024", GULF]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: chip and PIN, SMS alerts, biometrics and tokens; co-brand draws and campaigns on Mastercard and points on Visa; and self-service, a personal finance manager and AI in the app and chatbot.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "Chip, alerts, tokens.", "div": "nbe", "rev": "retail", "products": [
            P("security", "Card & channel security", "Chip and PIN and free SMS alerts on cards; biometric log-in and soft or hard tokens in Al Ahly Net and NBE Mobile. No Mastercard or Visa fraud product named ⚠.",
              s=["con", "sme"], lc="everyday", o="B", neo=[0, "No scheme fraud tool named ⚠."],
              mc="No scam or instant-payment fraud scoring in public view.",
              src=[["Bnok24: NBE Meeza debit card, Nov 2021", MEEZADC], ["Al Bawaba: new Al Ahly Net, Aug 2022", APP22]]),
        ]},
        {"id": "3.2", "ic": "gift", "name": "Rewards & offers", "blurb": "UCL draws, Visa points.", "div": "nbe", "rev": "retail", "products": [
            P("offers", "Campaigns & rewards", "UEFA Champions League card draws for travel vouchers (March 2026) and an international-spend campaign on Mastercard Titanium and UCL cards (August 2026 ⚠ from secondary reports); points and cashback promotions on Visa cards.",
              s=["con", "aff"], lc="grow", o="P", at="Mastercard, Visa", neo=[1, "Mastercard on co-brands, Visa on its range."],
              src=[["Banker: UCL card draw, Mar 2026", UEFAOFF], ["Elwatan: NBE Visa debit, Jan 2026", VISADC]]),
        ]},
        {"id": "3.3", "ic": "brain", "name": "Self-service & data", "blurb": "PFM, chatbot, AI.", "div": "nbe", "rev": "retail", "products": [
            P("pfm", "Personal finance manager & self-service", "Expense tracking and categories, card activation, suspension and PIN reset, I-Score credit reports and applications for loans and cards inside the app (from August 2022).",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["Al Bawaba: new Al Ahly Net, Aug 2022", APP22]]),
            P("chatbot", "Chatbot & AI", "A web chatbot linked from the homepage and AI across electronic channels; no usage figures and no open-banking APIs published ⚠.",
              s=["con"], lc="everyday", st="new", o="B", neo=[0, ""], src=[["NBE website", HOME], ["Banky: Abou El Fotouh interview, Nov 2025", FOTOUH]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: retail banking for 21.7 million customers, EGP 438 billion of retail loans, the country's largest corporate book at EGP 4.2 trillion, EGP 195 billion of SME finance, non-bank and payments businesses under Al Ahly Capital, and an international network from London to Saudi Arabia.",
    "tiles": [
        {"id": "4.1", "ic": "users-round", "name": "Retail banking", "blurb": "21.7 million customers.", "div": "nbe", "rev": "retail", "products": [
            P("retail", "Retail accounts & deposits", "21.7 million customers in 2025 (23.5 million cited in November 2025 ⚠); customer deposits EGP 5.7 trillion at December 2025 and EGP 6.4 trillion by August 2026.",
              s=["con"], lc="open", neo=[1, "Debit on Meeza, Visa and Mastercard."], src=[["Daily News Egypt: 2025 results, Oct 2026", FY25], ["Banky: Abou El Fotouh interview, Nov 2025", FOTOUH]]),
        ]},
        {"id": "4.2", "ic": "hand-coins", "name": "Consumer lending", "blurb": "EGP 506bn by August.", "div": "nbe", "rev": "retail", "products": [
            P("loans", "Retail loans", "Retail lending of EGP 438 billion at December 2025, up 23%, and EGP 506 billion by August 2026; personal and car loans can be applied for in the app.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Daily News Egypt: 2025 results, Oct 2026", FY25], ["Al Bawaba: new Al Ahly Net, Aug 2022", APP22]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Corporate & trade", "blurb": "EGP 4.2tn corporate book.", "div": "nbe", "rev": "corp", "products": [
            P("corporate", "Corporate lending", "Corporate loans of EGP 4.2 trillion at December 2025, up 23%, and above EGP 5 trillion by August 2026; about 85% of new requests from the private sector.",
              s=["corp"], lc="borrow", neo=[0, ""],
              mc="Commercial and virtual cards are absent from the corporate offer.",
              src=[["Daily News Egypt: 2025 results, Oct 2026", FY25], ["Banky: Abou El Fotouh interview, Nov 2025", FOTOUH]]),
            P("corpcards", "Corporate credit cards", "Corporate credit cards sit in the top FX band, the equivalent of EGP 60,000 a month since May 2024; network not stated ⚠.",
              s=["corp"], lc="move", o="P", neo=[None, "Network not stated ⚠."], src=[["Enterprise: FX limits, May 2024", FXLIM]]),
        ]},
        {"id": "4.4", "ic": "briefcase", "name": "SME & microfinance", "blurb": "EGP 218bn SME by August.", "div": "nbe", "rev": "sme", "products": [
            P("sme", "SME banking", "SME finance of EGP 195 billion at December 2025, up 13%, and EGP 218 billion by August 2026; EBRD US$100 million for MSMEs (December 2025); USD debit for SMEs with Mastercard (July 2026).",
              s=["sme"], lc="borrow", neo=[1, "USD debit on Mastercard."],
              mc="SME debit opens the door to business credit and payment controls.",
              src=[["Daily News Egypt: 2025 results, Oct 2026", FY25], ["Forbes Middle East: El-Etreby, 2026", FORBES26], ["Al Bawaba: USD corporate debit, Jul 2026", USDDC]]),
            P("micro", "Tamkeen microfinance", "Tamkeen, the group's non-bank platform, was set up for consumer finance, leasing, micro-insurance, factoring and microfinance, with plans in 2021 for 150 microfinance branches over three years, starting in Upper Egypt. Current figures not published ⚠.",
              s=["unb", "sme"], lc="borrow", o="B", neo=[0, ""], src=[["Enterprise: NBE non-bank push, Mar 2021", MOMKEN]]),
        ]},
        {"id": "4.5", "ic": "network", "name": "Al Ahly Capital & Momkn", "blurb": "Non-bank and payments.", "div": "alcap", "rev": "retail", "products": [
            P("alcap", "Al Ahly Capital Holding", "The holding company for the group's non-bank financial services and investments, which bought 75% of the e-payments firm Momken in March 2021 for a reported EGP 100–140 million.",
              s=["corp"], lc="beyond", o="B", neo=[0, ""], src=[["Enterprise: NBE non-bank push, Mar 2021", MOMKEN]]),
            P("momkn", "Al Ahly Momkn", "An e-payments company, 75% owned through Al Ahly Capital, for bill and digital payments; trades as Al Ahly Momkn ⚠ rebrand from secondary reports.",
              s=["con", "unb"], lc="move", o="A", neo=[None, "Nothing public."], src=[["Enterprise: NBE non-bank push, Mar 2021", MOMKEN]]),
        ]},
        {"id": "4.6", "ic": "globe", "name": "International", "blurb": "London to Saudi Arabia.", "div": "intl", "rev": "intl", "products": [
            P("nbeuk", "National Bank of Egypt (UK)", "A wholly owned London bank, set up in 1982, authorised by the PRA and regulated by the FCA and PRA: personal and corporate banking, buy-to-let mortgages, deposits and trade finance, mainly for the Egyptian community.",
              s=["exp", "corp"], lc="open", o="B", neo=[0, ""], src=[["NBE (UK)", NBEUK], ["Wikipedia: National Bank of Egypt", WIKI]]),
            P("ksa", "Saudi Arabia branch", "The first Egyptian bank branch in Saudi Arabia, licensed in 2021 and opened on 16 October 2025 after Saudi Central Bank approval, for corporate banking and trade finance.",
              s=["corp", "exp"], lc="move", st="new", ay="Oct 2025", o="B", neo=[0, ""],
              mc="A foothold in the largest source of remittances to Egypt.",
              src=[["Mubasher: Saudi branch, Oct 2025", KSA], ["ME Observer: Saudi branch, Oct 2025", KSA2]]),
            P("intlnet", "Branches & offices abroad", "Branches in New York and Shanghai, offices in Dubai (DIFC), Johannesburg and Addis Ababa, and units in Sudan and South Sudan ⚠ current status not checked; Iraq under study.",
              s=["corp"], lc="move", st="flux", neo=[0, ""], src=[["Daily News Egypt: 2025 results, Oct 2026", FY25], ["Wikipedia: National Bank of Egypt", WIKI], ["Banky: Abou El Fotouh interview, Nov 2025", FOTOUH]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach NBE: Al Ahly Net and NBE Mobile, more than 700 branches and units including 38 electronic branches, and 7,572 ATMs.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Al Ahly Net & NBE Mobile", "blurb": "Relaunched 2022.", "div": "nbe", "rev": "retail", "products": [
            P("ahlynet", "Al Ahly Net & NBE Mobile", "Internet and mobile banking relaunched in August 2022 with transfers, wallet top-ups, certificates, loan and card applications, Fawry bills and biometric log-in; a million downloads of the new app then. Current user numbers are not published in a dated source ⚠.",
              s=["con", "aff"], lc="everyday", o="B", neo=[0, ""], src=[["Al Bawaba: new Al Ahly Net, Aug 2022", APP22]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches", "blurb": "700+ branches and units.", "div": "nbe", "rev": "retail", "products": [
            P("branches", "Branch network", "More than 700 branches and units across Egypt including 38 electronic service branches (2025); Forbes counts 679 branches.",
              s=["con", "sme", "corp"], lc="open", neo=[0, ""], src=[["Daily News Egypt: 2025 results, Oct 2026", FY25], ["Forbes Middle East: El-Etreby, 2026", FORBES26]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "ATMs", "blurb": "7,572 ATMs.", "div": "nbe", "rev": "retail", "products": [
            P("atms", "ATM network", "7,572 ATMs in 2025, with free withdrawals for NBE cardholders and wallet cash-out for Phone Cash users.",
              s=["con", "unb"], lc="everyday", neo=[0, ""], src=[["Daily News Egypt: 2025 results, Oct 2026", FY25], ["Bnok24: Phone Cash, Nov 2021", PHONECASH]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at NBE", "blurb": "Co-brands, USD debit, gateway.", "products": [
        P("mcatnbe", "Mastercard at NBE", "Mastercard runs a credit range alongside Visa's, from Standard to World Elite, holds the UEFA Champions League (2024) and EgyptAir co-brands, launched a USD corporate debit card in July 2026 and provides the Mastercard Gateway for online acceptance. Meeza carries the mass debit base and InstaPay the account transfers; Visa holds debit and a USD credit card.",
          s=["con"], div="nbe", rev="retail", mc="The relationship this map is drawn for.",
          src=[["Mastercard: UCL card launch, Feb 2024", UEFA24], ["Al Bawaba: USD corporate debit, Jul 2026", USDDC], ["NBE Mastercard Gateway checkout", MPGS], ["Enterprise: FX limits, May 2024", FXLIM]]),
    ]},
    {"id": "pillar-market", "name": "Egypt payments", "blurb": "Meeza, InstaPay, wallets.", "products": [
        P("market", "The Egyptian market", "InstaPay, launched in April 2022, recorded 1.47 billion transactions worth EGP 4.33 trillion and 22 million registered customers by the end of Q2 2026 ⚠ period basis unclear; fees of 0.1% since April 2025; Meeza, the national scheme, cites 17 million cards and 22 million wallets ⚠ undated; Apple Pay since December 2024.",
          s=["con"], div="nbe", rev="retail",
          src=[["Arab Finance: IPN by Q2 2026", IPN26], ["Amwal Al Ghad: CBE fee waiver, Dec 2024", IPNWAIVE], ["Meeza", MEEZA], ["Business Today Egypt: Apple Pay, Dec 2024", APPLEPAY]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
