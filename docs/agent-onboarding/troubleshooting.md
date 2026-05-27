# Troubleshooting

## Symptom-to-Cause Index

- API missing in provision modal: `/provision/catalog` mismatch or frontend fetch failure.
- API fails contract validation: catalog/spec/provision mapping drift.
- Unauthorized after provisioning: activation delay or wrong key artifacts imported.
- Missing consumer key artifact: sandbox key row not yet visible or wrong flow path.

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
