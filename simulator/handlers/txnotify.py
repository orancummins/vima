import uuid
from flask import request, jsonify
from simulator.datastore import store

API = "txnotify"


def register(bp):
    @bp.route("/txnotify/notifications/transactions", methods=["POST"])
    def trigger_test_transaction():
        store.lazy_load(API)
        body = request.get_json(force=True) or {}
        trans_uid = f"sim-tx-{uuid.uuid4().hex[:8]}"
        record = {
            "transUid": trans_uid,
            "cardReference": body.get("cardReference", "sim-card-ref"),
            "cardholderAmount": body.get("cardholderAmount", 9.99),
            "cardholderCurrency": body.get("cardholderCurrency", "USD"),
            "merchantName": body.get("merchantName", "Coffee Corner"),
            "cardLastNumbers": body.get("cardLastNumbers", 1234),
            "transactionType": "PURCHASE",
            "postedDate": "2026-05-23T10:00:00Z",
        }
        store.put(API, "transactions", trans_uid, record)
        return jsonify(record), 200

    @bp.route("/txnotify/undelivered-notifications", methods=["GET"])
    def get_undelivered():
        store.lazy_load(API)
        items = store.list(API, "undelivered_notifications")
        page_number = int(request.args.get("pageNumber", 1))
        page_size = int(request.args.get("pageSize", 10))
        page = items[(page_number - 1) * page_size: page_number * page_size]
        return jsonify({"notifications": page, "totalCount": len(items)})
