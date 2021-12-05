#!/usr/bin/env python

# SSH Connect Using Netmiko
#
# Makes an SSH connection using Netmiko

# ConnectHandler
from netmiko import Netmiko
from getpass import getpass

net_conn = Netmiko(host ='192.168.152.100', username='bellw',
                   password=getpass(), device_type='cisco_ios')

print(net_conn.find_prompt())

net_conn.disconnect()

