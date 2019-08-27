#!/usr/bin/python3
# script sends a post requests

import requests
from sys import argv


if __name__ == "__main__":

    url = argv[1]
    params = {'email': argv[2]}
    response = requests.post(url, params)
    response = response.text
    print(response)
