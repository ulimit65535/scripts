#!/usr/bin/env python
# encoding: utf-8

import sys
from urllib.parse import urlparse

import requests

IP="10.2.2.202"

if __name__ == '__main__':
    filename = sys.argv[1]
    f = open(filename)
    for line in f.readlines():
        line = line.strip()
        urlp =urlparse(line)
        try:
            response = requests.get("http://" + IP + urlp.path, headers={"Host": urlp.netloc})
        except:
            pass

        if response.status_code == 200:
            print(line)

    f.close()
