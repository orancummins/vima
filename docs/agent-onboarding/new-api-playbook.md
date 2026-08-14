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
3. **Pick the catalog group deliberately** — do not let it default to `GROUP_DATA`.

### Picking a catalog group

`apis/catalog.py` defines four `GROUP_*` constants. Use this matrix to decide:

| Group                              | Constant              | Belongs here when the API…                                                                                              | Examples                                                                       |
|------------------------------------|-----------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| Open Banking & Open Finance        | `GROUP_OPEN_FINANCE`  | Aggregates accounts/transactions/balances or moves consent across financial institutions (Finicity, Aiia, CDR, PSD2).    | `open_finance`, `open_finance_au`, `open_finance_eu`                           |
| Security & Risk                    | `GROUP_SECURITY`      | Authenticates, authorises, flags fraud, scores risk, manages consent records, or sends transaction security signals.     | `consent_management`, `transaction_notifications`, `match`                     |
| Data & Insights                    | `GROUP_DATA`          | Enriches a transaction, BIN, merchant, or location with reference data; calculates rates; pure lookup/analytics.         | `bin_lookup`, `merchant_identifier`, `consumer_clarity`, `places`, `enhanced_currency_conversion_calculator` |
| Loyalty, Offers & Benefits         | `GROUP_LOYALTY`       | Surfaces card-linked offers, benefits, eligibility, redemptions, recurring billing updates, or experiences.              | `easy_savings`, `offers_for_publishers`, `offers_merchant_content`, `benefits_eligibility`, `benefits_content_eligibility`, `automatic_billing_updater`, `priceless_cities` |

If an API straddles two groups, place it where users will look for it first (think: which sidebar heading would I scan?). When in doubt, mirror the closest existing API.

## Bundle Assignment

Catalog groups drive the sidebar; **bundles** drive the solution-shaped grouping in the Bundles tab and the "Part of bundles" chip on the API detail panel. Every new API must be assigned to **at least one** bundle (or explicitly justified as not belonging to any).

1. Open `apis/bundles.py` and read each existing `Bundle(...)` block — the `tagline` and `description` describe what real-world solution the bundle delivers. Current bundles:

   | Bundle id            | Anchor                | Theme                                                                                         |
   |----------------------|-----------------------|-----------------------------------------------------------------------------------------------|
   | `pfm_stack`          | `open_finance`        | Pull, clean, geo-tag, contextualise and CO₂-score consumer transactions for PFM experiences. |
   | `subscriptions`      | `automatic_billing_updater` | Detect, keep alive and notify on recurring payments / subscriptions.                     |
   | `loyalty_stack`      | `easy_savings`        | Card-linked offers, benefits eligibility, and reward experiences.                            |
   | `merchant_resolution`| `consumer_clarity`    | Resolve cryptic descriptors to clean merchant names, logos and POIs.                         |
   | `issuer_toolkit`     | `bin_lookup`          | Issuer-side card-program ops: BIN data, billing updates, transaction signals.                |
   | `acquirer_risk`      | `match`               | Acquirer onboarding, risk screening and merchant controls.                                   |
   | `sustainability`     | `carbon_calculator`   | Climate-aware payment experiences sourced from real transactions.                            |

2. Decide membership using this rule of thumb:
   - **Anchor candidate?** If the new API defines a category of experience that the bundle would be meaningless without (e.g. Open Finance for `pfm_stack`), it may deserve its own bundle. Get reviewer agreement before adding one.
   - **Complement?** If the new API extends or enriches an anchor (cleaner data, more context, downstream signal), append its id to the existing bundle's `apis=(...)` tuple — ordered by how directly it pairs with the anchor.
   - **Multi-bundle?** APIs frequently belong to several bundles (e.g. `bin_lookup` is in `issuer_toolkit`, `acquirer_risk` and gates `easy_savings` inside `loyalty_stack`). Add it to every bundle where a developer would expect to find it.
   - **None of the above?** If the API genuinely doesn't pair with any existing bundle, record the rationale in the onboarding checklist and propose a new `Bundle(...)` entry (see step 4).

3. To add the API to an existing bundle, edit only the `apis=(...)` tuple — no other code changes required. Example:

   ```python
   # In apis/bundles.py, inside Bundle(id="pfm_stack", ...)
   apis=(
       "open_finance",
       "consumer_clarity",
       "merchant_identifier",
       "places",
       "carbon_calculator",
       "consent_management",
       "<new_api_id>",   # ← add here, position by how directly it pairs with the anchor
   ),
   ```

   If the bundle has a `journey=(...)` or `walkthroughs=(...)` block and the new API materially changes the story, add a step/sentence there too. Otherwise leave them alone — the API will still render under "APIs in this bundle".

4. To propose a new bundle, copy an existing `Bundle(...)` block at the top of `apis/bundles.py` and fill in `id`, `name`, `tagline`, `description`, `anchor`, `accent` (pick a hex distinct from the existing palette — currently amber, teal, purple, red, orange, blue, dark red, green), `icon_path`, `apis`, and ideally `value_props` + `journey` + `examples`. New bundles need reviewer signoff.

5. Verify in the UI:
   - Bundles tab lists the bundle, with the new API rendered in "APIs in this bundle".
   - APIs tab → open the new API → "Part of bundles" chip row includes every bundle you added it to, each in the bundle's accent colour.

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
