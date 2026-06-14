# Vima — API & Use Case Reference

This document is the authoritative map of every API and Use Case in the Vima explorer.
Its primary audience is agents and developers who need to know **which files to edit**
when making changes to a specific API or Use Case.

---

## Project structure overview

```
app.py                        — Flask entry point, routes, /catalog endpoint
apis/
  catalog.py                  — single source of truth for all APIs: id, env_prefix, auth, display order
  registry.py                 — dynamic loader; no edits needed when adding APIs
  bundles.py                  — solution-shaped API bundle definitions
  credentials.py              — credential resolution helpers
  <id>/
    __init__.py
    api.py                    — MANIFEST, execute(), is_configured(), get_state()
    client.py                 — (where present) HTTP client / OAuth signing logic
usecases/
  registry.py                 — USE_CASE_MODULES list; auto-loads all use case modules
  <id>.py  OR  <id>/__init__.py  — MANIFEST + optional do_action()
simulator/
  blueprint.py                — Flask Blueprint; /api-sim/* routes
  handlers/                   — per-API mock response handlers
  fixtures/                   — seed JSON responses
config/
  .env                        — credentials (created from .env.example on first run)
  keys/                       — downloaded .p12 / .pem key files
static/
  js/app.js                   — entire front-end SPA (render functions, API call UI)
  css/styles.css              — global styles
templates/
  index.html                  — main HTML shell
tests/
  run.py                      — test orchestrator; invoked by test.bat / test.sh
  smoke/smoke.py              — smoke tests (server reachable, catalog loads, APIs respond)
  apis/bin_lookup.py          — BIN Lookup API contract tests
  lib/                        — shared helpers: server start/stop, install, provision, utils
tools/
  mcd-key-automation/         — Playwright portal provisioning tool (own .venv)
    provision.py              — provision one or more APIs from developer.mastercard.com
    clean_portal_projects.py  — delete SST-* test projects after a clean test run
```

---

## APIs

APIs live under `apis/<id>/api.py`. Each exposes a `MANIFEST` dict, an `execute(op_id, params)` function, and optional `is_configured()` / `get_state()`.

To **add or register** a new API:
1. Add an `ApiCatalogEntry` to `apis/catalog.py`.
2. Create `apis/<id>/api.py` with `MANIFEST` + `execute`.
3. Add handler + fixture under `simulator/handlers/` and `simulator/fixtures/`.
4. Add provisioning config in `tools/mcd-key-automation/providers/mastercard/api_config.py`.

> **Note on IDs.** The `id` field in `apis/catalog.py` is the canonical identifier — the folder name, the env prefix root, and the key used in `REGISTRY`. Some APIs have a `legacy_id` (an older short alias) retained only for `.env` migration. All code should use the canonical `id`.

> **Disabled APIs.** APIs listed in `DISABLED_API_IDS` in `apis/catalog.py` are hidden from the sidebar and provisioning modal but their code remains intact. Currently disabled: `flight_delay_pass` (manual tenant onboarding required), `consent_management` (merged into `transaction_notifications`).

---

### `open_finance` — Open Finance US

| | |
|---|---|
| **Files** | `apis/open_finance/api.py`, `apis/open_finance/client.py` |
| **Docs** | https://developer.mastercard.com/open-finance-us/documentation/ |
| **Auth** | OAuth 2.0 — Partner ID + Partner Secret + App Key |
| **Env prefix** | `OPEN_FINANCE` |
| **Env vars** | `OPEN_FINANCE_PARTNER_ID`, `OPEN_FINANCE_PARTNER_SECRET`, `OPEN_FINANCE_APP_KEY`, `OPEN_FINANCE_BASE_URL` |

**Categories & operations:**
- **Auth** — Create Access Token
- **Customers** — Create Testing Customer, List Customers, Get Customer by ID, Delete Customer Access, Set Active Customer, Get Consumer by ID, Get Consumer Details
- **Data Connect** — Generate Data Connect URL, Data Connect Lite URL
- **Accounts** — Refresh Accounts, Get Accounts, Get Account Details, Get Account by ID
- **Transactions** — Get Account Transactions, Get Customer Transactions, Get All Customer Transactions
- **Institutions** — Get Institution by ID, Search Institutions
- **Reports** — Ensure Consumer Record, Generate VOA Report, Generate VOI Report, Generate Cash Flow Report, Generate VOAI Report, Generate Statement Report, Generate Pay Statement Report, Get Report by ID, Get Reports by Customer
- **Payments** — Generate Payment Success Indicators, Generate FCRA PSI
- **Micro Entries** — Initiate Micro Entries, Verify Micro Entries
- **Business** — Get Business by Customer
- **TxPush** — Subscribe to TxPush, Get TxPush Subscriptions, Disable TxPush, Fire TxPush Test
- **Transfer** — Get Transfer Account
- **Data Enrichment** — Enrich Transactions

---

### `open_finance_au` — Open Finance Australia

| | |
|---|---|
| **Files** | `apis/open_finance_au/api.py`, `apis/open_finance_au/client.py` |
| **Docs** | https://developer.mastercard.com/open-finance-au/documentation/ |
| **Auth** | OAuth 2.0 — Partner ID + Partner Secret + App Key (AU variant) |
| **Env prefix** | `OPEN_FINANCE_AU` |
| **Env vars** | `OPEN_FINANCE_AU_PARTNER_ID`, `OPEN_FINANCE_AU_PARTNER_SECRET`, `OPEN_FINANCE_AU_APP_KEY` |

Same Finicity stack as US Open Finance targeting the Australian CDR (Consumer Data Right) variant. The provisioning wizard selects Australia via the Commercial Countries dropdown (same portal slug as `open_finance`).

**Categories & operations:**
- **Auth** — Create Access Token
- **Customers** — Customer lifecycle operations
- **Connect** — Generate CDR Connect URL
- **Accounts** — Refresh Accounts, Get Accounts
- **Transactions** — Get Account Transactions
- **Consent (CDR)** — Consent management operations
- **Reports** — VOA, VOI, Cash Flow reports
- **Webhooks** — TxPush subscriptions

---

### `open_finance_eu` — Open Finance Europe

| | |
|---|---|
| **Files** | `apis/open_finance_eu/api.py`, `apis/open_finance_eu/client.py` |
| **Docs** | https://developer.mastercard.com/open-finance-data/documentation/ |
| **Auth** | OAuth 2.0 with RS256-signed JWT client assertion (Aiia-backed EU stack) |
| **Env prefix** | `OPEN_FINANCE_EU` |
| **Env vars** | `OPEN_FINANCE_EU_CLIENT_ID`, `OPEN_FINANCE_EU_PRIVATE_KEY_PATH` |
| **Manual onboarding** | Email `openbankingeu_support@mastercard.com` with your RSA-4096 public PEM to receive a sandbox `clientId`. |

Distinct from the Finicity US/AU stack. Uses the Aiia platform with a different auth flow: an RS256-signed JWT client assertion is exchanged for an access token. Provisioning is manual (no portal wizard).

**Categories & operations:**
- **Auth** — Obtain access token (client_credentials + RS256 JWT assertion)
- **Providers** — List providers, Get provider details
- **Consent** — Create consent, Get consent status, Revoke consent
- **Accounts** — Get accounts for a consent
- **Transactions** — Get transactions
- **Balances** — Get balances
- **Insights** — Categorised spend insights

---

### `bin_lookup` — BIN Lookup

| | |
|---|---|
| **Files** | `apis/bin_lookup/api.py` |
| **Docs** | https://developer.mastercard.com/bin-lookup/documentation/ |
| **Auth** | OAuth 1.0a |
| **Env prefix** | `BIN_LOOKUP` |
| **Env vars** | `BIN_LOOKUP_CONSUMER_KEY`, `BIN_LOOKUP_SIGNING_KEY_PATH` |

**Categories & operations:**
- **Lookup** — Lookup BIN (POST; takes a 6–8 digit BIN / account range; returns issuer, brand, product type, country, prepaid/debit flags)

Also used by the BIN Lookup use case's **batch search** feature which reads from a local database of BINs (`data/`).

---

### `merchant_identifier` — Merchant Identifier

| | |
|---|---|
| **Files** | `apis/merchant_identifier/api.py` |
| **Docs** | https://developer.mastercard.com/merchant-identifier/documentation/ |
| **Auth** | OAuth 1.0a |
| **Env prefix** | `MERCHANT_IDENTIFIER` |
| **Env vars** | `MERCHANT_IDENTIFIER_CONSUMER_KEY`, `MERCHANT_IDENTIFIER_SIGNING_KEY_PATH` |

**Categories & operations:**
- **Merchant** — Merchant Identifier search (POST; resolves a raw merchant name to a normalised Mastercard merchant record with address, MCC, BIN range)
- **Lookup** — Get merchant by ID

---

### `automatic_billing_updater` — Automatic Billing Updater

| | |
|---|---|
| **Files** | `apis/automatic_billing_updater/api.py` |
| **Docs** | https://developer.mastercard.com/automatic-billing-updater/documentation/ |
| **Auth** | OAuth 1.0a |
| **Env prefix** | `AUTOMATIC_BILLING_UPDATER` |
| **Env vars** | `AUTOMATIC_BILLING_UPDATER_CONSUMER_KEY`, `AUTOMATIC_BILLING_UPDATER_SIGNING_KEY_PATH` |
| **Note** | Push operations (real-time card update notifications) require ABU Push service registration with Mastercard. |

**Categories & operations:**
- **Card Lifecycle** — Card update inquiry (provides latest PAN / expiry / status for a card-on-file token)
- **Subscriptions** — Subscribe to push notifications, Get subscription, Delete subscription

---

### `match` — MATCH Pro

| | |
|---|---|
| **Files** | `apis/match/api.py` |
| **Docs** | https://developer.mastercard.com/match/documentation/ |
| **Auth** | OAuth 1.0a |
| **Env prefix** | `MATCH` |
| **Env vars** | `MATCH_CONSUMER_KEY`, `MATCH_SIGNING_KEY_PATH` |

**Categories & operations:**
- **Risk** — Add to termination list, Termination inquiry
- **Merchants** — Lookup merchant, Search terminated merchants

---

### `consumer_clarity` — Consumer Clarity

| | |
|---|---|
| **Files** | `apis/consumer_clarity/api.py` |
| **Docs** | https://developer.mastercard.com/consumer-clarity-us/documentation/ |
| **Auth** | OAuth 1.0a + JWE (response payload encryption) |
| **Env prefix** | `CONSUMER_CLARITY` |
| **Env vars** | `CONSUMER_CLARITY_CONSUMER_KEY`, `CONSUMER_CLARITY_SIGNING_KEY_PATH` |
| **Endpoint** | `https://sandbox.api.ethocaweb.com/ethoca/consumer-clarity/searches` |

**Categories & operations:**
- **Merchant Search** — Merchant Clarity Search (POST; resolves a raw card-acceptor descriptor into a clean merchant name, logo, address, MCC)

Sandbox preset queries are defined in `_PRESETS` at the top of `api.py` and referenced by the `consumer_clarity` use case.

---

### `priceless_cities` — Priceless Cities

| | |
|---|---|
| **Files** | `apis/priceless_cities/api.py` |
| **Docs** | https://developer.mastercard.com/mastercard-benefits-and-experiences-portal/documentation/, https://developer.mastercard.com/priceless-specials/documentation/ |
| **Auth** | OAuth 1.0a |
| **Env prefix** | `PRICELESS_CITIES` |
| **Env vars** | `PRICELESS_CITIES_CONSUMER_KEY`, `PRICELESS_CITIES_SIGNING_KEY_PATH`, `PRICELESS_CITIES_ENV` |
| **Note** | Requires API Owner approval |

**Categories & operations:**
- **Priceless Platform** — Health Check, List Products, Get Product Info, Get Product Inventory, Get Product Translations, List Categories, List Programs, List Languages, List Subscriptions
- **Priceless Cities** — List Cities, Get City Products, Get City Products Near Me
- **Priceless Specials** — List Offers, List Benefits, List Programs, List Merchants, List Categories, List Countries, List Languages, List Mastercard Products

---

### `easy_savings` — Easy Savings

| | |
|---|---|
| **Files** | `apis/easy_savings/api.py` |
| **Docs** | https://developer.mastercard.com/easy-savings/documentation/ |
| **Auth** | OAuth 1.0a |
| **Env prefix** | `EASY_SAVINGS` |
| **Env vars** | `EASY_SAVINGS_CONSUMER_KEY`, `EASY_SAVINGS_SIGNING_KEY_PATH` |

**Categories & operations:**
- **Lookups** — List supported countries
- **Offers** — List offers for a BIN (by BIN + ISO-3 country + language)
- **Redemptions** — Redeem an offer, Get redemption by order ID

Sandbox canonical BIN: `52345678`, country: `IND`, language: `en-US`.

---

### `places` — Places (Merchant Locator)

| | |
|---|---|
| **Files** | `apis/places/api.py` |
| **Docs** | https://developer.mastercard.com/places/documentation/ |
| **Auth** | OAuth 1.0a |
| **Env prefix** | `PLACES` |
| **Env vars** | `PLACES_CONSUMER_KEY`, `PLACES_SIGNING_KEY_PATH` |

**Categories & operations:**
- **Places** — Search places (POST; lat/lng radius or country/city filter), Get place details
- **Reference** — List MCC codes, Get MCC by code, List industry codes, Get industry code details

---

### `offers_for_publishers` — Offers for Publishers

| | |
|---|---|
| **Files** | `apis/offers_for_publishers/api.py` |
| **Docs** | https://developer.mastercard.com/presentment/documentation/ |
| **Auth** | OAuth 1.0a + JWE |
| **Env prefix** | `OFFERS_FOR_PUBLISHERS` |
| **Env vars** | `OFFERS_FOR_PUBLISHERS_CONSUMER_KEY`, `OFFERS_FOR_PUBLISHERS_SIGNING_KEY_PATH` |

**Categories & operations:**
- **Access** — Create access token (short-lived `X-Auth-Token` per user)
- **Presentment** — List offers, Get offer, Activate offer, Record activity (like/dislike), Get savings
- **Platform** — List platform offers (admin/catalogue view, no user token required)
- **User Admin** — Enrol user, Update user/account, Card replacement, Search users
- **Rebates** — Rebate operations

---

### `offers_merchant_content` — Offers Merchant Content

| | |
|---|---|
| **Files** | `apis/offers_merchant_content/api.py` |
| **Docs** | https://developer.mastercard.com/eop-admin/documentation/ |
| **Auth** | OAuth 1.0a |
| **Env prefix** | `OFFERS_MERCHANT_CONTENT` |
| **Env vars** | `OFFERS_MERCHANT_CONTENT_CONSUMER_KEY`, `OFFERS_MERCHANT_CONTENT_SIGNING_KEY_PATH` |

**Categories & operations:**
- **Categories** — Search categories
- **Sources** — List sources
- **Merchants** — Create merchant, Add merchant address, Upload image
- **Images** — Image management
- **Offers** — Create offer

---

### `consent_management` — Consent Management *(disabled)*

| | |
|---|---|
| **Files** | `apis/consent_management/api.py` |
| **Docs** | https://developer.mastercard.com/consent-management/documentation/ |
| **Auth** | OAuth 1.0a + JWE |
| **Env prefix** | `CONSENT_MANAGEMENT` |
| **Env vars** | `CONSENT_MANAGEMENT_CONSUMER_KEY`, `CONSENT_MANAGEMENT_SIGNING_KEY_PATH` |
| **Status** | Disabled in UI — merged conceptually into `transaction_notifications`. Code intact for tests and internal use. |
| **Sandbox PAN** | `2303779951000297` |

**State keys:** `card_ref`, `consent_id`

**Categories & operations:**
- **Consent** — Create consent (POST /consents), Get consents by card reference, Start 3DS authentication, Verify 3DS authentication, Delete all consents for a card, Delete single consent

---

### `transaction_notifications` — Transaction Notifications

| | |
|---|---|
| **Files** | `apis/transaction_notifications/api.py` |
| **Docs** | https://developer.mastercard.com/transaction-notifications/documentation/ |
| **Auth** | OAuth 1.0a + JWE |
| **Env prefix** | `TRANSACTION_NOTIFICATIONS` |
| **Env vars** | `TRANSACTION_NOTIFICATIONS_CONSUMER_KEY`, `TRANSACTION_NOTIFICATIONS_SIGNING_KEY_PATH` |

**Categories & operations:**
- **Consent** — Create consent, Get consents, Start 3DS authentication, Verify 3DS authentication
- **Notifications** — Trigger test transaction, Get undelivered notifications

Requires a pre-registered webhook URL. The `txnotify` use case provides a live webhook receiver at `POST /txnotify/webhook` and a polling UI.

---

### `benefits_eligibility` — Benefits Eligibility

| | |
|---|---|
| **Files** | `apis/benefits_eligibility/api.py` |
| **Docs** | https://developer.mastercard.com/eligibility-api/documentation/ |
| **Auth** | OAuth 1.0a + JWE |
| **Env prefix** | `BENEFITS_ELIGIBILITY` |
| **Env vars** | `BENEFITS_ELIGIBILITY_CONSUMER_KEY`, `BENEFITS_ELIGIBILITY_SIGNING_KEY_PATH`, `BENEFITS_ELIGIBILITY_ENV` |
| **Note** | Requires API Owner approval |
| **Sandbox PAN** | `5416116000000233` (HMB benefits), `5341676355168133` |

**Categories & operations:**
- **Benefits** — Search benefits (POST /benefits/searches; cardNumber or cardNumberId)
- **Products** — Search products (POST /products/searches)
- **Widgets** — Generate widget access token (GET /widgets/access-tokens)
- **Card Identifiers** — Tokenise PAN (POST /card-identifiers; JWE encryption required in production)

---

### `benefits_content_eligibility` — Benefits Content Eligibility Service

| | |
|---|---|
| **Files** | `apis/benefits_content_eligibility/api.py` |
| **Docs** | https://developer.mastercard.com/bces-service/documentation/ |
| **Auth** | OAuth 1.0a + JWE |
| **Env prefix** | `BENEFITS_CONTENT_ELIGIBILITY` |
| **Env vars** | `BENEFITS_CONTENT_ELIGIBILITY_CONSUMER_KEY`, `BENEFITS_CONTENT_ELIGIBILITY_SIGNING_KEY_PATH`, `BENEFITS_CONTENT_ELIGIBILITY_ENV` |
| **Sandbox PAN** | `5291070000000000`, benefit code `CDW`, product code `DCG` |

**Categories & operations:**
- **Benefits Content** — Search benefit contents (POST /benefit-contents/searches; returns rich renderable content: names, descriptions, imagery, T&Cs, FAQ, CTA links)

---

### `enhanced_currency_conversion_calculator` — Enhanced Currency Conversion Calculator

| | |
|---|---|
| **Files** | `apis/enhanced_currency_conversion_calculator/api.py` |
| **Docs** | https://developer.mastercard.com/enhanced-currency-conversion-calculator/documentation/ |
| **Auth** | OAuth 1.0a |
| **Env prefix** | `ENHANCED_CURRENCY_CONVERSION_CALCULATOR` |
| **Env vars** | `ENHANCED_CURRENCY_CONVERSION_CALCULATOR_CONSUMER_KEY`, `ENHANCED_CURRENCY_CONVERSION_CALCULATOR_SIGNING_KEY_PATH` |
| **Note** | Requires API Owner approval |

**Categories & operations:**
- **FX** — Get currency conversion rate (Mastercard daily settlement rate for a currency pair)
- **Settlement** — Get ECB reference rates (EU Reg 2019/518 full-disclosure rates)

---

### `carbon_calculator` — Carbon Calculator *(manual onboarding)*

| | |
|---|---|
| **Files** | `apis/carbon_calculator/api.py` |
| **Docs** | https://developer.mastercard.com/carbon-calculator/documentation/ |
| **Auth** | OAuth 1.0a + JWE |
| **Env prefix** | `CARBON_CALCULATOR` |
| **Env vars** | `CARBON_CALCULATOR_CONSUMER_KEY`, `CARBON_CALCULATOR_SIGNING_KEY_PATH` |
| **Manual onboarding** | Requires a Mastercard-issued Customer ID (CID), Legal Name, and BIN range. Contact `carboncalculator@mastercard.com`. |

**Categories & operations:**
- **Service Provider** — Register service provider, Get service provider
- **Payment Cards** — Register payment card, Get payment card, Delete payment card
- **Environmental Impact** — Calculate transaction carbon footprint, Get carbon scores
- **Engagement** — Get aggregated carbon footprint, Category breakdown

---

### `business_payment_controls` — Business Payment Controls

| | |
|---|---|
| **Files** | `apis/business_payment_controls/api.py` |
| **Docs** | https://developer.mastercard.com/business-payment-controls/documentation/ |
| **Auth** | OAuth 1.0a |
| **Env prefix** | `BUSINESS_PAYMENT_CONTROLS` |
| **Env vars** | `BUSINESS_PAYMENT_CONTROLS_CONSUMER_KEY`, `BUSINESS_PAYMENT_CONTROLS_SIGNING_KEY_PATH` |
| **Note** | Provisioning requires a registration token from your Mastercard Commercial Products implementation manager (playbook default: `123456789`). |

**Categories & operations:**
- **Real Cards** — Create real card, Get real card, Update real card, Delete real card
- **Virtual Cards** — Create virtual card, Get virtual card
- **Funding Sources** — List funding sources
- **Controls** — Set spending controls, Get controls
- **Custom Data** — Add custom data fields
- **Authorization Reports** — Get authorization report
- **Clearing Reports** — Get clearing report

---

### `flight_delay_pass` — Flight Delay Pass *(disabled)*

| | |
|---|---|
| **Files** | `apis/flight_delay_pass/api.py` |
| **Docs** | https://developer.mastercard.com/flight-delay-pass/documentation/ |
| **Auth** | OAuth 1.0a + JWE |
| **Env prefix** | `FLIGHT_DELAY_PASS` |
| **Env vars** | `FLIGHT_DELAY_PASS_CONSUMER_KEY`, `FLIGHT_DELAY_PASS_SIGNING_KEY_PATH` |
| **Status** | Disabled — issuer must be provisioned as a Flight Delay Pass tenant (~26 days) and the Client Key whitelisted before the API returns 2xx. |

**Categories & operations:**
- **Eligibility** — Check FDP eligibility for a card
- **Registrations** — Create registration, Get registration, Update registration, Delete registration

---

## Use Cases

Use Cases live under `usecases/<id>.py` (single file) or `usecases/<id>/__init__.py` (package).
Each exposes a `MANIFEST` dict and an optional `do_action(action, params)` function.

To **add or register** a new use case:
1. Create `usecases/<id>.py` or `usecases/<id>/` package with a `MANIFEST`.
2. Add `"<id>"` to `USE_CASE_MODULES` in `usecases/registry.py`.
3. Add a `renderXxx()` JS function in `static/js/app.js` and dispatch it in the `renderUseCase()` switch block.

The **front-end render** for each use case is identified by `MANIFEST["render"]` and dispatched in `static/js/app.js`.

---

### `pfm` — Personal Finance Manager

| | |
|---|---|
| **Files** | `usecases/pfm/`, `usecases/pfm/index.html`, `usecases/pfm/style.css` |
| **APIs used** | `open_finance` |
| **Render key** | `pfm` |
| **Static route** | `GET /pfm/<filename>` → served from `usecases/pfm/` |

Fetches linked account balances and 90 days of transactions from Open Finance, then shapes them into a phone-style PFM dashboard: net worth, spend-by-category breakdown, and a scrollable transaction history. The full UI lives in the self-contained `usecases/pfm/index.html` page, rendered via an iframe with a refresh button.

**`do_action` actions:** `create_customer`, `connect_url`, `refresh_accounts`, `enrich_transactions`, `get_recurring`

---

### `enrichment` — Data Enrichment

| | |
|---|---|
| **File** | `usecases/enrichment.py` |
| **APIs used** | `open_finance` |
| **Render key** | `enrichment` |

Sends a curated batch of raw transaction descriptions to the Open Finance Data Enrichment endpoint and shows before/after pairs. Uses a local JSON cache to survive sandbox quota exhaustion.

---

### `recurring` — Recurring Transactions

| | |
|---|---|
| **File** | `usecases/recurring.py` |
| **APIs used** | `open_finance` |
| **Render key** | `recurring` |

Calls the Open Finance Recurring Transactions API to surface every repeating debit and credit (subscriptions, salary credits, etc.) shaped into stream cards.

---

### `psi` — Payment Success Indicator

| | |
|---|---|
| **File** | `usecases/psi.py` |
| **APIs used** | `open_finance` |
| **Render key** | `psi` |

Evaluates ACH settlement risk over a 10-day window: per-day probability scores + an unauthorised-return fraud signal, rendered as a day-by-day confidence timeline.

---

### `financeincolour` — Finance In Colour

| | |
|---|---|
| **Files** | `usecases/financeincolour/__init__.py`, plus UI assets in same directory |
| **APIs used** | `open_finance` |
| **Render key** | `financeincolour` |

Turns a customer's transaction history into a richly coloured, behaviour-driven visualisation: a money-in vs money-out flow chart over time, a category-spend breakdown, a trend indicator showing whether spending is accelerating or cooling, and a generative "financial fingerprint" — an abstract graphic whose shape, colours and rhythm are derived from the customer's own behaviour. Data shape mirrors the PFM use case.

**`do_action` actions:** `get_data`

---

### `the_wire` — The Wire

| | |
|---|---|
| **Files** | `usecases/the_wire/__init__.py`, plus UI assets in same directory |
| **APIs used** | `open_finance` (data shape; demo data also baked in for offline use) |
| **Render key** | `the_wire` |

Shows the entire data journey of a single transaction: from raw POS descriptor at the merchant terminal, through Open Finance aggregation, merchant enrichment, category classification, and the final consumer-facing line in their banking app. Visualised as a vertical glowing wire with five animated nodes — each node reveals the exact JSON shape of the transaction at that stage. Makes the plumbing of Open Banking tangible.

---

### `binlookup` — BIN Lookup

| | |
|---|---|
| **Files** | `usecases/bin_lookup/` |
| **APIs used** | `bin_lookup` |
| **Render key** | `binlookup` |

Animates every data field returned by the BIN Lookup API onto an interactive payment card visualiser. Also exposes a **batch search** mode that reads a local BIN database (`data/`) and lets users expand rows to "Visualize as Card".

---

### `clarity` — Consumer Clarity

| | |
|---|---|
| **Files** | `usecases/consumer_clarity/` |
| **APIs used** | `consumer_clarity` |
| **Render key** | `clarity` |

Transforms a raw card-acceptor descriptor into a rich merchant card (clean name, logo, address, MCC). Imports `_PRESETS` directly from `apis/consumer_clarity/api.py` so the UI dropdown always matches backend test cases.

---

### `easysavings` — Easy Savings

| | |
|---|---|
| **Files** | `usecases/easy_savings/` |
| **APIs used** | `easy_savings` |
| **Render key** | `easysavings` |

Browse and redeem SME merchant offers from the Easy Savings catalogue. Default sandbox values: BIN `52345678`, country `IND`, language `en-US`.

**`do_action` actions:** `browse`, `redeem`

---

### `places` — Places

| | |
|---|---|
| **Files** | `usecases/places/` |
| **APIs used** | `places` |
| **Render key** | `places` |

Proximity-based merchant discovery: enter a location (lat/lng or city/country), filter by industry code, and see nearby merchants plotted on a map with NFC, EMV, and payment capability metadata.

---

### `txnotify` — Transaction Notifications Live

| | |
|---|---|
| **Files** | `usecases/txnotify/__init__.py`, plus UI assets in same directory |
| **APIs used** | `transaction_notifications` |
| **Render key** | `txnotify` |
| **Webhook endpoint** | `POST /txnotify/webhook` |

Live webhook demo: the Flask app receives signed Mastercard transaction notification payloads and surfaces them in real time. The use case guides the user through launching ngrok, registering the webhook URL in their developer project, enrolling a card, and triggering a test transaction. A ring buffer stores the 100 most recent events; the UI polls `do_action("poll")` every 2 s.

**`do_action` actions:** `poll`

---

### `identity` — Online Identity Verification

| | |
|---|---|
| **File** | `usecases/identity.py` |
| **APIs used** | *(simulation only — Finicity Connect, Mastercard Consent, Ekata)* |
| **Render key** | `identity` |

Front-end-only simulation of an identity verification journey combining bank ownership (Finicity Connect), card consent (Mastercard Consent API), and device/email risk signals (Ekata). No live API calls are made.

---

### `specials` — Priceless Concierge

| | |
|---|---|
| **File** | `usecases/specials.py` |
| **APIs used** | `priceless_cities` (Priceless Specials) |
| **Render key** | `specials` |

Trip-planner experience: pick an issuing country, destination, card product, and interest category; see curated offers, card benefits, marketing programs, and participating merchants. Defaults: eligible `US`, destination `JP`, product `MWE`.

---

### `findacard` — Find A Card

| | |
|---|---|
| **Files** | `usecases/findacard/` |
| **APIs used** | *(local agent — Open Finance, MDES, Offers, Rewards)* |
| **Render key** | `findacard` |
| **Local port** | `5432` |

Embeds a locally-running Find A Card web service (must be running on `localhost:5432`). Illustrates an autonomous agent that sources and provisions a card to a wallet. Shows an offline state if the service is not reachable.

---

### `sonic` — Sonic Branding

| | |
|---|---|
| **Files** | `usecases/sonic.py`, `usecases/sonicbrand/index.html`, `usecases/sonicbrand/style.css`, `usecases/sonicbrand/kicks/` |
| **APIs used** | *(front-end only — Web Audio API)* |
| **Render key** | `sonic` |
| **Static route** | `GET /sonicbrand/<filename>` → served from `usecases/sonicbrand/` |

Front-end-only showcase of Mastercard's sonic identity: acceptance sound, jingle, app UI micro-sounds, and regional variants. Sounds are synthesised in the browser using the Web Audio API. Actual licensed assets must be sourced from Mastercard Brand Centre.

---

### `testchat` — Test Chat

| | |
|---|---|
| **Files** | `usecases/testchat/__init__.py`, `usecases/testchat/testchat.html` |
| **APIs used** | *(none)* |
| **Render key** | `testchat` |
| **Static route** | `GET /testchat/<filename>` → served from `usecases/testchat/` |

Prototype chat interface with a canvas-based revolving Mastercard globe (Fibonacci lattice, no external deps). Features Refresh and Edit buttons; Edit opens the in-process Vima Chat modal (mounted at `/chat/simple`).

---

## Environment variables summary

| Variable | API | Description |
|---|---|---|
| `OPEN_FINANCE_PARTNER_ID` | open_finance | Finicity partner ID |
| `OPEN_FINANCE_PARTNER_SECRET` | open_finance | Finicity partner secret |
| `OPEN_FINANCE_APP_KEY` | open_finance | Finicity app key |
| `OPEN_FINANCE_BASE_URL` | open_finance | Finicity base URL (default: `https://api.finicity.com`) |
| `OPEN_FINANCE_AU_PARTNER_ID` | open_finance_au | Finicity AU partner ID |
| `OPEN_FINANCE_AU_PARTNER_SECRET` | open_finance_au | Finicity AU partner secret |
| `OPEN_FINANCE_AU_APP_KEY` | open_finance_au | Finicity AU app key |
| `OPEN_FINANCE_EU_CLIENT_ID` | open_finance_eu | Aiia client ID (issued by onboarding team) |
| `OPEN_FINANCE_EU_PRIVATE_KEY_PATH` | open_finance_eu | Path to RSA-4096 private key PEM |
| `BIN_LOOKUP_CONSUMER_KEY` | bin_lookup | OAuth consumer key |
| `BIN_LOOKUP_SIGNING_KEY_PATH` | bin_lookup | Path to `.p12` / `.pem` signing key |
| `MERCHANT_IDENTIFIER_CONSUMER_KEY` | merchant_identifier | OAuth consumer key |
| `MERCHANT_IDENTIFIER_SIGNING_KEY_PATH` | merchant_identifier | Path to signing key |
| `AUTOMATIC_BILLING_UPDATER_CONSUMER_KEY` | automatic_billing_updater | OAuth consumer key |
| `AUTOMATIC_BILLING_UPDATER_SIGNING_KEY_PATH` | automatic_billing_updater | Path to signing key |
| `MATCH_CONSUMER_KEY` | match | OAuth consumer key |
| `MATCH_SIGNING_KEY_PATH` | match | Path to signing key |
| `CONSUMER_CLARITY_CONSUMER_KEY` | consumer_clarity | OAuth consumer key |
| `CONSUMER_CLARITY_SIGNING_KEY_PATH` | consumer_clarity | Path to signing key |
| `PRICELESS_CITIES_CONSUMER_KEY` | priceless_cities | OAuth consumer key |
| `PRICELESS_CITIES_SIGNING_KEY_PATH` | priceless_cities | Path to signing key |
| `PRICELESS_CITIES_ENV` | priceless_cities | `sandbox` (default) or `production` |
| `EASY_SAVINGS_CONSUMER_KEY` | easy_savings | OAuth consumer key |
| `EASY_SAVINGS_SIGNING_KEY_PATH` | easy_savings | Path to signing key |
| `PLACES_CONSUMER_KEY` | places | OAuth consumer key |
| `PLACES_SIGNING_KEY_PATH` | places | Path to signing key |
| `OFFERS_FOR_PUBLISHERS_CONSUMER_KEY` | offers_for_publishers | OAuth consumer key |
| `OFFERS_FOR_PUBLISHERS_SIGNING_KEY_PATH` | offers_for_publishers | Path to signing key |
| `OFFERS_MERCHANT_CONTENT_CONSUMER_KEY` | offers_merchant_content | OAuth consumer key |
| `OFFERS_MERCHANT_CONTENT_SIGNING_KEY_PATH` | offers_merchant_content | Path to signing key |
| `CONSENT_MANAGEMENT_CONSUMER_KEY` | consent_management | OAuth consumer key |
| `CONSENT_MANAGEMENT_SIGNING_KEY_PATH` | consent_management | Path to signing key |
| `TRANSACTION_NOTIFICATIONS_CONSUMER_KEY` | transaction_notifications | OAuth consumer key |
| `TRANSACTION_NOTIFICATIONS_SIGNING_KEY_PATH` | transaction_notifications | Path to signing key |
| `BENEFITS_ELIGIBILITY_CONSUMER_KEY` | benefits_eligibility | OAuth consumer key |
| `BENEFITS_ELIGIBILITY_SIGNING_KEY_PATH` | benefits_eligibility | Path to signing key |
| `BENEFITS_ELIGIBILITY_ENV` | benefits_eligibility | `sandbox` (default) or `production` |
| `BENEFITS_CONTENT_ELIGIBILITY_CONSUMER_KEY` | benefits_content_eligibility | OAuth consumer key |
| `BENEFITS_CONTENT_ELIGIBILITY_SIGNING_KEY_PATH` | benefits_content_eligibility | Path to signing key |
| `BENEFITS_CONTENT_ELIGIBILITY_ENV` | benefits_content_eligibility | `sandbox` (default) or `production` |
| `ENHANCED_CURRENCY_CONVERSION_CALCULATOR_CONSUMER_KEY` | enhanced_currency_conversion_calculator | OAuth consumer key |
| `ENHANCED_CURRENCY_CONVERSION_CALCULATOR_SIGNING_KEY_PATH` | enhanced_currency_conversion_calculator | Path to signing key |
| `CARBON_CALCULATOR_CONSUMER_KEY` | carbon_calculator | OAuth consumer key |
| `CARBON_CALCULATOR_SIGNING_KEY_PATH` | carbon_calculator | Path to signing key |
| `BUSINESS_PAYMENT_CONTROLS_CONSUMER_KEY` | business_payment_controls | OAuth consumer key |
| `BUSINESS_PAYMENT_CONTROLS_SIGNING_KEY_PATH` | business_payment_controls | Path to signing key |
| `FLIGHT_DELAY_PASS_CONSUMER_KEY` | flight_delay_pass | OAuth consumer key |
| `FLIGHT_DELAY_PASS_SIGNING_KEY_PATH` | flight_delay_pass | Path to signing key |

---

## Key cross-cutting files

| File | Purpose |
|---|---|
| `app.py` | Flask routes; `GET /catalog` returns unified JSON of all APIs + use cases |
| `apis/catalog.py` | Single source of truth for API identity, env prefix, auth type, display order |
| `apis/registry.py` | Dynamic API loader — no edits needed when adding new APIs |
| `usecases/registry.py` | `USE_CASE_MODULES` list; edit to add/remove use cases |
| `static/js/app.js` | Entire SPA: API call UI, use case renderers, BIN batch search, modal, globe |
| `static/css/styles.css` | All styles including use-case-specific rules |
| `templates/index.html` | Main HTML shell |
| `simulator/blueprint.py` | Simulator Flask Blueprint (`/api-sim/*`) |
| `tests/run.py` | Test orchestrator — source of record for test flow and steps |
| `test.bat` / `test.sh` | Test launchers (Windows / macOS+Linux) |
| `tools/mcd-key-automation/` | Playwright portal automation tool (own `.venv`) |
| `tools/mcd-key-automation/clean_portal_projects.py` | Deletes SST-* projects after clean test runs |
