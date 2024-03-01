#!/bin/bash
#Script sends a DELETE request passed as first arg and display body of response
curl -sX DELETE "$1"
