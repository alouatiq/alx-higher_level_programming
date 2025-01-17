#!/usr/bin/python3
"""
Displays the value of X-Request-Id header from a URL response using urllib
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get("X-Request-Id"))
