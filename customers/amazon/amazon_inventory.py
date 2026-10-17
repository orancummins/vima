"""Amazon's layers, areas and products, read through payments, as at 17 October 2026 (see page_data.py for the format).

Figures are Amazon's own unless a source says otherwise: the Q2 2026 results (30 July 2026), the FY2025 10-K
(6 February 2026) and the Q2 2026 10-Q, with Synchrony's and Affirm's filings, issuer pages and press for the
card programmes. Q3 2026 results are due in late October. ``neo`` is the Mastercard lens: [depth, note], where
3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

Q2 = "https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Second-Quarter-Results"
Q4 = "https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Fourth-Quarter-Results/default.aspx"
TENK = "https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm"
TENQ = "https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm"
BOARD = "https://www.sec.gov/Archives/edgar/data/1018724/000101872426000036/amzn-20260908.htm"
OPENAI = "https://www.sec.gov/Archives/edgar/data/1018724/000110465926021050/tm267374d1_8k.htm"
MCAP = "https://companiesmarketcap.com/amazon/marketcap/"
AXIO = "https://www.business-standard.com/amp/companies/news/amazon-completes-axio-acquisition-secures-direct-lending-license-in-india-125090400781_1.html"
AFFIRM = "https://www.sec.gov/Archives/edgar/data/1820953/000162828025050159/afrm-20251102.htm"
SYF = "https://www.sec.gov/Archives/edgar/data/1601712/000160171226000006/syf-20251231.htm"
PAY = "https://pay.amazon.com/"
CHASE = "https://creditcards.chase.com/cash-back-credit-cards/amazon-prime-rewards"
BARC = "https://home.barclays/news/press-releases/2024/08/amazon-and-barclays-launch-new-co-branded-credit-card-that-gives"
BIALLO = "https://www.biallo.de/kreditkarte/news/amazon-visa-kreditkarte-mit-partner-santander/"
JAPAN = "https://paymentnavi.com/paymentnews/37622.html"
MEXICO = "https://expansion.mx/empresas/2018/03/13/amazon-mastercard-y-banorte-lanzan-tarjeta-de-debito-en-mexico"
AGENTCORE = "https://www.theblock.co/post/400421/aws-taps-coinbase-and-stripe-to-power-usdc-payments-for-ai-agents"
BWP = "https://buywithprime.amazon.com/"
BFM = "https://www.aboutamazon.com/news/retail/amazon-shopping-app-buy-for-me-brands"
PAYCRYPTO = "https://aws.amazon.com/payment-cryptography/"
VISAAWS = "https://press.aboutamazon.com/aws/2025/12/visa-and-aws-enable-next-generation-agentic-commerce-capabilities"
ONE = "https://thepaypers.com/payments/news/amazon-ends-amazon-one-palm-recognition-payment-system"
ENGADGET = "https://www.engadget.com/amazon-stop-accepting-uk-issued-visa-credit-cards-101233882.html"
BLOOMBERG = "https://www.bloomberg.com/news/articles/2022-02-17/amazon-says-it-s-reached-agreement-with-visa-on-payment-fees"
PULSE = "https://agentpulse.beehiiv.com/p/agentic-commerce-amazon-targets-10b-mastercard-sets-the-rules"
MA10K = "https://www.sec.gov/Archives/edgar/data/1141391/000114139126000013/ma-20251231.htm"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "sales · people · payments entities", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $716.9 billion of sales in 2025 and a first $200 billion quarter, a Seattle leadership led by Andy Jassy, the Amazon Payments companies that sign the payments contracts, and very large bets on AI.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & results", "blurb": "$716.9bn in 2025.", "div": "grp", "rev": "grp", "products": [
            P("results", "Sales & segments", "Net sales of $716.9 billion in 2025 (+12%): North America $426.3 billion, International $161.9 billion, AWS $128.7 billion; operating income $80.0 billion. Q2 2026 sales of $200.6 billion (+20%), the first quarter above $200 billion. Market value about $2.7 trillion at 16 October 2026; about 1.58 million staff.",
              s=["shop"], neo=[0, ""], src=[["Amazon: Q2 2026 results", Q2], ["Amazon 10-K FY2025", TENK], ["CompaniesMarketCap: Amazon, Oct 2026", MCAP]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Jassy, Herrington, Garman.", "div": "grp", "rev": "grp", "products": [
            P("leadership", "Executive officers & board", "Andy Jassy (CEO since July 2021), Doug Herrington (Worldwide Amazon Stores), Matt Garman (AWS), Brian Olsavsky (CFO), Jeff Bezos (Executive Chair); Kevin Mandia joined the board in September 2026. The global head of Amazon Pay could not be confirmed ⚠.",
              s=["shop"], neo=[0, ""], src=[["Amazon 10-K FY2025", TENK], ["Amazon 8-K, Sep 2026", BOARD]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Payments entities", "blurb": "Amazon Payments, Inc.", "div": "pay", "rev": "grp", "products": [
            P("entities", "Amazon Payments, Inc. & Amazon Payments Europe", "The legal counterparties for Amazon's payments contracts (Affirm signs with Amazon Payments, Inc.), with $13.4 billion of standby letters of credit 'primarily related to our payment-related services' at 30 June 2026.",
              s=["mer"], neo=[0, ""], src=[["Amazon 10-Q Q2 2026", TENQ], ["Affirm 8-K, Nov 2025", AFFIRM]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy & AI bets", "blurb": "Anthropic, OpenAI, capex.", "div": "grp", "rev": "grp", "products": [
            P("aibets", "AI investment", "$8.0 billion of Anthropic notes (2023–25), a $35 billion commitment to OpenAI with an AWS deal (February 2026), and capital spending up $66.1 billion year on year in Q2 2026; trailing free cash flow was −$7.6 billion.",
              s=["dev"], st="new", neo=[0, ""], src=[["Amazon 8-K: OpenAI, Feb 2026", OPENAI], ["Amazon: Q2 2026 results", Q2], ["Amazon 10-Q Q2 2026", TENQ]]),
            P("deals", "Payments deals", "Axio (formerly Capital Float), an Indian lending licence, bought in September 2025 for about $200 million; a warrant over up to 15 million Affirm shares; PAYFORT (2017, now Amazon Payment Services) in the Middle East ⚠ not re-verified.",
              s=["shop"], o="A", neo=[0, ""], src=[["Business Standard: Axio, Sep 2025", AXIO], ["Affirm 8-K, Nov 2025", AFFIRM]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: Amazon Pay checkout, US cards on Visa and a Synchrony store card, co-brands abroad (Visa in the UK and Germany, Mastercard in Japan and Mexico), instalments with Affirm and Synchrony, acceptance of every network, and USDC wallets for AI agents.",
    "tiles": [
        {"id": "2.1", "ic": "wallet", "name": "Amazon Pay", "blurb": "Checkout for other merchants.", "div": "pay", "rev": "na", "products": [
            P("amazonpay", "Amazon Pay", "Checkout with an Amazon account on other merchants' sites since 2007, integrated with Shopify, Stripe, BigCommerce, WooCommerce and Adobe Commerce, with Express Payout; about 18 countries (October 2024 ⚠).",
              s=["mer", "shop"], lc="move", neo=[1, "Holds cards on every network."],
              mc="Click to Pay and network tokens could sit behind Amazon Pay on third-party sites.",
              src=[["Amazon Pay", PAY]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "US cards", "blurb": "Prime Visa, Store Card.", "div": "amazon", "rev": "na", "products": [
            P("primevisa", "Prime Visa & Amazon Visa", "Chase-issued Visa cards with no annual fee: 5% back at Amazon, Whole Foods and Chase Travel for Prime members, 2% on gas, dining and transit, 1% elsewhere.", short="Prime Visa (Visa)",
              s=["prime", "shop"], lc="borrow", o="P", at="JPMorgan Chase, Visa", neo=[0, "Visa."],
              mc="The co-brand in Amazon's biggest market is Visa's.",
              src=[["Chase: Prime Visa", CHASE]]),
            P("storecard", "Amazon Store Card & Prime Store Card", "Closed-loop private-label cards from Synchrony, one of its five largest programmes, extended in 2025; top-five agreements run to 2030–35.", short="Store Card (closed loop)",
              s=["shop", "prime"], lc="borrow", o="P", at="Synchrony", neo=[0, "Closed loop, no network."],
              src=[["Synchrony 10-K FY2025", SYF]]),
            P("bizamex", "Amazon Business American Express", "Business cards with American Express: the UK card confirmed in 2021, the US Amazon Business Prime card from prior knowledge ⚠.",
              s=["biz"], lc="borrow", o="P", at="American Express", neo=[0, "American Express."], src=[["Engadget: Amazon UK and Visa, Nov 2021", ENGADGET]]),
        ]},
        {"id": "2.3", "ic": "wallet-cards", "name": "Co-brands abroad", "blurb": "Mastercard in Japan, Mexico.", "div": "amazon", "rev": "intl", "products": [
            P("barclaycard", "Amazon Barclaycard (UK)", "Barclays-issued Visa since 12 August 2024, Amazon's only UK personal co-brand; it replaced a Mastercard card ⚠ issuer.", short="UK Barclaycard (Visa)",
              s=["shop"], lc="borrow", ay="Aug 2024", o="P", at="Barclays, Visa", neo=[0, "Visa."],
              mc="Mastercard lost the UK co-brand to Visa in 2024.",
              src=[["Barclays: Amazon Barclaycard, Aug 2024", BARC], ["Engadget: Amazon UK and Visa, Nov 2021", ENGADGET]]),
            P("devisa", "Amazon Visa (Germany)", "Issued by Santander's Zinia from August 2024, replacing Landesbank Berlin (also Visa); no annual fee, 1% at Amazon, 1.5% FX fee.", short="Germany (Visa)",
              s=["shop"], lc="borrow", ay="Aug 2024", o="P", at="Zinia, Visa", neo=[0, "Visa."], src=[["biallo.de: Amazon Visa, Aug 2024", BIALLO]]),
            P("japanmc", "Amazon Mastercard (Japan)", "Amazon Mastercard and Amazon Prime Mastercard issued by Sumitomo Mitsui Card since February 2014, in Amazon's fourth-largest market ($30.7 billion in 2025); about 1.5% back at Amazon.", short="Japan (Mastercard)",
              s=["shop", "prime"], lc="borrow", ay="Feb 2014", o="P", at="Sumitomo Mitsui Card", neo=[2, "Mastercard, issued by SMBC Card."],
              mc="Mastercard's largest Amazon co-brand.",
              src=[["paymentnavi: Amazon Mastercard", JAPAN], ["Amazon 10-K FY2025", TENK]]),
            P("recargable", "Amazon Recargable (Mexico)", "A reloadable prepaid Mastercard from Banorte (13 March 2018), loaded with cash at more than 25,000 points including OXXO and 7-Eleven, to turn cash into an online payment.", short="Mexico prepaid (Mastercard)",
              s=["shop"], lc="open", ay="Mar 2018", o="P", at="Banorte", neo=[2, "Prepaid Mastercard, issued by Banorte."],
              src=[["Expansión: Amazon Recargable, Mar 2018", MEXICO]]),
            P("canbra", "Canada & Brazil co-brands", "An Amazon.ca Rewards Mastercard (MBNA) and a Bradescard card in Brazil are known only from prior knowledge ⚠; no Mexico credit co-brand was found ⚠.",
              s=["shop"], lc="borrow", st="unconf", neo=[None, "Networks not verified ⚠."],
              mc="Co-brand pipeline: Canada, Brazil and Mexico credit."),
        ]},
        {"id": "2.4", "ic": "hand-coins", "name": "Instalments", "blurb": "Affirm to 2031.", "div": "amazon", "rev": "na", "products": [
            P("affirm", "Affirm instalments", "Live since 2021; a restated agreement runs from 1 February 2026 to January 2031 with one-year renewals, on Amazon.com and the Amazon Pay widget on other sites.",
              s=["shop"], lc="borrow", o="P", at="Affirm", neo=[0, ""], src=[["Affirm 8-K, Nov 2025", AFFIRM]]),
            P("synpaylater", "Synchrony Pay Later", "'Pay monthly' and 'Pay in 4' from Synchrony at Amazon, with Synchrony cards provisioned into Amazon Pay.",
              s=["shop"], lc="borrow", o="P", at="Synchrony", neo=[0, ""], src=[["Synchrony 10-K FY2025", SYF]]),
            P("citiflex", "Citi Flex Pay & card instalments", "Instalments for Citi cardholders, and for Amazon Visa and Prime Visa holders, inside Amazon Pay.",
              s=["shop", "prime"], lc="borrow", o="P", at="Citi, Chase", neo=[0, "Visa for Amazon's cards; Citi's network not stated."], src=[["Amazon Pay", PAY]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acceptance", "blurb": "Every network, one dispute.", "div": "amazon", "rev": "na", "products": [
            P("accept", "Card acceptance", "Cards on every network at Amazon's stores. The 10-K warns interchange 'may increase over time' and that network rules could change; no Amazon–Mastercard acceptance dispute was found from 2015 to 2026.",
              s=["shop", "prime"], lc="move", neo=[1, "Accepts every network."], src=[["Amazon 10-K FY2025", TENK]]),
            P("visadeal", "The 2021–22 Visa dispute", "Amazon UK said it would stop taking UK Visa credit cards from January 2022 over fees, while Mastercard stayed; a global agreement in February 2022 restored Visa, ended surcharges in Singapore and Australia ⚠ and promised joint product work.",
              s=["shop"], lc="move", ay="Feb 2022", o="P", at="Visa", neo=[0, "Visa."],
              src=[["Engadget: Amazon UK and Visa, Nov 2021", ENGADGET], ["Bloomberg: Amazon and Visa agree, Feb 2022", BLOOMBERG]]),
        ]},
        {"id": "2.6", "ic": "coins", "name": "Agent payments", "blurb": "USDC for AI agents.", "div": "aws", "rev": "aws", "products": [
            P("agentcorepay", "AgentCore Payments", "Wallets for AI agents in USDC on Base and Solana over x402, with fiat funding, built with Coinbase and Stripe's Privy; in preview since 7 May 2026 for micropayments to APIs, MCP servers and content. No card network is named ⚠.",
              s=["dev"], lc="move", st="new", ay="May 2026", o="P", at="Coinbase, Stripe", neo=[0, "USDC; no card network named."],
              mc="Agent Pay for Machines could be the card and fiat bridge.",
              src=[["The Block: AgentCore Payments, May 2026", AGENTCORE], ["Amazon: Q2 2026 results", Q2]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every purchase: Prime and Buy with Prime, shopping agents that buy for the customer, AgentCore and Visa's agentic tools on AWS, and payment cryptography, with palm payments now ended.",
    "tiles": [
        {"id": "3.1", "ic": "gift", "name": "Prime", "blurb": "$49.6bn of subscriptions.", "div": "amazon", "rev": "na", "products": [
            P("prime", "Prime", "Subscriptions revenue of $49.6 billion in 2025 (Prime and others), with Alexa+ included for members. No current member count is published ⚠.",
              s=["prime"], lc="grow", neo=[0, ""], src=[["Amazon 10-K FY2025", TENK], ["Amazon: Q4 2025 results", Q4]]),
        ]},
        {"id": "3.2", "ic": "rocket", "name": "Buy with Prime", "blurb": "Prime on merchants' sites.", "div": "amazon", "rev": "na", "products": [
            P("bwp", "Buy with Prime", "Prime delivery and checkout on merchants' own sites, fulfilled by Amazon, through Shopify, Salesforce Commerce Cloud and TikTok; 16% more revenue per visitor in tests across 167 merchants (2023–24). Launched April 2022 ⚠.",
              s=["mer", "prime"], lc="grow", neo=[None, "Network not stated."], src=[["Buy with Prime", BWP]]),
        ]},
        {"id": "3.3", "ic": "bot", "name": "Shopping agents", "blurb": "Alexa for Shopping, Buy for Me.", "div": "amazon", "rev": "na", "products": [
            P("rufus", "Rufus & Alexa for Shopping", "Rufus (300 million users, about $12 billion of extra annualised sales) merged with Alexa+ into Alexa for Shopping, an agentic assistant with Price Alerts and Auto-Buy; interactions up more than five times in a year.",
              s=["shop", "prime"], lc="grow", st="new", neo=[0, ""], src=[["Amazon: Q2 2026 results", Q2], ["Amazon: Q4 2025 results", Q4]]),
            P("buyforme", "Buy for Me", "In beta for some US customers since 3 April 2025: Amazon's agent checks out on brands' own sites with the customer's encrypted name, address and payment details. Some retailers objected to being listed without consent ⚠.",
              s=["shop"], lc="move", st="new", ay="Apr 2025", neo=[1, "The customer's saved card, any network."],
              mc="Agent-made card-not-present payments are what Agent Pay and agentic tokens are for.",
              src=[["Amazon: Buy for Me", BFM], ["Agent Pulse, Jan 2026", PULSE]]),
        ]},
        {"id": "3.4", "ic": "network", "name": "Agentic commerce on AWS", "blurb": "AgentCore; Visa listed.", "div": "aws", "rev": "aws", "products": [
            P("agentcore", "Bedrock AgentCore", "The agent runtime on AWS, adding Policy, Evaluations and Memory, with Payments in preview.",
              s=["dev"], lc="open", st="new", neo=[0, ""], src=[["Amazon: Q4 2025 results", Q4], ["Amazon: Q2 2026 results", Q2]]),
            P("visaaws", "Visa Intelligent Commerce on AWS", "Visa's agentic tokens, authentication and intent capture in AWS Marketplace, and open AgentCore blueprints for retail, travel and B2B reconciliation (1 December 2025); 'multi-network' flows 'coming soon'.", short="Visa on AWS",
              s=["dev"], lc="move", st="new", ay="Dec 2025", o="P", at="Visa", neo=[0, "Visa."],
              mc="The only named network inside AWS's agentic tools; Mastercard is not mentioned.",
              src=[["AWS: Visa and AWS agentic commerce, Dec 2025", VISAAWS]]),
        ]},
        {"id": "3.5", "ic": "key-round", "name": "Payment security", "blurb": "Cryptography; palm ended.", "div": "aws", "rev": "aws", "products": [
            P("paycrypto", "AWS Payment Cryptography", "A managed service in place of payment HSMs: PIN and cryptogram checks and key exchange, PCI-aligned, used by issuers and processors. Generally available since 2023 ⚠.",
              s=["dev"], lc="everyday", neo=[0, ""], src=[["AWS Payment Cryptography", PAYCRYPTO]]),
            P("amazonone", "Amazon One palm payments", "Palm payments from 2020 at Whole Foods and Panera, ended on 3 June 2026 with the closure of Amazon Go and Amazon Fresh stores; healthcare check-in continues.",
              s=["shop"], lc="move", st="retired", neo=[0, ""], src=[["The Paypers: Amazon One ends, Jan 2026", ONE]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What Amazon sells: online stores and Whole Foods, a marketplace where sellers ship 61% of units, $68.6 billion of advertising, AWS, Amazon Business at $60 billion a year, and Amazon Pay's payments and credit in India.",
    "tiles": [
        {"id": "4.1", "ic": "store", "name": "Stores", "blurb": "$269.3bn online.", "div": "amazon", "rev": "na", "products": [
            P("onlinestores", "Online stores", "$269.3 billion of first-party online sales in 2025 and $70.4 billion in Q2 2026 (+15%); sales of $489.7 billion in the US, $45.9 billion in Germany, $43.2 billion in the UK and $30.7 billion in Japan in 2025.",
              s=["shop", "prime"], lc="everyday", neo=[1, "Accepts every network."], src=[["Amazon 10-K FY2025", TENK], ["Amazon: Q2 2026 results", Q2]]),
            P("wholefoods", "Whole Foods & physical stores", "$22.6 billion of physical-store sales in 2025, now centred on Whole Foods and online grocery after Go and Fresh closed (72 sites).",
              s=["shop"], lc="everyday", st="flux", neo=[1, "Accepts every network."], src=[["Amazon 10-K FY2025", TENK], ["The Paypers: Amazon One ends, Jan 2026", ONE]]),
        ]},
        {"id": "4.2", "ic": "users-round", "name": "Marketplace", "blurb": "61% of units.", "div": "amazon", "rev": "intl", "products": [
            P("marketplace", "Third-party seller services", "$172.2 billion in 2025 and $46.8 billion in Q2 2026 (+16%); sellers shipped 61% of paid units in Q4 2025. No current seller count was found.",
              s=["seller"], lc="everyday", neo=[0, ""], src=[["Amazon 10-K FY2025", TENK], ["Amazon: Q4 2025 results", Q4]]),
            P("lending", "Amazon Lending", "Loans to sellers ⚠ no 2025–26 figures found.",
              s=["seller"], lc="borrow", st="unconf", neo=[None, ""]),
            P("supplychain", "Amazon Supply Chain Services", "Freight and fulfilment for businesses, launched in Q2 2026.",
              s=["seller"], lc="beyond", st="new", neo=[0, ""], src=[["Amazon: Q2 2026 results", Q2]]),
        ]},
        {"id": "4.3", "ic": "presentation", "name": "Advertising", "blurb": "$68.6bn in 2025.", "div": "amazon", "rev": "na", "products": [
            P("ads", "Amazon Ads", "$68.6 billion in 2025 and $19.8 billion in Q2 2026 (+26%), with Prime Video ads and live sports, and an Ads Agent for sellers in 11 more countries.",
              s=["seller", "mer"], lc="grow", neo=[0, ""], src=[["Amazon: Q2 2026 results", Q2], ["Amazon 10-K FY2025", TENK]]),
        ]},
        {"id": "4.4", "ic": "database", "name": "AWS", "blurb": "+37% in Q2 2026.", "div": "aws", "rev": "aws", "products": [
            P("aws", "Amazon Web Services", "$128.7 billion of sales in 2025 with $45.6 billion of operating income; $42.2 billion in Q2 2026 (+37%).",
              s=["dev"], lc="beyond", neo=[0, ""], src=[["Amazon 10-K FY2025", TENK], ["Amazon: Q2 2026 results", Q2]]),
        ]},
        {"id": "4.5", "ic": "briefcase-business", "name": "Amazon Business", "blurb": "$60bn a year.", "div": "business", "rev": "na", "products": [
            P("business", "Amazon Business", "Business buying at $60 billion of annualised gross sales (Q2 2026).",
              s=["biz"], lc="everyday", neo=[0, ""],
              mc="Virtual and commercial cards for buyers, suppliers and seller payouts are untested ground.",
              src=[["Amazon: Q2 2026 results", Q2]]),
        ]},
        {"id": "4.6", "ic": "smartphone", "name": "Amazon Pay India", "blurb": "UPI, wallet, credit.", "div": "india", "rev": "intl", "products": [
            P("upi", "Amazon Pay UPI", "UPI with Axis Bank since February 2019: more than 110 million users but only about 0.5% of UPI, outside the top ten apps; biometric UPI added in December 2025.",
              s=["shop"], lc="move", o="P", at="Axis Bank", neo=[0, "UPI."]),
            P("wallet", "Amazon Pay Balance", "A wallet under an Indian wallet licence since 2016.",
              s=["shop"], lc="everyday", neo=[0, ""]),
            P("icici", "Amazon Pay ICICI Bank credit card", "Launched in October 2018, more than 5 million active users in 2025; the network was not confirmed ⚠ and is generally understood to be Visa.",
              s=["shop"], lc="borrow", o="P", at="ICICI Bank", neo=[None, "Network not confirmed ⚠."]),
            P("paylater", "Amazon Pay Later & Axio", "Pay Later since April 2020 (more than 10 million sign-ups), now lent through partner NBFCs and Axio, Amazon's own lending licence since September 2025, with insurance broking.",
              s=["shop"], lc="borrow", o="A", neo=[0, ""], src=[["Business Standard: Axio, Sep 2025", AXIO]]),
            P("fds", "Amazon Pay fixed deposits", "Fixed deposits through Amazon Pay, launched January 2026.",
              s=["shop"], lc="grow", st="new", neo=[0, ""]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Amazon: the website and app in more than 20 countries, Alexa+, and partners' sites, platforms and AWS Marketplace.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Stores & app", "blurb": "20+ countries.", "div": "amazon", "rev": "na", "products": [
            P("app", "Amazon website & app", "Amazon.com and more than 20 country stores, with the wallet, Prime and Rufus inside.",
              s=["shop", "prime", "seller"], lc="open", neo=[0, ""], src=[["Amazon 10-K FY2025", TENK]]),
        ]},
        {"id": "5.2", "ic": "sparkles", "name": "Alexa+", "blurb": "Free with Prime.", "div": "amazon", "rev": "na", "products": [
            P("alexa", "Alexa+", "Free with Prime or $19.99 a month, now in Germany, Austria, France and Brazil as well as the US; its users join Prime at a 'nearly 25% higher rate'.",
              s=["prime", "shop"], lc="open", st="new", neo=[0, ""], src=[["Amazon: Q2 2026 results", Q2], ["Amazon: Q4 2025 results", Q4]]),
        ]},
        {"id": "5.3", "ic": "plug", "name": "Partners", "blurb": "Shopify, AWS Marketplace.", "div": "pay", "rev": "aws", "products": [
            P("partners", "Partner checkout", "Amazon Pay and Buy with Prime on third-party sites through Shopify, Stripe, BigCommerce, WooCommerce, Salesforce Commerce Cloud and TikTok.",
              s=["mer"], lc="open", neo=[0, ""], src=[["Amazon Pay", PAY], ["Buy with Prime", BWP]]),
            P("awsmkt", "AWS Marketplace", "Where partners such as Visa list their payment products for builders on AWS.",
              s=["dev"], lc="open", neo=[0, "Visa listed; no Mastercard listing found."], src=[["AWS: Visa and AWS agentic commerce, Dec 2025", VISAAWS]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Amazon", "blurb": "Japan, Mexico, every checkout.", "products": [
        P("mcatamazon", "Mastercard at Amazon", "Every Amazon store accepts Mastercard, and Mastercard carries the Japan co-brand (SMBC Card, since 2014) and the Mexico prepaid card (Banorte, 2018). Visa holds the co-brands in the US, the UK (since 2024, from Mastercard) and Germany, has had a global agreement with Amazon since 2022, and is the only network named in AWS's agentic tools. No Amazon announcement on Agent Pay, Click to Pay or tokens was found.",
          s=["shop"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["paymentnavi: Amazon Mastercard", JAPAN], ["Barclays: Amazon Barclaycard, Aug 2024", BARC], ["AWS: Visa and AWS agentic commerce, Dec 2025", VISAAWS]]),
    ]},
    {"id": "pillar-market", "name": "Agentic commerce", "blurb": "Agents, tokens, stablecoins.", "products": [
        P("market", "The market", "Agentic commerce is the new contest: Visa inside AWS since December 2025, Coinbase and Stripe behind AgentCore's wallets, and Mastercard's Agent Pay live for all US cardholders with a global launch scheduled for early 2026; about 40% of Mastercard transactions are tokenised.",
          s=["dev"], div="grp", rev="grp", src=[["Mastercard 10-K FY2025", MA10K], ["The Block: AgentCore Payments, May 2026", AGENTCORE]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
