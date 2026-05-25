# Vima — API & Use Case Reference

This document is the authoritative map of every API and Use Case in the Vima explorer.
Its primary audience is agents and developers who need to know **which files to edit**
when making changes to a specific API or Use Case.

---

## Project structure overview

```
app.py                        — Flask entry point, routes, /catalog endpoint
apis/
  registry.py                 — REGISTRY dict + ORDER list; import order for the API tab
  <id>/
    __init__.py
    api.py                    — MANIFEST, execute(), is_configured(), get_state()
    client.py                 — (where present) HTTP client / OAuth signing logic
usecases/
  registry.py                 — USE_CASE_MODULES list; auto-loads all use case modules
  <id>.py  OR  <id>/__init__.py  — MANIFEST + optional do_action()
static/
  js/app.js                   — entire front-end SPA (render functions, API call UI)
  css/styles.css              — global styles
templates/
  index.html                  — main shell template
```

---

## APIs

APIs live under `apis/<id>/api.py`. Each exposes a `MANIFEST` dict, an `execute(op_id, params)` function, and optional `is_configured()` / `get_state()`.

To **add or register** a new API:
1. Create `apis/<id>/__init__.py` and `apis/<id>/api.py` (and `client.py` if needed).
2. Import it in `apis/registry.py` and add `"<id>"` to both `REGISTRY` and `ORDER`.

---

### `ofin` — Open Finance (Finicity / US Open Banking)

| | |
|---|---|
| **Files** | `apis/ofin/api.py`, `apis/ofin/client.py` |
| **Docs** | https://developer.mastercard.com/open-finance-us/documentation/ |
| **Auth** | Partner ID + Partner Secret + App Key (env: `PARTNER_ID`, `PARTNER_SECRET`, `APP_KEY`) |
| **Env** | `API_BASE_URL` (default: `https://api.finicity.com`) |

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

### `binlookup` — BIN Lookup

| | |
|---|---|
| **Files** | `apis/binlookup/api.py` |
| **Docs** | https://developer.mastercard.com/bin-lookup/documentation/ |
| **Auth** | OAuth 1.0a (env: `BINLOOKUP_CONSUMER_KEY`, `BINLOOKUP_SIGNING_KEY_PATH`) |
| **Cert** | `binlookup.p12` in project root |

**Categories & operations:**
- **Lookup** — Lookup BIN (POST; takes a 6–8 digit BIN / account range; returns issuer, brand, product type, country, prepaid/debit flags)

Also used by the BIN Lookup use case's **batch search** feature which reads from a local database of BINs (`data/`).

---

### `clarity` — Consumer Clarity (Ethoca)

| | |
|---|---|
| **Files** | `apis/clarity/api.py` |
| **Docs** | https://developer.mastercard.com/consumer-clarity/documentation/ |
| **Auth** | OAuth 1.0a (env: `CLARITY_CONSUMER_KEY`, `CLARITY_SIGNING_KEY_PATH`) |
| **Endpoint** | `https://sandbox.api.ethocaweb.com/ethoca/consumer-clarity/searches` |

**Categories & operations:**
- **Searches** — Merchant Clarity Search (POST; resolves a raw card-acceptor descriptor into a clean merchant name, logo, address, MCC)

Sandbox preset queries are defined in `_PRESETS` at the top of `api.py` and referenced by the `clarity` use case.

---

### `priceless` — Priceless (Platform + Cities + Specials)

| | |
|---|---|
| **Files** | `apis/priceless/api.py` |
| **Docs** | https://developer.mastercard.com/mastercard-benefits-and-experiences-portal/documentation/, https://developer.mastercard.com/priceless-specials/documentation/ |
| **Auth** | OAuth 1.0a (env: `PRICELESS_CONSUMER_KEY`, `PRICELESS_SIGNING_KEY_PATH`) |
| **Env** | `PRICELESS_ENV` (`sandbox` / `production`) |

**Categories & operations:**
- **Priceless Platform** — Health Check, List Products, Get Product Info, Get Product Inventory, Get Product Translations, List Categories, List Programs, List Languages, List Subscriptions
- **Priceless Cities** — List Cities, Get City Products, Get City Products Near Me
- **Priceless Specials** — List Offers, List Benefits, List Programs, List Merchants, List Categories, List Countries, List Languages, List Mastercard Products

---

### `easysavings` — Easy Savings Specials

| | |
|---|---|
| **Files** | `apis/easysavings/api.py` |
| **Docs** | https://developer.mastercard.com/easy-savings-specials/documentation/ |
| **Auth** | OAuth 1.0a (env: `EASYSAVINGS_CONSUMER_KEY`, `EASYSAVINGS_SIGNING_KEY_PATH`) |

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
| **Auth** | OAuth 1.0a (env: `PLACES_CONSUMER_KEY`, `PLACES_SIGNING_KEY_PATH`) |

**Categories & operations:**
- **Places** — Search places (POST; lat/lng radius or country/city filter), Get place details
- **Reference** — List MCC codes, Get MCC by code, List industry codes, Get industry code details

---

### `ofpub` — Offers for Publishers (Presentment)

| | |
|---|---|
| **Files** | `apis/ofpub/api.py` |
| **Docs** | https://developer.mastercard.com/presentment/documentation/ |
| **Auth** | OAuth 1.0a (env: `OFPUB_CONSUMER_KEY`, `OFPUB_SIGNING_KEY_PATH`) |

**Categories & operations:**
- **Access** — Create access token (short-lived `X-Auth-Token` per user)
- **Presentment** — List offers, Get offer, Activate offer, Record activity (like/dislike), Get savings
- **Platform** — List platform offers (admin/catalogue view, no user token required)
- **User Admin** — Enrol user, Update user/account, Card replacement, Search users
- **Rebates** — Rebate operations

---

### `ofmc` — Offers Merchant Content (EOP Admin)

| | |
|---|---|
| **Files** | `apis/ofmc/api.py` |
| **Docs** | https://developer.mastercard.com/eop-admin/documentation/ |
| **Auth** | OAuth 1.0a (env: `OFMC_CONSUMER_KEY`, `OFMC_SIGNING_KEY_PATH`) |

**Categories & operations:**
- **Categories** — Search categories
- **Sources** — List sources
- **Merchants** — Create merchant, Add merchant address, Upload image
- **Images** — Image management
- **Offers** — Create offer

---

### `consent` — Consent Management

| | |
|---|---|
| **Files** | `apis/consent/api.py` |
| **Docs** | https://developer.mastercard.com/consent-management/documentation/ |
| **Auth** | OAuth 1.0a (env: `CONSENT_CONSUMER_KEY`, `CONSENT_SIGNING_KEY_PATH`) |
| **Sandbox PAN** | `2303779951000297` |

**State keys:** `card_ref`, `consent_id`

**Categories & operations:**
- **Consent** — Create consent (POST /consents), Get consents by card reference, Start 3DS authentication, Verify 3DS authentication, Delete all consents for a card, Delete single consent

---

### `txnotify` — Transaction Notifications

| | |
|---|---|
| **Files** | `apis/txnotify/api.py` |
| **Docs** | https://developer.mastercard.com/transaction-notifications/documentation/ |
| **Auth** | OAuth 1.0a (env: `TXNOTIFY_CONSUMER_KEY`, `TXNOTIFY_SIGNING_KEY_PATH`) |

**Categories & operations:**
- **Notifications** — Trigger test transaction, Get undelivered notifications

Requires a pre-registered webhook URL and a `cardReference` obtained via the Consent Management API.

---

### `eligibility` — Benefits Eligibility

| | |
|---|---|
| **Files** | `apis/eligibility/api.py` |
| **Docs** | https://developer.mastercard.com/eligibility-api/documentation/ |
| **Auth** | OAuth 1.0a (env: `ELIGIBILITY_CONSUMER_KEY`, `ELIGIBILITY_SIGNING_KEY_PATH`) |
| **Env** | `ELIGIBILITY_ENV` (`sandbox` / `production`) |
| **Sandbox PAN** | `5416116000000233` (HMB benefits), `5341676355168133` |

**Categories & operations:**
- **Benefits** — Search benefits (POST /benefits/searches; cardNumber or cardNumberId)
- **Products** — Search products (POST /products/searches)
- **Widgets** — Generate widget access token (GET /widgets/access-tokens)
- **Card Identifiers** — Tokenise PAN (POST /card-identifiers; JWE encryption required in production)

---

### `bces` — Benefits Content Eligibility Service

| | |
|---|---|
| **Files** | `apis/bces/api.py` |
| **Docs** | https://developer.mastercard.com/bces-service/documentation/ |
| **Auth** | OAuth 1.0a (env: `BCES_CONSUMER_KEY`, `BCES_SIGNING_KEY_PATH`) |
| **Env** | `BCES_ENV` (`sandbox` / `production`) |
| **Sandbox PAN** | `5291070000000000`, benefit code `CDW`, product code `DCG` |

**Categories & operations:**
- **Benefits Content** — Search benefit contents (POST /benefit-contents/searches; returns rich renderable content: names, descriptions, imagery, T&Cs, FAQ, CTA links)

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
| **Files** | `usecases/pfm.py`, `usecases/pfm/index.html`, `usecases/pfm/style.css` |
| **APIs used** | `ofin` |
| **Render key** | `pfm` |
| **Static route** | `GET /pfm/<filename>` → served from `usecases/pfm/` |

Fetches linked account balances and 90 days of transactions from Open Finance, then shapes them into a phone-style PFM dashboard: net worth, spend-by-category breakdown, and a scrollable transaction history. The full UI lives in the self-contained `usecases/pfm/index.html` page, rendered via an iframe with a refresh button. All PFM-specific CSS is in `usecases/pfm/style.css`.

**`do_action` actions:** `create_customer`, `connect_url`, `refresh_accounts`, `enrich_transactions`, `get_recurring`

---

### `enrichment` — Data Enrichment

| | |
|---|---|
| **File** | `usecases/enrichment.py` |
| **APIs used** | `ofin` |
| **Render key** | `enrichment` |

Sends a curated batch of raw transaction descriptions to the Open Finance Data Enrichment endpoint and shows before/after pairs. Uses a local JSON cache to survive sandbox quota exhaustion.

---

### `recurring` — Recurring Transactions

| | |
|---|---|
| **File** | `usecases/recurring.py` |
| **APIs used** | `ofin` |
| **Render key** | `recurring` |

Calls the Open Finance Recurring Transactions API to surface every repeating debit and credit (subscriptions, salary credits, etc.) shaped into stream cards.

---

### `psi` — Payment Success Indicator

| | |
|---|---|
| **File** | `usecases/psi.py` |
| **APIs used** | `ofin` |
| **Render key** | `psi` |

Evaluates ACH settlement risk over a 10-day window: per-day probability scores + an unauthorised-return fraud signal, rendered as a day-by-day confidence timeline.

---

### `binlookup` — BIN Lookup

| | |
|---|---|
| **File** | `usecases/binlookup.py` |
| **APIs used** | `binlookup` |
| **Render key** | `binlookup` |

Animates every data field returned by the BIN Lookup API onto an interactive payment card visualiser. Also exposes a **batch search** mode that reads a local BIN database (`data/`) and lets users expand rows to "Visualize as Card".

---

### `clarity` — Consumer Clarity

| | |
|---|---|
| **File** | `usecases/clarity.py` |
| **APIs used** | `clarity` |
| **Render key** | `clarity` |

Transforms a raw card-acceptor descriptor into a rich merchant card (clean name, logo, address, MCC). Imports `_PRESETS` directly from `apis/clarity/api.py` so the UI dropdown always matches backend test cases.

---

### `easysavings` — Easy Savings

| | |
|---|---|
| **File** | `usecases/easysavings.py` |
| **APIs used** | `easysavings` |
| **Render key** | `easysavings` |

Browse and redeem SME merchant offers from the Easy Savings catalogue. Default sandbox values: BIN `52345678`, country `IND`, language `en-US`.

**`do_action` actions:** `browse`, `redeem`

---

### `places` — Places

| | |
|---|---|
| **File** | `usecases/places.py` |
| **APIs used** | `places` |
| **Render key** | `places` |

Proximity-based merchant discovery: enter a location (lat/lng or city/country), filter by industry code, and see nearby merchants plotted on a map with NFC, EMV, and payment capability metadata.

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
| **APIs used** | `priceless` (Priceless Specials) |
| **Render key** | `specials` |

Trip-planner experience: pick an issuing country, destination, card product, and interest category; see curated offers, card benefits, marketing programs, and participating merchants. Defaults: eligible `US`, destination `JP`, product `MWE`.

---

### `findacard` — Find A Card

| | |
|---|---|
| **File** | `usecases/findacard.py` |
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

Front-end-only showcase of Mastercard's sonic identity: acceptance sound, jingle, app UI micro-sounds, and regional variants. Sounds are synthesised in the browser using the Web Audio API. The full UI lives in the self-contained `usecases/sonicbrand/index.html` page, rendered via an iframe with a refresh button. Actual licensed assets must be sourced from Mastercard Brand Centre.

---

### `testchat` — Test Chat

| | |
|---|---|
| **Files** | `usecases/testchat/__init__.py`, `usecases/testchat/testchat.html` |
| **APIs used** | *(none)* |
| **Render key** | `testchat` |
| **Static route** | `GET /testchat/<filename>` → served from `usecases/testchat/` |

Prototype chat interface with a canvas-based revolving Mastercard globe (Fibonacci lattice, no external deps). Features Refresh and Edit buttons; Edit opens the in-process Vima Chat modal (mounted at `/chat/simple`). The page is self-contained in `testchat.html`.

---

## Environment variables summary

| Variable | API | Description |
|---|---|---|
| `PARTNER_ID` | ofin | Finicity partner ID |
| `PARTNER_SECRET` | ofin | Finicity partner secret |
| `APP_KEY` | ofin | Finicity app key |
| `API_BASE_URL` | ofin | Finicity base URL (default: `https://api.finicity.com`) |
| `BINLOOKUP_CONSUMER_KEY` | binlookup | OAuth consumer key |
| `BINLOOKUP_SIGNING_KEY_PATH` | binlookup | Path to `.p12` / `.pem` signing key |
| `CLARITY_CONSUMER_KEY` | clarity | OAuth consumer key |
| `CLARITY_SIGNING_KEY_PATH` | clarity | Path to signing key |
| `PRICELESS_CONSUMER_KEY` | priceless | OAuth consumer key |
| `PRICELESS_SIGNING_KEY_PATH` | priceless | Path to signing key |
| `PRICELESS_ENV` | priceless | `sandbox` (default) or `production` |
| `EASYSAVINGS_CONSUMER_KEY` | easysavings | OAuth consumer key |
| `EASYSAVINGS_SIGNING_KEY_PATH` | easysavings | Path to signing key |
| `PLACES_CONSUMER_KEY` | places | OAuth consumer key |
| `PLACES_SIGNING_KEY_PATH` | places | Path to signing key |
| `OFPUB_CONSUMER_KEY` | ofpub | OAuth consumer key |
| `OFPUB_SIGNING_KEY_PATH` | ofpub | Path to signing key |
| `OFMC_CONSUMER_KEY` | ofmc | OAuth consumer key |
| `OFMC_SIGNING_KEY_PATH` | ofmc | Path to signing key |
| `CONSENT_CONSUMER_KEY` | consent | OAuth consumer key |
| `CONSENT_SIGNING_KEY_PATH` | consent | Path to signing key |
| `TXNOTIFY_CONSUMER_KEY` | txnotify | OAuth consumer key |
| `TXNOTIFY_SIGNING_KEY_PATH` | txnotify | Path to signing key |
| `ELIGIBILITY_CONSUMER_KEY` | eligibility | OAuth consumer key |
| `ELIGIBILITY_SIGNING_KEY_PATH` | eligibility | Path to signing key |
| `ELIGIBILITY_ENV` | eligibility | `sandbox` (default) or `production` |
| `BCES_CONSUMER_KEY` | bces | OAuth consumer key |
| `BCES_SIGNING_KEY_PATH` | bces | Path to signing key |
| `BCES_ENV` | bces | `sandbox` (default) or `production` |

---

## Key cross-cutting files

| File | Purpose |
|---|---|
| `app.py` | Flask routes; `GET /catalog` returns unified JSON of all APIs + use cases |
| `apis/registry.py` | Import and order all API modules; edit to add/remove APIs |
| `usecases/registry.py` | `USE_CASE_MODULES` list; edit to add/remove use cases |
| `static/js/app.js` | Entire SPA: API call UI, use case renderers, BIN batch search, modal, globe |
| `static/css/styles.css` | All styles including use-case-specific rules (`.tc-*`, `.bin-*`, etc.) |
| `templates/index.html` | Main HTML shell |
