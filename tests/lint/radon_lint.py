"""tests/lint/radon_lint.py — Code complexity analysis via Radon.

Runs two checks:
  1. Cyclomatic Complexity (CC) — two tiers:
       FAIL:  rank E/F  (CC >= 21) — genuinely problematic
       INFO:  rank C/D  (CC 11-20) — visible but non-blocking
     Ranks: A=1-5  B=6-10  C=11-15  D=16-20  E=21-25  F=26+
  2. Maintainability Index (MI) — reports files ranked C (MI < 10).
     Ranks: A >= 20  B = 10-19  C < 10  (radon scale)

Independently runnable::

    python tests/lint/radon_lint.py
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from tests.lib.utils import TestRunner

_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))

_TARGETS = [
    "apis",
    "usecases",
    "chat",
    "simulator",
    "app.py",
    "clean_keys.py",
    "live_demo.py",
]

# CC rank thresholds:
#   FAIL on E/F  (CC >= 21) — genuinely problematic, not just architectural
#   INFO on C/D  (CC 11-20) — shown but non-blocking
_CC_FAIL_RANK = "E"   # E and above are failures
_CC_INFO_RANK = "C"   # C and above are shown (but only C/D are non-blocking)
# Report MI files at or below this rank (C = MI < 10)
_MI_WARN_RANK = "C"


def _run_radon(subcmd: str, extra_flags: list[str], targets: list[str]) -> tuple[dict, str]:
    """Run radon <subcmd> --json and return (parsed_dict, stderr)."""
    result = subprocess.run(
        [sys.executable, "-m", "radon", subcmd, "--json"] + extra_flags + targets,
        capture_output=True, text=True, encoding="utf-8",
        cwd=_ROOT,
    )
    try:
        return json.loads(result.stdout or "{}"), result.stderr or ""
    except json.JSONDecodeError:
        return {}, result.stderr or result.stdout or ""


def run(base_url: str = "") -> TestRunner:  # base_url unused
    runner = TestRunner("Code Complexity (Radon)")

    # ── Check radon is available ─────────────────────────────────
    def _check_radon():
        result = subprocess.run(
            [sys.executable, "-m", "radon", "--version"],
            capture_output=True, text=True,
            cwd=_ROOT,
        )
        assert result.returncode == 0, (
            "radon is not installed. Run: pip install radon>=6.0"
        )

    if not runner.run("radon is installed", _check_radon):
        return runner

    targets = [t for t in _TARGETS if os.path.exists(os.path.join(_ROOT, t))]

    # ── Scan scope summary ───────────────────────────────────────
    def _scan_scope():
        pass

    runner.run(
        f"Scan scope: {len(targets)} target(s)\n"
        f"  Targets:  {', '.join(targets)}\n"
        f"  CC fail:  rank E/F (CC >= 21) — genuinely problematic\n"
        f"  CC info:  rank C/D (CC 11\u201320) — visible, non-blocking\n"
        f"  MI check: maintainability index, report rank C (MI < 10)",
        _scan_scope,
    )

    # ── Cyclomatic Complexity ────────────────────────────────────
    cc_data, cc_err = _run_radon("cc", ["-s", "-n", _CC_INFO_RANK], targets)

    if cc_err and not cc_data:
        err_str = cc_err[:400]

        def _cc_error():
            raise AssertionError(f"radon cc failed:\n{err_str}")

        runner.run("Cyclomatic Complexity check", _cc_error)
    else:
        # Split findings into failures (E/F) and informational (C/D)
        fail_by_file: dict[str, list[str]] = {}
        info_by_file: dict[str, list[str]] = {}
        for filepath, blocks in cc_data.items():
            rel = os.path.relpath(filepath, _ROOT).replace("\\", "/")
            for block in blocks:
                rank = block.get("rank", "A")
                if rank < _CC_INFO_RANK:
                    continue
                name       = block.get("name", "?")
                lineno     = block.get("lineno", "?")
                complexity = block.get("complexity", "?")
                btype      = block.get("type", "")
                classname  = block.get("classname") or ""
                qualified  = f"{classname}.{name}" if classname else name
                entry = (
                    f"  line {lineno:>4}  CC {complexity:>3}  rank {rank}"
                    f"  {btype} {qualified}"
                )
                if rank >= _CC_FAIL_RANK:
                    fail_by_file.setdefault(rel, []).append(entry)
                else:
                    info_by_file.setdefault(rel, []).append(entry)

        if not fail_by_file and not info_by_file:
            def _cc_ok():
                pass
            runner.run("Cyclomatic Complexity: all blocks rank A or B (CC <= 10)", _cc_ok)
        else:
            # Failures first
            for filepath, lines in sorted(fail_by_file.items()):
                detail = "\n".join(lines)

                def _make_cc_fail(msg: str):
                    def _fail():
                        raise AssertionError(msg)
                    return _fail

                runner.run(
                    f"{filepath}: {len(lines)} high-complexity block(s) [rank E/F, CC >= 21]",
                    _make_cc_fail(detail),
                )

            # Informational (C/D) — shown as passing tests so they appear in the log
            info_total = sum(len(v) for v in info_by_file.values())
            if info_by_file:
                detail_lines = []
                for filepath, lines in sorted(info_by_file.items()):
                    detail_lines.append(f"  {filepath} ({len(lines)} block(s))")
                    detail_lines.extend(lines)

                def _cc_info():
                    pass  # informational — not a failure

                runner.run(
                    f"{info_total} moderate-complexity block(s) [rank C/D, CC 11\u201320 — informational]",
                    _cc_info,
                )

    # ── Maintainability Index ────────────────────────────────────
    mi_data, mi_err = _run_radon("mi", [], targets)

    if mi_err and not mi_data:
        err_str = mi_err[:400]

        def _mi_error():
            raise AssertionError(f"radon mi failed:\n{err_str}")

        runner.run("Maintainability Index check", _mi_error)
    else:
        low_mi = {
            os.path.relpath(fp, _ROOT).replace("\\", "/"): info
            for fp, info in mi_data.items()
            if (info.get("rank") or "A") >= _MI_WARN_RANK
        }

        if not low_mi:
            def _mi_ok():
                pass

            runner.run(
                f"Maintainability Index: all {len(mi_data)} file(s) rank A or B",
                _mi_ok,
            )
        else:
            for filepath, info in sorted(low_mi.items()):
                mi_val = info.get("mi", 0)
                rank   = info.get("rank", "?")
                detail = f"  MI {mi_val:.1f}  rank {rank}"
                captured = [detail]

                def _make_mi_fail(msg: str):
                    def _fail():
                        raise AssertionError(msg)
                    return _fail

                runner.run(
                    f"{filepath}: low maintainability",
                    _make_mi_fail(captured[0]),
                )

    return runner


if __name__ == "__main__":
    r = run()
    r.print_summary()
    sys.exit(0 if r.failed() == 0 else 1)
