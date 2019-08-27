#!/usr/bin/python3
# script that takes in a string and sends a search request to the github API

import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    API = 'https://api.github.com/user'

    request = requests.get(API, auth=HTTPBasicAuth(username, password))
    response = request.json()
    print("{}".format(response.get('id')))
