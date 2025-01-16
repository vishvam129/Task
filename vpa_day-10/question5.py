# Write a Python program to convert a given tuple of positive integers into an integer.

original_tuple = (1, 2, 3)
result = int(''.join(map(str,original_tuple)))
print(result)