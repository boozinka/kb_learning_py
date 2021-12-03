#!/usr/bin/env python

""" Prompt a user to enter in an IP address from standard input. Read the IP address in and break it up into its
    octets. Print out the octets in decimal, binary, and hex.

Your program output should look like the following:

 $ python exercise2.py 
Please enter an IP address: 80.98.100.240

    Octet1         Octet2         Octet3         Octet4     
------------------------------------------------------------
      80             98             100            240      
   0b1010000      0b1100010      0b1100100     0b11110000   
     0x50           0x62           0x64           0xf0      
------------------------------------------------------------

Four columns, fifteen characters wide, a header column, data centered in the column.
"""

# Ask for IP address
my_ipaddr = input("\nPlease enter an IP address to be converted Hex and Binary: ")

# Convert IP address to list based on "."
ip_list = my_ipaddr.split(".")

# Convert and print values in required format
print()
print(f'{"Octet1":^15} {"Octet2":^15} {"Octet3":^15} {"Octet4":^15}')
print("-" * 60)
print(f'{ip_list[0]:^15} {ip_list[1]:^15} {ip_list[2]:^15} {ip_list[3]:^15}')
print(f'{bin(int(ip_list[0])):^15} {bin(int(ip_list[1])):^15}'
      f'{bin(int(ip_list[2])):^15} {bin(int(ip_list[3])):^15}')
print(f'{hex(int(ip_list[0])):^15} {hex(int(ip_list[1])):^15}'
      f'{hex(int(ip_list[2])):^15} {hex(int(ip_list[3])):^15}')
print("-" * 60)

# Keep program open to diplay result before prompting user to quit.
input("\nPress enter to exit program. ")
