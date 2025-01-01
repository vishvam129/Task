# Word Count Program:

# Write a program that:

# Accepts a multi-line string.

multi_line=input('''Enter Multi-line String :- ''')

# Splits it into words.

word=multi_line.split()

# Counts the frequency of each word.

d={}
for i in word:
   d[i]=0
for i in word:
    d[i]=d[i]+1
print(d) 