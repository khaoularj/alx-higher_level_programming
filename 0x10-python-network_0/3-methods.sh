#!/bin/bash
#this script takes in a URL and displays all HTTP methods the server will accept.

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

allow_meth=$(curl -sI -X OPTIONS "$url" | grep -i Allow | awk '{print $2}')

echo "$allow_meth"
