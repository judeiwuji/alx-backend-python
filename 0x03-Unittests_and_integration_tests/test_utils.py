#!/usr/bin/env python3
"""Module: Test utils"""
import unittest
from parameterized import parameterized
utils = __import__("utils")


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for test_access_nested_map"""

    @parameterized.expand([
        ("nested_map", {'nested_map': {"a": 1}, 'path': ("a",), }, 1),
        ("nested_map", {'nested_map': {
         "a": {"b": 2}}, 'path': ("a",), }, {'b': 2}),
        ("nested_map", {'nested_map': {
         "a": {"b": 2}}, 'path': ("a", "b"), }, 2)
    ])
    def test_access_nested_map(self, name, input, expected):
        """Test cases for test_access_nested_map"""
        self.assertEqual(utils.access_nested_map(**input), expected)
