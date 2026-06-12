"""Public SDK surface: :class:`OfinClient`.

Lazily constructs per-region facades from a resolved :class:`ofin.config.Config`
so importing the SDK never forces all three regions to be configured.

Example::

    from ofin.config import Config
    from ofin.sdk import OfinClient

    cfg = Config.resolve()
    client = OfinClient(cfg)
    result = client.us.auth_token()
    print(result.ok, result.status)
"""
from __future__ import annotations

from typing import Optional

from ..errors import ConfigError
from .au import AUClient
from .base import Result
from .eu import EUClient
from .us import USClient

__all__ = ["OfinClient", "USClient", "AUClient", "EUClient", "Result"]


class OfinClient:
    """Facade exposing the three Open Finance regions: ``.us``, ``.au``, ``.eu``."""

    def __init__(self, config, timeout: Optional[int] = None) -> None:
        self._config = config
        self._timeout = timeout
        self._us: Optional[USClient] = None
        self._au: Optional[AUClient] = None
        self._eu: Optional[EUClient] = None

    @property
    def us(self) -> USClient:
        if self._us is None:
            c = self._config.us
            if not c.configured:
                raise ConfigError(c.missing_message())
            self._us = USClient(c.partner_id, c.partner_secret, c.app_key,
                                base_url=c.base_url, timeout=self._timeout)
        return self._us

    @property
    def au(self) -> AUClient:
        if self._au is None:
            c = self._config.au
            if not c.configured:
                raise ConfigError(c.missing_message())
            self._au = AUClient(c.partner_id, c.partner_secret, c.app_key,
                                base_url=c.base_url, timeout=self._timeout)
        return self._au

    @property
    def eu(self) -> EUClient:
        if self._eu is None:
            c = self._config.eu
            if not c.configured:
                raise ConfigError(c.missing_message())
            self._eu = EUClient(c.client_id, c.private_key_path, c.public_cert_path,
                                auth_base_url=c.auth_base_url, api_base_url=c.api_base_url,
                                application_id=c.application_id, timeout=self._timeout)
        return self._eu

    def region(self, name: str):
        """Return the facade for ``name`` ('us' | 'au' | 'eu')."""
        name = (name or "").lower()
        if name == "us":
            return self.us
        if name == "au":
            return self.au
        if name == "eu":
            return self.eu
        raise ConfigError(f"Unknown region '{name}'. Use one of: us, au, eu.")
