#!/usr/bin/python3
"""
Python script that takes URL,send reuest display body.
Handles HTTP Error
"""
if __name__ == '__main__':
    import urllib.request
    import urllib.error
    import sys
    req = sys.argv[1]
    try:
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            print(data)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
