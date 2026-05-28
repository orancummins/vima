# One-File API Onboarding Instruction

Purpose: run autonomous onboarding by giving an agent only this file and one Mastercard API documentation link.

## Operator Input (only two things)

1. This file path: docs/agent-onboarding/one-file-api-onboarding-instruction.md
2. Mastercard API docs URL: <paste URL here>

## What the agent must do

The recommended entry point is `./addapi.sh <DOCS_URL>`. It runs portal
provisioning (record-once-replay-forever) and then emits an "AGENT NEXT STEPS"
block telling the agent (you) exactly which codebase additions follow. You
may invoke `addapi.sh` yourself as the first action; the steps below describe
the complete workflow you are responsible for end-to-end.

1. Parse the API docs URL and infer product name, portal slug, likely auth model, and candidate operation for smoke tests.
2. If auth model cannot be inferred confidently, stop and ask for confirmation before coding.
3. Follow the full implementation workflow in:
- docs/agent-onboarding/new-api-playbook.md
- docs/agent-onboarding/provisioning-workflows.md
- docs/agent-onboarding/ui-integration-contract.md
- docs/agent-onboarding/testing-matrix.md
- docs/agent-onboarding/troubleshooting.md
4. Update docs/agent-onboarding/api-onboarding-spec.yaml for the new API.
5. Add API identity entry in apis/catalog.py.
6. Implement apis/<id>/api.py with MANIFEST (including docs_url and how_to) and execute.
7. Add simulator handler and fixture.
8. Add provisioning mapping in tools/mcd-key-automation/providers/mastercard/api_config.py and ensure the provision_type is supported in tools/mcd-key-automation/providers/mastercard/workflows/project_workflow.py.
9. Verify UI surfacing:
- appears in APIs tab via manifests
- appears in provisioning modal via /provision/catalog
- Docs and How To render
10. Run validation:
- ./.venv/bin/python tools/validate_api_contract.py
11. Run smoke checks:
- simulator operation
- live operation when credentials are available
12. After the provisioning mapping is wired (step 8), acquire portal credentials for the API:

    **From the repo root, prefer the wrapper:**
    ```
    ./addapi.sh <DOCS_URL>
    ```
    This runs `provision-api` and the post-provisioning smoke test in one step.

    **Record-once, replay-forever:** Some APIs (e.g. MATCH) use a structurally
    different create-project wizard and are driven by a recorded JSON playbook
    at `tools/mcd-key-automation/playbooks/mastercard/<slug>.json`. If
    `provision-api` prints a warning that no playbook exists for the slug:

    ```
    ./addapi.sh --record <DOCS_URL>
    ```
    Walk through the portal create-project flow manually (project name → all
    required fields → key alias + password → Create project → Download key
    file). When the key zip downloads, return to the terminal and press Enter.
    The recorder compresses the trace into a replayable playbook. Re-run
    `./addapi.sh <DOCS_URL>` to provision autonomously thereafter.

    Direct CLI equivalents (when not using the wrapper):
    ```
    cd tools/mcd-key-automation
    .venv/bin/mcd-key-automation provision-api <DOCS_URL>
    .venv/bin/mcd-key-automation record-api --api-slug <slug>   # one-time recording
    ```

    Prerequisites:
    - `MCD_PORTAL_EMAIL` and `MCD_PORTAL_PASSWORD` must be set in `config/.env` for login pre-fill.
    - If a valid session exists from a prior run (`session_state.json`), the browser skips login entirely.
    - If no session or credentials: the browser opens, complete sign-in + MFA manually, then the tool continues autonomously.

    After the command succeeds, merge the generated credentials into `config/.env`:
    ```
    cat config/.env.generated >> config/.env
    ```
    Then re-run the live smoke test to confirm credentials are active.
13. Create and complete a checklist artifact from docs/agent-onboarding/onboarding-checklist-template.md at docs/agent-onboarding/checklists/<api-id>-onboarding-checklist.md.
14. Source official sandbox test data from docs and set known-good operation defaults in `MANIFEST`.
15. Add a "Sandbox test values" subsection in `MANIFEST.how_to` that links the official dataset and lists operation-specific sample inputs.

## First-Pass Accuracy Guardrails (required)

1. Before coding request handlers, extract and write down the canonical request contract per operation:
- endpoint path
- method
- exact parameter names
- parameter cardinality (single vs list)
- required companion params
- value format constraints
2. Before composing any request URL, extract canonical base URLs directly from OpenAPI `servers` or Swagger `host` + `basePath`.
- Record sandbox and production base URL values explicitly.
- Build operation URLs as `base_url + endpoint_path` only (no inferred prefixes).
3. Do not translate field names across styles unless docs explicitly say so.
- Example risk pattern: `merchant_descriptor` incorrectly implemented as `merchantDescriptor`.
4. After first live call, if credentials are valid but status is 400:
- parse upstream error body
- map `Source` fields directly to request keys
- fix request contract before touching auth/provisioning.
5. If the response is edge/CDN HTML (for example Akamai/edgesuite reference page) with 5xx, treat as route/base-path issue first, not key activation.
6. For country codes and similar enums, confirm required standard and length from docs/examples before setting defaults.
7. Require at least one successful live operation before declaring onboarding complete when credentials are present.
8. If response is `200` with empty/non-actionable payload, treat as test-input mismatch first and retry with official sandbox samples.

## Required output format from agent

1. Proposed metadata:
- id
- legacy_id
- env_prefix
- portal_slug
- auth_type
- docs_url
- primary smoke operation
2. Files changed with one-line purpose each.
3. Validation command output.
4. Smoke test output (simulator and live, or credential-gated proof).
5. Request-contract proof:
- canonical field names used for each implemented operation
- one sample request URL/body per operation
 - spec-derived base URL proof (`servers` or `host/basePath`) and final joined URL used in runtime
6. Sandbox-data proof:
- docs source URL for official test dataset
- sample values selected per operation
- confirmation that default UI values use known-good sandbox samples
 - confirmation that How To modal includes linked sandbox test values
7. Completed checklist artifact path:
- docs/agent-onboarding/checklists/<api-id>-onboarding-checklist.md
8. Checklist status:
- Intake
- Discovery
- Catalog Registration
- Module Implementation
- Request-Contract Verification
- Sandbox Data Readiness
- Simulator Wiring
- Provisioning Wiring
- UI Wiring
- Testing
9. If blocked:
- exact blocker
- attempted recovery
- next action required from operator

## Hard success gates

1. tools/validate_api_contract.py passes
2. API is present in explorer manifests and provision catalog
3. API docs_url and how_to render in UI
4. Provisioning workflow is mapped correctly
5. Simulator smoke passes
6. Completed checklist artifact exists and is filled in
7. At least one operation returns non-empty/actionable data using official sandbox samples

## Operator launch message template

Use docs/agent-onboarding/one-file-api-onboarding-instruction.md and onboard this API:
<PASTE_MASTERCARD_API_DOCS_URL>

Proceed autonomously. Ask me only for login/MFA/CAPTCHA or unresolved auth-type confirmation.

## Autonomous portal credential acquisition — one-time setup

Before the first use, establish a cached portal session so all subsequent runs are headless:

```bash
cd tools/mcd-key-automation

# 1. Add credentials to config/.env (once)
echo "MCD_PORTAL_EMAIL=your@email.com" >> ../../config/.env
echo "MCD_PORTAL_PASSWORD=yourpassword" >> ../../config/.env

# 2. Establish session (opens browser once for MFA)
.venv/bin/mcd-key-automation init-session
```

After init-session succeeds, `provision-api` detects the fresh session and runs headless automatically:

```bash
# Fully autonomous — no browser window, no interaction
.venv/bin/mcd-key-automation provision-api <PASTE_MASTERCARD_API_DOCS_URL>
```

Session stays fresh for ~8 hours. Re-run `init-session` when it expires.
