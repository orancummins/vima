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

   While checking, ALSO harvest from the docs URL (fetch it) the candidate
   smoke-test operation + a working example request body / path params /
   query params. Save these test values to a scratch note — you will need
   them in Phase 3 even if the API already exists.
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

### Deliverable

Finish by writing a checklist at
`docs/agent-onboarding/checklists/<api_name>-onboarding-checklist.md`
based on `docs/agent-onboarding/onboarding-checklist-template.md`, ticking
off each phase and pasting in the successful live response (with secrets
redacted). Then summarise to the human: phase results, files changed,
and the exact smoke command they can re-run.

### Constraints

- Do not commit or push anything.
- Do not modify `config/.env` directly except by appending `config/.env.generated`.
- Do not mock the live call in Phase 3 — it must hit the real sandbox.
- If you genuinely cannot proceed (e.g. portal credentials missing from
  `config/.env`), stop and tell the human exactly what to add.
