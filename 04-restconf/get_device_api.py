#!/usr/bin/env python
import requests
import json

PREFIX = "http://"
HOST = 'ios-xe-mgmt.cisco.com'
PORT = 9443
USER = 'root'
PASS = 'D_Vay!_10&'
URI = "/restconf/api"

url = PREFIX + HOST + ":" + str(PORT) + URI
querystring = {}

headers = {}
headers["Authorization"] = "Basic cm9vdDpEX1ZheSFfMTAm"
headers["Accept"] = "application/vnd.yang.api+json"

response = requests.request("GET", url,
                            headers=headers,
                            params=querystring)
print(json.dumps(response.json(), indent=3))
