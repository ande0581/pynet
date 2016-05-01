import paramiko
import time

MAX_BUFFER = 65535


def clear_buffer(remote_conn):
    if remote_conn.recv_ready():
        return remote_conn.recv(MAX_BUFFER)


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
    remote_conn.send("terminal length 0\n")
    time.sleep(1)
    clear_buffer(remote_conn)

    # Print Show Version
    remote_conn.send("show version\n")
    time.sleep(2)
    output = remote_conn.recv(MAX_BUFFER)
    print output


if __name__ == '__main__':
    main()
