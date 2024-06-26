#!/usr/bin/python3
"""Take URL and parameter to URL and show response"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    parameter = sys.argv[2]
    email = {'email': parameter}
    response = requests.post(url, data=email)
    print(response.text)
