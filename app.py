"""Vima — Mastercard APIs explorer.

A small Flask app on port 9021 that exposes a tabbed UI for testing
Mastercard Developer APIs (Open Finance, BIN Lookup, …) and demoing use
cases composed from them.
"""
import os
import time
import threading
import json
import queue
import uuid
import subprocess
import sys
from collections import deque

import truststore
truststore.inject_into_ssl()

import requests as _requests
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request, redirect, send_from_directory

_CONFIG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config")
load_dotenv(os.path.join(_CONFIG_DIR, ".env"))

from apis import registry as api_registry  # noqa: E402
from usecases import registry as usecase_registry  # noqa: E402
from simulator.blueprint import sim_bp  # noqa: E402
from simulator.capture import capture_response  # noqa: E402
from simulator.switcher import is_simulated  # noqa: E402


app = Flask(__name__)

# Register the in-process Vima Chat blueprint at /chat. Vima Chat is no
# longer a standalone service — it lives inside Mastercard Solution Studio.
from chat.app import chat_bp  # noqa: E402
app.register_blueprint(chat_bp)
app.secret_key = os.environ.get("SECRET_KEY", "vima-dev-secret")
app.register_blueprint(sim_bp)

# In-memory store for TxPush events (last 50)
_txpush_events: deque = deque(maxlen=50)

# ---------------------------------------------------------------------------
# Outbound API call logger — intercepts all `requests` calls to external APIs
# ---------------------------------------------------------------------------
_api_call_log: deque = deque(maxlen=50)
_api_call_seq = 0
_api_call_lock = threading.Lock()

# URLs containing these substrings are considered "internal" and are skipped
_INTERNAL_HOSTS = ("localhost", "127.0.0.1", "0.0.0.0", "::1", "cloudflare.com")

_orig_send = _requests.Session.send  # keep reference before patching


def _patched_send(self, prepared_request, **kwargs):
    url = prepared_request.url or ""
    # Log simulator requests (/api-sim/) even though they're on localhost
    is_simulator = "/api-sim/" in url
    is_external = is_simulator or not any(h in url for h in _INTERNAL_HOSTS)

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

# ---------------------------------------------------------------------------
# Client geo/IP status cache (for Open Finance US VPN indicator)
# ---------------------------------------------------------------------------
_ip_status_cache = {
    "ts": 0.0,
    "payload": None,
}


def _fetch_geo_payload(client_ip: str) -> dict:
    """Resolve country and public IP using external geo services."""
    # Prefer a plain-text trace endpoint that exposes the egress country directly.
    attempts = [
        ("https://www.cloudflare.com/cdn-cgi/trace", "cloudflare-trace"),
        ("https://ipapi.co/json/", "ipapi"),
        ("https://ipwho.is/", "ipwhois"),
        ("https://ipinfo.io/json", "ipinfo"),
    ]

    for url, provider in attempts:
        try:
            # verify=False: VPN SSL-inspection injects a self-signed cert into the
            # chain, causing standard cert verification to fail.  These requests
            # carry no credentials so disabling verification here is safe.
            import urllib3
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            resp = _requests.get(url, timeout=4.0, verify=False)
            resp.raise_for_status()
            raw = resp.text
            if provider == "cloudflare-trace":
                trace = {}
                for line in raw.splitlines():
                    if "=" in line:
                        key, value = line.split("=", 1)
                        trace[key.strip()] = value.strip()
                country = (trace.get("loc") or "").upper()
                detected_ip = trace.get("ip") or client_ip
            else:
                data = json.loads(raw)
                if provider == "ipapi":
                    country = (data.get("country_code") or data.get("country") or "").upper()
                    detected_ip = data.get("ip") or client_ip
                elif provider == "ipwhois":
                    country = (data.get("country_code") or data.get("country") or "").upper()
                    detected_ip = data.get("ip") or client_ip
                else:
                    country = (data.get("country") or "").upper()
                    detected_ip = data.get("ip") or client_ip
            if country:
                return {
                    "ok": True,
                    "provider": provider,
                    "country_code": country,
                    "ip": str(detected_ip or ""),
                }
        except Exception:
            continue

    return {
        "ok": False,
        "provider": None,
        "country_code": "",
        "ip": str(client_ip or ""),
    }


# ----------------------------------------------------------------------------
# Pages
# ----------------------------------------------------------------------------

@app.route("/")
def home():
    return redirect("/app")


@app.route("/app")
def index():
    return render_template(
        "index.html",
        apis=api_registry.manifests(),
        use_cases=usecase_registry.manifests(),
        cache_bust=int(os.path.getmtime(os.path.join(os.path.dirname(__file__), 'static', 'js', 'app.js'))),
        css_bust=int(os.path.getmtime(os.path.join(os.path.dirname(__file__), 'static', 'css', 'styles.css'))),
    )


# ----------------------------------------------------------------------------
# API explorer endpoints
# ----------------------------------------------------------------------------

@app.route("/explorer/apis")
def explorer_apis():
    """Return the manifests for every registered API."""
    return jsonify({"apis": api_registry.manifests()})


@app.route("/diagnostics/us-ip-status")
def diagnostics_us_ip_status():
    """Return whether the caller appears to be on a US IP address."""
    now = time.time()
    cached = _ip_status_cache.get("payload")
    if cached and (now - float(_ip_status_cache.get("ts") or 0)) < 20:
        resp = jsonify(cached)
        resp.headers["Cache-Control"] = "no-store"
        return resp

    geo = _fetch_geo_payload((request.remote_addr or "").strip())
    country = (geo.get("country_code") or "").upper()
    is_us = country == "US"

    payload = {
        "success": bool(geo.get("ok")),
        "is_us": is_us,
        "country_code": country,
        "ip": geo.get("ip") or client_ip,
        "provider": geo.get("provider"),
        "checked_at": int(now),
    }
    _ip_status_cache["ts"] = now
    _ip_status_cache["payload"] = payload

    resp = jsonify(payload)
    resp.headers["Cache-Control"] = "no-store"
    return resp


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
    # Capture live responses into the simulator DB (non-simulated calls only)
    if result.get("success") and not is_simulated(api_id):
        resp_body = (result.get("response") or {}).get("body") or result.get("data")
        try:
            capture_response(api_id, op_id, resp_body)
        except Exception:
            pass
    # Merge in latest state snapshot for the UI
    result["state"] = getattr(mod, "get_state", lambda: {})()
    return jsonify(result)


@app.route("/explorer/consent/3ds-flow")
def consent_3ds_flow():
    """Unified 3DS browser flow page.

    Runs the EMV 3DS protocol end-to-end inside the user's browser, matching
    Mastercard's reference implementation:

      1. Fingerprint (hidden iframe POSTs threeDSMethodData to the ACS URL).
         The ACS returns JS that runs in that iframe, collects browser caps,
         posts to /process_browser_attributes, which then posts to Mastercard's
         server-to-server notification URL. When done it sends a postMessage
         (threeds-method-notification) to this page. We also have a 10s timeout.

      2. Start authentication — POST start-authentication with auth.params
         containing fingerprintStatus + browser info (user agent, screen size,
         timezone, etc). Response is one of:
            AUTHENTICATED      — frictionless, done.
            AUTH_IN_PROGRESS   — challenge required, params include acsUrl + encodedCReq.
            AUTH_FAILED        — failure.

      3. Challenge (only if AUTH_IN_PROGRESS) — visible iframe POSTs creq to acsUrl.
         The ACS shows the OTP UI (sandbox OTP: 123456). When the user submits
         and the challenge completes the ACS posts to a CRes notification URL
         which sends a threeds-challenge-notification postMessage to this page.

      4. Verify authentication — POST verify-authentication (empty params) to
         finalise the consent.
    """
    card_ref    = request.args.get("card_ref", "")
    method_url  = request.args.get("method_url", "")
    method_data = request.args.get("method_data", "")
    trans_id    = request.args.get("trans_id", "")
    if not card_ref:
        return "Missing card_ref", 400

    import html as _html, json as _json
    safe = {
        "card_ref":    _html.escape(card_ref, quote=True),
        "method_url":  _html.escape(method_url, quote=True),
        "method_data": _html.escape(method_data, quote=True),
        "trans_id":    _html.escape(trans_id, quote=True),
    }
    cfg_json = _json.dumps(safe)

    page = """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>3DS Authentication — Consent enrollment</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, sans-serif;
           display: flex; flex-direction: column; align-items: center;
           min-height: 100vh; margin: 0; background: #f4f6fa; color: #333; padding: 20px; }
    .card { background: #fff; border-radius: 10px; padding: 32px 40px;
            box-shadow: 0 2px 16px rgba(0,0,0,.1); text-align: center;
            max-width: 560px; width: 100%; margin-top: 40px; }
    h2 { margin: 0 0 8px; font-size: 20px; }
    .step { color: #666; font-size: 13px; margin: 4px 0; }
    .status { font-size: 14px; margin: 12px 0; min-height: 20px; }
    .spinner { width: 32px; height: 32px; border: 3px solid #e0e0e0;
               border-top-color: #005b99; border-radius: 50%;
               animation: spin .8s linear infinite; margin: 16px auto; }
    @keyframes spin { to { transform: rotate(360deg); } }
    .ok   { color: #1a7f4b; font-weight: 600; }
    .err  { color: #b00020; font-weight: 600; }
    pre { text-align: left; background: #f5f5f5; padding: 12px; border-radius: 6px;
          font-size: 12px; overflow: auto; max-height: 240px; }
    #fp-frame  { display: none; }
    #challenge-wrap { display: none; margin-top: 24px; }
    #challenge-frame { width: 600px; max-width: 100%; height: 440px;
                       border: 1px solid #ccc; border-radius: 6px; background: #fff; }
  </style>
</head>
<body>
  <div class="card">
    <h2>3DS Authentication</h2>
    <div class="step" id="step-fp">1. Device fingerprint…</div>
    <div class="step" id="step-sa">2. Start authentication…</div>
    <div class="step" id="step-ch">3. Challenge (if needed)…</div>
    <div class="step" id="step-vf">4. Verify authentication…</div>
    <div class="spinner" id="spinner"></div>
    <div class="status" id="status">Starting…</div>
    <pre id="result" style="display:none"></pre>
  </div>

  <div id="challenge-wrap" class="card">
    <h2>Please complete the challenge</h2>
    <div class="step">Sandbox OTP: <strong>123456</strong></div>
    <iframe id="challenge-frame" name="challenge-frame"></iframe>
  </div>

  <iframe id="fp-frame" name="fp-frame"></iframe>

  <script>
  (function() {
    var CFG = __CFG__;
    var statusEl = document.getElementById('status');
    var resultEl = document.getElementById('result');
    var spinnerEl = document.getElementById('spinner');

    function setStatus(msg, cls) {
      statusEl.textContent = msg;
      statusEl.className = 'status ' + (cls || '');
    }
    function markStep(id, mark) {
      var el = document.getElementById(id);
      if (el) el.textContent = mark + ' ' + el.textContent.replace(/^[✓✗•]\\s*/, '');
    }
    function showJSON(obj) {
      resultEl.style.display = 'block';
      resultEl.textContent = JSON.stringify(obj, null, 2);
    }
    function hideSpinner() { spinnerEl.style.display = 'none'; }

    function post(url, body) {
      return fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
      }).then(function(r) { return r.json(); });
    }

    function browserInfo(fpStatus) {
      return {
        fingerprintStatus:   fpStatus,
        challengeWindowSize: '04',
        browserAcceptHeader: 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        browserColorDepth:   String(window.screen.colorDepth),
        browserJavaEnabled:  false,
        browserLanguage:     navigator.language || 'en-US',
        browserScreenHeight: String(window.screen.height),
        browserScreenWidth:  String(window.screen.width),
        browserTZ:           String(new Date().getTimezoneOffset()),
        browserUserAgent:    window.navigator.userAgent,
      };
    }

    // ---- step 1: fingerprint ----
    function doFingerprint() {
      return new Promise(function(resolve) {
        if (!CFG.method_url || !CFG.method_data) {
          markStep('step-fp', '•');
          resolve('unavailable');
          return;
        }
        var done = false;
        function finish(status) {
          if (done) return;
          done = true;
          window.removeEventListener('message', onMsg);
          markStep('step-fp', status === 'complete' ? '✓' : '•');
          resolve(status);
        }
        function onMsg(e) {
          if (e && e.data && e.data.type === 'threeds-method-notification') {
            finish('complete');
          }
        }
        window.addEventListener('message', onMsg);

        // The reference impl writes an HTML doc into the iframe that submits
        // its own form to the ACS URL. We do the same so the iframe controls
        // the navigation; the ACS will later navigate the iframe back to the
        // notification page which posts the message to our window.
        var html =
          '<script>document.addEventListener("DOMContentLoaded",function(){'
          + 'var f=document.createElement("form");f.method="POST";'
          + 'f.action=' + JSON.stringify(CFG.method_url) + ';'
          + 'var i=document.createElement("input");i.name="threeDSMethodData";'
          + 'i.value=' + JSON.stringify(CFG.method_data) + ';'
          + 'f.appendChild(i);document.body.appendChild(f);f.submit();'
          + '});<\\/script>';
        var iframe = document.getElementById('fp-frame');
        var doc = iframe.contentWindow.document;
        doc.open(); doc.write('<html><body>' + html + '</body></html>'); doc.close();

        setTimeout(function() { finish('timeout'); }, 10000);
      });
    }

    // ---- step 3: challenge (only if AUTH_IN_PROGRESS) ----
    function doChallenge(acsUrl, creq) {
      return new Promise(function(resolve) {
        document.getElementById('challenge-wrap').style.display = 'block';
        function onMsg(e) {
          if (e && e.data && e.data.type === 'threeds-challenge-notification') {
            window.removeEventListener('message', onMsg);
            markStep('step-ch', '✓');
            resolve();
          }
        }
        window.addEventListener('message', onMsg);

        var html =
          '<script>document.addEventListener("DOMContentLoaded",function(){'
          + 'var f=document.createElement("form");f.method="POST";'
          + 'f.action=' + JSON.stringify(acsUrl) + ';'
          + 'var i=document.createElement("input");i.name="creq";'
          + 'i.value=' + JSON.stringify(creq) + ';'
          + 'f.appendChild(i);document.body.appendChild(f);f.submit();'
          + '});<\\/script>';
        var iframe = document.getElementById('challenge-frame');
        var doc = iframe.contentWindow.document;
        doc.open(); doc.write('<html><body>' + html + '</body></html>'); doc.close();
      });
    }

    // ---- main ----
    function run() {
      setStatus('Running 3DS Method (device fingerprint)…');
      doFingerprint().then(function(fpStatus) {
        setStatus('Calling start-authentication (' + fpStatus + ')…');
        return post('/explorer/consent/execute', {
          operation: 'start_authentication',
          params: Object.assign(
            { card_ref: CFG.card_ref, auth_type: 'THREEDS',
              auth_params: JSON.stringify(browserInfo(fpStatus)) },
            {}
          ),
        });
      }).then(function(sa) {
        if (!sa.success) {
          markStep('step-sa', '✗');
          hideSpinner();
          setStatus('start-authentication failed', 'err');
          showJSON(sa.error || sa);
          return;
        }
        markStep('step-sa', '✓');
        var auth   = (sa.data && sa.data.auth) || {};
        var status = auth.status;
        var params = auth.params || {};
        if (status === 'AUTHENTICATED') {
          hideSpinner();
          markStep('step-ch', '•');
          markStep('step-vf', '•');
          setStatus('Frictionless authentication succeeded.', 'ok');
          showJSON(sa.data);
          return;
        }
        if (status === 'AUTH_FAILED') {
          hideSpinner();
          markStep('step-ch', '✗');
          setStatus('Authentication failed.', 'err');
          showJSON(sa.data);
          return;
        }
        if (status !== 'AUTH_IN_PROGRESS') {
          hideSpinner();
          setStatus('Unexpected status: ' + status, 'err');
          showJSON(sa.data);
          return;
        }
        // challenge required
        setStatus('Challenge required — please complete the OTP in the iframe below.');
        var acsUrl = params.acsUrl || params.acsURL;
        var creq   = params.encodedCReq || params.creq;
        return doChallenge(acsUrl, creq).then(function() {
          setStatus('Verifying authentication…');
          return post('/explorer/consent/execute', {
            operation: 'verify_authentication',
            params: { card_ref: CFG.card_ref, auth_type: 'THREEDS', auth_params: '{}' },
          });
        }).then(function(vr) {
          document.getElementById('challenge-wrap').style.display = 'none';
          hideSpinner();
          if (vr && vr.success) {
            markStep('step-vf', '✓');
            setStatus('Authentication complete.', 'ok');
            showJSON(vr.data);
          } else {
            markStep('step-vf', '✗');
            setStatus('verify-authentication failed', 'err');
            showJSON((vr && vr.error) || vr);
          }
        });
      }).catch(function(err) {
        hideSpinner();
        setStatus('Error: ' + (err && err.message ? err.message : err), 'err');
      });
    }
    run();
  })();
  </script>
</body>
</html>"""
    page = page.replace("__CFG__", cfg_json)
    return page, 200, {"Content-Type": "text/html; charset=utf-8"}


# ----------------------------------------------------------------------------
# Use cases
# ----------------------------------------------------------------------------

@app.route("/testchat/<path:filename>")
def testchat_files(filename: str):
    """Serve files from the self-contained testchat use-case directory."""
    directory = os.path.join(os.path.dirname(__file__), "usecases", "testchat")
    return send_from_directory(directory, filename)


@app.route("/sonic/<path:filename>")
def sonic_files(filename: str):
    """Serve files from the self-contained sonic use-case directory."""
    directory = os.path.join(os.path.dirname(__file__), "usecases", "sonic")
    return send_from_directory(directory, filename)


@app.route("/pfm/<path:filename>")
def pfm_files(filename: str):
    """Serve files from the self-contained pfm use-case directory."""
    directory = os.path.join(os.path.dirname(__file__), "usecases", "pfm")
    return send_from_directory(directory, filename)


@app.route("/enrichment/<path:filename>")
def enrichment_files(filename: str):
    """Serve files from the self-contained enrichment use-case directory."""
    directory = os.path.join(os.path.dirname(__file__), "usecases", "enrichment")
    return send_from_directory(directory, filename)


@app.route("/binlookup/<path:filename>")
def binlookup_files(filename: str):
    """Serve files from the self-contained binlookup use-case directory."""
    directory = os.path.join(os.path.dirname(__file__), "usecases", "binlookup")
    return send_from_directory(directory, filename)


@app.route("/clarity/<path:filename>")
def clarity_files(filename: str):
    """Serve files from the self-contained clarity use-case directory."""
    directory = os.path.join(os.path.dirname(__file__), "usecases", "clarity")
    return send_from_directory(directory, filename)


@app.route("/easysavings/<path:filename>")
def easysavings_files(filename: str):
    """Serve files from the self-contained easysavings use-case directory."""
    directory = os.path.join(os.path.dirname(__file__), "usecases", "easysavings")
    return send_from_directory(directory, filename)


@app.route("/identity/<path:filename>")
def identity_files(filename: str):
    """Serve files from the self-contained identity use-case directory."""
    directory = os.path.join(os.path.dirname(__file__), "usecases", "identity")
    return send_from_directory(directory, filename)


@app.route("/psi/<path:filename>")
def psi_files(filename: str):
    """Serve files from the self-contained psi use-case directory."""
    directory = os.path.join(os.path.dirname(__file__), "usecases", "psi")
    return send_from_directory(directory, filename)


@app.route("/places/<path:filename>")
def places_files(filename: str):
    """Serve files from the self-contained places use-case directory."""
    directory = os.path.join(os.path.dirname(__file__), "usecases", "places")
    return send_from_directory(directory, filename)


@app.route("/recurring/<path:filename>")
def recurring_files(filename: str):
    """Serve files from the self-contained recurring use-case directory."""
    directory = os.path.join(os.path.dirname(__file__), "usecases", "recurring")
    return send_from_directory(directory, filename)


@app.route("/specials/<path:filename>")
def specials_files(filename: str):
    """Serve files from the self-contained specials use-case directory."""
    directory = os.path.join(os.path.dirname(__file__), "usecases", "specials")
    return send_from_directory(directory, filename)


@app.route("/findacard/<path:filename>")
def findacard_files(filename: str):
    """Serve files from the self-contained findacard use-case directory."""
    directory = os.path.join(os.path.dirname(__file__), "usecases", "findacard")
    return send_from_directory(directory, filename)


@app.route("/financeincolour/<path:filename>")
def financeincolour_files(filename: str):
    """Serve files from the self-contained financeincolour use-case directory."""
    directory = os.path.join(os.path.dirname(__file__), "usecases", "financeincolour")
    return send_from_directory(directory, filename)


@app.route("/catalog")
def catalog():
    """Unified catalog of all registered APIs and Use Cases."""
    apis = api_registry.manifests()
    use_cases = usecase_registry.manifests()
    return jsonify({
        "apis": [
            {
                "id": a["id"],
                "name": a["name"],
                "configured": a.get("configured", False),
                "categories": a.get("categories", []),
                "operations": [op["id"] for op in a.get("operations", [])],
            }
            for a in apis
        ],
        "use_cases": [
            {
                "id": u["id"],
                "name": u["name"],
                "apis": u.get("apis", []),
                "render": u.get("render", ""),
            }
            for u in use_cases
        ],
        "summary": {
            "total_apis": len(apis),
            "configured_apis": sum(1 for a in apis if a.get("configured")),
            "total_use_cases": len(use_cases),
        },
    })


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


# ----------------------------------------------------------------------------
# BIN Lookup — server-side SQLite FTS5 BIN ranges cache
# ----------------------------------------------------------------------------
import sqlite3 as _sqlite3

_BIN_CACHE = {"status": "idle", "count": 0, "loaded_at": None, "error": None, "persisted": False}
_BIN_CACHE_LOCK = threading.Lock()
_BIN_DB_CONN = None  # sqlite3 connection (disk-backed, persists across restarts)
_BIN_DB_PATH = os.path.join(os.path.dirname(__file__), "data", "bin_ranges.db")
_BIN_DB_TMP  = _BIN_DB_PATH + ".tmp"


def _bin_try_load_from_disk():
    """Called at startup: open the persisted disk DB if it exists."""
    global _BIN_DB_CONN
    if not os.path.exists(_BIN_DB_PATH):
        return
    try:
        conn = _sqlite3.connect(_BIN_DB_PATH, check_same_thread=False)
        conn.row_factory = _sqlite3.Row
        meta = conn.execute("SELECT count, loaded_at FROM meta LIMIT 1").fetchone()
        if not meta:
            conn.close()
            return
        actual = conn.execute("SELECT COUNT(*) FROM bin_ranges").fetchone()[0]
        if actual == 0:
            conn.close()
            return
        with _BIN_CACHE_LOCK:
            _BIN_DB_CONN = conn
            _BIN_CACHE["count"] = actual
            _BIN_CACHE["loaded_at"] = meta["loaded_at"]
            _BIN_CACHE["status"] = "loaded"
            _BIN_CACHE["persisted"] = True
            _BIN_CACHE["error"] = None
    except Exception:
        pass  # corrupt / incompatible DB — user can reload via UI


def _bin_build_sqlite(rows):
    """Build a disk-backed SQLite database with FTS5 index and persist it."""
    import shutil
    os.makedirs(os.path.dirname(_BIN_DB_PATH), exist_ok=True)
    # Write to a temp file first so a crash mid-build doesn't corrupt the live DB
    if os.path.exists(_BIN_DB_TMP):
        os.remove(_BIN_DB_TMP)
    conn = _sqlite3.connect(_BIN_DB_TMP, check_same_thread=False)
    conn.row_factory = _sqlite3.Row
    conn.execute("""CREATE TABLE meta (count INTEGER, loaded_at INTEGER)""")
    conn.execute("""
        CREATE TABLE bin_ranges (
            binNum TEXT, lowAccountRange TEXT, highAccountRange TEXT,
            binLength TEXT, acceptanceBrand TEXT, ica TEXT, customerName TEXT,
            smartDataEnabled TEXT, countryCode TEXT, countryAlpha3 TEXT, countryName TEXT,
            localUse TEXT, authorizationOnly TEXT, productCode TEXT, productDescription TEXT,
            governmentRange TEXT, nonReloadableIndicator TEXT, anonymousPrepaidIndicator TEXT,
            cardholderCurrencyIndicator TEXT, billingCurrencyDefault TEXT,
            comboCardIndicator TEXT, flexCardIndicator TEXT, fasterFundsIndicator TEXT,
            moneySendIndicator TEXT, gamblingBlockEnabled TEXT, programName TEXT,
            vertical TEXT, fundingSource TEXT, consumerType TEXT,
            affiliate TEXT, paymentAccountType TEXT, mastercardOneParticipationIndicator TEXT
        )
    """)
    conn.execute("CREATE INDEX idx_bin ON bin_ranges(binNum)")
    conn.execute("CREATE INDEX idx_low ON bin_ranges(lowAccountRange)")
    # FTS5 content table — fast full-text search on text columns
    conn.execute("""
        CREATE VIRTUAL TABLE bin_fts USING fts5(
            customerName, productDescription, countryName, acceptanceBrand, programName, vertical,
            content='bin_ranges', content_rowid='rowid', tokenize='unicode61'
        )
    """)

    records = []
    for row in rows:
        c = row.get("country", {})
        if isinstance(c, dict):
            cc, ca3, cn = str(c.get("code", "")), str(c.get("alpha3", "")), str(c.get("name", ""))
        else:
            cc, ca3, cn = "", "", str(c)
        records.append((
            str(row.get("binNum", "")), str(row.get("lowAccountRange", "")),
            str(row.get("highAccountRange", "")), str(row.get("binLength", "")),
            str(row.get("acceptanceBrand", "")), str(row.get("ica", "")),
            str(row.get("customerName", "")), str(row.get("smartDataEnabled", "")),
            cc, ca3, cn,
            str(row.get("localUse", "")), str(row.get("authorizationOnly", "")),
            str(row.get("productCode", "")), str(row.get("productDescription", "")),
            str(row.get("governmentRange", "")), str(row.get("nonReloadableIndicator", "")),
            str(row.get("anonymousPrepaidIndicator", "")),
            str(row.get("cardholderCurrencyIndicator", "")), str(row.get("billingCurrencyDefault", "")),
            str(row.get("comboCardIndicator", "")), str(row.get("flexCardIndicator", "")),
            str(row.get("fasterFundsIndicator", "")), str(row.get("moneySendIndicator", "")),
            str(row.get("gamblingBlockEnabled", "")), str(row.get("programName", "")),
            str(row.get("vertical", "")), str(row.get("fundingSource", "")),
            str(row.get("consumerType", "")), str(row.get("affiliate", "")),
            str(row.get("paymentAccountType", "")),
            str(row.get("mastercardOneParticipationIndicator", "")),
        ))

    conn.executemany(
        "INSERT INTO bin_ranges VALUES (" + ",".join(["?"] * 32) + ")",
        records,
    )
    conn.execute("INSERT INTO bin_fts(bin_fts) VALUES('rebuild')")
    conn.execute("INSERT INTO meta VALUES (?, ?)", (len(records), int(time.time())))
    conn.commit()
    conn.close()
    # Atomically replace the live DB file
    shutil.move(_BIN_DB_TMP, _BIN_DB_PATH)
    # Re-open a persistent connection to the final path
    final_conn = _sqlite3.connect(_BIN_DB_PATH, check_same_thread=False)
    final_conn.row_factory = _sqlite3.Row
    return final_conn


def _bin_row_to_dict(r):
    return {
        "binNum": r["binNum"], "lowAccountRange": r["lowAccountRange"],
        "highAccountRange": r["highAccountRange"], "binLength": r["binLength"],
        "acceptanceBrand": r["acceptanceBrand"], "ica": r["ica"],
        "customerName": r["customerName"], "smartDataEnabled": r["smartDataEnabled"],
        "country": {"code": r["countryCode"], "alpha3": r["countryAlpha3"], "name": r["countryName"]},
        "localUse": r["localUse"], "authorizationOnly": r["authorizationOnly"],
        "productCode": r["productCode"], "productDescription": r["productDescription"],
        "governmentRange": r["governmentRange"], "nonReloadableIndicator": r["nonReloadableIndicator"],
        "anonymousPrepaidIndicator": r["anonymousPrepaidIndicator"],
        "cardholderCurrencyIndicator": r["cardholderCurrencyIndicator"],
        "billingCurrencyDefault": r["billingCurrencyDefault"],
        "comboCardIndicator": r["comboCardIndicator"], "flexCardIndicator": r["flexCardIndicator"],
        "fasterFundsIndicator": r["fasterFundsIndicator"], "moneySendIndicator": r["moneySendIndicator"],
        "gamblingBlockEnabled": r["gamblingBlockEnabled"], "programName": r["programName"],
        "vertical": r["vertical"], "fundingSource": r["fundingSource"],
        "consumerType": r["consumerType"], "affiliate": r["affiliate"],
        "paymentAccountType": r["paymentAccountType"],
        "mastercardOneParticipationIndicator": r["mastercardOneParticipationIndicator"],
    }


def _bin_cache_do_load():
    """Background thread: fetch all BIN range pages and load into SQLite."""
    global _BIN_DB_CONN
    import ast
    import requests as _req
    import oauth1.authenticationutils as authutils
    from oauth1.oauth import OAuth

    consumer_key = os.environ.get("BINLOOKUP_CONSUMER_KEY", "")
    key_path = os.environ.get("BINLOOKUP_SIGNING_KEY_PATH", "")
    key_password = os.environ.get("BINLOOKUP_SIGNING_KEY_PASSWORD", "keystorepassword")
    env = os.environ.get("BINLOOKUP_ENV", "sandbox").lower()
    base_url = (
        "https://api.mastercard.com/bin-resources"
        if env == "production"
        else "https://sandbox.api.mastercard.com/bin-resources"
    )

    if not os.path.isabs(key_path):
        key_path = os.path.join(os.path.dirname(__file__), key_path)

    try:
        signing_key = authutils.load_signing_key(key_path, key_password)
    except Exception as e:
        with _BIN_CACHE_LOCK:
            _BIN_CACHE["status"] = "error"
            _BIN_CACHE["error"] = f"Could not load signing key: {e}"
        return

    rows = []
    page = 1
    total_pages = None
    try:
        while total_pages is None or page <= total_pages:
            url = f"{base_url}/bin-ranges?page={page}&size=10000"
            body_str = "[]"
            auth_header = OAuth.get_authorization_header(url, "POST", body_str, consumer_key, signing_key)
            headers = {"Content-Type": "application/json", "Accept": "application/json", "Authorization": auth_header}
            resp = _req.post(url, data=body_str, headers=headers, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            items = data.get("items", [])
            total_pages = data.get("totalPages", 1)
            for item in items:
                c = item.get("country", "")
                if isinstance(c, str) and c.startswith("{"):
                    try:
                        item["country"] = ast.literal_eval(c)
                    except Exception:
                        pass
            rows.extend(items)
            page += 1
    except Exception as e:
        with _BIN_CACHE_LOCK:
            _BIN_CACHE["status"] = "error"
            _BIN_CACHE["error"] = str(e)
        return

    try:
        db_conn = _bin_build_sqlite(rows)
    except Exception as e:
        with _BIN_CACHE_LOCK:
            _BIN_CACHE["status"] = "error"
            _BIN_CACHE["error"] = f"SQLite build failed: {e}"
        return

    with _BIN_CACHE_LOCK:
        old_conn = _BIN_DB_CONN
        _BIN_DB_CONN = db_conn
        _BIN_CACHE["count"] = len(rows)
        _BIN_CACHE["status"] = "loaded"
        _BIN_CACHE["loaded_at"] = int(time.time())
        _BIN_CACHE["persisted"] = True
        _BIN_CACHE["error"] = None
    if old_conn is not None:
        try:
            old_conn.close()
        except Exception:
            pass


@app.route("/usecases/binlookup/bin-ranges/status")
def binlookup_bin_ranges_status():
    with _BIN_CACHE_LOCK:
        return jsonify({
            "status": _BIN_CACHE["status"],
            "count": _BIN_CACHE["count"],
            "loaded_at": _BIN_CACHE["loaded_at"],
            "error": _BIN_CACHE["error"],
            "persisted": _BIN_CACHE["persisted"],
        })


@app.route("/usecases/binlookup/bin-ranges/load", methods=["POST"])
def binlookup_bin_ranges_load():
    with _BIN_CACHE_LOCK:
        if _BIN_CACHE["status"] == "loading":
            return jsonify({"ok": False, "message": "Already loading"})
        _BIN_CACHE["status"] = "loading"
        _BIN_CACHE["error"] = None
    t = threading.Thread(target=_bin_cache_do_load, daemon=True)
    t.start()
    return jsonify({"ok": True, "message": "Loading started"})


@app.route("/usecases/binlookup/bin-ranges/search")
def binlookup_bin_ranges_search():
    q = request.args.get("q", "").strip()
    per_page = 50
    page = max(1, int(request.args.get("page", 1)))
    offset = (page - 1) * per_page

    with _BIN_CACHE_LOCK:
        status = _BIN_CACHE["status"]
        conn = _BIN_DB_CONN

    if status != "loaded" or conn is None:
        return jsonify({"error": "BIN ranges not loaded", "results": [], "total": 0, "pages": 0, "page": 1})
    if not q:
        return jsonify({"results": [], "total": 0, "pages": 0, "page": 1})

    # Detect quoted exact-issuer mode: query starts and ends with " or '
    _exact_match = None
    if (q.startswith('"') and q.endswith('"') and len(q) > 2) or \
       (q.startswith("'") and q.endswith("'") and len(q) > 2):
        _exact_match = q[1:-1].strip()

    is_numeric = q.isdigit()
    try:
        if _exact_match is not None:
            # Exact case-insensitive match on customerName (issuer)
            total = conn.execute(
                "SELECT COUNT(*) FROM bin_ranges WHERE customerName = ? COLLATE NOCASE",
                (_exact_match,),
            ).fetchone()[0]
            cur = conn.execute(
                "SELECT * FROM bin_ranges WHERE customerName = ? COLLATE NOCASE ORDER BY binNum LIMIT ? OFFSET ?",
                (_exact_match, per_page, offset),
            )
        elif is_numeric:
            total = conn.execute(
                "SELECT COUNT(*) FROM bin_ranges WHERE binNum LIKE ? OR lowAccountRange LIKE ?",
                (q + "%", q + "%"),
            ).fetchone()[0]
            cur = conn.execute(
                "SELECT * FROM bin_ranges WHERE binNum LIKE ? OR lowAccountRange LIKE ? LIMIT ? OFFSET ?",
                (q + "%", q + "%", per_page, offset),
            )
        else:
            tokens = [t for t in q.replace('"', "").replace("'", "").replace("(", "").replace(")", "").split() if t]
            if not tokens:
                return jsonify({"results": [], "total": 0, "pages": 0, "page": 1})
            fts_q = " ".join(f'"{t}"*' for t in tokens)
            total = conn.execute(
                "SELECT COUNT(*) FROM bin_fts WHERE bin_fts MATCH ?",
                (fts_q,),
            ).fetchone()[0]
            cur = conn.execute(
                """SELECT bin_ranges.* FROM bin_fts
                   JOIN bin_ranges ON bin_fts.rowid = bin_ranges.rowid
                   WHERE bin_fts MATCH ?
                   ORDER BY rank LIMIT ? OFFSET ?""",
                (fts_q, per_page, offset),
            )
        results = [_bin_row_to_dict(r) for r in cur.fetchall()]
        import math
        pages = math.ceil(total / per_page) if total else 0
        return jsonify({"results": results, "total": total, "page": page, "pages": pages})
    except Exception as e:
        return jsonify({"error": str(e), "results": [], "total": 0, "pages": 0, "page": 1})


# BIN Lookup — download all BIN ranges as CSV
# ----------------------------------------------------------------------------

@app.route("/usecases/binlookup/download-bins")
def binlookup_download_bins():
    """Stream all BIN ranges from the Mastercard BIN Resource API as a CSV."""
    import csv
    import io
    import json as _json
    import requests as _req
    import oauth1.authenticationutils as authutils
    from oauth1.oauth import OAuth
    from flask import Response, stream_with_context

    consumer_key = os.environ.get("BINLOOKUP_CONSUMER_KEY", "")
    key_path = os.environ.get("BINLOOKUP_SIGNING_KEY_PATH", "")
    key_password = os.environ.get("BINLOOKUP_SIGNING_KEY_PASSWORD", "keystorepassword")
    env = os.environ.get("BINLOOKUP_ENV", "sandbox").lower()
    base_url = "https://api.mastercard.com/bin-resources" if env == "production" else "https://sandbox.api.mastercard.com/bin-resources"

    if not consumer_key or consumer_key == "your-consumer-key-here" or not key_path:
        return jsonify({"error": "BIN Lookup is not configured."}), 400

    if not os.path.isabs(key_path):
        key_path = os.path.join(os.path.dirname(__file__), key_path)

    try:
        signing_key = authutils.load_signing_key(key_path, key_password)
    except Exception as e:
        return jsonify({"error": f"Could not load signing key: {e}"}), 500

    def generate():
        output = io.StringIO()
        writer = None
        page = 1
        total_pages = None

        while total_pages is None or page <= total_pages:
            url = f"{base_url}/bin-ranges?page={page}&size=10000"
            body_str = "[]"
            try:
                auth_header = OAuth.get_authorization_header(url, "POST", body_str, consumer_key, signing_key)
                headers = {"Content-Type": "application/json", "Accept": "application/json", "Authorization": auth_header}
                resp = _req.post(url, data=body_str, headers=headers, timeout=30)
                resp.raise_for_status()
                data = resp.json()
            except Exception as e:
                yield f"# Error on page {page}: {e}\n"
                break

            items = data.get("items", [])
            total_pages = data.get("totalPages", 1)

            for item in items:
                if writer is None:
                    writer = csv.DictWriter(output, fieldnames=list(item.keys()), extrasaction="ignore")
                    writer.writeheader()
                    yield output.getvalue()
                    output.seek(0); output.truncate(0)
                writer.writerow(item)
                yield output.getvalue()
                output.seek(0); output.truncate(0)

            page += 1

    return Response(
        stream_with_context(generate()),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=bin_ranges.csv"},
    )


@app.route("/usecases/findacard/health")
def findacard_health():
    """Check whether the Find A Card service is reachable on localhost:5432."""
    import socket
    try:
        sock = socket.create_connection(("127.0.0.1", 5432), timeout=1)
        sock.close()
        return jsonify({"online": True})
    except (socket.timeout, ConnectionRefusedError, OSError):
        return jsonify({"online": False})


@app.route("/api-call-log")
def api_call_log():
    """Return the last outbound API calls captured by the request logger."""
    since = request.args.get("since", type=int, default=0)
    with _api_call_lock:
        entries = [e for e in _api_call_log if e.get("seq", 0) > since]
    return jsonify({"calls": list(reversed(entries))})


# ----------------------------------------------------------------------------
# Config management
# ----------------------------------------------------------------------------

_ENV_PATH = os.path.join(_CONFIG_DIR, ".env")
_KEYS_DIR = os.path.join(_CONFIG_DIR, "keys")

_CONFIG_SCHEMA = [
    {
        "id": "open_banking",
        "title": "Open Banking",
        "subtitle": "Mastercard Open Banking (Finicity)",
        "docs_url": "https://developer.mastercard.com/open-banking-us/documentation/",
        "fields": [
            {"key": "PARTNER_ID",     "label": "Partner ID",     "type": "text",     "info": "Your Finicity Partner ID. Sign up at developer.mastercard.com, create an Open Banking project, and copy the Partner ID from your project credentials."},
            {"key": "PARTNER_SECRET", "label": "Partner Secret", "type": "password", "info": "Finicity Partner Secret, paired with your Partner ID. Available in your project credentials on Mastercard Developers. Keep this confidential."},
            {"key": "APP_KEY",        "label": "App Key",        "type": "password", "info": "Application key for your Open Banking project. Found alongside your Partner ID in the Mastercard Developers portal."},
            {"key": "API_BASE_URL",   "label": "API Base URL",   "type": "text",     "info": "Base URL for the Open Banking API. Use https://api.finicity.com for production or the sandbox URL for testing."},
        ],
    },
    {
        "id": "binlookup",
        "title": "BIN Lookup",
        "subtitle": "Mastercard BIN Lookup API",
        "docs_url": "https://developer.mastercard.com/bin-lookup/documentation/",
        "fields": [
            {"key": "BINLOOKUP_CONSUMER_KEY",        "label": "Consumer Key",     "type": "password", "info": "OAuth 1.0a Consumer Key. Create a project on developer.mastercard.com, add the BIN Lookup API, and copy the Consumer Key from the project overview page."},
            {"key": "BINLOOKUP_SIGNING_KEY_PATH",     "label": "Signing Key File", "type": "file",     "info": "PKCS12 (.p12) signing key file. In your Mastercard Developers project, click 'Generate signing keys' and download the .p12 file."},
            {"key": "BINLOOKUP_SIGNING_KEY_ALIAS",    "label": "Key Alias",        "type": "text",     "info": "Alias for the private key within the .p12 file — usually the lowercase project name (e.g. 'binlookup'). Shown when generating keys on Mastercard Developers."},
            {"key": "BINLOOKUP_SIGNING_KEY_PASSWORD", "label": "Key Password",     "type": "password", "info": "Password protecting the .p12 key file. The default for Mastercard Developer-generated keys is 'keystorepassword'."},
            {"key": "BINLOOKUP_ENV",                  "label": "Environment",      "type": "text",     "info": "API environment: 'sandbox' or 'production'."},
        ],
    },
    {
        "id": "consumerclarity",
        "title": "Consumer Clarity",
        "subtitle": "Mastercard Consumer Clarity API",
        "docs_url": "https://developer.mastercard.com/consumer-clarity-us/documentation/",
        "fields": [
            {"key": "CONSUMERCLARITY_CONSUMER_KEY",        "label": "Consumer Key",     "type": "password", "info": "OAuth 1.0a Consumer Key. Create a project on developer.mastercard.com, add the Consumer Clarity API, and copy the Consumer Key."},
            {"key": "CONSUMERCLARITY_SIGNING_KEY_PATH",     "label": "Signing Key File", "type": "file",     "info": "PKCS12 (.p12) signing key file. In your Mastercard Developers project, click 'Generate signing keys' to download this file."},
            {"key": "CONSUMERCLARITY_SIGNING_KEY_ALIAS",    "label": "Key Alias",        "type": "text",     "info": "Alias for the private key within the .p12 file — usually the lowercase project name. Shown when generating keys on Mastercard Developers."},
            {"key": "CONSUMERCLARITY_SIGNING_KEY_PASSWORD", "label": "Key Password",     "type": "password", "info": "Password protecting the .p12 key file. The default for Mastercard Developer-generated keys is 'keystorepassword'."},
            {"key": "CONSUMERCLARITY_ENV",                  "label": "Environment",      "type": "text",     "info": "API environment: 'sandbox' or 'production'."},
        ],
    },
    {
        "id": "easysavings",
        "title": "Easy Savings",
        "subtitle": "Mastercard Easy Savings API",
        "docs_url": "https://developer.mastercard.com/easy-savings/documentation/",
        "fields": [
            {"key": "EASYSAVINGS_CONSUMER_KEY",        "label": "Consumer Key",     "type": "password", "info": "OAuth 1.0a Consumer Key. Create a project on developer.mastercard.com, add the Easy Savings API, and copy the Consumer Key."},
            {"key": "EASYSAVINGS_SIGNING_KEY_PATH",     "label": "Signing Key File", "type": "file",     "info": "PKCS12 (.p12) signing key file. In your Mastercard Developers project, click 'Generate signing keys' to download this file."},
            {"key": "EASYSAVINGS_SIGNING_KEY_ALIAS",    "label": "Key Alias",        "type": "text",     "info": "Alias for the private key within the .p12 file. Shown when generating keys on Mastercard Developers."},
            {"key": "EASYSAVINGS_SIGNING_KEY_PASSWORD", "label": "Key Password",     "type": "password", "info": "Password protecting the .p12 key file. The default is 'keystorepassword'."},
            {"key": "EASYSAVINGS_ENV",                  "label": "Environment",      "type": "text",     "info": "API environment: 'sandbox' or 'production'."},
        ],
    },
    {
        "id": "places",
        "title": "Places",
        "subtitle": "Mastercard Places API",
        "docs_url": "https://developer.mastercard.com/places/documentation/",
        "fields": [
            {"key": "PLACES_CONSUMER_KEY",        "label": "Consumer Key",     "type": "password", "info": "OAuth 1.0a Consumer Key. Create a project on developer.mastercard.com, add the Places API, and copy the Consumer Key."},
            {"key": "PLACES_SIGNING_KEY_PATH",     "label": "Signing Key File", "type": "file",     "info": "PKCS12 (.p12) signing key file. In your Mastercard Developers project, click 'Generate signing keys' to download this file."},
            {"key": "PLACES_SIGNING_KEY_ALIAS",    "label": "Key Alias",        "type": "text",     "info": "Alias for the private key within the .p12 file. Shown when generating keys on Mastercard Developers."},
            {"key": "PLACES_SIGNING_KEY_PASSWORD", "label": "Key Password",     "type": "password", "info": "Password protecting the .p12 key file. The default is 'keystorepassword'."},
            {"key": "PLACES_ENV",                  "label": "Environment",      "type": "text",     "info": "API environment: 'sandbox' or 'production'."},
        ],
    },
    {
        "id": "priceless",
        "title": "Priceless Cities",
        "subtitle": "Mastercard Priceless Cities API",
        "docs_url": "https://developer.mastercard.com/priceless-cities/documentation/",
        "fields": [
            {"key": "PRICELESS_CONSUMER_KEY",        "label": "Consumer Key",     "type": "password", "info": "OAuth 1.0a Consumer Key. Create a project on developer.mastercard.com, add the Priceless Cities API, and copy the Consumer Key."},
            {"key": "PRICELESS_SIGNING_KEY_PATH",     "label": "Signing Key File", "type": "file",     "info": "PKCS12 (.p12) signing key file. In your Mastercard Developers project, click 'Generate signing keys' to download this file."},
            {"key": "PRICELESS_SIGNING_KEY_ALIAS",    "label": "Key Alias",        "type": "text",     "info": "Alias for the private key within the .p12 file. Shown when generating keys on Mastercard Developers."},
            {"key": "PRICELESS_SIGNING_KEY_PASSWORD", "label": "Key Password",     "type": "password", "info": "Password protecting the .p12 key file. The default is 'keystorepassword'."},
            {"key": "PRICELESS_ENV",                  "label": "Environment",      "type": "text",     "info": "API environment: 'sandbox' or 'production'."},
        ],
    },
    {
        "id": "txnotify",
        "title": "Transaction Notifications",
        "subtitle": "Mastercard Transaction Notifications API",
        "docs_url": "https://developer.mastercard.com/transaction-notifications/documentation/",
        "fields": [
            {"key": "TXNOTIFY_CONSUMER_KEY",        "label": "Consumer Key",     "type": "password", "info": "OAuth 1.0a Consumer Key. Create a project on developer.mastercard.com, add the Transaction Notifications API, and copy the Consumer Key."},
            {"key": "TXNOTIFY_SIGNING_KEY_PATH",     "label": "Signing Key File", "type": "file",     "info": "PKCS12 (.p12) signing key file. In your Mastercard Developers project, click 'Generate signing keys' to download this file."},
            {"key": "TXNOTIFY_SIGNING_KEY_ALIAS",    "label": "Key Alias",        "type": "text",     "info": "Alias for the private key within the .p12 file. Shown when generating keys on Mastercard Developers."},
            {"key": "TXNOTIFY_SIGNING_KEY_PASSWORD", "label": "Key Password",     "type": "password", "info": "Password protecting the .p12 key file. The default is 'keystorepassword'."},
            {"key": "TXNOTIFY_ENV",                  "label": "Environment",      "type": "text",     "info": "API environment: 'sandbox' or 'production'."},
        ],
    },
    {
        "id": "consent",
        "title": "Consent Management",
        "subtitle": "Mastercard Consent Management API",
        "docs_url": "https://developer.mastercard.com/consent-management/documentation/",
        "fields": [
            {"key": "CONSENT_CONSUMER_KEY",          "label": "Consumer Key",          "type": "password", "info": "OAuth 1.0a Consumer Key. Create a project on developer.mastercard.com, add the Consent Management API, and copy the Consumer Key."},
            {"key": "CONSENT_SIGNING_KEY_PATH",       "label": "Signing Key File",      "type": "file",     "info": "PKCS12 (.p12) signing key file. In your Mastercard Developers project, click 'Generate signing keys' to download this file."},
            {"key": "CONSENT_SIGNING_KEY_ALIAS",      "label": "Key Alias",             "type": "text",     "info": "Alias for the private key within the .p12 file. Shown when generating keys on Mastercard Developers."},
            {"key": "CONSENT_SIGNING_KEY_PASSWORD",   "label": "Key Password",          "type": "password", "info": "Password protecting the .p12 key file. The default is 'keystorepassword'."},
            {"key": "CONSENT_ENV",                    "label": "Environment",           "type": "text",     "info": "API environment: 'sandbox' or 'production'."},
            {"key": "CONSENT_ENCRYPTION_KEY_PATH",    "label": "Client Encryption Key", "type": "file",     "info": "Client encryption .pem file. Download from your Mastercard Developers project under 'Client Encryption Keys → Actions → Download'."},
        ],
    },
    {
        "id": "ofpub",
        "title": "Offers for Publishers",
        "subtitle": "Mastercard Offers for Publishers API",
        "docs_url": "https://developer.mastercard.com/presentment/documentation/",
        "fields": [
            {"key": "OFPUB_CONSUMER_KEY",        "label": "Consumer Key",     "type": "password", "info": "OAuth 1.0a Consumer Key. Create a project on developer.mastercard.com, add the Offers for Publishers API, and copy the Consumer Key."},
            {"key": "OFPUB_SIGNING_KEY_PATH",     "label": "Signing Key File", "type": "file",     "info": "PKCS12 (.p12) signing key file. In your Mastercard Developers project, click 'Generate signing keys' to download this file."},
            {"key": "OFPUB_SIGNING_KEY_ALIAS",    "label": "Key Alias",        "type": "text",     "info": "Alias for the private key within the .p12 file. Shown when generating keys on Mastercard Developers."},
            {"key": "OFPUB_SIGNING_KEY_PASSWORD", "label": "Key Password",     "type": "password", "info": "Password protecting the .p12 key file. The default is 'keystorepassword'."},
            {"key": "OFPUB_ENV",                  "label": "Environment",      "type": "text",     "info": "API environment: 'sandbox' or 'production'."},
        ],
    },
    {
        "id": "ofmc",
        "title": "Offers Merchant Content",
        "subtitle": "Mastercard Offers Merchant Content API",
        "docs_url": "https://developer.mastercard.com/eop-admin/documentation/",
        "fields": [
            {"key": "OFMC_CONSUMER_KEY",        "label": "Consumer Key",     "type": "password", "info": "OAuth 1.0a Consumer Key. Create a project on developer.mastercard.com, add the Offers Merchant Content API, and copy the Consumer Key."},
            {"key": "OFMC_SIGNING_KEY_PATH",     "label": "Signing Key File", "type": "file",     "info": "PKCS12 (.p12) signing key file. In your Mastercard Developers project, click 'Generate signing keys' to download this file."},
            {"key": "OFMC_SIGNING_KEY_ALIAS",    "label": "Key Alias",        "type": "text",     "info": "Alias for the private key within the .p12 file. Shown when generating keys on Mastercard Developers."},
            {"key": "OFMC_SIGNING_KEY_PASSWORD", "label": "Key Password",     "type": "password", "info": "Password protecting the .p12 key file. The default is 'keystorepassword'."},
            {"key": "OFMC_ENV",                  "label": "Environment",      "type": "text",     "info": "API environment: 'sandbox' or 'production'."},
        ],
    },
    {
        "id": "eligibility",
        "title": "Benefits Eligibility",
        "subtitle": "Mastercard Benefits Eligibility API",
        "docs_url": "https://developer.mastercard.com/eligibility-api/documentation/",
        "fields": [
            {"key": "ELIGIBILITY_CONSUMER_KEY",        "label": "Consumer Key",     "type": "password", "info": "OAuth 1.0a Consumer Key. Create a project on developer.mastercard.com, add the Benefits Eligibility API, and copy the Consumer Key."},
            {"key": "ELIGIBILITY_SIGNING_KEY_PATH",     "label": "Signing Key File", "type": "file",     "info": "PKCS12 (.p12) signing key file. In your Mastercard Developers project, click 'Generate signing keys' to download this file."},
            {"key": "ELIGIBILITY_SIGNING_KEY_ALIAS",    "label": "Key Alias",        "type": "text",     "info": "Alias for the private key within the .p12 file. Shown when generating keys on Mastercard Developers."},
            {"key": "ELIGIBILITY_SIGNING_KEY_PASSWORD", "label": "Key Password",     "type": "password", "info": "Password protecting the .p12 key file. The default is 'keystorepassword'."},
            {"key": "ELIGIBILITY_ENV",                  "label": "Environment",      "type": "text",     "info": "API environment: 'sandbox' or 'production'."},
        ],
    },
    {
        "id": "bces",
        "title": "Benefits Content Eligibility",
        "subtitle": "Mastercard Benefits Content Eligibility Service (BCES)",
        "docs_url": "https://developer.mastercard.com/bces-service/documentation/",
        "fields": [
            {"key": "BCES_CONSUMER_KEY",             "label": "Consumer Key",          "type": "password", "info": "OAuth 1.0a Consumer Key. Create a project on developer.mastercard.com, add the Benefits Content Eligibility Service API, and copy the Consumer Key."},
            {"key": "BCES_SIGNING_KEY_PATH",          "label": "Signing Key File",      "type": "file",     "info": "PKCS12 (.p12) signing key file. In your Mastercard Developers project, click 'Generate signing keys' to download this file."},
            {"key": "BCES_SIGNING_KEY_ALIAS",         "label": "Key Alias",             "type": "text",     "info": "Alias for the private key within the .p12 file. Shown when generating keys on Mastercard Developers."},
            {"key": "BCES_SIGNING_KEY_PASSWORD",      "label": "Key Password",          "type": "password", "info": "Password protecting the .p12 key file. The default is 'keystorepassword'."},
            {"key": "BCES_ENV",                       "label": "Environment",           "type": "text",     "info": "API environment: 'sandbox' or 'production'."},
            {"key": "BCES_ENCRYPTION_CERT_PATH",      "label": "Client Encryption Key", "type": "file",     "info": "Client encryption .pem file. Download from your Mastercard Developers project under 'Client Encryption Keys → Actions → Download'."},
        ],
    },
    {
        "id": "claude_chat",
        "title": "Claude Chat",
        "subtitle": "Anthropic Claude API for the embedded coding assistant",
        "docs_url": "https://console.anthropic.com/",
        "exclude_export": True,
        "fields": [
            {"key": "ANTHROPIC_API_KEY", "label": "API Key", "type": "password", "info": "Your Anthropic API key. Sign up at console.anthropic.com, go to Settings → API Keys, and create a new key. Keys start with 'sk-ant-'. Usage is billed to your Anthropic account."},
        ],
    },
]


def _read_env_values() -> dict:
    """Parse .env file, return {KEY: value} preserving raw values."""
    result: dict = {}
    try:
        with open(_ENV_PATH, "r", encoding="utf-8") as fh:
            for line in fh:
                s = line.strip()
                if s and not s.startswith("#") and "=" in s:
                    key, _, val = s.partition("=")
                    result[key.strip()] = val.strip()
    except OSError:
        pass
    return result


def _write_env_values(updates: dict) -> None:
    """Write updated key=value pairs into .env, preserving comments and order."""
    try:
        with open(_ENV_PATH, "r", encoding="utf-8") as fh:
            lines = fh.readlines()
    except OSError:
        lines = []

    written: set = set()
    new_lines = []
    for line in lines:
        s = line.strip()
        if s and not s.startswith("#") and "=" in s:
            key, _, _ = s.partition("=")
            key = key.strip()
            if key in updates:
                new_lines.append(f"{key}={updates[key]}\n")
                written.add(key)
                continue
        new_lines.append(line)

    # Section headers to prepend when adding a key for the first time
    _SECTION_HEADERS = {
        "ANTHROPIC_API_KEY": "\n# CLAUDE / VIMA CHAT\n",
    }
    for key, val in updates.items():
        if key not in written:
            if key in _SECTION_HEADERS:
                new_lines.append(_SECTION_HEADERS[key])
            new_lines.append(f"{key}={val}\n")

    with open(_ENV_PATH, "w", encoding="utf-8") as fh:
        fh.writelines(new_lines)


@app.route("/config", methods=["GET"])
def config_get():
    env = _read_env_values()
    groups = []
    for g in _CONFIG_SCHEMA:
        fields = []
        for f in g["fields"]:
            fields.append({
                "key":   f["key"],
                "label": f["label"],
                "type":  f["type"],
                "info":  f["info"],
                "value": env.get(f["key"], ""),
            })
        groups.append({
            "id":       g["id"],
            "title":    g["title"],
            "subtitle": g["subtitle"],
            "docs_url": g["docs_url"],
            "fields":   fields,
        })
    return jsonify({"groups": groups})


@app.route("/config", methods=["POST"])
def config_save_route():
    body = request.get_json(silent=True) or {}
    updates = body.get("updates") or {}
    if not isinstance(updates, dict):
        return jsonify({"error": "updates must be an object"}), 400
    # Whitelist: only keys declared in the schema are accepted
    allowed = {f["key"] for g in _CONFIG_SCHEMA for f in g["fields"]}
    filtered = {k: str(v) for k, v in updates.items() if k in allowed}
    try:
        _write_env_values(filtered)
    except OSError as exc:
        return jsonify({"error": str(exc)}), 500
    load_dotenv(override=True)
    return jsonify({"saved": list(filtered.keys())})


@app.route("/config/export", methods=["GET"])
def config_export():
    """Export config/keys + .env (with ANTHROPIC_API_KEY redacted) as a zip."""
    import zipfile, io, re as _re

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        # .env — redact ANTHROPIC_API_KEY
        if os.path.isfile(_ENV_PATH):
            with open(_ENV_PATH, "r", encoding="utf-8") as fh:
                env_text = fh.read()
            env_text = _re.sub(
                r"(?m)^(ANTHROPIC_API_KEY\s*=\s*).*$",
                r"\1YOUR_ANTHROPIC_API_KEY_HERE",
                env_text,
            )
            zf.writestr("config/.env", env_text)
        # all key files — always use forward slashes in zip entries (cross-platform)
        if os.path.isdir(_KEYS_DIR):
            for fname in os.listdir(_KEYS_DIR):
                fpath = os.path.join(_KEYS_DIR, fname)
                if os.path.isfile(fpath):
                    zf.write(fpath, "config/keys/" + fname)

    buf.seek(0)
    from flask import send_file
    return send_file(
        buf,
        mimetype="application/zip",
        as_attachment=True,
        download_name="vima-config.zip",
    )


@app.route("/config/import", methods=["POST"])
def config_import():
    """Import a vima-config.zip — overwrites .env and key files."""
    import zipfile, io as _io

    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
    fobj = request.files["file"]
    try:
        data = fobj.read()
        with zipfile.ZipFile(_io.BytesIO(data)) as zf:
            # Normalise to forward slashes (handles zips created on Windows)
            names = zf.namelist()
            norm = {n: n.replace("\\", "/") for n in names}

            # Validate: must contain config/.env or config/keys/*
            valid_entries = [v for v in norm.values()
                             if v.startswith("config/.env") or v.startswith("config/keys/")]
            if not valid_entries:
                return jsonify({"error": "Zip does not contain a valid vima config layout"}), 400

            os.makedirs(_KEYS_DIR, exist_ok=True)
            imported = []
            for orig, name in norm.items():
                # .env
                if name == "config/.env":
                    env_text = zf.read(orig).decode("utf-8")
                    with open(_ENV_PATH, "w", encoding="utf-8") as fh:
                        fh.write(env_text)
                    load_dotenv(_ENV_PATH, override=True)
                    imported.append(".env")
                # key files
                elif name.startswith("config/keys/") and not name.endswith("/"):
                    fname = name.split("/")[-1]
                    if not fname:
                        continue
                    ext = os.path.splitext(fname)[1].lower()
                    if ext not in (".p12", ".pkcs12", ".pem"):
                        continue
                    dest = os.path.join(_KEYS_DIR, fname)
                    with open(dest, "wb") as fh:
                        fh.write(zf.read(orig))
                    imported.append("config/keys/" + fname)
        return jsonify({"imported": imported})
    except zipfile.BadZipFile:
        return jsonify({"error": "Not a valid zip file"}), 400
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


def config_upload_key():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
    fobj = request.files["file"]
    fname = (fobj.filename or "").strip()
    if not fname:
        return jsonify({"error": "Empty filename"}), 400
    ext = os.path.splitext(fname)[1].lower()
    if ext not in (".p12", ".pkcs12", ".pem"):
        return jsonify({"error": "Only .p12, .pkcs12, or .pem files are accepted"}), 400
    # Use only basename to prevent path traversal
    safe_name = os.path.basename(fname)
    os.makedirs(_KEYS_DIR, exist_ok=True)
    save_path = os.path.join(_KEYS_DIR, safe_name)
    fobj.save(save_path)
    # Always use forward slashes — works on Windows, Mac, and Linux
    rel_path = "config/keys/" + safe_name
    return jsonify({"filename": safe_name, "path": rel_path})


# ----------------------------------------------------------------------------
# Auto-provision endpoints
# ----------------------------------------------------------------------------

_provision_jobs: dict = {}


@app.route("/provision/status")
def provision_status():
    has_env = os.path.isfile(_ENV_PATH)
    apis = api_registry.manifests()
    configured = sum(1 for a in apis if a.get("configured"))
    needs_setup = not has_env or configured == 0
    return jsonify({"needs_setup": needs_setup, "configured": configured, "total": len(apis)})


@app.route("/provision/start", methods=["POST"])
def provision_start():
    body = request.get_json(silent=True) or {}
    selected_apis = body.get("apis", [])
    password = body.get("password", "foobar!!")
    if not selected_apis:
        return jsonify({"error": "No APIs selected"}), 400

    tool_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools", "mcd-key-automation")
    python_bin = os.path.join(tool_dir, ".venv", "bin", "python")

    # Preflight: ensure the tool's virtualenv exists
    if not os.path.isfile(python_bin):
        return jsonify({
            "error": (
                f"mcd-key-automation virtualenv not found at {python_bin}. "
                "Run: cd tools/mcd-key-automation && python -m venv .venv && "
                ".venv/bin/pip install -r requirements.txt && "
                ".venv/bin/playwright install chromium"
            )
        }), 500

    projects_yaml = "\n".join(
        f"  - name: {api}\n    apis: [{api}]" for api in selected_apis
    )
    cfg_text = f"""environment: sandbox
organization: mastercard
login_url: https://developer.mastercard.com/account/log-in
dashboard_url_pattern: "**/dashboard**"
key_password: "{password}"
projects:
{projects_yaml}
"""
    import tempfile
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        f.write(cfg_text)
        cfg_path = f.name

    job_id = str(uuid.uuid4())[:8]
    q = queue.Queue()
    _provision_jobs[job_id] = {"queue": q, "done": False, "proc": None}

    # Remove any stale zip so we only import a zip produced by this run
    zip_path = os.path.join(tool_dir, "output", "vima-config.zip")
    try:
        os.remove(zip_path)
    except OSError:
        pass

    def _run():
        rc = None
        try:
            proc = subprocess.Popen(
                [python_bin, "app/main.py", "run", "-c", cfg_path],
                cwd=tool_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
            )
            _provision_jobs[job_id]["proc"] = proc
            for line in proc.stdout:
                q.put(line.rstrip())
            proc.wait()
            rc = proc.returncode
        except Exception as exc:
            q.put(f"ERROR launching provisioner: {exc}")

        if rc is not None and rc != 0:
            q.put(f"ERROR: provisioner exited with code {rc}")

        if os.path.isfile(zip_path):
            try:
                import zipfile, io as _io
                with open(zip_path, "rb") as zf_file:
                    data = zf_file.read()
                with zipfile.ZipFile(_io.BytesIO(data)) as zf:
                    names = zf.namelist()
                    norm = {n: n.replace("\\", "/") for n in names}
                    os.makedirs(_KEYS_DIR, exist_ok=True)
                    for orig, name in norm.items():
                        if name == "config/.env":
                            env_text = zf.read(orig).decode("utf-8")
                            with open(_ENV_PATH, "w", encoding="utf-8") as fh:
                                fh.write(env_text)
                            load_dotenv(_ENV_PATH, override=True)
                        elif name.startswith("config/keys/") and not name.endswith("/"):
                            fname = name.split("/")[-1]
                            ext = os.path.splitext(fname)[1].lower()
                            if ext in (".p12", ".pkcs12", ".pem"):
                                dest = os.path.join(_KEYS_DIR, fname)
                                with open(dest, "wb") as fh:
                                    fh.write(zf.read(orig))
                q.put("__IMPORT_COMPLETE__")
            except Exception as exc:
                q.put(f"__IMPORT_ERROR__: {exc}")
        else:
            q.put("__NO_ZIP__")

        _provision_jobs[job_id]["done"] = True
        q.put(None)

    t = threading.Thread(target=_run, daemon=True)
    t.start()
    return jsonify({"job_id": job_id})


@app.route("/provision/stream/<job_id>")
def provision_stream(job_id):
    job = _provision_jobs.get(job_id)
    if not job:
        return jsonify({"error": "Unknown job"}), 404

    _SENTINELS = {"__DONE__", "__IMPORT_COMPLETE__", "__NO_ZIP__"}

    def generate():
        q = job["queue"]
        while True:
            try:
                line = q.get(timeout=60)
            except queue.Empty:
                yield "data: \n\n"
                continue
            if line is None:
                yield "data: __DONE__\n\n"
                break
            # Send sentinel control strings raw; JSON-encode all other log lines
            if line in _SENTINELS or (isinstance(line, str) and line.startswith("__IMPORT_ERROR__")):
                yield f"data: {line}\n\n"
            else:
                yield f"data: {json.dumps(line)}\n\n"

    return app.response_class(
        generate(),
        mimetype="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


if __name__ == "__main__":
    _bin_try_load_from_disk()
    port = int(os.environ.get("PORT", "9021"))
    apis = api_registry.manifests()
    print("\n" + "=" * 60)
    print("Vima - Mastercard API explorer")
    print("=" * 60)
    for a in apis:
        flag = "+" if a.get("configured") else "-"
        print(f"  {flag} {a['name']:<20} ({len(a['operations'])} operations)")
    print(f"\nListening on http://0.0.0.0:{port}")
    print("=" * 60 + "\n")
    app.run(host="0.0.0.0", port=port, debug=True, use_reloader=False)
