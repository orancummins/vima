"""tests/lint/vulture_lint.py — Dead code analysis via Vulture.

Runs `vulture <targets> --min-confidence 80` and reports one test result
per file containing unused code.  Files with no findings produce a single
aggregate PASS.

Independently runnable::

    python tests/lint/vulture_lint.py
"""
from __future__ import annotations

import os
import subprocess
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from tests.lib.utils import TestRunner

_TARGETS = [
    "apis",
    "usecases",
    "chat",
    "simulator",
    "app.py",
    "clean_keys.py",
    "live_demo.py",
]

# Only report findings at or above this confidence level (0-100).
_MIN_CONFIDENCE = 80


def run(base_url: str = "") -> TestRunner:  # base_url unused
    runner = TestRunner("Dead Code (Vulture)")

    root = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))

    # ── Check vulture is available ───────────────────────────────
    def _check_vulture():
        result = subprocess.run(
            [sys.executable, "-m", "vulture", "--version"],
            capture_output=True, text=True,
            cwd=root,
        )
        assert result.returncode == 0, (
            "vulture is not installed. Run: pip install vulture>=2.10"
        )

    if not runner.run("vulture is installed", _check_vulture):
        return runner

    targets = [t for t in _TARGETS if os.path.exists(os.path.join(root, t))]

    result = subprocess.run(
        [
            sys.executable, "-m", "vulture",
            "--min-confidence", str(_MIN_CONFIDENCE),
        ] + targets,
        capture_output=True, text=True, encoding="utf-8",
        cwd=root,
    )

    # vulture exits: 0 = no unused code, 1 = unused code found, 2 = syntax error
    if result.returncode == 2:
        def _vulture_error():
            raise AssertionError(f"vulture exited with error:\n{result.stderr[:500]}")
        runner.run("vulture check (error)", _vulture_error)
        return runner

    # Parse line-oriented output: path:line: message (confidence%)
    lines = [l for l in (result.stdout or "").splitlines() if l.strip()]

    # ── Scan scope summary ───────────────────────────────────────
    import glob as _glob

    def _count_files(target: str) -> int:
        p = os.path.join(root, target)
        if os.path.isfile(p):
            return 1
        return len(_glob.glob(os.path.join(p, "**", "*.py"), recursive=True))

    total_files = sum(_count_files(t) for t in targets)

    def _scan_scope():
        pass

    runner.run(
        f"Scan scope: {total_files} file(s)\n"
        f"  Targets:        {', '.join(targets)}\n"
        f"  Min confidence: {_MIN_CONFIDENCE}%\n"
        f"  Checks:         unused functions, classes, variables, imports, attributes",
        _scan_scope,
    )

    if not lines:
        def _all_clean():
            pass
        runner.run(f"All {total_files} file(s) clean — no dead code found", _all_clean)
        return runner

    # Group findings by file
    findings_by_file: dict[str, list[str]] = {}
    for line in lines:
        # typical format: apis/foo.py:42: unused function 'bar' (80% confidence)
        parts = line.split(":", 2)
        if len(parts) >= 3:
            filepath = parts[0].replace("\\", "/")
            findings_by_file.setdefault(filepath, []).append(line)
        else:
            findings_by_file.setdefault("(unknown)", []).append(line)

    for filepath, file_lines in sorted(findings_by_file.items()):
        detail = "\n".join(f"  {l}" for l in file_lines)
        captured = [detail]

        def _make_test(msg):
            def _test():
                raise AssertionError(msg)
            return _test

        runner.run(
            f"{filepath}: {len(file_lines)} finding(s)",
            _make_test(captured[0]),
        )

    return runner


if __name__ == "__main__":
    r = run()
    r.print_summary()
    sys.exit(0 if r.failed() == 0 else 1)
