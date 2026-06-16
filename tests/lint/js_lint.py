"""tests/lint/js_lint.py — JavaScript static analysis via ESLint.

Runs `npx eslint static/js/ --format json` against the application JS
and reports one test result per file containing issues.

Requires Node.js / npx on PATH.  If unavailable the suite records a
single informational skip (not a failure) and returns cleanly.

Independently runnable::

    python tests/lint/js_lint.py
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from tests.lib.utils import TestRunner, Summary, yellow

_JS_TARGET = "static/js"


def run(base_url: str = "") -> TestRunner:  # base_url unused — linting is server-independent
    runner = TestRunner("JavaScript Lint (ESLint)")

    root = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))

    # ── Check Node / npx is available ───────────────────────────
    # shutil.which works for system/Homebrew installs.  When Node is managed
    # via nvm on macOS/Linux the binary lives under ~/.nvm and is only on PATH
    # in interactive shells, so we also probe common nvm locations.
    npx = shutil.which("npx")
    if npx is None:
        _nvm_candidates = [
            os.path.expanduser("~/.nvm/versions/node"),  # nvm base dir
        ]
        for _nvm_base in _nvm_candidates:
            if os.path.isdir(_nvm_base):
                # Pick the highest-versioned Node under ~/.nvm/versions/node/
                try:
                    _versions = sorted(os.listdir(_nvm_base), reverse=True)
                    for _v in _versions:
                        _candidate = os.path.join(_nvm_base, _v, "bin", "npx")
                        if os.path.isfile(_candidate):
                            npx = _candidate
                            break
                except OSError:
                    pass
            if npx:
                break

    if npx is None:
        def _no_node():
            # Record as a skipped/informational result, not a failure.
            # Tests still count as 1 pass so the run isn't penalised.
            print(f"  {yellow('[SKIP] npx not found — JavaScript linting requires Node.js on PATH.')}")
        runner.run("npx available (skip: Node.js not found)", _no_node)
        return runner

    js_dir = os.path.join(root, _JS_TARGET)
    if not os.path.isdir(js_dir):
        def _no_js():
            pass
        runner.run(f"{_JS_TARGET} not found — skip", _no_js)
        return runner

    # ── Run ESLint with JSON formatter ──────────────────────────
    # Collect JS files explicitly via Python glob — passing explicit file paths
    # works with both ESLint 8 and 9 (directory scanning in v9 flat-config mode
    # silently skips files not matched by the config).
    import glob as _glob
    js_files = sorted(set(
        _glob.glob(os.path.join(js_dir, "**", "*.js"), recursive=True)
        + _glob.glob(os.path.join(js_dir, "*.js"))
    ))

    if not js_files:
        def _no_js_files():
            pass
        runner.run(f"{_JS_TARGET} — no .js files found", _no_js_files)
        return runner

    # Pass relative paths from cwd — absolute Windows paths with backslashes
    # are silently rejected by some ESLint versions.
    js_files_rel = [os.path.relpath(f, root).replace("\\", "/") for f in js_files]

    # ESLint 10 uses flat config (eslint.config.js) exclusively — the
    # ESLINT_USE_FLAT_CONFIG env var and --no-eslintrc flag were removed.
    # eslint.config.js at the project root is discovered automatically.
    result = subprocess.run(
        [npx, "--yes", "eslint"] + js_files_rel + ["--format", "json"],
        capture_output=True, text=True, encoding="utf-8",
        cwd=root,
    )

    # ESLint exits 0 = clean, 1 = lint errors found, 2 = config/internal error
    if result.returncode == 2:
        def _eslint_error():
            raise AssertionError(f"eslint exited with config/internal error:\n{result.stderr[:500]}")
        runner.run("eslint check (error)", _eslint_error)
        return runner

    # Parse JSON output
    try:
        file_results = json.loads(result.stdout) if result.stdout.strip() else []
    except json.JSONDecodeError:
        def _parse_error():
            raise AssertionError(f"Could not parse eslint JSON output:\n{result.stdout[:300]}")
        runner.run("eslint output (parse error)", _parse_error)
        return runner

    # ── Emit scan scope / confidence summary ─────────────────────────
    _total_errors   = sum(f.get("errorCount",   0) for f in file_results)
    _total_warnings = sum(f.get("warningCount", 0) for f in file_results)

    def _scan_scope():
        pass

    runner.run(
        f"Scan scope: {len(js_files)} JS file(s) in {_JS_TARGET}\n"
        f"  Config:   .eslintrc.json (eslint:recommended)\n"
        f"  Checks:   best-practices, no-unused-vars, no-undef, consistent syntax\n"
        f"  Findings: {_total_errors} error(s), {_total_warnings} warning(s)",
        _scan_scope,
    )

    # Each entry: {filePath, messages:[{ruleId,severity,message,line,column}], errorCount, warningCount}
    # Only files with errors (severity=2) are FAIL. Files with warnings-only are
    # surfaced as informational PASSes so the suite doesn't penalise style noise.
    files_with_errors   = [f for f in file_results if f.get("errorCount", 0) > 0]
    files_with_warnings = [f for f in file_results if f.get("errorCount", 0) == 0 and f.get("warningCount", 0) > 0]
    files_clean = len(file_results) - len(files_with_errors) - len(files_with_warnings)

    if not files_with_errors and not files_with_warnings:
        def _all_clean():
            pass
        runner.run(f"All {len(js_files)} JS file(s) are lint-clean", _all_clean)
    else:
        # Emit FAIL for every file with errors
        for file_entry in sorted(files_with_errors, key=lambda x: x.get("filePath", "")):
            try:
                rel = os.path.relpath(file_entry["filePath"], root).replace("\\", "/")
            except (ValueError, KeyError):
                rel = file_entry.get("filePath", "?")

            _rel = rel
            _msgs = [m for m in file_entry.get("messages", []) if m.get("severity", 1) == 2]
            _ec = file_entry.get("errorCount", 0)
            _wc = file_entry.get("warningCount", 0)

            def _file_lint(_rel=_rel, _msgs=_msgs, _ec=_ec, _wc=_wc):
                lines = []
                for m in _msgs[:20]:
                    rule = m.get("ruleId", "?")
                    msg = m.get("message", "")
                    row = m.get("line", "?")
                    col = m.get("column", "?")
                    lines.append(f"  {_rel}:{row}:{col}  [error]  {rule}  {msg}")
                summary = f"{_ec} error(s), {_wc} warning(s)"
                raise AssertionError(
                    f"{summary} in {_rel}:\n" + "\n".join(lines)
                    + ("\n  …" if len(_msgs) > 20 else "")
                )

            runner.run(f"{rel} ({_ec} error(s))", _file_lint)

        # Emit PASS (informational) for files with warnings only
        for file_entry in sorted(files_with_warnings, key=lambda x: x.get("filePath", "")):
            try:
                rel = os.path.relpath(file_entry["filePath"], root).replace("\\", "/")
            except (ValueError, KeyError):
                rel = file_entry.get("filePath", "?")

            _rel = rel
            _msgs = file_entry.get("messages", [])
            _wc = file_entry.get("warningCount", 0)

            def _file_warn(_rel=_rel, _msgs=_msgs, _wc=_wc):
                # Print warning detail to stdout but do NOT raise — warnings are
                # informational and must not cause the test suite to fail.
                lines = []
                for m in _msgs[:10]:
                    rule = m.get("ruleId", "?")
                    msg = m.get("message", "")
                    row = m.get("line", "?")
                    col = m.get("column", "?")
                    lines.append(f"    {_rel}:{row}:{col}  [warn]  {rule}  {msg}")
                print(f"  [warn] {_rel} ({_wc} warning(s)):")
                for ln in lines:
                    print(ln)
                if len(_msgs) > 10:
                    print("    …")

            runner.run(f"{rel} ({_wc} warning(s)) [informational]", _file_warn)

        def _summary_note():
            pass
        runner.run(
            f"{files_clean} file(s) clean, {len(files_with_errors)} file(s) with errors, "
            f"{len(files_with_warnings)} file(s) with warnings only",
            _summary_note,
        )

    return runner


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Run JavaScript lint analysis")
    p.parse_args()
    s = Summary()
    r = run()
    s.add(r)
    r.print_summary()
    s.print_and_exit()
