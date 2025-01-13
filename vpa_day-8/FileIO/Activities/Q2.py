# Create a program to:
# Write a list of numbers to a text file.
# Read the file back and calculate their sum.

def num(file):
    numbers = input("Enter Numbers with spaces (ex: 10 20 39) :- ").split()
    sum_numbers = 0
    
    with open(file,'w+') as file:
        for i in numbers:
            file.write(f"{i} ")
        file.seek(0)
        print("The Entered num is :- ")
        for i in file.readline().split():
            print(i,end=" ")
            sum_numbers += int(i)
    print("\n Sum of all numbers is :- ",sum_numbers)
            
num("abc.txt")
            