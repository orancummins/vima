# API Onboarding Checklist

## Metadata

- API id: match
- Display name: MATCH Pro
- Docs URL: https://developer.mastercard.com/match/documentation/
- Portal slug: match
- Auth type: oauth1
- PR link: local workspace changes
- Date: 2026-05-28
- Implementer: GitHub Copilot

## Intake

- [x] API product page and docs URL confirmed.
- [x] Auth model confirmed (`oauth1`, `oauth1_enc`, or `oauth2`).
- [x] Portal slug confirmed.
- [x] Provisioning behavior identified.

Evidence:
- Notes: MATCH docs + swagger confirmed OAuth1 and /mcp/match/api bases. Standard oauth1 provisioning path applies.

## Discovery

- [x] `api-onboarding-spec.yaml` row added/updated.
- [x] Baseline validator run completed.

Evidence:
- Validator command: `./.venv/bin/python tools/validate_api_contract.py`
- Validator result: PASS (Catalog APIs 15, Manifest APIs 15, Provision catalog APIs 15)

## Catalog Registration

- [x] Entry added in `apis/catalog.py`.
- [x] `id`, `legacy_id`, `env_prefix`, `portal_slug`, `docs_url`, `auth` verified.

Evidence:
- Catalog entry snippet/location: `match` row in `apis/catalog.py`

## Module Implementation

- [x] `apis/<id>/api.py` added.
- [x] `MANIFEST` includes docs_url and how_to.
- [x] `execute()` implemented for all selected operations.
- [x] `get_state()` and `is_configured()` behavior verified.

Evidence:
- Module files changed: `apis/match/api.py`, `apis/match/__init__.py`

## Request-Contract Verification

| Operation ID | Method | Endpoint Path | Canonical Field Names | Required Companions | Format Constraints | Verified (Y/N) |
| --- | --- | --- | --- | --- | --- | --- |
| create_termination_inquiry | POST | /termination-inquiries | terminationInquiryRequest, acquirerId, merchant, principals | merchant.address + principal.address blocks | country alpha-3; numeric phone/acquirer constraints from spec | Y |
| get_inquiry_history | GET | /termination-inquiries/{inquiry_ref_num} | inquiry_ref_num, page_length, page_offset | inquiry_ref_num path parameter | page_length 1-100, page_offset non-negative | Y |
| get_contact_details | POST | /contact-details | contactRequest.acquirerId | contactRequest wrapper required | acquirerId numeric string | Y |
| get_countries | GET | /countries | n/a | none | n/a | Y |
| get_states | GET | /countries/{country_code}/states | country_code | path parameter required | country_code alpha-3 | Y |
| get_cities | GET | /countries/{country_code}/cities | country_code, state_code | country_code required | country_code alpha-3, state_code optional | Y |

- [x] `MANIFEST.operations[*].params[*].name` matches canonical fields.
- [x] Outbound query/body fields match canonical fields.
- [ ] At least one live probe run per operation (when credentials available).
- [x] Any 400 `MISSING_REQUIRED_INPUT` / `INVALID_INPUT_VALUE` resolved as request-contract mismatch first.

Evidence:
- Sample request URL/body per operation: implemented in `apis/match/api.py`.
- Upstream error payloads analyzed (if any): none yet in this implementation pass.

## Endpoint Base URL Verification

- [x] Canonical sandbox base URL captured from OpenAPI `servers` or Swagger `host` + `basePath`.
- [x] Canonical production base URL captured from OpenAPI `servers` or Swagger `host` + `basePath`.
- [x] Runtime request URLs are built as base URL + endpoint path (no inferred prefixes).
- [ ] At least one live request URL captured and confirmed to include the documented service namespace path.
- [x] Any HTML 5xx edge/CDN response triaged as route/base-path issue before key-activation diagnosis.

Evidence:
- Spec source for base URLs: `/match/swagger/match-pro.yaml` via MCP.
- Sandbox base URL: `https://sandbox.apiedge.mastercard.com/mcp/match/api`
- Production base URL: `https://apiedge.mastercard.com/mcp/match/api`
- Captured runtime URL(s): pending live run.
- 5xx triage notes (if any): none observed in this implementation pass.

## Sandbox Data Readiness

- [ ] Official sandbox test data source identified (URL recorded).
- [x] At least 3 known-good sample values captured for key operations.
- [x] `MANIFEST` default values set to known-good sandbox samples.
- [x] `MANIFEST.how_to` includes linked sandbox source and operation-specific sample values.
- [ ] At least one live response confirmed non-empty/actionable using official sample data.

Evidence:
- Sandbox data source URL: pending explicit MATCH sample-data page capture.
- Sample values by operation: ICA `1996`, country `USA`, state `MO`, merchant/principal sample profile defaults.
- How To link location: `MANIFEST.how_to` in `apis/match/api.py`.
- Non-empty response proof: pending live run.

## Simulator Wiring

- [x] `simulator/handlers/<id>.py` added.
- [x] `simulator/fixtures/<id>.json` added.
- [x] Simulator operation smoke passed.

Evidence:
- Simulator smoke command/output: PASS via Flask test client on `/api-sim/match/*` routes (countries, states, cities, create inquiry, inquiry history, contact details).

## Provisioning Wiring

- [x] API mapped in `api_config.py`.
- [x] `provision_type` supported in workflow.
- [ ] Provisioning smoke path completed (or explicitly N/A with reason).

Evidence:
- Provisioning notes/output: mapping is catalog-driven for oauth1_standard; smoke pending.

## UI Wiring

- [x] API appears in APIs tab.
- [x] API appears in provisioning modal.
- [x] Docs button and How To modal render.

Evidence:
- `/explorer/apis` check: contract validation confirmed catalog/manifest parity includes `match`.
- `/provision/catalog` check: contract validation confirmed provisioning catalog parity includes `match`.

## Testing

- [x] `tools/validate_api_contract.py` passes.
- [x] Simulator smoke passes.
- [ ] Live smoke passes when credentials are available.
- [ ] Live smoke includes official sandbox samples and yields actionable data.

Evidence:
- Validator output summary: PASS (`tools/validate_api_contract.py`).
- Smoke output summary: PASS via Flask `app.test_client()` against MATCH simulator routes.

## Final Gate

- [ ] Checklist is complete.
- [ ] Linked in PR description.
- [ ] No unresolved blockers.

## Blockers / Follow-ups

- Blocker: Live MATCH credentials and sandbox sample-data confirmation not yet executed in this pass.
- Attempted recovery: Implemented simulator coverage and canonical contract mapping for all selected operations.
- Next action: Run validator + simulator smoke + optional live smoke with provisioned keys.
