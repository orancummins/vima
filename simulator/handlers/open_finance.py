import uuid
import time
from flask import request, jsonify
from simulator.datastore import store

API = "open_finance"


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
