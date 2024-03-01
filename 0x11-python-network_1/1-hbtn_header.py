#!/usr/bin/python3
"""Displays X-Request-Id header variable of a request to a URL"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as resp:
        print(dict(resp.headers).get("X-Request-Id"))
