# Write a program that:
# Creates a tuple of numbers from 1 to 10.
# Finds the sum and product of all numbers in the tuple.

Tuple=(1,2,3,4,5,6,7,8,9,10)

print("Sum of all the elements is :- ",sum(Tuple))

product = 1
for i in Tuple:
    product *= i

print("Product of all the elements is :- ",product)