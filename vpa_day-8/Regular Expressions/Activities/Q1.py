# Write a program to:
# Validate email addresses using regular expressions.
# Extract all phone numbers from a given text.

import re
email = input("Enter Email Address for varify :- ")
valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',email)
print("email is Valid " if valid else "email is Invalid ")

name_number = input("Enter your name and phone number :- ")
# name = re.findall(r'[a-zA-Z]',name_number)
phonenumber = re.findall(r'\d{10}',name_number)
# print(name)
print(phonenumber)