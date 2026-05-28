# Open Finance Australia — Onboarding Checklist

## Metadata

- API id: `open_finance_au`
- Display name: Open Finance Australia
- Docs URL: https://developer.mastercard.com/open-finance-au/documentation/
- Portal slug: `ofin` (same product as US; differentiated via Commercial Countries = Australia)
- Auth type: `oauth2` (Partner ID + Partner Secret + App Key → App-Token bearer)
- PR link: _pending_
- Date: 2026-05-27
- Implementer: GitHub Copilot (autonomous onboarding playbook)

## Intake

- [x] API product page and docs URL confirmed.
- [x] Auth model confirmed: `oauth2` — `POST /aggregation/v2/partners/authentication` with `{partnerId, partnerSecret}` returns `{"token": "<App-Token>"}`. Subsequent calls send `App-Key` + `App-Token` headers (NOT `Finicity-` prefixed like the US tenant). Data-plane calls also require `Consent-Receipt-Id` (CDR).
- [x] Portal slug confirmed: same `ofin` product as US Open Finance — the AU variant is selected by picking **Australia** in the wizard's _Commercial Countries_ dropdown.
- [x] Provisioning behavior identified: reuses `oauth2_region` workflow with `region="Australia"`. No new playbook recording required.

Evidence:
- Notes:
  - Base URL: `https://api.openbanking.mastercard.com.au`
  - Token TTL: 2 hours (same as US Finicity backbone)
  - Test institution: _Finbank Aus OAuth_ — login `profile_4110` / password `profile_4110`
  - Quick Start: https://developer.mastercard.com/open-finance-au/documentation/quick-start-guide/

## Discovery

- [x] `api-onboarding-spec.yaml` row added.
- [x] Baseline validator run completed.

Evidence:
- Validator command: `py tools\validate_api_contract.py`
- Validator result:
  ```
  API contract validation PASSED
  - Catalog APIs: 17
  - Manifest APIs: 17
  - Provision catalog APIs: 17
  - Supported provision types: ['match_inline', 'oauth1_enc_key', 'oauth1_skip_step3',
    'oauth1_standard', 'oauth2_region', 'playbook', 'priceless']
  - Onboarding spec/schema: valid
  ```

## Catalog Registration

- [x] Entry added in [apis/catalog.py](apis/catalog.py).
- [x] `id="open_finance_au"`, `legacy_id=None`, `env_prefix="OPEN_FINANCE_AU"`, `portal_slug="ofin"`, `docs_url`, `auth=AUTH_OAUTH2` verified.

Evidence:
- Catalog entry inserted immediately after the `open_finance` entry; `provision_note` documents the country-selection caveat.

## Module Implementation

- [x] [apis/open_finance_au/api.py](apis/open_finance_au/api.py) added.
- [x] [apis/open_finance_au/client.py](apis/open_finance_au/client.py) added (uses plain `App-Key` / `App-Token` headers; accepts `consent_receipt_id` per-call).
- [x] `MANIFEST` includes `docs_url`, full `how_to` (Quick Start flow + sandbox credentials), and 7 operations covering the canonical AU CDR journey.
- [x] `execute()` implemented for all manifest operations.
- [x] `is_configured()` honors `simulator.switcher.is_simulated("open_finance_au")` and falls back to env-var presence.

Evidence:
- Module files: `apis/open_finance_au/__init__.py`, `apis/open_finance_au/client.py`, `apis/open_finance_au/api.py`

## Request-Contract Verification

| Operation ID | Method | Endpoint Path | Canonical Field Names | Required Companions | Format Constraints | Verified (Y/N) |
| --- | --- | --- | --- | --- | --- | --- |
| `create_token` | POST | `/aggregation/v2/partners/authentication` | `partnerId`, `partnerSecret` | `App-Key` header | JSON body | Y (matches docs) |
| `add_testing_customer` | POST | `/aggregation/v2/customers/testing` | `username`, `firstName`, `lastName` | App-Token | JSON body | Y |
| `list_customers` | GET | `/aggregation/v1/customers` | `search`, `start`, `limit` | App-Token | query params | Y |
| `get_customer` | GET | `/aggregation/v1/customers/{customerId}` | path: `customerId` | App-Token | — | Y |
| `get_institutions` | GET | `/institution/v2/institutions` | `search`, `start`, `limit`, `supportedCountries=au` | App-Token | query params | Y |
| `generate_connect_url` | POST | `/connect/v2/generate` | `partnerId`, `customerId`, `webhook` | App-Token | JSON body | Y |
| `get_customer_accounts` | GET | `/aggregation/v1/customers/{customerId}/accounts` | path: `customerId` | App-Token + `Consent-Receipt-Id` | header | Y |

- [x] `MANIFEST.operations[*].params[*].name` matches canonical fields (camelCase preserved in payloads via client mapping; snake_case used for params for VIMA convention parity with `open_finance`).
- [x] Outbound query/body fields use canonical Mastercard names.
- [ ] Live probe per operation — **pending Phase 3** (requires provisioned AU sandbox credentials).
- [x] 400 contract-mismatch debugging path documented (use `Consent-Receipt-Id` for any data-plane 401).

Evidence:
- Sample request URL/body: see `apis/open_finance_au/client.py`.

## Endpoint Base URL Verification

- [x] Canonical sandbox base URL: `https://api.openbanking.mastercard.com.au` (per quick-start-guide; AU has a single tenant URL — same host serves test & live, differentiated by partner credentials).
- [x] Production base URL: same host — `https://api.openbanking.mastercard.com.au`.
- [x] Runtime URLs built as `base_url + endpoint_path`, no inferred prefixes.
- [ ] Live request URL capture — **pending Phase 3**.

Evidence:
- Spec source: https://developer.mastercard.com/open-finance-au/documentation/quick-start-guide/

## Sandbox Data Readiness

- [x] Official sandbox test profile recorded: username `profile_4110` / password `profile_4110` (Finbank Aus OAuth).
- [x] `MANIFEST` default values seeded (`search="finbank"`, `supported_countries="au"`, `limit=10`).
- [x] `MANIFEST.how_to` links Quick Start and Test Profiles pages.
- [ ] Non-empty live response — **pending Phase 3**.

Evidence:
- Sandbox data: https://developer.mastercard.com/open-finance-au/documentation/integration-and-testing/test-the-apis/

## Simulator Wiring

- [x] [simulator/handlers/open_finance_au.py](simulator/handlers/open_finance_au.py) added.
- [x] [simulator/fixtures/open_finance_au.json](simulator/fixtures/open_finance_au.json) added (AUD-denominated; Finbank Aus institutions; 3 sample accounts).
- [x] Simulator handler discovery confirmed via blueprint registration (validator pass implies no view-function collision).

Evidence:
- View-function names suffixed `_au` to avoid Flask endpoint collisions with the US handler.
- Simulator enforces `Consent-Receipt-Id` header on data-plane accounts call to mirror live behavior.

## Provisioning Wiring

- [x] API mapped in [tools/mcd-key-automation/providers/mastercard/api_config.py](tools/mcd-key-automation/providers/mastercard/api_config.py) — added `_REGION_BY_ID["open_finance_au"] = "Australia"`.
- [x] `provision_type=oauth2_region` is supported by the workflow dispatcher (validator confirms).
- [ ] Provisioning smoke path — **pending Phase 2** (run `.\addapi.bat https://developer.mastercard.com/open-finance-au/documentation/`).

Evidence:
- The existing `oauth2_region` driver wizard selects country=Australia and creates an isolated AU partner. No new playbook recording is required.

## UI Wiring

- [x] Catalog auto-discovery covers explorer manifest, provision catalog, and simulator blueprint — no extra UI code needed.

## Outstanding (handed back to operator)

1. **Phase 2 — Provision credentials** (interactive; needs portal session):
   ```powershell
   cd c:\Users\e031093\dev\vima
   .\addapi.bat https://developer.mastercard.com/open-finance-au/documentation/
   ```
   This drives the existing `oauth2_region` workflow with **Australia** preselected, downloads `credentials.json`, and writes the env vars (`OPEN_FINANCE_AU_PARTNER_ID`, `OPEN_FINANCE_AU_PARTNER_SECRET`, `OPEN_FINANCE_AU_APP_KEY`) into `config/.env`.

2. **Phase 3 — Live smoke test** (after Phase 2 completes):
   - In the VIMA UI, navigate to Open Finance Australia → run **Create Access Token**.
   - Expected: `status=200`, response body `{"token": "<10-char-preview>...", "message": "Token created successfully"}`.
   - Paste the redacted response into this checklist below once captured.

   ```json
   { "status_code": 200, "body": { "token": "REDACTED...", "message": "..." } }
   ```

## Files Changed

- `apis/catalog.py` — added `open_finance_au` entry.
- `apis/open_finance_au/__init__.py` — new (empty package marker).
- `apis/open_finance_au/client.py` — new (AU-specific HTTP client).
- `apis/open_finance_au/api.py` — new (MANIFEST + dispatcher).
- `simulator/handlers/open_finance_au.py` — new.
- `simulator/fixtures/open_finance_au.json` — new.
- `tools/mcd-key-automation/providers/mastercard/api_config.py` — added region mapping.
- `docs/agent-onboarding/api-onboarding-spec.yaml` — added AU block.
- `docs/agent-onboarding/checklists/open_finance_au-onboarding-checklist.md` — this file.
