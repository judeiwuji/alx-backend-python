#!/usr/bin/env python3
import unittest
from unittest.mock import patch, MagicMock, Mock, PropertyMock
from parameterized import parameterized
from client import (GithubOrgClient)


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
