# Use Paramiko to change the 'logging buffered <size>' configuration

import paramiko
import time

MAX_BUFFER = 65535


def clear_buffer(remote_conn):
    if remote_conn.recv_ready():
        return remote_conn.recv(MAX_BUFFER)


def send_command(remote_conn, cmd='', delay=1):
    '''
    Send command down the channel. Retrieve and return the output.
    '''
    if cmd != '':
        cmd = cmd.strip()
    remote_conn.send(cmd + '\n')
    time.sleep(delay)

    if remote_conn.recv_ready():
        return remote_conn.recv(MAX_BUFFER)
    else:
        return ''



def main():
    ip_addr = '10.40.0.1'
    username = 'myuser'
    password = 'mypass'

    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Create SSH Session
    remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False)

    # Invoke Interactive Shell
    remote_conn = remote_conn_pre.invoke_shell()
    time.sleep(1)
    clear_buffer(remote_conn)

    # Disable Paging
    send_command(remote_conn, 'terminal length 0')

    # Show logging config
    print "Pre-change logging level"
    output = send_command(remote_conn, 'show run | in logging')
    print output

    # Change Logging Buffered
    send_command(remote_conn, 'config t')
    send_command(remote_conn, 'logging buffered 25000')
    send_command(remote_conn, 'exit')

    # Show logging config
    print "Post-change logging level"
    output = send_command(remote_conn, 'show run | in logging')
    print output

    # Save config
    send_command(remote_conn, 'wr mem')


if __name__ == '__main__':
    main()
