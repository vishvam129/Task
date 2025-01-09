# Import the math module and calculate the area of a circle given its radius.
import random as r
import math as m

rad = input("Enter radius of circle or press Enter for random number between 10 to 20 :- ") or r.randint(10,20)
ans = m.pi*(int(rad)**2)
print(f"The Area of radius {rad} is {ans}")