"""tests/lib/install.py - obtain a working copy of the codebase.

Two modes:
  - clone_repo(dest_dir)  - git-clone from the remote URL detected in the
                            current working directory into *dest_dir*.
  - copy_local(src, dest) - fast local copy (no git required; good for
                            testing uncommitted changes).

Returns the absolute path to the directory that contains app.py.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import tempfile


def _git_remote_url(src_dir: str) -> str:
    """Return the first git remote URL, or raise RuntimeError."""
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            cwd=src_dir,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(
            f"Could not detect git remote URL in {src_dir!r}. "
            f"Make sure this is a git repository with an 'origin' remote. "
            f"stderr: {exc.stderr.strip()}"
        ) from exc
    except FileNotFoundError:
        raise RuntimeError(
            "git is not installed or not on PATH. "
            "Install git and re-run, or use copy_local() instead."
        )


def clone_repo(src_dir: str, dest_dir: str | None = None) -> str:
    """Clone the repo whose remote is detected in *src_dir* into *dest_dir*.

    If *dest_dir* is None a timestamped directory under the system temp
    folder is created automatically.

    Returns the absolute path to the cloned directory.
    """
    url = _git_remote_url(src_dir)

    if dest_dir is None:
        import time
        ts = time.strftime("%Y%m%d-%H%M%S")
        dest_dir = os.path.join(tempfile.gettempdir(), f"vima-test-{ts}")

    os.makedirs(dest_dir, exist_ok=True)
    print(f"  Cloning {url} -> {dest_dir} ...")

    try:
        subprocess.run(
            ["git", "clone", "--depth", "1", url, dest_dir],
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(
            f"git clone failed (exit {exc.returncode}). "
            f"Check network connectivity and portal access."
        ) from exc

    return os.path.abspath(dest_dir)


def copy_local(src_dir: str, dest_dir: str | None = None) -> str:
    """Copy *src_dir* to *dest_dir* (or a new temp dir) and return dest path.

    Ignores: .venv, __pycache__, config/keys, config/.env, *.pyc, .git.
    """
    if dest_dir is None:
        import time
        ts = time.strftime("%Y%m%d-%H%M%S")
        dest_dir = os.path.join(tempfile.gettempdir(), f"vima-copy-{ts}")

    _IGNORE = shutil.ignore_patterns(
        ".venv", "__pycache__", "*.pyc", ".git",
        "*.p12", "*.pem", "*.key", ".env",
    )
    print(f"  Copying {src_dir} -> {dest_dir} ...")
    shutil.copytree(src_dir, dest_dir, ignore=_IGNORE)
    return os.path.abspath(dest_dir)


def install_dependencies(work_dir: str) -> None:
    """Run pip install -r requirements.txt inside *work_dir* using run.bat/run.sh
    or directly via pip if the launchers are not available."""
    req_path = os.path.join(work_dir, "requirements.txt")
    if not os.path.isfile(req_path):
        print("  requirements.txt not found — skipping pip install.")
        return

    import sys
    python = sys.executable
    venv_win = os.path.join(work_dir, ".venv", "Scripts", "python.exe")
    venv_nix = os.path.join(work_dir, ".venv", "bin", "python3")
    if os.path.isfile(venv_win):
        python = venv_win
    elif os.path.isfile(venv_nix):
        python = venv_nix

    print("  Installing dependencies ...")
    cmd = [python, "-m", "pip", "install", "-r", req_path, "--quiet"]
    # Use truststore for corporate proxy cert chains when available
    try:
        subprocess.run(
            cmd + ["--use-feature=truststore"],
            cwd=work_dir,
            check=True,
        )
    except subprocess.CalledProcessError:
        # Older pip or truststore unavailable — try without flag
        subprocess.run(cmd, cwd=work_dir, check=True)
