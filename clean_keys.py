#!/usr/bin/env python3
"""clean_keys.py — Purge all provisioned API keys and the local .env file.

Removes:
  - config/keys/   (all .p12 and .pem key files)
  - config/.env    (the generated environment file)

Also clears the credential env vars from the running Vima server so the UI
reflects the clean state immediately (no server restart required).

Safe to run at any time; idempotent if already clean.
"""
import shutil
import sys
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).parent
KEYS_DIR = ROOT / "config" / "keys"
ENV_FILE = ROOT / "config" / ".env"
VIMA_URL = "http://localhost:9021/config/purge"


def confirm(prompt: str) -> bool:
    answer = input(f"{prompt} [y/N]: ").strip().lower()
    return answer == "y"


def purge_via_server() -> bool:
    """Ask the running Vima server to purge keys + env vars. Returns True on success."""
    try:
        req = urllib.request.Request(VIMA_URL, data=b"{}", method="POST",
                                     headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.status == 200
    except urllib.error.URLError:
        return False


def purge_files() -> list[str]:
    """Directly remove key files and .env. Returns list of removed items."""
    removed = []
    if KEYS_DIR.exists():
        shutil.rmtree(KEYS_DIR)
        KEYS_DIR.mkdir()   # recreate empty dir so the app doesn't error
        removed.append(str(KEYS_DIR))
    if ENV_FILE.exists():
        ENV_FILE.unlink()
        removed.append(str(ENV_FILE))
    return removed


def main() -> None:
    targets = []
    if KEYS_DIR.exists() and any(KEYS_DIR.iterdir()):
        targets.append(f"  • {KEYS_DIR}/ ({len(list(KEYS_DIR.iterdir()))} files)")
    if ENV_FILE.exists():
        targets.append(f"  • {ENV_FILE}")

    if not targets:
        print("Nothing to clean — no keys or .env file found.")
        return

    print("The following will be permanently deleted:")
    for t in targets:
        print(t)
    print()

    if not confirm("Are you sure you want to proceed?"):
        print("Aborted.")
        sys.exit(0)

    print()

    # Prefer calling the server so env vars are cleared from the running process too.
    if purge_via_server():
        print("  ✓ Server purged keys and cleared env vars — UI will reflect clean state immediately.")
    else:
        removed = purge_files()
        for r in removed:
            print(f"  ✓ Removed {r}")
        print("\n  ⚠️  Vima server not reachable — restart it for the UI to reflect the clean state.")

    print("\nDone. Re-run provisioning to restore keys.")


if __name__ == "__main__":
    main()

