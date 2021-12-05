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
 
