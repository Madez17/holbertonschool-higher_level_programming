#!/usr/bin/python3
# script sends a request to the URL and displays response (decoded in utf-8).

import urllib.parse
import urllib.request
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":

    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            response_text = response.read().decode('utf-8')
            print(response_text)

    except HTTPError as e:
        print('Error code:', e.code)
