#!/usr/bin/env python
# encoding: utf-8

import requests
import sys
from urllib.parse import urlparse

#IP="10.2.2.202"
IP="10.2.2.61"

if __name__ == '__main__':
    filename = sys.argv[1]
    f = open(filename)
    for line in f.readlines():
        line = line.strip()
        urlp =urlparse(line)
        try:
            response = requests.get("http://" + IP + urlp.path, headers={ "Host": urlp.netloc }, allow_redirects=False)
        except:
            pass

        if response.status_code == 200:
            print(line)

    f.close()
