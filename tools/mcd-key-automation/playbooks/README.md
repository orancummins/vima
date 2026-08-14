# Portal Playbooks

A playbook is a JSON file that describes the deterministic steps to create a
Mastercard portal project for one API. The playbook is **recorded once** by
walking through the create-project UI in a real browser, then **replayed
autonomously** for every subsequent provisioning.

## Why playbooks?

The Mastercard developer portal's create-project wizard differs structurally
per API (some have wizards, others are single forms; some have conditional
fields like MATCH's contact email). Hand-coding a flow per API is brittle.
A recorded playbook captures the exact selectors and value sequence the user
performed and replays them with realistic pacing.

## Layout

```
playbooks/
  <organization>/
    <api-slug>.json
```

For Mastercard APIs the organization is `mastercard`. The `api-slug` matches
the URL slug (`bin-lookup`, `match`, `enhanced-currency-conversion-calculator`,
etc.).

## Schema (v1)

```jsonc
{
  "schema": 1,
  "organization": "mastercard",
  "api_slug": "match",
  "recorded_at": "2026-05-28T01:27:29Z",
  "start_url": "https://developer.mastercard.com/create-project?services=match",
  "final_url_pattern": "/project-details/",
  "variables": ["project_name", "alias", "key_password", "contact_email", "ica"],
  "steps": [
    { "action": "wait_for", "selector": "input[data-testid='project-name']" },
    { "action": "fill", "selector": "input[data-testid='project-name']", "value": "{{project_name}}" },
    { "action": "wait_for_proceed_enabled" },
    { "action": "click_proceed" },
    { "action": "click_radio", "name_suffix": "_accessToBeUsedBy", "value": "Internal MasterCard Partner" },
    { "action": "wait_for", "selector": "input[data-testid='acquirerica-text']" },
    { "action": "fill", "selector": "input[data-testid='acquirerica-text']", "value": "{{ica}}" },
    { "action": "fill", "selector": "input[data-testid='acquirercontactemail-text']", "value": "{{contact_email}}" },
    { "action": "click_radio", "name_suffix": "_isReplacingClientId", "value": "No" },
    { "action": "wait_for_proceed_enabled" },
    { "action": "click_proceed" },
    { "action": "wait_for", "selector": "input[data-testid='key-alias-input']" },
    { "action": "fill", "selector": "input[data-testid='key-alias-input']", "value": "{{alias}}" },
    { "action": "fill", "selector": "input[data-testid='key-store-password-input']", "value": "{{key_password}}" },
    { "action": "wait_for_proceed_enabled" },
    { "action": "click_proceed" },
    {
      "action": "expect_download",
      "click_selector": "button[data-testid='download-key-action-project-creation']",
      "timeout_ms": 240000
    },
    { "action": "click", "selector": "button[data-testid='proceed-button-create-new-project']" },
    { "action": "wait_for_url_contains", "value": "/project-details/", "timeout_ms": 60000 }
  ]
}
```

### Supported actions

| action                       | required fields                                   | notes                                                     |
|------------------------------|---------------------------------------------------|-----------------------------------------------------------|
| `goto`                       | `url`                                             | navigate                                                  |
| `wait_for`                   | `selector`                                        | wait for selector visible                                 |
| `wait_for_url_contains`      | `value`                                           | poll until `page.url` contains `value`                    |
| `wait_for_proceed_enabled`   | —                                                 | wait until `button[data-testid='proceed-btn']` enabled    |
| `fill`                       | `selector`, `value`                               | real keystrokes via `press_sequentially`                  |
| `click`                      | `selector`                                        | real Playwright click                                     |
| `click_proceed`              | —                                                 | click `button[data-testid='proceed-btn']` (JS-safe)       |
| `click_radio`                | `name_suffix`, `value`                            | clicks the radio whose `name` ends with `name_suffix`     |
| `expect_download`            | `click_selector`, `timeout_ms`                    | clicks the selector inside `expect_download` context      |
| `sleep`                      | `ms`                                              | hard wait (use sparingly)                                 |
| `screenshot`                 | `name`                                            | debug screenshot                                          |

Values can reference variables via `{{name}}` substitution. The runner
provides these variables:

- `project_name` — portal project name
- `alias`        — signing key alias
- `key_password` — signing key store password
- `contact_email`— logged-in user's email (auto-resolved from session JWT)
- `ica`          — default `123456789`

## Recording a new playbook

```bash
./addapi.sh --record https://developer.mastercard.com/<slug>/documentation/
```

This opens a headful browser at the create-project page for the API, captures
your interactions, and writes `playbooks/mastercard/<slug>.json` on exit.

## Replaying

The default `./addapi.sh <URL>` flow automatically prefers a playbook when
one exists for the slug. If none exists you'll be prompted to record one.
