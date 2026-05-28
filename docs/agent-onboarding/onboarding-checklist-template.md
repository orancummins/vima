# API Onboarding Checklist Template

Copy this file to:
`docs/agent-onboarding/checklists/<api-id>-onboarding-checklist.md`

Keep all sections. Mark each checkbox and fill required evidence fields.

## Metadata

- API id:
- Display name:
- Docs URL:
- Portal slug:
- Auth type:
- PR link:
- Date:
- Implementer:

## Intake

- [ ] API product page and docs URL confirmed.
- [ ] Auth model confirmed (`oauth1`, `oauth1_enc`, or `oauth2`).
- [ ] Portal slug confirmed.
- [ ] Provisioning behavior identified.

Evidence:
- Notes:

## Discovery

- [ ] `api-onboarding-spec.yaml` row added/updated.
- [ ] Baseline validator run completed.

Evidence:
- Validator command:
- Validator result:

## Catalog Registration

- [ ] Entry added in `apis/catalog.py`.
- [ ] `id`, `legacy_id`, `env_prefix`, `portal_slug`, `docs_url`, `auth` verified.

Evidence:
- Catalog entry snippet/location:

## Module Implementation

- [ ] `apis/<id>/api.py` added.
- [ ] `MANIFEST` includes docs_url and how_to.
- [ ] `execute()` implemented for all selected operations.
- [ ] `get_state()` and `is_configured()` behavior verified.

Evidence:
- Module files changed:

## Request-Contract Verification

For each operation, capture exact request contract from Mastercard docs and confirm implementation matches.

| Operation ID | Method | Endpoint Path | Canonical Field Names | Required Companions | Format Constraints | Verified (Y/N) |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

- [ ] `MANIFEST.operations[*].params[*].name` matches canonical fields.
- [ ] Outbound query/body fields match canonical fields.
- [ ] At least one live probe run per operation (when credentials available).
- [ ] Any 400 `MISSING_REQUIRED_INPUT` / `INVALID_INPUT_VALUE` resolved as request-contract mismatch first.

Evidence:
- Sample request URL/body per operation:
- Upstream error payloads analyzed (if any):

## Endpoint Base URL Verification

- [ ] Canonical sandbox base URL captured from OpenAPI `servers` or Swagger `host` + `basePath`.
- [ ] Canonical production base URL captured from OpenAPI `servers` or Swagger `host` + `basePath`.
- [ ] Runtime request URLs are built as base URL + endpoint path (no inferred prefixes).
- [ ] At least one live request URL captured and confirmed to include the documented service namespace path.
- [ ] Any HTML 5xx edge/CDN response triaged as route/base-path issue before key-activation diagnosis.

Evidence:
- Spec source for base URLs:
- Sandbox base URL:
- Production base URL:
- Captured runtime URL(s):
- 5xx triage notes (if any):

## Sandbox Data Readiness

- [ ] Official sandbox test data source identified (URL recorded).
- [ ] At least 3 known-good sample values captured for key operations.
- [ ] `MANIFEST` default values set to known-good sandbox samples.
- [ ] `MANIFEST.how_to` includes linked sandbox source and operation-specific sample values.
- [ ] At least one live response confirmed non-empty/actionable using official sample data.

Evidence:
- Sandbox data source URL:
- Sample values by operation:
- How To link location:
- Non-empty response proof:

## Simulator Wiring

- [ ] `simulator/handlers/<id>.py` added.
- [ ] `simulator/fixtures/<id>.json` added.
- [ ] Simulator operation smoke passed.

Evidence:
- Simulator smoke command/output:

## Provisioning Wiring

- [ ] API mapped in `api_config.py`.
- [ ] `provision_type` supported in workflow.
- [ ] Provisioning smoke path completed (or explicitly N/A with reason).

Evidence:
- Provisioning notes/output:

## UI Wiring

- [ ] API appears in APIs tab.
- [ ] API appears in provisioning modal.
- [ ] Docs button and How To modal render.

Evidence:
- `/explorer/apis` check:
- `/provision/catalog` check:

## Testing

- [ ] `tools/validate_api_contract.py` passes.
- [ ] Simulator smoke passes.
- [ ] Live smoke passes when credentials are available.
- [ ] Live smoke includes official sandbox samples and yields actionable data.

Evidence:
- Validator output summary:
- Smoke output summary:

## Final Gate

- [ ] Checklist is complete.
- [ ] Linked in PR description.
- [ ] No unresolved blockers.

## Blockers / Follow-ups

- Blocker:
- Attempted recovery:
- Next action:
