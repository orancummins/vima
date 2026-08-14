#!/usr/bin/env python3
"""Build a portable, no-binary ``ofin`` distribution.

Produces ``cli/dist/`` containing:

* ``ofin.pyz``   — a stdlib :mod:`zipapp` of the ``ofin`` package, with the
  three Open Finance ``client.py`` files vendored under ``ofin/sdk/_vendor/``
  (single source of truth: copied from ``apis/`` at build time).
* ``ofin.env``   — credentials assembled from the repo's ``config/.env``
  (the single source of truth), with EU key/cert paths rewritten to point at
  the adjacent ``keys/`` folder.
* ``keys/``      — the EU RSA private key + public cert, copied as real files
  (the EU client opens them with ``open()``, so they must live on disk — never
  inside the zip).
* ``ofin.cmd`` / ``ofin`` — text wrapper scripts (NOT executables) that run
  ``python ofin.pyz`` with ``--env-file`` pointing at the adjacent ``ofin.env``.

The whole ``dist/`` folder can be copied to any Windows/macOS/Linux machine
that has Python 3.9+ with ``requests`` and ``cryptography`` installed.

Usage::

    python cli/build.py
"""
from __future__ import annotations

import os
import re
import shutil
import sys
import zipapp

HERE = os.path.dirname(os.path.abspath(__file__))          # .../cli
REPO_ROOT = os.path.abspath(os.path.join(HERE, ".."))      # repo root
PKG_DIR = os.path.join(HERE, "ofin")                       # .../cli/ofin
VENDOR_DIR = os.path.join(PKG_DIR, "sdk", "_vendor")
DIST_DIR = os.path.join(HERE, "dist")

# (source client.py, vendored module filename)
VENDOR_SOURCES = [
    (os.path.join(REPO_ROOT, "apis", "open_finance", "client.py"), "open_finance_client.py"),
    (os.path.join(REPO_ROOT, "apis", "open_finance_au", "client.py"), "open_finance_au_client.py"),
    (os.path.join(REPO_ROOT, "apis", "open_finance_eu", "client.py"), "open_finance_eu_client.py"),
]

# EU key/cert env vars -> bundled relative location under dist/keys/.
EU_KEY_VARS = ("OPEN_FINANCE_EU_PRIVATE_KEY_PATH", "OPEN_FINANCE_EU_PUBLIC_CERT_PATH")


def log(msg: str) -> None:
    print(f"[build] {msg}")


def vendor_clients() -> None:
    """Copy the three client.py files into the package's _vendor/ dir."""
    os.makedirs(VENDOR_DIR, exist_ok=True)
    # Keep the package marker; clear stale vendored modules.
    for name in os.listdir(VENDOR_DIR):
        if name.endswith("_client.py"):
            os.remove(os.path.join(VENDOR_DIR, name))
    for src, dst_name in VENDOR_SOURCES:
        if not os.path.isfile(src):
            raise SystemExit(f"Missing source client: {src}")
        with open(src, encoding="utf-8") as fh:
            code = fh.read()
        # The clients use only stdlib + requests + cryptography (no relative
        # imports today). Defensively neutralise any future ``from .x`` import.
        code = re.sub(r"^from \.\S*", "# vendored: removed relative import", code, flags=re.M)
        with open(os.path.join(VENDOR_DIR, dst_name), "w", encoding="utf-8") as fh:
            fh.write(code)
        log(f"vendored {os.path.relpath(src, REPO_ROOT)} -> sdk/_vendor/{dst_name}")


def parse_env(path: str) -> list[tuple[str, str]]:
    """Read KEY=VALUE lines, preserving order. Comments/blanks dropped."""
    out = []
    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            if line.lower().startswith("export "):
                line = line[7:].strip()
            key, _, val = line.partition("=")
            out.append((key.strip(), val.strip().strip('"').strip("'")))
    return out


def assemble_config() -> None:
    """Write dist/ofin.env + dist/keys/ from the repo's config/.env."""
    src_env = os.path.join(REPO_ROOT, "config", ".env")
    if not os.path.isfile(src_env):
        log("WARNING: config/.env not found — skipping bundled config/keys.")
        return
    pairs = parse_env(src_env)
    keys_dir = os.path.join(DIST_DIR, "keys")
    os.makedirs(keys_dir, exist_ok=True)

    rewritten = []
    for key, val in pairs:
        if key in EU_KEY_VARS and val:
            src_key = val if os.path.isabs(val) else os.path.join(REPO_ROOT, val)
            if os.path.isfile(src_key):
                fname = os.path.basename(src_key)
                shutil.copy2(src_key, os.path.join(keys_dir, fname))
                val = os.path.join("keys", fname).replace("\\", "/")
                log(f"copied EU material {fname} -> dist/keys/")
            else:
                log(f"WARNING: EU key path not found, leaving as-is: {src_key}")
        rewritten.append((key, val))

    out_env = os.path.join(DIST_DIR, "ofin.env")
    with open(out_env, "w", encoding="utf-8") as fh:
        fh.write("# Assembled by cli/build.py from config/.env (single source of truth).\n")
        fh.write("# EU key paths are relative to this file's directory.\n")
        for key, val in rewritten:
            fh.write(f"{key}={val}\n")
    log(f"wrote {os.path.relpath(out_env, HERE)}")


_ROOT_MAIN = (
    "import sys\n"
    "from ofin.cli import main\n"
    "sys.exit(main())\n"
)


def build_pyz() -> None:
    target = os.path.join(DIST_DIR, "ofin.pyz")
    if os.path.exists(target):
        os.remove(target)
    # Stage ``ofin`` as a real package inside the archive so the package's
    # relative imports resolve, with a root __main__.py that drives it and
    # preserves the process exit code.
    stage = os.path.join(DIST_DIR, "_stage")
    if os.path.exists(stage):
        shutil.rmtree(stage)
    shutil.copytree(
        PKG_DIR,
        os.path.join(stage, "ofin"),
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
    )
    with open(os.path.join(stage, "__main__.py"), "w", encoding="utf-8") as fh:
        fh.write(_ROOT_MAIN)
    try:
        zipapp.create_archive(
            source=stage,
            target=target,
            interpreter="/usr/bin/env python3",
            main=None,  # stage/__main__.py is the entry point.
        )
    finally:
        shutil.rmtree(stage, ignore_errors=True)
    log(f"built {os.path.relpath(target, HERE)}")


def write_wrappers() -> None:
    # Windows wrapper.
    cmd = (
        "@echo off\r\n"
        "REM ofin launcher (text script, not an executable).\r\n"
        "set OFIN_DIR=%~dp0\r\n"
        'python "%OFIN_DIR%ofin.pyz" --env-file "%OFIN_DIR%ofin.env" %*\r\n'
    )
    with open(os.path.join(DIST_DIR, "ofin.cmd"), "w", encoding="utf-8", newline="") as fh:
        fh.write(cmd)

    # POSIX wrapper.
    sh = (
        "#!/usr/bin/env bash\n"
        "# ofin launcher (text script, not an executable binary).\n"
        'DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"\n'
        'exec python3 "$DIR/ofin.pyz" --env-file "$DIR/ofin.env" "$@"\n'
    )
    sh_path = os.path.join(DIST_DIR, "ofin")
    with open(sh_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(sh)
    try:
        os.chmod(sh_path, 0o755)
    except OSError:
        pass
    log("wrote wrappers ofin.cmd + ofin")


def main() -> int:
    os.makedirs(DIST_DIR, exist_ok=True)
    log(f"output dir: {DIST_DIR}")
    vendor_clients()
    build_pyz()
    assemble_config()
    write_wrappers()
    log("done. Try:  python dist/ofin.pyz --env-file dist/ofin.env config show")
    return 0


if __name__ == "__main__":
    sys.exit(main())
