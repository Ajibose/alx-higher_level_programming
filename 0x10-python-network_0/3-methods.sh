#!/bin/bash
# displays all HTTP methods the server will accept.
curl -si $1 | grep "allow" | cut -d " " -f 2-
