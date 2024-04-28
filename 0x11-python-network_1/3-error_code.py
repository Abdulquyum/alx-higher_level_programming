#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
manages urllib.error.HTTPError exceptions
"""

import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            print(data)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
