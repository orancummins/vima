from flask import request, jsonify
from simulator.datastore import store

API = "merchant_identifier"


def _split_csv(value: str) -> list[str]:
    return [p.strip() for p in (value or "").split(",") if p.strip()]


def register(bp):
    @bp.route("/merchant_identifier/merchants", methods=["GET"])
    def match_merchants():
        store.lazy_load(API)
        descriptor = (
            request.args.get("merchant_descriptor")
            or request.args.get("merchantDescriptor")
            or ""
        ).strip().lower()

        merchants = store.list(API, "merchants")
        if descriptor:
            items = [
                m for m in merchants
                if descriptor in str(m.get("merchantDescriptor", "")).lower()
            ]
        else:
            items = merchants
        return jsonify({"items": items, "total": len(items)})

    @bp.route("/merchant_identifier/merchants-by-card-acceptor-ids", methods=["GET"])
    def match_by_card_acceptor_ids():
        store.lazy_load(API)
        raw_ids = (
            request.args.get("card_acceptor_id")
            or request.args.get("cardAcceptorIds")
            or request.args.get("card_acceptor_ids")
            or ""
        )
        requested = set(_split_csv(raw_ids))

        merchants = store.list(API, "merchants")
        if requested:
            items = [m for m in merchants if str(m.get("cardAcceptorId", "")) in requested]
        else:
            items = merchants
        return jsonify({"items": items, "total": len(items)})

    @bp.route("/merchant_identifier/merchants-by-tax-ids", methods=["GET"])
    def match_by_tax_ids():
        store.lazy_load(API)
        raw_ids = (
            request.args.get("tax_id")
            or request.args.get("taxIds")
            or request.args.get("tax_ids")
            or ""
        )
        requested = set(_split_csv(raw_ids))

        merchants = store.list(API, "merchants")
        if requested:
            items = [m for m in merchants if str(m.get("taxId", "")) in requested]
        else:
            items = merchants
        return jsonify({"items": items, "total": len(items)})
