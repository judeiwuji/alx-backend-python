#!/usr/bin/env python3
"""Module: Basic async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait random

    Args:
        max_delay(int)
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
