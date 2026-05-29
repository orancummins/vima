# Autonomous API Onboarding

Single self-contained instruction for an agent (Copilot Chat, Claude, etc.)
to onboard a new Mastercard API into vima end-to-end.

## Trigger

Paste into the agent:

> Follow `docs/agent-onboarding/autonomous-api-onboarding.md` for `<DOCS_URL>`.

That's it. The agent reads this file and runs the three phases below.

---

## Instruction

You are onboarding a new Mastercard API into the vima repository. The docs URL
is provided by the user.

Work autonomously through the three phases below. You MAY open browser windows
or pause for the human at portal-login or captcha steps — that is expected and
fine. Do NOT stop just because a step needs a real browser. After each phase,
print a one-line status summary so the human can follow along.

### Phase 1 — Does the API already exist in vima?

1. Derive the canonical `api_name` (snake_case of the portal slug, e.g.
   `enhanced-currency-conversion-calculator` → `enhanced_currency_conversion_calculator`).
2. Check ALL of:
   - `apis/<api_name>/api.py` exists with a `MANIFEST` + `execute()`
   - `apis/catalog.py` has an `ApiCatalogEntry` for it
   - `simulator/handlers/<api_name>.py` exists
   - `simulator/fixtures/<api_name>.json` exists
   - `tools/mcd-key-automation/providers/mastercard/api_config.py` has a mapping
   - `docs/agent-onboarding/api-onboarding-spec.yaml` has an entry

   While checking, ALSO harvest from the docs URL (fetch it) the **Test Data
   Kit** — see §Phase 1a below. You will need this in Phase 3 even if the
   API already exists.
3. If every item above is present → log `API already integrated` and skip
   to Phase 3 (still run the end-to-end test). Otherwise continue with the
   full implementation per:
   - `docs/agent-onboarding/one-file-api-onboarding-instruction.md`
   - `docs/agent-onboarding/new-api-playbook.md`
   - `docs/agent-onboarding/ui-integration-contract.md`
   - `docs/agent-onboarding/provisioning-workflows.md`

   Add catalog entry, `apis/<api_name>/api.py`, simulator handler + fixture,
   provisioning mapping, and `api-onboarding-spec.yaml` row. Run
   `./.venv/bin/python tools/validate_api_contract.py` and fix anything
   it complains about before continuing.

### Phase 1a — Harvest the Test Data Kit from Mastercard Developers

Before writing any code, fetch the docs URL **and** its sibling pages and
record the following in a scratch note (you will paste links into the
`how_to` field and use the values in Phase 3):

- **Try-It panel URL** — the live console page (usually `…/documentation/api-reference/`
  or a `Try It` tab). Capture the deep link.
- **Sample request / response** — copy a known-good JSON body verbatim.
- **Sandbox test values** — test BINs, test PANs, test merchant IDs, test
  customer IDs, test account refs, test card tokens, etc. Mastercard
  publishes these under headings like *Test Data*, *Sample Data*,
  *Test Cases*, *Sandbox Reference Data*, or *Try It Values*. Pull every
  value you find — you will need several to demonstrate different response
  shapes.
- **Auth model** — OAuth 1.0a (signing key + consumer key), OAuth 1.0a + JWE
  (encryption client required), OAuth 2.0 (client_credentials), or a
  custom flow. Note the token URL if OAuth 2.0.
- **Sandbox base URL** vs production base URL.
- **Rate limits / entitlement gates** — note anything that says "requires
  approval", "contact your account manager", or "production access only".
  These map to `provision_note="Requires API Owner approval"` on the
  catalog entry.
- **Catalog group** — decide which `GROUP_*` constant in
  `apis/catalog.py` this API belongs to BEFORE writing the entry. Use the
  matrix in `new-api-playbook.md` §"Picking a catalog group". Do NOT let
  it default to `GROUP_DATA`.

### Phase 1b — Pre-flight check before any provisioning attempt

Run these checks now; each one prevents a class of basic Phase 2 error:

1. `py tools\validate_api_contract.py` — must print `OK`. Catches missing
   manifest, missing fixture, catalog/spec drift, and bad `module_path`.
2. `py -c "from apis.catalog import CATALOG; e=[x for x in CATALOG if x.id=='<api_name>'][0]; print(e.group, e.env_prefix, e.portal_slug, e.auth)"` —
   confirms the entry loads, the group is the one you chose, and the
   `env_prefix` is unique (grep for it in `apis/catalog.py`; collisions cause
   the prefix-match bug we fixed in the `.env` merge).
3. Open `tools/mcd-key-automation/providers/mastercard/api_config.py` and
   confirm the new mapping has: matching `api_name`, correct `portal_slug`,
   correct `provision_type` (`playbook` only if the JSON exists under
   `playbooks/mastercard/<portal-slug>.json`), and a `key_alias` that matches
   what `apis/<api_name>/api.py` reads from `<ENV_PREFIX>_SIGNING_KEY_ALIAS`.
4. If the auth is OAuth 1.0a + JWE, verify the encryption client is wired up
   in `apis/<api_name>/api.py` (encryption certs, content encryption alg).
   If it isn't, add the API to `DISABLED_API_IDS` and stop — flag to the
   human that JWE is required.
5. Confirm portal credentials exist in `config/.env`:
   `MCD_PORTAL_USERNAME`, `MCD_PORTAL_PASSWORD`, and `MCD_PORTAL_TOTP_SECRET`
   (or that the human is on standby for interactive 2FA). If missing, stop
   and tell the human exactly what to add.

Only proceed to Phase 2 when all five pre-flight checks pass.

### Phase 2 — Is the 'Add Project' (portal provisioning) workflow working?

1. Check `tools/mcd-key-automation/playbooks/mastercard/<portal-slug>.json`.
   If it exists, the playbook driver replays the wizard headlessly. If it
   does NOT exist, the API needs a one-time recording.
2. Confirm the `api_config.py` mapping for this `api_name` has the correct
   `provision_type` (`playbook` if a JSON playbook exists, otherwise whatever
   driver matches the portal flow — see `provisioning-workflows.md`).
3. Smoke the provisioning end-to-end with a dry run:

   ```bash
   ./addapi.sh --headful <DOCS_URL>
   ```

   If it hangs, errors, or produces no `config/keys/<api_name>.p12`:

   - Read the traceback and identify the failing step (selector miss,
     wrong driver, missing playbook, expired session, etc.).
   - If it is a missing/broken playbook, re-record:

     ```bash
     ./addapi.sh --record <DOCS_URL>
     ```

     and drive the wizard manually in the browser window that opens.
   - If it is a driver/selector issue, patch the relevant file under
     `tools/mcd-key-automation/providers/mastercard/` and re-run.
   - Iterate (record → patch → re-run) until `./addapi.sh <DOCS_URL>`
     completes cleanly, writes `config/.env.generated`, AND drops a
     `config/keys/<api_name>.p12` file. Then:

     ```bash
     cat config/.env.generated >> config/.env
     ```

4. Phase 2 is done when a fresh `./addapi.sh <DOCS_URL>` run succeeds
   without manual intervention (other than the initial recording, if any).

### Phase 3 — End-to-end live test with a freshly-provisioned project

1. Provision a brand-new project via `./addapi.sh <DOCS_URL>` so you have
   fresh keys. Confirm `config/.env` now has `<ENV_PREFIX>_CONSUMER_KEY`,
   `<ENV_PREFIX>_SIGNING_KEY_ALIAS`, `<ENV_PREFIX>_SIGNING_KEY_PASSWORD` set.
2. Call the candidate smoke operation (the one harvested in Phase 1)
   against the live sandbox. Prefer:

   ```bash
   cd tools/mcd-key-automation && \
   ./.venv/bin/mcd-key-automation test-api <DOCS_URL>
   ```

   …or invoke `apis/<api_name>/api.py:execute()` directly with the test
   values you harvested.
3. On any non-2xx response or exception:
   - Re-fetch the docs URL and look for sample requests / required
     fields / sandbox-specific test values (test BINs, test card
     numbers, allowed merchant IDs, etc.). Mastercard docs usually
     have a "Try It" panel or a "Test Cases" / "Sample Data" section
     — pull a known-good payload from there.
   - Update the smoke values (and simulator fixture if needed).
   - If the failure is auth-related (401/403), verify the signing key
     alias, password, and consumer key in `config/.env` match
     `config/.env.generated` exactly; re-provision if not.
   - If the failure is schema-related, fix the `MANIFEST` or request
     builder in `apis/<api_name>/api.py`.
   - Retry. Keep iterating until you get a clean 2xx with a payload
     that matches the documented response schema.
4. Once the live call succeeds, also run the simulator path
   (`simulator/handlers/<api_name>.py` via the local dev server) to
   confirm parity, and run:

   ```bash
   ./.venv/bin/python tools/validate_api_contract.py
   ```

5. **Final gate — confirm HTTP 200 OK from the live sandbox.**
   Run:

   ```bash
   cd tools/mcd-key-automation && \
   ./.venv/bin/mcd-key-automation test-api <DOCS_URL>
   ```

   The output MUST include `✅ PASS` and print `status=200` (or another
   2xx code documented as the success response for that operation).
   If it does not:
   - Do not mark onboarding complete.
   - Re-read the docs, fix the request, and retry until you see 200 OK.
   Paste the final passing line (secrets redacted) into the checklist.

### Phase 3a — `how_to` quality bar

The `how_to` HTML string in `apis/<api_name>/api.py:MANIFEST` is what the
user sees in the *How To Use: <API>* modal. It MUST contain, in this order:

1. A one-sentence plain-English summary of what the API does.
2. **Numbered "How to use" steps** that name the exact operation in the
   sidebar (`<strong>Category → Operation name</strong>`) and the exact
   field values to type — taken verbatim from the Test Data Kit harvested
   in Phase 1a. Never invent values; only ship values that returned 2xx in
   Phase 3.
3. **"What you get back"** bullets — the headline response fields.
4. **"Test data & references"** section with explicit links:
   - `<a href="<docs_url>">API documentation</a>`
   - `<a href="<docs_url>api-reference/">Try It console</a>` (or the actual
     deep link harvested in Phase 1a)
   - `<a href="<sandbox-test-data-url>">Sandbox test data</a>` if Mastercard
     publishes a dedicated test-data page
   - An inline `<ul>` of the 3–5 test values you confirmed working (BINs,
     PANs, merchant IDs, etc.) with a one-line caption each.
5. If the API requires approval / has entitlement gates, an italicised
   note: *"Requires API Owner approval on developer.mastercard.com before
   the sandbox returns live data."*

Compare your draft against `apis/bin_lookup/api.py` and
`apis/consumer_clarity/api.py` — those are the reference quality bar. If
your `how_to` is shorter or has fewer concrete values/links, expand it.

### Deliverable

Finish by writing a checklist at
`docs/agent-onboarding/checklists/<api_name>-onboarding-checklist.md`
based on `docs/agent-onboarding/onboarding-checklist-template.md`, ticking
off each phase and pasting in the successful live response (with secrets
redacted). Then summarise to the human: phase results, catalog group
chosen, files changed, and the exact smoke command they can re-run.

### Constraints

- Do not commit or push anything.
- Do not modify `config/.env` directly except by appending `config/.env.generated`.
- Do not mock the live call in Phase 3 — it must hit the real sandbox.
- Do not let the catalog `group` default to `GROUP_DATA`; pick deliberately.
- Do not ship a `how_to` that fails the Phase 3a rubric.
- If you genuinely cannot proceed (e.g. portal credentials missing from
  `config/.env`, or JWE wiring required), stop and tell the human exactly
  what to add.

### Common failure modes (and how to pre-empt them)

| Symptom in Phase 2/3                                  | Root cause                                              | Pre-empt in Phase 1b                                                       |
|-------------------------------------------------------|---------------------------------------------------------|----------------------------------------------------------------------------|
| `.env` merge puts new keys under the wrong API header | Two `env_prefix` values share a prefix (e.g. `FOO` vs `FOO_BAR`) | Grep `apis/catalog.py` for prefix collisions; the merge uses longest-prefix-first, but only if each prefix is unique |
| `addapi.sh` hangs on portal login                     | Missing/expired `MCD_PORTAL_*` credentials              | Pre-flight check #5                                                        |
| Playbook driver errors `selector not found`           | Portal UI changed since playbook was recorded           | Re-record with `./addapi.sh --record <DOCS_URL>`                            |
| Phase 3 returns 401/403                               | `key_alias`/`env_prefix` mismatch between catalog and `api_config.py` | Pre-flight check #3                                                        |
| Phase 3 returns 404                                   | Sandbox base URL wrong, or the project lacks entitlement | Phase 1a (base URL) + flag `provision_note="Requires API Owner approval"` |
| Phase 3 returns 400 "invalid field"                   | Sample body invented instead of harvested               | Phase 1a (copy Mastercard's sample verbatim)                                |
| API renders in wrong sidebar section                  | `group` defaulted to `GROUP_DATA`                       | Phase 1a final bullet                                                      |
