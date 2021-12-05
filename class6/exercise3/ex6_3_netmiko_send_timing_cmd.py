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

# set filename and command varible
filename = 'small.txt'
command = 'delete flash:{}'.format(filename)

net_conn = Netmiko(**my_device)
net_conn.enable()

output = net_conn.send_command_timing(command)   # Send the command down the SSH channel
prompt = net_conn.find_prompt()                  # Find the current prompt

while '#' not in prompt:   # Run loop while the prompt isn't enable
    # Send carriage return down the channel
    output += net_conn.send_command_timing('\n', strip_prompt=False, strip_command=False)
    prompt = net_conn.find_prompt()   # Find the new prompt
    
    print()
    print("-" * 80)
    print('\n', output, '\n')
    print("-" * 80)
    print()

net_conn.disconnect

