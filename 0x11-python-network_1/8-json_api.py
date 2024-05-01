#!/usr/bin/python3
"""Script that takes parameter and checks json."""
import requests
import sys

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        q = sys.argv[1]
    else:
        q = ""
    data = {'q': q}
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)
    json_ = response.json()
    if json_ == {}:
        print("No result")
    try:
        for key, value in json_.items():
            if key == "id":
                print("[{}] ".format(json_[key], end=""))
            if key == "name":
                print(value)
    except ValueError:
        print("Not a valid JSON")
