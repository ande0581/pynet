'''
Requires paramiko >=1.8.0 (paramiko had an issue with multiprocessing prior
to this)
Example code showing how to use netmiko for multiprocessing.  Create a
separate process for each ssh connection.  Each subprocess executes a
'show version' command on the remote device.  Use a multiprocessing.queue to
pass data from subprocess to parent process.
Only supports Python2
'''

import warnings
with warnings.catch_warnings(record=True) as w:
    import paramiko

import multiprocessing
from datetime import datetime
import netmiko
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException


def worker_show_version():
    pass


def print_output():
    pass


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

    mp_queue = multiprocessing.Queue()
    processes = []

    print "\nStart time:", str(datetime.now())

    for router in routers:

        p = multiprocessing.Process(target=worker_show_version, args=(router, mp_queue))
        processes.append(p)
        # start the work process
        p.start()

    # wait until the child processes have completed
    for p in processes:
        p.join()

    # retrieve all the data from the queue
    results = []
    for p in processes:
        results.append(mp_queue.get())

    print_output(results)

if __name__ == '__main__':
    main()