#!/usr/bin/env bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
url="$1"
response_body=$(mktemp)
curl -s -o "$response_body" "$url" | wc -c
