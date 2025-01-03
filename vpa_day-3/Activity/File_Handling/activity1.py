# Write a program to read a text file and count the frequency of each word.

with open('test.txt','r') as file:
    text=file.read().strip().split()
    d={}
    for i in text:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
            
print(d)
