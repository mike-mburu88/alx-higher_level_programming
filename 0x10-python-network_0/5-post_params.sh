#!/usr/bin/bash
#script for a POST request with a given URL
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
