from flask import request, jsonify
from simulator.datastore import store

API = "clarity"


def register(bp):
    @bp.route("/clarity/consumer-clarity/searches", methods=["POST"])
    def search_merchant():
        store.lazy_load(API)
        body = request.get_json(force=True) or {}
        search_criteria = body.get("searchCriteria", [{}])
        criteria = search_criteria[0].get("merchantCriteria", {}) if search_criteria else {}
        name = (criteria.get("cardAcceptorName") or "").upper()

        # Match by cardAcceptorName prefix against stored merchant keys
        all_merchants = store.list(API, "merchants")
        matched = None
        for m in all_merchants:
            stored_name = (m.get("cardAcceptorName") or "").upper()
            if stored_name and name and name.startswith(stored_name[:4]):
                matched = m
                break
            if not matched and stored_name == name:
                matched = m

        if not matched and all_merchants:
            matched = all_merchants[0]

        if matched:
            results = matched.get("searchResults", [])
        else:
            results = []

        return jsonify({"searchResults": results})
