# New API Playbook

Use this checklist to onboard a new Mastercard Developers API end-to-end.

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

## Catalog Registration

1. Add new entry in `apis/catalog.py`.
2. Ensure `id`, `legacy_id`, `env_prefix`, `portal_slug`, `docs_url`, `auth` are correct.

## Module Implementation

1. Create `apis/<id>/api.py`.
2. Implement `MANIFEST` with `docs_url` and `how_to`.
3. Implement `execute(op_id, params)` and optional `get_state`/`is_configured`.

## Simulator Wiring

1. Add `simulator/handlers/<id>.py`.
2. Add `simulator/fixtures/<id>.json`.
3. Verify fallback behavior with no credentials.

## Provisioning Wiring

1. Ensure API is in `tools/mcd-key-automation/providers/mastercard/api_config.py`.
2. Ensure `provision_type` is supported by `project_workflow.py`.
3. Run provisioning smoke path (reuse-existing or generate-new).

## UI Wiring

1. Verify API appears in APIs tab.
2. Verify API appears in provision selection modal.
3. Verify Docs button and How To modal content render.

## Testing

1. Run:

```bash
./.venv/bin/python tools/validate_api_contract.py
```

2. Execute API-specific smoke operation in simulator mode.
3. Execute API-specific smoke operation in live mode (when keys are present).

## Merge Criteria

- Contract validator passes.
- UI parity confirmed.
- Provisioning artifacts match expectations.
- Docs/spec updated in the same PR.
