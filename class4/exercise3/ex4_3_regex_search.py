#!/usr/bin/env python

"""
Read in the "show_version.txt" file. From this file use regular expressions to extract the
os_version, serial_number, and configuration register value.

Your output should look as follows:

          OS Version: 15.4(2)T1
       Serial Number: FTX0000038X
     Config Register: 0x2102
"""

#from __future__ import unicode_literals, print_function
# Import Path library and assign path to a variable
import pathlib
import re

datafolder = pathlib.Path(r'C:\Users\wbell\Documents\Python\Kirk Byers Online\Lesson 4 - Dictionaries and RegEx')

# Open file and read it as a string (better to use 'readlines' and read as a list)
my_file = datafolder / "show_version.txt"

with open(my_file) as sh_ver:
    sh_ver = sh_ver.read()

match = re.search(r"^Cisco IOS Software,.* Version (.*),", sh_ver, flags=re.M)
if match:
    os_version = match.group(1)

match = re.search(r"^Processor board ID (.*)\s*$", sh_ver, flags=re.M)
if match:
    serial_number = match.group(1)

match = re.search(r"^Configuration register is (.*)\s*$", sh_ver, flags=re.M)
if match:
    config_register = match.group(1)

print()
print("{:>20}: {:15}".format("OS Version", os_version))
print("{:>20}: {:15}".format("Serial Number", serial_number))
print("{:>20}: {:15}".format("Config Register", config_register))
print()
