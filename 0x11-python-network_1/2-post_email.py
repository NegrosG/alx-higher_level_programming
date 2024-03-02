#!/usr/bin/python3
""" Module sends post reqest to a url with given email"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(val).encode("ascii")
    try:
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as resp:
            print(resp.read().decode("utf-8"))
    except HTTPError as e:
        print(f"HTTP error occured: {e.code} {e.reason}")
    except URLError as e:
        print(f"URL error occured: {e.reason}")
