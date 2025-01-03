# Write a program to read a file line by line and store non-empty lines in a list.

with open("test2.txt") as file:
    lines1=file.readlines()
    lines=list(line for line in (l.strip() for l in lines1) if line)
    print(lines)