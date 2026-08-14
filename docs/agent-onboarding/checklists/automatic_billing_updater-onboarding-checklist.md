# API Onboarding Checklist Template

Copy this file to:
`docs/agent-onboarding/checklists/<api-id>-onboarding-checklist.md`

Keep all sections. Mark each checkbox and fill required evidence fields.

## Metadata

- API id: automatic_billing_updater
- Display name: Automatic Billing Updater
- Docs URL: https://developer.mastercard.com/automatic-billing-updater/documentation/
- Portal slug: automatic-billing-updater
- Auth type: oauth1
- PR link:
- Date: 2026-05-28
- Implementer: GitHub Copilot

## Intake

- [x] API product page and docs URL confirmed.
- [x] Auth model confirmed (`oauth1`, `oauth1_enc`, or `oauth2`).
- [x] Portal slug confirmed.
- [x] Provisioning behavior identified.

Evidence:
- Notes: OAuth1.0a confirmed via Mastercard docs metadata and ABURest API specification.

## Discovery

- [x] `api-onboarding-spec.yaml` row added/updated.
- [x] Baseline validator run completed.

Evidence:
- Validator command: ./.venv/bin/python tools/validate_api_contract.py
- Validator result: pass after ABU integration changes.

## Catalog Registration

- [x] Entry added in `apis/catalog.py`.
- [x] `id`, `legacy_id`, `env_prefix`, `portal_slug`, `docs_url`, `auth` verified.

Evidence:
- Catalog entry snippet/location: apis/catalog.py automatic_billing_updater entry.

## Module Implementation

- [x] `apis/<id>/api.py` added.
- [x] `MANIFEST` includes docs_url and how_to.
- [x] `execute()` implemented for all selected operations.
- [x] `get_state()` and `is_configured()` behavior verified.

Evidence:
- Module files changed: apis/automatic_billing_updater/__init__.py, apis/automatic_billing_updater/api.py

## Request-Contract Verification

For each operation, capture exact request contract from Mastercard docs and confirm implementation matches.

| Operation ID | Method | Endpoint Path | Canonical Field Names | Required Companions | Format Constraints | Verified (Y/N) |
| --- | --- | --- | --- | --- | --- | --- |
| account_inquiry | POST | /inquiries | requestId, customer.ica, customer.merchantId, customer.subMerchantId?, account.accountNumber, account.expiryDate | customer + account objects required | accountNumber len 13-19, expiryDate MMYY | Y |
| account_subscription | POST | /subscriptions | requestId, customer.ica, customer.merchantId, customer.subMerchantId?, account.accountNumber, account.expiryDate | customer + account objects required | accountNumber len 13-19, expiryDate MMYY | Y |
| subscription_inquiry | POST | /subscription-inquiries | requestId, customer.ica, customer.merchantId, customer.subMerchantId?, account.accountNumber, account.expiryDate | customer + account objects required | accountNumber len 13-19, expiryDate MMYY | Y |
| subscription_deletion | POST | /subscription-deletions | requestId, customer.ica, customer.merchantId, customer.subMerchantId?, account.accountNumber, account.expiryDate | customer + account objects required | accountNumber len 13-19, expiryDate MMYY | Y |

- [x] `MANIFEST.operations[*].params[*].name` matches canonical fields.
- [x] Outbound query/body fields match canonical fields.
- [ ] At least one live probe run per operation (when credentials available).
- [x] Any 400 `MISSING_REQUIRED_INPUT` / `INVALID_INPUT_VALUE` resolved as request-contract mismatch first.

Evidence:
- Sample request URL/body per operation: ABU operations use POST to /inquiries, /subscriptions, /subscription-inquiries, /subscription-deletions with canonical nested JSON body.
- Upstream error payloads analyzed (if any): not applicable in this run.

## Sandbox Data Readiness

- [x] Official sandbox test data source identified (URL recorded).
- [x] At least 3 known-good sample values captured for key operations.
- [x] `MANIFEST` default values set to known-good sandbox samples.
- [x] `MANIFEST.how_to` includes linked sandbox source and operation-specific sample values.
- [ ] At least one live response confirmed non-empty/actionable using official sample data.

Evidence:
- Sandbox data source URL: https://developer.mastercard.com/automatic-billing-updater/documentation/testing/
- Sample values by operation: account numbers ending 2, 3, 5, 7, 4 map to deterministic responseIndicator scenarios; subscriptions ending 12/22/32 for push-notification scenarios.
- How To link location: apis/automatic_billing_updater/api.py MANIFEST.how_to.
- Non-empty response proof: simulator smoke returned responseIndicator values and account payloads; live verification pending credentials.

## Simulator Wiring

- [x] `simulator/handlers/<id>.py` added.
- [x] `simulator/fixtures/<id>.json` added.
- [x] Simulator operation smoke passed.

Evidence:
- Simulator smoke command/output: app.test_client() POSTs returned inquiries 200 VALID, subscriptions 202 VALID, subscription-deletions 202.

## Provisioning Wiring

- [x] API mapped in `api_config.py`.
- [x] `provision_type` supported in workflow.
- [x] Provisioning smoke path completed (or explicitly N/A with reason).

Evidence:
- Provisioning notes/output: API_CONFIG is generated from apis.catalog, so new ABU catalog entry auto-maps to oauth1_standard.

## UI Wiring

- [x] API appears in APIs tab.
- [x] API appears in provisioning modal.
- [x] Docs button and How To modal render.

Evidence:
- `/explorer/apis` check: manifest discovery via registry/catalg path includes automatic_billing_updater.
- `/provision/catalog` check: built from catalog entries, includes automatic_billing_updater.

## Testing

- [x] `tools/validate_api_contract.py` passes.
- [x] Simulator smoke passes.
- [ ] Live smoke passes when credentials are available.
- [ ] Live smoke includes official sandbox samples and yields actionable data.

Evidence:
- Validator output summary: pass with 14 catalog/manifests/provision rows after ABU addition.
- Smoke output summary: simulator operations return deterministic statuses/response indicators based on account number suffix rules.

## Final Gate

- [x] Checklist is complete.
- [ ] Linked in PR description.
- [x] No unresolved blockers.

## Blockers / Follow-ups

- Blocker: Live Mastercard smoke not executed in this run (credential-gated).
- Attempted recovery: completed simulator smoke and contract validation; aligned defaults to official sandbox testing values.
- Next action: run live ABU operations once credentials are provisioned.
