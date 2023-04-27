#!/bin/bash
#bash script to send a request to a URL as an argument
#then displays the status code only
curl -s - o /dev/null -w "%{http_code}" "$1"
