"""API of the Day — curated insights surfaced on the Studio home page.

Each entry pairs an API id with:

    * ``insight`` — one to two sentences that explain *why* the API matters
                    to a senior business audience (the strategic angle).
    * ``example`` — a concrete, specific data point or scenario that brings
                    the insight to life (the "show me" angle).

Keep both fields short — the spotlight card is glanceable, not exhaustive.
The full how-to / docs / operation list already live on the API detail panel
inside the Studio.

A deterministic per-day picker (``pick_today``) ensures every viewer sees
the same API on any given calendar day — so a partner who lands on the home
page in the morning sees the same spotlight as a colleague who lands on it
in the afternoon, which makes the feature reliable for demo conversations
("hey, did you see today's API?").

Adding a new API: just add a key to ``SPOTLIGHTS`` keyed by the catalog id.
Missing entries fall back to a generic blurb so the UI never breaks; logged
gaps prompt the next content pass.
"""
from __future__ import annotations

import datetime
import hashlib
from collections.abc import Iterable

SPOTLIGHTS: dict[str, dict[str, str]] = {
    "open_finance": {
        "insight": (
            "The on-ramp to consumer financial data. Open Finance US "
            "aggregates accounts, transactions and balances from 95%+ of "
            "US deposit institutions through one consent flow — the same "
            "Finicity stack that powers Rocket Mortgage's income "
            "verification."
        ),
        "example": (
            "One call to Cash Flow Verification returns 24 months of "
            "categorised inflows and outflows for a borrower — replacing "
            "weeks of manual pay-stub and bank-statement review with a "
            "real-time JSON payload."
        ),
    },
    "open_finance_au": {
        "insight": (
            "The Australian Consumer Data Right (CDR), wrapped. Same "
            "Finicity engine as US Open Finance, plus full CDR consent "
            "lifecycle, dashboard and audit trail handled for you."
        ),
        "example": (
            "Issue a 90-day CDR consent, fetch a consumer's transaction "
            "history across multiple banks, and present the same revoke-"
            "anytime dashboard the OAIC requires — without building a "
            "single consent screen yourself."
        ),
    },
    "open_finance_eu": {
        "insight": (
            "PSD2 Account Information across Europe through one API. "
            "Aiia-backed coverage of 3,000+ EU banks, with SCA, consent "
            "lifecycle and provider routing abstracted away."
        ),
        "example": (
            "A Berlin consumer connects their Deutsche Bank account in 8 "
            "seconds; you receive 12 months of transactions in a "
            "harmonised schema — same shape whether the bank is in "
            "Germany, France or Finland."
        ),
    },
    "bin_lookup": {
        "insight": (
            "The lookup that decides whether a payment journey even starts. "
            "Resolve any BIN to issuer country, brand, product tier, "
            "funding type and rewards programme in <100 ms — the building "
            "block of card-detect UX, dynamic routing and acceptance "
            "decisions."
        ),
        "example": (
            "BIN ``542418`` resolves instantly to a Mastercard World "
            "Elite credit card issued by Lloyds in the UK — enough "
            "context to surface the right currency, the right reward "
            "messaging and the right 3DS challenge mode at checkout."
        ),
    },
    "merchant_identifier": {
        "insight": (
            "Turn a fuzzy descriptor like ``SQ *COFFEE 4434 NYC`` into a "
            "clean merchant identity — name, address, MCC, parent brand "
            "and logo — using the network's own merchant graph."
        ),
        "example": (
            "Search ``WHOLEFDS`` across NY ZIP 10001 and get back the "
            "exact Whole Foods Market store, with its parent (Amazon), "
            "MCC (5411), and logo URL — ready to drop into a statement, "
            "PFM feed or fraud-review screen."
        ),
    },
    "automatic_billing_updater": {
        "insight": (
            "The reason your subscription survives a card reissue. ABU "
            "lets merchants and PSPs query the network for the latest "
            "card number, expiry and account status when a card-on-file "
            "stops working — before a recurring payment ever declines."
        ),
        "example": (
            "Netflix queries ABU nightly for its 270 million tokens; "
            "≈1.5% return an updated PAN/expiry, preventing the "
            "involuntary churn that kills $2 billion of subscription "
            "revenue industry-wide every year."
        ),
    },
    "match": {
        "insight": (
            "The shared database every acquirer checks before boarding a "
            "merchant. MATCH (Member Alert To Control High-risk Merchants) "
            "lets you screen new merchant applicants against terminations "
            "reported by every other Mastercard acquirer worldwide."
        ),
        "example": (
            "An acquirer running a 30-second MATCH inquiry on a new "
            "merchant applicant flags an owner previously terminated for "
            "excessive chargebacks under a different DBA — stopping a "
            "high-risk boarding decision before it costs five-figure "
            "fees."
        ),
    },
    "consumer_clarity": {
        "insight": (
            "Cryptic statement descriptors are the #1 driver of avoidable "
            "chargebacks ('I don't recognise this charge'). Consumer "
            "Clarity returns clean merchant names, logos, locations and "
            "categories — solving the problem at the descriptor level."
        ),
        "example": (
            "``AMZN MKTP US*RT4Y2L8K3`` becomes ``Amazon Marketplace`` "
            "with the Amazon logo, a 'Online Shopping' category and a "
            "Seattle HQ address — banks using Consumer Clarity report "
            "20–30% fewer 'unrecognised transaction' calls."
        ),
    },
    "priceless_cities": {
        "insight": (
            "Mastercard's curated experience platform — concerts, "
            "Michelin-starred dinners, F1 hot laps — available as an API "
            "so issuers can embed the Priceless catalogue directly into "
            "their own card-holder apps."
        ),
        "example": (
            "Surface a 'Priceless Tonight in London' rail inside your "
            "banking app: real Priceless inventory, real ticketing, "
            "redeemable with the card-holder's existing benefits — no "
            "separate Priceless.com sign-in required."
        ),
    },
    "easy_savings": {
        "insight": (
            "An always-on, card-linked rebate programme available to any "
            "Mastercard small-business card holder — zero enrolment, "
            "rebates posted automatically. The simplest way for an issuer "
            "to add tangible card benefits without building an offers "
            "engine."
        ),
        "example": (
            "A small-business card holder fuels at a Shell station, gets "
            "an automatic 3% rebate posted to their statement within "
            "days — no coupon, no app, no opt-in. The issuer adds value "
            "with zero merchant negotiation effort."
        ),
    },
    "places": {
        "insight": (
            "The geo-layer of the Mastercard network. Search 100M+ "
            "merchant locations worldwide by name, category or radius — "
            "and tie each result back to acceptance data, footfall "
            "patterns and transaction insights."
        ),
        "example": (
            "Query 'coffee shops within 500m of latitude 51.5074, "
            "longitude -0.1278' and get a ranked list of London "
            "café-acceptance locations with addresses, MCCs and "
            "Mastercard-acceptance confirmation — ready to plot on a "
            "map."
        ),
    },
    "offers_for_publishers": {
        "insight": (
            "Card-linked offers exposed for publisher channels — news "
            "sites, browser extensions, loyalty apps. Show consumers "
            "relevant cashback offers in editorial context, and earn an "
            "affiliate-style margin on every linked spend."
        ),
        "example": (
            "A money-saving publisher renders a personalised 'Top 5 "
            "cashback offers for your card' widget; a reader links their "
            "card, spends £80 at one of the merchants, the publisher "
            "earns a programmatic share of the activated offer value."
        ),
    },
    "offers_merchant_content": {
        "insight": (
            "The merchant-side data behind every card-linked offer — "
            "names, logos, taglines, T&Cs, fulfilment terms — served as "
            "structured JSON so any front-end can render a polished "
            "offers experience without curating creative."
        ),
        "example": (
            "A bank app pulls 50 active offers, each with a 200x200 "
            "logo, a 'Get 5% back at checkout' tagline and the legal "
            "expiry date — ready to drop into a card-art carousel "
            "without a single design ticket."
        ),
    },
    "consent_management": {
        "insight": (
            "The audit-grade consent ledger required by PSD2, CDR, GLBA "
            "and every Open Banking regulator that exists. Capture, "
            "version, revoke and replay consumer consents with the "
            "cryptographic receipts regulators expect."
        ),
        "example": (
            "A consumer grants 90-day account-data access; the consent "
            "is signed, time-stamped, stored, and surfaced in a "
            "revoke-anytime dashboard — when the regulator audits the "
            "flow two years later, every grant is reproducible to the "
            "second."
        ),
    },
    "transaction_notifications": {
        "insight": (
            "Real-time, network-side transaction signals — the same feed "
            "issuers use to power push notifications, fraud step-up and "
            "spend-control rules. Fires the moment a swipe / tap / "
            "online transaction is authorised."
        ),
        "example": (
            "A consumer taps to pay at a Tokyo café; within 200 ms the "
            "issuer's app shows 'JPY 1,200 at Blue Bottle Coffee' with "
            "merchant logo and FX-converted home-currency amount — "
            "before the receipt prints."
        ),
    },
    "benefits_eligibility": {
        "insight": (
            "Card programme benefits — travel insurance, purchase "
            "protection, concierge — are useless if a card-holder can't "
            "find out whether *they* qualify. Benefits Eligibility "
            "answers that in one API call, per card, per benefit."
        ),
        "example": (
            "A card-holder taps 'Am I covered for this trip?' in their "
            "bank app; one call returns a definitive yes / no for "
            "travel insurance on their specific card product — replacing "
            "a phone call to a benefits hotline."
        ),
    },
    "benefits_content_eligibility": {
        "insight": (
            "Pair benefits eligibility with a searchable, structured "
            "content catalogue — so card-holders can browse what's "
            "available *and* see what they qualify for, in the same "
            "experience."
        ),
        "example": (
            "An issuer renders 'Your card unlocks 14 benefits' with full "
            "imagery and copy pulled from Mastercard's content catalogue "
            "— no manual content syncing, no out-of-date entitlement "
            "lists."
        ),
    },
    "enhanced_currency_conversion_calculator": {
        "insight": (
            "EU Regulation 2019/518 requires cross-border payments to "
            "disclose the FX mark-up versus the ECB reference rate. "
            "ECCC returns both the Mastercard wholesale rate and the ECB "
            "benchmark — the disclosure regulators look for, in one call."
        ),
        "example": (
            "A €100 GBP purchase: the API returns Mastercard's rate "
            "(1.176), the ECB reference rate (1.175) and the percentage "
            "difference (0.09%) — exactly the comparison that has to "
            "appear on the consumer's notification."
        ),
    },
    "flight_delay_pass": {
        "insight": (
            "Turn a 2-hour flight delay into a positive brand moment. "
            "Eligible card-holders get automatic lounge access the "
            "moment their flight is delayed beyond the threshold — no "
            "claims form, no receipts."
        ),
        "example": (
            "A card-holder's BA flight is delayed 90 minutes; their "
            "issuer's app surfaces a one-tap lounge pass for Heathrow "
            "T5, drawn from the Flight Delay Pass registration tied to "
            "their card — friction-free, no human in the loop."
        ),
    },
    "carbon_calculator": {
        "insight": (
            "Doconomy's climate-impact engine, wrapped as a Mastercard "
            "API. Convert any transaction (merchant + amount) into a CO₂ "
            "estimate using peer-reviewed lifecycle data — the same "
            "engine behind Klarna's Conscious mode and Santander's "
            "footprint tracker."
        ),
        "example": (
            "A £62 transaction at a UK supermarket is scored at 14.3 kg "
            "CO₂e — surfaced in the consumer's banking app alongside the "
            "transaction, with category-level benchmarks for comparison."
        ),
    },
    "business_payment_controls": {
        "insight": (
            "Programmable spend rules at the network level. Issuers can "
            "let corporate card admins set per-card limits, MCC blocks, "
            "geographic restrictions and velocity caps — enforced "
            "before the authorisation completes, not after."
        ),
        "example": (
            "A fleet card programme blocks every MCC except fuel and "
            "vehicle services, caps daily spend at £150, restricts "
            "transactions to the UK — and the rule travels with the "
            "card across every terminal in the world."
        ),
    },
}


_DEFAULT_INSIGHT = (
    "A Mastercard Developer API integrated end-to-end inside Solution "
    "Studio — open the API panel to inspect every operation, send live "
    "requests and see how it composes with the rest of the catalogue."
)


def for_api(api_id: str) -> dict[str, str]:
    """Return the spotlight content for ``api_id`` (with a safe fallback)."""
    entry = SPOTLIGHTS.get(api_id)
    if entry:
        return {"insight": entry["insight"], "example": entry.get("example", "")}
    return {"insight": _DEFAULT_INSIGHT, "example": ""}


def pick_today(
    api_ids: Iterable[str],
    *,
    today: datetime.date | None = None,
) -> str | None:
    """Pick the API id to spotlight on ``today`` (UTC by default).

    Deterministic per calendar day: hashes the ISO date string against the
    available id list so every viewer on the same day sees the same API.
    Returns ``None`` if the input list is empty.

    Eligible ids are the ones in ``api_ids`` *and* present in
    ``SPOTLIGHTS`` — APIs without curated content are skipped so the home
    page never shows a generic placeholder when a real insight exists.
    """
    ids = [a for a in api_ids if a in SPOTLIGHTS]
    if not ids:
        # Fall back to the raw input so we always render *something*.
        ids = list(api_ids)
    if not ids:
        return None
    day = today or datetime.datetime.now(datetime.timezone.utc).date()
    digest = hashlib.sha256(day.isoformat().encode("utf-8")).digest()
    idx = int.from_bytes(digest[:4], "big") % len(ids)
    return ids[idx]


__all__ = ["SPOTLIGHTS", "for_api", "pick_today"]
