#!/usr/bin/python3
"""
Script that list 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails”. Using the GitHub API.
"""

import sys
import requests


if __name__ == "__main__":
    response = requests.get(
            "https://api.github.com/repos/{}/{}/commits".
            format(sys.argv[2], sys.argv[1]))
    for _ in range(0, min(len(response.json()), 10)):
        print("{}: {}".format(
                response.json()[_]['sha'],
                response.json()[_]['commit']['author']['name']))
