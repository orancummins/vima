"""tests/lib/server.py — start / stop the Flask app server.

Launches `app.py` as a subprocess, polls until ready, and provides
a clean shutdown method.  Works on both Windows and macOS/Linux.
"""
from __future__ import annotations

import os
import sys
import time
import signal
import subprocess
from typing import Optional

import requests


_DEFAULT_PORT     = 9021
_DEFAULT_BASE_URL = f"http://127.0.0.1:{_DEFAULT_PORT}"
_POLL_INTERVAL    = 0.5   # seconds between readiness checks


def _python_exe(work_dir: str) -> str:
    """Return the best Python executable for *work_dir*.

    Prefers the venv inside work_dir, then the current interpreter (which
    already has all deps if we're running inside a venv), then falls back
    to `py` (Windows launcher) / `python3`.
    """
    candidates: list[str] = []

    venv_win = os.path.join(work_dir, ".venv", "Scripts", "python.exe")
    venv_nix = os.path.join(work_dir, ".venv", "bin", "python3")
    if os.path.isfile(venv_win):
        candidates.append(venv_win)
    if os.path.isfile(venv_nix):
        candidates.append(venv_nix)

    # Current interpreter (likely already in the venv)
    candidates.append(sys.executable)

    # Platform fallbacks
    if sys.platform == "win32":
        candidates.extend(["py", "python"])
    else:
        candidates.extend(["python3", "python"])

    for exe in candidates:
        if os.path.isfile(exe):
            return exe
        # For PATH-resolved names (py, python3 …) test with where/which
        try:
            subprocess.run(
                [exe, "--version"],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            return exe
        except (FileNotFoundError, subprocess.CalledProcessError):
            continue

    return "python"


def start_server(work_dir: str, port: int = _DEFAULT_PORT) -> subprocess.Popen:
    """Start `app.py` in *work_dir* and return the Popen handle.

    Stdout / stderr are left connected to the parent so server tracebacks
    are visible in the test output.  The process is started without the
    Flask debug reloader so it stays as a single PID.
    """
    python = _python_exe(work_dir)
    env = {**os.environ, "FLASK_ENV": "development", "PORT": str(port)}
    proc = subprocess.Popen(
        [python, "app.py", "--port", str(port)],
        cwd=work_dir,
        env=env,
        # Keep stdout/stderr visible so server tracebacks appear in test output
    )
    return proc


def wait_server_ready(
    base_url: str = _DEFAULT_BASE_URL,
    timeout: float = 30.0,
) -> None:
    """Poll GET /app until a 200 response is received or *timeout* expires.

    Raises RuntimeError on timeout.
    """
    deadline = time.time() + timeout
    last_err: Optional[Exception] = None
    while time.time() < deadline:
        try:
            r = requests.get(f"{base_url}/app", timeout=3)
            if r.status_code == 200:
                return
        except requests.RequestException as exc:
            last_err = exc
        time.sleep(_POLL_INTERVAL)
    raise RuntimeError(
        f"Server at {base_url} did not become ready within {timeout:.0f}s. "
        f"Last error: {last_err}"
    )


def stop_server(proc: subprocess.Popen) -> None:
    """Terminate the server process gracefully, then forcibly if needed."""
    if proc.poll() is not None:
        return  # already exited
    try:
        if sys.platform == "win32":
            proc.terminate()
        else:
            proc.send_signal(signal.SIGTERM)
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()
    except Exception:
        pass
