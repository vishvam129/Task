# Multiprocessing Exercise:
# - Create a program to calculate the factorial of numbers using multiple processes

import multiprocessing

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(fact)

n = int(input("Enter the number for fact :- "))
fact_process = multiprocessing.Process(target=factorial,args=(n,))

fact_process.start()
fact_process.join()