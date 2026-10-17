"""BDO Unibank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own as reported in the Philippine press: the first-half 2026 results (25 July 2026) and
the 2025 results (27 February 2026). BDO's website refused automated requests, so several BDO pages are cited
from search-engine text and marked ⚠. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own
product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1PR = "https://www.bdo.com.ph/content/dam/bdounibank/en-ph/about-bdo/disclosures/all-disclosures/2026/results-july252026-boardmtg-financials-pr.pdf"
SUNH1 = "https://www.sunstar.com.ph/davao/bdo-posts-407b-first-half-net-income"
INSH1 = "https://insiderph.com/bdo-first-half-2026-profit-hits-p407b-as-loans-grow-15"
FY25 = "https://www.philstar.com/business/2026/02/28/2510903/bdo-posts-record-p872-billion-profit-2025/amp/"
Q4Q = "https://quartr.com/events/bdo-unibank-inc-bdo-q4-2025_FMHuXOsS"
RANK = "https://tribune.net.ph/2026/04/17/bdo-stays-on-top-of-philippine-banking"
WIKI = "https://en.wikipedia.org/wiki/BDO_Unibank"
ASM = "https://www.bdo.com.ph/content/dam/bdounibank/en-ph/about-bdo/disclosures/sec-17-c/2026/results-apr242026-asm.pdf"
MC20 = "https://www.sunstar.com.ph/davao/business/bdo-mastercard-mark-20-years-serving-ofws"
MC20B = "https://www.bdo.com.ph/about-bdo/learn/news-and-features/bdo-mastercard-20-years-overseas-filipinos"
EMV16 = "https://www.philstar.com/business/2016/03/21/1564909/bdo-rolls-out-first-emv-mastercard-atm"
VISA14 = "https://www.visa.com.ph/about-visa/newsroom/press-releases/bdo-cardholders-can-now-enjoy-contactless-payments-with-visa-paywave.html"
JCB17 = "https://www.electronicpaymentsinternational.com/news/jcb-international-bdo-unibank-unveil-new-contactless-card"
JCBPLAT = "https://www.theasianbanker.com/press-releases/bdo-jcb-platinum-credit-card-launch"
DINERS = "https://resources.dinersclub.com/home/bdo-unibank-diners-club-philippines"
PROMO = "https://www.bdo.com.ph/personal/cards/credit-and-debit-card-promos/omnibus/upgrade-your-credit-card-now"
CASHCARD = "https://www.bdo.com.ph/accounts/cash-card"
DEBIT = "https://bdo.com.ph/node/12469"
ATM = "https://www.bdo.com.ph/personal/digital/atm"
PAYT = "https://tribune.net.ph/2026/08/17/bdo-pay-named-philippines-best-digital-wallet"
PAYI = "https://insiderph.com/winning-bdo-pay-makes-everyday-digital-payments-simpler"
QRATM = "https://fintechalliance.ph/bdo-to-install-more-machines-for-qr-code-based-use/"
BSP26 = "https://mb.com.ph/2026/08/17/digital-payments-hit-647-of-philippine-retail-transactions-nearing-bsps-70-target"
BANCNET = "https://www.philstar.com/business/2025/02/11/2420601/bancnet-transactions-reach-p114-trillion-2024/amp/"
QRPM = "https://mb.com.ph/2026/07/02/qr-ph-overtakes-cards-e-wallets-to-dominate-philippine-business-paymentspaymongo"
PODIUM = "https://context.ph/2024/10/24/bdo-the-podium-complex-merger-secures-regulatory-approval/"
NOMURA = "https://www.philstar.com/business/2020/11/27/2059655/business"
ONB = "https://www.retailbankerinternational.com/news/philippines-bdo-unibank-acquires-one-network-bank-241214-4477578/"
RCBCV = "https://www.visa.com.ph/about-visa/newsroom/press-releases/visa-and-rcbc-launch-debit-partnership-to-expand-payment-options-for-filipinos.html"
USSCV = "https://www.visa.com.ph/about-visa/newsroom/press-releases/visa-and-ussc-announce-strategic-issuing-and-money-movement-partnership-to-transform-payment-solutions.html"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · SM Group · heritage", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: the Philippines' largest bank by assets, loans, deposits and trust funds, ₱40.7 billion of profit in the first half of 2026, the Sy family's SM Group behind it, and a history of buying banks since 1976.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "Number one; ₱87.2bn in 2025.", "div": "bdo", "rev": "group", "products": [
            P("balance", "Balance sheet & earnings", "Net income of ₱40.7 billion in the first half of 2026 (ROE 12.7%) and a record ₱87.2 billion in 2025 (ROE 14.4%); gross loans up 15% to ₱3.9 trillion and deposits up 13%; NPL ratio 1.64%; CET1 13.1%. Total assets about ₱5.43 trillion at end-2025 ⚠. First by assets, loans, deposits and trust funds.",
              s=["con"], neo=[0, ""], src=[["SunStar: H1 2026 results, Jul 2026", SUNH1], ["Philippine Star: 2025 results, Feb 2026", FY25], ["Quartr: Q4 2025 summary", Q4Q], ["Daily Tribune: BDO stays on top, Apr 2026", RANK]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Sy and Tan.", "div": "bdo", "rev": "group", "products": [
            P("leadership", "Board & executives", "Board elected 24 April 2026 includes Teresita T. Sy (chair ⚠) and Nestor V. Tan (President and CEO), with independent directors including Franklin Drilon and Vicente Perez Jr. Named executives: Genie Gloria (remittance), Roy Villareal (digital, consumer banking). CFO and cards head not confirmed ⚠.",
              s=["corp"], neo=[0, ""], src=[["BDO: 2026 ASM results ⚠", ASM], ["Daily Tribune: BDO Pay award, Aug 2026", PAYT], ["SunStar: BDO and Mastercard, May 2026", MC20]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & SM Group", "blurb": "Acme Savings Bank, 1968.", "div": "bdo", "rev": "group", "products": [
            P("heritage", "Heritage & ownership", "Founded in 1968 as Acme Savings Bank and bought by Henry Sy's SM Group in 1976; grew by buying Dao Heng, 1st e-Bank, Banco Santander Philippines, Equitable PCI (2007), GE Money Bank and One Network Bank. Listed on the PSE; SM Investments the controlling shareholder ⚠ current stake.",
              s=["con"], o="I", neo=[0, ""], src=[["Wikipedia: BDO Unibank", WIKI], ["Retail Banker International: One Network Bank, Dec 2014", ONB]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & operations", "blurb": "Re-engineered after 2020.", "div": "bdo", "rev": "group", "products": [
            P("tech", "Platforms & automation", "End-to-end re-engineering of digital platforms and robotic process automation after 2020 capacity problems; digital transformation named a 2025 priority. No public AI programme ⚠.",
              s=["corp"], neo=[0, ""], src=[["Fintech Alliance: QR ATMs and re-engineering, Feb 2021", QRATM], ["Quartr: Q4 2025 summary", Q4Q]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "Wealth, insurance, MSMEs.", "div": "bdo", "rev": "group", "products": [
            P("strategy", "Strategy", "Grow the core, with focus on wealth management, insurance and MSMEs, plus digital transformation; coal loans to be no more than 2% of the book by 2033.",
              s=["corp"], neo=[0, ""], src=[["Quartr: Q4 2025 summary", Q4Q]]),
            P("deals", "Deals", "Bought Nomura's 49% of BDO Nomura Securities (November 2020) and Keppel's stake in The Podium Complex (December 2023), merged into the bank in November 2024. No bank acquisitions found since 2014 ⚠.",
              s=["corp"], o="A", neo=[0, ""], src=[["Philippine Star: Nomura buyout, Nov 2020", NOMURA], ["Context.ph: Podium merger, Oct 2024", PODIUM]]),
            P("bonds", "Sustainability bonds", "A record ₱115 billion from its fourth peso ASEAN Sustainability Bond (July 2025); a leader in green and blue bonds.",
              s=["corp"], ay="Jul 2025", neo=[0, ""], src=[["Philippine Star: 2025 results, Feb 2026", FY25], ["Quartr: Q4 2025 summary", Q4Q]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: Mastercard ATM debit cards, credit cards on six networks, prepaid cards, twenty years of Mastercard remittances, acquiring for every brand, and free InstaPay, PESONet and QR Ph transfers.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit & ATM cards", "blurb": "Millions on Mastercard.", "div": "bdo", "rev": "consumer", "products": [
            P("debit", "BDO ATM debit cards", "\"Millions\" of BDO ATM cards carry Mastercard and work for remittances and purchases at home and abroad; BDO issued the country's first EMV-chip Mastercard ATM debit cards in 2016. Switched domestically through BancNet.", short="Debit (Mastercard)",
              s=["con", "ofw"], lc="everyday", ay="Mar 2016", o="P", at="Mastercard, BancNet", neo=[2, "Mastercard-branded ATM debit."],
              mc="Mastercard's biggest footprint at BDO, and the card behind the remittance franchise.",
              src=[["Philippine Star: EMV Mastercard ATM, Mar 2016", EMV16], ["SunStar: BDO and Mastercard, May 2026", MC20]]),
            P("visadebit", "BDO Visa debit", "An EMV Visa debit card from 2017; BDO's debit page says the card works wherever Visa or Mastercard is accepted ⚠. Share of each network not public.",
              s=["con"], lc="everyday", st="unconf", ay="2017", o="P", at="Visa", neo=[0, "Visa ⚠."], src=[["Wikipedia: BDO Unibank", WIKI], ["BDO: debit card ⚠", DEBIT]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Six networks.", "div": "cards", "rev": "consumer", "products": [
            P("credit", "BDO credit cards", "The widest set of brands in the country: Mastercard, Visa, American Express, JCB and UnionPay, from Gold (Gold Mastercard, Visa Gold, JCB Gold) to Elite (Platinum Mastercard, Visa Platinum, JCB Platinum, UnionPay Diamond, Amex Platinum). Visa payWave contactless from 2014; JCB contactless and Platinum firsts in 2017. Card count and network split not public ⚠.", short="Credit (multi-network)",
              s=["con", "aff"], lc="borrow", o="P", at="Mastercard, Visa, Amex, JCB, UnionPay", neo=[1, "One network among six."],
              mc="Mastercard competes for every BDO card launch against five other brands.",
              src=[["Visa: BDO payWave, Mar 2014", VISA14], ["The Asian Banker: JCB Platinum, Jul 2017", JCBPLAT], ["BDO: card upgrade promo ⚠", PROMO]]),
            P("diners", "BDO Diners Club", "Exclusive issuer of Diners Club cards in the Philippines since October 2016, including Diners Club Premiere, and Diners' acquiring partner.",
              s=["aff"], lc="borrow", ay="Oct 2016", o="P", at="Diners Club (Discover)", neo=[0, "Diners Club."], src=[["Diners Club: BDO, Oct 2016", DINERS]]),
        ]},
        {"id": "2.3", "ic": "wallet", "name": "Prepaid", "blurb": "Cash Card to Pay Card.", "div": "pay", "rev": "consumer", "products": [
            P("paycard", "BDO Cash Card & BDO Pay Card", "The prepaid Cash Card was usable until 20 July 2026 ⚠ and is being replaced by the free BDO Pay Card, a debit card linked to a Basic Account. Network not confirmed ⚠.",
              s=["con"], lc="open", st="flux", ay="Jul 2026", neo=[None, "Network not confirmed."], src=[["BDO: Cash Card advisory ⚠", CASHCARD]]),
        ]},
        {"id": "2.4", "ic": "earth", "name": "Remittances", "blurb": "20 years with Mastercard.", "div": "remit", "rev": "consumer", "products": [
            P("remit", "Remittances with Mastercard", "Twenty years (2006–2026) of combining BDO's remittance network with Mastercard's payments infrastructure, reaching more than 4 million Filipinos abroad; 13 international offices. In May 2026 both promised new cross-border security and convenience in 2026.", short="Remittances (Mastercard)",
              s=["ofw"], lc="move", st="active", o="P", at="Mastercard", neo=[2, "Mastercard's infrastructure."],
              mc="The relationship's anchor; Visa Direct is spreading to BPI, USSC and GCash.",
              src=[["SunStar: BDO and Mastercard, May 2026", MC20], ["BDO: 20 years with Mastercard ⚠", MC20B], ["InsiderPH: BDO Pay, Aug 2026", PAYI]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acquiring", "blurb": "Every brand accepted.", "div": "bdo", "rev": "commercial", "products": [
            P("acquiring", "Merchant acquiring", "BDO terminals accept Mastercard, Visa, Amex, JCB and UnionPay plus BancNet, MegaLink and Expressnet (2014), Diners Club (2016) and JCB J/Speedy (2017). Terminal count and market share not public ⚠.",
              s=["merch", "sme"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["Visa: BDO payWave, Mar 2014", VISA14], ["Diners Club: BDO, Oct 2016", DINERS], ["Electronic Payments International: J/Speedy, Jun 2017", JCB17]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Instant & QR", "blurb": "InstaPay, PESONet, QR Ph.", "div": "pay", "rev": "consumer", "products": [
            P("instapay", "InstaPay & PESONet transfers", "Free InstaPay and PESONet transfers in BDO Pay, with online transaction fees waived from July 2026. Nationally the two rails carried 4.2 billion transfers worth ₱16.09 trillion in the first half of 2026.",
              s=["con", "sme"], lc="move", st="new", ay="Jul 2026", o="P", at="BancNet, PCHC", neo=[0, "Domestic instant rails."],
              src=[["Daily Tribune: BDO Pay award, Aug 2026", PAYT], ["Manila Bulletin: BSP digital payments, Aug 2026", BSP26]]),
            P("qrph", "QR Ph payments & QR ATM", "QR Ph payments ⚠ and cardless QR withdrawals at more than 100 ATMs (2021). QR Ph passed card transactions nationally in 2025: 2.47 billion worth ₱1.16 trillion.",
              s=["con", "merch"], lc="move", o="P", at="QR Ph", neo=[0, "National QR standard."],
              mc="QR Ph is taking card share at the point of sale.",
              src=[["Fintech Alliance: QR ATMs, Feb 2021", QRATM], ["Manila Bulletin: BSP digital payments, Aug 2026", BSP26]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: chip cards and account security after a 2021 hack, rewards and wallet promotions, and data and AI with nothing public.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "EMV first; a 2021 hack.", "div": "bdo", "rev": "consumer", "products": [
            P("emv", "EMV chip cards", "First EMV-chip Mastercard ATM debit cards in the country (2016), with a three-year migration from magnetic stripe.",
              s=["con"], lc="everyday", ay="Mar 2016", o="P", at="Mastercard", neo=[2, "Mastercard EMV debit."], src=[["Philippine Star: EMV Mastercard ATM, Mar 2016", EMV16]]),
            P("fraud", "Account fraud & scams", "A December 2021 hack moved money out of customer accounts ⚠; free instant transfers since July 2026 raise exposure to scams. No named fraud tools in public sources ⚠.",
              s=["con"], lc="everyday", neo=[None, "No public fraud partner."],
              mc="Account-to-account scam scoring fits the surge in free instant transfers.",
              src=[["Wikipedia: BDO Unibank", WIKI], ["Daily Tribune: BDO Pay award, Aug 2026", PAYT]]),
        ]},
        {"id": "3.2", "ic": "gift", "name": "Rewards & offers", "blurb": "Points and wallet promos.", "div": "cards", "rev": "consumer", "products": [
            P("rewards", "Card rewards & promotions", "BDO Rewards points ⚠ and card upgrade and spend promotions across the Gold and Elite tiers.",
              s=["con", "aff"], lc="grow", neo=[None, "Bank-run promotions."], src=[["BDO: card upgrade promo ⚠", PROMO]]),
            P("payrewards", "BDO Pay rewards", "Rewards and promotions inside BDO Pay, and a referral offer (₱100 for the referrer, ₱50 for the new user, 1 July–30 September 2026).",
              s=["con"], lc="grow", st="new", neo=[0, ""],
              mc="Card-linked offers could feed the wallet's rewards.",
              src=[["Daily Tribune: BDO Pay award, Aug 2026", PAYT]]),
        ]},
        {"id": "3.3", "ic": "brain", "name": "Data & AI", "blurb": "Nothing public.", "div": "bdo", "rev": "group", "products": [
            P("data", "Data, AI & insights", "No public AI or data programme found; BDO Pay offers balance and spending tracking ⚠.",
              s=["con"], lc="everyday", st="unconf", neo=[None, "Nothing public."], src=[["InsiderPH: BDO Pay, Aug 2026", PAYI]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: corporate, commercial and MSME loans, consumer loans and deposits, the country's largest trust business, BDO Private Bank and BDO Life, capital markets and leasing, and rural banking through BDO Network Bank.",
    "tiles": [
        {"id": "4.1", "ic": "building-2", "name": "Corporate & MSME", "blurb": "Double-digit loan growth.", "div": "bdo", "rev": "corporate", "products": [
            P("corp", "Corporate banking", "Loans to large corporates, growing at double digits in the first half of 2026 as gross loans reached ₱3.9 trillion.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["SunStar: H1 2026 results, Jul 2026", SUNH1], ["InsiderPH: H1 2026 results, Jul 2026", INSH1]]),
            P("msme", "Commercial & MSME banking", "Middle-market and MSME lending, a named strategic focus, with double-digit growth.",
              s=["sme"], lc="borrow", neo=[0, ""],
              mc="Commercial cards and payment controls for MSMEs are untested ground.",
              src=[["Quartr: Q4 2025 summary", Q4Q], ["SunStar: H1 2026 results, Jul 2026", SUNH1]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Consumer loans & deposits", "blurb": "₱4.19tn of deposits.", "div": "bdo", "rev": "consumer", "products": [
            P("loans", "Consumer lending", "Cards, home and auto loans, growing at double digits in 2025 and 2026; book sizes not public ⚠.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["SunStar: H1 2026 results, Jul 2026", SUNH1], ["Philippine Star: 2025 results, Feb 2026", FY25]]),
            P("deposits", "Deposits & accounts", "About ₱4.19 trillion of deposits at end-2025 (up 10%), 68% of them current and savings accounts; deposits up 13% in the first half of 2026.",
              s=["con", "ofw"], lc="everyday", neo=[1, "Mastercard and Visa debit ⚠."], src=[["Quartr: Q4 2025 summary", Q4Q], ["Philippine Star: 2025 results, Feb 2026", FY25], ["InsiderPH: H1 2026 results, Jul 2026", INSH1]]),
        ]},
        {"id": "4.3", "ic": "gem", "name": "Trust, wealth & insurance", "blurb": "Number one in trust.", "div": "private", "rev": "wealth", "products": [
            P("trust", "Trust & BDO Private Bank", "The largest trust business in the country (₱1.80 trillion of AUM in 2024) and BDO Private Bank, the former Banco Santander Philippines (2003).",
              s=["aff"], lc="grow", o="A", neo=[0, ""], src=[["Wikipedia: BDO Unibank", WIKI], ["Daily Tribune: BDO stays on top, Apr 2026", RANK]]),
            P("life", "BDO Life & insurance", "BDO Life Assurance and BDO Insurance Brokers; insurance income up 10% in 2025 and 14% in the first half of 2026.",
              s=["aff", "con"], lc="grow", neo=[0, ""], src=[["Philippine Star: 2025 results, Feb 2026", FY25], ["SunStar: H1 2026 results, Jul 2026", SUNH1]]),
        ]},
        {"id": "4.4", "ic": "chart-candlestick", "name": "Capital markets & leasing", "blurb": "BDO Capital, Securities.", "div": "capital", "rev": "corporate", "products": [
            P("capital", "BDO Capital & BDO Securities", "Investment banking and stockbroking; BDO Securities absorbed BDO Nomura after the 2020 buyout.",
              s=["corp", "aff"], lc="grow", o="A", neo=[0, ""], src=[["Wikipedia: BDO Unibank", WIKI], ["Philippine Star: Nomura buyout, Nov 2020", NOMURA]]),
            P("leasing", "BDO Leasing and Finance", "Equipment leasing and finance for businesses.",
              s=["sme"], lc="borrow", neo=[0, ""], src=[["Wikipedia: BDO Unibank", WIKI]]),
        ]},
        {"id": "4.5", "ic": "flag", "name": "Rural banking", "blurb": "BDO Network Bank.", "div": "network", "rev": "commercial", "products": [
            P("network", "BDO Network Bank", "A rural bank, bought as One Network Bank (105 branches) in December 2014 and renamed in 2019.",
              s=["sme", "con"], lc="everyday", o="A", neo=[None, ""], src=[["Retail Banker International: One Network Bank, Dec 2014", ONB], ["Wikipedia: BDO Unibank", WIKI]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach BDO: the country's largest network of more than 2,000 branches and 7,900 teller machines, the BDO Pay wallet, BDO Online, and 13 offices abroad.",
    "tiles": [
        {"id": "5.1", "ic": "building", "name": "Branches & ATMs", "blurb": "2,000+ and 7,900+.", "div": "bdo", "rev": "consumer", "products": [
            P("branches", "Branches", "More than 2,000 consolidated operating branches (August 2026), up from 1,892 at end-2025: the largest network in the country.",
              s=["con", "sme"], lc="open", neo=[0, ""], src=[["InsiderPH: BDO Pay, Aug 2026", PAYI], ["Quartr: Q4 2025 summary", Q4Q]]),
            P("atms", "ATMs & teller machines", "Over 7,900 teller machines (August 2026); ₱18 for non-BDO cards under acquirer-based fees; QR cardless withdrawals.",
              s=["con", "ofw"], lc="everyday", neo=[1, "Takes Mastercard and BancNet cards."], src=[["InsiderPH: BDO Pay, Aug 2026", PAYI], ["BDO: ATM banking ⚠", ATM], ["Fintech Alliance: QR ATMs, Feb 2021", QRATM]]),
        ]},
        {"id": "5.2", "ic": "smartphone", "name": "BDO Pay", "blurb": "Best wallet, 2026.", "div": "pay", "rev": "consumer", "products": [
            P("bdopay", "BDO Pay", "A wallet linked straight to BDO accounts and cards, with no cash-in: pay in store, transfer, split bills and pay bills. Best Digital Wallet in the Philippines at The Asian Banker awards (August 2026). User count not public ⚠.",
              s=["con"], lc="everyday", st="new", neo=[None, "Cards inside it are multi-network."],
              mc="Tokenised Mastercard debit and credit could ride inside it.",
              src=[["Daily Tribune: BDO Pay award, Aug 2026", PAYT], ["InsiderPH: BDO Pay, Aug 2026", PAYI]]),
        ]},
        {"id": "5.3", "ic": "monitor", "name": "BDO Online", "blurb": "Fees waived, July 2026.", "div": "bdo", "rev": "consumer", "products": [
            P("online", "BDO Online & digital banking", "Online and mobile banking, used to create QR withdrawal codes; online transaction fees waived from July 2026. User numbers not public ⚠.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["Fintech Alliance: QR ATMs, Feb 2021", QRATM], ["Daily Tribune: BDO Pay award, Aug 2026", PAYT]]),
        ]},
        {"id": "5.4", "ic": "plane", "name": "Offices abroad", "blurb": "13 international offices.", "div": "remit", "rev": "consumer", "products": [
            P("intl", "International offices & remittance partners", "Thirteen international offices and remittance partners serving overseas Filipinos and their families.",
              s=["ofw"], lc="move", neo=[1, "Mastercard remittance partner."], src=[["InsiderPH: BDO Pay, Aug 2026", PAYI], ["SunStar: BDO and Mastercard, May 2026", MC20]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at BDO", "blurb": "Debit and remittances, 20 years.", "products": [
        P("mcatbdo", "Mastercard at BDO", "Mastercard has carried BDO's ATM debit cards and remittances for 20 years, reaching more than 4 million Filipinos abroad, and BDO issued the first EMV Mastercard debit cards in the country (2016). In credit Mastercard is one of six brands alongside Visa, Amex, JCB, UnionPay and Diners, and Visa has some BDO debit ⚠. No public tokenisation, fraud or open-finance work together ⚠.",
          s=["con"], div="bdo", rev="group", mc="The relationship this map is drawn for.",
          src=[["SunStar: BDO and Mastercard, May 2026", MC20], ["Philippine Star: EMV Mastercard ATM, Mar 2016", EMV16]]),
    ]},
    {"id": "pillar-market", "name": "Philippine payments", "blurb": "QR Ph and instant rails.", "products": [
        P("market", "The Philippine market", "Digital payments were 64.7% of retail volume in 2025, against a 70% target; InstaPay and PESONet moved ₱24.7 trillion in 2025, QR Ph passed cards, and BancNet switches 2.37 billion transactions a year. Visa signed RCBC debit (January 2026) and Visa Direct deals with USSC and others.",
          s=["con"], div="bdo", rev="group",
          src=[["Manila Bulletin: BSP digital payments, Aug 2026", BSP26], ["Philippine Star: BancNet 2024", BANCNET], ["Visa: RCBC debit, Jan 2026", RCBCV], ["Visa: USSC, Apr 2025", USSCV], ["Manila Bulletin: QR Ph overtakes cards, Jul 2026", QRPM]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
