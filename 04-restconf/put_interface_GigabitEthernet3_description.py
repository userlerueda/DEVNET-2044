#!/usr/bin/env python
import requests
import json
from collections import OrderedDict
import ciscoasnfv

PREFIX = "http://"
HOST = 'ios-xe-mgmt.cisco.com'
PORT = 9443
USER = 'root'
PASS = 'D_Vay!_10&'
URI = "/restconf/api/running/interfaces/interface/GigabitEthernet3"
DESCRIPTION = "lurueda was here!"

url = PREFIX + HOST + ":" + str(PORT) + URI
querystring = {}

headers = {}
headers["Authorization"] = "Basic cm9vdDpEX1ZheSFfMTAm"
headers["Accept"] = "application/vnd.yang.data+json"
headers["content-type"] = "application/vnd.yang.data+json"

payload = OrderedDict({})
payload["ietf-interfaces:interface"] = OrderedDict({})
payload["ietf-interfaces:interface"]["name"] = "GigabitEthernet3"
payload["ietf-interfaces:interface"]["type"] = "iana-if-type:ethernetCsmacd"
payload["ietf-interfaces:interface"]["description"] = DESCRIPTION
payload["ietf-interfaces:interface"]["enabled"] = True
payload["ietf-interfaces:interface"]["ietf-ip:ipv4"] = {}
payload["ietf-interfaces:interface"]["ietf-ip:ipv6"] = {}
print("PAYLOAD: {}\n".format(json.dumps(payload, indent=3)))

response = requests.request("PUT", url,
                            headers=headers,
                            params=querystring,
                            data=json.dumps(payload))
if response.status_code == 204:
    print("Success!")
else:
    print(response.text)
