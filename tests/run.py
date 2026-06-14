"""tests/run.py — Vima / Solution Studio test orchestrator.

Usage (via launchers)::

    test.bat          # Windows
    ./test.sh         # macOS / Linux

One-call examples::

    .\test.bat --email you@mastercard.com --sso --clean
    .\test.bat --email you@mastercard.com --portal-password secret --existing
    ./test.sh  --email you@mastercard.com --sso --clean

Direct usage::

    python tests/run.py --email you@example.com --install-type E
    python tests/run.py --email you@example.com --sso --install-type E
    python tests/run.py --email you@example.com --install-type C --key-password foobar!!

Options
-------
--email            Mastercard Developers account email
--sso              SSO login: only email is auto-filled; no portal password required
--portal-password  Mastercard Developers password for non-SSO auto-login
--smoke            Run smoke tests only (default)
--full             Run the full test suite (smoke + API + use case + bundles + SDKs)
--install-type     C = clean clone into temp dir | E = use --work-dir as-is
--key-password     Password for provisioned .p12 certs (default: foobar!!)
--work-dir         Root of the Vima repository (defaults to the directory containing this file)
--base-url         Override the server base URL (default: http://127.0.0.1:9021)
--no-server        Skip starting the server (assume one is already running)
--skip-provision   Skip the provisioning step even on a clean install

Flow
----
  1. (Clean) Clone repo → install deps
  2. Start Flask server, wait until ready
  3. Smoke tests            — tests/smoke/smoke.py
  4. (Clean) Auto-provision BIN Lookup key, then wait for completion
  5. BIN Lookup API tests   — tests/apis/bin_lookup.py
  6. BIN Lookup UC tests    — tests/usecases/bin_lookup.py
  7. Bundles (placeholder)  — tests/bundles/_placeholder.py
  8. SDKs (placeholder)     — tests/sdks/_placeholder.py
  9. Print summary; exit 0 on all-pass, 1 on any failure
"""
from __future__ import annotations

import argparse
import os
import sys

# ── Path bootstrap ─────────────────────────────────────────────────────────────
# Must run before ANY package import so that `tests.*` resolves correctly
# regardless of whether the file is invoked as `python tests/run.py` (where
# cwd is the repo root) or as `python run.py` from inside tests/.
_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

# Import via importlib so the path is guaranteed set first even if Python
# cached a partial sys.path before executing the top of this module.
import importlib

def _imp(dotted: str):
    return importlib.import_module(dotted)

_utils      = _imp("tests.lib.utils")
_server_mod = _imp("tests.lib.server")
_smoke      = _imp("tests.smoke.smoke")
_api_bin    = _imp("tests.apis.bin_lookup")
_uc_bin     = _imp("tests.usecases.bin_lookup")
_bundles    = _imp("tests.bundles._placeholder")
_sdks       = _imp("tests.sdks._placeholder")

Summary            = _utils.Summary
TestRunner         = _utils.TestRunner
bold, green, red   = _utils.bold, _utils.green, _utils.red
yellow, cyan       = _utils.yellow, _utils.cyan
start_server       = _server_mod.start_server
wait_server_ready  = _server_mod.wait_server_ready
stop_server        = _server_mod.stop_server


# ── CLI ───────────────────────────────────────────────────────────────────────
def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Vima test orchestrator")
    p.add_argument("--email",            required=True, help="Mastercard Developers email")
    p.add_argument("--sso",              action="store_true",
                   help="SSO login: only email is auto-filled (no portal password required)")
    p.add_argument("--portal-password",  default="",
                   help="Mastercard Developers portal password for non-SSO auto-login")
    _scope = p.add_mutually_exclusive_group()
    _scope.add_argument("--smoke",        action="store_true",
                        help="Run smoke tests (currently runs all tests; --full reserved for future expansion)")
    _scope.add_argument("--full",         action="store_true",
                        help="Reserved for future expansion (currently same as --smoke)")
    p.add_argument("--install-type",     choices=["C", "c", "E", "e"], default="E")
    p.add_argument("--key-password", "--storepass",     default="foobar!!",
                   help="Password for provisioned .p12 certs (default: foobar!!)")
    p.add_argument("--work-dir",         default=_ROOT)
    p.add_argument("--base-url",         default="http://127.0.0.1:9021")
    p.add_argument("--no-server",        action="store_true",
                   help="Skip starting the server (assume one is already running)")
    p.add_argument("--skip-provision",   action="store_true",
                   help="Skip provisioning even on a clean install")
    p.add_argument("--nocleanup",        action="store_true",
                   help="Skip all cleanup: keep cloned dir, keys/certs, and portal projects")
    return p.parse_args()


# ── Helpers ───────────────────────────────────────────────────────────────────
def _header(text: str) -> None:
    print(f"\n{bold(cyan('-' * 60))}")
    print(f"{bold(cyan(text))}")
    print(bold(cyan('-' * 60)))


def _step(text: str) -> None:
    print(f"\n{bold(f'>> {text}')}")


# ── Main ──────────────────────────────────────────────────────────────────────
def main() -> None:
    args = _parse_args()
    install_type = args.install_type.upper()
    # Normalize work_dir: strip trailing separator (Windows %~dp0 quirk) and
    # resolve to absolute path so subprocess.Popen(cwd=) never sees a stale cwd.
    work_dir = os.path.normpath(os.path.abspath(args.work_dir.strip('\"')))
    base_url     = args.base_url.rstrip("/")

    # Resolve test scope: flags accepted for future use; all tests run for now

    _header("Vima / Solution Studio — Automated Test Suite")
    print(f"  Email:         {args.email}")
    print(f"  Login mode:    {'SSO (email auto-fill only)' if args.sso else 'Standard (email + password auto-fill)'}")
    print(f"  Install type:  {'Clean (clone)' if install_type == 'C' else 'Existing'}")
    print(f"  Work dir:      {work_dir}")
    print(f"  Server:        {base_url}")

    summary = Summary()
    server_proc = None

    try:
        # ── Step 1: Clean install ──────────────────────────────
        if install_type == "C":
            _step("Clean install — cloning repository")
            from tests.lib.install import clone_repo, install_dependencies
            work_dir = clone_repo(work_dir)
            print(f"  Cloned to: {work_dir}")
            install_dependencies(work_dir)

        # ── Step 2: Start server ───────────────────────────────
        if args.no_server:
            _step("Skipping server start (--no-server)")
        else:
            _step("Starting Flask server")
            server_proc = start_server(work_dir)
            print(f"  Waiting for server at {base_url} …")
            try:
                wait_server_ready(base_url, timeout=30)
                print(f"  {green('[OK]  Server ready.')}")
            except RuntimeError as exc:
                print(f"  {red(f'Server failed to start: {exc}')}")
                sys.exit(1)

        # ── Step 3: Smoke tests ────────────────────────────────
        _step("Smoke tests")
        runner = _smoke.run(base_url)  # noqa: PLC0415
        summary.add(runner)
        runner.print_summary()

        # Abort early if smoke fails — no point continuing
        if runner.failed() > 0:
            print(f"\n{red('Smoke tests failed. Aborting further tests.')}")
            summary.print_and_exit()

        # ── Step 4: Provision (clean install only) ────────────────
        if install_type == "C" and not args.skip_provision:
            _step("Auto-provisioning BIN Lookup API key")
            from tests.lib.provision import (
                start_provision_job, wait_provision_complete, save_portal_credentials,
            )
            try:
                # Save portal credentials so the provisioner auto-fills the login form.
                # SSO mode: only email saved — triggers email-autofill + SSO redirect.
                # Non-SSO mode: email + password saved — triggers full credential fill.
                _step("Saving portal credentials for provisioner auto-login")
                portal_password = getattr(args, "portal_password", "") or ""
                save_portal_credentials(base_url, args.email, portal_password)

                job_id = start_provision_job(base_url, ["bin_lookup"], args.key_password)
                print(f"  Provision job started: {job_id}")
                ok = wait_provision_complete(base_url, job_id, args.email)
                if ok:
                    print(f"  {green('[OK]  Provisioning complete.')}")
                else:
                    print(f"  {yellow('Provisioning did not complete — API tests may fail.')}")
                    print(f"  {yellow('You can re-run with --skip-provision on an existing install.')}")
            except Exception as exc:
                print(f"  {red(f'Provisioning error: {exc}')}")
                print(f"  {yellow('Continuing with remaining tests …')}")

        # ── Step 5: BIN Lookup API tests ───────────────────────
        _step("BIN Lookup API tests")
        runner = _api_bin.run(base_url)
        summary.add(runner)
        runner.print_summary()

        # ── Step 6: BIN Lookup Use Case tests ─────────────────
        _step("BIN Lookup Use Case tests")
        runner = _uc_bin.run(base_url)
        summary.add(runner)
        runner.print_summary()

        # ── Step 7: Bundles ────────────────────────────────────
        _step("Bundles tests")
        runner = _bundles.run(base_url)
        summary.add(runner)
        runner.print_summary()

        # ── Step 8: SDKs ───────────────────────────────────────
        _step("SDK tests")
        runner = _sdks.run(base_url)
        summary.add(runner)
        runner.print_summary()

    finally:
        if server_proc is not None:
            _step("Stopping server")
            stop_server(server_proc)
            print(f"  {green('[OK]  Server stopped.')}")

    # ── Step 9: Portal project cleanup (clean install, unless --nocleanup) ──
    # Treated as a test suite — failure counts toward the final exit code.
    # Runs after the server is stopped so test failures never skip cleanup.
    # ALWAYS use the original repo's tool venv — the cloned temp dir has no .venv.
    if install_type == "C" and not args.skip_provision and not args.nocleanup:
        import subprocess as _sp
        _cleanup_runner = TestRunner("Portal project cleanup")
        _orig_tool_dir = os.path.join(_ROOT, "tools", "mcd-key-automation")
        _tool_python = os.path.join(_orig_tool_dir, ".venv", "Scripts", "python.exe")
        if not os.path.exists(_tool_python):
            _tool_python = os.path.join(_orig_tool_dir, ".venv", "bin", "python")
        _cleanup_script = os.path.join(_orig_tool_dir, "clean_portal_projects.py")

        def _run_portal_cleanup():
            proc = _sp.run(
                [_tool_python, _cleanup_script, "--prefix", "SST-"],
                cwd=_orig_tool_dir,
                capture_output=False,
            )
            assert proc.returncode == 0, \
                f"clean_portal_projects.py exited with code {proc.returncode}"

        _cleanup_runner.run("Delete SST-* projects from Mastercard Developers", _run_portal_cleanup)
        summary.add(_cleanup_runner)

    # ── Step 10: Local cleanup (clean install, unless --nocleanup) ─────────
    if install_type == "C" and not args.nocleanup:
        _step("Removing local keys/certs and cloned directory")
        import shutil as _shutil
        # Remove keys directory (inside the cloned work_dir or the original)
        _keys_dir = os.path.join(work_dir, "config", "keys")
        if os.path.isdir(_keys_dir):
            try:
                _shutil.rmtree(_keys_dir)
                print(f"  {green('[OK]  Removed keys/certs: ' + _keys_dir)}")
            except Exception as exc:
                print(f"  {yellow(f'[WARN] Could not remove keys dir: {exc}')}")
        # Remove the cloned temp directory (work_dir itself if it was a temp clone).
        # Only remove if it looks like a temp dir (not the original repo).
        _orig_root = os.path.normpath(os.path.abspath(_ROOT))
        _cur_work  = os.path.normpath(os.path.abspath(work_dir))
        if _cur_work != _orig_root:
            try:
                _shutil.rmtree(_cur_work)
                print(f"  {green('[OK]  Removed cloned directory: ' + _cur_work)}")
            except Exception as exc:
                print(f"  {yellow(f'[WARN] Could not remove cloned dir: {exc}')}")
        else:
            print(f"  {yellow('[INFO] work-dir is the original repo — skipping directory removal.')}")

    # ── Final summary ──────────────────────────────────────────
    summary.print_and_exit()


if __name__ == "__main__":
    main()
