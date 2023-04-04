#!/usr/bin/env python3
"""Module: Async Comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async Comprehension
    """
    rands = [i async for i in async_generator()]
    return rands
