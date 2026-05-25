import os
import json
from pathlib import Path

from flask import Blueprint, render_template, request, jsonify, Response, stream_with_context
import anthropic
from dotenv import load_dotenv, dotenv_values

_config_env_path = Path(__file__).parent.parent / "config" / ".env"
load_dotenv(_config_env_path)

from .config import MODEL, MAX_FILE_SIZE, MODELS, DEFAULT_MODEL_ID

# Blueprint mounted at /chat by the main Vima app. Vima Chat is no longer
# available as a standalone service — it is only usable from within
# Mastercard Solution Studio (same origin, same Flask process).
chat_bp = Blueprint(
    "chat",
    __name__,
    url_prefix="/chat",
    template_folder="templates",
)

# ─── Anthropic client ──────────────────────────────────────────────────────────
# Re-reads the API key from config/.env on each call so changes via the UI
# take effect without restarting the server.
_current_api_key: str | None = dotenv_values(_config_env_path).get("ANTHROPIC_API_KEY")
if not _current_api_key:
    print("WARNING: ANTHROPIC_API_KEY is not set in config/.env -- Claude API calls will fail.")
client = anthropic.Anthropic(api_key=_current_api_key or "", timeout=60.0)


def _refresh_client_if_needed() -> None:
    """Re-create the Anthropic client if the API key in config/.env has changed."""
    global client, _current_api_key
    fresh_key = dotenv_values(_config_env_path).get("ANTHROPIC_API_KEY") or ""
    if fresh_key != (_current_api_key or ""):
        _current_api_key = fresh_key
        client = anthropic.Anthropic(api_key=fresh_key, timeout=60.0)


# Project root: the server install directory. Claude reads/writes relative to
# this root; writes are further confined to the per-item subdirectory supplied
# by the client (a use case or API folder).
PROJECT_ROOT = Path(__file__).parent.parent.resolve()
_simple_conversations: dict[str, list] = {}

# ─── Tool definitions ──────────────────────────────────────────────────────────
TOOLS = [
    {
        "name": "list_directory",
        "description": "List files/folders at a relative path inside the work dir.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Relative path; '.' for root."},
            },
            "required": ["path"],
        },
    },
    {
        "name": "read_file",
        "description": "Read a file. Default returns up to 400 lines from the top; for more, pass start_line/end_line (1-indexed). Max 1500 lines per call. The response always includes total_lines so you know whether to request more.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "start_line": {"type": "integer", "description": "1-indexed first line."},
                "end_line": {"type": "integer", "description": "1-indexed last line, inclusive."},
            },
            "required": ["path"],
        },
    },
    {
        "name": "search_file",
        "description": "Case-insensitive substring search inside ONE file; returns matching lines with numbers. Use grep_files instead if you don't know which file.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "pattern": {"type": "string"},
                "context_lines": {"type": "integer", "description": "Lines of context per match. Default 3."},
            },
            "required": ["path", "pattern"],
        },
    },
    {
        "name": "grep_files",
        "description": "Recursively search across all files in the work dir for a substring (case-insensitive). Returns {path, line, text} hits. USE THIS FIRST when you don't know which file contains what you need to change — it avoids chains of list_directory + read_file. Skips binary files and common noise dirs.",
        "input_schema": {
            "type": "object",
            "properties": {
                "pattern": {"type": "string"},
                "glob": {"type": "string", "description": "Optional fnmatch-style filename glob (e.g. '*.html', '*.py'). Default: all text files."},
                "max_results": {"type": "integer", "description": "Cap on hits. Default 80."},
            },
            "required": ["pattern"],
        },
    },
    {
        "name": "write_file",
        "description": "Create or fully overwrite a file. Use patch_file for edits to existing files.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "content": {"type": "string"},
            },
            "required": ["path", "content"],
        },
    },
    {
        "name": "patch_file",
        "description": "Replace old_string with new_string in a file. By default replaces exactly one occurrence (include 2-3 lines of context to make old_string unique). Set replace_all=true to replace EVERY occurrence in the file in one call — use this when the user says 'everywhere', 'all occurrences', or you have grepped and know there are multiple sites. AVOID for blocks that contain unusual characters (box-drawing ─│└, smart quotes, emoji) — use replace_lines instead because byte-exact matching is fragile across encodings.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "old_string": {"type": "string"},
                "new_string": {"type": "string"},
                "replace_all": {"type": "boolean", "description": "If true, replace every occurrence. Default false."},
            },
            "required": ["path", "old_string", "new_string"],
        },
    },
    {
        "name": "replace_lines",
        "description": "Replace a contiguous range of lines [start_line, end_line] (both 1-based, inclusive) with new_text. Set new_text to an empty string to DELETE those lines. This is the PREFERRED tool when you have line numbers from grep_files/read_file and need to remove or rewrite a block — it never fails on whitespace, line-ending, or encoding mismatches. Always read_file the range first to confirm the line numbers.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "start_line": {"type": "integer", "description": "1-based inclusive start line."},
                "end_line": {"type": "integer", "description": "1-based inclusive end line."},
                "new_text": {"type": "string", "description": "Replacement text. Empty string deletes the range. Do NOT include a trailing newline unless you want a blank line at the end of the inserted block."},
            },
            "required": ["path", "start_line", "end_line", "new_text"],
        },
    },
    {
        "name": "multi_edit",
        "description": "Apply MULTIPLE edits in a single atomic tool call. All edits succeed or none are written. Each edit is either {op:'patch', path, old_string, new_string, replace_all?} or {op:'replace_lines', path, start_line, end_line, new_text}. USE THIS whenever you need to make 2+ related edits (e.g. removing a UI element AND its CSS AND its JS handlers) — it halves round-trips and guarantees you don't leave a file half-edited. Edits to the SAME file are applied top-to-bottom; for replace_lines ops on the same file sort them by start_line DESCENDING so earlier line numbers stay valid.",
        "input_schema": {
            "type": "object",
            "properties": {
                "edits": {
                    "type": "array",
                    "description": "Ordered list of edit operations. All applied atomically.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "op": {"type": "string", "enum": ["patch", "replace_lines"]},
                            "path": {"type": "string"},
                            "old_string": {"type": "string"},
                            "new_string": {"type": "string"},
                            "replace_all": {"type": "boolean"},
                            "start_line": {"type": "integer"},
                            "end_line": {"type": "integer"},
                            "new_text": {"type": "string"},
                        },
                        "required": ["op", "path"],
                    },
                },
            },
            "required": ["edits"],
        },
    },
]

# ─── Helpers ───────────────────────────────────────────────────────────────────

def _validate_vima_path(path_str: str):
    """Resolve a path and confirm it exists, is a directory, and is inside
    PROJECT_ROOT. Returns (resolved_path, None) on success, (None, error) on failure."""
    try:
        resolved = Path(path_str).resolve()
    except Exception as exc:
        return None, f"Invalid path: {exc}"
    if not resolved.exists():
        return None, f"Directory not found: {resolved}"
    if not resolved.is_dir():
        return None, f"Not a directory: {resolved}"
    try:
        resolved.relative_to(PROJECT_ROOT)
    except ValueError:
        return None, f"Path is outside the Vima project root: {resolved}"
    return resolved, None


def _vima_md() -> str:
    """Return contents of vima.md at the project root, or empty string."""
    candidate = PROJECT_ROOT / "vima.md"
    if candidate.is_file():
        try:
            return candidate.read_text(encoding="utf-8")
        except Exception:
            return ""
    return ""


def _safe_path(relative: str, work_dir: Path, read_root: Path | None = None, write: bool = False) -> Path:
    """Resolve `relative` against work_dir and verify it stays within the
    appropriate boundary.

    - For write/exec operations (write=True), the resolved path MUST be inside
      work_dir.
    - For read operations, the path may resolve anywhere inside read_root
      (typically the project root), so Claude can study sibling code.
    """
    target = (work_dir / relative).resolve()
    boundary = work_dir if (write or read_root is None) else read_root
    try:
        target.relative_to(boundary)
    except ValueError:
        scope = "work directory" if boundary == work_dir else "project root"
        raise ValueError(f"Access denied: '{relative}' is outside the {scope}.")
    return target


# ─── Pure edit helpers (shared by patch_file / replace_lines / multi_edit) ────

def _apply_patch_to_string(content: str, old_string: str, new_string: str, replace_all: bool) -> dict:
    """Return {'new_text': ..., 'replacements': N} or {'error': ...}."""
    count = content.count(old_string)
    if count == 0:
        first_line = next((ln for ln in old_string.splitlines() if ln.strip()), "").strip()
        hint_lines: list[str] = []
        if first_line:
            for i, ln in enumerate(content.splitlines(), 1):
                if first_line in ln:
                    hint_lines.append(f"  L{i}: {ln}")
                    if len(hint_lines) >= 5:
                        break
        hint = (
            "\n\nLines containing the first line of your old_string (whitespace may differ):\n" + "\n".join(hint_lines)
        ) if hint_lines else ""
        return {
            "error": (
                "old_string not found in file. Common causes: extra/missing leading whitespace, "
                "tabs vs spaces, or CRLF vs LF line endings. Use read_file with start_line/end_line "
                "to copy the exact bytes, or switch to replace_lines." + hint
            )
        }
    if count > 1 and not replace_all:
        return {"error": f"old_string matches {count} locations \u2014 either make it more specific or pass replace_all=true."}
    n = count if replace_all else 1
    return {"new_text": content.replace(old_string, new_string), "replacements": n}


def _apply_replace_lines_to_string(content: str, start_line, end_line, new_text: str) -> dict:
    """Return {'new_text': ..., 'lines_removed': N, 'lines_inserted': M} or {'error': ...}."""
    try:
        start = int(start_line)
        end = int(end_line)
    except (TypeError, ValueError):
        return {"error": "start_line and end_line must be integers (1-based, inclusive)."}
    nl = "\r\n" if "\r\n" in content else "\n"
    lines = content.split(nl)
    total = len(lines) - 1 if lines and lines[-1] == "" else len(lines)
    if start < 1 or end < start or start > total:
        return {"error": f"Invalid range [{start},{end}] for file with {total} lines."}
    if end > total:
        end = total
    before = lines[: start - 1]
    after = lines[end:]
    new_chunk = new_text.split(nl) if new_text != "" else []
    merged = before + new_chunk + after
    return {
        "new_text": nl.join(merged),
        "lines_removed": end - start + 1,
        "lines_inserted": len(new_chunk),
    }


def _apply_patch_to_text(path: Path, old_string: str, new_string: str, replace_all: bool) -> dict:
    if not path.exists():
        return {"error": f"File not found: {path}"}
    if not path.is_file():
        return {"error": f"Not a file: {path}"}
    content = path.read_text(encoding="utf-8", errors="replace")
    return _apply_patch_to_string(content, old_string, new_string, replace_all)


def _apply_replace_lines_to_text(path: Path, start_line, end_line, new_text: str) -> dict:
    if not path.exists():
        return {"error": f"File not found: {path}"}
    if not path.is_file():
        return {"error": f"Not a file: {path}"}
    content = path.read_text(encoding="utf-8", errors="replace")
    return _apply_replace_lines_to_string(content, start_line, end_line, new_text)


def _execute_tool(name: str, inp: dict, work_dir: Path, read_root: Path | None = None) -> dict:
    """Execute a tool and return a JSON-serialisable result dict.

    Reads honour `read_root` (defaults to work_dir if not given); writes are
    always confined to work_dir.
    """
    wd = work_dir
    rr = read_root or work_dir
    try:
        if name == "list_directory":
            path = _safe_path(inp.get("path", "."), wd, rr)
            if not path.exists():
                return {"error": f"Path not found: {inp.get('path')}"}
            if not path.is_dir():
                return {"error": f"Not a directory: {inp.get('path')}"}
            items = [
                {
                    "name": item.name,
                    "type": "directory" if item.is_dir() else "file",
                    "size": item.stat().st_size if item.is_file() else None,
                }
                for item in sorted(path.iterdir())
            ]
            return {"path": inp.get("path", "."), "items": items}

        elif name == "read_file":
            path = _safe_path(inp["path"], wd, rr)
            if not path.exists():
                return {"error": f"File not found: {inp['path']}"}
            if not path.is_file():
                return {"error": f"Not a file: {inp['path']}"}
            if path.stat().st_size > MAX_FILE_SIZE:
                return {"error": f"File exceeds {MAX_FILE_SIZE // 1024 // 1024} MB limit."}
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)
            total = len(lines)
            DEFAULT_WINDOW = 400
            MAX_WINDOW = 1500
            has_start = inp.get("start_line") is not None
            has_end = inp.get("end_line") is not None
            if not has_start and not has_end:
                start = 0
                end = min(total, DEFAULT_WINDOW)
            else:
                start = max(1, int(inp.get("start_line") or 1)) - 1
                end = min(total, int(inp.get("end_line") or total))
            # Hard cap to keep token usage sane even if Claude asks for too much
            if end - start > MAX_WINDOW:
                end = start + MAX_WINDOW
            selected = lines[start:end]
            return {
                "path": inp["path"],
                "start_line": start + 1,
                "end_line": end,
                "total_lines": total,
                "content": "".join(selected),
            }

        elif name == "search_file":
            path = _safe_path(inp["path"], wd, rr)
            if not path.exists():
                return {"error": f"File not found: {inp['path']}"}
            if not path.is_file():
                return {"error": f"Not a file: {inp['path']}"}
            pattern = inp.get("pattern", "").lower()
            ctx = max(0, int(inp.get("context_lines") or 3))
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
            total = len(lines)
            matches = [i for i, l in enumerate(lines) if pattern in l.lower()]
            if not matches:
                return {"path": inp["path"], "pattern": inp["pattern"], "matches": []}
            results = []
            covered: set = set()
            for mi in matches:
                lo, hi = max(0, mi - ctx), min(total - 1, mi + ctx)
                block = [
                    {"line": lo + 1 + j, "text": lines[lo + j], "match": (lo + j) == mi}
                    for j in range(hi - lo + 1)
                    if (lo + j) not in covered
                ]
                covered.update(range(lo, hi + 1))
                if block:
                    results.append(block)
            return {
                "path": inp["path"],
                "pattern": inp["pattern"],
                "total_lines": total,
                "match_count": len(matches),
                "matches": results,
            }

        elif name == "grep_files":
            import fnmatch
            pattern = (inp.get("pattern") or "").lower()
            if not pattern:
                return {"error": "pattern is required"}
            glob_pat = inp.get("glob") or ""
            max_results = max(1, min(500, int(inp.get("max_results") or 80)))
            SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv", "venv",
                         "dist", "build", ".next", ".cache", ".idea", ".vscode"}
            TEXT_EXT = {".py", ".js", ".ts", ".jsx", ".tsx", ".html", ".css",
                        ".scss", ".json", ".md", ".txt", ".yml", ".yaml",
                        ".toml", ".ini", ".cfg", ".sh", ".bat", ".env"}
            MAX_FILE = 2 * 1024 * 1024  # skip files >2MB
            hits: list[dict] = []
            files_scanned = 0
            try:
                for root, dirs, files in os.walk(rr):
                    dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
                    for fname in files:
                        if glob_pat and not fnmatch.fnmatch(fname, glob_pat):
                            continue
                        if not glob_pat:
                            ext = os.path.splitext(fname)[1].lower()
                            if ext and ext not in TEXT_EXT:
                                continue
                        fpath = Path(root) / fname
                        try:
                            if fpath.stat().st_size > MAX_FILE:
                                continue
                            text = fpath.read_text(encoding="utf-8", errors="replace")
                        except Exception:
                            continue
                        files_scanned += 1
                        rel = str(fpath.relative_to(rr)).replace("\\", "/")
                        for i, line in enumerate(text.splitlines(), 1):
                            if pattern in line.lower():
                                hits.append({"path": rel, "line": i, "text": line[:300]})
                                if len(hits) >= max_results:
                                    break
                        if len(hits) >= max_results:
                            break
                    if len(hits) >= max_results:
                        break
            except Exception as exc:
                return {"error": f"grep_files error: {exc}"}
            return {
                "pattern": inp.get("pattern"),
                "glob": glob_pat or None,
                "files_scanned": files_scanned,
                "match_count": len(hits),
                "truncated": len(hits) >= max_results,
                "matches": hits,
            }

        elif name == "patch_file":
            path = _safe_path(inp["path"], wd, write=True)
            res = _apply_patch_to_text(
                path,
                inp.get("old_string", ""),
                inp.get("new_string", ""),
                bool(inp.get("replace_all", False)),
            )
            if "error" in res:
                return res
            path.write_text(res["new_text"], encoding="utf-8")
            return {"success": True, "path": inp["path"], "replacements": res["replacements"]}

        elif name == "replace_lines":
            path = _safe_path(inp["path"], wd, write=True)
            res = _apply_replace_lines_to_text(
                path,
                inp.get("start_line"),
                inp.get("end_line"),
                inp.get("new_text", ""),
            )
            if "error" in res:
                return res
            path.write_text(res["new_text"], encoding="utf-8")
            return {
                "success": True,
                "path": inp["path"],
                "lines_removed": res["lines_removed"],
                "lines_inserted": res["lines_inserted"],
            }

        elif name == "multi_edit":
            edits = inp.get("edits") or []
            if not isinstance(edits, list) or not edits:
                return {"error": "multi_edit requires a non-empty 'edits' array."}
            # Group edits by resolved path; apply in array order against an
            # in-memory string for each file. Only flush to disk after all
            # edits succeed, so any failure leaves the workspace untouched.
            file_state: dict[Path, str] = {}
            file_paths: dict[Path, str] = {}  # resolved -> original input path string
            per_edit: list[dict] = []
            for idx, e in enumerate(edits):
                if not isinstance(e, dict):
                    return {"error": f"edit {idx}: not an object"}
                op = e.get("op")
                rel = e.get("path")
                if op not in ("patch", "replace_lines") or not rel:
                    return {"error": f"edit {idx}: missing or invalid op/path"}
                try:
                    p = _safe_path(rel, wd, write=True)
                except ValueError as exc:
                    return {"error": f"edit {idx} ({rel}): {exc}"}
                if not p.exists() or not p.is_file():
                    return {"error": f"edit {idx} ({rel}): file not found"}
                if p not in file_state:
                    file_state[p] = p.read_text(encoding="utf-8", errors="replace")
                    file_paths[p] = rel
                if op == "patch":
                    sub = _apply_patch_to_string(
                        file_state[p],
                        e.get("old_string", ""),
                        e.get("new_string", ""),
                        bool(e.get("replace_all", False)),
                    )
                else:  # replace_lines
                    sub = _apply_replace_lines_to_string(
                        file_state[p],
                        e.get("start_line"),
                        e.get("end_line"),
                        e.get("new_text", ""),
                    )
                if "error" in sub:
                    return {"error": f"edit {idx} ({rel}, op={op}): {sub['error']}"}
                file_state[p] = sub["new_text"]
                per_edit.append({"op": op, "path": rel, **{k: v for k, v in sub.items() if k != "new_text"}})
            # All succeeded — flush
            for p, txt in file_state.items():
                p.write_text(txt, encoding="utf-8")
            return {
                "success": True,
                "files_modified": [file_paths[p] for p in file_state.keys()],
                "edits_applied": per_edit,
            }

        elif name == "write_file":
            path = _safe_path(inp["path"], wd, write=True)
            content = inp.get("content", "")
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            return {"success": True, "path": inp["path"], "bytes_written": len(content.encode())}

        else:
            return {"error": f"Unknown tool: {name}"}

    except ValueError as exc:
        return {"error": str(exc)}
    except Exception as exc:
        return {"error": f"Tool error: {exc}"}


def _sse(data: dict) -> str:
    return f"data: {json.dumps(data)}\n\n"


# ─── Shared SSE streaming generator ───────────────────────────────────────────

# Approx max characters of conversation history to keep in context.
# At ~4 chars/token this is roughly 30k tokens of history.
_MAX_CONV_CHARS = 120_000
# Number of most-recent tool_result blocks whose content we keep verbatim.
# Older tool_results have their content replaced with a short placeholder.
_KEEP_RECENT_TOOL_RESULTS = 6


def _trim_conversation(conv: list) -> None:
    """Mutate `conv` in place to keep token usage bounded.

    1. Replace older tool_result contents with a short placeholder so the
       tool_use_id linkage stays valid but the bytes are dropped.
    2. If still too long, drop oldest assistant+user pair until we fit.
       Never split a tool_use / tool_result pair.
    """
    # 1) Elide older tool_results
    tr_idx: list[tuple[int, int]] = []
    for mi, msg in enumerate(conv):
        content = msg.get("content")
        if msg.get("role") == "user" and isinstance(content, list):
            for bi, blk in enumerate(content):
                if isinstance(blk, dict) and blk.get("type") == "tool_result":
                    tr_idx.append((mi, bi))

    if len(tr_idx) > _KEEP_RECENT_TOOL_RESULTS:
        for mi, bi in tr_idx[: -_KEEP_RECENT_TOOL_RESULTS]:
            blk = conv[mi]["content"][bi]
            existing = blk.get("content")
            if existing and existing != "[elided]":
                blk["content"] = "[elided: prior tool result removed to save context]"

    # 2) Drop oldest assistant+user pair until under budget
    def _size(c: list) -> int:
        return len(json.dumps(c, default=str))

    while _size(conv) > _MAX_CONV_CHARS and len(conv) >= 2:
        first_assistant = next(
            (i for i, m in enumerate(conv) if m.get("role") == "assistant"), None
        )
        if first_assistant is None:
            break
        end = first_assistant + 2 if first_assistant + 1 < len(conv) else first_assistant + 1
        del conv[first_assistant:end]


def _apply_message_cache(conv: list) -> None:
    """Place a single ephemeral cache breakpoint on the last content block of
    the most recent message, and clear any previously placed message-level
    cache markers. Combined with the cached system prompt this gives Anthropic
    a stable prefix to reuse across every tool-loop iteration.
    """
    # Strip any prior message-level cache_control markers
    for msg in conv:
        content = msg.get("content")
        if isinstance(content, list):
            for blk in content:
                if isinstance(blk, dict):
                    blk.pop("cache_control", None)

    if not conv:
        return
    last = conv[-1]
    content = last.get("content")
    if isinstance(content, str):
        last["content"] = [{"type": "text", "text": content,
                            "cache_control": {"type": "ephemeral"}}]
    elif isinstance(content, list) and content:
        # Find the last dict block and mark it
        for blk in reversed(content):
            if isinstance(blk, dict):
                blk["cache_control"] = {"type": "ephemeral"}
                break


def _make_chat_generator(gen_conversation: list, work_dir, system_prompt: str, model: str | None = None, read_root: Path | None = None):
    """Return the SSE-streaming agentic-loop generator for a given work context."""
    # Hot-reload the API key if it changed via the config UI
    _refresh_client_if_needed()
    # Cache the (large, stable) system prompt + tools across loop iterations and
    # turns within a session. This dramatically reduces latency and cost on the
    # 2nd+ tool call within the same conversation.
    cached_system = [{"type": "text", "text": system_prompt, "cache_control": {"type": "ephemeral"}}]
    use_model = model or MODEL
    # Extended thinking gives the model a private scratchpad before it picks
    # tool calls. Materially better at "remove X without breaking dependents"
    # tasks. Haiku doesn't support it. Opus 4.7+ uses the new "adaptive"
    # thinking API; Sonnet 4.6 and earlier use the legacy "enabled" form.
    thinking_kwargs: dict = {}
    if "haiku" not in use_model:
        if "opus" in use_model:
            # New adaptive API on Opus 4.7+ — model auto-sizes its scratchpad
            # based on task complexity, controlled by output_config.effort.
            thinking_kwargs["thinking"] = {"type": "adaptive"}
            thinking_kwargs["output_config"] = {"effort": "medium"}
        else:
            thinking_kwargs["thinking"] = {"type": "enabled", "budget_tokens": 2000}

    def generate():
        MAX_LOOPS = 30
        _trim_conversation(gen_conversation)
        # Running token totals across every loop iteration in this turn.
        totals = {"input": 0, "output": 0, "cache_creation": 0, "cache_read": 0}
        for loop_idx in range(MAX_LOOPS):
            text_chunks: list[str] = []
            tool_uses: list[dict] = []
            # Thinking blocks must be preserved verbatim and replayed back on
            # the next turn when extended thinking + tool_use are interleaved.
            thinking_blocks: list[dict] = []
            in_tool = False
            in_thinking = False
            cur_tool_id = cur_tool_name = cur_tool_json = None
            cur_thinking_text = ""
            cur_thinking_sig = ""

            # Add an ephemeral cache breakpoint on the LAST message so the
            # entire conversation prefix is reused across loop iterations.
            # This cuts ~70-90% of input cost/latency in multi-tool turns.
            _apply_message_cache(gen_conversation)

            try:
                with client.messages.stream(
                    model=use_model,
                    max_tokens=16384,
                    system=cached_system,
                    tools=TOOLS,
                    messages=gen_conversation,
                    **thinking_kwargs,
                ) as stream:
                    for event in stream:
                        etype = getattr(event, "type", None)

                        if etype == "content_block_start":
                            blk = event.content_block
                            if blk.type == "text":
                                in_tool = False
                                in_thinking = False
                            elif blk.type == "thinking":
                                in_thinking = True
                                cur_thinking_text = ""
                                cur_thinking_sig = ""
                            elif blk.type == "tool_use":
                                in_tool = True
                                cur_tool_id = blk.id
                                cur_tool_name = blk.name
                                cur_tool_json = ""
                                yield _sse({"type": "tool_start", "name": blk.name})

                        elif etype == "content_block_delta":
                            delta = event.delta
                            dtype = getattr(delta, "type", None)
                            if dtype == "text_delta":
                                text_chunks.append(delta.text)
                                yield _sse({"type": "text", "content": delta.text})
                            elif dtype == "input_json_delta":
                                if cur_tool_json is not None:
                                    cur_tool_json += delta.partial_json
                            elif dtype == "thinking_delta":
                                cur_thinking_text += delta.thinking
                            elif dtype == "signature_delta":
                                cur_thinking_sig += delta.signature

                        elif etype == "content_block_stop":
                            if in_tool and cur_tool_id:
                                try:
                                    tool_input = json.loads(cur_tool_json) if cur_tool_json else {}
                                except json.JSONDecodeError:
                                    tool_input = {}
                                tool_uses.append({
                                    "id": cur_tool_id,
                                    "name": cur_tool_name,
                                    "input": tool_input,
                                })
                                in_tool = False
                            elif in_thinking:
                                thinking_blocks.append({
                                    "type": "thinking",
                                    "thinking": cur_thinking_text,
                                    "signature": cur_thinking_sig,
                                })
                                in_thinking = False

                    final_msg = stream.get_final_message()
                    stop_reason = final_msg.stop_reason
                    usage = final_msg.usage
                    totals["input"] += getattr(usage, "input_tokens", 0) or 0
                    totals["output"] += getattr(usage, "output_tokens", 0) or 0
                    totals["cache_creation"] += getattr(usage, "cache_creation_input_tokens", 0) or 0
                    totals["cache_read"] += getattr(usage, "cache_read_input_tokens", 0) or 0

            except anthropic.APIStatusError as exc:
                # Graceful fallback: if the model rejects our thinking config
                # (model variants change this API), drop thinking and retry
                # the same loop iteration once.
                msg = str(getattr(exc, "message", exc))
                if exc.status_code == 400 and thinking_kwargs and ("thinking" in msg or "output_config" in msg):
                    thinking_kwargs.clear()
                    continue
                yield _sse({"type": "error", "message": f"Claude API error {exc.status_code}: {msg}"})
                return
            except anthropic.APIError as exc:
                yield _sse({"type": "error", "message": f"Claude API error: {exc}"})
                return
            except Exception as exc:
                yield _sse({"type": "error", "message": f"Unexpected error communicating with Claude: {exc}"})
                return

            # Record assistant turn in conversation. Thinking blocks MUST come
            # first when present and MUST be replayed verbatim, otherwise the
            # API rejects the next request when tool_use is involved.
            content_blocks: list[dict] = []
            content_blocks.extend(thinking_blocks)
            if text_chunks:
                content_blocks.append({"type": "text", "text": "".join(text_chunks)})
            for tu in tool_uses:
                content_blocks.append({
                    "type": "tool_use",
                    "id": tu["id"],
                    "name": tu["name"],
                    "input": tu["input"],
                })
            if content_blocks:
                gen_conversation.append({"role": "assistant", "content": content_blocks})

            # Done — no tool calls
            if stop_reason == "end_turn" or not tool_uses:
                yield _sse({"type": "usage", **totals, "model": use_model})
                yield _sse({"type": "done"})
                return

            # Execute tools and loop
            tool_results = []
            for tu in tool_uses:
                yield _sse({"type": "tool_executing", "name": tu["name"], "input": tu["input"]})
                result = _execute_tool(tu["name"], tu["input"], work_dir, read_root=read_root)
                yield _sse({"type": "tool_result", "name": tu["name"], "result": result})
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": tu["id"],
                    "content": json.dumps(result),
                })

            gen_conversation.append({"role": "user", "content": tool_results})

        yield _sse({"type": "usage", **totals, "model": use_model})
        yield _sse({"type": "error", "message": f"Reached max tool-use loops ({MAX_LOOPS}). Stopping."})
        yield _sse({"type": "done"})

    return generate


_SSE_RESPONSE_HEADERS = {
    "Cache-Control": "no-cache",
    "X-Accel-Buffering": "no",
    "Connection": "keep-alive",
}


# ─── Simple (modal-embedded) chat ──────────────────────────────────────────────

@chat_bp.route("/simple")
def simple():
    return render_template("simple.html")


@chat_bp.route("/api/simple/items")
def api_simple_items():
    """Return use cases and APIs from the in-process registries, scoped to PROJECT_ROOT."""
    base = PROJECT_ROOT

    # Import locally to avoid a hard import-time dependency when this module
    # is loaded outside the Vima app context (e.g. tests).
    try:
        from apis import registry as api_registry
        from usecases import registry as usecase_registry
        catalog_apis = api_registry.manifests()
        catalog_ucs = usecase_registry.manifests()
    except Exception as exc:
        return jsonify({"error": f"Could not load Vima registries: {exc}"}), 500

    def resolve_item(category: str, item_id: str) -> dict:
        """Scope work_dir to the item's own directory so Claude is sandboxed to it."""
        dir_path = base / category / item_id
        if dir_path.is_dir():
            return {"path": str(dir_path), "file": "."}
        py_path = base / category / f"{item_id}.py"
        if py_path.exists():
            return {"path": str(py_path.parent), "file": py_path.name}
        return {"path": str(base / category), "file": item_id}

    result = {
        "base": str(base),
        "usecases": [
            {
                "name": uc["name"],
                "id": uc["id"],
                **resolve_item("usecases", uc["id"]),
            }
            for uc in catalog_ucs
        ],
        "apis": [
            {
                "name": api["name"],
                "id": api["id"],
                **resolve_item("apis", api["id"]),
            }
            for api in catalog_apis
        ],
    }
    return jsonify(result)


@chat_bp.route("/api/simple/chat/clear", methods=["POST"])
def api_simple_chat_clear():
    data = request.get_json() or {}
    sid = data.get("session_id")
    if sid and sid in _simple_conversations:
        del _simple_conversations[sid]
    return jsonify({"success": True})


@chat_bp.route("/api/simple/chat", methods=["POST"])
def api_simple_chat():
    data = request.get_json() or {}
    session_id = data.get("session_id", "")
    user_message = data.get("message", "").strip()
    work_dir_param = data.get("work_dir", "")
    item_name = data.get("item_name", "")
    item_type = data.get("item_type", "")  # "usecase" or "api"
    item_file = data.get("item_file", "")  # specific filename if single-file module
    model_id = data.get("model") or DEFAULT_MODEL_ID

    # Validate model against whitelist
    allowed_model_ids = {m["id"] for m in MODELS}
    if model_id not in allowed_model_ids:
        model_id = DEFAULT_MODEL_ID

    if not session_id or not user_message:
        return jsonify({"error": "session_id and message are required"}), 400

    # Resolve work directory. Require an explicit work_dir from the client and
    # verify it sits inside PROJECT_ROOT. No fallback — a missing/invalid
    # work_dir is always a client bug.
    if not work_dir_param:
        return jsonify({"error": "work_dir is required \u2014 select an item from the list first."}), 400
    work_dir, err = _validate_vima_path(work_dir_param)
    if err:
        return jsonify({"error": err}), 400

    if session_id not in _simple_conversations:
        _simple_conversations[session_id] = []

    conversation = _simple_conversations[session_id]

    item_label = (
        f"{'Use Case' if item_type == 'usecase' else 'API'} '{item_name}'"
        if item_name else "the selected item"
    )

    # Detect whether item_file points to a file or a directory and PRELOAD the
    # primary file's contents into the conversation as a synthetic tool_use +
    # tool_result pair. This grounds the model in real bytes immediately and
    # eliminates the wasted first-round-trip "let me read the file" that
    # otherwise happens on every single turn.
    preload_text = ""
    item_is_dir = False
    item_exists = False
    if item_file:
        try:
            item_path = (work_dir / item_file).resolve()
            item_path.relative_to(work_dir)
            item_is_dir = item_path.is_dir()
            item_exists = item_path.exists()
        except Exception:
            pass

        if item_exists and not item_is_dir and len(conversation) == 0:
            # Only preload on the first turn — subsequent turns reuse history.
            try:
                file_bytes = item_path.read_bytes()
                if len(file_bytes) <= MAX_FILE_SIZE:
                    raw = file_bytes.decode("utf-8", errors="replace")
                    lines = raw.splitlines()
                    LIMIT = 1500
                    truncated = len(lines) > LIMIT
                    shown = lines[:LIMIT]
                    numbered = "\n".join(f"{i:5d} | {ln}" for i, ln in enumerate(shown, 1))
                    preload_text = (
                        f"Pre-loaded contents of `{item_file}` "
                        f"({len(lines)} total lines"
                        f"{', truncated to first 1500' if truncated else ''}):\n"
                        f"```\n{numbered}\n```"
                    )
            except Exception:
                preload_text = ""

    if item_file:
        if item_is_dir:
            first_step = (
                f"The work directory IS the {item_label} directory. "
                f"Start by calling list_directory on \".\" to see what's inside, "
                f"then read the relevant file(s)."
            )
        elif item_exists:
            if preload_text:
                first_step = (
                    f"The primary file `{item_file}` has been pre-loaded for you below "
                    f"(do NOT call read_file on it again unless you need a range outside the preload). "
                    f"Make your edits directly using patch_file / replace_lines / multi_edit."
                )
            else:
                first_step = (
                    f"The primary file for this item is `{item_file}` (relative to the work directory). "
                    f"Read that file first."
                )
        else:
            first_step = (
                f"The item is at `{item_file}` but it does not exist yet \u2014 "
                f"call list_directory on \".\" to confirm before creating anything."
            )
        file_instruction = f"\n{first_step}"
    else:
        file_instruction = (
            "\nStart by calling list_directory with path \".\" to explore the project, "
            "then identify which files relate to the item you are working on."
        )

    # Stitch user message: optionally prepend the preload so the model sees it
    # before the actual request.
    if preload_text:
        conversation.append({
            "role": "user",
            "content": f"{preload_text}\n\n---\n\n{user_message}",
        })
    else:
        conversation.append({"role": "user", "content": user_message})

    # Read access spans the whole Vima project so Claude can study sibling
    # use cases / APIs and copy patterns. Writes remain confined to work_dir.
    read_root = PROJECT_ROOT
    try:
        rel_wd = str(Path(work_dir).resolve().relative_to(read_root)).replace("\\", "/")
    except Exception:
        rel_wd = str(work_dir)

    system_prompt = f"""You are a coding assistant embedded in the Vima platform, working on {item_label}.

Write scope (you can create/edit/run here): {work_dir}
Read scope (you can browse/read but NOT modify): {read_root}
The write scope is `{rel_wd}` relative to the read scope, so e.g. `../findacard/index.html` reads a sibling use case.
{file_instruction}

Tools:
- grep_files: recursive substring search across the WHOLE project — USE THIS FIRST. Pass a `glob` like `*.html` or `*.py` to narrow.
- list_directory, search_file (single file), read_file (defaults to first 400 lines; pass start_line/end_line for more).
- patch_file (exact-string replace for small/simple edits — include 2-3 lines of context to make old_string unique; pass replace_all=true for bulk changes).
- replace_lines (PREFERRED for removing or rewriting a multi-line block when you know the line numbers from grep_files/read_file — never fails on whitespace/encoding).
- multi_edit (PREFERRED whenever you need 2+ related edits — applied atomically, all-or-nothing).
- write_file (only for NEW files).

Workflow for a typical change:
1. If unsure of the style/structure, grep_files or read_file a sibling item under the read scope to copy the pattern.
2. grep_files for the symbol/text you need to touch — note the line numbers and how many hits there are.
3. **Before deleting or moving any UI element (HTML tag, button, section), grep_files for its `id`, class name, or visible text to find dependent CSS rules and JS handlers. Removing an element without removing its dependents is the #1 cause of broken UIs.**
4. read_file the matching range (use start_line/end_line near the hit) BEFORE editing so you know exact line numbers and bytes.
5. Edit. If you have 2+ changes (e.g. HTML + CSS + JS for one feature removal), bundle them into ONE multi_edit call — atomic and faster.
   - To DELETE a block or rewrite ≥3 lines: replace_lines.
   - Small targeted swap (1-2 lines, no unusual chars): patch_file.
   - "Change everywhere": patch_file with replace_all=true.
6. If patch_file returns "old_string not found", do NOT retry with a different anchor — switch to replace_lines.
7. Once edit tools return success, stop. Do NOT re-read or re-grep to "verify". Do NOT write a recap.

Rules:
- Writes MUST target paths inside the write scope. Never use write_file to edit an existing file.
- NEVER invent a file path. If a file isn't shown by list_directory or grep_files, it does not exist — do not create a directory or file unless the user explicitly asked for a NEW item.
- You may issue multiple independent tool_use blocks in one response to parallelise.
- You MUST make at least one tool call (read_file/grep_files at minimum) before claiming a change is unnecessary. NEVER assume the file already matches the desired state — verify with read_file or grep_files first.
- If your verification shows the requested change is already present in the WRITE SCOPE file (not a sibling under the read scope), say so explicitly ("file already in the requested state, no edit needed") rather than implying you made an edit."""
    return Response(
        stream_with_context(
            _make_chat_generator(conversation, work_dir, system_prompt, model=model_id, read_root=read_root)()
        ),
        mimetype="text/event-stream",
        headers=_SSE_RESPONSE_HEADERS,
    )


@chat_bp.route("/api/simple/models")
def api_simple_models():
    return jsonify({"models": MODELS, "default": DEFAULT_MODEL_ID})
