"""Simulator Flask Blueprint — discovers handlers dynamically from ``apis.catalog``.

Each entry in the API catalog must have a matching ``simulator/handlers/<id>.py``
module exposing a ``register(bp)`` function that mounts the simulator routes.
"""
from __future__ import annotations

import importlib

from flask import Blueprint, jsonify, request

from apis.catalog import iter_ordered
from simulator import switcher
from simulator.datastore import store

# Ordered list of api ids handled by the simulator (sourced from the catalog).
_ALL_APIS: list[str] = [entry.id for entry in iter_ordered()]


sim_bp = Blueprint("simulator", __name__, url_prefix="/api-sim")


# Discover and register each handler module.
for _api_id in _ALL_APIS:
    try:
        _mod = importlib.import_module(f"simulator.handlers.{_api_id}")
    except ModuleNotFoundError as _e:
        print(f"[simulator] no handler module for {_api_id}: {_e}")
        continue
    if hasattr(_mod, "register"):
        _mod.register(sim_bp)
    else:
        print(f"[simulator] handler {_api_id} has no register() function")


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
