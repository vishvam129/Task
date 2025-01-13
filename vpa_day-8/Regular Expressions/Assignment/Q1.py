# Create a program that:
# Validates a user-provided IPv4 address.

import re

# Define the regex pattern for a valid IPv4 address
ipv4_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')

def is_valid_ipv4(ip):
    if not ipv4_pattern.match(ip):
        return False
    parts = ip.split(".")
    for part in parts:
        if not 0 <= int(part) <= 255:
            return False
    return True

ip_address = input("Please enter an IPv4 address: ")
if is_valid_ipv4(ip_address):
    print(f"{ip_address} is a valid IPv4 address.")
else:
    print(f"{ip_address} is not a valid IPv4 address.")
