"""Simulator handler for Open Finance Australia.

Mirrors the AU base URL shape under ``/api-sim/open_finance_au/...`` so the
api module can target it in simulator mode. Endpoints are intentionally a
small superset of the operations declared in
:py:data:`apis.open_finance_au.api.MANIFEST`.
"""
from __future__ import annotations

import time
import uuid

from flask import jsonify, request

from simulator.datastore import store

API = "open_finance_au"


def register(bp):
    # ── Authentication ──────────────────────────────────────────────────────
    @bp.route("/open_finance_au/aggregation/v2/partners/authentication", methods=["POST"])
    def partner_auth_au():
        return jsonify({"token": "sim_au_token_" + uuid.uuid4().hex[:12]})

    # ── Customers ───────────────────────────────────────────────────────────
    @bp.route("/open_finance_au/aggregation/v2/customers/testing", methods=["POST"])
    def add_testing_customer_au():
        store.lazy_load(API)
        body = request.get_json(force=True, silent=True) or {}
        cust_id = str(int(time.time() * 1000) % 10_000_000_000)
        customer = {
            "id": cust_id,
            "username": body.get("username", f"au_user_{cust_id}"),
            "type": "testing",
            "createdDate": int(time.time()),
            "firstName": body.get("firstName", "Test"),
            "lastName": body.get("lastName", "User"),
        }
        store.put(API, "customers", cust_id, customer)
        return jsonify(customer), 201

    @bp.route("/open_finance_au/aggregation/v1/customers", methods=["GET"])
    def list_customers_au():
        store.lazy_load(API)
        customers = store.list(API, "customers")
        search = (request.args.get("search") or "").lower()
        if search:
            customers = [c for c in customers
                         if search in (c.get("username", "") + " " +
                                       c.get("firstName", "") + " " +
                                       c.get("lastName", "")).lower()]
        return jsonify({"found": len(customers), "customers": customers})

    @bp.route("/open_finance_au/aggregation/v1/customers/<customer_id>", methods=["GET"])
    def get_customer_au(customer_id):
        store.lazy_load(API)
        rec = store.get(API, "customers", customer_id)
        if rec is None:
            customers = store.list(API, "customers")
            rec = next((c for c in customers if str(c.get("id")) == str(customer_id)),
                       customers[0] if customers else {"id": customer_id})
        return jsonify(rec)

    # ── Accounts (consent-gated) ────────────────────────────────────────────
    @bp.route("/open_finance_au/aggregation/v1/customers/<customer_id>/accounts", methods=["GET"])
    def list_customer_accounts_au(customer_id):
        store.lazy_load(API)
        if not request.headers.get("Consent-Receipt-Id"):
            return jsonify({"code": 401, "title": "Unauthorized",
                            "message": "Consent-Receipt-Id header is required."}), 401
        all_accounts = store.list(API, "accounts")
        accounts = [a for a in all_accounts if str(a.get("customerId")) == str(customer_id)]
        if not accounts:
            accounts = all_accounts[:2]
        return jsonify({"found": len(accounts), "accounts": accounts})

    # ── Institutions ────────────────────────────────────────────────────────
    @bp.route("/open_finance_au/institution/v2/institutions", methods=["GET"])
    def list_institutions_au():
        store.lazy_load(API)
        institutions = store.list(API, "institutions")
        search = (request.args.get("search") or "").lower()
        if search:
            institutions = [i for i in institutions if search in i.get("name", "").lower()]
        try:
            limit = int(request.args.get("limit") or 25)
        except ValueError:
            limit = 25
        return jsonify({
            "found": len(institutions),
            "displaying": min(limit, len(institutions)),
            "moreAvailable": False,
            "createdDate": int(time.time()),
            "institutions": institutions[:limit],
        })

    @bp.route("/open_finance_au/institution/v2/institutions/<institution_id>", methods=["GET"])
    def get_institution_au(institution_id):
        store.lazy_load(API)
        rec = store.get(API, "institutions", institution_id)
        if rec is None:
            institutions = store.list(API, "institutions")
            rec = next((i for i in institutions if str(i.get("id")) == str(institution_id)),
                       institutions[0] if institutions else {"id": institution_id})
        return jsonify({"institution": rec})

    # ── Connect ─────────────────────────────────────────────────────────────
    @bp.route("/open_finance_au/connect/v2/generate", methods=["POST"])
    def generate_connect_au():
        body = request.get_json(force=True, silent=True) or {}
        customer_id = body.get("customerId", "1005061234")
        partner_id = body.get("partnerId", "sim_partner")
        ts = int(time.time() * 1000)
        link = (
            "https://connect.openbanking.mastercard.com.au"
            f"?customerId={customer_id}&experience=default&origin=url"
            f"&partnerId={partner_id}&signature=sim_signature"
            f"&timestamp={ts}&ttl={ts + 7200000}"
        )
        if body.get("webhook"):
            link += f"&webhook={body['webhook']}"
        return jsonify({"link": link})
