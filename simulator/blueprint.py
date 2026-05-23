"""Simulator Flask Blueprint — mounts all API handlers at /api-sim/."""
from flask import Blueprint, request, jsonify

from simulator.datastore import store
from simulator import switcher

import simulator.handlers.binlookup as binlookup_h
import simulator.handlers.clarity as clarity_h
import simulator.handlers.priceless as priceless_h
import simulator.handlers.easysavings as easysavings_h
import simulator.handlers.places as places_h
import simulator.handlers.eligibility as eligibility_h
import simulator.handlers.bces as bces_h
import simulator.handlers.ofpub as ofpub_h
import simulator.handlers.ofmc as ofmc_h
import simulator.handlers.consent as consent_h
import simulator.handlers.txnotify as txnotify_h
import simulator.handlers.ofin as ofin_h

_ALL_APIS = [
    "binlookup", "clarity", "priceless", "easysavings", "places",
    "eligibility", "bces", "ofpub", "ofmc", "consent", "txnotify", "ofin",
]

sim_bp = Blueprint("simulator", __name__, url_prefix="/api-sim")

for _mod in [
    binlookup_h, clarity_h, priceless_h, easysavings_h, places_h,
    eligibility_h, bces_h, ofpub_h, ofmc_h, consent_h, txnotify_h, ofin_h,
]:
    _mod.register(sim_bp)


# ── Admin routes ──────────────────────────────────────────────────────────────

@sim_bp.route("/admin/status")
def admin_status():
    status = {}
    for api in _ALL_APIS:
        status[api] = {
            "simulated": switcher.is_simulated(api),
            "data_loaded": api in store._loaded,
        }
    return jsonify(status)


@sim_bp.route("/admin/toggle", methods=["POST"])
def admin_toggle():
    body = request.get_json(force=True) or {}
    api = body.get("api", "all")
    simulated = bool(body.get("simulated", True))
    targets = _ALL_APIS if api == "all" else [api]
    for slug in targets:
        switcher.RUNTIME_OVERRIDES[slug] = simulated
    return jsonify({"ok": True, "overrides": switcher.RUNTIME_OVERRIDES})


@sim_bp.route("/admin/<api>/load", methods=["POST"])
def admin_load(api):
    data = request.get_json(force=True) or {}
    store.reset(api)
    for resource, records in data.items():
        for i, rec in enumerate(records):
            rid = str(rec.get("id", rec.get("uuid", rec.get("offerId", i))))
            store.put(api, resource, rid, rec)
    store._loaded.add(api)
    return jsonify({"ok": True, "api": api})


@sim_bp.route("/admin/<api>/reset", methods=["POST"])
def admin_reset(api):
    store.reset(api)
    store.lazy_load(api)
    return jsonify({"ok": True, "api": api})


@sim_bp.route("/admin/<api>/data")
def admin_data(api):
    resources = [
        "bins", "merchants", "products", "offers", "places", "benefits",
        "customers", "accounts", "transactions", "institutions", "sources",
        "categories", "countries", "redemptions", "users", "rebates",
        "access_tokens", "savings", "consents", "undelivered_notifications",
        "benefit_contents", "reports", "mcc_codes", "industry_codes",
        "platform_products", "platform_categories", "platform_programs",
        "platform_locations", "platform_languages",
        "specials_offers", "specials_benefits", "specials_programs",
        "specials_merchants", "specials_categories", "specials_countries",
        "specials_languages", "specials_mastercard_products",
    ]
    result = {}
    for r in resources:
        rows = store.list(api, r)
        if rows:
            result[r] = rows
    return jsonify(result)
