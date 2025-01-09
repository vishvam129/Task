# Uses the math module to calculate the square root of a 
# user-provided number.if the user enters invalid input then raise ValueError.

import math as m

try:
    number = int(input("Enter Number for square root :- "))
except:
    raise ValueError ("The value is not a integer")
else:
    print(f"The square root of {number} is {m.sqrt(number)}")
