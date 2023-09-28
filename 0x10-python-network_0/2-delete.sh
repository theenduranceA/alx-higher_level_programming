#!/bin/bash
# Script that sends a DELETE request to the URL passed as the first argument,
# And displays the body of the response.

curl -s -X DELETE "$1"
