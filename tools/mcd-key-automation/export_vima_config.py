#!/usr/bin/env python3
"""
export_vima_config.py — Build a vima-config.zip from the latest provisioned keys.

The zip has the layout that vima's /config/import endpoint expects:

    config/.env           — all API env vars pointing to config/keys/<file>
    config/keys/*.p12     — OAuth 1.0a signing keystores
    config/keys/*.pem     — PEM keys (encryption certs, OAuth 2.0 sig-verification)

Usage:
    python export_vima_config.py [--normalized-dir temp/normalized] \
                                 [--password foobar!!] \
                                 [--output output/vima-config.zip]
"""
from __future__ import annotations

import argparse
import io
import json
import os
import re
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import Optional

_SLUG_RE = re.compile(r"[^a-z0-9]+")


def _slug(value: str) -> str:
    """Convert an API id to its hyphenated slug form as used in filenames."""
    return _SLUG_RE.sub("-", value.lower()).strip("-")

# Make the vima repo importable so we can read the canonical API catalog.
_HERE = Path(__file__).resolve().parent
if str(_HERE / "app") not in sys.path:
    sys.path.insert(0, str(_HERE))
from app._vima_catalog import (  # noqa: E402
    AUTH_OAUTH1,
    AUTH_OAUTH1_ENC,
    AUTH_OAUTH2,
    iter_ordered,
)


# ---------------------------------------------------------------------------
# API mapping: mcd-key-automation api_id (legacy) → vima .env prefix + key filenames
# ---------------------------------------------------------------------------
# Built from apis.catalog so every API is described in exactly one place.
# Each entry: (vima_prefix, p12_dest_name, pem_env_var | None, pem_dest_name | None)

API_MAP: dict[str, tuple[str, str, Optional[str], Optional[str]]] = {}
OFIN_IDS: list[str] = []  # all aliases (legacy + canonical) to probe for OFin artifacts
OFIN_PREFIX: str = "OPEN_FINANCE"

for _entry in iter_ordered():
    _aliases = [_entry.id]
    if _entry.legacy_id and _entry.legacy_id != _entry.id:
        _aliases.append(_entry.legacy_id)
    if _entry.auth == AUTH_OAUTH2:
        # OAuth 2.0 (Open Finance) is handled in its own block below.
        OFIN_IDS = _aliases
        OFIN_PREFIX = _entry.env_prefix
        continue
    _p12_dest = f"{_entry.id}.p12"
    if _entry.auth == AUTH_OAUTH1_ENC:
        _pem_env = f"{_entry.env_prefix}_ENCRYPTION_KEY_PATH"
        _pem_dest = f"{_entry.id}-clientenc.pem"
    else:
        _pem_env = None
        _pem_dest = None
    # Register under both ids so artifacts produced by old or new YAML configs resolve.
    for _alias in _aliases:
        API_MAP[_alias] = (_entry.env_prefix, _p12_dest, _pem_env, _pem_dest)


def _newest(paths: list[Path]) -> Optional[Path]:
    return max(paths, key=lambda p: p.stat().st_mtime) if paths else None


def _aliases_for_entry(entry) -> list[str]:
    out = [entry.id]
    if entry.legacy_id and entry.legacy_id != entry.id:
        out.append(entry.legacy_id)
    return out


def _find_credentials(api_id: str, normalized: Path) -> Optional[Path]:
    slug = _slug(api_id)
    return _newest(list(normalized.glob(f"*-{slug}-signing-v1-credentials.json")))


def _find_credentials_any(aliases: list[str], normalized: Path) -> tuple[Optional[Path], Optional[str]]:
    """Return (path, alias_that_matched) for the newest credentials JSON across all aliases."""
    best: tuple[Optional[Path], Optional[str]] = (None, None)
    for alias in aliases:
        p = _find_credentials(alias, normalized)
        if p and (best[0] is None or p.stat().st_mtime > best[0].stat().st_mtime):
            best = (p, alias)
    return best


def _find_zip(api_id: str, normalized: Path, cred_path: Optional[Path]) -> Optional[Path]:
    if cred_path:
        candidate = cred_path.parent / cred_path.name.replace("-credentials.json", ".zip")
        if candidate.exists():
            return candidate
    slug = _slug(api_id)
    return _newest(list(normalized.glob(f"*-{slug}-signing-v1.zip")))
    return _newest(list(normalized.glob(f"*-{api_id}-signing-v1.zip")))


def _find_pem(api_id: str, normalized: Path, cred_path: Optional[Path]) -> Optional[Path]:
    if cred_path:
        # Try sibling PEM with same base name (signing-named PEMs from old runs).
        candidate = cred_path.parent / cred_path.name.replace("-credentials.json", ".pem")
        if candidate.exists():
            return candidate
    slug = _slug(api_id)
    # New naming: encryption PEM saved with -enc- purpose marker.
    enc_pem = _newest(list(normalized.glob(f"*-{slug}-enc-v1.pem")))
    if enc_pem:
        return enc_pem
    # Legacy fallback: PEM saved with -signing- marker (old runs).
    return _newest(list(normalized.glob(f"*-{slug}-signing-v1.pem")))


def _extract_p12_bytes(zip_path: Path) -> tuple[bytes, str]:
    """Return (p12_bytes, original_filename) from inside the signing zip."""
    with zipfile.ZipFile(zip_path) as zf:
        for name in zf.namelist():
            if name.lower().endswith(".p12") or name.lower().endswith(".pkcs12"):
                return zf.read(name), name
    raise ValueError(f"No .p12 file found inside {zip_path}")


def build_vima_config_zip(
    normalized_dir: Path,
    password: str,
    output_path: Path,
) -> dict:
    """
    Build output_path (a zip) consumable by vima /config/import.
    Returns a summary dict of what was included.
    """
    env_lines: list[str] = ["# Generated by mcd-key-automation export_vima_config.py", ""]
    included: dict[str, list[str]] = {"apis": [], "skipped": []}

    # Collect all files to put into config/keys/
    key_files: dict[str, bytes] = {}  # dest_name → bytes

    # -----------------------------------------------------------------------
    # OAuth 1.0a APIs — walk catalog, probe each entry's aliases for artifacts
    # -----------------------------------------------------------------------
    for entry in iter_ordered():
        if entry.auth == AUTH_OAUTH2:
            continue  # handled below
        aliases = _aliases_for_entry(entry)
        cred_path, matched_alias = _find_credentials_any(aliases, normalized_dir)
        if not cred_path or matched_alias is None:
            included["skipped"].append(f"{entry.id} (no credentials JSON)")
            continue

        prefix = entry.env_prefix
        p12_dest = f"{entry.id}.p12"

        creds = json.loads(cred_path.read_text())
        consumer_key = creds.get("consumer_key", "")
        key_alias = creds.get("key_alias", matched_alias)

        zip_path = _find_zip(matched_alias, normalized_dir, cred_path)
        if not zip_path:
            included["skipped"].append(f"{entry.id} (no signing ZIP)")
            continue

        try:
            p12_bytes, _ = _extract_p12_bytes(zip_path)
        except ValueError as e:
            included["skipped"].append(f"{entry.id} ({e})")
            continue

        key_files[p12_dest] = p12_bytes

        env_lines += [
            f"# {prefix}",
            f"{prefix}_CONSUMER_KEY={consumer_key}",
            f"{prefix}_SIGNING_KEY_PATH=config/keys/{p12_dest}",
            f"{prefix}_SIGNING_KEY_ALIAS={key_alias}",
            f"{prefix}_SIGNING_KEY_PASSWORD={password}",
            f"{prefix}_ENV=sandbox",
        ]

        # Optional client encryption PEM
        if entry.auth == AUTH_OAUTH1_ENC:
            pem_env = f"{prefix}_ENCRYPTION_KEY_PATH"
            pem_dest = f"{entry.id}-clientenc.pem"
            pem_path = _find_pem(matched_alias, normalized_dir, cred_path)
            if pem_path:
                key_files[pem_dest] = pem_path.read_bytes()
                env_lines.append(f"{pem_env}=config/keys/{pem_dest}")
            else:
                env_lines.append(f"{pem_env}=")

        env_lines.append("")
        included["apis"].append(entry.id)

    # -----------------------------------------------------------------------
    # OAuth 2.0 APIs (Open Finance — US, AU, …) — Finicity-style credentials.
    # Iterate over every OAuth2 entry so multi-region tenants (e.g. the AU
    # variant alongside the US one) each get their own env block.
    # -----------------------------------------------------------------------
    _DEFAULT_OAUTH2_BASE_URL: dict[str, str] = {
        "open_finance":    "https://api.finicity.com",
        "open_finance_au": "https://api.openbanking.mastercard.com.au",
    }
    for ofin_entry in [e for e in iter_ordered() if e.auth == AUTH_OAUTH2]:
        cred_path, matched_alias = _find_credentials_any(
            _aliases_for_entry(ofin_entry), normalized_dir
        )
        if not cred_path:
            included["skipped"].append(f"{ofin_entry.id} (no credentials JSON)")
            continue

        creds = json.loads(cred_path.read_text())
        partner_id = creds.get("partner_id", "")
        app_key    = creds.get("app_key", "")
        secret     = creds.get("secret", "")

        base_url = _DEFAULT_OAUTH2_BASE_URL.get(
            ofin_entry.id, "https://api.finicity.com"
        )

        pem_path = _find_pem(matched_alias, normalized_dir, cred_path)
        env_lines += [
            f"# {ofin_entry.env_prefix} ({ofin_entry.display_name} — OAuth 2.0)",
            f"{ofin_entry.env_prefix}_PARTNER_ID={partner_id}",
            f"{ofin_entry.env_prefix}_PARTNER_SECRET={secret}",
            f"{ofin_entry.env_prefix}_APP_KEY={app_key}",
            f"{ofin_entry.env_prefix}_API_BASE_URL={base_url}",
        ]
        if pem_path:
            pem_dest = f"{ofin_entry.id}-sig-verification.pem"
            key_files[pem_dest] = pem_path.read_bytes()
            env_lines.append(f"{ofin_entry.env_prefix}_SIG_KEY_PATH=config/keys/{pem_dest}")
        env_lines.append("")
        included["apis"].append(ofin_entry.id)

    # -----------------------------------------------------------------------
    # CLAUDE / VIMA CHAT — preserve existing key if present on disk
    # -----------------------------------------------------------------------
    anthropic_key = os.environ.get("ANTHROPIC_API_KEY", "your_api_key_here")
    env_lines += [
        "# CLAUDE / VIMA CHAT",
        f"ANTHROPIC_API_KEY={anthropic_key}",
        "",
    ]

    # -----------------------------------------------------------------------
    # Write zip
    # -----------------------------------------------------------------------
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("config/.env", "\n".join(env_lines))
        for dest_name, data in key_files.items():
            zf.writestr(f"config/keys/{dest_name}", data)

    return included


def main():
    parser = argparse.ArgumentParser(description="Build vima-config.zip from latest provisioned keys")
    parser.add_argument("--normalized-dir", default="temp/normalized",
                        help="Path to temp/normalized directory")
    parser.add_argument("--password", default="foobar!!",
                        help="Keystore password used when creating keys (default: foobar!!)")
    parser.add_argument("--output", default="output/vima-config.zip",
                        help="Output zip path (default: output/vima-config.zip)")
    args = parser.parse_args()

    normalized_dir = Path(args.normalized_dir).resolve()
    if not normalized_dir.exists():
        print(f"ERROR: normalized dir not found: {normalized_dir}", file=sys.stderr)
        sys.exit(1)

    output_path = Path(args.output)
    result = build_vima_config_zip(normalized_dir, args.password, output_path)

    print(f"\nBuilt: {output_path.resolve()}")
    print(f"  Included APIs : {', '.join(result['apis'])}")
    if result["skipped"]:
        print(f"  Skipped       : {', '.join(result['skipped'])}")
    print(f"\nImport into vima via Settings → Import Config, or:")
    print(f"  curl -X POST http://localhost:5001/config/import -F file=@{output_path.resolve()}")


if __name__ == "__main__":
    main()
