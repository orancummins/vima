import os
import json
import subprocess
from pathlib import Path

from flask import Flask, render_template, request, jsonify, Response, stream_with_context, send_from_directory
import anthropic
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / "config" / ".env")
load_dotenv(Path(__file__).parent / ".env")  # fallback / overrides for chat-specific vars

from config import WORK_DIR, MODEL, MAX_FILE_SIZE, ALLOWED_COMMANDS, VIMA_URL, MODELS, DEFAULT_MODEL_ID

app = Flask(__name__)

# ─── Anthropic client ──────────────────────────────────────────────────────────
_api_key = os.environ.get("ANTHROPIC_API_KEY")
if not _api_key:
    print("WARNING: ANTHROPIC_API_KEY is not set -- Claude API calls will fail.")
client = anthropic.Anthropic(api_key=_api_key)

# ─── Runtime-mutable allowed commands (updated via Settings tab) ───────────────
_allowed_commands: list[str] = list(ALLOWED_COMMANDS)

# ─── Per-session conversation history (includes tool results) ─────────────────
_conversations: dict[str, list] = {}

# ─── Simple-mode config (modal embedded chat) ─────────────────────────────────
SIMPLE_WORK_DIR = Path(
    os.environ.get(
        "SIMPLE_WORK_DIR",
        str(Path(__file__).parent.parent / "usecases" / "testchat"),
    )
).resolve()
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
        "description": "Read a file. For files >400 lines you MUST pass start_line/end_line (1-indexed). Max 1500 lines per call.",
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
        "description": "Case-insensitive substring search; returns matching lines with numbers. Use before read_file on large files.",
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
        "description": "Replace exactly one occurrence of old_string with new_string. Include 2-3 lines of context to make old_string unique.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "old_string": {"type": "string"},
                "new_string": {"type": "string"},
            },
            "required": ["path", "old_string", "new_string"],
        },
    },
    {
        "name": "run_command",
        "description": "Run a whitelisted shell command in the work dir.",
        "input_schema": {
            "type": "object",
            "properties": {"command": {"type": "string"}},
            "required": ["command"],
        },
    },
]

# ─── Helpers ───────────────────────────────────────────────────────────────────

def _work_dir() -> Path:
    return Path(WORK_DIR).resolve()

def _validate_vima_path(path_str: str):
    """Resolve a path and confirm it exists and is a directory.
    Returns (resolved_path, None) on success, (None, error_str) on failure."""
    try:
        resolved = Path(path_str).resolve()
    except Exception as exc:
        return None, f"Invalid path: {exc}"
    if not resolved.exists():
        return None, f"Directory not found: {resolved}"
    if not resolved.is_dir():
        return None, f"Not a directory: {resolved}"
    return resolved, None


def _vima_base() -> str:
    """Return the simple mode base directory from config."""
    return str(SIMPLE_WORK_DIR)


def _vima_md() -> str:
    """Walk up from SIMPLE_WORK_DIR looking for vima.md; return its contents or empty string."""
    path = SIMPLE_WORK_DIR
    for _ in range(6):
        candidate = path / "vima.md"
        if candidate.is_file():
            try:
                return candidate.read_text(encoding="utf-8")
            except Exception:
                return ""
        if path == path.parent:  # filesystem root
            break
        path = path.parent
    return ""


def _safe_path(relative: str, work_dir=None) -> Path:
    """Resolve a relative path inside work_dir; raises ValueError on traversal."""
    wd = work_dir or _work_dir()
    target = (wd / relative).resolve()
    try:
        target.relative_to(wd)
    except ValueError:
        raise ValueError(f"Access denied: '{relative}' is outside the work directory.")
    return target


def _command_allowed(command: str, allowed_cmds=None) -> bool:
    cmd = command.strip()
    for prefix in (allowed_cmds or _allowed_commands):
        p = prefix.strip()
        if cmd == p or cmd.startswith(p + " "):
            return True
    return False


def _execute_tool(name: str, inp: dict, work_dir=None, allowed_cmds=None) -> dict:
    """Execute a tool and return a JSON-serialisable result dict."""
    wd = work_dir or _work_dir()
    cmds = allowed_cmds if allowed_cmds is not None else _allowed_commands
    try:
        if name == "list_directory":
            path = _safe_path(inp.get("path", "."), wd)
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
            path = _safe_path(inp["path"], wd)
            if not path.exists():
                return {"error": f"File not found: {inp['path']}"}
            if not path.is_file():
                return {"error": f"Not a file: {inp['path']}"}
            if path.stat().st_size > MAX_FILE_SIZE:
                return {"error": f"File exceeds {MAX_FILE_SIZE // 1024 // 1024} MB limit."}
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)
            total = len(lines)
            start = max(1, int(inp.get("start_line") or 1)) - 1
            end = min(total, int(inp.get("end_line") or total))
            selected = lines[start:end]
            return {
                "path": inp["path"],
                "start_line": start + 1,
                "end_line": end,
                "total_lines": total,
                "content": "".join(selected),
            }

        elif name == "search_file":
            path = _safe_path(inp["path"], wd)
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

        elif name == "patch_file":
            path = _safe_path(inp["path"], wd)
            if not path.exists():
                return {"error": f"File not found: {inp['path']}"}
            if not path.is_file():
                return {"error": f"Not a file: {inp['path']}"}
            old_string = inp.get("old_string", "")
            new_string = inp.get("new_string", "")
            content = path.read_text(encoding="utf-8", errors="replace")
            count = content.count(old_string)
            if count == 0:
                # Helpful hint: try matching the first non-empty line of old_string
                first_line = next((ln for ln in old_string.splitlines() if ln.strip()), "").strip()
                hint_lines = []
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
                        "tabs vs spaces, or CRLF vs LF line endings. Use search_file or read_file with "
                        "start_line/end_line to copy the exact bytes, then retry patch_file." + hint
                    )
                }
            if count > 1:
                return {"error": f"old_string matches {count} locations — make it more specific by including more surrounding context."}
            path.write_text(content.replace(old_string, new_string, 1), encoding="utf-8")
            return {"success": True, "path": inp["path"]}

        elif name == "write_file":
            path = _safe_path(inp["path"], wd)
            content = inp.get("content", "")
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            return {"success": True, "path": inp["path"], "bytes_written": len(content.encode())}

        elif name == "run_command":
            command = inp.get("command", "").strip()
            if not command:
                return {"error": "No command provided."}
            if not _command_allowed(command, cmds):
                return {
                    "error": f"Command not allowed: '{command}'",
                    "allowed_prefixes": cmds,
                }
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30,
                cwd=str(wd),
            )
            return {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode,
            }

        else:
            return {"error": f"Unknown tool: {name}"}

    except ValueError as exc:
        return {"error": str(exc)}
    except subprocess.TimeoutExpired:
        return {"error": "Command timed out after 30 seconds."}
    except Exception as exc:
        return {"error": f"Tool error: {exc}"}


def _sse(data: dict) -> str:
    return f"data: {json.dumps(data)}\n\n"


# ─── Routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html", work_dir=str(_work_dir()))


@app.route("/preview")
def preview():
    return send_from_directory(str(_work_dir()), "index.html")


@app.route("/preview/<path:filename>")
def preview_file(filename):
    try:
        _safe_path(filename)
    except ValueError:
        return "Forbidden", 403
    return send_from_directory(str(_work_dir()), filename)


# File API

@app.route("/api/files")
def api_files():
    rel = request.args.get("path", ".")
    return jsonify(_execute_tool("list_directory", {"path": rel}))


@app.route("/api/files/read")
def api_files_read():
    rel = request.args.get("path")
    if not rel:
        return jsonify({"error": "path parameter required"}), 400
    result = _execute_tool("read_file", {"path": rel})
    return jsonify(result), 400 if "error" in result else 200


@app.route("/api/files/write", methods=["POST"])
def api_files_write():
    data = request.get_json() or {}
    result = _execute_tool("write_file", data)
    return jsonify(result), 400 if "error" in result else 200


# Config API

@app.route("/api/config")
def api_config():
    return jsonify({
        "work_dir": str(_work_dir()),
        "model": MODEL,
        "allowed_commands": _allowed_commands,
    })


@app.route("/api/config/commands", methods=["POST"])
def api_config_commands():
    data = request.get_json() or {}
    commands = data.get("commands", [])
    if not isinstance(commands, list) or not all(isinstance(c, str) for c in commands):
        return jsonify({"error": "commands must be a list of strings"}), 400
    _allowed_commands.clear()
    _allowed_commands.extend(commands)
    return jsonify({"success": True, "allowed_commands": _allowed_commands})


# Chat clear

@app.route("/api/chat/clear", methods=["POST"])
def api_chat_clear():
    data = request.get_json() or {}
    sid = data.get("session_id")
    if sid and sid in _conversations:
        del _conversations[sid]
    return jsonify({"success": True})


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


def _make_chat_generator(gen_conversation: list, work_dir, allowed_cmds: list, system_prompt: str, model: str | None = None):
    """Return the SSE-streaming agentic-loop generator for a given work context."""
    # Cache the (large, stable) system prompt + tools across loop iterations and
    # turns within a session. This dramatically reduces latency and cost on the
    # 2nd+ tool call within the same conversation.
    cached_system = [{"type": "text", "text": system_prompt, "cache_control": {"type": "ephemeral"}}]
    use_model = model or MODEL

    def generate():
        MAX_LOOPS = 30
        _trim_conversation(gen_conversation)
        for loop_idx in range(MAX_LOOPS):
            text_chunks: list[str] = []
            tool_uses: list[dict] = []
            in_tool = False
            cur_tool_id = cur_tool_name = cur_tool_json = None

            try:
                with client.messages.stream(
                    model=use_model,
                    max_tokens=8096,
                    system=cached_system,
                    tools=TOOLS,
                    messages=gen_conversation,
                ) as stream:
                    for event in stream:
                        etype = getattr(event, "type", None)

                        if etype == "content_block_start":
                            blk = event.content_block
                            if blk.type == "text":
                                in_tool = False
                            elif blk.type == "tool_use":
                                in_tool = True
                                cur_tool_id = blk.id
                                cur_tool_name = blk.name
                                cur_tool_json = ""
                                yield _sse({"type": "tool_start", "name": blk.name})

                        elif etype == "content_block_delta":
                            delta = event.delta
                            if delta.type == "text_delta":
                                text_chunks.append(delta.text)
                                yield _sse({"type": "text", "content": delta.text})
                            elif delta.type == "input_json_delta":
                                if cur_tool_json is not None:
                                    cur_tool_json += delta.partial_json

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

                    final_msg = stream.get_final_message()
                    stop_reason = final_msg.stop_reason

            except anthropic.APIStatusError as exc:
                yield _sse({"type": "error", "message": f"Claude API error {exc.status_code}: {exc.message}"})
                return
            except anthropic.APIError as exc:
                yield _sse({"type": "error", "message": f"Claude API error: {exc}"})
                return

            # Record assistant turn in conversation
            content_blocks = []
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
                yield _sse({"type": "done"})
                return

            # Execute tools and loop
            tool_results = []
            for tu in tool_uses:
                yield _sse({"type": "tool_executing", "name": tu["name"], "input": tu["input"]})
                result = _execute_tool(tu["name"], tu["input"], work_dir, allowed_cmds)
                yield _sse({"type": "tool_result", "name": tu["name"], "result": result})
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": tu["id"],
                    "content": json.dumps(result),
                })

            gen_conversation.append({"role": "user", "content": tool_results})

        yield _sse({"type": "error", "message": f"Reached max tool-use loops ({MAX_LOOPS}). Stopping."})
        yield _sse({"type": "done"})

    return generate


_SSE_RESPONSE_HEADERS = {
    "Cache-Control": "no-cache",
    "X-Accel-Buffering": "no",
    "Connection": "keep-alive",
}


# Chat (SSE streaming)

@app.route("/api/chat", methods=["POST"])
def api_chat():
    data = request.get_json() or {}
    session_id = data.get("session_id", "")
    user_message = data.get("message", "").strip()

    if not session_id or not user_message:
        return jsonify({"error": "session_id and message are required"}), 400

    if session_id not in _conversations:
        _conversations[session_id] = []

    conversation = _conversations[session_id]
    conversation.append({"role": "user", "content": user_message})

    work_dir = _work_dir()
    system_prompt = f"""You are a helpful coding assistant with access to a code directory on the user's machine.

Work directory: {work_dir}

You have four tools available:
- list_directory: list files and folders
- read_file: read file contents
- write_file: create or overwrite files
- run_command: execute whitelisted terminal commands

Allowed terminal command prefixes: {json.dumps(_allowed_commands)}

Guidelines:
- Always read a file before modifying it so you understand its current state.
- Make precise, targeted changes and explain what you changed.
- After writing files, let the user know what was updated.
- Stay within the work directory at all times."""

    return Response(
        stream_with_context(_make_chat_generator(conversation, work_dir, _allowed_commands, system_prompt)()),
        mimetype="text/event-stream",
        headers=_SSE_RESPONSE_HEADERS,
    )


# ─── Simple (modal-embedded) chat ──────────────────────────────────────────────

@app.route("/simple")
def simple():
    return render_template("simple.html", work_dir=str(SIMPLE_WORK_DIR), vima_base=_vima_base())


@app.route("/api/simple/items")
def api_simple_items():
    """Return use cases and APIs from the vima /catalog endpoint.
    The dir param must still be a valid vima directory so we can resolve file paths.
    """
    dir_param = request.args.get("dir", "").strip()
    if not dir_param:
        return jsonify({"error": "dir parameter required"}), 400
    base, err = _validate_vima_path(dir_param)
    if err:
        return jsonify({"error": err}), 400

    # Fetch catalog from the running vima instance
    try:
        import urllib.request
        with urllib.request.urlopen(f"{VIMA_URL}/catalog", timeout=4) as resp:
            catalog = json.loads(resp.read())
    except Exception as exc:
        return jsonify({"error": f"Could not reach vima catalog at {VIMA_URL}/catalog: {exc}"}), 502

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
            for uc in catalog.get("use_cases", [])
        ],
        "apis": [
            {
                "name": api["name"],
                "id": api["id"],
                **resolve_item("apis", api["id"]),
            }
            for api in catalog.get("apis", [])
        ],
    }
    return jsonify(result)


@app.route("/api/simple/chat/clear", methods=["POST"])
def api_simple_chat_clear():
    data = request.get_json() or {}
    sid = data.get("session_id")
    if sid and sid in _simple_conversations:
        del _simple_conversations[sid]
    return jsonify({"success": True})


@app.route("/api/simple/chat", methods=["POST"])
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

    # Resolve work directory
    if work_dir_param:
        work_dir, err = _validate_vima_path(work_dir_param)
        if err:
            return jsonify({"error": err}), 400
    else:
        work_dir = SIMPLE_WORK_DIR

    if session_id not in _simple_conversations:
        _simple_conversations[session_id] = []

    conversation = _simple_conversations[session_id]
    conversation.append({"role": "user", "content": user_message})

    item_label = (
        f"{'Use Case' if item_type == 'usecase' else 'API'} '{item_name}'"
        if item_name else "the selected item"
    )

    # Detect whether item_file points to a file or a directory so we can give
    # Claude an accurate first-step instruction (avoids wasted read_file calls
    # on directories).
    if item_file:
        try:
            item_path = (work_dir / item_file).resolve()
            item_path.relative_to(work_dir)
            item_is_dir = item_path.is_dir()
            item_exists = item_path.exists()
        except Exception:
            item_is_dir = False
            item_exists = False

        if item_is_dir:
            first_step = (
                f"The work directory IS the {item_label} directory. "
                f"Start by calling list_directory on \".\" to see what's inside, "
                f"then read the relevant file(s)."
            )
        elif item_exists:
            first_step = (
                f"The primary file for this item is `{item_file}` (relative to the work directory). "
                f"Read that file first."
            )
        else:
            first_step = (
                f"The item is at `{item_file}` but it does not exist yet — "
                f"call list_directory on \".\" to confirm before creating anything."
            )
        file_instruction = f"\n{first_step}"
    else:
        file_instruction = (
            "\nStart by calling list_directory with path \".\" to explore the project, "
            "then identify which files relate to the item you are working on."
        )

    system_prompt = f"""You are a coding assistant embedded in the Vima platform, working on {item_label}.
Work directory (scoped to this item — all paths relative to this): {work_dir}
{file_instruction}

Tools: list_directory, search_file, read_file (use start_line/end_line for files >400 lines), patch_file (preferred for edits), write_file (only for new files), run_command.

Workflow:
1. If you know the file, go straight to search_file on it.
2. Read only the matching range with read_file start_line/end_line.
3. Apply the change with patch_file (old_string with 2-3 lines of context + new_string).
4. After all changes, finish with a concise bullet-point summary of EXACTLY what was changed: which files were edited and what was changed in each. No preamble.

Do NOT traverse outside the work directory, list parent dirs, read whole files, or use write_file for edits. You may issue multiple independent tool_use blocks in one response.

Allowed command prefixes: {json.dumps(sorted(_allowed_commands))}"""

    return Response(
        stream_with_context(
            _make_chat_generator(conversation, work_dir, _allowed_commands, system_prompt, model=model_id)()
        ),
        mimetype="text/event-stream",
        headers=_SSE_RESPONSE_HEADERS,
    )


@app.route("/api/simple/models")
def api_simple_models():
    return jsonify({"models": MODELS, "default": DEFAULT_MODEL_ID})


# ─── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    _work_dir().mkdir(parents=True, exist_ok=True)
    SIMPLE_WORK_DIR.mkdir(parents=True, exist_ok=True)
    print(f">>  Vima Chat running at http://localhost:3333")
    print(f"    Work directory : {_work_dir()}")
    print(f"    Simple dir     : {SIMPLE_WORK_DIR}")
    print(f"    Model          : {MODEL}")
    debug = os.environ.get("FLASK_DEBUG", "1") != "0"
    app.run(host="0.0.0.0", port=3333, debug=debug, use_reloader=debug, threaded=True)
