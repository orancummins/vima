import uuid
from flask import request, jsonify
from simulator.datastore import store

API = "eligibility"


def register(bp):
    @bp.route("/eligibility/benefits/searches", methods=["POST"])
    def search_benefits():
        store.lazy_load(API)
        benefits = store.list(API, "benefits")
        return jsonify({"data": benefits})

    @bp.route("/eligibility/products/searches", methods=["POST"])
    def search_products():
        store.lazy_load(API)
        products = store.list(API, "products")
        return jsonify({"data": products})

    @bp.route("/eligibility/widgets/access-tokens", methods=["GET"])
    def access_token():
        store.lazy_load(API)
        tokens = store.list(API, "access_tokens")
        token_val = tokens[0].get("token", f"sim-widget-token-{uuid.uuid4().hex[:12]}") if tokens else f"sim-widget-token-{uuid.uuid4().hex[:12]}"
        return jsonify({"accessToken": token_val})
