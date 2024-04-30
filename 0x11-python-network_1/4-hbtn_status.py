#!/usr/bin/python3
""" Use request to request"""
import requests

if __name__ == '__main__':
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(response.txt)))
    print("\t- content: {}".format(response.txt))
