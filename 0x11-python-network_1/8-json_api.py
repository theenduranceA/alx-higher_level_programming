#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests

if __name__ == "__main__":

    if len(sys.argv) == 1:
        data = {"q": ""}
    else:
        data = {"q": sys.argv[1]}

    response = requests.post("http://0.0.0.0:5000/search_user", data=data)
    if response.headers.get("content-type") != "application/json":
        print("Not a valid JSON")
    elif response.json() == {}:
        print("No result")
    else:
        print("[{}] {}".format(response.json()["id"], response.json()["name"]))
