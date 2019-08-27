#!/usr/bin/python3
# script sends a request to the URL and displays X-Request-Id

import requests
from sys import argv


if __name__ == "__main__":

    url = argv[1]
    data = requests.get(url)
    data = data.headers.get("X-Request-Id")
    print(data)
