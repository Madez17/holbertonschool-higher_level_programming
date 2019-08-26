#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id"""

import urllib.parse
import urllib.request
from sys import argv

url = argv[1]
params = {"value": argv[2]}
query_string = urllib.parse.urlencode(params).encode("ascii")

if __name__ == "__main__":
    with urllib.request.urlopen(url, query_string) as response:
        response_text = response.read().decode('utf-8')
        print(response_text)
