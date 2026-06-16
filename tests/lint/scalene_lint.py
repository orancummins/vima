"""tests/lint/scalene_lint.py — Runtime performance profiling via Scalene.

Profiles Flask app startup and core request handling via an in-process
test client.  Reports the top CPU / memory consumers by file.

Independently runnable::

    python tests/lint/scalene_lint.py
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from tests.lib.utils import TestRunner

_ROOT   = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
_TARGET = os.path.join(os.path.dirname(__file__), "profile_target.py")

# Report files at or above this CPU% as hotspots.
_CPU_THRESHOLD = 5.0
# Report lines within a hotspot file at or above this CPU%.
_LINE_CPU_THRESHOLD = 2.0
# Max hotspot lines to show per file.
_MAX_LINES = 5


def run(base_url: str = "") -> TestRunner:  # base_url unused
    runner = TestRunner("Runtime Performance (Scalene)")

    # ── Check scalene is available ───────────────────────────────
    def _check_scalene():
        result = subprocess.run(
            [sys.executable, "-m", "scalene", "--version"],
            capture_output=True, text=True,
            cwd=_ROOT,
        )
        assert result.returncode == 0, (
            "scalene is not installed. Run: pip install scalene>=1.5"
        )

    if not runner.run("scalene is installed", _check_scalene):
        return runner

    # ── Scan scope summary ───────────────────────────────────────
    def _scan_scope():
        pass

    runner.run(
        "Profile target: Flask app startup + in-process requests\n"
        "  Target:    tests/lint/profile_target.py\n"
        "  Profiling: CPU time, memory allocation\n"
        f"  Hotspot:   files >= {_CPU_THRESHOLD:.0f}% CPU; lines >= {_LINE_CPU_THRESHOLD:.0f}% CPU",
        _scan_scope,
    )

    # ── Run scalene ──────────────────────────────────────────────
    tmp_fd, tmp_path = tempfile.mkstemp(suffix=".json")
    os.close(tmp_fd)

    try:
        result = subprocess.run(
            [
                sys.executable, "-m", "scalene",
                "run",
                "--memory",
                "-o", tmp_path,
                _TARGET,
            ],
            capture_output=True, text=True, encoding="utf-8",
            cwd=_ROOT,
        )

        # scalene exits 0 on success; target exiting non-zero is still ok
        if result.returncode not in (0, 1):
            stderr_snippet = (result.stderr or "")[:500]

            def _run_error():
                raise AssertionError(
                    f"scalene exited {result.returncode}:\n{stderr_snippet}"
                )

            runner.run("scalene profile run", _run_error)
            return runner

        try:
            with open(tmp_path, encoding="utf-8") as f:
                content = f.read().strip()
            profile = json.loads(content) if content else {}
        except (FileNotFoundError, json.JSONDecodeError) as exc:
            exc_str = str(exc)

            def _parse_error():
                raise AssertionError(f"Could not parse scalene output: {exc_str}")

            runner.run("scalene profile run", _parse_error)
            return runner

    finally:
        try:
            os.unlink(tmp_path)
        except Exception:
            pass

    # ── Parse and report ─────────────────────────────────────────
    elapsed = profile.get("elapsed_time_sec", 0)
    files   = profile.get("files", {})

    if not files:
        def _no_data():
            pass
        runner.run(
            f"Profile complete ({elapsed:.2f}s) — no profiling data captured",
            _no_data,
        )
        return runner

    # Collect hotspot files (sorted by CPU% descending)
    hotspot_files = [
        (path, fdata)
        for path, fdata in files.items()
        if (fdata.get("percent_cpu_time") or 0) >= _CPU_THRESHOLD
    ]
    hotspot_files.sort(key=lambda x: x[1].get("percent_cpu_time", 0), reverse=True)

    if not hotspot_files:
        def _all_ok():
            pass
        runner.run(
            f"Profile complete ({elapsed:.2f}s, {len(files)} file(s) sampled)"
            f" — no file >= {_CPU_THRESHOLD:.0f}% CPU",
            _all_ok,
        )
        return runner

    # Report each hotspot file as an informational PASS
    for filepath, fdata in hotspot_files:
        rel      = os.path.relpath(filepath, _ROOT).replace("\\", "/")
        file_cpu = fdata.get("percent_cpu_time", 0)
        lines    = fdata.get("lines", [])

        # Top hotspot lines within this file
        hot_lines = [
            ln for ln in lines
            if (ln.get("n_cpu_percent_python", 0) + ln.get("n_cpu_percent_c", 0)) >= _LINE_CPU_THRESHOLD
        ]
        hot_lines.sort(
            key=lambda ln: ln.get("n_cpu_percent_python", 0) + ln.get("n_cpu_percent_c", 0),
            reverse=True,
        )

        detail_parts = []
        for ln in hot_lines[:_MAX_LINES]:
            cpu    = ln.get("n_cpu_percent_python", 0) + ln.get("n_cpu_percent_c", 0)
            mem    = ln.get("n_peak_mb", 0)
            lineno = ln.get("lineno", "?")
            src    = ln.get("line", "").rstrip()
            detail_parts.append(
                f"  line {lineno:>4}  CPU {cpu:.1f}%  peak {mem:.1f} MB  {src}"
            )

        detail_str = "\n".join(detail_parts) if detail_parts else "  (no individual lines above threshold)"
        captured   = [detail_str]

        def _make_report(cap):
            def _report():
                pass  # hotspots are informational, not failures
            return _report

        runner.run(
            f"{rel}  CPU {file_cpu:.1f}%\n{captured[0]}",
            _make_report(captured),
        )

    return runner


if __name__ == "__main__":
    r = run()
    r.print_summary()
    sys.exit(0 if r.failed() == 0 else 1)
