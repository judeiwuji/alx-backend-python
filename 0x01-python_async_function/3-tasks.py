#!/usr/bin/env python3
"""Module: Measure runtime"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Task Wait Random

    Args:
        max_delay(int)
    """
    return asyncio.tasks.create_task(wait_random(max_delay))
