#!/usr/bin/env python

# SSH Connect Using Netmiko
#
# Makes an SSH connection using Netmiko

# ConnectHandler
from netmiko import Netmiko
from getpass import getpass

# Input password and assign it to a varible
password = getpass()

# Create dicionary of parameter to feed into 'net_connect'
my_device = {
    'host': '192.168.152.100',
    'username': 'bellw',
    'password': password,
    'secret': password,
    'device_type': 'cisco_ios'
}

command = "show ip int brief"

net_conn = Netmiko(**my_device)
net_conn.send_command_timing('disable')
print(net_conn.find_prompt())   # Returns prompt

net_conn.enable()   # Automatically enter enable mode
output = net_connect.send_command(command)
print()
print("-" * 80)
print(output)
print("-" * 80)
print()

net_conn.disconnect()

