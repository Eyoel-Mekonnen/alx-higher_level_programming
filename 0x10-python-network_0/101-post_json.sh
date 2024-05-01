#!/bin/bash
# Send JSON POST request to a URL
curl -X POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"

