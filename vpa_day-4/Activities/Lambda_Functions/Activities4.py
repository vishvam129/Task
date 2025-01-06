# Use reduce() to concatenate a list of strings into a single string.
from functools import reduce

List=['h','e','l','l','o',' ','h','o','w',' ','a','r','e',' ','u','?']
x=reduce(lambda s,s1 : (s+s1),List)
print(x)