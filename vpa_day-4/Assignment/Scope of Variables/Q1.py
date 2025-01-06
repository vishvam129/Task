# Define a global counter and modify it inside a function using the global keyword.

globel_var="Hello Globel var"
def change():
    global globel_var
    globel_var = "Hello Changed Globel var"
    print(globel_var)
change()
print(globel_var)