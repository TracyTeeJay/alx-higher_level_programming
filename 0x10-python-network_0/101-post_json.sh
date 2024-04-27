#!/bin/bash
# Script to send JSON POST request to URL with a given JSON file
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
