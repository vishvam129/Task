# Create a file reader that catches FileNotFoundError and prompts the user for a new file path.

try:
    file_path=input("Enter path of a file (file/test.txt) :- ")
    with open(file_path) as file:
        print(file.read())
except FileNotFoundError as e:
    print("the path is wrong re Enter it. ")
    if e:
        file_path=input("Enter path of a file (file/test.txt) :- ")
    with open(file_path) as file:
        print(file.read())
else:
    print("This is a else part ")


        
