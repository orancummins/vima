"""Live Demo — real Open Finance bank linking across US / AU / EU.

Drives the "Live Demo" section in the Open Finance SDK panel:

  * An admin can enable Open Finance per continent (us / au / eu).
  * Only enabled regions expose a "Connect a bank" option to the end user.
  * Connecting runs the *real* hosted Connect/flow against the live
    sandbox APIs (Finicity / CDR / Aiia), opens the bank login in a new
    tab, then polls for the linked accounts + transactions.
  * Connected accounts and transactions are persisted to
    ``data/live_demo_state.json`` so the data survives restarts and can be
    shown again without re-linking. Reconnect / refresh overwrites it.

The real work is delegated to the existing API modules' ``execute()``
functions (single source of truth), so there is no duplicate HTTP logic.
"""
from __future__ import annotations

import os
import json
import time
import threading
from typing import Any, Dict, List, Optional, Tuple

from apis import registry as api_registry

# region key -> backing API module id
_REGION_API = {
    "us": "open_finance",
    "au": "open_finance_au",
    "eu": "open_finance_eu",
}

_REGION_BANK = {
    "us": "Finicity (United States)",
    "au": "CDR (Australia)",
    "eu": "Aiia (Europe)",
}

_REGIONS = ("us", "au", "eu")

_STATE_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "data", "live_demo_state.json"
)

_lock = threading.Lock()


def _blank_connection() -> Dict[str, Any]:
    return {
        "connected": False,
        "bank_name": None,
        "connected_at": None,
        "customer_id": None,
        "consent_receipt_id": None,
        "consent_id": None,
        "end_user_id": None,
        "account_id": None,
        "flow_url": None,
        "accounts": [],
        "transactions": [],
    }


def _default_state() -> Dict[str, Any]:
    return {
        "enabled": {r: False for r in _REGIONS},
        "connections": {r: _blank_connection() for r in _REGIONS},
    }


def _load() -> Dict[str, Any]:
    try:
        with open(_STATE_FILE, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, ValueError):
        return _default_state()
    state = _default_state()
    if isinstance(data, dict):
        en = data.get("enabled") or {}
        for r in _REGIONS:
            state["enabled"][r] = bool(en.get(r))
        conns = data.get("connections") or {}
        for r in _REGIONS:
            base = _blank_connection()
            base.update(conns.get(r) or {})
            state["connections"][r] = base
    return state


def _save(state: Dict[str, Any]) -> None:
    os.makedirs(os.path.dirname(_STATE_FILE), exist_ok=True)
    tmp = _STATE_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=2)
    os.replace(tmp, _STATE_FILE)


def _module(region: str):
    api_id = _REGION_API.get(region)
    if not api_id:
        return None
    return api_registry.get_module(api_id)


def _is_configured(region: str) -> bool:
    mod = _module(region)
    if mod is None:
        return False
    fn = getattr(mod, "is_configured", None)
    if callable(fn):
        try:
            return bool(fn())
        except Exception:
            return False
    # Fallback: assume configured if the module loads.
    return True


def _exec(region: str, op_id: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    mod = _module(region)
    if mod is None:
        return {"success": False, "error": f"{region} API not available", "data": None}
    try:
        return mod.execute(op_id, params or {})
    except Exception as exc:  # noqa: BLE001
        return {"success": False, "error": str(exc), "data": None}


def _ok(res: Dict[str, Any]) -> bool:
    """API modules signal success with status == 'ok' (no 'success' key)."""
    if not isinstance(res, dict):
        return False
    if res.get("status") == "ok":
        return True
    if res.get("success"):
        return True
    code = res.get("code")
    return isinstance(code, int) and 200 <= code < 300


def _err(res: Dict[str, Any], fallback: str) -> str:
    """Pull the human error message out of a failed API result."""
    if isinstance(res, dict):
        if res.get("error"):
            return str(res["error"])
        data = res.get("data")
        if isinstance(data, dict) and data.get("error"):
            return str(data["error"])
    return fallback


# ---------------------------------------------------------------------------
# Normalizers — fold each provider's account/transaction shape into a common
# form the UI can render uniformly.
# ---------------------------------------------------------------------------
def _num(*vals: Any) -> Optional[float]:
    for v in vals:
        if v is None or v == "":
            continue
        try:
            return float(v)
        except (TypeError, ValueError):
            continue
    return None


def _first(d: Dict[str, Any], *keys: str) -> Any:
    for k in keys:
        if isinstance(d, dict) and d.get(k) not in (None, ""):
            return d.get(k)
    return None


def _norm_account(region: str, a: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(a, dict):
        return {"id": None, "name": "Account", "type": "", "balance": None, "currency": "", "mask": ""}
    balance = _num(
        a.get("balance"), a.get("currentBalance"), a.get("availableBalance"),
        (a.get("balances") or {}).get("current") if isinstance(a.get("balances"), dict) else None,
        ((a.get("balance") or {}).get("amount") if isinstance(a.get("balance"), dict) else None),
    )
    currency = _first(a, "currency", "currencyCode") or ""
    if not currency and isinstance(a.get("balance"), dict):
        currency = a["balance"].get("currency") or ""
    name = _first(a, "name", "label", "nickname", "displayName", "productName", "type") or "Account"
    mask = _first(a, "accountNumberDisplay", "maskedNumber", "number", "accountNumber") or ""
    if isinstance(mask, str) and len(mask) > 4:
        mask = "••" + mask[-4:]
    return {
        "id": _first(a, "id", "accountId", "account_id"),
        "name": str(name),
        "type": str(_first(a, "type", "accountType", "category") or ""),
        "balance": balance,
        "currency": str(currency),
        "mask": str(mask or ""),
    }


def _norm_txn(region: str, t: Dict[str, Any],
              default_account_id: Optional[str] = None) -> Dict[str, Any]:
    if not isinstance(t, dict):
        return {"date": "", "description": "", "amount": None,
                "currency": "", "account_id": default_account_id}
    amount = _num(
        t.get("amount"),
        ((t.get("amount") or {}).get("value") if isinstance(t.get("amount"), dict) else None),
        ((t.get("transactionAmount") or {}).get("amount") if isinstance(t.get("transactionAmount"), dict) else None),
    )
    # Open Finance Europe (Aiia) reports a positive amount plus a
    # creditDebitIndicator rather than a signed value — fold that into a
    # signed amount so debits render negative like the other regions.
    indicator = str(_first(t, "creditDebitIndicator", "credit_debit_indicator") or "").upper()
    if amount is not None and indicator in ("DEBIT", "DBIT") and amount > 0:
        amount = -amount
    currency = ""
    if isinstance(t.get("amount"), dict):
        currency = t["amount"].get("currency") or ""
    if not currency and isinstance(t.get("transactionAmount"), dict):
        currency = t["transactionAmount"].get("currency") or ""
    currency = currency or _first(t, "currency", "currencyCode") or ""
    date = _first(
        t, "date", "postedDate", "transactionDate", "bookingDate", "valueDate",
        "bookingDateTime", "valueDateTime", "executionDateTime",
    ) or ""
    # Finicity uses epoch seconds for postedDate / transactionDate.
    if isinstance(date, (int, float)) or (isinstance(date, str) and date.isdigit()):
        try:
            date = time.strftime("%Y-%m-%d", time.gmtime(int(date)))
        except (ValueError, OSError):
            date = str(date)
    # EU returns ISO 8601 timestamps (e.g. 2026-05-26T00:00:00Z) — keep the
    # calendar date only.
    if isinstance(date, str) and "T" in date:
        date = date.split("T", 1)[0]
    desc = _first(
        t, "description", "text", "memo", "originalDescription",
        "normalizedPayeeName", "merchantName", "reference",
        "remittanceInformationUnstructured", "remittanceInformation",
        "transactionInformation", "creditorName", "debtorName",
        "proprietaryBankTransactionCode",
    )
    # transactionInformation / remittanceInformation may arrive as a list.
    if isinstance(desc, list):
        desc = " ".join(str(x) for x in desc if x)
    desc = desc or ""
    account_id = _first(t, "accountId", "account_id", "accountKey") or default_account_id
    return {
        "date": str(date),
        "description": str(desc),
        "amount": amount,
        "currency": str(currency),
        "account_id": str(account_id) if account_id else None,
    }


def _extract_accounts(region: str, data: Any) -> List[Dict[str, Any]]:
    if not isinstance(data, dict):
        return []
    raw = data.get("accounts") or data.get("items")
    if not raw and isinstance(data.get("data"), dict):
        raw = data["data"].get("accounts")
    raw = raw or []
    if not isinstance(raw, list):
        return []
    return [_norm_account(region, a) for a in raw]


def _extract_txns(region: str, data: Any,
                  default_account_id: Optional[str] = None) -> List[Dict[str, Any]]:
    if not isinstance(data, dict):
        return []
    raw = data.get("transactions") or data.get("items")
    if not raw and isinstance(data.get("data"), dict):
        raw = data["data"].get("transactions")
    raw = raw or []
    if not isinstance(raw, list):
        return []
    return [_norm_txn(region, t, default_account_id) for t in raw]


# ---------------------------------------------------------------------------
# Public state helpers
# ---------------------------------------------------------------------------
def _public_connection(region: str, conn: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "region": region,
        "connected": bool(conn.get("connected")),
        "bank_name": conn.get("bank_name"),
        "connected_at": conn.get("connected_at"),
        "accounts": conn.get("accounts") or [],
        "transactions": conn.get("transactions") or [],
    }


def get_public_state() -> Dict[str, Any]:
    with _lock:
        state = _load()
    return {
        "regions": [
            {
                "region": r,
                "label": _REGION_BANK[r],
                "enabled": bool(state["enabled"].get(r)),
                "configured": _is_configured(r),
                "connection": _public_connection(r, state["connections"][r]),
            }
            for r in _REGIONS
        ]
    }


def set_enabled(region: str, enabled: bool) -> Dict[str, Any]:
    if region not in _REGIONS:
        return {"success": False, "error": f"unknown region {region!r}"}
    with _lock:
        state = _load()
        state["enabled"][region] = bool(enabled)
        _save(state)
    return {"success": True, "state": get_public_state()}


# ---------------------------------------------------------------------------
# Connect flows — kick off the real hosted bank login per region.
# ---------------------------------------------------------------------------
def start_connect(region: str) -> Dict[str, Any]:
    if region not in _REGIONS:
        return {"success": False, "error": f"unknown region {region!r}"}
    with _lock:
        state = _load()
        if not state["enabled"].get(region):
            return {"success": False, "error": "Region not enabled by admin"}
        conn = state["connections"][region]

    if region == "us":
        cid = conn.get("customer_id")
        if not cid:
            res = _exec("us", "create_test_customer", {})
            if not _ok(res):
                return {"success": False, "error": _err(res, "Could not create customer")}
            cid = (res.get("state_updates") or {}).get("customer_id")
        if not cid:
            return {"success": False, "error": "No customer id available"}
        res = _exec("us", "generate_connect_url", {"customer_id": cid})
        url = (res.get("hints") or {}).get("open_link")
        if not url:
            return {"success": False, "error": _err(res, "No Connect URL returned")}
        with _lock:
            state = _load()
            c = state["connections"]["us"]
            c["customer_id"] = cid
            c["flow_url"] = url
            _save(state)
        return {"success": True, "flow_url": url}

    if region == "au":
        cid = conn.get("customer_id")
        if not cid:
            res = _exec("au", "add_testing_customer", {})
            if not _ok(res):
                return {"success": False, "error": _err(res, "Could not create customer")}
            cid = (res.get("state_updates") or {}).get("customer_id")
        if not cid:
            return {"success": False, "error": "No customer id available"}
        res = _exec("au", "generate_connect_url", {"customer_id": cid})
        url = (res.get("hints") or {}).get("open_link")
        if not url:
            return {"success": False, "error": _err(res, "No Connect URL returned")}
        with _lock:
            state = _load()
            c = state["connections"]["au"]
            c["customer_id"] = cid
            c["flow_url"] = url
            _save(state)
        return {"success": True, "flow_url": url}

    if region == "eu":
        res = _exec("eu", "create_consent", {})
        if not _ok(res):
            return {"success": False, "error": _err(res, "Could not create consent")}
        su = res.get("state_updates") or {}
        consent_id = su.get("consent_id")
        end_user_id = su.get("end_user_id")
        if not consent_id:
            return {"success": False, "error": "No consent id returned"}
        res = _exec("eu", "create_managed_flow", {
            "consent_id": consent_id, "end_user_id": end_user_id,
        })
        url = (res.get("hints") or {}).get("open_link")
        if not url:
            return {"success": False, "error": _err(res, "No flow URL returned")}
        with _lock:
            state = _load()
            c = state["connections"]["eu"]
            c["consent_id"] = consent_id
            c["end_user_id"] = end_user_id
            c["flow_url"] = url
            _save(state)
        return {"success": True, "flow_url": url}

    return {"success": False, "error": "unsupported region"}


def _pull_us(conn: Dict[str, Any]) -> Tuple[bool, List, List, Optional[str]]:
    cid = conn.get("customer_id")
    if not cid:
        return False, [], [], "No customer linked yet"
    # Finicity test customers only expose their accounts after a refresh
    # triggers aggregation — a plain GET returns an empty list until then.
    # Mirror the Finance In Colour use case: refresh first, then read.
    res = _exec("us", "refresh_accounts", {"customer_id": cid})
    accounts = _extract_accounts("us", res.get("data"))
    if not accounts:
        # Fall back to a plain GET in case aggregation already completed
        # on a prior poll (refresh can intermittently 4xx mid-aggregation).
        res = _exec("us", "get_accounts", {"customer_id": cid})
        accounts = _extract_accounts("us", res.get("data"))
    if not accounts:
        return False, [], [], None
    txns: List = []
    res_t = _exec("us", "get_transactions", {"customer_id": cid, "days": 90})
    txns = _extract_txns("us", res_t.get("data"))
    return True, accounts, txns, None


def _pull_au(conn: Dict[str, Any]) -> Tuple[bool, List, List, Optional[str]]:
    cid = conn.get("customer_id")
    if not cid:
        return False, [], [], "No customer linked yet"
    receipt = conn.get("consent_receipt_id")
    if not receipt:
        res = _exec("au", "get_data_sharing_consents", {"customer_id": cid, "status": "ACTIVE"})
        receipt = (res.get("state_updates") or {}).get("consent_receipt_id")
        if not receipt:
            return False, [], [], None
        conn["consent_receipt_id"] = receipt
    res = _exec("au", "get_customer_accounts", {
        "customer_id": cid, "consent_receipt_id": receipt,
    })
    accounts = _extract_accounts("au", res.get("data"))
    if not accounts:
        return False, [], [], None
    return True, accounts, [], None


def _pull_eu(conn: Dict[str, Any]) -> Tuple[bool, List, List, Optional[str]]:
    consent_id = conn.get("consent_id")
    if not consent_id:
        return False, [], [], "No consent created yet"
    res = _exec("eu", "get_accounts", {"consent_id": consent_id})
    accounts = _extract_accounts("eu", res.get("data"))
    if not accounts:
        return False, [], [], None
    conn["account_id"] = accounts[0].get("id")
    # Pull transactions for every account so the UI can show them per-account.
    txns: List = []
    for acct in accounts:
        aid = acct.get("id")
        if not aid:
            continue
        res_t = _exec("eu", "get_transactions", {
            "consent_id": consent_id, "account_id": aid, "limit": 50,
        })
        txns.extend(_extract_txns("eu", res_t.get("data"), default_account_id=aid))
    return True, accounts, txns, None


_PULLERS = {"us": _pull_us, "au": _pull_au, "eu": _pull_eu}


def _do_pull(region: str) -> Dict[str, Any]:
    with _lock:
        state = _load()
        conn = state["connections"][region]
    puller = _PULLERS.get(region)
    if not puller:
        return {"success": False, "error": "unsupported region"}
    connected, accounts, txns, err = puller(conn)
    if err:
        return {"success": False, "error": err, "connected": False}
    if not connected:
        return {"success": True, "connected": False}
    with _lock:
        state = _load()
        c = state["connections"][region]
        # carry over ids discovered during the pull
        for k in ("consent_receipt_id", "account_id"):
            if conn.get(k):
                c[k] = conn[k]
        c["connected"] = True
        c["bank_name"] = c.get("bank_name") or _REGION_BANK[region]
        c["connected_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
        c["accounts"] = accounts
        c["transactions"] = txns
        _save(state)
    return {
        "success": True,
        "connected": True,
        "connection": _public_connection(region, c),
    }


def poll_connect(region: str) -> Dict[str, Any]:
    if region not in _REGIONS:
        return {"success": False, "error": f"unknown region {region!r}"}
    return _do_pull(region)


def refresh(region: str) -> Dict[str, Any]:
    if region not in _REGIONS:
        return {"success": False, "error": f"unknown region {region!r}"}
    return _do_pull(region)
