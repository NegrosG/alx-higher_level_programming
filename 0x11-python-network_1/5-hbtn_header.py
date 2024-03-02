#!/usr/bin/python3
"""Displays X-request-id header of a request given URL"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    print(req.headers.get("X-Requests-Id"))
