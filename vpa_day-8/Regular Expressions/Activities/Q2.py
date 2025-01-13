# Create a program to:
# Replace all occurrences of a word in a text file with another word.
# Find all dates in the format dd-mm-yyyy or yyyy-mm-dd in a given string.

# import re
# text = input("Enter Text :- ")
# word = input("Enter word with the new word u want to replace (ex:oldword newword) :- ").split()
# print("old text :- ",text)
# print("new text :- ",re.sub(word[0],word[1],text))
import re
# text_date = input("Enter text with dates formate like dd-mm-yyyy or yyyy-mm-dd :- ") or "hello 2024-23-12 hi 2025-01-23 hi 23-02-1234"
text_date = "hello 2024-23-12 hi 2025-01-23 hi 23-02-1234"
date = re.findall(r'\d{1,2}\-\d{1,2}\-\d{2,4}',text_date)
print(date)