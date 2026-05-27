#!/usr/bin/env python3
"""clean_keys.py — Purge all provisioned API keys and the local .env file.

Removes:
  - config/keys/      (all .p12 and .pem key files)
  - config/.env       (the generated environment file)
  - config/.env.TEMP  (stale migration artifact, if present)

Files are always removed directly from disk so this works whether or not the
Vima server is running. If the server happens to be running, we also POST
/config/purge so the in-memory os.environ is cleared (no restart needed).

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
ENV_TEMP = ROOT / "config" / ".env.TEMP"
TOOL_WORKSPACE = ROOT / "tools" / "mcd-key-automation" / "temp"
TOOL_OUTPUT = ROOT / "tools" / "mcd-key-automation" / "output"
VIMA_URL = "http://localhost:9021/config/purge"


def confirm(prompt: str) -> bool:
    answer = input(f"{prompt} [y/N]: ").strip().lower()
    return answer == "y"


def remove_files() -> list[str]:
    """Delete key files + .env files + tool workspace/output artifacts from disk."""
    removed = []
    if KEYS_DIR.exists():
        # Remove all contents but keep the directory (app expects it to exist).
        for child in KEYS_DIR.iterdir():
            if child.is_file() or child.is_symlink():
                child.unlink()
            elif child.is_dir():
                shutil.rmtree(child)
        removed.append(f"{KEYS_DIR}/* (key files)")
    for env_file in (ENV_FILE, ENV_TEMP):
        if env_file.exists():
            env_file.unlink()
            removed.append(str(env_file))
    # Clear accumulated tool artifacts so old keys aren't re-imported on the
    # next provisioning run.
    for tool_dir in ("normalized", "downloads"):
        d = TOOL_WORKSPACE / tool_dir
        if d.exists():
            shutil.rmtree(d)
            removed.append(str(d))
    # Remove output bundles/zips that contain key material.
    if TOOL_OUTPUT.exists():
        for child in TOOL_OUTPUT.iterdir():
            if child.is_file() and child.suffix.lower() == ".zip":
                child.unlink()
                removed.append(str(child))
    return removed


def notify_server() -> bool:
    """Tell the running Vima server to clear cached env vars. Silent if no server."""
    try:
        req = urllib.request.Request(
            VIMA_URL, data=b"{}", method="POST",
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=2) as resp:
            return 200 <= resp.status < 300
    except (urllib.error.URLError, ConnectionError, TimeoutError):
        return False


def main() -> None:
    targets = []
    if KEYS_DIR.exists():
        files = [p for p in KEYS_DIR.iterdir() if p.is_file()]
        if files:
            targets.append(f"  • {KEYS_DIR}/ ({len(files)} files)")
    if ENV_FILE.exists():
        targets.append(f"  • {ENV_FILE}")
    if ENV_TEMP.exists():
        targets.append(f"  • {ENV_TEMP}")
    for tool_dir in ("normalized", "downloads"):
        d = TOOL_WORKSPACE / tool_dir
        if d.exists() and any(d.iterdir()):
            targets.append(f"  • {d}/ (tool artifacts)")
    if TOOL_OUTPUT.exists():
        zips = [p for p in TOOL_OUTPUT.iterdir() if p.is_file() and p.suffix.lower() == ".zip"]
        if zips:
            targets.append(f"  • {TOOL_OUTPUT}/ ({len(zips)} bundle zip(s))")

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

    # Always delete from disk first — this works whether the server is running
    # or not, and whether or not the server has the /config/purge endpoint.
    removed = remove_files()
    for r in removed:
        print(f"  ✓ Removed {r}")

    # If the server is running, ask it to drop in-memory env vars too so the
    # UI reflects clean state without a restart. Silent if no server.
    if notify_server():
        print("  ✓ Notified running Vima server to clear in-memory env vars.")

    print("\nDone. Re-run provisioning to restore keys.")


if __name__ == "__main__":
    main()
