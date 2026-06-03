"""Runnable Python snippet generator for Mastercard APIs.

Strategy: rather than guessing how to call each API, we *actually*
invoke the registered module's ``execute()`` with sample parameters,
while temporarily monkey-patching the ``requests`` library to capture
the outbound HTTP call instead of sending it. That gives us the exact
URL, method, body and content-type the module would send — i.e. the
ground truth — which we then wrap in a self-contained, runnable
template that performs OAuth1 signing the same way the module does.

The generated snippet:

    * imports ``requests`` and ``mastercard-oauth1-signer`` (the same
      libraries Solution Studio uses)
    * reads credentials from the same env vars the module does
      (``<PREFIX>_CONSUMER_KEY``, ``<PREFIX>_SIGNING_KEY_PATH``,
      ``<PREFIX>_SIGNING_KEY_PASSWORD``)
    * targets the real upstream URL (sandbox by default)
    * sends the actual request body the operation builds
    * signs the request with a fresh nonce/timestamp/body-hash each run

So a developer can copy the snippet into a file, ``pip install`` the
two deps, set the env vars Solution Studio already documents, and run
it as-is.

Open Finance APIs use Bearer tokens rather than OAuth1 — they get a
family-specific snippet that walks through the partner-token exchange.
"""
from __future__ import annotations

import json
import os
from contextlib import contextmanager
from typing import Any, Dict, Iterator, Optional, Tuple


# ----------------------------------------------------------------------------
# Request interception
# ----------------------------------------------------------------------------

class _FakeResponse:
    """Minimal ``requests.Response`` stand-in so ``execute()`` doesn't
    crash before we've extracted the interesting data."""
    status_code = 200
    text = "{}"
    headers: Dict[str, str] = {}

    def json(self) -> Dict[str, Any]:
        return {}

    def raise_for_status(self) -> None:  # pragma: no cover — defensive
        return None


@contextmanager
def _stub_oauth() -> Iterator[None]:
    """Stub out OAuth1 signing while we're capturing.

    Modules call ``authutils.load_signing_key(path, password)`` followed
    by ``OAuth.get_authorization_header(...)`` *before* invoking
    ``requests.post(...)``. With no real key on disk the first call
    raises and the module returns an error tuple, so we never reach the
    HTTP layer. We swap both functions for harmless stubs while the
    context is active.
    """
    try:
        import oauth1.authenticationutils as _au
        from oauth1.oauth import OAuth as _OAuth
    except Exception:
        yield
        return

    orig_load = _au.load_signing_key
    orig_sign = _OAuth.get_authorization_header
    _au.load_signing_key = lambda path, password=None: object()  # type: ignore[assignment]
    _OAuth.get_authorization_header = staticmethod(  # type: ignore[assignment]
        lambda url, method, body, consumer_key, signing_key: (
            'OAuth oauth_consumer_key="...",oauth_signature_method="RSA-SHA256",'
            'oauth_timestamp="...",oauth_nonce="...",oauth_body_hash="...",'
            'oauth_version="1.0",oauth_signature="..."'
        )
    )
    try:
        yield
    finally:
        _au.load_signing_key = orig_load
        _OAuth.get_authorization_header = orig_sign


@contextmanager
def _capture_requests() -> Iterator[Dict[str, Any]]:
    """Replace ``requests.{get,post,put,patch,delete,request}`` with a
    capturer that records the first call and returns ``_FakeResponse``.

    Yields a dict mutated in-place with the captured call. Restores the
    original functions when the context exits.
    """
    import requests as _r

    captured: Dict[str, Any] = {}

    def _record(method: str, url: str, **kwargs: Any) -> _FakeResponse:
        if not captured:
            captured.update(
                method=str(method).upper(),
                url=str(url),
                headers=dict(kwargs.get("headers") or {}),
                data=kwargs.get("data"),
                json=kwargs.get("json"),
                params=kwargs.get("params"),
            )
        return _FakeResponse()

    def _request(method: str, url: str, **kwargs: Any) -> _FakeResponse:
        return _record(method, url, **kwargs)

    def _get(url: str, **kwargs: Any) -> _FakeResponse:
        return _record("GET", url, **kwargs)

    def _post(url: str, **kwargs: Any) -> _FakeResponse:
        return _record("POST", url, **kwargs)

    def _put(url: str, **kwargs: Any) -> _FakeResponse:
        return _record("PUT", url, **kwargs)

    def _patch(url: str, **kwargs: Any) -> _FakeResponse:
        return _record("PATCH", url, **kwargs)

    def _delete(url: str, **kwargs: Any) -> _FakeResponse:
        return _record("DELETE", url, **kwargs)

    originals = {
        "request": _r.request,
        "get": _r.get,
        "post": _r.post,
        "put": _r.put,
        "patch": _r.patch,
        "delete": _r.delete,
    }
    _r.request, _r.get, _r.post, _r.put, _r.patch, _r.delete = (
        _request, _get, _post, _put, _patch, _delete,
    )
    try:
        yield captured
    finally:
        _r.request = originals["request"]
        _r.get = originals["get"]
        _r.post = originals["post"]
        _r.put = originals["put"]
        _r.patch = originals["patch"]
        _r.delete = originals["delete"]


# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------

def _sample_params(op: Dict[str, Any], mod: Any = None) -> Dict[str, Any]:
    """Build a sample params dict from operation defaults.

    Mirrors the UI's behaviour: optional params left blank are omitted
    so the module's ``if value:`` guards skip them, rather than passing
    placeholder text that turns into a real (and bogus) filter value.

    When the module exposes ``get_state()`` and a param name matches a
    state key (e.g. ``customer_id``, ``account_id``, ``consumer_id``),
    the live value is used instead of a ``<your ...>`` placeholder so
    the rendered snippet has a real, runnable URL when possible.
    """
    state: Dict[str, Any] = {}
    if mod is not None:
        try:
            state = dict(getattr(mod, "get_state", lambda: {})() or {})
        except Exception:
            state = {}
    out: Dict[str, Any] = {}
    for p in op.get("params") or []:
        name = p["name"]
        default = p.get("default")
        required = bool(p.get("required"))
        if default not in (None, ""):
            out[name] = default
        elif p.get("options"):
            out[name] = p["options"][0].get("value")
        elif state.get(name) not in (None, ""):
            # Prefer a live state value (e.g. customer_id) so the
            # captured URL works as-is when the user runs the snippet.
            out[name] = state[name]
        elif not required:
            # Optional + no default → leave blank, just like the UI.
            out[name] = ""
        elif p.get("type") == "number":
            out[name] = 0
        elif p.get("type") == "boolean":
            out[name] = False
        else:
            out[name] = f"<your {name}>"
    return out


def _split_base_and_path(url: str, mod: Any) -> Tuple[str, str]:
    """Split a captured absolute URL into (BASE_URL, path+query)."""
    for attr in ("_SANDBOX_BASE_URL", "_PROD_BASE_URL"):
        base = getattr(mod, attr, None)
        if isinstance(base, str) and base and url.startswith(base):
            return base, url[len(base):]
    # Fall back: split at the third '/' (after https://host/).
    try:
        scheme, rest = url.split("://", 1)
        host, _, path = rest.partition("/")
        return f"{scheme}://{host}", f"/{path}"
    except ValueError:
        return "", url


def _py_repr(value: Any, indent: int = 4) -> str:
    return (
        json.dumps(value, indent=indent)
        .replace(": true", ": True")
        .replace(": false", ": False")
        .replace(": null", ": None")
    )


def _ensure_env_set(env_prefix: str) -> Dict[str, str]:
    """Stub env vars the module reads, so its config branch doesn't
    short-circuit before reaching the HTTP layer. Returns a dict mapping
    each env var name to its prior value (``""`` if it was unset) so we
    can restore afterwards.
    """
    saved: Dict[str, str] = {}
    placeholders = {
        f"{env_prefix}_CONSUMER_KEY": "snippet-dry-run",
        f"{env_prefix}_SIGNING_KEY_PATH": "/tmp/snippet-dry-run.p12",
    }
    # Open Finance / Finicity uses OAuth2-style partner credentials
    # instead of OAuth1, so stub those too when relevant.
    if env_prefix.startswith("OPEN_FINANCE"):
        placeholders.update({
            f"{env_prefix}_PARTNER_ID":     "snippet-dry-run-partner",
            f"{env_prefix}_PARTNER_SECRET": "snippet-dry-run-secret",
            f"{env_prefix}_APP_KEY":        "snippet-dry-run-appkey",
        })
    for name, val in placeholders.items():
        if name not in os.environ:
            saved[name] = ""  # marker: was unset
            os.environ[name] = val
    return saved


def _restore_env(saved: Dict[str, str]) -> None:
    for name, val in saved.items():
        if val == "":
            os.environ.pop(name, None)
        else:
            os.environ[name] = val


# ----------------------------------------------------------------------------
# Capture
# ----------------------------------------------------------------------------

def _capture_call(
    mod: Any,
    op_id: str,
    op: Dict[str, Any],
    env_prefix: str,
) -> Optional[Dict[str, Any]]:
    """Run ``mod.execute(op_id, sample_params)`` inside a request capturer.

    Returns the captured call dict, or ``None`` if nothing was captured
    (e.g. the module short-circuited before reaching the HTTP layer).
    """
    # Force the sandbox env switch where the module honours it, and
    # disable the simulator so we hit the real URL-build path.
    env_switch = f"{env_prefix}_ENV"
    saved_env_switch = os.environ.get(env_switch)
    os.environ[env_switch] = "sandbox"
    saved_sim = os.environ.get("VIMA_SIMULATE")
    os.environ["VIMA_SIMULATE"] = "off"

    saved_creds = _ensure_env_set(env_prefix)
    sample = _sample_params(op, mod)

    # For Open Finance we also need to (a) reset the module's cached
    # client so it picks up the placeholder credentials we just stubbed,
    # and (b) bypass the real partner-authentication call so the op's
    # actual HTTP request is what gets captured (not the auth fetch).
    of_client_cls = None
    saved_get_token = None
    saved_cached_client = None
    if env_prefix.startswith("OPEN_FINANCE"):
        try:
            from apis.open_finance.client import OpenFinanceClient as of_client_cls  # type: ignore
        except Exception:
            of_client_cls = None
        if of_client_cls is not None:
            saved_get_token = of_client_cls._get_token
            of_client_cls._get_token = lambda self: "snippet-dry-run-token"
        if hasattr(mod, "_client"):
            saved_cached_client = getattr(mod, "_client")
            mod._client = None

    try:
        with _stub_oauth(), _capture_requests() as captured:
            try:
                mod.execute(op_id, sample)
            except Exception:
                # The module may raise after we return a FakeResponse —
                # that's fine; we already have what we need.
                pass
        return dict(captured) if captured else None
    finally:
        _restore_env(saved_creds)
        if saved_env_switch is None:
            os.environ.pop(env_switch, None)
        else:
            os.environ[env_switch] = saved_env_switch
        if saved_sim is None:
            os.environ.pop("VIMA_SIMULATE", None)
        else:
            os.environ["VIMA_SIMULATE"] = saved_sim
        if of_client_cls is not None and saved_get_token is not None:
            of_client_cls._get_token = saved_get_token
        if hasattr(mod, "_client") and saved_cached_client is not None:
            mod._client = saved_cached_client


# ----------------------------------------------------------------------------
# Snippet rendering
# ----------------------------------------------------------------------------

def _render_body_block(captured: Dict[str, Any]) -> Tuple[str, str]:
    """Return (request_body_section, requests_kwargs_fragment)."""
    if captured.get("json") is not None:
        body_repr = _py_repr(captured["json"], indent=4)
        return (
            "payload = " + body_repr + "\n"
            "body = json.dumps(payload)\n",
            "data=body",
        )
    if isinstance(captured.get("data"), (bytes, bytearray)):
        try:
            parsed = json.loads(bytes(captured["data"]).decode("utf-8"))
            body_repr = _py_repr(parsed, indent=4)
            return (
                "payload = " + body_repr + "\n"
                "body = json.dumps(payload)\n",
                "data=body",
            )
        except Exception:
            data_str = bytes(captured["data"]).decode("utf-8", errors="replace")
            return (f"body = {json.dumps(data_str)}\n", "data=body")
    if isinstance(captured.get("data"), str):
        s = captured["data"]
        try:
            parsed = json.loads(s)
            body_repr = _py_repr(parsed, indent=4)
            return (
                "payload = " + body_repr + "\n"
                "body = json.dumps(payload)\n",
                "data=body",
            )
        except (ValueError, TypeError):
            return (f"body = {json.dumps(s)}\n", "data=body")
    if captured.get("params"):
        params_repr = _py_repr(captured["params"], indent=4)
        return (
            "# This operation passes its inputs as query parameters.\n"
            "params = " + params_repr + "\n"
            "body = None\n",
            "params=params",
        )
    return ("body = None\n", "")


def _oauth1_snippet_runnable(
    api_id: str,
    op: Dict[str, Any],
    env_prefix: str,
    captured: Dict[str, Any],
    docs_url: str,
    mod: Any,
) -> str:
    """Wrap a captured request in a fully runnable OAuth1-signed template."""
    method = captured.get("method") or (op.get("method") or "POST").upper()
    url = captured.get("url") or ""
    base, path = _split_base_and_path(url, mod)
    placeholders = _extract_placeholders(path)
    todo_block = ""
    path_literal: str
    if placeholders:
        for name in placeholders:
            path = path.replace(f"<your {name}>", "{" + name.upper() + "}")
        const_lines = "\n".join(
            f'{name.upper()} = "<your {name}>"  # TODO: replace with a real {name}'
            for name in placeholders
        )
        todo_block = (
            "# --- TODO: fill in the inputs this operation needs --------\n"
            f"{const_lines}\n\n"
        )
        path_literal = f"f{json.dumps(path)}"
    else:
        path_literal = json.dumps(path)
    body_section, requests_kwarg = _render_body_block(captured)
    op_name = op.get("name") or op.get("id") or "operation"
    op_id_str = op.get("id", "call")

    return (
        f'"""\n'
        f'{api_id} — {op_name}\n'
        f'\n'
        f'Runnable Python that calls the Mastercard {api_id} API\n'
        f'directly with OAuth1 request signing — captured from the\n'
        f'actual Solution Studio implementation, so URL, body and\n'
        f'headers match exactly.\n'
        f'\n'
        f'Docs: {docs_url}\n'
        f'\n'
        f'Install:\n'
        f'    pip install requests mastercard-oauth1-signer\n'
        f'\n'
        f'Run:\n'
        f'    export {env_prefix}_CONSUMER_KEY="..."\n'
        f'    export {env_prefix}_SIGNING_KEY_PATH="/path/to/sandbox.p12"\n'
        f'    export {env_prefix}_SIGNING_KEY_PASSWORD="keystorepassword"\n'
        f'    python {api_id}_{op_id_str}.py\n'
        f'"""\n'
        f"import json\n"
        f"import os\n"
        f"\n"
        f"import requests\n"
        f"import oauth1.authenticationutils as authutils\n"
        f"from oauth1.oauth import OAuth\n"
        f"\n"
        f"# --- Credentials (same env vars Solution Studio reads) ----\n"
        f'consumer_key = os.environ["{env_prefix}_CONSUMER_KEY"]\n'
        f'key_path     = os.environ["{env_prefix}_SIGNING_KEY_PATH"]\n'
        f'key_password = os.environ.get("{env_prefix}_SIGNING_KEY_PASSWORD", "keystorepassword")\n'
        f"signing_key  = authutils.load_signing_key(key_path, key_password)\n"
        f"\n"
        f"# --- Endpoint (sandbox) ---\n"
        f"{todo_block}"
        f"BASE_URL = {json.dumps(base)}\n"
        f"PATH     = {path_literal}\n"
        f'METHOD   = "{method}"\n'
        f'url      = f"{{BASE_URL}}{{PATH}}"\n'
        f"\n"
        f"# --- Request ---\n"
        f"{body_section}"
        f"\n"
        f"# --- OAuth1 signing ---\n"
        f"# Binds consumer key + timestamp + nonce + SHA-256 body hash\n"
        f"# into the Authorization header.\n"
        f"auth_header = OAuth.get_authorization_header(url, METHOD, body, consumer_key, signing_key)\n"
        f"headers = {{\n"
        f'    "Authorization": auth_header,\n'
        f'    "Accept": "application/json",\n'
        f'    "Content-Type": "application/json",\n'
        f"}}\n"
        f"\n"
        f"resp = requests.request(METHOD, url, {(requests_kwarg + ', ') if requests_kwarg else ''}headers=headers, timeout=30)\n"
        f"\n"
        f"# --- Show what we sent and what we got back ---\n"
        f'print("=" * 72)\n'
        f'print(f"REQUEST  {{METHOD}} {{url}}")\n'
        f'print("-" * 72)\n'
        f'print("Headers:")\n'
        f"for k, v in headers.items():\n"
        f"    # Truncate the signed Authorization header so it's still readable.\n"
        f'    shown = (v[:80] + "\\u2026") if k == "Authorization" and len(v) > 80 else v\n'
        f'    print(f"  {{k}}: {{shown}}")\n'
        f"if body:\n"
        f'    print("Body:")\n'
        f"    print(body if len(body) < 2000 else body[:2000] + '\\u2026')\n"
        f'print("=" * 72)\n'
        f'print(f"RESPONSE {{resp.status_code}} {{resp.reason}}")\n'
        f'print("-" * 72)\n'
        f"try:\n"
        f"    print(json.dumps(resp.json(), indent=2))\n"
        f"except ValueError:\n"
        f"    print(resp.text)\n"
        f'print("=" * 72)\n'
        f"resp.raise_for_status()\n"
    )


def _extract_placeholders(s: str) -> list:
    """Return ordered, de-duplicated ``<your foo>`` placeholders in ``s``."""
    import re as _re
    seen: list = []
    for m in _re.finditer(r"<your ([a-zA-Z_][a-zA-Z0-9_]*)>", s):
        name = m.group(1)
        if name not in seen:
            seen.append(name)
    return seen


def _open_finance_snippet(api_id: str, op: Dict[str, Any], docs_url: str) -> str:
    """Fallback static template — used only when capture fails.
    Shows the partner-authentication token-exchange step.
    """
    op_name = op.get("name") or op.get("id") or "operation"
    return (
        f'"""\n'
        f'{api_id} — {op_name}\n'
        f'\n'
        f'Open Finance (Finicity) uses partner-scoped App + Customer\n'
        f'Bearer tokens rather than OAuth1 signing. This snippet shows\n'
        f'the token-exchange step — see the docs for the per-endpoint\n'
        f'paths and Customer-scoped flows:\n'
        f'\n'
        f'    {docs_url}\n'
        f'\n'
        f'Install:\n'
        f'    pip install requests\n'
        f'\n'
        f'Run:\n'
        f'    export OPEN_FINANCE_PARTNER_ID="..."\n'
        f'    export OPEN_FINANCE_PARTNER_SECRET="..."\n'
        f'    export OPEN_FINANCE_APP_KEY="..."\n'
        f'    python {api_id}_token.py\n'
        f'"""\n'
        f"import os\n"
        f"import requests\n"
        f"\n"
        f"# 1. Exchange partner credentials for a 2-hour App token.\n"
        f"app_resp = requests.post(\n"
        f'    "https://api.finicity.com/aggregation/v2/partners/authentication",\n'
        f"    headers={{\n"
        f'        "Finicity-App-Key": os.environ["OPEN_FINANCE_APP_KEY"],\n'
        f'        "Content-Type": "application/json",\n'
        f'        "Accept": "application/json",\n'
        f"    }},\n"
        f"    json={{\n"
        f'        "partnerId":     os.environ["OPEN_FINANCE_PARTNER_ID"],\n'
        f'        "partnerSecret": os.environ["OPEN_FINANCE_PARTNER_SECRET"],\n'
        f"    }},\n"
        f"    timeout=30,\n"
        f")\n"
        f"app_resp.raise_for_status()\n"
        f'app_token = app_resp.json()["token"]\n'
        f'print("App token acquired:", app_token[:12] + "\u2026")\n'
        f"\n"
        f"# 2. Use the App token in subsequent requests via the\n"
        f"#    'Finicity-App-Token' header alongside 'Finicity-App-Key'.\n"
        f"#    See docs for per-endpoint paths and Customer flows.\n"
    )


def _open_finance_snippet_runnable(
    api_id: str,
    op: Dict[str, Any],
    captured: Dict[str, Any],
    docs_url: str,
) -> str:
    """Render a runnable Finicity Bearer-token snippet around a captured call.

    Same idea as ``_oauth1_snippet_runnable`` but for Finicity's
    Partner-ID/Partner-Secret/App-Key authentication: fetch an App
    token, then invoke the operation's endpoint with the captured
    URL/method/body/params.
    """
    method = (captured.get("method") or op.get("method") or "GET").upper()
    url = captured.get("url") or ""
    try:
        scheme, rest = url.split("://", 1)
        host, _, path = rest.partition("/")
        base = f"{scheme}://{host}"
        path = f"/{path}"
    except ValueError:
        base, path = "https://api.finicity.com", url
    # Lift any `<your foo>` placeholders out of the captured path into
    # TODO constants so the user sees them clearly at the top of the
    # script rather than being baked into a URL that 404s.
    placeholders = _extract_placeholders(path)
    todo_block = ""
    path_literal: str
    if placeholders:
        for name in placeholders:
            path = path.replace(f"<your {name}>", "{" + name.upper() + "}")
        const_lines = "\n".join(
            f'{name.upper()} = "<your {name}>"  # TODO: replace with a real {name}'
            for name in placeholders
        )
        todo_block = (
            "# --- TODO: fill in the inputs this operation needs --------\n"
            f"{const_lines}\n\n"
        )
        path_literal = f"f{json.dumps(path)}"
    else:
        path_literal = json.dumps(path)
    body_section, requests_kwarg = _render_body_block(captured)
    op_name = op.get("name") or op.get("id") or "operation"
    op_id_str = op.get("id", "call")

    return (
        f'"""\n'
        f'{api_id} — {op_name}\n'
        f'\n'
        f'Runnable Python that calls the Mastercard Open Banking\n'
        f'(Finicity) {api_id} API directly with App-Token auth — captured\n'
        f'from the actual Solution Studio implementation, so URL, body\n'
        f'and headers match exactly.\n'
        f'\n'
        f'Docs: {docs_url}\n'
        f'\n'
        f'Install:\n'
        f'    pip install requests\n'
        f'\n'
        f'Run:\n'
        f'    export OPEN_FINANCE_PARTNER_ID="..."\n'
        f'    export OPEN_FINANCE_PARTNER_SECRET="..."\n'
        f'    export OPEN_FINANCE_APP_KEY="..."\n'
        f'    python {api_id}_{op_id_str}.py\n'
        f'"""\n'
        f"import json\n"
        f"import os\n"
        f"\n"
        f"import requests\n"
        f"\n"
        f"# --- Credentials (same env vars Solution Studio reads) ----\n"
        f'PARTNER_ID     = os.environ["OPEN_FINANCE_PARTNER_ID"]\n'
        f'PARTNER_SECRET = os.environ["OPEN_FINANCE_PARTNER_SECRET"]\n'
        f'APP_KEY        = os.environ["OPEN_FINANCE_APP_KEY"]\n'
        f'BASE_URL       = os.environ.get("OPEN_FINANCE_API_BASE_URL", {json.dumps(base)})\n'
        f"\n"
        f"# --- 1. Exchange partner credentials for a 2-hour App token ---\n"
        f"auth_resp = requests.post(\n"
        f'    f"{{BASE_URL}}/aggregation/v2/partners/authentication",\n'
        f"    headers={{\n"
        f'        "Finicity-App-Key": APP_KEY,\n'
        f'        "Content-Type":     "application/json",\n'
        f'        "Accept":           "application/json",\n'
        f"    }},\n"
        f'    json={{"partnerId": PARTNER_ID, "partnerSecret": PARTNER_SECRET}},\n'
        f"    timeout=30,\n"
        f")\n"
        f"auth_resp.raise_for_status()\n"
        f'APP_TOKEN = auth_resp.json()["token"]\n'
        f'print("App token acquired:", APP_TOKEN[:10] + "\u2026")\n'
        f"\n"
        f"# --- 2. Call the operation endpoint ---\n"
        f"{todo_block}"
        f"PATH    = {path_literal}\n"
        f'METHOD  = "{method}"\n'
        f'url     = f"{{BASE_URL}}{{PATH}}"\n'
        f"headers = {{\n"
        f'    "Finicity-App-Key":   APP_KEY,\n'
        f'    "Finicity-App-Token": APP_TOKEN,\n'
        f'    "Content-Type":       "application/json",\n'
        f'    "Accept":             "application/json",\n'
        f"}}\n"
        f"\n"
        f"# --- Request ---\n"
        f"{body_section}"
        f"\n"
        f"resp = requests.request(METHOD, url, {(requests_kwarg + ', ') if requests_kwarg else ''}headers=headers, timeout=30)\n"
        f"\n"
        f"# --- Show what we sent and what we got back ---\n"
        f'print("=" * 72)\n'
        f'print(f"REQUEST  {{METHOD}} {{url}}")\n'
        f'print("-" * 72)\n'
        f'print("Headers:")\n'
        f"for k, v in headers.items():\n"
        f'    shown = (v[:80] + "\\u2026") if k.endswith("-Token") and len(v) > 80 else v\n'
        f'    print(f"  {{k}}: {{shown}}")\n'
        f"if body:\n"
        f'    print("Body:")\n'
        f"    print(body if len(body) < 2000 else body[:2000] + '\\u2026')\n"
        f'print("=" * 72)\n'
        f'print(f"RESPONSE {{resp.status_code}} {{resp.reason}}")\n'
        f'print("-" * 72)\n'
        f"try:\n"
        f"    print(json.dumps(resp.json(), indent=2))\n"
        f"except ValueError:\n"
        f"    print(resp.text)\n"
        f'print("=" * 72)\n'
        f"resp.raise_for_status()\n"
    )


def build_snippet(
    api_id: str,
    op_id: str,
    *,
    mod: Any,
    manifest: Dict[str, Any],
) -> Dict[str, Any]:
    """Return ``{snippet, summary, language, runnable, docs_url}`` for the
    given (api_id, op_id) pair.

    ``runnable`` is True when we captured a real outbound HTTP call from
    the module and could build a self-contained signing template around
    it; False when we had to fall back to a docs-pointer stub.
    """
    ops = manifest.get("operations") or []
    op = next((o for o in ops if o.get("id") == op_id), ops[0] if ops else {})
    docs_url = manifest.get("docs_url") or "https://developer.mastercard.com"
    env_prefix = manifest.get("env_prefix") or api_id.upper()

    runnable = False
    if api_id.startswith("open_finance"):
        # For create_token the module never calls _make_request — it just
        # invokes the internal _get_token() helper — so capture would be
        # empty. Fall back to the static token-exchange template, which
        # *is* exactly what create_token would do at the HTTP layer.
        if op_id == "create_token":
            snippet = _open_finance_snippet(api_id, op, docs_url)
            runnable = True
        else:
            captured = _capture_call(mod, op_id, op, env_prefix)
            if captured and captured.get("url"):
                snippet = _open_finance_snippet_runnable(api_id, op, captured, docs_url)
                runnable = True
            else:
                snippet = _open_finance_snippet(api_id, op, docs_url)
    else:
        captured = _capture_call(mod, op_id, op, env_prefix)
        if captured and captured.get("url"):
            snippet = _oauth1_snippet_runnable(api_id, op, env_prefix, captured, docs_url, mod)
            runnable = True
        else:
            snippet = (
                f'"""\n'
                f'{api_id} — {op.get("name") or op.get("id") or "operation"}\n'
                f'\n'
                f'No outbound HTTP call was captured for this operation.\n'
                f'The module may short-circuit before hitting the wire\n'
                f'(e.g. config validation). See the docs for the call:\n'
                f'\n'
                f'    {docs_url}\n'
                f'"""\n'
            )

    summary = f"{op.get('method', 'POST')} \u00b7 {op.get('name') or op.get('id') or 'operation'}"
    return {
        "api_id": api_id,
        "operation_id": op.get("id") or op_id,
        "summary": summary,
        "language": "python",
        "snippet": snippet,
        "runnable": runnable,
        "docs_url": docs_url,
    }
