# Use the nonlocal keyword in a nested function to maintain a counter in the outer function.
def outer():
    x='Local'
    
    def inner():
        nonlocal x
        x='non local'
        print(x)
    
    inner()
    print(x)
    
outer()