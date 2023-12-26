#!/bin/bash
# Bash script that allows methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-