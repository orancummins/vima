import uuid
import time
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from flask import request, jsonify
from simulator.datastore import store

API = "open_finance"
_FIXTURE_PATH = Path(__file__).parents[1] / "fixtures" / "open_finance.json"
_FIXTURE_CACHE: dict | None = None


def _fixture_records(resource: str) -> list[dict]:
    global _FIXTURE_CACHE
    if _FIXTURE_CACHE is None:
        try:
            _FIXTURE_CACHE = json.loads(_FIXTURE_PATH.read_text())
        except (OSError, json.JSONDecodeError):
            _FIXTURE_CACHE = {}
    records = _FIXTURE_CACHE.get(resource) if isinstance(_FIXTURE_CACHE, dict) else []
    return records if isinstance(records, list) else []


def _safe_float(value, default=0.0):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _indicator(risk_score: float) -> str:
    if risk_score >= 70:
        return "HIGH"
    if risk_score >= 35:
        return "MEDIUM"
    return "LOW"


def _clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def _find_account(customer_id: str, account_id: str) -> dict:
    store.lazy_load(API)
    account = store.get(API, "accounts", account_id)
    if account:
        return account
    accounts = [
        a for a in store.list(API, "accounts")
        if str(a.get("customerId")) == str(customer_id)
    ]
    if accounts:
        return accounts[0]
    fixture_accounts = _fixture_records("accounts")
    account = next((a for a in fixture_accounts if str(a.get("id")) == str(account_id)), None)
    if account:
        return account
    account = next((a for a in fixture_accounts if str(a.get("customerId")) == str(customer_id)), None)
    return account or {"id": account_id, "customerId": customer_id, "balance": 0.0}


def _account_transactions(account_id: str) -> list[dict]:
    txns = [
        t for t in store.list(API, "transactions")
        if str(t.get("accountId")) == str(account_id)
    ]
    if txns:
        return txns
    fixture_txns = [
        t for t in _fixture_records("transactions")
        if str(t.get("accountId")) == str(account_id)
    ]
    return fixture_txns or store.list(API, "transactions")[:10] or _fixture_records("transactions")[:10]


def _build_psi_result(customer_id: str, account_id: str, amount: float, settle_by_date: str | None) -> dict:
    account = _find_account(customer_id, account_id)
    txns = _account_transactions(str(account.get("id") or account_id))
    balance = _safe_float(account.get("availableBalance", account.get("balance")), 0.0)
    amount = max(_safe_float(amount, 0.0), 0.0)

    credits = [_safe_float(t.get("amount")) for t in txns if _safe_float(t.get("amount")) > 0]
    debits = [abs(_safe_float(t.get("amount"))) for t in txns if _safe_float(t.get("amount")) < 0]
    avg_credit = sum(credits) / len(credits) if credits else 0.0
    monthly_debits = sum(debits)
    daily_spend = _clamp(monthly_debits / 30.0, 8.0, 180.0) if monthly_debits else 25.0
    large_debit_pressure = _clamp((max(debits) if debits else 0.0) / max(balance, 1.0) * 100.0, 0.0, 45.0)
    today = datetime.now(timezone.utc).date()

    daily_results = []
    for day in range(1, 11):
        projected_balance = balance - (daily_spend * day)
        if avg_credit and day >= 5:
            projected_balance += avg_credit

        coverage_ratio = amount / max(projected_balance, 1.0)
        shortfall = max(amount - projected_balance, 0.0)
        shortfall_ratio = shortfall / max(amount, 1.0)

        if shortfall > 0:
            risk_score = 72.0 + (shortfall_ratio * 24.0)
        elif coverage_ratio >= 0.85:
            risk_score = 50.0 + ((coverage_ratio - 0.85) / 0.15 * 18.0)
        elif coverage_ratio >= 0.55:
            risk_score = 28.0 + ((coverage_ratio - 0.55) / 0.30 * 20.0)
        else:
            risk_score = 8.0 + (coverage_ratio * 28.0)

        risk_score += large_debit_pressure * 0.25
        risk_score += min(day * 0.9, 8.0)
        risk_score = round(_clamp(risk_score, 2.0, 98.0), 1)
        success_score = round(100.0 - risk_score, 1)

        daily_results.append({
            "potentialSettlementDate": (today + timedelta(days=day)).isoformat(),
            "score": success_score,
            "indicator": _indicator(risk_score),
            "reasons": {
                "recentBalance": round(_clamp(100.0 - (projected_balance / max(amount, 1.0) * 45.0), 0.0, 100.0), 1),
                "balanceHistory": round(_clamp(28.0 + large_debit_pressure, 0.0, 100.0), 1),
                "nsfHistory": round(_clamp(shortfall_ratio * 80.0, 0.0, 100.0), 1),
                "recentNsfHistory": round(_clamp(shortfall_ratio * 65.0, 0.0, 100.0), 1),
                "recurringNsf": round(_clamp(shortfall_ratio * 55.0, 0.0, 100.0), 1),
                "spendHistory": round(_clamp((daily_spend / max(balance, 1.0)) * 900.0, 0.0, 100.0), 1),
                "depositHistory": round(_clamp(55.0 - (avg_credit / max(amount, 1.0) * 12.0), 0.0, 100.0), 1),
                "transactionAmount": round(_clamp(coverage_ratio * 85.0, 0.0, 100.0), 1),
            },
        })

    first_score = daily_results[0]["score"] if daily_results else 0.0
    unauth_risk_score = round(_clamp(6.0 + (amount / max(balance, 1.0) * 10.0) + large_debit_pressure * 0.12, 2.0, 42.0), 1)
    unauth_score = round(100.0 - unauth_risk_score, 1)
    pay_request_id = str(uuid.uuid4())

    return {
        "payRequestId": pay_request_id,
        "status": "SUCCESS",
        "customerId": str(customer_id),
        "accountId": str(account_id),
        "requestDate": today.isoformat(),
        "transaction": {
            "settleByDate": settle_by_date or (today + timedelta(days=3)).isoformat(),
            "amount": amount,
        },
        "nsfReturnRisk": {
            "score": first_score,
            "indicator": daily_results[0]["indicator"] if daily_results else "LOW",
            "result": {
                "availableBalance": round(balance, 2),
                "dailyResults": daily_results,
            },
        },
        "unauthorizedReturnRisk": {
            "score": unauth_score,
            "indicator": _indicator(unauth_risk_score),
            "result": {
                "score": unauth_score,
                "indicator": _indicator(unauth_risk_score),
            },
        },
    }


def register(bp):
    # ── Authentication ────────────────────────────────────────────────────────
    @bp.route("/open_finance/aggregation/v2/partners/authentication", methods=["POST"])
    def partner_auth():
        return jsonify({"token": "sim_token_abc123", "expiresAt": "2026-12-31T00:00:00Z"})

    # ── Customers ─────────────────────────────────────────────────────────────
    @bp.route("/open_finance/aggregation/v2/customers/testing", methods=["POST"])
    def create_customer():
        store.lazy_load(API)
        body = request.get_json(force=True) or {}
        cust_id = str(int(time.time() * 1000) % 10_000_000_000)
        customer = {
            "id": cust_id,
            "username": body.get("username", f"user_{cust_id}"),
            "type": "testing",
            "createdDate": int(time.time()),
            "firstName": body.get("firstName", "Test"),
            "lastName": body.get("lastName", "User"),
        }
        store.put(API, "customers", cust_id, customer)
        return jsonify(customer), 201

    @bp.route("/open_finance/aggregation/v1/customers", methods=["GET"])
    def list_customers():
        store.lazy_load(API)
        customers = store.list(API, "customers")
        return jsonify({"found": len(customers), "customers": customers})

    @bp.route("/open_finance/aggregation/v1/customers/<customer_id>", methods=["GET"])
    def get_customer(customer_id):
        store.lazy_load(API)
        rec = store.get(API, "customers", customer_id)
        if rec is None:
            customers = store.list(API, "customers")
            rec = next((c for c in customers if c.get("id") == customer_id),
                       customers[0] if customers else {"id": customer_id})
        return jsonify(rec)

    # ── Accounts ──────────────────────────────────────────────────────────────
    @bp.route("/open_finance/aggregation/v1/customers/<customer_id>/accounts", methods=["GET"])
    def list_customer_accounts(customer_id):
        store.lazy_load(API)
        all_accounts = store.list(API, "accounts")
        accounts = [a for a in all_accounts if str(a.get("customerId")) == str(customer_id)]
        if not accounts:
            accounts = all_accounts[:2]
        return jsonify({"found": len(accounts), "accounts": accounts})

    @bp.route("/open_finance/aggregation/v1/customers/<customer_id>/institutionLogins", methods=["GET"])
    def list_institution_logins(customer_id):
        store.lazy_load(API)
        accounts = store.list(API, "accounts")
        logins = [{"id": a.get("id"), "institutionId": a.get("institutionId"), "status": "active"} for a in accounts[:2]]
        return jsonify({"found": len(logins), "institutionLogins": logins})

    # ── Transactions ──────────────────────────────────────────────────────────
    @bp.route("/open_finance/aggregation/v3/customers/<customer_id>/transactions", methods=["GET"])
    def list_transactions(customer_id):
        store.lazy_load(API)
        all_txns = store.list(API, "transactions")
        txns = [t for t in all_txns if str(t.get("customerId")) == str(customer_id)]
        if not txns:
            txns = all_txns

        from_date = request.args.get("fromDate")
        to_date = request.args.get("toDate")
        if from_date:
            try:
                txns = [t for t in txns if t.get("postedDate", 0) >= int(from_date)]
            except ValueError:
                pass
        if to_date:
            try:
                txns = [t for t in txns if t.get("postedDate", 0) <= int(to_date)]
            except ValueError:
                pass

        return jsonify({"found": len(txns), "transactions": txns})

    @bp.route("/open_finance/aggregation/v4/customers/<customer_id>/accounts/<account_id>/transactions", methods=["GET"])
    def list_account_transactions(customer_id, account_id):
        store.lazy_load(API)
        all_txns = store.list(API, "transactions")
        txns = [t for t in all_txns if str(t.get("accountId")) == str(account_id)]
        if not txns:
            txns = all_txns[:5]
        return jsonify({"found": len(txns), "transactions": txns})

    # ── Institutions ──────────────────────────────────────────────────────────
    @bp.route("/open_finance/institution/v2/institutions/<institution_id>", methods=["GET"])
    def get_institution(institution_id):
        store.lazy_load(API)
        rec = store.get(API, "institutions", institution_id)
        if rec is None:
            institutions = store.list(API, "institutions")
            rec = next((i for i in institutions if str(i.get("id")) == str(institution_id)),
                       institutions[0] if institutions else {"id": institution_id})
        return jsonify({"institution": rec})

    @bp.route("/open_finance/institution/v2/institutions", methods=["GET"])
    def list_institutions():
        store.lazy_load(API)
        institutions = store.list(API, "institutions")
        return jsonify({"found": len(institutions), "institutions": institutions})

    # ── Reports ───────────────────────────────────────────────────────────────
    @bp.route("/open_finance/analytics/data/v1/customers/<customer_id>/reports", methods=["GET"])
    def list_reports(customer_id):
        store.lazy_load(API)
        reports = store.list(API, "reports")
        return jsonify({"reports": reports, "found": len(reports)})

    @bp.route("/open_finance/analytics/data/v1/customers/<customer_id>/reports/<report_id>", methods=["GET"])
    def get_report(customer_id, report_id):
        rec = store.get(API, "reports", report_id)
        return jsonify(rec or {"id": report_id, "status": "success"})

    # ── Payment Success Indicators ───────────────────────────────────────────
    @bp.route("/open_finance/payments/customers/<customer_id>/accounts/<account_id>/payment-success-indicators", methods=["POST"])
    def generate_payment_success_indicators(customer_id, account_id):
        body = request.get_json(force=True) or {}
        transaction = body.get("transaction") or {}
        result = _build_psi_result(
            customer_id,
            account_id,
            _safe_float(transaction.get("amount"), 0.0),
            transaction.get("settleByDate"),
        )
        store.put(API, "payment_success_indicators", result["payRequestId"], result)
        return jsonify(result)

    @bp.route("/open_finance/payments/customers/<customer_id>/accounts/<account_id>/payment-success-indicators/<pay_request_id>", methods=["GET"])
    def get_payment_success_indicators(customer_id, account_id, pay_request_id):
        result = store.get(API, "payment_success_indicators", pay_request_id)
        if result is None:
            result = _build_psi_result(customer_id, account_id, 500.0, None)
            result["payRequestId"] = pay_request_id
            store.put(API, "payment_success_indicators", pay_request_id, result)
        return jsonify(result)
