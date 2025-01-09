# Write a program that raises a ValueError if the user enters 
# invalid input (e.g., entering a string when a number is expected).

try:
    num = int(input("Enter number :- "))
except ValueError as e:
    print(e)