# Write a program that asks for a user's full name and performs the following:

fullName=input("Enter your Fullname:- ")
name=fullName.split()


# Prints the initials.

print("initials :- ",name[0][0]+name[1][0])

# Reverses the name

print("Reversed Name :- ",name[0][::-1])

# Checks if the name is a palindrome

print(name[0]==name[0][::-1])



