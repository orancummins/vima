"""Recurring Transactions — use case.

Calls the Open Finance Recurring Transactions API to identify repeating debit
and credit patterns across a customer's accounts.  Results are shaped into a
stream-card structure for the UI.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional

MANIFEST: Dict[str, Any] = {
    "id": "recurring",
    "name": "Recurring Transactions",
    "description": (
        "Subscriptions are growing — and so is subscription fatigue. The Open Finance "
        "Recurring Transactions API automatically surfaces every repeating debit and credit "
        "across a customer's connected accounts: from streaming services and gym memberships "
        "to salary credits and mortgage payments. Each detected stream includes merchant name, "
        "recurrence frequency, average amount, and the next expected date — giving consumers "
        "full visibility and empowering them to take control of their financial commitments."
    ),
    "apis": ["open_finance", "automatic_billing_updater", "transaction_notifications", "consent_management"],
    "render": "recurring",
}


def _client():
    from apis.open_finance import api as ofin_api
    return ofin_api._get_client()


def _cadence_to_frequency(cadence: Optional[int]) -> str:
    """Convert mean-days-between-transactions to a human frequency label."""
    if cadence is None:
        return "UNKNOWN"
    if cadence <= 9:
        return "WEEKLY"
    if cadence <= 18:
        return "BIWEEKLY"
    if cadence <= 45:
        return "MONTHLY"
    if cadence <= 75:
        return "BIMONTHLY"
    if cadence <= 180:
        return "QUARTERLY"
    return "ANNUAL"


def _parse_stream(s: Dict[str, Any], stream_type: str) -> Dict[str, Any]:
    """Normalise a raw recurringOutflow / recurringInflow object."""
    categories: List[str] = s.get("transactionCategories") or []
    return {
        "merchantName":      s.get("normalizedPayeeName") or "Unknown",
        "type":              stream_type,          # "DEBIT" or "CREDIT"
        "frequency":         _cadence_to_frequency(s.get("cadence")),
        "cadence":           s.get("cadence"),     # mean days between txns
        "category":          categories[0] if categories else "",
        "amount":            (
                                 s.get("expectedNextTransactionAmount")
                                 or s.get("meanHistoricalAmount")
                                 or 0
                             ),
        "meanAmount":        s.get("meanHistoricalAmount"),
        "minAmount":         s.get("minimumHistoricalAmount"),
        "maxAmount":         s.get("maximumHistoricalAmount"),
        "nextExpectedDate":  s.get("expectedNextTransactionDate", ""),
        "count":             s.get("countOfTransactions", 0),
        "status":            s.get("status", ""),
    }


def do_action(action: str, params: Dict[str, Any]) -> Dict[str, Any]:
    client = _client()

    # ------------------------------------------------------------------
    # get_accounts — return checking/savings accounts for a customer
    # ------------------------------------------------------------------
    if action == "get_accounts":
        customer_id = params.get("customer_id", "").strip()
        if not customer_id:
            return {"error": "customer_id is required"}
        data, status = client.get_customer_accounts(customer_id)
        if status >= 400:
            return {"error": f"API returned {status}", "detail": data}
        eligible_types = {"checking", "savings", "moneyMarket"}
        accounts: List[Dict[str, Any]] = [
            {
                "id":     str(a["id"]),
                "name":   a.get("name", "Account"),
                "type":   a.get("type", ""),
                "number": a.get("number", ""),
            }
            for a in (data.get("accounts") or [])
            if a.get("type") in eligible_types
        ]
        return {"accounts": accounts}

    # ------------------------------------------------------------------
    # get_recurring — fetch recurring transaction streams
    # ------------------------------------------------------------------
    elif action == "get_recurring":
        customer_id = params.get("customer_id", "").strip()
        if not customer_id:
            return {"error": "customer_id is required"}

        # Optional account filter — comma-separated IDs become a list
        raw_ids = params.get("account_ids", "")
        account_ids: Optional[List[str]] = None
        if raw_ids:
            account_ids = [x.strip() for x in str(raw_ids).split(",") if x.strip()]

        data, status = client.get_recurring_transactions(customer_id, account_ids)
        if status >= 400:
            return {"error": f"API returned {status}", "detail": data}

        # Response shape:
        # {
        #   "customerRecurringTransactions": {
        #     "recurringOutflows": [...],   ← debits
        #     "recurringInflows":  [...]    ← credits
        #   },
        #   "accountRecurringTransactions": [{ "accountId": ..., "recurringOutflows": ..., "recurringInflows": ... }]
        # }
        crt = data.get("customerRecurringTransactions") or {}
        raw_debits  = crt.get("recurringOutflows") or []
        raw_credits = crt.get("recurringInflows")  or []

        debits  = [_parse_stream(s, "DEBIT")  for s in raw_debits]
        credits = [_parse_stream(s, "CREDIT") for s in raw_credits]

        # Sort each group by amount descending
        debits.sort(key=lambda s: -abs(s["amount"]))
        credits.sort(key=lambda s: -abs(s["amount"]))

        streams = credits + debits
        return {"streams": streams, "total": len(streams)}

    # ------------------------------------------------------------------
    # get_transactions — fetch recent transactions for one account
    # ------------------------------------------------------------------
    elif action == "get_transactions":
        import time
        customer_id = params.get("customer_id", "").strip()
        account_id  = params.get("account_id", "").strip()
        if not customer_id or not account_id:
            return {"error": "customer_id and account_id are required"}
        to_date   = int(time.time())
        from_date = to_date - 90 * 86400  # last 90 days
        data, status = client.get_account_transactions(
            customer_id, account_id, from_date, to_date, 1, 500
        )
        if status >= 400:
            return {"error": f"API returned {status}", "detail": data}
        raw_txns = data.get("transactions") or []
        transactions = []
        for t in raw_txns:
            cat = t.get("categorization") or {}
            transactions.append({
                "id":            t.get("id"),
                "description":   t.get("description", ""),
                "normalizedPayee": cat.get("normalizedPayeeName", ""),
                "category":      cat.get("category", ""),
                "amount":        t.get("amount", 0),
                "date":          t.get("postedDate") or t.get("transactionDate") or 0,
            })
        transactions.sort(key=lambda x: -(x["date"] or 0))
        return {"transactions": transactions}

    return {"error": f"Unknown action: {action}"}

