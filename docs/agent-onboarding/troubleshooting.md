# Troubleshooting

## Symptom-to-Cause Index

- API missing in provision modal: `/provision/catalog` mismatch or frontend fetch failure.
- API fails contract validation: catalog/spec/provision mapping drift.
- Unauthorized after provisioning: activation delay or wrong key artifacts imported.
- Missing consumer key artifact: sandbox key row not yet visible or wrong flow path.
- 400 with valid credentials and `MISSING_REQUIRED_INPUT`: request parameter name/casing mismatch.
- 400 with valid credentials and `INVALID_INPUT_VALUE`: field format mismatch (for example country code length/standard).
- 200 with valid credentials but empty/non-useful payload: input values do not match official sandbox dataset.
- 503 with HTML edge page (for example Akamai/edgesuite reference): wrong base URL or missing service namespace path.

## Portal Drift Signals

- Step labels changed.
- Buttons renamed or moved.
- Wizard jumps directly to project page.

## Selector Breakage Response

1. Capture screenshot and current URL.
2. Record failing selector and page state.
3. Update selector source in provider page objects.
4. Re-run dry-run and full provisioning checks.

## Credential Import Failures

1. Verify zip layout includes `config/.env` and `config/keys/*`.
2. Verify key file extensions are supported.
3. Re-run export/import path and inspect logs for parse errors.

## Unauthorized After Provisioning

1. Wait 2-3 minutes and retry operation.
2. Confirm environment variables point to imported key files.
3. Confirm manifest `configured` flag is true.
4. Confirm sandbox vs production env values are correct.

## 503 HTML Edge Error (Akamai/edgesuite)

1. Check whether the response is HTML with an edge reference ID rather than JSON API error payload.
2. Re-read API spec server definition and capture canonical base URL:
- OpenAPI: `servers[*].url`
- Swagger: `host` + `basePath`
3. Confirm runtime URL includes service namespace segment (for example `/abu/accounts/...`).
4. Re-test the same operation with corrected URL before changing credentials or waiting for activation.
5. Only classify as potential activation/service availability delay after URL shape is verified against spec.

## Request Contract Mismatch

1. Inspect upstream error payload `Source` fields and compare against outbound keys.
2. Align outbound request keys to canonical API reference names exactly.
3. Verify singular vs plural parameter naming and required companion fields.
4. Re-test with documented sample values and required format constraints.
5. Only revisit auth/provisioning after request contract is confirmed correct.

## 200 But No Useful Data

1. Verify whether docs provide sandbox test data (sheet/table/examples) and use those values exactly.
2. Confirm parameter value format (spacing, punctuation, country code standard, length).
3. Re-run with at least 3 known-good samples from the official dataset.
4. Update operation defaults in `MANIFEST` to known-good sandbox values.
5. If still empty with official samples, capture request/response pair and escalate as potential sandbox data drift.

## Rollback and Retry Procedure

1. Purge existing config (`/config/purge` endpoint path in app).
2. Re-run provisioning for selected APIs.
3. Re-import generated config bundle.
4. Re-run contract validation and smoke checks.

## Escalation Threshold

Escalate after 3 failed retries with evidence attached:

- command output
- screenshot path
- failing API id and workflow type
