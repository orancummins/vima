"""Mastercard Open Finance Australia API client.

The AU variant is structurally similar to the US (both Finicity-backed) but
differs in:
    * Base URL: ``https://api.openbanking.mastercard.com.au``
    * Auth headers: ``App-Key`` / ``App-Token`` (not ``Finicity-App-Key`` /
      ``Finicity-App-Token`` like the US tenant).
    * Most data-plane calls require a ``Consent-Receipt-Id`` header tied to
      the CDR (Consumer Data Right) consent the customer granted via Connect.
"""
from __future__ import annotations

import time
from typing import Any, Dict, Optional, Tuple

import requests


class OpenFinanceAUClient:
    """Client for Mastercard Open Finance Australia APIs."""

    def __init__(
        self,
        partner_id: str,
        partner_secret: str,
        app_key: str,
        base_url: str = "https://api.openbanking.mastercard.com.au",
    ) -> None:
        self.partner_id = partner_id
        self.partner_secret = partner_secret
        self.app_key = app_key
        self.base_url = base_url.rstrip("/")
        self._token: Optional[str] = None
        self._token_timestamp: float = 0.0
        self._last_request: Optional[Dict[str, Any]] = None
        self._last_response: Optional[Dict[str, Any]] = None

    # ------------------------------------------------------------------
    # Introspection
    # ------------------------------------------------------------------
    @property
    def last_request(self) -> Optional[Dict[str, Any]]:
        return self._last_request

    @property
    def last_response(self) -> Optional[Dict[str, Any]]:
        return self._last_response

    # ------------------------------------------------------------------
    # Token
    # ------------------------------------------------------------------
    def _get_token(self, force_refresh: bool = False) -> str:
        # AU token valid 2 h — refresh proactively after 90 min.
        if not force_refresh and self._token and (time.time() - self._token_timestamp) < 5400:
            return self._token

        url = f"{self.base_url}/aggregation/v2/partners/authentication"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "App-Key": self.app_key,
        }
        payload = {"partnerId": self.partner_id, "partnerSecret": self.partner_secret}

        self._last_request = {
            "method": "POST",
            "url": url,
            "headers": dict(headers),
            "body": {**payload, "partnerSecret": "********"},
        }
        resp = requests.post(url, headers=headers, json=payload, timeout=30)
        try:
            body = resp.json()
        except ValueError:
            body = resp.text
        self._last_response = {
            "status_code": resp.status_code,
            "headers": dict(resp.headers),
            "body": body,
        }

        if not resp.ok:
            raise RuntimeError(f"Open Finance AU token request failed ({resp.status_code}): {body}")
        token = (body or {}).get("token") if isinstance(body, dict) else None
        if not token:
            raise RuntimeError("Open Finance AU token response missing 'token' field")
        self._token = token
        self._token_timestamp = time.time()
        return token

    # ------------------------------------------------------------------
    # Authenticated request
    # ------------------------------------------------------------------
    def _request(
        self,
        method: str,
        endpoint: str,
        *,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        consent_receipt_id: Optional[str] = None,
    ) -> Tuple[Any, int]:
        token = self._get_token()
        url = f"{self.base_url}{endpoint}"
        headers: Dict[str, str] = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "App-Key": self.app_key,
            "App-Token": token,
        }
        if consent_receipt_id:
            headers["Consent-Receipt-Id"] = consent_receipt_id

        # Mask token in the captured request for UI display.
        masked_headers = dict(headers)
        masked_headers["App-Token"] = (token[:10] + "...") if token else ""
        self._last_request = {
            "method": method,
            "url": url,
            "headers": masked_headers,
            "body": data,
            "params": params,
        }

        resp = requests.request(method=method, url=url, headers=headers,
                                json=data, params=params, timeout=60)
        try:
            body = resp.json()
        except ValueError:
            body = resp.text
        self._last_response = {
            "status_code": resp.status_code,
            "headers": dict(resp.headers),
            "body": body,
        }
        return body, resp.status_code

    # ------------------------------------------------------------------
    # Operations
    # ------------------------------------------------------------------
    def create_token(self) -> Tuple[Dict[str, Any], int]:
        """Force a fresh token and return a redacted preview.

        Useful as a smoke test — succeeds with only partner credentials and
        does not depend on customer/consent state.
        """
        self._token = None
        token = self._get_token(force_refresh=True)
        return (
            {"token": token[:10] + "...", "message": "Token created successfully"},
            200,
        )

    def add_testing_customer(
        self,
        username: str,
        first_name: str = "Alex",
        last_name: str = "Smith",
        email: str = "alex.smith@example.com",
        phone: str = "+61400000000",
    ) -> Tuple[Any, int]:
        # AU sandbox requires firstName, lastName, email and phone — all
        # fields are sent unconditionally with safe defaults so the call
        # works as a one-click smoke test from the UI.
        body: Dict[str, Any] = {
            "username": username,
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
            "phone": phone,
        }
        return self._request("POST", "/aggregation/v2/customers/testing", data=body)

    def get_customers(self, search: str = "", start: int = 1, limit: int = 25) -> Tuple[Any, int]:
        params: Dict[str, Any] = {"start": start, "limit": limit}
        if search:
            params["search"] = search
        return self._request("GET", "/aggregation/v1/customers", params=params)

    def get_customer(self, customer_id: str) -> Tuple[Any, int]:
        return self._request("GET", f"/aggregation/v1/customers/{customer_id}")

    def get_institutions(self, search: str = "", start: int = 1, limit: int = 25,
                         supported_countries: str = "au") -> Tuple[Any, int]:
        params: Dict[str, Any] = {
            "start": start,
            "limit": limit,
            "supportedCountries": supported_countries,
        }
        if search:
            params["search"] = search
        return self._request("GET", "/institution/v2/institutions", params=params)

    def generate_connect_url(self, customer_id: str,
                             webhook_url: str = "") -> Tuple[Any, int]:
        body: Dict[str, Any] = {
            "partnerId": self.partner_id,
            "customerId": customer_id,
        }
        if webhook_url:
            body["webhook"] = webhook_url
        return self._request("POST", "/connect/v2/generate", data=body)

    def get_customer_accounts(self, customer_id: str,
                              consent_receipt_id: str) -> Tuple[Any, int]:
        return self._request(
            "GET",
            f"/aggregation/v1/customers/{customer_id}/accounts",
            consent_receipt_id=consent_receipt_id,
        )

    def get_data_sharing_consents(self, customer_id: str,
                                  status: str = "ACTIVE",
                                  start: int = 1,
                                  limit: int = 25) -> Tuple[Any, int]:
        """List CDR data-sharing consents for a customer.

        Use this to retrieve the ``consent_receipt_id`` produced when a
        customer completes the Connect flow — no webhook listener needed.
        Default filter is ``status=ACTIVE`` so a freshly-granted consent
        appears here within a few seconds of completing FinBank OAuth.
        """
        params: Dict[str, Any] = {
            "customer_id": customer_id,
            "status": status,
            "start": start,
            "limit": limit,
            "sort_by": "startDate",
            "sort_order": "Desc",
        }
        return self._request("GET", "/data-sharing-consents", params=params)
