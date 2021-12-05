# Kirk Byers Learning Python Course

This course covers basic python applied to Network Engineering and Automation

## Topics covered include:

 - [ ] Class 1 - Why Python, the Shell, and Strings
 - [ ] Class 2 - Numbers, Files, Lists, and Linters
 - [ ] Class 3 - Conditionals and Loops
 - [ ] Class 4 - Dictionaries, Exceptions, and Regular Expressions
 - [ ] Class 5 - Functions and the Python Debugger
 - [ ] Class 6 - Netmiko
 - [ ] Class 7 - Jinja2, YAML and JSON
 - [ ] Class 8 - Libraries, PIP, and Virtual Environments

------------------------------------------------------------------

## Class1. Why Python, the Shell, and Strings

### Videos:

 - [ ] I.    Introduction
 - [ ] II.   Why Learn Programing?
 - [ ] III.  Why Python?
 - [ ] IV.   Python2 versus Python3
 - [ ] V.    Characteristics of Python
 - [ ] VI.   The Python Interpreter Shell
 - [ ] VII.  IPython
 - [ ] VIII. Printing to stdout and Reading from stdin
 - [ ] IX.   Dir, Help, and Variables​
 - [ ] X.    Python Strings (Part 1)
 - [ ] XI.   Python Strings (Part 2)
 - [ ] XII.  Python Strings (Part 3)
 - [ ] XIII. Python String Formatting (Part 1)
 - [ ] XIV.  Python String Formatting (Part 2)
 
### Exercises:

1. Create a Python script that has three variables: ip_addr1, ip_addr2, ip_addr3 (representing three corresponding IP addresses). Print these three variables to standard output using a single print statement.

   Make your print statement compatible with both Python2 and Python3.

   If you are using either Linux or MacOS make your program executable by adding a shebang line and by changing the files permissions (i.e. chmod 755 exercise1.py).

2. Prompt a user to enter in an IP address from standard input. Read the IP address in and break it up into its octets. Print out the octets in decimal, binary, and hex.

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

3. Create three different variables the first variable should use all lower case characters with underscore ( _ ) as the word separator. The second variable should use all upper case characters with underscore as the word separator. The third variable should use numbers, letters, and underscore, but still be a valid variable Python variable name.

   Make all three variables be strings that refer to IPv6 addresses.

   Use the from future technique so that any string literals in Python2 are unicode.

   - compare if variable1 equals variable2
   - compare if variable1 is not equal to variable3

4. Create a show_version variable that contains the following

       show_version = "*0        CISCO881-SEC-K9       FTX0000038X    " 

   - Remove all leading and trailing whitespace from the string.
   - Split the string and extract the model and serial_number from it.
   - Check if 'Cisco' is contained in the model string (ignore capitalization).
   - Check if '881' is in the model string.
   - Print out both the serial number and the model.

5. You have the following three variables from the arp table of a router:

       mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
       mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
       mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

   Process these ARP entries and print out a table of "IP ADDR" to "MAC ADDRESS" mappings. The output should look like following:

            IP ADDR          MAC ADDRESS
       ------------       --------------
       10.220.88.29       5254.abbe.5b7b
       10.220.88.30       5254.ab71.e119
       10.220.88.32       5254.abc7.26aa

   Two columns, 20 characters wide, data right aligned, a header column.

------------------------------------------------------------------

## Class2. Numbers, Files, Lists, and Linters

### Videos:

 - [ ] I.    Numbers
 - [ ] II.   Files
 - [ ] III.  Lists
 - [ ] IV.   List Slices
 - [ ] V.    Lists are Mutable
 - [ ] VI.   Tuples
 - [ ] VII.  Using .join()
 - [ ] VIII. sys.argv
 - [ ] IX.   Linters
 
### Exercises:

1. Open the "show_version.txt" file for reading. Use the .read() method to read in the entire file contents to a variable. Print out the file contents to the screen. Also print out the type of the variable (you should have a string at this point).

   Close the file.

   Open the file a second time using a Python context manager (with statement). Read in the file contents using the .readlines() method. Print out the file contents to the screen. Also print out the type of the variable (you should have a list at this point).

2. Create a list of five IP addresses.

   - Use the .append() method to add an IP address onto the end of the list. Use the .extend() method to add two more IP addresses to the end of the list.
   - Use list concatenation to add two more IP addresses to the end of the list.
   - Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in the list.
   - Using the .pop() method to remove the first IP address in the list and the last IP address in the list.
   - Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.

3. Read in the "show_arp.txt" file using the readlines() method. Use a list slice to remove the header line.

   - Use pretty print to print out the resulting list to the screen, syntax is:

       from pprint import pprint
       pprint(some_var)

   - Use the list .sort() method to sort the list based on IP addresses.
   - Create a new list slice that is only the first three ARP entries.
   - Use the .join() method to join these first three ARP entries back together as a single string using the newline character ('\n') as the separator.
   - Write this string containing the three ARP entries out to a file named "arp_entries.txt".

4. Read in the "show_ip_int_brief.txt" file into your program using the .readlines() method.

   - Obtain the list entry associated with the FastEthernet4 interface. You can just hard-code the index at this point since we haven't covered for-loops or regular expressions. Use the string .split() method to obtain both the IP address and the corresponding interface associated with the IP.
   - Create a two element tuple from the result (intf_name, ip_address).
   - Print that tuple to the screen.

   Use pycodestyle on this script. Get the warnings/errors to zero. You might need to 'pip install pycodestyle' on your computer (you should be able to type this from the shell prompt). Alternatively, you can type 'python -m pip install pycodestyle'.

5. Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the first and last lines of the output.

   - From the first line use the string .split() method to obtain the local AS number.
   - From the last line use the string .split() method to obtain the BGP peer IP address.
   - Print both local AS number and the BGP peer IP address to the screen.

------------------------------------------------------------------

## Class3. Conditionals and Loops

### Videos:

 - [ ] I.    Conditionals
 - [ ] II.   Boolean Logic (Booleans, Ternary Operator, None)
 - [ ] III.  Python For Loops
 - [ ] IV.   For Loops (Enumerate)
 - [ ] V.    For Loops (Break and Continue)
 - [ ] VI.   While Loops
 - [ ] VII.  Loops Miscillaneous

### Exercises:

1. Read the "show_vlan.txt" file into your program. Loop through the lines in this file and extract all of the VLAN_ID, VLAN_NAME combinations. From these VLAN_ID and VLAN_NAME construct a new list where each element in the list is a tuple consisting of (VLAN_ID, VLAN_NAME). Print this data structure to the screen. Your output should look as follows:

       [('1', 'default'),
        ('400', 'blue400'),
        ('401', 'blue401'),
        ('402', 'blue402'),
        ('403', 'blue403')]


2. Read the contents of the "show_arp.txt" file. Using a for loop, iterate over the lines of this file. Process the lines of the file and separate out the ip_addr and mac_addr for each entry into a separate variable.

   - Add a conditional statement that searches for '10.220.88.1'. If 10.220.88.1 is found, print out the string "Default gateway IP/Mac" and the corresponding IP address and MAC Address.
   - Using a conditional statement, also search for '10.220.88.30'. If this IP address is found, then print out "Arista3 IP/Mac is" and the corresponding ip_addr and mac_addr.
   - Keep track of whether you have found both the Default Gateway and the Arista3 switch. Once you have found both of these devices, 'break' out of the for loop.


3.  Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this file. Keep reading the lines until you have encountered the remote "System Name" and remote "Port id". Save these two items into variables and print them to the screen. You should extract only the system name and port id from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15'). Break out of your loop once you have retrieved these two items.


4. You have the following data structure:

       arp_table = [('10.220.88.1', '0062.ec29.70fe'),
        ('10.220.88.20', 'c89c.1dea.0eb6'),
        ('10.220.88.21', '1c6a.7aaf.576c'),
        ('10.220.88.28', '5254.aba8.9aea'),
        ('10.220.88.29', '5254.abbe.5b7b'),
        ('10.220.88.30', '5254.ab71.e119'),
        ('10.220.88.32', '5254.abc7.26aa'),
        ('10.220.88.33', '5254.ab3a.8d26'),
        ('10.220.88.35', '5254.abfb.af12'),
        ('10.220.88.37', '0001.00ff.0001'),
        ('10.220.88.38', '0002.00ff.0001'),
        ('10.220.88.39', '6464.9be8.08c8'),
        ('10.220.88.40', '001c.c4bf.826a'),
        ('10.220.88.41', '001b.7873.5634')]

   Loop over this data structure and extract all of the MAC addresses. Process all of the MAC addresses to get them into a standard format. Print all of the new standardized MAC address to the screen. The standardized format should be as follows:

       00:62:EC:29:70:FE

   The hex digits should be capitalized. Additionally, there should be a colon between each octet in the MAC address.

5. [Optional/bonus]

   ***Note***, to actually test this in your environment, change the test IP addresses to something in your environment that you can ping successfully. ***

   - Construct a list of 254 IP addresses. The base IP address should be equal to '10.10.100.0' or '10.10.100.'.
   - You should use the 'range' builtin to accomplish this.
   - Your list should have all of the IP addresses from 10.10.100.1 to 10.10.100.254.
   - Use Python's 'enumerate' to print out all of the IP addresses and their corresponding list index.

   The output should look similar to the following:

       0 ---> 10.10.100.1
       1 ---> 10.10.100.2
       2 ---> 10.10.100.3
       3 ---> 10.10.100.4
       4 ---> 10.10.100.5
       ...

   - Use a list slice to create a new list that goes from 10.10.100.3 to 10.10.100.6.
   - Using a loop and os.system("ping -c 3 10.10.100.3") try pinging all of the IP addresses in this short list. For Windows the command will probably be os.system("ping -n 3 10.10.100.3").
   - Put a variable at the top to define whether you are using Windows or Linux/MacOs. This should be similar to the following:

           WINDOWS = False
           
           base_cmd_linux = 'ping -c 2'
           base_cmd_windows = 'ping -n 2'
           # Ternary operator
           base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

------------------------------------------------------------------

## Class4. Dictionaries, Exceptions, and Regular Expressions

### Videos:

 - [ ] I.    Dictionaries
 - [ ] II.   Dictionary Methods
 - [ ] III.  Sets
 - [ ] IV.   Exceptions
 - [ ] V.    Regular Expressions (Part1)
 - [ ] VI.   Regular Expressions (Part2)
 - [ ] VII.  Regular Expressions (Part3)
 - [ ] VIII. Regular Expressions, Other Methods

### Exercises:

1. Create a dictionary representing a network device. The dictionary should have key-value pairs representing the 'ip_addr', 'vendor', 'username', and 'password' fields.

   - Print out the 'ip_addr' key from the dictionary.
   - If the 'vendor' key is 'cisco', then set the 'platform' to 'ios'. If the 'vendor' key is 'juniper', then set the 'platform' to 'junos'.
   - Create a second dictionary named 'bgp_fields'. The 'bgp_fields' dictionary should have a keys for 'bgp_as', 'peer_as', and 'peer_ip'.
   - Using the .update() method add all of the 'bgp_fields' dictionary key-value pairs to the network device dictionary.
   - Using a for-loop, iterate over the dictionary and print out all of the dictionary keys.
   - Using a single for-loop, iterate over the dictionary and print out all of the dictionary keys and values.

2. Create three separate lists of IP addresses. The first list should be the IP addresses of the Houston data center routers, and it should have over ten RFC1918 IP addresses in it (including some duplicate IP addresses).

   The second list should be the IP addresses of the Atlanta data center routers, and it should have at least eight RFC1918 IP addresses (including some addresses that overlap with the Houston data center).

   The third list should be the IP addresses of the Chicago data center routers, and it should have at least eight RFC1918 IP addresses. The Chicago IP addresses should have some overlap with both the IP addresses in Houston and Atlanta.

   Convert each of these three lists to a set.

   - Using a set operation, find the IP addresses that are duplicated between Houston and Atlanta.
   - Using set operations, find the IP addresses that are duplicated in all three sites.
   - Using set operations, find the IP addresses that are entirely unique in Chicago.

3. Read in the 'show_version.txt' file. From this file, use regular expressions to extract the OS version, serial number, and configuration register values.

   Your output should look as follows:

       OS Version: 15.4(2)T1
       Serial Number: FTX0000038X
       Config Register: 0x2102

4. Using a named regular expression (?P<name>), extract the model from the below string:

        show_version = '''
        Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
        Processor board ID FTX0000038X
        
        5 FastEthernet interfaces
        1 Virtual Private Network (VPN) Module
        256K bytes of non-volatile configuration memory.
        126000K bytes of ATA CompactFlash (Read/Write)
        '''

   Note that, in this example, '881' is the relevant model. Your regular expression should not, however, include '881' in its search pattern since this number changes across devices.

   Using a named regular expression, also extract the '236544K/25600K' memory string.

   Once again, none of the actual digits of the memory on this device should be used in the regular expression search pattern.

   Print both the model number and the memory string to the screen.

5. Read the 'show_ipv6_intf.txt' file.

   From this file, use Python regular expressions to extract the two IPv6 addresses.

   The two relevant IPv6 addresses you need to extract are:

       2001:11:2233::a1/24
       2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2/64

   Try to use re.DOTALL flag as part of your search. Your search pattern should not include any of the literal characters in the IPv6 address.

   From this, create a list of IPv6 addresses that includes only the above two addresses.

   Print this list to the screen.

------------------------------------------------------------------

## Class5. Functions and the Python Debugger

### Videos:

 - [ ] I.    Functions (Part1)
 - [ ] II.   Functions (Part2)
 - [ ] III.  Misc Topics (Part1)
 - [ ] IV.   Misc Topics (Part1)
 - [ ] V.    Python Debugger (pdb)

### Exercises:

1. Function Arguments - Positional, Named and No Arguments

   a. Create an ssh_conn function. This function should have three parameters: ip_addr, username, and password. The function should print out each of these three variables and clearly indicate which variable it is printing out.

   - Call this ssh_conn function using entirely positional arguments.
   - Call this ssh_conn function using entirely named arguments.
   - Call this ssh_conn function using a mix of positional and named arguments.

   b. Expand on the ssh_conn function from exercise1 except add a fourth parameter 'device_type' with a default value of 'cisco_ios'. Print all four of the function variables out as part of the function's execution.

   Call the 'ssh_conn2' function both with and without specifying the device_type

   Create a dictionary that maps to the function's parameters. Call this ssh_conn2 function using the `**kwargs` technique.


2. Create a function that randomly generates an IP address for a network. The default base network should be '10.10.10.'. For simplicity the network will always be a /24.

   You should be able to pass a different base network into your function as an argument.

   Randomly pick a number between 1 and 254 for the last octet and return the full IP address.

   You can use the following to randomly generate the last octet:

       import random
       random.randint(1, 254)

   - Call your function using no arguments.
   - Call your function using a positional argument.
   - Call your function using a named argument.

   For each function call print the returned IP address to the screen.

3. Similar to lesson3, exercise4 write a function that normalizes a MAC address to the following format:

       01:23:45:67:89:AB

   - This function should handle the lower-case to upper-case conversion.
   - It should also handle converting from '0000.aaaa.bbbb' and from '00-00-aa-aa-bb-bb' formats.
   - The function should have one parameter, the mac_address. It should return the normalized MAC address

   Single digit bytes should be zero-padded to two digits. In other words, this:

       a:b:c:d:e:f

   should be converted to:

       0A:0B:0C:0D:0E:0F

   Write several test cases for your function and verify it is working properly.

4. Copy your solution from exercise3 to exercise4. Add an 'import pdb' and pdb.set_trace() statement outside of your function (i.e. where you have your function calls).

   Inside of pdb, experiment with:

   - Listing your code.
   - Using 'next' and 'step' to walk through your code. Make sure you understand the difference between next and step.
   - Experiment with 'up' and 'down' to move up and down the code stack.
   - Use p <variable> to inspect a variable.
   - Set a breakpoint and run your code to the breakpoint.
   - Use '!command' to change a variable (for example !new_mac = [])

------------------------------------------------------------------

## Class5. Functions and the Python Debugger

### Videos:

 - [ ] I.    Functions (Part1)
 - [ ] II.   Functions (Part2)
 - [ ] III.  Misc Topics (Part1)
 - [ ] IV.   Misc Topics (Part1)
 - [ ] V.    Python Debugger (pdb)

### Exercises:

1. Function Arguments - Positional, Named and No Arguments

   a. Create an ssh_conn function. This function should have three parameters: ip_addr, username, and password. The function should print out each of these three variables and clearly indicate which variable it is printing out.

   - Call this ssh_conn function using entirely positional arguments.
   - Call this ssh_conn function using entirely named arguments.
   - Call this ssh_conn function using a mix of positional and named arguments.

   b. Expand on the ssh_conn function from exercise1 except add a fourth parameter 'device_type' with a default value of 'cisco_ios'. Print all four of the function variables out as part of the function's execution.

   Call the 'ssh_conn2' function both with and without specifying the device_type

   Create a dictionary that maps to the function's parameters. Call this ssh_conn2 function using the `**kwargs` technique.


2. Create a function that randomly generates an IP address for a network. The default base network should be '10.10.10.'. For simplicity the network will always be a /24.

   You should be able to pass a different base network into your function as an argument.

   Randomly pick a number between 1 and 254 for the last octet and return the full IP address.

   You can use the following to randomly generate the last octet:

       import random
       random.randint(1, 254)

   - Call your function using no arguments.
   - Call your function using a positional argument.
   - Call your function using a named argument.

   For each function call print the returned IP address to the screen.

3. Similar to lesson3, exercise4 write a function that normalizes a MAC address to the following format:

       01:23:45:67:89:AB

   - This function should handle the lower-case to upper-case conversion.
   - It should also handle converting from '0000.aaaa.bbbb' and from '00-00-aa-aa-bb-bb' formats.
   - The function should have one parameter, the mac_address. It should return the normalized MAC address

   Single digit bytes should be zero-padded to two digits. In other words, this:

       a:b:c:d:e:f

   should be converted to:

       0A:0B:0C:0D:0E:0F

   Write several test cases for your function and verify it is working properly.

4. Copy your solution from exercise3 to exercise4. Add an 'import pdb' and pdb.set_trace() statement outside of your function (i.e. where you have your function calls).

   Inside of pdb, experiment with:

   - Listing your code.
   - Using 'next' and 'step' to walk through your code. Make sure you understand the difference between next and step.
   - Experiment with 'up' and 'down' to move up and down the code stack.
   - Use p <variable> to inspect a variable.
   - Set a breakpoint and run your code to the breakpoint.
   - Use '!command' to change a variable (for example !new_mac = [])

------------------------------------------------------------------

## Class6. Netmiko

### Videos:

 - [ ] I.    Netmiko Introduction and Basics
 - [ ] II.   Netmiko Show Commands
 - [ ] III.  Netmiko and Prompting
 - [ ] IV.   Netmiko and TextFSM
 - [ ] V.    Netmiko Config Changes
 - [ ] VI.   Netmiko Troubleshooting
 
### Exercises:

***Note***, you will need some sort of a network device to work on these exercises. This can be a virtual or physical device. Make sure you are only working on test or lab devices.

1. Using Netmiko, establish a connection to a network device and print out the device's prompt.

2. Use send_command() to send a show command down the SSH channel. Retrieve the results and print the results to the screen.

3. Find a command on your device that has additional prompting. Use send_command_timing to send the command down the SSH channel. Capture the output and handle the additional prompting.

4. Use send_config_set() and send_config_from_file() to make configuration changes. 

   The configuration changes should be benign. For example, on Cisco IOS I typically change the logging buffer size. 

   As part of your program verify that the configuration change occurred properly. For example, use send_command() to execute 'show run' and verify the new configuration.


5. Optional, use send_command() in conjunction with ntc-templates to execute a show command. Have TextFSM automatically convert this show command output to structured data.


6. Optional, connect to three networking devices one after the other. Use send_command() to execute a show command on each of these devices. Print this output to the screen.

------------------------------------------------------------------

## Class7. Jinja2, YAML and JSON

### Videos:

 - [ ] I.    Jinja2 Basics
 - [ ] II.   Jinja2 For-Loops and Conditionals
 - [ ] III.  Jinja2 and CSV
 - [ ] IV.   Jinja2 Dictionaries and Nested Loops
 - [ ] V.    YAML Basics
 - [ ] VI.   YAML Part2
 - [ ] VII.  Using Python to Write YAML
 - [ ] VIII. JSON
 - [ ] IX.   Managing Data Structures
 
### Exercises:

1. Jinja2 Rendering, with Conditionals and For-Loops

   a. Use Jinja2 templating to render the following:

       vlan 
          name 

   Your template should be inside of your Python program for simplicity.

   The output from processing your template should be as follows. This should be printed to stdout.

       vlan 400
          name red400

   b. Using a conditional in a Jinja2 template, generate the following output:

       crypto isakmp policy 10
        encr aes
        authentication pre-share
        group 5
       crypto isakmp key my_key address 1.1.1.1 no-xauth
       crypto isakmp keepalive 10 periodic

   The encryption of aes, and the Diffie-Hellman group should be variables in the template.

   Additionally this entire ISAKMP section should only be added if the isakmp_enable variable is set to True.

   Your template should be inside your Python program for simplicity.

   c. Using Jinja2 templating and a for-loop inside the template, generate the following configuration snippet:

       vlan 501
          name blue501
       vlan 502
          name blue502
       vlan 503
          name blue503
       vlan 504
          name blue504
       vlan 505
          name blue505
       vlan 506
          name blue506
       vlan 507
          name blue507
       vlan 508
          name blue508

   Your template should be inside your Python program for simplicity.

   It is fine for your VLAN IDs to be out of order in the generated configuration (for example, VLAN ID 508 can come before VLAN ID 504).

2. Using Python and Jinja2 templating generate the following OSPF configuration:

       interface vlan 1
          ip ospf priority 100

       router ospf 10
          passive-interface default
          no passive-interface Vlan1
          no passive-interface Vlan2
          network 10.10.10.0/24 area 0.0.0.0
          network 10.10.20.0/24 area 0.0.0.0
          network 10.10.30.0/24 area 0.0.0.0
          max-lsa 12000

   The following items should be variables in your Jinja2 template:

       ospf_process_id
       ospf_priority
       ospf_active_interfaces (i.e. the non-passive interfaces)
       ospf_area0_networks (the three networks that are specified as belonging to area0)

   Your template should be in an external file.

   Your template should also use a conditional to control whether this is output or not:

       interface vlan 1
          ip ospf priority 100

   If the 'ospf_priority variable is defined', then include that section. If 'ospf_priority' is not defined then only include the 'router ospf 10' section.

3. YAML File Data Structures

   a. Create a YAML file that defines a list of interface names. Use the expanded form of YAML.

   Use a Python script to read in this YAML list and print it to the screen.

   The output of your Python script should be:

       ['Ethernet1', 'Ethernet2', 'Ethernet3', 'Ethernet4', 'Ethernet5', 'Ethernet6', 'Ethernet7', 'Management1', 'Vlan1']

   b. Expand the data structure defined earlier in exercise3a. This time you should have an 'interfaces' key that refers to a dictionary.

   Use Python to read in this YAML data structure and print this to the screen.

   The output of your Python script should look as follows (in other words, your YAML data structure should yield the following when read by Python). You YAML data structure should be written in expanded YAML format.

       {'interfaces': {
           'Ethernet1': {'mode': 'access', 'vlan': 10},
           'Ethernet2': {'mode': 'access', 'vlan': 20},
           'Ethernet3': {'mode': 'trunk',
                         'native_vlan': 1,
                         'trunk_vlans': 'all'}
           }
       }

4. Take the YAML file and corresponding data structure that you defined in exercise3b:

       {'interfaces': {
           'Ethernet1': {'mode': 'access', 'vlan': 10},
           'Ethernet2': {'mode': 'access', 'vlan': 20},
           'Ethernet3': {'mode': 'trunk',
                         'native_vlan': 1,
                         'trunk_vlans': 'all'}
           }
       }

   From this YAML data input source, use Jinja templating to generate the following configuration output:

       interface Ethernet1
         switchport mode access
         switchport access vlan 10
       interface Ethernet2
         switchport mode access
         switchport access vlan 20
       interface Ethernet3
         switchport mode trunk
         switchport trunk native vlan 1
         switchport trunk allowed vlan all

   The following should all be variables in your Jinja template (the names may be different than below, but they should be variabilized and not be hard-coded in your template).

   interface_name
   switchport_mode
   access_vlan
   native_vlan
   trunk_vlans

   All your Jinja2 variables should be retrieved from your YAML file. 

   This exercise might be challenging.

------------------------------------------------------------------

## Class8. Libraries, PIP, and Virtual Environments

### Videos:

 - [ ] I.    Importing Libraries
 - [ ] II.   sys.path and PYTHONPATH
 - [ ] III.  pip
 - [ ] IV.   Virtual Environments
 - [ ] V.    Creating a Simple Python Module
 
### Exercises:

1. Importing Modules and the PYHONPATH environment varible

   a. Importing Modules
   
   Import the 'datetime' library. Print out the module that is being imported by datetime (the  `__file__` attribute)

   Import the Python ipaddress library. Print out the module that is being imported by ipaddress (the  `__file__` attribute). If you are using Python 2.7, you will need to pip install the ipaddress library.

   Import sys and use pprint to pprint sys.path

   b. In a separate Python file named 'my_devices.py', define a dictionary named 'rtr1' with the following key-value pairs:

       host = rtr1.domain.com
       username = cisco
       password = cisco123
       device_type = cisco_ios

   Import my_devices into this program, and print the rtr1 dictionary to the screen using pprint.

   c. In a Python shell, try importing the 'my_devices' when my_devices.py is not in your current working directory.

   What exception do you get when you do this?

   Update your PYTHONPATH environment variable so that you are successfully able to import this module.


2. Virtual Environments

   a. Create a new virtual environment on your system named 'test_venv'.
   b. Activate the virtual environment
   c. Use 'which python' to see the path of the Python that you are using.
   d. Use 'pip list' to see the packages you have installed.
   e. Use pip to install Netmiko and the requests library.
   f. Use 'pip list' to see the updated list of installed packages.

3. Pip install

   a. Using the same 'test_venv' that you created in exercise2, install netmiko version 2.0.1. Verify that this version is installed by executing the following from the Python shell:

       >>> import netmiko
       >>> netmiko.__version__
       '2.0.1'

   b. Using pip, upgrade your version of Netmiko to the latest version.
   c. Deactivate your virtual environment. See 'which python' is now being used.

4. Pip uninstall

   a. Activate your 'test_venv' virtual environment.
   b. Use pip to uninstall the Netmiko library.
   c. Verify that Netmiko is no longer installed.
   d. Use pip to install the 'develop' branch of Netmiko.


