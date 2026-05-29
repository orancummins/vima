# API Onboarding Checklist — Business Payment Controls

## Metadata

- API id: `business_payment_controls`
- Display name: Business Payment Controls
- Docs URL: https://developer.mastercard.com/business-payment-controls/documentation/
- API reference: https://developer.mastercard.com/business-payment-controls/documentation/api-reference/
- Portal slug: `business-payment-controls`
- Auth type: `oauth1` (standard OAuth 1.0a; payload encryption is optional per project)
- Catalog group: `GROUP_SECURITY` ("Security & Risk")
- Status: **Auto-provisionable wiring in place; playbook RECORDED & re-authored; Phase 2 BLOCKED only on a real registration token**
- Date: 2026-05-29
- Implementer: Autonomous agent (Copilot / Claude Opus 4.7)

## Intake

- [x] API product page and docs URL confirmed.
- [x] Auth model confirmed — OAuth 1.0a standard. Payload encryption (JWE) optional per the [Payload Encryption FAQ](https://developer.mastercard.com/business-payment-controls/documentation/support/#payload-encryption); not enabled by default.
- [x] Portal slug confirmed: `business-payment-controls`.
- [x] Provisioning behaviour: portal wizard with one extra free-text *registration token* field on Step 2, otherwise the standard create-project flow.

Notes:
- Sandbox project creation gated behind a **registration token** issued by a Mastercard Commercial Products implementation manager.
- Caller must already have, or be set up with, a Mastercard Commercial Identity (ICCP or In Control API customer).
- Contact: phone `+1-800-288-3381` (US) / `+1-636-722-6636` (intl), Option 4. Email: `commercial.support@mastercard.com`.

## Phase 1 — existence check ✅ PASS

- [x] `apis/business_payment_controls/api.py` — MANIFEST + `execute()` stub (returns `not_configured` until a real consumer key + key file are provisioned).
- [x] `apis/catalog.py` — `ApiCatalogEntry` present, `group=GROUP_SECURITY`, `auto_provisionable=True`, `provision_note` set.
- [x] **NOT in `DISABLED_API_IDS`** (the prior version of this checklist was wrong; this session promoted BPC to auto-provisionable).
- [x] `simulator/handlers/business_payment_controls.py` — 7 routes (entities, real cards, virtual cards, funding sources, authorization reports).
- [x] `simulator/fixtures/business_payment_controls.json` — one entity / one RCN / one VCN / one funding source / one auth report.
- [x] `tools/mcd-key-automation/providers/mastercard/api_config.py` — `_SPECIAL_BY_ID["business_payment_controls"] = {"provision_type": "playbook"}`.
- [x] `tools/mcd-key-automation/playbooks/mastercard/business-payment-controls.json` — **RECORDED 2026-05-29 14:19 from a live wizard session (project `testbizpaycontrols2`), then hand-edited to re-insert `wait_for_proceed_enabled` / `click_proceed` / `os_click` / `expect_download` / `wait_for_url_contains` steps that the recorder dropped.** 26 steps, 7 variables (`project_name, alias, key_password, contact_email, registration_token, encryption_alias, encryption_password`), defaults for `registration_token=123456789`, `encryption_alias={{alias}}-enc`, `encryption_password={{key_password}}`. **Verified selectors observed live**: `input[data-testid='project-name']`, `input[data-testid='regtoken-text']` (NOT `registrationtoken-text` as previously guessed), `input[data-testid='key-alias-input']`, `input[data-testid='key-store-password-input']`, `input[data-testid='business-payment-controls-mastercard-encryption-key-alias-input']`, `input[data-testid='business-payment-controls-mastercard-encryption-key-store-password-input']`, `button[data-testid='download-key-action-project-creation']`, `button[data-testid='proceed-button-create-new-project']`.
- [x] `docs/agent-onboarding/api-onboarding-spec.yaml` row appended.

## Phase 1a — Test Data Kit harvested from Mastercard Developers ✅ DONE

- **Try-It panel / API reference:** https://developer.mastercard.com/business-payment-controls/documentation/api-reference/
- **Sandbox tutorial:** https://developer.mastercard.com/business-payment-controls/documentation/tutorial/tutorial-1/
- **Reference application (Java):** https://developer.mastercard.com/business-payment-controls/documentation/reference-app/
- **Sample request / response:** Per-tenant. Mastercard does **not** publish shared sandbox PANs / GUIDs for BPC the way they do for BIN Lookup, BCES, Eligibility, etc. `ownerGUID` / `entityGUID` and funding-source GUIDs are minted at registration.
- **Sandbox base URL:** `https://sandbox.api.mastercard.com/business-payment-controls`
- **Production base URL:** `https://api.mastercard.com/business-payment-controls`
- **Rate limit:** 600 RPS (Sandbox & Production).
- **Auth model:** OAuth 1.0a one-legged, body-signed. Optional Mastercard payload encryption (JWE) per project.
- **Idempotency:** all endpoints honour `Idempotency-Key` header (v4 UUID, 30-second window).
- **Entitlement gates:** Issuer / corporate customer / payment agent only. Must be onboarded by Mastercard Commercial Products team.

## Phase 1b — pre-flight checks ✅ PASS

| # | Check | Result |
|---|---|---|
| 1 | `py tools\validate_api_contract.py` | **PASS** — 21 catalog APIs, 19 manifest APIs, 19 provision-catalog APIs, onboarding spec/schema valid |
| 2 | Catalog entry loads, group + env_prefix correct, no prefix collisions | **PASS** — `group=Security & Risk`, `env_prefix=BUSINESS_PAYMENT_CONTROLS` (unique) |
| 3 | `api_config.py` mapping — matching `api_name`, correct `portal_slug`, `provision_type=playbook` matches existing JSON | **PASS** |
| 4 | JWE wiring (optional, off by default for BPC) | **N/A** — JWE not required for this project |
| 5 | Portal credentials in `config/.env` | **N/A via env** — `config/.env` has no `MCD_PORTAL_*` keys, but `tools/mcd-key-automation/session_state.json` is fresh (rewritten 14:58 today, ~17 min before this run) so login works via cached cookies |

## Phase 2 — provisioning smoke ⚠️ PARTIAL

Recording session (2026-05-29 14:19) succeeded end-to-end: project `testbizpaycontrols2` was created on the live portal using the placeholder token `123456789` (the portal *did* accept it for the wizard — either the token is genuinely valid for sandbox testing, or the token gate is enforced server-side after project creation when the API is actually called). All selectors were captured and verified against the live DOM; the wizard fully completed (key downloaded, project created, project-details page reached).

### Headless replay status

Not yet smoke-tested end-to-end. The hand-authored playbook should now replay headlessly, but the user opted to stop after the recording session.

### Recorder fix shipped this session

The recorder's click-event capture was upgraded so future re-recordings on this portal style won't lose Proceed-button clicks:

- `tools/mcd-key-automation/app/playbook_record.py` — `describe()` now promotes a clicked `<span>` / `<i>` / `<svg>` to its enclosing `<button>` / `<a>` via `el.closest('button, a')`, so `data-testid='proceed-btn'` is captured on the outer button. (Prior behaviour: BPC's Proceed-text-on-span buttons produced clicks with empty `testid`, and the consolidator's `_is_proceed()` dropped them; resulting playbook had no `click_proceed` steps between form sections.)

### Required to fully unblock Phase 2

- [ ] **Obtain a real BPC registration token** (or confirm `123456789` is the documented sandbox value). Replace `defaults.registration_token` in the playbook if needed.
- [ ] Smoke-test the headless replay: `.\addapi.bat https://developer.mastercard.com/business-payment-controls/documentation/`. If a step fails, the strategy learner will write `tools/mcd-key-automation/output/failures/business_payment_controls-*.json` pointing at the exact selector miss.
- [ ] On success, confirm `config/.env.generated` and `config/keys/business_payment_controls.p12` exist, then `type config\.env.generated >> config\.env`.

## Phase 3 — live sandbox call ❌ BLOCKED (transitive)

Blocked by Phase 2. Additionally:

- [ ] `apis/business_payment_controls/api.py:execute()` is currently a **stub** that returns `{"ok": False, "error": "not_configured"}`. Once Phase 2 produces real credentials, replace the stub with an OAuth 1.0a signing call against `GET {SANDBOX_BASE}/entities/user-entity` (the entry point harvested in Phase 1a). Use `apis/bin_lookup/api.py` as the reference implementation: `oauth1.authenticationutils.load_signing_key()` + `oauth1.oauth.OAuth.get_authorization_header()`.
- [ ] After wiring `execute()`, run:
  ```
  cd tools\mcd-key-automation
  .venv\Scripts\python.exe -m app.main test-api https://developer.mastercard.com/business-payment-controls/documentation/
  ```
  Output MUST include `✅ PASS` and `status=200`. If not, iterate per the autonomous-onboarding doc's Phase 3 loop.

## Phase 3a — `how_to` quality bar ✅ PASS (against current scope)

- [x] One-sentence summary of what the API does.
- [x] Numbered onboarding steps naming the contact paths (phone, email, registration-token flow).
- [x] "How it works" enumeration of the four microservices.
- [x] "Operation groups" enumeration from the API reference.
- [x] Authentication notes (OAuth 1.0a + optional JWE).
- [x] Idempotency note.
- [x] "Test data & references" section with **6 explicit links** (overview, API reference, sandbox tutorial, reference app, use cases, API status).
- [x] Italicised note about per-tenant GUIDs (no shared sandbox values).

Will need to be revisited once Phase 3 produces a real `ownerGUID` + sandbox funding-source GUID — those values should be embedded in the operation `params[].default` fields so the UI's *Try It* button works out of the box.

## Simulator parity (manual verification once Flask is running)

```
curl -X GET   http://localhost:9021/api-sim/business_payment_controls/entities/user-entity
curl -X POST  http://localhost:9021/api-sim/business_payment_controls/real-card-accounts -H 'Content-Type: application/json' -d '{"ownerGuid":"11111111-1111-1111-1111-111111111111","cardNumber":"5111111111110042","expirationMonth":"12","expirationYear":"2030"}'
curl -X POST  http://localhost:9021/api-sim/business_payment_controls/virtual-card-accounts -H 'Content-Type: application/json' -d '{"fundingSourceGuid":"44444444-4444-4444-4444-444444444444","validityMonths":12,"spendLimit":100000}'
curl -X POST  http://localhost:9021/api-sim/business_payment_controls/authorization-reports -H 'Content-Type: application/json' -d '{"fromDate":"2026-01-01","toDate":"2026-01-31"}'
```

## Final gate

**Not achievable in this run.** Two human-gated inputs are required and the user has explicitly opted to stop here:

1. A real Mastercard-issued BPC registration token.
2. One interactive `addapi.bat --record` session to capture the live wizard selectors.

When both are available, follow the Phase 2 / Phase 3 unblock steps above and update this checklist's status line.

## Files changed (this onboarding pass — uncommitted)

- `apis/catalog.py` — added BPC `ApiCatalogEntry` (`group=GROUP_SECURITY`, `auto_provisionable=True`, `provision_note` set). **Not** in `DISABLED_API_IDS`.
- `apis/business_payment_controls/__init__.py` — new.
- `apis/business_payment_controls/api.py` — new (MANIFEST + stub `execute()`).
- `simulator/handlers/business_payment_controls.py` — new (7 routes).
- `simulator/fixtures/business_payment_controls.json` — new.
- `docs/agent-onboarding/api-onboarding-spec.yaml` — appended one row.
- `tools/mcd-key-automation/providers/mastercard/api_config.py` — added `"business_payment_controls": {"provision_type": "playbook"}` to `_SPECIAL_BY_ID`.
- `tools/mcd-key-automation/playbooks/mastercard/business-payment-controls.json` — **recorded live (2026-05-29 14:19, project `testbizpaycontrols2`) then hand-edited** to re-insert dropped proceed/download/final-click steps (26 steps, 7 variables).
- `tools/mcd-key-automation/app/playbook_record.py` — recorder `describe()` now climbs from clicked `<span>`/`<i>`/`<svg>` to enclosing `<button>`/`<a>` so wrapping-button `data-testid` (e.g. `proceed-btn`) is captured on portals that use text-on-span buttons.
- `addapi.bat` — added `--record` flag (was missing in the no-exe refactor); fixed `for /f` slug-extraction to use token 3 (URLs have empty token 2 from `//`); used quoted-set form for flag vars so trailing spaces don't break `if` checks.
- `docs/agent-onboarding/checklists/business_payment_controls-onboarding-checklist.md` — this file.

## Smoke commands

Contract validation (always runs clean):
```
py tools\validate_api_contract.py
```

Once a registration token is in hand and the playbook is re-recorded:
```
addapi.bat --record https://developer.mastercard.com/business-payment-controls/documentation/
addapi.bat        https://developer.mastercard.com/business-payment-controls/documentation/
cd tools\mcd-key-automation
.venv\Scripts\python.exe -m app.main test-api https://developer.mastercard.com/business-payment-controls/documentation/
```
