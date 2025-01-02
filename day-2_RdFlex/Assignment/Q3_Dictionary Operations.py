# Write a program to:
# Count occurrences of each character in a given string using a dictionary.
# Delete a specific key from the dictionary and handle the case where the key does not exist.

String='hello how are u are u fine and why are u'

d = dict()

for i in String:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
        
print(d)


input_key = input("Enter the key u want to delete :- ")

try:
    d.pop(input_key)
except KeyError:
    print("The Key is not exist")
else:
    print("Key deleted successfully")
    
print(d)