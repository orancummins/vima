# Mastercard Solution Studio

A unified platform for exploring, showcasing and innovating across
[Mastercard APIs](https://developer.mastercard.com/) and use cases.

> **ViMA** = **Vi**becoding with **MA**stercard — the codename for the
> embedded AI coding assistant that lets you customise and extend use cases
> from inside the running app.

![Solution Studio home](docs/screenshots/MastercardSolutionStudio-home.png)

---

## What it does

Solution Studio wires up a curated set of Mastercard Developer APIs so they
"just work" out of the box, then layers a collection of **Use Cases** on top
to demonstrate, combine and innovate on those capabilities. An embedded
Claude-powered chat (ViMA) lets you edit any use case in place — no IDE
required.

### Wired-up APIs

All accessible from the **APIs** tab. Each has full request/response
inspection, parameter forms and state chaining between operations.

| API | Notes |
|---|---|
| **Open Finance** | Mastercard / Finicity US Open Banking — accounts, transactions, balances, reports (VOA / VOI / Cash Flow), Data Connect, ACH details. *US IP required.* |
| **BIN Lookup** | Card range / BIN metadata |
| **Consumer Clarity** | Enhanced merchant data and logos |
| **Consent Management** | Card-on-file consent capture and authentication |
| **Easy Savings** | Card-linked offers and redemption |
| **Benefits Eligibility** | Card benefit eligibility checks |
| **Benefits Content Eligibility** | Searchable benefit content catalogue |
| **Offers for Publishers** | Card-linked offers for publisher channels |
| **Offers Merchant Content** | Merchant content for offers |
| **MATCH Pro** | Merchant Alert to Control High-Risk merchants — termination inquiry and lookup |
| **Places** | Mastercard Places merchant location data |
| **Priceless** | Priceless Cities experiences |
| **Transaction Notifications** | Real-time transaction notifications |

![APIs tab](docs/screenshots/MastercardSolutionStudio-API.png)

![Open Finance API](docs/screenshots/MastercardSolutionStudio-API-OpenFinance.png)

### Use Cases

Showcased under the **Use Cases** tab. Each is a self-contained scenario
that composes one or more of the APIs above:

- **Personal Finance Manager** — full PFM dashboard over Open Finance
- **Data Enrichment** — merchant enrichment with logos & categories
- **Recurring Transactions** — recurring payment detection
- **Payment Success Indicator (PSI)** — score the likelihood of payment success
- **BIN Lookup** — interactive BIN explorer
- **Consumer Clarity** — merchant search with rich content
- **Easy Savings** — browse and redeem card-linked offers
- **Places** — merchant location explorer
- **Online Identity Verification** — IDV flow demo
- **Specials** — themed offer collections
- **[Find A Card](https://github.com/orancummins/fac)** — card recommendation engine (separate repo, embedded)
- **Sonic Branding** — Mastercard sound experience
- **Finance In Colour** — visual spend analytics
- **Test Chat** — ViMA chat playground

![Use Case — Open Finance](docs/screenshots/MastercardSolutionStudio-UseCase-OpenFinance.png)

![Use Case — BIN Lookup](docs/screenshots/MastercardSolutionStudio-UseCase-BINLookup.png)

### ViMA — Vibecoding with Mastercard

Click the pencil icon in the top bar of any use case to open the embedded
Claude chat. Ask it to tweak the UI, change the layout, add features —
edits are applied directly to the use case source and hot-reload in the
preview. Requires an Anthropic API key (see Setup).

![ViMA chat](docs/screenshots/MastercardSolutionStudio-AIChat.png)

---

## Setup

### 1. Clone & install

```bash
git clone https://github.com/orancummins/vima
cd vima
python -m venv .venv
# Windows
.\.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate
pip install -r requirements.txt -r chat/requirements.txt
```

### 2. Run

```bash
# Windows
.\run.bat

# macOS / Linux
./run.sh
```

Solution Studio (including the ViMA chat) starts on a single port:
**http://localhost:9021**

ViMA chat is embedded directly in the main Flask app — no separate process
or port is needed.

### 3. Configure API keys — one-click auto-provisioning

Click the **Save +** button in the top-right of the app. Solution Studio will
open a provisioning panel listing every wired API. Select the ones you want,
hit **Provision Selected APIs**, and the automation:

1. Opens the Mastercard Developer portal in a headless browser
2. Creates a project, adds each selected API, and generates signing keys
3. Downloads the `.p12` key files and writes all credentials directly into `config/.env`

No manual portal steps required — just wait ~60 seconds per API.

![Select APIs to Provision](docs/screenshots/MastercardSolutionStudio-APIProvisioning.png)

> **Note:** Priceless Cities requires separate API Owner approval and won't
> activate immediately. All other APIs activate within a few minutes of provisioning.

Credentials are stored locally in `config/.env`. Use the **Export** button
to bundle keys for sharing (the `ANTHROPIC_API_KEY` is redacted from
exports for safety).

### 4. (Optional) Enable ViMA chat

ViMA uses Anthropic's Claude. To enable it:

1. Sign up at [console.anthropic.com](https://console.anthropic.com/)
2. Go to **Settings → API Keys** and create a new key (starts with `sk-ant-`)
3. Paste it into the **Claude Chat** section of Solution Studio's config
   panel

See Anthropic's
[getting started guide](https://docs.anthropic.com/en/docs/get-started)
for more detail.

### 5. (US Open Finance only) Use a US IP

Mastercard's US Open Finance APIs reject non-US source IPs. If you're
running outside the US, connect to a US VPN endpoint before exercising
those endpoints. The Open Finance tab and Use Cases that depend on it
will display a banner if a non-US IP is detected.

---

## Rotating or removing API keys

Run `clean_keys.py` to wipe all local credentials and — optionally — delete the
corresponding projects from the Mastercard Developers portal in one step:

```bash
python clean_keys.py
```

What it does:

1. **Deletes local key material** — `config/keys/*.p12`, `config/keys/*.pem`, `config/.env`, and any cached tool artifacts (`tools/mcd-key-automation/temp/`, output zips).
2. **Clears the running app** — if Solution Studio is open on `localhost:9021` it posts to `/config/purge` so the in-memory env-vars are cleared immediately (no restart needed).
3. **Optionally deletes portal projects** — prompts you before opening a browser. Uses `MCD_PORTAL_EMAIL` / `MCD_PORTAL_PASSWORD` from `config/.env` to log in automatically (same credentials used during provisioning); no manual typing required.

After cleaning, re-run `./addapi.sh <DOCS_URL>` (or the Copilot agent command) to reprovision fresh keys for any API.

---

## Extending the platform

### Add a new API (or fix an existing one)

Paste this into Copilot Chat (agent mode) — that's it:

```
Follow docs/agent-onboarding/autonomous-api-onboarding.md for <DOCS_URL>
```

**Example — MATCH Pro:**

```
Follow docs/agent-onboarding/autonomous-api-onboarding.md for https://developer.mastercard.com/match/documentation/
```

The agent works through three phases automatically:

1. **Phase 1** — Checks whether the API is already integrated (catalog, `apis/<id>/api.py`, simulator handler + fixture, provisioning mapping). If not, it implements everything.
2. **Phase 2** — Runs `./addapi.sh <DOCS_URL>` to provision a live Mastercard Developer project and write credentials to `config/.env` — zero manual portal interaction required for supported APIs.
3. **Phase 3** — Calls the live sandbox and must see `✅ PASS status=200` before it declares success.

See [docs/agent-onboarding/autonomous-api-onboarding.md](docs/agent-onboarding/autonomous-api-onboarding.md) for the full instruction the agent reads.

<details>
<summary>Manual steps (if you prefer to wire an API by hand)</summary>

1. Add a canonical entry in [apis/catalog.py](apis/catalog.py). This is the source of truth for API identity, auth type, docs URL, and display order.
2. Create `apis/<id>/api.py` exposing:
   - `MANIFEST` — `id`, `name`, `description`, `categories`, `operations`, `state_schema`
   - `execute(op_id, params) -> dict` returning `{success, data, error, request, response, state_updates, hints}`
   - optional `get_state()`, `is_configured()`
3. Add matching handler/fixture files under `simulator/handlers/` and `simulator/fixtures/`.
4. Add or verify the provisioning mapping in `tools/mcd-key-automation/providers/mastercard/api_config.py`.
5. Run contract validation before merging:

```bash
./.venv/bin/python tools/validate_api_contract.py
```

`apis/registry.py` loads APIs dynamically from the catalog — no manual registry edits needed.

</details>

### Add a new use case

Two patterns are supported:

**A. Inline UI** — typical for use cases that compose Mastercard APIs
directly. Add a folder under `usecases/<id>/` with `__init__.py`
(exposing `MANIFEST`), `index.html` and `style.css`. Register the
module name in [usecases/registry.py](usecases/registry.py).

**B. Embedded external project** — for use cases that wrap a separate
running app, see [usecases/findacard/](usecases/findacard/) for the
canonical example. It pulls and embeds
[github.com/orancummins/fac](https://github.com/orancummins/fac) as a
web UI inside Solution Studio. Copy that pattern to bring any other
external project into the platform.

---

## Architecture

```
Mastercard Solution Studio (port 9021, Flask)
├── apis/         ← wired Mastercard API integrations
├── usecases/     ← end-to-end demos composing those APIs
├── simulator/    ← optional response mocking for offline / no-key runs
└── chat/         ← ViMA — Claude-powered coding assistant (Blueprint at /chat)
```

The main Flask app serves the UI, proxies API calls, and hosts ViMA chat
as an in-process Blueprint — all on a single port. `run.bat` / `run.sh`
start one process and you're ready to go.

---

## License

Internal exploration / showcase project.

