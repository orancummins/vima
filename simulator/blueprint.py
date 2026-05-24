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
        stats = store.stats(api)
        total = sum(v["total"] for v in stats.values())
        captured = sum(v["captured"] for v in stats.values())
        status[api] = {
            "simulated": switcher.is_simulated(api),
            "data_loaded": api in store._loaded,
            "records": total,
            "captured_from_sandbox": captured,
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
    from simulator.datastore import _id_for
    data = request.get_json(force=True) or {}
    store.reset(api)
    for resource, records in data.items():
        for i, rec in enumerate(records):
            rid = _id_for(rec, i)
            store.put(api, resource, rid, rec)
    store._loaded.add(api)
    return jsonify({"ok": True, "api": api})


@sim_bp.route("/admin/<api>/reset", methods=["POST"])
def admin_reset(api):
    store.reset(api)
    store.lazy_load(api)
    return jsonify({"ok": True, "api": api})


@sim_bp.route("/admin/<api>/stats")
def admin_stats(api):
    stats = store.stats(api)
    return jsonify({"api": api, "collections": stats})


@sim_bp.route("/admin/<api>/data")
def admin_data(api):
    result = {}
    resources = store._conn(api).execute(
        "SELECT DISTINCT resource FROM records"
    ).fetchall()
    for (r,) in resources:
        rows = store.list(api, r)
        if rows:
            result[r] = rows
    return jsonify(result)
