import uuid
from flask import request, jsonify
from simulator.datastore import store

API = "easysavings"


def register(bp):
    @bp.route("/easysavings/easysavings/specials/countries", methods=["GET"])
    def list_countries():
        store.lazy_load(API)
        return jsonify(store.list(API, "countries"))

    @bp.route("/easysavings/easysavings/specials/offers", methods=["GET"])
    def easysavings_list_offers():
        store.lazy_load(API)
        offers = store.list(API, "offers")
        offset = int(request.args.get("offset", 0))
        limit = int(request.args.get("limit", 30))
        page = offers[offset: offset + limit]
        return jsonify({"offers": page, "totalCount": len(offers), "offset": offset, "limit": limit})

    @bp.route("/easysavings/easysavings/specials/redemptions", methods=["POST"])
    def redeem_offer():
        store.lazy_load(API)
        body = request.get_json(force=True) or {}
        offer_ids = [o.get("id") for o in body.get("offers", [])]
        order_id = str(uuid.uuid4())
        redemption = {
            "orderId": order_id,
            "bin": body.get("bin", ""),
            "offers": [{"id": oid, "voucherCode": f"VOUCHER-{oid[:8]}", "status": "SUCCESS"} for oid in offer_ids],
        }
        store.put(API, "redemptions", order_id, redemption)
        return jsonify(redemption), 200

    @bp.route("/easysavings/easysavings/specials/redemptions/<order_id>", methods=["GET"])
    def get_redemption(order_id):
        store.lazy_load(API)
        rec = store.get(API, "redemptions", order_id)
        if rec is None:
            existing = store.list(API, "redemptions")
            rec = existing[0] if existing else {"orderId": order_id, "offers": []}
        return jsonify(rec)
