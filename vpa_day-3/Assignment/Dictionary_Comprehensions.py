# Write a program to:
# Create a dictionary from a list of words where keys are words and values are their lengths.
# Filter a dictionary to keep only items where the value is greater than 5.


# Create a dictionary from a list of words where keys are words and values are their lengths.

List=['one','two','three','four','five','six','seven','eight','nine','ten']
Dict={list:len(list) for list in List}
print(Dict)


# Filter a dictionary to keep only items where the value is greater than 5.

d={"1":5,"2":7,"3":4,"4":7}
result={k:v for (k,v) in d.items() if v>5}
print(result)