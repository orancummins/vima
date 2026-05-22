"""Payment Success Indicator — use case.

Calls the Open Finance PSI API to evaluate the likelihood of a chosen ACH
transaction succeeding or returning as NSF/unauthorized over an n-day
settlement window (n = the number of dailyResults the API returns).
Results are shaped for a day-by-day settlement confidence timeline in the UI.
"""
from __future__ import annotations

import time
from typing import Any, Dict, List, Optional

MANIFEST: Dict[str, Any] = {
    "id": "psi",
    "name": "Payment Success Indicator",
    "description": (
        "Every ACH payment carries settlement risk — but it doesn't have to be a gamble. "
        "Payment Success Indicator applies machine learning to consumer-permissioned bank data "
        "to deliver a real-time per-day probability score across the full settlement window, "
        "alongside a dedicated unauthorised-return fraud signal. Lenders and payment processors "
        "can move confidently, approve more good payments, and dramatically cut costly return rates "
        "— all from a single, low-friction API call before a transaction is ever submitted."
    ),
    "apis": ["ofin"],
    "render": "psi",
}


def _client():
    from apis.ofin import api as ofin_api
    return ofin_api._get_client()


def do_action(action: str, params: Dict[str, Any]) -> Dict[str, Any]:
    client = _client()

    # ------------------------------------------------------------------
    # get_accounts — returns checking/savings accounts for a customer
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
                "id":       str(a["id"]),
                "name":     a.get("name", "Account"),
                "type":     a.get("type", ""),
                "number":   a.get("number", ""),
                "balance":  a.get("balance"),
                "currency": a.get("currency", "USD"),
            }
            for a in (data.get("accounts") or [])
            if a.get("type") in eligible_types
        ]
        return {"accounts": accounts}

    # ------------------------------------------------------------------
    # score — call PSI for a given customer/account/amount
    # ------------------------------------------------------------------
    elif action == "score":
        customer_id = params.get("customer_id", "").strip()
        account_id  = params.get("account_id",  "").strip()
        amount      = float(params.get("amount", 100.0))
        if not customer_id or not account_id:
            return {"error": "customer_id and account_id are required"}
        if amount <= 0:
            return {"error": "amount must be greater than zero"}

        data, status = client.generate_payment_success_indicators(
            customer_id, account_id, amount
        )
        if status >= 400:
            return {"error": f"PSI API returned {status}", "detail": data}

        # Poll if async
        pay_request_id: Optional[str] = data.get("payRequestId")
        for _ in range(8):
            if data.get("status") == "SUCCESS":
                break
            if pay_request_id and data.get("status") == "IN PROGRESS":
                time.sleep(1.2)
                data, status = client.get_payment_success_indicators(
                    customer_id, account_id, pay_request_id
                )
            else:
                break

        return {"result": _shape_result(data)}

    return {"error": f"Unknown action: {action}"}


# ---------------------------------------------------------------------------
# Shape the raw PSI response into a frontend-friendly dict
# ---------------------------------------------------------------------------
def _shape_result(raw: Dict[str, Any]) -> Dict[str, Any]:
    nsf      = raw.get("nsfReturnRisk")    or {}
    unauth   = raw.get("unauthorizedReturnRisk") or {}
    nsf_res  = nsf.get("result")   or {}
    unauth_res = unauth.get("result") or {}

    daily_raw: List[Dict] = nsf_res.get("dailyResults") or []
    daily: List[Dict[str, Any]] = []
    for d in daily_raw:
        nsf_score  = d.get("score", 0)
        confidence = round(100 - nsf_score, 1)
        indicator  = d.get("indicator", "")
        risk_level = _indicator_level(indicator)
        reasons    = d.get("reasons") or {}
        daily.append({
            "date":        d.get("potentialSettlementDate", ""),
            "nsfScore":    nsf_score,
            "confidence":  confidence,
            "indicator":   indicator,
            "riskLevel":   risk_level,   # "low" | "medium" | "high"
            "reasons": {
                "recentBalance":    reasons.get("recentBalance",    0),
                "balanceHistory":   reasons.get("balanceHistory",   0),
                "nsfHistory":       reasons.get("nsfHistory",       0),
                "recentNsfHistory": reasons.get("recentNsfHistory", 0),
                "recurringNsf":     reasons.get("recurringNsf",     0),
                "spendHistory":     reasons.get("spendHistory",     0),
                "depositHistory":   reasons.get("depositHistory",   0),
                "transactionAmount":reasons.get("transactionAmount",0),
            },
        })

    unauth_score = unauth_res.get("score")
    unauth_ind   = unauth_res.get("indicator", "")

    return {
        "customerId":       raw.get("customerId"),
        "accountId":        raw.get("accountId"),
        "requestDate":      raw.get("requestDate"),
        "settleByDate":     (raw.get("transaction") or {}).get("settleByDate"),
        "amount":           (raw.get("transaction") or {}).get("amount"),
        "availableBalance": nsf_res.get("availableBalance"),
        "dailyResults":     daily,
        "windowDays":       len(daily),   # actual n — not assumed to be 10
        "nsfError":         nsf.get("error"),
        "unauthorizedReturnRisk": {
            "score":     unauth_score,
            "indicator": unauth_ind,
            "riskLevel": _indicator_level(unauth_ind),
        } if unauth_score is not None else None,
    }


def _indicator_level(indicator: str) -> str:
    ind = (indicator or "").lower()
    if "high" in ind:
        return "high"
    if "medium" in ind or "med" in ind:
        return "medium"
    return "low"
