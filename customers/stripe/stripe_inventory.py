"""Stripe's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Volumes and counts are Stripe's own claims (annual letters, Sessions, its blog) unless a source says
otherwise. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product or network
runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

from stripe_foundation import FOUNDATION

NEWS = "https://stripe.com/newsroom/news/"
BLOG = "https://stripe.com/blog/"
S25 = NEWS + "sessions-2025"
S26 = NEWS + "sessions-2026"
S26ALL = BLOG + "everything-we-announced-at-sessions-2026"
LETTER25 = NEWS + "stripe-2025-update"
SPT = "https://stripe.com/br/blog/supporting-additional-payment-methods-for-agentic-commerce"
FINTECHS = BLOG + "new-ways-for-fintechs-to-move-money-and-expand-globally"
OUSD = NEWS + "ousd-is-now-available-on-stripe"
TEMPO_TESTNET = "https://decrypt.co/351661/stripes-tempo-payments-blockchain-opens-public-mastercard-ubs-onboard"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves through Stripe: cards and 125-plus local methods accepted as a principal acquirer, bank rails, payouts to cards, banks and wallets in 160 countries, 400 million issued cards, stablecoins from Bridge to OUSD on Tempo, and balances held in Treasury.",
    "tiles": [
        {"id": "2.1", "ic": "store", "name": "Acceptance & acquiring", "blurb": "Cards and 125-plus methods.", "div": "stripe", "rev": "pay", "products": [
            P("acquiring", "Stripe as acquirer", "A principal acquirer on Visa and Mastercard in Europe (Stripe Technology Europe), the UK and other markets, and in the US through its own Georgia acquiring bank (May 2026) alongside sponsor acquirers such as Goldman Sachs.",
              s=["ent", "start", "plat"], lc="move", neo=[2, "Direct Mastercard membership as acquirer."],
              mc="As a principal member Stripe chooses which network services to switch on for 5 million businesses: tokens, authentication, merchant data and disputes.",
              rel=["malpb"], src=[["TechCrunch: no, Stripe is not becoming a bank, Apr 2025", "https://techcrunch.com/2025/04/08/no-stripe-is-not-becoming-a-bank"], ["Stripe: STEL financial terms", "https://stripe.com/legal/stel-financial-terms"]]),
            P("methods", "Payment methods", "Cards plus more than 125 methods, from Apple Pay, Google Pay, Klarna and Affirm to Pix (up to 38% more conversion in Brazil), UPI, BLIK, Bizum and TWINT; 25 added at Sessions 2025 and more in 2026.",
              s=["ent", "start", "retail"], lc="move", neo=[1, "Mastercard among many networks and methods."],
              src=[["Stripe: Sessions 2025", S25], ["Stripe: new ways to turn global demand into revenue, Jun 2026", BLOG + "new-ways-to-turn-global-demand-into-revenue"]]),
            P("terminal", "Terminal & Tap to Pay", "In-person payments on Stripe readers, Verifone devices and phones (Tap to Pay on iPhone and Android); the Reader T600 and 15 more markets in 2026.",
              s=["retail", "ent", "plat"], lc="move", neo=[1, "Contactless Mastercard among other methods."],
              src=[["Stripe: everything announced at Sessions 2026", S26ALL]]),
        ]},
        {"id": "2.2", "ic": "arrow-left-right", "name": "Bank rails", "blurb": "ACH, SEPA, Pix, UPI.", "div": "stripe", "rev": "pay", "products": [
            P("bankrails", "Bank debits & pay by bank", "ACH, SEPA, pay by bank and instant rails such as Pix and UPI, with Radar now screening ACH and SEPA (fraud down 20% and 42%); US RTP due by the end of 2026.",
              s=["saas", "ent"], lc="move", neo=[0, "Account-to-account."],
              mc="US pay by bank is where Mastercard Open Finance competes with Stripe's own Financial Connections.",
              src=[["Stripe: Sessions 2025", S25], ["Stripe: everything announced at Sessions 2026", S26ALL]]),
        ]},
        {"id": "2.3", "ic": "send", "name": "Payouts", "blurb": "160 countries, in minutes.", "div": "stripe", "rev": "plat", "products": [
            P("instantpayouts", "Instant Payouts", "Push-to-debit payouts to sellers' cards over Mastercard Send and Visa Direct, arriving in about 30 minutes, up to $9,999 a payout.",
              s=["plat"], lc="move", o="P", at="Mastercard, Visa", ay="Sep 2016", neo=[1, "Mastercard Send beside Visa Direct."],
              src=[["PYMNTS: Mastercard Send and Stripe, 2016", "https://www.pymnts.com/mastercard/2016/mastercard-send-stripe-real-time-payments/"], ["Mastercard Move: Stripe as a licensed provider", "https://b2b.mastercard.com/move/partner-program/find-a-partner/licensed-providers/stripe"]]),
            P("globalpayouts", "Global Payouts", "Pay third parties by email in more than 100 countries in local currency and 160 in stablecoins (June 2025); Turo has paid out more than $160 million at a 99.5% success rate.",
              s=["plat", "fin"], lc="move", st="new", ay="Jun 2025", neo=[0, "Bank and stablecoin rails."],
              mc="Mastercard Move reaches cards, accounts and wallets in the corridors where bank payouts fail.",
              src=[["Stripe: Global Payouts, Jun 2025", "https://stripe.com/gb/blog/global-payouts-a-new-way-to-send-money-directly-to-third-parties"], ["Stripe: new ways for fintechs to move money, Oct 2026", FINTECHS]]),
        ]},
        {"id": "2.4", "ic": "credit-card", "name": "Issuing", "blurb": "400 million cards.", "div": "stripe", "rev": "money", "products": [
            P("issuing", "Stripe Issuing", "Card programmes for fintechs and platforms on Visa and Mastercard: more than 400 million cards, with Ramp the flagship customer; managed consumer credit (2025) and consumer debit in preview (2026).",
              s=["fin", "plat"], lc="move", neo=[1, "Visa and Mastercard; Mastercard added to the settlement API in May 2026."],
              mc="Every new card programme on Stripe is a network choice; commercial-card controls and data are where Mastercard can win them.",
              src=[["Stripe: Issuing for commercial cards", "https://stripe.com/issuing/commercial"], ["Stripe: Ramp", "https://stripe.com/en-cy/customers/ramp"]]),
            P("bridgecards", "Stablecoin-linked cards", "Bridge-issued cards that spend stablecoin balances anywhere Visa is taken: six Latin American markets in April 2025, more than 65 countries by October 2026 (Kraken, Ramp, Morse), about $1.2 billion a month of spend by press estimates.",
              s=["fin"], lc="move", st="new", ay="Apr 2025", o="P", at="Visa, Lead Bank", neo=[0, "Visa."],
              mc="The clearest place Visa is ahead at Stripe: the stablecoin card programme runs on Visa, with an on-chain settlement pilot. Mastercard's own answer, the BVNK Global Money Platform (October 2026), competes for the same programme managers.",
              src=[["Visa and Bridge: stablecoin-linked cards, Apr 2025", "https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.21371.html"], ["Crowdfund Insider: 27 EU countries, Oct 2026", "https://www.crowdfundinsider.com/?p=316824"]]),
        ]},
        {"id": "2.5", "ic": "coins", "name": "Stablecoins", "blurb": "Bridge, Privy, Tempo, OUSD.", "div": "bridge", "rev": "crypto", "products": [
            P("bridge", "Bridge", "Stablecoin orchestration and issuance (bought for about $1.1 billion, February 2025): volume more than quadrupled in 2025; Open Issuance (October 2025) lets any business launch its own stablecoin, with reserves at BlackRock and Fidelity.",
              s=["fin", "ent"], lc="move", o="A", ay="Feb 2025", neo=[0, ""],
              src=[["Stripe: completes Bridge acquisition, Feb 2025", "https://stripe.com/us/newsroom/news/stripe-completes-bridge-acquisition"], ["Stripe: Open Issuance from Bridge, 2025", "https://stripe.com/ae/blog/introducing-open-issuance-from-bridge"]]),
            P("ousd", "OUSD & Open Standard", "Open USD, issued by Bridge and governed by Open Standard, which Coinbase, Mastercard, Shopify, Stripe and Visa founded; live on 30 September 2026 and now Stripe's default stablecoin across Treasury, Issuing, payouts and payments.", short="OUSD",
              s=["fin", "ent", "plat"], lc="move", st="new", ay="Sep 2026", o="P", at="Coinbase, Mastercard, Shopify, Visa", neo=[1, "Mastercard a co-founder of Open Standard."],
              mc="Mastercard sits at the table for the stablecoin Stripe is making its default; card-to-OUSD settlement is the bridge to build.",
              src=[["Stripe: OUSD is now available on Stripe", OUSD], ["Bridge: OUSD is live, Sep 2026", "https://bridge.xyz/blog/ousd-is-live-issued-by-bridge"]]),
            P("tempo", "Tempo", "A payments blockchain incubated with Paradigm and run as its own company ($500 million at $5 billion, October 2025): testnet December 2025 with Mastercard, Visa, OpenAI and Shopify among design partners (Visa is also an anchor validator); mainnet 18 March 2026 with the Machine Payments Protocol.",
              s=["ai", "fin"], lc="move", st="new", ay="Mar 2026", o="P", at="Paradigm", div="tempo", neo=[1, "Mastercard a testnet design partner."],
              src=[["Decrypt: Tempo testnet with Mastercard and UBS, Dec 2025", TEMPO_TESTNET], ["The Block: Tempo mainnet, Mar 2026", "https://www.theblock.co/post/394131/tempo-mainnet-goes-live-with-machine-payments-protocol-for-agents"]]),
            P("privy", "Privy wallets", "Programmable wallets (bought June 2025): more than 110 million by February 2026, digital-asset accounts used by Ramp, Deel and DoorDash, and agent wallets; its CEO now leads Stripe's crypto work.",
              s=["fin", "con"], lc="move", o="A", ay="Jun 2025", div="privy", neo=[0, ""],
              src=[["Stripe: Sessions 2026", S26]]),
            P("stableaccept", "Stablecoin payments & accounts", "Accept USDC and other stablecoins (US merchants, customers in 150-plus countries), stablecoin subscriptions (October 2025), and Stablecoin Financial Accounts for businesses in 101 countries (May 2025).", short="Stablecoin payments",
              s=["ai", "saas", "fin"], lc="move", st="new", neo=[0, ""],
              src=[["Stripe docs: stablecoins", "https://docs.stripe.com/crypto/stablecoins"], ["Stripe: Sessions 2025", S25]]),
        ]},
        {"id": "2.6", "ic": "wallet", "name": "Treasury & FX", "blurb": "A business account in 15 currencies.", "div": "stripe", "rev": "money", "products": [
            P("treasury", "Treasury business accounts", "Relaunched at Sessions 2026 as a global business account: balances in 15 currencies, free instant US Stripe-to-Stripe transfers (4.8 million B2B payments a day on Stripe), a US Stripe Mastercard with 2% cash back, and control from ChatGPT; the US and UK now, the euro area and Australia later in 2026. Shopify Balance runs on it.",
              s=["start", "saas", "plat"], lc="everyday", st="new", ay="Apr 2026", neo=[2, "The Stripe business card is a Mastercard; cash back only on Mastercard."],
              mc="The one place Stripe steers to Mastercard: the 2% cash back applies only to Mastercard cards, and Visa holders can ask to switch.",
              src=[["Stripe: Sessions 2026", S26], ["Stripe docs: Treasury cash back", "https://docs.stripe.com/treasury/cashback"], ["Stripe: Treasury for platforms", "https://stripe.com/us/treasury/platforms"]]),
            P("fx", "Multicurrency settlement & FX", "Settlement in up to 18 currencies across 37 markets by the end of 2026 and round-the-clock conversion across 15 (August 2026).",
              s=["ent", "plat"], lc="move", st="new", neo=[0, ""],
              src=[["Stripe: reduce FX costs, Aug 2026", BLOG + "reduce-fx-costs-with-stripe"]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every payment: stop the fraud and win the dispute, prove who someone is, push the authorisation through, remember the shopper in Link, make the data queryable, and let AI agents buy safely.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & disputes", "blurb": "Radar, now for other processors too.", "div": "stripe", "rev": "pay", "products": [
            P("radar", "Radar", "Machine-learning fraud screening on the payments foundation model; since 2026 a risk layer for payments on other processors too, with bot and free-trial abuse protection for AI companies and screening on Affirm, Cash App, Klarna and PayPal.",
              s=["ent", "ai", "start"], lc="move", neo=[1, "Uses network signals; no named Mastercard product."],
              mc="Decision Intelligence and Ethoca's early-fraud and dispute data are the network signals a multi-processor Radar would want.",
              src=[["Stripe: expanding Radar, May 2026", BLOG + "expanding-stripe-radar-to-protect-more-of-your-business"]]),
            P("disputes", "Smart Disputes & dispute prevention", "AI-assembled dispute evidence (2025), which Stripe says wins 13% more disputes, and prevention through Mastercard's Ethoca Alerts and Visa's Verifi, wired in through Radar rules.", short="Smart Disputes",
              s=["ent", "start"], lc="move", st="new", neo=[1, "Ethoca Alerts beside Visa's Verifi."],
              mc="Ethoca Alerts are already in; Consumer Clarity and merchant-descriptor enrichment for Stripe's long tail of small and AI-native merchants are not.",
              src=[["Stripe: Sessions 2025", S25], ["Stripe docs: dispute prevention", "https://docs.stripe.com/disputes/get-started/prevention"]]),
        ]},
        {"id": "3.2", "ic": "fingerprint", "name": "Identity & bank data", "blurb": "Who they are, what they hold.", "div": "stripe", "rev": "pay", "products": [
            P("identity", "Stripe Identity", "Document and selfie verification for onboarding, with 3D face checks and 41 more countries on the roadmap.",
              s=["fin", "plat"], lc="open", neo=[0, ""], src=[["Stripe: everything announced at Sessions 2026", S26ALL]]),
            P("finconnect", "Financial Connections", "Customers link bank accounts for payments, verification and data (May 2022), through aggregators including MX and Mastercard's Finicity; it also powers bank payments in Link.",
              s=["fin", "saas", "con"], lc="open", ay="May 2022", o="P", at="Finicity, MX", neo=[1, "Finicity one of the aggregators."],
              mc="A low-profile Mastercard dependency already in place; US pay by bank would build on it, though it would compete with Link's own bank payments.",
              src=[["TechCrunch: Stripe launches Financial Connections, May 2022", "https://techcrunch.com/2022/05/04/stripe-launches-financial-connections-for-customers-to-pull-banking-data-used-to-power-transactions-automatically"], ["Link: connecting your bank account", "https://support.link.com/questions/connecting-your-bank-account"]]),
        ]},
        {"id": "3.3", "ic": "gauge", "name": "Authorisation & tokens", "blurb": "+3.8% acceptance.", "div": "stripe", "rev": "pay", "products": [
            P("authboost", "Authorization Boost", "Adaptive Acceptance (machine-learning retries), network tokens from Visa, Mastercard, Amex and Discover, and a cross-brand card account updater: an average 3.8% lift in acceptance. Stripe was a readiness partner for Visa's authentication programme (April 2026); network tokens and a real-time account updater for Mastercard went global in February 2023.",
              s=["ent", "saas"], lc="move", neo=[1, "Mastercard tokens (MDES) among all networks'."],
              mc="Mastercard network tokens, Identity Check and Click to Pay are the levers; Visa is currently the network Stripe publicly credits for cost savings.",
              src=[["Stripe: Authorization Boost", "https://stripe.com/au/authorization-boost/"], ["Stripe: network tokens and card account updater, Feb 2023", "https://stripe.com/de-us/newsroom/news/network-tokens-card-account-updater"], ["Stripe: Visa's digital commerce authentication programme, Jun 2026", BLOG + "helping-businesses-optimize-network-costs-with-visa-digital-commerce-authentication-program"]]),
            P("orchestration", "Orchestration", "Manage several processors and their routing from the Stripe Dashboard (announced May 2025), with standalone 3-D Secure for other processors in 2026; general availability not confirmed.",
              s=["ent"], lc="move", st="unconf", ay="May 2025", neo=[0, ""],
              src=[["Stripe: Sessions 2025", S25]]),
        ]},
        {"id": "3.4", "ic": "wallet-cards", "name": "Link", "blurb": "300 million shoppers.", "div": "stripe", "rev": "pay", "products": [
            P("link", "Link", "Stripe's own saved-payment network: more than 300 million users and a million merchants (September 2026), with Pix and stablecoins added and a native app in 2026.",
              s=["con", "retail"], lc="move", neo=[1, "Stores Mastercards among others; a rival to Click to Pay."],
              mc="Link is Stripe's own answer to Click to Pay, whose onboarding Stripe's docs describe as paused: one-click checkout without the network.",
              src=[["Stripe: Meta Muse shops with Link, Sep 2026", NEWS + "stripe-helps-meta-muse-shop-with-link"]]),
            P("linkagent", "Link agent wallet", "A wallet for AI agents (April 2026) that issues a one-time card for each task with the user's approval; Meta's Muse uses it (September 2026).",
              s=["con", "ai"], lc="move", st="new", ay="Apr 2026", neo=[1, "One-time cards; network not stated."],
              src=[["Stripe: Meta Muse shops with Link, Sep 2026", NEWS + "stripe-helps-meta-muse-shop-with-link"], ["Stripe: helping personal agents shop, Sep 2026", BLOG + "helping-personal-agents-shop-more-intelligently-and-reliably-with-link"]]),
        ]},
        {"id": "3.5", "ic": "database", "name": "Data", "blurb": "Sigma to Postgres.", "div": "stripe", "rev": "rev", "products": [
            P("data", "Sigma, Data Pipeline & Stripe Database", "SQL over Stripe data, syncs to Snowflake, Redshift and Databricks, real-time Postgres sync (October 2026) and a managed Stripe Database in preview.",
              s=["ent", "saas"], lc="everyday", neo=[0, ""],
              src=[["Stripe: real-time Stripe data in Postgres, Oct 2026", BLOG + "real-time-stripe-data-postgres"]]),
        ]},
        {"id": "3.6", "ic": "bot", "name": "Agentic commerce", "blurb": "ChatGPT, Gemini, Copilot, Meta.", "div": "stripe", "rev": "ai", "products": [
            P("acp", "Agentic Commerce Protocol", "An open standard co-developed with OpenAI, launched with Instant Checkout in ChatGPT on 29 September 2025 (Etsy first, then Shopify merchants); Salesforce's Agentforce followed.",
              s=["ai", "retail", "ent"], lc="move", st="new", ay="Sep 2025", o="P", at="OpenAI", neo=[0, "Stripe's protocol; cards underneath."],
              mc="ACP competes with the networks' own agent protocols; what Mastercard needs is for Agent Pay tokens to travel inside it.",
              src=[["Stripe and OpenAI: Instant Checkout, Sep 2025", NEWS + "stripe-openai-instant-checkout"]]),
            P("spt", "Shared Payment Tokens", "Tokens scoped to one merchant and one amount so an agent never sees the card; since 3 March 2026 they carry Mastercard Agent Pay and Visa Intelligent Commerce agentic tokens, plus Affirm and Klarna, and Stripe says it is the only provider supporting both networks'. Marc Lore's Wizard uses Agent Pay through them (April 2026), and Stripe is among the partners for Mastercard's Agent Pay for Machines (June 2026).",
              s=["ai", "ent"], lc="move", st="new", ay="Mar 2026", o="P", at="Mastercard, Visa", neo=[2, "Carries Mastercard Agent Pay tokens."],
              src=[["Stripe: more payment methods for agentic commerce, Mar 2026", SPT], ["PYMNTS: Mastercard and Stripe help Wizard, Apr 2026", "https://www.pymnts.com/partnerships/2026/mastercard-and-stripe-help-wizard-personalize-agentic-shopping/"], ["Mastercard: Agent Pay for Machines, Jun 2026", "https://investor.mastercard.com/investor-news/investor-news-details/2026/Mastercard-Launches-Agent-Pay-for-Machines-to-Unlock-Super-Fast-Always-On-Payments/default.aspx"]]),
            P("acsuite", "Agentic Commerce Suite", "One integration to sell through AI agents (December 2025): Coach, Kate Spade, URBN and Ashley among brands; Microsoft Copilot Checkout (January 2026), Google AI Mode and Gemini, and checkout inside Meta ads (April 2026).",
              s=["retail", "ent"], lc="move", st="new", ay="Dec 2025", neo=[1, "Card tokens, Agent Pay among them."],
              src=[["Stripe: Agentic Commerce Suite", "https://stripe.com/us/newsroom/news/agentic-commerce-suite"], ["Stripe: Microsoft Copilot and Stripe", "https://stripe.com/us/newsroom/news/microsoft-copilot-and-stripe"]]),
            P("mpp", "Machine payments", "The Machine Payments Protocol, co-written with Tempo (March 2026), for stablecoin micropayments per API or tool call, and streaming payments that pair Metronome metering with Tempo for per-token billing.",
              s=["ai"], lc="move", st="new", ay="Mar 2026", neo=[0, "Stablecoin rails."],
              mc="If machines pay each other in stablecoins, cards are bypassed. Visa shipped a card spec for MPP on launch day; Mastercard's compatibility work through Tempo is still in progress.",
              src=[["The Block: Tempo mainnet and MPP, Mar 2026", "https://www.theblock.co/post/394131/tempo-mainnet-goes-live-with-machine-payments-protocol-for-agents"]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What businesses buy from Stripe: payments and checkout, Connect for platforms, the revenue and finance suite (on track for a $1 billion run rate), Capital, everything to start a company, and the AI infrastructure built around OpenRouter.",
    "tiles": [
        {"id": "4.1", "ic": "credit-card", "name": "Payments & checkout", "blurb": "Optimised checkout.", "div": "stripe", "rev": "pay", "products": [
            P("checkout", "Checkout & Payment Element", "Hosted and embedded checkout with Link and AI ordering of payment methods (the Optimized Checkout Suite), Adaptive Pricing in local currency (+17.8% cross-border revenue) and Checkout studio for A/B tests (2026).",
              s=["ent", "start", "retail"], lc="move", neo=[1, "Cards among methods."],
              src=[["Stripe: new ways to turn global demand into revenue, Jun 2026", BLOG + "new-ways-to-turn-global-demand-into-revenue"]]),
        ]},
        {"id": "4.2", "ic": "network", "name": "Connect & platforms", "blurb": "18,000 platforms.", "div": "stripe", "rev": "plat", "products": [
            P("connect", "Connect", "Payments for platforms and marketplaces: more than 18,000 platforms helping about 11 million businesses get paid, with network-cost pass-through, seller wallets and prepaid cards in preview, and multi-processor payouts for EU marketplaces in 2026.",
              s=["plat", "saas"], lc="move", neo=[1, "Cards, and prepaid cards in preview."],
              src=[["Stripe: Sessions 2026", S26], ["Stripe: agrees to acquire Parafin, Sep 2026", NEWS + "stripe-agrees-to-acquire-parafin"]]),
        ]},
        {"id": "4.3", "ic": "refresh-cw", "name": "Revenue & finance automation", "blurb": "Heading for $1 billion.", "div": "stripe", "rev": "rev", "products": [
            P("billing", "Billing & Metronome", "Subscriptions and usage-based billing, with Metronome (closed January 2026) metering for OpenAI, Anthropic and Nvidia; streaming per-token billing from April 2026. The revenue suite is on track for a $1 billion run rate in 2026.",
              s=["saas", "ai"], lc="grow", o="A", ay="Jan 2026", neo=[0, "Uses card updaters underneath."],
              mc="Recurring billing lives or dies on card-on-file: the Automatic Billing Updater and Smart Subscriptions sit directly under it.",
              src=[["Stripe: completes Metronome acquisition, Jan 2026", NEWS + "stripe-completes-metronome-acquisition"], ["Stripe: 2025 annual letter, Feb 2026", LETTER25]]),
            P("tax", "Tax, Invoicing & Revenue Recognition", "Tax calculation in more than 100 countries and US filing through TaxJar, hosted invoicing (Anthropic is a customer) and automated revenue recognition.", short="Tax & Invoicing",
              s=["saas", "ent"], lc="everyday", neo=[0, ""],
              src=[["Stripe: Sessions 2025", S25], ["Stripe: Anthropic", "https://stripe.com/en-at/customers/anthropic"]]),
            P("managed", "Managed Payments", "Stripe as merchant of record for digital businesses, handling indirect tax in more than 80 countries, open to all from April 2026; it grew out of Lemon Squeezy.",
              s=["start", "saas", "ai"], lc="move", st="new", ay="Apr 2026", neo=[0, ""],
              src=[["Stripe: Sessions 2026", S26]]),
        ]},
        {"id": "4.4", "ic": "hand-coins", "name": "Capital", "blurb": "Lending on Stripe data.", "div": "stripe", "rev": "money", "products": [
            P("capital", "Stripe Capital", "Loans and merchant cash advances underwritten on Stripe data (since 2019; issued by Celtic Bank in the US and YouLend elsewhere), offered through platforms in more markets in 2026; FedEx shipping data will inform underwriting from 2027.",
              s=["start", "plat", "retail"], lc="borrow", o="P", at="Celtic Bank, YouLend", neo=[0, ""],
              src=[["Stripe: FedEx and Stripe, Oct 2026", NEWS + "fedex-and-stripe"]]),
            P("parafin", "Parafin", "Embedded small-business credit for DoorDash, Gusto, Jobber and Mindbody, with more than 60,000 businesses funded; agreed 30 September 2026, awaiting clearance.",
              s=["plat"], lc="borrow", st="new", ay="Sep 2026", o="A", neo=[0, ""],
              src=[["Stripe: agrees to acquire Parafin, Sep 2026", NEWS + "stripe-agrees-to-acquire-parafin"]]),
        ]},
        {"id": "4.5", "ic": "rocket", "name": "Starting a company", "blurb": "A quarter of Delaware's.", "div": "stripe", "rev": "rev", "products": [
            P("atlas", "Atlas & Clerky", "Atlas forms about a quarter of new Delaware corporations and now takes SAFE funding into Treasury; Clerky (startup legal, September 2026) extends it to fundraising paperwork.",
              s=["start"], lc="open", neo=[0, ""],
              src=[["Stripe: 2025 annual letter, Feb 2026", LETTER25], ["Crowdfund Insider: Stripe acquires Clerky, Sep 2026", "https://www.crowdfundinsider.com/2026/09/304464-fintech-stripe-acquires-online-legal-platform-clerky/"]]),
        ]},
        {"id": "4.6", "ic": "brain", "name": "AI infrastructure", "blurb": "Tokens as a currency.", "div": "openrouter", "rev": "ai", "products": [
            P("openrouter", "OpenRouter", "One API to more than 400 AI models, agreed in August 2026 (reported at $7–8 billion) and to run independently; Stripe calls tokens 'the central currency' of the AI economy.",
              s=["ai", "start"], lc="beyond", st="new", ay="Aug 2026", o="A", neo=[0, ""],
              src=[["Stripe: agrees to acquire OpenRouter, Aug 2026", NEWS + "stripe-agrees-to-acquire-openrouter"]]),
            P("projects", "Stripe Projects", "Provision and pay for a whole development stack (Vercel, Supabase, Cloudflare, Twilio, ElevenLabs and 30-odd others) from one place, generally available April 2026.",
              s=["start", "ai"], lc="open", st="new", ay="Apr 2026", neo=[0, ""],
              src=[["Stripe: Projects adds agents and providers, Jun 2026", BLOG + "stripe-projects-adds-new-agents-providers-developer-controls"]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How businesses reach Stripe: the Dashboard and its agentic Console, the API and an MCP server for agents, the platforms and AI companies that put Stripe inside their own products, Stripe Apps, and Sessions, Press and Climate.",
    "tiles": [
        {"id": "5.1", "ic": "monitor", "name": "Dashboard & Console", "blurb": "An agent in the Dashboard.", "div": "stripe", "rev": "grp", "products": [
            P("dashboard", "Dashboard & Stripe Console", "The Stripe Dashboard and mobile app, with Stripe Console, an agentic assistant, in preview from April 2026.",
              s=["start", "ent", "saas"], lc="everyday", neo=[0, ""], src=[["Stripe: everything announced at Sessions 2026", S26ALL]]),
        ]},
        {"id": "5.2", "ic": "code-xml", "name": "API & MCP", "blurb": "For developers, and their agents.", "div": "stripe", "rev": "grp", "products": [
            P("api", "API & SDKs", "Versioned APIs and SDKs, with Workbench for monitoring and custom objects in preview.",
              s=["start", "ent", "plat"], lc="open", neo=[0, ""], src=[["Stripe docs: changelog", "https://docs.stripe.com/changelog"]]),
            P("mcp", "Stripe MCP server & agent toolkit", "A remote MCP server and toolkit for OpenAI, LangChain, CrewAI and Vercel agents, with Treasury money movement and guardrails (identities, scopes, approvals) added in 2026.",
              s=["ai", "start"], lc="open", st="new", neo=[0, ""], src=[["Stripe docs: MCP", "https://docs.stripe.com/mcp"]]),
        ]},
        {"id": "5.3", "ic": "plug", "name": "Partners & platforms", "blurb": "Inside Shopify, ChatGPT, Gemini.", "div": "stripe", "rev": "grp", "products": [
            P("partners", "Partner channels", "Stripe reaches businesses through other people's products: Shopify Payments and Shopify Balance, Salesforce Agentforce, ChatGPT, Gemini, Microsoft Copilot and Meta ads checkout, and FedEx (October 2026). Among AI companies it runs payments for OpenAI, Anthropic, Cursor and Lovable, though OpenAI has added Adyen.",
              s=["plat", "ai", "ent"], lc="open", o="P", at="Shopify, Salesforce, OpenAI, Google, Microsoft, Meta", neo=[0, ""],
              src=[["Stripe: Sessions 2026", S26], ["Stripe: FedEx and Stripe, Oct 2026", NEWS + "fedex-and-stripe"]]),
        ]},
        {"id": "5.4", "ic": "sparkles", "name": "Stripe Apps", "blurb": "Extensions in the Dashboard.", "div": "stripe", "rev": "grp", "products": [
            P("apps", "Stripe Apps & Workflows", "Third-party apps inside the Dashboard (since May 2022) and Stripe Workflows for no-code automation, generally available in 2026.",
              s=["saas", "ent"], lc="everyday", neo=[0, ""], src=[["Stripe: Stripe Apps more than doubles", BLOG + "stripe-apps-more-than-doubles-in-size-offers-new-ways-to-discover-apps"]]),
        ]},
        {"id": "5.5", "ic": "presentation", "name": "Sessions, Press & Climate", "blurb": "288 launches in one week.", "div": "stripe", "rev": "grp", "products": [
            P("sessions", "Sessions", "Stripe's annual conference in San Francisco: 288 launches and more than 9,000 attendees in April 2026, with a public roadmap of about 330 items.",
              s=["ent", "start"], lc="beyond", neo=[0, ""], src=[["Stripe: Sessions 2026", S26]]),
            P("climate", "Stripe Climate & Frontier", "Carbon removal: Frontier, the advance market commitment Stripe founded in 2022 with Alphabet, Shopify, Meta and McKinsey, has grown to about $1.8 billion of commitments.",
              s=["ent", "start"], lc="beyond", neo=[0, ""],
              mc="Merchants who fund carbon removal at checkout are natural users of a carbon calculator for their customers' purchases.",
              src=[["Wikipedia: Frontier Climate", "https://en.wikipedia.org/wiki/Frontier_Climate"]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Stripe", "blurb": "Network, partner, rival.", "products": [
        P("mcatstripe", "Mastercard at Stripe", "Mastercard is a network Stripe acquires and issues on, the rail under Instant Payouts (Send) and the agentic tokens Stripe carries (Agent Pay), a co-founder of Open Standard and a Tempo design partner. Stripe's own Link, ACP, Bridge cards on Visa and stablecoin machine payments compete with parts of it.",
          s=["fin"], div="stripe", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Stripe: more payment methods for agentic commerce, Mar 2026", SPT], ["Stripe: OUSD is now available on Stripe", OUSD], ["Decrypt: Tempo testnet, Dec 2025", TEMPO_TESTNET]]),
    ]},
    {"id": "pillar-market", "name": "The payments field", "blurb": "Adyen, PayPal, Fiserv, the networks.", "products": [
        P("field", "Stripe's competitors", "Adyen, PayPal and Braintree (which Stripe bid for in July 2026), Fiserv and Clover, Checkout.com and Block, and in agentic commerce Google's and the networks' own protocols beside Stripe's ACP. The FTC sent Stripe, PayPal, Visa and Mastercard warning letters on 'debanking' in March 2026.",
          s=["ent"], div="stripe", rev="grp",
          src=[["Axios: Stripe and Advent bid for PayPal, Jul 2026", "https://www.axios.com/2026/07/15/paypal-bid-stripe-advent"], ["FTC: letter to Stripe, Mar 2026", "https://www.ftc.gov/system/files/ftc_gov/pdf/stripe-debanking-letter.pdf"]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
