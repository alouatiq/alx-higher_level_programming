#!/usr/bin/python3
"""
Displays the X-Request-Id header from a URL response using requests
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
