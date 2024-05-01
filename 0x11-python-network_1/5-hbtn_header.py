#!/usr/bin/python3
"""Take URL send request and display variable X-Request-ID"""
import requests
import sys
if __name__ == '__main__':
    request = sys.argv[1]
    response = requests.get(request)
    print(response.headers.get("X-Request-ID"))
