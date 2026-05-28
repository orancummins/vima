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
from typing import Any, Dict, Optional

from .client import OpenFinanceEUClient


# ---------------------------------------------------------------------------
# Client (singleton)
# ---------------------------------------------------------------------------

_client: Optional[OpenFinanceEUClient] = None


def _get_client() -> Optional[OpenFinanceEUClient]:
    global _client
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
    if _client is not None:
        return _client
    cid = os.environ.get("OPEN_FINANCE_EU_CLIENT_ID", "")
    pkey = os.environ.get("OPEN_FINANCE_EU_PRIVATE_KEY_PATH", "")
    pcert = os.environ.get("OPEN_FINANCE_EU_PUBLIC_CERT_PATH", "")
    auth_base = os.environ.get(
        "OPEN_FINANCE_EU_AUTH_BASE_URL",
        OpenFinanceEUClient.DEFAULT_AUTH_BASE,
    )
    api_base = os.environ.get(
        "OPEN_FINANCE_EU_API_BASE_URL",
        OpenFinanceEUClient.DEFAULT_API_BASE,
    )
    if not (cid and pkey and pcert) or cid == "your_client_id_here":
        return None
    _client = OpenFinanceEUClient(
        client_id=cid,
        private_key_path=pkey,
        public_cert_path=pcert,
        auth_base_url=auth_base,
        api_base_url=api_base,
    )
    return _client


def is_configured() -> bool:
    from simulator.switcher import is_simulated
    return is_simulated("open_finance_eu") or _get_client() is not None


# ---------------------------------------------------------------------------
# Per-API state
# ---------------------------------------------------------------------------

STATE: Dict[str, Any] = {
    "provider_id": None,
    "consent_id": None,
    "flow_url": None,
    "account_id": None,
}


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------

MANIFEST: Dict[str, Any] = {
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
        "<li>Test bank: Aiia provides a simulated ASPSP in the MTF environment "
        "with example users and account data.</li>"
        "<li>Docs: "
        "<a href='https://developer.mastercard.com/open-finance-data/documentation/' "
        "target='_blank' rel='noopener'>Open Finance Data</a> · "
        "<a href='https://developer.mastercard.com/open-finance-data/documentation/developer-support/api-basics/authentication/' "
        "target='_blank' rel='noopener'>Authentication</a></li>"
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
                "Create a data-sharing consent for the chosen provider. Returns "
                "a consent_id which is saved to state."
            ),
            "params": [
                {"name": "provider_id", "label": "Provider ID", "type": "string",
                 "source": "state:provider_id", "required": True},
                {"name": "redirect_url", "label": "Redirect URL", "type": "string",
                 "default": "", "required": False,
                 "warning": "Where the user is sent after completing bank SCA."},
            ],
            "requires": ["provider_id"],
            "produces": ["consent_id"],
        },
        {
            "id": "create_managed_flow",
            "name": "Create Managed Flow",
            "category": "Consent",
            "method": "POST",
            "description": (
                "Generate the hosted Aiia Flow URL the customer opens to grant "
                "consent at their bank. Replaces the AU Connect URL step."
            ),
            "params": [
                {"name": "consent_id", "label": "Consent ID", "type": "string",
                 "source": "state:consent_id", "required": True},
                {"name": "redirect_url", "label": "Redirect URL", "type": "string",
                 "default": "", "required": False},
                {"name": "language", "label": "Language", "type": "string",
                 "default": "en", "required": False},
            ],
            "requires": ["consent_id"],
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
                "List accounts visible under the active consent. Saves the first "
                "account_id to state for downstream operations."
            ),
            "params": [
                {"name": "consent_id", "label": "Consent ID", "type": "string",
                 "source": "state:consent_id", "required": False},
            ],
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
                "checks immediately before initiating a payment."
            ),
            "params": [
                {"name": "account_id", "label": "Account ID", "type": "string",
                 "source": "state:account_id", "required": True},
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
                "compares the consented account holder to an expected name."
            ),
            "params": [
                {"name": "account_id", "label": "Account ID", "type": "string",
                 "source": "state:account_id", "required": True},
                {"name": "expected_name", "label": "Expected Name",
                 "type": "string", "default": "", "required": False},
            ],
            "requires": ["account_id"],
        },
    ],
}


# ---------------------------------------------------------------------------
# Dispatcher
# ---------------------------------------------------------------------------

def _err(msg: str, code: int = 400) -> Dict[str, Any]:
    return {"status": "error", "code": code, "data": {"error": msg},
            "state_updates": {}, "hints": {}}


def _ok(data: Any, code: int = 200,
        state_updates: Optional[Dict[str, Any]] = None,
        hints: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
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


def get_state() -> Dict[str, Any]:
    return {
        "provider_id": STATE.get("provider_id"),
        "consent_id": STATE.get("consent_id"),
        "account_id": STATE.get("account_id"),
        "flow_url": STATE.get("flow_url"),
    }


def _extract_first(data: Any, *keys: str) -> Optional[str]:
    """Defensive lookup — the Aiia response shape uses both camelCase and
    snake_case across versions; try the listed keys in order."""
    if not isinstance(data, dict):
        return None
    for k in keys:
        v = data.get(k)
        if v:
            return str(v)
    return None


def execute(op_id: str, params: Dict[str, Any]) -> Dict[str, Any]:
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
            return _ok(data, code)

        if op_id == "create_consent":
            pid = p.get("provider_id") or STATE.get("provider_id")
            if not pid:
                return _err("provider_id is required (run Get Providers first)")
            data, code = client.create_consent(
                provider_id=str(pid),
                redirect_url=p.get("redirect_url", ""),
            )
            cid = _extract_first(data, "consent_id", "consentId", "id")
            return _ok(data, code, {"consent_id": cid} if cid else None)

        if op_id == "create_managed_flow":
            cid = p.get("consent_id") or STATE.get("consent_id")
            if not cid:
                return _err("consent_id is required (run Create Consent first)")
            data, code = client.create_managed_flow(
                consent_id=str(cid),
                redirect_url=p.get("redirect_url", ""),
                language=p.get("language") or "en",
            )
            url = _extract_first(data, "flow_url", "url", "redirect_url")
            state_updates: Dict[str, Any] = {}
            hints: Dict[str, Any] = {}
            if url:
                state_updates["flow_url"] = url
                hints["open_link"] = url
                hints["open_link_label"] = "Launch Aiia Flow ↗"
                hints["open_link_note"] = (
                    "Open in a new tab, complete the bank SCA, then run "
                    "Get Consent to confirm status."
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
            data, code = client.get_accounts(consent_id=cid)
            # Capture first account id when available.
            state_updates = {}
            if isinstance(data, dict):
                accounts = data.get("accounts") or data.get("items") or []
                if accounts and isinstance(accounts, list):
                    first = accounts[0] or {}
                    aid = _extract_first(first, "account_id", "id", "accountId")
                    if aid:
                        state_updates["account_id"] = aid
            return _ok(data, code, state_updates or None)

        if op_id == "get_account":
            aid = p.get("account_id") or STATE.get("account_id")
            if not aid:
                return _err("account_id is required (run Get Accounts first)")
            data, code = client.get_account(str(aid))
            return _ok(data, code)

        if op_id == "get_transactions":
            aid = p.get("account_id") or STATE.get("account_id")
            if not aid:
                return _err("account_id is required (run Get Accounts first)")
            try:
                limit = int(p.get("limit") or 50)
            except (TypeError, ValueError):
                limit = 50
            data, code = client.get_transactions(
                account_id=str(aid),
                from_date=p.get("from_date", ""),
                to_date=p.get("to_date", ""),
                limit=limit,
            )
            return _ok(data, code)

        if op_id == "check_balance":
            aid = p.get("account_id") or STATE.get("account_id")
            if not aid:
                return _err("account_id is required")
            data, code = client.check_balance(str(aid))
            return _ok(data, code)

        if op_id == "verify_account_ownership":
            aid = p.get("account_id") or STATE.get("account_id")
            if not aid:
                return _err("account_id is required")
            data, code = client.verify_account_ownership(
                account_id=str(aid),
                expected_name=p.get("expected_name", ""),
            )
            return _ok(data, code)

        return _err(f"Unknown operation: {op_id!r}", code=404)
    except Exception as exc:  # noqa: BLE001
        return _err(f"Open Finance EU error: {exc}", code=500)
