# Use Netmiko to execute 'show arp' on multiple devices

from netmiko import ConnectHandler


def main():

    router1 = {
        'device_type': 'cisco_ios',
        'ip': '10.40.0.1',
        'username': 'myuser',
        'password': 'mypass'
    }

    router2 = {
        'device_type': 'cisco_ios',
        'ip': '10.40.0.1',
        'username': 'myuser',
        'password': 'mypass'
    }

    routers = [router1, router2]

    for router in routers:

        # Connect to device
        device_conn = ConnectHandler(**router)

        # Print arp table
        print device_conn.send_command("show arp")
        print "\n\n"

        # Close connection
        device_conn.disconnect()


if __name__ == '__main__':
    main()