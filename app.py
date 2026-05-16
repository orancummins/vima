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
def home():
    return render_template("home.html")


@app.route("/app")
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

_ENV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")

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
        ],
    },
    {
        "id": "bces",
        "title": "Benefits Content Eligibility",
        "subtitle": "Mastercard Benefits Content Eligibility Service (BCES)",
        "docs_url": "https://developer.mastercard.com/bces-service/documentation/",
        "fields": [
            {"key": "BCES_CONSUMER_KEY",        "label": "Consumer Key",     "type": "password", "info": "OAuth 1.0a Consumer Key. Create a project on developer.mastercard.com, add the Benefits Content Eligibility Service API, and copy the Consumer Key."},
            {"key": "BCES_SIGNING_KEY_PATH",     "label": "Signing Key File", "type": "file",     "info": "PKCS12 (.p12) signing key file. In your Mastercard Developers project, click 'Generate signing keys' to download this file."},
            {"key": "BCES_SIGNING_KEY_ALIAS",    "label": "Key Alias",        "type": "text",     "info": "Alias for the private key within the .p12 file. Shown when generating keys on Mastercard Developers."},
            {"key": "BCES_SIGNING_KEY_PASSWORD", "label": "Key Password",     "type": "password", "info": "Password protecting the .p12 key file. The default is 'keystorepassword'."},
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

    for key, val in updates.items():
        if key not in written:
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


@app.route("/config/upload-key", methods=["POST"])
def config_upload_key():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
    fobj = request.files["file"]
    fname = (fobj.filename or "").strip()
    if not fname:
        return jsonify({"error": "Empty filename"}), 400
    ext = os.path.splitext(fname)[1].lower()
    if ext not in (".p12", ".pkcs12"):
        return jsonify({"error": "Only .p12 or .pkcs12 files are accepted"}), 400
    # Use only basename to prevent path traversal
    safe_name = os.path.basename(fname)
    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), safe_name)
    fobj.save(save_path)
    return jsonify({"filename": safe_name, "path": safe_name})


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
    app.run(host="0.0.0.0", port=port, debug=True, use_reloader=False)
