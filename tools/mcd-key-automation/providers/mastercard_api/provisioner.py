"""API-based provisioning via the Mastercard Developers admin key (Option B).

Provisions an OAuth 1.0a API end-to-end **without a browser**:

    1. POST /projects                       (type OAUTH10A + service{serviceId, config})
    2. generate an RSA keypair + CSR locally
    3. POST /projects/{id}/credentials       (SIGNING, nested credentialDetails) → consumerKey
    4. build a local PKCS#12 from the keypair (+ a self-signed cert) and write the
       artifacts (credentials JSON + signing zip) into ``temp/normalized`` using the
       SAME naming the browser path produces, so ``export_vima_config`` picks them
       up unchanged.

Scope: only APIs the Developers API can fully provision unattended —
``oauth1_standard`` services that either need no create-time config, or whose
config we know (``KNOWN_SERVICE_CONFIG``). Everything else (OAuth2/Open Finance,
encryption-key APIs, playbooks, priceless, sub-API selection, or an unknown
config schema) raises :class:`UnsupportedViaApi` so the caller falls back to the
browser flow, which reads the live schema from the portal.
"""
from __future__ import annotations

import datetime as _dt
import json
import os
import zipfile
from pathlib import Path
from typing import Any

from loguru import logger

from app.alias_engine import make_alias, make_filename
from app.models import DownloadedArtifact
from app.validators import classify_extension, sha256_file
from app._vima_catalog import AUTH_OAUTH1, AUTH_OAUTH1_ENC, AUTH_OAUTH2
from providers.mastercard_api.client import DevelopersApiClient, DevelopersApiError

# Services whose create-project call requires a `config` object. The Developers
# API exposes the service's ``configSchemaId`` but NOT the schema body, so we
# can't build an arbitrary config unattended — known services get sensible
# sandbox defaults; unknown ones fall back to the browser (which reads the live
# schema from the portal wizard).
KNOWN_SERVICE_CONFIG: dict[int, dict] = {
    1800: {  # BIN Lookup
        "customerSegment": "merchant",
        "intendedUse": ["paymentRouting"],
        "useCase": "Sandbox integration testing and evaluation of this API for a proof of concept.",
    },
    283: {  # Carbon Calculator (schema 97e6e6e9-…): customerId + scoreRetentionPeriod
        "customerId": "1",
        "scoreRetentionPeriod": "3",
    },
    2086: {  # MATCH Pro (schema 2302ed74-52a3-…). accessToBeUsedBy + acquirerICA +
             # isReplacingClientId are always required; acquirerContactEmail is
             # required for every company type except plain "Acquirer".
        "accessToBeUsedBy": "Internal MasterCard Partner",
        "acquirerICA": "123456789",
        "acquirerContactEmail": os.environ.get("MCD_PORTAL_EMAIL") or "developer@example.com",
        "isReplacingClientId": "No",
    },
    2245: {  # Business Payment Controls (schema 2302ed74-52ba-…): registration token.
        "regToken": "123456789",
    },
}

# Explicit Developers-API serviceId for APIs whose catalog display name doesn't
# match the service name closely enough (e.g. "Consent Management" -> "Consents").
_SERVICE_ID_BY_API: dict[str, int] = {
    "transaction_notifications": 2324,
    "consent_management": 2884,
    "automatic_billing_updater": 2088,
    "match": 2086,
    "business_payment_controls": 2245,
}

# How to obtain / configure the admin key. Printed on first launch when the key
# is not yet configured, so the tool is transparent about the fast path.
ADMIN_KEY_INSTRUCTIONS = """
============================================================================
 Mastercard Developers API key (optional — enables FAST, browser-free setup)
============================================================================
 This tool can provision most APIs directly through the Mastercard Developers
 API instead of driving the website with a browser. That requires a one-time
 "Developers API" admin key on your Mastercard Developers account:

   1. Sign in at https://developer.mastercard.com
   2. Open  Account  ->  (your profile)  ->  "API keys"  and add a key for the
      "Mastercard Developers API" (a.k.a. Developer Enablement) service.
   3. Generate the key, set a keystore password, and DOWNLOAD the .p12 keystore.
   4. Copy the .p12 to  config/keys/mcd-developers-api.p12  and note the
      Consumer Key shown on the key's row.
   5. Add to config/.env:
        MCD_DEVELOPERS_API_CONSUMER_KEY=<consumer key>
        MCD_DEVELOPERS_API_SIGNING_KEY_PATH=config/keys/mcd-developers-api.p12
        MCD_DEVELOPERS_API_SIGNING_KEY_PASSWORD=<keystore password>

   Or let the tool bootstrap it for you (drives the portal once):
        python -m app.main provision-admin-key --headful
        python -m app.main sync-admin-key     # once the key is Approved/Active

 Until it is configured, provisioning uses BROWSER AUTOMATION (Playwright).
============================================================================
"""


class UnsupportedViaApi(RuntimeError):
    """Raised when an API cannot be provisioned unattended via the Developers API."""


def is_admin_key_configured() -> bool:
    """True if the MCD_DEVELOPERS_API_* env vars look usable (not placeholders)."""
    ck = os.environ.get("MCD_DEVELOPERS_API_CONSUMER_KEY", "").strip()
    kp = os.environ.get("MCD_DEVELOPERS_API_SIGNING_KEY_PATH", "").strip()
    return bool(ck and kp and ck != "your_consumer_key_here")


def _make_p12(private_key, alias: str, password: str) -> bytes:
    """Serialise the private key + a self-signed cert into a PKCS#12 keystore.

    Only the private key is used to sign OAuth 1.0a requests; the self-signed
    cert is just a container so the .p12 is well-formed and loadable by the same
    ``oauth1.authenticationutils.load_signing_key`` used everywhere else.
    """
    from cryptography import x509
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.serialization import (
        BestAvailableEncryption,
        pkcs12,
    )
    from cryptography.x509.oid import NameOID

    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME, "MasterCardKey"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "MasterCard"),
    ])
    now = _dt.datetime.now(_dt.timezone.utc)
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(private_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - _dt.timedelta(days=1))
        .not_valid_after(now + _dt.timedelta(days=825))
        .sign(private_key, hashes.SHA256())
    )
    return pkcs12.serialize_key_and_certificates(
        name=alias.encode("utf-8"),
        key=private_key,
        cert=cert,
        cas=None,
        encryption_algorithm=BestAvailableEncryption(password.encode("utf-8")),
    )


def _make_csr(private_key) -> str:
    from cryptography import x509
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.x509.oid import NameOID

    csr = (
        x509.CertificateSigningRequestBuilder()
        .subject_name(x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, "MasterCardKey"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, "MasterCard"),
            x509.NameAttribute(NameOID.COUNTRY_NAME, "IE"),
        ]))
        .sign(private_key, hashes.SHA256())
    )
    return csr.public_bytes(serialization.Encoding.PEM).decode("ascii")


class ApiProvisioner:
    """Provisions supported APIs through the Mastercard Developers API."""

    def __init__(self, client: DevelopersApiClient) -> None:
        self.client = client
        self._services: list[dict] | None = None

    # ------------------------------------------------------------------ factory
    @classmethod
    def try_from_env(cls) -> "ApiProvisioner | None":
        """Build + validate a provisioner from env, or return None if unusable.

        Performs a single authenticated ``GET /services`` so a pending/declined
        admin key (401) transparently downgrades to the browser flow.
        """
        if not is_admin_key_configured():
            return None
        try:
            client = DevelopersApiClient.from_env()
            inst = cls(client)
            inst._load_services()  # validates auth
            return inst
        except (DevelopersApiError, RuntimeError, Exception) as exc:  # noqa: BLE001
            logger.warning(
                "Developers API admin key not usable ({}) — using browser flow.",
                getattr(exc, "status_code", type(exc).__name__),
            )
            return None

    # ------------------------------------------------------------------ services
    def _load_services(self) -> list[dict]:
        if self._services is None:
            data = self.client.get_services()
            self._services = data.get("services", data) if isinstance(data, dict) else data
        return self._services or []

    def _service_for(self, entry, api_id: str | None = None) -> dict | None:
        """Match a catalog entry to a Developers API service.

        Prefers an explicit serviceId override (``_SERVICE_ID_BY_API``) for APIs
        whose display name doesn't match the service name; otherwise matches by
        display name. Handles the regionalised Open Finance names: the catalog
        calls them "Open Finance US" / "Open Finance AU" while the Developers API
        service is just "Open Finance" (region is a separate create field).
        """
        services = self._load_services()
        override = _SERVICE_ID_BY_API.get(api_id or "")
        if override is not None:
            for svc in services:
                if int(svc.get("id") or svc.get("serviceId") or 0) == override:
                    return svc
        target = (getattr(entry, "display_name", "") or "").strip().lower()
        if not target:
            return None
        # Candidate names: the full display name, plus a variant with a trailing
        # region token removed ("open finance us" -> "open finance").
        candidates = [target]
        parts = target.split()
        if len(parts) > 1 and parts[-1] in {"us", "au", "eu", "uk", "usa", "europe"}:
            candidates.append(" ".join(parts[:-1]))
        for cand in candidates:
            for svc in services:
                if str(svc.get("name", "")).strip().lower() == cand:
                    return svc
        # Loose fallback: one name contained in the other.
        for svc in services:
            name = str(svc.get("name", "")).strip().lower()
            if name and (name in target or target in name):
                return svc
        return None

    @staticmethod
    def _sandbox_config_schema_id(svc: dict) -> str | None:
        for env in svc.get("environments", []) or []:
            if env.get("name") == "SANDBOX":
                return env.get("configSchemaId")
        return None

    # ------------------------------------------------------------------ support
    def supports(self, api_id: str, setup, entry) -> bool:
        """True if this API can be fully provisioned unattended via the API."""
        if setup is None or entry is None:
            return False
        svc = self._service_for(entry, api_id)
        if not svc:
            return False
        service_id = svc.get("id") or svc.get("serviceId")
        if not service_id:
            return False

        auth = getattr(entry, "auth", "")
        if auth == AUTH_OAUTH2:
            # Open Finance partner credentials (Finicity-style). The create call
            # accepts an empty config and returns partnerId/appKey/secret; a
            # region (US/AU) is required and comes from the ApiSetup.
            return getattr(setup, "provision_type", "") == "oauth2_region" and bool(
                getattr(setup, "region", None)
            )
        if auth in (AUTH_OAUTH1, AUTH_OAUTH1_ENC):
            # OAuth 1.0a signing-key APIs (with or without a client-encryption
            # key). We provision the SIGNING credential, which is all vima's
            # clients use — the JWE/client-encryption key is not exercised by the
            # generated clients (documented "not implemented"), so a signing-only
            # provision fully satisfies is_configured() without a downgrade.
            #
            # Excluded (need the browser or extra steps we can't do unattended):
            #   * match_inline — the legacy hard-coded MATCH flow (superseded);
            #   * Priceless (sub-API selection + API-owner approval).
            # MATCH Pro and Business Payment Controls use provision_type 'playbook'
            # but ARE supported here now that their create-time config schemas are
            # known (KNOWN_SERVICE_CONFIG 2086 / 2245) — the config gate below lets
            # them through and rejects any other playbook API we don't have a
            # config for.
            ptype = getattr(setup, "provision_type", "")
            if ptype in ("match_inline", "priceless"):
                return False
            schema_id = self._sandbox_config_schema_id(svc)
            if schema_id and int(service_id) not in KNOWN_SERVICE_CONFIG:
                # Needs a config we can't build unattended — let the browser read it.
                return False
            return True
        return False

    @staticmethod
    def _region_code(setup) -> str:
        """Map the ApiSetup region display name to the API's region code (US/AU/…)."""
        region = (getattr(setup, "region", "") or "").strip().lower()
        return {
            "united states of america": "US",
            "australia": "AU",
            "united kingdom": "UK",
            "europe": "EU",
        }.get(region, region.upper() or "US")

    # ------------------------------------------------------------------ provision
    def provision(
        self,
        *,
        api_id: str,
        entry,
        setup,
        project_name: str,
        portal_project_name: str,
        organization: str,
        environment: str,
        key_password: str,
        dest_dir: Path,
    ) -> list[DownloadedArtifact]:
        """Provision the API and write normalized artifacts (dispatches by auth type)."""
        if getattr(entry, "auth", "") == AUTH_OAUTH2:
            return self._provision_oauth2_partner(
                api_id=api_id, entry=entry, setup=setup, project_name=project_name,
                portal_project_name=portal_project_name, organization=organization,
                environment=environment, dest_dir=dest_dir,
            )
        return self._provision_oauth1_signing(
            api_id=api_id, entry=entry, project_name=project_name,
            portal_project_name=portal_project_name, organization=organization,
            environment=environment, key_password=key_password, dest_dir=dest_dir,
        )

    def _provision_oauth2_partner(
        self,
        *,
        api_id: str,
        entry,
        setup,
        project_name: str,
        portal_project_name: str,
        organization: str,
        environment: str,
        dest_dir: Path,
    ) -> list[DownloadedArtifact]:
        """Open Finance (OAuth 2.0 / partner) — create the project + PARTNER credential.

        The Developers API returns the Finicity-style partnerId / appKey / secret
        inline. The Mastercard Signature Verification key (a portal-only download)
        is NOT fetched — the US Open Finance client doesn't require it.
        """
        svc = self._service_for(entry, api_id)
        if not svc:
            raise UnsupportedViaApi(f"no Developers API service found for {api_id!r}")
        service_id = int(svc.get("id") or svc.get("serviceId"))
        env_name = "SANDBOX" if environment.lower() == "sandbox" else "PRODUCTION"
        region = self._region_code(setup)

        proj = self.client.create_project({
            "type": "OPEN_BANKING_PARTNER",
            "name": portal_project_name,
            "environment": env_name,
            "region": region,
            "service": {"serviceId": service_id, "config": {}},
            "credential": {"type": "PARTNER", "description": "vima"},
        })

        partner_id = app_key = secret = ""
        for env in proj.get("environments", []) or []:
            for cr in env.get("credentials", []) or []:
                if cr.get("type") == "PARTNER":
                    partner_id = cr.get("partnerId", "") or partner_id
                    app_key = cr.get("appKey", "") or app_key
                    secrets = cr.get("secrets") or []
                    if secrets:
                        secret = secrets[0].get("secret", "") or secret
        if not (partner_id and app_key and secret):
            raise DevelopersApiError(500, "POST", "/projects", proj)

        normalized = dest_dir / "normalized"
        normalized.mkdir(parents=True, exist_ok=True)
        base_alias = make_alias(
            organization=organization, environment=environment,
            project=project_name, api=api_id, purpose="signing",
        )
        creds_alias = f"{base_alias}-credentials"
        creds_path = normalized / make_filename(creds_alias, "json")
        creds_path.write_text(json.dumps(
            {"partner_id": partner_id, "app_key": app_key, "secret": secret}, indent=2
        ))
        logger.info(
            "Developers API: created Open Finance project {} ({}) partner_id={}",
            proj.get("id"), region, partner_id,
        )
        return [self._artifact(creds_alias, creds_path, project_name, api_id)]

    def _provision_oauth1_signing(
        self,
        *,
        api_id: str,
        entry,
        project_name: str,
        portal_project_name: str,
        organization: str,
        environment: str,
        key_password: str,
        dest_dir: Path,
    ) -> list[DownloadedArtifact]:
        """Create the project + signing credential and write normalized artifacts."""
        from cryptography.hazmat.primitives.asymmetric import rsa

        svc = self._service_for(entry, api_id)
        if not svc:
            raise UnsupportedViaApi(f"no Developers API service found for {api_id!r}")
        service_id = int(svc.get("id") or svc.get("serviceId"))
        schema_id = self._sandbox_config_schema_id(svc)
        config = KNOWN_SERVICE_CONFIG.get(service_id, {}) if schema_id else {}

        env_name = "SANDBOX" if environment.lower() == "sandbox" else "PRODUCTION"

        # 1) create the project (service + optional config).
        create_body = {
            "type": "OAUTH10A",
            "name": portal_project_name,
            "environment": env_name,
            "service": {"serviceId": service_id, "config": config},
        }
        proj = self.client.create_project(create_body)
        project_id = proj.get("id")
        if not project_id:
            raise DevelopersApiError(500, "POST", "/projects", proj)

        # 2) keypair + CSR, 3) add the SIGNING credential.
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        # The Developers API requires the credential alias to be 8–75 chars, so
        # pad short api ids (e.g. "match") and clamp very long ones.
        alias = api_id if len(api_id) >= 8 else f"{api_id}-signing"
        alias = alias[:75]
        csr_pem = _make_csr(private_key)
        cred = self.client.add_credential(
            project_id,
            {
                "environment": env_name,
                "credentialDetails": {"type": "SIGNING", "alias": alias, "csr": csr_pem},
            },
        )
        details = cred.get("credentialDetails", cred) if isinstance(cred, dict) else {}
        consumer_key = details.get("consumerKey", "")
        if not consumer_key:
            raise DevelopersApiError(500, "POST", f"/projects/{project_id}/credentials", cred)

        # 4) build the .p12 + write normalized artifacts (same layout as browser path).
        p12_bytes = _make_p12(private_key, alias, key_password)
        normalized = dest_dir / "normalized"
        normalized.mkdir(parents=True, exist_ok=True)

        base_alias = make_alias(
            organization=organization,
            environment=environment,
            project=project_name,
            api=api_id,
            purpose="signing",
        )
        artifacts: list[DownloadedArtifact] = []

        # signing zip (contains <alias>.p12)
        zip_name = make_filename(base_alias, "zip")
        zip_path = normalized / zip_name
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.writestr(f"{alias}.p12", p12_bytes)
        artifacts.append(self._artifact(base_alias, zip_path, project_name, api_id))

        # credentials JSON
        creds_alias = f"{base_alias}-credentials"
        creds_name = make_filename(creds_alias, "json")
        creds_path = normalized / creds_name
        creds_path.write_text(json.dumps(
            {"consumer_key": consumer_key, "key_alias": alias}, indent=2
        ))
        artifacts.append(self._artifact(creds_alias, creds_path, project_name, api_id))

        logger.info(
            "Developers API: created project {} + signing key for '{}' (consumer_key={}…)",
            project_id, api_id, consumer_key[:12],
        )
        return artifacts

    @staticmethod
    def _artifact(alias: str, path: Path, project: str, api: str) -> DownloadedArtifact:
        return DownloadedArtifact(
            alias=alias,
            filename=path.name,
            path=str(path),
            sha256=sha256_file(path),
            kind=classify_extension(path.name),
            project=project,
            api=api,
        )
