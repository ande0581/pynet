# Use Netmiko to change the logging buffer size (logging buffered <size>)

from netmiko import ConnectHandler
import sys
import time


def main():

    router = {
        'device_type': 'cisco_ios',
        'ip': '10.40.0.1',
        'username': 'myuser',
        'password': 'mypass'
    }

    # Connect to device
    device_conn = ConnectHandler(**router)

    # Show logging buffered
    print "Pre Change Logging Check:"
    print device_conn.send_command("show run | in logging")

    # Change logging buffer
    device_conn.config_mode()

    if device_conn.check_config_mode():
        print "Changing logging buffered...."
        device_conn.send_command("logging buffered 25555")
        device_conn.exit_config_mode()
    else:
        print "Entering Config Mode Failed"
        sys.exit(0)

    # Show logging buffered
    print "Post Change Logging Check:"
    print device_conn.send_command("show run | in logging")

    # Save config
    device_conn.send_command("wr mem")

    # Close connection
    device_conn.disconnect()


if __name__ == '__main__':
    main()