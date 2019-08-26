#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id"""

import urllib.request
from sys import argv

url = argv[1]

if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        data = response.info()
        print(data['X-Request-Id'])
