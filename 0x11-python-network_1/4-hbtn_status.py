#!/usr/bin/python3
"""this fecthes https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    req = requests.get("https://alx-intranet.hbtn.io/status")
    print("body response:")
