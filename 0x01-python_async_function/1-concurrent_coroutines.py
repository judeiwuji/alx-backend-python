#!/usr/bin/env python3
"""Module: Multiple Coroutines"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """Wait N

    Args:
        n(int)
        max_delay:(int)
    """
    tasks = (wait_random(max_delay) for _ in range(n))
    results = await asyncio.gather(*tasks)
    return results
