#!/usr/bin/python3
"""Displays 10 commits from most recent to oldest."""
import sys
import requests


if __name__ == '__main__':
    repository = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repository)
    response = requests.get(url)
    if response.status_code == 200:
        json_ = response.json()
        count = 0
        for commits in json_:
            print("{}: {}".format(commits['sha'], commits['commit']['author']['name']))
            count = count + 1
            if count >= 10:
                break
