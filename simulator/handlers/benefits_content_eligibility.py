from flask import request, jsonify
from simulator.datastore import store

API = "benefits_content_eligibility"


def register(bp):
    @bp.route("/benefits_content_eligibility/benefit-contents/searches", methods=["POST"])
    def search_contents():
        store.lazy_load(API)
        body = request.get_json(force=True) or {}
        benefit_code = body.get("benefitCode", "")
        product_code = body.get("productCode", "")

        contents = store.list(API, "benefit_contents")
        if benefit_code or product_code:
            filtered = [
                c for c in contents
                if (not benefit_code or any(
                    b.get("benefitCode") == benefit_code
                    for b in c.get("benefits", [])
                ))
                and (not product_code or c.get("productCode") == product_code)
            ]
            contents = filtered if filtered else contents

        return jsonify({"bundles": contents})
