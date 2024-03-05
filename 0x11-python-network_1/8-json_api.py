#!/usr/bin/python3
"""Sends aPOSt requesr to http://0.0.0.0:5000/search_user with a letter
The letter is sent as a value of the variable 'q'
If no letter is provided, sencs 'q=""'
"""
import requests
import sys


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
