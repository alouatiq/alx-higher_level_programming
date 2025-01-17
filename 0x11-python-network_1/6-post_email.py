#!/usr/bin/python3
"""
Sends a POST request to a URL with an email parameter using requests
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    response = requests.post(url, data=email)
    print(response.text)
