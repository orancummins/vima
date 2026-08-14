# Testing Matrix

## Test Levels

1. Contract validation.
2. UI wiring validation.
3. Provisioning validation.
4. Runtime operation validation.

## Auth Family Matrix

| Auth | Simulator | Live | Provisioning |
|---|---|---|---|
| oauth1 | required | required when keys available | required |
| oauth1_enc | required | required when keys available | required |
| oauth2 | required | required when keys available | required |

## Per-API Smoke Template

For each API:

1. Validate contract:

```bash
./.venv/bin/python tools/validate_api_contract.py
```

2. Confirm API appears in `/explorer/apis` output.
3. Confirm API appears in `/provision/catalog` output.
4. Execute one primary operation in simulator mode.
5. Execute one primary operation in live mode (if configured).

## Provisioning Verification

1. Run selected API provisioning.
2. Confirm expected artifacts exist.
3. Confirm config import succeeded.
4. Confirm `/provision/status` reports configured true (or explicit pending approval case).

## UI Verification

1. API visible in APIs sidebar.
2. How-to modal renders API-specific content.
3. Docs button points to Mastercard Developers docs URL.
4. Provision modal lists API and status card updates correctly.

## Regression Gate

A change fails the gate if any of these are true:

- Contract validator fails.
- API is in catalog but not in provision catalog.
- API is provisionable but missing workflow mapping.
- How-to or docs_url is empty in manifest.
