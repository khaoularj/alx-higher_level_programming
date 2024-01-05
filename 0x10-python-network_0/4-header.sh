#!/bin/bash
#this script takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1
header_val=98

response=$(curl -s -H "X-School-User-Id: $header_val" "$url")

echo "$response"
