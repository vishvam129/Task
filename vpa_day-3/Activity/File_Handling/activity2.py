# Create a program to write user input into a file and read it back.

user_input=input("What do u want to Enter in the file :- ")
File_name=input("Do u want to give a file name or Press Enter to keep a Default (test1.txt) :- ") or "text1.txt"

with open(File_name , 'w') as file:
    file.write(user_input)
    
with open(File_name,"r") as file:
    text=file.read()
    
print("Did u Enter this (don't Lie ) :- ",text)
