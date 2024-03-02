#!/usr/bin/python3
"""Script Sends a post request to a given url with a given mail"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}

    req = requests.post(url, data=val)
    print(req.text)
