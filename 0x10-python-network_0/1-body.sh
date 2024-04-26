#!/bin/bash
#  takes in a URL, sends a GET request to the URL, and displays the body of the response
url="$1"
response_body=$(mktemp)
curl -s -o "$response_body" -w "%{http_code}" "$url" > /dev/null
