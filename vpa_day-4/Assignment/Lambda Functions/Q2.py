# Use map() with a lambda function to convert a list of integers into their string representations.
List=range(21)
x=map(lambda x:str(x) ,List)
print(list(x))