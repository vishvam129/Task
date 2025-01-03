# Write a program to handle a ZeroDivisionError gracefully.

num1=int(input("Enter num1 :- "))
num2=int(input("Enter num2 :- "))

try:
    division=num1/num2
except ZeroDivisionError:
    print("You are trying to divide with 0")
else:
    print(division)
finally:
    print("always remember to not to divide with 0")