# Use Netmiko to change the logging buffer size (logging buffered <size>)
# and to disable console logging (no logging console) from a file on two routers

from netmiko import ConnectHandler


def main():

    router1 = {
        'device_type': 'cisco_ios',
        'ip': '10.9.0.67',
        'username': 'myuser',
        'password': 'mypass'
    }

    router2 = {
        'device_type': 'cisco_ios',
        'ip': '10.63.176.57',
        'username': 'myuser',
        'password': 'mypass'
    }

    routers = [router1, router2]

    for router in routers:
        # Connect to device
        device_conn = ConnectHandler(**router)

        # Change config from file
        device_conn.send_config_from_file(config_file='config_commands.txt')

        # Validate changes
        print ">>> " + device_conn.find_prompt() + " <<<"
        #output = device_conn.send_command("show run | in logging", delay_factor=.5)
        output = device_conn.send_command_expect("show run | in logging")
        print output + "\n\n"

        # Close connection
        device_conn.disconnect()


if __name__ == '__main__':
    main()