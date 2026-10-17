"""DBS Group's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the 2Q26 results (6 August 2026), the FY2025
results (9 February 2026) and the 2025 Annual Report. Card networks were read from DBS card pages and
card-face images on 17 October 2026. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's
own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

NR = "https://www.dbs.com/newsroom/"
Q2 = NR + "DBS_second_quarter_net_profit_up_9pct_to_record_SGD_3_08_billion_as_quarterly_total_income_crosses_SGD_6_billion_for_first_time"
Q2S = "https://www.dbs.com/iwov-resources/images/investors/quarterly-financials/2026/2Q26_performance_summary.pdf"
Q2T = "https://www.dbs.com/iwov-resources/images/investors/quarterly-financials/2026/2Q26_media_transcript.pdf"
Q2P = "https://www.dbs.com/iwov-resources/images/investors/quarterly-financials/2026/2Q26_CEO_presentation.pdf"
FY25 = NR + "Full_year_profit_before_tax_at_record_SGD_13_1_billion_net_profit_at_SGD_11_0_billion_with_ROE_at_16_2pct"
AR25 = "https://www.dbs.com/annualreports/2025/i/pdf/dbs-ar-2025.pdf"
INV = "https://www.dbs.com/investors/default.page"
RESHUFFLE = "https://sea.peoplemattersglobal.com/news/business/dbs-reshuffles-leadership-across-hong-kong-taiwan-and-indonesia-ahead-of-2027-transition-51487"
SEAH = "https://theedgemalaysia.com/node/815048"
CEO = "https://finews.asia/people/41820-dbs-tan-su-shan-piyush-gupta-singapore"
HKAI = NR + "DBS_Hong_Kong_Gen_AI_enabled_virtual_assistants_reach_over_1_million_customers_and_go_agentic_EN"
VIC = NR + "DBS_is_first_bank_in_Asia_Pacific_to_pilot_Visa_Intelligent_Commerce_for_everyday_payments"
AGENTSG = "https://newsroom.mastercard.com/news/ap/en/newsroom/press-releases/en/2026/mastercard-delivers-its-first-live-agentic-transaction-in-singapore-with-dbs-and-uob/"
AGENTHK = "https://newsroom.mastercard.com/news/ap/en-hk/newsroom/press-releases/en-hk/2026/mastercard-completes-its-first-live-agentic-transaction-in-hong-kong/"
HOTELS = NR + "DBS_Hong_Kong_unveils_new_DBS_redemption_rewards_converging_points_from_5_leading_hotel_loyalty_programmes_en"
INSTAL = NR + "Mastercard_DBS_Bank_and_Pine_Labs_offer_consumers_a_new_payment_option_in_multiple_Asian_cities"
SGCARDS = "https://www.dbs.com.sg/personal/cards/cards-comparator.page"
HKCARDS = "https://www.dbs.com.hk/personal/credit-cards/default.page"
TWCARDS = "https://www.dbs.com.tw/personal-zh/cards/dbs-credit-cards/default.page"
CITITW = NR + "DBS_completes_acquisition_of_Citis_consumer_banking_business_in_Taiwan"
MAS23 = "https://eastandpartners.com/news/mas-lifts-dbs-capital-requirement-again/"
MAS24 = "https://www.singaporelawwatch.sg/Results/dbs-may-resume-non-essential-banking-activities-but-higher-capital-buffer-stays-mas"
KINEXYS = NR + "DBS_and_Kinexys_by_JP_Morgan_to_develop_framework_for_interbank_tokenised_deposit_transfers_across_multiple_blockchains"
TOKENS = "https://www.theblock.co/post/321926/singapores-biggest-bank-dbs-introduces-token-services-to-enable-blockchain-based-banking"
GOLD = NR + "DBS_expands_gold_offerings_with_market_first_tokenised_physical_gold_for_customers_in_Singapore"
PAYLAH = "https://www.dbs.com.sg/personal/deposits/pay-with-ease/dbs-paylah"
YUU = NR + "DBS_partners_with_leading_retail_brands_to_help_customers_maximise_value_from_everyday_spending"
PASSKEY = "https://newsroom.mastercard.com/news/ap/en/newsroom/press-releases/en/2025/mastercard-champions-password-free-number-free-checkout-across-asia-pacific-by-2030/"
PARTIOR = "https://www.partior.com/"
ASCENDA = "https://www.aap.com.au/aapreleases/cision20260427ae42999/"
CHROMO = "https://www.dbs.com.sg/personal/cards/credit-cards/dbs-chromo-card"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · heritage · AI", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: S$966 billion of assets and a record S$3.08 billion quarterly profit, a CEO who sits on Mastercard's Asia Pacific advisory board, a bank founded in 1968 that MAS penalised for outages, about S$1 billion a year of value from AI, and the Citi Taiwan purchase.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "Record S$3.08bn quarter.", "div": "dbs", "rev": "oth", "products": [
            P("balance", "Balance sheet & earnings", "2Q26 net profit of a record S$3.08 billion (+9%) on income of S$6.09 billion; ROE 17.9%; CET1 16.6%; deposits S$638 billion, loans S$469 billion and assets S$965.6 billion at 30 June 2026. FY2025 net profit S$11.0 billion (ROE 16.2%). Market value US$124 billion at end-2025; rated AA- and Aa1 ⚠ agencies not named.",
              s=["corp"], neo=[0, ""], src=[["2Q26 results", Q2], ["2Q26 performance summary", Q2S], ["FY2025 results", FY25], ["Annual Report 2025", AR25]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Tan Su Shan, CEO since 2025.", "div": "dbs", "rev": "oth", "products": [
            P("leadership", "Board & management", "CEO Tan Su Shan since 28 March 2025, after Piyush Gupta; she sits on Mastercard's Asia Pacific Advisory Board. Chairman Peter Seah since 2010, with succession reported in August 2026. New country heads for Indonesia, Taiwan and Hong Kong from December 2026 to March 2027. About 39,900 staff.",
              s=["corp"], st="flux", neo=[0, ""], mc="A direct executive link: the CEO advises Mastercard in Asia Pacific.",
              src=[["Annual Report 2025", AR25], ["finews.asia: CEO succession, Aug 2024", CEO], ["People Matters: reshuffle, Aug 2026", RESHUFFLE], ["The Edge: chairman succession, Aug 2026", SEAH]]),
        ]},
        {"id": "1.3", "ic": "flag", "name": "Heritage & regulation", "blurb": "1968; MAS penalties.", "div": "dbs", "rev": "oth", "products": [
            P("heritage", "Heritage & brands", "Founded in 1968 as the Development Bank of Singapore; POSB is its mass-market brand. Named World's Best Bank 2025 by Euromoney, Global Finance and The Banker.",
              s=["con"], o="I", neo=[0, ""], src=[["Annual Report 2025", AR25], ["DBS investors", INV]]),
            P("mas", "MAS capital multiplier", "After digital outages MAS set a 1.5x operational-risk capital multiplier in 2022 and raised it to 1.8x in May 2023 (about S$1.6 billion of capital); a six-month pause on non-essential activity ended in April 2024 ⚠ current multiplier status not found.",
              s=["corp"], st="unconf", neo=[0, ""], src=[["East & Partners: MAS multiplier, May 2023", MAS23], ["Singapore Law Watch: pause ends, Apr 2024", MAS24]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Data & AI", "blurb": "About S$1bn from AI.", "div": "dbs", "rev": "oth", "products": [
            P("ai", "Data & AI", "More than 2,000 models across 430 use cases, worth about S$1 billion in 2025; DBS-GPT for all staff; agents planned across 12 'big journeys'; over 11,000 staff marked for AI reskilling.",
              s=["corp"], neo=[0, ""], src=[["Annual Report 2025", AR25], ["2Q26 media briefing", Q2T]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "ROE 15–17%, Citi Taiwan.", "div": "dbs", "rev": "oth", "products": [
            P("strategy", "Targets", "ROE of 15–17% over the medium term, an S$8 billion capital return for 2025–27 and an ambition of more than S$1 trillion of wealth and retail assets; guidance raised in August 2026.",
              s=["corp"], neo=[0, ""], src=[["Annual Report 2025", AR25], ["2Q26 CEO presentation", Q2P]]),
            P("deals", "Deals", "Citi's Taiwan consumer business (August 2023): customers doubled to more than 1.1 million and card accounts rose about fivefold to more than 3 million. The Shenzhen Rural Commercial Bank stake rose to 19.9% in 2025; card and unsecured-lending partnerships in India were exited in 2025.",
              s=["con", "card"], o="A", neo=[None, "Network mix of the Citi accounts not public."],
              mc="Three million migrated Taiwan card accounts, network mix unknown.",
              src=[["Citi Taiwan completed, Aug 2023", CITITW], ["Annual Report 2025", AR25]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Singapore credit cards split between Visa, Mastercard and Amex, Hong Kong and Taiwan cards, debit, Mastercard Installments, PayNow and PayLah!, cross-border remittances, and tokenised deposits, Partior and a digital exchange.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Singapore credit cards", "blurb": "5 Visa, 5 Mastercard, 3 Amex.", "div": "dbs", "rev": "cbg", "products": [
            P("altitude", "Altitude & Vantage", "The premium miles cards: Altitude Visa Signature (also on Amex) at up to 2.2 miles per S$1 overseas, and Vantage Visa Infinite. Group card fees were S$1,225 million in 2025 (−1%).", short="Altitude & Vantage (Visa)",
              s=["card"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."],
              mc="The premium miles franchise is Visa's.",
              src=[["DBS Singapore cards", SGCARDS], ["Annual Report 2025", AR25]]),
            P("chromo", "DBS Chromo Card", "A Visa card for ages 21–29 with up to 5% cash back on two top categories and no FX fee ⚠ appears to have replaced Live Fresh in Singapore.", short="Chromo (Visa)",
              s=["card"], lc="borrow", st="new", o="P", at="Visa", neo=[0, "Visa."], src=[["DBS Chromo Card", CHROMO]]),
            P("womans", "DBS Woman's & Woman's World Mastercard", "5X and 10X points online (up to 4 miles per S$1).", short="Woman's (Mastercard)",
              s=["card"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["DBS Singapore cards", SGCARDS]]),
            P("posbeveryday", "POSB Everyday Card", "Up to 10% dining rebates; the card face shows Mastercard ⚠ it may once have been Visa.", short="POSB Everyday (Mastercard)",
              s=["card", "con"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard ⚠ switch unconfirmed."], src=[["DBS Singapore cards", SGCARDS]]),
            P("partnercards", "Partner cards", "Esso Mastercard (up to 23% fuel savings) and SAFRA DBS Mastercard; yuu and Takashimaya cards on Visa or Amex.", short="Partner cards (mixed)",
              s=["card"], lc="borrow", o="P", at="Esso, SAFRA, yuu, Takashimaya", neo=[1, "Esso and SAFRA on Mastercard; yuu and Takashimaya on Visa or Amex."], src=[["DBS Singapore cards", SGCARDS], ["DBS retail partners, Jul 2025", YUU]]),
        ]},
        {"id": "2.2", "ic": "globe", "name": "Hong Kong & Taiwan cards", "blurb": "Black World on Mastercard.", "div": "hk", "rev": "cbg", "products": [
            P("hkcards", "Hong Kong cards", "DBS Black World Mastercard and Live Fresh World Mastercard; Eminent Visa Signature and COMPASS Visa; DBS Card+ issued in the app ⚠ network not stated.", short="Hong Kong (mixed)",
              s=["card"], lc="borrow", o="P", at="Mastercard, Visa", neo=[1, "Premium Black World on Mastercard; Eminent and COMPASS on Visa."], src=[["DBS Hong Kong cards", HKCARDS]]),
            P("twcards", "Taiwan cards", "Travel World Elite ⚠ Mastercard from the image file name, everyday Visa Signature, Infinite cards ⚠ likely Visa, and a Garena gaming co-brand (2025, network not stated).", short="Taiwan (mixed ⚠)",
              s=["card"], lc="borrow", o="P", neo=[1, "World Elite ⚠ on Mastercard; Visa tiers."], src=[["DBS Taiwan cards", TWCARDS], ["Annual Report 2025", AR25]]),
        ]},
        {"id": "2.3", "ic": "wallet-cards", "name": "Debit", "blurb": "3 Visa, 2 Mastercard, 1 UnionPay.", "div": "posb", "rev": "cbg", "products": [
            P("debitcards", "Debit cards", "DBS Visa Debit, TravelLah! Visa Platinum (no FX or ATM fees, linked to the PayLah! multi-currency wallet) and Takashimaya Visa; PAssion POSB Platinum Mastercard (up to 9% with yuu partners) and SAFRA Mastercard; a UnionPay card for China.", short="Debit (mostly Visa)",
              s=["con"], lc="everyday", o="P", at="Visa, Mastercard, UnionPay", neo=[1, "PAssion and SAFRA on Mastercard; main and travel debit on Visa."], src=[["DBS Singapore cards", SGCARDS], ["DBS PayLah!", PAYLAH]]),
        ]},
        {"id": "2.4", "ic": "refresh-cw", "name": "Instalments", "blurb": "Mastercard Installments, 2022.", "div": "dbs", "rev": "cbg", "products": [
            P("installments", "Mastercard Installments with Pine Labs", "Launched in Singapore on 1 March 2022 for about 2 million cardholders across Visa, Mastercard and Amex; DBS was Asia's first regional issuer on it ⚠ current status and rollout unknown.",
              s=["card"], lc="borrow", ay="Mar 2022", o="P", at="Mastercard, Pine Labs", neo=[3, "Mastercard Installments ⚠ status."], src=[["Mastercard Installments, Mar 2022", INSTAL]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "PayNow & PayLah!", "blurb": "60% of hawker QR.", "div": "paylah", "rev": "cbg", "products": [
            P("paylah", "DBS PayLah!", "A wallet with more than 3 million users and over 60% of QR payments at hawker centres: Scan & Pay over PayNow, SGQR and NETS QR, Express Checkout and Teen Mode.",
              s=["con"], lc="everyday", neo=[0, "Account-to-account."],
              mc="QR payments at the till run off card rails.",
              src=[["Annual Report 2025", AR25], ["DBS PayLah!", PAYLAH]]),
            P("paynow", "PayNow & linked corridors", "DBS handled 60% of PayNow cross-border transfers in 2025, launched PayNow–DuitNow and widened PayNow–UPI.",
              s=["con", "sme"], lc="move", neo=[0, "National rail."], src=[["Annual Report 2025", AR25]]),
            P("alipay", "Alipay+ & Weixin Pay links", "PayLah! users can pay at more than 150 million Alipay+ merchants, and DBS Remit can send to WeChat wallets.",
              s=["con"], lc="move", o="P", at="Ant International, Tencent", neo=[0, ""], src=[["Annual Report 2025", AR25]]),
        ]},
        {"id": "2.6", "ic": "send", "name": "Cross-border", "blurb": "Remit, GlobeSend.", "div": "dbs", "rev": "ibg", "products": [
            P("remit", "DBS Remit", "Consumer remittances, same-day and fee-free from Taiwan.",
              s=["con", "mig"], lc="move", neo=[0, ""],
              mc="Mastercard Move could add card and wallet endpoints beyond UPI, DuitNow, Alipay+ and WeChat.",
              src=[["Annual Report 2025", AR25]]),
            P("globesend", "DBS GlobeSend", "A cross-border payments portal for SMEs, launched in Taiwan in 2025 'to compete with fintechs'.",
              s=["sme"], lc="move", st="new", neo=[0, ""], src=[["Annual Report 2025", AR25], ["2Q26 media briefing", Q2T]]),
        ]},
        {"id": "2.7", "ic": "coins", "name": "Digital money", "blurb": "Tokens, Partior, DDEx.", "div": "ddex", "rev": "ibg", "products": [
            P("tokens", "DBS Token Services", "Treasury Tokens (tokenised deposits), conditional payments and programmable rewards on a permissioned chain (launched 2024 ⚠ month), extended to Singapore and Hong Kong clients in 2025; an interbank framework with J.P. Morgan's Kinexys (November 2025).",
              s=["corp"], lc="move", o="B", neo=[0, "DBS's own chain."],
              mc="No Mastercard Multi-Token Network link is visible.",
              src=[["The Block: Token Services ⚠", TOKENS], ["Kinexys framework, Nov 2025", KINEXYS], ["Annual Report 2025", AR25]]),
            P("partior", "Partior", "Round-the-clock atomic cross-border and FX settlement; DBS uses it and Lim Soon Chong sits on its board ⚠ shareholding not verified.",
              s=["corp"], lc="move", o="P", at="Partior", neo=[0, ""], src=[["Partior", PARTIOR], ["Annual Report 2025", AR25]]),
            P("ddex", "DBS Digital Exchange & gold tokens", "Lists Ripple's RLUSD stablecoin and Franklin Templeton's sgBENJI fund; tokenised notes on Ethereum; tokenised physical gold announced June 2026, on digibank from H2 2026.",
              s=["wealth", "corp"], lc="grow", st="new", neo=[0, ""], src=[["Annual Report 2025", AR25], ["Tokenised gold, Jun 2026", GOLD]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: scam controls that cut wallet-provisioning scams by 98%, the first live agentic card payments in Singapore and Hong Kong, digibot and Joy, and points with Mastercard Gamer Exchange and hotel conversion.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Scams & fraud", "blurb": "98% fewer wallet scams.", "div": "dbs", "rev": "cbg", "products": [
            P("scams", "Scam & fraud controls", "35% more scam saves in 2025; the first bank to take on the full surveillance duties of the MAS Shared Responsibility Framework; time-bound controls on adding cards to mobile wallets cut related scams by 98%; mule detection up 175%.",
              s=["con"], lc="everyday", neo=[0, "DBS's own."],
              mc="Mastercard's 2027 tokenised-checkout target for Singapore fits the wallet-provisioning work.",
              src=[["Annual Report 2025", AR25], ["Mastercard: password-free checkout, Nov 2025", PASSKEY]]),
        ]},
        {"id": "3.2", "ic": "sparkles", "name": "Agentic payments", "blurb": "Visa first, Mastercard live.", "div": "dbs", "rev": "cbg", "products": [
            P("agentpay", "Mastercard Agent Pay", "Singapore's first live authenticated agentic transaction with DBS and UOB (4 March 2026), using an agentic token and Mastercard Payment Passkeys; DBS Hong Kong took part in the first in Hong Kong (27 March 2026).",
              s=["card"], lc="move", st="new", ay="Mar 2026", o="P", at="Mastercard", neo=[3, "Mastercard Agent Pay."],
              mc="First live agentic payments in both of DBS's wealth hubs.",
              src=[["Mastercard: Singapore agentic transaction, Mar 2026", AGENTSG], ["Mastercard: Hong Kong agentic transaction, Mar 2026", AGENTHK]]),
            P("vic", "Visa Intelligent Commerce pilot", "DBS was the first Asia Pacific bank to pilot it (16 February 2026), on food and beverage payments with DBS and POSB credit and debit cards; online shopping and travel next.",
              s=["card", "con"], lc="move", st="new", ay="Feb 2026", o="P", at="Visa", neo=[0, "Visa."], src=[["Visa Intelligent Commerce pilot, Feb 2026", VIC]]),
        ]},
        {"id": "3.3", "ic": "bot", "name": "Virtual assistants", "blurb": "digibot and Joy go agentic.", "div": "dbs", "rev": "cbg", "products": [
            P("digibot", "DBS digibot", "Launched 2016; more than 5 million users in Singapore and more than a million in Hong Kong; resolved 9 in 10 queries without a follow-up call in H1 2026; agentic card block and replace and fee waivers due in 2027.",
              s=["con"], lc="everyday", neo=[0, ""],
              mc="Card servicing by agent from 2027 is an opening for agentic tokens.",
              src=[["DBS Hong Kong agentic assistants, Sep 2026", HKAI]]),
            P("joy", "DBS Joy", "The DBS IDEAL corporate assistant for more than 100,000 Hong Kong users, with hotline calls down 16%; agentic in Hong Kong from 26 September 2026.",
              s=["corp"], lc="move", st="new", ay="Sep 2026", neo=[0, ""], src=[["DBS Hong Kong agentic assistants, Sep 2026", HKAI]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Loyalty", "blurb": "Gamer Exchange, hotel points.", "div": "dbs", "rev": "cbg", "products": [
            P("points", "DBS Points, Daily$ & DBS$", "DBS Points, POSB Daily$, non-expiring DBS$ in Hong Kong, InstaRedeem and the yuu partner rebates (July 2025); Ascenda runs a loyalty partnership in Hong Kong (April 2026).",
              s=["card", "con"], lc="grow", o="P", at="Ascenda, yuu", neo=[0, "DBS's own."], src=[["DBS retail partners, Jul 2025", YUU], ["Ascenda and DBS Hong Kong, Apr 2026", ASCENDA]]),
            P("gamer", "Mastercard Gamer Exchange", "DBS was the first in Singapore to let points be redeemed for gaming credits (2025).",
              s=["card"], lc="grow", st="new", o="P", at="Mastercard", neo=[3, "Mastercard's own."], src=[["Annual Report 2025", AR25]]),
            P("hotels", "Black World hotel conversion", "Since 27 April 2026 DBS$ convert to Accor, Hilton, IHG, Marriott and Shangri-La points, which Mastercard called an expanded partnership in the premium space.",
              s=["card"], lc="grow", st="new", ay="Apr 2026", o="P", at="Mastercard", neo=[2, "On Black World Mastercard."], src=[["DBS Hong Kong hotel rewards, Apr 2026", HOTELS]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: consumer banking led by POSB, S$516 billion of wealth assets, institutional banking and transaction services, markets, and franchises in Hong Kong, Taiwan, China, India and Indonesia.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Consumer banking", "blurb": "Singapore's savings leader.", "div": "posb", "rev": "cbg", "products": [
            P("posbbank", "DBS & POSB consumer banking", "Leader in Singapore savings deposits; about 75% of Work Permit holders use POSB digibank. Consumer Banking/Wealth Management earned S$5.52 billion in H1 2026 (+5%).",
              s=["con", "mig"], lc="everyday", neo=[1, "Debit and POSB cards split."], src=[["Annual Report 2025", AR25], ["2Q26 performance summary", Q2S]]),
        ]},
        {"id": "4.2", "ic": "gem", "name": "Wealth", "blurb": "S$516 billion of assets.", "div": "treasures", "rev": "cbg", "products": [
            P("treasures", "Treasures, Treasures Private Client & Private Bank", "Wealth assets of S$516 billion (2Q26) with S$11 billion of net new money in the quarter; wealth fees of S$919 million (+42%); banks about a third of Singapore's 2,000-plus single family offices.",
              s=["wealth"], lc="grow", neo=[0, ""], src=[["2Q26 results", Q2], ["Annual Report 2025", AR25]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Institutional banking", "blurb": "Record transaction fees.", "div": "dbs", "rev": "ibg", "products": [
            P("ibg", "Institutional Banking & Global Transaction Services", "Cash management, trade and transaction services; transaction-service fees of a record S$942 million in 2025; the first Singapore bank appointed as an RMB clearing bank.",
              s=["corp", "sme"], lc="move", neo=[None, "Commercial card network not public."], src=[["Annual Report 2025", AR25], ["2Q26 performance summary", Q2S]]),
        ]},
        {"id": "4.4", "ic": "chart-candlestick", "name": "Markets", "blurb": "Record treasury sales.", "div": "dbs", "rev": "gfm", "products": [
            P("gfm", "Global Financial Markets", "Record treasury customer sales of about S$680 million in 2Q26 and the highest markets trading income in five years in H1 2026.",
              s=["corp", "wealth"], lc="grow", neo=[0, ""], src=[["2Q26 results", Q2], ["2Q26 media briefing", Q2T]]),
        ]},
        {"id": "4.5", "ic": "earth", "name": "Markets beyond Singapore", "blurb": "Hong Kong, Taiwan, India.", "div": "dbs", "rev": "cbg", "products": [
            P("hongkong", "DBS Hong Kong", "H1 2026 income of S$1.95 billion and net profit of S$1.03 billion (+23% in constant currency); one of DBS's two wealth hubs.",
              s=["con", "wealth"], lc="everyday", neo=[1, "Black World and Live Fresh on Mastercard."], src=[["2Q26 performance summary", Q2S]]),
            P("taiwan", "DBS Taiwan & China", "Rest of Greater China earned S$1.24 billion in H1 2026; DBS is Taiwan's largest foreign bank by assets after the Citi deal.",
              s=["con"], lc="everyday", neo=[1, "Mixed card networks ⚠."], src=[["2Q26 performance summary", Q2S], ["Citi Taiwan completed, Aug 2023", CITITW]]),
            P("southasia", "DBS India & Indonesia", "South and Southeast Asia earned S$815 million in H1 2026; India income was a record S$909 million in 2025 ⚠ card lineups not found.",
              s=["con"], lc="everyday", neo=[None, "Card lineups not found."], src=[["2Q26 performance summary", Q2S], ["Annual Report 2025", AR25]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach DBS: digibank in four markets, DBS IDEAL for companies, and partners from yuu and Esso to Alipay+ and Garena.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "digibank", "blurb": "Four markets.", "div": "dbs", "rev": "cbg", "products": [
            P("digibank", "digibank", "The mobile bank in Singapore, Hong Kong, India and Indonesia, with the DBS Card+ app in Hong Kong ⚠ branch and ATM counts not found.",
              s=["con", "mig", "wealth"], lc="everyday", neo=[0, ""], src=[["Annual Report 2025", AR25], ["DBS Hong Kong agentic assistants, Sep 2026", HKAI]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "DBS IDEAL", "blurb": "The corporate channel.", "div": "dbs", "rev": "ibg", "products": [
            P("ideal", "DBS IDEAL", "Online banking for companies and SMEs, home of the Joy assistant.",
              s=["corp", "sme"], lc="move", neo=[0, ""], src=[["DBS Hong Kong agentic assistants, Sep 2026", HKAI]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partners", "blurb": "yuu, Esso, Alipay+.", "div": "dbs", "rev": "cbg", "products": [
            P("partners", "Partners & ecosystems", "yuu retail partners (Cold Storage, Giant, Guardian, 7-Eleven), Esso, SAFRA, Takashimaya, Garena, Alipay+ and Weixin Pay.",
              s=["card", "con"], lc="open", o="P", neo=[1, "Esso and SAFRA on Mastercard."], src=[["DBS retail partners, Jul 2025", YUU], ["DBS Singapore cards", SGCARDS], ["Annual Report 2025", AR25]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at DBS", "blurb": "An even split, agents first.", "products": [
        P("mcatdbs", "Mastercard at DBS", "Singapore's credit cards split five Visa, five Mastercard and three Amex: Visa holds the premium miles cards (Altitude, Vantage), the youth card and the main debit cards; Mastercard holds Woman's World, POSB Everyday, Esso, SAFRA and PAssion debit, and in Hong Kong the premium Black World. DBS piloted Visa Intelligent Commerce first (February 2026) and ran Singapore's first live Mastercard Agent Pay payment three weeks later. The CEO sits on Mastercard's Asia Pacific advisory board.",
          s=["card"], div="dbs", rev="oth", mc="The relationship this map is drawn for.",
          src=[["DBS Singapore cards", SGCARDS], ["Mastercard: Singapore agentic transaction, Mar 2026", AGENTSG], ["Visa Intelligent Commerce pilot, Feb 2026", VIC]]),
    ]},
    {"id": "pillar-market", "name": "Singapore & Asia", "blurb": "Scams, QR, tokens.", "products": [
        P("market", "The market", "MAS's Shared Responsibility Framework for scams, account-to-account QR and PayNow corridors, tokenised money and stablecoins, a 15% global minimum tax, and rivals OCBC, UOB, Standard Chartered, Citi, HSBC and digital banks.",
          s=["con"], div="dbs", rev="oth", src=[["Annual Report 2025", AR25], ["FY2025 results", FY25]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
