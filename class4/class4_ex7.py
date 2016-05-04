# Use Netmiko to change the logging buffer size (logging buffered <size>)

from netmiko import ConnectHandler
import sys
import time


def main():

    router = {
        'device_type': 'cisco_ios',
        'ip': '10.9.0.67',
        'username': 'myuser',
        'password': 'mypass'
    }

    # Connect to device
    device_conn = ConnectHandler(**router)

    # Show logging buffered
    print "Pre Change Logging Check:"
    print device_conn.send_command("show run | in logging")

    # To change the logging buffered value
    config_commands = ['logging buffered 30000', 'do wr mem']
    output = device_conn.send_config_set(config_commands)
    print output

    # Show logging buffered
    print "Post Change Logging Check:"
    print device_conn.send_command("show run | in logging")

    # Save config
    device_conn.send_command("wr mem")

    # Close connection
    device_conn.disconnect()


if __name__ == '__main__':
    main()