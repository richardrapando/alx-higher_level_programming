#!/bin/bash
# Bash script sending JSON POST request to a URL passed as first argument
curl -sL -H "content-type:application/json" -d @"$2" -X POST "$1"

