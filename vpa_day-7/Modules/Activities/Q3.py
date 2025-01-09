# Create a custom module with utility 
# functions (factorial, is_prime, reverse_string) and use it in another script.
import math as m

def factorial(num):
    return f"The factorial of {num} is {m.factorial(num)}"
    
def is_prime(num):
    if num > 1:
        for i in range(2,(num//2)+1):
            if (num % i) == 0:
                return num, "is not a prime number."
        else:
            return(num,"is a Prime number.")
    else:
        return(num,"is a Prime number.")
    

def reverse_string(String):
    return f"The reverse String of {String} is {String[::-1] }"