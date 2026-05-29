# Enhanced Currency Conversion Calculator — Onboarding Checklist

## Metadata

- API id: `enhanced_currency_conversion_calculator`
- Display name: Enhanced Currency Conversion Calculator
- Docs URL: https://developer.mastercard.com/enhanced-currency-conversion-calculator/documentation/
- Portal slug: `enhanced-currency-conversion-calculator`
- Auth type: `oauth1` (OAuth 1.0a standard, no encryption key)
- PR link: _(pending)_
- Date: 2026-05-28
- Implementer: autonomous-api-onboarding agent run

## Intake

- [x] API product page and docs URL confirmed.
- [x] Auth model confirmed (`oauth1`).
- [x] Portal slug confirmed (`enhanced-currency-conversion-calculator`).
- [x] Provisioning behavior identified (Add Project + standard OAuth1 key flow — **but see Blockers**).

Evidence:
- Notes: EEA-issuer-restricted product. Catalog `provision_note` flagged a quarterly portal subscription; the portal still permits Add Project / key issuance for this API, but the resulting consumer key is not entitled at the gateway.

## Discovery

- [x] `api-onboarding-spec.yaml` row added.
- [x] Baseline validator run completed.

Evidence:
- Validator command: `./.venv/bin/python tools/validate_api_contract.py`
- Validator result: `PASSED — Catalog APIs: 16, Manifest APIs: 16, Provision catalog APIs: 16`

## Catalog Registration

- [x] Entry added in [apis/catalog.py](apis/catalog.py).
- [x] `id`, `env_prefix`, `portal_slug`, `docs_url`, `auth` verified.

Evidence:
- `ApiCatalogEntry(id="enhanced_currency_conversion_calculator", env_prefix="ENHANCED_CURRENCY_CONVERSION_CALCULATOR", portal_slug="enhanced-currency-conversion-calculator", display_name="Enhanced Currency Conversion Calculator", auth=AUTH_OAUTH1, categories=("FX", "Settlement"), docs_url=…, provision_note="EEA issuers only; quarterly subscription on the portal")`

## Module Implementation

- [x] [apis/enhanced_currency_conversion_calculator/api.py](apis/enhanced_currency_conversion_calculator/api.py) added.
- [x] `MANIFEST` includes `docs_url` and `how_to`.
- [x] `execute()` implemented for all 4 ops.
- [x] `is_configured()` honored — returns guard error when env vars unset.

Evidence:
- Module files: [apis/enhanced_currency_conversion_calculator/__init__.py](apis/enhanced_currency_conversion_calculator/__init__.py), [apis/enhanced_currency_conversion_calculator/api.py](apis/enhanced_currency_conversion_calculator/api.py)

## Request-Contract Verification

| Operation ID | Method | Endpoint Path | Canonical Fields | Required Companions | Format Constraints | Verified (Y/N) |
| --- | --- | --- | --- | --- | --- | --- |
| summary_rate | GET | /summary-rates | fxDate, transCurr, crdhldBillCurr, transAmt | all 4 | fxDate ISO `YYYY-MM-DD`; amount decimal | Y (contract); N (live — gateway 404, see Blockers) |
| rate_status | GET | /rate-statuses | fxDate | — | fxDate ISO | Y / N (live) |
| list_mc_currencies | GET | /mc-currencies | — | — | — | Y / N (live) |
| list_ecb_currencies | GET | /ecb-currencies | — | — | — | Y / N (live) |

- [x] `MANIFEST.operations[*].params[*].name` matches canonical fields (camelCase passthrough).
- [x] Outbound query strings match canonical fields.
- [ ] At least one live probe run per operation succeeded — **blocked at gateway entitlement layer** (see Blockers).
- [x] 404s analyzed: traced to gateway-side entitlement, not request-contract mismatch (X-MC-Correlation-ID returned, no `MISSING_REQUIRED_INPUT`).

Evidence:
- Sample request URL: `GET https://sandbox.api.mastercard.com/enhanced/settlement/currencyrate/mc-currencies`
- Upstream error payload: `{"Errors":{"Error":[{"Recoverable":false,"Source":"Gateway","ReasonCode":"NOT_FOUND","Description":"Not Found"}]}}`
- Correlation ID observed: `0.c63e1202.1779961183.8c33327b`

## Endpoint Base URL Verification

- [x] Canonical sandbox base URL captured from `API Host` block in [API Reference](https://developer.mastercard.com/enhanced-currency-conversion-calculator/documentation/api-reference/).
- [x] Production base URL: `https://api.mastercard.com/enhanced/settlement/currencyrate` (sandbox swap).
- [x] Runtime request URLs assemble as base + path with no inferred prefixes.
- [x] Live request URL captured and includes documented service namespace.
- [x] Gateway 404 triaged as entitlement (not edge/CDN) — response is a structured JSON error with `Source: Gateway` and an `X-MC-Correlation-ID` header.

Evidence:
- Spec source: developer portal API Reference page, `## API Host` section.
- Sandbox base URL: `https://sandbox.api.mastercard.com/enhanced/settlement/currencyrate`
- Production base URL: `https://api.mastercard.com/enhanced/settlement/currencyrate`

## Sandbox Data Readiness

- [x] Official sandbox test data source identified (interactive `Try It` panel + OpenAPI examples on docs page).
- [x] Sample values captured for `summary_rate`: `fxDate=0000-00-00`, `transCurr=USD`, `crdhldBillCurr=EUR`, `transAmt=100`.
- [x] `MANIFEST` defaults set to known-good sandbox samples (also `2024-06-01` fallback for past-date probes).
- [x] `MANIFEST.how_to` links to docs and lists per-operation samples.
- [ ] Non-empty live response confirmed — **not achievable: gateway returns NOT_FOUND for unsubscribed key**.

Evidence:
- Sandbox data source: docs API Reference `Try It` panel.
- Non-empty response proof: **N/A under current key entitlement**.

## Simulator Wiring

- [x] [simulator/handlers/enhanced_currency_conversion_calculator.py](simulator/handlers/enhanced_currency_conversion_calculator.py) added.
- [x] [simulator/fixtures/enhanced_currency_conversion_calculator.json](simulator/fixtures/enhanced_currency_conversion_calculator.json) added (7 currency pairs, 9 MC currencies, 11 ECB currencies).
- [x] Simulator operation smoke passed.

Evidence:
- All 4 ops return 200 against `/api-sim/enhanced_currency_conversion_calculator/*` with `SIMULATED_SANDBOX=1` (Flask on :9021).

## Provisioning Wiring

- [x] API mapped in [tools/mcd-key-automation/providers/mastercard/api_config.py](tools/mcd-key-automation/providers/mastercard/api_config.py) — inherits default `oauth1_standard` driver (no override needed).
- [x] `provision_type: oauth1_standard` registered in [api-onboarding-spec.yaml](docs/agent-onboarding/api-onboarding-spec.yaml).
- [x] Provisioning smoke path completed end-to-end:
  - Project created, API attached, signing key issued, key zip downloaded.
  - `.p12` extracted, copied to [config/keys/enhanced_currency_conversion_calculator.p12](config/keys/enhanced_currency_conversion_calculator.p12).
  - `config/.env.generated` populated with `ENHANCED_CURRENCY_CONVERSION_CALCULATOR_*` env vars and appended to `config/.env`.

Evidence:
- Orchestrator log: `Provisioned 'enhanced_currency_conversion_calculator' ✓`
- Two pre-existing bugs fixed during this run:
  1. Portal validation: project names > 50 chars rejected. Patched [tools/mcd-key-automation/providers/mastercard/workflows/project_workflow.py](tools/mcd-key-automation/providers/mastercard/workflows/project_workflow.py) to truncate the slug portion when `SS-<slug>-<ts>` exceeds 50 chars.
  2. Artifact resolver: `_find_artifact` in [tools/mcd-key-automation/app/main.py](tools/mcd-key-automation/app/main.py) only matched raw `.p12` files but the portal delivers the key inside a `.zip`. Added a fallback that extracts the `.p12` member from a matching zip on demand so `provision-api` can wire the env vars and copy the key.
- Stale 6-step playbook quarantined: `tools/mcd-key-automation/playbooks/mastercard/enhanced-currency-conversion-calculator.json.broken-partial`.

## UI Wiring

- [ ] API appears in APIs tab — _not yet verified in this run._
- [ ] API appears in provisioning modal — _not yet verified in this run._
- [ ] Docs button and How To modal render — _not yet verified in this run._

Evidence:
- `/explorer/apis` check: pending.
- `/provision/catalog` check: pending.

## Testing

- [x] `tools/validate_api_contract.py` passes (16/16).
- [x] Simulator smoke passes (4/4 ops, 200 OK).
- [ ] Live smoke passes — **blocked**, gateway entitlement (see Blockers).
- [ ] Live smoke yields actionable data — **blocked**.

Evidence:
- Validator output: `PASSED - Catalog APIs: 16, Manifest APIs: 16, Provision catalog APIs: 16`
- Simulator smoke: all 4 ops return 200 with fixture data via `/api-sim/enhanced_currency_conversion_calculator/*`.
- Live probe (all 4 ops): `status=404 ReasonCode=NOT_FOUND Source=Gateway`.

## Final Gate

- [ ] Checklist is complete.
- [ ] Linked in PR description.
- [ ] No unresolved blockers — **NOT MET**: live entitlement blocker.

## Blockers / Follow-ups

- **Blocker:** Mastercard sandbox gateway returns `NOT_FOUND / Source=Gateway` for every ECCC operation when signed by the consumer key that auto-provisioning issued. The OAuth1 signature is accepted (no 401, `X-MC-Correlation-ID` header returned), but the gateway does not route the key to the ECCC backend. This matches the documented restriction: ECCC is a subscription-gated, EEA-issuer-only product. The "Add Project + select API" portal flow grants a project-scoped key but does not grant the quarterly product entitlement.
- **Attempted recovery:**
  1. Confirmed base URL and path against the published `API Host` block — exact match.
  2. Re-ran with several `fxDate` values (`0000-00-00`, `2024-06-01`) and with no params at all (`/mc-currencies`, `/ecb-currencies`). All four ops, including the no-param list ops, return identical Gateway NOT_FOUND. Rules out request-contract / sample-value issues.
  3. Verified consumer key + signing key load cleanly and signature header reaches the gateway (correlation ID observed).
- **Next action:**
  1. Request ECCC subscription entitlement on the sandbox project through the developer portal (manual step — quarterly approval cycle). Mastercard rep / partnerships contact required.
  2. Once entitled, re-run: `cd tools/mcd-key-automation && ./.venv/bin/python -m app.main test-api 'https://developer.mastercard.com/enhanced-currency-conversion-calculator/documentation/'` and flip the live-smoke checkboxes above.
  3. Verify UI wiring in the meantime — simulator path is fully functional, so the explorer, provision modal, and How To panels can be exercised end-to-end with `SIMULATED_SANDBOX=1`.

## Generic infrastructure fixes shipped during this run

These are not ECCC-specific and benefit every future onboarding:

- 50-char portal-name truncation in `project_workflow.py` (any API with a slug longer than ~33 chars previously failed at the Add Project form).
- `.p12`-from-`.zip` fallback in `_find_artifact` so the `provision-api` command can wire env vars for any standard OAuth1 product. Without this, every newly provisioned API since the portal switched to delivering keys inside a zip would have failed to populate `config/.env.generated`.
