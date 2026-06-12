"""Open Finance Australia (Mastercard AU Open Banking) API module.

Exposes a MANIFEST describing the operations available, plus an `execute`
function that dispatches an operation against the underlying client.

This integration intentionally exposes the canonical Quick Start flow
(token → test customer → list customers / institutions → Connect URL →
accounts) as the smallest demonstration of an end-to-end AU CDR journey.
Additional endpoints can be added by mirroring the same operation/dispatch
pattern used by the larger US Open Finance module.
"""
from __future__ import annotations

import os
import time
from typing import Any, Dict, List, Optional

from .client import OpenFinanceAUClient


# ---------------------------------------------------------------------------
# Client (singleton)
# ---------------------------------------------------------------------------

_client: Optional[OpenFinanceAUClient] = None


def _get_client() -> Optional[OpenFinanceAUClient]:
    global _client
    from simulator.switcher import is_simulated
    if is_simulated("open_finance_au"):
        port = int(os.environ.get("PORT", 9021))
        sim_base = f"http://localhost:{port}/api-sim/open_finance_au"
        return OpenFinanceAUClient("sim_partner", "sim_secret", "sim_appkey", base_url=sim_base)
    if _client is not None:
        return _client
    pid = os.environ.get("OPEN_FINANCE_AU_PARTNER_ID", "")
    psec = os.environ.get("OPEN_FINANCE_AU_PARTNER_SECRET", "")
    akey = os.environ.get("OPEN_FINANCE_AU_APP_KEY", "")
    base = os.environ.get(
        "OPEN_FINANCE_AU_API_BASE_URL",
        "https://api.openbanking.mastercard.com.au",
    )
    if not (pid and psec and akey) or pid == "your_partner_id_here":
        return None
    _client = OpenFinanceAUClient(pid, psec, akey, base_url=base)
    return _client


def is_configured() -> bool:
    from simulator.switcher import is_simulated
    return is_simulated("open_finance_au") or _get_client() is not None


# ---------------------------------------------------------------------------
# Per-API state
# ---------------------------------------------------------------------------

STATE: Dict[str, Any] = {
    "customer_id": None,
    "customer_username": None,
    "institution_id": None,
    "consent_receipt_id": None,
    "connect_url": None,
}


# ---------------------------------------------------------------------------
# Sandbox test credentials (Mastercard Open Finance AU / CDR)
# ---------------------------------------------------------------------------
# Reference: https://developer.mastercard.com/open-finance-au/documentation/
#            integration-and-testing/test-the-apis/
# Three OAuth-enabled FinBank test institutions are available. Consumer
# profiles `profile_4110` – `profile_4115` (password == username) cover
# personal scenarios; business profiles `profile_4116` – `profile_4118`
# cover business banking. `profile_4110` is the most data-rich default.

TEST_USERS_DOCS_URL = (
    "https://developer.mastercard.com/open-finance-au/documentation/"
    "integration-and-testing/test-the-apis/"
)

TEST_USERS: List[Dict[str, Any]] = [
    {"username": "profile_4110", "password": "profile_4110",
     "kind": "Consumer",
     "scenario": "Default rich consumer profile (savings + transaction accounts)",
     "recommended": True},
    {"username": "profile_4111", "password": "profile_4111",
     "kind": "Consumer", "scenario": "Joint-account consumer profile"},
    {"username": "profile_4112", "password": "profile_4112",
     "kind": "Consumer", "scenario": "Loan + credit-card consumer profile"},
    {"username": "profile_4113", "password": "profile_4113",
     "kind": "Consumer", "scenario": "Single transaction-account consumer"},
    {"username": "profile_4114", "password": "profile_4114",
     "kind": "Consumer", "scenario": "Term-deposit + savings consumer"},
    {"username": "profile_4115", "password": "profile_4115",
     "kind": "Consumer", "scenario": "Multi-account high-balance consumer"},
    {"username": "profile_4116", "password": "profile_4116",
     "kind": "Business", "scenario": "Sole-trader business profile"},
    {"username": "profile_4117", "password": "profile_4117",
     "kind": "Business", "scenario": "Trust + business account profile"},
    {"username": "profile_4118", "password": "profile_4118",
     "kind": "Business", "scenario": "Company business profile (multi-entity)"},
]

TEST_PROVIDERS_NOTE = (
    "Pick one of the three OAuth FinBank sandbox institutions in Connect: "
    "Finbank Aus OAuth (200003), FinBank Aus B OAuth (2002119), or "
    "FinBank Outh Aus C (2002120). All three accept the profile credentials "
    "below and walk you through the CDR consent flow."
)


def _test_credentials_payload() -> Dict[str, Any]:
    """Compact representation of the AU CDR sandbox test profiles.

    Returned as a hint on Generate Connect URL so the UI can surface the
    profile usernames + the three test institutions next to the Launch
    Connect button. Emitted on both success and error responses so it
    stays visible while debugging sandbox issues.
    """
    return {
        "title": "AU CDR sandbox profiles (username = password for all)",
        "docs_url": TEST_USERS_DOCS_URL,
        "docs_label": "Mastercard Open Finance AU — Test Profiles docs",
        "providers_note": TEST_PROVIDERS_NOTE,
        "columns": ["Username", "Password", "Type", "Scenario"],
        "rows": [
            [u["username"], u["password"], u["kind"], u["scenario"]]
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

MANIFEST: Dict[str, Any] = {
    "id": "open_finance_au",
    "name": "Open Finance Australia",
    "description": (
        "Mastercard Open Finance Australia — CDR-compliant Open Banking APIs "
        "for accounts, transactions, consent, and decisioning."
    ),
    "how_to": (
        "<p><strong>Mastercard Open Finance Australia</strong> exposes the same Finicity-powered "
        "platform as US Open Finance, layered on the Australian Consumer Data Right (CDR) "
        "consent model. The basic Quick Start flow is:</p>"
        "<ol>"
        "<li><strong>Auth → Create Access Token</strong> — authenticates with your AU partner "
        "credentials. The token is cached automatically for all subsequent calls.</li>"
        "<li><strong>Customers → Add Testing Customer</strong> — creates a sandbox customer. Returns a "
        "<code>customerId</code> which is saved to state and reused by every operation below.</li>"
        "<li><strong>Institutions → Get Institutions</strong> — list AU-supported institutions "
        "(filtered by <code>supportedCountries=au</code> by default). Useful as a credential-only "
        "smoke test; no consent required.</li>"
        "<li><strong>Connect → Generate Connect URL</strong> — produces a "
        "<code>https://connect2.openbanking.mastercard.com.au/...</code> link. <strong>Open it in a "
        "new tab</strong>, search for <em>Finbank Aus OAuth</em>, and sign in with username "
        "<code>profile_4110</code> / password <code>profile_4110</code> to grant CDR consent.</li>"
        "<li><strong>Consent → Get Data Sharing Consents</strong> — <em>no webhook required.</em> "
        "Once you finish Connect, run this operation; it polls "
        "<code>GET /data-sharing-consents?customer_id=…&amp;status=ACTIVE</code> and auto-populates the "
        "<code>consentReceiptId</code> into state so the next call works one-click.</li>"
        "<li><strong>Accounts → Get Customer Accounts</strong> — uses the consent receipt from state to "
        "fetch the linked accounts.</li>"
        "</ol>"
        "<h3>Testing without a webhook</h3>"
        "<p>The AU CDR flow normally sends a notification to your callback URL when the customer "
        "grants consent. For local development you don’t need a public webhook — use the "
        "<strong>Get Data Sharing Consents</strong> operation to poll for the active consent record "
        "directly. The CDR consent receipt id is included in the response and saved to state.</p>"
        "<h3>Sandbox test values</h3>"
        "<ul>"
        "<li>Test institutions: <em>Finbank Aus OAuth</em> (200003), <em>FinBank Aus B OAuth</em> (2002119), <em>FinBank Outh Aus C</em> (2002120)</li>"
        "<li>Consumer profiles: <code>profile_4110</code> through <code>profile_4115</code> (password = username)</li>"
        "<li>Business profiles: <code>profile_4116</code> / <code>profile_4117</code> / <code>profile_4118</code></li>"
        "<li>Reference docs: "
        "<a href='https://developer.mastercard.com/open-finance-au/documentation/quick-start-guide/' target='_blank' rel='noopener'>"
        "Quick Start Guide</a> · "
        "<a href='https://developer.mastercard.com/open-finance-au/documentation/integration-and-testing/test-the-apis/' target='_blank' rel='noopener'>"
        "Test Profiles</a></li>"
        "</ul>"
        "<p><em>Tip:</em> the <strong>Create Access Token</strong> operation is the simplest live "
        "smoke test — it requires only your Partner ID, Partner Secret, and App Key, and does not "
        "need a customer or consent receipt.</p>"
    ),
    "docs_url": "https://developer.mastercard.com/open-finance-au/documentation/",
    "categories": [
        "Auth", "Customers", "Connect", "Consent (CDR)", "Accounts",
    ],
    "state_schema": [
        {"key": "customer_id", "label": "Customer ID"},
        {"key": "customer_username", "label": "Username"},
        {"key": "institution_id", "label": "Institution ID"},
        {"key": "consent_receipt_id", "label": "Consent Receipt ID"},
    ],
    "operations": [
        # ---- Auth ----
        {
            "id": "create_token",
            "name": "Create Access Token",
            "category": "Auth",
            "method": "POST",
            "description": (
                "Authenticate with your AU partner credentials. Token cached "
                "automatically for subsequent calls. Smoke-test operation: "
                "requires only Partner ID, Partner Secret, and App Key."
            ),
            "params": [],
            "requires": [],
            "produces": [],
        },
        # ---- Customers ----
        {
            "id": "add_testing_customer",
            "name": "Add Testing Customer",
            "category": "Customers",
            "method": "POST",
            "description": (
                "Enroll a sandbox testing customer (FinBank Aus profile). The AU "
                "sandbox requires firstName, lastName, email and phone — all four "
                "are sent automatically with safe defaults if you leave them blank."
            ),
            "params": [
                {"name": "username", "label": "Username", "type": "string",
                 "default": "CustomerUsername${timestamp}", "required": False,
                 "warning": "AU policy rejects usernames containing 'test'."},
                {"name": "first_name", "label": "First Name", "type": "string",
                 "default": "Alex", "required": False},
                {"name": "last_name", "label": "Last Name", "type": "string",
                 "default": "Smith", "required": False},
                {"name": "email", "label": "Email", "type": "string",
                 "default": "alex.smith@example.com", "required": False},
                {"name": "phone", "label": "Phone", "type": "string",
                 "default": "+61400000000", "required": False},
            ],
            "requires": [],
            "produces": ["customer_id", "customer_username"],
        },
        {
            "id": "list_customers",
            "name": "List Customers",
            "category": "Customers",
            "method": "GET",
            "description": "Search/list existing customers under this partner.",
            "params": [
                {"name": "search", "label": "Search", "type": "string",
                 "default": "", "required": False},
            ],
        },
        {
            "id": "get_customer",
            "name": "Get Customer by ID",
            "category": "Customers",
            "method": "GET",
            "description": "Retrieve a customer record by customer ID.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
            ],
            "requires": ["customer_id"],
        },
        {
            "id": "set_customer",
            "name": "Set Active Customer",
            "category": "Customers",
            "method": "LOCAL",
            "description": "Set the local active customer_id used as default for downstream operations (no API call). Useful when you already have a customer from a previous run.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
            ],
            "produces": ["customer_id"],
        },
        # ---- Institutions ----
        {
            "id": "get_institutions",
            "name": "Get Institutions",
            "category": "Connect",
            "method": "GET",
            "description": (
                "Search supported financial institutions. Filtered to AU by "
                "default. Does not require a consent receipt — good smoke test."
            ),
            "params": [
                {"name": "search", "label": "Search", "type": "string",
                 "default": "finbank", "required": False},
                {"name": "supported_countries", "label": "Supported Countries",
                 "type": "string", "default": "au", "required": False},
                {"name": "limit", "label": "Limit", "type": "number",
                 "default": 10, "required": False},
            ],
        },
        # ---- Connect ----
        {
            "id": "generate_connect_url",
            "name": "Generate Connect URL",
            "category": "Connect",
            "method": "POST",
            "description": (
                "Generate a Connect 2.0 URL the customer opens to link their "
                "bank and grant CDR consent. Open in a new tab and complete "
                "the FinBank Aus OAuth flow."
            ),
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "webhook_url", "label": "Webhook URL", "type": "string",
                 "default": "", "required": False},
            ],
            "requires": ["customer_id"],
            "produces": ["connect_url"],
            "ui_hint": "open_link",
        },
        # ---- Accounts ----
        {
            "id": "get_data_sharing_consents",
            "name": "Get Data Sharing Consents",
            "category": "Consent (CDR)",
            "method": "GET",
            "description": (
                "Poll for the customer's active CDR consents (no webhook required). "
                "Run this after completing the FinBank OAuth flow at the Connect URL — "
                "the consentReceiptId from the most recent ACTIVE consent is saved to state "
                "and reused by Get Customer Accounts."
            ),
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "status", "label": "Status", "type": "string",
                 "default": "ACTIVE", "required": False,
                 "warning": "ACTIVE | INACTIVE | DRAFT"},
            ],
            "requires": ["customer_id"],
            "produces": ["consent_receipt_id"],
        },
        {
            "id": "get_customer_accounts",
            "name": "Get Customer Accounts",
            "category": "Accounts",
            "method": "GET",
            "description": (
                "Retrieve all accounts owned by the given customer. Requires "
                "the Consent-Receipt-Id from the customer's CDR consent — run "
                "'Get Data Sharing Consents' first to populate it from state."
            ),
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "consent_receipt_id", "label": "Consent Receipt ID",
                 "type": "string", "source": "state:consent_receipt_id",
                 "required": True},
            ],
            "requires": ["customer_id", "consent_receipt_id"],
        },
    ],
}


# ---------------------------------------------------------------------------
# Dispatcher
# ---------------------------------------------------------------------------

def _err(msg: str, code: int = 400) -> Dict[str, Any]:
    return {"status": "error", "code": code, "data": {"error": msg},
            "state_updates": {}, "hints": {}}


def _ok(data: Any, code: int = 200, state_updates: Optional[Dict[str, Any]] = None,
        hints: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    # Mutate the module-level STATE so the UI's get_state() snapshot reflects
    # produced values on the next poll (in addition to returning them in the
    # envelope for any callers that read state_updates directly).
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
    """Return a UI-safe snapshot of state for the explorer state panel."""
    return {
        "customer_id": STATE.get("customer_id"),
        "customer_username": STATE.get("customer_username"),
        "institution_id": STATE.get("institution_id"),
        "consent_receipt_id": STATE.get("consent_receipt_id"),
        "connect_url": STATE.get("connect_url"),
    }


def execute(op_id: str, params: Dict[str, Any]) -> Dict[str, Any]:
    """Dispatch operation by id; returns {status, code, data, state_updates}."""
    p = params or {}

    # LOCAL operations don't need a client.
    if op_id == "set_customer":
        cid = p.get("customer_id")
        if not cid:
            return _err("customer_id is required")
        return _ok(
            {"message": f"Active customer set to {cid}", "customer_id": str(cid)},
            200,
            {"customer_id": str(cid)},
        )

    client = _get_client()
    if client is None:
        return _err(
            "Open Finance Australia is not configured. Provision via the auto-provisioning "
            "modal or run `./addapi.sh https://developer.mastercard.com/open-finance-au/documentation/` "
            "to obtain Partner ID / Partner Secret / App Key.",
            code=412,
        )

    try:
        if op_id == "create_token":
            data, code = client.create_token()
            return _ok(data, code)

        if op_id == "add_testing_customer":
            # AU username policy rejects anything containing the word "test"
            # (case-insensitive) — default to a non-triggering pattern.
            username = p.get("username") or f"CustomerUsername{int(time.time())}"
            if "${timestamp}" in str(username):
                username = str(username).replace("${timestamp}", str(int(time.time())))
            data, code = client.add_testing_customer(
                username=username,
                first_name=p.get("first_name") or "Alex",
                last_name=p.get("last_name") or "Smith",
                email=p.get("email") or "alex.smith@example.com",
                phone=p.get("phone") or "+61400000000",
            )
            state: Dict[str, Any] = {}
            if isinstance(data, dict) and data.get("id"):
                state["customer_id"] = str(data["id"])
                state["customer_username"] = data.get("username") or username
            return _ok(data, code, state)

        if op_id == "list_customers":
            data, code = client.get_customers(search=p.get("search", ""))
            return _ok(data, code)

        if op_id == "get_customer":
            cid = p.get("customer_id") or STATE.get("customer_id")
            if not cid:
                return _err("customer_id is required (run Add Testing Customer first)")
            data, code = client.get_customer(str(cid))
            return _ok(data, code)

        if op_id == "get_institutions":
            try:
                limit = int(p.get("limit") or 10)
            except (TypeError, ValueError):
                limit = 10
            data, code = client.get_institutions(
                search=p.get("search", ""),
                limit=limit,
                supported_countries=p.get("supported_countries") or "au",
            )
            return _ok(data, code)

        if op_id == "generate_connect_url":
            cid = p.get("customer_id") or STATE.get("customer_id")
            if not cid:
                return _err("customer_id is required (run Add Testing Customer first)")
            data, code = client.generate_connect_url(
                customer_id=str(cid),
                webhook_url=p.get("webhook_url", ""),
            )
            state = {}
            hints: Dict[str, Any] = {"test_credentials": _test_credentials_payload()}
            if isinstance(data, dict) and data.get("link"):
                state["connect_url"] = data["link"]
                hints["open_link"] = data["link"]
                hints["open_link_label"] = "Launch Connect ↗"
                hints["open_link_note"] = (
                    "Open in a new tab, search for one of the FinBank Aus OAuth "
                    "institutions, then sign in with one of the sandbox profiles below."
                )
            return _ok(data, code, state, hints)

        if op_id == "get_data_sharing_consents":
            cid = p.get("customer_id") or STATE.get("customer_id")
            if not cid:
                return _err("customer_id is required (run Add Testing Customer first)")
            data, code = client.get_data_sharing_consents(
                customer_id=str(cid),
                status=(p.get("status") or "ACTIVE").upper(),
            )
            # The AU response shape is { "consentReceipts": [...] } or { "consents": [...] }
            # depending on API version — handle both and pull the newest receipt id.
            state = {}
            if isinstance(data, dict):
                records = (
                    data.get("consentReceipts")
                    or data.get("consents")
                    or data.get("dataSharingConsents")
                    or []
                )
                if records and isinstance(records, list):
                    first = records[0] or {}
                    rid = (
                        first.get("consentReceiptId")
                        or first.get("consent_receipt_id")
                        or first.get("id")
                    )
                    if rid:
                        state["consent_receipt_id"] = str(rid)
            return _ok(data, code, state)

        if op_id == "get_customer_accounts":
            cid = p.get("customer_id") or STATE.get("customer_id")
            consent = p.get("consent_receipt_id") or STATE.get("consent_receipt_id")
            if not cid:
                return _err("customer_id is required (run Add Testing Customer first)")
            if not consent:
                return _err(
                    "consent_receipt_id is required — complete the Connect flow, then run "
                    "'Get Data Sharing Consents' to auto-populate it (no webhook needed)."
                )
            data, code = client.get_customer_accounts(
                customer_id=str(cid),
                consent_receipt_id=str(consent),
            )
            return _ok(data, code)

        return _err(f"Unknown operation: {op_id!r}", code=404)
    except Exception as exc:  # noqa: BLE001 — surface upstream errors to UI
        return _err(f"Open Finance AU error: {exc}", code=500)
