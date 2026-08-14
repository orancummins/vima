from flask import jsonify, request

from simulator.datastore import store

API = "bin_lookup"


def register(bp):
    @bp.route("/bin_lookup/bin-ranges", methods=["POST"])
    def bin_ranges():
        store.lazy_load(API)
        body = request.get_json(force=True) or []
        filters = [{"key": f["key"], "value": f["value"]} for f in body if "key" in f and "value" in f]
        results = store.search(API, "bins", filters) if filters else store.list(API, "bins")
        page = int(request.args.get("page", 1))
        size = int(request.args.get("size", 10))
        items = results[(page - 1) * size: page * size]
        return jsonify({"items": items, "totalItems": len(results), "currentPageNumber": page})
