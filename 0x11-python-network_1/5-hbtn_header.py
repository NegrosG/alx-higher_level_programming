#!/usr/bin/python3
"""Displays X-request-id header of a request given URL"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        r = requests.get(url)
        x_request_id = r.headers.get("X-Request-Id")
        if x_request_id is None:
            print("X-Request-Id header not found.")
        else:
            print(x_request_id)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
