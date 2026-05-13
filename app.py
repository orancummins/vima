"""Vima — Mastercard APIs explorer.

A small Flask app on port 9021 that exposes a tabbed UI for testing
Mastercard Developer APIs (Open Finance, BIN Lookup, …) and demoing use
cases composed from them.
"""
import os
import time
import threading
from collections import deque

import requests as _requests
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

load_dotenv()

from apis import registry as api_registry  # noqa: E402
from usecases import registry as usecase_registry  # noqa: E402


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "vima-dev-secret")

# In-memory store for TxPush events (last 50)
_txpush_events: deque = deque(maxlen=50)

# ---------------------------------------------------------------------------
# Outbound API call logger — intercepts all `requests` calls to external APIs
# ---------------------------------------------------------------------------
_api_call_log: deque = deque(maxlen=50)
_api_call_seq = 0
_api_call_lock = threading.Lock()

# URLs containing these substrings are considered "internal" and are skipped
_INTERNAL_HOSTS = ("localhost", "127.0.0.1", "0.0.0.0", "::1")

_orig_send = _requests.Session.send  # keep reference before patching


def _patched_send(self, prepared_request, **kwargs):
    url = prepared_request.url or ""
    # Only log outbound calls to external APIs, not loopback traffic
    is_external = not any(h in url for h in _INTERNAL_HOSTS)

    if not is_external:
        return _orig_send(self, prepared_request, **kwargs)

    global _api_call_seq
    t0 = time.time()
    try:
        body_bytes = prepared_request.body
        if isinstance(body_bytes, bytes):
            try:
                import json as _json
                req_body = _json.loads(body_bytes)
            except Exception:
                req_body = body_bytes.decode("utf-8", errors="replace")
        elif isinstance(body_bytes, str):
            try:
                import json as _json
                req_body = _json.loads(body_bytes)
            except Exception:
                req_body = body_bytes
        else:
            req_body = None
    except Exception:
        req_body = None

    entry: dict = {
        "seq": None,
        "ts": time.strftime("%H:%M:%S"),
        "method": (prepared_request.method or "").upper(),
        "url": url,
        "requestBody": req_body,
        "status": None,
        "responseBody": None,
        "elapsed_ms": None,
    }

    try:
        resp = _orig_send(self, prepared_request, **kwargs)
    except Exception as exc:
        entry["status"] = "ERR"
        entry["elapsed_ms"] = round((time.time() - t0) * 1000)
        with _api_call_lock:
            _api_call_seq += 1
            entry["seq"] = _api_call_seq
            _api_call_log.appendleft(entry)
        raise

    entry["status"] = resp.status_code
    entry["elapsed_ms"] = round((time.time() - t0) * 1000)
    try:
        entry["responseBody"] = resp.json()
    except Exception:
        entry["responseBody"] = resp.text

    with _api_call_lock:
        _api_call_seq += 1
        entry["seq"] = _api_call_seq
        _api_call_log.appendleft(entry)

    return resp


_requests.Session.send = _patched_send


# ----------------------------------------------------------------------------
# Pages
# ----------------------------------------------------------------------------

@app.route("/")
def index():
    return render_template(
        "index.html",
        apis=api_registry.manifests(),
        use_cases=usecase_registry.manifests(),
    )


# ----------------------------------------------------------------------------
# API explorer endpoints
# ----------------------------------------------------------------------------

@app.route("/explorer/apis")
def explorer_apis():
    """Return the manifests for every registered API."""
    return jsonify({"apis": api_registry.manifests()})


@app.route("/explorer/<api_id>/state")
def explorer_state(api_id: str):
    mod = api_registry.get_module(api_id)
    if mod is None:
        return jsonify({"error": "Unknown API"}), 404
    state = getattr(mod, "get_state", lambda: {})()
    return jsonify({"state": state})


@app.route("/explorer/<api_id>/execute", methods=["POST"])
def explorer_execute(api_id: str):
    mod = api_registry.get_module(api_id)
    if mod is None:
        return jsonify({"error": "Unknown API"}), 404
    body = request.get_json(silent=True) or {}
    op_id = body.get("operation")
    params = body.get("params") or {}
    if not op_id:
        return jsonify({"error": "'operation' is required"}), 400
    try:
        result = mod.execute(op_id, params)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
    # Merge in latest state snapshot for the UI
    result["state"] = getattr(mod, "get_state", lambda: {})()
    return jsonify(result)


# ----------------------------------------------------------------------------
# Use cases
# ----------------------------------------------------------------------------

@app.route("/usecases")
def usecases_list():
    return jsonify({"use_cases": usecase_registry.manifests()})


@app.route("/usecases/<uc_id>/data")
def usecase_data(uc_id: str):
    mod = usecase_registry.get_module(uc_id)
    if mod is None:
        return jsonify({"error": "Unknown use case"}), 404
    # Use cases that expose a no-arg data fetcher (e.g. enrichment static data)
    if hasattr(mod, "get_enrichment_data"):
        try:
            return jsonify(mod.get_enrichment_data())
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    if not hasattr(mod, "get_data"):
        return jsonify({"error": "Unknown use case"}), 404
    # Resolve customer_id: explicit query param wins, else fall back to OFIN's active state.
    customer_id = request.args.get("customer_id")
    if not customer_id:
        ofin_mod = api_registry.get_module("ofin")
        if ofin_mod is not None:
            state = getattr(ofin_mod, "get_state", lambda: {})()
            customer_id = state.get("customer_id")
    if not customer_id:
        return jsonify({"error": "No customer linked. Use the Open Finance tab "
                                 "to create or select a customer first."}), 400
    try:
        return jsonify(mod.get_data(customer_id))
    except Exception as e:  # pragma: no cover
        return jsonify({"error": str(e)}), 500


@app.route("/usecases/<uc_id>/action", methods=["POST"])
def usecase_action(uc_id: str):
    mod = usecase_registry.get_module(uc_id)
    if mod is None or not hasattr(mod, "do_action"):
        return jsonify({"error": "Unknown action"}), 404
    body = request.get_json(silent=True) or {}
    action = body.get("action")
    params = body.get("params") or {}
    if not action:
        return jsonify({"error": "'action' is required"}), 400
    try:
        return jsonify(mod.do_action(action, params))
    except Exception as e:  # pragma: no cover
        return jsonify({"error": str(e)}), 500


# ----------------------------------------------------------------------------
# TxPush listener  (use as callback URL with ngrok)
# ----------------------------------------------------------------------------

@app.route("/txpush-listener", methods=["POST"])
def txpush_listener():
    """Receive TxPush notifications from Finicity and store them."""
    import datetime
    payload = request.get_json(silent=True) or request.get_data(as_text=True)
    _txpush_events.appendleft({
        "received_at": datetime.datetime.utcnow().isoformat() + "Z",
        "payload": payload,
    })
    return "", 200


@app.route("/txpush-events")
def txpush_events():
    """Return the last received TxPush events (for the UI to poll)."""
    return jsonify({"events": list(_txpush_events)})


@app.route("/api-call-log")
def api_call_log():
    """Return the last outbound API calls captured by the request logger."""
    since = request.args.get("since", type=int, default=0)
    with _api_call_lock:
        entries = [e for e in _api_call_log if e.get("seq", 0) > since]
    return jsonify({"calls": list(reversed(entries))})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "9021"))
    apis = api_registry.manifests()
    print("\n" + "=" * 60)
    print("Vima — Mastercard API explorer")
    print("=" * 60)
    for a in apis:
        flag = "✓" if a.get("configured") else "✗"
        print(f"  {flag} {a['name']:<20} ({len(a['operations'])} operations)")
    print(f"\nListening on http://0.0.0.0:{port}")
    print("=" * 60 + "\n")
    app.run(host="0.0.0.0", port=port, debug=True)
