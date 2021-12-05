#!/usr/bin/env python

# SSH Connect Using Netmiko
#
# Makes an SSH connection using Netmiko

# ConnectHandler
from netmiko import Netmiko
from getpass import getpass

# Input password and assign it to a varible
password = getpass()

# Create a dicionary per device with parameters to feed into 'net_connect'
cisco1 = {
    'host': '192.168.152.100',
    'username': 'bellw',
    'password': password,
    'secret': password,
    'device_type': 'cisco_ios',
    'command': 'sh ip arp'
}

arista1 = {
    'host': '192.168.152.101',
    'username': 'bellw',
    'password': password,
    'secret': password,
    'device_type': 'arista_eos',
    'command': 'sh ip arp'
}

fortigate1 = {
    'host': '192.168.152.102',
    'username': 'bellw',
    'password': password,
    'secret': password,
    'device_type': 'fortinet',
    'command': 'get system arp'
}

# loop through each dictionary
for device in (cisco1, arista1, fortigate1):
    command = device.pop('command')  # Pop command from dictionary before Netmiko and assign to varible
    net_conn = Netmiko(**device)
    output = net_conn.send_command(command)
    print(output)

net_conn.disconnect()

