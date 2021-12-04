#!/usr/bin/env python

"""
Create three separate lists of IP addresses.

The first list should be the IP addresses for the Houston data center routers and should have
over ten IP addresses in it including some duplicate IP addresses.

The second list should be the Atlanta data center routers and should have at least eight IP
addresses including some that overlap with the Houston data center.

The third list should be the Chicago data center routers and should have at least eight IP
addresses. The Chicago IP addresses have some overlap with the IP addresses in both Houston
and in Atlanta

Convert each of these three lists to a set.

Using set operations, find the IP addresses that are duplicated between Houston and Atlanta.

Using set operations, find the IP addresses that are duplicated in all three sites.

Using set operations, find the IP addresses that are entirely unique in Chicago.
"""

from __future__ import unicode_literals, print_function

houston_ips = [
    '10.10.10.1',
    '10.10.20.1',
    '10.10.30.1',
    '10.10.40.1',
    '10.10.50.1',
    '10.10.60.1',
    '10.10.70.1',
    '10.10.80.1',
    '10.10.10.1',
    '10.10.20.1',
    '10.10.70.1',
]

atlanta_ips = [
    '10.10.10.1',
    '10.10.20.1',
    '10.10.30.1',
    '10.10.140.1',
    '10.10.150.1',
    '10.10.160.1',
    '10.10.170.1',
    '10.10.180.1',
]

chicago_ips = [
    '10.10.10.1',
    '10.10.20.1',
    '10.10.140.1',
    '10.10.150.1',
    '10.10.210.1',
    '10.10.220.1',
    '10.10.230.1',
    '10.10.240.1',
]

# Convert each list into a set
houston_set = set(houston_ips)
atlanta_set = set(atlanta_ips)
chicago_set = set(chicago_ips)

print("houston:", houston_set)
print("atlanta:", atlanta_set)
print("chicago:", chicago_set)

# Find the IP addresses that are duplicated between Houston and Atlanta.
common_houston_atlanta = houston_set & atlanta_set     # Intersection operator, gives elements common to both sets
print("\nIP addresses that are common to Houston and Atlanta are:\n")
for i in common_houston_atlanta:
    print(i)

# Find the IP addresses that are duplicated in all three sites.
common_all = houston_set & atlanta_set & chicago_set   # Intersection operator, gives elements common to both sets
print("\nIP addresses that are common to all three sets are:\n")
for i in common_all:
    print(i)

# Find the IP addresses that are entirely unique in Chicago.
unique_houston_atlanta = houston_set | atlanta_set     # Union operator, removes duplicates leaving one occurrence
common_chicago = unique_houston_atlanta & chicago_set  # Intersection operator, gives elements common to both sets
unique_chicago = chicago_set - common_chicago          # Differences operator, removes elements from first set that
                                                       # are also in second set.

unique_both = atlanta_set ^ houston_set                 # Symmetric difference operator, removes duplicates leaving
                                                       # no occurrence (apply to max of two sets)

print("\nIP addresses that are entirely unique to all sets are:\n")
for i in unique_both:
    print(i)

print("\nIP addresses that are entirely unique to Houston and Atlanta are:\n")
for i in unique_houston_atlanta:
    print(i)

print("\nIP addresses that are common to Chicago and all other sets are:\n")
for i in common_chicago:
    print(i)

print("\nIP addresses that are entirely unique to Chicago are:\n")
for i in unique_chicago:
    print(i)

print()
# Alternativily... Chicago unique IP addresses using alternative syntax for difference operator (set1 - set2)
print("-" * 80)
print("Alternativily... Chicago unique IP addresses:\n\n{}".format(
        chicago_set.difference(houston_set).difference(atlanta_set)))
print("-" * 80)
print()



