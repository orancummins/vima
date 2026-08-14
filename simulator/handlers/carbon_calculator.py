"""Simulator handler for Mastercard Carbon Calculator.

Mirrors a subset of the live sandbox endpoints under ``/carbon`` so local
development can run without a CID-bound project.
"""
import uuid

from flask import jsonify, request

from simulator.datastore import store

API = "carbon_calculator"


def register(bp):
    @bp.route("/carbon_calculator/service-providers", methods=["GET"])
    def get_service_provider():
        store.lazy_load(API)
        rows = store.list(API, "service_providers")
        return jsonify(rows[0] if rows else {})

    @bp.route("/carbon_calculator/service-providers", methods=["PUT"])
    def update_service_provider():
        store.lazy_load(API)
        rows = store.list(API, "service_providers")
        if not rows:
            return jsonify({}), 404
        rec = rows[0]
        body = request.get_json(silent=True) or {}
        for k in ("legalName", "country"):
            if body.get(k):
                rec[k] = body[k]
        return jsonify(rec)

    @bp.route("/carbon_calculator/service-providers/payment-cards", methods=["POST"])
    def bulk_register_cards():
        store.lazy_load(API)
        body = request.get_json(silent=True) or {}
        pans = body.get("primaryAccountNumbers") or []
        if isinstance(pans, str):
            pans = [p.strip() for p in pans.split(",") if p.strip()]
        out = []
        for _pan in pans:
            cid = f"PC-{uuid.uuid4().hex[:10].upper()}"
            rec = {"paymentCardId": cid, "status": "REGISTERED"}
            store.add(API, "payment_cards", rec)
            out.append(rec)
        return jsonify({"paymentCards": out}), 201

    @bp.route("/carbon_calculator/service-providers/payment-cards/<card_id>", methods=["DELETE"])
    def delete_card(card_id):
        store.lazy_load(API)
        rows = store.list(API, "payment_cards")
        for row in rows:
            if str(row.get("paymentCardId") or row.get("id")) == card_id:
                row["status"] = "DELETED"
                return ("", 204)
        return jsonify({"Errors": {"Error": [{"Source": "Carbon Calculator", "ReasonCode": "NOT_FOUND",
                                              "Description": f"No card with id {card_id}"}]}}), 404

    @bp.route("/carbon_calculator/payment-cards/<card_id>/transaction-footprints", methods=["GET"])
    def historical(card_id):
        store.lazy_load(API)
        rows = store.list(API, "footprints")
        return jsonify({"paymentCardId": card_id, "transactionFootprints": rows})

    @bp.route("/carbon_calculator/payment-cards/transaction-footprints/aggregates", methods=["POST"])
    def aggregates():
        store.lazy_load(API)
        body = request.get_json(silent=True) or {}
        aggregation = (body.get("aggregation") or "MONTHLY").upper()
        rows = store.list(API, "aggregates")
        return jsonify({"aggregation": aggregation, "aggregates": rows})

    @bp.route("/carbon_calculator/transaction-footprints", methods=["POST"])
    def calculate():
        body = request.get_json(silent=True) or {}
        txns = body.get("transactions") or []
        scored = []
        for t in txns:
            amount = float(t.get("amount") or 0)
            mcc    = str(t.get("mcc") or "5411")
            # Simple deterministic stub: 0.4 kg CO2e per USD-equivalent, scaled by MCC.
            mcc_factor = {"5411": 0.30, "5812": 0.55, "4111": 0.90, "5541": 1.20}.get(mcc, 0.50)
            score = round(amount * mcc_factor, 3)
            scored.append({
                "transactionId": t.get("transactionId"),
                "carbonEmissionInGrams": int(score * 1000),
                "amount":   amount,
                "currency": t.get("currency"),
                "mcc":      mcc,
            })
        return jsonify({"transactionFootprints": scored})

    @bp.route("/carbon_calculator/supported-currencies", methods=["GET"])
    def supported_currencies():
        store.lazy_load(API)
        return jsonify({"currencies": store.list(API, "currencies")})

    @bp.route("/carbon_calculator/supported-merchant-categories", methods=["GET"])
    def supported_mccs():
        store.lazy_load(API)
        return jsonify({"merchantCategories": store.list(API, "mccs")})
