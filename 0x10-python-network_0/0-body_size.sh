#!/bin/bash
# this script takes in a url and send request to the url to display size of the body
#of the response

curl -s "$1" | wc -c
