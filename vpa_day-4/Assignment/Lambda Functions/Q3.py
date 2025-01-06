# Use filter() to find all names in a list that end with "e".
List=["hello","hi",'aee','bee','cee']
x=filter(lambda x:x if x.endswith("e") else False ,List)
print(list(x))