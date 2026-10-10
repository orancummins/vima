"""tests/lint/duplication_lint.py — Duplicate code detection (pure Python).

Uses a sliding-window hash approach to find copy-paste clones across both
Python and JavaScript source files.  No external tools or npm required.

Algorithm
---------
1. Collect all .py and .js files under the configured targets.
2. Normalise each file to a list of (lineno, normalised_text) pairs,
   skipping blank and comment-only lines.
3. Slide a window of MIN_LINES normalised lines and SHA-256-hash each window.
4. Any hash that appears in 2+ locations is a clone candidate.
5. Group candidates by file pair; merge overlapping windows into blocks.
6. Report file pairs whose total duplicated lines meet the threshold.

Independently runnable::

    python tests/lint/duplication_lint.py
"""
from __future__ import annotations

import glob
import hashlib
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from tests.lib.utils import TestRunner

_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))

_TARGETS = [
    "apis",
    "usecases",
    "chat",
    "simulator",
    "static/js",
    "app.py",
    "clean_keys.py",
    "live_demo.py",
]

# Minimum consecutive *normalised* lines that count as one clone block.
_MIN_LINES = 6

# A file pair is reported as a FAIL when its total shared (non-overlapping)
# lines in *either* file reach this count.
# 50 lines filters out API-boilerplate similarity (shared PAN/auth field
# schemas) that is intentional in this architecture.
_DUP_LINE_THRESHOLD = 50

# Known false-positive pairs: (relative_path_a, relative_path_b) → reason.
# Paths use forward slashes, both orders are checked.
# These are shown in test output as explicit informational results so the
# reason is visible rather than the finding silently disappearing.
_IGNORED_PAIRS: dict[tuple[str, str], str] = {
    ("app.py", "app.py"): (
        "Multiple Flask route handlers share the same guard/jsonify boilerplate "
        "— structural pattern inherent to Flask routing, not copy-paste logic"
    ),
    ("apis/snippet.py", "apis/snippet.py"): (
        "Code-generator with three auth-flavour branches (OAuth1, Finicity, EU JWT); "
        "each branch produces a similarly-shaped script — template content, not logic"
    ),
    ("apis/open_finance/api.py", "apis/open_finance/api.py"): (
        "Large single-API file with ~15 endpoints that each declare an identical "
        "customer_id/account_id param dict — operation data definition, not logic"
    ),
    ("usecases/the_wire/__init__.py", "usecases/the_wire/__init__.py"): (
        "Six hand-assembled fixture journeys each with the same 5-stage schema "
        "(bank -> agg -> merchant -> category -> app) — the repetition is the dataset"
    ),
    ("static/js/app/main.js", "static/js/app/main.js"): (
        "3000-line UI file with repeated panel/event-handler patterns "
        "— frontend boilerplate; refactoring requires dedicated JS test coverage"
    ),
    # --- Cross-file structural similarity: independent API modules ---
    ("apis/transaction_notifications/api.py", "apis/transaction_notifications/api.py"): (
        "Large single-file API with consent-enrollment handlers that each share the same "
        "param-guard + OAuth-sign pattern — structural within-file similarity, not extractable logic"
    ),
    ("apis/carbon_calculator/api.py", "apis/flight_delay_pass/api.py"): (
        "Independent API modules sharing OAuth1 signing helper and JWE operation structures "
        "— per-API module design; cross-module extraction adds coupling with no clear benefit"
    ),
    ("apis/benefits_eligibility/api.py", "apis/carbon_calculator/api.py"): (
        "Independent API modules sharing OAuth1 signing boilerplate "
        "— each is a self-contained data + request definition unit"
    ),
    ("apis/benefits_eligibility/api.py", "apis/flight_delay_pass/api.py"): (
        "Independent API modules sharing OAuth1 signing boilerplate "
        "— each is a self-contained data + request definition unit"
    ),
    ("apis/open_finance/api.py", "apis/open_finance_au/api.py"): (
        "Regional Open Finance API variants (global vs AU) — structurally similar by design, "
        "independently maintained for different Mastercard Open Banking regions"
    ),
    ("apis/easy_savings/api.py", "apis/places/api.py"): (
        "Both are location/offer search APIs with similar geographic parameter dicts "
        "— independent modules sharing query-parameter schema by product design"
    ),
    ("apis/open_finance_au/api.py", "apis/open_finance_eu/api.py"): (
        "Regional Open Finance API variants (AU vs EU) — structurally similar by design, "
        "independently maintained for different Mastercard Open Banking regions"
    ),
    ("apis/offers_for_publishers/api.py", "apis/offers_merchant_content/api.py"): (
        "Closely related Offers product APIs sharing response schema and parameter patterns "
        "— independently maintained per-API modules in the same product family"
    ),
    ("apis/benefits_content_eligibility/api.py", "apis/benefits_eligibility/api.py"): (
        "Benefits API family sharing eligibility parameter structures "
        "— independently maintained per-API modules in the same product family"
    ),
    ("apis/open_finance_au/client.py", "apis/open_finance_eu/client.py"): (
        "Regional Open Finance client implementations (AU Finicity vs EU JWT OAuth2) "
        "— structural similarity is intentional; independently maintained for different auth flows"
    ),
    # --- Legacy alias modules (canonical id <-> legacy id) ---
    # Each legacy-id module is a back-compat shim that mirrors its canonical
    # counterpart so old .env prefixes, artifact names and imports keep working
    # (see apis/catalog.py `legacy_id`). The near-identical body is the shim.
    ("apis/open_finance/api.py", "apis/ofin/api.py"): "Legacy alias shim: 'ofin' mirrors canonical 'open_finance'.",
    ("apis/open_finance/client.py", "apis/ofin/client.py"): "Legacy alias shim: 'ofin' client mirrors 'open_finance' client.",
    ("apis/priceless_cities/api.py", "apis/priceless/api.py"): "Legacy alias shim: 'priceless' mirrors 'priceless_cities'.",
    ("apis/offers_merchant_content/api.py", "apis/ofmc/api.py"): "Legacy alias shim: 'ofmc' mirrors 'offers_merchant_content'.",
    ("apis/offers_for_publishers/api.py", "apis/ofpub/api.py"): "Legacy alias shim: 'ofpub' mirrors 'offers_for_publishers'.",
    ("apis/transaction_notifications/api.py", "apis/txnotify/api.py"): "Legacy alias shim: 'txnotify' mirrors 'transaction_notifications'.",
    ("apis/transaction_notifications/api.py", "apis/consent/api.py"): "Legacy alias shim: 'consent' is merged into 'transaction_notifications'.",
    ("apis/benefits_eligibility/api.py", "apis/eligibility/api.py"): "Legacy alias shim: 'eligibility' mirrors 'benefits_eligibility'.",
    ("apis/benefits_content_eligibility/api.py", "apis/bces/api.py"): "Legacy alias shim: 'bces' mirrors 'benefits_content_eligibility'.",
    ("apis/easy_savings/api.py", "apis/easysavings/api.py"): "Legacy alias shim: 'easysavings' mirrors 'easy_savings'.",
    ("apis/consumer_clarity/api.py", "apis/clarity/api.py"): "Legacy alias shim: 'clarity' mirrors 'consumer_clarity'.",
    ("apis/bin_lookup/api.py", "apis/binlookup/api.py"): "Legacy alias shim: 'binlookup' mirrors 'bin_lookup'.",
    ("usecases/bin_lookup/__init__.py", "usecases/binlookup/__init__.py"): "Legacy alias shim: 'binlookup' use case mirrors 'bin_lookup'.",
    ("usecases/consumer_clarity/__init__.py", "usecases/clarity/__init__.py"): "Legacy alias shim: 'clarity' use case mirrors 'consumer_clarity'.",
    ("usecases/easy_savings/__init__.py", "usecases/easysavings/__init__.py"): "Legacy alias shim: 'easysavings' use case mirrors 'easy_savings'.",
    # --- Within-file repeated boilerplate (self-pairs) ---
    ("apis/ofin/api.py", "apis/ofin/api.py"): (
        "Legacy alias of open_finance; repeated per-endpoint param dicts mirror the "
        "canonical module's within-file structural similarity (already allowlisted there)."
    ),
    ("apis/consent/api.py", "apis/consent/api.py"): (
        "Legacy consent shim; repeated 3DS/enrollment handlers share the same param-guard "
        "+ OAuth-sign pattern — within-file structural similarity, not extractable logic."
    ),
    ("static/js/app.js", "static/js/app.js"): (
        "Legacy pre-split UI monolith; repeated panel/event-handler patterns — frontend "
        "boilerplate retained for back-compat while logic lives in static/js/app/*."
    ),
    # --- Legacy JS monolith vs the modules it was split into ---
    ("static/js/app.js", "static/js/app/main.js"): "Legacy app.js monolith duplicates the split-out app/main.js module.",
    ("static/js/app.js", "static/js/app/workbench/core.js"): "Legacy app.js monolith duplicates the split-out app/workbench/core.js module.",
    ("static/js/app.js", "static/js/app/features/apiCallLog.js"): "Legacy app.js monolith duplicates the split-out app/features/apiCallLog.js module.",
    # --- Same product-family structural similarity (shared schemas) ---
    ("apis/ofmc/api.py", "apis/ofpub/api.py"): "Offers product family — legacy shims share response/param schemas by design.",
    ("apis/offers_merchant_content/api.py", "apis/ofpub/api.py"): "Offers product family — shared response/param schemas across related APIs.",
    ("apis/offers_for_publishers/api.py", "apis/ofmc/api.py"): "Offers product family — shared response/param schemas across related APIs.",
    ("apis/bces/api.py", "apis/eligibility/api.py"): "Benefits product family — legacy shims share eligibility param schemas by design.",
    ("apis/easysavings/api.py", "apis/places/api.py"): "Location/offer search APIs share geographic parameter schema by product design.",
    ("apis/ofin/api.py", "apis/open_finance_au/api.py"): "Regional Open Finance variants (legacy ofin vs AU) — structurally similar by design.",
}


# ── File collection ────────────────────────────────────────────────────────────

def _collect_files(root: str) -> list[str]:
    files: list[str] = []
    for target in _TARGETS:
        path = os.path.join(root, target)
        if os.path.isfile(path):
            if path.endswith((".py", ".js")) and ".min.js" not in path:
                files.append(os.path.normpath(path))
        elif os.path.isdir(path):
            for ext in ("*.py", "*.js"):
                files.extend(
                    os.path.normpath(p)
                    for p in glob.glob(os.path.join(path, "**", ext), recursive=True)
                    if ".min.js" not in p
                    and os.sep + "node_modules" + os.sep not in os.path.normpath(p)
                )
    return sorted(set(files))


# ── Line normalisation ─────────────────────────────────────────────────────────

def _is_trivial(line: str) -> bool:
    s = line.strip()
    if not s:
        return True
    # Python / JS single-line comments
    if s.startswith("#") or s.startswith("//"):
        return True
    # Very short structural lines that are noise (braces, pass, etc.)
    if s in ("{", "}", "};", "pass", "...", "return", "break", "continue"):
        return True
    return False


def _normalise_lines(filepath: str) -> list[tuple[int, str]]:
    """Return (original_lineno, normalised_text) for non-trivial lines."""
    try:
        with open(filepath, encoding="utf-8", errors="replace") as fh:
            raw = fh.readlines()
    except OSError:
        return []

    result: list[tuple[int, str]] = []
    for i, line in enumerate(raw, 1):
        if _is_trivial(line):
            continue
        # Collapse internal whitespace; treat different indent as equivalent
        normalised = " ".join(line.split())
        result.append((i, normalised))
    return result


# ── Hashing ────────────────────────────────────────────────────────────────────

def _window_hashes(
    lines: list[tuple[int, str]], window: int
) -> list[tuple[str, int, int]]:
    """Yield (sha256, first_lineno, last_lineno) for every window."""
    out: list[tuple[str, int, int]] = []
    for i in range(len(lines) - window + 1):
        chunk = lines[i : i + window]
        text = "\n".join(norm for _, norm in chunk)
        h = hashlib.sha256(text.encode()).hexdigest()
        out.append((h, chunk[0][0], chunk[-1][0]))
    return out


# ── Clone detection ────────────────────────────────────────────────────────────

def _merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    merged: list[list[int]] = []
    for start, end in sorted(ranges):
        if merged and start <= merged[-1][1] + 1:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return [(s, e) for s, e in merged]


def _find_clone_pairs(
    files: list[str],
) -> list[tuple[str, str, int, list[tuple[int, int]], list[tuple[int, int]]]]:
    """
    Returns a list of (file_a, file_b, dup_lines, ranges_a, ranges_b), sorted
    descending by dup_lines (lines counted once per file, merged, file_a side).
    """
    # Build hash → [(filepath, start, end), ...]
    hash_map: dict[str, list[tuple[str, int, int]]] = {}
    file_lines: dict[str, list[tuple[int, str]]] = {}

    for fpath in files:
        lines = _normalise_lines(fpath)
        file_lines[fpath] = lines
        if len(lines) < _MIN_LINES:
            continue
        for h, start, end in _window_hashes(lines, _MIN_LINES):
            hash_map.setdefault(h, []).append((fpath, start, end))

    # Group duplicate windows by (file_a, file_b) pair
    pair_windows: dict[
        tuple[str, str], list[tuple[tuple[int, int], tuple[int, int]]]
    ] = {}

    for h, occurrences in hash_map.items():
        if len(occurrences) < 2:
            continue
        # Limit combinatorial explosion: cap at 8 occurrences per hash
        for i in range(min(len(occurrences), 8)):
            for j in range(i + 1, min(len(occurrences), 8)):
                fa, sa, ea = occurrences[i]
                fb, sb, eb = occurrences[j]
                if fa == fb and sa == sb:
                    continue  # same location
                # Canonical ordering so (a,b) == (b,a)
                key: tuple[str, str] = (fa, fb) if fa <= fb else (fb, fa)
                ra = (sa, ea) if fa <= fb else (sb, eb)
                rb = (sb, eb) if fa <= fb else (sa, ea)
                pair_windows.setdefault(key, []).append((ra, rb))

    results = []
    for (fa, fb), windows in pair_windows.items():
        ranges_a = _merge_ranges([r for r, _ in windows])
        ranges_b = _merge_ranges([r for _, r in windows])
        dup_a = sum(e - s + 1 for s, e in ranges_a)
        dup_b = sum(e - s + 1 for s, e in ranges_b)
        dup_lines = max(dup_a, dup_b)
        results.append((fa, fb, dup_lines, ranges_a, ranges_b))

    return sorted(results, key=lambda x: -x[2])


# ── Runner ─────────────────────────────────────────────────────────────────────

def run(base_url: str = "") -> TestRunner:  # base_url unused — static analysis
    runner = TestRunner("Code Duplication (pure Python)")

    root = _ROOT

    files = _collect_files(root)
    py_count = sum(1 for f in files if f.endswith(".py"))
    js_count = sum(1 for f in files if f.endswith(".js"))

    def _scan_scope():
        pass

    runner.run(
        f"Scan scope: {len(files)} file(s) ({py_count} Python, {js_count} JavaScript)\n"
        f"  Targets:       {', '.join(_TARGETS)}\n"
        f"  Window size:   {_MIN_LINES} lines (normalised)\n"
        f"  Report threshold: {_DUP_LINE_THRESHOLD} duplicated lines per pair",
        _scan_scope,
    )

    if not files:
        def _no_files():
            pass
        runner.run("No source files found", _no_files)
        return runner

    pairs = _find_clone_pairs(files)

    def _rel(path: str) -> str:
        try:
            return os.path.relpath(path, root).replace("\\", "/")
        except ValueError:
            return path

    def _ignore_reason(fa: str, fb: str) -> str | None:
        ra, rb = _rel(fa), _rel(fb)
        return _IGNORED_PAIRS.get((ra, rb)) or _IGNORED_PAIRS.get((rb, ra))

    # Split into failures, explicitly-ignored, and informational (below threshold)
    failures = [
        (fa, fb, n, ra, rb) for fa, fb, n, ra, rb in pairs
        if n >= _DUP_LINE_THRESHOLD and not _ignore_reason(fa, fb)
    ]
    ignored  = [
        (fa, fb, n, ra, rb) for fa, fb, n, ra, rb in pairs
        if n >= _DUP_LINE_THRESHOLD and _ignore_reason(fa, fb)
    ]
    info     = [(fa, fb, n, ra, rb) for fa, fb, n, ra, rb in pairs if 0 < n < _DUP_LINE_THRESHOLD]

    if not failures and not ignored and not info:
        def _clean():
            pass
        runner.run(f"All {len(files)} file(s) clean — no significant duplication found", _clean)
        return runner

    # ── Explicitly ignored (above threshold but architectural / intentional) ──
    for fa, fb, dup_lines, _ra, _rb in ignored:
        reason = _ignore_reason(fa, fb) or ""
        label = f"Ignored: {_rel(fa)} <-> {_rel(fb)}"

        def _make_ignored(lbl: str, r: str, n: int):
            def _t():
                pass
            _t.__doc__ = f"{n} shared lines — ignored\n  Reason: {r}"
            return _t

        runner.run(
            f"{label}\n  {dup_lines} shared line(s) — ignored\n  Reason: {reason}",
            _make_ignored(label, reason, dup_lines),
        )

    # ── Informational (below threshold) ───────────────────────────────────────
    if info:
        info_lines = []
        for fa, fb, n, ra, rb in info:
            info_lines.append(f"  {_rel(fa)} <-> {_rel(fb)}: {n} shared line(s)")

        def _make_info(msg: str):
            def _t():
                pass
            return _t

        runner.run(
            f"{len(info)} pair(s) with minor duplication (< {_DUP_LINE_THRESHOLD} lines) — informational\n"
            + "\n".join(info_lines),
            _make_info("\n".join(info_lines)),
        )

    # ── Failures (above threshold) ─────────────────────────────────────────────
    for fa, fb, dup_lines, ranges_a, ranges_b in failures:
        ra_str = ", ".join(
            f"L{s}-{e}" if s != e else f"L{s}"
            for s, e in ranges_a[:6]
        ) + (" ..." if len(ranges_a) > 6 else "")
        rb_str = ", ".join(
            f"L{s}-{e}" if s != e else f"L{s}"
            for s, e in ranges_b[:6]
        ) + (" ..." if len(ranges_b) > 6 else "")

        label = f"{_rel(fa)} <-> {_rel(fb)}"
        detail = (
            f"{dup_lines} duplicated line(s) between:\n"
            f"  {_rel(fa)}: {ra_str}\n"
            f"  {_rel(fb)}: {rb_str}"
        )
        captured = [detail]

        def _make_fail(msg: str):
            def _t():
                raise AssertionError(msg)
            return _t

        runner.run(label, _make_fail(captured[0]))

    return runner


if __name__ == "__main__":
    from tests.lib.utils import Summary
    s = Summary()
    s.add(run())
    s.print_and_exit()
