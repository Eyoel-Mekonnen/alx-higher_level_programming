#!/bin/bash
# which method sever will accepts
curl -s "$1" | grep 'Allow' 
