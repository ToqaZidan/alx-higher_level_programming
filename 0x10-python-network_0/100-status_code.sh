#!/bin/bash
# Get only the status code of the response
curl -LI "$1" -o /dev/null -w '%{http_code}\n' -s
