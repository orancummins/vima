"""Mastercard Offers for Publishers API — OAuth 1.0a.

Two underlying APIs share the same base host:
  - Presentment        (offers, access tokens, activations, activities, ...)
  - User Account Admin (enrollments, accounts, replacements, rebates, ...)

Base URLs:
  Sandbox    https://sandbox.api.mastercard.com/loyalty/offers
             https://sandbox.api.mastercard.com/loyalty/offers/presentment
  Production https://api.mastercard.com/loyalty/offers
             https://api.mastercard.com/loyalty/offers/presentment

Docs:
  https://developer.mastercard.com/presentment/documentation/
  https://developer.mastercard.com/presentment/documentation/api-reference/
"""
from __future__ import annotations

import json
import os
from typing import Any
from urllib.parse import urlencode

_SANDBOX_BASE = "https://sandbox.api.mastercard.com/loyalty/offers"
_PROD_BASE    = "https://api.mastercard.com/loyalty/offers"

# Presentment endpoints live under /presentment ; user-account-admin lives at the root.
_PRESENTMENT_SUFFIX = "/presentment"


MANIFEST: dict[str, Any] = {
    "id": "offers_for_publishers",
    "name": "Offers for Publishers",
    "description": (
        "Mastercard Offers for Publishers — REST APIs for publishers to run an "
        "end-to-end merchant-funded offers programme across web and mobile, "
        "including cardholder enrolment, offer presentment, activation, and "
        "savings tracking."
    ),
    "docs_url": "https://developer.mastercard.com/presentment/documentation/",
    "how_to": (
        "<p><strong>Offers for Publishers</strong> exposes two REST APIs over "
        "the same OAuth 1.0a credentials:</p>"
        "<ul>"
        "<li><strong>User Account Administration</strong> — enrol cardholders, "
        "update users / accounts, process card replacements, and search users "
        "(requires the <code>X-FID</code> header — the partner ICA).</li>"
        "<li><strong>Presentment</strong> — issue a short-lived access token "
        "for an enrolled user, then list / fetch offers, activate them, "
        "record like / dislike activities, and retrieve savings.</li>"
        "</ul>"
        "<h3>Typical flow</h3>"
        "<ol>"
        "<li>Use <strong>User Admin → Enrol user</strong> to onboard a "
        "cardholder under a programme.</li>"
        "<li>Use <strong>Presentment → Create access token</strong> with the "
        "same <code>userId</code> / <code>fiId</code> to obtain an "
        "<code>X-Auth-Token</code>.</li>"
        "<li>Pass that token into <strong>List offers</strong> / "
        "<strong>Get offer</strong> / <strong>Activate offer</strong>.</li>"
        "<li>Use <strong>Platform → List platform offers</strong> for an "
        "admin / catalogue-style view that does not require a user token.</li>"
        "</ol>"
        "<h3>Sandbox tips</h3>"
        "<ul>"
        "<li>The sandbox returns mocked offers; most filters are accepted but "
        "ignored.</li>"
        "<li>The <code>X-Auth-Token</code> is bound to the <code>fiId</code> + "
        "<code>userId</code> pair used to create it — generate a fresh one if "
        "you switch users.</li>"
        "</ul>"
    ),
    "categories": ["Access", "Presentment", "Platform", "User Admin", "Rebates"],
    "state_schema": [],
    "configured": bool(
        os.environ.get("OFFERS_FOR_PUBLISHERS_CONSUMER_KEY")
        and os.environ.get("OFFERS_FOR_PUBLISHERS_CONSUMER_KEY") != "your-consumer-key-here"
        and os.environ.get("OFFERS_FOR_PUBLISHERS_SIGNING_KEY_PATH")
    ),
    "operations": [
        # ---- Platform (no auth token needed — smoke test entry point) ------
        {
            "id": "list_platform_offers",
            "name": "List platform offers",
            "category": "Platform",
            "method": "GET",
            "description": (
                "Catalogue view of all offers across the platform — does not require a user-scoped access token "
                "and does not require User Account Administration. "
                "✅ Start here to verify your Presentment API credentials are working."
            ),
            "params": [
                {"name": "fi_id",                "label": "X-FID (FI identifier)",     "type": "text", "default": "999999", "required": True},
                {"name": "category",              "label": "category",              "type": "text", "default": "", "required": False},
                {"name": "presentment_countries", "label": "presentment_countries (ISO-3)", "type": "text", "default": "", "required": False},
                {"name": "limit",                 "label": "limit",                 "type": "text", "default": "10", "required": False},
                {"name": "offset",                "label": "offset",                "type": "text", "default": "0",  "required": False},
                {"name": "accept_language",       "label": "Accept-Language",       "type": "text", "default": "en-US", "required": False},
            ],
        },
        # ---- Presentment --------------------------------------------------
        {
            "id": "create_access_token",
            "name": "Create access token",
            "category": "Access",
            "method": "POST",
            "description": (
                "Exchange an enrolled user's identifiers for a short-lived X-Auth-Token used by all other Presentment calls. "
                "⚠️ The userId must belong to a user already enrolled via the User Account Administration API "
                "(requires a separate project subscription). "
                "If you have not enrolled any users, start with List platform offers instead — that endpoint "
                "works without a user token and does not require User Account Administration."
            ),
            "params": [
                {"name": "fi_id",      "label": "fiId (FI identifier)", "type": "text", "default": "999999", "required": True},
                {"name": "user_id",    "label": "userId (BCN — 16-19 digit numeric)", "type": "text", "default": "5500005555555559", "required": True},
                {"name": "utc_offset", "label": "utcOffset",            "type": "text", "default": "+00:00", "required": True},
            ],
        },
        {
            "id": "list_offers",
            "name": "List offers for user",
            "category": "Presentment",
            "method": "GET",
            "description": "Return all available offers for the user identified by the supplied access token.",
            "params": [
                {"name": "access_token",          "label": "X-Auth-Token",          "type": "text", "default": "", "required": True},
                {"name": "offer_types",           "label": "offer_types",           "type": "text", "default": "", "required": False},
                {"name": "category",              "label": "category",              "type": "text", "default": "", "required": False},
                {"name": "offer_countries",       "label": "offer_countries (ISO-3)", "type": "text", "default": "", "required": False},
                {"name": "active",                "label": "active (true/false)",   "type": "text", "default": "", "required": False},
                {"name": "channels",              "label": "channels (ONLINE/INSTORE)", "type": "text", "default": "", "required": False},
                {"name": "presentment_countries", "label": "presentment_countries (ISO-3)", "type": "text", "default": "", "required": False},
                {"name": "limit",                 "label": "limit",                 "type": "text", "default": "10", "required": False},
                {"name": "offset",                "label": "offset",                "type": "text", "default": "0",  "required": False},
                {"name": "accept_language",       "label": "Accept-Language",       "type": "text", "default": "en-US", "required": False},
            ],
        },
        {
            "id": "get_offer",
            "name": "Get offer by ID",
            "category": "Presentment",
            "method": "GET",
            "description": "Return the full detail view of a single offer for the user.",
            "params": [
                {"name": "access_token",    "label": "X-Auth-Token",    "type": "text", "default": "", "required": True},
                {"name": "offer_id",        "label": "Offer ID",        "type": "text", "default": "", "required": True},
                {"name": "accept_language", "label": "Accept-Language", "type": "text", "default": "en-US", "required": False},
            ],
        },
        {
            "id": "activate_offer",
            "name": "Activate an offer",
            "category": "Presentment",
            "method": "POST",
            "description": "Activate one or more offers for the user behind the supplied access token.",
            "params": [
                {"name": "access_token", "label": "X-Auth-Token", "type": "text", "default": "", "required": True},
                {"name": "offer_id",     "label": "Offer ID",     "type": "text", "default": "", "required": True},
            ],
        },
        {
            "id": "list_activities",
            "name": "List like/dislike activities",
            "category": "Presentment",
            "method": "GET",
            "description": "Return the user's like / dislike activities for a given source type.",
            "params": [
                {"name": "access_token", "label": "X-Auth-Token", "type": "text", "default": "", "required": True},
                {"name": "source_type",  "label": "source_type (e.g. OFFER)", "type": "text", "default": "OFFER", "required": True},
            ],
        },
        {
            "id": "get_savings",
            "name": "Get savings",
            "category": "Presentment",
            "method": "GET",
            "description": "Return accumulated and potential savings for the user.",
            "params": [
                {"name": "access_token", "label": "X-Auth-Token", "type": "text", "default": "", "required": True},
            ],
        },
        # ---- User Account Administration ---------------------------------
        {
            "id": "enroll_user",
            "name": "Enrol user + account",
            "category": "User Admin",
            "method": "POST",
            "description": (
                "Enrol an initial user and primary account into the offers programme. "
                "⚠️ Requires the User Account Administration service to be added to your "
                "Mastercard Developers project separately from the Presentment API. "
                "If you see 401 DECLINED, your credentials are not subscribed to this service. "
                "For Presentment-only testing, use Create access token directly — "
                "the sandbox has pre-enrolled test users."
            ),
            "params": [
                {"name": "fi_id",              "label": "X-FID (ICA)",        "type": "text", "default": "999999", "required": True},
                {"name": "user_id",            "label": "userId (BCN)",        "type": "text", "default": "5500005555555559", "required": True},
                {"name": "user_id_type",       "label": "userIdType",         "type": "select", "options": ["BAN", "BCN", "ARK", "CRK"], "default": "BCN", "required": True},
                {"name": "first_name",         "label": "firstName",          "type": "text", "default": "Jane",  "required": False},
                {"name": "last_name",          "label": "lastName",           "type": "text", "default": "Doe",   "required": False},
                {"name": "email_address",      "label": "emailAddress",       "type": "text", "default": "jane.doe@example.com", "required": False},
                {"name": "preferred_language", "label": "preferredLanguage",  "type": "text", "default": "en-US", "required": False},
                {"name": "account_id",         "label": "account.accountId (BAN 16-19 digits)", "type": "text", "default": "5500005555555559", "required": True},
                {"name": "account_id_type",    "label": "account.accountIdType", "type": "select", "options": ["BAN", "BCN", "ARK", "CRK"], "default": "BAN", "required": True},
                {"name": "bank_product_code",  "label": "account.bankProductCode", "type": "text", "default": "BPC001", "required": True},
                {"name": "program_identifier", "label": "account.programIdentifier", "type": "text", "default": "999999", "required": True},
            ],
        },
        {
            "id": "retrieve_user",
            "name": "Retrieve user by CRK",
            "category": "User Admin",
            "method": "GET",
            "description": "Look up an enrolled user (and all accounts) by Customer Reference Key (CRK).",
            "params": [
                {"name": "fi_id", "label": "X-FID (ICA)", "type": "text", "default": "999999", "required": True},
                {"name": "crk",   "label": "CRK",         "type": "text", "default": "", "required": True},
            ],
        },
        {
            "id": "search_users",
            "name": "Search users",
            "category": "User Admin",
            "method": "POST",
            "description": "Search for a user by BAN, BCN, ARK or CRK.",
            "params": [
                {"name": "fi_id",        "label": "X-FID (ICA)",      "type": "text", "default": "999999", "required": True},
                {"name": "search_id",    "label": "Search identifier","type": "text", "default": "5500005555555559", "required": True},
                {"name": "search_type",  "label": "Identifier type",  "type": "select", "options": ["BAN", "BCN", "ARK", "CRK"], "default": "BCN", "required": True},
            ],
        },
        # ---- Rebates ------------------------------------------------------
        {
            "id": "list_rebates",
            "name": "List rebates",
            "category": "Rebates",
            "method": "GET",
            "description": "Retrieve rebates matching the supplied filters.",
            "params": [
                {"name": "fi_id",  "label": "X-FID (ICA)", "type": "text", "default": "999999",   "required": True},
                {"name": "limit",  "label": "limit",       "type": "text", "default": "10",   "required": False},
                {"name": "offset", "label": "offset",      "type": "text", "default": "0",    "required": False},
            ],
        },
    ],
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _base_url() -> str:
    from simulator.switcher import sim_base_url
    env = os.environ.get("OFFERS_FOR_PUBLISHERS_ENV", "sandbox").lower()
    real = _PROD_BASE if env == "production" else _SANDBOX_BASE
    return sim_base_url("offers_for_publishers", real)


def _is_prod() -> bool:
    return os.environ.get("OFFERS_FOR_PUBLISHERS_ENV", "sandbox").lower() == "production"


def _presentment_url(path: str) -> str:
    from simulator.switcher import is_simulated
    if is_simulated("offers_for_publishers"):
        port = int(os.environ.get("PORT", 9021))
        return f"http://localhost:{port}/api-sim/offers_for_publishers/presentment{path}"
    base = _PROD_BASE if _is_prod() else _SANDBOX_BASE
    return f"{base}{_PRESENTMENT_SUFFIX}{path}"


def _admin_url(path: str) -> str:
    from simulator.switcher import is_simulated
    if is_simulated("offers_for_publishers"):
        port = int(os.environ.get("PORT", 9021))
        return f"http://localhost:{port}/api-sim/offers_for_publishers/admin{path}"
    base = _PROD_BASE if _is_prod() else _SANDBOX_BASE
    return f"{base}{path}"


def _configured() -> bool:
    key = os.environ.get("OFFERS_FOR_PUBLISHERS_CONSUMER_KEY", "")
    path = os.environ.get("OFFERS_FOR_PUBLISHERS_SIGNING_KEY_PATH", "")
    return bool(key and key != "your-consumer-key-here" and path)


def is_configured() -> bool:
    from simulator.switcher import is_simulated
    return _configured() or is_simulated("offers_for_publishers")


def get_state() -> dict[str, Any]:
    return {"configured": _configured()}


def _not_configured_err() -> dict[str, Any]:
    return {
        "success": False,
        "error": (
            "Offers for Publishers is not configured. Set OFFERS_FOR_PUBLISHERS_CONSUMER_KEY "
            "and OFFERS_FOR_PUBLISHERS_SIGNING_KEY_PATH in .env, then restart the server."
        ),
    }


def _resolve_key_path(path: str) -> str:
    if os.path.isabs(path):
        return path
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    return os.path.join(project_root, path)


def _signed_request(method: str, url: str, body_str: str | None, extra_headers: dict[str, str] | None = None) -> dict[str, Any]:
    """Build OAuth-signed headers + execute the HTTP call.

    Returns a uniform response envelope: success / data / error / request /
    response — matching the convention used by the other Mastercard APIs.
    """
    import requests

    from simulator.switcher import is_simulated as _is_sim

    if not _configured() and not _is_sim("offers_for_publishers"):
        return _not_configured_err()

    headers = {"Accept": "application/json"}
    if body_str is not None:
        headers["Content-Type"] = "application/json"
    if extra_headers:
        headers.update(extra_headers)

    if _is_sim("offers_for_publishers"):
        headers["Authorization"] = "Simulated"
    else:
        import oauth1.authenticationutils as authutils
        from oauth1.oauth import OAuth

        consumer_key = os.environ["OFFERS_FOR_PUBLISHERS_CONSUMER_KEY"]
        key_path     = _resolve_key_path(os.environ["OFFERS_FOR_PUBLISHERS_SIGNING_KEY_PATH"])
        key_password = os.environ.get("OFFERS_FOR_PUBLISHERS_SIGNING_KEY_PASSWORD", "keystorepassword")

        try:
            signing_key = authutils.load_signing_key(key_path, key_password)
            auth_header = OAuth.get_authorization_header(
                url, method, body_str or "", consumer_key, signing_key
            )
            headers["Authorization"] = auth_header
        except Exception as exc:
            return {"success": False, "error": f"OAuth signing failed: {exc}"}

    try:
        resp = requests.request(
            method=method,
            url=url,
            data=body_str,
            headers=headers,
            timeout=15,
        )
        status_code = resp.status_code
        try:
            resp_body = resp.json()
        except Exception:
            resp_body = {"raw": resp.text}
    except Exception as exc:
        return {"success": False, "error": f"Request failed: {exc}"}

    success = 200 <= status_code < 300
    return {
        "success": success,
        "data": resp_body if success else {},
        "error": None if success else (resp_body.get("Errors") if isinstance(resp_body, dict) else resp_body),
        "request": {"method": method, "url": url, "body": body_str, "headers": {k: v for k, v in headers.items() if k != "Authorization"}},
        "response": {"status_code": status_code, "body": resp_body},
        "state_updates": {},
    }


def _qs(params: dict[str, Any]) -> str:
    items = {k: v for k, v in params.items() if v not in (None, "", [])}
    return ("?" + urlencode(items)) if items else ""


def _enc_cert_path() -> str | None:
    """Return the absolute path to the JWE encryption certificate, or None if not configured."""
    cert = os.environ.get("OFFERS_FOR_PUBLISHERS_ENCRYPTION_KEY_PATH", "").strip()
    if not cert or cert == "your-encryption-cert.pem":
        return None
    if not os.path.isabs(cert):
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        cert = os.path.join(project_root, cert)
    return cert if os.path.exists(cert) else None


def _encrypt_admin_body(body: dict[str, Any]) -> str:
    """JWE-encrypt a UA Admin request body using the Mastercard client-encryption library."""
    from client_encryption.jwe_encryption import encrypt_payload
    from client_encryption.jwe_encryption_config import JweEncryptionConfig

    cert_path = _enc_cert_path()
    if not cert_path:
        # No cert — send plain (sandbox may permit this during initial testing)
        return json.dumps(body)

    config = JweEncryptionConfig({
        "paths": {
            "$": {
                "toEncrypt": {"$": "$"},
                "toDecrypt": {},
            }
        },
        "encryptedValueFieldName": "jweEncryptedData",
        "encryptionCertificate": cert_path,
    })
    encrypted = encrypt_payload(json.dumps(body), config)
    return json.dumps(encrypted)


# ---------------------------------------------------------------------------
# Operations
# ---------------------------------------------------------------------------
def execute(op_id: str, params: dict[str, Any]) -> dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("offers_for_publishers"):
        return _not_configured_err()
    dispatch = {
        "create_access_token":   _create_access_token,
        "list_offers":           _list_offers,
        "get_offer":             _get_offer,
        "list_platform_offers":  _list_platform_offers,
        "activate_offer":        _activate_offer,
        "list_activities":       _list_activities,
        "get_savings":           _get_savings,
        "enroll_user":           _enroll_user,
        "retrieve_user":         _retrieve_user,
        "search_users":          _search_users,
        "list_rebates":          _list_rebates,
    }
    fn = dispatch.get(op_id)
    if not fn:
        return {"success": False, "error": f"Unknown operation: {op_id}"}
    return fn(params)


def _create_access_token(p: dict[str, Any]) -> dict[str, Any]:
    body: dict[str, Any] = {
        "fiId":      (p.get("fi_id") or "").strip(),
        "userId":    (p.get("user_id") or "").strip(),
        "utcOffset": (p.get("utc_offset") or "+00:00").strip(),
    }
    return _signed_request("POST", _presentment_url("/access-tokens"), json.dumps(body), _fid_header(p))


def _auth_headers(p: dict[str, Any]) -> dict[str, str]:
    tok = (p.get("access_token") or "").strip()
    headers: dict[str, str] = {}
    if tok:
        headers["X-Auth-Token"] = tok
    lang = (p.get("accept_language") or "").strip()
    if lang:
        headers["Accept-Language"] = lang
    return headers


def _list_offers(p: dict[str, Any]) -> dict[str, Any]:
    if not (p.get("access_token") or "").strip():
        return {"success": False, "error": "'access_token' (X-Auth-Token) is required. Use Create access token first."}
    qs = _qs({
        "offer_types":           p.get("offer_types"),
        "category":              p.get("category"),
        "offer_countries":       p.get("offer_countries"),
        "active":                p.get("active"),
        "channels":              p.get("channels"),
        "presentment_countries": p.get("presentment_countries"),
        "limit":                 p.get("limit") or "10",
        "offset":                p.get("offset") or "0",
    })
    return _signed_request("GET", _presentment_url(f"/offers{qs}"), None, _auth_headers(p))


def _get_offer(p: dict[str, Any]) -> dict[str, Any]:
    if not (p.get("access_token") or "").strip():
        return {"success": False, "error": "'access_token' (X-Auth-Token) is required. Use Create access token first."}
    offer_id = (p.get("offer_id") or "").strip()
    if not offer_id:
        return {"success": False, "error": "'offer_id' is required."}
    return _signed_request("GET", _presentment_url(f"/offers/{offer_id}"), None, _auth_headers(p))


def _list_platform_offers(p: dict[str, Any]) -> dict[str, Any]:
    qs = _qs({
        "fid":                   p.get("fi_id") or "999999",
        "category":              p.get("category"),
        "presentment_countries": p.get("presentment_countries"),
        "limit":                 p.get("limit") or "10",
        "offset":                p.get("offset") or "0",
    })
    return _signed_request("GET", _presentment_url(f"/platforms/offers{qs}"), None, _auth_headers(p))


def _activate_offer(p: dict[str, Any]) -> dict[str, Any]:
    if not (p.get("access_token") or "").strip():
        return {"success": False, "error": "'access_token' (X-Auth-Token) is required. Use Create access token first."}
    offer_id = (p.get("offer_id") or "").strip()
    if not offer_id:
        return {"success": False, "error": "'offer_id' is required."}
    body = {"activations": [{"offerId": offer_id}]}
    return _signed_request("POST", _presentment_url("/activations"), json.dumps(body), _auth_headers(p))


def _list_activities(p: dict[str, Any]) -> dict[str, Any]:
    if not (p.get("access_token") or "").strip():
        return {"success": False, "error": "'access_token' (X-Auth-Token) is required. Use Create access token first."}
    source_type = (p.get("source_type") or "OFFER").strip()
    return _signed_request("GET", _presentment_url(f"/activities/{source_type}"), None, _auth_headers(p))


def _get_savings(p: dict[str, Any]) -> dict[str, Any]:
    if not (p.get("access_token") or "").strip():
        return {"success": False, "error": "'access_token' (X-Auth-Token) is required. Use Create access token first."}
    return _signed_request("GET", _presentment_url("/savings"), None, _auth_headers(p))


def _fid_header(p: dict[str, Any]) -> dict[str, str]:
    fid = (p.get("fi_id") or "").strip()
    return {"X-FID": fid} if fid else {}


def _enroll_user(p: dict[str, Any]) -> dict[str, Any]:
    body: dict[str, Any] = {
        "userId":     (p.get("user_id") or "").strip(),
        "userIdType": (p.get("user_id_type") or "BCN").strip(),
        "account": {
            "accountId":         (p.get("account_id") or "").strip(),
            "accountIdType":     (p.get("account_id_type") or "BAN").strip(),
            "bankProductCode":   (p.get("bank_product_code") or "").strip(),
            "programIdentifier": (p.get("program_identifier") or "").strip(),
        },
    }
    for k_in, k_out in (
        ("first_name", "firstName"),
        ("last_name", "lastName"),
        ("email_address", "emailAddress"),
        ("preferred_language", "preferredLanguage"),
    ):
        v = (p.get(k_in) or "").strip()
        if v:
            body[k_out] = v
    return _signed_request("POST", _admin_url("/enrollments/users"), _encrypt_admin_body(body), _fid_header(p))


def _retrieve_user(p: dict[str, Any]) -> dict[str, Any]:
    crk = (p.get("crk") or "").strip()
    if not crk:
        return {"success": False, "error": "'crk' is required."}
    return _signed_request("GET", _admin_url(f"/enrollments/users/{crk}"), None, _fid_header(p))


def _search_users(p: dict[str, Any]) -> dict[str, Any]:
    search_id   = (p.get("search_id") or "").strip()
    search_type = (p.get("search_type") or "BCN").strip()
    if not search_id:
        return {"success": False, "error": "'search_id' is required."}
    body = {"id": search_id, "idType": search_type}
    return _signed_request("POST", _admin_url("/enrollments/users/searches"), _encrypt_admin_body(body), _fid_header(p))


def _list_rebates(p: dict[str, Any]) -> dict[str, Any]:
    qs = _qs({"limit": p.get("limit") or "10", "offset": p.get("offset") or "0"})
    return _signed_request("GET", _admin_url(f"/rebates{qs}"), None, _fid_header(p))
