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

net_conn = Netmiko(**my_device)
net_conn.send_command_timing('disable')
print(net_conn.find_prompt())   # Returns prompt

net_conn.enable()   # Automatically enter enable mode
print(net_conn.find_prompt())

net_conn.disconnect()

