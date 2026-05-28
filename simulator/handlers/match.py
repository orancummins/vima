from flask import jsonify, request

from simulator.datastore import store

API = "match"


def register(bp):
    @bp.route("/match/countries", methods=["GET"])
    def get_countries():
        store.lazy_load(API)
        countries = store.list(API, "countries")
        payload = [
            {
                "countryCode": c.get("countryCode"),
                "regionCode": c.get("regionCode"),
                "name": c.get("name"),
                "isStatesAvailable": bool(c.get("isStatesAvailable", False)),
            }
            for c in countries
        ]
        return jsonify({"countries": payload})

    @bp.route("/match/countries/<country_code>/states", methods=["GET"])
    def get_states(country_code):
        store.lazy_load(API)
        cc = str(country_code or "").upper()
        states = [
            s for s in store.list(API, "states")
            if str(s.get("countryCode", "")).upper() == cc
        ]
        payload = [{"stateCode": s.get("stateCode"), "name": s.get("name")} for s in states]
        return jsonify({"states": payload})

    @bp.route("/match/countries/<country_code>/cities", methods=["GET"])
    def get_cities(country_code):
        store.lazy_load(API)
        cc = str(country_code or "").upper()
        state_code = (request.args.get("state_code") or "").strip().upper()

        cities = [
            c for c in store.list(API, "cities")
            if str(c.get("countryCode", "")).upper() == cc
        ]
        if state_code:
            cities = [c for c in cities if str(c.get("stateCode", "")).upper() == state_code]

        return jsonify({"cities": [c.get("name") for c in cities]})

    @bp.route("/match/contact-details", methods=["POST"])
    def get_contact_details():
        store.lazy_load(API)
        body = request.get_json(force=True) or {}
        acquirer_id = str((body.get("contactRequest") or {}).get("acquirerId") or "").strip()
        if not acquirer_id:
            return jsonify({"Errors": {"Error": [{"ReasonCode": "INVALID_REQUEST", "Description": "Missing contactRequest.acquirerId"}]}}), 400

        details = store.get(API, "contact_details", acquirer_id)
        if not details:
            return jsonify({"contactDetails": []})

        payload = {
            "bankName": details.get("bankName"),
            "region": details.get("region"),
            "firstName": details.get("firstName"),
            "lastName": details.get("lastName"),
            "phoneNumber": details.get("phoneNumber"),
            "faxNumber": details.get("faxNumber"),
            "emailAddress": details.get("emailAddress"),
        }
        return jsonify({"contactDetails": [payload]})

    @bp.route("/match/termination-inquiries", methods=["POST"])
    def create_termination_inquiry():
        store.lazy_load(API)
        body = request.get_json(force=True) or {}

        request_obj = body.get("terminationInquiryRequest")
        if not isinstance(request_obj, dict):
            return jsonify({"Errors": {"Error": [{"ReasonCode": "INVALID_REQUEST", "Description": "Missing terminationInquiryRequest"}]}}), 400

        merchant = request_obj.get("merchant") or {}
        if not request_obj.get("acquirerId") or not merchant.get("name"):
            return jsonify({"Errors": {"Error": [{"ReasonCode": "INVALID_REQUEST", "Description": "acquirerId and merchant.name are required"}]}}), 400

        existing = store.list(API, "termination_inquiry_response")
        next_num = len(existing) + 1
        inquiry_ref = f"IRN{next_num:06d}"

        response = {
            "pageOffset": int(request.args.get("page_offset") or 0),
            "ref": inquiry_ref,
            "possibleMerchantMatches": [],
        }
        history = {
            "terminationInquiryRequest": request_obj,
            "terminationInquiryResponse": response,
        }

        store.put(API, "termination_inquiry_response", inquiry_ref, response)
        store.put(API, "termination_inquiry_history", inquiry_ref, history)

        return jsonify({"terminationInquiryResponse": response})

    @bp.route("/match/termination-inquiries/<inquiry_ref_num>", methods=["GET"])
    def get_inquiry_history(inquiry_ref_num):
        store.lazy_load(API)
        irn = str(inquiry_ref_num or "").strip()
        history = store.get(API, "termination_inquiry_history", irn)
        if not history:
            return jsonify({"Errors": {"Error": [{"ReasonCode": "NOT_FOUND", "Description": "Inquiry reference not found"}]}}), 404
        return jsonify({"terminationInquiryHistory": history})
