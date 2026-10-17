"""Global Payments' layers, areas and products (Worldpay included), as at 17 October 2026 (see page_data.py).

Figures are the company's own unless a source says otherwise: the Q2 2026 results and 10-Q (5 August 2026),
the completion release (12 January 2026) and the FY2025 10-K. ``neo`` is the Mastercard lens:
[depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

SEC = "https://www.sec.gov/Archives/edgar/data/1123360/"
CLOSE = SEC + "000110465926002705/tm262856d1_ex99-1.htm"
DEAL = SEC + "000110465925035771/tm2512552d1_ex99-1.htm"
Q2 = "https://www.sec.gov/Archives/edgar/data/0001123360/000112336026000082/exhibit99120260630.htm"
Q2Q = "https://www.sec.gov/Archives/edgar/data/0001123360/000112336026000084/gpn-20260630.htm"
FY25 = SEC + "000112336026000004/exhibit99120251231.htm"
K25 = SEC + "000112336026000008/gpn-20251231.htm"
Q1C = "https://finance.yahoo.com/markets/stocks/articles/global-payments-gpn-q1-2026-190830091.html"
PR = "https://investors.globalpayments.com/news-events/press-releases/detail/"
FIS = "https://www.fisglobal.com/about-us/media-room/press-release/2026/fis-completes-strategic-acquisition-of-global-payments-issuer-solutions-business"
MOVE = "https://www.zawya.com/en/press-release/companies-news/worldpay-leverages-mastercard-move-to-empower-consumers-and-businesses-to-send-and-receive-payments-quickly-and-securely-in-the-uae-d7ejsp66"
THRIVE = "https://www.thepower50.com/worldpay-and-mastercard-team-up-with-mary-portas-to-spotlight-uk-indie-retail-at-thrive-street-2025"
TAP = "https://www.worldpay.com/en/news/worldpay-collaborates-visa-and-cloudflare-advance-trusted-agent"
VISA20 = "https://www.worldpay.com/en/press-releases/worldpay-fis-and-visa-collaborate-strengthen-digital-commerce"
BVNK = "https://bvnk.com/blog/worldpay-bvnk-enable-stablecoin-payouts"
AGENTIC = "https://worldpay.com/en/agentic-commerce"
UCP = "https://worldpay.com/en/news/worldpay-continues-collaboration-with-google"
MCP = "https://www.digitaltransactions.net/worldpay-launches-a-protocol-for-creating-ai-agents-and-connecting-them-to-its-platform/"
RAVELIN = "https://www.worldpay.com/en/press-releases/worldpay-acquire-ravelin-leading-ai-native-fraud-prevention"
PLATFORMS = "https://platforms.globalpayments.com/"
GPR = "https://treasurytoday.com/press-releases/press-release-worldpay-now-global-payments-releases-global-payments-report-2026-digital-wallets-qr-adoption-real-time-payments-and-a2a-growth/"
SOLANA = "https://finance.yahoo.com/markets/crypto/articles/mastercard-western-union-worldpay-building-135504877.html"
MCAP = "https://stockanalysis.com/stocks/gpn/market-cap/"
WIKI = "https://en.wikipedia.org/wiki/Global_Payments"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "scale · network rules · the Worldpay deal", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $3.7 trillion of volume across 6 million locations after Worldpay, licences and network sponsorship in 175 countries, a heritage from NDC, Heartland and RBS WorldPay, and a swap that turned an issuer processor into a pure merchant company.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & finances", "blurb": "$3.7 trillion, 94 billion transactions.", "div": "gpn", "rev": "grp", "products": [
            P("scale", "Scale", "More than 6 million merchant locations, about $3.7 trillion of volume and about 94 billion transactions a year in more than 175 countries, by the company's count at completion.",
              s=["inv"], neo=[0, ""], src=[["Worldpay completion release, Jan 2026", CLOSE]]),
            P("finances", "Finances", "Q2 2026 adjusted net revenue of $3.16 billion (about +4% normalised) and adjusted EPS of $3.46; 2026 outlook cut in August to 4–5% growth and EPS of $13.60–13.80, citing travel hit by the Middle East conflict; net leverage 3.5x at close, 3.0x targeted; market value about $22 billion.",
              s=["inv"], neo=[0, ""], src=[["Q2 2026 results", Q2], ["StockAnalysis: market cap", MCAP]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Licences & network rules", "blurb": "Sponsored, licensed, regulated.", "div": "gpn", "rev": "grp", "products": [
            P("licences", "Network membership & licences", "Direct member of some networks and bank-sponsored elsewhere (Global Payments Direct is a registered ISO of PNC); payment-institution licences across Europe and the UK; Visa and Mastercard registration appears in its filings only as a risk factor.",
              s=["inv", "bank"], neo=[1, "Mastercard rules and registration."], src=[["FY2025 10-K", K25], ["Worldpay completion release, Jan 2026", CLOSE]]),
        ]},
        {"id": "1.3", "ic": "users-round", "name": "Leadership", "blurb": "Bready, Cortopassi, Whipple.", "div": "gpn", "rev": "grp", "products": [
            P("leadership", "Leadership", "CEO Cameron Bready (since June 2023), President and COO Bob Cortopassi, CFO Josh Whipple, Chief Product Officer Cindy Turner (from Worldpay), David Rumph for SMB, Matt Downs for platforms; chair Troy Woods; a board integration committee after Elliott's involvement.",
              s=["inv"], neo=[0, ""], src=[["Global Payments press release, May 2026", PR + "511"], ["Q1 2026 call", Q1C]]),
        ]},
        {"id": "1.4", "ic": "badge-check", "name": "Heritage", "blurb": "NDC, Heartland, RBS WorldPay.", "div": "grp", "rev": "grp", "products": [
            P("heritage", "Two family trees", "Global Payments: spun off from NDC (2001), Heartland (2016), TSYS (2019), EVO (2023). Worldpay: Streamline at NatWest (1989), WorldPay (1997), RBS WorldPay, Vantiv (2018), FIS (2019), GTCR (2024).",
              s=["inv"], o="A", neo=[0, ""], src=[["Wikipedia: Global Payments", WIKI], ["FY2025 10-K", K25]]),
        ]},
        {"id": "1.5", "ic": "arrow-left-right", "name": "The Worldpay swap", "blurb": "Worldpay in, TSYS out.", "div": "worldpay", "rev": "grp", "products": [
            P("swap", "Worldpay in, Issuer Solutions out", "Closed 9 January 2026: Worldpay bought from GTCR and FIS (net $22.7 billion), and TSYS Issuer Solutions sold to FIS for $13.5 billion, now FIS Total Issuing Solutions. Mastercard's issuer-processing ties to TSYS now run through FIS.", short="The Worldpay swap",
              s=["inv"], st="new", ay="Jan 2026", o="A", neo=[0, ""],
              src=[["Worldpay completion release, Jan 2026", CLOSE], ["Deal announcement, Apr 2025", DEAL], ["FIS completion release, Jan 2026", FIS]]),
        ]},
        {"id": "1.6", "ic": "target", "name": "Strategy & synergies", "blurb": "$600 million of cost synergies.", "div": "gpn", "rev": "grp", "products": [
            P("strategy", "Pure-play commerce", "One Global Payments brand, more than $1 billion a year on innovation, about $600 million of cost and $200 million of revenue synergies, and $7.5 billion returned to shareholders over 2025–27.",
              s=["inv"], neo=[0, ""], src=[["Deal announcement, Apr 2025", DEAL], ["Q2 2026 results", Q2]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: Worldpay's enterprise acquiring, small-business acquiring from Heartland to EVO, the online gateway and local payment methods, payouts on Mastercard Move and stablecoins, currency and marketplaces, and government payments.",
    "tiles": [
        {"id": "2.1", "ic": "building-2", "name": "Enterprise acquiring", "blurb": "Worldpay, top three in the US.", "div": "worldpay", "rev": "ent", "products": [
            P("wpenterprise", "Worldpay enterprise acquiring", "Card-present and online acquiring for large and multinational merchants (Abercrombie & Fitch, Aldi Süd, Morrisons, KFC, Marriott in Asia-Pacific); third among US acquirers by transactions in 2024 and the largest UK enterprise acquirer.",
              s=["ent"], lc="move", neo=[1, "Accepts every network."], src=[["Q1 2026 call", Q1C], ["Q2 2026 results", Q2]]),
        ]},
        {"id": "2.2", "ic": "store", "name": "SMB acquiring", "blurb": "Heartland, EVO, takepayments.", "div": "heartland", "rev": "smb", "products": [
            P("smbacq", "Small-business acquiring", "Direct and referral acquiring for small and medium businesses in the Americas, Europe and Asia, built from Heartland (2016), EVO (2023) and ⚠ takepayments in the UK; the brands are folding into Global Payments and Genius.",
              s=["sme"], lc="move", neo=[1, "Accepts every network."], src=[["FY2025 10-K", K25]]),
        ]},
        {"id": "2.3", "ic": "globe", "name": "Online & payment methods", "blurb": "Gateway, wallets, local methods.", "div": "worldpay", "rev": "ent", "products": [
            P("gateway", "Online gateway & payment methods", "Worldpay's online, in-store and omnichannel gateway with wallets and local methods, and Global Payments' ex-Realex gateway; the company's 2026 report finds wallets at 77% of online spend in Asia-Pacific.",
              s=["ent", "sme"], lc="move", neo=[1, "Mastercard among many methods."],
              mc="Visa has had a dated Click to Pay and token commitment at Worldpay since 2020; Mastercard has none in public.",
              src=[["Worldpay: agentic commerce", AGENTIC], ["Global Payments Report 2026, Apr 2026", GPR], ["Worldpay and Visa, Dec 2020", VISA20]]),
        ]},
        {"id": "2.4", "ic": "send", "name": "Payouts", "blurb": "Push-to-Card on Mastercard Move.", "div": "worldpay", "rev": "plat", "products": [
            P("move", "Push-to-Card on Mastercard Move (UAE)", "Worldpay one of the first UAE acquirers on Mastercard Move (August 2025): payouts to cards for gig pay, insurance claims, remittances and crypto withdrawals, funded from acquiring flows.", short="Mastercard Move payouts",
              s=["plat", "ent"], lc="move", st="new", ay="Aug 2025", o="P", at="Mastercard", neo=[3, "Mastercard Move."],
              mc="Push-to-Card runs in the UK, EU, US and Australia too; only the UAE is co-branded with Move.",
              src=[["Zawya: Worldpay and Mastercard Move, Aug 2025", MOVE]]),
            P("stablecoinpayouts", "Stablecoin payouts & settlement", "Stablecoin payouts with BVNK in more than 180 markets (2025), USDC settlement since 2022, and the Solana Developer Platform for merchant settlement (2026).",
              s=["plat"], lc="move", st="new", o="P", at="BVNK", neo=[0, "Off the card networks."],
              src=[["BVNK: Worldpay stablecoin payouts, May 2025", BVNK], ["Yahoo Finance: Solana Developer Platform, Mar 2026", SOLANA]]),
        ]},
        {"id": "2.5", "ic": "coins", "name": "Currency & marketplaces", "blurb": "Multi-currency, split payments.", "div": "worldpay", "rev": "plat", "products": [
            P("fx", "Currency & marketplaces", "Multi-currency pricing and settlement and a marketplace product for split payments and seller onboarding.",
              s=["ent", "plat"], lc="move", neo=[0, ""], src=[["Worldpay: agentic commerce", AGENTIC], ["Global Payments for Platforms", PLATFORMS]]),
        ]},
        {"id": "2.6", "ic": "landmark", "name": "Government payments", "blurb": "Link2Gov and the IRS.", "div": "gpn", "rev": "smb", "products": [
            P("link2gov", "Link2Gov & Pay1040", "Tax, fee and bill payments for government, named the IRS's preferred digital payment partner for the 2026 tax season.",
              s=["con"], lc="move", neo=[1, "Card payments among methods."], src=[["Global Payments: Link2Gov and the IRS, Mar 2026", PR + "503"]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every transaction: Ravelin's AI fraud models, tokens and authorisation optimisation, disputes and insights, agentic commerce across protocols, embedded finance for platforms, and gift and loyalty.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud", "blurb": "Ravelin.", "div": "worldpay", "rev": "ent", "products": [
            P("ravelin", "Ravelin & fraud prevention", "Ravelin's AI fraud platform (agreed February 2025) for payment fraud, account takeover, refund abuse and 3-D Secure, alongside Worldpay's fraud screening and 3DS Flex.",
              s=["ent", "sme"], lc="everyday", o="A", neo=[0, "In-house."],
              mc="No Decision Intelligence or Ethoca link with Worldpay or Genius in public.",
              src=[["Worldpay to acquire Ravelin, Feb 2025", RAVELIN], ["Q1 2026 call", Q1C]]),
        ]},
        {"id": "3.2", "ic": "key-round", "name": "Tokens & authorisation", "blurb": "Vault, Revenue Boost, routing.", "div": "worldpay", "rev": "ent", "products": [
            P("tokens", "Vault, credential management & Revenue Boost", "Tokenisation so neither merchants nor agents hold card data, card-updater and credential management, AI authorisation optimisation and adaptive routing.",
              s=["ent", "plat"], lc="grow", neo=[1, "Network tokens among them."],
              mc="Mastercard tokens and Click to Pay are surely supported, but no dated announcement exists.",
              src=[["Worldpay: agentic commerce", AGENTIC], ["Q1 2026 call", Q1C]]),
        ]},
        {"id": "3.3", "ic": "receipt-text", "name": "Disputes & insights", "blurb": "Disputes Defender.", "div": "worldpay", "rev": "ent", "products": [
            P("disputes", "Disputes Defender & insights", "Chargeback automation, including for purchases by AI agents, and merchant analytics and reporting.",
              s=["ent", "sme"], lc="grow", neo=[0, ""],
              mc="Verifiable Intent's audit trail and Consumer Clarity map directly onto agent disputes.",
              src=[["Worldpay: agentic commerce", AGENTIC]]),
        ]},
        {"id": "3.4", "ic": "bot", "name": "Agentic commerce", "blurb": "Visa TAP, ACP, UCP, MCP.", "div": "worldpay", "rev": "ent", "products": [
            P("agentic", "Agentic commerce", "Worldpay worked with Visa and Cloudflare on the Trusted Agent Protocol (October 2025), supports OpenAI's ACP and Google's UCP (January 2026), and published its own MCP server (November 2025); Mastercard's logo appears on its agentic page, but no Agent Pay announcement has been made.",
              s=["ent", "plat"], lc="move", st="new", neo=[0, "Visa TAP, ACP and UCP; Mastercard not announced."],
              mc="The clearest opening: Agent Pay and Verifiable Intent acceptance at Worldpay.",
              src=[["Worldpay, Visa and Cloudflare, Oct 2025", TAP], ["Worldpay and Google UCP, Jan 2026", UCP], ["Digital Transactions: Worldpay MCP, Nov 2025", MCP]]),
        ]},
        {"id": "3.5", "ic": "plug", "name": "Embedded finance", "blurb": "Working capital, accounts.", "div": "gpn", "rev": "plat", "products": [
            P("embedded", "Working capital & money management", "Merchant financing and embedded business accounts and cards that platforms offer their merchants.",
              s=["plat"], lc="borrow", neo=[None, "Card network not public."], src=[["Global Payments for Platforms", PLATFORMS]]),
        ]},
        {"id": "3.6", "ic": "gift", "name": "Gift & loyalty", "blurb": "For merchants and platforms.", "div": "worldpay", "rev": "ent", "products": [
            P("loyalty", "Gift & loyalty", "Gift-card and loyalty programmes for enterprise merchants and platforms.",
              s=["ent", "con"], lc="grow", neo=[0, ""], src=[["Worldpay: agentic commerce", AGENTIC], ["Global Payments for Platforms", PLATFORMS]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "Three segments opened out: Enterprise (mostly Worldpay), Platforms (embedded payments for software companies), SMB (payments and Genius software), plus restaurant POS, vertical software and the businesses sold to get here.",
    "tiles": [
        {"id": "4.1", "ic": "building-2", "name": "Enterprise", "blurb": "$838 million a quarter.", "div": "worldpay", "rev": "ent", "products": [
            P("enterprise", "Enterprise segment", "Payments for large and multinational merchants: $838 million of adjusted revenue and a 78% margin in Q2 2026; bookings up 9% in the first quarter.",
              s=["ent"], lc="everyday", neo=[1, "Accepts every network."], src=[["Q2 2026 results", Q2], ["Q1 2026 call", Q1C]]),
        ]},
        {"id": "4.2", "ic": "code-xml", "name": "Platforms", "blurb": "Payrix and integrated partners.", "div": "worldpay", "rev": "plat", "products": [
            P("platforms", "Global Payments for Platforms", "Embedded payments for software platforms, from referral to managed payfac (Payrix Pro): $628 million in Q2 2026; 44 new ISVs in the first quarter; Lightspeed DMS among them.",
              s=["plat"], lc="everyday", neo=[1, "Accepts every network."], src=[["Global Payments for Platforms", PLATFORMS], ["Q2 2026 results", Q2]]),
        ]},
        {"id": "4.3", "ic": "store", "name": "SMB", "blurb": "$1.5 billion a quarter.", "div": "genius", "rev": "smb", "products": [
            P("smb", "SMB segment", "Payments and software for small and medium businesses: $1.51 billion in Q2 2026, the largest segment; Worldpay e-commerce now sold through Global Payments' small-business channels.",
              s=["sme"], lc="everyday", neo=[1, "Accepts every network."], src=[["Q2 2026 results", Q2], ["Q1 2026 call", Q1C]]),
        ]},
        {"id": "4.4", "ic": "factory", "name": "Restaurants", "blurb": "CKE, Subway.", "div": "genius", "rev": "smb", "products": [
            P("restaurants", "Restaurant POS", "Genius for enterprise restaurants: exclusive at CKE's 2,400 Hardee's and Carl's Jr. (May 2026) and Genius Kitchen at about 2,500 Subway locations.",
              s=["ent", "sme"], lc="everyday", st="new", neo=[0, ""], src=[["Global Payments: CKE Restaurants, May 2026", PR + "508"], ["Q1 2026 call", Q1C]]),
        ]},
        {"id": "4.5", "ic": "graduation-cap", "name": "Vertical software", "blurb": "Education, communities, property.", "div": "gpn", "rev": "smb", "products": [
            P("vertical", "Vertical software", "Software and payments for universities and schools, health clubs and event organisers, and property managers.",
              s=["sme", "con"], lc="beyond", neo=[0, ""], src=[["FY2025 10-K", K25]]),
        ]},
        {"id": "4.6", "ic": "x", "name": "Sold to get here", "blurb": "Issuing, payroll, AdvancedMD.", "div": "grp", "rev": "grp", "products": [
            P("divested", "Divested businesses", "Issuer Solutions to FIS (January 2026), payroll to Acrisure (September 2025), AdvancedMD (December 2024), gaming and Netspend consumer (2023); 'Other' non-core portfolios still shrinking.",
              s=["inv"], st="retired", neo=[0, ""], src=[["Q2 2026 10-Q", Q2Q], ["FY2025 10-K", K25]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How merchants reach the company: Genius devices, developer hubs and MCP servers, a growing direct sales force, bank channels, and research and events.",
    "tiles": [
        {"id": "5.1", "ic": "monitor", "name": "Genius", "blurb": "Cloud POS, AI handheld.", "div": "genius", "rev": "smb", "products": [
            P("genius", "Genius devices", "Cloud point of sale launched in 2025: an AI-first handheld (May 2026), kiosks, countertop terminals, drive-thru and kitchen systems; new locations up 25%.",
              s=["sme", "ent"], lc="open", st="new", neo=[0, ""], src=[["Global Payments: Genius handheld, May 2026", PR + "509"], ["Q1 2026 call", Q1C]]),
        ]},
        {"id": "5.2", "ic": "code-xml", "name": "Developers & MCP", "blurb": "Two hubs, two MCP servers.", "div": "worldpay", "rev": "plat", "products": [
            P("developers", "Developer hubs & MCP", "The Worldpay developer hub and its open-source MCP server (November 2025), the Global Payments developer portal and its own MCP server (2026).",
              s=["plat", "ent"], lc="open", neo=[0, ""], src=[["Digital Transactions: Worldpay MCP, Nov 2025", MCP], ["Q1 2026 call", Q1C]]),
        ]},
        {"id": "5.3", "ic": "headset", "name": "Direct sales", "blurb": "500 new hires.", "div": "gpn", "rev": "smb", "products": [
            P("sales", "Direct sales", "More than 300 of 500 planned North American sales hires onboarded and a new direct channel in Mexico.",
              s=["sme"], lc="open", neo=[0, ""], src=[["Q1 2026 call", Q1C]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Bank & partner channels", "blurb": "6,000 US branches.", "div": "worldpay", "rev": "smb", "products": [
            P("banks", "Bank & partner channels", "Worldpay's financial-institution channel (about 6,000 US bank branches, Genius from 2027), bank partners and joint ventures (Peoples Bank, Erste, NBG Pay), ISOs and the Acrisure referral deal.",
              s=["bank", "sme"], lc="open", neo=[0, ""], src=[["Q1 2026 call", Q1C], ["Q2 2026 10-Q", Q2Q]]),
        ]},
        {"id": "5.5", "ic": "presentation", "name": "Research & events", "blurb": "Report, Thrive Street.", "div": "worldpay", "rev": "smb", "products": [
            P("events", "Global Payments Report & Thrive Street", "The annual Global Payments Report (April 2026), Genius World (August 2026), and Thrive Street, a UK independent-retail festival with Mastercard and Mary Portas (2025).",
              s=["sme", "inv"], lc="grow", o="P", at="Mastercard", neo=[1, "Thrive Street with Mastercard."],
              src=[["Global Payments Report 2026, Apr 2026", GPR], ["Thrive Street 2025", THRIVE]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Global Payments", "blurb": "Move in the UAE, Thrive Street.", "products": [
        P("mcatgpn", "Mastercard at Global Payments", "Every merchant accepts Mastercard, and Worldpay pays out on Mastercard Move in the UAE (August 2025) and co-ran Thrive Street with Mastercard in the UK. Visa has more dated collaborations (Click to Pay and tokens in 2020, the Trusted Agent Protocol in 2025), and TSYS's issuer processing now sits with FIS.",
          s=["inv"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Zawya: Worldpay and Mastercard Move, Aug 2025", MOVE], ["Worldpay, Visa and Cloudflare, Oct 2025", TAP]]),
    ]},
    {"id": "pillar-market", "name": "Acquiring", "blurb": "Scale versus e-commerce challengers.", "products": [
        P("market", "The acquiring market", "JPMorgan, Fiserv and the new Global Payments at the top by volume; Adyen, Stripe and Checkout.com growing faster online; wallets and account-to-account gaining in Asia-Pacific; agents choosing how to pay.",
          s=["inv"], div="grp", rev="grp", src=[["Global Payments Report 2026, Apr 2026", GPR]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
