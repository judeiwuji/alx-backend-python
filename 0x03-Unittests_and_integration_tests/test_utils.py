#!/usr/bin/env python3
"""Module: Test utils"""
import unittest
from unittest import mock
from parameterized import parameterized
from typing import Dict, Union, Tuple
utils = __import__("utils")
memoize = utils.memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for test_access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Dict,
                               path: Tuple,
                               expected: Union[int, Dict]):
        """Test cases for test_access_nested_map"""
        self.assertEqual(utils.access_nested_map(
            nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Dict,
                                         path: Tuple):
        """Test access nested map exception"""
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map=nested_map, path=path)


class TestGetJson(unittest.TestCase):
    """Test Get Json"""

    @parameterized.expand([("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})])
    @mock.patch("utils.requests")
    def test_get_json(self, test_url: str, test_payload: Dict[str, bool],
                      mock_requests: mock.Mock):
        """Test Get JSON"""

        mock_response = mock.MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = test_payload
        mock_requests.get.return_value = mock_response
        self.assertEqual(utils.get_json(
            test_url), mock_response.json())
        mock_requests.get.assert_called_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test Memoize"""

    def test_memoize(self):
        """Test memoize"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with mock.patch.object(TestClass, 'a_method',
                               return_value=42) as mock_method:
            test = TestClass()
            test.a_property
            test.a_property
        mock_method.assert_called_once()
