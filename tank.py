# !/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
from time import sleep
import http.client
import urllib.parse

channel_id = XXXXXX
write_key = 'write_apikey'

data = xx # read from sensor

def update_tank():
    data = xx
    params = urllib.parse.urlencode({'field2': data, 'key': write_key})
    headers = {"Content-typZZe": "application/x-www-form-urlencoded",
            "Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print('connection failed')


