#!/bin/bash
#sends a JSON post for a URL with a specified JSON file
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
