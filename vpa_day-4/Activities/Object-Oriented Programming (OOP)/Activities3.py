# Write a static method to check if a given year is a leap year in a Library class.
import calendar
class Libarary:
    @staticmethod
    def check_leap(year):
        if (calendar.isleap(year)):
            print(f"{year} is a Leap year.")
        else:
            print(f"{year} is not a leap year.")

Libarary.check_leap(2040)
Libarary.check_leap(2039)