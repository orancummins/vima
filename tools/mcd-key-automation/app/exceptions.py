"""Custom exceptions."""
from __future__ import annotations


class McdAutomationError(Exception):
    """Base exception."""


class ConfigError(McdAutomationError):
    pass


class LoginTimeoutError(McdAutomationError):
    pass


class WorkflowError(McdAutomationError):
    pass


class DownloadError(McdAutomationError):
    pass


class PackagingError(McdAutomationError):
    pass
