#!/usr/bin/env python
import requests
import json

PREFIX = "http://"
HOST = 'ios-xe-mgmt.cisco.com'
PORT = 9443
USER = 'root'
PASS = 'D_Vay!_10&'
URI = "/restconf/api/running/interfaces/interface/GigabitEthernet3/description"

url = PREFIX + HOST + ":" + str(PORT) + URI
querystring = {}

headers = {}
headers["Authorization"] = "Basic cm9vdDpEX1ZheSFfMTAm"
headers["Accept"] = "application/vnd.yang.data+json"

response = requests.request("DELETE", url,
                            headers=headers,
                            params=querystring)

if response.status_code == 204:
    print("Success!")
else:
    print("Failed!")
    print(response.status_code)
    print(response.text)
