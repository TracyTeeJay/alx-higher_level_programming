#!/bin/bash
# Script to send GET request to URL and display response status code
curl -s -o /dev/null -w "%{http_code}" "$1"
