#!/usr/bin/env python3
"""Module: """
import asyncio
import random
from typing import Iterator


async def async_generator() -> Iterator[float]:
    """Async Generator: generates numbers
    """
    for i in range(10):
        await asyncio.sleep(1)
        rand = random.uniform(0, 10)
        yield rand
