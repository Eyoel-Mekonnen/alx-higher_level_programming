#!/usr/bin/python3
""" passes an email as a parameter to the server."""
import sys

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    url_request = sys.argv[1]
    email_var = sys.argv[2]
    email_dict = urllib.parse.urlencode({'email': email_var}).encode('utf-8')
    request = urllib.request.Request(url_request, data=email_dict)

    with urllib.request.urlopen(request) as response:
        rep = response.read().decode('utf-8')
        print(rep)
