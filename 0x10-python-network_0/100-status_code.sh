#!/bin/bash
# Get only the status code of the response
curl -sLI -o /dev/null -w '%{http_code}\n' "$1"
