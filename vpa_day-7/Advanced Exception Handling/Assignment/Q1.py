# Prompts the user to input two numbers and divides them.
# Handles ZeroDivisionError, ValueError, and logs any unhandled exceptions to a file.

import logging
try:
    num1 = int(input("Enter number :- "))
    num2 = int(input("Enter number :- "))
    ans = num1 / num2
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)   
except:
    logging.basicConfig(filename="error1.txt",filemode="w",format='%(asctime)s %(message)s')
    loger = logging.getLogger()
    loger.setLevel(logging.DEBUG)
    loger.debug("There is another error in the code ")
else:
    print(ans)