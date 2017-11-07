#!/usr/bin/env python

from ncclient import manager
import sys
import xml.dom.minidom

# the variables below assume the user is leveraging the
# dCloud network programmability lab.
#
# use the IP address or hostname of your CSR1000V device
HOST = 'ios-xe-mgmt.cisco.com'
PORT = 10000
USER = 'root'
PASS = 'D_Vay!_10&'


# create a main() method
def main():
    """
    Main method that retrieves information via NETCONF
    """
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False, look_for_keys=False) as m:

        print("NETCONF CAPABILITIES:\n")
        for capability in m.server_capabilities:
            print(capability)

        # XML filter to issue with the get operation
        hostname_filter = '''
                          <filter>
                              <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                                  <hostname></hostname>
                                  <version></version>
                              </native>
                          </filter>
                          '''

        result = m.get_config('running', hostname_filter)
        xml_doc = xml.dom.minidom.parseString(result.xml)
        print("XML RESPONSE:\n{}".format(xml_doc.toprettyxml()))
        hostname = xml_doc.getElementsByTagName("hostname")
        version = xml_doc.getElementsByTagName("version")

        print("HOSTNAME: {}".format(hostname[0].firstChild.nodeValue))
        print("VERSION: {}".format(version[0].firstChild.nodeValue))


if __name__ == '__main__':
    sys.exit(main())
