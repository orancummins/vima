"""Open Finance (Mastercard / Finicity US Open Banking) API module.

Exposes a MANIFEST describing the operations available, plus an `execute`
function that dispatches an operation against the underlying client.
"""
from __future__ import annotations

import os
import time
from typing import Any, Dict, List, Optional, Tuple

from .client import OpenFinanceClient


# ---------------------------------------------------------------------------
# Client (singleton)
# ---------------------------------------------------------------------------

_client: Optional[OpenFinanceClient] = None


def _get_client() -> Optional[OpenFinanceClient]:
    global _client
    from simulator.switcher import is_simulated
    if is_simulated("ofin"):
        port = int(os.environ.get("PORT", 9021))
        sim_base = f"http://localhost:{port}/api-sim/ofin"
        return OpenFinanceClient("sim_partner", "sim_secret", "sim_appkey", base_url=sim_base)
    if _client is not None:
        return _client
    pid = os.environ.get("PARTNER_ID", "")
    psec = os.environ.get("PARTNER_SECRET", "")
    akey = os.environ.get("APP_KEY", "")
    base = os.environ.get("API_BASE_URL", "https://api.finicity.com")
    if not (pid and psec and akey) or pid == "your_partner_id_here":
        return None
    _client = OpenFinanceClient(pid, psec, akey, base_url=base)
    return _client


def is_configured() -> bool:
    from simulator.switcher import is_simulated
    return is_simulated("ofin") or _get_client() is not None


# ---------------------------------------------------------------------------
# Per-API state
# ---------------------------------------------------------------------------
# Single-user demo state. Keys produced by one operation are pre-filled into
# the inputs of dependent operations in the UI.
STATE: Dict[str, Any] = {
    "customer_id": None,
    "customer_username": None,
    "consumer_id": None,
    "account_id": None,
    "report_id": None,
    "micro_account_id": None,
    "accounts": [],
}


# ---------------------------------------------------------------------------
# Operation manifest
# ---------------------------------------------------------------------------
# Each operation has:
#   id, name, category, description
#   method (HTTP verb hint for UI)
#   params: [{name, label, type, default, required, source}]
#       source: "state:<key>" auto-fills from STATE; "auto:timestamp" generates
#   requires: state keys that must be set
#   produces: state keys that this op will populate
#   ui_hint: optional hint, e.g., "open_link" if response contains a link


MANIFEST: Dict[str, Any] = {
    "id": "ofin",
    "name": "Open Finance",
    "description": (
        "Mastercard Open Finance (US Open Banking) — Finicity-powered "
        "account, transaction, and decisioning APIs."
    ),
    "how_to": (
        "<p><strong>Mastercard Open Finance</strong> (Finicity) lets you link a customer\u2019s bank "
        "accounts, read their data, run verification reports, assess payment risk, and subscribe to "
        "real-time transaction webhooks \u2014 all against the Finicity sandbox.</p>"
        "<h3>Quick-start \u2014 link accounts</h3>"
        "<ol>"
        "<li><strong>Auth \u2192 Create Access Token</strong> \u2014 authenticates with your partner credentials. "
        "The token is cached automatically for all subsequent calls.</li>"
        "<li><strong>Customers \u2192 Create Testing Customer</strong> \u2014 creates a sandbox customer and saves "
        "their <code>customer_id</code> to state. Or use <em>List Customers</em> to find an existing one.</li>"
        "<li><strong>Data Connect \u2192 Generate Data Connect URL</strong> \u2014 opens the Finicity bank-linking "
        "flow in a new tab. In sandbox, complete the FinBank flow with any username and password. "
        "This links test accounts to your customer.</li>"
        "<li><strong>Accounts \u2192 Refresh Accounts</strong>, then <strong>Get Accounts</strong> \u2014 lists "
        "linked accounts. Click a row to set the active <code>account_id</code>.</li>"
        "<li><strong>Transactions \u2192 Get Account Transactions</strong> \u2014 pulls raw transactions for the "
        "selected account.</li>"
        "</ol>"
        "<h3>Reports</h3>"
        "<ol>"
        "<li><strong>Reports \u2192 Ensure Consumer Record</strong> \u2014 creates the PII record required before "
        "any regulated report.</li>"
        "<li>Run any <strong>Generate \u2026 Report</strong> (VOA, VOI, Cash Flow, VOAI, etc.). "
        "A <code>report_id</code> is saved to state.</li>"
        "<li><strong>Reports \u2192 Get Report by ID</strong> \u2014 poll until <code>status</code> changes from "
        "<code>inProgress</code> to <code>success</code>, then inspect the full payload.</li>"
        "</ol>"
        "<h3>Payment Success Indicators</h3>"
        "<ol>"
        "<li>Ensure you have a <code>customer_id</code> and <code>account_id</code> in state.</li>"
        "<li><strong>Payments \u2192 Generate Payment Success Indicators</strong> \u2014 returns a non-FCRA risk "
        "score for a given payment amount.</li>"
        "<li><strong>Payments \u2192 Generate FCRA PSI</strong> \u2014 the FCRA-regulated variant. Requires purpose "
        "code <code>1P</code> and an email on the customer record.</li>"
        "</ol>"
        "<h3>TxPush \u2014 real-time webhooks</h3>"
        "<ol>"
        "<li>Run <code>ngrok http 9021</code> in a separate terminal to get a public HTTPS URL.</li>"
        "<li><strong>TxPush \u2192 Subscribe to TxPush</strong> \u2014 paste "
        "<code>https://\u2026.ngrok-free.app/txpush-listener</code> as the callback URL. "
        "Finicity validates it immediately on subscribe.</li>"
        "<li>Use <em>Fire TxPush Test</em> to trigger a test event; view received events at "
        "<a href='/txpush-events' target='_blank'>/txpush-events</a>.</li>"
        "<li><strong>TxPush \u2192 Disable TxPush</strong> when finished.</li>"
        "</ol>"
        "<h3>Micro Entries \u2014 account verification</h3>"
        "<ol>"
        "<li><strong>Micro Entries \u2192 Initiate Micro Entries</strong> \u2014 sandbox: routing "
        "<code>011000138</code>, account <code>5111111111</code>.</li>"
        "<li><strong>Micro Entries \u2192 Verify Micro Entries</strong> \u2014 confirm the two amounts "
        "(always <code>0.01</code> and <code>0.02</code> in sandbox). AVA Account ID auto-fills.</li>"
        "</ol>"
        "<h3>Tips</h3>"
        "<ul>"
        "<li>The <strong>state bar</strong> shows acquired IDs, updated automatically after each successful call.</li>"
        "<li>The <strong>Request</strong> panel shows the exact payload sent \u2014 ready to copy into curl or Postman.</li>"
        "<li>Re-selecting an operation restores its last request/response without a new API call.</li>"
        "</ul>"
    ),
    "docs_url": "https://developer.mastercard.com/open-finance-us/documentation/",
    "categories": [
        "Auth", "Customers", "Data Connect", "Accounts",
        "Transactions", "Institutions", "Reports", "Payments", "Micro Entries",
        "Business", "TxPush", "Transfer", "Data Enrichment",
    ],
    "state_schema": [
        {"key": "customer_id", "label": "Customer ID"},
        {"key": "customer_username", "label": "Username"},
        {"key": "consumer_id", "label": "Consumer ID"},
        {"key": "report_id", "label": "Last Report ID"},
        {"key": "account_id", "label": "Account ID (selected)"},
        {"key": "micro_account_id", "label": "Micro Entry Account ID"},
    ],
    "operations": [
        # ---- Auth ----
        {
            "id": "create_token",
            "name": "Create Access Token",
            "category": "Auth",
            "method": "POST",
            "description": "Authenticate with partner credentials. Token cached automatically for subsequent calls.",
            "params": [],
            "requires": [],
            "produces": [],
        },

        # ---- Customers ----
        {
            "id": "create_test_customer",
            "name": "Create Testing Customer",
            "category": "Customers",
            "method": "POST",
            "description": "Create a new sandbox testing customer in FinBank. Most other calls require a customer_id.",
            "params": [
                {"name": "username", "label": "Username", "type": "string",
                 "default": "test_user_${timestamp}", "required": False},
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
            "id": "delete_customer",
            "name": "Delete Customer Access",
            "category": "Customers",
            "method": "DELETE",
            "description": "Remove access to a customer and all associated accounts. Data is retained per retention policy.",
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
            "description": "Set the local active customer_id used as default for downstream operations (no API call).",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
            ],
            "produces": ["customer_id"],
        },
        {
            "id": "get_consumer_by_id",
            "name": "Get Consumer by ID",
            "category": "Customers",
            "method": "GET",
            "description": "Get consumer record details by consumer ID. Auto-filled after running Get Consumer Details, Ensure Consumer Record, or Create Consumer.",
            "params": [
                {"name": "consumer_id", "label": "Consumer ID", "type": "string",
                 "source": "state:consumer_id", "required": True,
                 "warning": "Run \"Get Consumer Details\" first to populate this field"},
            ],
        },
        {
            "id": "get_customer_consumer",
            "name": "Get Consumer Details",
            "category": "Customers",
            "method": "GET",
            "description": "Get the consumer (PII) record attached to a customer. Returns 404 if no consumer record has been created — run 'Ensure Consumer Record' (under Reports) or generate any report first to create one.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
            ],
            "requires": ["customer_id"],
        },

        # ---- Data Connect ----
        {
            "id": "generate_connect_url",
            "name": "Generate Data Connect URL",
            "category": "Data Connect",
            "method": "POST",
            "description": "Generate a URL the customer opens to link their bank. Open in a new tab and complete the FinBank flow, then refresh accounts.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
            ],
            "requires": ["customer_id"],
            "ui_hint": "open_link",
        },
        {
            "id": "generate_lite_connect_url",
            "name": "Data Connect Lite URL",
            "category": "Data Connect",
            "method": "POST",
            "description": "Lite version of Data Connect — sign-in and MFA only, no account management. Requires an institution ID.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "institution_id", "label": "Institution ID", "type": "string",
                 "default": "102105", "required": True},
            ],
            "requires": ["customer_id"],
            "ui_hint": "open_link",
        },
        {
            "id": "generate_fix_connect_url",
            "name": "Data Connect Fix URL",
            "category": "Data Connect",
            "method": "POST",
            "description": "Re-engage a customer to fix a broken institution connection (lost credentials, MFA expiry). Requires institutionLoginId.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "institution_login_id", "label": "Institution Login ID", "type": "string",
                 "default": "", "required": True},
            ],
            "requires": ["customer_id"],
            "ui_hint": "open_link",
        },

        # ---- Accounts ----
        {
            "id": "refresh_accounts",
            "name": "Refresh Accounts",
            "category": "Accounts",
            "method": "POST",
            "description": "Refresh all linked accounts for the customer. Populates state with account list.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
            ],
            "requires": ["customer_id"],
            "produces": ["accounts", "account_id"],
        },
        {
            "id": "get_accounts",
            "name": "Get Accounts",
            "category": "Accounts",
            "method": "GET",
            "description": "Get all accounts linked to a customer (no refresh).",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
            ],
            "requires": ["customer_id"],
            "produces": ["accounts", "account_id"],
        },
        {
            "id": "get_account",
            "name": "Get Account",
            "category": "Accounts",
            "method": "GET",
            "description": "Fetch a single account.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "account_id", "label": "Account", "type": "account_select",
                 "source": "state:account_id", "required": True},
            ],
            "requires": ["customer_id", "account_id"],
        },
        {
            "id": "get_account_balance",
            "name": "Get Live Available Balance",
            "category": "Accounts",
            "method": "GET",
            "description": "Get real-time available balance for an account.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "account_id", "label": "Account", "type": "account_select",
                 "source": "state:account_id", "required": True},
            ],
            "requires": ["customer_id", "account_id"],
        },
        {
            "id": "get_account_owner",
            "name": "Get Account Owner",
            "category": "Accounts",
            "method": "GET",
            "description": "Get owner / KYC info for an account.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "account_id", "label": "Account", "type": "account_select",
                 "source": "state:account_id", "required": True},
            ],
            "requires": ["customer_id", "account_id"],
        },
        {
            "id": "get_account_payment_details",
            "name": "Get ACH/Payment Details",
            "category": "Accounts",
            "method": "GET",
            "description": "Get ACH routing + RTP/FedNow eligibility for an account (v3).",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "account_id", "label": "Account", "type": "account_select",
                 "source": "state:account_id", "required": True},
            ],
            "requires": ["customer_id", "account_id"],
        },
        {
            "id": "get_ach_details",
            "name": "Get ACH Details (Basic)",
            "category": "Accounts",
            "method": "GET",
            "description": "Get real account number and routing number for ACH payment (v1).",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "account_id", "label": "Account", "type": "account_select",
                 "source": "state:account_id", "required": True},
            ],
            "requires": ["customer_id", "account_id"],
        },
        {
            "id": "get_account_owner_details",
            "name": "Get Account Owner Details (v3)",
            "category": "Accounts",
            "method": "GET",
            "description": "Enhanced owner data: addresses, emails, phones, documentations, identity insights.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "account_id", "label": "Account", "type": "account_select",
                 "source": "state:account_id", "required": True},
            ],
            "requires": ["customer_id", "account_id"],
        },
        {
            "id": "get_account_statement",
            "name": "Get Account Statement",
            "category": "Accounts",
            "method": "GET",
            "description": "Download account statement (PDF) for the given index (1 = most recent, up to 24).",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "account_id", "label": "Account", "type": "account_select",
                 "source": "state:account_id", "required": True},
                {"name": "index", "label": "Statement Index", "type": "number",
                 "default": "1", "required": False},
            ],
            "requires": ["customer_id", "account_id"],
        },
        {
            "id": "load_historic_transactions",
            "name": "Load Historic Transactions",
            "category": "Accounts",
            "method": "POST",
            "description": "Trigger a background refresh of up to 24 months of historic transactions for an account. Returns 204 No Content on success — run \"Get Account Transactions\" after 30-60 seconds to see the data.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "account_id", "label": "Account", "type": "account_select",
                 "source": "state:account_id", "required": True},
            ],
            "requires": ["customer_id", "account_id"],
        },
        {
            "id": "get_loan_payment_details",
            "name": "Get Loan Payment Details",
            "category": "Accounts",
            "method": "GET",
            "description": (
                "Return loan payment details for a studentLoan-type account. "
                "IMPORTANT: This endpoint only works with student loan accounts — "
                "auto, mortgage, and personal loan accounts will return a 404. "
                "To test this, connect a student loan institution in the sandbox "
                "(e.g. FinBank Student Loans, institution ID 102224) and select "
                "the resulting studentLoan account from the dropdown."
            ),
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "account_id", "label": "Account", "type": "account_select",
                 "source": "state:account_id", "required": True},
            ],
            "requires": ["customer_id", "account_id"],
        },
        {
            "id": "delete_customer_account",
            "name": "Delete Account Access",
            "category": "Accounts",
            "method": "DELETE",
            "description": "Remove access to a specific linked account. Data is retained per retention policy.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "account_id", "label": "Account", "type": "account_select",
                 "source": "state:account_id", "required": True},
            ],
            "requires": ["customer_id", "account_id"],
        },
        {
            "id": "account_owner_match",
            "name": "Account Owner Match",
            "category": "Accounts",
            "method": "POST",
            "description": "Compare provided name/address/email/phone against FI account holder data. Returns confidence scores 0–100. The sandbox account owner is JOHN DOE.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "account_id", "label": "Account", "type": "account_select",
                 "source": "state:account_id", "required": True},
                {"name": "first_name", "label": "First Name", "type": "string",
                 "default": "JOHN", "required": True},
                {"name": "last_name", "label": "Last Name", "type": "string",
                 "default": "DOE", "required": True},
                {"name": "email", "label": "Email", "type": "string",
                 "default": "", "required": False},
                {"name": "phone", "label": "Phone", "type": "string",
                 "default": "", "required": False},
            ],
            "requires": ["customer_id", "account_id"],
        },

        # ---- Transactions ----
        {
            "id": "get_transactions",
            "name": "Get Customer Transactions",
            "category": "Transactions",
            "method": "GET",
            "description": "Get transactions for the customer over the past N days.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "days", "label": "Days back", "type": "number",
                 "default": "90", "required": False},
            ],
            "requires": ["customer_id"],
        },
        {
            "id": "get_account_transactions",
            "name": "Get Account Transactions",
            "category": "Transactions",
            "method": "GET",
            "description": "Get transactions for a single account.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "account_id", "label": "Account", "type": "account_select",
                 "source": "state:account_id", "required": True},
                {"name": "days", "label": "Days back", "type": "number",
                 "default": "90", "required": False},
            ],
            "requires": ["customer_id", "account_id"],
        },
        {
            "id": "get_recurring_transactions",
            "name": "Get Recurring Transactions",
            "category": "Transactions",
            "method": "POST",
            "description": "Detect recurring transactions for the customer.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
            ],
            "requires": ["customer_id"],
        },

        # ---- Institutions ----
        {
            "id": "search_institutions",
            "name": "Search Institutions",
            "category": "Institutions",
            "method": "GET",
            "description": "Search supported financial institutions.",
            "params": [
                {"name": "search", "label": "Search", "type": "string",
                 "default": "finbank", "required": False},
            ],
        },
        {
            "id": "get_institution",
            "name": "Get Institution",
            "category": "Institutions",
            "method": "GET",
            "description": "Get institution details by ID.",
            "params": [
                {"name": "institution_id", "label": "Institution ID",
                 "type": "string", "default": "102105", "required": True},
            ],
        },
        {
            "id": "get_certified_institutions",
            "name": "Get Certified Institutions",
            "category": "Institutions",
            "method": "GET",
            "description": "Search institutions certified for specific product types (VOA, VOI, ACH, etc.).",
            "params": [
                {"name": "search", "label": "Search", "type": "string",
                 "default": "finbank", "required": False},
            ],
        },
        {
            "id": "get_institution_by_routing",
            "name": "Search by Routing Number",
            "category": "Institutions",
            "method": "GET",
            "description": "Find a financial institution by its ABA routing number.",
            "params": [
                {"name": "routing_number", "label": "Routing Number", "type": "string",
                 "default": "021000021", "required": True},
            ],
        },
        {
            "id": "get_institution_branding",
            "name": "Get Institution Branding",
            "category": "Institutions",
            "method": "GET",
            "description": "Get branding assets (SVG logos) for a financial institution.",
            "params": [
                {"name": "institution_id", "label": "Institution ID", "type": "string",
                 "default": "102105", "required": True},
            ],
        },

        # ---- Reports ----
        {
            "id": "ensure_consumer",
            "name": "Ensure Consumer Record",
            "category": "Reports",
            "method": "POST",
            "description": "Create a test consumer record for the customer if missing. Required before report generation.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
            ],
            "requires": ["customer_id"],
        },
        {
            "id": "generate_voa",
            "name": "Generate VOA Report",
            "category": "Reports",
            "method": "POST",
            "description": "Verification of Assets. Auto-creates consumer record if needed.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
            ],
            "requires": ["customer_id"],
        },
        {
            "id": "generate_voi",
            "name": "Generate VOI Report",
            "category": "Reports",
            "method": "POST",
            "description": "Verification of Income. Auto-creates consumer record if needed.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
            ],
            "requires": ["customer_id"],
        },
        {
            "id": "generate_cashflow",
            "name": "Generate Cash Flow Report",
            "category": "Reports",
            "method": "POST",
            "description": "Personal cash flow report.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
            ],
            "requires": ["customer_id"],
        },
        {
            "id": "generate_balance_analytics",
            "name": "Generate Balance Analytics",
            "category": "Reports",
            "method": "POST",
            "description": "Balance analytics report.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
            ],
            "requires": ["customer_id"],
        },
        {
            "id": "generate_voai",
            "name": "Generate VOAI Report",
            "category": "Reports",
            "method": "POST",
            "description": "Verification of Assets with Income — up to 24 months of transaction history.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
            ],
            "requires": ["customer_id"],
        },
        {
            "id": "generate_cashflow_business",
            "name": "Generate Cash Flow Report (Business)",
            "category": "Reports",
            "method": "POST",
            "description": "Cash Flow Report for business use. No consumer record required.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
            ],
            "requires": ["customer_id"],
        },
        {
            "id": "generate_cashflow_analytics",
            "name": "Generate Cash Flow Analytics",
            "category": "Reports",
            "method": "POST",
            "description": "Cash Flow Analytics report — risk metrics and behavioral insights from transaction data.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
            ],
            "requires": ["customer_id"],
        },
        {
            "id": "generate_transactions_report",
            "name": "Generate Transactions Report",
            "category": "Reports",
            "method": "POST",
            "description": "Generate a Transactions Report for a date range (max 24 months). Consumer required.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "days", "label": "Days back", "type": "number",
                 "default": "90", "required": False},
            ],
            "requires": ["customer_id"],
        },
        {
            "id": "get_report_by_id",
            "name": "Get Report by ID",
            "category": "Reports",
            "method": "POST",
            "description": "Fetch a previously generated report by its report ID. Auto-filled after any Generate report call. Poll until status changes from 'inProgress' to 'success'.",
            "params": [
                {"name": "report_id", "label": "Report ID", "type": "string",
                 "source": "state:report_id", "required": True},
                {"name": "purpose_code", "label": "Purpose Code", "type": "select",
                 "options": ["3F", "3G", "3H", "12F", "13F"],
                 "default": "3F", "required": True,
                 "hint": "FCRA 2-digit Permissible Purpose Code. 3F = Credit Transaction (most common for testing)"},
            ],
        },
        {
            "id": "list_reports",
            "name": "List Reports",
            "category": "Reports",
            "method": "GET",
            "description": "List all reports generated for a customer.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
            ],
            "requires": ["customer_id"],
        },
        {
            "id": "get_report_by_customer",
            "name": "Get Report by Customer",
            "category": "Reports",
            "method": "GET",
            "description": "Fetch a specific report by both customer ID and report ID.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "report_id", "label": "Report ID", "type": "string",
                 "source": "state:report_id", "required": True},
                {"name": "purpose_code", "label": "Purpose Code", "type": "select",
                 "options": ["3F", "3G", "3H", "12F", "13F"],
                 "default": "3F", "required": True,
                 "hint": "FCRA 2-digit Permissible Purpose Code. 3F = Credit Transaction"},
            ],
            "requires": ["customer_id"],
        },
        {
            "id": "create_consumer",
            "name": "Create Consumer",
            "category": "Reports",
            "method": "POST",
            "description": "Create a full consumer record with PII. Required before CRA report generation.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "first_name", "label": "First Name", "type": "string",
                 "default": "John", "required": True},
                {"name": "last_name", "label": "Last Name", "type": "string",
                 "default": "Smith", "required": True},
                {"name": "email", "label": "Email", "type": "string",
                 "default": "john.smith@example.com", "required": True},
                {"name": "phone", "label": "Phone", "type": "string",
                 "default": "5558001234", "required": False},
                {"name": "ssn", "label": "SSN (optional)", "type": "string",
                 "default": "", "required": False},
            ],
            "requires": ["customer_id"],
        },

        # ---- Payments ----
        {
            "id": "generate_psi",
            "name": "Generate Payment Success Indicators",
            "category": "Payments",
            "method": "POST",
            "description": "Run Payment Success Indicators (PSI) for an account + amount.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "account_id", "label": "Account", "type": "account_select",
                 "source": "state:account_id", "required": True},
                {"name": "amount", "label": "Amount (USD)", "type": "number",
                 "default": "100.00", "required": True},
            ],
            "requires": ["customer_id", "account_id"],
        },
        # ---- Micro Entries ----
        {
            "id": "initiate_micro_entries",
            "name": "Initiate Micro Entries",
            "category": "Micro Entries",
            "method": "POST",
            "description": "Initiate micro entry verification — two random amounts under $1 deposited to the customer's account. Use a real (or sandbox test) routing + account number.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "routing_number", "label": "Routing Number", "type": "string",
                 "default": "011000138", "required": True,
                 "hint": "Sandbox: use 011000138 or 121000358"},
                {"name": "account_number", "label": "Account Number", "type": "select",
                 "options": ["5111111111", "5999999999", "6111111111", "6222222222", "4111111111", "1111111111"],
                 "default": "5111111111", "required": True,
                 "hint": "5111111111/5999999999=manual verify · 6111111111/6222222222=auto-verify after ~1h · 1111111111=rejected"},
                {"name": "account_type", "label": "Account Type", "type": "select",
                 "options": ["personalChecking", "businessChecking"],
                 "default": "personalChecking", "required": False},
            ],
            "requires": ["customer_id"],
        },
        {
            "id": "verify_micro_entries",
            "name": "Verify Micro Entries",
            "category": "Micro Entries",
            "method": "POST",
            "description": "Verify the two micro amounts received in the customer's account. In sandbox always use 0.01 and 0.02.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "account_id", "label": "AVA Account ID", "type": "string",
                 "source": "state:micro_account_id", "required": True,
                 "hint": "Auto-filled from Initiate Micro Entries response"},
                {"name": "amount1", "label": "Amount 1 (USD)", "type": "number",
                 "default": "0.01", "required": True,
                 "hint": "Sandbox: always 0.01"},
                {"name": "amount2", "label": "Amount 2 (USD)", "type": "number",
                 "default": "0.02", "required": True,
                 "hint": "Sandbox: always 0.02"},
            ],
            "requires": ["customer_id"],
        },
        {
            "id": "get_micro_entries",
            "name": "Get Micro Entry Details",
            "category": "Micro Entries",
            "method": "GET",
            "description": "Fetch the micro entry verification details and current status for an account.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "account_id", "label": "AVA Account ID", "type": "string",
                 "source": "state:micro_account_id", "required": True,
                 "hint": "Auto-filled from Initiate Micro Entries response"},
            ],
            "requires": ["customer_id"],
        },

        # ---- Business ----
        {
            "id": "create_business",
            "name": "Create Business",
            "category": "Business",
            "method": "POST",
            "description": "Create a business record for the customer. Required before some analytics reports.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "business_name", "label": "Business Name", "type": "string",
                 "default": "Test Business LLC", "required": True},
                {"name": "personally_liable", "label": "Personally Liable", "type": "select",
                 "options": ["true", "false"], "default": "true", "required": True},
                {"name": "address_line1", "label": "Address Line 1", "type": "string",
                 "default": "123 Main St", "required": True},
                {"name": "city", "label": "City", "type": "string",
                 "default": "Salt Lake City", "required": True},
                {"name": "state", "label": "State", "type": "string",
                 "default": "UT", "required": True},
                {"name": "country", "label": "Country (2-letter)", "type": "string",
                 "default": "US", "required": True},
                {"name": "postal_code", "label": "Postal Code", "type": "string",
                 "default": "84101", "required": True},
                {"name": "phone_country_code", "label": "Phone Country Code", "type": "string",
                 "default": "1", "required": True},
                {"name": "phone_no", "label": "Phone Number (10 digits)", "type": "string",
                 "default": "2025550100", "required": True},
                {"name": "email", "label": "Email", "type": "string",
                 "default": "biz@example.com", "required": False},
                {"name": "business_type", "label": "Business Type", "type": "string",
                 "default": "LLC", "required": False},
            ],
            "requires": ["customer_id"],
        },
        {
            "id": "get_business",
            "name": "Get Business for Customer",
            "category": "Business",
            "method": "GET",
            "description": "Retrieve the business record associated with a customer.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
            ],
            "requires": ["customer_id"],
        },

        # ---- TxPush ----
        {
            "id": "subscribe_txpush",
            "name": "Subscribe to TxPush",
            "category": "TxPush",
            "method": "POST",
            "description": "Register a TxPush webhook listener for account and transaction events.",
            "note": (
                "<strong>Testing with ngrok</strong> &mdash; Finicity validates the callback URL "
                "immediately on subscribe. "
                "Run <code>ngrok http 9021</code> in a separate terminal, copy the "
                "<code>https://…ngrok-free.app</code> URL it prints, then paste it here with "
                "<code>/txpush-listener</code> appended.<br>"
                "After subscribing, use <em>Fire TxPush Test</em> to send a test event and "
                "view it at <a href='/txpush-events' target='_blank'>/txpush-events</a>."
            ),
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "account_id", "label": "Account", "type": "account_select",
                 "source": "state:account_id", "required": True},
                {"name": "callback_url", "label": "Callback URL (HTTPS)", "type": "string",
                 "default": "https://YOUR-NGROK-ID.ngrok-free.app/txpush-listener", "required": True},
            ],
            "requires": ["customer_id", "account_id"],
        },
        {
            "id": "disable_txpush",
            "name": "Disable TxPush",
            "category": "TxPush",
            "method": "DELETE",
            "description": "Delete all TxPush subscriptions for an account — no more notifications will be sent.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "account_id", "label": "Account", "type": "account_select",
                 "source": "state:account_id", "required": True},
            ],
            "requires": ["customer_id", "account_id"],
        },

        # ---- Transfer ----
        {
            "id": "get_deposit_switches",
            "name": "Get Deposit Switches",
            "category": "Transfer",
            "method": "GET",
            "description": "Retrieve all deposit switch records for a customer.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
            ],
            "requires": ["customer_id"],
        },
        {
            "id": "get_bill_pay_switches",
            "name": "Get Bill Pay Switches",
            "category": "Transfer",
            "method": "GET",
            "description": "Retrieve all bill pay switch records for a customer.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
            ],
            "requires": ["customer_id"],
        },

        # ---- Data Enrichment ----
        {
            "id": "enrich_transactions",
            "name": "Enrich Transactions",
            "category": "Data Enrichment",
            "method": "POST",
            "description": "Submit a raw transaction for enrichment: category, merchant name, logo, and entity recognition.",
            "params": [
                {"name": "description", "label": "Transaction Description", "type": "string",
                 "default": "STARBUCKS #1234", "required": True},
                {"name": "amount", "label": "Amount", "type": "number",
                 "default": "5.75", "required": True},
                {"name": "account_type", "label": "Account Type", "type": "select",
                 "options": ["checking", "savings", "creditCard", "loan", "mortgage", "investment"],
                 "default": "checking", "required": True},
                {"name": "external_customer_id", "label": "External Customer ID", "type": "string",
                 "default": "test-customer-1", "required": True,
                 "hint": "Your own customer identifier — any non-empty string"},
                {"name": "posted_date", "label": "Posted Date (YYYY-MM-DD)", "type": "string",
                 "default": "", "required": False},
            ],
        },

        {
            "id": "generate_fcra_psi",
            "name": "Generate FCRA Payment Success Indicators",
            "category": "Payments",
            "method": "POST",
            "description": "Run FCRA-regulated Payment Success Indicators for an account + amount. Requires a Permissible Purpose Code.",
            "params": [
                {"name": "customer_id", "label": "Customer ID", "type": "string",
                 "source": "state:customer_id", "required": True},
                {"name": "account_id", "label": "Account", "type": "account_select",
                 "source": "state:account_id", "required": True},
                {"name": "amount", "label": "Amount (USD)", "type": "number",
                 "default": "100.00", "required": True},
                {"name": "user_email", "label": "User Email", "type": "string",
                 "default": "test@example.com", "required": True},
                {"name": "purpose", "label": "Purpose Code", "type": "select",
                 "options": ["1P"], "default": "1P", "required": True},
            ],
            "requires": ["customer_id", "account_id"],
        },
    ],
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _err(msg: str, status: int = 500) -> Dict[str, Any]:
    return {
        "success": False,
        "data": None,
        "error": msg,
        "request": None,
        "response": {"status_code": status, "body": {"error": msg}},
        "state_updates": {},
    }


def _wrap(client: OpenFinanceClient, data: Any, status: int,
          state_updates: Optional[Dict[str, Any]] = None,
          hints: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return {
        "success": status < 400,
        "data": data,
        "error": None if status < 400 else (
            data.get("message") if isinstance(data, dict) else str(data)
        ),
        "request": client.last_request,
        "response": client.last_response,
        "state_updates": state_updates or {},
        "hints": hints or {},
    }


def _ensure_consumer(client: OpenFinanceClient, customer_id: str) -> Tuple[Dict, int]:
    data, status = client.get_consumer_for_customer(customer_id)
    if status == 200 and isinstance(data, dict) and data.get("id"):
        return data, status
    return client.create_consumer(
        customer_id=customer_id,
        first_name="Test", last_name="User",
        address="123 Main St", city="Chicago", state="IL", zip_code="60601",
        phone="3125551234", ssn="999999999",
        birthday={"year": 1990, "month": 1, "dayOfMonth": 15},
        email="test@example.com",
    )


def _report_updates(data: Any, status: int) -> Dict[str, Any]:
    """Extract report_id from a 202 generate response and return kwargs for _wrap."""
    updates: Dict[str, Any] = {}
    hints: Dict[str, Any] = {}
    if status in (200, 202) and isinstance(data, dict) and data.get("id"):
        rid = data["id"]
        STATE["report_id"] = rid
        updates["report_id"] = rid
        hints["note"] = (
            f"Report queued (ID: {rid}). Status is '{data.get('status', 'inProgress')}'. "
            "Run \"Get Report by ID\" — the ID is auto-filled. "
            "Poll every few seconds until status changes from 'inProgress' to 'success'."
        )
    return {"state_updates": updates, "hints": hints}


# ---------------------------------------------------------------------------
# Dispatch
# ---------------------------------------------------------------------------

def execute(op_id: str, params: Dict[str, Any]) -> Dict[str, Any]:
    client = _get_client()
    if client is None:
        return _err("Open Finance client not configured. Check PARTNER_ID / PARTNER_SECRET / APP_KEY in .env")

    p = params or {}

    # Local-only operations
    if op_id == "set_customer":
        cid = p.get("customer_id")
        if not cid:
            return _err("customer_id required", 400)
        STATE["customer_id"] = str(cid)
        return {
            "success": True,
            "data": {"customer_id": cid},
            "error": None,
            "request": {"method": "LOCAL", "url": "(client-side state)", "body": {"customer_id": cid}},
            "response": {"status_code": 200, "body": {"customer_id": cid}},
            "state_updates": {"customer_id": str(cid)},
        }

    try:
        if op_id == "create_token":
            data, status = client.create_token()
            return _wrap(client, data, status)

        if op_id == "create_test_customer":
            username = p.get("username") or f"test_user_{int(time.time())}"
            data, status = client.add_testing_customer(username)
            updates: Dict[str, Any] = {}
            if status < 400 and isinstance(data, dict) and data.get("id"):
                updates["customer_id"] = str(data["id"])
                updates["customer_username"] = username
                STATE.update(updates)
            return _wrap(client, data, status, state_updates=updates)

        if op_id == "list_customers":
            data, status = client.get_customers(search=p.get("search", ""))
            return _wrap(client, data, status)

        if op_id == "get_customer_consumer":
            data, status = client.get_consumer_for_customer(p["customer_id"])
            hints = {}
            updates = {}
            if status == 404:
                hints["note"] = (
                    "No consumer record exists for this customer yet. "
                    "Run 'Ensure Consumer Record' (Reports category) or generate "
                    "any report — both will auto-create a test consumer PII record."
                )
            elif status < 400 and isinstance(data, dict):
                cid = data.get("id")
                if cid:
                    STATE["consumer_id"] = str(cid)
                    updates["consumer_id"] = STATE["consumer_id"]
            return _wrap(client, data, status, state_updates=updates, hints=hints)

        if op_id == "get_consumer_by_id":
            data, status = client.get_consumer(p["consumer_id"])
            return _wrap(client, data, status)

        if op_id == "generate_connect_url":
            data, status = client.generate_connect_url(
                p["customer_id"], os.environ.get("PARTNER_ID", "")
            )
            hints = {}
            if isinstance(data, dict) and data.get("link"):
                hints["open_link"] = data["link"]
            return _wrap(client, data, status, hints=hints)

        if op_id == "generate_lite_connect_url":
            data, status = client.generate_lite_connect_url(
                p["customer_id"], p["institution_id"]
            )
            hints = {}
            if isinstance(data, dict) and data.get("link"):
                hints["open_link"] = data["link"]
            return _wrap(client, data, status, hints=hints)

        if op_id == "generate_fix_connect_url":
            data, status = client.generate_fix_connect_url(
                p["customer_id"], p["institution_login_id"]
            )
            hints = {}
            if isinstance(data, dict) and data.get("link"):
                hints["open_link"] = data["link"]
            return _wrap(client, data, status, hints=hints)

        if op_id in ("refresh_accounts", "get_accounts"):
            if op_id == "refresh_accounts":
                data, status = client.refresh_customer_accounts(p["customer_id"])
            else:
                data, status = client.get_customer_accounts(p["customer_id"])
            updates = {}
            if status < 400 and isinstance(data, dict):
                accounts = data.get("accounts", [])
                STATE["accounts"] = accounts
                updates["accounts"] = accounts
                if accounts and not STATE.get("account_id"):
                    checking = next(
                        (a for a in accounts if "checking" in (a.get("type") or "").lower()),
                        accounts[0]
                    )
                    STATE["account_id"] = str(checking.get("id"))
                    updates["account_id"] = STATE["account_id"]
            return _wrap(client, data, status, state_updates=updates)

        if op_id == "get_account":
            data, status = client.get_customer_account(p["customer_id"], p["account_id"])
            return _wrap(client, data, status)

        if op_id == "get_account_balance":
            data, status = client.get_available_balance(p["customer_id"], p["account_id"])
            return _wrap(client, data, status)

        if op_id == "get_account_owner":
            data, status = client.get_account_owner(p["customer_id"], p["account_id"])
            return _wrap(client, data, status)

        if op_id == "get_account_payment_details":
            data, status = client.get_account_payment_details(p["customer_id"], p["account_id"])
            return _wrap(client, data, status)

        if op_id == "get_ach_details":
            data, status = client.get_account_ach_details(p["customer_id"], p["account_id"])
            return _wrap(client, data, status)

        if op_id == "get_account_owner_details":
            data, status = client.get_account_owner_details(p["customer_id"], p["account_id"])
            return _wrap(client, data, status)

        if op_id == "get_account_statement":
            index = int(p.get("index") or 1)
            data, status = client.get_account_statement(p["customer_id"], p["account_id"], index)
            hints: Dict[str, Any] = {}
            if status < 400 and isinstance(data, dict) and data.get("pdf_base64"):
                hints["pdf_base64"] = data["pdf_base64"]
            return _wrap(client, data, status, hints=hints)

        if op_id == "load_historic_transactions":
            data, status = client.load_historic_transactions(p["customer_id"], p["account_id"])
            hints: Dict[str, Any] = {}
            if status == 204:
                hints["note"] = (
                    "204 No Content — success. Finicity has queued a background refresh of up to "
                    "24 months of historic transactions. Run \"Get Account Transactions\" in "
                    "30-60 seconds to see the results."
                )
                data = {"message": "Background refresh queued (204 No Content)"}
            return _wrap(client, data, status, hints=hints)

        if op_id == "get_loan_payment_details":
            data, status = client.get_loan_payment_details(p["customer_id"], p["account_id"])
            return _wrap(client, data, status)

        if op_id == "get_transactions":
            days = int(p.get("days") or 90)
            to_date = int(time.time())
            from_date = to_date - days * 86400
            data, status = client.get_customer_transactions(p["customer_id"], from_date, to_date)
            return _wrap(client, data, status)

        if op_id == "get_account_transactions":
            days = int(p.get("days") or 90)
            to_date = int(time.time())
            from_date = to_date - days * 86400
            data, status = client.get_account_transactions(
                p["customer_id"], p["account_id"], from_date, to_date,
            )
            return _wrap(client, data, status)

        if op_id == "get_recurring_transactions":
            account_ids = [str(a["id"]) for a in STATE.get("accounts", []) if a.get("id")]
            data, status = client.get_recurring_transactions(
                p["customer_id"], account_ids or None,
            )
            return _wrap(client, data, status)

        if op_id == "search_institutions":
            data, status = client.get_institutions(search=p.get("search", ""))
            return _wrap(client, data, status)

        if op_id == "get_institution":
            data, status = client.get_institution(p["institution_id"])
            return _wrap(client, data, status)

        if op_id == "get_certified_institutions":
            data, status = client.get_certified_institutions(search=p.get("search", ""))
            return _wrap(client, data, status)

        if op_id == "get_institution_by_routing":
            data, status = client.get_institutions_by_routing_number(p["routing_number"])
            return _wrap(client, data, status)

        if op_id == "ensure_consumer":
            data, status = _ensure_consumer(client, p["customer_id"])
            updates = {}
            if status < 400 and isinstance(data, dict):
                cid = data.get("id")
                if cid:
                    STATE["consumer_id"] = str(cid)
                    updates["consumer_id"] = STATE["consumer_id"]
            return _wrap(client, data, status, state_updates=updates)

        if op_id == "generate_voa":
            _ensure_consumer(client, p["customer_id"])
            data, status = client.generate_voa_report(p["customer_id"])
            return _wrap(client, data, status, **_report_updates(data, status))

        if op_id == "generate_voi":
            _ensure_consumer(client, p["customer_id"])
            data, status = client.generate_voi_report(p["customer_id"])
            return _wrap(client, data, status, **_report_updates(data, status))

        if op_id == "generate_cashflow":
            _ensure_consumer(client, p["customer_id"])
            data, status = client.generate_cash_flow_personal_report(p["customer_id"])
            return _wrap(client, data, status, **_report_updates(data, status))

        if op_id == "generate_balance_analytics":
            _ensure_consumer(client, p["customer_id"])
            data, status = client.generate_balance_analytics_report(p["customer_id"])
            return _wrap(client, data, status, **_report_updates(data, status))

        if op_id == "list_reports":
            data, status = client.get_reports_by_customer(p["customer_id"])
            return _wrap(client, data, status)

        if op_id == "generate_voai":
            _ensure_consumer(client, p["customer_id"])
            data, status = client.generate_voai_report(p["customer_id"])
            return _wrap(client, data, status, **_report_updates(data, status))

        if op_id == "generate_cashflow_business":
            data, status = client.generate_cash_flow_business_report(p["customer_id"])
            return _wrap(client, data, status, **_report_updates(data, status))

        if op_id == "generate_cashflow_analytics":
            _ensure_consumer(client, p["customer_id"])
            data, status = client.generate_cashflow_analytics_report(p["customer_id"])
            return _wrap(client, data, status, **_report_updates(data, status))

        if op_id == "generate_transactions_report":
            _ensure_consumer(client, p["customer_id"])
            days = int(p.get("days") or 90)
            to_date = int(time.time())
            from_date = to_date - days * 86400
            data, status = client.generate_transactions_report(p["customer_id"], from_date, to_date)
            return _wrap(client, data, status, **_report_updates(data, status))

        if op_id == "get_report_by_id":
            data, status = client.get_report(p["report_id"], p.get("purpose_code") or "3F")
            return _wrap(client, data, status)

        if op_id == "initiate_micro_entries":
            routing = p.get("routing_number", "").strip()
            account = p.get("account_number", "").strip()
            if not routing or not account:
                return _wrap(client, {"message": "routing_number and account_number are required"}, 400)
            acct_type_map = {
                "personal_checking": "personalChecking",
                "business_checking": "businessChecking",
                "personalchecking": "personalChecking",
                "businesschecking": "businessChecking",
            }
            raw_type = (p.get("account_type") or "personalChecking").lower().replace("_", "")
            receiver = {
                "routingNumber": routing,
                "accountNumber": account,
                "accountType": acct_type_map.get(raw_type, "personalChecking"),
                "name": p.get("customer_name") or "Test User",
            }
            data, status = client.initiate_micro_deposits(p["customer_id"], receiver)
            state_updates: Dict[str, Any] = {}
            if status == 200 and isinstance(data, dict) and data.get("accountId"):
                STATE["micro_account_id"] = str(data["accountId"])
                state_updates["micro_account_id"] = STATE["micro_account_id"]
            return _wrap(client, data, status, state_updates=state_updates)

        if op_id == "verify_micro_entries":
            amounts = [float(p.get("amount1") or 0.11), float(p.get("amount2") or 0.22)]
            data, status = client.verify_micro_deposits(p["customer_id"], p["account_id"], amounts)
            return _wrap(client, data, status)

        if op_id == "get_micro_entries":
            data, status = client.get_micro_deposit_details(p["customer_id"], p["account_id"])
            return _wrap(client, data, status)

        if op_id == "generate_psi":
            amount = float(p.get("amount") or 100.00)
            data, status = client.generate_payment_success_indicators(
                p["customer_id"], p["account_id"], amount,
            )
            # Poll briefly if in progress
            if isinstance(data, dict) and data.get("status") == "IN PROGRESS":
                pay_request_id = data.get("payRequestId")
                for _ in range(10):
                    time.sleep(1)
                    result, rstatus = client.get_payment_success_indicators(
                        p["customer_id"], p["account_id"], pay_request_id,
                    )
                    if isinstance(result, dict) and result.get("status") == "SUCCESS":
                        data, status = result, rstatus
                        break
            return _wrap(client, data, status)

        if op_id == "get_customer":
            data, status = client.get_customer(p["customer_id"])
            return _wrap(client, data, status)

        if op_id == "delete_customer":
            data, status = client.delete_customer(p["customer_id"])
            return _wrap(client, data, status)

        if op_id == "get_institution_branding":
            data, status = client.get_institution_branding(p["institution_id"])
            return _wrap(client, data, status)

        if op_id == "delete_customer_account":
            data, status = client.delete_customer_account(p["customer_id"], p["account_id"])
            return _wrap(client, data, status)

        if op_id == "account_owner_match":
            email = p.get("email") or None
            phone = p.get("phone") or None
            data, status = client.account_owner_match(
                p["customer_id"], p["account_id"],
                first_name=p.get("first_name") or "",
                last_name=p.get("last_name") or "",
                email=email, phone=phone
            )
            return _wrap(client, data, status)

        if op_id == "get_report_by_customer":
            data, status = client.get_report_by_customer(p["customer_id"], p["report_id"], p.get("purpose_code") or "3F")
            return _wrap(client, data, status)

        if op_id == "create_consumer":
            data, status = client.create_consumer(
                p["customer_id"],
                p.get("first_name") or "John",
                p.get("last_name") or "Smith",
                email=p.get("email") or "",
                phone=p.get("phone") or "",
                ssn=p.get("ssn") or "",
            )
            updates = {}
            if status < 400 and isinstance(data, dict):
                cid = data.get("id")
                if cid:
                    STATE["consumer_id"] = str(cid)
                    updates["consumer_id"] = STATE["consumer_id"]
            return _wrap(client, data, status, state_updates=updates)

        if op_id == "create_business":
            data, status = client.create_business(
                p["customer_id"],
                p.get("business_name") or "Test Business LLC",
                personally_liable=p.get("personally_liable", "true") == "true",
                address_line1=p.get("address_line1") or "123 Main St",
                city=p.get("city") or "Salt Lake City",
                state=p.get("state") or "UT",
                country=p.get("country") or "US",
                postal_code=p.get("postal_code") or "84101",
                phone_country_code=p.get("phone_country_code") or "1",
                phone_no=p.get("phone_no") or "2025550100",
                email=p.get("email") or None,
                business_type=p.get("business_type") or None,
            )
            return _wrap(client, data, status)

        if op_id == "get_business":
            data, status = client.get_business_for_customer(p["customer_id"])
            return _wrap(client, data, status)

        if op_id == "subscribe_txpush":
            data, status = client.subscribe_to_txpush(
                p["customer_id"], p["account_id"], p.get("callback_url") or ""
            )
            return _wrap(client, data, status)

        if op_id == "disable_txpush":
            data, status = client.disable_txpush(p["customer_id"], p["account_id"])
            return _wrap(client, data, status)

        if op_id == "get_deposit_switches":
            data, status = client.get_deposit_switches(p["customer_id"])
            return _wrap(client, data, status)

        if op_id == "get_bill_pay_switches":
            data, status = client.get_bill_pay_switches(p["customer_id"])
            return _wrap(client, data, status)

        if op_id == "enrich_transactions":
            import datetime
            posted = p.get("posted_date") or datetime.date.today().isoformat()
            txn = {
                "description": p.get("description") or "STARBUCKS #1234",
                "amount": float(p.get("amount") or 5.75),
                "postedDate": posted,
                "transactionDate": posted,
                "accountType": p.get("account_type") or "checking",
                "externalCustomerId": p.get("external_customer_id") or "test-customer-1",
                "externalTransactionId": f"txn-{int(__import__('time').time())}",
            }
            data, status = client.enrich_transactions([txn])
            return _wrap(client, data, status)

        if op_id == "generate_fcra_psi":
            amount = float(p.get("amount") or 100.00)
            purpose = p.get("purpose") or "1P"
            user_email = p.get("user_email") or "test@example.com"
            # The PSI-FCRA endpoint requires the customer profile to have an email set.
            # Patch it first (silently) then call PSI.
            client.update_customer(p["customer_id"], email=user_email)
            data, status = client.generate_fcra_payment_success_indicators(
                p["customer_id"], p["account_id"], amount, purpose, user_email=user_email,
            )
            if isinstance(data, dict) and data.get("status") == "IN PROGRESS":
                pay_request_id = data.get("payRequestId")
                for _ in range(10):
                    time.sleep(1)
                    result, rstatus = client.get_fcra_payment_success_indicators(
                        p["customer_id"], p["account_id"], pay_request_id,
                    )
                    if isinstance(result, dict) and result.get("status") == "SUCCESS":
                        data, status = result, rstatus
                        break
            return _wrap(client, data, status)

        return _err(f"Unknown operation: {op_id}", 404)

    except KeyError as e:
        return _err(f"Missing required parameter: {e.args[0]}", 400)
    except Exception as e:
        return _err(str(e))


_seeded = False


def _seed_default_customer() -> None:
    """On first state access, seed customer_id.

    If OFIN_DEFAULT_CUSTOMER_ID is set in the environment, use that customer
    directly (faster). Otherwise fall back to scanning the customer list for
    the most recently created testing customer with a checking account.
    """
    global _seeded
    if _seeded or STATE.get("customer_id"):
        _seeded = True
        return
    _seeded = True
    client = _get_client()
    if client is None:
        return

    # Fast path: use the configured default customer ID
    default_cid = os.environ.get("OFIN_DEFAULT_CUSTOMER_ID", "").strip()
    if default_cid:
        try:
            acc_data, acc_status = client.get_customer_accounts(default_cid)
            if acc_status < 400 and isinstance(acc_data, dict):
                accounts = acc_data.get("accounts") or []
                checking = next((a for a in accounts if a.get("type") == "checking"), None)
                STATE["customer_id"] = default_cid
                STATE["accounts"] = accounts
                if checking:
                    STATE["account_id"] = str(checking.get("id"))
                elif accounts:
                    STATE["account_id"] = str(accounts[0].get("id"))
                return
        except Exception:
            pass  # Fall through to scan

    try:
        data, status = client.get_customers(start=1, limit=25)
        if status >= 400 or not isinstance(data, dict):
            return
        customers = data.get("customers") or []
        # Newest testing customers first
        candidates = sorted(
            customers,
            key=lambda c: (c.get("type") == "testing", c.get("createdDate", 0)),
            reverse=True,
        )
        # First pass: find a customer with a checking account
        # Second pass: accept any customer with accounts (fallback)
        best: Optional[tuple] = None  # (customer, accounts, default_account)
        for c in candidates:
            cid = str(c.get("id"))
            acc_data, acc_status = client.get_customer_accounts(cid)
            if acc_status >= 400 or not isinstance(acc_data, dict):
                continue
            accounts = acc_data.get("accounts") or []
            if not accounts:
                continue
            checking = next((a for a in accounts if a.get("type") == "checking"), None)
            if checking:
                # Perfect match — use immediately
                STATE["customer_id"] = cid
                STATE["customer_username"] = c.get("username")
                STATE["accounts"] = accounts
                STATE["account_id"] = str(checking.get("id"))
                return
            # Has accounts but no checking — keep as fallback
            if best is None:
                best = (c, accounts, accounts[0])
        # Use best fallback if no checking customer found
        if best:
            c, accounts, default_account = best
            STATE["customer_id"] = str(c.get("id"))
            STATE["customer_username"] = c.get("username")
            STATE["accounts"] = accounts
            STATE["account_id"] = str(default_account.get("id"))
            return
        # No customer with any accounts — just set the first candidate's id
        if candidates:
            c = candidates[0]
            STATE["customer_id"] = str(c.get("id"))
            STATE["customer_username"] = c.get("username")
    except Exception:
        pass


def get_state() -> Dict[str, Any]:
    """Return a UI-safe snapshot of state."""
    _seed_default_customer()
    accounts = STATE.get("accounts") or []
    return {
        "customer_id": STATE.get("customer_id"),
        "customer_username": STATE.get("customer_username"),
        "consumer_id": STATE.get("consumer_id"),
        "report_id": STATE.get("report_id"),
        "account_id": STATE.get("account_id"),
        "micro_account_id": STATE.get("micro_account_id"),
        "accounts_count": len(accounts),
        "accounts": [
            {
                "id": str(a.get("id")),
                "number": a.get("number") or a.get("accountNumberDisplay") or "",
                "name": a.get("name") or "",
                "type": a.get("type") or "",
            }
            for a in accounts if a.get("id") is not None
        ],
        "configured": is_configured(),
    }
