#!/usr/bin/bash
# Get the byte size of order
curl -s "$1" | wc -c
