import uuid

from flask import jsonify, request

from simulator.datastore import store

API = "offers_merchant_content"


def register(bp):
    @bp.route("/offers_merchant_content/categories/category-searches", methods=["POST"])
    def search_categories():
        store.lazy_load(API)
        categories = store.list(API, "categories")
        return jsonify({"categories": categories, "totalCount": len(categories)})

    @bp.route("/offers_merchant_content/sources", methods=["GET"])
    def list_sources():
        store.lazy_load(API)
        sources = store.list(API, "sources")
        return jsonify({"sources": sources, "totalCount": len(sources)})

    @bp.route("/offers_merchant_content/sources/<source_uuid>", methods=["GET"])
    def get_source(source_uuid):
        store.lazy_load(API)
        rec = store.get(API, "sources", source_uuid)
        if rec is None:
            sources = store.list(API, "sources")
            rec = next((s for s in sources if s.get("uuid") == source_uuid), sources[0] if sources else {"uuid": source_uuid})
        return jsonify(rec)

    @bp.route("/offers_merchant_content/merchants", methods=["POST"])
    def create_merchant():
        store.lazy_load(API)
        body = request.get_json(force=True) or {}
        mer_uuid = str(uuid.uuid4())
        merchant = {
            "uuid": mer_uuid,
            "name": body.get("name", f"merchant_{mer_uuid[:8]}"),
            "displayName": body.get("displayName", "New Merchant"),
            "externalMerchantId": body.get("externalMerchantId", f"ext-{mer_uuid[:8]}"),
            "country": body.get("country", "USA"),
            "status": "ACTIVE",
            **{k: v for k, v in body.items() if k not in ("name", "displayName", "externalMerchantId", "country")},
        }
        store.put(API, "merchants", mer_uuid, merchant)
        return jsonify(merchant), 200

    @bp.route("/offers_merchant_content/merchants/<merchant_id>", methods=["GET"])
    def get_merchant(merchant_id):
        store.lazy_load(API)
        rec = store.get(API, "merchants", merchant_id)
        if rec is None:
            merchants = store.list(API, "merchants")
            rec = next((m for m in merchants if m.get("uuid") == merchant_id), merchants[0] if merchants else {"uuid": merchant_id})
        return jsonify(rec)

    @bp.route("/offers_merchant_content/merchants/<merchant_id>", methods=["PUT"])
    def update_merchant(merchant_id):
        store.lazy_load(API)
        body = request.get_json(force=True) or {}
        existing = store.get(API, "merchants", merchant_id) or {"uuid": merchant_id}
        existing.update(body)
        store.put(API, "merchants", merchant_id, existing)
        return jsonify(existing)

    @bp.route("/offers_merchant_content/merchants/<merchant_id>/addresses", methods=["POST"])
    def add_merchant_address(merchant_id):
        body = request.get_json(force=True) or {}
        return jsonify({"uuid": str(uuid.uuid4()), "merchantId": merchant_id, **body}), 200

    @bp.route("/offers_merchant_content/merchants/<merchant_id>/images", methods=["GET"])
    def get_merchant_images(merchant_id):
        return jsonify({"images": [], "merchantId": merchant_id})

    @bp.route("/offers_merchant_content/merchants/<merchant_id>/images", methods=["POST"])
    def upload_merchant_image(merchant_id):
        return jsonify({"uuid": str(uuid.uuid4()), "merchantId": merchant_id, "status": "UPLOADED"}), 200

    @bp.route("/offers_merchant_content/offers", methods=["POST"])
    def create_offer():
        store.lazy_load(API)
        body = request.get_json(force=True) or {}
        offer_uuid = str(uuid.uuid4())
        offer = {"uuid": offer_uuid, "status": "ACTIVE", **body}
        store.put(API, "offers", offer_uuid, offer)
        return jsonify(offer), 200
