#!/bin/bash
# Request to a URL and display the size of the body of the response
curl -sI "$1" | grep -iE '^Content-Length:' | awk '{print $2}'
