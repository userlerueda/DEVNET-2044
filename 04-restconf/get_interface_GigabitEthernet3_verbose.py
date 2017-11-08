#!/usr/bin/env python
import requests
import json

PREFIX = "http://"
HOST = 'ios-xe-mgmt.cisco.com'
PORT = 9443
USER = 'root'
PASS = 'D_Vay!_10&'
URI = "/restconf/api/running/interfaces/interface/GigabitEthernet3"

url = PREFIX + HOST + ":" + str(PORT) + URI
querystring = {}
querystring["verbose"] = ""

headers = {}
headers["Authorization"] = "Basic cm9vdDpEX1ZheSFfMTAm"
headers["Accept"] = "application/vnd.yang.data+json"

response = requests.request("GET", url,
                            headers=headers,
                            params=querystring)
print(json.dumps(response.json(), indent=3))
