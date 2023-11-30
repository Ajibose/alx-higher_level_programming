#!/bin/bash
# send a GET request
curl -Xs GET -o /dev/null -w "%{http_code}" | xargs -I {} sh -c if [ "{}" -eq 200 ]; then curl -s "$1"; fi' 
