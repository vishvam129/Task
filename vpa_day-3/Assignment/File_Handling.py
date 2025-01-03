# Write a program to:
# Accept a list of names from the user and write them into a file.
# Read the file back and print the names in alphabetical order.

user_input=input("Enter the list of names with spaces (ex: john ellie manoj) :- ").split()

with open('names.txt','a') as file:
    for i in user_input:
        file.write(i)

with open('names.txt') as file:
    names=[]
    for i in file.readlines():
        names.append(i.strip())
    
print(sorted(names))

