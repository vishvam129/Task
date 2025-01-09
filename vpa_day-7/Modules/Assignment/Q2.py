# Write a Python Program to get the current date and also month,year and day.

import datetime
print(f"Todays date is {datetime.datetime.today().date()}")
print(f" month is {datetime.datetime.today().month}")
print(f" year is {datetime.datetime.today().year}")
print(f"Todays day is {datetime.datetime.today().day}")
