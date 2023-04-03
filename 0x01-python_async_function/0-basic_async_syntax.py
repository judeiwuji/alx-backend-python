#!/usr/bin/env python3
"""Module: Basic async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait random

    Args:
        max_delay(int)
    """
    result = await asyncio.sleep(max_delay, random.random() * max_delay)
    return result
