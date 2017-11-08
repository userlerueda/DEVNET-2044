#!/usr/bin/env python

from ncclient import manager
import sys
import xml.dom.minidom
try:
    from os import scandir, walk
except ImportError:
    from scandir import scandir, walk

# the variables below assume the user is leveraging the
# dCloud network programmability lab.
#
# use the IP address or hostname of your CSR1000V device
HOST = 'ios-xe-mgmt.cisco.com'
PORT = 10000
USER = 'root'
PASS = 'D_Vay!_10&'
CAPABILITY = "ietf-interfaces"
YANG_PATH = "~/Documents/github.com/YangModels/yang/"
VENDOR = "cisco"
OS = "xe"
OS_VERSION = "1651"


# create a main() method
def main():
    """
    Main method that retrieves information via NETCONF
    """
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False, look_for_keys=False) as m:

        for capability in m.server_capabilities:
            if CAPABILITY in capability:
                print(capability)


if __name__ == '__main__':
    sys.exit(main())
