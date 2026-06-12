"""AU (CDR / Finicity-backed) Open Finance SDK facade.

Wraps :class:`OpenFinanceAUClient`. The notable AU specifics handled here:

* data-plane account calls require a ``Consent-Receipt-Id`` (obtained after the
  customer completes the CDR Connect flow); ``list_consents`` captures it.
* customer enrolment auto-captures the ``customer_id``.
"""
from __future__ import annotations

from typing import Any, Optional

from ._imports import AUClientCls
from .base import Result, first


class AUClient:
    """Curated wrapper around the AU Open Finance client."""

    region = "au"

    def __init__(self, partner_id: str, partner_secret: str, app_key: str,
                 base_url: str = "https://api.openbanking.mastercard.com.au",
                 timeout: Optional[int] = None) -> None:
        self._c = AUClientCls(partner_id, partner_secret, app_key, base_url=base_url)
        self._timeout = timeout

    def _wrap(self, body: Any, status: int, *, state_updates=None, hints=None) -> Result:
        return Result(
            status=status,
            body=body,
            request=self._c.last_request,
            response=self._c.last_response,
            state_updates=state_updates or {},
            hints=hints or {},
        )

    # -- auth ---------------------------------------------------------------
    def auth_token(self) -> Result:
        body, status = self._c.create_token()
        return self._wrap(body, status)

    # -- customers ----------------------------------------------------------
    def add_testing_customer(self, username: str, first_name: str = "Alex",
                             last_name: str = "Smith",
                             email: str = "alex.smith@example.com",
                             phone: str = "+61400000000") -> Result:
        body, status = self._c.add_testing_customer(
            username, first_name=first_name, last_name=last_name,
            email=email, phone=phone)
        updates = {}
        if 200 <= status < 300:
            cid = first(body, "id", "customerId")
            if cid:
                updates = {"customer_id": str(cid), "customer_username": username}
        return self._wrap(body, status, state_updates=updates)

    def list_customers(self, search: str = "", limit: int = 25) -> Result:
        body, status = self._c.get_customers(search=search, limit=limit)
        return self._wrap(body, status)

    # -- institutions -------------------------------------------------------
    def list_institutions(self, search: str = "", limit: int = 25,
                          supported_countries: str = "au") -> Result:
        body, status = self._c.get_institutions(
            search=search, limit=limit, supported_countries=supported_countries)
        return self._wrap(body, status)

    # -- connect ------------------------------------------------------------
    def generate_connect_url(self, customer_id: str, webhook_url: str = "") -> Result:
        body, status = self._c.generate_connect_url(customer_id, webhook_url=webhook_url)
        hints = {}
        if 200 <= status < 300:
            link = first(body, "link", "connectUrl", "url")
            if link:
                hints = {"open_link": link, "open_link_label": "Launch CDR Connect"}
        return self._wrap(body, status, hints=hints)

    # -- consents -----------------------------------------------------------
    def list_consents(self, customer_id: str, status: str = "ACTIVE") -> Result:
        body, http_status = self._c.get_data_sharing_consents(customer_id, status=status)
        updates = {}
        if 200 <= http_status < 300 and isinstance(body, dict):
            items = body.get("consents") or body.get("data") or body.get("items") or []
            if isinstance(items, list) and items:
                rcpt = first(items[0], "consentReceiptId", "receiptId", "id")
                if rcpt:
                    updates = {"consent_receipt_id": str(rcpt)}
        return self._wrap(body, http_status, state_updates=updates)

    # -- accounts -----------------------------------------------------------
    def list_accounts(self, customer_id: str, consent_receipt_id: str) -> Result:
        body, status = self._c.get_customer_accounts(customer_id, consent_receipt_id)
        updates = {}
        if 200 <= status < 300 and isinstance(body, dict):
            accounts = body.get("accounts")
            if isinstance(accounts, list) and accounts:
                aid = first(accounts[0], "id", "accountId")
                if aid:
                    updates = {"account_id": str(aid)}
        return self._wrap(body, status, state_updates=updates)
