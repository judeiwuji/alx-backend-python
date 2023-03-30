#!/usr/bin/env python3
"""Module: Complex types - string and int/float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a tuple

    Args:
        k(str)
        v(int | float)
    """
    return tuple([k, float(v)])
