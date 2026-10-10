"""Open Finance Europe (Mastercard / Aiia) API module.

The EU stack is a separate product family from US/AU Finicity:

  * OAuth 2.0 client_credentials with a JWT client-assertion (RS256), signed
    by the partner's RSA private key. ``kid`` = SHA-256 thumbprint (base64url)
    of the public certificate body.
  * Manual onboarding — Mastercard EU onboarding officer provisions a clientId
    and adds the public cert to the trust list. No self-serve portal flow.
  * Consent endpoints (``/consents``, ``/consents/{id}/managed-flows``) drive
    the Aiia Flow that the customer completes in their bank.
"""
from __future__ import annotations

import os
import uuid
from typing import Any

from .client import OpenFinanceEUClient

# ---------------------------------------------------------------------------
# Client (singleton)
# ---------------------------------------------------------------------------

_client: OpenFinanceEUClient | None = None
_client_sig: tuple | None = None


def _get_client() -> OpenFinanceEUClient | None:
    global _client, _client_sig
    from simulator.switcher import is_simulated
    if is_simulated("open_finance_eu"):
        # The simulator does not perform JWT verification; pass dummy paths.
        port = int(os.environ.get("PORT", 9021))
        sim_base = f"http://localhost:{port}/api-sim/open_finance_eu"
        return OpenFinanceEUClient(
            client_id="sim_client",
            private_key_path="__simulator__",
            public_cert_path="__simulator__",
            auth_base_url=sim_base,
            api_base_url=sim_base,
        )
    cid = os.environ.get("OPEN_FINANCE_EU_CLIENT_ID", "")
    pkey = os.environ.get("OPEN_FINANCE_EU_PRIVATE_KEY_PATH", "")
    pcert = os.environ.get("OPEN_FINANCE_EU_PUBLIC_CERT_PATH", "")
    app_id = os.environ.get("OPEN_FINANCE_EU_APPLICATION_ID", "")
    auth_base = os.environ.get(
        "OPEN_FINANCE_EU_AUTH_BASE_URL",
        OpenFinanceEUClient.DEFAULT_AUTH_BASE,
    )
    api_base = os.environ.get(
        "OPEN_FINANCE_EU_API_BASE_URL",
        OpenFinanceEUClient.DEFAULT_API_BASE,
    )
    if not (cid and pkey and pcert) or cid == "your_client_id_here":
        _client = _client_sig = None
        return None
    # Rebuild the cached client whenever any credential changes so a config
    # save/import takes effect without a server restart.
    sig = (cid, pkey, pcert, app_id, auth_base, api_base)
    if _client is not None and _client_sig == sig:
        return _client
    _client = OpenFinanceEUClient(
        client_id=cid,
        private_key_path=pkey,
        public_cert_path=pcert,
        auth_base_url=auth_base,
        api_base_url=api_base,
        application_id=app_id,
    )
    _client_sig = sig
    return _client


def is_configured() -> bool:
    from simulator.switcher import is_simulated
    return is_simulated("open_finance_eu") or _get_client() is not None


# ---------------------------------------------------------------------------
# Per-API state
# ---------------------------------------------------------------------------

STATE: dict[str, Any] = {
    "provider_id": None,
    "consent_id": None,
    "flow_url": None,
    "account_id": None,
    # End-user identifier used in Create Consent / Create Managed Flow.
    # Generated once per session and re-used so both calls reference the
    # same PSU (required by Aiia — the consent's endUsers[0].identifier
    # must match the managed flow's endUser.identifier).
    "end_user_id": None,
    # Required by the Aiia Consent Machine on every Create Consent call.
    "end_user_email": None,
    # Mastercard onboarding hands out a useCaseConfigurationId per use case.
    # Seeded from OPEN_FINANCE_EU_USE_CASE_ID; the user can override via
    # the Create Consent form.
    "use_case_configuration_id": None,
    # Populated by Get Providers — feeds the provider_select dropdown on
    # Create Managed Flow. Items: {id, name, country}.
    "providers": [],
    # Seeded from OPEN_FINANCE_EU_REDIRECT_URL. Informational only — the
    # actual redirect target is fixed on the Mastercard onboarding record
    # and cannot be overridden per-request.
    "redirect_urls": [],
}


# ---------------------------------------------------------------------------
# Sandbox test credentials (Mastercard Open Finance EU)
# ---------------------------------------------------------------------------
# Sourced verbatim from the official Testing page:
#   https://developer.mastercard.com/open-finance-data/documentation/developer-support/testing/
# All users have German IBANs in EUR; password is `12345` for every user.
# ``john.smith`` is the only user with rich/dynamic data (4 accounts since
# 2023-01-01) — recommend it as the default for new integrators.

TEST_USERS_DOCS_URL = (
    "https://developer.mastercard.com/open-finance-data/documentation/"
    "developer-support/testing/"
)

TEST_USERS: list[dict[str, Any]] = [
    {"username": "john.smith",         "password": "12345", "otp": "987654",
     "flow": "Redirect",                                  "data": "Advanced (4 accounts since 2023, dynamic)",
     "recommended": True},
    {"username": "mattias.mustermann", "password": "12345", "otp": "12345",
     "flow": "Redirect",                                  "data": "Basic"},
    {"username": "max.mustermann",     "password": "12345", "otp": "987654",
     "flow": "Embedded with OTP",                         "data": "Basic"},
    {"username": "erika.mustermann",   "password": "12345", "otp": "987654",
     "flow": "Embedded with OTP + OTP-type choice",       "data": "Basic"},
    {"username": "dan.mustermann",     "password": "12345", "otp": "987654",
     "flow": "Decoupled",                                 "data": "Basic"},
    {"username": "nomoney.mustermann", "password": "12345", "otp": "987654",
     "flow": "Embedded with OTP",                         "data": "No accounts (failure path)"},
]

TEST_PROVIDERS_NOTE = (
    "Sandbox exposes four test providers: Mock Bank, Redirect Test Bank, "
    "Embedded Test Bank, Decoupled Test Bank. Pick the bank whose name "
    "matches the test user's default flow (or Mock Bank to let the user's "
    "default flow drive selection)."
)


def _test_credentials_payload() -> dict[str, Any]:
    """Compact representation of the sandbox PSU credentials table.

    Returned as a hint on consent / managed-flow operations so the UI can
    surface the official Aiia test users (and the docs link) without
    requiring the user to leave the explorer. Emitted on both success and
    error responses so it remains visible while debugging sandbox issues.
    """
    return {
        "title": "Sandbox test users (password is 12345 for all)",
        "docs_url": TEST_USERS_DOCS_URL,
        "docs_label": "Mastercard Open Finance EU — Testing docs",
        "providers_note": TEST_PROVIDERS_NOTE,
        "columns": ["Username", "Password", "OTP", "Flow", "Data"],
        "rows": [
            [u["username"], u["password"], u["otp"], u["flow"], u["data"]]
            for u in TEST_USERS
        ],
        "recommended": next(
            (u["username"] for u in TEST_USERS if u.get("recommended")),
            None,
        ),
    }


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------

MANIFEST: dict[str, Any] = {
    "id": "open_finance_eu",
    "name": "Open Finance Europe",
    "description": (
        "Mastercard Open Finance Europe (Aiia) — PSD2-aligned consent, account "
        "information, transactions, balances, and account-ownership insights "
        "across ~3,000 European banks via a single API."
    ),
    "how_to": (
        "<p><strong>Mastercard Open Finance Europe</strong> is the Aiia-backed "
        "European stack — a different product family from the Finicity-backed "
        "US and Australia APIs. Authentication uses OAuth 2.0 with a "
        "<em>JWT client assertion</em> signed by your RSA private key.</p>"
        "<h3>Onboarding (manual)</h3>"
        "<ol>"
        "<li>Generate a 4096-bit RSA keypair locally:<br>"
        "<code>openssl req -x509 -sha256 -nodes -newkey rsa:4096 "
        "-keyout private.key -days 730 -out public.pem</code></li>"
        "<li>Email <a href='mailto:openbankingeu_support@mastercard.com'>"
        "openbankingeu_support@mastercard.com</a> attaching <code>public.pem</code> "
        "to receive a sandbox <code>clientId</code>.</li>"
        "<li>Populate <code>config/.env</code> with: "
        "<code>OPEN_FINANCE_EU_CLIENT_ID</code>, "
        "<code>OPEN_FINANCE_EU_PRIVATE_KEY_PATH</code>, "
        "<code>OPEN_FINANCE_EU_PUBLIC_CERT_PATH</code>.</li>"
        "</ol>"
        "<h3>Quick Start flow</h3>"
        "<ol>"
        "<li><strong>Auth → Create Access Token</strong> — signs a JWT and exchanges "
        "it for a bearer token at <code>/oauth2/token</code>. Cached for ~1 hour.</li>"
        "<li><strong>Providers → Get Providers</strong> — list supported ASPSPs. "
        "Credential-only smoke test; no consent needed.</li>"
        "<li><strong>Consent → Create Consent</strong> — produces a "
        "<code>consent_id</code> stored in state.</li>"
        "<li><strong>Consent → Create Managed Flow</strong> — returns a hosted Aiia "
        "Flow URL. <strong>Open in a new tab</strong>, complete the bank SCA, then "
        "come back.</li>"
        "<li><strong>Consent → Get Consent</strong> — poll until status is "
        "<code>granted</code> (replaces webhook for testing).</li>"
        "<li><strong>Accounts → Get Accounts</strong> — list accounts under the "
        "active consent. Auto-saves the first <code>account_id</code> to state.</li>"
        "<li><strong>Transactions → Get Transactions</strong> — pull recent "
        "transactions for the active account.</li>"
        "</ol>"
        "<h3>Sandbox</h3>"
        "<ul>"
        "<li>Auth host: <code>mtf.auth.openbanking.mastercard.eu</code></li>"
        "<li>API host: <code>mtf.api.openbanking.mastercard.com</code></li>"
        "<li>Test banks (4): <code>Mock Bank</code>, <code>Redirect Test Bank</code>, "
        "<code>Embedded Test Bank</code>, <code>Decoupled Test Bank</code> — pick "
        "the bank that matches the test user's default flow.</li>"
        "<li><strong>Test users</strong> (password <code>12345</code> for all):"
        "<ul>"
        "<li><code>john.smith</code> — Redirect, OTP <code>987654</code> — "
        "<em>advanced data</em> (4 accounts since 2023, dynamic). <strong>Recommended starter.</strong></li>"
        "<li><code>mattias.mustermann</code> — Redirect, OTP <code>12345</code> — basic data</li>"
        "<li><code>max.mustermann</code> — Embedded with OTP <code>987654</code> — basic data</li>"
        "<li><code>erika.mustermann</code> — Embedded with OTP-type choice, OTP <code>987654</code> — basic data</li>"
        "<li><code>dan.mustermann</code> — Decoupled, OTP <code>987654</code> — basic data</li>"
        "<li><code>nomoney.mustermann</code> — Embedded, OTP <code>987654</code> — <em>no accounts</em> (failure path)</li>"
        "</ul>"
        "Full table: <a href='https://developer.mastercard.com/open-finance-data/documentation/developer-support/testing/' "
        "target='_blank' rel='noopener'>Testing docs ↗</a></li>"
        "<li>Docs: "
        "<a href='https://developer.mastercard.com/open-finance-data/documentation/' "
        "target='_blank' rel='noopener'>Open Finance Data</a> · "
        "<a href='https://developer.mastercard.com/open-finance-data/documentation/developer-support/api-basics/authentication/' "
        "target='_blank' rel='noopener'>Authentication</a> · "
        "<a href='https://developer.mastercard.com/open-finance-data/documentation/developer-support/testing/' "
        "target='_blank' rel='noopener'>Testing &amp; PSU credentials</a> · "
        "<a href='https://developer.mastercard.com/open-finance-data/documentation/use-cases/account-opening-guide/account-opening-guide/' "
        "target='_blank' rel='noopener'>Account Opening Guide</a></li>"
        "</ul>"
        "<p><em>Tip:</em> <strong>Create Access Token</strong> is the simplest live "
        "smoke test — it confirms your private key, kid, and clientId are all "
        "correct without needing a consent.</p>"
    ),
    "docs_url": "https://developer.mastercard.com/open-finance-data/documentation/",
    "categories": [
        "Auth", "Providers", "Consent", "Accounts", "Transactions",
        "Balances", "Insights",
    ],
    "state_schema": [
        {"key": "provider_id", "label": "Provider ID"},
        {"key": "consent_id", "label": "Consent ID"},
        {"key": "account_id", "label": "Account ID"},
        {"key": "end_user_id", "label": "End User ID"},
        {"key": "use_case_configuration_id", "label": "Use Case Config ID"},
    ],
    # Curated guide for the floating API Guide coach. Walks a valid happy path
    # only — no other API calls.
    "guide": [
        {
            "op": "create_token",
            "title": "Create Access Token",
            "summary": "Authenticate with partner credentials. Click Send below.",
        },
        {
            "op": "create_consent",
            "title": "Create Consent",
            "summary": "Create the consent that authorises account access. Click Send below.",
        },
        {
            "op": "create_managed_flow",
            "title": "Create Managed Flow",
            "summary": "Generate the hosted bank-login URL. Click Send below.",
        },
        {
            "type": "manual",
            "id": "launch_connect",
            "title": "Launch Connect",
            "summary": "Click the orange Launch Connect button and complete consent, then continue.",
            "done_label": "I've completed consent",
        },
        {
            "op": "get_accounts",
            "title": "Get Accounts",
            "summary": "List the consented accounts. Click Send below.",
        },
        {
            "op": "get_transactions",
            "title": "Get Transactions",
            "summary": "Pull recent transactions for the account. Click Send below.",
        },
    ],
    "operations": [
        # ---- Auth ----
        {
            "id": "create_token",
            "name": "Create Access Token",
            "category": "Auth",
            "method": "POST",
            "description": (
                "Sign a JWT with your private key and exchange it for a bearer "
                "access token at /oauth2/token. Smoke-test operation — requires "
                "only clientId + private key + public cert."
            ),
            "params": [],
            "requires": [],
            "produces": [],
        },
        # ---- Providers ----
        {
            "id": "get_providers",
            "name": "Get Providers",
            "category": "Providers",
            "method": "GET",
            "description": (
                "List supported European banks (ASPSPs). No consent required — "
                "good credential-only smoke test."
            ),
            "params": [
                {"name": "country", "label": "Country (ISO 3166-1 alpha-2)",
                 "type": "string", "default": "DK", "required": False},
                {"name": "limit", "label": "Limit", "type": "number",
                 "default": 25, "required": False},
            ],
        },
        {
            "id": "set_provider",
            "name": "Set Active Provider",
            "category": "Providers",
            "method": "LOCAL",
            "description": (
                "Set the active provider_id used as default by Create Consent. "
                "Useful when you already picked a provider from Get Providers."
            ),
            "params": [
                {"name": "provider_id", "label": "Provider ID", "type": "string",
                 "source": "state:provider_id", "required": True},
            ],
            "produces": ["provider_id"],
        },
        # ---- Consent ----
        {
            "id": "create_consent",
            "name": "Create Consent",
            "category": "Consent",
            "method": "POST",
            "description": (
                "Create a Mastercard Open Finance consent. Body matches the "
                "official Account Opening Guide: \u007BuseCaseConfigurationId, "
                "endUsers:[{identifier}]\u007D. The provider/bank is chosen by "
                "the end user later inside the Aiia Flow UI."
            ),
            "params": [
                {"name": "use_case_configuration_id",
                 "label": "Use Case Configuration ID",
                 "type": "string",
                 "source": "state:use_case_configuration_id",
                 "required": True,
                 "help": "Provisioned by Mastercard onboarding (env: OPEN_FINANCE_EU_USE_CASE_ID)."},
                {"name": "end_user_id",
                 "label": "End User ID",
                 "type": "string",
                 "source": "state:end_user_id",
                 "required": False,
                 "help": "Stable identifier for the PSU. Leave blank to auto-generate a UUID and reuse for the managed flow."},
                {"name": "end_user_email",
                 "label": "End User Email",
                 "type": "string",
                 "source": "state:end_user_email",
                 "default": "vima-sandbox@example.com",
                 "required": True,
                 "help": "Required by the Aiia Consent Machine. Use any deliverable address \u2014 sandbox does not send mail."},
            ],
            "requires": [],
            "produces": ["consent_id", "end_user_id"],
        },
        {
            "id": "create_managed_flow",
            "name": "Create Managed Flow",
            "category": "Consent",
            "method": "POST",
            "description": (
                "Generate the hosted Aiia Flow URL the customer opens to grant "
                "consent at their bank. The end_user identifier must match the "
                "one used in Create Consent. Provider hint is optional — if "
                "omitted the end user picks the bank from the Aiia bank list. "
                "Sandbox: log in with one of the test PSUs (e.g. "
                "<code>john.smith</code> / <code>12345</code>, OTP <code>987654</code>) — "
                "the launch banner shows the full credentials table with a link "
                "to the official Testing docs."
            ),
            "params": [
                {"name": "consent_id", "label": "Consent ID", "type": "string",
                 "source": "state:consent_id", "required": True},
                {"name": "end_user_id", "label": "End User ID", "type": "string",
                 "source": "state:end_user_id", "required": True,
                 "help": "Must match endUsers[0].identifier from Create Consent."},
                {"name": "provider_id", "label": "Provider (optional hint)",
                 "type": "provider_select",
                 "source": "state:provider_id", "required": False,
                 "help": "Optional: pre-select the bank to skip the bank-picker step. Populated by Get Providers."},
                {"name": "language", "label": "Language", "type": "string",
                 "default": "en", "required": False},
            ],
            "requires": ["consent_id", "end_user_id"],
            "produces": ["flow_url"],
            "ui_hint": "open_link",
        },
        {
            "id": "get_consent",
            "name": "Get Consent",
            "category": "Consent",
            "method": "GET",
            "description": (
                "Poll for the current status of a consent (no webhook required). "
                "Run after the customer completes the Aiia Flow to confirm the "
                "consent is granted before fetching accounts."
            ),
            "params": [
                {"name": "consent_id", "label": "Consent ID", "type": "string",
                 "source": "state:consent_id", "required": True},
            ],
            "requires": ["consent_id"],
        },
        {
            "id": "revoke_consent",
            "name": "Revoke Consent",
            "category": "Consent",
            "method": "DELETE",
            "description": "Revoke a previously-granted consent.",
            "params": [
                {"name": "consent_id", "label": "Consent ID", "type": "string",
                 "source": "state:consent_id", "required": True},
            ],
            "requires": ["consent_id"],
        },
        # ---- Accounts ----
        {
            "id": "get_accounts",
            "name": "Get Accounts",
            "category": "Accounts",
            "method": "GET",
            "description": (
                "List accounts visible under the active consent. Calls "
                "GET /data/accounts with the X-Consent-Id header. Saves the "
                "first account_id to state for downstream operations."
            ),
            "params": [
                {"name": "consent_id", "label": "Consent ID", "type": "string",
                 "source": "state:consent_id", "required": True},
                {"name": "include", "label": "Include", "type": "string",
                 "default": "balances,holders,identifiers,additionalInformation",
                 "required": False,
                 "help": "Comma-separated sub-resources to expand."},
            ],
            "requires": ["consent_id"],
            "produces": ["account_id"],
        },
        {
            "id": "get_account",
            "name": "Get Account",
            "category": "Accounts",
            "method": "GET",
            "description": "Retrieve details for a single account by ID.",
            "params": [
                {"name": "account_id", "label": "Account ID", "type": "string",
                 "source": "state:account_id", "required": True},
            ],
            "requires": ["account_id"],
        },
        # ---- Transactions / Balances ----
        {
            "id": "get_transactions",
            "name": "Get Transactions",
            "category": "Transactions",
            "method": "GET",
            "description": "Retrieve transactions for the active account.",
            "params": [
                {"name": "account_id", "label": "Account ID", "type": "string",
                 "source": "state:account_id", "required": True},
                {"name": "from_date", "label": "From (YYYY-MM-DD)",
                 "type": "string", "default": "", "required": False},
                {"name": "to_date", "label": "To (YYYY-MM-DD)",
                 "type": "string", "default": "", "required": False},
                {"name": "limit", "label": "Limit", "type": "number",
                 "default": 50, "required": False},
            ],
            "requires": ["account_id"],
        },
        {
            "id": "check_balance",
            "name": "Check Account Balance",
            "category": "Balances",
            "method": "POST",
            "description": (
                "Trigger an on-demand balance retrieval. Useful for affordability "
                "checks immediately before initiating a payment. The freshness "
                "policy (<code>maxAge</code>) controls whether the cached balance "
                "is returned or a live provider call is forced \u2014 use "
                "<code>PT0S</code> for an immediate provider refresh."
            ),
            "params": [
                {"name": "account_id", "label": "Account ID", "type": "string",
                 "source": "state:account_id", "required": True},
                {"name": "max_age", "label": "Max Age (ISO 8601 duration)",
                 "type": "string", "default": "PT15M", "required": False,
                 "help": "ISO 8601 duration. PT0S forces a live provider call; PT15M returns the cached balance if it is fresher than 15 minutes."},
            ],
            "requires": ["account_id"],
        },
        # ---- Insights ----
        {
            "id": "verify_account_ownership",
            "name": "Verify Account Ownership",
            "category": "Insights",
            "method": "POST",
            "description": (
                "Submit an Account Ownership Verification (Account Match) — "
                "compares the consented account holder(s) to the supplied "
                "customer name and returns a 0\u2013100 similarity score per "
                "account holder. Leave Account IDs blank to match against "
                "every authorized account on the consent."
            ),
            "params": [
                {"name": "customer_name", "label": "Customer Name",
                 "type": "string", "default": "John Smith", "required": True,
                 "help": "Full name to compare against the provider-reported account holder(s)."},
                {"name": "account_ids", "label": "Account IDs (optional, comma-separated)",
                 "type": "string", "source": "state:account_id", "required": False,
                 "help": "Optional UUIDs to restrict the check. Leave blank to verify every authorized account."},
            ],
            "requires": [],
        },
    ],
}


# ---------------------------------------------------------------------------
# Dispatcher
# ---------------------------------------------------------------------------

def _err(msg: str, code: int = 400,
         hints: dict[str, Any] | None = None) -> dict[str, Any]:
    return {"status": "error", "code": code, "data": {"error": msg},
            "state_updates": {}, "hints": hints or {}}


def _ok(data: Any, code: int = 200,
        state_updates: dict[str, Any] | None = None,
        hints: dict[str, Any] | None = None) -> dict[str, Any]:
    if state_updates:
        for k, v in state_updates.items():
            if v is not None:
                STATE[k] = v
    return {
        "status": "ok",
        "code": code,
        "data": data,
        "state_updates": state_updates or {},
        "hints": hints or {},
    }


def _seed_defaults() -> None:
    """Lazy-seed STATE from env on first access.

    * ``redirect_urls`` — from OPEN_FINANCE_EU_REDIRECT_URL.
    * ``use_case_configuration_id`` — from OPEN_FINANCE_EU_USE_CASE_ID.
    * ``end_user_id`` — stays None until the first Create Consent call,
      where a UUID is generated and stashed for the managed flow to reuse.
    """
    if not STATE.get("redirect_urls"):
        env_url = os.environ.get("OPEN_FINANCE_EU_REDIRECT_URL", "").strip()
        STATE["redirect_urls"] = [env_url] if env_url else []
    if not STATE.get("use_case_configuration_id"):
        env_ucid = os.environ.get("OPEN_FINANCE_EU_USE_CASE_ID", "").strip()
        if env_ucid:
            STATE["use_case_configuration_id"] = env_ucid


def _record_redirect_url(url: str | None) -> None:
    """Append a user-supplied redirect URL to STATE['redirect_urls']."""
    if not url:
        return
    bucket = STATE.setdefault("redirect_urls", [])
    if url not in bucket:
        bucket.append(url)


def get_state() -> dict[str, Any]:
    _seed_defaults()
    return {
        "provider_id": STATE.get("provider_id"),
        "consent_id": STATE.get("consent_id"),
        "account_id": STATE.get("account_id"),
        "flow_url": STATE.get("flow_url"),
        "end_user_id": STATE.get("end_user_id"),
        "end_user_email": STATE.get("end_user_email"),
        "use_case_configuration_id": STATE.get("use_case_configuration_id"),
        "providers": list(STATE.get("providers") or []),
        "redirect_urls": list(STATE.get("redirect_urls") or []),
    }


def _extract_first(data: Any, *keys: str) -> str | None:
    """Defensive lookup — the Aiia response shape uses both camelCase and
    snake_case across versions; try the listed keys in order."""
    if not isinstance(data, dict):
        return None
    for k in keys:
        v = data.get(k)
        if v:
            return str(v)
    return None


def execute(op_id: str, params: dict[str, Any]) -> dict[str, Any]:
    """Dispatch operation by id; returns {status, code, data, state_updates, hints}."""
    p = params or {}

    # LOCAL operations.
    if op_id == "set_provider":
        pid = p.get("provider_id")
        if not pid:
            return _err("provider_id is required")
        return _ok({"provider_id": str(pid), "message": "Active provider set"},
                   200, {"provider_id": str(pid)})

    client = _get_client()
    if client is None:
        return _err(
            "Open Finance Europe is not configured. Email "
            "openbankingeu_support@mastercard.com to obtain a clientId, then set "
            "OPEN_FINANCE_EU_CLIENT_ID + OPEN_FINANCE_EU_PRIVATE_KEY_PATH + "
            "OPEN_FINANCE_EU_PUBLIC_CERT_PATH in config/.env.",
            code=412,
        )

    try:
        if op_id == "create_token":
            data, code = client.create_token()
            return _ok(data, code)

        if op_id == "get_providers":
            try:
                limit = int(p.get("limit") or 25)
            except (TypeError, ValueError):
                limit = 25
            data, code = client.get_providers(country=p.get("country", ""),
                                              limit=limit)
            # Cache a slim provider list in state so Create Consent can
            # render a dropdown without re-fetching.
            state_updates: dict[str, Any] = {}
            if isinstance(data, dict):
                items = data.get("items") or data.get("providers") or []
                if isinstance(items, list):
                    slim = []
                    for it in items:
                        if not isinstance(it, dict):
                            continue
                        pid = it.get("id") or it.get("provider_id")
                        if not pid:
                            continue
                        slim.append({
                            "id": str(pid),
                            "name": it.get("displayName") or it.get("name") or str(pid),
                            "country": it.get("countryCode") or it.get("country") or "",
                        })
                    if slim:
                        STATE["providers"] = slim
                        state_updates["providers"] = slim
            return _ok(data, code, state_updates or None)

        if op_id == "create_consent":
            _seed_defaults()
            creds_hint = {"test_credentials": _test_credentials_payload()}
            ucid = (p.get("use_case_configuration_id")
                    or STATE.get("use_case_configuration_id"))
            if not ucid:
                return _err(
                    "use_case_configuration_id is required — set "
                    "OPEN_FINANCE_EU_USE_CASE_ID in config/.env or pass it on "
                    "the Create Consent form.",
                    hints=creds_hint,
                )
            eu_id = (p.get("end_user_id") or STATE.get("end_user_id")
                     or str(uuid.uuid4()))
            email = (p.get("end_user_email")
                     or STATE.get("end_user_email")
                     or os.environ.get("OPEN_FINANCE_EU_END_USER_EMAIL", "").strip()
                     or "vima-sandbox@example.com")
            data, code = client.create_consent(
                use_case_configuration_id=str(ucid),
                end_user_id=str(eu_id),
                end_user_email=str(email),
            )
            cid = _extract_first(data, "consentId", "consent_id", "id")
            state_updates: dict[str, Any] = {
                "use_case_configuration_id": str(ucid),
                "end_user_id": str(eu_id),
                "end_user_email": str(email),
            }
            if cid:
                state_updates["consent_id"] = cid
            return _ok(data, code, state_updates, creds_hint)

        if op_id == "create_managed_flow":
            creds_hint = {"test_credentials": _test_credentials_payload()}
            cid = p.get("consent_id") or STATE.get("consent_id")
            if not cid:
                return _err("consent_id is required (run Create Consent first)",
                            hints=creds_hint)
            eu_id = p.get("end_user_id") or STATE.get("end_user_id")
            if not eu_id:
                return _err(
                    "end_user_id is required — it must match the identifier "
                    "used in Create Consent.",
                    hints=creds_hint,
                )
            pid = p.get("provider_id") or STATE.get("provider_id") or ""
            data, code = client.create_managed_flow(
                consent_id=str(cid),
                end_user_id=str(eu_id),
                language=p.get("language") or "en",
                provider_id=str(pid) if pid else "",
            )
            url = _extract_first(data, "flowUrl", "flow_url", "link")
            state_updates: dict[str, Any] = {}
            # Always surface the sandbox PSU credentials + docs link so users
            # can see what to log in with, even when the Aiia call fails
            # (e.g. a sandbox 403) and no flowUrl is returned.
            hints: dict[str, Any] = {"test_credentials": _test_credentials_payload()}
            if pid:
                state_updates["provider_id"] = str(pid)
            if url:
                state_updates["flow_url"] = url
                hints["open_link"] = url
                hints["open_link_label"] = "Launch Connect ↗"
                hints["open_link_note"] = (
                    "Open in a new tab, pick a bank, then log in with one of the "
                    "sandbox test users below. After SCA completes, run Get Consent "
                    "to confirm status before fetching accounts."
                )
            return _ok(data, code, state_updates, hints)

        if op_id == "get_consent":
            cid = p.get("consent_id") or STATE.get("consent_id")
            if not cid:
                return _err("consent_id is required")
            data, code = client.get_consent(str(cid))
            return _ok(data, code)

        if op_id == "revoke_consent":
            cid = p.get("consent_id") or STATE.get("consent_id")
            if not cid:
                return _err("consent_id is required")
            data, code = client.revoke_consent(str(cid))
            return _ok(data, code)

        if op_id == "get_accounts":
            cid = p.get("consent_id") or STATE.get("consent_id")
            if not cid:
                return _err("consent_id is required (run Create Consent first)")
            include = p.get("include") or "balances,holders,identifiers,additionalInformation"
            data, code = client.get_accounts(consent_id=str(cid), include=include)
            # Capture first account id when available.
            state_updates = {}
            if isinstance(data, dict):
                accounts = data.get("items") or data.get("accounts") or []
                if accounts and isinstance(accounts, list):
                    first = accounts[0] or {}
                    aid = _extract_first(first, "id", "accountId", "account_id")
                    if aid:
                        state_updates["account_id"] = aid
            return _ok(data, code, state_updates or None)

        if op_id == "get_account":
            aid = p.get("account_id") or STATE.get("account_id")
            cid = p.get("consent_id") or STATE.get("consent_id")
            if not aid:
                return _err("account_id is required (run Get Accounts first)")
            if not cid:
                return _err("consent_id is required")
            data, code = client.get_account(str(aid), consent_id=str(cid))
            return _ok(data, code)

        if op_id == "get_transactions":
            aid = p.get("account_id") or STATE.get("account_id")
            cid = p.get("consent_id") or STATE.get("consent_id")
            if not aid:
                return _err("account_id is required (run Get Accounts first)")
            if not cid:
                return _err("consent_id is required")
            try:
                limit = int(p.get("limit") or 50)
            except (TypeError, ValueError):
                limit = 50
            data, code = client.get_transactions(
                account_id=str(aid),
                consent_id=str(cid),
                from_date=p.get("from_date", ""),
                to_date=p.get("to_date", ""),
                limit=limit,
            )
            return _ok(data, code)

        if op_id == "check_balance":
            aid = p.get("account_id") or STATE.get("account_id")
            cid = p.get("consent_id") or STATE.get("consent_id")
            if not aid:
                return _err("account_id is required")
            if not cid:
                return _err("consent_id is required")
            data, code = client.check_balance(
                str(aid),
                consent_id=str(cid),
                max_age=str(p.get("max_age") or "PT15M"),
            )
            return _ok(data, code)

        if op_id == "verify_account_ownership":
            cid = p.get("consent_id") or STATE.get("consent_id")
            if not cid:
                return _err("consent_id is required")
            # Backwards-compat: older callers may still send ``expected_name``.
            name = (p.get("customer_name")
                    or p.get("expected_name")
                    or "").strip()
            if not name:
                return _err(
                    "customer_name is required \u2014 enter the full name to "
                    "compare against the consented account holder(s)."
                )
            raw_ids = p.get("account_ids") or p.get("account_id") or ""
            account_ids: list[str] = []
            if isinstance(raw_ids, list):
                account_ids = [str(x).strip() for x in raw_ids if str(x).strip()]
            elif isinstance(raw_ids, str) and raw_ids.strip():
                account_ids = [s.strip() for s in raw_ids.split(",") if s.strip()]
            data, code = client.verify_account_ownership(
                consent_id=str(cid),
                customer_name=name,
                account_ids=account_ids or None,
            )
            return _ok(data, code)

        return _err(f"Unknown operation: {op_id!r}", code=404)
    except Exception as exc:  # noqa: BLE001
        return _err(f"Open Finance EU error: {exc}", code=500)
