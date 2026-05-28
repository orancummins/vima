# Open Finance Europe — Onboarding Checklist

## Metadata

- API id: `open_finance_eu`
- Display name: Open Finance Europe
- Docs URL: https://developer.mastercard.com/open-finance-data/documentation/
- Portal slug: `ofin-eu` (placeholder — manual onboarding, no self-serve wizard)
- Auth type: `oauth2` (client_credentials + RS256-signed JWT client assertion)
- PR link: _pending_
- Date: 2026-05-28
- Implementer: GitHub Copilot (autonomous onboarding playbook)

## Intake

- [x] API product page and docs URL confirmed.
- [x] Auth model confirmed: OAuth 2.0 `client_credentials` with a JWT client assertion (RS256, `aud=auth.mastercard.com`, `kid` = SHA-256 thumbprint of public cert body) → `Authorization: Bearer <token>` on subsequent calls.
- [x] Portal slug confirmed: **no portal wizard** — onboarding is manual (email `openbankingeu_support@mastercard.com` with a 4096-bit RSA public PEM to receive a sandbox `clientId`).
- [x] Provisioning behavior identified: `manual_onboarding` — separate path from the US/AU portal-wizard flow.

Evidence:
- Notes:
  - Auth host: `https://mtf.auth.openbanking.mastercard.eu` (MTF/Sandbox)
  - API host: `https://mtf.api.openbanking.mastercard.com` (MTF/Sandbox)
  - Token TTL: 1 hour
  - Cert generation: `openssl req -x509 -sha256 -nodes -newkey rsa:4096 -keyout private.key -days 730 -out public.pem`
  - Reference auth doc: https://developer.mastercard.com/open-finance-data/documentation/developer-support/api-basics/authentication/

## Discovery

- [x] `api-onboarding-spec.yaml` row added (provision_type=`manual_onboarding`, skip_step3=true, manual_approval_required=true).
- [x] Baseline validator run completed.

Evidence:
- Validator command: `py tools\validate_api_contract.py`
- Validator result: see Phase 1 validation log below.

## Catalog Registration

- [x] Entry added in [apis/catalog.py](apis/catalog.py).
- [x] `id="open_finance_eu"`, `legacy_id=None`, `env_prefix="OPEN_FINANCE_EU"`, `portal_slug="ofin-eu"`, `docs_url`, `auth=AUTH_OAUTH2` verified.

Evidence:
- Catalog entry inserted immediately after `open_finance_au`; `provision_note` documents the manual-onboarding command + email contact.

## Module Implementation

- [x] [apis/open_finance_eu/api.py](apis/open_finance_eu/api.py) added.
- [x] [apis/open_finance_eu/client.py](apis/open_finance_eu/client.py) added — JWT signing built on `cryptography` (no new dependency); kid = base64url(SHA-256(DER cert body)); token cache keyed on expiry.
- [x] `MANIFEST` includes `docs_url`, `how_to` (onboarding instructions + Quick Start), 12 operations across Auth/Providers/Consent/Accounts/Transactions/Balances/Insights, `state_schema`, and ui_hints on the managed-flow op.
- [x] `execute()` implemented for all manifest operations including the LOCAL `set_provider` op.
- [x] `is_configured()` honors `simulator.switcher.is_simulated("open_finance_eu")` and falls back to env-var presence.
- [x] `get_state()` returns curated subset for UI panel; `STATE` mutated via `_ok()` envelope.
- [x] `create_managed_flow` emits `hints.open_link` → orange "Launch Aiia Flow ↗" button in the explorer.

## Simulator

- [x] [simulator/handlers/open_finance_eu.py](simulator/handlers/open_finance_eu.py) registers routes under `/api-sim/open_finance_eu/...` (auto-discovered by `simulator/blueprint.py`).
- [x] [simulator/fixtures/open_finance_eu.json](simulator/fixtures/open_finance_eu.json) seeds 5 providers (DK/SE/DE/UK), 3 accounts, 4 transactions.
- [x] `/oauth2/token` simulator stub allows the JWT-signing flow to no-op locally for UI testing without real keys.
- [x] Simulated consent auto-progresses to `granted` on first `GET /consents/{id}` to make the Quick Start one-click in sim mode.

## Validation

- [x] `tools/validate_api_contract.py` PASSED.
- [x] Manifest loadable; `execute('set_provider', …)` works without credentials (LOCAL op).
- [ ] Live smoke test deferred — requires manual provisioning (clientId via email + locally-generated RSA keypair).

## Hand-off / Phase 2 prerequisites

To exercise live calls (Phase 2), the operator must:

1. **Generate keypair** locally:
   ```powershell
   openssl req -x509 -sha256 -nodes -newkey rsa:4096 `
     -keyout config\keys\ofin-eu-private.key `
     -days 730 -out config\keys\ofin-eu-public.pem
   ```
2. **Email** `openbankingeu_support@mastercard.com` requesting a sandbox `clientId`, attaching `ofin-eu-public.pem`.
3. **Populate** `config/.env`:
   ```
   OPEN_FINANCE_EU_CLIENT_ID=<value returned by onboarding officer>
   OPEN_FINANCE_EU_PRIVATE_KEY_PATH=config/keys/ofin-eu-private.key
   OPEN_FINANCE_EU_PUBLIC_CERT_PATH=config/keys/ofin-eu-public.pem
   ```
4. Run **Create Access Token** in the VIMA UI — a 200 with a bearer token confirms cert trust + clientId binding.
5. Continue to **Get Providers**, **Create Consent**, **Create Managed Flow** (opens the Aiia hosted bank-link UI), **Get Consent** (polls until `granted`), then **Get Accounts**.

Expected manual-onboarding turnaround: ~2 business days (`expected_activation_delay_minutes: 2880` in the YAML spec).
