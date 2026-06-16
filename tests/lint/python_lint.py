"""tests/lint/python_lint.py — Python static analysis via Ruff.

Runs `ruff check` on the application source tree and reports one test
result per file containing issues.  Files with no issues produce a
single aggregate PASS result.

Independently runnable::

    python tests/lint/python_lint.py
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from tests.lib.utils import TestRunner, Summary, bold, green, red, yellow

# Directories / files to lint (relative to repo root).
# tests/ and tools/ are excluded via ruff.toml as well, but we also
# restrict the targets here so the report is focused on application code.
_TARGETS = [
    "apis",
    "usecases",
    "chat",
    "simulator",
    "app.py",
    "clean_keys.py",
    "live_demo.py",
]


def run(base_url: str = "") -> TestRunner:  # base_url unused — linting is server-independent
    runner = TestRunner("Python Lint (Ruff)")

    root = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))

    # ── Check ruff is available ──────────────────────────────────
    def _check_ruff():
        result = subprocess.run(
            [sys.executable, "-m", "ruff", "--version"],
            capture_output=True, text=True,
            cwd=root,
        )
        assert result.returncode == 0, (
            "ruff is not installed. Run: pip install ruff>=0.4.0"
        )

    if not runner.run("ruff is installed", _check_ruff):
        return runner  # nothing else will work

    # ── Run ruff check --output-format json ──────────────────────
    targets = [t for t in _TARGETS if os.path.exists(os.path.join(root, t))]
    result = subprocess.run(
        [sys.executable, "-m", "ruff", "check", "--output-format", "json"] + targets,
        capture_output=True, text=True, encoding="utf-8",
        cwd=root,
    )

    # ruff exits 0 = clean, 1 = issues found, 2 = internal error
    if result.returncode == 2:
        def _ruff_error():
            raise AssertionError(f"ruff exited with error:\n{result.stderr[:500]}")
        runner.run("ruff check (internal error)", _ruff_error)
        return runner

    # Parse JSON output
    try:
        issues = json.loads(result.stdout) if result.stdout.strip() else []
    except json.JSONDecodeError:
        def _parse_error():
            raise AssertionError(f"Could not parse ruff output:\n{result.stdout[:300]}")
        runner.run("ruff output (parse error)", _parse_error)
        return runner

    # ── Compute file count and load ruff config for scan scope summary ─
    import tomllib  # Python 3.11+ stdlib
    total_files = sum(
        1 for t in targets
        for _dp, _ds, _fs in (
            [(root, [], [t])] if t.endswith(".py") else os.walk(os.path.join(root, t))
        )
        for f in _fs if f.endswith(".py")
    )
    _ruff_cfg: dict = {}
    _ruff_toml = os.path.join(root, "ruff.toml")
    if os.path.isfile(_ruff_toml):
        try:
            with open(_ruff_toml, "rb") as _tf:
                _ruff_cfg = tomllib.load(_tf)
        except Exception:
            pass
    _lint_cfg        = _ruff_cfg.get("lint", {})
    _rules_selected  = _lint_cfg.get("select", ["E", "F"])
    _rules_ignored   = _lint_cfg.get("ignore", [])
    _rule_desc = {"E": "style", "W": "warnings", "F": "Pyflakes",
                  "I": "imports", "B": "bugbear", "UP": "pyupgrade"}
    _rules_str = ", ".join(
        f"{r}({_rule_desc[r]})" if r in _rule_desc else r for r in _rules_selected
    )

    def _scan_scope():
        pass

    runner.run(
        f"Scan scope: {total_files} Python file(s) across {len(targets)} target(s)\n"
        f"  Targets: {', '.join(targets)}\n"
        f"  Rules:   {_rules_str}\n"
        f"  Ignored: {', '.join(_rules_ignored) if _rules_ignored else 'none'}\n"
        f"  Issues:  {len(issues)} total across {len(set(i.get('filename') for i in issues))} file(s)",
        _scan_scope,
    )

    # Group issues by filename (relative path)
    by_file: dict[str, list[dict]] = {}
    for issue in issues:
        rel = issue.get("filename", "?")
        try:
            rel = os.path.relpath(rel, root).replace("\\", "/")
        except ValueError:
            pass
        by_file.setdefault(rel, []).append(issue)

    if not by_file:
        # All clean — one aggregate pass
        def _all_clean():
            pass
        runner.run(f"All {len(targets)} target(s) are lint-clean", _all_clean)
    else:
        # One test per file that has issues
        for filepath, file_issues in sorted(by_file.items()):
            # Capture loop variable
            _fp = filepath
            _fi = file_issues

            def _file_lint(_fp=_fp, _fi=_fi):
                lines = []
                for issue in _fi:
                    loc = issue.get("location", {})
                    row = loc.get("row", "?")
                    col = loc.get("column", "?")
                    code = issue.get("code", "?")
                    msg = issue.get("message", "")
                    lines.append(f"  {_fp}:{row}:{col}  {code}  {msg}")
                raise AssertionError(
                    f"{len(_fi)} issue(s) in {_fp}:\n" + "\n".join(lines[:20])
                    + ("\n  …" if len(_fi) > 20 else "")
                )

            runner.run(f"{filepath} ({len(file_issues)} issue(s))", _file_lint)

        def _summary_note():
            pass
        runner.run(
            f"{total_files - len(by_file)} file(s) clean, {len(by_file)} file(s) with issues",
            _summary_note,
        )

    return runner


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Run Python lint analysis")
    p.parse_args()
    s = Summary()
    r = run()
    s.add(r)
    r.print_summary()
    s.print_and_exit()
