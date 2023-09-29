#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status.
"""

import requests


if __name__ == "__main__":
    html = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")5
    print("\t- type: {}".format(type(html.text)))
    print("\t- content: {}".format(html.text))
