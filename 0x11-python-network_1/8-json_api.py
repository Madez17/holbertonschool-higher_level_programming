#!/usr/bin/python3
# Python script that takes in a letter and sends a POST request

import requests
from sys import argv


if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'
    q = ""

    if len(argv) > 1:
        q = argv[1]

    params = {'q': q}
    response = requests.post(url, params)

    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response['id'],
                                   json_response['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
