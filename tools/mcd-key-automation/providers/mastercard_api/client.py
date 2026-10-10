"""Mastercard **Developers API** client (Option B — API-based provisioning).

Thin, dependency-light REST client for the documented Mastercard Developers
API (https://developer.mastercard.com/mastercard-developers-api). It mirrors
the Developers Dashboard: list services, create/list/delete projects, add
services to a project environment, and manage credentials — all without
driving the portal UI.

Auth: OAuth 1.0a, signed with the same ``mastercard-oauth1-signer`` (``oauth1``)
library VIMA already uses for every other Mastercard API. Bootstrap the
credential once with ``provision-admin-key`` (keystore) + the consumer key.

Base URL (per Mastercard's client-generation tutorial):
    https://apiedge.mastercard.com/developers
The environment (SANDBOX / PRODUCTION) is selected per project/request body,
not by host, so a single base URL serves both.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import requests

DEFAULT_BASE_URL = "https://apiedge.mastercard.com/developers"


class DevelopersApiError(RuntimeError):
    """Raised when the Developers API returns a non-2xx response."""

    def __init__(self, status_code: int, method: str, url: str, body: Any) -> None:
        self.status_code = status_code
        self.method = method
        self.url = url
        self.body = body
        super().__init__(f"{method} {url} -> {status_code}: {body}")


@dataclass
class DevelopersApiClient:
    consumer_key: str
    signing_key_path: str
    key_password: str
    base_url: str = DEFAULT_BASE_URL
    timeout: float = 30.0

    def __post_init__(self) -> None:
        # Resolve a relative keystore path against the VIMA repo root so callers
        # can pass "config/keys/mcd-developers-api.p12" like the rest of VIMA.
        p = Path(self.signing_key_path)
        if not p.is_absolute():
            # client.py lives at tools/mcd-key-automation/providers/mastercard_api/;
            # parents[4] is the VIMA repo root (config/keys/... is relative to it).
            repo_root = Path(__file__).resolve().parents[4]
            p = repo_root / self.signing_key_path
        self._key_file = str(p)
        self._signing_key = None  # lazy-loaded

    # ------------------------------------------------------------------ factory
    @classmethod
    def from_env(cls, *, base_url: str | None = None) -> "DevelopersApiClient":
        """Build a client from MCD_DEVELOPERS_API_* environment variables."""
        consumer_key = os.environ.get("MCD_DEVELOPERS_API_CONSUMER_KEY", "").strip()
        key_path = os.environ.get("MCD_DEVELOPERS_API_SIGNING_KEY_PATH", "").strip()
        password = os.environ.get("MCD_DEVELOPERS_API_SIGNING_KEY_PASSWORD", "keystorepassword").strip()
        if not consumer_key or not key_path:
            raise RuntimeError(
                "Developers API credentials missing. Set MCD_DEVELOPERS_API_CONSUMER_KEY "
                "and MCD_DEVELOPERS_API_SIGNING_KEY_PATH (run 'provision-admin-key' and "
                "'sync-admin-key' once the key is approved)."
            )
        return cls(
            consumer_key=consumer_key,
            signing_key_path=key_path,
            key_password=password,
            base_url=base_url or DEFAULT_BASE_URL,
        )

    # ------------------------------------------------------------------ signing
    def _load_key(self):
        if self._signing_key is None:
            import oauth1.authenticationutils as authutils
            self._signing_key = authutils.load_signing_key(self._key_file, self.key_password)
        return self._signing_key

    def _request(
        self, method: str, path: str, *, body: Any = None, params: dict | None = None
    ) -> Any:
        from oauth1.oauth import OAuth

        url = f"{self.base_url}{path}"
        if params:
            from urllib.parse import urlencode
            url = f"{url}?{urlencode(params)}"
        payload = json.dumps(body) if body is not None else ""
        signing_key = self._load_key()
        auth_header = OAuth.get_authorization_header(
            url, method, payload or "", self.consumer_key, signing_key
        )
        headers = {
            "Authorization": auth_header,
            "Accept": "application/json",
        }
        if body is not None:
            headers["Content-Type"] = "application/json"

        resp = requests.request(
            method, url, data=payload if body is not None else None,
            headers=headers, timeout=self.timeout,
        )
        try:
            parsed = resp.json() if resp.content else None
        except ValueError:
            parsed = {"raw": resp.text}
        if not (200 <= resp.status_code < 300):
            raise DevelopersApiError(resp.status_code, method, url, parsed)
        return parsed

    # ------------------------------------------------------------------ services
    def get_services(self, params: dict | None = None) -> Any:
        """GET /services — list all services (maps API name -> serviceId)."""
        return self._request("GET", "/services", params=params)

    def get_service(self, service_id: int | str) -> Any:
        """GET /services/{service_id}."""
        return self._request("GET", f"/services/{service_id}")

    def find_service_id(self, name_substring: str) -> int | None:
        """Return the serviceId whose name contains ``name_substring`` (case-insensitive)."""
        data = self.get_services()
        items = data.get("services", data) if isinstance(data, dict) else data
        needle = name_substring.lower()
        for svc in items or []:
            name = str(svc.get("name", "")).lower()
            if needle in name:
                return svc.get("id") or svc.get("serviceId")
        return None

    # ------------------------------------------------------------------ projects
    def get_projects(self) -> Any:
        """GET /projects — list your projects."""
        return self._request("GET", "/projects")

    def get_project(self, project_id: str) -> Any:
        """GET /projects/{project_id}."""
        return self._request("GET", f"/projects/{project_id}")

    def create_project(self, payload: dict) -> Any:
        """POST /projects — create a new project.

        Example payload (from Mastercard's tutorial)::

            {
              "type": "STANDARD",
              "name": "My BIN Lookup project",
              "environment": "SANDBOX",
              "service": {"serviceId": 1443},
              "credential": {"description": "vima", "type": "PARTNER"}
            }
        """
        return self._request("POST", "/projects", body=payload)

    def delete_project(self, project_id: str) -> Any:
        """DELETE /projects/{project_id}."""
        return self._request("DELETE", f"/projects/{project_id}")

    def create_project_environment(self, project_id: str, payload: dict) -> Any:
        """POST /projects/{project_id}/environments — add a Sandbox/Production env."""
        return self._request("POST", f"/projects/{project_id}/environments", body=payload)

    def add_service_to_environment(self, project_id: str, environment_name: str, payload: dict) -> Any:
        """POST /projects/{project_id}/environments/{environment_name}/services."""
        return self._request(
            "POST", f"/projects/{project_id}/environments/{environment_name}/services", body=payload
        )

    # ------------------------------------------------------------------ credentials
    def add_credential(self, project_id: str, payload: dict) -> Any:
        """POST /projects/{project_id}/credentials — add a credential/key."""
        return self._request("POST", f"/projects/{project_id}/credentials", body=payload)

    def revoke_credential(self, project_id: str, credential_id: str) -> Any:
        """DELETE /projects/{project_id}/credentials/{credential_id}."""
        return self._request("DELETE", f"/projects/{project_id}/credentials/{credential_id}")
