"""Booking Holdings' layers, areas and products, read through payments, as at 17 October 2026 (see page_data.py for the format).

Figures are Booking Holdings' own unless a source says otherwise: the Q2 2026 results (4 August 2026), the Q4 and
full-year 2025 results (18 February 2026) and the FY2025 10-K, with Booking.com's newsroom and developer docs, the
BHFS USA licence page, and Mastercard, Visa, Affirm, KTC and trade press for the payment programmes. Q3 2026 results
are due in late October. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it,
2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q2 = "https://www.sec.gov/Archives/edgar/data/0001075531/000107553126000036/q2-26bkngearningsrelease.htm"
Q4 = "https://s201.q4cdn.com/865305287/files/doc_financials/2025/q4/Q4-25-BKNG-Earnings-Release.pdf"
TENK = "https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm"
MCAP = "https://companiesmarketcap.com/booking-holdings/marketcap/"
FACTS = "https://www.bookingholdings.com/about/factsheet/"
HOME = "https://www.bookingholdings.com/"
LEAD = "https://www.bookingholdings.com/about/leadership/"
HIST = "https://www.bookingholdings.com/about/history/"
BHFS = "https://www.bookingholdings.com/about/financial-services/"
BHFSUS = "https://www.bookingholdingsfs.us/"
B_BOOKING = "https://www.bookingholdings.com/brands/booking/"
B_AGODA = "https://www.bookingholdings.com/brands/agoda/"
B_PRICELINE = "https://www.bookingholdings.com/brands/priceline/"
B_KAYAK = "https://www.bookingholdings.com/brands/kayak/"
B_OT = "https://www.bookingholdings.com/brands/opentable/"
CALL = "https://transcripts.platformaeronaut.com/summaries/BKNG-4Q25-AI-Summary"
CNMC = "https://www.thelocal.es/20240730/spains-watchdog-hands-e413-million-fine-to-booking-com"
PARITY = "https://news.booking.com/amsterdam-court-upholds-key-elements-of-bookingcoms-position-in-german-price-parity-case/"
GUESTY = "https://help.guesty.com/hc/en-gb/articles/27810859878685-Understanding-Booking-com-reservation-payouts"
PAYOUTS = "https://developers.booking.com/connectivity/docs/payments-by-booking-onboarding-api/understanding-payouts"
NIGHTS = "https://nightsbridge.screenstepslive.com/a/1722322-booking-com-payment-options"
MCBOOK = "https://www.mastercard.com/europe/en/news-and-trends/press/2024/January/mastercard-strengthens-collaboration-with-bookingcom-to-remove-payment-friction-for-partners.html"
TRAVO = "https://www.travolution.com/news/mastercard-strengthens-collaboration-with-booking.com-to-remove-payment-friction-for-travel-partners"
MCAGODA = "https://www.mastercard.com/news/ap/en/newsroom/press-releases/en/2023/mastercard-and-agoda-expand-partnership-to-drive-innovation-and-efficiency-in-b2b-payments-for-the-travel-industry/"
MCREDEEM = "https://www.mastercard.com/news/ap/en/newsroom/press-releases/en/2026/agoda-and-mastercard-collaborate-to-modernize-loyalty-programs-with-flexible-travel-rewards/"
TTG = "https://www.ttgasia.com/2026/01/20/agoda-mastercard-introduce-travel-rewards-solution/"
KTC = "https://www.ktc.co.th/en/news/ktc-agoda-mastercard"
PRICELINE = "https://pymnts.com/?p=1392672"
AFFIRM = "https://investors.affirm.com/news-releases/news-release-details/affirm-partners-bookingcom-offer-travelers-increased-flexible"
AGODAVISA = "https://marketech-apac.com/agoda-partners-with-visa-to-offer-interest-free-credit-card-instalments-for-travellers-in-sea/"
JCB = "https://www.barchart.com/story/news/35972921/jcb-and-agoda-enter-long-term-partnership-to-enhance-travel-and-payment-experience-across-asia"
OTVISA = "https://www.pymnts.com/partnerships/2024/opentable-and-visa-launch-restaurant-reservation-partnership/"
OTRENEW = "https://www.opentable.com/blog/?p=152873"
PLANNER = "https://www.phocuswire.com/booking-com-adds-conversational-trip-planning-chatgpt"
CHATGPT = "https://news.booking.com/bookingcom-is-making-car-rentals-easier-with-app-in-chatgpt/"
AIRINDIA = "https://news.booking.com/air-india-and-bookingcom-partner-to-offer-integrated-booking-experiences-and-exclusive-rewards-to-travellers/"
UEFA = "https://news.booking.com/bookingcom-renews-partnership-with-uefa-national-team-competitions/"
AGENTPAY = "https://eco.com/support/en/articles/14845483-mastercard-agent-pay-explained"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "scale · people · licences", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $186.1 billion of gross bookings in 2025, a leadership led by Glenn Fogel, the e-money and money-transmitter licences of Booking Holdings Financial Services, a cost programme, and European regulators.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & results", "blurb": "$186.1bn booked in 2025.", "div": "grp", "rev": "grp", "products": [
            P("results", "Full-year 2025", "Gross bookings of $186.1 billion (+12%) and revenue of $26.9 billion (+13%): merchant $17.8 billion, agency $8.0 billion, advertising and other $1.2 billion. 1,235 million room nights (+8%); adjusted EBITDA $9.9 billion (36.9% margin); net income $5.4 billion. About 24,300 staff.",
              s=["trav"], neo=[0, ""], src=[["Booking Holdings: Q4 2025 results", Q4], ["Booking Holdings 10-K FY2025", TENK]]),
            P("q2", "Q2 2026", "Gross bookings of $51.0 billion (+9%), revenue of $7.4 billion (+8%) and 325 million room nights (+5%); adjusted EBITDA $2.6 billion. Guidance for the year is high single-digit growth, held back by the Middle East conflict. Market value about $126.7 billion at 17 October 2026.",
              s=["trav"], st="new", neo=[0, ""], src=[["Booking Holdings: Q2 2026 results", Q2], ["CompaniesMarketCap: Booking Holdings, Oct 2026", MCAP]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Fogel, Steenbergen, Mylod.", "div": "grp", "rev": "grp", "products": [
            P("leadership", "Executives & brand CEOs", "Glenn Fogel (CEO of Booking Holdings and Booking.com), Ewout Steenbergen (CFO), Peter Millones (General Counsel); brand CEOs Brigit Zimmerman (Priceline), Omri Morgenshtern (Agoda), Peer Bueller (KAYAK) and Debby Soo (OpenTable); Robert Mylod chairs the board. No named head of payments was found ⚠.",
              s=["trav"], neo=[0, ""], src=[["Booking Holdings: leadership", LEAD]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Payments licences", "blurb": "E-money and money transmission.", "div": "bhfs", "rev": "merchant", "products": [
            P("bhfs", "Booking Holdings Financial Services", "'A number of licensed and regulated e-money institutions' that run payment products for the brands. The European entities and their licences are not itemised publicly ⚠.",
              s=["prop", "trav"], lc="move", neo=[0, ""],
              mc="The licensed entity a Mastercard issuing or acquiring deal would sign with.",
              src=[["Booking Holdings: Financial Services", BHFS]]),
            P("bhfsus", "BHFS USA LLC", "A licensed money transmitter (NMLS ID 2436940) in about 45 US states and territories, including California and Florida; disclosures updated in March 2026.",
              s=["prop"], lc="move", neo=[0, ""], src=[["BHFS USA licence disclosures", BHFSUS]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy & capital", "blurb": "$650m savings, buybacks.", "div": "grp", "rev": "grp", "products": [
            P("transform", "Transformation Program", "About $550 million of run-rate savings enabled by the end of 2025, raised to about $650 million by the end of 2027, to fund generative AI and the Connected Trip.",
              s=["trav"], st="new", neo=[0, ""], src=[["Booking Holdings: Q2 2026 results", Q2], ["Booking Holdings: Q4 2025 results", Q4]]),
            P("capital", "Capital returns & split", "$6.4 billion of buybacks and $1.2 billion of dividends in 2025, $3.7 billion of buybacks in Q2 2026; a 25-for-1 stock split on 2 April 2026. Total debt $18.7 billion at the end of 2025.",
              s=["trav"], neo=[0, ""], src=[["Booking Holdings: Q2 2026 results", Q2], ["Booking Holdings 10-K FY2025", TENK]]),
            P("deals", "Deals", "Getaroom and Flyiin bought in 2021; centres of excellence in Bucharest (2021) and Bengaluru (2022). The Etraveli flight deal was blocked in Brussels in 2023 ⚠. KAYAK took $457 million of impairments in 2025.",
              s=["trav"], o="A", neo=[0, ""], src=[["Booking Holdings: history", HIST], ["Booking Holdings 10-K FY2025", TENK]]),
        ]},
        {"id": "1.5", "ic": "scroll-text", "name": "Regulation", "blurb": "DMA gatekeeper, Spain's fine.", "div": "booking", "rev": "grp", "products": [
            P("dma", "EU Digital Markets Act & DSA", "Designated a gatekeeper in May 2024; Booking.com dropped parity clauses in the EEA. Also a Very Large Online Platform under the Digital Services Act.",
              s=["prop"], neo=[0, ""], src=[["Booking Holdings 10-K FY2025", TENK]]),
            P("cnmc", "Spain's competition fine", "Spain's CNMC fined Booking.com €413.24 million on 30 July 2024, citing a 70–90% share of hotel online booking in Spain; Booking is appealing.",
              s=["prop"], neo=[0, ""], src=[["The Local: CNMC fine, Jul 2024", CNMC]]),
            P("parity", "German price-parity case", "An Amsterdam court upheld key parts of Booking.com's position in hotels' claims over German parity clauses (4 March 2026).",
              s=["prop"], neo=[0, ""], src=[["Booking.com: Amsterdam court ruling, Mar 2026", PARITY]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Five ways money moves: Booking.com as merchant of record on 70% of bookings, payouts to properties by virtual card, bank transfer or Stripe, Mastercard virtual cards at Agoda, co-brand cards (Visa at Priceline, Mastercard at Agoda in Thailand) and instalments with Affirm and Visa.",
    "tiles": [
        {"id": "2.1", "ic": "wallet", "name": "Merchant of record", "blurb": "$130bn, 70% of bookings.", "div": "booking", "rev": "merchant", "products": [
            P("mor", "Payments by Booking.com", "Booking.com takes the guest's payment and pays the property: $130.0 billion of merchant gross bookings in 2025 (+25%, 70% of the total, from 63%) and $37.0 billion in Q2 2026 (+14.5%). Merchant transaction costs rose $381 million in 2025.",
              s=["trav", "prop"], lc="move", neo=[1, "Accepts every network."],
              mc="The largest Mastercard-relevant flow in the group: card-not-present acceptance at $130 billion a year.",
              src=[["Booking Holdings 10-K FY2025", TENK], ["Guesty: Booking.com payouts", GUESTY]]),
            P("accept", "Card acceptance", "Guests pay by card on every major network, with local methods ⚠; Booking Holdings does not publish a network split.",
              s=["trav", "genius"], lc="move", neo=[1, "Accepts every network."],
              mc="Click to Pay and network tokens could cut the costs that rose with merchant mix.",
              src=[["Booking Holdings 10-K FY2025", TENK]]),
        ]},
        {"id": "2.2", "ic": "send", "name": "Payouts to properties", "blurb": "Card, bank or Stripe.", "div": "booking", "rev": "merchant", "products": [
            P("vcc", "Virtual credit cards", "A single-use card per booking for the exact amount the guest paid, charged by the property through a card-not-present terminal or its PSP; almost always paid gross. An integrator names Mastercard as the network; the issuer is not public ⚠.", short="Virtual cards (Mastercard ⚠)",
              s=["prop"], lc="move", o="P", at="Mastercard", neo=[2, "Mastercard virtual cards ⚠ issuer not public."],
              mc="Mastercard's main foothold in Booking.com's payments.",
              src=[["Booking.com developers: payouts", PAYOUTS], ["NightsBridge: Booking.com payment options", NIGHTS]]),
            P("banktransfer", "Bank-transfer payouts", "Monthly, weekly or (in some countries) daily payouts to the property's bank account in local currency, net or gross.",
              s=["prop"], lc="move", neo=[0, "Bank transfer."],
              mc="Cross-border payouts that Mastercard Move could carry.",
              src=[["Booking.com developers: payouts", PAYOUTS]]),
            P("stripe", "Stripe payouts", "For homes in the US and Canada only: Stripe pays out, usually daily on the guest's check-in day.",
              s=["prop"], lc="move", o="P", at="Stripe", neo=[0, "Stripe."], src=[["Booking.com developers: payouts", PAYOUTS]]),
        ]},
        {"id": "2.3", "ic": "credit-card", "name": "B2B virtual cards", "blurb": "Mastercard, 2023–24.", "div": "booking", "rev": "merchant", "products": [
            P("mcvcc", "Mastercard Virtual Cards for Pay by Booking", "An expanded partnership (25 January 2024) to speed Mastercard Virtual Cards in Booking.com's payouts to travel partners, with reconciliation, data insights and support for flights, car hire and attractions; announced by Mark Barnett, President, Mastercard Europe.", short="Pay by Booking (Mastercard)",
              s=["prop"], lc="move", ay="Jan 2024", o="P", at="Mastercard", neo=[3, "Mastercard Virtual Cards."],
              src=[["Mastercard: Booking.com collaboration, Jan 2024", MCBOOK], ["Travolution, Jan 2024", TRAVO]]),
            P("agodab2b", "Agoda B2B payments", "Mastercard and Agoda expanded their partnership in 2023 so Agoda can make and receive B2B payments worldwide with Mastercard virtual cards ⚠ month.", short="Agoda B2B (Mastercard)",
              s=["prop"], lc="move", ay="2023", o="P", at="Mastercard", neo=[3, "Mastercard virtual cards."],
              src=[["Mastercard: Agoda B2B partnership, 2023", MCAGODA]]),
        ]},
        {"id": "2.4", "ic": "wallet-cards", "name": "Co-brand cards", "blurb": "Visa at Priceline.", "div": "priceline", "rev": "agency", "products": [
            P("pricelinevisa", "Priceline VIP Rewards Visa", "Issued by Barclays US: 5x points on Priceline, with PricePoints earning on redeemed points (September 2022). Current terms not re-checked ⚠.", short="Priceline (Visa)",
              s=["trav"], lc="borrow", o="P", at="Barclays, Visa", neo=[0, "Visa."],
              mc="Priceline's US co-brand is Visa's.",
              src=[["PYMNTS: Priceline VIP Rewards Visa, Sep 2022", PRICELINE]]),
            P("ktcagoda", "KTC–Agoda Mastercard (Thailand)", "Three tiers from Krungthai Card with Agoda VIP Platinum on approval and bonus points on Agoda; target 150,000 cardmembers in five years (30 March 2022).", short="KTC–Agoda (Mastercard)",
              s=["trav"], lc="borrow", ay="Mar 2022", o="P", at="KTC", neo=[2, "Mastercard, issued by KTC."],
              src=[["KTC: KTC–Agoda Mastercard, Mar 2022", KTC]]),
            P("bookingcard", "Booking.com co-brand", "No Booking.com-branded credit card was found ⚠.",
              s=["trav", "genius"], lc="borrow", st="unconf", neo=[None, "None found ⚠."],
              mc="Open ground for a Genius-linked card."),
        ]},
        {"id": "2.5", "ic": "hand-coins", "name": "Instalments", "blurb": "Affirm; Visa at Agoda.", "div": "booking", "rev": "merchant", "products": [
            P("affirm", "Affirm", "Monthly or bi-weekly plans at Booking.com from 7 September 2023, after Affirm at KAYAK, Agoda and Priceline.",
              s=["trav"], lc="borrow", ay="Sep 2023", o="P", at="Affirm", neo=[0, "Affirm."], src=[["Affirm: Booking.com partnership, Sep 2023", AFFIRM]]),
            P("agodavisa", "Agoda card instalments", "Interest-free instalments for Visa cardholders at checkout, first with HSBC Malaysia (12 May 2022), planned for six more Asian markets.",
              s=["trav"], lc="borrow", ay="May 2022", o="P", at="Visa", neo=[0, "Visa."],
              mc="Mastercard Installments could sit beside it.",
              src=[["Marketech APAC: Agoda and Visa, May 2022", AGODAVISA]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every booking: Genius loyalty, Agoda inside Mastercard's redemption suite, Visa at OpenTable and JCB at Agoda, AI planners and agents, and tools, APIs and reviews for properties.",
    "tiles": [
        {"id": "3.1", "ic": "gift", "name": "Genius loyalty", "blurb": "Across verticals.", "div": "booking", "rev": "merchant", "products": [
            P("genius", "Genius", "Booking.com's tiered loyalty programme, being extended across flights, cars and attractions. Member numbers are not published ⚠.",
              s=["genius"], lc="grow", neo=[0, ""],
              mc="Genius tiers could map to card benefits, as on a co-brand.",
              src=[["Booking Holdings 10-K FY2025", TENK]]),
        ]},
        {"id": "3.2", "ic": "sparkles", "name": "Card loyalty & offers", "blurb": "Mastercard at Agoda, Visa at OpenTable.", "div": "agoda", "rev": "merchant", "products": [
            P("agodaredeem", "Agoda in Mastercard's Global Redemption Suite", "Agoda flights and stays as real-time points redemption for issuing banks in Asia-Pacific, under the banks' own brands (20–21 January 2026); Damien Pfirsch (Agoda) and Matthew Driver (Mastercard).", short="Agoda redemption (Mastercard)",
              s=["partner", "trav"], lc="grow", ay="Jan 2026", st="new", o="P", at="Mastercard", neo=[3, "Mastercard's Global Redemption Suite."],
              mc="A model to take to Booking.com and Priceline.",
              src=[["Mastercard: Agoda redemption, Jan 2026", MCREDEEM], ["TTG Asia, Jan 2026", TTG]]),
            P("visadining", "OpenTable & Visa Dining Collection", "Priority reservations and events for Visa Infinite holders in the US, Canada and Mexico (16 July 2024); a renewal was announced on 6 October 2026 ⚠.", short="Visa Dining Collection (Visa)",
              s=["rest", "trav"], lc="grow", ay="Jul 2024", o="P", at="Visa", neo=[0, "Visa."],
              mc="Visa holds OpenTable's card perks; Priceless has no equivalent here.",
              src=[["PYMNTS: OpenTable and Visa, Jul 2024", OTVISA], ["OpenTable: Visa renewal, Oct 2026", OTRENEW]]),
            P("jcb", "JCB × Agoda", "A three-year agreement (November 2025) giving JCB cardmembers offers on Agoda in key markets from April 2026.",
              s=["trav"], lc="grow", ay="Nov 2025", o="P", at="JCB", st="new", neo=[0, "JCB."], src=[["JCB and Agoda, Nov 2025", JCB]]),
        ]},
        {"id": "3.3", "ic": "bot", "name": "AI planners & agents", "blurb": "Trip Planner to AI agents.", "div": "booking", "rev": "merchant", "products": [
            P("tripplanner", "AI Trip Planner", "A conversational planner on OpenAI's models, in beta for US Genius members from June 2023.",
              s=["trav", "genius"], lc="open", ay="Jun 2023", o="P", at="OpenAI", neo=[0, ""], src=[["PhocusWire: AI Trip Planner, Jun 2023", PLANNER]]),
            P("aiagents", "AI assistants & smart search", "AI support agents, smart filters, review summaries and an AI Car Rental Helper; 'advancing our use of Generative AI' is the CEO's stated priority for 2026.",
              s=["trav"], lc="everyday", st="new", neo=[0, ""], src=[["Booking.com: car rentals in ChatGPT, May 2026", CHATGPT], ["Booking Holdings: Q4 2025 results", Q4]]),
        ]},
        {"id": "3.4", "ic": "code-xml", "name": "Partner tools & trust", "blurb": "APIs, AI replies, reviews.", "div": "booking", "rev": "agency", "products": [
            P("connapi", "Connectivity APIs", "APIs for property-management systems and channel managers, including the Payments by Booking onboarding API that sets payout methods.",
              s=["prop"], lc="open", neo=[0, ""], src=[["Booking.com developers: payouts", PAYOUTS]]),
            P("smartmsg", "Smart Messenger & Auto-Reply", "Generative-AI tools that answer guests for properties.",
              s=["prop"], lc="everyday", st="new", neo=[0, ""], src=[["Booking Holdings 10-K FY2025", TENK]]),
            P("trust", "Reviews & platform trust", "More than 370 million verified reviews; DSA audits as a Very Large Online Platform. Fraud and authentication tooling is not disclosed ⚠.",
              s=["trav", "prop"], lc="everyday", neo=[None, "Fraud tools not public."],
              mc="Merchant-of-record risk now sits on Booking's book; fraud and identity tools could fit.",
              src=[["Booking Holdings: Booking.com", B_BOOKING], ["Booking Holdings 10-K FY2025", TENK]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What Booking Holdings sells: stays on Booking.com, the Connected Trip of flights, cars and attractions, Priceline in the US, Agoda in Asia, KAYAK's search, ads and business travel, and OpenTable for restaurants.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Stays", "blurb": "31m+ listings.", "div": "booking", "rev": "merchant", "products": [
            P("stays", "Booking.com accommodation", "More than 31 million reported listings in 175,000+ destinations and 45 languages; 1,235 million group room nights in 2025.",
              s=["trav", "genius", "prop"], lc="everyday", neo=[1, "Accepts every network."], src=[["Booking Holdings: Booking.com", B_BOOKING], ["Booking Holdings: Q4 2025 results", Q4]]),
            P("altacc", "Alternative accommodation", "Homes and apartments: about 3.9 million properties and about 36% of Booking.com room nights in 2025.",
              s=["trav", "prop"], lc="everyday", neo=[1, "Accepts every network."], src=[["Booking Holdings 10-K FY2025", TENK], ["Booking Holdings: factsheet", FACTS]]),
        ]},
        {"id": "4.2", "ic": "plane", "name": "Connected Trip", "blurb": "Flights +37%.", "div": "booking", "rev": "merchant", "products": [
            P("flights", "Flights", "68 million tickets in 2025 (+37%), about $16.8 billion of gross bookings ⚠; 17 million in Q2 2026 (+3.7%).",
              s=["trav"], lc="everyday", neo=[1, "Accepts every network."], src=[["Booking Holdings 10-K FY2025", TENK], ["Q4 2025 call summary", CALL], ["Booking Holdings: Q2 2026 results", Q2]]),
            P("cars", "Car rental", "Rentalcars.com by Booking.com: 88 million rental car days in 2025 (+5.8%), 23 million in Q2 2026 (−6.5%).",
              s=["trav"], lc="everyday", neo=[1, "Accepts every network."], src=[["Booking Holdings 10-K FY2025", TENK], ["Booking Holdings: Q2 2026 results", Q2]]),
            P("attractions", "Attractions & connected trips", "Attraction tickets up about 80% in 2025; connected-trip transactions grew in the high 20s %, a low double-digit share of Booking.com transactions ⚠. FareHarbor sells booking software to tour operators.",
              s=["trav"], lc="grow", neo=[1, "Accepts every network."], src=[["Booking Holdings 10-K FY2025", TENK], ["Q4 2025 call summary", CALL]]),
        ]},
        {"id": "4.3", "ic": "store", "name": "Priceline", "blurb": "US deals.", "div": "priceline", "rev": "merchant", "products": [
            P("priceline", "Priceline", "Hotels, flights, cars, cruises and packages in 116+ countries, with Express Deals up to 60% off and Priceline VIP.",
              s=["trav"], lc="everyday", neo=[1, "Accepts every network."], src=[["Booking Holdings: Priceline", B_PRICELINE]]),
        ]},
        {"id": "4.4", "ic": "globe", "name": "Agoda", "blurb": "Asia, 6m properties.", "div": "agoda", "rev": "merchant", "products": [
            P("agoda", "Agoda", "Singapore-based, with 6 million+ properties, flights and activities in 39 languages and more than 7,000 staff in 27 markets.",
              s=["trav"], lc="everyday", neo=[1, "Accepts every network."], src=[["Booking Holdings: Agoda", B_AGODA]]),
        ]},
        {"id": "4.5", "ic": "presentation", "name": "KAYAK, meta & business", "blurb": "$1.2bn ads and other.", "div": "kayak", "rev": "ads", "products": [
            P("kayak", "KAYAK, momondo, Cheapflights, HotelsCombined", "Travel search on 60+ sites in 25+ languages, earning most of the group's $1,194 million of advertising and other revenue in 2025; KAYAK took $457 million of impairments in Q3 2025.",
              s=["trav"], lc="grow", neo=[0, ""], src=[["Booking Holdings: KAYAK", B_KAYAK], ["Booking Holdings 10-K FY2025", TENK]]),
            P("biztravel", "KAYAK for Business, Lola, Vayo", "KAYAK's corporate travel tool; Lola and Vayo are listed among the group's brands, their roles not verified ⚠.",
              s=["biz"], lc="everyday", st="unconf", neo=[None, "No card programme found."],
              mc="Commercial and virtual cards for business trips are untested here.",
              src=[["Booking Holdings: KAYAK", B_KAYAK], ["Booking Holdings home page", HOME]]),
        ]},
        {"id": "4.6", "ic": "users-round", "name": "OpenTable", "blurb": "70,000 restaurants.", "div": "opentable", "rev": "ads", "products": [
            P("opentable", "OpenTable", "Reservations and restaurant software for more than 70,000 restaurants seating 2 billion+ diners a year.",
              s=["rest", "trav"], lc="everyday", neo=[0, ""], src=[["Booking Holdings: OpenTable", B_OT]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers and partners reach Booking: the apps, AI front doors such as the Booking.com app in ChatGPT, the extranet for properties, and partners such as Air India.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Apps & sites", "blurb": "Mid-50s % by app.", "div": "booking", "rev": "merchant", "products": [
            P("apps", "Brand apps & websites", "The mobile app took a mid-fifties share of room nights in 2025 (low fifties in 2024); direct B2C mix was in the mid-60s %.",
              s=["trav", "genius"], lc="open", neo=[0, ""], src=[["Booking Holdings 10-K FY2025", TENK], ["Q4 2025 call summary", CALL]]),
        ]},
        {"id": "5.2", "ic": "bot", "name": "AI front doors", "blurb": "Booking.com in ChatGPT.", "div": "booking", "rev": "merchant", "products": [
            P("chatgpt", "Booking.com app in ChatGPT", "Stays and, from 20 May 2026, car rentals searched inside ChatGPT; the customer is sent to Booking.com to pay. Launched for stays in October 2025 ⚠.",
              s=["trav"], lc="open", st="new", o="P", at="OpenAI", neo=[0, "Checkout on Booking.com; no network named."],
              mc="When the agent pays rather than redirects, Agent Pay and agentic tokens are the rails.",
              src=[["Booking.com: car rentals in ChatGPT, May 2026", CHATGPT]]),
        ]},
        {"id": "5.3", "ic": "log-in", "name": "Partner extranet", "blurb": "Where properties get paid.", "div": "booking", "rev": "agency", "products": [
            P("extranet", "Extranet & Finance tab", "Where properties manage rates and see whether each payout comes by virtual card or bank transfer.",
              s=["prop"], lc="everyday", neo=[1, "Shows Mastercard virtual-card payouts ⚠."], src=[["Booking.com developers: payouts", PAYOUTS]]),
        ]},
        {"id": "5.4", "ic": "plug", "name": "Distribution partners", "blurb": "Air India, UEFA.", "div": "booking", "rev": "merchant", "products": [
            P("airindia", "Air India co-branded stays", "Air India's website and app sell stays powered by Booking.com, earning 5 Maharaja Points per INR 100 (22 June 2026).",
              s=["partner", "trav"], lc="grow", ay="Jun 2026", st="new", o="P", at="Air India", neo=[0, ""], src=[["Booking.com: Air India, Jun 2026", AIRINDIA]]),
            P("uefa", "UEFA sponsorship", "Booking.com renewed its UEFA national-team competitions partnership in September 2026.",
              s=["trav"], lc="grow", o="P", at="UEFA", neo=[0, ""], src=[["Booking.com: UEFA renewal, Sep 2026", UEFA]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Booking", "blurb": "Virtual cards, Agoda loyalty.", "products": [
        P("mcatbooking", "Mastercard at Booking Holdings", "Mastercard pays hotels: virtual cards for Booking.com's Pay by Booking (January 2024) and Agoda's B2B payments (2023). In Asia it carries the KTC–Agoda card (2022) and Agoda redemptions for banks (January 2026). Visa holds the Priceline co-brand, Agoda's instalments and OpenTable's dining collection; Affirm and JCB have their own deals. No Booking announcement on Agent Pay, Click to Pay or tokens was found.",
          s=["prop"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Mastercard: Booking.com collaboration, Jan 2024", MCBOOK], ["Mastercard: Agoda redemption, Jan 2026", MCREDEEM], ["PYMNTS: OpenTable and Visa, Jul 2024", OTVISA]]),
    ]},
    {"id": "pillar-market", "name": "Online travel", "blurb": "Merchant mix, AI agents, regulators.", "products": [
        P("market", "The market", "Booking moved from 63% to 70% merchant in a year, taking on payment costs and risk; AI assistants such as ChatGPT are becoming front doors; Europe treats Booking as a gatekeeper. Mastercard's Agent Pay reached all US cardholders in November 2025 ⚠ secondary source.",
          s=["trav"], div="grp", rev="grp", src=[["Booking Holdings 10-K FY2025", TENK], ["Eco: Mastercard Agent Pay explained", AGENTPAY]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
