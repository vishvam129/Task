# Use filter() and a lambda function to extract words longer than 4 characters from 
# a list of strings.
List=["hello","hi","why","greet"]
x=filter(lambda s: len(s)>4, List)
print(list(x))
