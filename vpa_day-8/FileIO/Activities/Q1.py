# Write a program to:
# Read a text file and count the number of lines, words, and characters in it.
# Handle cases where the file does not exist using exception handling.

def file_op(file):
    count_words = 0
    count_char = 0
    with open(file,'r+') as file_:
        for i in file_.read().strip():
            count_char += 1
        file_.seek(0)
        for i in file_.readlines():
            for j in i.strip().split():
                count_words += 1
        file_.seek(0)
        print(len(file_.readlines()))    
    print(count_char)
    print(count_words)
file_op('test.txt')
        