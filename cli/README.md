# ofin — Open Finance CLI + SDK

A standalone command-line interface and Python SDK that wraps the three
Mastercard **Open Finance** APIs — **US** (Finicity), **Australia** (CDR), and
**Europe** (Aiia) — behind one consistent tool.

It runs **completely independently** of the Flask web app, works on
**Windows, macOS, and Linux**, and ships as a portable Python zipapp
(`ofin.pyz`) — **no `.exe`, no compiled binary**.

```
ofin us auth token
ofin eu providers list --country DK
ofin au connect generate --open
```

---

## Requirements

* Python **3.9+**
* `requests` and `cryptography`
  (`cryptography` is required for EU JWT signing)

```bash
pip install requests cryptography
```

---

## Three ways to run it

### 0. Root launcher scripts (easiest)

From the repo root, use the `ofin` launcher for your platform:

```bash
# macOS / Linux
./ofin.sh                     # no args -> welcome screen (config + quickstart)
./ofin.sh us auth token       # run any command
./ofin.sh build               # build the portable bundle into cli/dist/
./ofin.sh help

# Windows
ofin.bat
ofin.bat us auth token
ofin.bat build
ofin.bat help
```

Running with no command prints a welcome screen showing where credentials were
loaded from, which regions are configured, the state-file location, and a
quickstart.

### 1. From the repo (development)

```bash
python -m ofin config show        # from cli/, or anywhere with cli/ on PYTHONPATH
```

The SDK imports the existing `apis/open_finance*/client.py` directly — a single
source of truth, no duplication. Credentials are auto-discovered from the
repo's `config/.env`.

### 2. Editable install (`ofin` on your PATH)

```bash
pip install -e cli
ofin config show
```

### 3. Portable bundle (copy anywhere)

```bash
python cli/build.py
```

This produces `cli/dist/` containing:

| File | Purpose |
|------|---------|
| `ofin.pyz` | The CLI + SDK, with the three clients vendored inside (self-contained code). |
| `ofin.env` | Credentials assembled from `config/.env` (single source of truth). |
| `keys/` | The EU RSA key + cert as real files (the EU client reads them from disk). |
| `ofin.cmd` / `ofin` | Text launcher scripts that wire `--env-file` automatically. |

Copy the whole `dist/` folder to any machine with Python + the two deps:

```bash
# Windows
dist\ofin.cmd config show

# macOS / Linux
./dist/ofin config show

# or directly
python dist/ofin.pyz --env-file dist/ofin.env us auth token
```

---

## Configuration & precedence

Credentials resolve in this order (highest first):

1. CLI flags
2. OS environment variables
3. `--env-file PATH`
4. The repo's `config/.env` (auto-discovered in dev)
5. The bundled `ofin.env` (in a built `dist/`)

| Region | Variables |
|--------|-----------|
| US | `OPEN_FINANCE_PARTNER_ID`, `OPEN_FINANCE_PARTNER_SECRET`, `OPEN_FINANCE_APP_KEY`, `OPEN_FINANCE_API_BASE_URL` |
| AU | `OPEN_FINANCE_AU_PARTNER_ID`, `OPEN_FINANCE_AU_PARTNER_SECRET`, `OPEN_FINANCE_AU_APP_KEY`, `OPEN_FINANCE_AU_API_BASE_URL` |
| EU | `OPEN_FINANCE_EU_CLIENT_ID`, `OPEN_FINANCE_EU_PRIVATE_KEY_PATH`, `OPEN_FINANCE_EU_PUBLIC_CERT_PATH`, `OPEN_FINANCE_EU_APPLICATION_ID`, `OPEN_FINANCE_EU_AUTH_BASE_URL`, `OPEN_FINANCE_EU_API_BASE_URL`, `OPEN_FINANCE_EU_USE_CASE_ID` |

Check what's wired up:

```bash
ofin config show
```

---

## Stateful flows

Multi-step flows feel stateful between separate invocations. Ids produced by
one command (customer, consent, account, EU `end_user_id`, …) are saved to
`~/.ofin/state.json` and reused automatically.

```bash
ofin us customers add-testing --username demo1   # saves customer_id
ofin us accounts list                            # uses the saved customer_id

ofin state show
ofin state clear us
```

Override the state file with `--state-file PATH` or `OFIN_STATE_FILE`.

---

## Global flags

| Flag | Effect |
|------|--------|
| `--json` | Emit the full result envelope as JSON. |
| `--raw` | Print only the response body. |
| `--no-color` | Disable ANSI colors. |
| `--env-file PATH` | Use a specific credentials file. |
| `--state-file PATH` | Use a specific state file. |
| `--timeout N` | Per-request timeout (seconds). |
| `-v`, `--verbose` | Show tracebacks on unexpected errors. |

---

## Command reference

List everything per region:

```bash
ofin ops          # all regions
ofin ops eu       # just EU
```

### US (Finicity)

```bash
ofin us auth token
ofin us customers add-testing --username demo1
ofin us customers list [--search foo] [--limit 25]
ofin us customers get [--customer-id ID]
ofin us customers use <CUSTOMER_ID>
ofin us connect generate [--customer-id ID] [--experience EXP] [--open]
ofin us accounts list [--customer-id ID]
ofin us accounts refresh [--customer-id ID]
ofin us balance [--customer-id ID] [--account-id ID]
ofin us transactions list --from-date <epoch> --to-date <epoch> [--limit N]
ofin us reports voa [--account-ids a,b]
ofin us reports voi [--account-ids a,b]
```

### AU (CDR)

```bash
ofin au auth token
ofin au customers add-testing --username demo1
ofin au customers list
ofin au institutions list [--search foo]
ofin au connect generate [--customer-id ID] [--webhook-url URL] [--open]
ofin au consents list [--customer-id ID] [--status ACTIVE]   # captures consent-receipt-id
ofin au accounts list [--customer-id ID] [--consent-receipt-id ID]
```

### EU (Aiia)

```bash
ofin eu auth token
ofin eu providers list [--country DK] [--limit 25]
ofin eu consent create --email you@example.com [--use-case-id ID] [--end-user-id ID]
ofin eu consent get [--consent-id ID]
ofin eu consent revoke [--consent-id ID] --yes
ofin eu flow create [--consent-id ID] [--end-user-id ID] [--provider-id ID] [--open]
ofin eu accounts list [--consent-id ID]
ofin eu account get [--account-id ID] [--consent-id ID]
ofin eu transactions list [--account-id ID] [--consent-id ID] [--from-date D] [--to-date D]
ofin eu balance [--account-id ID] [--consent-id ID] [--max-age PT0S]
ofin eu verify-ownership --customer-name "Jane Doe" [--account-ids a,b]
```

> Destructive operations (e.g. `eu consent revoke`) require `--yes`.

---

## Example: full EU happy path

```bash
ofin eu auth token
ofin eu providers list --country DK
ofin eu consent create --email demo@example.com          # saves consent_id + end_user_id
ofin eu flow create --open                               # opens the hosted bank login
# ...complete the sandbox login in the browser...
ofin eu consent get                                      # poll until granted
ofin eu accounts list                                    # saves first account_id
ofin eu transactions list
ofin eu balance --max-age PT0S
```

---

## Using the SDK directly

```python
from ofin import OfinClient

client = OfinClient.from_env()          # credentials auto-loaded from config/.env
res = client.eu.list_providers(country="DK")
print(res.ok, res.status)
print(res.body)
```

Every call returns a `Result` with `.ok`, `.status`, `.token`, `.body`,
`.request`, `.response`, `.state_updates`, and `.hints`.

---

## Architecture

```
cli/
  build.py            # assembles the portable dist/ (zipapp + env + keys + wrappers)
  pyproject.toml      # editable install + 'ofin' console script
  ofin/
    cli.py            # argparse root, global flags, dispatch
    config.py         # credential resolution (flags > env > --env-file > repo .env > bundled)
    state.py          # ~/.ofin/state.json active-id store
    output.py         # --json / --raw / human rendering, color, browser open
    errors.py         # typed errors -> clean exit codes
    sdk/
      __init__.py     # OfinClient facade (.us .au .eu)
      _imports.py     # resolve clients: apis.* (dev) or ._vendor.* (bundled)
      base.py         # Result envelope
      us.py au.py eu.py
      _vendor/        # build-time copies of apis/*/client.py (gitignored)
    commands/
      common_cmd.py us_cmd.py au_cmd.py eu_cmd.py
```

The SDK wraps only the API **clients** (not the web app's dispatchers), so it
carries no Flask / simulator coupling.
