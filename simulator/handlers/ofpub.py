import uuid
from flask import request, jsonify
from simulator.datastore import store

API = "ofpub"


def register(bp):
    # ── Access token ──────────────────────────────────────────────────────────
    @bp.route("/ofpub/presentment/loyalty/offers/presentment/access-tokens", methods=["POST"])
    def create_access_token():
        store.lazy_load(API)
        tokens = store.list(API, "access_tokens")
        if tokens:
            return jsonify(tokens[0])
        return jsonify({"id": "sim-token-001", "token": "sim-auth-token-abc123xyz", "expiresAt": "2026-12-31T00:00:00Z"})

    # ── Offers ────────────────────────────────────────────────────────────────
    @bp.route("/ofpub/presentment/loyalty/offers/presentment/offers", methods=["GET"])
    def list_offers():
        store.lazy_load(API)
        offers = store.list(API, "offers")
        return jsonify({"offers": offers, "totalCount": len(offers)})

    @bp.route("/ofpub/presentment/loyalty/offers/presentment/offers/<offer_id>", methods=["GET"])
    def get_offer(offer_id):
        store.lazy_load(API)
        rec = store.get(API, "offers", offer_id)
        if rec is None:
            offers = store.list(API, "offers")
            rec = next((o for o in offers if o.get("offerId") == offer_id or o.get("id") == offer_id),
                       offers[0] if offers else {"id": offer_id})
        return jsonify(rec)

    @bp.route("/ofpub/presentment/loyalty/offers/presentment/platforms/offers", methods=["GET"])
    def list_platform_offers():
        store.lazy_load(API)
        offers = store.list(API, "offers")
        return jsonify({"offers": offers, "totalCount": len(offers)})

    @bp.route("/ofpub/presentment/loyalty/offers/presentment/activations", methods=["POST"])
    def activate_offer():
        body = request.get_json(force=True) or {}
        offer_id = body.get("offerId", "sim-offer")
        activation_id = f"sim-act-{uuid.uuid4().hex[:8]}"
        return jsonify({"activationId": activation_id, "offerId": offer_id, "status": "ACTIVATED"})

    @bp.route("/ofpub/presentment/loyalty/offers/presentment/activities/<activity_type>", methods=["GET"])
    def get_activities(activity_type):
        return jsonify({"activities": [], "totalCount": 0, "activityType": activity_type})

    @bp.route("/ofpub/presentment/loyalty/offers/presentment/savings", methods=["GET"])
    def get_savings():
        store.lazy_load(API)
        savings = store.list(API, "savings")
        return jsonify(savings[0] if savings else {"totalSavings": 0, "currency": "USD"})

    # ── User enrollment ───────────────────────────────────────────────────────
    @bp.route("/ofpub/admin/loyalty/offers/enrollments/users", methods=["POST"])
    def enrol_user():
        store.lazy_load(API)
        body = request.get_json(force=True) or {}
        crk = f"sim-crk-{uuid.uuid4().hex[:8]}"
        user = {
            "crk": crk,
            "userId": body.get("userId", f"user-{uuid.uuid4().hex[:6]}"),
            "userIdType": body.get("userIdType", "BCN"),
            "firstName": body.get("firstName", "Test"),
            "lastName": body.get("lastName", "User"),
            "emailAddress": body.get("emailAddress", "test@example.com"),
            "fiId": body.get("fiId", "1234"),
            "accounts": body.get("accounts", []),
        }
        store.put(API, "users", crk, user)
        return jsonify(user), 200

    @bp.route("/ofpub/admin/loyalty/offers/enrollments/users/<crk>", methods=["GET"])
    def get_user(crk):
        store.lazy_load(API)
        rec = store.get(API, "users", crk)
        if rec is None:
            users = store.list(API, "users")
            rec = next((u for u in users if u.get("crk") == crk), users[0] if users else {"crk": crk})
        return jsonify(rec)

    @bp.route("/ofpub/admin/loyalty/offers/enrollments/users/searches", methods=["POST"])
    def search_users():
        store.lazy_load(API)
        users = store.list(API, "users")
        return jsonify({"users": users, "totalCount": len(users)})

    # ── Rebates ───────────────────────────────────────────────────────────────
    @bp.route("/ofpub/admin/loyalty/offers/rebates", methods=["GET"])
    def get_rebates():
        store.lazy_load(API)
        rebates = store.list(API, "rebates")
        return jsonify({"rebates": rebates, "totalCount": len(rebates)})
