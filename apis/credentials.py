"""Centralised credential loader.

Every API's credentials are derived from a single env-var prefix declared in
``apis/catalog.py``.  Modules call ``load_credentials(api_id)`` instead of
poking ``os.environ`` directly — that way the env-var names are defined in
exactly one place (the catalog) and all downstream code is rename-safe.

The returned dict's keys are the *semantic* names of the fields (e.g.
``consumer_key``, ``signing_key_path``, ``partner_id``).  The credential
schema depends on the API's ``auth`` type:

    AUTH_OAUTH1 / AUTH_OAUTH1_ENC:
        consumer_key, signing_key_path, signing_key_alias,
        signing_key_password, env, [encryption_key_path]

    AUTH_OAUTH2:
        partner_id, partner_secret, app_key, api_base_url, sig_key_path

Multi-instance hook
-------------------
A reserved (currently unused) convention supports multiple instances per API,
e.g. ``OPEN_FINANCE_INSTANCES=us,eu`` would declare two instances and
``OPEN_FINANCE__US_PARTNER_ID`` / ``OPEN_FINANCE__EU_PARTNER_ID`` would carry
the per-instance secrets.  ``load_credentials(api_id, instance="us")`` would
then resolve them.  Today, ``instance`` is accepted but only the default
(``instance is None``) path is exercised.
"""
from __future__ import annotations

import os
from typing import Any

from apis.catalog import (
    AUTH_JWT_RS256,
    AUTH_OAUTH1,
    AUTH_OAUTH1_ENC,
    AUTH_OAUTH2,
    ApiCatalogEntry,
)
from apis.catalog import (
    get as get_catalog_entry,
)

_SENTINEL_PLACEHOLDERS = {
    "",
    "your-consumer-key-here",
    "your_partner_id_here",
    "your_api_key_here",
    "your_app_key_here",
    "your_partner_secret_here",
    "your_client_id_here",
}


def _prefix(entry: ApiCatalogEntry, instance: str | None) -> str:
    """Return the env-var prefix for the default or a named instance."""
    if instance:
        return f"{entry.env_prefix}__{instance.upper()}"
    return entry.env_prefix


def _resolve_entry(api_id: str | ApiCatalogEntry) -> ApiCatalogEntry:
    if isinstance(api_id, ApiCatalogEntry):
        return api_id
    entry = get_catalog_entry(api_id)
    if entry is None:
        raise KeyError(f"Unknown API id: {api_id!r}")
    return entry


def _get(name: str, default: str = "") -> str:
    return os.environ.get(name, default).strip()


def load_credentials(api_id: str | ApiCatalogEntry, *, instance: str | None = None) -> dict[str, Any]:
    """Load credentials for ``api_id`` from environment variables.

    The returned dict keys depend on the entry's ``auth`` type.  See the
    module docstring for the full schema.  Missing values are returned as
    empty strings so callers can compute ``configured`` cheaply.
    """
    entry = _resolve_entry(api_id)
    prefix = _prefix(entry, instance)

    if entry.auth in (AUTH_OAUTH1, AUTH_OAUTH1_ENC):
        creds: dict[str, Any] = {
            "consumer_key":          _get(f"{prefix}_CONSUMER_KEY"),
            "signing_key_path":      _get(f"{prefix}_SIGNING_KEY_PATH"),
            "signing_key_alias":     _get(f"{prefix}_SIGNING_KEY_ALIAS"),
            "signing_key_password":  _get(f"{prefix}_SIGNING_KEY_PASSWORD", "keystorepassword"),
            "env":                   _get(f"{prefix}_ENV", "sandbox").lower(),
        }
        if entry.auth == AUTH_OAUTH1_ENC:
            creds["encryption_key_path"] = _get(f"{prefix}_ENCRYPTION_KEY_PATH")
        return creds

    if entry.auth == AUTH_OAUTH2:
        return {
            "partner_id":     _get(f"{prefix}_PARTNER_ID"),
            "partner_secret": _get(f"{prefix}_PARTNER_SECRET"),
            "app_key":        _get(f"{prefix}_APP_KEY"),
            "api_base_url":   _get(f"{prefix}_API_BASE_URL", "https://api.finicity.com"),
            "sig_key_path":   _get(f"{prefix}_SIG_KEY_PATH"),
        }

    if entry.auth == AUTH_JWT_RS256:
        # OAuth 2.0 client_credentials with an RS256-signed JWT client
        # assertion (Mastercard Aiia / Open Finance Europe). Onboarding is
        # manual — an officer adds the partner's public RSA cert to a trust
        # list and returns a ``client_id``; nothing is provisionable from
        # the developer portal.
        return {
            "client_id":                 _get(f"{prefix}_CLIENT_ID"),
            "private_key_path":          _get(f"{prefix}_PRIVATE_KEY_PATH"),
            "public_cert_path":          _get(f"{prefix}_PUBLIC_CERT_PATH"),
            "application_id":            _get(f"{prefix}_APPLICATION_ID"),
            "use_case_configuration_id": _get(f"{prefix}_USE_CASE_ID"),
            "redirect_url":              _get(f"{prefix}_REDIRECT_URL"),
            "auth_base_url":             _get(f"{prefix}_AUTH_BASE_URL"),
            "api_base_url":              _get(f"{prefix}_API_BASE_URL"),
        }

    raise ValueError(f"Unknown auth scheme {entry.auth!r} for {entry.id}")


def is_configured(api_id: str | ApiCatalogEntry, *, instance: str | None = None) -> bool:
    """Return ``True`` if the minimum credentials for an API are present."""
    entry = _resolve_entry(api_id)
    creds = load_credentials(entry, instance=instance)

    if entry.auth in (AUTH_OAUTH1, AUTH_OAUTH1_ENC):
        return (
            creds["consumer_key"] not in _SENTINEL_PLACEHOLDERS
            and creds["signing_key_path"] not in _SENTINEL_PLACEHOLDERS
        )
    if entry.auth == AUTH_OAUTH2:
        return all(
            creds[k] not in _SENTINEL_PLACEHOLDERS
            for k in ("partner_id", "partner_secret", "app_key")
        )
    if entry.auth == AUTH_JWT_RS256:
        return all(
            creds[k] not in _SENTINEL_PLACEHOLDERS
            for k in ("client_id", "private_key_path", "public_cert_path")
        )
    return False


__all__ = ["load_credentials", "is_configured"]
