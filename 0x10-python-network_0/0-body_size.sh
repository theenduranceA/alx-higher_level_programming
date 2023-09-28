#!/bin/bash
# Script that takes in a URL, sends a request to that URL,
# And displays the size of the body of the response.

curl -s "$1" | wc -c
