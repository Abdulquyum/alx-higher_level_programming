#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status
using urllib in python library
"""

import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        utf_content = body.decode('utf-8')
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {str(body)}")
    print(f"\t- utf8 content: {utf_content}")
