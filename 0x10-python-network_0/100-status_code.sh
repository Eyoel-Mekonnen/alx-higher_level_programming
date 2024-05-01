#!/bin/bash
# send GET request and recive the status code
curl -o /dev/null -s -w '%{http_code}' "$1"
