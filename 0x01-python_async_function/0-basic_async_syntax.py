#!/usr/bin/env python3
"""Module: Basic async"""
import asyncio
import random


async def wait_random(max_delay=10):
    """Wait random

    Args:
        max_delay(int)
    """
    await asyncio.sleep(max_delay)
    return random.uniform(0, max_delay)
