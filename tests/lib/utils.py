"""tests/lib/utils.py — shared test primitives.

Provides:
  - TestRunner   — collects pass/fail results, prints coloured output
  - assert_status / assert_json_field — convenience assertion helpers
  - get / post   — thin wrappers around requests with consistent error handling
"""
from __future__ import annotations

import sys
import json
import time
from dataclasses import dataclass, field
from typing import Any

import requests


def _ascii_safe(text: str) -> str:
    """Replace non-encodable chars with '?' for the current stdout encoding."""
    enc = getattr(sys.stdout, 'encoding', None) or 'ascii'
    return text.encode(enc, errors='replace').decode(enc)


def _safe_print(text: str) -> None:
    """Print *text*, replacing any unencodable characters with '?'."""
    print(_ascii_safe(text))


# ── ANSI colour helpers ────────────────────────────────────────────────────────
_USE_COLOUR = sys.stdout.isatty() or sys.platform == "win32"

def _c(code: str, text: str) -> str:
    if not _USE_COLOUR:
        return text
    return f"\033[{code}m{text}\033[0m"

def green(t: str) -> str:  return _c("32", t)
def red(t: str) -> str:    return _c("31", t)
def yellow(t: str) -> str: return _c("33", t)
def cyan(t: str) -> str:   return _c("36", t)
def bold(t: str) -> str:   return _c("1",  t)
def dim(t: str) -> str:    return _c("2",  t)


def _safe(text: str) -> str:
    """Return *text* with non-ASCII chars stripped when stdout is not UTF-8."""
    enc = getattr(sys.stdout, 'encoding', 'utf-8') or 'utf-8'
    try:
        text.encode(enc)
        return text
    except (UnicodeEncodeError, LookupError):
        return text.encode(enc, errors='replace').decode(enc)


# ── Result record ──────────────────────────────────────────────────────────────
@dataclass
class TestResult:
    name: str
    passed: bool
    message: str = ""


# ── TestRunner ─────────────────────────────────────────────────────────────────
class TestRunner:
    """Lightweight test collector.  Usage::

        runner = TestRunner("BIN Lookup API")
        runner.run("Execute lookup_bin", lambda: assert_status(get(base_url + "..."), 200))
        runner.summary()
    """

    def __init__(self, suite: str):
        self.suite = suite
        self.results: list[TestResult] = []
        print(f"\n{bold(cyan(f'>> {suite}'))}")

    def run(self, name: str, fn) -> bool:
        """Execute *fn*, record pass/fail.  Returns True on pass."""
        try:
            fn()
            self.results.append(TestResult(name, True))
            print(f"  {green('[PASS]')} {name}")
            return True
        except AssertionError as exc:
            msg = str(exc)
            self.results.append(TestResult(name, False, msg))
            print(f"  {red('[FAIL]')} {name}")
            if msg:
                _safe_print(f"    {dim(_ascii_safe(msg))}")
            return False
        except Exception as exc:
            msg = f"{type(exc).__name__}: {exc}"
            self.results.append(TestResult(name, False, msg))
            print(f"  {red('[FAIL]')} {name}")
            _safe_print(f"    {dim(_ascii_safe(msg))}")
            return False

    def passed(self) -> int:
        return sum(1 for r in self.results if r.passed)

    def failed(self) -> int:
        return sum(1 for r in self.results if not r.passed)

    def print_summary(self) -> None:
        p, f = self.passed(), self.failed()
        total = p + f
        colour = green if f == 0 else red
        print(f"  {colour(f'{p}/{total} passed')}")


# ── Global summary ─────────────────────────────────────────────────────────────
class Summary:
    def __init__(self):
        self._suites: list[TestRunner] = []

    def add(self, runner: TestRunner) -> None:
        self._suites.append(runner)

    def print_and_exit(self) -> None:
        total_p = sum(r.passed() for r in self._suites)
        total_f = sum(r.failed() for r in self._suites)
        total   = total_p + total_f
        print("\n" + "=" * 60)
        print(bold("Test Summary"))
        print("=" * 60)
        for r in self._suites:
            p, f = r.passed(), r.failed()
            icon = green("[OK]") if f == 0 else red("[FAIL]")
            print(f"  {icon}  {r.suite:<35} {p}/{p+f}")
        print("-" * 60)
        colour = green if total_f == 0 else red
        print(colour(bold(f"  {total_p}/{total} passed")))
        print("=" * 60 + "\n")
        sys.exit(0 if total_f == 0 else 1)


# ── HTTP helpers ───────────────────────────────────────────────────────────────
_DEFAULT_TIMEOUT = 20   # seconds


def get(url: str, **kwargs) -> requests.Response:
    kwargs.setdefault("timeout", _DEFAULT_TIMEOUT)
    return requests.get(url, **kwargs)


def post(url: str, payload: dict | None = None, **kwargs) -> requests.Response:
    kwargs.setdefault("timeout", _DEFAULT_TIMEOUT)
    return requests.post(url, json=payload, **kwargs)


# ── Assertions ─────────────────────────────────────────────────────────────────
def assert_status(resp: requests.Response, *expected: int) -> requests.Response:
    """Assert HTTP status is one of *expected*."""
    if resp.status_code not in expected:
        expected_str = " or ".join(str(e) for e in expected)
        raise AssertionError(
            f"Expected HTTP {expected_str}, got {resp.status_code}. "
            f"URL: {resp.url}. Body (first 200): {resp.text[:200]}"
        )
    return resp


def assert_json(resp: requests.Response) -> Any:
    """Parse response as JSON; raise AssertionError on failure."""
    try:
        return resp.json()
    except Exception:
        raise AssertionError(
            f"Response from {resp.url} is not valid JSON. "
            f"Content-Type: {resp.headers.get('content-type')}. "
            f"Body (first 200): {resp.text[:200]}"
        )


def assert_field(data: Any, *path: str | int, msg: str = "") -> Any:
    """Walk *path* into nested dict/list, assert it exists and is truthy."""
    cursor = data
    for step in path:
        try:
            cursor = cursor[step]
        except (KeyError, IndexError, TypeError):
            dotpath = ".".join(str(s) for s in path)
            raise AssertionError(msg or f"Missing field '{dotpath}' in response: {json.dumps(data)[:300]}")
    if cursor is None or cursor == "" or cursor == []:
        dotpath = ".".join(str(s) for s in path)
        raise AssertionError(msg or f"Field '{dotpath}' is empty/null in response.")
    return cursor


def assert_no_server_error(html: str, url: str = "") -> None:
    """Assert that HTML response does not contain Flask/Python error pages."""
    for marker in ("Internal Server Error", "Traceback (most recent call last)", "raise ", "AttributeError"):
        if marker in html:
            raise AssertionError(
                f"Server error page detected at {url!r}. Marker: {marker!r}. "
                f"HTML (first 400): {html[:400]}"
            )
