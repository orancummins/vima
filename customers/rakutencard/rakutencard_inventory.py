"""Rakuten Card's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are Rakuten's own unless a source says otherwise: the Q2 2026 and FY2025 investor presentations, the
20 May 2026 reorganisation agreement and the 30 September 2026 business-card release. Rakuten Card's own website
could not be read, so card brands per product rest partly on secondary sources (marked ⚠). ``neo`` is the
Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard,
1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

REORG = "https://corp.rakuten.co.jp/news/press/2026/0520_11.html"
EFFECT = "https://corp.rakuten.co.jp/news/press/2026/1001_11.html"
RESTART = "https://corp.rakuten.co.jp/news/press/2026/0225_13.html"
JCRRB = "https://jcr.co.jp/download/cad5b0f4dbfd9e7048ab4b12fbd05a2a4f65b8270454a92d64/26d0220.pdf"
JCRRG = "https://www.jcr.co.jp/download/afc8c4f3571972c77a797b035f6e2aaaca2907214a3e121209/26d0215_1.pdf"
Q2PPT = "https://global.rakuten.com/corp/investors/assets/doc/documents/26Q2PPT_E.pdf"
FY25PPT = "https://global.rakuten.com/corp/investors/assets/doc/documents/25Q4PPT_E.pdf"
Q1PR = "https://global.rakuten.com/corp/news/press/2026/0514_01.html"
PNQ2 = "https://paymentnavi.com/?p=180280"
BIZPLAT = "https://corp.rakuten.co.jp/news/press/2026/0930_01.html"
AIAGENT = "https://corp.rakuten.co.jp/news/press/2026/0219_02.html"
CHATAI = "https://prtimes.jp/main/html/rd/p/000000183.000035783.html"
MYNUM = "https://paymentnavi.com/paymentnews/174277.html"
CASHPAY = "https://paymentnavi.com/paymentnews/176551.html"
PAYBAL = "https://corp.rakuten.co.jp/news/press/2026/0508_01.html"
TRAVEL = "https://corp.rakuten.co.jp/news/press/2026/0202_03.html"
PANDA = "https://paymentnavi.com/paymentnews/183185.html"
MZCAP = "https://corp.rakuten.co.jp/news/press/2024/1113_12.html"
MZALL = "https://corp.rakuten.co.jp/news/press/2024/1113_02.html"
MZCARD = "https://corp.rakuten.co.jp/news/press/2024/1114_03.html"
PRES = "https://www2.jpx.co.jp/disc/47550/140120241205534830.pdf"
WIKI = "https://ja.wikipedia.org/wiki/%E6%A5%BD%E5%A4%A9%E3%82%AB%E3%83%BC%E3%83%89"
APPLE16 = "https://www.rakuten-card.co.jp/corporate/press_release/20161025/"
APPLE21 = "https://www.rakuten-card.co.jp/support/customer/voice/202107_2/"
VISACAMP = "https://www.rakuten-card.co.jp/campaign/spt/visa_applepay/"
VOIX = "https://voix.jp/?p=123768"
BRANDS = "https://appllio.com/rakuten-card-visa-jcb-mastercard-amex"
US14 = "https://paymentnavi.com/?p=39012"
RBDEBIT = "https://paymentnavi.com/?p=94281"
CASHLESS = "https://www.watch.impress.co.jp/docs/news/2099068.html"
SCBRI = "https://www.scbri.jp/reports/.assets/newstopics_20260403.pdf"
FRAUD = "https://ecnomikata.com/ecnews/marketing/49820/"
PAYPAY = "https://about.paypay.ne.jp/en/pr/20260810/01/"
QUARTR = "https://quartr.com/events/rakuten-bank-ltd-5838-corporate-presentation_FkdIm7WS"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "volume · ownership · funding", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Japan's biggest card book by spend, ¥26.5 trillion in 2025, a company now owned outright by Rakuten Bank, Mizuho as a partner, and a plan to cut funding costs and join up the bank, card and securities customer bases.",
    "tiles": [
        {"id": "1.1", "ic": "chart-column", "name": "Scale & results", "blurb": "34 million cards, ¥26.5tn spend.", "div": "rcard", "rev": "card", "products": [
            P("scale", "Scale & earnings", "34.31 million cards issued at end-June 2026; shopping GTV of ¥26.5 trillion in 2025 (+10.3%) and ¥7.1 trillion in Q2 2026 (+9.4%); revenue of ¥385.2 billion and Non-GAAP operating income of ¥63.5 billion in 2025, and ¥107.9 billion and ¥17.4 billion in Q2 2026; card loans of ¥3.59 trillion at 30 June 2026.",
              s=["con"], neo=[0, ""], src=[["Rakuten Q2 2026 presentation", Q2PPT], ["Rakuten FY2025 presentation", FY25PPT], ["Business Card Platinum release, Sep 2026", BIZPLAT]]),
            P("rank", "Number one by spend", "Rakuten Bank calls Rakuten Card Japan's largest issuer by shopping volume, ¥27.7 trillion over the 12 months to June 2026 ⚠; set against ¥134.6 trillion of Japanese credit card payments in 2025, its 2025 spend is about a fifth of the market ⚠ (this map's arithmetic).",
              s=["con"], neo=[0, ""], src=[["Rakuten Bank presentation summary ⚠", QUARTR], ["SCBRI: 2025 cashless mix", SCBRI]]),
            P("ratings", "Credit ratings", "JCR long-term issuer rating A-, stable, equal to the Rakuten group's credit, unchanged by the October 2026 reorganisation.",
              s=["corp"], neo=[0, ""], src=[["JCR on Rakuten Bank, Card and Securities, May 2026", JCRRB]]),
        ]},
        {"id": "1.2", "ic": "building-2", "name": "Ownership", "blurb": "Under Rakuten Bank since 1 October.", "div": "rbank", "rev": "bank", "products": [
            P("reorg", "Rakuten Bank group", "On 1 October 2026 Rakuten Card became a wholly owned subsidiary of Rakuten Bank (TSE Prime), alongside Rakuten Securities HD; Rakuten Group keeps about 49.9% of Rakuten Bank's votes and about 72% of its economic interest. Rakuten Payment was moved out to Rakuten Group first, valued at ¥100 billion.",
              s=["corp"], st="new", ay="Oct 2026", o="I", neo=[0, ""],
              mc="The card's owner is now a bank whose debit card already runs on Mastercard.",
              src=[["Reorganisation agreement, May 2026", REORG], ["Reorganisation effective, Oct 2026", EFFECT], ["JCR on Rakuten Group, May 2026", JCRRG]]),
            P("mizuho", "Mizuho stake", "Mizuho bought 14.99% of Rakuten Card for about ¥165 billion in December 2024; in October 2026 it swapped that stake for about 10.5% of Rakuten Bank's votes.",
              s=["corp"], ay="Dec 2024", o="P", at="Mizuho", neo=[0, ""], src=[["Rakuten Card and Mizuho capital alliance, Nov 2024", MZCAP], ["Reorganisation agreement, May 2026", REORG]]),
        ]},
        {"id": "1.3", "ic": "scale", "name": "Leadership", "blurb": "Nakamura and Mikitani.", "div": "rcard", "rev": "card", "products": [
            P("leaders", "Board & management", "President Koichi Nakamura (since March 2025, succeeding Masayuki Hosaka ⚠), chairman Hiroshi Mikitani, Rakuten Group's founder and CEO; Rakuten Bank, the new parent, is led by Tomotaka Tobayashi; 3,432 staff on a consolidated basis.",
              s=["corp"], neo=[0, ""], src=[["Reorganisation agreement, May 2026", REORG], ["Rakuten disclosure on the president, Dec 2024 ⚠", PRES], ["Business Card Platinum release, Sep 2026", BIZPLAT]]),
        ]},
        {"id": "1.4", "ic": "badge-check", "name": "Heritage", "blurb": "From Aozora Card, 2001.", "div": "rgroup", "rev": "card", "products": [
            P("heritage", "Heritage", "Founded in December 2001 as Aozora Card by Aozora Bank and Orix, bought by Rakuten in 2004, and renamed Rakuten Card in August 2011 after taking over the card business of Rakuten KC (formerly Kokunai Shinpan) ⚠.",
              s=["con"], o="A", neo=[0, ""], src=[["Japanese Wikipedia: Rakuten Card ⚠", WIKI], ["Rakuten Card and Mizuho capital alliance, Nov 2024", MZCAP]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & synergies", "blurb": "About ¥85bn a year targeted.", "div": "rbank", "rev": "bank", "products": [
            P("synergy", "Bank, card & securities synergies", "Funding the card book from Rakuten Bank (about ¥53 billion a year) and joint marketing and products (about ¥32 billion), about ¥33 billion in the year to March 2028 and about ¥85 billion a year or more in the medium term; Rakuten Bank settlement accounts hold 4.3 times the balances of other cardholders.",
              s=["con", "bank"], st="new", neo=[0, ""], src=[["Reorganisation agreement, May 2026", REORG], ["Payment Navi on Q2 2026, Aug 2026", PNQ2], ["JCR on Rakuten Bank, Card and Securities, May 2026", JCRRB]]),
            P("funding", "Funding & rates", "Bonds and borrowings for the card business were ¥718.8 billion at June 2026; Bank of Japan rate rises lifted funding costs, offset by higher revolving and instalment rates.",
              s=["corp"], st="flux", neo=[0, ""], src=[["Rakuten Q2 2026 presentation", Q2PPT]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: the standard Rakuten Card on all four brands, gold, premium and black tiers, co-brands with Mizuho, ANA and Alpen, principal memberships of Visa and Mastercard plus JCB and Amex, acquiring, wallets and contactless, and revolving, instalment and cash-advance credit.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Rakuten Card", "blurb": "One card, four brands.", "div": "rcard", "rev": "card", "products": [
            P("classic", "Rakuten Card", "No annual fee and 1% back in Rakuten Points; Visa, Mastercard, JCB or American Express, chosen at application and not changeable after issue; many designs, including Panda designs renewed in October 2026.", short="Rakuten Card (4 brands)",
              s=["con", "shop"], lc="everyday", o="B", at="Visa, Mastercard, JCB, Amex", neo=[1, "One of four brands."],
              mc="Japan's biggest card by spend; Mastercard is one choice of four.",
              src=[["Japanese Wikipedia: Rakuten Card ⚠", WIKI], ["Appllio: brand choice, Mar 2026 ⚠", BRANDS], ["Payment Navi: Panda designs ⚠", PANDA]]),
            P("academy", "Rakuten Academy Card", "Student card with travel and points benefits, on Visa or JCB.", short="Academy (Visa, JCB)",
              s=["con"], lc="open", at="Visa, JCB", neo=[0, "Visa or JCB."], src=[["Japanese Wikipedia: Rakuten Card ⚠", WIKI]]),
        ]},
        {"id": "2.2", "ic": "gem", "name": "Gold, Premium & Black", "blurb": "Mastercard on the Black Card.", "div": "rcard", "rev": "card", "products": [
            P("gold", "Rakuten Gold Card", "Lower-cost gold card on Visa, Mastercard or JCB.", short="Gold (V, M, J)",
              s=["con"], lc="everyday", at="Visa, Mastercard, JCB", neo=[1, "One of three brands."], src=[["Japanese Wikipedia: Rakuten Card ⚠", WIKI]]),
            P("premium", "Rakuten Premium Card", "Gold-tier travel card on Visa, Mastercard, JCB or Amex; sole proprietors can add the Rakuten Business Card to it.", short="Premium (4 brands)",
              s=["prem"], lc="everyday", at="Visa, Mastercard, JCB, Amex", neo=[1, "One of four brands."], src=[["Japanese Wikipedia: Rakuten Card ⚠", WIKI], ["Business Card Platinum release, Sep 2026", BIZPLAT]]),
            P("black", "Rakuten Black Card", "Platinum-tier card on Mastercard, JCB or Amex, with no Visa option ⚠; Mastercard tier not confirmed.", short="Black (M, J, A)",
              s=["prem"], lc="everyday", at="Mastercard, JCB, Amex", neo=[1, "Mastercard, JCB or Amex."],
              mc="The top tier is one where Visa is absent.",
              src=[["Japanese Wikipedia: Rakuten Card ⚠", WIKI]]),
        ]},
        {"id": "2.3", "ic": "users-round", "name": "Co-brands", "blurb": "Mizuho on Visa, Alpen on Mastercard.", "div": "mizuho", "rev": "card", "products": [
            P("mizuhocard", "Mizuho Rakuten Card", "Co-brand with Mizuho Bank from 3 December 2024: Rakuten Points and Mizuho ATM benefits, on Visa only.", short="Mizuho Rakuten (Visa)",
              s=["con", "bank"], lc="everyday", st="new", ay="Dec 2024", o="P", at="Mizuho Bank", neo=[0, "Visa."],
              src=[["Mizuho Rakuten Card, Nov 2024", MZCARD], ["Six-company alliance, Nov 2024", MZALL]]),
            P("ana", "Rakuten ANA Mileage Club Card", "Co-brand with ANA earning miles or points, on Visa, Mastercard or JCB.", short="ANA (V, M, J)",
              s=["prem"], lc="everyday", o="P", at="ANA", neo=[1, "One of three brands."], src=[["Japanese Wikipedia: Rakuten Card ⚠", WIKI]]),
            P("alpen", "Alpen & My Color Selection cards", "The Alpen Group Rakuten Card and Rakuten Card My Color Selection are Mastercard only; the Hiroshima Bank co-brand is Visa only ⚠.", short="Alpen, My Color (Mastercard)",
              s=["con"], lc="everyday", o="P", at="Alpen Group", neo=[2, "Mastercard only."], src=[["Japanese Wikipedia: Rakuten Card ⚠", WIKI]]),
        ]},
        {"id": "2.4", "ic": "network", "name": "Network memberships", "blurb": "Visa, Mastercard, JCB, Amex.", "div": "rcard", "rev": "card", "products": [
            P("netvisa", "Visa", "Principal member of Visa; Visa appears to be the majority choice (about 55.5% of users, one consumer site ⚠); every new Rakuten programme of 2024–26 and the 2026 Apple Pay cashback campaigns are Visa.", short="Visa (principal member)",
              s=["con"], lc="move", at="Visa", neo=[0, "Visa."],
              mc="Visa holds the new launches and the brand marketing.",
              src=[["Japanese Wikipedia: Rakuten Card ⚠", WIKI], ["Rakuten Card: Visa touch campaign ⚠", VISACAMP], ["voix.jp: Visa Apple Pay cashback, Sep 2026 ⚠", VOIX]]),
            P("netmc", "Mastercard", "Principal member of Mastercard; Mastercard is on the standard, Gold, Premium, Black, ANA, Alpen and My Color Selection cards and is the only brand accepted at Costco Japan ⚠. No card-count or volume split is published.", short="Mastercard (principal member)",
              s=["con", "prem"], lc="move", at="Mastercard", neo=[2, "Mastercard-branded cards."],
              mc="One of four brands, strongest at the top tier and in co-brands.",
              src=[["Japanese Wikipedia: Rakuten Card ⚠", WIKI], ["Appllio: brand choice, Mar 2026 ⚠", BRANDS]]),
            P("netjcb", "JCB & American Express", "JCB cards issued in partnership with JCB (the only brand on the Rakuten Bank Card); American Express cards since September 2018, which do not work with Apple Pay or Google Pay ⚠.", short="JCB & Amex",
              s=["con"], lc="move", ay="Sep 2018", at="JCB, American Express", neo=[0, "JCB and Amex."],
              src=[["Japanese Wikipedia: Rakuten Card ⚠", WIKI], ["Appllio: brand choice, Mar 2026 ⚠", BRANDS]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acquiring", "blurb": "Mastercard acquiring since 2011.", "div": "rcard", "rev": "card", "products": [
            P("acquiring", "Merchant acquiring", "Rakuten Card acquires card payments for merchants, adding Mastercard to Visa in about December 2011 ⚠; with Mizuho, UC Card and Orico it plans shared acquiring and back office and mutual access to merchant networks of several million each (November 2024).", short="Acquiring",
              s=["merch"], lc="move", ay="Dec 2011", o="B", at="Mizuho, UC Card, Orico", neo=[1, "Acquires Mastercard among others ⚠."],
              mc="Rakuten is both issuer and acquirer on its own marketplace.",
              src=[["Japanese Wikipedia: Rakuten Card ⚠", WIKI], ["Six-company alliance, Nov 2024", MZALL]]),
        ]},
        {"id": "2.6", "ic": "smartphone", "name": "Wallets & contactless", "blurb": "Apple Pay, Edy, Rakuten Pay.", "div": "rpay", "rev": "payment", "products": [
            P("applepay", "Apple Pay & Google Pay", "Apple Pay for Mastercard and JCB cards from October 2016 and for Visa from 2021; Amex cards are not supported; Visa paid for Apple Pay cashback campaigns in mid-2026 and from September 2026 ⚠.", short="Apple Pay (M, J 2016; V 2021)",
              s=["con"], lc="everyday", ay="Oct 2016", o="P", at="Apple, Google", neo=[1, "Mastercard first in 2016."],
              src=[["Rakuten Card: Apple Pay, Oct 2016 ⚠", APPLE16], ["Rakuten Card: Visa on Apple Pay, 2021 ⚠", APPLE21], ["voix.jp: Visa Apple Pay cashback, Sep 2026 ⚠", VOIX]]),
            P("paycharge", "Rakuten Pay & Edy funding", "Rakuten Card funds Rakuten Pay and built-in Rakuten Edy e-money; from 2 July 2026 a cash advance can top up a withdrawable Rakuten Pay balance from ¥1,000. Rakuten Payment moved to Rakuten Group before 1 October 2026.",
              s=["con", "shop"], lc="move", st="new", ay="Jul 2026", neo=[0, "Rakuten's own wallet."],
              src=[["Payment Navi: cash advance to Rakuten Pay, Jul 2026", CASHPAY], ["Rakuten Pay balance renaming, May 2026", PAYBAL], ["Reorganisation agreement, May 2026", REORG]]),
        ]},
        {"id": "2.7", "ic": "hand-coins", "name": "Revolving & instalments", "blurb": "Rates raised as funding rose.", "div": "rcard", "rev": "card", "products": [
            P("revolving", "Revolving & instalments", "Revolving and instalment repayment on every card, with rates raised in 2025–26 to offset higher funding costs; Rakuten Travel took card instalments as a booking option in February 2026; Orico's AI credit scoring is being studied for digital instalments ⚠.",
              s=["con", "shop"], lc="borrow", st="flux", neo=[1, "Rides on each card's brand."],
              src=[["Rakuten Q2 2026 presentation", Q2PPT], ["Rakuten Travel instalments, Feb 2026", TRAVEL], ["Six-company alliance, Nov 2024", MZALL]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every card: fraud controls against Japan's ¥51 billion of card fraud and My Number identity checks, an AI agent in the English app and AI in chat support, Rakuten Points across the ecosystem, and funding from Rakuten Bank.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & identity", "blurb": "¥51bn of fraud in Japan.", "div": "rcard", "rev": "card", "products": [
            P("fraud", "Fraud controls", "Japanese card fraud losses were ¥51.05 billion in 2025 (−8.0%), ¥47.5 billion from stolen card numbers; Rakuten Card shares fraud methods and countermeasures with Mizuho's card companies under the 2024 alliance. Its own tools are not described in the sources read ⚠.",
              s=["con", "merch"], lc="everyday", o="P", at="Mizuho, UC Card, Orico", neo=[None, "Nothing public."],
              mc="Number theft is the problem tokens and passkeys address.",
              src=[["ECのミカタ: 2025 card fraud", FRAUD], ["Six-company alliance, Nov 2024", MZALL]]),
            P("mynumber", "My Number verification", "Since May 2026 the iOS Rakuten Card app uses the My Number card on iPhone to verify the customer before showing the card number ⚠.",
              s=["con"], lc="everyday", st="new", ay="May 2026", neo=[0, ""], src=[["Payment Navi: card-number display ⚠", MYNUM]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI", "blurb": "An agent in Rakuten Card Lite.", "div": "rcard", "rev": "card", "products": [
            P("aiagent", "AI agent", "Rakuten's in-house AI agent in the English-language Rakuten Card Lite app from 19 February 2026, answering spending questions in Japanese and English from 14 months of statements; due in the main app during 2026.",
              s=["con"], lc="everyday", st="new", ay="Feb 2026", o="B", neo=[0, ""],
              mc="Agentic purchases are the next step; Agent Pay is untouched here.",
              src=[["AI agent in Rakuten Card Lite, Feb 2026", AIAGENT]]),
            P("chatai", "AI in chat support", "AI search across Rakuten Card chat support from April 2026 ⚠.",
              s=["con"], lc="everyday", st="new", ay="Apr 2026", o="B", neo=[0, ""], src=[["PR Times: AI chat support ⚠", CHATAI]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Points & offers", "blurb": "1% in Rakuten Points.", "div": "rgroup", "rev": "card", "products": [
            P("points", "Rakuten Points", "1% back on card spend, more on Rakuten Ichiba and Travel; the Business Card Platinum earns 3x on Ichiba, 3.5x on domestic Travel and bonus points on Rakuten Mobile lines, with Visa Business Offers alongside.",
              s=["con", "shop", "sme"], lc="grow", neo=[0, "Rakuten's own points."],
              src=[["Business Card Platinum release, Sep 2026", BIZPLAT], ["Japanese Wikipedia: Rakuten Card ⚠", WIKI]]),
        ]},
        {"id": "3.4", "ic": "database", "name": "Bank link & data", "blurb": "4.3x balances with Rakuten Bank.", "div": "rbank", "rev": "bank", "products": [
            P("banklink", "Rakuten Bank settlement & data", "Cardholders who settle from Rakuten Bank hold 4.3 times the balances of others; the reorganisation is meant to join customer data and AI across bank, card and securities.",
              s=["bank"], lc="everyday", st="new", neo=[0, ""], src=[["Payment Navi on Q2 2026, Aug 2026", PNQ2], ["Reorganisation agreement, May 2026", REORG]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: consumer cards, new business and corporate cards launched on 1 October 2026 with Mizuho's UPSIDER, cash advances and card loans, Taiwan Rakuten Card, and the Rakuten Bank group around them.",
    "tiles": [
        {"id": "4.1", "ic": "briefcase-business", "name": "Business & corporate cards", "blurb": "Platinum on Visa, from October.", "div": "mizuho", "rev": "card", "products": [
            P("bizplat", "Rakuten Business Card Platinum", "Visa card for companies from 1 October 2026: no annual fee, limits up to ¥1 billion, up to 100 cards to start, accounting integration, built with UPSIDER's credit model and card platform under the Mizuho alliance.", short="Business Platinum (Visa)",
              s=["sme"], lc="everyday", st="new", ay="Oct 2026", o="P", at="UPSIDER, Mizuho", neo=[0, "Visa."],
              mc="The newest card line went to Visa.",
              src=[["Business Card Platinum release, Sep 2026", BIZPLAT]]),
            P("bizcard", "Rakuten Business Card", "Visa add-on to the Rakuten Premium Card for sole proprietors.", short="Business Card (Visa)",
              s=["sme"], lc="everyday", at="Visa", neo=[0, "Visa."], src=[["Business Card Platinum release, Sep 2026", BIZPLAT]]),
            P("corporate", "Rakuten Corporate Card", "Card for large companies, open for applications from 1 October 2026; network not stated ⚠.",
              s=["corp"], lc="everyday", st="new", ay="Oct 2026", neo=[None, "Network not stated."],
              mc="An open network decision for large-company spend.",
              src=[["Business Card Platinum release, Sep 2026", BIZPLAT]]),
        ]},
        {"id": "4.2", "ic": "coins", "name": "Cash advance & loans", "blurb": "¥169bn of cash advances.", "div": "rcard", "rev": "card", "products": [
            P("cashing", "Cash advance & card loans", "Cash advance balance of ¥168.9 billion at March 2026, plus the Rakuten VIP Loan Card ⚠; cash advances can now fund the Rakuten Pay balance.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Reorganisation agreement, May 2026", REORG], ["Payment Navi: cash advance to Rakuten Pay, Jul 2026", CASHPAY]]),
        ]},
        {"id": "4.3", "ic": "earth", "name": "Overseas", "blurb": "Taiwan, and a US past.", "div": "taiwan", "rev": "other", "products": [
            P("taiwan", "Taiwan Rakuten Card", "Wholly owned card issuer in Taiwan ⚠; networks not confirmed. Overseas card subsidiaries are reported under FinTech 'Others'.",
              s=["con"], lc="everyday", neo=[None, "Networks not confirmed."], src=[["Japanese Wikipedia: Rakuten Card ⚠", WIKI], ["Rakuten Q2 2026 presentation", Q2PPT]]),
            P("usa", "Rakuten Rewards MasterCard (US)", "Rakuten Card USA was set up in 2014 to run the Rakuten Rewards MasterCard, issued by FNBO's First Bankcard and earning Rakuten points; current status unknown ⚠.",
              s=["con"], lc="everyday", st="unconf", ay="Apr 2014", o="P", at="FNBO", neo=[2, "Mastercard ⚠ status."],
              src=[["Payment Navi: Rakuten Card USA, Apr 2014", US14]]),
        ]},
        {"id": "4.4", "ic": "landmark", "name": "Rakuten Bank group", "blurb": "18.5m bank accounts.", "div": "rbank", "rev": "bank", "products": [
            P("rakutenbank", "Rakuten Bank", "The new parent: 18.46 million accounts and ¥13.3 trillion of deposits at June 2026; its debit card has been on Mastercard since May 2020.", short="Rakuten Bank (Mastercard debit)",
              s=["bank"], lc="everyday", o="I", at="Mastercard", neo=[1, "Debit on Mastercard."],
              mc="Mastercard already sits in the parent's debit card.",
              src=[["Rakuten Q2 2026 presentation", Q2PPT], ["Payment Navi: Rakuten Bank Mastercard debit, May 2020", RBDEBIT]]),
            P("securities", "Rakuten Securities", "14.39 million accounts and 7.92 million NISA accounts at June 2026, now a sister company under Rakuten Bank; Mizuho Securities keeps 49%.",
              s=["bank"], lc="grow", o="I", neo=[0, ""], src=[["Rakuten Q2 2026 presentation", Q2PPT], ["Reorganisation agreement, May 2026", REORG]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Rakuten Card: the Rakuten Card app and its English sibling, the Rakuten ecosystem of Ichiba, Travel and Mobile, and partner channels through Mizuho, ANA and regional banks.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Apps", "blurb": "Rakuten Card app and Lite.", "div": "rcard", "rev": "card", "products": [
            P("app", "Rakuten Card app & e-NAVI", "Statements, card-number display, cash advance and settings online; app user numbers are not published ⚠.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["Payment Navi: card-number display ⚠", MYNUM], ["Payment Navi: cash advance to Rakuten Pay, Jul 2026", CASHPAY]]),
            P("lite", "Rakuten Card Lite", "English-language app for Rakuten Card members, the first home of the AI agent (February 2026).",
              s=["con"], lc="everyday", st="new", o="B", neo=[0, ""], src=[["AI agent in Rakuten Card Lite, Feb 2026", AIAGENT]]),
        ]},
        {"id": "5.2", "ic": "store", "name": "Rakuten ecosystem", "blurb": "Ichiba, Travel, Mobile.", "div": "rgroup", "rev": "other", "products": [
            P("ichiba", "Rakuten Ichiba, Travel & Mobile", "The ecosystem where the card is acquired and used: domestic e-commerce GMS of ¥1.5 trillion in Q1 2026, Rakuten Travel and Rakuten Mobile, all tied together by Rakuten Points.",
              s=["shop"], lc="open", neo=[0, ""], src=[["Rakuten Q1 2026 results", Q1PR], ["Business Card Platinum release, Sep 2026", BIZPLAT]]),
            P("rakutenpay", "Rakuten Pay", "Rakuten Payment's QR and wallet app, with Rakuten Edy and Rakuten Point Card; ¥29.1 billion of revenue in Q2 2026; moved to Rakuten Group in September 2026. PayPay, the market leader, has 75 million users.",
              s=["con", "shop"], lc="move", st="flux", neo=[0, "Rakuten's own wallet."], src=[["Rakuten Q2 2026 presentation", Q2PPT], ["Reorganisation agreement, May 2026", REORG], ["PayPay: 75 million users, Aug 2026", PAYPAY]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partner channels", "blurb": "Mizuho, ANA, regional banks.", "div": "mizuho", "rev": "card", "products": [
            P("partners", "Partner channels", "Mizuho Bank (the Mizuho Rakuten Card and the business-card alliance), Hiroshima Bank, ANA and Alpen; the business cards are sold only through Rakuten Card's site.",
              s=["con", "sme"], lc="open", o="P", at="Mizuho, ANA, Hiroshima Bank", neo=[0, ""], src=[["Business Card Platinum release, Sep 2026", BIZPLAT], ["Japanese Wikipedia: Rakuten Card ⚠", WIKI]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Rakuten Card", "blurb": "One of four brands, Visa leading.", "products": [
        P("mcatrakuten", "Mastercard at Rakuten Card", "Rakuten Card is a principal member of Mastercard and of Visa and also issues JCB and Amex. Mastercard is on most consumer tiers, alone on the Alpen and My Color Selection cards, and on the Black Card where Visa is absent; it was first on Apple Pay in 2016 and is acquired by Rakuten Card. Visa looks like the majority choice and holds every new programme of 2024–26 ⚠. No network split is published.",
          s=["con"], div="rcard", rev="card", mc="The relationship this map is drawn for.",
          src=[["Japanese Wikipedia: Rakuten Card ⚠", WIKI], ["Business Card Platinum release, Sep 2026", BIZPLAT]]),
    ]},
    {"id": "pillar-market", "name": "Japanese payments", "blurb": "58% cashless, credit-led.", "products": [
        P("market", "The Japanese market", "Cashless payments were 58.0% of consumption in 2025 on METI's new measure (¥162.7 trillion), with credit cards 82.7% of that value; code payments are 10.2%, led by PayPay; card fraud losses were ¥51 billion. The target is 65% by 2030.",
          s=["con"], div="rgroup", rev="other", src=[["Impress Watch: METI cashless ratio, Apr 2026", CASHLESS], ["SCBRI: 2025 cashless mix", SCBRI], ["ECのミカタ: 2025 card fraud", FRAUD]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
