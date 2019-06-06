#!/usr/bin/python3
import json


def load_from_json_file(filename):
    with open(filename, mode='r', encoding='UTF8') as MyFile:
        return json.loads(MyFile.read())
