"""Wait helpers."""
from __future__ import annotations

import asyncio
from typing import Awaitable, Callable

from loguru import logger

from app.exceptions import LoginTimeoutError


async def wait_until(
    predicate: Callable[[], Awaitable[bool]],
    *,
    timeout_s: float = 600.0,
    poll_interval_s: float = 1.5,
    description: str = "condition",
) -> None:
    """Poll an async predicate until True or raise LoginTimeoutError."""
    deadline = asyncio.get_event_loop().time() + timeout_s
    last_log = 0.0
    while True:
        try:
            if await predicate():
                logger.info("Reached {}", description)
                return
        except Exception as e:
            logger.debug("Predicate {} raised: {}", description, e)
        now = asyncio.get_event_loop().time()
        if now > deadline:
            raise LoginTimeoutError(f"Timed out waiting for {description}")
        if now - last_log > 15:
            logger.info("Still waiting for {}...", description)
            last_log = now
        await asyncio.sleep(poll_interval_s)
