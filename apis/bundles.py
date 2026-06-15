"""Solution-shaped bundles of complementary Mastercard APIs.

The :mod:`apis.catalog` groups APIs by *Mastercard Developers portal
category* (Open Finance, Security & Risk, Data, Loyalty). That mirrors how
a developer browses developer.mastercard.com, but it hides the fact that
real implementations almost always combine APIs from multiple groups.

This module is the **single source of truth** for those solution-shaped
bundles. Each bundle is a small dataclass with:

    * ``id``         — short, snake_case identifier (also the URL slug).
    * ``name``       — human-readable label.
    * ``tagline``    — one-line description rendered on the solution card.
    * ``anchor``     — the api id that defines the bundle (drives the
                       primary CTA / icon). May be ``None`` for bundles
                       without a clear single anchor.
    * ``apis``       — ordered tuple of api ids that compose the bundle.
                       Order is meaningful: anchor first, then the
                       complements ordered by how directly they pair.

The bundles are intentionally a *flat list*: an API can appear in several
bundles (e.g. BIN Lookup is in the issuer toolkit, the acquirer/risk
stack and gates Easy Savings inside the loyalty stack).

Adding a bundle is one ``Bundle(...)`` entry — no other code changes.
"""
from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(frozen=True)
class Bundle:
    id: str
    name: str
    tagline: str
    apis: tuple[str, ...]
    anchor: str | None = None
    # Longer-form explanation rendered on the bundle detail page below the
    # tagline. Should answer "why do these APIs belong together?" in 2-3
    # sentences.
    description: str = ""
    # Accent colour used by the bundle card (CSS hex). Drives the gradient
    # banner and the anchor pill.
    accent: str = "#ffcb05"
    # Inline SVG ``<path>`` data (24x24 viewbox) for the bundle icon. Kept as
    # path data so the SPA can recolour the stroke per-bundle.
    icon_path: str = "M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2z"
    # Headline benefits — short bullet phrases (≤7 words). Rendered as the
    # "What you can do" grid on the detail page.
    value_props: tuple[str, ...] = ()
    # Step-by-step technical journey across the APIs in this bundle. Each
    # entry is ``(api_id, action, detail)``. Rendered as the numbered
    # "How the APIs fit together" timeline.
    journey: tuple[tuple[str, str, str], ...] = ()
    # Walkthrough narratives — concrete end-to-end scenarios that show the
    # bundle in action. Each entry is ``(title, body)``. Rendered as the
    # "Walkthroughs" section.
    walkthroughs: tuple[tuple[str, str], ...] = ()
    # Quick example use cases — short bullet phrases. Rendered as the
    # "Example experiences" chip row.
    examples: tuple[str, ...] = ()


_BUNDLES: tuple[Bundle, ...] = (
    Bundle(
        id="pfm_stack",
        name="Account intelligence & PFM",
        tagline=(
            "Open Finance gives you raw transactions; the rest of this "
            "stack cleans, geo-tags and contextualises every line."
        ),
        description=(
            "Build a money-management experience that actually feels modern. "
            "Open Finance pulls account data; Consumer Clarity and Merchant "
            "Identifier turn cryptic descriptors into clean merchant names "
            "and brand logos; Places adds the physical context; Carbon "
            "Calculator turns each cleaned transaction into a CO₂ figure; "
            "Consent Management governs the underlying data-sharing grant."
        ),
        anchor="open_finance",
        accent="#0891b2",
        icon_path="M3 3h2v18H3zM7 13h2v8H7zM11 9h2v12h-2zM15 5h2v16h-2zM19 11h2v10h-2z",
        examples=(
            "Phone-style PFM dashboards with live balances and clean merchant names",
            "Spend-by-category breakdowns with brand logos and geo pins",
            "Carbon footprint estimates per transaction",
        ),
        apis=(
            "open_finance",
            "open_finance_au",
            "open_finance_eu",
            "consumer_clarity",
            "merchant_identifier",
            "places",
            "carbon_calculator",
            "consent_management",
        ),
    ),
    Bundle(
        id="subscriptions",
        name="Subscription & card-on-file lifecycle",
        tagline=(
            "Detect recurring charges in Open Finance, keep the card on "
            "file valid with ABU, notify the cardholder and govern the "
            "mandate with Consent Management."
        ),
        description=(
            "End-to-end subscription intelligence in one stack. Spot the "
            "recurring streams in a cardholder's bank data, keep the card "
            "details on file fresh as cards are reissued, alert the "
            "cardholder before each charge and capture the mandate via "
            "3-D Secure consent. The result: fewer involuntary churn "
            "events for merchants, fewer surprise charges and stronger "
            "PSD2 / SCA compliance posture for issuers."
        ),
        anchor="automatic_billing_updater",
        accent="#7c3aed",
        icon_path="M21 12a9 9 0 1 1-3-6.7M21 4v5h-5",
        value_props=(
            "Automatic detection of recurring streams",
            "Zero-touch card refresh on reissue",
            "Pre-charge cardholder notifications",
            "3DS-anchored subscription mandates",
            "Slashes involuntary churn",
            "SCA-compliant out of the box",
        ),
        journey=(
            ("open_finance", "Detect recurring patterns",
             "Recurring Transactions endpoint flags streaming, gym, SaaS and salary patterns with frequency and next-expected-date."),
            ("consent_management", "Capture the subscription mandate",
             "3DS authentication binds the cardholder consent to the recurring merchant + amount range."),
            ("automatic_billing_updater", "Keep card-on-file fresh",
             "Push or pull updates so when the issuer reissues plastic the merchant never sees a decline."),
            ("transaction_notifications", "Alert before each charge",
             "Pre-debit push to the cardholder's wallet with one-tap dispute / pause hooks."),
        ),
        walkthroughs=(
            (
                "Subscription manager inside a banking app",
                "The bank shows a 'Subscriptions' tab. Open Finance Recurring Transactions surfaces every detected stream &mdash; Netflix, Spotify, a gym &mdash; with next-charge date and average amount. Tapping a stream shows the mandate captured via Consent Management. If the user wants to cancel, the issuer can pause future ABU updates so the merchant cannot keep charging. Pre-charge alerts come from Transaction Notifications, with a one-tap 'pause for this month' hook."
            ),
            (
                "Merchant retention loop",
                "A SaaS merchant integrates ABU push to keep card-on-file valid, halving involuntary churn from card reissuance events. When a card finally hard-fails, Open Finance recurring detection on the cardholder's side can spot the missed charge and surface a 'one of your subscriptions failed' nudge so the user can update the card directly without a dunning email chain."
            ),
        ),
        examples=(
            "Subscription manager that surfaces streaming, gym and SaaS spend",
            "Auto-refresh card-on-file when issuers reissue plastic",
            "Pre-charge notifications + dispute hooks",
        ),
        apis=(
            "open_finance",
            "automatic_billing_updater",
            "transaction_notifications",
            "consent_management",
        ),
    ),
    Bundle(
        id="loyalty_stack",
        name="Loyalty, offers & benefits",
        tagline=(
            "Everything needed to surface the right offer or benefit to "
            "the right cardholder, gated by BIN and geo."
        ),
        description=(
            "The full Mastercard loyalty surface area in one bundle. "
            "Resolve cardholder eligibility from a BIN, source merchant "
            "and city-curated offers, manage publisher rebates, and "
            "expose benefits like Flight Delay Pass \u2014 all tied to a "
            "single cardholder context. Issuers and partners get a "
            "turn-key route from 'who is this cardholder?' to 'here is a "
            "redeemable offer in their pocket right now.'"
        ),
        anchor="offers_for_publishers",
        accent="#eb001b",
        icon_path="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z",
        value_props=(
            "BIN-gated eligibility",
            "City and country curated catalogues",
            "Publisher-managed rebates",
            "Branded benefit enrolment",
            "Merchant content management",
            "Trip-aware concierge experiences",
        ),
        journey=(
            ("bin_lookup", "Identify the card programme",
             "BIN Lookup determines issuer, product type and country \u2014 the eligibility key for every downstream offer."),
            ("benefits_eligibility", "Resolve entitlement bundle",
             "Eligibility API returns the benefits attached to the BIN (lounge access, insurance, concierge)."),
            ("easy_savings", "Surface always-on merchant offers",
             "Pulls the live offer catalogue keyed to BIN + country + language for in-app display."),
            ("priceless_cities", "Add destination-curated experiences",
             "Layer in city-specific Priceless experiences when the cardholder is travelling."),
            ("places", "Filter by proximity",
             "Rank offers by distance so a city-centre user sees the nearest participating merchants first."),
            ("offers_for_publishers", "Activate + record engagement",
             "Mint a per-user token, activate the offer, capture like/dislike and earned savings."),
            ("offers_merchant_content", "Manage the merchant catalogue",
             "Operators add merchants, addresses and creative; categories and sources stay in sync."),
            ("flight_delay_pass", "Enrol high-tier benefit",
             "Premium cardholders are auto-registered for lounge access on qualifying flights."),
        ),
        walkthroughs=(
            (
                "Issuer-branded offer wallet",
                "Inside the issuer's mobile banking app, the 'Rewards' tab shows a personalised feed. BIN Lookup confirms the user's card programme; Benefits Eligibility decides which entitlement set they get; Easy Savings supplies the always-on merchant offers; Places filters by proximity to surface what's actually near them; Offers for Publishers handles activation and captures engagement signals to feed back into ranking. The result feels native to the bank rather than a generic offer wall."
            ),
            (
                "Priceless Concierge trip planner",
                "User picks 'I'm flying to Tokyo for 5 days with my World Elite card'. Priceless Cities returns curated experiences for Tokyo; Benefits Eligibility checks lounge and insurance perks; Flight Delay Pass auto-enrols the upcoming flight; Easy Savings lists nearby merchant offers in Tokyo neighbourhoods; Offers for Publishers handles in-trip redemption. The whole itinerary is rendered as a single trip pack from one set of integrations."
            ),
        ),
        examples=(
            "Issuer-branded offer wallet inside a banking app",
            "City-specific Priceless concierge experiences",
            "Flight-delay lounge pass enrolment for premium card tiers",
        ),
        apis=(
            "priceless_cities",
            "easy_savings",
            "offers_for_publishers",
            "offers_merchant_content",
            "benefits_eligibility",
            "benefits_content_eligibility",
            "flight_delay_pass",
            "bin_lookup",
            "places",
            "consumer_clarity",
        ),
    ),
    Bundle(
        id="merchant_resolution",
        name="Merchant resolution",
        tagline=(
            "Three lenses on the same question — who and where is this "
            "merchant? Descriptor → canonical id → physical location."
        ),
        description=(
            "A drop-in enrichment trio. Take an opaque card-acceptor "
            "descriptor and resolve it three ways: a clean human-readable "
            "merchant name and logo (Consumer Clarity), a canonical "
            "Mastercard merchant identifier (Merchant Identifier), and "
            "the merchant's physical footprint and MCC (Places). "
            "Together they cut chargeback volume, improve statement "
            "comprehension and unlock per-merchant analytics."
        ),
        anchor="consumer_clarity",
        accent="#f37338",
        icon_path="M21 21l-4.35-4.35M11 19a8 8 0 1 1 0-16 8 8 0 0 1 0 16z",
        value_props=(
            "Clean merchant names + logos",
            "Canonical merchant identifiers",
            "MCC + industry categorisation",
            "Physical store geo coordinates",
            "Drops chargeback dispute volume",
            "Enables per-merchant analytics",
        ),
        journey=(
            ("consumer_clarity", "Resolve the descriptor",
             "Parse the raw card-acceptor string into a clean merchant name, logo, MCC and confidence score."),
            ("merchant_identifier", "Attach a stable id",
             "Map the clean merchant to a canonical Mastercard merchant id usable across reports and workflows."),
            ("places", "Resolve physical context",
             "Lookup nearby branches by coordinates, get the official MCC, and enrich with industry metadata."),
        ),
        walkthroughs=(
            (
                "In-app statement enrichment",
                "A mobile banking app calls Consumer Clarity on every new transaction. Cryptic strings like 'AMZN MKTP US*MK7G3B2X1' become 'Amazon Marketplace \u00b7 Books' with the Amazon logo. Each clean merchant is then run through Merchant Identifier so the bank can fold transactions into per-merchant analytics ('You spent \u00a3312 with Amazon last month, up 18%'). Places provides the physical location for card-present transactions so the user can verify on a map."
            ),
            (
                "Chargeback triage",
                "A dispute lands in the support queue. Consumer Clarity instantly shows the agent the clean merchant name and category; Merchant Identifier surfaces every other transaction from the same merchant in the cardholder's history; Places highlights whether the disputed transaction's coordinates match any of the cardholder's prior visits. Many disputes resolve in seconds because the cardholder simply didn't recognise the descriptor."
            ),
        ),
        examples=(
            "Statement-line enrichment in mobile banking",
            "Chargeback resolution \u2014 \"is this really my merchant?\"",
            "Geo-pinning of card-present transactions on a map",
        ),
        apis=(
            "consumer_clarity",
            "merchant_identifier",
            "places",
        ),
    ),
    Bundle(
        id="issuer_toolkit",
        name="Issuer & commercial toolkit",
        tagline=(
            "The natural starting set for an issuer or commercial-card "
            "programme manager."
        ),
        description=(
            "Spin up the operational backbone of a commercial or fleet "
            "programme: BIN intelligence, virtual-card spend controls, "
            "card-lifecycle refreshing, cross-border FX math, real-time "
            "cardholder alerts and consent governance. Programme "
            "managers get a complete control plane without stitching "
            "together six separate vendors."
        ),
        anchor="business_payment_controls",
        accent="#1a5fb4",
        icon_path="M3 7h18v12H3zM3 7l9-4 9 4M8 11h.01M16 11h.01",
        value_props=(
            "Virtual & real card issuance",
            "Per-card spend controls",
            "Real-time cardholder alerts",
            "Cross-border FX visibility",
            "Lifecycle automation",
            "Auditable consent trail",
        ),
        journey=(
            ("bin_lookup", "Validate accepted programmes",
             "Lookup determines product type and country \u2014 gates which spend control templates apply."),
            ("business_payment_controls", "Issue cards with controls",
             "Mint real or virtual cards bound to a funding source with per-MCC, per-amount and per-time controls."),
            ("automatic_billing_updater", "Keep card-on-file fresh",
             "When a card is reissued, downstream merchants and bill-pay vendors get the new details automatically."),
            ("enhanced_currency_conversion_calculator", "Show true cross-border cost",
             "Real settlement rate + DCC alternative so cardholders see the true cost of an overseas swipe."),
            ("transaction_notifications", "Push real-time alerts",
             "Sub-second push to the cardholder for every authorisation, with rich merchant context."),
            ("consent_management", "Capture mandates with 3DS",
             "Any recurring or stored-credential flow is anchored by an SCA-compliant consent record."),
        ),
        walkthroughs=(
            (
                "Virtual-card spend governance for a SaaS company",
                "Finance issues virtual cards via Business Payment Controls with a $250 monthly cap and MCC restrictions to SaaS-only. ABU keeps the cards live across reissue events. Every charge fires a Transaction Notification to the budget owner, who can approve or instantly freeze the card. ECCC surfaces the true cost when a vendor is billed in EUR. The whole stack delivers FBO-style controls without leaving the issuer's portal."
            ),
            (
                "Cross-border fleet card programme",
                "A logistics company runs drivers across three countries. BIN Lookup validates accepted card programmes; Business Payment Controls restricts spend to fuel + tolls; Transaction Notifications give the fleet manager real-time visibility; ECCC shows the FX impact of cross-border refuelling; ABU avoids declines when cards are reissued mid-route; Consent Management captures the driver's mandate for digital receipts."
            ),
        ),
        examples=(
            "Virtual-card issuance with category and amount limits",
            "Multi-currency expense management with live FX",
            "Real-time spend alerts to the cardholder's phone",
        ),
        apis=(
            "bin_lookup",
            "business_payment_controls",
            "automatic_billing_updater",
            "enhanced_currency_conversion_calculator",
            "transaction_notifications",
            "consent_management",
        ),
    ),
    Bundle(
        id="acquirer_risk",
        name="Acquirer & risk",
        tagline=(
            "Screen terminated merchants with MATCH; resolve and "
            "characterise the merchant/card being onboarded."
        ),
        description=(
            "Underwriting and merchant onboarding hardened against fraud. "
            "Screen prospective merchants against the MATCH Pro list, "
            "resolve who they actually are, and characterise the cards "
            "they accept by issuer, brand and country. The result is a "
            "single risk decision powered by data that would otherwise "
            "require multiple bureau integrations."
        ),
        anchor="match",
        accent="#a01010",
        icon_path="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z",
        value_props=(
            "MATCH Pro screening",
            "Canonical merchant identity",
            "BIN-level acceptance profile",
            "Descriptor sanity check",
            "Continuous portfolio monitoring",
            "Single risk decision surface",
        ),
        journey=(
            ("match", "Screen against terminated list",
             "MATCH Pro lookup flags merchants previously terminated for fraud, money laundering, excessive chargebacks."),
            ("merchant_identifier", "Resolve canonical identity",
             "Confirm the merchant's legal name and Mastercard merchant id matches what was submitted on the application."),
            ("bin_lookup", "Profile accepted card programmes",
             "Identify which BINs the merchant accepts to assess interchange exposure and cross-border risk."),
            ("consumer_clarity", "Validate the descriptor",
             "Confirm the merchant's actual card-acceptor descriptor matches the legal name \u2014 mismatches are a classic fraud signal."),
        ),
        walkthroughs=(
            (
                "Merchant onboarding decision",
                "A new merchant applies to be acquired. The application is screened against MATCH Pro to surface any prior termination; Merchant Identifier resolves the legal identity and confirms the merchant id matches; BIN Lookup profiles the BIN mix on their existing transaction volume; Consumer Clarity confirms the descriptor they intend to use parses to a clean, sane merchant name. The acquirer can approve, decline or escalate with one consolidated view."
            ),
            (
                "Portfolio re-screening",
                "Once a month the acquirer re-runs every active merchant through MATCH Pro to detect any post-onboarding listings, and Consumer Clarity to flag descriptor drift (a sudden change in descriptor pattern is a classic transaction-laundering signal). Merchant Identifier is used to detect merchant id collisions, and BIN Lookup to surface unusual BIN-mix shifts that suggest the merchant has changed business model."
            ),
        ),
        examples=(
            "Underwriting workflow for a new merchant application",
            "Card-acceptance risk scoring at terminal activation",
            "Periodic re-screening of existing merchant portfolio",
        ),
        apis=(
            "match",
            "merchant_identifier",
            "bin_lookup",
            "consumer_clarity",
        ),
    ),
    Bundle(
        id="sustainability",
        name="Sustainability / ESG",
        tagline=(
            "Carbon Calculator is meaningless without a transaction "
            "source and clean merchant categorisation."
        ),
        description=(
            "Embed climate-aware insights into every payment journey. "
            "Source the transactions through Open Finance, clean and "
            "categorise the merchants, then turn each line into a "
            "scientifically-grounded carbon footprint figure."
        ),
        anchor="carbon_calculator",
        accent="#0a8a52",
        icon_path="M12 22a10 10 0 0 0 0-20v20zM12 2a10 10 0 0 0 0 20",
        examples=(
            "Per-transaction CO₂ figure inside a banking statement view",
            "Monthly carbon report with offset purchase CTA",
            "Category-level emissions benchmarks (travel vs grocery vs fuel)",
        ),
        apis=(
            "carbon_calculator",
            "open_finance",
            "consumer_clarity",
            "merchant_identifier",
        ),
    ),
)


BUNDLES: dict[str, Bundle] = {b.id: b for b in _BUNDLES}


def iter_bundles() -> Iterable[Bundle]:
    """Iterate bundles in declared display order."""
    return iter(_BUNDLES)


def get(bundle_id: str) -> Bundle | None:
    return BUNDLES.get(bundle_id)


def bundles_for_api(api_id: str) -> list[Bundle]:
    """Return every bundle that includes ``api_id``."""
    return [b for b in _BUNDLES if api_id in b.apis]


__all__ = [
    "Bundle",
    "BUNDLES",
    "iter_bundles",
    "get",
    "bundles_for_api",
]
