# New API Playbook

Use this checklist to onboard a new Mastercard Developers API end-to-end.

Operator shortcut: for one-file execution, start with [one-file-api-onboarding-instruction.md](one-file-api-onboarding-instruction.md) and pass only the API docs URL.

Evidence artifact: create and complete a copy of [onboarding-checklist-template.md](onboarding-checklist-template.md) at `docs/agent-onboarding/checklists/<api-id>-onboarding-checklist.md`.

## Intake Checklist

- API product page and docs URL confirmed.
- Auth model identified (`oauth1`, `oauth1_enc`, or `oauth2`).
- Portal slug confirmed.
- Expected provisioning behavior identified.

## Discovery

1. Add/update entry in [api-onboarding-spec.yaml](api-onboarding-spec.yaml).
2. Run contract validator baseline:

```bash
./.venv/bin/python tools/validate_api_contract.py
```

## Endpoint Base URL Verification (must do before writing request code)

1. Derive base URL from the API spec itself (OpenAPI `servers`, Swagger `host` + `basePath`), not from assumptions or copied examples.
2. Record the canonical sandbox and production base URLs in onboarding notes.
3. Build operation URLs by joining base URL + operation path from the spec.
4. Run a URL-shape proof call for at least one operation and capture the final outbound URL.
5. If response is CDN/edge HTML (for example edgesuite/Akamai reference page), treat as route/base-path mismatch first.
6. Only consider key activation delay after URL shape is confirmed correct.

## Catalog Registration

1. Add new entry in `apis/catalog.py`.
2. Ensure `id`, `legacy_id`, `env_prefix`, `portal_slug`, `docs_url`, `auth` are correct.

## Module Implementation

1. Create `apis/<id>/api.py`.
2. Implement `MANIFEST` with `docs_url` and `how_to`.
3. Implement `execute(op_id, params)` and optional `get_state`/`is_configured`.

## Request-Contract Verification (must do before smoke signoff)

1. Verify request parameter contract from API reference, not by inference:
- exact field names (snake_case vs camelCase)
- singular vs plural names
- required companion fields (for example tax ID + country code)
- strict value formats (for example country code length and ISO variant)
2. Reflect those exact names/formats in both places:
- `MANIFEST.operations[*].params[*].name`
- outbound request query/body field names in `execute` handlers
3. Run one live probe per operation and inspect the upstream error payload if non-2xx.
4. If upstream returns `MISSING_REQUIRED_INPUT` or `INVALID_INPUT_VALUE`, treat as contract mismatch first, not credential failure.
5. Keep backward-compatible aliases only as optional fallbacks (for prior UI state), but always send canonical fields to Mastercard.

## Sandbox Data Readiness (must do before first UX signoff)

1. Locate official sandbox test data in the developer docs (spreadsheet/table/examples) and record the source URL.
2. Select at least 3 known-good sample values per high-value operation (or the max available when fewer exist).
3. Use those known-good values as `MANIFEST` defaults for first-run success in the UI.
4. If live response is `200` but empty or non-actionable, treat this as input dataset mismatch first.
5. Re-run with official sandbox samples before changing auth, provisioning, or code structure.
6. Add a "Sandbox test values" subsection to `MANIFEST.how_to` with:
- link to official sandbox data source
- operation-specific sample values that are known to return actionable data

## Simulator Wiring

1. Add `simulator/handlers/<id>.py`.
2. Add `simulator/fixtures/<id>.json`.
3. Verify fallback behavior with no credentials.

## Provisioning Wiring

1. Ensure API is in `tools/mcd-key-automation/providers/mastercard/api_config.py`.
2. Ensure `provision_type` is supported by `project_workflow.py`.
3. Run provisioning smoke path (generate-new key flow).

## UI Wiring

1. Verify API appears in APIs tab.
2. Verify API appears in provision selection modal.
3. Verify Docs button and How To modal content render.
4. Verify How To modal includes the sandbox test-values link and examples when official test data exists.

## Testing

1. Run:

```bash
./.venv/bin/python tools/validate_api_contract.py
```

2. Execute API-specific smoke operation in simulator mode.
3. Execute API-specific smoke operation in live mode (when keys are present).
4. For each live smoke, record status + key response or error codes and confirm they map to expected request fields.
5. Include one smoke using official sandbox sample data and confirm response is non-empty/actionable.
6. Confirm live calls hit the documented service namespace path (for example `/abu/accounts/...` rather than root-domain path).

## Merge Criteria

- Contract validator passes.
- UI parity confirmed.
- Provisioning artifacts match expectations.
- Docs/spec updated in the same PR.
- Completed onboarding checklist artifact is included in the PR.
- Endpoint base URL proof is included (spec source + captured final request URL).
