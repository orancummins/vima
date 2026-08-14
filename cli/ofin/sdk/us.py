"""US (Finicity) Open Finance SDK facade.

Wraps :class:`OpenFinanceClient` and exposes a curated set of the most common
flows as clean methods returning :class:`Result`. The facade also captures
useful ids (customer_id, account_id, report_id) into ``state_updates`` so the
CLI can persist an "active" customer between invocations.
"""
from __future__ import annotations

from typing import Any

from ._imports import USClientCls
from .base import Result, first


class USClient:
    """Curated wrapper around the US Open Finance client."""

    region = "us"

    def __init__(self, partner_id: str, partner_secret: str, app_key: str,
                 base_url: str = "https://api.finicity.com", timeout: int | None = None) -> None:
        self._c = USClientCls(partner_id, partner_secret, app_key, base_url=base_url)
        self._timeout = timeout

    # -- internal -----------------------------------------------------------
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
    def add_testing_customer(self, username: str) -> Result:
        body, status = self._c.add_testing_customer(username)
        updates = {}
        if 200 <= status < 300:
            cid = first(body, "id", "customerId")
            if cid:
                updates = {"customer_id": str(cid), "customer_username": username}
        return self._wrap(body, status, state_updates=updates)

    def list_customers(self, search: str = "", limit: int = 25) -> Result:
        body, status = self._c.get_customers(search=search, limit=limit)
        return self._wrap(body, status)

    def get_customer(self, customer_id: str) -> Result:
        body, status = self._c.get_customer(customer_id)
        return self._wrap(body, status)

    # -- data connect -------------------------------------------------------
    def generate_connect_url(self, customer_id: str, experience: str | None = None) -> Result:
        body, status = self._c.generate_connect_url(customer_id, experience=experience)
        hints = {}
        if 200 <= status < 300:
            link = first(body, "link", "connectUrl", "url")
            if link:
                hints = {"open_link": link, "open_link_label": "Launch Data Connect"}
        return self._wrap(body, status, hints=hints)

    # -- accounts -----------------------------------------------------------
    def list_accounts(self, customer_id: str) -> Result:
        body, status = self._c.get_customer_accounts(customer_id)
        updates = {}
        if 200 <= status < 300:
            accounts = body.get("accounts") if isinstance(body, dict) else None
            if isinstance(accounts, list) and accounts:
                aid = first(accounts[0], "id", "accountId")
                if aid:
                    updates = {"account_id": str(aid)}
        return self._wrap(body, status, state_updates=updates)

    def refresh_accounts(self, customer_id: str) -> Result:
        body, status = self._c.refresh_customer_accounts(customer_id)
        return self._wrap(body, status)

    def get_balance(self, customer_id: str, account_id: str) -> Result:
        body, status = self._c.get_available_balance(customer_id, account_id)
        return self._wrap(body, status)

    # -- transactions -------------------------------------------------------
    def list_transactions(self, customer_id: str, from_date: int, to_date: int,
                          limit: int = 1000) -> Result:
        body, status = self._c.get_customer_transactions(
            customer_id, from_date=from_date, to_date=to_date, limit=limit)
        return self._wrap(body, status)

    # -- reports ------------------------------------------------------------
    def generate_voa(self, customer_id: str, account_ids: list[str] | None = None) -> Result:
        body, status = self._c.generate_voa_report(customer_id, account_ids=account_ids)
        updates = {}
        if 200 <= status < 300:
            rid = first(body, "reportId", "id")
            if rid:
                updates = {"report_id": str(rid)}
        return self._wrap(body, status, state_updates=updates)

    def generate_voi(self, customer_id: str, account_ids: list[str] | None = None) -> Result:
        body, status = self._c.generate_voi_report(customer_id, account_ids=account_ids)
        updates = {}
        if 200 <= status < 300:
            rid = first(body, "reportId", "id")
            if rid:
                updates = {"report_id": str(rid)}
        return self._wrap(body, status, state_updates=updates)
