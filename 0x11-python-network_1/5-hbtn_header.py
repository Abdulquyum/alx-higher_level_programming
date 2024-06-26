#!/usr/bin/python3
""" sends a request to URL and displays,
the value of the variable X-Request-Id in the response header
Using responses library in python
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    data = requests.get(url)
    body = data.headers['X-Request-Id']
    print(body)
