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


def worker_show_version(router, mp_queue):
    '''
    :return: A dictionary where the key is the device identifier
    Value is (success|fail(boolean), return_string)
    '''

    try:
        router['port']
    except KeyError:
        router['port'] = 22

    identifier = '{ip}:{port}'.format(**router)
    return_data = {}

    show_ver_command = 'show version'
    SSHClass = netmiko.ssh_dispatcher(router['device_type'])

    try:
        net_connect = SSHClass(**router)
        show_version = net_connect.send_command(show_ver_command)
    except (NetMikoTimeoutException, NetMikoAuthenticationException) as e:
        return_data[identifier] = (False, e)

        # Add data to the queue (for parent process)
        mp_queue.put(return_data)
        return None

    return_data[identifier] = (True, show_version)
    mp_queue.put(return_data)


def print_output(results):

    print "\nSuccessful devices:"
    for a_dict in results:
        for identifier, v in a_dict.iteritems():
            (success, out_string) = v
            if success:
                print '\n\n'
                print '#' * 80
                print 'Device = {0}\n'.format(identifier)
                print out_string
                print '#' * 80

    print "\n\nFailed devices:\n"
    for a_dict in results:
        for identifier, v in a_dict.iteritems():
            success, out_string = v
            if not success:
                print 'Device failed = {0}'.format(identifier)

    print "\nEnd time:", str(datetime.now())



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