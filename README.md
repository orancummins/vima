# Vima — Mastercard APIs Explorer

A small Flask app that provides a tabbed UI for testing Mastercard Developer
APIs, plus a place to build use cases composed from them.

```
http://localhost:9021
```

## Tabs

- **APIs**
  - **Open Finance** — Mastercard / Finicity US Open Banking. Fully wired.
  - **BIN Lookup** — stub; scaffold for the BIN Resource Lookup API.
- **Use Cases** — empty scaffold for end-to-end demos that compose the APIs.

## Setup

```bash
cd /Users/orancummins/dev/vima
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Credentials live in `.env` (copied from the `usob` project for the initial
Open Finance integration). The BIN Lookup project requires a separate
Mastercard consumer key and `.p12` signing key — add when implementing.

## Open Finance flow (suggested order)

The operation panel pre-fills inputs from server-side state once produced
by an earlier call:

1. **Auth → Create Access Token** (sanity check)
2. **Customers → Create Testing Customer** (`customer_id` populated)
3. **Data Connect → Generate Data Connect URL** → click *Open Data Connect*,
   complete the FinBank flow in the new tab
4. **Accounts → Refresh Accounts** (`account_id` populated)
5. Any of: Get Transactions, Get Live Balance, Get Account Owner,
   Get ACH/Payment Details, Get Recurring Transactions
6. **Reports →** VOA / VOI / Cash Flow / Balance Analytics
   (the consumer record is auto-created if missing)
7. **Payments → Generate PSI** for a chosen account + amount

## Adding a new API

1. Create `apis/<id>/api.py` exposing:
   - `MANIFEST` — id, name, description, categories, operations, state_schema
   - `execute(op_id, params) -> dict` returning `{success, data, error,
     request, response, state_updates, hints}`
   - optional `get_state()`, `is_configured()`
2. Register it in [apis/registry.py](apis/registry.py).

## Adding a use case

Edit `USE_CASES` in [usecases/registry.py](usecases/registry.py) (and expand
the registry pattern to mirror `apis/` once richer behaviour is needed).
