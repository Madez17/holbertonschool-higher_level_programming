#!/usr/bin/python3
# script that takes in a string and sends a search request to the Star Wars API

import requests
from sys import argv


if __name__ == "__main__":

    search = argv[1]
    API = 'https://swapi.co/api/people/'
    request = requests.get(API, params={'search': search})
    req_file = request.json()
    counter = req_file['count']
    print("Number of results: {}".format(counter))
    for each_name in req_file['results']:
        print(each_name['name'])
