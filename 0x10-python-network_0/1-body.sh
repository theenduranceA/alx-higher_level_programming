#!/bin/bash
# Script that takes in a URL, sends a GET request to the URL
# And displays the body of the response.

curl -s -L "$1"
