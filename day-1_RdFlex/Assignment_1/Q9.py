# Text Statistics

# Total number of words in a paragraph.

p='''hello how are you 
hello why are you'''

words=p.split()
print("Total number of words in a paragraph:- ",len(words))

sentences=p.split("\n")
print(len(sentences))

# Average word length.

char=0
for i in words:
    for j in i:
        char=char+1
print("Avg word length :- ",char//len(words))