#!/usr/bin/env python3
"""Module: Multiple tasks"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Task Wait N

    Args:
        n(int)
        max_delay:(int)
    """
    results = await asyncio.gather(*(task_wait_random(max_delay)
                                     for _ in range(n)))
    return results
