from flask import jsonify

from simulator.datastore import store

API = "priceless_cities"


def register(bp):
    # ── Platform ──────────────────────────────────────────────────────────────
    @bp.route("/priceless_cities/platform/health-checks", methods=["GET"])
    def platform_health():
        return jsonify({"msg": "OK", "data": {}})

    @bp.route("/priceless_cities/platform/products", methods=["GET"])
    def platform_products():
        store.lazy_load(API)
        items = store.list(API, "platform_products")
        return jsonify({"msg": "OK", "data": items})

    @bp.route("/priceless_cities/platform/products/<product_id>", methods=["GET"])
    def platform_product_info(product_id):
        store.lazy_load(API)
        rec = store.get(API, "platform_products", product_id)
        if rec is None:
            items = store.list(API, "platform_products")
            rec = next((p for p in items if str(p.get("id")) == product_id), items[0] if items else {})
        return jsonify({"msg": "OK", "data": rec})

    @bp.route("/priceless_cities/platform/products/<product_id>/inventories", methods=["GET"])
    def platform_product_inventory(product_id):
        return jsonify({"msg": "OK", "data": {"productId": product_id, "quantity": 100}})

    @bp.route("/priceless_cities/platform/products/<product_id>/translations", methods=["GET"])
    def platform_product_translations(product_id):
        return jsonify({"msg": "OK", "data": [{"language": "en", "name": "Sample Product"}]})

    @bp.route("/priceless_cities/platform/categories", methods=["GET"])
    def platform_categories():
        store.lazy_load(API)
        return jsonify({"msg": "OK", "data": store.list(API, "platform_categories")})

    @bp.route("/priceless_cities/platform/programs", methods=["GET"])
    def platform_programs():
        store.lazy_load(API)
        return jsonify({"msg": "OK", "data": store.list(API, "platform_programs")})

    @bp.route("/priceless_cities/platform/languages", methods=["GET"])
    def platform_languages():
        store.lazy_load(API)
        return jsonify({"msg": "OK", "data": store.list(API, "platform_languages")})

    @bp.route("/priceless_cities/platform/subscriptions", methods=["GET"])
    def platform_subscriptions():
        return jsonify({"msg": "OK", "data": [{"id": "sub-001", "status": "ACTIVE"}]})

    @bp.route("/priceless_cities/platform/locations", methods=["GET"])
    def platform_locations():
        store.lazy_load(API)
        return jsonify({"msg": "OK", "data": store.list(API, "platform_locations")})

    @bp.route("/priceless_cities/platform/products-locations", methods=["GET"])
    def platform_products_locations():
        store.lazy_load(API)
        items = store.list(API, "platform_products")
        return jsonify({"msg": "OK", "data": items})

    # ── Specials ──────────────────────────────────────────────────────────────
    @bp.route("/priceless_cities/specials/offers", methods=["GET"])
    def specials_offers():
        store.lazy_load(API)
        return jsonify(store.list(API, "specials_offers"))

    @bp.route("/priceless_cities/specials/benefits", methods=["GET"])
    def specials_benefits():
        store.lazy_load(API)
        return jsonify(store.list(API, "specials_benefits"))

    @bp.route("/priceless_cities/specials/programs", methods=["GET"])
    def specials_programs():
        store.lazy_load(API)
        return jsonify(store.list(API, "specials_programs"))

    @bp.route("/priceless_cities/specials/merchants", methods=["GET"])
    def specials_merchants():
        store.lazy_load(API)
        return jsonify(store.list(API, "specials_merchants"))

    @bp.route("/priceless_cities/specials/categories", methods=["GET"])
    def specials_categories():
        store.lazy_load(API)
        return jsonify(store.list(API, "specials_categories"))

    @bp.route("/priceless_cities/specials/countries", methods=["GET"])
    def specials_countries():
        store.lazy_load(API)
        return jsonify(store.list(API, "specials_countries"))

    @bp.route("/priceless_cities/specials/languages", methods=["GET"])
    def specials_languages():
        store.lazy_load(API)
        return jsonify(store.list(API, "specials_languages"))

    @bp.route("/priceless_cities/specials/mastercard-products", methods=["GET"])
    def specials_mastercard_products():
        store.lazy_load(API)
        return jsonify(store.list(API, "specials_mastercard_products"))

    @bp.route("/priceless_cities/specials/card-products", methods=["GET"])
    def specials_card_products():
        store.lazy_load(API)
        return jsonify(store.list(API, "specials_mastercard_products"))
