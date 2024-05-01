#!/bin/bash
# Send JSON POST request to a URL
FILE=$2
URL=$1
curl -X POST -H "Content-Type: application/json" -d @"$FILE" "$URL"

