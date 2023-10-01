#!/usr/bin/python3
"""
Script that takes my GitHub credentials (username and password)
and uses the GitHub API to display my id.
"""

import sys
import requests


if __name__ == "__main__":
    response = requests.get(
            "https://api.github.com/user",
            auth=(sys.argv[1], sys.argv[2])).json()
    if "id" not in response:
        print("None")
    else:
        print(response["id"])
