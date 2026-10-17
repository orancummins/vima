"""Apple's layers, areas and products, read through payments, as at 17 October 2026 (see page_data.py for the format).

Figures are Apple's own unless a source says otherwise: the Q3 FY2026 results (30 July 2026) and their condensed
statements, the Q4 FY2025 statements (30 October 2025), Apple's newsroom, product and support pages, its developer
pages, the European Commission and the CFPB. Apple does not report Apple Pay volumes, users or revenue; payments sit
inside Services. Q4 FY2026 results are due at the end of October. ``neo`` is the Mastercard lens: [depth, note], where
3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

Q3 = "https://www.apple.com/newsroom/2026/07/apple-reports-third-quarter-results/"
Q3FS = "https://www.apple.com/newsroom/pdfs/fy2026q3/FY26_Q3_Consolidated_Financial_Statements.pdf"
Q4FS = "https://www.apple.com/newsroom/pdfs/fy2025-q4/FY25_Q4_Consolidated_Financial_Statements.pdf"
CEO = "https://www.apple.com/newsroom/2026/04/tim-cook-to-become-apple-executive-chairman-john-ternus-to-become-apple-ceo/"
CHASE = "https://www.apple.com/newsroom/2026/01/chase-to-become-new-issuer-of-apple-card/"
JPM = "https://www.jpmorganchase.com/newsroom/press-releases/2026/chase-to-become-new-issuer-of-apple-card"
CARD19 = "https://www.apple.com/newsroom/2019/03/introducing-apple-card-a-new-kind-of-credit-card-created-by-apple/"
PAY14 = "https://www.apple.com/newsroom/2014/09/09Apple-Announces-Apple-Pay/"
APL = "https://www.apple.com/newsroom/2023/03/apple-introduces-apple-pay-later/"
APLEND = "https://www.consumeraffairs.com/news/apple-is-discontinuing-apple-pay-later-061824.html"
TTP22 = "https://www.apple.com/newsroom/2022/02/apple-unveils-contactless-payments-via-tap-to-pay-on-iphone/"
TTPREG = "https://developer.apple.com/tap-to-pay/regions/"
NFCSE = "https://developer.apple.com/support/nfc-se-platform/"
EC = "https://ec.europa.eu/commission/presscorner/detail/en/ip_24_3706"
COUNTRIES = "https://support.apple.com/en-us/102775"
PAYPAGE = "https://www.apple.com/apple-pay/"
CARDPAGE = "https://www.apple.com/apple-card/"
CASHPAGE = "https://www.apple.com/apple-cash/"
WALLETPAGE = "https://www.apple.com/wallet/"
INST = "https://support.apple.com/en-us/120477"
REWARDS = "https://support.apple.com/en-us/120479"
DIGID = "https://www.apple.com/newsroom/2025/11/apple-introduces-digital-id-a-new-way-to-create-and-present-an-id-in-apple-wallet/"
INDIA = "https://www.macrumors.com/2026/09/29/apple-pay-india/"
INDIAP = "https://yourstory.com/2026/09/apple-pay-india-axis-bank-pay-u-launch-partners"
CFPB = "https://www.consumerfinance.gov/archive/newsroom/cfpb-orders-apple-and-goldman-sachs-to-pay-over-89-million-for-apple-card-failures/"
DOJ = "https://www.justice.gov/opa/pr/justice-department-sues-apple-monopolizing-smartphone-markets"
DOJMTD = "https://digital-release.thehill.com/policy/technology/5380007-apple-federal-judge-antitrust-case/"
DOJTALK = "https://www.thestar.com.my/tech/tech-news/2026/07/18/apple-in-early-settlement-talks-with-us-doj-over-antitrust-case-bloomberg-news-reports"
CU = "https://www.pymnts.com/apple/2023/apple-must-face-antitrust-suit-over-apple-pay/"
IOS27 = "https://appleosophy.com/2026/06/09/apples-wallet-app-is-getting-some-neat-updates-in-ios-27/"
STORES = "https://www.macrumors.com/2026/07/12/apple-stores-to-expand-tap-to-pay-on-iphone/"
USERS = "https://www.nasdaq.com/articles/chase-issue-apple-card-whats-ahead-apples-payments-business"
UK15 = "https://finchannel.com/apple-pay-available-to-mastercard-customers-in-the-uk-from-july-14/47073/american-business-trends/banks/2015/07/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "scale · people · entities · rules", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $416.2 billion of sales in FY2025 with $109.2 billion from Services, a new chief executive since September 2026, payments entities that are service providers rather than banks, the Secure Element, and the regulators and courts that are opening the iPhone's NFC chip.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & results", "blurb": "$416.2bn in FY2025.", "div": "grp", "rev": "grp", "products": [
            P("results", "Sales & segments", "Net sales of $416.2 billion in FY2025 (to 27 September 2025): Americas $178.4 billion, Europe $111.0 billion, Greater China $64.4 billion, Japan $28.7 billion, Rest of Asia Pacific $33.7 billion; net income $112.0 billion. Q3 FY2026 (to 27 June 2026): $109.4 billion (+16%), net income $29.8 billion. Market value about $4 trillion (Apple, April 2026).",
              s=["con"], neo=[0, ""], src=[["Apple: Q3 FY2026 statements", Q3FS], ["Apple: Q4 FY2025 statements", Q4FS], ["Apple: CEO succession, Apr 2026", CEO]]),
            P("services", "Services revenue", "$109.2 billion in FY2025 (+14%) and $30.7 billion in Q3 FY2026 (+12%), a June-quarter record. Apple Pay sits inside Services; Apple publishes no payments revenue, volume or user count. Apple Pay active users grew at a double-digit rate in Q4 FY2025 ⚠.",
              s=["con"], neo=[0, ""], src=[["Apple: Q3 FY2026 results", Q3], ["Apple: Q4 FY2025 statements", Q4FS], ["Nasdaq: Apple's payments business, Jan 2026", USERS]]),
        ]},
        {"id": "1.2", "ic": "users-round", "name": "Leadership", "blurb": "Ternus, Cook, Bailey.", "div": "grp", "rev": "grp", "products": [
            P("leadership", "Executives & board", "John Ternus, CEO since 1 September 2026; Tim Cook, Executive Chairman; Arthur Levinson, Lead Independent Director; Kevan Parekh, CFO; Jennifer Bailey, Vice President of Apple Pay and Apple Wallet, who has led Apple Pay since launch. Eddy Cue's Services role is assumed current ⚠.",
              s=["con"], neo=[0, ""], src=[["Apple: CEO succession, Apr 2026", CEO], ["Apple: Q3 FY2026 results", Q3], ["Apple: Apple Card to Chase, Jan 2026", CHASE]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Payments entities", "blurb": "Service providers, not banks.", "div": "card", "rev": "americas", "products": [
            P("entities", "Apple Payments Services LLC & partner banks", "Apple Payments Services LLC is service provider to Goldman Sachs Bank USA for Apple Card and Savings and to Green Dot Bank for Apple Cash; it is not a bank. Apple Financing LLC made the Apple Pay Later loans. Chase is to become the Apple Card issuer.",
              s=["cardh"], o="P", at="Goldman Sachs, Green Dot", neo=[0, ""], src=[["Apple Pay", PAYPAGE], ["Apple: Apple Card to Chase, Jan 2026", CHASE]]),
        ]},
        {"id": "1.4", "ic": "shield-check", "name": "Security & privacy", "blurb": "Secure Element, no card numbers.", "div": "pay", "rev": "grp", "products": [
            P("secure", "Secure Element & Device Account Numbers", "Since 2014, card numbers are not stored on the device or Apple's servers: a Device Account Number sits in the Secure Element, each payment uses a one-time dynamic code, and Face ID or Touch ID approves it. Apple says it does not collect what was bought.",
              s=["con", "iss"], lc="everyday", neo=[1, "Network tokens per scheme; Mastercard's for Mastercard cards ⚠."], src=[["Apple: Apple Pay launch, Sep 2014", PAY14]]),
        ]},
        {"id": "1.5", "ic": "scale", "name": "Regulation & courts", "blurb": "EU NFC, DOJ, CFPB.", "div": "ttp", "rev": "europe", "products": [
            P("ecnfc", "EU NFC commitments", "The European Commission made Apple's commitments binding on 11 July 2024 under Article 102: free NFC access in host card emulation (HCE) for third-party wallets, default-payment-app choice, Field Detect and Double-click, for ten years across the EEA, with a monitoring trustee.",
              s=["dev", "iss"], st="active", ay="Jul 2024", neo=[0, ""], src=[["European Commission: Apple NFC commitments, Jul 2024", EC]]),
            P("doj", "US antitrust cases", "The Justice Department's monopolisation suit (21 March 2024) names digital wallets among five claims; Apple's motion to dismiss was denied in June 2025, and early settlement talks were reported in July 2026, with no trial date. A credit unions' Apple Pay suit was allowed to proceed in 2023.",
              s=["iss"], st="flux", neo=[0, ""], src=[["DOJ: suit against Apple, Mar 2024", DOJ], ["The Hill: motion denied, Jun 2025", DOJMTD], ["The Star: settlement talks, Jul 2026", DOJTALK], ["PYMNTS: credit unions' suit, Sep 2023", CU]]),
            P("cfpb", "CFPB Apple Card order", "On 23 October 2024 the CFPB ordered Apple ($25 million penalty) and Goldman Sachs ($45 million plus $19.8 million of redress) to pay over Apple Card disputes and misleading instalment claims; the order was terminated on 22 September 2025.",
              s=["cardh"], st="retired", neo=[0, ""], src=[["CFPB: Apple and Goldman order, Oct 2024", CFPB]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: Apple Pay in stores, online and in apps on every network, Apple Card on Mastercard moving to Chase, Apple Cash on Visa, partners' instalments and rewards at checkout, Apple Pay in 101 countries and regions with India the newest, and Tap to Pay on iPhone for merchants.",
    "tiles": [
        {"id": "2.1", "ic": "wallet", "name": "Apple Pay", "blurb": "Every network.", "div": "pay", "rev": "americas", "products": [
            P("applepay", "Apple Pay in store", "Contactless payment with iPhone and Apple Watch since 2014, launched with American Express, Mastercard and Visa cards from banks with 83% of US credit card volume; Express Transit; accepted 'at millions of places'.", short="Apple Pay (all networks)",
              s=["con"], lc="move", ay="Sep 2014", neo=[1, "All networks, Mastercard among them."],
              mc="Mastercard has been a network in Apple Pay since the first day.",
              src=[["Apple: Apple Pay launch, Sep 2014", PAY14], ["Apple Pay", PAYPAGE]]),
            P("applepayweb", "Apple Pay online & in apps", "Apple Pay in Safari, in apps and in other browsers, with a redesigned checkout sheet in iOS 27 that shows rewards and debit balances and pay-later options ⚠.",
              s=["con", "mer"], lc="move", st="new", neo=[1, "All networks; competes with Click to Pay."],
              mc="The Apple Pay sheet is where Click to Pay competes for online checkout.",
              src=[["Apple Pay", PAYPAGE], ["Appleosophy: iOS 27 Wallet, Jun 2026", IOS27]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Apple Card", "blurb": "Mastercard, to Chase.", "div": "card", "rev": "americas", "products": [
            P("applecard", "Apple Card", "A US credit card on Mastercard, issued by Goldman Sachs since March 2019: up to 3% Daily Cash, no fees, a titanium card with no printed number, variable APR of 17.49%–27.74% (1 January 2026).", short="Apple Card (Mastercard)",
              s=["cardh"], lc="borrow", ay="Mar 2019", o="P", at="Goldman Sachs, Mastercard", neo=[2, "Mastercard."],
              mc="Apple's only credit card, on Mastercard.",
              src=[["Apple: Apple Card launch, Mar 2019", CARD19], ["Apple: Apple Card to Chase, Jan 2026", CHASE], ["Apple Card", CARDPAGE]]),
            P("chase", "Move to Chase", "Chase will replace Goldman Sachs as issuer in about 24 months from 7 January 2026 (early 2028), taking more than $20 billion of balances; Mastercard stays the network. Linda Kirkpatrick, President of the Americas at Mastercard, was quoted.", short="Chase transition",
              s=["cardh"], lc="borrow", st="flux", ay="Jan 2026", o="P", at="JPMorgan Chase, Mastercard", neo=[2, "Mastercard stays the network."],
              mc="Mastercard kept the card through a move to a mostly Visa issuer.",
              src=[["Apple: Apple Card to Chase, Jan 2026", CHASE], ["JPMorgan Chase: Apple Card, Jan 2026", JPM]]),
            P("acmi", "Apple Card Monthly Installments", "0% APR financing for new Apple products, chosen at checkout in the US, with 3% Daily Cash up front.",
              s=["cardh"], lc="borrow", o="P", at="Goldman Sachs", neo=[2, "On Apple Card, Mastercard."], src=[["Apple: Apple Card to Chase, Jan 2026", CHASE], ["Apple Card", CARDPAGE]]),
            P("family", "Apple Card Family", "Shared Apple Card accounts for members of a Family Sharing group, who need not be related.",
              s=["cardh"], lc="borrow", o="P", at="Goldman Sachs", neo=[2, "Mastercard."], src=[["Apple: Apple Card to Chase, Jan 2026", CHASE]]),
        ]},
        {"id": "2.3", "ic": "send", "name": "Apple Cash", "blurb": "Visa, with Green Dot.", "div": "cash", "rev": "americas", "products": [
            P("applecash", "Apple Cash", "A US stored-value balance from Green Dot Bank for sending money in Messages and paying with Apple Pay; its virtual card number works online 'anywhere Visa is accepted'.", short="Apple Cash (Visa)",
              s=["con"], lc="move", o="P", at="Green Dot Bank, Visa", neo=[0, "Visa."],
              mc="Apple's own debit-like card is Visa's.",
              src=[["Apple Cash", CASHPAGE]]),
            P("taptocash", "Tap to Cash & bill splitting", "Send Apple Cash by holding two iPhones together, up to $2,000 in a rolling seven days; iOS 27 adds receipt scanning to split bills, only where Apple Cash is offered ⚠.",
              s=["con"], lc="move", st="new", o="P", at="Green Dot Bank", neo=[0, "Apple Cash, Visa."], src=[["Apple Cash", CASHPAGE], ["Appleosophy: iOS 27 Wallet, Jun 2026", IOS27]]),
        ]},
        {"id": "2.4", "ic": "hand-coins", "name": "Instalments & rewards", "blurb": "Partners, not Apple.", "div": "pay", "rev": "americas", "products": [
            P("instalments", "Instalments in Apple Pay", "Pay-later and monthly plans 'through an eligible card or pay-later provider': online and in apps since iOS 18, in stores since iOS 26; Affirm is a named US lender ⚠. Not in all markets.",
              s=["con", "iss"], lc="borrow", st="new", o="P", at="Affirm, card issuers", neo=[1, "Card instalments on the card's network; Affirm off-network."],
              mc="Mastercard Installments could reach the sheet through issuers.",
              src=[["Apple Support: instalments, Sep 2026", INST], ["Consumer Affairs: Apple Pay Later ends, Jun 2024", APLEND]]),
            P("rewards", "Pay with rewards", "Redeem a card's cash back, points or miles at checkout as a statement credit: online since iOS 18, in stores since iOS 26; issuers are not named.",
              s=["con", "iss"], lc="grow", st="new", o="P", neo=[1, "Any participating issuer's cards."], src=[["Apple Support: rewards, Sep 2026", REWARDS]]),
            P("paylater", "Apple Pay Later", "Loans of $50 to $1,000 in four payments over six weeks, made by Apple Financing LLC from 28 March 2023 and 'enabled through the Mastercard Installments program', with a Goldman-issued Mastercard credential; ended in June 2024 for partners' instalments.", short="Apple Pay Later (Mastercard Installments)",
              s=["con"], lc="borrow", st="retired", ay="Mar 2023", o="B", at="Mastercard, Goldman Sachs", neo=[3, "Ran on Mastercard Installments."],
              mc="Apple's only in-house loan ran on Mastercard's own instalment product.",
              src=[["Apple: Apple Pay Later, Mar 2023", APL], ["Consumer Affairs: Apple Pay Later ends, Jun 2024", APLEND]]),
        ]},
        {"id": "2.5", "ic": "earth", "name": "Apple Pay abroad", "blurb": "101 places; India new.", "div": "pay", "rev": "rap", "products": [
            P("countries", "Apple Pay worldwide", "101 countries and regions on Apple's list (30 September 2026), 56 of them in Europe; UK Mastercard holders could use it from 14 July 2015. Domestic schemes vary by market ⚠.",
              s=["con", "iss"], lc="move", neo=[1, "All networks."], src=[["Apple Support: Apple Pay countries, Sep 2026", COUNTRIES], ["FinChannel: UK Mastercard launch, Jul 2015", UK15]]),
            P("india", "Apple Pay India", "Live from 30 September 2026 with Axis Bank credit cards on Visa and Mastercard; RuPay and UPI not supported; HDFC Bank, ICICI Bank and SBI Card not yet live. PayU named as a launch partner.", short="India (Visa, Mastercard)",
              s=["con", "iss"], lc="move", st="new", ay="Sep 2026", o="P", at="Axis Bank, PayU", neo=[1, "Visa and Mastercard; not RuPay."],
              mc="Mastercard is one of two networks at launch; more issuers to come.",
              src=[["MacRumors: Apple Pay India, Sep 2026", INDIA], ["YourStory: India launch partners, Sep 2026", INDIAP]]),
            P("transit", "Express Transit", "Tap through transit gates without Face ID, with bank cards or transit cards such as Suica in Japan ⚠.",
              s=["con"], lc="move", neo=[1, "Open-loop cards on any network; closed-loop cards off-network ⚠."], src=[["Apple Pay", PAYPAGE]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Tap to Pay on iPhone", "blurb": "59 countries.", "div": "ttp", "rev": "europe", "products": [
            P("taptopay", "Tap to Pay on iPhone", "Merchants accept contactless cards and wallets on an iPhone with no extra hardware: announced 8 February 2022 with Stripe first, accepting American Express, Discover, Mastercard and Visa; now in 59 countries and regions through PSPs. Built on Mobeewave, bought in 2020 ⚠.",
              s=["mer"], lc="move", ay="Feb 2022", o="P", at="Stripe, Adyen, Square and others", neo=[1, "Accepts Mastercard among others."],
              mc="Mastercard acceptance on Apple's software terminal.",
              src=[["Apple: Tap to Pay on iPhone, Feb 2022", TTP22], ["Apple Developer: Tap to Pay regions", TTPREG]]),
            P("applestores", "Tap to Pay in Apple Stores", "Apple's own stores are replacing Bluetooth card readers with Tap to Pay on iPhone, moving to iPhone 16 units (July 2026) ⚠.",
              s=["mer"], lc="move", st="new", neo=[1, "Accepts every network."], src=[["MacRumors: Apple Stores Tap to Pay, Jul 2026", STORES]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every payment: tokens and device checks, identity documents in Wallet, passes and keys, Tap to Share for loyalty at the counter, and the NFC access that lets other wallets onto the iPhone.",
    "tiles": [
        {"id": "3.1", "ic": "key-round", "name": "Tokens & authentication", "blurb": "Device numbers, Face ID.", "div": "pay", "rev": "grp", "products": [
            P("tokens", "Card tokens", "Each card added to Wallet gets a Device Account Number, a network token from its scheme; Mastercard cards use Mastercard's token service ⚠ not re-verified. Each transaction carries a one-time code.",
              s=["iss", "con"], lc="everyday", o="P", neo=[1, "Mastercard tokens for Mastercard cards ⚠."],
              mc="Every Mastercard in Apple Pay is a Mastercard token.",
              src=[["Apple: Apple Pay launch, Sep 2014", PAY14]]),
            P("devauth", "Device authentication", "Face ID, Touch ID or passcode approves each Apple Pay payment; the same tools are open to EEA HCE wallets under the 2024 commitments.",
              s=["con", "dev"], lc="everyday", neo=[0, ""], src=[["European Commission: Apple NFC commitments, Jul 2024", EC]]),
        ]},
        {"id": "3.2", "ic": "fingerprint", "name": "Identity in Wallet", "blurb": "Digital ID, licences.", "div": "wallet", "rev": "americas", "products": [
            P("digitalid", "Digital ID", "An ID created from a US passport and presented with iPhone or Apple Watch, accepted in beta at more than 250 TSA checkpoints (12 November 2025); not for international travel.",
              s=["con"], lc="open", st="new", ay="Nov 2025", neo=[0, ""],
              mc="Identity sits in the same wallet as the cards.",
              src=[["Apple: Digital ID, Nov 2025", DIGID]]),
            P("licences", "Driver's licences & state IDs", "In Wallet in 12 states and Puerto Rico, with Montana, North Dakota and West Virginia the latest; Government ID on the NFC platform for the EU, New Zealand and the US from iOS 26.4.",
              s=["con"], lc="open", neo=[0, ""], src=[["Apple: Digital ID, Nov 2025", DIGID], ["Apple Developer: NFC & SE Platform", NFCSE]]),
        ]},
        {"id": "3.3", "ic": "wallet-cards", "name": "Passes & keys", "blurb": "Tickets, keys, Create a Pass.", "div": "wallet", "rev": "grp", "products": [
            P("passes", "Passes, tickets & keys", "Boarding passes, event tickets, transit cards and car, home and hotel keys in Wallet; iOS 27 adds trip details to hotel keys ⚠.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Apple Wallet", WALLETPAGE], ["Appleosophy: iOS 27 Wallet, Jun 2026", IOS27]]),
            P("createpass", "Create a Pass", "iOS 27 turns barcode and QR-code cards into Wallet passes by camera or by hand (WWDC, 8 June 2026) ⚠.",
              s=["con", "mer"], lc="grow", st="new", ay="Jun 2026", neo=[0, ""], src=[["Appleosophy: iOS 27 Wallet, Jun 2026", IOS27]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Loyalty at the counter", "blurb": "Tap to Share.", "div": "ttp", "rev": "americas", "products": [
            P("taptoshare", "Tap to Share", "In iOS 27, customers share contact details and loyalty memberships with a merchant through Tap to Pay on iPhone; not in the EU ⚠.",
              s=["mer", "con"], lc="grow", st="new", ay="Jun 2026", neo=[None, "No network role stated."],
              mc="Loyalty at the tap is where Mastercard's offers and loyalty tools play.",
              src=[["Appleosophy: iOS 27 Wallet, Jun 2026", IOS27], ["MacRumors: Apple Stores Tap to Pay, Jul 2026", STORES]]),
        ]},
        {"id": "3.5", "ic": "network", "name": "Open NFC", "blurb": "HCE in the EEA, a platform elsewhere.", "div": "ttp", "rev": "europe", "products": [
            P("hce", "HCE wallets in the EEA", "EEA developers can build in-store payment apps on the iPhone's NFC chip in HCE mode, free of charge, and users can make one their default instead of Apple Pay; no PSP licence is needed. Vipps MobilePay, Curve and PayPal are among reported users ⚠.",
              s=["dev", "iss"], lc="open", ay="Jul 2024", neo=[None, "No public Mastercard role."],
              mc="Third-party wallets on iPhone need tokens and HCE credentials.",
              src=[["European Commission: Apple NFC commitments, Jul 2024", EC]]),
            P("nfcse", "NFC & SE Platform", "A paid entitlement (from iOS 18.1) for banks and licensed PSPs to make in-store payments, keys, badges and IDs with the Secure Element in 49 territories outside the EEA, from the US, UK, Japan, Canada and Australia (iOS 18.1) to India and Vietnam (iOS 26).",
              s=["dev", "iss"], lc="open", st="new", neo=[None, "No public Mastercard role."], src=[["Apple Developer: NFC & SE Platform", NFCSE]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What Apple sells around payments: Services ($109.2 billion in FY2025), the iPhone that carries the wallet, consumer finance through partner banks, acceptance through 100-plus PSPs, and a place in the wallet for issuers.",
    "tiles": [
        {"id": "4.1", "ic": "chart-column", "name": "Services", "blurb": "$30.7bn in Q3 FY2026.", "div": "grp", "rev": "grp", "products": [
            P("servicesline", "Services", "App Store, iCloud, Music, TV, AppleCare, advertising and payments: $109.2 billion in FY2025, 26% of sales, and $91.7 billion in the nine months to June 2026.",
              s=["con"], lc="beyond", neo=[0, ""], src=[["Apple: Q3 FY2026 statements", Q3FS], ["Apple: Q4 FY2025 statements", Q4FS]]),
        ]},
        {"id": "4.2", "ic": "smartphone", "name": "iPhone & devices", "blurb": "$209.6bn of iPhone.", "div": "grp", "rev": "china", "products": [
            P("iphone", "iPhone, Watch & Mac", "iPhone sales of $209.6 billion in FY2025 and $54.3 billion in Q3 FY2026 (+22%), with Greater China up 22%; the installed base of active devices at a new high (no number given; above 2.35 billion in January 2025 ⚠).",
              s=["con"], lc="beyond", neo=[0, ""], src=[["Apple: Q3 FY2026 statements", Q3FS], ["Apple: Q3 FY2026 results", Q3]]),
        ]},
        {"id": "4.3", "ic": "coins", "name": "Consumer finance", "blurb": "$20bn+ of card balances.", "div": "card", "rev": "americas", "products": [
            P("cardbook", "Apple Card book", "More than $20 billion of Apple Card balances moving from Goldman Sachs to Chase; Apple earns as a service provider, not a lender. No account count is published ⚠.",
              s=["cardh"], lc="borrow", st="flux", o="P", at="Goldman Sachs, JPMorgan Chase", neo=[2, "Mastercard."], src=[["JPMorgan Chase: Apple Card, Jan 2026", JPM], ["Apple: Apple Card to Chase, Jan 2026", CHASE]]),
            P("savings", "Savings", "A high-yield savings account opened through Apple Card, provided by Goldman Sachs Bank USA, that takes Daily Cash automatically and transfers from Apple Cash and bank accounts. Its future under Chase is not stated ⚠.",
              s=["cardh"], lc="grow", o="P", at="Goldman Sachs", neo=[0, "A deposit; no network."], src=[["Apple: Apple Card to Chase, Jan 2026", CHASE], ["Apple Card", CARDPAGE]]),
        ]},
        {"id": "4.4", "ic": "briefcase-business", "name": "Merchant acceptance", "blurb": "100+ PSPs.", "div": "ttp", "rev": "europe", "products": [
            P("psps", "PSP programme", "Tap to Pay on iPhone through more than 100 PSPs across 59 countries and regions, among them Adyen, Stripe, Square, Worldline, Nexi, PayPal, Chase, Fiserv's Clover and Visa Acceptance Solutions.",
              s=["mer"], lc="move", o="P", at="PSPs", neo=[1, "Accepts every network."], src=[["Apple Developer: Tap to Pay regions", TTPREG]]),
            P("merchantpay", "Apple Pay for merchants", "Merchants add Apple Pay online and in apps through their PSPs, with no change needed for pay-later options at checkout.",
              s=["mer"], lc="move", o="P", neo=[1, "All networks."], src=[["Apple: Apple Pay Later, Mar 2023", APL], ["Apple Pay", PAYPAGE]]),
        ]},
        {"id": "4.5", "ic": "landmark", "name": "Issuer services", "blurb": "Banks in the wallet.", "div": "pay", "rev": "grp", "products": [
            P("issuers", "Issuer participation", "Banks worldwide add their cards to Apple Pay and, where offered, their instalments and rewards. Apple charges issuers a fee per transaction that it does not disclose ⚠ (reported at about 0.15% on US credit).",
              s=["iss"], lc="everyday", o="P", neo=[1, "Mastercard issuers among them."],
              mc="Every Mastercard issuer in Apple Pay pays Apple and relies on Mastercard tokens.",
              src=[["Apple Pay", PAYPAGE], ["Apple Support: instalments, Sep 2026", INST]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How people reach Apple's payments: the Wallet app on iPhone and Apple Watch, Apple's own stores, and the banks, PSPs and third-party wallets that sit on top.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Wallet app", "blurb": "iPhone and Watch.", "div": "wallet", "rev": "grp", "products": [
            P("walletapp", "Apple Wallet", "Cards, Apple Cash, IDs, keys, tickets and passes in one app on iPhone and Apple Watch, with Mac and iPad for online payments; Apple Card's spending tools sit inside it.",
              s=["con", "cardh"], lc="open", neo=[1, "Holds cards on every network."], src=[["Apple Wallet", WALLETPAGE]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Apple Stores", "blurb": "Tap to Pay at the counter.", "div": "ttp", "rev": "americas", "products": [
            P("stores", "Apple retail", "Apple's stores take Apple Pay and every card, and offer Apple Card Monthly Installments; staff take payment on iPhone.",
              s=["con", "cardh"], lc="open", neo=[1, "Accepts every network."], src=[["MacRumors: Apple Stores Tap to Pay, Jul 2026", STORES], ["Apple Card", CARDPAGE]]),
        ]},
        {"id": "5.3", "ic": "plug", "name": "Partners", "blurb": "Banks, PSPs, wallets.", "div": "pay", "rev": "grp", "products": [
            P("partnerbanks", "Banks & PSPs", "Issuers that put cards in Apple Pay (Axis Bank the newest, in India), PSPs that offer Tap to Pay, and Green Dot, Goldman Sachs and Chase behind Apple's own products.",
              s=["iss", "mer"], lc="open", o="P", neo=[1, "Mixed networks."], src=[["Apple Developer: Tap to Pay regions", TTPREG], ["MacRumors: Apple Pay India, Sep 2026", INDIA]]),
            P("thirdwallets", "Third-party wallets on iPhone", "Bank and fintech wallets using HCE in the EEA or the NFC & SE Platform elsewhere, which users can set as default ⚠ (no Apple list of live apps).",
              s=["dev"], lc="open", st="new", neo=[None, "Not known."], src=[["Apple Developer: NFC & SE Platform", NFCSE], ["European Commission: Apple NFC commitments, Jul 2024", EC]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Apple", "blurb": "Apple Card, Pay Later, every wallet.", "products": [
        P("mcatapple", "Mastercard at Apple", "Mastercard is the network on Apple Card (since 2019, and staying through the move to Chase announced in January 2026), ran Apple Pay Later through Mastercard Installments (2023–24), has been in Apple Pay since 2014 and is one of two networks at the India launch. Visa carries Apple Cash. No Apple work with Mastercard on Click to Pay, Agent Pay, loyalty or open finance was found.",
          s=["cardh"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Apple: Apple Card to Chase, Jan 2026", CHASE], ["Apple: Apple Pay Later, Mar 2023", APL], ["MacRumors: Apple Pay India, Sep 2026", INDIA]]),
    ]},
    {"id": "pillar-market", "name": "Phone wallets", "blurb": "Opened NFC, rivals, rules.", "products": [
        P("market", "The market", "Apple Pay is the in-store wallet on iOS, which the European Commission found dominant in 2024; the EEA is now open to HCE wallets for ten years, a paid platform covers 49 more territories, and the DOJ suit names wallets. Rivals include Google Pay, Samsung Wallet, PayPal, UPI and Pix ⚠.",
          s=["dev"], div="grp", rev="grp", src=[["European Commission: Apple NFC commitments, Jul 2024", EC], ["DOJ: suit against Apple, Mar 2024", DOJ]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
