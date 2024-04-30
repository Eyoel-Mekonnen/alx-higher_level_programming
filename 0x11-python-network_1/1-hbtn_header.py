#!/usr/bin/python3
"""Display the value of X-Request-ID."""
import sys

if __name__ == '__main__':
    import urllib.request
    my_request = sys.argv[1]
    with urllib.request.urlopen(my_request) as r:
        id_request = r.getheader('X-Request-ID')
        print(id_request)
