#!/usr/bin/env python3
"""Module: complex types mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """Computes sum of floats

    Args:
        input_list(list[float])
    """
    sum: float = 0.0
    for n in mxd_lst:
        sum += n
    return sum
