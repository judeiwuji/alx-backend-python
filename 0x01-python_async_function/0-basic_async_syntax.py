#!/usr/bin/env python3
"""Module: Basic async"""
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait random

    Args:
        max_delay(int)
    """
    return random.uniform(0, max_delay)
