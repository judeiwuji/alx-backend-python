#!/usr/bin/env python3
"""Module: Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiplier wrapper
    """
    return lambda n: n * multiplier
