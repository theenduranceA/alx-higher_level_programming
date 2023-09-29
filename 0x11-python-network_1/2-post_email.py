#!/usr/bin/python3
"""
Script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8).
"""

import sys
import urllib.request


if __name__ == "__main__":
    info = urllib.parse.urlencode({'email': sys.argv[2]}).encode()
    req = urllib.request.Request(sys.argv[1], info)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
