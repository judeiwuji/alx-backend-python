#!/usr/bin/env python3
"""Module: complex types"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Computes sum of floats

    Args:
        input_list(list[float])
    """
    sum: float = 0.0
    for n in input_list:
        sum += n
    return sum
