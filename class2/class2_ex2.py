#!/usr/bin/env python

import telnetlib
import time

IP_ADDRESS = '50.76.53.27'
TELNET_PORT = 23
TELNET_TIMEOUT = 6


def main():
    remote_conn = telnetlib.Telnet(IP_ADDRESS, TELNET_PORT, TELNET_TIMEOUT)
    
    remote_conn.read_until('sername', TELNET_TIMEOUT)
    remote_conn.write('pyclass' + '\n')
    remote_conn.read_until('assword', TELNET_TIMEOUT)
    remote_conn.write('88newclass' + '\n')

    remote_conn.write('show ip int brief' + '\n')
    time.sleep(1)
    output = remote_conn.read_very_eager() 
    print output

    remote_conn.close()

main()
