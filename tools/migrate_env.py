#!/usr/bin/env python3
"""Migrate config/.env from legacy API env-var prefixes to the formal ones.

Reads ``config/.env``, renames keys to their new prefixes (per ``apis.catalog``
+ a few explicit special cases), writes a backup, then overwrites the file.

Usage:
    python tools/migrate_env.py [--env config/.env] [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

# Add repo root so we can import the catalog.
_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from apis.catalog import LEGACY_TO_ID, CATALOG  # noqa: E402


def _build_prefix_map() -> list[tuple[str, str]]:
    """Build (old_prefix, new_prefix) pairs, sorted longest first."""
    pairs: list[tuple[str, str]] = []
    for legacy_id, new_id in LEGACY_TO_ID.items():
        entry = CATALOG[new_id]
        old_prefix = legacy_id.upper()
        # consumerclarity legacy id is "clarity" but env prefix was "CONSUMERCLARITY"
        # so we also need an explicit alias for that.
        if entry.env_prefix != old_prefix:
            pairs.append((old_prefix + "_", entry.env_prefix + "_"))
    # Explicit aliases for cases where the legacy env prefix didn't match
    # legacy_id.upper().
    pairs.append(("CONSUMERCLARITY_", "CONSUMER_CLARITY_"))
    # De-duplicate while preserving order.
    seen: set = set()
    dedup: list[tuple[str, str]] = []
    for p in pairs:
        if p not in seen:
            seen.add(p)
            dedup.append(p)
    # Longest first so e.g. CONSUMERCLARITY_ wins over CONSUMER_.
    dedup.sort(key=lambda x: len(x[0]), reverse=True)
    return dedup


# Bare OFin vars (no prefix in legacy .env) → OPEN_FINANCE_*
_BARE_OFIN: dict[str, str] = {
    "PARTNER_ID":              "OPEN_FINANCE_PARTNER_ID",
    "PARTNER_SECRET":          "OPEN_FINANCE_PARTNER_SECRET",
    "APP_KEY":                 "OPEN_FINANCE_APP_KEY",
    "API_BASE_URL":            "OPEN_FINANCE_API_BASE_URL",
    "OFIN_SIG_KEY_PATH":       "OPEN_FINANCE_SIG_KEY_PATH",
    "OFIN_DEFAULT_CUSTOMER_ID":"OPEN_FINANCE_DEFAULT_CUSTOMER_ID",
}

# One-off key renames where naming convention also changed (cert → key).
_EXPLICIT_KEY_RENAMES: dict[str, str] = {
    "BCES_ENCRYPTION_CERT_PATH": "BENEFITS_CONTENT_ELIGIBILITY_ENCRYPTION_KEY_PATH",
}


def migrate_key(key: str, prefix_map: list[tuple[str, str]]) -> str:
    """Return the new env-var name for ``key`` (or ``key`` unchanged)."""
    if key in _EXPLICIT_KEY_RENAMES:
        return _EXPLICIT_KEY_RENAMES[key]
    if key in _BARE_OFIN:
        return _BARE_OFIN[key]
    for old, new in prefix_map:
        if key.startswith(old):
            return new + key[len(old):]
    return key


_KV_RE = re.compile(r"^([A-Z][A-Z0-9_]*)=(.*)$")


def migrate_file(env_path: Path, prefix_map: list[tuple[str, str]]) -> tuple[list[str], list[tuple[str, str]]]:
    """Return (new_lines, renames) for the given .env file."""
    lines = env_path.read_text(encoding="utf-8").splitlines(keepends=True)
    out: list[str] = []
    renames: list[tuple[str, str]] = []
    for line in lines:
        m = _KV_RE.match(line.rstrip("\n").rstrip("\r"))
        if not m:
            out.append(line)
            continue
        key, value = m.group(1), m.group(2)
        new_key = migrate_key(key, prefix_map)
        if new_key != key:
            renames.append((key, new_key))
        # Preserve trailing newline if present.
        eol = ""
        if line.endswith("\r\n"):
            eol = "\r\n"
        elif line.endswith("\n"):
            eol = "\n"
        out.append(f"{new_key}={value}{eol}")
    return out, renames


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--env", type=Path, default=_REPO_ROOT / "config" / ".env",
                    help="Path to .env file (default: config/.env)")
    ap.add_argument("--dry-run", action="store_true", help="Print changes; do not write")
    args = ap.parse_args()

    env_path: Path = args.env
    if not env_path.exists():
        print(f"ERROR: {env_path} not found", file=sys.stderr)
        return 2

    prefix_map = _build_prefix_map()
    new_lines, renames = migrate_file(env_path, prefix_map)

    print(f"Found {len(renames)} key(s) to rename in {env_path}:")
    for old, new in renames:
        print(f"  {old:40s} -> {new}")

    if not renames:
        print("Nothing to do.")
        return 0

    if args.dry_run:
        print("\n(dry-run; no files written)")
        return 0

    backup = env_path.with_suffix(env_path.suffix + ".bak")
    shutil.copy2(env_path, backup)
    env_path.write_text("".join(new_lines), encoding="utf-8")
    print(f"\nBackup: {backup}")
    print(f"Wrote : {env_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
