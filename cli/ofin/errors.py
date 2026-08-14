"""Typed errors raised across the ofin SDK + CLI.

Keeping these in one tiny module lets the CLI map exceptions to clean exit
codes and messages without leaking tracebacks to end users (unless ``-v`` is
passed).
"""
from __future__ import annotations


class OfinError(Exception):
    """Base class for all expected ofin failures."""

    #: Process exit code the CLI should return for this error.
    exit_code: int = 1


class ConfigError(OfinError):
    """Raised when credentials/config for a region are missing or invalid."""

    exit_code = 2


class ApiError(OfinError):
    """Raised when an API call returns a non-2xx response.

    Carries the HTTP status and the parsed response body so callers (and the
    CLI) can render structured details.
    """

    exit_code = 3

    def __init__(self, message: str, *, status: int | None = None, body=None) -> None:
        super().__init__(message)
        self.status = status
        self.body = body


class UsageError(OfinError):
    """Raised for bad command-line usage that argparse cannot catch itself."""

    exit_code = 64  # EX_USAGE
