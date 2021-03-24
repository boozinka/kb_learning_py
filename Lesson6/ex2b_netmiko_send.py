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

cisco1 = {
    'host': '192.168.152.100',
    'username': 'bellw',
    'password': password,
    'secret': password,
    'device_type': 'cisco_ios'
}

arista1 = {
    'host': '192.168.152.101',
    'username': 'bellw',
    'password': password,
    'secret': password,
    'device_type': 'arista_eos'
}

fortigate1 = {
    'host': '192.168.152.102',
    'username': 'bellw',
    'password': password,
    'secret': password,
    'device_type': 'dummy_ios'
}

net_conn = Netmiko(**my_device)
net_conn.send_command_timing('disable')
print(net_conn.find_prompt())   # Returns prompt

net_conn.enable()   # Automatically enter enable mode
print(net_conn.find_prompt())

output = net_conn.send_command('show ip interface brief')
print(output)

for device in (cisco1, arista1, fortigate1):
    net_conn = Netmiko(**device)
    output = netconn.send_command('show ip arp', expect_string=r'#')
    print(output)

