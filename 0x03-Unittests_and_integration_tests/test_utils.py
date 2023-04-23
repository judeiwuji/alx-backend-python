#!/usr/bin/env python3
"""Module: Test utils"""
import unittest
from parameterized import parameterized
from typing import Dict, Union, Tuple
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
    def test_access_nested_map(self, name: str,
                               input: Dict[str, Union[Dict, Tuple]],
                               expected: Union[int, Dict]):
        """Test cases for test_access_nested_map"""
        self.assertEqual(utils.access_nested_map(**input), expected)

    @parameterized.expand([
        ("nested_map", {'nested_map': {}, 'path': ("a",), }, KeyError),
        ("nested_map", {'nested_map': {"a": 1},
         'path': ("a", "b"), }, KeyError)
    ])
    def test_access_nested_map_exception(self, name: str,
                                         input: Dict[str, Union[Dict, Tuple]],
                                         expected: Union[int, Dict]):
        """Test access nested map exception"""
        with self.assertRaises(expected):
            utils.access_nested_map(**input)
