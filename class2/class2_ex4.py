#!/usr/bin/env python

from snmp_helper import snmp_get_oid,snmp_extract



my_hosts = [{'ip_addr': '50.76.53.27', 'port': 7961, 'community': 'galileo'},
            {'ip_addr': '50.76.53.27', 'port': 8061, 'community': 'galileo'}]

for host in my_hosts:
    oid = '1.3.6.1.2.1.1.5.0'
    my_device = (host['ip_addr'], host['community'], host['port'])
    snmp_data = snmp_get_oid(my_device, oid=oid)
    output = snmp_extract(snmp_data)
    print "Hostname:"
    print output + "\n"

    oid = '1.3.6.1.2.1.1.1.0'
    snmp_data = snmp_get_oid(my_device, oid=oid)
    output = snmp_extract(snmp_data)
    print "System Description:"
    print output
    print "-" * 80
    print "\n"


