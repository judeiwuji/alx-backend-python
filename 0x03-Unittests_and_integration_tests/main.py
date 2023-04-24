#!/usr/bin/env python3
utils = __import__("utils")
# print(utils.access_nested_map({"a": 1}, path=("a",)))
# print(utils.access_nested_map({"a": {"b": 2}}, path=("a",)))
# print(utils.access_nested_map({"a": {"b": 2}}, path=("a", "b")))

print(utils.get_json("http://example.com"))
print(utils.get_json("http://holberton.io"))
