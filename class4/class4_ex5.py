# Use Netmiko to enter into configuration mode on pynet-rtr2. Also use Netmiko to verify your state

from netmiko import ConnectHandler


def main():

    my_device = {
        'device_type': 'cisco_ios',
        'ip': '10.40.0.1',
        'username': 'myuser',
        'password': 'mypass'
    }

    # Connect to device
    device_conn = ConnectHandler(**my_device)

    # Enter Config mode
    device_conn.config_mode()

    # Verify current mode
    print device_conn.check_config_mode()

    # Print the current prompt
    print device_conn.find_prompt()

    # Close connection
    device_conn.disconnect()


if __name__ == '__main__':
    main()


