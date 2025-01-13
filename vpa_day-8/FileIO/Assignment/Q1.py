# Write a program to:
# Accept a file path from the user and count the frequency of each word in the file.
# Write the word frequencies into a new text file.

file_path = input("Enter path of your file :- ")
words = {}
with open(file_path,'r+') as file:
    for i in file.readlines():
        for j in i.strip().split():
            if j in words:
                words[j] += 1
            else:
                words[j] = 1
with open("newfile.txt",'w+') as file:
    for i in words:
        file.write(f"{i} ---------------> {str(words[i])} \n")
print(words)  
# vpa_day-8/FileIO/Activities/test.txt