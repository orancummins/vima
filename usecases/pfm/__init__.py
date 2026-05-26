"""Personal Finance Manager — sample use case.

Composes the Open Finance API to power a phone-style PFM app:
  - Linked account balances
  - Transaction history (last 90 days)
  - Spend-by-category breakdown
"""
from __future__ import annotations

import time
from typing import Any, Dict, List

MANIFEST: Dict[str, Any] = {
    "id": "pfm",
    "name": "Personal Finance Manager",
    "description": (
        "Transform raw transaction data into a rich, real-time money management experience. "
        "By connecting a customer's accounts through the Open Finance API, this use case "
        "delivers live balances, intelligent spend categorisation across dozens of merchant "
        "types, and a full scrollable transaction history — the complete building blocks of "
        "a world-class personal finance app, powered by a single Mastercard integration."
    ),
    "apis": ["open_finance"],
    "render": "pfm",
}


def _client():
    # Defer import so the registry doesn't fail when OFIN isn't configured.
    from apis.open_finance import api as ofin_api
    return ofin_api._get_client()


def _categorize(txn: Dict[str, Any]) -> str:
    cat = (txn.get("categorization") or {}).get("category")
    if cat:
        return cat
    if txn.get("amount", 0) > 0:
        return "Income"
    return "Other"


def get_data(customer_id: str) -> Dict[str, Any]:
    """Fetch and shape data for the PFM dashboard."""
    client = _client()

    # Accounts
    acct_resp, acct_status = client.get_customer_accounts(customer_id)
    if acct_status >= 400 or not isinstance(acct_resp, dict):
        return {"error": "Could not load accounts", "status": acct_status, "detail": acct_resp}
    accounts = acct_resp.get("accounts", []) or []

    # Transactions (last 90 days)
    now = int(time.time())
    past = now - 90 * 24 * 3600
    txn_resp, txn_status = client.get_customer_transactions(customer_id, past, now, limit=500)
    transactions = []
    if isinstance(txn_resp, dict) and txn_status < 400:
        transactions = txn_resp.get("transactions", []) or []

    # Sort transactions by date descending
    transactions.sort(key=lambda t: t.get("transactionDate", 0), reverse=True)

    # Shape accounts
    shaped_accounts: List[Dict[str, Any]] = []
    for a in accounts:
        shaped_accounts.append({
            "id": str(a.get("id")),
            "name": a.get("name") or "Account",
            "type": a.get("type") or "",
            "balance": float(a.get("balance") or 0),
            "available_balance": float(a.get("availableBalance") or a.get("balance") or 0),
            "currency": a.get("currency") or "USD",
            "number": a.get("number") or "",
            "institution": a.get("institutionName") or "",
        })

    # Net worth & balance buckets
    asset_types = {"checking", "savings", "investment", "moneyMarket", "cd"}
    liability_types = {"loan", "mortgage", "creditCard", "lineOfCredit"}
    assets = sum(a["balance"] for a in shaped_accounts if a["type"] in asset_types)
    liabilities = sum(a["balance"] for a in shaped_accounts if a["type"] in liability_types)
    net_worth = assets + liabilities  # liabilities are already negative

    # Spend by category (debits only)
    cat_totals: Dict[str, float] = {}
    monthly_spend = 0.0
    monthly_income = 0.0
    now_dt = now
    one_month = now_dt - 30 * 24 * 3600

    shaped_txns: List[Dict[str, Any]] = []
    for t in transactions:
        amt = float(t.get("amount") or 0)
        ts = int(t.get("transactionDate") or 0)
        cat = _categorize(t)
        norm_name = ((t.get("categorization") or {}).get("normalizedPayeeName")
                     or t.get("description") or "Transaction")
        shaped_txns.append({
            "id": str(t.get("id")),
            "amount": amt,
            "date": ts,
            "name": norm_name,
            "category": cat,
            "description": t.get("description") or "",
            "status": t.get("status") or "posted",
            "account_id": str(t.get("accountId") or ""),
        })
        if ts >= one_month:
            if amt < 0:
                cat_totals[cat] = cat_totals.get(cat, 0) + abs(amt)
                monthly_spend += abs(amt)
            else:
                monthly_income += amt

    # Top categories sorted by spend
    top_categories = [
        {"category": k, "amount": round(v, 2),
         "pct": round((v / monthly_spend * 100) if monthly_spend else 0, 1)}
        for k, v in sorted(cat_totals.items(), key=lambda kv: kv[1], reverse=True)
    ]

    return {
        "customer_id": customer_id,
        "accounts": shaped_accounts,
        "transactions": shaped_txns[:50],
        "summary": {
            "assets": round(assets, 2),
            "liabilities": round(liabilities, 2),
            "net_worth": round(net_worth, 2),
            "monthly_spend": round(monthly_spend, 2),
            "monthly_income": round(monthly_income, 2),
        },
        "categories": top_categories,
    }


def do_action(action: str, params: Dict[str, Any]) -> Dict[str, Any]:
    """Backend actions for the PFM use case (used by the in-app Connect flow)."""
    client = _client()

    if action == "create_customer":
        # Create a sandbox testing customer with a random username.
        import secrets
        username = params.get("username") or f"vima_{secrets.token_hex(4)}"
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
        return {
            "link": data.get("link"),
            "connect_url": data.get("link"),
        }

    if action == "refresh_accounts":
        customer_id = params.get("customer_id")
        if not customer_id:
            return {"error": "'customer_id' is required"}
        data, status = client.refresh_customer_accounts(str(customer_id))
        # 200 or 204 are both fine; ignore body
        if status >= 400:
            return {"error": "Could not refresh accounts", "status": status, "detail": data}
        return {"ok": True}

    if action == "enrich_transactions":
        import datetime
        transactions = params.get("transactions") or []
        if not transactions:
            return {"enriched": {}}
        api_txns = []
        for t in transactions[:50]:
            if not t.get("id") or not t.get("description"):
                continue
            ts = t.get("date", 0)
            try:
                ts_str = datetime.datetime.utcfromtimestamp(int(ts)).strftime("%Y-%m-%dT%H:%M:%SZ")
            except Exception:
                ts_str = "2026-01-01T00:00:00Z"
            api_txns.append({
                "externalCustomerId": "pfm_enrich",
                "externalAccountId": str(t.get("account_id") or "pfm_acct"),
                "accountType": "checking",
                "externalTransactionId": str(t["id"]),
                "transactionTimestamp": ts_str,
                "description": str(t["description"]),
                "amount": float(t.get("amount") or 0),
                "directionIndicator": "credit" if float(t.get("amount") or 0) > 0 else "debit",
            })
        if not api_txns:
            return {"enriched": {}}
        data, status = client.enrich_transactions(api_txns)
        if status >= 400 or not isinstance(data, dict):
            return {"error": f"Enrichment API returned {status}", "enriched": {}}
        enriched: Dict[str, Any] = {}
        for t in (data.get("transactions") or []):
            txn_id = t.get("externalTransactionId")
            if not txn_id:
                continue
            entities: list = t.get("entities") or []
            primary = entities[0] if entities else {}
            enriched[txn_id] = {
                "name": primary.get("name"),
                "logoUrl": primary.get("logoUrl"),
                "isRecurring": bool(t.get("isRecurringTransaction")),
                "category": t.get("transactionCategory"),
            }
        return {"enriched": enriched}

    if action == "get_recurring":
        customer_id = params.get("customer_id", "").strip()
        if not customer_id:
            return {"error": "customer_id is required"}
        from usecases.recurring import _parse_stream
        # The API requires account IDs — fetch them first
        acct_data, acct_status = client.get_customer_accounts(customer_id)
        account_ids: list = []
        if acct_status < 400:
            account_ids = [str(a["id"]) for a in (acct_data.get("accounts") or []) if a.get("id")]
        data, status = client.get_recurring_transactions(customer_id, account_ids or None)
        if status >= 400:
            return {"error": f"API returned {status}", "detail": data}
        crt = data.get("customerRecurringTransactions") or {}
        raw_debits = crt.get("recurringOutflows") or []
        raw_credits = crt.get("recurringInflows") or []
        debits = [_parse_stream(s, "DEBIT") for s in raw_debits]
        credits = [_parse_stream(s, "CREDIT") for s in raw_credits]
        debits.sort(key=lambda s: -abs(s["amount"]))
        credits.sort(key=lambda s: -abs(s["amount"]))
        return {"streams": credits + debits, "total": len(debits) + len(credits)}

    return {"error": f"Unknown action: {action}"}
