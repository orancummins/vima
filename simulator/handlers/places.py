from flask import request, jsonify
from simulator.datastore import store

API = "places"


def register(bp):
    @bp.route("/places/location-intelligence/places-locator/places/searches", methods=["POST"])
    def search_places():
        store.lazy_load(API)
        body = request.get_json(force=True) or {}
        place_filter = body.get("place", {})
        country = (place_filter.get("countryCode") or "").upper()
        industry = (place_filter.get("industry") or "").upper()

        all_places = store.list(API, "places")
        results = []
        for p in all_places:
            if country and p.get("countryCode", "").upper() != country:
                continue
            if industry and p.get("industry", "").upper() != industry:
                continue
            results.append(p)

        offset = int(request.args.get("offset", 0))
        limit = int(request.args.get("limit", 25))
        page = results[offset: offset + limit]
        return jsonify({"places": page, "totalCount": len(results), "offset": offset, "limit": limit})

    @bp.route("/places/location-intelligence/places-locator/places/<location_id>", methods=["GET"])
    def get_place(location_id):
        store.lazy_load(API)
        rec = store.get(API, "places", location_id)
        if rec is None:
            places = store.list(API, "places")
            rec = places[0] if places else {"locationId": location_id}
        return jsonify(rec)

    @bp.route("/places/location-intelligence/places-locator/merchant-category-codes", methods=["GET"])
    def list_mcc_codes():
        store.lazy_load(API)
        return jsonify({"merchantCategoryCodes": store.list(API, "mcc_codes")})

    @bp.route("/places/location-intelligence/places-locator/merchant-category-codes/mcc-codes/<mcc>", methods=["GET"])
    def get_mcc_code(mcc):
        store.lazy_load(API)
        rec = store.get(API, "mcc_codes", mcc)
        if rec is None:
            codes = store.list(API, "mcc_codes")
            rec = next((c for c in codes if str(c.get("code")) == mcc), codes[0] if codes else {"code": mcc})
        return jsonify(rec)

    @bp.route("/places/location-intelligence/places-locator/merchant-industry-codes", methods=["GET"])
    def list_industry_codes():
        store.lazy_load(API)
        return jsonify({"merchantIndustryCodes": store.list(API, "industry_codes")})

    @bp.route("/places/location-intelligence/places-locator/merchant-industry-codes/industries/<industry>", methods=["GET"])
    def get_industry_code(industry):
        store.lazy_load(API)
        rec = store.get(API, "industry_codes", industry)
        if rec is None:
            codes = store.list(API, "industry_codes")
            rec = next((c for c in codes if c.get("industryCode") == industry), codes[0] if codes else {"industryCode": industry})
        return jsonify(rec)
