#!/usr/bin/python3
"""Script take Github credential and use GITHUB API."""
import sys
import requests


if __name__ == '__main__':
    username = sys.argv[1]
    token = sys.argv[2]
    response = requests.get("https://api.github.com/user", auth=(username, token))
    if (response.status_code == 200):
        json_ = response.json()
        for key, value in json_.items():
            if key == 'id':
                print(value)
    else:
        print("None")
