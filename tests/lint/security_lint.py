"""tests/lint/security_lint.py — Python security analysis via Bandit.

Runs `bandit -r <targets> -f json` and reports one test result per file
containing medium/high severity + medium/high confidence issues.
Low-severity findings are noted as informational but never cause failures.

Independently runnable::

    python tests/lint/security_lint.py
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from tests.lib.utils import TestRunner, Summary, yellow

_TARGETS = [
    "apis",
    "usecases",
    "chat",
    "simulator",
    "app.py",
    "clean_keys.py",
    "live_demo.py",
]

# Report findings at or above these thresholds.
# LOW findings are collected but never cause test failures.
_MIN_SEVERITY   = "MEDIUM"  # LOW | MEDIUM | HIGH
_MIN_CONFIDENCE = "MEDIUM"  # LOW | MEDIUM | HIGH

_SEV_ORDER = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}


def run(base_url: str = "") -> TestRunner:  # base_url unused — security scan is server-independent
    runner = TestRunner("Security (Bandit)")

    root = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))

    # ── Check bandit is available ────────────────────────────────
    def _check_bandit():
        result = subprocess.run(
            [sys.executable, "-m", "bandit", "--version"],
            capture_output=True, text=True,
            cwd=root,
        )
        assert result.returncode == 0, (
            "bandit is not installed. Run: pip install bandit>=1.7.0"
        )

    if not runner.run("bandit is installed", _check_bandit):
        return runner

    targets = [t for t in _TARGETS if os.path.exists(os.path.join(root, t))]

    result = subprocess.run(
        [
            sys.executable, "-m", "bandit",
            "-r",               # recursive
            "-f", "json",       # machine-readable output
            "-l",               # include LOW severity in JSON (we filter ourselves)
            "-i",               # include LOW confidence in JSON
            "--exclude", ".venv,tests,tools",
            "-q",               # quiet: suppress the progress spinner on stdout
        ] + targets,
        capture_output=True, text=True, encoding="utf-8",
        cwd=root,
    )

    # bandit exits: 0 = clean, 1 = issues found, 2 = internal error
    if result.returncode == 2:
        def _bandit_error():
            raise AssertionError(f"bandit exited with error:\n{result.stderr[:500]}")
        runner.run("bandit check (error)", _bandit_error)
        return runner

    try:
        report = json.loads(result.stdout) if result.stdout.strip() else {}
    except json.JSONDecodeError:
        def _parse_error():
            raise AssertionError(f"Could not parse bandit output:\n{result.stdout[:300]}")
        runner.run("bandit output (parse error)", _parse_error)
        return runner

    all_issues = report.get("results", [])

    # ── Emit scan scope / confidence summary ─────────────────────────
    metrics       = report.get("metrics", {})
    totals        = metrics.get("_totals", {})
    files_scanned = max(0, len(metrics) - 1)   # one entry per file + "_totals"
    loc            = int(totals.get("loc", 0))
    sev_h = int(totals.get("SEVERITY.HIGH",   0))
    sev_m = int(totals.get("SEVERITY.MEDIUM", 0))
    sev_l = int(totals.get("SEVERITY.LOW",    0))

    def _scan_scope():
        pass

    runner.run(
        f"Scan scope: {files_scanned} file(s), {loc:,} lines of code\n"
        f"  Targets:   {', '.join(targets)}\n"
        f"  Threshold: severity >={_MIN_SEVERITY}, confidence >={_MIN_CONFIDENCE}\n"
        f"  Checks:    B1xx (injection), B2xx (shell), B3xx (imports), B4xx (ciphers),\n"
        f"             B5xx (assert/try), B6xx (crypto/ssl), B7xx (xml/yaml)\n"
        f"  Findings:  {sev_h} HIGH, {sev_m} MEDIUM, {sev_l} LOW (all severities, before filter)",
        _scan_scope,
    )

    # Split into flagged (medium+ sev AND medium+ conf) vs low/informational
    flagged = [
        i for i in all_issues
        if _SEV_ORDER.get(i.get("issue_severity", "LOW"), 0) >= _SEV_ORDER[_MIN_SEVERITY]
        and _SEV_ORDER.get(i.get("issue_confidence", "LOW"), 0) >= _SEV_ORDER[_MIN_CONFIDENCE]
    ]
    low_count = len(all_issues) - len(flagged)

    # Group flagged issues by filename
    by_file: dict[str, list[dict]] = {}
    for issue in flagged:
        rel = issue.get("filename", "?")
        try:
            rel = os.path.relpath(rel, root).replace("\\", "/")
        except ValueError:
            pass
        by_file.setdefault(rel, []).append(issue)

    if not by_file:
        def _all_clean():
            pass
        runner.run(
            f"No medium/high security issues in {len(targets)} target(s)",
            _all_clean,
        )
    else:
        for filepath, issues in sorted(by_file.items()):
            _fp = filepath
            _fi = sorted(issues, key=lambda x: -_SEV_ORDER.get(x.get("issue_severity", "LOW"), 0))

            def _file_security(_fp=_fp, _fi=_fi):
                lines = []
                for issue in _fi[:20]:
                    sev  = issue.get("issue_severity", "?")
                    conf = issue.get("issue_confidence", "?")
                    test = issue.get("test_id", "?")
                    msg  = issue.get("issue_text", "")
                    line = issue.get("line_number", "?")
                    lines.append(f"  [{sev}/{conf}] {_fp}:{line}  {test}  {msg}")
                raise AssertionError(
                    f"{len(_fi)} issue(s) in {_fp}:\n" + "\n".join(lines)
                    + ("\n  …" if len(_fi) > 20 else "")
                )

            high = sum(1 for i in issues if i.get("issue_severity") == "HIGH")
            med  = sum(1 for i in issues if i.get("issue_severity") == "MEDIUM")
            label_parts = []
            if high:
                label_parts.append(f"{high} HIGH")
            if med:
                label_parts.append(f"{med} MEDIUM")
            runner.run(f"{filepath} ({', '.join(label_parts)})", _file_security)

    # ── Suppressions: scan source for # nosec annotations ───────
    # Collect every line that contains # nosec so the run detail view
    # shows exactly what was intentionally suppressed and why.
    nosec_lines: list[str] = []
    for t in targets:
        tpath = os.path.join(root, t)
        if t.endswith(".py") and os.path.isfile(tpath):
            _scan_file_for_nosec(tpath, root, nosec_lines)
        elif os.path.isdir(tpath):
            for dirpath, dirs, files in os.walk(tpath):
                dirs[:] = [d for d in dirs if d not in (".venv", "__pycache__")]
                for fname in files:
                    if fname.endswith(".py"):
                        _scan_file_for_nosec(os.path.join(dirpath, fname), root, nosec_lines)

    if nosec_lines:
        _nl = list(nosec_lines)

        def _suppressions(_nl=_nl):
            pass  # always passes — informational display only

        runner.run(
            f"Suppressions ({len(nosec_lines)} # nosec annotation(s)):\n"
            + "\n".join(f"  {line}" for line in _nl),
            _suppressions,
        )
    else:
        def _no_suppressions():
            pass
        runner.run("No # nosec suppressions in scanned files", _no_suppressions)

    # Informational note for low-severity findings — not a test, just output
    if low_count:
        print(f"  {yellow(f'[INFO] {low_count} low-severity/confidence finding(s) below threshold — run bandit manually to review')}")

    return runner


def _scan_file_for_nosec(filepath: str, root: str, out: list[str]) -> None:
    """Append 'relpath:lineno  <line content>' entries for every # nosec line."""
    try:
        rel = os.path.relpath(filepath, root).replace("\\", "/")
        with open(filepath, encoding="utf-8", errors="replace") as fh:
            for lineno, raw in enumerate(fh, 1):
                stripped = raw.rstrip()
                if "# nosec" in stripped:
                    out.append(f"{rel}:{lineno}  {stripped.lstrip()}")
    except OSError:
        pass


if __name__ == "__main__":
    s = Summary()
    r = run()
    s.add(r)
    r.print_summary()
    s.print_and_exit()
