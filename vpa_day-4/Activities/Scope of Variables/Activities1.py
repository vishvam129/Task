# Write a program to illustrate how modifying a global variable inside a function affects its value.
gloable_var="hello this is the globle var value"
def Change():
    gloable_var="Hello this is changed globle var value"
    print(gloable_var)
    
print(gloable_var)
Change()