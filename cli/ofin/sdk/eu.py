"""EU (Aiia) Open Finance SDK facade.

Wraps :class:`OpenFinanceEUClient`. EU auth is OAuth 2.0 with a JWT client
assertion (RS256) signed by the partner's RSA private key — the underlying
client handles all of that; this facade only orchestrates the bits the web
app's ``api.py`` normally does:

* a single ``end_user_id`` (UUID) must be shared between Create Consent and
  Create Managed Flow. The facade generates one when not supplied and surfaces
  it via ``state_updates`` so the CLI can persist + reuse it.
* the hosted flow URL is surfaced as an ``open_link`` hint.
"""
from __future__ import annotations

import uuid
from typing import Any

from ._imports import EUClientCls
from .base import Result, first


class EUClient:
    """Curated wrapper around the EU Open Finance client."""

    region = "eu"

    def __init__(self, client_id: str, private_key_path: str, public_cert_path: str,
                 auth_base_url: str | None = None, api_base_url: str | None = None,
                 application_id: str = "", timeout: int | None = None) -> None:
        kwargs: dict = {"application_id": application_id}
        if auth_base_url:
            kwargs["auth_base_url"] = auth_base_url
        if api_base_url:
            kwargs["api_base_url"] = api_base_url
        self._c = EUClientCls(client_id, private_key_path, public_cert_path, **kwargs)
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

    # -- providers ----------------------------------------------------------
    def list_providers(self, country: str = "", limit: int = 25) -> Result:
        body, status = self._c.get_providers(country=country, limit=limit)
        return self._wrap(body, status)

    # -- consent ------------------------------------------------------------
    def create_consent(self, use_case_configuration_id: str, end_user_email: str,
                        end_user_id: str | None = None) -> Result:
        # The same end_user_id must be reused by create_flow; generate one if
        # the caller didn't supply (or persist) it.
        eu_id = end_user_id or str(uuid.uuid4())
        body, status = self._c.create_consent(
            use_case_configuration_id=use_case_configuration_id,
            end_user_id=eu_id,
            end_user_email=end_user_email,
        )
        updates = {"end_user_id": eu_id, "end_user_email": end_user_email}
        if 200 <= status < 300:
            cid = first(body, "consentId", "consent_id", "id")
            if cid:
                updates["consent_id"] = str(cid)
        return self._wrap(body, status, state_updates=updates)

    def get_consent(self, consent_id: str) -> Result:
        body, status = self._c.get_consent(consent_id)
        return self._wrap(body, status)

    def revoke_consent(self, consent_id: str) -> Result:
        body, status = self._c.revoke_consent(consent_id)
        return self._wrap(body, status)

    # -- managed flow -------------------------------------------------------
    def create_flow(self, consent_id: str, end_user_id: str, language: str = "en",
                    provider_id: str = "") -> Result:
        body, status = self._c.create_managed_flow(
            consent_id=consent_id, end_user_id=end_user_id,
            language=language, provider_id=provider_id)
        hints = {}
        updates = {}
        if 200 <= status < 300:
            url = first(body, "flowUrl", "flow_url", "link")
            if url:
                hints = {"open_link": url, "open_link_label": "Launch Connect"}
                updates = {"flow_url": url}
        return self._wrap(body, status, state_updates=updates, hints=hints)

    # -- accounts -----------------------------------------------------------
    def list_accounts(self, consent_id: str,
                      include: str = "balances,holders,identifiers,additionalInformation") -> Result:
        body, status = self._c.get_accounts(consent_id=consent_id, include=include)
        updates = {}
        if 200 <= status < 300 and isinstance(body, dict):
            items = body.get("items") or body.get("accounts") or []
            if isinstance(items, list) and items:
                aid = first(items[0], "id", "accountId")
                if aid:
                    updates = {"account_id": str(aid)}
        return self._wrap(body, status, state_updates=updates)

    def get_account(self, account_id: str, consent_id: str) -> Result:
        body, status = self._c.get_account(account_id, consent_id)
        return self._wrap(body, status)

    # -- transactions -------------------------------------------------------
    def list_transactions(self, account_id: str, consent_id: str, from_date: str = "",
                          to_date: str = "", limit: int = 50) -> Result:
        body, status = self._c.get_transactions(
            account_id, consent_id, from_date=from_date, to_date=to_date, limit=limit)
        return self._wrap(body, status)

    # -- balances -----------------------------------------------------------
    def check_balance(self, account_id: str, consent_id: str, max_age: str = "PT15M") -> Result:
        body, status = self._c.check_balance(account_id, consent_id, max_age=max_age)
        return self._wrap(body, status)

    # -- insights -----------------------------------------------------------
    def verify_ownership(self, consent_id: str, customer_name: str,
                         account_ids: list[str] | None = None) -> Result:
        body, status = self._c.verify_account_ownership(
            consent_id=consent_id, customer_name=customer_name, account_ids=account_ids)
        updates = {}
        if 200 <= status < 300:
            vid = first(body, "verificationId", "id")
            if vid:
                updates = {"verification_id": str(vid)}
        return self._wrap(body, status, state_updates=updates)
