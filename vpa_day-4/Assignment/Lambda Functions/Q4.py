# Use reduce() to find the greatest number in a list of integers.
from functools import reduce
List=[23,34,32,12,45,54,34,23]
x=reduce(lambda a,b :a if a>b else b,List)
print(x)