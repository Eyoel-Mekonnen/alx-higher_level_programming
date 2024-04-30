#!/usr/bin/python3

"""
script that fetches website.

fetches https://alx-intranet.hbtn.io/status.
"""


if __name__ == '__main__':
    from urllib import request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        data = r.read()
        print("Body response:")
        print("\t- type : {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode("utf-8")))