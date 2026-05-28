"""Simulator handler for Open Finance Europe (Aiia).

Mirrors the EU API shape under ``/api-sim/open_finance_eu/...`` for the
api module to target in simulator mode. Includes an `/oauth2/token`
stub so the JWT-signed flow becomes a no-op pass-through during local
development without real keys.
"""
from __future__ import annotations

import time
import uuid
from typing import Any, Dict

from flask import jsonify, request

from simulator.datastore import store

API = "open_finance_eu"


def register(bp):
    # ── OAuth2 token (JWT assertion accepted but not verified) ─────────────
    @bp.route("/open_finance_eu/oauth2/token", methods=["POST"])
    def oauth_token_eu():
        return jsonify({
            "access_token": "sim_eu_token_" + uuid.uuid4().hex[:16],
            "token_type": "bearer",
            "expires_in": 3600,
            "scope": "ob_data ob_providers",
        })

    # ── Providers ───────────────────────────────────────────────────────────
    @bp.route("/open_finance_eu/providers", methods=["GET"])
    def list_providers_eu():
        store.lazy_load(API)
        providers = store.list(API, "providers")
        country = (request.args.get("country") or "").upper()
        if country:
            providers = [p for p in providers if p.get("country", "").upper() == country]
        try:
            limit = int(request.args.get("limit") or 25)
        except ValueError:
            limit = 25
        return jsonify({
            "providers": providers[:limit],
            "count": len(providers),
        })

    @bp.route("/open_finance_eu/provider-groups", methods=["GET"])
    def list_provider_groups_eu():
        return jsonify({"provider_groups": [
            {"id": "aiia-test-banks", "name": "Aiia Test Banks", "count": 5},
        ]})

    # ── Consents ────────────────────────────────────────────────────────────
    @bp.route("/open_finance_eu/consents", methods=["POST"])
    def create_consent_eu():
        store.lazy_load(API)
        body = request.get_json(force=True, silent=True) or {}
        consent_id = "con_" + uuid.uuid4().hex[:16]
        record: Dict[str, Any] = {
            "consent_id": consent_id,
            "id": consent_id,
            "provider_id": body.get("provider_id"),
            "scopes": body.get("scopes") or ["accounts", "transactions", "balances"],
            "status": "awaiting_authorisation",
            "created_at": int(time.time()),
            "redirect_url": body.get("redirect_url", ""),
        }
        store.put(API, "consents", consent_id, record)
        return jsonify(record), 201

    @bp.route("/open_finance_eu/consents/<consent_id>", methods=["GET"])
    def get_consent_eu(consent_id):
        store.lazy_load(API)
        rec = store.get(API, "consents", consent_id) or {
            "consent_id": consent_id, "id": consent_id, "status": "granted",
            "scopes": ["accounts", "transactions", "balances"],
        }
        # Auto-progress simulated consent to "granted" after creation so
        # downstream operations succeed without manual mutation.
        if rec.get("status") == "awaiting_authorisation":
            rec["status"] = "granted"
            store.put(API, "consents", consent_id, rec)
        return jsonify(rec)

    @bp.route("/open_finance_eu/consents/<consent_id>", methods=["DELETE"])
    def revoke_consent_eu(consent_id):
        store.lazy_load(API)
        rec = store.get(API, "consents", consent_id)
        if rec:
            rec["status"] = "revoked"
            store.put(API, "consents", consent_id, rec)
        return jsonify({"consent_id": consent_id, "status": "revoked"})

    @bp.route("/open_finance_eu/consents/<consent_id>/managed-flows", methods=["POST"])
    def create_managed_flow_eu(consent_id):
        body = request.get_json(force=True, silent=True) or {}
        flow_id = "flow_" + uuid.uuid4().hex[:12]
        url = (
            "https://flow.openbanking.mastercard.eu/"
            f"?flow_id={flow_id}&consent_id={consent_id}"
            f"&language={body.get('language', 'en')}"
        )
        return jsonify({
            "flow_id": flow_id,
            "url": url,
            "flow_url": url,
            "expires_in": 1800,
        }), 201

    # ── Accounts ────────────────────────────────────────────────────────────
    @bp.route("/open_finance_eu/accounts", methods=["GET"])
    def list_accounts_eu():
        store.lazy_load(API)
        accounts = store.list(API, "accounts")
        return jsonify({"accounts": accounts, "count": len(accounts)})

    @bp.route("/open_finance_eu/accounts/<account_id>", methods=["GET"])
    def get_account_eu(account_id):
        store.lazy_load(API)
        rec = store.get(API, "accounts", account_id)
        if rec is None:
            accounts = store.list(API, "accounts")
            rec = next((a for a in accounts if str(a.get("id")) == str(account_id)),
                       accounts[0] if accounts else {"id": account_id})
        return jsonify(rec)

    # ── Transactions ────────────────────────────────────────────────────────
    @bp.route("/open_finance_eu/accounts/<account_id>/transactions", methods=["GET"])
    def list_transactions_eu(account_id):
        store.lazy_load(API)
        all_tx = store.list(API, "transactions")
        tx = [t for t in all_tx if str(t.get("account_id")) == str(account_id)]
        if not tx:
            tx = all_tx[:4]
        try:
            limit = int(request.args.get("limit") or 50)
        except ValueError:
            limit = 50
        return jsonify({"transactions": tx[:limit], "count": len(tx)})

    # ── Balances ────────────────────────────────────────────────────────────
    @bp.route("/open_finance_eu/accounts/<account_id>/balance-checks", methods=["POST"])
    def balance_check_eu(account_id):
        store.lazy_load(API)
        rec = store.get(API, "accounts", account_id)
        balance = (rec or {}).get("balance", 0.0)
        currency = (rec or {}).get("currency", "EUR")
        return jsonify({
            "account_id": account_id,
            "balances": [
                {"type": "available", "amount": balance, "currency": currency},
                {"type": "booked", "amount": balance, "currency": currency},
            ],
            "retrieved_at": int(time.time()),
        })

    # ── Insights — Account Ownership Verification ───────────────────────────
    @bp.route("/open_finance_eu/account-ownership-verifications", methods=["POST"])
    def verify_ownership_eu():
        body = request.get_json(force=True, silent=True) or {}
        verification_id = "vrf_" + uuid.uuid4().hex[:12]
        return jsonify({
            "verification_id": verification_id,
            "account_id": body.get("account_id"),
            "match": True,
            "match_score": 0.97,
            "holder_name": "Alex Müller",
            "expected_name": body.get("expected_name", ""),
            "status": "completed",
        }), 201
