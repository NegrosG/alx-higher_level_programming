#!/usr/bin/python3
"""Uses the Github API to display a GITHub ID based on given credentials.
-Uses Basic authentication to access the ID
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
