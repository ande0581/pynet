# Use Pexpect to retrieve the output of 'show ip int brief'

import pexpect


def main():
    ip_addr = '10.40.0.1'
    username = 'myuser'
    password = 'mypass'
    port = 22

    # Spawn child process to connect to router
    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)
    ssh_conn.expect('891#')

    print ssh_conn.before
    print ssh_conn.after


if __name__ == '__main__':
    main()