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

# Establish SSH session and enter enable mode
net_conn = Netmiko(**my_device)
net_conn.enable()

# Issue show commands to confirm initial settings
sh_cmds = ['show ip dns view', 'show log | inc Log Buffer']
for command in sh_cmds:
    sh_output = net_conn.send_command(command)   # Send the command down the SSH channel Print(sh_output, '\n')
    print(sh_output, '\n')

# Create a list of commands to execute
ex_cmds = ['no ip domain-lookup', 'logging buffered 4096']
ex_output = net_conn.send_config_set(ex_cmds)   # Send the excute commands down the SSH channel
print(ex_output, '\n')

for command in sh_cmds:
    sh_output = net_conn.send_command(command)   # Send the command down the SSH channel Print(sh_output, '\n')
    print(sh_output, '\n')

net_conn.disconnect

