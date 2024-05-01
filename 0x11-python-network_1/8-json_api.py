#!/usr/bin/python3
"""Script that takes parameter and checks json."""
import requests
import sys

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        variable = sys.argv[1]
    else:
        varialbe = ""
    q = {'q': variable}
    response = requests.post("http://0.0.0.0:5000/search_user", data=q)
    json = response.json()
    if json == {}:
        print("No result")
    try:
        for key, value in json.items():
            if key == "id":
                print("[{}] ".format(json[key], end=""))
            if key == "name":
                print("{}".format(json[key]))
    except ValueError:
        print("Not a valid JSON")
