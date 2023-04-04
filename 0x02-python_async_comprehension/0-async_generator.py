#!/usr/bin/env python3
"""Module: """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Async Generator: generates numbers
    """
    for i in range(10):
        rand = await asyncio.sleep(1, random.uniform(0, 10))
        yield rand
