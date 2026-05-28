from flask import request, jsonify
from simulator.datastore import store

API = "automatic_billing_updater"


def _suffix(account_number: str) -> str:
    text = (account_number or "").strip()
    return text[-1] if text else ""


def _case_for(resource: str, suffix: str) -> dict | None:
    cases = store.list(API, resource)
    for rec in cases:
        if str(rec.get("suffix", "")) == str(suffix):
            return rec
    return None


def _extract_account(body: dict) -> dict:
    return (body.get("account") or {}) if isinstance(body, dict) else {}


def register(bp):
    @bp.route("/automatic_billing_updater/inquiries", methods=["POST"])
    def account_inquiry():
        store.lazy_load(API)
        body = request.get_json(force=True) or {}
        account = _extract_account(body)
        suffix = _suffix(account.get("accountNumber", ""))
        case = _case_for("inquiry_cases", suffix)

        if case and case.get("http_status") and int(case["http_status"]) >= 400:
            return jsonify(case.get("response", {})), int(case["http_status"])

        response_indicator = (case or {}).get("responseIndicator", "VALID")
        returned_account = {
            "accountNumber": account.get("accountNumber", "5200000000000002"),
            "expiryDate": account.get("expiryDate", "1218"),
        }
        if response_indicator == "ACCOUNT_UPDATE":
            returned_account["accountNumber"] = "2222222222222256"
            returned_account["expiryDate"] = "0929"
        elif response_indicator == "EXPIRY":
            returned_account["expiryDate"] = "0929"
        elif response_indicator == "CONTACT":
            returned_account["expiryDate"] = "0000"

        return jsonify({
            "account": returned_account,
            "responseIndicator": response_indicator,
        })

    @bp.route("/automatic_billing_updater/subscriptions", methods=["POST"])
    def account_subscription():
        store.lazy_load(API)
        body = request.get_json(force=True) or {}
        account = _extract_account(body)
        suffix = _suffix(account.get("accountNumber", ""))
        case = _case_for("subscription_cases", suffix)

        if case and case.get("http_status") and int(case["http_status"]) >= 400:
            return jsonify(case.get("response", {})), int(case["http_status"])

        response_indicator = (case or {}).get("responseIndicator", "VALID")
        return jsonify({
            "account": {
                "accountNumber": account.get("accountNumber", "5200000000000012"),
                "expiryDate": account.get("expiryDate", "1218"),
            },
            "responseIndicator": response_indicator,
        }), 202

    @bp.route("/automatic_billing_updater/subscription-inquiries", methods=["POST"])
    def subscription_inquiry():
        store.lazy_load(API)
        body = request.get_json(force=True) or {}
        account = _extract_account(body)
        suffix = _suffix(account.get("accountNumber", ""))
        case = _case_for("subscription_inquiry_cases", suffix)

        if case and case.get("http_status") and int(case["http_status"]) >= 400:
            return jsonify(case.get("response", {})), int(case["http_status"])

        subscribed = bool((case or {}).get("subscribed", True))
        return jsonify({"subscribed": subscribed})

    @bp.route("/automatic_billing_updater/subscription-deletions", methods=["POST"])
    def subscription_deletion():
        store.lazy_load(API)
        return "", 202
