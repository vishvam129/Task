# my_project/
# ├── calculations/
# │   ├── __init__.py
# │   ├── arithmetic.py
# │   ├── geometry.py
# └── main.py
# Import functions from arithmetic.py and geometry.py into main.py and use them.

from calculations import arithmetic as a
from calculations import geometry as g

print("Enter numbers for arithmetic operations ")
num1=int(input("Enter Num1 :- "))
num2=int(input("Enter Num2 :- "))

print(f"The sum of {num1} and {num2} is {a.sum(num1,num2)}")
print(f"The subtract of {num1} and {num2} is {a.subtract(num1,num2)}")
print(f"The division of {num1} and {num2} is {a.division(num1,num2)}")
print(f"The multiply of {num1} and {num2} is {a.multiply(num1,num2)}")

radius = int(input("Enter radius of circle :- "))
print(f"The area of {radius} circle is {g.circle_area(radius)}")

side = int(input("Enter side of square :- "))
print(f"The area of {side} circle is {g.square_area(side)}")