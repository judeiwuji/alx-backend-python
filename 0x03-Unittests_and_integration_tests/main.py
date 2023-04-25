#!/usr/bin/env python3
from client import (GithubOrgClient)
utils = __import__("utils")
print(utils.access_nested_map({"a": 1}, path=("a",)))
print(utils.access_nested_map({"a": {"b": 2}}, path=("a",)))
print(utils.access_nested_map({"a": {"b": 2}}, path=("a", "b")))
# client = GithubOrgClient("google")
# print(GithubOrgClient.has_license(
#     repo={"license": {"key": "my_license"}}, license_key="my_license"))
