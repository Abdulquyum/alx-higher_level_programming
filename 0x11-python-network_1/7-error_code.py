#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
manages urllib.error.HTTPError exceptions
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        data = requests.get(url)
        data.raise_for_status()
        cont = data.content
        print(cont)
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {e.data.status_code}")
