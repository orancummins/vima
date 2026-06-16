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
from collections.abc import Iterator
from contextlib import contextmanager
from typing import Any

# ----------------------------------------------------------------------------
# Open Finance variant config
# ----------------------------------------------------------------------------
# The three Open Finance APIs share a "Bearer token + per-vendor headers"
# shape but differ in env-var names, auth URL, header names and (for EU)
# the entire auth flow. Centralised here so snippet rendering, env-var
# stubbing during capture, and the /explorer/<api>/setup + /run endpoints
# in app.py all stay in sync.

_OF_VARIANTS: dict[str, dict[str, Any]] = {
    "OPEN_FINANCE": {
        "kind":         "finicity",
        "default_base": "https://api.finicity.com",
        "auth_path":    "/aggregation/v2/partners/authentication",
        "key_header":   "Finicity-App-Key",
        "token_header": "Finicity-App-Token",
        "env_vars":     ("PARTNER_ID", "PARTNER_SECRET", "APP_KEY"),
        "packages":     ("requests",),
        "label":        "Mastercard Open Banking (Finicity, US)",
    },
    "OPEN_FINANCE_AU": {
        "kind":         "finicity",
        "default_base": "https://api.openbanking.mastercard.com.au",
        "auth_path":    "/aggregation/v2/partners/authentication",
        "key_header":   "App-Key",
        "token_header": "App-Token",
        "env_vars":     ("PARTNER_ID", "PARTNER_SECRET", "APP_KEY"),
        "packages":     ("requests",),
        "label":        "Mastercard Open Finance Australia",
    },
    "OPEN_FINANCE_EU": {
        "kind":              "jwt_oauth2",
        "default_auth_base": "https://mtf.auth.openbanking.mastercard.eu",
        "default_api_base":  "https://mtf.api.openbanking.mastercard.eu",
        "jwt_audience":      "auth.mastercard.com",
        "env_vars":          ("CLIENT_ID", "PRIVATE_KEY_PATH", "PUBLIC_CERT_PATH"),
        "packages":          ("requests", "cryptography"),
        "label":             "Mastercard Open Finance Europe (Aiia)",
    },
}


def _of_variant(env_prefix: str) -> dict[str, Any] | None:
    return _OF_VARIANTS.get(env_prefix)


def of_runtime_for_prefix(env_prefix: str) -> dict[str, Any] | None:
    """Public helper used by ``/explorer/<api>/setup`` and ``/run`` in
    ``app.py`` so they advertise / export the right env vars and pip
    packages for each Open Finance variant.

    Returns ``None`` for non-Open-Finance APIs (caller should fall back
    to the standard OAuth1 credential triple).
    """
    v = _of_variant(env_prefix)
    if not v:
        return None
    return {
        "env_var_names": [f"{env_prefix}_{n}" for n in v["env_vars"]],
        "packages":      list(v["packages"]),
    }


# ----------------------------------------------------------------------------
# Request interception
# ----------------------------------------------------------------------------

class _FakeResponse:
    """Minimal ``requests.Response`` stand-in so ``execute()`` doesn't
    crash before we've extracted the interesting data."""
    status_code = 200
    text = "{}"
    headers: dict[str, str] = {}

    def json(self) -> dict[str, Any]:
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
def _capture_requests() -> Iterator[dict[str, Any]]:
    """Replace ``requests.{get,post,put,patch,delete,request}`` with a
    capturer that records the first call and returns ``_FakeResponse``.

    Yields a dict mutated in-place with the captured call. Restores the
    original functions when the context exits.
    """
    import requests as _r

    captured: dict[str, Any] = {}

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

def _sample_params(op: dict[str, Any], mod: Any = None) -> dict[str, Any]:
    """Build a sample params dict from operation defaults.

    Mirrors the UI's behaviour: optional params left blank are omitted
    so the module's ``if value:`` guards skip them, rather than passing
    placeholder text that turns into a real (and bogus) filter value.

    When the module exposes ``get_state()`` and a param name matches a
    state key (e.g. ``customer_id``, ``account_id``, ``consumer_id``),
    the live value is used instead of a ``<your ...>`` placeholder so
    the rendered snippet has a real, runnable URL when possible.
    """
    state: dict[str, Any] = {}
    if mod is not None:
        try:
            state = dict(getattr(mod, "get_state", lambda: {})() or {})
        except Exception:
            state = {}
    out: dict[str, Any] = {}
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


def _split_base_and_path(url: str, mod: Any) -> tuple[str, str]:
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


def _ensure_env_set(env_prefix: str) -> dict[str, str]:
    """Stub env vars the module reads, so its config branch doesn't
    short-circuit before reaching the HTTP layer. Returns a dict mapping
    each env var name to its prior value (``""`` if it was unset) so we
    can restore afterwards.
    """
    saved: dict[str, str] = {}
    placeholders = {
        f"{env_prefix}_CONSUMER_KEY": "snippet-dry-run",
        f"{env_prefix}_SIGNING_KEY_PATH": "/tmp/snippet-dry-run.p12",  # nosec B108 — placeholder path, never created
    }
    # Open Finance variants use vendor-specific credentials rather than
    # OAuth1, so stub those too when relevant.
    variant = _of_variant(env_prefix)
    if variant:
        if variant["kind"] == "finicity":
            # US (Finicity) and AU (Mastercard Open Banking AU) both use
            # Partner ID / Partner Secret / App Key.
            placeholders.update({
                f"{env_prefix}_PARTNER_ID":     "snippet-dry-run-partner",
                f"{env_prefix}_PARTNER_SECRET": "snippet-dry-run-secret",
                f"{env_prefix}_APP_KEY":        "snippet-dry-run-appkey",
            })
        elif variant["kind"] == "jwt_oauth2":
            # EU (Aiia) uses an OAuth2 client_credentials grant with a
            # JWT client assertion. The key/cert files don't have to
            # exist because _capture_call short-circuits _get_token
            # before _load_private_key()/_compute_kid() ever runs.
            placeholders.update({
                f"{env_prefix}_CLIENT_ID":        "snippet-dry-run-client",
                f"{env_prefix}_PRIVATE_KEY_PATH": "/tmp/snippet-dry-run-key.pem",  # nosec B108 — placeholder path, never created
                f"{env_prefix}_PUBLIC_CERT_PATH": "/tmp/snippet-dry-run-cert.pem",  # nosec B108 — placeholder path, never created
            })
    for name, val in placeholders.items():
        if name not in os.environ:
            saved[name] = ""  # marker: was unset
            os.environ[name] = val
    return saved


def _restore_env(saved: dict[str, str]) -> None:
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
    op: dict[str, Any],
    env_prefix: str,
) -> dict[str, Any] | None:
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
    # and (b) bypass the real auth call so the op's actual HTTP request
    # is what gets captured (not the token-exchange fetch). We patch
    # _get_token on every available OF client class because we don't
    # know up front which one ``mod`` will instantiate.
    of_client_restore: list[tuple[Any, Any]] = []
    saved_cached_client = None
    if env_prefix.startswith("OPEN_FINANCE"):
        for _mod_path, _cls_name in (
            ("apis.open_finance.client",    "OpenFinanceClient"),
            ("apis.open_finance_au.client", "OpenFinanceAUClient"),
            ("apis.open_finance_eu.client", "OpenFinanceEUClient"),
        ):
            try:
                _m = __import__(_mod_path, fromlist=[_cls_name])
                _cls = getattr(_m, _cls_name, None)
            except Exception:
                _cls = None
            if _cls is not None and hasattr(_cls, "_get_token"):
                _orig = _cls._get_token
                _cls._get_token = lambda self, *a, **_kw: "snippet-dry-run-token"
                of_client_restore.append((_cls, _orig))
        if hasattr(mod, "_client"):
            saved_cached_client = mod._client
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
        for _cls, _orig in of_client_restore:
            _cls._get_token = _orig
        if hasattr(mod, "_client") and saved_cached_client is not None:
            mod._client = saved_cached_client


# ----------------------------------------------------------------------------
# Snippet rendering
# ----------------------------------------------------------------------------

def _render_body_block(captured: dict[str, Any]) -> tuple[str, str]:
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
    op: dict[str, Any],
    env_prefix: str,
    captured: dict[str, Any],
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


def _open_finance_snippet(api_id: str, op: dict[str, Any], env_prefix: str, docs_url: str) -> str:
    """Fallback / `create_token` template. Dispatches by variant kind."""
    variant = _of_variant(env_prefix) or _OF_VARIANTS["OPEN_FINANCE"]
    if variant["kind"] == "jwt_oauth2":
        return _eu_create_token_snippet(api_id, op, env_prefix, docs_url, variant)
    return _finicity_create_token_snippet(api_id, op, env_prefix, docs_url, variant)


def _open_finance_snippet_runnable(
    api_id: str,
    op: dict[str, Any],
    env_prefix: str,
    captured: dict[str, Any],
    docs_url: str,
) -> str:
    """Render a runnable snippet around a captured call. Dispatches by variant."""
    variant = _of_variant(env_prefix) or _OF_VARIANTS["OPEN_FINANCE"]
    if variant["kind"] == "jwt_oauth2":
        return _eu_snippet_runnable(api_id, op, env_prefix, captured, docs_url, variant)
    return _finicity_snippet_runnable(api_id, op, env_prefix, captured, docs_url, variant)


# ----------------------------------------------------------------------------
# Finicity-flavoured renderers (US + AU)
# ----------------------------------------------------------------------------

def _finicity_create_token_snippet(
    api_id: str,
    op: dict[str, Any],
    env_prefix: str,
    docs_url: str,
    variant: dict[str, Any],
) -> str:
    """Static `create_token` template for US (Finicity) + AU."""
    op_name = op.get("name") or op.get("id") or "operation"
    base = variant["default_base"]
    auth_path = variant["auth_path"]
    key_hdr = variant["key_header"]
    label = variant.get("label", "Mastercard Open Banking")
    return (
        f'"""\n'
        f'{api_id} — {op_name}\n'
        f'\n'
        f'{label} uses partner-scoped App + Customer Bearer tokens rather\n'
        f'than OAuth1 signing. This snippet performs the token-exchange\n'
        f'step — see the docs for per-endpoint paths and Customer-scoped\n'
        f'flows:\n'
        f'\n'
        f'    {docs_url}\n'
        f'\n'
        f'Install:\n'
        f'    pip install requests\n'
        f'\n'
        f'Run:\n'
        f'    export {env_prefix}_PARTNER_ID="..."\n'
        f'    export {env_prefix}_PARTNER_SECRET="..."\n'
        f'    export {env_prefix}_APP_KEY="..."\n'
        f'    python {api_id}_token.py\n'
        f'"""\n'
        f"import os\n"
        f"import requests\n"
        f"\n"
        f'BASE_URL = os.environ.get("{env_prefix}_API_BASE_URL", {json.dumps(base)})\n'
        f"\n"
        f"# 1. Exchange partner credentials for a 2-hour App token.\n"
        f"app_resp = requests.post(\n"
        f'    f"{{BASE_URL}}{auth_path}",\n'
        f"    headers={{\n"
        f'        "{key_hdr}": os.environ["{env_prefix}_APP_KEY"],\n'
        f'        "Content-Type": "application/json",\n'
        f'        "Accept":       "application/json",\n'
        f"    }},\n"
        f"    json={{\n"
        f'        "partnerId":     os.environ["{env_prefix}_PARTNER_ID"],\n'
        f'        "partnerSecret": os.environ["{env_prefix}_PARTNER_SECRET"],\n'
        f"    }},\n"
        f"    timeout=30,\n"
        f")\n"
        f"app_resp.raise_for_status()\n"
        f'app_token = app_resp.json()["token"]\n'
        f'print("App token acquired:", app_token[:12] + "\u2026")\n'
        f"\n"
        f"# 2. Use the App token in subsequent requests via the\n"
        f"#    '{variant['token_header']}' header alongside '{key_hdr}'.\n"
        f"#    See docs for per-endpoint paths and Customer flows.\n"
    )


def _finicity_snippet_runnable(
    api_id: str,
    op: dict[str, Any],
    env_prefix: str,
    captured: dict[str, Any],
    docs_url: str,
    variant: dict[str, Any],
) -> str:
    """Render a runnable Bearer-token snippet around a captured call.

    Used by both US (Finicity) and AU (Mastercard Open Banking AU) —
    only the env-var prefix, base URL and header names differ.
    """
    method = (captured.get("method") or op.get("method") or "GET").upper()
    url = captured.get("url") or ""
    try:
        scheme, rest = url.split("://", 1)
        host, _, path = rest.partition("/")
        base = f"{scheme}://{host}"
        path = f"/{path}"
    except ValueError:
        base, path = variant["default_base"], url
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
    auth_path = variant["auth_path"]
    key_hdr = variant["key_header"]
    tok_hdr = variant["token_header"]
    label = variant.get("label", "Mastercard Open Banking")

    return (
        f'"""\n'
        f'{api_id} — {op_name}\n'
        f'\n'
        f'Runnable Python that calls the {label} {api_id} API directly\n'
        f'with App-Token auth — captured from the actual Solution Studio\n'
        f'implementation, so URL, body and headers match exactly.\n'
        f'\n'
        f'Docs: {docs_url}\n'
        f'\n'
        f'Install:\n'
        f'    pip install requests\n'
        f'\n'
        f'Run:\n'
        f'    export {env_prefix}_PARTNER_ID="..."\n'
        f'    export {env_prefix}_PARTNER_SECRET="..."\n'
        f'    export {env_prefix}_APP_KEY="..."\n'
        f'    python {api_id}_{op_id_str}.py\n'
        f'"""\n'
        f"import json\n"
        f"import os\n"
        f"\n"
        f"import requests\n"
        f"\n"
        f"# --- Credentials (same env vars Solution Studio reads) ----\n"
        f'PARTNER_ID     = os.environ["{env_prefix}_PARTNER_ID"]\n'
        f'PARTNER_SECRET = os.environ["{env_prefix}_PARTNER_SECRET"]\n'
        f'APP_KEY        = os.environ["{env_prefix}_APP_KEY"]\n'
        f'BASE_URL       = os.environ.get("{env_prefix}_API_BASE_URL", {json.dumps(base)})\n'
        f"\n"
        f"# --- 1. Exchange partner credentials for a 2-hour App token ---\n"
        f"auth_resp = requests.post(\n"
        f'    f"{{BASE_URL}}{auth_path}",\n'
        f"    headers={{\n"
        f'        "{key_hdr}":   APP_KEY,\n'
        f'        "Content-Type": "application/json",\n'
        f'        "Accept":       "application/json",\n'
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
        f'    "{key_hdr}":   APP_KEY,\n'
        f'    "{tok_hdr}":   APP_TOKEN,\n'
        f'    "Content-Type": "application/json",\n'
        f'    "Accept":       "application/json",\n'
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


# ----------------------------------------------------------------------------
# Open Finance EU renderer (RS256-signed JWT + OAuth2 client_credentials)
# ----------------------------------------------------------------------------

_EU_AUTH_BLOCK = '''\
# --- 1. Build a one-shot client-assertion JWT signed by the partner key ---
def _b64url(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode("ascii")

with open(PUBLIC_CERT_PATH, "rb") as _f:
    _cert_pem = _f.read()
load_pem_x509_certificate(_cert_pem)  # validates cert is well-formed
_cert_body = (
    _cert_pem.decode("ascii")
    .replace("-----BEGIN CERTIFICATE-----", "")
    .replace("-----END CERTIFICATE-----", "")
)
_der = base64.b64decode("".join(_cert_body.split()))
KID = _b64url(hashlib.sha256(_der).digest())

with open(PRIVATE_KEY_PATH, "rb") as _f:
    _priv = serialization.load_pem_private_key(_f.read(), password=None)
if not isinstance(_priv, rsa.RSAPrivateKey):
    raise SystemExit("Open Finance EU private key must be RSA")

_now = int(time.time())
_header = {"alg": "RS256", "typ": "JWT", "kid": KID}
_claims = {
    "sub": CLIENT_ID,
    "iss": CLIENT_ID,
    "aud": JWT_AUDIENCE,
    "exp": _now + 300,
    "iat": _now,
    "jti": str(uuid.uuid4()),
}
_h = _b64url(json.dumps(_header,  separators=(",", ":")).encode("utf-8"))
_p = _b64url(json.dumps(_claims, separators=(",", ":")).encode("utf-8"))
_signing_input = f"{_h}.{_p}".encode("ascii")
_signature = _priv.sign(_signing_input, padding.PKCS1v15(), hashes.SHA256())
ASSERTION = f"{_h}.{_p}.{_b64url(_signature)}"

# --- 2. Exchange the assertion for an access token ---
# NB: Mastercard's /oauth2/token expects a JSON body (not the standard
# OAuth 2.0 application/x-www-form-urlencoded). Form-encoded returns
#   FORMAT_ERROR — Content-Type ... does not match ... [application/json]
auth_resp = requests.post(
    f"{AUTH_BASE}/oauth2/token",
    headers={
        "Content-Type": "application/json",
        "Accept":       "application/json",
    },
    json={
        "grant_type":            "client_credentials",
        "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
        "client_assertion":      ASSERTION,
        "scope":                 SCOPES,
    },
    timeout=30,
)
auth_resp.raise_for_status()
ACCESS_TOKEN = auth_resp.json()["access_token"]
print("Access token acquired:", ACCESS_TOKEN[:12] + "\u2026")
'''


def _eu_create_token_snippet(
    api_id: str,
    op: dict[str, Any],
    env_prefix: str,
    docs_url: str,
    variant: dict[str, Any],
) -> str:
    """Static `create_token` template for EU (Aiia, RS256+OAuth2)."""
    op_name = op.get("name") or op.get("id") or "operation"
    auth_base = variant["default_auth_base"]
    aud = variant["jwt_audience"]
    label = variant.get("label", "Mastercard Open Finance Europe")
    return (
        f'"""\n'
        f'{api_id} — {op_name}\n'
        f'\n'
        f'{label} uses OAuth 2.0 client_credentials with a JWT client\n'
        f'assertion (RS256) instead of partner Bearer tokens.\n'
        f'\n'
        f'Docs: {docs_url}\n'
        f'\n'
        f'Install:\n'
        f'    pip install requests cryptography\n'
        f'\n'
        f'Run:\n'
        f'    export {env_prefix}_CLIENT_ID="..."\n'
        f'    export {env_prefix}_PRIVATE_KEY_PATH="/path/to/private.pem"\n'
        f'    export {env_prefix}_PUBLIC_CERT_PATH="/path/to/public.pem"\n'
        f'    python {api_id}_token.py\n'
        f'"""\n'
        f"import base64\n"
        f"import hashlib\n"
        f"import json\n"
        f"import os\n"
        f"import time\n"
        f"import uuid\n"
        f"\n"
        f"import requests\n"
        f"from cryptography.hazmat.primitives import hashes, serialization\n"
        f"from cryptography.hazmat.primitives.asymmetric import padding, rsa\n"
        f"from cryptography.x509 import load_pem_x509_certificate\n"
        f"\n"
        f"# --- Credentials (same env vars Solution Studio reads) ----\n"
        f'CLIENT_ID        = os.environ["{env_prefix}_CLIENT_ID"]\n'
        f'PRIVATE_KEY_PATH = os.environ["{env_prefix}_PRIVATE_KEY_PATH"]\n'
        f'PUBLIC_CERT_PATH = os.environ["{env_prefix}_PUBLIC_CERT_PATH"]\n'
        f'AUTH_BASE        = os.environ.get("{env_prefix}_AUTH_BASE_URL", {json.dumps(auth_base)})\n'
        f'JWT_AUDIENCE     = {json.dumps(aud)}\n'
        f'SCOPES           = "ob_data ob_providers"\n'
        f"\n"
        f"{_EU_AUTH_BLOCK}"
    )


def _eu_snippet_runnable(
    api_id: str,
    op: dict[str, Any],
    env_prefix: str,
    captured: dict[str, Any],
    docs_url: str,
    variant: dict[str, Any],
) -> str:
    """Render a runnable EU snippet around a captured call."""
    method = (captured.get("method") or op.get("method") or "GET").upper()
    url = captured.get("url") or ""
    try:
        scheme, rest = url.split("://", 1)
        host, _, path = rest.partition("/")
        base = f"{scheme}://{host}"
        path = f"/{path}"
    except ValueError:
        base, path = variant["default_api_base"], url
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
    auth_base = variant["default_auth_base"]
    aud = variant["jwt_audience"]
    label = variant.get("label", "Mastercard Open Finance Europe")

    return (
        f'"""\n'
        f'{api_id} — {op_name}\n'
        f'\n'
        f'Runnable Python that calls the {label} {api_id} API directly.\n'
        f'Signs an RS256 JWT assertion with the partner private key,\n'
        f'exchanges it for an OAuth 2.0 access token, then invokes the\n'
        f'captured operation URL with Bearer auth. URL, body and headers\n'
        f'are captured from the Solution Studio implementation.\n'
        f'\n'
        f'Docs: {docs_url}\n'
        f'\n'
        f'Install:\n'
        f'    pip install requests cryptography\n'
        f'\n'
        f'Run:\n'
        f'    export {env_prefix}_CLIENT_ID="..."\n'
        f'    export {env_prefix}_PRIVATE_KEY_PATH="/path/to/private.pem"\n'
        f'    export {env_prefix}_PUBLIC_CERT_PATH="/path/to/public.pem"\n'
        f'    python {api_id}_{op_id_str}.py\n'
        f'"""\n'
        f"import base64\n"
        f"import hashlib\n"
        f"import json\n"
        f"import os\n"
        f"import time\n"
        f"import uuid\n"
        f"\n"
        f"import requests\n"
        f"from cryptography.hazmat.primitives import hashes, serialization\n"
        f"from cryptography.hazmat.primitives.asymmetric import padding, rsa\n"
        f"from cryptography.x509 import load_pem_x509_certificate\n"
        f"\n"
        f"# --- Credentials (same env vars Solution Studio reads) ----\n"
        f'CLIENT_ID        = os.environ["{env_prefix}_CLIENT_ID"]\n'
        f'PRIVATE_KEY_PATH = os.environ["{env_prefix}_PRIVATE_KEY_PATH"]\n'
        f'PUBLIC_CERT_PATH = os.environ["{env_prefix}_PUBLIC_CERT_PATH"]\n'
        f'APPLICATION_ID   = os.environ.get("{env_prefix}_APPLICATION_ID", "")\n'
        f'AUTH_BASE        = os.environ.get("{env_prefix}_AUTH_BASE_URL", {json.dumps(auth_base)})\n'
        f'API_BASE         = os.environ.get("{env_prefix}_API_BASE_URL",  {json.dumps(base)})\n'
        f'JWT_AUDIENCE     = {json.dumps(aud)}\n'
        f'SCOPES           = "ob_data ob_providers"\n'
        f"\n"
        f"{_EU_AUTH_BLOCK}"
        f"\n"
        f"# --- 3. Call the operation endpoint ---\n"
        f"{todo_block}"
        f"PATH    = {path_literal}\n"
        f'METHOD  = "{method}"\n'
        f'url     = f"{{API_BASE}}{{PATH}}"\n'
        f"headers = {{\n"
        f'    "Accept":        "application/json",\n'
        f'    "Authorization": f"Bearer {{ACCESS_TOKEN}}",\n'
        f"}}\n"
        f"# Consent Machine + downstream APIs require X-Application-Id on every call.\n"
        f"if APPLICATION_ID:\n"
        f'    headers["X-Application-Id"] = APPLICATION_ID\n'
        f"\n"
        f"# --- Request ---\n"
        f"{body_section}"
        f'if body:\n'
        f'    headers["Content-Type"] = "application/json"\n'
        f"\n"
        f"resp = requests.request(METHOD, url, {(requests_kwarg + ', ') if requests_kwarg else ''}headers=headers, timeout=30)\n"
        f"\n"
        f"# --- Show what we sent and what we got back ---\n"
        f'print("=" * 72)\n'
        f'print(f"REQUEST  {{METHOD}} {{url}}")\n'
        f'print("-" * 72)\n'
        f'print("Headers:")\n'
        f"for k, v in headers.items():\n"
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


def build_snippet(
    api_id: str,
    op_id: str,
    *,
    mod: Any,
    manifest: dict[str, Any],
) -> dict[str, Any]:
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
            snippet = _open_finance_snippet(api_id, op, env_prefix, docs_url)
            runnable = True
        else:
            captured = _capture_call(mod, op_id, op, env_prefix)
            if captured and captured.get("url"):
                snippet = _open_finance_snippet_runnable(api_id, op, env_prefix, captured, docs_url)
                runnable = True
            else:
                snippet = _open_finance_snippet(api_id, op, env_prefix, docs_url)
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
