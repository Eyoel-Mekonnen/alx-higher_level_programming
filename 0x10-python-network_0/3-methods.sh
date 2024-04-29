#!/bin/bash
# which method sever will accepts
curl -sI "$1" | grep 'Allow' | cut -d ' ' -f 2-
