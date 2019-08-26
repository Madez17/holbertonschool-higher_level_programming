#!/usr/bin/python3
#script that fetches URL
import urllib.request

url = 'https://intranet.hbtn.io/status'

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        data = response.read()
        print("Body response:")
        print("\t - type: {}".format(type(data)))
        print("\t - content: {}".format(data))
        print("\t - utf8 content: {}".format(data.decode('utf-8')))
