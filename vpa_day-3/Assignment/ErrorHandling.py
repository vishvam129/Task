# Write a program that:
# Prompts the user for a number, divides 100 by it, and handles any errors.
# Ensures that the program does not crash for invalid inputs and always 
# prints "Program Completed" at the end.


try:
    user_input=int(input("Enter Number divide by 100 :- "))
    ans=user_input//100
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print(ans)
finally:
    print("Program completed")