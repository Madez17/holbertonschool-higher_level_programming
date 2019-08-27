#!/usr/bin/python3
# Script sends a POST request to the passed URL with the email as a parameter

import urllib.parse
import urllib.request
from sys import argv


if __name__ == "__main__":

    url = argv[1]
    params = {"email": argv[2]}
    query_string = urllib.parse.urlencode(params).encode('ascii')
    with urllib.request.urlopen(url, query_string) as response:
        response_text = response.read().decode('utf-8')
        print(response_text)
