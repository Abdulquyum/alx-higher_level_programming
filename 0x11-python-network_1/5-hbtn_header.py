#!/usr/bin/python3
"""
sends a request to the URL and displays,
the value of the variable X-Request-Id in the response header
"""

import requests


data = requests.get('https://alx-intranet.hbtn.io/status')
body = data.headers['X-Request-Id']
print(body)
