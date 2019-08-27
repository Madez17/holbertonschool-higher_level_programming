#!/usr/bin/python3
# script that fetches URL

import requests

url = 'https://intranet.hbtn.io/status'

if __name__ == "__main__":
    data = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(data.text)))
    print("\t- content: {}".format(data.text))
