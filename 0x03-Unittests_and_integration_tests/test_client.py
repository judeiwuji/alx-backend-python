#!/usr/bin/env python3
import unittest
from unittest.mock import patch, MagicMock, Mock, PropertyMock
from parameterized import parameterized
from client import (GithubOrgClient)
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """Test Github org client"""

    @parameterized.expand([
        "google",
        "abc"
    ])
    @patch("client.get_json")
    def test_org(self, input: str, mock_get_json: Mock):
        """Test github org client"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        client = GithubOrgClient(input)
        client.org()
        mock_get_json.assert_called_once_with(client.ORG_URL.format(org=input))

    def test_public_repos_url(self):
        """Test public repos url"""
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_public_repos_url:
            payload = "google"
            mock_public_repos_url.return_value = payload
            mock = GithubOrgClient("google")
            self.assertEqual(mock._public_repos_url, payload)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: Mock):
        """Test public repos"""
        mock_get_json.return_value = [{'name': 'google'}]

        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_public_repos_url:
            payload = {'name': 'google'}
            mock_public_repos_url.return_value = payload
            mock = GithubOrgClient("google")
            data = mock.public_repos()
            self.assertEqual(list(payload.values()), data)
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"repo": {"license": {"key": "my_license"}},
         "license_key": "my_license"}, True),
        ({"repo": {"license": {"key": "other_license"}},
         "license_key": "my_license"}, False)
    ])
    def test_has_license(self, input: Dict[str, Dict[str, str]], expected: bool):
        """Test has license method"""
        self.assertEqual(GithubOrgClient.has_license(**input), expected)
