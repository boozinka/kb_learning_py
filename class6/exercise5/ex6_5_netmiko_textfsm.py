#!/usr/bin/env python

# SSH Connect Using Netmiko
#
# Makes an SSH connection using Netmiko

# ConnectHandler
from netmiko import Netmiko
from getpass import getpass
from pprint import pprint

# Input password and assign it to a varible
password = getpass()

try:
    host = raw_input("Enter host to connect to: ")
except NameError:
    host = input("Enter host to connect to: ")

# Create dicionary of parameter to feed into 'net_connect'
my_device = {
    'host': host,
    'username': 'bellw',
    'password': password,
    'secret': password,
    'device_type': 'cisco_ios'
}

# Establish SSH Connection
net_conn = Netmiko(**my_device)

# Enter enable mode
net_conn.enable()   # Automatically enter enable mode

# Send command down the channel, expecting raw output
output = net_conn.send_command('show ip interface brief')
print('\nOutput Type = ', type(output))
print('\n\n')
print(output)

# Send command down the channel and parse through TextFSM
output = net_conn.send_command('show ip interface brief', use_textfsm=True)
print('\nOutput Type = ', type(output))
print('\n\n')
print(output)

# Print structured output header
print('\n\n')
print(f'{"Interface":<20} {" "*3:3} {"IP Address":<15} {" "*3:3} {"Status":<22} {" "*3:3} {"Line Protocol":<14}')
print('-'*85)

# Print structured output
for dict in output:
    print(f'{dict["intf"]:<20} {" "*3:3} {dict["ipaddr"]:<15} {" "*3:3} {dict["status"]:<22} {" "*3:3} {dict["proto"]:<14}')

net_conn.disconnect()

