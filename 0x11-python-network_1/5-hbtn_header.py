#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL ,
nd displays the value of the variable X-Request-Id in the response header.
"""

import sys
import requests


if __name__ == "_main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
