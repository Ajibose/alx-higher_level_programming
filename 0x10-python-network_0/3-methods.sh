#!/bin/bash
# displays all HTTP methods the server will accept.
curl -s -I -X OPTIONS "$URL" | grep -i "allow" | tr -d '\r' | awk '{print "Allowed HTTP methods:", $2}'
