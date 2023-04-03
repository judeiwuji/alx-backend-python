#!/usr/bin/env python3
"""Module: Measure runtime"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure Time

    Args:
        n(int)
        max_delay(int)
    """
    total_time = 0
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start
    return total_time / n
