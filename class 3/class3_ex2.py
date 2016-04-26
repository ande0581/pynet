# SnmpWalk.exe -r:10.40.0.1 -t:10 -c:"private" -os:1.3.6.1.2.1.2.2.1 -op:1.3.6.1.2.1.2.2.1.20
import time

import snmp_helper
import pygal

# Print debug output
DEBUG = False

# Polling Interval in Seconds
INTERVAL_TIME = 60

# Number of interfaces
INTERVAL_COUNT = 5


def main():
    ip = '10.40.0.1'
    a_user = 'mysnmpuser'
    auth_key = 'myauthkey'
    encrypt_key = 'myencryptkey'
    snmp_user = (a_user, auth_key, encrypt_key)
    my_router = (ip, 161)

    systemName = '1.3.6.1.2.1.1.5.0'
    fa8description = '1.3.6.1.2.1.2.2.1.2.10'
    fa8InOctets = '1.3.6.1.2.1.2.2.1.10.10'
    fa8InUcastPkts = '1.3.6.1.2.1.2.2.1.11.10'
    fa8OutOctets = '1.3.6.1.2.1.2.2.1.16.10'
    fa8OutUcastPkts = '1.3.6.1.2.1.2.2.1.17.10'

    fa8_in_octets = []
    fa8_in_packets = []
    fa8_out_octets = []
    fa8_out_packets = []

    fa8_in_octets_last = 0
    fa8_in_packets_last = 0
    fa8_out_octets_last = 0
    fa8_out_packets_last = 0

    for i in range(INTERVAL_COUNT + 1):
        snmp_data = snmp_helper.snmp_get_oid_v3(my_router, snmp_user, oid=fa8InOctets)
        snmp_data = int(snmp_helper.snmp_extract(snmp_data))
        if fa8_in_octets:
            fa8_in_octets.append(snmp_data - fa8_in_octets_last)
        else:
            fa8_in_octets.append(snmp_data)
        fa8_in_octets_last = snmp_data

        snmp_data = snmp_helper.snmp_get_oid_v3(my_router, snmp_user, oid=fa8InUcastPkts)
        snmp_data = int(snmp_helper.snmp_extract(snmp_data))
        if fa8_in_packets:
            fa8_in_packets.append(snmp_data - fa8_in_packets_last)
        else:
            fa8_in_packets.append(snmp_data)
        fa8_in_packets_last = snmp_data

        snmp_data = snmp_helper.snmp_get_oid_v3(my_router, snmp_user, oid=fa8OutOctets)
        snmp_data = int(snmp_helper.snmp_extract(snmp_data))
        if fa8_out_octets:
            fa8_out_octets.append(snmp_data - fa8_out_octets_last)
        else:
            fa8_out_octets.append(snmp_data)
        fa8_out_octets_last = snmp_data

        snmp_data = snmp_helper.snmp_get_oid_v3(my_router, snmp_user, oid=fa8OutUcastPkts)
        snmp_data = int(snmp_helper.snmp_extract(snmp_data))
        if fa8_out_packets:
            fa8_out_packets.append(snmp_data - fa8_out_packets_last)
        else:
            fa8_out_packets.append(snmp_data)
        fa8_out_packets_last = snmp_data

        print "{}% Complete".format((float(i) / INTERVAL_COUNT) * 100)
        time.sleep(INTERVAL_TIME)

    if DEBUG:
        print fa8_in_octets[1:]
        print fa8_in_packets[1:]
        print fa8_out_octets[1:]
        print fa8_out_packets[1:]

    # Create a Chart of type Line
    line_chart = pygal.Line()

    # Title
    line_chart.title = 'Input/Output Packets and Bytes - Interface Fa8'

    # X-axis labels
    label = []
    for i in range(INTERVAL_COUNT):
        label.append(str(i + 1))

    line_chart.x_labels = label

    # Add each one of the above lists to the graph as a line with corresponding label
    line_chart.add('InPackets', fa8_in_packets[1:])
    line_chart.add('OutPackets', fa8_out_packets[1:])
    line_chart.add('InBytes', fa8_in_octets[1:])
    line_chart.add('OutBytes', fa8_out_octets[1:])

    # Create an output image file
    line_chart.render_to_file('fa8.svg')


if __name__ == '__main__':
    main()