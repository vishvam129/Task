# Character Frequency Counter:

# Counts the frequency of each character (ignoring case) in a string.

String=input("Enter String :- ")
d={}

for i in String.lower():
    d[i]=0
for i in String.lower():
    d[i]=d[i]+1
print(d)    