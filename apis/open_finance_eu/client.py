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
from typing import Any, Dict, List, Optional, Tuple

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
    DEFAULT_API_BASE = "https://mtf.api.openbanking.mastercard.com"
    JWT_AUDIENCE = "auth.mastercard.com"

    def __init__(
        self,
        client_id: str,
        private_key_path: str,
        public_cert_path: str,
        auth_base_url: str = DEFAULT_AUTH_BASE,
        api_base_url: str = DEFAULT_API_BASE,
    ) -> None:
        self.client_id = client_id
        self.private_key_path = private_key_path
        self.public_cert_path = public_cert_path
        self.auth_base_url = auth_base_url.rstrip("/")
        self.api_base_url = api_base_url.rstrip("/")

        self._private_key: Optional[rsa.RSAPrivateKey] = None
        self._kid: Optional[str] = None
        self._token: Optional[str] = None
        self._token_expiry: float = 0.0
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
                   scopes: Optional[List[str]] = None) -> str:
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
        headers = {"Content-Type": "application/x-www-form-urlencoded",
                   "Accept": "application/json"}

        # Mask the JWT assertion in the captured request for UI display.
        masked = dict(form)
        masked["client_assertion"] = assertion[:24] + "..." + assertion[-12:]
        self._last_request = {"method": "POST", "url": url,
                              "headers": dict(headers), "body": masked}

        resp = requests.post(url, headers=headers, data=form, timeout=30)
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
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        scopes: Optional[List[str]] = None,
    ) -> Tuple[Any, int]:
        token = self._get_token(scopes=scopes)
        url = f"{self.api_base_url}{endpoint}"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
        }
        if data is not None:
            headers["Content-Type"] = "application/json"

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
    def create_token(self) -> Tuple[Dict[str, Any], int]:
        """Force a fresh access token. Smoke-test op — needs only clientId+key."""
        self._token = None
        token = self._get_token(force_refresh=True)
        return ({"access_token": token[:12] + "...",
                 "token_type": "bearer",
                 "kid": self._compute_kid(),
                 "message": "Token created successfully"}, 200)

    def get_providers(self, country: str = "", limit: int = 25) -> Tuple[Any, int]:
        params: Dict[str, Any] = {"limit": limit}
        if country:
            params["country"] = country
        return self._request("GET", "/providers", params=params,
                             scopes=["ob_providers"])

    def get_provider_groups(self, country: str = "") -> Tuple[Any, int]:
        params = {"country": country} if country else None
        return self._request("GET", "/provider-groups", params=params,
                             scopes=["ob_providers"])

    def create_consent(self, provider_id: str,
                       user_id: Optional[str] = None,
                       scopes: Optional[List[str]] = None,
                       redirect_url: str = "") -> Tuple[Any, int]:
        body: Dict[str, Any] = {
            "provider_id": provider_id,
            "scopes": scopes or ["accounts", "transactions", "balances"],
        }
        if user_id:
            body["user_id"] = user_id
        if redirect_url:
            body["redirect_url"] = redirect_url
        return self._request("POST", "/consents", data=body, scopes=["ob_data"])

    def get_consent(self, consent_id: str) -> Tuple[Any, int]:
        return self._request("GET", f"/consents/{consent_id}", scopes=["ob_data"])

    def revoke_consent(self, consent_id: str) -> Tuple[Any, int]:
        return self._request("DELETE", f"/consents/{consent_id}",
                             scopes=["ob_data"])

    def create_managed_flow(self, consent_id: str,
                            redirect_url: str = "",
                            language: str = "en") -> Tuple[Any, int]:
        body: Dict[str, Any] = {"language": language}
        if redirect_url:
            body["redirect_url"] = redirect_url
        return self._request(
            "POST", f"/consents/{consent_id}/managed-flows",
            data=body, scopes=["ob_data"],
        )

    def get_accounts(self, consent_id: Optional[str] = None) -> Tuple[Any, int]:
        params = {"consent_id": consent_id} if consent_id else None
        return self._request("GET", "/accounts", params=params, scopes=["ob_data"])

    def get_account(self, account_id: str) -> Tuple[Any, int]:
        return self._request("GET", f"/accounts/{account_id}", scopes=["ob_data"])

    def get_transactions(self, account_id: str,
                         from_date: str = "", to_date: str = "",
                         limit: int = 50) -> Tuple[Any, int]:
        params: Dict[str, Any] = {"limit": limit}
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date
        return self._request("GET", f"/accounts/{account_id}/transactions",
                             params=params, scopes=["ob_data"])

    def check_balance(self, account_id: str) -> Tuple[Any, int]:
        return self._request("POST", f"/accounts/{account_id}/balance-checks",
                             data={}, scopes=["ob_data"])

    def verify_account_ownership(self, account_id: str,
                                 expected_name: str = "") -> Tuple[Any, int]:
        body: Dict[str, Any] = {"account_id": account_id}
        if expected_name:
            body["expected_name"] = expected_name
        return self._request("POST", "/account-ownership-verifications",
                             data=body, scopes=["ob_data"])
