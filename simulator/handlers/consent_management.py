import uuid

from flask import jsonify, request

from simulator.datastore import store

API = "consent_management"


def register(bp):
    @bp.route("/consent_management/consents", methods=["POST"])
    def create_consent():
        store.lazy_load(API)
        body = request.get_json(force=True) or {}
        card_ref = str(uuid.uuid4())
        pan = (body.get("cardDetails") or {}).get("pan", "sim-pan")
        consent_names = [c.get("name", "notification") for c in body.get("consents", [{"name": "notification"}])]
        consent_records = [
            {"id": f"sim-consent-{i+1:03d}", "name": name, "status": "APPROVED",
             "createdAt": "2026-01-01T00:00:00Z", "updatedAt": "2026-01-01T00:00:00Z"}
            for i, name in enumerate(consent_names)
        ]
        record = {
            "cardReference": card_ref,
            "pan": pan,
            "consents": consent_records,
            "auth": {
                "type": "THREEDS",
                "status": "AUTHENTICATED",
                "params": {
                    "threeDsMethodUrl": "",
                    "threeDSMethodData": "",
                    "threeDSServerTransID": f"sim-trans-{uuid.uuid4().hex[:8]}",
                },
            },
        }
        store.put(API, "consents", card_ref, record)
        return jsonify(record), 200

    @bp.route("/consent_management/consents/<card_ref>", methods=["GET"])
    def get_consents(card_ref):
        store.lazy_load(API)
        rec = store.get(API, "consents", card_ref)
        if rec is None:
            all_consents = store.list(API, "consents")
            rec = next((c for c in all_consents if c.get("cardReference") == card_ref),
                       all_consents[0] if all_consents else {"cardReference": card_ref, "consents": []})
        return jsonify(rec)

    @bp.route("/consent_management/consents/<card_ref>/start-authentication", methods=["POST"])
    def start_authentication(card_ref):
        return jsonify({
            "cardReference": card_ref,
            "auth": {"type": "THREEDS", "status": "AUTHENTICATED", "params": {}},
        })

    @bp.route("/consent_management/consents/<card_ref>/verify-authentication", methods=["POST"])
    def verify_authentication(card_ref):
        return jsonify({
            "cardReference": card_ref,
            "auth": {"type": "THREEDS", "status": "AUTHENTICATED"},
        })

    @bp.route("/consent_management/consents/<card_ref>", methods=["DELETE"])
    def delete_consents(card_ref):
        store.lazy_load(API)
        store.delete(API, "consents", card_ref)
        return "", 204

    @bp.route("/consent_management/consents/<card_ref>/consents/<consent_id>", methods=["DELETE"])
    def delete_single_consent(card_ref, consent_id):
        return "", 204
