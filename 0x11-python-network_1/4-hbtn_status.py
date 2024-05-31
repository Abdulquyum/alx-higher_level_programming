#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status
Using reequest pyhton library
"""

import requests


data = requests.get('https://alx-intranet.hbtn.io/status')
body = data.content.decode('utf-8')
print("Body response:")
print(f"\t- type: {type(body)}")
print(f"\t- content: {str(body)}")
