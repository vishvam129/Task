# Write a program that:

# Takes a sentence as input.

sentence=input("Enter Sen :- ")

# Converts the sentence to uppercase and lowercase.

print("Uppercase:- ",sentence.upper())
print("Lowercase:- ",sentence.lower())

# Removes all spaces and counts the total number of characters.
rm=sentence.replace(" ","")

print("Total Number of characters:- ",len(rm))