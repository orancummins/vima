"""Mastercard Open Finance Europe (Aiia) API client.

The EU stack is structurally different from the US/AU Finicity-backed APIs:

    * Auth: OAuth 2.0 ``client_credentials`` grant with a **JWT client
      assertion** signed by the partner's RSA private key (RS256). The ``kid``
      in the JWT header is the base64url-encoded SHA-256 thumbprint of the
      public certificate body.
    * Auth host:  ``https://mtf.auth.openbanking.mastercard.eu`` (sandbox/MTF)
    * API host:   ``https://mtf.api.openbanking.mastercard.com`` (sandbox/MTF)
    * Access token TTL: 1 h. Tokens are reused until ~5 min before expiry.

Only `cryptography` (already a transitive dep) is required — the JWT is
constructed by hand to avoid pulling in PyJWT for one signing operation.
"""
from __future__ import annotations

import base64
import hashlib
import json
import os
import time
import uuid
from typing import Any

import requests
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.x509 import load_pem_x509_certificate


def _b64url(raw: bytes) -> str:
    """URL-safe base64 with padding stripped (RFC 7515)."""
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode("ascii")


class OpenFinanceEUClient:
    """Client for Mastercard Open Finance Europe (Aiia) APIs."""

    DEFAULT_AUTH_BASE = "https://mtf.auth.openbanking.mastercard.eu"
    DEFAULT_API_BASE = "https://mtf.api.openbanking.mastercard.eu"
    JWT_AUDIENCE = "auth.mastercard.com"

    def __init__(
        self,
        client_id: str,
        private_key_path: str,
        public_cert_path: str,
        auth_base_url: str = DEFAULT_AUTH_BASE,
        api_base_url: str = DEFAULT_API_BASE,
        application_id: str = "",
    ) -> None:
        self.client_id = client_id
        self.private_key_path = private_key_path
        self.public_cert_path = public_cert_path
        self.auth_base_url = auth_base_url.rstrip("/")
        self.api_base_url = api_base_url.rstrip("/")
        # Required by the Mastercard Consent Machine API as the
        # ``X-Application-Id`` request header on every consent / data call.
        # Issued by the EU onboarding officer alongside the clientId.
        self.application_id = application_id

        self._private_key: rsa.RSAPrivateKey | None = None
        self._kid: str | None = None
        self._token: str | None = None
        self._token_expiry: float = 0.0
        self._last_request: dict[str, Any] | None = None
        self._last_response: dict[str, Any] | None = None

    # ------------------------------------------------------------------
    # Introspection
    # ------------------------------------------------------------------
    @property
    def last_request(self) -> dict[str, Any] | None:
        return self._last_request

    @property
    def last_response(self) -> dict[str, Any] | None:
        return self._last_response

    # ------------------------------------------------------------------
    # Key + JWT
    # ------------------------------------------------------------------
    def _load_private_key(self) -> rsa.RSAPrivateKey:
        if self._private_key is not None:
            return self._private_key
        if not os.path.isfile(self.private_key_path):
            raise RuntimeError(
                f"Open Finance EU private key not found: {self.private_key_path}"
            )
        with open(self.private_key_path, "rb") as f:
            key = serialization.load_pem_private_key(f.read(), password=None)
        if not isinstance(key, rsa.RSAPrivateKey):
            raise RuntimeError("Open Finance EU private key must be RSA")
        self._private_key = key
        return key

    def _compute_kid(self) -> str:
        """SHA-256 thumbprint of the public cert body, base64url-encoded.

        Matches the algorithm shown in Mastercard's authentication docs:
        strip PEM armour + whitespace, base64-decode to DER, SHA-256, base64url.
        """
        if self._kid is not None:
            return self._kid
        if not os.path.isfile(self.public_cert_path):
            raise RuntimeError(
                f"Open Finance EU public cert not found: {self.public_cert_path}"
            )
        with open(self.public_cert_path, "rb") as f:
            pem = f.read()
        # Validate it's a real cert (raises if malformed).
        load_pem_x509_certificate(pem)
        # Strip headers/footers/whitespace, base64-decode to DER bytes.
        body = (
            pem.decode("ascii")
            .replace("-----BEGIN CERTIFICATE-----", "")
            .replace("-----END CERTIFICATE-----", "")
        )
        body = "".join(body.split())
        der = base64.b64decode(body)
        digest = hashlib.sha256(der).digest()
        self._kid = _b64url(digest)
        return self._kid

    def _build_jwt(self) -> str:
        header = {"alg": "RS256", "typ": "JWT", "kid": self._compute_kid()}
        now = int(time.time())
        payload = {
            "sub": self.client_id,
            "iss": self.client_id,
            "aud": self.JWT_AUDIENCE,
            "exp": now + 300,  # 5 min; JWT is single-use for token request
            "iat": now,
            "jti": str(uuid.uuid4()),
        }
        h = _b64url(json.dumps(header, separators=(",", ":")).encode("utf-8"))
        p = _b64url(json.dumps(payload, separators=(",", ":")).encode("utf-8"))
        signing_input = f"{h}.{p}".encode("ascii")
        signature = self._load_private_key().sign(
            signing_input,
            padding.PKCS1v15(),
            hashes.SHA256(),
        )
        return f"{h}.{p}.{_b64url(signature)}"

    # ------------------------------------------------------------------
    # Token
    # ------------------------------------------------------------------
    def _get_token(self, force_refresh: bool = False,
                   scopes: list[str] | None = None) -> str:
        # Reuse cached token until 5 min before expiry.
        if not force_refresh and self._token and time.time() < (self._token_expiry - 300):
            return self._token

        assertion = self._build_jwt()
        url = f"{self.auth_base_url}/oauth2/token"
        form = {
            "grant_type": "client_credentials",
            "client_assertion_type":
                "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
            "client_assertion": assertion,
            "scope": " ".join(scopes or ["ob_data", "ob_providers"]),
        }
        # NB: Mastercard's /oauth2/token expects a JSON body, not the
        # standard OAuth 2.0 ``application/x-www-form-urlencoded``. Sending
        # form-encoded yields:
        #   FORMAT_ERROR — Content-Type ... does not match ... [application/json]
        headers = {"Content-Type": "application/json",
                   "Accept": "application/json"}

        # Mask the JWT assertion in the captured request for UI display.
        masked = dict(form)
        masked["client_assertion"] = assertion[:24] + "..." + assertion[-12:]
        self._last_request = {"method": "POST", "url": url,
                              "headers": dict(headers), "body": masked}

        resp = requests.post(url, headers=headers, json=form, timeout=30)
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
            raise RuntimeError(
                f"Open Finance EU token request failed ({resp.status_code}): {body}"
            )
        token = (body or {}).get("access_token") if isinstance(body, dict) else None
        expires_in = (body or {}).get("expires_in", 3600) if isinstance(body, dict) else 3600
        if not token:
            raise RuntimeError("Open Finance EU token response missing 'access_token'")
        self._token = token
        self._token_expiry = time.time() + int(expires_in)
        return token

    # ------------------------------------------------------------------
    # Authenticated request
    # ------------------------------------------------------------------
    def _request(
        self,
        method: str,
        endpoint: str,
        *,
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        scopes: list[str] | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> tuple[Any, int]:
        token = self._get_token(scopes=scopes)
        url = f"{self.api_base_url}{endpoint}"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
        }
        if data is not None:
            headers["Content-Type"] = "application/json"
        # Consent Machine + downstream APIs require X-Application-Id on every
        # call. Missing this returns:
        #   BAD_REQUEST — Required request header 'X-Application-Id' for
        #   method parameter type UUID is not present
        if self.application_id:
            headers["X-Application-Id"] = self.application_id
        if extra_headers:
            headers.update(extra_headers)

        masked = dict(headers)
        masked["Authorization"] = f"Bearer {token[:10]}..."
        self._last_request = {"method": method, "url": url, "headers": masked,
                              "body": data, "params": params}

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
    def create_token(self) -> tuple[dict[str, Any], int]:
        """Force a fresh access token. Smoke-test op — needs only clientId+key."""
        self._token = None
        token = self._get_token(force_refresh=True)
        return ({"access_token": token[:12] + "...",
                 "token_type": "bearer",
                 "kid": self._compute_kid(),
                 "message": "Token created successfully"}, 200)

    def get_providers(self, country: str = "", limit: int = 25) -> tuple[Any, int]:
        params: dict[str, Any] = {"limit": limit}
        if country:
            params["country"] = country
        return self._request("GET", "/providers", params=params,
                             scopes=["ob_providers"])

    def get_provider_groups(self, country: str = "") -> tuple[Any, int]:
        params = {"country": country} if country else None
        return self._request("GET", "/provider-groups", params=params,
                             scopes=["ob_providers"])

    def create_consent(
        self,
        use_case_configuration_id: str,
        end_user_id: str,
        end_user_email: str,
        idempotency_key: str | None = None,
    ) -> tuple[Any, int]:
        """POST /consents per the Mastercard Open Finance Europe docs.

        Body shape (verified from the Account Opening Guide cURL sample
        and the live sandbox 400 response, which rejects payloads without
        an email on each end user):
            {"useCaseConfigurationId": "...",
             "endUsers": [{"identifier": "...", "email": "..."}]}

        The provider/bank is chosen later by the End User inside the Aiia
        managed flow UI — it is *not* part of the consent creation body.
        """
        body: dict[str, Any] = {
            "useCaseConfigurationId": use_case_configuration_id,
            "endUsers": [{
                "identifier": end_user_id,
                "email": end_user_email,
            }],
        }
        headers = {"Idempotency-Key": idempotency_key or str(uuid.uuid4())}
        return self._request("POST", "/consents", data=body,
                             scopes=["ob_data"], extra_headers=headers)

    def get_consent(self, consent_id: str) -> tuple[Any, int]:
        return self._request("GET", f"/consents/{consent_id}", scopes=["ob_data"])

    def revoke_consent(self, consent_id: str) -> tuple[Any, int]:
        return self._request("DELETE", f"/consents/{consent_id}",
                             scopes=["ob_data"])

    def create_managed_flow(
        self,
        consent_id: str,
        end_user_id: str,
        flow_type: str = "CONNECT_ACCOUNTS",
        language: str = "en",
        provider_id: str = "",
    ) -> tuple[Any, int]:
        """POST /consents/{consent_id}/managed-flows per the official docs.

        Body shape (verified):
            {"type": "CONNECT_ACCOUNTS",
             "endUser": {"identifier": "..."},
             "language": "en"}

        Redirect URLs are configured at app-onboarding time by Mastercard
        (the URL the partner emails alongside the public cert), not per-call.
        ``provider_id`` is sent as a soft hint when supplied — Aiia may use
        it to skip the bank-selection step, but it is silently ignored if
        not supported by the current tenant configuration.
        """
        body: dict[str, Any] = {
            "type": flow_type,
            "endUser": {"identifier": end_user_id},
            "language": language,
        }
        if provider_id:
            body["providerId"] = provider_id
        return self._request(
            "POST", f"/consents/{consent_id}/managed-flows",
            data=body, scopes=["ob_data"],
        )

    def get_accounts(self, consent_id: str,
                     include: str = "balances,holders,identifiers,additionalInformation",
                     limit: int = 10, offset: int = 0) -> tuple[Any, int]:
        """GET /data/accounts — the X-Consent-Id header scopes the call to
        the End User who granted the consent. The ``include`` query expands
        the response with optional sub-resources.
        """
        params: dict[str, Any] = {"include": include, "limit": limit, "offset": offset}
        return self._request("GET", "/data/accounts", params=params,
                             scopes=["ob_data"],
                             extra_headers={"X-Consent-Id": consent_id})

    def get_account(self, account_id: str, consent_id: str) -> tuple[Any, int]:
        return self._request("GET", f"/data/accounts/{account_id}",
                             scopes=["ob_data"],
                             extra_headers={"X-Consent-Id": consent_id})

    def get_transactions(self, account_id: str, consent_id: str,
                         from_date: str = "", to_date: str = "",
                         limit: int = 50) -> tuple[Any, int]:
        params: dict[str, Any] = {"limit": limit}
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date
        return self._request("GET", f"/data/accounts/{account_id}/transactions",
                             params=params, scopes=["ob_data"],
                             extra_headers={"X-Consent-Id": consent_id})

    def check_balance(self, account_id: str, consent_id: str,
                      max_age: str = "PT15M") -> tuple[Any, int]:
        # The Accounts API requires a freshness policy. ``PT0S`` forces a live
        # provider call; any other ISO 8601 duration (e.g. ``PT15M``) lets the
        # service return the cached balance if it is fresher than ``maxAge``.
        body = {"freshness": {"maxAge": max_age or "PT15M"}}
        headers = {
            "X-Consent-Id": consent_id,
            "Idempotency-Key": str(uuid.uuid4()),
        }
        return self._request("POST", f"/data/accounts/{account_id}/balance-checks",
                             data=body, scopes=["ob_data"],
                             extra_headers=headers)

    def verify_account_ownership(self, consent_id: str, customer_name: str,
                                 account_ids: list[str] | None = None
                                 ) -> tuple[Any, int]:
        # The Insights API lives under the ``/insights`` server prefix and
        # expects ``customerName`` (string) plus optional ``accountIds``
        # (array of UUIDs). Omitting ``accountIds`` matches against every
        # authorized account on the consent.
        body: dict[str, Any] = {"customerName": customer_name}
        if account_ids:
            body["accountIds"] = [a for a in account_ids if a]
        return self._request("POST", "/insights/account-ownership-verifications",
                             data=body, scopes=["ob_data"],
                             extra_headers={"X-Consent-Id": consent_id})

    def get_account_ownership_verification(self, verification_id: str,
                                           consent_id: str
                                           ) -> tuple[Any, int]:
        return self._request("GET",
                             f"/insights/account-ownership-verifications/{verification_id}",
                             scopes=["ob_data"],
                             extra_headers={"X-Consent-Id": consent_id})
