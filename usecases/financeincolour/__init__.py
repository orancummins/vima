"""Finance In Colour — sample use case.

Turns a customer's transaction history into a richly coloured, behaviour-
driven visualisation:

  - A money in vs money out flow chart over time
  - A category-spend breakdown with distinctive colours per category
  - A trend indicator showing whether spending is accelerating / cooling
  - A generative "financial fingerprint" — an abstract graphic whose
    shape, colours and rhythm are derived from the customer's own
    behaviour, so the picture itself says something about who they are.

The data shape mirrors the PFM use case (so the front-end can lean on
the same Open Finance endpoints) but adds a daily time-series and a
fingerprint summary tailored to the visualisations.
"""
from __future__ import annotations

import time
from typing import Any, Dict, List


MANIFEST: Dict[str, Any] = {
    "id": "financeincolour",
    "name": "Finance In Colour",
    "description": (
        "Finance In Colour translates raw Open Finance transactions into a "
        "single, expressive picture of how a customer earns, spends and "
        "behaves over time. Money in and money out flow across a tinted "
        "timeline, spending is broken down by category in vivid colour, a "
        "trend gauge reveals whether outgoings are heating up or cooling "
        "down, and a generative \"financial fingerprint\" composes all of "
        "the above into one personalised graphic — so a single glance "
        "tells you who this customer is, financially."
    ),
    "apis": ["ofin"],
    "render": "financeincolour",
}


def _client():
    from apis.ofin import api as ofin_api
    return ofin_api._get_client()


def _categorize(txn: Dict[str, Any]) -> str:
    cat = (txn.get("categorization") or {}).get("category")
    if cat:
        return cat
    if txn.get("amount", 0) > 0:
        return "Income"
    return "Other"


def _day_key(ts: int) -> str:
    # YYYY-MM-DD in UTC for grouping
    import datetime
    try:
        return datetime.datetime.utcfromtimestamp(int(ts)).strftime("%Y-%m-%d")
    except Exception:
        return "1970-01-01"


def get_data(customer_id: str) -> Dict[str, Any]:
    """Fetch and shape data for the Finance In Colour dashboard."""
    client = _client()

    # Customer profile (name)
    customer_name = None
    try:
        cust_resp, cust_status = client.get_customer(customer_id)
        if cust_status < 400 and isinstance(cust_resp, dict):
            first = cust_resp.get("firstName") or ""
            last  = cust_resp.get("lastName")  or ""
            full  = f"{first} {last}".strip()
            customer_name = full or cust_resp.get("username") or None
    except Exception:
        pass

    # Accounts (for net worth + currency hints)
    acct_resp, acct_status = client.get_customer_accounts(customer_id)
    if acct_status >= 400 or not isinstance(acct_resp, dict):
        return {"error": "Could not load accounts", "status": acct_status, "detail": acct_resp}
    accounts = acct_resp.get("accounts", []) or []
    # If no accounts yet, the bank link is still aggregating. Surface this as
    # a retryable error so the front-end can keep polling.
    if not accounts:
        return {"error": "No accounts linked yet", "status": 202, "pending": True}

    # Transactions — last 90 days
    now = int(time.time())
    past = now - 90 * 24 * 3600
    txn_resp, txn_status = client.get_customer_transactions(customer_id, past, now, limit=500)
    transactions = []
    if isinstance(txn_resp, dict) and txn_status < 400:
        transactions = txn_resp.get("transactions", []) or []

    transactions.sort(key=lambda t: t.get("transactionDate", 0))

    currency = "USD"
    for a in accounts:
        if a.get("currency"):
            currency = a.get("currency")
            break

    # ── Daily flow series ─────────────────────────────────────────────
    daily: Dict[str, Dict[str, float]] = {}
    cat_totals: Dict[str, float] = {}
    total_in = 0.0
    total_out = 0.0
    txn_count_in = 0
    txn_count_out = 0
    shaped_txns: List[Dict[str, Any]] = []

    for t in transactions:
        amt = float(t.get("amount") or 0)
        ts = int(t.get("transactionDate") or 0)
        cat = _categorize(t)
        day = _day_key(ts)
        d = daily.setdefault(day, {"in": 0.0, "out": 0.0})
        if amt >= 0:
            d["in"] += amt
            total_in += amt
            txn_count_in += 1
        else:
            d["out"] += abs(amt)
            total_out += abs(amt)
            txn_count_out += 1
            cat_totals[cat] = cat_totals.get(cat, 0.0) + abs(amt)
        shaped_txns.append({
            "id": str(t.get("id")),
            "amount": amt,
            "date": ts,
            "day": day,
            "name": ((t.get("categorization") or {}).get("normalizedPayeeName")
                     or t.get("description") or "Transaction"),
            "category": cat,
        })

    # Fill in zero-value days so the chart has a continuous x-axis
    import datetime
    series: List[Dict[str, Any]] = []
    start_dt = datetime.datetime.utcfromtimestamp(past).date()
    end_dt = datetime.datetime.utcfromtimestamp(now).date()
    cur = start_dt
    while cur <= end_dt:
        key = cur.strftime("%Y-%m-%d")
        d = daily.get(key, {"in": 0.0, "out": 0.0})
        series.append({
            "day": key,
            "in": round(d["in"], 2),
            "out": round(d["out"], 2),
            "net": round(d["in"] - d["out"], 2),
        })
        cur += datetime.timedelta(days=1)

    # ── Categories sorted by spend ────────────────────────────────────
    categories = [
        {
            "category": k,
            "amount": round(v, 2),
            "pct": round((v / total_out * 100) if total_out else 0, 1),
        }
        for k, v in sorted(cat_totals.items(), key=lambda kv: kv[1], reverse=True)
    ]

    # ── Trend: compare last 30 days vs the previous 30 days ───────────
    cutoff_recent = now - 30 * 24 * 3600
    cutoff_prior = now - 60 * 24 * 3600
    recent_out = 0.0
    prior_out = 0.0
    recent_in = 0.0
    prior_in = 0.0
    for t in transactions:
        amt = float(t.get("amount") or 0)
        ts = int(t.get("transactionDate") or 0)
        if ts >= cutoff_recent:
            if amt < 0: recent_out += abs(amt)
            else:       recent_in  += amt
        elif ts >= cutoff_prior:
            if amt < 0: prior_out += abs(amt)
            else:       prior_in  += amt

    def _pct_change(now_v: float, prev_v: float) -> float:
        if prev_v <= 0:
            return 0.0 if now_v <= 0 else 100.0
        return round((now_v - prev_v) / prev_v * 100, 1)

    spend_change = _pct_change(recent_out, prior_out)
    income_change = _pct_change(recent_in, prior_in)
    if spend_change > 8:
        trend = "rising"
    elif spend_change < -8:
        trend = "cooling"
    else:
        trend = "steady"

    # ── Financial fingerprint metrics ─────────────────────────────────
    # These drive the generative "who you are" graphic on the front end.
    savings_rate = 0.0
    if total_in > 0:
        savings_rate = max(min((total_in - total_out) / total_in, 1.0), -1.0)

    # Volatility = stddev of daily net / mean abs daily flow
    nets = [s["net"] for s in series]
    flows = [s["in"] + s["out"] for s in series]
    mean_flow = (sum(flows) / len(flows)) if flows else 0.0
    if nets and mean_flow > 0:
        mean_net = sum(nets) / len(nets)
        var = sum((n - mean_net) ** 2 for n in nets) / len(nets)
        volatility = round((var ** 0.5) / mean_flow, 3)
    else:
        volatility = 0.0

    # Diversity = number of distinct categories with >2% share
    diversity = sum(1 for c in categories if c["pct"] >= 2.0)

    # Top category share (concentration)
    top_share = categories[0]["pct"] if categories else 0.0

    fingerprint = {
        "savings_rate": round(savings_rate, 3),
        "volatility": volatility,
        "diversity": diversity,
        "top_share": top_share,
        "spend_change": spend_change,
        "income_change": income_change,
        "trend": trend,
        "txn_per_day": round((txn_count_in + txn_count_out) / max(len(series), 1), 2),
    }

    return {
        "customer_id": customer_id,
        "customer_name": customer_name,
        "currency": currency,
        "range_days": 90,
        "series": series,
        "categories": categories,
        "transactions": shaped_txns[-100:][::-1],  # newest first, capped
        "summary": {
            "total_in": round(total_in, 2),
            "total_out": round(total_out, 2),
            "net": round(total_in - total_out, 2),
            "txn_count_in": txn_count_in,
            "txn_count_out": txn_count_out,
        },
        "trend": {
            "label": trend,
            "spend_change_pct": spend_change,
            "income_change_pct": income_change,
            "recent_out": round(recent_out, 2),
            "prior_out": round(prior_out, 2),
            "recent_in": round(recent_in, 2),
            "prior_in": round(prior_in, 2),
        },
        "fingerprint": fingerprint,
    }


def do_action(action: str, params: Dict[str, Any]) -> Dict[str, Any]:
    """Backend actions for the Finance In Colour connect flow."""
    client = _client()

    if action == "create_customer":
        import secrets
        username = params.get("username") or f"fic_{secrets.token_hex(4)}"
        data, status = client.add_testing_customer(username)
        if status >= 400 or not isinstance(data, dict):
            return {"error": "Could not create customer", "status": status, "detail": data}
        return {
            "customer_id": str(data.get("id")),
            "username": data.get("username") or username,
        }

    if action == "connect_url":
        customer_id = params.get("customer_id")
        if not customer_id:
            return {"error": "'customer_id' is required"}
        data, status = client.generate_connect_url(str(customer_id))
        if status >= 400 or not isinstance(data, dict):
            return {"error": "Could not generate Connect URL", "status": status, "detail": data}
        return {"connect_url": data.get("link")}

    if action == "refresh_accounts":
        customer_id = params.get("customer_id")
        if not customer_id:
            return {"error": "'customer_id' is required"}
        data, status = client.refresh_customer_accounts(str(customer_id))
        if status >= 400:
            return {"error": "Could not refresh accounts", "status": status, "detail": data}
        return {"ok": True}

    return {"error": f"Unknown action: {action}"}
