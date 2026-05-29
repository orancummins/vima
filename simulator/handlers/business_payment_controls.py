"""Simulator handler for Mastercard Business Payment Controls.

Mirrors a useful subset of the BPC endpoints under
``/api-sim/business_payment_controls/...`` so the UI can demo the API
without the manual Commercial Products onboarding.
"""
import uuid
from flask import request, jsonify
from simulator.datastore import store

API = "business_payment_controls"


def register(bp):
    @bp.route("/business_payment_controls/entities/user-entity", methods=["GET"])
    def user_entity():
        store.lazy_load(API)
        rows = store.list(API, "entities")
        return jsonify(rows[0] if rows else {})

    @bp.route("/business_payment_controls/real-card-accounts", methods=["POST"])
    def register_real_card():
        store.lazy_load(API)
        body = request.get_json(silent=True) or {}
        rec = {
            "accountGuid": str(uuid.uuid4()),
            "ownerGuid": body.get("ownerGuid"),
            "cardNumber": (body.get("cardNumber") or "")[-4:].rjust(16, "*"),
            "expirationMonth": body.get("expirationMonth"),
            "expirationYear": body.get("expirationYear"),
            "status": "ACTIVE",
        }
        return jsonify(rec), 201

    @bp.route("/business_payment_controls/real-card-accounts/searches", methods=["POST"])
    def search_real_cards():
        store.lazy_load(API)
        return jsonify({"realCardAccounts": store.list(API, "real_cards")})

    @bp.route("/business_payment_controls/virtual-card-accounts", methods=["POST"])
    def register_virtual_card():
        store.lazy_load(API)
        body = request.get_json(silent=True) or {}
        rec = {
            "accountGuid": str(uuid.uuid4()),
            "fundingSourceGuid": body.get("fundingSourceGuid"),
            "validityMonths": body.get("validityMonths", 12),
            "spendLimit": body.get("spendLimit", 100000),
            "status": "ACTIVE",
            "panLast4": "0042",
        }
        return jsonify(rec), 201

    @bp.route("/business_payment_controls/virtual-card-accounts/searches", methods=["POST"])
    def search_virtual_cards():
        store.lazy_load(API)
        return jsonify({"virtualCardAccounts": store.list(API, "virtual_cards")})

    @bp.route("/business_payment_controls/funding-sources/searches", methods=["POST"])
    def search_funding_sources():
        store.lazy_load(API)
        return jsonify({"fundingSources": store.list(API, "funding_sources")})

    @bp.route("/business_payment_controls/authorization-reports", methods=["POST"])
    def create_authorization_report():
        store.lazy_load(API)
        body = request.get_json(silent=True) or {}
        rec = {
            "guid": str(uuid.uuid4()),
            "status": "COMPLETED",
            "fromDate": body.get("fromDate"),
            "toDate": body.get("toDate"),
        }
        return jsonify(rec), 201

    @bp.route("/business_payment_controls/authorization-reports", methods=["GET"])
    def list_authorization_reports():
        store.lazy_load(API)
        return jsonify({"reports": store.list(API, "authorization_reports")})
