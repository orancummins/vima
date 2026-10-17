"""Stripe's Foundation layer, as at 17 October 2026 (see page_data.py for the format).

Stripe is private: volumes and customer counts are its own claims (annual letters, Sessions);
revenue and cash flow are press estimates, and say so.
"""
# ruff: noqa: E501

NEWS = "https://stripe.com/newsroom/"
LETTER25 = NEWS + "news/stripe-2025-update"
LETTER24 = NEWS + "news/stripe-2024-update"
INFO = NEWS + "information"
SESSIONS26 = NEWS + "news/sessions-2026"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "scale · licences · founders", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $1.9 trillion of payments a year, a set of licences that now includes its own US acquiring bank, two Irish founders still running it, a payments foundation model, and a strategy to be the economic infrastructure for AI, bought into with OpenRouter.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & economics", "blurb": "$1.9 trillion a year.", "div": "stripe", "rev": "grp", "products": [
            P("tpv", "Total payment volume", "$1.9 trillion in 2025, up 34% and about 1.6% of world GDP, after about $1 trillion in 2023 and $1.4 trillion in 2024 (Stripe's own figures). More than 5 million businesses use Stripe directly or through platforms, including 90% of the Dow Jones and 80% of the Nasdaq 100, and more than 100 process over $1 billion a year.",
              s=["ent", "start", "plat"], neo=[1, "Card volume runs over Visa, Mastercard and the other networks."],
              src=[["Stripe: 2025 annual letter, Feb 2026", LETTER25], ["Stripe: 2024 annual letter, Feb 2025", LETTER24], ["Stripe: newsroom information", INFO]]),
            P("economics", "Revenue, profit & valuation", "Profitable by its own account. Press estimates put revenue at about $6.8 billion in 2025 (up about 33%) and free cash flow at about $3.2 billion. Valued at $159 billion in a February 2026 tender led by Thrive, Coatue and a16z, up from $91.5 billion a year earlier; still private, with 'no rush' to list.", short="Revenue & valuation",
              s=["ent"], neo=[0, ""],
              src=[["Stripe: 2025 annual letter, Feb 2026", LETTER25], ["CNBC: Stripe's tender offer, Feb 2026", "https://www.cnbc.com/2026/02/24/stripe-value-stock-sale-tender-offer.html"], ["Sacra: Stripe (press estimates)", "https://sacra.com/c/stripe/"]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Licences & charters", "blurb": "Its own acquiring bank, since May 2026.", "div": "stripe", "rev": "grp", "products": [
            P("malpb", "Stripe MALPB (Georgia)", "A Georgia merchant-acquirer limited-purpose bank, approved in June 2025 and open for business on 28 May 2026, which lets Stripe acquire card payments directly as a Visa and Mastercard member rather than only through sponsor banks. It cannot take deposits or issue cards.", short="Georgia acquiring bank",
              s=["ent", "start"], st="new", ay="May 2026", neo=[2, "A direct Mastercard acquiring member."],
              mc="Direct membership changes the relationship: Stripe becomes a principal acquirer on Mastercard in the US, with its own say on network services and pricing.",
              src=[["Payments Dive: Stripe's Georgia charter, Apr 2025", "https://www.paymentsdive.com/news/stripe-georgia-special-banking-charter-credit-card-payments/744613/"], ["PYMNTS: payments firms put Georgia charters to work, Sep 2026", "https://www.pymnts.com/news/acquiring/2026/payments-firms-put-georgia-limited-purpose-bank-charter-work/"]]),
            P("emi", "E-money licences in Ireland and the UK", "Stripe Technology Europe is an e-money institution authorised by the Central Bank of Ireland (2019) and passported across the EEA; Stripe Payments UK is authorised by the FCA.", short="Irish & UK e-money",
              s=["ent", "start", "plat"], o="B", ay="2019", neo=[0, ""],
              src=[["Stripe: Stripe Technology Europe", "https://stripe.com/legal/stel"], ["Stripe: Stripe Payments UK", "https://stripe.com/legal/spukl"]]),
            P("bridgecharter", "Bridge National Trust", "Bridge applied to the OCC for a national trust bank in October 2025 and won preliminary conditional approval in February 2026, over opposition from community-bank groups; it is not yet operating.",
              s=["fin", "plat"], st="flux", ay="Feb 2026", neo=[0, ""],
              src=[["CoinDesk: Bridge wins initial charter approval, Feb 2026", "https://www.coindesk.com/business/2026/02/17/stripe-s-stablecoin-firm-bridge-wins-initial-approval-of-national-bank-trust-charter"]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Founders & leadership", "blurb": "Two brothers from Limerick.", "div": "stripe", "rev": "grp", "products": [
            P("founders", "The Collisons", "Founded in 2010 by Patrick (CEO) and John Collison (President), from Limerick; launched in 2011. Headquartered in South San Francisco and Dublin, where a permanent headquarters opened in October 2025. Mission: 'increase the GDP of the internet'.",
              s=["start"], neo=[0, ""], src=[["Stripe: newsroom information", INFO], ["ThinkBusiness: Stripe's Dublin headquarters, Oct 2025", "https://www.thinkbusiness.ie/articles/stripe-dublin-headquarters-expansion/"]]),
            P("leadership", "Leadership & board", "Will Gaybrick (President, technology and business), CFO Steffan Tomlinson, CRO Tyler Bryson, Vice Chair Eileen O'Mara; the CTO post has been empty since Rahul Patil left for Anthropic in October 2025. Board includes Christa Davies (lead independent), Bill Winters and Matt Huang. Roughly 9,000–10,000 staff (estimates).",
              s=["ent"], neo=[0, ""], src=[["Stripe: newsroom information", INFO], ["TechCrunch: Anthropic hires Stripe's CTO, Oct 2025", "https://techcrunch.com/2025/10/02/anthropic-hires-new-cto-with-focus-on-ai-infrastructure"]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Data & AI core", "blurb": "A payments foundation model.", "div": "stripe", "rev": "grp", "products": [
            P("pfm", "Payments foundation model", "A transformer trained on tens of billions of Stripe transactions (May 2025), built with Nvidia, which Stripe says lifted detection of card-testing attacks on large businesses by 64%; it now sits under Radar, authorisation optimisation and dispute tools.",
              s=["ent", "start"], st="new", ay="May 2025", o="P", at="Nvidia", neo=[0, "Stripe's own model, on network data among other things."],
              mc="Stripe's own model competes with network-level intelligence such as Decision Intelligence; network signals are what it cannot see on its own.",
              src=[["TechCrunch: Stripe's foundation model for payments, May 2025", "https://techcrunch.com/2025/05/07/stripe-unveils-ai-foundation-model-for-payments-reveals-deeper-partnership-with-nvidia"]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "Economic infrastructure for AI.", "div": "stripe", "rev": "grp", "products": [
            P("aistrategy", "Economic infrastructure for AI", "Patrick Collison calls AI the biggest platform shift for the economy since the internet: usage and token billing (Metronome), model routing (OpenRouter), agentic commerce with OpenAI, Google, Microsoft and Meta, and stablecoins (Bridge, Privy, Tempo) for machine-to-machine money. Customers include OpenAI, Anthropic, Cursor, Lovable and Vercel.", short="Infrastructure for AI",
              s=["ai", "ent"], st="new", neo=[1, "Card rails under agentic checkout; stablecoins as an alternative."],
              src=[["Stripe: Sessions 2026, Apr 2026", SESSIONS26], ["Stripe: 2025 annual letter, Feb 2026", LETTER25]]),
            P("deals", "Acquisitions", "Paystack (2020), TaxJar (2021), BBPOS (2022), Lemon Squeezy (2024), Bridge ($1.1 billion, closed February 2025), Privy (June 2025), Metronome (January 2026), OpenRouter (agreed August 2026; reported at $7–8 billion), Clerky and Parafin (September 2026). With Advent, Stripe bid about $53 billion for PayPal in July 2026; the bid was reported abandoned in August.", short="Bridge to OpenRouter",
              s=["ent"], o="A", neo=[0, ""],
              src=[["Stripe: completes Bridge acquisition, Feb 2025", "https://stripe.com/us/newsroom/news/stripe-completes-bridge-acquisition"], ["Stripe: agrees to acquire OpenRouter, Aug 2026", NEWS + "news/stripe-agrees-to-acquire-openrouter"], ["Axios: Stripe and Advent bid for PayPal, Jul 2026", "https://www.axios.com/2026/07/15/paypal-bid-stripe-advent"]]),
        ]},
    ],
}
