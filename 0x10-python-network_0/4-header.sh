#!/bin/bash
#sends a GET request for a header variable
curl -sH "X-School-User-Id: 98" "$1"
