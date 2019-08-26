#!/usr/bin/python3
# script that takes in a URL, sends a request to the URL display X-Request-Id

import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        data = response.info()
        print(data["X-Request-Id"])
