# UI Integration Contract

Defines mandatory UI behavior for every API onboarded into Solution Studio.

## API List Rendering Contract

- Source: `window.__APIS__` populated from backend manifests.
- Required fields: `id`, `name`, `description`, `configured`.
- API list item status must reflect `configured` boolean.

## How-To Modal Contract

- Trigger: `How To Use These APIs` button in API workbench.
- Source fields: `api.name`, `api.how_to`.
- Behavior: show API-specific title and rich content; fallback message when missing.
- When official sandbox test data exists: `api.how_to` should include a linked source URL and operation-specific sample values.

## Docs Link Contract

- Source field: `api.docs_url`.
- Behavior: always render docs button; opens Mastercard Developers docs in new tab.

## Config Modal Contract

- Source: dynamic groups from backend `/config` response.
- Required per API: group id matches catalog `id`, docs_url present, auth fields based on auth type.

## Provision Modal Contract

- Source: backend `/provision/catalog` endpoint.
- Required fields: `id`, `legacy_id`, `name`, `configured`, `docs_url`, `requires_owner_approval`, `provision_note`.
- Status updates: log-derived start/done/fail must reconcile with `/provision/status` at completion.
- Legacy ID mapping: must support orchestrator logs using legacy names.

## Backward-Compatibility Rules

- If `/provision/catalog` fetch fails, fallback may use `window.__APIS__`.
- Missing optional fields should not break rendering.
- Unknown APIs in logs should not crash status UI.
