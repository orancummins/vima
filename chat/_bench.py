"""Benchmark the Vima Chat agent loop on real UI-change tasks.

Run from the project root:
    py -m chat._bench

Reports per-task: pass/fail, wall time, # tool calls, tool-call mix, total
characters streamed back. Uses the real Anthropic API but does its file work
in a temp copy of the target so the repo isn't mutated.
"""
from __future__ import annotations

import json
import shutil
import sys
import tempfile
import time
from pathlib import Path

# Inject OS cert store BEFORE any HTTPS clients are created (matches what
# app.py does at startup).
import truststore

truststore.inject_into_ssl()

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from chat.app import PROJECT_ROOT, _make_chat_generator  # noqa: E402


def _consume(gen):
    """Drain the SSE generator, returning (events, raw_text, elapsed)."""
    events: list[dict] = []
    raw = []
    t0 = time.time()
    for chunk in gen():
        raw.append(chunk)
        if chunk.startswith("data:"):
            try:
                events.append(json.loads(chunk[5:].strip()))
            except Exception:
                pass
    return events, "".join(raw), time.time() - t0


def _run_task(label: str, work_subdir: str, message: str, verifier):
    """Copy work_subdir into a temp scratch, run the agent, verify the change."""
    src = PROJECT_ROOT / work_subdir
    if not src.is_dir():
        print(f"[SKIP] {label}: source dir not found: {src}")
        return

    with tempfile.TemporaryDirectory(prefix="vima-bench-") as tmp:
        scratch_root = Path(tmp) / "vima_root"
        # Mirror just enough of the project for read_root to work: copy whole
        # repo minus heavy/noisy dirs.
        EXCLUDE = {".git", ".venv", "venv", "__pycache__", "node_modules",
                   "simulator", "config", ".vscode", ".idea"}
        shutil.copytree(
            PROJECT_ROOT, scratch_root,
            ignore=shutil.ignore_patterns(*EXCLUDE),
        )
        work_dir = scratch_root / work_subdir
        conversation = [{"role": "user", "content": message}]
        gen = _make_chat_generator(
            gen_conversation=conversation,
            work_dir=work_dir,
            system_prompt=(
                f"You are a coding assistant working on {work_subdir}.\n"
                f"Write scope: {work_dir}\nRead scope: {scratch_root}\n"
                "Use grep_files first when you don't know which file holds something. "
                "Use patch_file for edits. Stop when done — no recap."
            ),
            model="claude-sonnet-4-6",
            read_root=scratch_root,
        )
        events, raw, elapsed = _consume(gen)

        tool_calls = [e for e in events if e["type"] == "tool_executing"]
        errors = [e for e in events if e["type"] == "error"]
        text_chunks = [e["content"] for e in events if e["type"] == "text"]
        text_out = "".join(text_chunks)

        ok, detail = verifier(work_dir)
        status = "PASS" if ok else "FAIL"

        from collections import Counter
        mix = Counter(t["name"] for t in tool_calls)

        print(f"\n=== {label} ===")
        print(f"  status      : {status}  ({detail})")
        print(f"  elapsed     : {elapsed:.1f}s")
        print(f"  tool calls  : {sum(mix.values())}  {dict(mix)}")
        print(f"  text out    : {len(text_out)} chars")
        print(f"  errors      : {len(errors)}")
        for e in errors:
            print(f"     ! {e.get('message','')[:140]}")
        if not ok:
            tail = text_out[-400:].replace("\n", " ")
            print(f"  last text   : {tail}")
        return {
            "label": label, "status": status, "elapsed": elapsed,
            "tool_calls": sum(mix.values()), "mix": dict(mix),
            "errors": len(errors),
        }


# ─── Verifiers ────────────────────────────────────────────────────────────────

def _verify_color_change(work: Path):
    html = (work / "testchat.html").read_text(encoding="utf-8", errors="replace")
    if "#00ff00" in html and "#a855f7" not in html:
        return True, "color updated and old value gone"
    if "#00ff00" in html:
        return True, "new color present (old value also still present)"
    return False, "#00ff00 not found in testchat.html"


def _verify_title_change(work: Path):
    html = (work / "testchat.html").read_text(encoding="utf-8", errors="replace")
    if "<title>Vima Test Chat</title>" in html:
        return True, "title replaced"
    return False, "expected <title>Vima Test Chat</title>"


def _verify_button_label(work: Path):
    html = (work / "testchat.html").read_text(encoding="utf-8", errors="replace")
    # The Refresh button should now read "Reload"
    import re
    m = re.search(r">\s*Reload\s*<", html)
    return (bool(m), "Refresh -> Reload landed" if m else "Reload text not found")


TASKS = [
    ("Change default globe color to #00ff00", "usecases/testchat",
     "In testchat.html, change the default globe color from #a855f7 to #00ff00 "
     "everywhere it appears as a default value (the input element AND the JS "
     "defaults object). Do not change anything else.",
     _verify_color_change),
    ("Set page <title> to 'Vima Test Chat'", "usecases/testchat",
     "Change the <title> tag in testchat.html so the page title reads "
     "exactly: Vima Test Chat",
     _verify_title_change),
    ("Rename the Refresh button to Reload", "usecases/testchat",
     "In testchat.html, rename the Refresh button so its visible label reads 'Reload' instead.",
     _verify_button_label),
]


if __name__ == "__main__":
    results = []
    for label, sub, msg, verifier in TASKS:
        r = _run_task(label, sub, msg, verifier)
        if r:
            results.append(r)
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    pass_n = sum(1 for r in results if r["status"] == "PASS")
    total_calls = sum(r["tool_calls"] for r in results)
    total_time = sum(r["elapsed"] for r in results)
    print(f"  {pass_n}/{len(results)} passed")
    print(f"  total tool calls : {total_calls}  (avg {total_calls/max(1,len(results)):.1f}/task)")
    print(f"  total wall time  : {total_time:.1f}s  (avg {total_time/max(1,len(results)):.1f}s/task)")
