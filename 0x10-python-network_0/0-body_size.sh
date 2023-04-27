#!/usr/bin/bash
#gets the byte size for a HTTP response header for a URL
curl -s "$1" | wc -c
